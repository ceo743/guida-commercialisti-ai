# [CLAUDE] 17/10/2026 notte: variante F (struttura della landing sibill.com/commercialista adattata: «Meno burocrazia. Più consulenza.»,
# il programma fa le cose per te; mai «segreteria/segretaria» riferito alle persone). Base: build3 (A-E, popup).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'build3.py')).read()
src = src[:src.rindex("for v, fn in")]
exec(src)

TIT1 = os.environ.get('F_T1', 'Meno lavoro amministrativo.')
TIT2 = os.environ.get('F_T2', 'Più consulenza.')
SUBF = os.environ.get('F_SUB', "Commercialista AI fa le cose per te: risposte pronte alle email dei clienti, F24 mandati con i solleciti, scadenze e avvisi bonari, fatture estere, estratti conto, 730, circolari e parcelle. Giovedì 29 ottobre alle 21 te lo mostro dal vivo: così tu e chi lavora con te tornate a consulenza e clienti.")
POPUP['f'] = ('#ffffff', '#1b1f4b', '#5b5f80', '#ff6b4a')

F_CSS = '''
:root{--ind:#1b1f4b;--ind2:#2a2f6e;--ink:#1b1f4b;--mute:#5b5f80;--cor:#ff6b4a;--cor2:#e85532;--bg:#fbfbfd;--line:#e3e4ef;--lav:#c9ccff}
body{background:var(--bg);color:var(--ink);font-family:'Manrope',system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
.disc{background:var(--ind);color:#cfd1ee;opacity:1}
.heroF{background:radial-gradient(1200px 500px at 85% 20%,#2f3585 0%,var(--ind) 60%);color:#fff;padding:0 0 70px}
.heroF .top{display:flex;justify-content:space-between;align-items:center;padding:22px 0 30px;gap:12px}
.heroF .brand{font-weight:800;font-size:18px}.heroF .brand span{color:var(--cor)}
.heroF .top a{color:#fff;font-weight:700;text-decoration:none;font-size:15px;border:1px solid rgba(255,255,255,.35);padding:9px 16px;border-radius:999px}
.heroF .grid{display:grid;grid-template-columns:1fr 1.05fr;gap:50px;align-items:center}
.tag{display:inline-flex;gap:8px;align-items:center;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:6px 14px;font-size:14px;font-weight:600;margin-bottom:24px}
.tag i{width:8px;height:8px;border-radius:50%;background:var(--cor)}
.heroF h1{font-size:clamp(46px,6vw,84px);font-weight:800;line-height:.98;letter-spacing:-.035em;margin-bottom:22px}
.heroF h1 span{display:block;color:var(--lav)}
.heroF .lead{font-size:clamp(17px,1.4vw,20px);color:#dfe1f7;max-width:560px;margin-bottom:28px}
.heroF .lead b{color:#fff}
.cta{display:inline-block;background:var(--cor);color:#fff;text-decoration:none;font-weight:800;font-size:17px;padding:16px 30px;border-radius:999px;transition:background .15s}
.cta:hover{background:var(--cor2)}
.host{display:flex;align-items:center;gap:12px;margin-top:26px}
.host img{width:50px;height:50px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.6)}
.host p{font-size:14.5px;color:#cfd1ee;line-height:1.4}.host b{color:#fff}
.proofF{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:22px;padding-top:18px;border-top:1px solid rgba(255,255,255,.18);font-size:14.5px;color:#dfe1f7}
.proofF b{color:#fff}
.win{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.45)}
.win .bar{display:flex;gap:6px;padding:10px 12px;background:#f3f4fa}
.win .bar i{width:9px;height:9px;border-radius:50%;background:#d5d7e6}
.win figcaption{font-size:13px;color:var(--mute);padding:9px 14px;border-top:1px solid var(--line)}
section{padding:72px 0}
h2{font-size:clamp(30px,3.4vw,46px);font-weight:800;line-height:1.08;letter-spacing:-.02em;margin-bottom:14px}
h2 span{color:var(--cor)}
.sub{color:var(--mute);max-width:660px;margin-bottom:36px}
.pil{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.pil div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px}
.pil small{display:block;font-weight:800;color:var(--cor);font-size:13px;margin-bottom:8px}
.pil h3{font-size:20px;line-height:1.2;margin-bottom:10px}
.pil ul{list-style:none;font-size:15px;color:var(--mute)}
.pil li{padding:7px 0;border-top:1px solid var(--line)}
.pil li::before{content:"✓ ";color:var(--ind2);font-weight:800}
.month{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line);border-radius:18px;overflow:hidden;background:#fff}
.month div{padding:24px 22px;border-right:1px solid var(--line)}
.month div:last-child{border-right:0}
.month b{display:block;font-size:13px;font-weight:800;color:var(--cor);margin-bottom:6px}
.month h3{font-size:18px;margin-bottom:8px}
.month p{font-size:15px;color:var(--mute)}
.tt-b{color:var(--ink);background:#fff;border:1px solid var(--line)}
.tt-b[aria-selected="true"]{background:var(--ind);color:#fff;border-color:var(--ind)}
.tt-p .ph{border:1px solid var(--line);box-shadow:0 24px 60px rgb(27 31 75/14%)}
.tt-p .noimg{background:#fff;border:1px dashed var(--lav);color:var(--ind2)}
.tt-p p,.tt-safe{color:var(--mute)}.tt-safe b{color:var(--ink)}
.agF{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.agF div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}
.agF h3{font-size:18px;margin-bottom:4px}.agF p{color:var(--mute);font-size:15.5px}
.whoF{display:grid;grid-template-columns:200px 1fr;gap:32px;align-items:center;background:var(--ind);color:#fff;border-radius:22px;padding:30px}
.whoF img{border-radius:16px;aspect-ratio:1;object-fit:cover}
.whoF h3{font-size:27px;margin-bottom:8px}.whoF p{color:#dfe1f7;margin-bottom:10px}
.press{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;font-weight:700}.press a{color:var(--lav)}
.faq{max-width:760px}.faq-i{border-bottom:1px solid var(--line)}.faq-i p{color:var(--mute)}
#iscrizione{background:var(--ind);color:#fff}
#iscrizione .wrap{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
#iscrizione .sub{color:#dfe1f7}
.formbox{background:#fff;color:var(--ink);border-radius:22px;padding:32px 28px;box-shadow:0 30px 70px rgba(0,0,0,.35)}
.formbox h3{font-size:26px;font-weight:800;margin-bottom:4px}
.formsub{color:var(--mute);font-size:14.5px;margin-bottom:18px}
.formnote{font-size:12.5px;color:var(--mute);text-align:center;margin-top:12px}
.wk-field{width:100%;font:inherit;font-size:16px;padding:14px;border:1px solid var(--line);border-radius:12px;background:#f8f8fc;color:var(--ink)}
.wk-field:focus{outline:2px solid var(--ind2);border-color:var(--ind2)}
.wk-priv{color:var(--mute)}.wk-priv a{color:var(--ind2)}
.wk-errore{background:#fde7e2;color:#a3260f}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:var(--cor);color:#fff;border:0;border-radius:999px;font:inherit;font-weight:800;font-size:16px;padding:16px 18px;cursor:pointer;text-decoration:none}
.btn-gold:hover{background:var(--cor2)}.btn-gold:disabled{opacity:.6}
#iscrizione .cd>div{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:8px 4px}
#iscrizione .cd b{color:#fff}#iscrizione .cd span{color:#cfd1ee}
.wk-modal .box{background:#fff;color:var(--ink)}.wk-modal .box p{color:var(--mute)}
.wk-modal .box>div:first-child{background:#ffe7e0!important;color:var(--cor)!important}
.foot{text-align:center;font-size:12.5px;color:var(--mute);padding:30px 20px 40px}.foot a{color:var(--mute)}
@media (max-width:900px){
 .heroF .grid,#iscrizione .wrap,.agF{grid-template-columns:1fr;gap:30px}.heroF .top a{display:none}
 .pil,.month{grid-template-columns:1fr}.month div{border-right:0;border-bottom:1px solid var(--line)}
 .whoF{grid-template-columns:1fr;padding:22px}.whoF img{max-width:180px}section{padding:52px 0}
}
'''
F_CSS = TUTTO_CSS + F_CSS

MESE = [
 ("Ogni giorno", "La posta", "Le email dei clienti arrivano con la risposta già scritta da rileggere. Scadenze e avvisi bonari trovati nella posta finiscono in calendario."),
 ("Prima del 16", "Gli F24", "Carichi gli F24 del gestionale: il programma riconosce il cliente e prepara le email. Tu controlli e premi Invia, poi vedi chi ha ricevuto."),
 ("Durante il mese", "Fatture e conti", "Fatture estere trasformate in XML, estratti conto che carichi abbinati alle fatture, differenze con i movimenti trovate dal Confronto."),
 ("Quando serve", "Clienti e studio", "Documenti del 730 chiesti ai clienti che scegli, circolari con la fonte ufficiale, parcelle dello studio con i promemoria."),
]

def F():
    mese = ''.join(f'<div><b>{q}</b><h3>{t}</h3><p>{d}</p></div>' for q, t, d in MESE)
    body = f'''<div class="heroF"><div class="wrap">
<header class="top"><div class="brand">Commercialista<span>AI</span> · dal vivo</div><a href="#iscrizione">Riserva il posto</a></header>
<div class="grid">
<div>
<p class="tag"><i aria-hidden="true"></i>Workshop gratuito su Zoom · giovedì 29 ottobre, ore 21:00</p>
<h1>{TIT1}<span>{TIT2}</span></h1>
<p class="lead">{SUBF}</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="proofF"><span><b>182</b> iscritti all'edizione del 15 ottobre</span><span>Il gestionale <b>resta il tuo</b></span><span>Niente parte <b>senza il tuo sì</b></span></div>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="50" height="50"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
</div>
<figure class="win"><div class="bar" aria-hidden="true"><i></i><i></i><i></i></div>
<picture><source media="(max-width:700px)" srcset="img-ott/email-telefono.webp"/><img src="img-ott/email.webp" width="1440" height="860" alt="Email dei clienti in Commercialista AI: le risposte preparate dal programma"/></picture>
<figcaption>Email dei clienti in Commercialista AI, studio dimostrativo: le risposte preparate da rileggere.</figcaption></figure>
</div></div></div>
<main>
<section><div class="wrap">
<h2>Cosa fa Commercialista AI per lo studio. <span>Il lavoro ripetitivo lo prepara il programma.</span></h2>
<p class="sub">F24, posta, scadenze, documenti: il lavoro che oggi si fa a mano. La contabilità resta nel tuo gestionale. Chi lavora nello studio, spesso commercialista come te, torna alle pratiche e ai clienti.</p>
<div class="pil">
<div><small>In un posto solo</small><h3>Clienti, documenti e posta in ordine</h3><ul><li>una scheda per ogni cliente</li><li>i documenti arrivati nella scheda giusta</li><li>ogni invio con il suo esito</li></ul></div>
<div><small>Preparato dall'AI</small><h3>Il lavoro ripetitivo, pronto da controllare</h3><ul><li>F24 mandati, con i solleciti</li><li>scadenze e avvisi bonari dalle email</li><li>risposte ai clienti, XML delle fatture estere</li></ul></div>
<div><small>Più tempo</small><h3>Consulenza e clienti</h3><ul><li>circolari ai clienti giusti</li><li>parcelle dello studio con i promemoria</li><li>le ore tornano alle pratiche</li></ul></div>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Il mese dello studio, preparato</h2>
<p class="sub">Clienti di prova, programma vero: giovedì lo vedi scorrere dal vivo.</p>
<div class="month">{mese}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Tutto quello che fa per lo studio</h2>
<p class="sub">Tredici funzioni, un solo programma accanto al tuo gestionale. Scegli una voce e guarda la schermata vera.</p>
{tutto('f')}
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<div class="agF">{agenda('<div><h3>{n}. {t}</h3><p>{d}</p></div>')}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="whoF"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="200" height="200" loading="lazy"/><div>
<h3>Conduco io, Davide Caiazzo</h3><p>{BIO}</p><div class="press">{STAMPA}</div><p style="margin-top:12px;font-size:15px">{SQUADRA}</p>
</div></div></div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:24px">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · solo per commercialisti')}
</div></section>
</main>'''
    return page('F', "Workshop gratuito per commercialisti: meno lavoro amministrativo, più consulenza. Commercialista AI fa le cose per te",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo tutto Commercialista AI: il lavoro amministrativo dello studio lo prepara il programma, tu e chi lavora con te tornate a consulenza e clienti.",
      'family=Manrope:wght@400;600;700;800', F_CSS, body,
      "[CLAUDE] 2026-10-17 notte variante F (prova ott A-F): struttura della landing sibill.com/commercialista adattata («Meno lavoro amministrativo. Più consulenza.», il programma fa le cose per te; titolo scelto da CMO fra 3 con lente Hormozi), indaco e corallo, tutto il programma, mai «segreteria». Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

for v, fn in (('b', B), ('c', C), ('d', D), ('e', E), ('f', F)):
    out = os.path.join(REPO, 'workshop-ott-%s.html' % v)
    open(out, 'w').write(con_popup(fn(), v))
    print('scritto', out)
