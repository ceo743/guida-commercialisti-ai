# [CLAUDE] 17/10/2026 sera tardi: aggiunge la variante E (chi lavora nello studio è una professionista, non una segretaria)
# e il popup di uscita (popup-uscita.js) su B, C, D, E. Base: build2 (B/C/D tutto il programma) + build_v1 (modulo copiato da A).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'build2.py')).read()
src = src[:src.rindex("for v, fn in")]
src = src.replace("src = open(os.path.join(HERE, 'build_v1.py')).read()", "src = open(os.path.join(HERE, 'build_v1.py')).read()")
exec(src)

POPUP = {
 'b': ('#ffffff', '#17263c', '#526176', '#2254c5'),
 'c': ('#efe8d8', '#1d2b2e', '#5d625c', '#c9a24d'),
 'd': ('#fbfcf8', '#1e2a21', '#58655b', '#2f5d3a'),
 'e': ('#ffffff', '#2b1e36', '#6b6176', '#0e7c72'),
}
def con_popup(html, v):
    bg, fg, mu, ac = POPUP[v]
    tag = f'<script src="popup-uscita.js?v=20261017" data-bg="{bg}" data-fg="{fg}" data-muted="{mu}" data-accent="{ac}"></script>\n</body>'
    assert html.count('</body>') == 1
    return html.replace('</body>', tag)

E_CSS = '''
:root{--bg:#f5f3f8;--card:#fff;--ink:#2b1e36;--mute:#6b6176;--teal:#0e7c72;--teal2:#0a5f57;--sun:#f2b84b;--line:#e2dcea}
body{background:var(--bg);color:var(--ink);font-family:'Figtree',system-ui,sans-serif;font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased}
h1,h2,h3.s{font-family:'Literata',Georgia,serif;letter-spacing:-.01em}
.top .wrap{display:flex;justify-content:space-between;align-items:center;padding-top:18px;padding-bottom:18px;gap:12px}
.brand{font-weight:800;font-size:17px}.brand span{color:var(--teal)}
.top a{color:var(--teal);font-weight:700;text-decoration:none;font-size:15px}
.hero{padding:36px 0 64px}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:54px;align-items:center}
.pill{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:99px;padding:7px 14px;font-weight:700;font-size:14px;margin-bottom:22px}
.pill b{color:var(--teal)}
h1{font-size:clamp(34px,4.3vw,56px);font-weight:600;line-height:1.08;margin-bottom:20px}
h1 em{font-style:italic;color:var(--teal)}
.lead{color:var(--mute);max-width:600px;margin-bottom:26px}
.lead b{color:var(--ink)}
.cta{display:inline-block;background:var(--teal);color:#fff;text-decoration:none;font-weight:800;font-size:17px;padding:16px 28px;border-radius:999px;transition:background .15s}
.cta:hover{background:var(--teal2)}
.host{display:flex;align-items:center;gap:12px;margin-top:24px}
.host img{width:50px;height:50px;border-radius:50%;object-fit:cover}
.host p{font-size:14.5px;color:var(--mute);line-height:1.4}.host b{color:var(--ink)}
.proof{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:20px;font-size:14px;color:var(--mute)}
.proof span::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--sun);margin-right:8px;vertical-align:middle}
.desk{background:#fff;border:1px solid var(--line);border-radius:22px;padding:28px 26px;box-shadow:0 30px 60px rgb(43 30 54/10%)}
.desk h3{font-family:'Literata',Georgia,serif;font-size:21px;margin-bottom:4px}
.desk .who2{font-size:13.5px;color:var(--mute);margin-bottom:18px}
.desk h4{font-size:12.5px;font-weight:800;color:var(--mute);margin:14px 0 8px}
.desk ul{list-style:none}
.desk li{padding:7px 0;border-bottom:1px solid var(--line);font-size:15px}
.desk .off li{color:var(--mute);text-decoration:line-through;text-decoration-color:var(--sun);text-decoration-thickness:2px}
.desk .on li{font-weight:700}
.desk .on li::before{content:"✓ ";color:var(--teal)}
.desk small{display:block;margin-top:14px;font-size:12.5px;color:var(--mute)}
section{padding:70px 0}
h2{font-size:clamp(28px,3.2vw,42px);font-weight:600;line-height:1.12;margin-bottom:14px}
.sub{color:var(--mute);max-width:660px;margin-bottom:34px}
.two{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--line);border-radius:18px;overflow:hidden;background:#fff}
.two .hd{padding:14px 22px;font-weight:800;font-size:14px;background:#f0edf5}
.two .hd.t{background:var(--teal);color:#fff}
.two .c{padding:18px 22px;border-top:1px solid var(--line);font-size:15.5px}
.two .c.l{color:var(--mute);border-right:1px solid var(--line)}
.two .c b{display:block;font-size:13px;color:var(--ink);margin-bottom:2px}
.quote{margin-top:30px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.quote blockquote{background:#fff;border-left:4px solid var(--sun);border-radius:12px;padding:20px 22px;font-family:'Literata',Georgia,serif;font-size:19px;line-height:1.4}
.quote blockquote span{display:block;font-family:'Figtree',sans-serif;font-size:13px;color:var(--mute);margin-top:8px}
.quote .key{background:var(--ink);color:#fff;border-radius:12px;padding:20px 22px;font-size:18px;font-weight:700;line-height:1.4}
.tt-b{color:var(--ink);background:#fff;border:1px solid var(--line)}
.tt-b[aria-selected="true"]{background:var(--ink);color:#fff;border-color:var(--ink)}
.tt-p .ph{border:1px solid var(--line);box-shadow:0 24px 50px rgb(43 30 54/10%)}
.tt-p .noimg{background:#fff;border:1px dashed var(--line);color:var(--teal)}
.tt-p h3{font-family:'Literata',Georgia,serif}
.tt-p p,.tt-safe{color:var(--mute)}.tt-safe b{color:var(--ink)}
.agenda{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.ag{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px}
.ag .n{display:inline-flex;width:30px;height:30px;border-radius:50%;background:var(--sun);font-weight:800;align-items:center;justify-content:center;margin-bottom:10px}
.ag h3{font-size:18px;margin-bottom:4px}.ag p{color:var(--mute);font-size:15.5px}
.whoD{display:grid;grid-template-columns:200px 1fr;gap:32px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:22px;padding:30px}
.whoD img{border-radius:16px;aspect-ratio:1;object-fit:cover}
.whoD h3{font-family:'Literata',Georgia,serif;font-size:27px;margin-bottom:8px}
.whoD p{color:var(--mute);margin-bottom:10px}
.press{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;font-weight:700}.press a{color:var(--teal)}
.faq{max-width:760px}.faq-i{border-bottom:1px solid var(--line)}.faq-i p{color:var(--mute)}
#iscrizione .wrap{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.formbox{background:#fff;border:1px solid var(--line);border-radius:22px;box-shadow:0 30px 60px rgb(43 30 54/12%);padding:32px 28px}
.formbox h3{font-family:'Literata',Georgia,serif;font-size:27px;margin-bottom:4px}
.formsub{color:var(--mute);font-size:14.5px;margin-bottom:18px}
.formnote{font-size:12.5px;color:var(--mute);text-align:center;margin-top:12px}
.wk-field{width:100%;font:inherit;font-size:16px;padding:14px;border:1px solid var(--line);border-radius:12px;background:#faf9fc;color:var(--ink)}
.wk-field:focus{outline:2px solid var(--teal);border-color:var(--teal)}
.wk-priv{color:var(--mute)}.wk-priv a{color:var(--teal)}
.wk-errore{background:#fbe3e1;color:#9b1c13}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:var(--teal);color:#fff;border:0;border-radius:999px;font:inherit;font-weight:800;font-size:16px;padding:16px 18px;cursor:pointer;text-decoration:none}
.btn-gold:hover{background:var(--teal2)}.btn-gold:disabled{opacity:.6}
.cd>div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px 4px}
.cd b{font-family:'Literata',Georgia,serif;color:var(--ink)}.cd span{color:var(--mute)}
.wk-modal .box{background:#fff;color:var(--ink)}.wk-modal .box p{color:var(--mute)}
.wk-modal .box>div:first-child{background:#e3f3f1!important;color:var(--teal)!important}
.foot{text-align:center;font-size:12.5px;color:var(--mute);padding:30px 20px 40px}.foot a{color:var(--mute)}
@media (max-width:900px){
 .hero .wrap,#iscrizione .wrap,.quote,.agenda{grid-template-columns:1fr;gap:26px}
 .two{grid-template-columns:1fr}.two .hd.l2{display:none}.two .c.l{border-right:0}
 .whoD{grid-template-columns:1fr;padding:22px}.whoD img{max-width:180px}section{padding:50px 0}
}
'''
E_CSS = TUTTO_CSS + E_CSS

RIGHE_E = [
 ("Gli F24 del mese", "Controlla a mano chi ha ricevuto l'F24 e chi no, poi telefona.", "Vede in un elenco chi ha ricevuto; il sollecito a chi non risponde lo accendi tu."),
 ("Le domande dei clienti", "Risponde una per una a «cos'è questo codice tributo?».", "Trova la risposta già scritta nel tono dello studio: la rilegge e la manda."),
 ("Scadenze e avvisi bonari", "Segna a mano le scadenze di avvisi e cartelle arrivati per email.", "Le trova il programma nelle email e nei PDF, con la data calcolata: lei conferma."),
 ("Le fatture estere", "Ricopia i dati della fattura del fornitore estero nel gestionale.", "Ha l'XML pronto da controllare e importare, anche da una scansione."),
 ("I documenti del 730", "Richiama i clienti per i documenti che mancano.", "L'elenco parte ai clienti scelti, con il promemoria a chi non ha finito."),
]

def E():
    righe = ''.join(f'<div class="c l"><b>{t}</b>{o}</div><div class="c"><b>{t}</b>{c}</div>' for t, o, c in RIGHE_E)
    body = f'''<header class="top"><div class="wrap"><div class="brand">Commercialista<span>AI</span> dal vivo</div><a href="#iscrizione">Iscriviti gratis</a></div></header>
<main>
<section class="hero"><div class="wrap">
<div>
<p class="pill"><b>Workshop gratuito su Zoom</b> · giovedì 29 ottobre, ore 21:00</p>
<h1>Chi lavora nel tuo studio è una professionista. <em>Non l'hai assunta per fare la segreteria.</em></h1>
<p class="lead">Sei un commercialista? Anche chi lavora con te passa la giornata tra email, F24, solleciti e documenti da chiedere. <b>Giovedì 29 ottobre alle 21 ti mostro Commercialista AI dal vivo.</b> L'AI prepara il lavoro ripetitivo. Chi lavora con te controlla il risultato e può dedicarsi alle pratiche e ai clienti.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<p style="font-size:14px;color:var(--mute);margin-top:10px">Lavori in uno studio? Iscriviti anche tu.</p>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="50" height="50"/><p><b>Davide Caiazzo</b><br/>ha venduto MYGO SRL a Zucchetti</p></div>
<div class="proof"><span>182 iscritti all'edizione del 15 ottobre</span><span>Il gestionale resta il tuo</span><span>Scegli cosa inviare e quali solleciti attivare</span></div>
</div>
<div class="desk" aria-label="Esempio: la giornata di chi lavora nello studio">
<h3>Il lavoro per cui l'hai scelta</h3>
<p class="who2">La giornata di chi lavora nello studio, con Commercialista AI</p>
<h4>Lo prepara il programma</h4>
<ul class="off"><li>mandare gli F24 uno a uno</li><li>rispondere sempre alle stesse domande</li><li>segnare le scadenze a mano</li><li>ricopiare le fatture estere</li><li>rincorrere i documenti del 730</li></ul>
<h4>Torna a chi lavora con te</h4>
<ul class="on"><li>le pratiche dei clienti</li><li>i controlli che contano</li><li>la consulenza</li></ul>
<small>Il programma prepara. Lo studio controlla gli invii e sceglie quali solleciti automatici attivare.</small>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Oggi e con il programma</h2>
<p class="sub">Cinque attività che conosci bene. Giovedì vedi come il programma le prepara, su uno studio di esempio.</p>
<div class="two"><div class="hd l2">Oggi, a mano</div><div class="hd t">Con Commercialista AI</div>{righe}</div>
<div class="quote">
<blockquote>«Arranchiamo a trovare collaboratori.»<span>Un commercialista, parlando con noi</span></blockquote>
<div class="key">Chi lavora con te ha competenze da dedicare ai clienti. Il programma prepara le attività ripetitive. Le persone restano al centro delle pratiche e dei controlli.</div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Tutto quello che fa per lo studio</h2>
<p class="sub">Tredici funzioni, un solo programma accanto al tuo gestionale. Scegli una voce e guarda la schermata vera.</p>
{tutto('e')}
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<p class="sub">Clienti di prova, programma vero. Gira questa pagina a chi lavora con te: può iscriversi anche chi lavora nello studio.</p>
<div class="agenda">{agenda('<div class="ag"><div class="n">{n}</div><h3>{t}</h3><p>{d}</p></div>')}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="whoD"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="200" height="200" loading="lazy"/><div>
<h3>Te lo mostro io, Davide Caiazzo</h3><p>{BIO}</p><div class="press">{STAMPA}</div><p style="margin-top:12px;font-size:15px">{SQUADRA}</p>
</div></div></div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:24px">Compila il modulo per riservare il posto. Ricevi subito l'email di conferma. Il link Zoom arriva via email il giorno del webinar.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · per titolari e collaboratori degli studi')}
</div></section>
</main>'''
    return page('E', "Workshop gratuito per commercialisti: chi lavora nel tuo studio è una professionista, non la segreteria",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo tutto Commercialista AI: il lavoro ripetitivo lo prepara il programma, chi lavora nello studio torna al lavoro per cui è stata assunta.",
      'family=Literata:ital,opsz,wght@0,7..72,600;1,7..72,600&family=Figtree:wght@400;600;700;800', E_CSS, body,
      "[CLAUDE] 2026-10-17 sera variante E (prova ott A/B/C/D/E): chi lavora nello studio è una professionista, non una segretaria; prugna e verde acqua; tutto il programma. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

for v, fn in (('b', B), ('c', C), ('d', D), ('e', E)):
    out = os.path.join(REPO, 'workshop-ott-%s.html' % v)
    open(out, 'w').write(con_popup(fn(), v))
    print('scritto', out)
