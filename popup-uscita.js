/* [CLAUDE] 2026-10-17 popup di uscita delle pagine di iscrizione al workshop (ordine di Davide:
   «quando uno sta per uscire dalle landing fai comparire un popup con i campi per la registrazione»).
   - Il modulo NON e' una copia: e' lo stesso <form id="leadForm"> della pagina, spostato nel popup quando si apre
     e rimesso al suo posto quando si chiude. Stessi campi, stesso invio a Kajabi, stessi utm, stessa conferma,
     stessa pagina grazie con il Lead del pixel.
   - Quando compare: computer = il mouse esce dalla finestra verso l'alto (dopo 3 secondi sulla pagina);
     telefono = dopo almeno 15 secondi, uno scorrimento rapido verso l'alto oppure il tasto indietro.
   - Una volta sola per visitatore (localStorage dc_popup_uscita_visto). Mai a chi si e' gia' iscritto
     (dc_iscrizione_email) o mentre sta gia' compilando il modulo.
   - Eventi al modulo Google della scheda GRAZIE (stesso meccanismo di landing_visita): popup_aperto, popup_iscrizione.
     I campi Kajabi non si toccano.
   - Prove: ?popup=1 lo apre dopo 1 secondo senza segnarlo come visto. */
(function () {
  'use strict';
  var KEY = 'dc_popup_uscita_visto';
  var MODULO = 'https://docs.google.com/forms/d/e/1FAIpQLScIE7ZE1P1eKVEilQk_lTO4Nx5CY_VgljBQIn9LNftH2DkRKw/formResponse';
  var CAMPI = {visitatore: 'entry.491521358', email: 'entry.1233226114', variante: 'entry.1781041701',
               evento: 'entry.2099289393', dettaglio: 'entry.1395317553'};
  var me = document.currentScript;
  var tema = {
    bg: (me && me.getAttribute('data-bg')) || '#ffffff',
    fg: (me && me.getAttribute('data-fg')) || '#17263c',
    muted: (me && me.getAttribute('data-muted')) || '#526176',
    accent: (me && me.getAttribute('data-accent')) || '#2254c5'
  };
  function leggi(k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } }
  function scrivi(k, v) { try { window.localStorage.setItem(k, v); } catch (e) {} }
  var q = null; try { q = new URLSearchParams(location.search); } catch (e) {}
  var forza = !!(q && q.get('popup') === '1');
  var form = document.getElementById('leadForm');
  if (!form) return;
  if (!forza && (leggi(KEY) || leggi('dc_iscrizione_email'))) return;

  function evento(nome, dett) {
    try {
      var L = window.DCLanding || {};
      if (navigator.webdriver && !L.prova) return;
      var d = new URLSearchParams();
      d.append(CAMPI.visitatore, L.visitatore || leggi('dc_landing_visitatore') || '');
      d.append(CAMPI.email, '');
      d.append(CAMPI.variante, 'landing-' + (L.variante || '?'));
      d.append(CAMPI.evento, nome);
      d.append(CAMPI.dettaglio, (dett || '') + (L.prova ? ' · prova' : ''));
      if (navigator.sendBeacon && navigator.sendBeacon(MODULO, d)) return;
      fetch(MODULO, {method: 'POST', mode: 'no-cors', body: d, keepalive: true});
    } catch (e) {}
  }

  var css = document.createElement('style');
  css.textContent =
    '.dcpu{position:fixed;inset:0;z-index:2147483000;display:none;align-items:center;justify-content:center;padding:16px;background:rgba(10,14,22,.62)}' +
    '.dcpu.open{display:flex}' +
    '.dcpu-box{position:relative;width:100%;max-width:440px;max-height:calc(100vh - 32px);overflow:auto;border-radius:16px;padding:30px 24px 22px;box-shadow:0 30px 80px rgba(0,0,0,.4);background:' + tema.bg + ';color:' + tema.fg + '}' +
    '.dcpu-box h2{font-size:24px;line-height:1.2;margin:0 34px 8px 0;font-weight:800}' +
    '.dcpu-box .dcpu-sub{font-size:15px;line-height:1.5;margin:0 0 18px;color:' + tema.muted + '}' +
    '.dcpu-x{position:absolute;top:10px;right:10px;width:40px;height:40px;border:0;border-radius:50%;background:transparent;color:' + tema.fg + ';font-size:26px;line-height:1;cursor:pointer}' +
    '.dcpu-x:focus-visible{outline:3px solid ' + tema.accent + '}' +
    '.dcpu-box #leadForm{gap:11px!important}' +
    '@media (max-width:480px){.dcpu{align-items:flex-end;padding:0}.dcpu-box{border-radius:16px 16px 0 0;max-height:92vh}}';
  document.head.appendChild(css);

  var wrap = document.createElement('div');
  wrap.className = 'dcpu';
  wrap.setAttribute('role', 'dialog');
  wrap.setAttribute('aria-modal', 'true');
  wrap.setAttribute('aria-labelledby', 'dcpuTitolo');
  wrap.innerHTML = '<div class="dcpu-box"><button type="button" class="dcpu-x" aria-label="Chiudi">&times;</button>' +
    '<h2 id="dcpuTitolo">Prima di andare: il tuo posto è gratis</h2>' +
    '<p class="dcpu-sub">Giovedì 29 ottobre alle 21:00, su Zoom: ti mostro dal vivo tutto Commercialista AI al lavoro. Ti servono 30 secondi. <b>Davide Caiazzo</b></p>' +
    '<div class="dcpu-slot"></div></div>';
  document.body.appendChild(wrap);
  var slot = wrap.querySelector('.dcpu-slot');
  var segnaposto = document.createComment('posto del modulo');
  var aperto = false, lastFocus = null, inizio = Date.now();

  function apri(motivo) {
    if (aperto) return;
    var modale = document.getElementById('confirmModal');
    if (modale && modale.classList.contains('open')) return;
    aperto = true; mostrato = true;
    if (!forza) scrivi(KEY, String(Date.now()));
    lastFocus = document.activeElement;
    form.parentNode.insertBefore(segnaposto, form);
    slot.appendChild(form);
    wrap.classList.add('open');
    document.body.style.overflow = 'hidden';
    var primo = document.getElementById('fieldName');
    setTimeout(function () { try { primo.focus(); } catch (e) {} }, 30);
    evento('popup_aperto', motivo);
    stacca();
  }
  function chiudi() {
    if (!aperto) return;
    aperto = false;
    wrap.classList.remove('open');
    document.body.style.overflow = '';
    if (segnaposto.parentNode) { segnaposto.parentNode.insertBefore(form, segnaposto); segnaposto.parentNode.removeChild(segnaposto); }
    try { if (lastFocus && lastFocus.focus) lastFocus.focus(); } catch (e) {}
  }
  wrap.querySelector('.dcpu-x').addEventListener('click', chiudi);
  wrap.addEventListener('click', function (e) { if (e.target === wrap) chiudi(); });
  document.addEventListener('keydown', function (e) {
    if (!aperto) return;
    if (e.key === 'Escape') { chiudi(); return; }
    if (e.key === 'Tab') {
      var f = wrap.querySelectorAll('button,input,a[href]'); f = Array.prototype.filter.call(f, function (x) { return !x.disabled && x.offsetParent !== null; });
      if (!f.length) return;
      var a = f[0], z = f[f.length - 1];
      if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
      else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
    }
  });

  // Iscrizione andata a buon fine dal popup: evento in piu' e popup chiuso (la conferma della pagina resta quella di sempre).
  var L = window.DCLanding;
  if (L && typeof L.iscrizione === 'function') {
    var orig = L.iscrizione;
    L.iscrizione = function () {
      if (aperto) { evento('popup_iscrizione', ''); wrap.classList.remove('open'); }
      return orig.apply(this, arguments);
    };
  }

  // Non disturbare chi sta gia' compilando il modulo nella pagina.
  var staCompilando = false;
  form.addEventListener('focusin', function () { if (!aperto) staCompilando = true; });

  var telefono = false;
  try { telefono = window.matchMedia('(hover: none), (pointer: coarse)').matches; } catch (e) {}
  function pronto(ms) { return Date.now() - inizio >= ms && !staCompilando; }

  function suMouseOut(e) {
    if (e.relatedTarget || e.toElement) return;
    if (e.clientY > 0) return;
    if (pronto(3000)) apri('uscita-mouse');
  }
  // Scorrimento rapido verso l'alto: almeno 250 px saliti in meno di mezzo secondo (anche con lo scorrimento morbido).
  var lastY = window.scrollY, ancY = window.scrollY, ancT = Date.now();
  function suScroll() {
    var y = window.scrollY, t = Date.now();
    if (y >= lastY || t - ancT > 500) { ancY = Math.max(y, lastY); ancT = t; }
    lastY = y;
    if (ancY - y > 250 && t - ancT < 500 && y > 300 && pronto(15000)) apri('scorrimento-su');
  }
  var trappola = false, mostrato = false;
  function suIndietro() {
    if (!trappola) return;
    trappola = false;
    if (!mostrato) apri('tasto-indietro'); else { try { history.back(); } catch (e) {} }
  }
  function armaIndietro() {
    if (trappola || aperto) return;
    try { history.pushState({dcpu: 1}, '', location.href); trappola = true; } catch (e) {}
  }
  function stacca() {
    document.removeEventListener('mouseout', suMouseOut);
    window.removeEventListener('scroll', suScroll);
  }
  if (forza) { setTimeout(function () { apri('prova'); }, 1000); return; }
  if (telefono) {
    window.addEventListener('scroll', suScroll, {passive: true});
    setTimeout(armaIndietro, 15000);
    window.addEventListener('popstate', suIndietro);
  } else {
    document.addEventListener('mouseout', suMouseOut);
  }
}());
