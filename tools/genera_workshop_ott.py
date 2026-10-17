# [CLAUDE] 17/10/2026 sera: varianti B, C, D riscritte su ordine di Davide («noi facciamo TUTTO, qui dici F24 e basta»).
# Ogni pagina presenta tutto il programma (sezione «Tutto quello che fa per lo studio», 13 funzioni attive con schermate vere);
# cambiano solo il gancio del primo schermo e la grafica. Modulo e tracciamento copiati identici da workshop.html (base: build v1).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'build_v1.py')).read()
src = src[:src.index("for v, fn in (('b', B), ('c', C), ('d', D)):")]
exec(src)

FUNZ = [
 ("email", "Email dei clienti", "Prepara le risposte ai clienti",
  "Il cliente scrive una domanda o manda un documento: l'AI prepara la risposta nel tono dello studio. Tu la leggi, la correggi se serve e la mandi."),
 ("scadenze", "Scadenze e avvisi bonari", "Mette in calendario le scadenze dei clienti",
  "Un avviso bonario, una cartella, una scadenza in un PDF: l'AI le trova nelle email e nei documenti, calcola la data con la sospensione feriale, ti manda due promemoria e prepara l'F24. Tu confermi."),
 ("invia-f24", "Invia F24", "Manda gli F24 ai clienti e sollecita chi non risponde",
  "Carichi gli F24 fatti con il gestionale: l'AI capisce di quale cliente è ognuno, prepara l'email e sollecita chi non risponde. Promemoria due giorni prima, F24 scaduti fermati. Tu controlli e premi Invia."),
 ("controllo-incrociato", "Confronto", "Trova le differenze tra estratto conto e movimenti",
  "Carichi l'estratto della banca e la lista movimenti del gestionale: l'AI ti mostra cosa c'è solo da una parte e le date diverse. Confronta anche le fatture dell'Agenzia con il registro. Tu guardi solo le differenze."),
 ("clienti", "Clienti e Archivio", "Tiene in ordine clienti e documenti",
  "Una scheda per ogni cliente. L'AI trova le email dei clienti e mette i documenti che arrivano nella scheda giusta; quelli dubbi te li segna."),
 ("fatture-estere", "Fatture estere", "Dal PDF del fornitore estero all'XML",
  "Legge importi, date e partita IVA anche da una scansione e prepara l'XML da importare nel gestionale. Le autofatture in inversione contabile, pronte da scaricare."),
 ("estratti-fatture", "Estratti e fatture", "Abbina pagamenti e fatture",
  "Banca, carta o PayPal: l'AI abbina i movimenti alle fatture e ti segnala solo i pagamenti senza fattura e quelli da controllare."),
 ("", "Genera F24", "Prepara l'F24 delle ritenute",
  "Carichi la parcella o la fattura in PDF: l'AI trova la ritenuta e prepara l'F24 con la scadenza giusta. Tu confermi solo la data del pagamento."),
 ("redditi", "730 e Redditi", "Chiede i documenti della dichiarazione",
  "Scegli i clienti e il giorno: a ognuno parte l'elenco dei documenti da mandare, anche in foto, e un promemoria a chi non li manda."),
 ("", "Circolari", "Le novità fiscali ai clienti giusti",
  "Quando esce una novità importante l'AI prepara la circolare con la fonte ufficiale. Tu scegli a quali clienti mandarla."),
 ("fatturazione", "Fatturazione dello studio", "Manda le parcelle ai clienti",
  "Scritti gli onorari, la parcella parte a ogni cliente nel giorno che scegli, con i promemoria a chi non ha pagato e la fattura elettronica pronta."),
 ("", "Email inviate", "Ogni invio con il suo esito",
  "Per ogni email vedi se è stata accettata e se il cliente ha confermato di averla ricevuta. Senza telefonare a nessuno."),
 ("", "Colleghi", "Uno spazio con altri commercialisti",
  "Confronti dubbi e soluzioni con gli altri studi che usano il programma."),
]
TUTTO_CSS = '''
.tutto{display:grid;grid-template-columns:300px 1fr;gap:26px;align-items:start}
.tt-list{display:flex;flex-direction:column;gap:6px}
.tt-b{all:unset;box-sizing:border-box;cursor:pointer;display:block;width:100%;padding:11px 14px;border-radius:10px;font-weight:600;font-size:15.5px;line-height:1.3}
.tt-b small{display:block;font-weight:400;font-size:13px;opacity:.75;margin-top:2px}
.tt-b:focus-visible{outline:3px solid currentColor;outline-offset:2px}
.tt-p figure{margin:0}
.tt-p .ph{border-radius:12px;overflow:hidden}
.tt-p .ph img{width:100%;height:auto}
.tt-p .noimg{display:flex;align-items:center;justify-content:center;min-height:200px;border-radius:12px;font-size:15px;text-align:center;padding:24px}
.tt-p h3{font-size:22px;margin:18px 0 6px}
.tt-p p{font-size:16px;line-height:1.6}
.tt-safe{margin-top:22px;font-size:15px;line-height:1.55}
.tt-p [hidden]{display:none!important}
@media (max-width:900px){.tutto{grid-template-columns:1fr}.tt-list{display:grid;grid-template-columns:1fr 1fr;gap:6px}.tt-b{padding:9px 10px;font-size:14px}.tt-b small{display:none}}
'''
def tutto(prefix):
    btns = []
    for i, (img, nome, cosa, testo) in enumerate(FUNZ):
        btns.append(f'<button type="button" class="tt-b" role="tab" aria-selected="{"true" if i==0 else "false"}" data-i="{i}">{nome}<small>{cosa}</small></button>')
    data = [{"img": ("img-ott/%s.webp" % f[0]) if f[0] else "", "imgt": ("img-ott/%s-telefono.webp" % f[0]) if f[0] else "", "nome": f[1], "cosa": f[2], "testo": f[3]} for f in FUNZ]
    import json
    first = FUNZ[0]
    return f'''<div class="tutto" id="{prefix}tutto">
<div class="tt-list" role="tablist" aria-label="Le funzioni del programma">{''.join(btns)}</div>
<div class="tt-p" role="tabpanel" aria-live="polite">
<figure class="ph"><picture><source media="(max-width:700px)" srcset="img-ott/{first[0]}-telefono.webp"/><img src="img-ott/{first[0]}.webp" width="1440" height="860" alt="{first[1]} in Commercialista AI, studio dimostrativo"/></picture></figure>
<div class="noimg" hidden></div>
<h3>{first[1]}: {first[2][0].lower()+first[2][1:]}</h3><p>{first[3]}</p>
</div></div>
<p class="tt-safe"><b>Il gestionale resta il tuo:</b> il programma legge i PDF che ti fa scaricare. Tu carichi, controlli e premi Invia. Niente parte senza il tuo sì: anche i solleciti automatici li accendi tu. Non tiene la contabilità e non sostituisce il gestionale: lavora accanto al tuo. Schermate dello studio di esempio, con clienti e dati finti.</p>
<script>
(function(){{
 var D={json.dumps(data, ensure_ascii=False)};
 var box=document.getElementById('{prefix}tutto'); if(!box) return;
 var bs=box.querySelectorAll('.tt-b'), fig=box.querySelector('.ph'), no=box.querySelector('.noimg'), h=box.querySelector('.tt-p h3'), p=box.querySelector('.tt-p p');
 function show(i){{
  var d=D[i];
  bs.forEach(function(b,k){{b.setAttribute('aria-selected',k===i?'true':'false');}});
  if(d.img){{fig.hidden=false;no.hidden=true;fig.querySelector('source').srcset=d.imgt;var im=fig.querySelector('img');im.src=d.img;im.alt=d.nome+' in Commercialista AI, studio dimostrativo';}}
  else{{fig.hidden=true;no.hidden=false;no.textContent=d.nome+': lo vedi dal vivo giovedì.';}}
  h.textContent=d.nome+': '+d.cosa.charAt(0).toLowerCase()+d.cosa.slice(1);p.textContent=d.testo;
 }}
 var cur=0,auto=null;
 try{{if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){{auto=setInterval(function(){{cur=(cur+1)%D.length;show(cur);}},4500);}}}}catch(e){{}}
 function stop(){{if(auto){{clearInterval(auto);auto=null;}}}}
 box.addEventListener('pointerenter',stop);box.addEventListener('focusin',stop);
 bs.forEach(function(b,k){{b.addEventListener('click',function(){{stop();cur=k;show(k);}});}});
}})();
</script>'''

AGENDA = [
 ("La giornata di uno studio, sul programma vero", "Apro Commercialista AI su uno studio di esempio e facciamo il giro intero: la posta già letta con le risposte ai clienti pronte, le scadenze e gli avvisi bonari trovati, gli F24 mandati e chi li ha ricevuti, i documenti del 730 chiesti ai clienti che scegli, le circolari, le parcelle, ogni invio con il suo esito."),
 ("Fatture estere, estratti e confronti", "La fattura del fornitore estero che diventa XML, gli estratti conto abbinati alle fatture, le differenze tra estratto conto e movimenti del gestionale."),
 ("Le tue 3 attività, guardate in diretta", "Porta le 3 cose che ripeti ogni settimana e che vorresti non fare più. Ti dico quali il programma fa già e cosa serve per partire."),
 ("Le tue domande", "Rispondo io, sul tuo studio. Alla fine ti dico quanto costa e come si attiva. Nessun obbligo."),
]
def agenda(item_tpl):
    return '\n'.join(item_tpl.format(n=i+1, t=t, d=d) for i, (t, d) in enumerate(AGENDA))

BIO = ("Ho costruito My Governance, un software per le aziende, e l'ho venduta al gruppo Zucchetti: «valutazione oltre 10 milioni», ha titolato Il Sole 24 Ore. "
       "Sono TOP 20 al mondo in “LinkedIn® Growth” secondo Favikon 2025. Commercialista AI l'ho costruito e provato insieme a due studi commercialisti.")
SQUADRA = "In squadra con me Gianfranco Motta, il tecnico di DC Academy: tiene d'occhio la chat e mi porta le domande più tecniche."

# ---------------- B ----------------
B2_CSS = B_CSS + TUTTO_CSS + '''
.stack{position:relative;min-height:440px}
.stack figure{position:absolute;width:82%;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 24px 50px rgb(23 38 60/14%);overflow:hidden}
.stack figure:nth-child(1){top:0;left:0;z-index:1}
.stack figure:nth-child(2){top:90px;left:9%;z-index:2}
.stack figure:nth-child(3){top:180px;left:18%;z-index:3}
.stack figcaption{font-size:12.5px;color:var(--grey);padding:7px 12px;border-top:1px solid var(--line);font-weight:600}
.tt-b{color:var(--ink);background:#fff;border:1px solid var(--line)}
.tt-b[aria-selected="true"]{background:var(--blue);color:#fff;border-color:var(--blue)}
.tt-p .ph{border:1px solid var(--line);box-shadow:0 20px 50px rgb(23 38 60/12%)}
.tt-p .noimg{background:var(--tint);color:var(--blue2);border:1px dashed #b9c9ea}
.tt-p h3{font-family:'Source Serif 4',Georgia,serif;font-weight:600}
.tt-p p,.tt-safe{color:var(--grey)}
.how{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.how div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px}
.how b{display:block;font-size:18px;margin-bottom:6px;color:var(--ink)}
.how p{color:var(--grey);font-size:15.5px}
@media (max-width:900px){.stack{min-height:0}.stack figure{position:static;width:100%}.stack figure:nth-child(n+2){display:none}.how{grid-template-columns:1fr}}
'''
def B():
    body = f'''<header class="top"><div class="wrap"><div class="logo">Commercialista<span>AI</span> · dal vivo</div><a class="mini" href="#iscrizione">Riserva il posto</a></div></header>
<main>
<section class="hero"><div class="wrap">
<div>
<p class="when"><i aria-hidden="true"></i>Workshop gratuito su Zoom · giovedì 29 ottobre, ore 21:00</p>
<h1>Il lavoro di una segreteria intera, preparato dall'intelligenza artificiale. <em>Tu controlli e fai il consulente.</em></h1>
<p class="lead">Risposte ai clienti, scadenze e avvisi bonari letti dalle email, F24 mandati con i solleciti, documenti del 730, fatture estere in XML, estratti conto abbinati, circolari, parcelle, archivio. Giovedì 29 ottobre apro Commercialista AI e ti faccio vedere tutto, dal vivo.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="52" height="52"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
<div class="proof"><span>Il gestionale resta il tuo</span><span>Tu controlli e premi Invia</span><span>182 iscritti all'edizione del 15 ottobre</span></div>
</div>
<div class="stack">
<figure><img src="img-ott/invia-f24.webp" width="1440" height="860" alt="Invia F24 in Commercialista AI"/><figcaption>Invia F24</figcaption></figure>
<figure><img src="img-ott/scadenze.webp" width="1440" height="860" alt="Scadenze in Commercialista AI"/><figcaption>Scadenze e avvisi bonari</figcaption></figure>
<figure><picture><source media="(max-width:700px)" srcset="img-ott/email-telefono.webp"/><img src="img-ott/email.webp" width="1440" height="860" alt="Email dei clienti in Commercialista AI"/></picture><figcaption>Risposte ai clienti già scritte</figcaption></figure>
</div>
</div></section>

<section><div class="wrap">
<h2 class="sec-h">Tutto quello che fa per lo studio</h2>
<p class="sec-p">Tredici funzioni, un solo programma accanto al tuo gestionale. Scegli una voce e guarda la schermata vera: l'AI prepara, tu controlli.</p>
{tutto('b')}
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2 class="sec-h">Meno segreteria, più consulenza.</h2>
<div class="how">
<div><b>L'AI prepara</b><p>Legge email, PDF ed estratti, riconosce il cliente giusto e prepara F24, risposte, scadenze, documenti e file.</p></div>
<div><b>Tu controlli</b><p>Vedi tutto in una pagina per ogni lavoro. Correggi se serve. Niente parte senza il tuo sì.</p></div>
<div><b>Lo studio respira</b><p>Le ore che oggi se ne vanno in segreteria tornano alla consulenza ai clienti.</p></div>
</div></div></section>

<div class="band"><div class="wrap"><h2>Giovedì 29 ottobre, ore 21:00. La diretta inizia tra</h2>{COUNTDOWN}<a class="cta" href="#iscrizione">Iscriviti gratis</a></div></div>

<section><div class="wrap">
<h2 class="sec-h">Cosa vedi dal vivo</h2>
<p class="sec-p">Clienti di prova, programma vero. Nessuna slide.</p>
<div class="agenda">{agenda('<div class="ag"><div class="n">{n}</div><div><h3>{t}</h3><p>{d}</p></div></div>')}</div>
</div></section>

<section><div class="wrap">
<div class="who"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="200" height="200" loading="lazy"/><div>
<h3>Conduco io, Davide Caiazzo</h3><p>{BIO}</p><div class="press">{STAMPA}</div><p class="team">{SQUADRA}</p>
</div></div></div></section>

<section><div class="wrap">
<h2 class="sec-h">Per chi è</h2>
<div class="fit"><div><h3>Fa per te se</h3><ul><li>✓ hai uno studio, da solo o associato, e le giornate se ne vanno in email, F24, documenti, scadenze e parcelle</li><li>✓ vorresti fare più consulenza ai clienti</li><li>✓ il gestionale ti va bene e non vuoi cambiarlo</li></ul></div>
<div><h3>Non fa per te se</h3><ul><li>✗ vuoi che il programma risponda ai clienti senza che tu legga</li><li>✗ cerchi un gestionale nuovo: questo lavora accanto al tuo</li></ul></div></div>
</div></section>

<section><div class="wrap"><h2 class="sec-h">Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2 class="sec-h">Giovedì 29 ottobre, ore 21:00. Su Zoom.</h2><p class="sec-p">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom con i promemoria.</p></div>
{form_block('', 'Riserva il tuo posto gratis', 'Giovedì 29 ottobre, ore 21:00 · Live su Zoom')}
</div></section>
</main>'''
    return page('B', "Workshop gratuito per commercialisti: il lavoro di una segreteria intera, fatto dall'intelligenza artificiale",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo Commercialista AI: F24, scadenze e avvisi bonari, risposte ai clienti, 730, fatture estere, estratti e confronti, circolari, parcelle.",
      'family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700', B2_CSS, body,
      "[CLAUDE] 2026-10-17 sera variante B v2 (prova ott A/B/C/D): stile Commercialista AI, gancio «una segreteria intera fatta dal programma», tutto il programma. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

# ---------------- C ----------------
GIORNATA = [
 ("8:30", "La posta", "Email dei clienti da leggere una a una, documenti da salvare, scadenze da segnare a mano.", "L'AI le ha già lette: ha trovato scadenze e avvisi bonari, messo i documenti nella scheda del cliente e scritto le risposte. Tu rileggi e premi Invia."),
 ("10:00", "Gli F24", "Mandati uno a uno, poi le telefonate per sapere chi li ha ricevuti.", "Pronti per tutti i clienti in una volta: controlli e premi Invia. Poi promemoria due giorni prima e sollecito a chi non risponde."),
 ("12:00", "I documenti del 730", "La lista dei documenti mandata e rimandata, cliente per cliente.", "Scegli i clienti e il giorno: a ognuno parte l'elenco, anche da mandare in foto, con il promemoria a chi non ha finito."),
 ("15:00", "Fatture e quadrature", "La fattura del fornitore estero da ribattere, l'estratto conto da confrontare riga per riga.", "XML pronto da importare, estratti e fatture abbinati, le differenze già trovate."),
 ("18:00", "Lo studio", "Circolari da scrivere, parcelle da preparare, file sparsi.", "Circolare con la fonte ufficiale mandata ai clienti giusti, parcelle partite, archivio in ordine. Alle 18 fai l'unica cosa che nessuna AI fa: la consulenza."),
]
C2_CSS = C_CSS + TUTTO_CSS + '''
.hero h1{font-size:clamp(34px,4.8vw,64px)}
.hero h1 q{quotes:"“" "”"}
.hero .lead{max-width:700px}
.hero .portrait{width:120px;height:120px;border-radius:50%;object-fit:cover;border:3px solid var(--brass);margin:0 auto 26px}
.day{border-top:1px solid var(--line)}
.dr{display:grid;grid-template-columns:110px 1fr 1fr;gap:26px;padding:24px 0;border-bottom:1px solid var(--line)}
.dr .t{font-family:'Fraunces',Georgia,serif;font-size:30px;color:var(--brass2);line-height:1}
.dr .t small{display:block;font-family:'Instrument Sans',sans-serif;font-size:14px;color:var(--paper);margin-top:8px}
.dr h4{font-size:12.5px;font-weight:700;color:var(--mute);margin-bottom:6px}
.dr .after h4{color:var(--brass2)}
.dr p{color:var(--mute);font-size:15.5px}
.dr .after p{color:var(--paper)}
.tt-b{color:var(--paper);border:1px solid var(--line)}
.tt-b[aria-selected="true"]{background:var(--brass);color:#14262a;border-color:var(--brass)}
.tt-p .ph{border:1px solid var(--line);box-shadow:0 30px 70px rgb(0 0 0/35%)}
.tt-p .noimg{background:var(--bg2);color:var(--brass2);border:1px dashed var(--line)}
.tt-p h3{font-family:'Fraunces',Georgia,serif;font-weight:500}
.tt-p p,.tt-safe{color:var(--mute)}.tt-safe b{color:var(--paper)}
.ag2{display:grid;grid-template-columns:repeat(2,1fr);gap:0 40px;border-top:1px solid var(--line)}
.ag2 div{padding:22px 0;border-bottom:1px solid var(--line)}
.ag2 h3{font-size:19px;margin-bottom:6px}.ag2 p{color:var(--mute);font-size:15.5px}
@media (max-width:900px){.dr{grid-template-columns:1fr;gap:10px}.ag2{grid-template-columns:1fr}}
'''
def C():
    giorn = '\n'.join(f'<div class="dr"><div class="t">{o}<small>{t}</small></div><div><h4>Prima</h4><p>{pr}</p></div><div class="after"><h4>Con Commercialista AI</h4><p>{do}</p></div></div>' for o, t, pr, do in GIORNATA)
    body = f'''<header class="top"><div class="wrap"><div class="mark">Davide Caiazzo <small>workshop per commercialisti</small></div><div class="datechip">Giovedì 29 ottobre, ore 21:00, su Zoom</div></div></header>
<main>
<section class="hero"><div class="wrap">
<img class="portrait" src="davide-linkedin.jpg" alt="Davide Caiazzo" width="120" height="120"/>
<p class="kick">Workshop gratuito dal vivo, solo per commercialisti · conduce Davide Caiazzo</p>
<p class="kick" style="font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:20px;color:var(--paper)">«Ho bisogno di un consulente, non di una segretaria», dicevo al mio commercialista.</p>
<h1>Non gli mancava la competenza. <span class="b">Gli mancava il tempo.</span></h1>
<p class="lead">Pensavo che non fosse bravo. Costruendo Commercialista AI ho capito che mi sbagliavo: <b>il suo tempo se lo mangiava la segreteria</b>, tra email, scadenze, F24, documenti, fatture, circolari e parcelle. Giovedì 29 ottobre alle 21 ti mostro la giornata dello studio con tutto quel lavoro fatto dall'intelligenza artificiale.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
</div></section>
<div class="strip"><div class="wrap"><span><b>182</b> iscritti all'edizione del 15 ottobre</span><span>Il gestionale <b>resta il tuo</b></span><span><b>Gratis</b>, su Zoom</span></div></div>

<section><div class="wrap">
<h2>La giornata dello studio, prima e dopo</h2>
<p class="sub">Clienti di prova, programma vero. Giovedì la vedi scorrere dal vivo.</p>
<div class="day">{giorn}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Tutto quello che fa per lo studio</h2>
<p class="sub">Tredici funzioni, un solo programma accanto al tuo gestionale. Scegli una voce e guarda la schermata vera: l'AI prepara, tu controlli.</p>
{tutto('c')}
</div></section>

<section style="padding-top:0"><div class="wrap story">
<img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="400" height="400" loading="lazy"/>
<div>
<p>Sono Davide Caiazzo. {BIO} Giovedì te lo mostro io, dal vivo.</p>
<div class="press">{STAMPA}</div>
<p style="margin-top:16px">{SQUADRA}</p>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<div class="ag2">{agenda('<div><h3>{t}</h3><p>{d}</p></div>')}</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:26px">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · solo per commercialisti')}
</div></section>
</main>'''
    return page('C', "Workshop gratuito per commercialisti: consulente, non segretaria. La giornata dello studio con l'intelligenza artificiale",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra la giornata di uno studio con Commercialista AI: F24, scadenze, email, 730, fatture estere, quadrature, circolari, parcelle.",
      'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,500&family=Instrument+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400', C2_CSS, body,
      "[CLAUDE] 2026-10-17 sera variante C v2 (prova ott A/B/C/D): notte petrolio e ottone, gancio storia di Davide «consulente, non segretaria» + giornata prima/dopo, tutto il programma. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

# ---------------- D ----------------
D2_CSS = D_CSS + TUTTO_CSS + '''
.big{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;margin-bottom:22px}
.big .n{font-family:'Bricolage Grotesque',sans-serif;font-weight:700;font-size:clamp(110px,14vw,190px);line-height:.8;letter-spacing:-.05em;color:var(--green)}

.chk{list-style:none;columns:2;column-gap:22px;background:var(--paper);border:2px solid var(--ink);border-radius:14px;box-shadow:8px 8px 0 var(--ink);padding:20px 22px}
.chk li{break-inside:avoid;padding:6px 0 6px 28px;position:relative;font-size:15px;border-bottom:1px dashed var(--line)}
.chk li::before{content:"✓";position:absolute;left:4px;top:5px;color:var(--green);font-weight:700}
.nums{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.num{background:var(--paper);border:2px solid var(--ink);border-radius:14px;padding:22px}
.num b{display:block;font-family:'Bricolage Grotesque',sans-serif;font-size:44px;line-height:1;margin-bottom:8px}
.num p{color:var(--mute);font-size:15px}
.never{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.never div{border-top:4px solid var(--ink);padding-top:14px}
.never h3{font-family:'Bricolage Grotesque',sans-serif;font-size:21px;margin-bottom:6px}
.never p{color:var(--mute);font-size:15.5px}
.tt-b{color:var(--ink);background:var(--paper);border:2px solid var(--ink)}
.tt-b[aria-selected="true"]{background:var(--hi)}
.tt-p .ph{border:2px solid var(--ink)}
.tt-p .noimg{background:var(--paper);border:2px dashed var(--ink)}
.tt-p h3{font-family:'Bricolage Grotesque',sans-serif}
.tt-p p,.tt-safe{color:var(--mute)}.tt-safe b{color:var(--ink)}
@media (max-width:900px){.big{grid-template-columns:1fr;gap:6px}.chk{columns:1;box-shadow:5px 5px 0 var(--ink)}.nums,.never{grid-template-columns:1fr}}
'''
def D():
    chk = ''.join(f'<li>{f[1]}</li>' for f in FUNZ)
    body = f'''<header class="top"><div class="wrap"><div class="brand">Workshop <span>commercialisti</span></div><a href="#iscrizione">Iscriviti gratis</a></div></header>
<main>
<section class="hero"><div class="wrap">
<div>
<p class="date">Giovedì 29 ottobre, ore 21:00 · gratis su Zoom</p>
<div class="big"><div class="n"><span>13</span></div><h1>funzioni per il lavoro ripetitivo dello studio. <mark>L'AI prepara, tu controlli.</mark></h1></div>
<p class="lead">Dalle risposte ai clienti agli F24 mandati con i solleciti, dai documenti del 730 alle fatture estere, dagli estratti conto alle circolari, fino a parcelle e archivio. <b>Scadenze, documenti e risposte sotto controllo.</b> Giovedì 29 ottobre te lo faccio vedere dal vivo.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="50" height="50"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
</div>
<div><ul class="chk" aria-label="Le 13 funzioni">{chk}</ul><p class="note">Tutte già attive nel programma: le vedi dal vivo il 29. Il gestionale resta il tuo.</p></div>
</div></section>

<section style="padding-top:10px"><div class="wrap">
<div class="nums">
<div class="num"><b>23 su 31</b><p>commercialisti al sondaggio del webinar del 30 settembre hanno messo F24 e solleciti fra le cose che tolgono più tempo.</p></div>
<div class="num"><b>182</b><p>iscritti all'edizione del 15 ottobre.</p></div>
<div class="num"><b>0</b><p>gestionali da cambiare. Non tiene la contabilità: lavora accanto al tuo e legge i PDF che ti fa scaricare.</p></div>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Le cose che oggi rischiano di scappare</h2>
<div class="never">
<div><h3>Gli invii del 16</h3><p>F24 pronti per tutti i clienti in una volta, promemoria due giorni prima, sollecito a chi non risponde, F24 scaduti fermati.</p></div>
<div><h3>L'avviso bonario inoltrato tardi</h3><p>L'AI lo legge, cerca la data di notifica nella conversazione e calcola la scadenza con la sospensione feriale.</p></div>
<div><h3>Il cliente che non manda i documenti</h3><p>Scegli i clienti e il giorno: l'elenco del 730 parte a ognuno, con il promemoria a chi non ha finito.</p></div>
</div>
<p class="sub" style="margin-top:26px">Quante ore a settimana se ne vanno così, nel tuo studio? Le contiamo insieme in diretta, sulle tue 3 attività più ripetitive.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Tutto quello che fa per lo studio</h2>
<p class="sub">Tredici funzioni, un solo programma. Scegli una voce e guarda la schermata vera.</p>
{tutto('d')}
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<div class="list">{agenda('<div class="li"><div class="c">{n}</div><div><h3>{t}</h3><p>{d}</p></div></div>')}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="who"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="220" height="220" loading="lazy"/><div>
<h3>Conduco io, Davide Caiazzo</h3><p>{BIO}</p><div class="press">{STAMPA}</div><p style="margin-top:14px;font-size:15px">{SQUADRA}</p>
</div></div></div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:24px">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · solo per commercialisti')}
</div></section>
</main>'''
    return page('D', "Workshop gratuito per commercialisti: 13 funzioni per il lavoro ripetitivo dello studio, le prepara l'intelligenza artificiale",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo i 13 lavori che Commercialista AI prepara per lo studio: F24, scadenze, email, 730, fatture estere, estratti, circolari, parcelle.",
      'family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Public+Sans:wght@400;600;700', D2_CSS, body,
      "[CLAUDE] 2026-10-17 sera variante D v2 (prova ott A/B/C/D): salvia ed evidenziatore, gancio numeri e risultato (13 lavori, cose che non scappano), tutto il programma. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

for v, fn in (('b', B), ('c', C), ('d', D)):
    out = os.path.join(REPO, 'workshop-ott-%s.html' % v)
    open(out, 'w').write(fn())
    print('scritto', out)
