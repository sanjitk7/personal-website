"""Generates the three redesign mockups from content.py. Run: python3 mockups/build.py"""
import html, pathlib
from content import *
OUT = pathlib.Path(__file__).resolve().parent
e = html.escape

def page(title_suffix, fonts, css, body, js=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  {seo_head()}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
  <style>{css}</style>
</head>
<body>
{body}
{f'<script>{js}</script>' if js else ''}
</body>
</html>
"""

def ext(url):
    return '' if url.startswith(('mailto:', '../', '#')) else ' target="_blank" rel="noopener"'

# ---------------------------------------------------------------- A: Quiet
CSS_A = r"""
:root{--bg:#fbfaf7;--ink:#1c1b19;--muted:#6f6b63;--line:#e7e3da;--accent:#2b59c3;--chip:#f1eee7}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--ink:#ecebe6;--muted:#9a968c;--line:#2a2926;--accent:#8fb0ff;--chip:#1f1e1c}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 "Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:640px;margin:0 auto;padding:72px 24px 96px}
a{color:inherit;text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px;text-decoration-thickness:1px;transition:text-decoration-color .2s}
a:hover{text-decoration-color:var(--accent)}
header{display:flex;gap:20px;align-items:center;margin-bottom:28px}
header img{width:64px;height:64px;border-radius:50%;object-fit:cover;flex:none}
h1{font:500 30px/1.15 "Newsreader",Georgia,serif;letter-spacing:-.01em;margin:0}
.role{color:var(--muted);margin:2px 0 0;font-size:15px}
.intro p{margin:0 0 14px}
.links{display:flex;flex-wrap:wrap;gap:6px 18px;margin:22px 0 0;padding:0;list-style:none;font-size:15px}
.links a{text-decoration:none;color:var(--muted)}.links a:hover{color:var(--accent)}
section{margin-top:64px}
h2{font:500 13px/1 "Inter",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 20px}
.row{display:grid;grid-template-columns:72px 1fr;gap:4px 20px;padding:16px 0;border-top:1px solid var(--line)}
.row:last-child{border-bottom:1px solid var(--line)}
.yr{color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums;padding-top:2px}
.t{font-weight:500}.t .at{color:var(--muted);font-weight:400}
.d{grid-column:2;color:var(--muted);font-size:15px;margin:2px 0 0}
.metric{display:inline-block;font-size:13px;background:var(--chip);border-radius:4px;padding:1px 7px;margin-top:6px;color:var(--ink)}
details{grid-column:2}summary{cursor:pointer;list-style:none;color:var(--muted);font-size:14px;margin-top:4px}
summary::-webkit-details-marker{display:none}summary::before{content:"+ ";}details[open] summary::before{content:"– "}
details p{margin:6px 0 0;font-size:15px;color:var(--muted)}
.photo{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px;border:1px solid var(--line);border-radius:10px;text-decoration:none}
.photo:hover{border-color:var(--accent)}.photo span{color:var(--muted);font-size:15px}
footer{margin-top:72px;color:var(--muted);font-size:13px}
@media (max-width:520px){main{padding:40px 16px 64px}.row{grid-template-columns:1fr}.d,details{grid-column:1}.yr{order:-1}h1{font-size:26px}}
"""

def build_a():
    exp = "".join(f"""
    <div class="row"><div class="yr">{x['start']}</div>
      <div class="t">{e(x['role'])} <span class="at">· <a href="{x['url']}"{ext(x['url'])}>{e(x['org'])}</a></span></div>
      <p class="d">{e(x['summary'])}{f'<br><span class="metric">{e(x["metric"])}</span>' if x['metric'] else ''}</p></div>""" for x in EXPERIENCE)
    proj = "".join(f"""
    <div class="row"><div class="yr">{e(p['short'])}</div>
      <div class="t"><a href="{p['url']}"{ext(p['url'])}>{e(p['name'])}</a></div>
      <p class="d">{e(p['line'])}</p>
      <details><summary>More</summary><p>{e(p['more'])}</p></details></div>""" for p in PROJECTS)
    links = "".join(f'<li><a href="{u}"{ext(u)}>{n}</a></li>' for n, u in LINKS)
    body = f"""<main>
  <header><img src="../images/sanjit-profile-pic-circle.jpeg" alt="Sanjit Kumar, software engineer at Amazon" width="64" height="64">
    <div><h1>Sanjit Kumar</h1><p class="role">Software engineer · Amazon Music · Seattle</p></div></header>
  <div class="intro"><p>{e(INTRO)}</p><p>{e(OUTSIDE)}</p></div>
  <ul class="links">{links}</ul>
  <section><h2>Experience</h2>{exp}</section>
  <section><h2>Selected work</h2>{proj}</section>
  <section><h2>Writing</h2>
    <div class="row"><div class="yr">2021</div><div class="t"><a href="{PUBLICATION['url']}" target="_blank" rel="noopener">{e(PUBLICATION['title'])}</a></div><p class="d">{PUBLICATION['venue']}</p></div></section>
  <section><h2>Photography</h2>
    <a class="photo" href="{VSCO}" target="_blank" rel="noopener"><div><b>Through the lens</b><br><span>Street, coffee shops and long rides, on VSCO.</span></div><span>→</span></a></section>
  <footer>© 2026 Sanjit Kumar</footer>
</main>"""
    return page("Quiet", "family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,500", CSS_A, body)

# ---------------------------------------------------------------- B: Cards
CSS_B = r"""
:root{--bg:#ffffff;--surface:#f5f5f4;--ink:#0c0c0d;--muted:#5f6368;--line:#e8e8e6;--accent:#ff5a1f}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 32px}
nav{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.82);backdrop-filter:saturate(180%) blur(14px);-webkit-backdrop-filter:saturate(180%) blur(14px);border-bottom:1px solid transparent}
nav .wrap{display:flex;justify-content:space-between;align-items:center;height:60px}
.brand{font-weight:600;letter-spacing:-.01em}
nav ul{display:flex;gap:28px;list-style:none;margin:0;padding:0;font-size:14px;color:var(--muted)}nav ul a:hover{color:var(--ink)}
.cta{background:var(--ink);color:#fff;border-radius:999px;padding:8px 16px;font-size:14px;font-weight:500}
.hero{display:grid;grid-template-columns:1.4fr 1fr;gap:56px;align-items:center;padding:88px 0 96px}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);background:var(--surface);border-radius:999px;padding:5px 12px 5px 8px}
.eyebrow i{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px #22c55e33}
h1{font-size:clamp(44px,6.4vw,76px);line-height:1;letter-spacing:-.04em;font-weight:600;margin:20px 0 14px}
.sub{font-size:clamp(22px,2.6vw,30px);line-height:1.25;letter-spacing:-.02em;font-weight:500;margin:0 0 18px;max-width:560px}
.lede{font-size:18px;color:var(--muted);max-width:520px;margin:0 0 28px}
.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{border:1px solid var(--line);border-radius:999px;padding:10px 18px;font-size:14px;font-weight:500;transition:border-color .2s,background .2s}
.btn:hover{border-color:var(--ink)}.btn.primary{background:var(--ink);color:#fff;border-color:var(--ink)}
.portrait{aspect-ratio:1/1;border-radius:50%;overflow:hidden;background:var(--surface);max-width:400px;justify-self:end;width:100%}
.portrait img{width:100%;height:100%;object-fit:cover;display:block}
section{padding:72px 0;border-top:1px solid var(--line)}
.sh{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin-bottom:32px}
h2{font-size:28px;letter-spacing:-.02em;font-weight:600;margin:0}.sh p{margin:0;color:var(--muted);font-size:15px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:var(--surface);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;transition:transform .25s ease}
.card:hover{transform:translateY(-4px)}
.card .img{aspect-ratio:16/10;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;border-bottom:1px solid var(--line)}
.card .img img{width:100%;height:100%;object-fit:cover}
.card .c{padding:20px 22px 24px}.tag{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.card h3{font-size:19px;letter-spacing:-.01em;margin:6px 0 8px}.card p{margin:0;color:var(--muted);font-size:15px}
.list{margin-top:28px;border-top:1px solid var(--line)}
.li{display:grid;grid-template-columns:220px 1fr auto;gap:24px;align-items:baseline;padding:18px 4px;border-bottom:1px solid var(--line);transition:background .2s}
.li:hover{background:var(--surface)}.li b{font-weight:600}.li span{color:var(--muted);font-size:15px}.li em{font-style:normal;color:var(--muted);font-size:13px}
.exp{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.job{border:1px solid var(--line);border-radius:20px;padding:24px;display:flex;gap:16px}
.job img{width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;border:1px solid var(--line);flex:none}
.job h3{font-size:17px;margin:0}.job .m{color:var(--muted);font-size:14px;margin:2px 0 10px}.job p{margin:0;font-size:15px;color:var(--muted)}
.pill{display:inline-block;margin-top:12px;font-size:13px;font-weight:500;color:var(--accent);background:#ff5a1f14;border-radius:999px;padding:3px 10px}
.photo{border-radius:28px;background:#111;color:#fff;padding:56px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:end;
  background-image:radial-gradient(120% 140% at 100% 0%,#3a2a20 0%,#111 55%)}
.photo h2{font-size:clamp(28px,4vw,44px);letter-spacing:-.03em}.photo p{color:#bbb;margin:10px 0 0;max-width:460px}
.photo .btn{border-color:#444;color:#fff}.photo .btn:hover{border-color:#fff}
footer{padding:72px 0 56px;border-top:1px solid var(--line)}
footer h2{font-size:clamp(28px,4.4vw,48px);letter-spacing:-.03em;line-height:1.1;margin-bottom:24px}
.fine{color:var(--muted);font-size:13px;margin-top:48px}
@media (max-width:860px){.hero{grid-template-columns:1fr;gap:36px;padding:48px 0 64px}.portrait{max-width:112px;justify-self:start;order:-1}
 .grid,.exp{grid-template-columns:1fr}.li{grid-template-columns:1fr;gap:2px}nav ul{display:none}}
@media (max-width:520px){.sh p{display:none}.wrap{padding:0 16px}section{padding:56px 0}.photo{padding:32px 24px;grid-template-columns:1fr}.job{flex-direction:column}}
"""

def build_b():
    feat = [p for p in PROJECTS if p['featured']]; rest = [p for p in PROJECTS if not p['featured']]
    cards = "".join(f"""<a class="card" href="{p['url']}"{ext(p['url'])}><div class="img"><img src="../images/{p['img']}" alt="{e(p['name'])}" loading="lazy"></div>
      <div class="c"><div class="tag">{e(p['tag'])}</div><h3>{e(p['name'])}</h3><p>{e(p['line'])}</p></div></a>""" for p in feat)
    lis = "".join(f"""<a class="li" href="{p['url']}"{ext(p['url'])}><b>{e(p['name'])}</b><span>{e(p['line'])}</span><em>{' · '.join(p['stack'])} ↗</em></a>""" for p in rest)
    jobs = "".join(f"""<div class="job"><img src="../images/{x['logo']}" alt="{e(x['org'])} logo" loading="lazy">
      <div><h3>{e(x['role'])}</h3><div class="m"><a href="{x['url']}"{ext(x['url'])}>{e(x['org'])}</a> · {x['dates']}</div><p>{e(x['summary'])}</p>
      {f'<span class="pill">{e(x["metric"])}</span>' if x['metric'] else ''}</div></div>""" for x in EXPERIENCE)
    body = f"""<nav><div class="wrap"><a class="brand" href="#">Sanjit Kumar</a>
  <ul><li><a href="#work">Work</a></li><li><a href="#experience">Experience</a></li><li><a href="#photography">Photography</a></li></ul>
  <a class="cta" href="mailto:sanjitk2018@gmail.com">Get in touch</a></div></nav>
<main class="wrap">
  <div class="hero"><div>
    <span class="eyebrow"><i></i>Software engineer at Amazon Music</span>
    <h1>Sanjit Kumar</h1><p class="sub">Software engineer working on subscription growth at Amazon Music.</p>
    <p class="lede">M.S. in Computer Science from UIUC. Into full stack and distributed systems. {e(OUTSIDE)}</p>
    <div class="btns"><a class="btn primary" href="../data/SanjitKumarResume_FullStack.pdf">Resume</a>
      <a class="btn" href="https://github.com/sanjitk7/" target="_blank" rel="noopener">GitHub</a>
      <a class="btn" href="https://www.linkedin.com/in/sanjitk7/" target="_blank" rel="noopener">LinkedIn</a></div></div>
    <div class="portrait"><img src="../images/sanjit-profile-pic-circle.jpeg" alt="Sanjit Kumar, software engineer at Amazon" width="400" height="400"></div></div>
  <section id="work"><div class="sh"><h2>Selected work</h2><p>Systems, kernels, graphics.</p></div>
    <div class="grid">{cards}</div><div class="list">{lis}</div></section>
  <section id="experience"><div class="sh"><h2>Experience</h2><p>M.S. CS, UIUC</p></div><div class="exp">{jobs}</div></section>
  <section id="photography"><a class="photo" href="{VSCO}" target="_blank" rel="noopener"><div><h2>Photography</h2>
    <p>When I'm not shipping code I'm usually out with a camera. A running gallery lives on VSCO.</p></div><span class="btn">Open gallery ↗</span></a></section>
  <footer><h2>Let's build something.<br><span style="color:var(--muted)">sanjitk2018@gmail.com</span></h2>
    <div class="btns"><a class="btn primary" href="mailto:sanjitk2018@gmail.com">Email me</a><a class="btn" href="{PUBLICATION['url']}" target="_blank" rel="noopener">IoT security survey (AIMV 2021) ↗</a></div>
    <p class="fine">© 2026 Sanjit Kumar · Seattle, WA</p></footer>
</main>"""
    return page("Cards", "family=Inter:wght@400;500;600;700", CSS_B, body)

# ---------------------------------------------------------------- C: Split (dark)
CSS_C = r"""
:root{--bg:#0b0d10;--panel:#12151a;--ink:#e6e8eb;--muted:#8b929c;--dim:#5b616a;--line:#1e232a;--accent:#7dd3c0}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--muted);font:16px/1.65 "Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(600px circle at var(--mx,20%) var(--my,10%),rgba(125,211,192,.06),transparent 60%)}
a{color:var(--ink);text-decoration:none}a:hover{color:var(--accent)}
.shell{max-width:1180px;margin:0 auto;padding:0 48px;display:grid;grid-template-columns:5fr 7fr;gap:64px}
aside{position:sticky;top:0;height:100vh;padding:96px 0 56px;display:flex;flex-direction:column;justify-content:space-between}
h1{color:var(--ink);font-size:44px;line-height:1.05;letter-spacing:-.03em;font-weight:600;margin:0}
.title{color:var(--ink);font-size:18px;margin:10px 0 14px;font-weight:500}.blurb{max-width:340px;margin:0}
.toc{list-style:none;padding:0;margin:56px 0 0;font:500 12px/1 "JetBrains Mono",monospace;letter-spacing:.12em;text-transform:uppercase}
.toc a{display:flex;align-items:center;gap:14px;padding:10px 0;color:var(--dim)}
.toc a::before{content:"";width:32px;height:1px;background:var(--dim);transition:all .25s}
.toc a:hover,.toc a.on{color:var(--ink)}.toc a:hover::before,.toc a.on::before{width:64px;background:var(--ink)}
.social{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:14px}.social a{color:var(--muted)}.social a:hover{color:var(--accent)}
main{padding:96px 0}
section{margin-bottom:112px;scroll-margin-top:96px}
.mh{display:none}
.about p{margin:0 0 16px}.about b{color:var(--ink);font-weight:500}
.item{display:grid;grid-template-columns:130px 1fr;gap:24px;padding:22px 24px;margin:0 -24px 8px;border-radius:12px;transition:background .2s,box-shadow .2s}
.item:hover{background:var(--panel);box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}
.when{font:500 12px/1.9 "JetBrains Mono",monospace;color:var(--dim);text-transform:uppercase;letter-spacing:.04em}
.item h3{color:var(--ink);font-size:16px;font-weight:500;margin:0 0 6px;line-height:1.4}.item p{margin:0;font-size:15px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.chips span{font:500 12px/1 "Inter",sans-serif;color:var(--accent);background:rgba(125,211,192,.1);padding:6px 10px;border-radius:999px}
.thumb{width:130px;aspect-ratio:16/10;border-radius:6px;border:2px solid var(--line);object-fit:cover;background:#fff;opacity:.85}
.item:hover .thumb{opacity:1;border-color:#2b323b}
.more{display:inline-block;margin-top:8px;color:var(--ink);font-weight:500}.more:hover{color:var(--accent)}
.photo{display:block;padding:32px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(135deg,#12151a,#0e1a18)}
.photo h3{color:var(--ink);font-size:22px;margin:0 0 6px;letter-spacing:-.01em}
footer{font-size:13px;color:var(--dim)}
@media (max-width:960px){.social{margin-top:24px}.shell{grid-template-columns:1fr;gap:0;padding:0 24px}aside{position:static;height:auto;padding:64px 0 24px}.toc{display:none}
 main{padding:24px 0 64px}.mh{display:block;position:sticky;top:0;z-index:5;margin:0 -24px 20px;padding:14px 24px;background:rgba(11,13,16,.85);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
 color:var(--ink);font:500 12px/1 "JetBrains Mono",monospace;letter-spacing:.12em;text-transform:uppercase}section{margin-bottom:72px}}
@media (max-width:560px){.shell{padding:0 16px}.mh{margin:0 -16px 20px;padding:14px 16px}h1{font-size:36px}.item{grid-template-columns:1fr;gap:8px;margin:0 0 8px;padding:16px 0}.item:hover{background:none;box-shadow:none}.thumb{display:none}}
"""
JS_C = r"""
const links=[...document.querySelectorAll('.toc a')];const secs=links.map(a=>document.querySelector(a.getAttribute('href')));
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){links.forEach(l=>l.classList.toggle('on',l.getAttribute('href')==='#'+en.target.id))}}),{rootMargin:'-40% 0px -55% 0px'});
secs.forEach(s=>s&&io.observe(s));
if(matchMedia('(pointer:fine)').matches)addEventListener('pointermove',ev=>{document.body.style.setProperty('--mx',ev.clientX+'px');document.body.style.setProperty('--my',ev.clientY+'px')});
"""

def build_c():
    exp = "".join(f"""<div class="item"><div class="when">{x['dates']}</div><div><h3>{e(x['role'])} · <a href="{x['url']}"{ext(x['url'])}>{e(x['org'])}</a></h3>
      <p>{e(x['summary'])}</p>{f'<div class="chips"><span>{e(x["metric"])}</span></div>' if x['metric'] else ''}</div></div>""" for x in EXPERIENCE)
    proj = "".join(f"""<div class="item"><img class="thumb" src="../images/{p['img']}" alt="{e(p['name'])}" loading="lazy"><div>
      <h3><a href="{p['url']}"{ext(p['url'])}>{e(p['name'])} ↗</a></h3><p>{e(p['line'])}</p>
      <div class="chips">{''.join(f'<span>{s}</span>' for s in p['stack'])}</div></div></div>""" for p in PROJECTS[:6])
    social = "".join(f'<a href="{u}"{ext(u)}>{n}</a>' for n, u in LINKS)
    body = f"""<div class="shell">
  <aside><div><h1><a href="#">Sanjit Kumar</a></h1><div class="title">Software Engineer, Amazon Music</div>
    <p class="blurb">Subscription growth at scale, and a soft spot for the distributed systems underneath.</p>
    <ul class="toc"><li><a href="#about">About</a></li><li><a href="#experience">Experience</a></li><li><a href="#projects">Projects</a></li><li><a href="#photography">Photography</a></li></ul></div>
    <div class="social">{social}</div></aside>
  <main>
    <section id="about" class="about"><div class="mh">About</div>
      <p>I'm a software engineer at <a href="https://music.amazon.com" target="_blank" rel="noopener">Amazon Music</a> in Seattle, working on <b>subscription growth</b> across voice and mobile.</p>
      <p>Before that I did my master's in computer science at the <a href="https://cs.illinois.edu" target="_blank" rel="noopener">University of Illinois Urbana-Champaign</a>, where I TA'd distributed systems. I'm drawn to <b>full stack development</b> and <b>distributed, networked systems</b>.</p>
      <p>{e(OUTSIDE)}</p></section>
    <section id="experience"><div class="mh">Experience</div>{exp}
      <a class="more" href="../data/SanjitKumarResume_FullStack.pdf">View full resume ↗</a></section>
    <section id="projects"><div class="mh">Projects</div>{proj}
      <a class="more" href="https://github.com/sanjitk7/" target="_blank" rel="noopener">All projects on GitHub ↗</a></section>
    <section id="photography"><div class="mh">Photography</div>
      <a class="photo" href="{VSCO}" target="_blank" rel="noopener"><h3>Photography ↗</h3><p>Rides, cities and coffee shops. The full gallery lives on VSCO.</p></a></section>
    <footer>Published: <a href="{PUBLICATION['url']}" target="_blank" rel="noopener">{e(PUBLICATION['title'])}</a>, {PUBLICATION['venue']}.<br><br>© 2026 Sanjit Kumar</footer>
  </main></div>"""
    return page("Split", "family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500", CSS_C, body, JS_C)

INDEX = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>Redesign mockups</title><style>body{font:16px/1.6 system-ui;max-width:560px;margin:64px auto;padding:0 16px}a{display:block;padding:14px 0;border-bottom:1px solid #eee}</style></head>
<body><h1>Redesign mockups</h1><a href="a-quiet.html">A · Quiet: text-first single column</a><a href="b-cards.html">B · Cards: modern portfolio with featured work</a><a href="c-split.html">C · Split: dark, sticky sidebar</a></body></html>"""

if __name__ == "__main__":
    (OUT/'a-quiet.html').write_text(build_a()); (OUT/'b-cards.html').write_text(build_b()); (OUT/'c-split.html').write_text(build_c()); (OUT/'index.html').write_text(INDEX)
    print("built")
