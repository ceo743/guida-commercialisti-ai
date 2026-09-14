/* First-party experiment. No enrollment/storage before analytics consent. */
(function () {
  'use strict';
  var API='https://commercialista-ai.davidecaiazzo.it/workshop-test';
  var KEY='dc_workshop_video_20260914';
  var END=Date.parse('2026-09-30T16:30:00Z');
  var section=document.getElementById('dimostrazione');
  var qa=new URLSearchParams(location.search).get('wkqa')==='1';
  var busy=false, exposedBeforeAssignment=false, stopped=false;
  var state=null, exposure=Promise.resolve();
  function consent(){
    try {return window.CookieScript.instance.currentState().categories.indexOf('performance')!==-1;}
    catch(e){return false;}
  }
  function request(path,body){
    return fetch(API+path,{method:'POST',credentials:'omit',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
      .then(function(r){return r.json().then(function(d){if(!r.ok)throw new Error(d.motivo||'Misurazione non disponibile');return d;});});
  }
  function visible(){return section.getBoundingClientRect().top<innerHeight && section.getBoundingClientRect().bottom>0;}
  function markSeen(){if(!state&&!busy&&visible())exposedBeforeAssignment=true;}
  addEventListener('scroll',markSeen,{passive:true});
  function stop(){
    state=null;stopped=true;section.hidden=false;
    try{localStorage.removeItem(KEY);}catch(e){}
    document.documentElement.removeAttribute('data-workshop-variant');
  }
  window.DCWorkshopExperiment={
    current:function(){return state;},
    submit:function(fields){
      if(!state||!consent()||Date.now()>=END)return null;
      var assigned=state;
      return exposure.then(function(){return request('/submit',{token:assigned.token,campi:fields,qa_result:qa?'accepted':undefined});});
    }
  };
  function enroll(){
    if(!section||busy||state||stopped||Date.now()>=END||!consent())return;
    if((navigator.webdriver&&!qa)||exposedBeforeAssignment||visible())return;
    var saved;
    try{
      saved=JSON.parse(localStorage.getItem(KEY)||'null');
      if(!saved||saved.qa!==qa||saved.end!==END){
        var bytes=new Uint8Array(16);crypto.getRandomValues(bytes);
        saved={id:Array.from(bytes,function(x){return x.toString(16).padStart(2,'0');}).join(''),qa:qa,end:END};
        localStorage.setItem(KEY,JSON.stringify(saved));
      }
    }catch(e){return;}
    busy=true;
    request('/assign',{visitor_id:saved.id,consent:true,qa:qa}).then(function(d){
      if(!consent()||visible()||stopped){busy=false;return;}
      section.hidden=d.variant==='A';
      document.documentElement.setAttribute('data-workshop-variant',d.variant);
      // Enrollment is counted only after the assigned page version was applied.
      state=d;
      exposure=request('/expose',{token:d.token}).catch(function(){return request('/expose',{token:d.token});});
      return exposure;
    }).catch(function(){state=null;section.hidden=false;document.documentElement.removeAttribute('data-workshop-variant');})
      .finally(function(){busy=false;});
  }
  addEventListener('CookieScriptCategory-performance',enroll);
  addEventListener('CookieScriptAcceptAll',enroll);
  addEventListener('CookieScriptAccept',function(){if(consent())enroll();else stop();});
  addEventListener('CookieScriptReject',stop);
  addEventListener('CookieScriptRejectAll',stop);
  enroll();
  var attempts=0,timer=setInterval(function(){enroll();if(++attempts>=20||state||stopped)clearInterval(timer);},500);
}());
