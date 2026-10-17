# [CLAUDE] 17/10/2026 genera le varianti B, C, D della prova pagine workshop commercialisti (edizione 29/10).
# Le parti di tracciamento e il modulo si COPIANO da workshop.html (pagina A) senza modificarle,
# cosi' il modulo e' identico: stessi campi, stesso ponte Kajabi, stessi utm, stessa pagina grazie con il Lead.
import sys, re, os
REPO = sys.argv[1]
A = open(os.path.join(REPO, 'workshop.html')).read()

def between(s, start, end, incl_end=True):
    i = s.index(start); j = s.index(end, i)
    return s[i:j + (len(end) if incl_end else 0)]

PIXEL = between(A, '<!-- Meta Pixel', '</noscript>')
DCL = between(A, "<script>\n/* [CLAUDE] 2026-10-02: prova A/B", '</script>')
assert "var variante = 'ott-A';" in DCL or "var variante = 'settembre-A';" in DCL
COOKIE = between(A, '<script type="text/javascript" charset="UTF-8" src="//cdn.cookie-script.com', '</script>')
WIDGETCSS = '<link rel="stylesheet" href="https://dc-chatbot-vswb.onrender.com/static/widget.css"/>'
assert WIDGETCSS in A
FORM = between(A, '<form id="leadForm"', '</form>')
MODAL = between(A, '<div class="wk-modal" id="confirmModal">', '</div></div>')
SUBMIT = between(A, "<script>\n(function(){\n  var params = new URLSearchParams(window.location.search);", '</script>')
WIDGETJS = '<script src="https://dc-chatbot-vswb.onrender.com/widget.js" data-bot="commercialisti" data-auto-open="false"></script>'
EXPJS = '<script src="workshop-experiment.js?v=20260914a"></script>'
assert WIDGETJS in A and EXPJS in A

def dcl(v):
    return re.sub(r"var variante = '[^']*';", "var variante = 'ott-%s';" % v, DCL)

COUNTDOWN = '''<div class="cd" aria-label="Tempo alla diretta"><div><b id="cdG">--</b><span>giorni</span></div><div><b id="cdH">--</b><span>ore</span></div><div><b id="cdM">--</b><span>minuti</span></div><div><b id="cdS">--</b><span>secondi</span></div></div>'''

FAQ = [
 ("È un corso?", "No. È una serata dal vivo: apro il programma e ti mostro un caso intero, dall'inizio alla fine, su uno studio di esempio. Tu guardi e fai domande."),
 ("Quanto costa partecipare?", "Niente, il workshop è gratuito. A fine serata ti racconto anche come lavorare con me e il mio team, se vorrai approfondire, senza nessun obbligo."),
 ("Funziona con il gestionale che uso in studio?", "Sì. Il gestionale resta il tuo: il programma legge i PDF che il gestionale ti fa scaricare e prepara il lavoro che poi ci entra. TeamSystem, Zucchetti, Profis o altro."),
 ("Devo saper usare la tecnologia?", "No. Guardi il mio schermo mentre lavoro: le dimostrazioni le faccio io, tu fai le domande. Ti basta il link Zoom che arriva via email, si apre anche dal browser."),
 ("Cosa NON fa il programma?", "Non tiene la contabilità e non sostituisce il gestionale. Prepara il lavoro che ci entra e quello che va ai clienti: F24, risposte, scadenze, documenti. Te lo dico subito, così giovedì sai cosa aspettarti."),
 ("E i dati dei miei clienti?", "Ne parlo in diretta. Il principio è uno: il programma prepara, il professionista controlla e approva. Niente parte senza il tuo sì."),
 ("Non posso esserci giovedì 29. Che faccio?", "Iscriviti comunque: dopo la diretta ti mando la registrazione per email, online per 48 ore. Le domande però le fai solo dal vivo."),
]
def faq_html():
    return '\n'.join('<details class="faq-i"><summary>%s</summary><p>%s</p></details>' % q for q in FAQ)

DAVIDE_BIO = ("Imprenditore. Ha costruito My Governance, un software per le aziende, e l'ha venduta al gruppo Zucchetti: "
  "«valutazione oltre 10 milioni», ha titolato Il Sole 24 Ore. È TOP 20 al mondo in “LinkedIn® Growth” secondo Favikon 2025. "
  "Usa l'intelligenza artificiale ogni giorno nelle sue aziende: Commercialista AI nasce da lì, costruito e provato insieme a due studi commercialisti.")
STAMPA = ('<a href="https://ntplusdiritto.ilsole24ore.com/art/zucchetti-acquisisce-my-governance-valutazione-oltre-10-milioni-caiazzo-confermato-ad-AHraItpC" target="_blank" rel="noopener noreferrer">Il Sole 24 Ore</a>'
  '<a href="https://www.iltempo.it/tv-news/2026/03/11/video/libri-arriva-il-potere-di-linkedin-di-davide-caiazzo-46755479/" target="_blank" rel="noopener noreferrer">Il Tempo</a>'
  '<a href="https://www.leggo.it/video/libri_arriva_il_potere_di_linkedin_di_davide_caiazzo-9409483.html" target="_blank" rel="noopener noreferrer">Leggo</a>')

FOOTER = '''<footer class="foot"><p>DC Academy S.r.l. | P.IVA 05125350750 | Via I. Adriano 9, Lecce | academy@davidecaiazzo.it<br/>
<a href="https://docs.google.com/document/d/1qUNgRcZ0W9aZxutDu1Fv2k5aM6Nti4V0/edit" target="_blank" rel="noopener">Privacy</a> ·
<a href="https://docs.google.com/document/d/1PTTs2QFMqBtZaefLHPrrfMxJRnlGewih/edit" target="_blank" rel="noopener">Cookie</a> ·
<a href="https://docs.google.com/document/d/1K6WGjt9aFTRN-zWMvEOh5bw2A32nNag-/edit" target="_blank" rel="noopener">Condizioni di Vendita</a></p></footer>'''

def page(v, title, desc, fonts, css, body, note):
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
{PIXEL}

<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
{dcl(v)}
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="https://commercialisti.davidecaiazzo.it/"/>
<meta name="robots" content="noindex,follow"/>
<!-- {note} -->
<meta property="og:type" content="website"/>
<meta property="og:url" content="https://commercialisti.davidecaiazzo.it/"/>
<meta property="og:title" content="Il lavoro ripetitivo dello studio lo fa il programma. Dimostrazione dal vivo, gratis."/>
<meta property="og:description" content="F24, documenti, scadenze e risposte ai clienti: lo vedi fare su uno studio vero, su Zoom."/>
<meta property="og:image" content="https://commercialisti.davidecaiazzo.it/og-commercialisti.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<link rel="icon" type="image/png" href="https://automazioni.davidecaiazzo.it/favicon.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet"/>
{COOKIE}
{WIDGETCSS}
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
img{{max-width:100%;height:auto;display:block}}
a{{color:inherit}}
.wrap{{max-width:1160px;margin:0 auto;padding:0 20px}}
.wk-errore{{font-size:14px;line-height:1.5;padding:12px 14px;border-radius:8px}}
.wk-field.error{{outline:2px solid #d93025!important}}
.wk-priv{{display:flex;gap:10px;align-items:flex-start;font-size:13px;line-height:1.45;cursor:pointer;text-align:left}}
.wk-priv input{{margin-top:3px;width:17px;height:17px;flex:0 0 auto}}
.checkbox-error span{{color:#d93025}}
.wk-modal{{position:fixed;inset:0;z-index:9999;display:none;align-items:center;justify-content:center;padding:20px;background:rgba(10,15,25,.6)}}
.wk-modal.open{{display:flex}}
.wk-modal .box{{max-width:440px;width:100%;border-radius:16px;padding:34px 28px;text-align:center}}
.wk-modal h4{{font-size:24px;margin-bottom:10px}}
.wk-modal p{{font-size:15px;line-height:1.6;margin-bottom:8px}}
.cd{{display:flex;gap:10px}}
.cd>div{{min-width:64px;text-align:center}}
.cd b{{display:block;font-size:26px;font-variant-numeric:tabular-nums;line-height:1.1}}
.cd span{{font-size:11px;opacity:.7}}
.faq-i summary{{cursor:pointer;list-style:none;font-weight:700;padding:18px 32px 18px 0;position:relative}}
.faq-i summary::-webkit-details-marker{{display:none}}
.faq-i summary::after{{content:"+";position:absolute;right:4px;top:14px;font-size:22px;font-weight:400}}
.faq-i[open] summary::after{{content:"–"}}
.faq-i p{{padding:0 0 18px;line-height:1.65}}
:focus-visible{{outline:3px solid currentColor;outline-offset:3px}}
.disc{{text-align:center;padding:8px 16px;font-size:10.5px;line-height:1.5;opacity:.6}}
.disc a{{text-decoration:underline}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important;scroll-behavior:auto!important}}}}
{css}
</style>
</head>
<body>
<div class="disc"><strong>I contenuti di questo sito hanno natura pubblicitaria</strong> a favore della DC Academy S.r.l. · Per qualsiasi approfondimento sui nostri servizi, clienti, testimonianze, testate e sui numeri citati su questo sito visita la pagina: <a href="https://www.davidecaiazzo.it/trasparenza" target="_blank" rel="noopener">www.davidecaiazzo.it/trasparenza</a></div>
{body}
{FOOTER}
{MODAL}
{SUBMIT}
{WIDGETJS}
{EXPJS}
</body>
</html>
'''

def form_block(cls_title, title, sub):
    return f'''<div class="formbox"><h3 class="{cls_title}">{title}</h3><p class="formsub">{sub}</p>
{FORM}
<p class="formnote">Il link Zoom arriva via email prima della diretta. Nessuno spam.</p></div>'''

# =============== B: stile Commercialista AI + Invia F24 ===============
B_CSS = '''
:root{--bg:#f7f9fc;--card:#fff;--ink:#17263c;--grey:#526176;--blue:#2254c5;--blue2:#183e96;--tint:#edf3ff;--line:#dce3ec;--green:#226343}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
.serif{font-family:'Source Serif 4',Georgia,serif}
.top{border-bottom:1px solid var(--line);background:#fff}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;gap:12px}
.logo{font-family:'Source Serif 4',Georgia,serif;font-weight:700;font-size:19px}
.logo span{color:var(--blue)}
.top a.mini{background:var(--blue);color:#fff;text-decoration:none;font-weight:600;font-size:14px;padding:9px 14px;border-radius:10px;white-space:nowrap}
.hero{padding:56px 0 40px}
.hero .wrap{display:grid;grid-template-columns:1fr 1.1fr;gap:48px;align-items:center}
.when{display:inline-flex;align-items:center;gap:8px;background:var(--tint);color:var(--blue2);font-weight:600;font-size:14px;padding:7px 14px;border-radius:99px;margin-bottom:22px}
.when i{width:8px;height:8px;border-radius:50%;background:#d93025;display:inline-block}
h1{font-family:'Source Serif 4',Georgia,serif;font-weight:600;font-size:clamp(34px,4.2vw,54px);line-height:1.08;letter-spacing:-.02em;margin-bottom:20px}
h1 em{font-style:normal;color:var(--blue)}
.lead{font-size:clamp(17px,1.4vw,19px);color:var(--grey);max-width:560px;margin-bottom:26px}
.cta{display:inline-flex;align-items:center;justify-content:center;background:var(--blue);color:#fff;text-decoration:none;font-weight:700;font-size:17px;padding:16px 26px;border-radius:10px;box-shadow:0 6px 18px rgb(34 84 197/25%);transition:background .15s}
.cta:hover{background:var(--blue2)}
.host{display:flex;align-items:center;gap:12px;margin-top:26px}
.host img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 0 0 1px var(--line)}
.host p{font-size:14.5px;color:var(--grey);line-height:1.4}
.host b{color:var(--ink)}
.proof{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:22px;padding-top:18px;border-top:1px solid var(--line);font-size:14px;color:var(--grey)}
.proof span::before{content:"✓";color:var(--green);font-weight:700;margin-right:6px}
.shot{background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:0 24px 60px rgb(23 38 60/14%);overflow:hidden}
.shot .bar{display:flex;gap:6px;padding:10px 12px;border-bottom:1px solid var(--line);background:#fbfcfe}
.shot .bar i{width:9px;height:9px;border-radius:50%;background:#dce3ec}
.shot figcaption{font-size:13px;color:var(--grey);padding:10px 14px;border-top:1px solid var(--line)}
section{padding:64px 0}
.sec-h{font-family:'Source Serif 4',Georgia,serif;font-size:clamp(28px,3vw,38px);font-weight:600;line-height:1.15;margin-bottom:12px;letter-spacing:-.01em}
.sec-p{color:var(--grey);max-width:640px;margin-bottom:34px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.col{background:#fff;border:1px solid var(--line);border-radius:12px;padding:26px 24px;box-shadow:0 3px 12px rgb(23 38 60/6%)}
.col h3{font-size:19px;margin-bottom:10px}
.col p{color:var(--grey);font-size:15.5px;margin-bottom:12px}
.col ul{list-style:none;font-size:15px}
.col li{padding:6px 0;border-top:1px solid var(--line)}
.col li::before{content:"✓ ";color:var(--green);font-weight:700}
.band{background:var(--ink);color:#fff;padding:34px 0}
.band .wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.band h2{font-family:'Source Serif 4',Georgia,serif;font-weight:600;font-size:clamp(22px,2.4vw,30px)}
.band .cta{background:#fff;color:var(--ink);box-shadow:none}
.band .cd b{color:#fff}.band .cd span{color:#c8d3e4}
.agenda{display:grid;gap:14px;max-width:860px}
.ag{display:grid;grid-template-columns:44px 1fr;gap:16px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px}
.ag .n{width:36px;height:36px;border-radius:10px;background:var(--tint);color:var(--blue2);font-weight:700;display:flex;align-items:center;justify-content:center}
.ag h3{font-size:18px;margin-bottom:4px}
.ag p{color:var(--grey);font-size:15.5px}
.who{display:grid;grid-template-columns:200px 1fr;gap:34px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:16px;padding:32px}
.who img{border-radius:14px;aspect-ratio:1;object-fit:cover}
.who h3{font-family:'Source Serif 4',Georgia,serif;font-size:28px;font-weight:600;margin-bottom:8px}
.who p{color:var(--grey);margin-bottom:12px}
.press{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;font-weight:600}
.press a{color:var(--blue2)}
.team{margin-top:14px;font-size:15px;color:var(--grey);border-top:1px solid var(--line);padding-top:12px}
.fit{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.fit div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:24px}
.fit h3{font-size:18px;margin-bottom:10px}
.fit li{list-style:none;padding:6px 0;font-size:15.5px;color:var(--grey)}
.faq{max-width:760px}
.faq-i{border-bottom:1px solid var(--line)}
.faq-i p{color:var(--grey)}
#iscrizione{background:linear-gradient(180deg,var(--bg),#e8eef9)}
#iscrizione .wrap{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.formbox{background:#fff;border:1.5px solid var(--blue);border-radius:16px;padding:32px 28px;box-shadow:0 20px 50px rgb(34 84 197/12%)}
.formbox h3{font-family:'Source Serif 4',Georgia,serif;font-size:26px;font-weight:600;margin-bottom:4px}
.formsub{color:var(--grey);font-size:14.5px;margin-bottom:18px}
.formnote{font-size:12.5px;color:var(--grey);text-align:center;margin-top:12px}
.wk-field{width:100%;font:inherit;font-size:16px;padding:14px 14px;border:1px solid var(--line);border-radius:10px;background:#fbfcfe;color:var(--ink)}
.wk-field:focus{outline:2px solid var(--blue);border-color:var(--blue)}
.wk-priv{color:var(--grey)}.wk-priv a{color:var(--blue2)}
.wk-errore{background:#fdeceb;color:#a81f15}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:var(--blue);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;font-size:16px;padding:16px 18px;cursor:pointer;text-decoration:none}
.btn-gold:hover{background:var(--blue2)}.btn-gold:disabled{opacity:.6}
.cd b{color:var(--ink)}.cd span{color:var(--grey)}
.wk-modal .box{background:#fff;color:var(--ink)}.wk-modal .box p{color:var(--grey)}
.wk-modal .box>div:first-child{background:var(--tint)!important;color:var(--blue)!important}
.foot{text-align:center;font-size:12.5px;color:var(--grey);padding:30px 20px 40px;border-top:1px solid var(--line)}
.foot a{color:var(--grey)}
@media (max-width:900px){
 .hero{padding:32px 0 28px}.hero .wrap,#iscrizione .wrap{grid-template-columns:1fr;gap:28px}
 .cols,.fit{grid-template-columns:1fr}.who{grid-template-columns:1fr;padding:22px}.who img{max-width:180px}
 section{padding:46px 0}.top a.mini{display:none}
}
'''

def B():
    body = f'''<header class="top"><div class="wrap"><div class="logo">Commercialista<span>AI</span> · dal vivo</div><a class="mini" href="#iscrizione">Riserva il posto</a></div></header>
<main>
<section class="hero"><div class="wrap">
<div>
<p class="when"><i aria-hidden="true"></i>Workshop gratuito su Zoom · giovedì 29 ottobre, ore 21:00</p>
<h1>Il 16 mandi gli F24 a tutti i clienti. <em>E sai chi li ha ricevuti.</em></h1>
<p class="lead">Giovedì 29 ottobre apro il computer e te lo faccio vedere sul programma vero: riconosce il cliente da ogni F24, prepara le email e sollecita chi non risponde. Tu controlli e premi Invia. Il gestionale resta il tuo.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="52" height="52"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
<div class="proof"><span>Più di 180 commercialisti iscritti all'edizione del 15 ottobre</span><span>Si guarda e si fanno domande</span><span>Gratis</span></div>
</div>
<figure class="shot"><div class="bar" aria-hidden="true"><i></i><i></i><i></i></div>
<picture><source media="(max-width:700px)" srcset="img-ott/invia-f24-telefono.webp"/><img src="img-ott/invia-f24.webp" width="1440" height="860" alt="La pagina Invia F24 di Commercialista AI: F24 da mandare, in attesa di risposta, confermati"/></picture>
<figcaption>Invia F24 in Commercialista AI, studio dimostrativo: da mandare, aspettano risposta, confermati.</figcaption></figure>
</div></section>

<section><div class="wrap">
<h2 class="sec-h">L'F24 al cliente lo manda il programma. Tu torni a fare consulenza.</h2>
<p class="sec-p">Quante ore al mese passi a mandare gli F24 ai clienti uno a uno? Mi dicevano che nessun commercialista avrebbe lasciato fare questo lavoro a un programma. L'ho fatto lo stesso. Giovedì lo vedi fare queste tre cose al posto tuo.</p>
<div class="cols">
<div class="col"><h3>Ogni F24 al cliente giusto</h3><p>Carichi gli F24 del mese, fatti con il gestionale.</p><ul><li>riconosce di quale cliente è ogni F24</li><li>prepara l'email con l'allegato giusto</li><li>parte solo quando premi Invia</li></ul></div>
<div class="col"><h3>Chi ha ricevuto e chi no</h3><p>Le conferme si segnano da sole.</p><ul><li>elenco di chi ha risposto e chi aspetta</li><li>sollecito a chi non risponde</li><li>promemoria due giorni prima, gli F24 scaduti fermati</li></ul></div>
<div class="col"><h3>«Cos'è il 6099?»</h3><p>Il giorno dopo arrivano le domande.</p><ul><li>legge l'email del cliente</li><li>prepara la risposta nel tono dello studio</li><li>l'ultima parola è tua</li></ul></div>
</div></div></section>

<div class="band"><div class="wrap"><h2>Giovedì 29 ottobre, ore 21:00. La diretta inizia tra</h2>{COUNTDOWN}<a class="cta" href="#iscrizione">Iscriviti gratis</a></div></div>

<section><div class="wrap">
<h2 class="sec-h">Cosa vedi dal vivo</h2>
<p class="sec-p">Un caso intero su uno studio di esempio, dall'inizio alla fine. Clienti di prova, programma vero.</p>
<div class="agenda">
<div class="ag"><div class="n">1</div><div><h3>Il 16 del mese, dall'F24 caricato al «ricevuto»</h3><p>Carico tutti gli F24 del mese. Il programma capisce di quale cliente è ognuno e prepara le email. Controllo, premo Invia, e vedi chi conferma e chi riceve il sollecito.</p></div></div>
<div class="ag"><div class="n">2</div><div><h3>Le domande dei clienti con la risposta già pronta</h3><p>Un'email vera di un cliente e la risposta scritta dal programma, con tutta la conversazione tenuta a mente. La mandi tu.</p></div></div>
<div class="ag"><div class="n">3</div><div><h3>Scadenze e avvisi bonari che non scappano</h3><p>Il programma trova le scadenze in documenti e posta, legge l'avviso bonario e ti avvisa prima. Tu confermi.</p></div></div>
<div class="ag"><div class="n">4</div><div><h3>Le tue domande, in diretta</h3><p>Rispondo io, sul tuo studio. Alla fine ti dico quanto costa e come si attiva. Nessun obbligo.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="who"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="200" height="200" loading="lazy"/><div>
<h3>Conduco io, Davide Caiazzo</h3>
<p>Ho costruito My Governance, un software per le aziende, e l'ho venduta al gruppo Zucchetti: «valutazione oltre 10 milioni», ha titolato Il Sole 24 Ore. Sono TOP 20 al mondo in “LinkedIn® Growth” secondo Favikon 2025. Commercialista AI l'ho costruito e provato insieme a due studi commercialisti.</p>
<div class="press">{STAMPA}</div>
<p class="team">In squadra con me Gianfranco Motta, il tecnico di DC Academy: tiene d'occhio la chat e mi porta le domande più tecniche.</p>
</div></div>
</div></section>

<section><div class="wrap">
<h2 class="sec-h">Per chi è</h2>
<div class="fit"><div><h3>Fa per te se</h3><ul><li>✓ hai uno studio, da solo o associato, e il 16 ti mangia la giornata</li><li>✓ vuoi vedere l'intelligenza artificiale sul lavoro vero di uno studio, non la teoria</li><li>✓ non hai competenze tecniche: non servono</li></ul></div>
<div><h3>Non fa per te se</h3><ul><li>✗ cerchi un corso di teoria sull'intelligenza artificiale</li><li>✗ vuoi solo la registrazione da guardare «prima o poi»</li></ul></div></div>
</div></section>

<section><div class="wrap"><h2 class="sec-h">Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2 class="sec-h">Giovedì 29 ottobre, ore 21:00. Su Zoom.</h2><p class="sec-p">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom con i promemoria.</p></div>
{form_block('', 'Riserva il tuo posto gratis', 'Giovedì 29 ottobre, ore 21:00 · Live su Zoom')}
</div></section>
</main>'''
    return page('B', "Workshop gratuito per commercialisti: gli F24 a tutti i clienti, e sai chi li ha ricevuti",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo Commercialista AI: F24 inviati a ogni cliente, conferme di ricezione e solleciti.",
      'family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700', B_CSS, body,
      "[CLAUDE] 2026-10-17 variante B (prova ott A/B/C/D): stile del sito Commercialista AI + gancio Invia F24 + struttura landing Sibill. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

# =============== C: notte petrolio + ottone, Fatture estere ===============
C_CSS = '''
:root{--bg:#0c262b;--bg2:#103239;--paper:#efe8d8;--mute:#a7b9b5;--brass:#c9a24d;--brass2:#e0bd6c;--line:#24474e}
body{background:var(--bg);color:var(--paper);font-family:'Instrument Sans',system-ui,sans-serif;font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3.d{font-family:'Fraunces',Georgia,serif;font-weight:500;letter-spacing:-.01em}
.top{padding:22px 0;border-bottom:1px solid var(--line)}
.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:12px}
.mark{font-family:'Fraunces',Georgia,serif;font-size:18px}
.mark small{color:var(--mute);font-family:'Instrument Sans',sans-serif;font-size:13px;margin-left:8px}
.datechip{color:var(--brass2);font-size:14px;font-weight:600;white-space:nowrap}
.hero{padding:70px 0 54px;text-align:center}
.kick{color:var(--mute);font-size:15px;margin-bottom:22px}
h1{font-size:clamp(36px,5.4vw,72px);line-height:1.04;max-width:980px;margin:0 auto 26px}
h1 .b{color:var(--brass2);font-style:italic}
.lead{max-width:660px;margin:0 auto 34px;color:var(--mute);font-size:clamp(17px,1.4vw,19px)}
.lead b{color:var(--paper);font-weight:600}
.flow{display:grid;grid-template-columns:1fr 70px 1fr;align-items:center;max-width:900px;margin:0 auto 40px;text-align:left}
.doc{background:var(--paper);color:#2a2a26;border-radius:6px;padding:22px 22px 18px;box-shadow:0 30px 60px rgb(0 0 0/35%);font-size:13px;line-height:1.5;min-height:210px}
.doc .h{display:flex;justify-content:space-between;font-weight:700;font-size:12px;letter-spacing:.04em;border-bottom:1px solid #d6cdb8;padding-bottom:8px;margin-bottom:10px}
.doc .h span:last-child{background:#b3261e;color:#fff;border-radius:3px;padding:1px 6px;font-size:11px}
.doc dl{display:grid;grid-template-columns:auto 1fr;gap:3px 12px}
.doc dt{color:#7a7465}.doc dd{font-weight:600}
.arrow{text-align:center;color:var(--brass2);font-size:30px}
.xml{background:#071a1e;border:1px solid var(--brass);border-radius:6px;padding:20px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12.5px;line-height:1.7;color:#cfe1dc;min-height:210px;overflow-wrap:anywhere}
.xml .t{color:var(--brass2)}.xml .ok{color:#8fd19e}
.xml .h{font-family:'Instrument Sans',sans-serif;font-weight:700;color:var(--paper);font-size:12px;margin-bottom:8px}
.cta{display:inline-block;background:var(--brass);color:#14262a;font-weight:700;text-decoration:none;font-size:17px;padding:17px 30px;border-radius:4px;transition:background .15s}
.cta:hover{background:var(--brass2)}
.byline{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:30px;text-align:left}
.byline img{width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid var(--brass)}
.byline p{font-size:14.5px;color:var(--mute);line-height:1.45}
.byline b{color:var(--paper)}
.strip{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:18px 0;color:var(--mute);font-size:14.5px}
.strip .wrap{display:flex;justify-content:center;gap:12px 34px;flex-wrap:wrap;text-align:center}
.strip b{color:var(--paper)}
section{padding:80px 0}
.story{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;align-items:center}
.story img{border-radius:4px;filter:grayscale(.15);aspect-ratio:1;object-fit:cover}
.story blockquote{font-family:'Fraunces',Georgia,serif;font-size:clamp(26px,3vw,40px);line-height:1.2;margin-bottom:22px}
.story blockquote::before{content:"“";color:var(--brass2)}
.story blockquote::after{content:"”";color:var(--brass2)}
.story p{color:var(--mute);margin-bottom:14px}
.story p b{color:var(--paper)}
.press{display:flex;gap:20px;flex-wrap:wrap;font-size:14px;margin-top:6px}
.press a{color:var(--brass2)}
h2{font-size:clamp(30px,3.4vw,46px);line-height:1.1;margin-bottom:16px}
.sub{color:var(--mute);max-width:640px;margin-bottom:40px}
.steps{counter-reset:s;display:grid;gap:0;border-top:1px solid var(--line)}
.st{display:grid;grid-template-columns:90px 1fr;gap:20px;padding:28px 0;border-bottom:1px solid var(--line)}
.st::before{counter-increment:s;content:counter(s,decimal-leading-zero);font-family:'Fraunces',Georgia,serif;font-size:40px;color:var(--brass);line-height:1}
.st h3{font-size:20px;margin-bottom:6px;font-family:'Instrument Sans',sans-serif}
.st p{color:var(--mute)}
.shot{border:1px solid var(--line);border-radius:6px;overflow:hidden;margin-top:36px;box-shadow:0 30px 70px rgb(0 0 0/35%)}
.shot figcaption{background:var(--bg2);font-size:13px;color:var(--mute);padding:10px 14px}
.fit{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.fit h3{font-size:18px;margin-bottom:12px;color:var(--brass2)}
.fit li{list-style:none;padding:8px 0;border-bottom:1px solid var(--line);color:var(--mute)}
.faq{max-width:780px}
.faq-i{border-bottom:1px solid var(--line)}
.faq-i p{color:var(--mute)}
#iscrizione{background:var(--bg2)}
#iscrizione .wrap{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.formbox{background:var(--paper);color:#1d2b2e;border-radius:6px;padding:34px 30px;box-shadow:0 30px 70px rgb(0 0 0/35%)}
.formbox h3{font-family:'Fraunces',Georgia,serif;font-size:28px;font-weight:500;margin-bottom:4px}
.formsub{color:#5d625c;font-size:14.5px;margin-bottom:18px}
.formnote{font-size:12.5px;color:#5d625c;text-align:center;margin-top:12px}
.wk-field{width:100%;font:inherit;font-size:16px;padding:14px;border:1px solid #cfc6b1;border-radius:4px;background:#fffdf7;color:#1d2b2e}
.wk-field:focus{outline:2px solid var(--brass);border-color:var(--brass)}
.wk-priv{color:#4d524c}.wk-priv a{color:#1d2b2e}
.wk-errore{background:#f7dedb;color:#8c1d14}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:#14262a;color:var(--paper);border:0;border-radius:4px;font:inherit;font-weight:700;font-size:16px;padding:16px 18px;cursor:pointer;text-decoration:none}
.btn-gold:hover{background:#0c1a1d}.btn-gold:disabled{opacity:.6}
.cd b{color:var(--paper);font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:34px}.cd span{color:var(--mute)}
.wk-modal .box{background:var(--paper);color:#1d2b2e}.wk-modal .box p{color:#4d524c}
.wk-modal .box>div:first-child{background:#e6d9b8!important;color:#14262a!important}
.wk-modal .btn-gold{background:#14262a}
.foot{text-align:center;font-size:12.5px;color:var(--mute);padding:30px 20px 40px}
.foot a{color:var(--mute)}
@media (max-width:900px){
 .hero{padding:44px 0 36px}.flow{grid-template-columns:1fr;gap:10px}.arrow{transform:rotate(90deg)}
 .story,#iscrizione .wrap,.fit{grid-template-columns:1fr;gap:28px}.story img{max-width:220px}
 section{padding:54px 0}.st{grid-template-columns:56px 1fr}.st::before{font-size:30px}.datechip{display:none}
}
'''

def C():
    body = f'''<header class="top"><div class="wrap"><div class="mark">Davide Caiazzo <small>workshop per commercialisti</small></div><div class="datechip">Giovedì 29 ottobre, ore 21:00, su Zoom</div></div></header>
<main>
<section class="hero"><div class="wrap">
<p class="kick">Workshop gratuito dal vivo, solo per commercialisti</p>
<h1>La fattura del fornitore estero arriva in PDF. <span class="b">Il gestionale vuole l'XML.</span></h1>
<p class="lead">Una scansione storta del fornitore tedesco, i dati copiati a mano, l'autofattura. Ogni mese. <b>Giovedì 29 ottobre alle 21 lo faccio davanti a te</b>, su Commercialista AI: carico il PDF, anche scansionato, ed esce il file da importare.</p>
<div class="flow" aria-hidden="true">
<div class="doc"><div class="h"><span>INVOICE · PDF</span><span>da registrare</span></div><dl><dt>Fornitore</dt><dd>Demo Cloud Services GmbH</dd><dt>Data</dt><dd>12/07/2026</dd><dt>Descrizione</dt><dd>Cloud hosting, monthly plan</dd><dt>Totale</dt><dd>49,00 €</dd><dt>Cliente</dt><dd>Bertoldi Costruzioni S.r.l.</dd></dl></div>
<div class="arrow">→</div>
<div class="xml"><div class="h">Pronto da importare nel gestionale</div><span class="t">&lt;TipoDocumento&gt;</span>TD17<span class="t">&lt;/TipoDocumento&gt;</span><br/><span class="t">&lt;Denominazione&gt;</span>Demo Cloud Services GmbH<span class="t">&lt;/Denominazione&gt;</span><br/><span class="t">&lt;Data&gt;</span>2026-07-12<span class="t">&lt;/Data&gt;</span><br/><span class="t">&lt;ImportoTotale&gt;</span>49.00<span class="t">&lt;/ImportoTotale&gt;</span><br/><span class="ok">✓ servizio da fornitore UE riconosciuto</span><br/><span class="ok">✓ dati controllati prima del file</span></div>
</div>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="byline"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="56" height="56"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
</div></section>
<div class="strip"><div class="wrap"><span><b>Più di 180</b> commercialisti iscritti all'edizione del 15 ottobre</span><span>Il gestionale <b>resta il tuo</b></span><span><b>Gratis</b>, su Zoom</span></div></div>

<section><div class="wrap story">
<img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="400" height="400" loading="lazy"/>
<div>
<blockquote>Ho bisogno di un consulente, non di una segretaria.</blockquote>
<p>Per anni ho pensato che il mio commercialista non fosse bravo. O che non fosse un consulente. Glielo dicevo, con queste parole. Costruendo Commercialista AI ho capito che mi sbagliavo: <b>non gli mancava la competenza. Gli mancava il tempo.</b></p>
<p>Sono Davide Caiazzo. Ho costruito My Governance e l'ho venduta al gruppo Zucchetti: «valutazione oltre 10 milioni», ha titolato Il Sole 24 Ore. Commercialista AI l'ho costruito e provato insieme a due studi commercialisti. Giovedì te lo mostro io, dal vivo.</p>
<div class="press">{STAMPA}</div>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<p class="sub">La verità è che non puoi fare tutto tu. In una sera ti mostro i lavori che il tuo studio può smettere di fare a mano, su uno studio di esempio: clienti di prova, programma vero.</p>
<div class="steps">
<div class="st"><div><h3>Dal PDF estero al file XML</h3><p>Carico la fattura del fornitore estero, anche una scansione. Il programma legge i dati, riconosce se sono beni o servizi e se l'acquisto è dall'Unione europea, e prepara l'XML da importare nel gestionale. Se manca un dato, te lo dice prima.</p></div></div>
<div class="st"><div><h3>Le autofatture in inversione contabile</h3><p>Dalle fatture d'acquisto in inversione contabile escono le autofatture, pronte da scaricare.</p></div></div>
<div class="st"><div><h3>Gli F24 a tutti i clienti, e sai chi ha ricevuto</h3><p>Il programma riconosce il cliente da ogni F24, prepara le email, sollecita chi non risponde. Tu controlli e premi Invia.</p></div></div>
<div class="st"><div><h3>Le tue domande, in diretta</h3><p>Rispondo io. Alla fine ti dico quanto costa e come si attiva. Nessun obbligo.</p></div></div>
</div>
<figure class="shot"><picture><source media="(max-width:700px)" srcset="img-ott/fatture-estere-telefono.webp"/><img src="img-ott/fatture-estere.webp" width="1440" height="860" loading="lazy" alt="La pagina Fatture estere e autofatture in XML di Commercialista AI"/></picture><figcaption>Fatture estere e autofatture in XML, studio dimostrativo di Commercialista AI.</figcaption></figure>
<p style="margin-top:22px;color:var(--mute);font-size:15px">In squadra con me Gianfranco Motta, il tecnico di DC Academy: tiene d'occhio la chat e mi porta le domande più tecniche.</p>
</div></section>

<section style="padding-top:0"><div class="wrap fit">
<div><h3>Fa per te se</h3><ul><li>hai clienti che comprano servizi o merce dall'estero</li><li>le giornate se ne vanno tra F24, documenti e scadenze</li><li>non hai competenze tecniche: non servono</li></ul></div>
<div><h3>Non fa per te se</h3><ul><li>cerchi un corso di teoria sull'intelligenza artificiale</li><li>vuoi solo la registrazione da guardare «prima o poi»</li></ul></div>
</div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:26px">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · solo per commercialisti')}
</div></section>
</main>'''
    return page('C', "Workshop gratuito per commercialisti: dalla fattura estera in PDF all'XML, dal vivo",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo Commercialista AI: fatture estere dal PDF all'XML, autofatture in inversione contabile, F24 ai clienti.",
      'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,500&family=Instrument+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400', C_CSS, body,
      "[CLAUDE] 2026-10-17 variante C (prova ott A/B/C/D): notte petrolio e ottone + gancio Fatture estere in XML + storia vera di Davide. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

# =============== D: salvia + evidenziatore, Scadenze e avvisi bonari ===============
D_CSS = '''
:root{--bg:#edf1e7;--paper:#fbfcf8;--ink:#1e2a21;--mute:#58655b;--green:#2f5d3a;--green2:#244a2e;--hi:#ffe066;--red:#b3261e;--line:#d3dccd}
body{background:var(--bg);color:var(--ink);font-family:'Public Sans',system-ui,sans-serif;font-size:17px;line-height:1.6}
h1,h2,.d{font-family:'Bricolage Grotesque',system-ui,sans-serif;letter-spacing:-.02em}
.top .wrap{display:flex;justify-content:space-between;align-items:center;padding-top:20px;padding-bottom:20px;gap:12px}
.brand{font-family:'Bricolage Grotesque',sans-serif;font-weight:700;font-size:18px}
.brand span{background:var(--hi);padding:0 4px}
.top a{font-weight:700;color:var(--green);text-decoration:none;font-size:15px}
.hero{padding:30px 0 60px}
.hero .wrap{display:grid;grid-template-columns:1.05fr 1fr;gap:50px;align-items:center}
.date{display:inline-block;border:2px solid var(--ink);border-radius:8px;padding:6px 12px;font-weight:700;font-size:15px;margin-bottom:22px;background:var(--paper)}
h1{font-size:clamp(36px,4.6vw,62px);font-weight:700;line-height:1.02;margin-bottom:22px}
h1 mark{background:linear-gradient(transparent 55%,var(--hi) 55%);color:inherit;padding:0 2px}
.lead{color:var(--mute);max-width:560px;margin-bottom:26px}
.lead b{color:var(--ink)}
.cta{display:inline-block;background:var(--green);color:#fff;text-decoration:none;font-weight:700;font-size:17px;padding:16px 28px;border-radius:12px;box-shadow:0 4px 0 var(--green2);transition:transform .1s}
.cta:active{transform:translateY(2px);box-shadow:0 2px 0 var(--green2)}
.host{display:flex;align-items:center;gap:12px;margin-top:24px}
.host img{width:50px;height:50px;border-radius:50%;object-fit:cover}
.host p{font-size:14.5px;color:var(--mute);line-height:1.4}.host b{color:var(--ink)}
.agenda-card{background:var(--paper);border:2px solid var(--ink);border-radius:14px;box-shadow:8px 8px 0 var(--ink);overflow:hidden}
.agenda-card .hd{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:2px solid var(--ink);font-weight:700}
.agenda-card .hd span{font-size:13px;font-weight:400;color:var(--mute)}
.row{display:grid;grid-template-columns:92px 1fr;gap:12px;padding:14px 18px;border-bottom:1px solid var(--line);font-size:15px;align-items:start}
.row:last-child{border-bottom:0}
.row .q{font-weight:700;font-size:13px;color:var(--green)}
.row .q.r{color:var(--red)}
.row b{display:block}
.row small{color:var(--mute);font-size:13.5px}
.row.hi{background:#fff8d1}
.note{font-size:13px;color:var(--mute);margin-top:12px}
.facts{background:var(--ink);color:#f3f6ef;padding:22px 0}
.facts .wrap{display:flex;justify-content:space-between;gap:14px 30px;flex-wrap:wrap;font-size:15px}
.facts b{color:var(--hi)}
section{padding:70px 0}
h2{font-size:clamp(30px,3.4vw,44px);font-weight:700;line-height:1.08;margin-bottom:14px}
.sub{color:var(--mute);max-width:640px;margin-bottom:36px}
.flow3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.f{background:var(--paper);border:2px solid var(--ink);border-radius:14px;padding:24px}
.f .k{display:inline-block;background:var(--hi);font-weight:700;font-size:13px;padding:2px 8px;border-radius:6px;margin-bottom:12px}
.f h3{font-family:'Bricolage Grotesque',sans-serif;font-size:21px;line-height:1.15;margin-bottom:8px}
.f p{color:var(--mute);font-size:15.5px}
.shot{margin-top:30px;border:2px solid var(--ink);border-radius:14px;overflow:hidden;background:var(--paper)}
.shot figcaption{padding:10px 14px;font-size:13px;color:var(--mute);border-top:1px solid var(--line)}
.list{max-width:860px;display:grid;gap:12px}
.li{display:grid;grid-template-columns:34px 1fr;gap:14px;padding:18px 0;border-bottom:2px dashed var(--line)}
.li .c{width:28px;height:28px;border:2px solid var(--ink);border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--green)}
.li h3{font-size:19px;margin-bottom:4px}
.li p{color:var(--mute);font-size:15.5px}
.who{display:grid;grid-template-columns:220px 1fr;gap:34px;align-items:center;background:var(--paper);border:2px solid var(--ink);border-radius:14px;padding:30px}
.who img{border-radius:10px;aspect-ratio:1;object-fit:cover}
.who h3{font-family:'Bricolage Grotesque',sans-serif;font-size:28px;margin-bottom:8px}
.who p{color:var(--mute);margin-bottom:12px}
.press{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;font-weight:700}
.press a{color:var(--green)}
.faq{max-width:760px}
.faq-i{border-bottom:2px solid var(--line)}
.faq-i p{color:var(--mute)}
#iscrizione .wrap{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.formbox{background:var(--paper);border:2px solid var(--ink);border-radius:14px;box-shadow:8px 8px 0 var(--green);padding:32px 28px}
.formbox h3{font-family:'Bricolage Grotesque',sans-serif;font-size:27px;margin-bottom:4px}
.formsub{color:var(--mute);font-size:14.5px;margin-bottom:18px}
.formnote{font-size:12.5px;color:var(--mute);text-align:center;margin-top:12px}
.wk-field{width:100%;font:inherit;font-size:16px;padding:14px;border:2px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}
.wk-field:focus{outline:none;border-color:var(--green)}
.wk-priv{color:var(--mute)}.wk-priv a{color:var(--green)}
.wk-errore{background:#fbe3e1;color:var(--red)}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:var(--green);color:#fff;border:0;border-radius:12px;font:inherit;font-weight:700;font-size:16px;padding:16px 18px;cursor:pointer;box-shadow:0 4px 0 var(--green2);text-decoration:none}
.btn-gold:disabled{opacity:.6}
.cd>div{background:var(--paper);border:2px solid var(--ink);border-radius:10px;padding:8px 4px}
.cd b{font-family:'Bricolage Grotesque',sans-serif;color:var(--ink)}.cd span{color:var(--mute)}
.wk-modal .box{background:var(--paper);color:var(--ink);border:2px solid var(--ink)}.wk-modal .box p{color:var(--mute)}
.wk-modal .box>div:first-child{background:var(--hi)!important;color:var(--ink)!important}
.foot{text-align:center;font-size:12.5px;color:var(--mute);padding:30px 20px 40px}
.foot a{color:var(--mute)}
@media (max-width:900px){
 .hero .wrap,#iscrizione .wrap{grid-template-columns:1fr;gap:30px}.flow3{grid-template-columns:1fr}
 .who{grid-template-columns:1fr;padding:22px}.who img{max-width:180px}section{padding:50px 0}
 .agenda-card{box-shadow:5px 5px 0 var(--ink)}.row{grid-template-columns:78px 1fr}
}
'''

def D():
    body = f'''<header class="top"><div class="wrap"><div class="brand">Workshop <span>commercialisti</span></div><a href="#iscrizione">Iscriviti gratis</a></div></header>
<main>
<section class="hero"><div class="wrap">
<div>
<p class="date">Giovedì 29 ottobre, ore 21:00 · gratis su Zoom</p>
<h1>Un avviso bonario nella PEC. Un F24 da mandare. <mark>Niente ti scappa più.</mark></h1>
<p class="lead">Giovedì 29 ottobre ti faccio vedere dal vivo come Commercialista AI <b>trova le scadenze in documenti e posta</b>, legge l'avviso bonario, calcola la scadenza e ti avvisa prima. Tu confermi. Il gestionale resta il tuo.</p>
<a class="cta" href="#iscrizione">Riserva il posto gratis</a>
<div class="host"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="50" height="50"/><p><b>Conduce Davide Caiazzo</b><br/>ha venduto la sua azienda al gruppo Zucchetti</p></div>
</div>
<div>
<div class="agenda-card" role="img" aria-label="Esempio di elenco scadenze dello studio in Commercialista AI">
<div class="hd">Scadenze dello studio <span>studio dimostrativo</span></div>
<div class="row hi"><span class="q r">Scaduta 13/10</span><div><b>Bertoldi Costruzioni S.r.l.</b><small>F24 settembre 2026 · 415,00 € · sollecito pronto</small></div></div>
<div class="row"><span class="q">Avviso bonario</span><div><b>Farmacia Sant'Anna S.n.c.</b><small>scadenza calcolata dal programma · due promemoria · F24 pronto</small></div></div>
<div class="row"><span class="q">Da mandare</span><div><b>Autofficina Gallo</b><small>F24 agosto 2026 · 615,00 € · scade il 25 ottobre</small></div></div>
<div class="row"><span class="q">Da mandare</span><div><b>Rossi Impianti S.r.l.</b><small>F24 agosto 2026 · 7.415,20 € · scade il 25 ottobre</small></div></div>
</div>
<p class="note">Clienti di prova, programma vero: lo vedi all'opera giovedì.</p>
</div>
</div></section>
<div class="facts"><div class="wrap"><span><b>Più di 180</b> commercialisti iscritti all'edizione del 15 ottobre</span><span>Si guarda e si fanno domande: <b>zero tecnica</b></span><span>Niente parte senza <b>il tuo sì</b></span></div></div>

<section><div class="wrap">
<h2>Il cliente ti inoltra l'avviso bonario tre settimane dopo.</h2>
<p class="sub">Il programma lo legge, cerca la data di notifica nella conversazione, calcola la scadenza vera con la sospensione feriale e la mette in agenda. Il rischio vero non è sbagliare un calcolo: è dimenticare una scadenza tra le centinaia che lo studio tiene d'occhio.</p>
<div class="flow3">
<div class="f"><span class="k">arriva</span><h3>L'avviso bonario nella posta</h3><p>Il programma lo legge dalla casella dello studio o dal documento caricato.</p></div>
<div class="f"><span class="k">si calcola</span><h3>La scadenza giusta</h3><p>Calcola la scadenza, anche con la sospensione feriale, e la mette in calendario sul cliente giusto.</p></div>
<div class="f"><span class="k">ti avvisa</span><h3>Due promemoria e l'F24 pronto</h3><p>Prima che scada ricevi i promemoria. Tu controlli e confermi.</p></div>
</div>
<figure class="shot"><picture><source media="(max-width:700px)" srcset="img-ott/scadenze-telefono.webp"/><img src="img-ott/scadenze.webp" width="1440" height="860" loading="lazy" alt="La pagina Scadenze di Commercialista AI con le scadenze da fare"/></picture><figcaption>Scadenze in Commercialista AI, studio dimostrativo.</figcaption></figure>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2>Cosa vedi dal vivo</h2>
<p class="sub">Un caso intero su uno studio di esempio, dall'inizio alla fine.</p>
<div class="list">
<div class="li"><div class="c">✓</div><div><h3>Scadenze trovate in documenti e posta</h3><p>Un elenco di scadenze in Excel o PDF, un avviso bonario, una email: finiscono in calendario cliente per cliente.</p></div></div>
<div class="li"><div class="c">✓</div><div><h3>Gli F24 a tutti i clienti, e sai chi ha ricevuto</h3><p>Il programma riconosce il cliente da ogni F24, prepara le email e sollecita chi non risponde. Tu premi Invia.</p></div></div>
<div class="li"><div class="c">✓</div><div><h3>I documenti del 730 chiesti da soli</h3><p>A ogni persona fisica parte l'elenco dei documenti, con un link per mandarli in foto, e i promemoria a chi non ha finito.</p></div></div>
<div class="li"><div class="c">✓</div><div><h3>Le tue domande, in diretta</h3><p>Rispondo io. Alla fine ti dico quanto costa e come si attiva. Nessun obbligo.</p></div></div>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<div class="who"><img src="davide-linkedin.jpg" alt="Davide Caiazzo" width="220" height="220" loading="lazy"/><div>
<h3>Conduco io, Davide Caiazzo</h3>
<p>Ho costruito My Governance, un software per le aziende, e l'ho venduta al gruppo Zucchetti: «valutazione oltre 10 milioni», ha titolato Il Sole 24 Ore. Sono TOP 20 al mondo in “LinkedIn® Growth” secondo Favikon 2025. Commercialista AI l'ho costruito e provato insieme a due studi commercialisti.</p>
<div class="press">{STAMPA}</div>
<p style="margin-top:14px;font-size:15px">In squadra con me Gianfranco Motta, il tecnico di DC Academy: tiene d'occhio la chat e mi porta le domande più tecniche.</p>
</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap"><h2>Domande frequenti</h2><div class="faq">{faq_html()}</div></div></section>

<section id="iscrizione"><div class="wrap">
<div><h2>Giovedì 29 ottobre, ore 21:00</h2><p class="sub" style="margin-bottom:24px">Ti iscrivi in trenta secondi. Ricevi subito l'email di conferma e, prima della diretta, il link Zoom.</p>{COUNTDOWN}</div>
{form_block('', 'Riserva il tuo posto gratis', 'Live su Zoom · solo per commercialisti')}
</div></section>
</main>'''
    return page('D', "Workshop gratuito per commercialisti: scadenze e avvisi bonari che non scappano più",
      "Workshop live gratuito su Zoom per commercialisti, giovedì 29 ottobre alle 21:00. Davide Caiazzo mostra dal vivo Commercialista AI: scadenze trovate in documenti e posta, avvisi bonari letti, promemoria e F24 pronti.",
      'family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Public+Sans:wght@400;600;700', D_CSS, body,
      "[CLAUDE] 2026-10-17 variante D (prova ott A/B/C/D): carta salvia ed evidenziatore + gancio Scadenze e avvisi bonari. Modulo e tracciamento copiati da workshop.html. Ipotesi: Projects/Tool-Commercialisti/consegne-a-sviluppi/workshop-pagine-ott-20261017/ipotesi.md")

for v, fn in (('b', B), ('c', C), ('d', D)):
    out = os.path.join(REPO, 'workshop-ott-%s.html' % v)
    open(out, 'w').write(fn())
    print('scritto', out)
