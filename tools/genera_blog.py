#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generatore blog statico per commercialisti.davidecaiazzo.it/blog
Repo: ceo743/guida-commercialisti-ai (GitHub Pages, nessun CMS)
Uso: build_article(dati) -> scrive /blog/<slug>/index.html
     build_listing(posts) -> scrive /blog/index.html
     aggiorna sitemap.xml
Tutti gli articoli DEVONO passare da qui: garantisce title<=60, meta<=160,
canonical, OG, JSON-LD Article + FAQPage + Breadcrumb, stesso brand del sito.
"""
import json, re, html, os

BASE_URL = "https://commercialisti.davidecaiazzo.it"
ORG = {
    "name": "DC Academy S.r.l.",
    "url": "https://www.davidecaiazzo.it",
    "logo": "https://automazioni.davidecaiazzo.it/favicon.png",
}

HEAD_CSS = """
:root{--gold:#ff3d2e;--gold2:#c62d20;--bg:#05070e;--bg2:#0c0f1a;--line:rgba(255,255,255,.08);--txt:#fff;--txt-dim:rgba(255,255,255,.62);--txt-faint:rgba(255,255,255,.35)}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);overflow-x:hidden;line-height:1.65}
a{color:var(--gold)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.blog-hdr{border-bottom:1px solid var(--line);padding:18px 0}
.blog-hdr .wrap{display:flex;align-items:center;justify-content:space-between;max-width:1040px}
.logo{font-family:'Playfair Display',serif;font-weight:800;font-size:17px;letter-spacing:.06em;color:#fff;text-decoration:none;text-transform:uppercase}
.back{font-size:13px;color:var(--txt-dim);text-decoration:none}
.back:hover{color:#fff}
.disclaimer{text-align:center;padding:8px 16px;font-size:10.5px;color:var(--txt-faint);letter-spacing:.3px;line-height:1.5;background:rgba(255,255,255,.02);border-bottom:1px solid var(--line)}
main{padding:48px 0 80px}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
h1.art-title{font-family:'Playfair Display',serif;font-weight:800;font-size:clamp(28px,4.2vw,44px);line-height:1.12;letter-spacing:-.01em;margin:10px 0 14px}
.meta-line{font-size:13px;color:var(--txt-faint);margin-bottom:28px}
.cover{width:100%;border-radius:10px;margin:0 0 34px;display:block;aspect-ratio:16/9;object-fit:cover;background:#111}
.direct-answer{font-size:17px;color:var(--txt-dim);border-left:3px solid var(--gold);padding:4px 0 4px 18px;margin:0 0 34px}
article h2{font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(21px,2.6vw,28px);margin:40px 0 14px;letter-spacing:-.005em}
article h3{font-size:18px;font-weight:700;margin:26px 0 10px}
article p{font-size:16px;color:var(--txt-dim);margin:0 0 16px}
article ul{margin:0 0 20px;padding-left:20px}
article li{font-size:16px;color:var(--txt-dim);margin-bottom:10px}
article strong{color:#fff}
.stat-band{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:30px 0;padding:22px;background:var(--bg2);border:1px solid var(--line);border-radius:10px}
.stat-num{font-family:'Playfair Display',serif;font-weight:800;font-size:28px;color:var(--gold)}
.stat-label{font-size:12.5px;color:var(--txt-faint);margin-top:4px}
.cta-box{text-align:center;margin:44px 0;padding:34px 24px;background:var(--bg2);border:1px solid var(--line);border-radius:14px}
.btn-gold{display:inline-flex;align-items:center;gap:10px;padding:16px 36px;background:linear-gradient(135deg,var(--gold2),var(--gold));color:#000;font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:2px;border:none;border-radius:60px;text-decoration:none;box-shadow:0 4px 30px rgba(255,61,46,.2)}
.cta-note{font-size:13px;color:var(--txt-faint);margin-top:14px}
.related{margin:50px 0 0;padding-top:30px;border-top:1px solid var(--line)}
.related h3{font-family:'Playfair Display',serif;font-size:18px;margin:0 0 16px}
.related ul{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.related a{color:var(--txt-dim);text-decoration:none;font-size:15px}
.related a:hover{color:var(--gold)}
footer.blog-ftr{border-top:1px solid var(--line);padding:30px 32px 40px;text-align:center}
footer.blog-ftr p{font-size:12px;color:var(--txt-faint);line-height:1.8}
footer.blog-ftr a{color:rgba(255,255,255,.4);text-decoration:underline}
.listing-grid{display:grid;gap:22px;margin-top:34px}
.card{display:block;text-decoration:none;color:inherit;background:var(--bg2);border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:border-color .2s}
.card:hover{border-color:var(--gold)}
.card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.card-body{padding:18px 20px 22px}
.card-cat{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.card h2{font-family:'Playfair Display',serif;font-size:19px;font-weight:700;margin:8px 0 6px;line-height:1.3}
.card p{font-size:14px;color:var(--txt-faint);margin:0}
.empty{color:var(--txt-faint);font-size:15px;margin-top:30px}
"""

HEAD_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700&display=swap" rel="stylesheet"/>
<link rel="icon" type="image/png" href="https://automazioni.davidecaiazzo.it/favicon.png"/>"""

HEADER_HTML = """<div class="disclaimer"><strong>I contenuti di questo blog hanno natura pubblicitaria</strong> a favore della DC Academy S.r.l. &middot; Approfondimenti su <a href="https://www.davidecaiazzo.it/trasparenza" target="_blank" rel="noopener">www.davidecaiazzo.it/trasparenza</a></div>
<header class="blog-hdr"><div class="wrap">
<a href="/" class="logo">Commercialista AI</a>
<a href="/blog/" class="back">&larr; Tutti gli articoli</a>
</div></header>"""

FOOTER_HTML = """<footer class="blog-ftr">
<p>DC Academy S.r.l. | P.IVA 05125350750 | Via I. Adriano 9, Lecce | academy@davidecaiazzo.it<br/>
<a href="https://docs.google.com/document/d/1qUNgRcZ0W9aZxutDu1Fv2k5aM6Nti4V0/edit" target="_blank" rel="noopener">Privacy</a> &middot;
<a href="https://docs.google.com/document/d/1PTTs2QFMqBtZaefLHPrrfMxJRnlGewih/edit" target="_blank" rel="noopener">Cookie</a> &middot;
<a href="https://docs.google.com/document/d/1K6WGjt9aFTRN-zWMvEOh5bw2A32nNag-/edit" target="_blank" rel="noopener">Condizioni di Vendita</a></p>
</footer>"""


def esc(s):
    return html.escape(s, quote=True)


def build_faq_jsonld(faq_items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faq_items
        ],
    }


def build_article_jsonld(d):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": d["title"],
        "description": d["meta_description"],
        "image": d["cover_url"],
        "datePublished": d["date_iso"],
        "dateModified": d["date_iso"],
        "author": {"@type": "Organization", "name": ORG["name"], "url": ORG["url"]},
        "publisher": {
            "@type": "Organization",
            "name": ORG["name"],
            "logo": {"@type": "ImageObject", "url": ORG["logo"]},
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{BASE_URL}/blog/{d['slug']}/"},
    }


def build_breadcrumb_jsonld(d):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Blog", "item": f"{BASE_URL}/blog/"},
            {"@type": "ListItem", "position": 2, "name": d["title"], "item": f"{BASE_URL}/blog/{d['slug']}/"},
        ],
    }


def build_article(d):
    """
    d = {
      slug, title, page_title, meta_description, category_label,
      cover_url, cover_alt, date_iso, date_human, direct_answer,
      stats: [(num,label)...] or None,
      body_html: str (h2/p/ul già pronti, NO h2 finali con '?': quelli vanno in faq),
      faq: [(domanda, risposta_html_plain_text)...],
      related: [(slug_o_url_assoluto, titolo)...]  (max 4)
      cta_url, cta_note
    }
    """
    assert len(d["page_title"]) <= 60, f"page_title troppo lungo ({len(d['page_title'])}): {d['page_title']}"
    assert len(d["meta_description"]) <= 160, f"meta_description troppo lunga ({len(d['meta_description'])})"

    faq_html_blocks = []
    faq_plain = []
    for q, a in d["faq"]:
        faq_html_blocks.append(f"<h2>{esc(q)}</h2>\n<p>{a}</p>")
        plain_a = re.sub("<[^>]+>", "", a)
        faq_plain.append((q, plain_a))
    faq_html = "\n".join(faq_html_blocks)

    stats_html = ""
    if d.get("stats"):
        cells = "".join(
            f'<div><div class="stat-num">{esc(n)}</div><div class="stat-label">{esc(l)}</div></div>'
            for n, l in d["stats"]
        )
        stats_html = f'<div class="stat-band">{cells}</div>'

    related_items = d.get("related", [])[:4]
    related_html = ""
    if related_items:
        lis = "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for u, t in related_items)
        related_html = f'<div class="related"><h3>Articoli correlati</h3><ul>{lis}</ul></div>'

    jsonld_article = json.dumps(build_article_jsonld(d), ensure_ascii=False)
    jsonld_faq = json.dumps(build_faq_jsonld(faq_plain), ensure_ascii=False)
    jsonld_breadcrumb = json.dumps(build_breadcrumb_jsonld(d), ensure_ascii=False)

    page_url = f"{BASE_URL}/blog/{d['slug']}/"

    html_out = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{esc(d['page_title'])}</title>
<meta name="description" content="{esc(d['meta_description'])}"/>
<link rel="canonical" href="{page_url}"/>
{HEAD_LINKS}
<meta property="og:type" content="article"/>
<meta property="og:title" content="{esc(d['page_title'])}"/>
<meta property="og:description" content="{esc(d['meta_description'])}"/>
<meta property="og:image" content="{esc(d['cover_url'])}"/>
<meta property="og:url" content="{page_url}"/>
<meta property="og:site_name" content="Commercialista AI"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{esc(d['page_title'])}"/>
<meta name="twitter:description" content="{esc(d['meta_description'])}"/>
<meta name="twitter:image" content="{esc(d['cover_url'])}"/>
<script type="application/ld+json">{jsonld_article}</script>
<script type="application/ld+json">{jsonld_faq}</script>
<script type="application/ld+json">{jsonld_breadcrumb}</script>
<style>{HEAD_CSS}</style>
</head>
<body>
{HEADER_HTML}
<main class="wrap">
<article>
<div class="eyebrow">{esc(d['category_label'])}</div>
<h1 class="art-title">{esc(d['title'])}</h1>
<div class="meta-line">Commercialista AI &middot; {esc(d['date_human'])}</div>
<img class="cover" src="{esc(d['cover_url'])}" alt="{esc(d['cover_alt'])}"/>
<p class="direct-answer">{d['direct_answer']}</p>
{stats_html}
{d['body_html']}
{faq_html}
<div class="cta-box">
<a class="btn-gold" href="{esc(d['cta_url'])}">GUARDA COME FUNZIONA</a>
<p class="cta-note">{d['cta_note']}</p>
</div>
{related_html}
</article>
</main>
{FOOTER_HTML}
</body>
</html>
"""
    return html_out


def build_listing(posts):
    """posts = [{slug,title,excerpt,cover_url,cover_alt,category_label,date_human}], newest first"""
    if posts:
        cards = "\n".join(
            f"""<a class="card" href="/blog/{p['slug']}/">
<img src="{esc(p['cover_url'])}" alt="{esc(p['cover_alt'])}" loading="lazy"/>
<div class="card-body">
<div class="card-cat">{esc(p['category_label'])}</div>
<h2>{esc(p['title'])}</h2>
<p>{esc(p['excerpt'])}</p>
</div>
</a>"""
            for p in posts
        )
        grid = f'<div class="listing-grid">{cards}</div>'
    else:
        grid = '<p class="empty">Primi articoli in arrivo.</p>'

    jsonld_blog = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": "Commercialista AI — Blog",
            "url": f"{BASE_URL}/blog/",
            "publisher": {"@type": "Organization", "name": ORG["name"], "url": ORG["url"]},
        },
        ensure_ascii=False,
    )

    title = "Blog Commercialista AI: guide e novità per lo studio"
    desc = "Articoli su intelligenza artificiale, F24, scadenze e automazioni per commercialisti. Guide tecniche e novità di settore da Commercialista AI."

    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}"/>
<link rel="canonical" href="{BASE_URL}/blog/"/>
{HEAD_LINKS}
<meta property="og:type" content="website"/>
<meta property="og:title" content="{esc(title)}"/>
<meta property="og:description" content="{esc(desc)}"/>
<meta property="og:url" content="{BASE_URL}/blog/"/>
<script type="application/ld+json">{jsonld_blog}</script>
<style>{HEAD_CSS}</style>
</head>
<body>
{HEADER_HTML}
<main class="wrap" style="max-width:1040px">
<div class="eyebrow">Blog</div>
<h1 class="art-title">Guide e novità per lo studio</h1>
{grid}
</main>
{FOOTER_HTML}
</body>
</html>
"""


def update_sitemap(existing_xml, new_urls):
    """new_urls = list of absolute urls to ensure are present"""
    urls = re.findall(r"<loc>(.*?)</loc>", existing_xml)
    for u in new_urls:
        if u not in urls:
            urls.append(u)
    body = "\n".join(f"<url><loc>{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'
