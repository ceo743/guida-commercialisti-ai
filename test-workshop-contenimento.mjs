import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';

const html=readFileSync(new URL('./index.html',import.meta.url),'utf8');
const script=html.match(/function dcPhoneOk[\s\S]*?\n<\/script>/)?.[0].replace(/\n<\/script>$/,'');
assert.ok(script);
assert.match(html,/fbq\('track','PageView'\)/);
assert.doesNotMatch(html,/fbq\('track','Lead'\)/);
assert.doesNotMatch(script,/DCLanding\.iscrizione\(/);

function harness(server, session=new Map(), options={}){
  let now=0,nextTimer=1,modal=0,abRegistrations=0;
  const timers=new Map(),calls=[],els=new Map();
  function el(id){
    if(!els.has(id))els.set(id,{value:'',checked:false,disabled:false,textContent:'',innerHTML:'',
      style:{display:'none'},classList:{add(kind){if(id==='confirmModal'&&kind==='open')modal++;},remove(){}},scrollIntoView(){}});
    return els.get(id);
  }
  if(!options.emptyFields){
    el('fieldName').value='Mario Rossi';el('fieldEmail').value='ceo@example.test';
    el('fieldPhone').value='3331234567';el('fieldPrivacy').checked=true;
  }
  for(const id of ['utm_source','utm_medium','utm_campaign','utm_content'])el(id).value='prova';
  const storage={getItem:k=>session.get(k)||null,setItem:(k,v)=>session.set(k,String(v))};
  const document={cookie:'',getElementById:el};
  const window={DCLanding:{iscrizione(){abRegistrations++;}},DCWorkshopExperiment:{submit(){throw Error('expired experiment called');}},location:{href:''}};
  const context={window,document,sessionStorage:storage,localStorage:storage,URLSearchParams,AbortController,
    setTimeout(fn,delay){const id=nextTimer++;timers.set(id,{at:now+delay,fn});return id;},
    clearTimeout(id){timers.delete(id);},setInterval(){throw Error('automatic redirect');},clearInterval(){},
    fetch(url,options){calls.push({url,options});return server(url,options,calls);}};
  vm.createContext(context);vm.runInContext(script,context);
  async function flush(){for(let i=0;i<15;i++)await Promise.resolve();}
  async function tick(){const first=[...timers].sort((a,b)=>a[1].at-b[1].at)[0];assert.ok(first,'expected timer');timers.delete(first[0]);now=first[1].at;first[1].fn();await flush();}
  return {el,calls,session,window,submit(){context.submitForm({preventDefault(){}});},flush,tick,
    get modal(){return modal;},get abRegistrations(){return abRegistrations;},get now(){return now;}};
}
const response=(body,status=200)=>Promise.resolve({ok:status>=200&&status<300,json:()=>Promise.resolve(body)});
const posts=h=>h.calls.filter(x=>x.options?.method==='POST');
function noFalseConfirmation(h,expectedEmail='ceo@example.test'){
  assert.equal(h.modal,0);assert.equal(h.abRegistrations,0);assert.equal(h.window.location.href,'');
  assert.equal(h.el('submitBtn').disabled,true);
  assert.equal(h.el('btnText').textContent,'INVIO DA VERIFICARE');
  assert.match(h.el('formErrore').innerHTML,/Guarda il video/);
  assert.equal(h.el('fieldEmail').value,expectedEmail);
}

const bridge=harness((url)=>url.endsWith('/health')?response({status:'ok'}):response({ok:true,stato_kajabi:302}));
bridge.submit();await bridge.flush();
assert.equal(posts(bridge).length,1);assert.equal(posts(bridge)[0].url,'https://dc-chatbot-vswb.onrender.com/lead-kajabi');
assert.match(bridge.el('formErrore').innerHTML,/Richiesta inviata\. Controlla l’email di conferma; da qui non possiamo verificare l’iscrizione\./);
assert.equal(bridge.session.get('dc_workshop_invio_2149685500_20261015'),'inviata','marker is scoped to form and edition');
noFalseConfirmation(bridge);
bridge.submit();await bridge.flush();assert.equal(posts(bridge).length,1,'same tab cannot repost');
const refreshed=harness(()=>{throw Error('refresh must not fetch');},bridge.session,{emptyFields:true});
noFalseConfirmation(refreshed,'');
assert.doesNotMatch(refreshed.el('formErrore').innerHTML,/dati restano|dati.*compilat/i,'reload does not promise missing draft fields');
refreshed.submit();await refreshed.flush();assert.equal(posts(refreshed).length,0);

const oldEdition=new Map([['dc_workshop_invio_da_verificare','incerta'],['dc_workshop_invio_2149685500_20260930','incerta']]);
const newEdition=harness((url)=>url.endsWith('/health')?response({status:'ok'}):response({ok:true}),oldEdition);
newEdition.submit();await newEdition.flush();
assert.equal(posts(newEdition).length,1,'old edition marker cannot block this edition');

const opaque=harness((url)=>url.endsWith('/health')?Promise.reject(Error('bridge asleep')):Promise.resolve({type:'opaque',ok:false}));
opaque.submit();await opaque.flush();
assert.equal(posts(opaque).length,1,'bridge failure selects one direct POST');
assert.equal(posts(opaque)[0].options.mode,'no-cors');
assert.match(opaque.el('formErrore').innerHTML,/Richiesta inviata\. Controlla l’email di conferma/);
noFalseConfirmation(opaque);

const timeout=harness((url)=>url.endsWith('/health')?response({status:'ok'}):new Promise(()=>{}));
timeout.submit();await timeout.flush();await timeout.tick();
assert.equal(timeout.now,25000);assert.equal(posts(timeout).length,1,'POST timeout never starts a direct fallback');
assert.equal(posts(timeout)[0].options.signal.aborted,true);
assert.match(timeout.el('formErrore').innerHTML,/L’invio non è verificato\. Non lo ripetiamo/);
noFalseConfirmation(timeout);
timeout.submit();await timeout.flush();assert.equal(posts(timeout).length,1,'uncertain POST cannot be repeated');

const healthTimeout=harness((url)=>url.endsWith('/health')?new Promise(()=>{}):Promise.resolve({type:'opaque',ok:false}));
healthTimeout.submit();await healthTimeout.flush();await healthTimeout.tick();await healthTimeout.flush();
assert.equal(healthTimeout.now,4000);assert.equal(posts(healthTimeout).length,1,'health timeout selects one direct POST');
assert.equal(posts(healthTimeout)[0].options.mode,'no-cors');
noFalseConfirmation(healthTimeout);

console.log('Workshop containment tests passed');
