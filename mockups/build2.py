"""Option D (bento sibling of B) and E (Swiss/editorial index). Run: python3 mockups/build2.py"""
from build import page, ext, e, OUT
from content import *

# ---------------------------------------------------------------- D: Bento
CSS_D = r"""
:root{--bg:#f4f4f1;--tile:#ffffff;--ink:#111214;--muted:#62666d;--line:#e6e6e1;--accent:#4f46e5;--accent-soft:#eef0ff}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{max-width:1120px;margin:0 auto;padding:0 28px}
nav{position:sticky;top:12px;z-index:10;margin:12px auto 0;max-width:1120px;padding:0 28px}
nav .bar{display:flex;justify-content:space-between;align-items:center;height:56px;padding:0 10px 0 20px;background:rgba(255,255,255,.78);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid var(--line);border-radius:999px}
nav ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-size:14px;color:var(--muted)}nav ul a:hover{color:var(--ink)}
.brand{font-weight:600}.cta{background:var(--ink);color:#fff;border-radius:999px;padding:8px 16px;font-size:14px;font-weight:500}
.tile{background:var(--tile);border:1px solid var(--line);border-radius:24px;padding:28px;transition:transform .25s,box-shadow .25s}
a.tile:hover{transform:translateY(-3px);box-shadow:0 12px 30px -18px rgba(0,0,0,.25)}
.label{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);font-weight:500}
.bento{display:grid;gap:14px;margin-top:40px;grid-template-columns:repeat(4,1fr);grid-template-areas:"intro intro intro photo" "metric edu loc lens"}
.intro{grid-area:intro;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:28px}
h1{font-size:clamp(40px,5.4vw,64px);line-height:1;letter-spacing:-.04em;margin:0 0 14px;font-weight:600}
.intro .sub{font-size:clamp(18px,2vw,22px);letter-spacing:-.01em;margin:0;max-width:560px;color:var(--muted)}.intro .sub b{color:var(--ink);font-weight:500}
.btns{display:flex;flex-wrap:wrap;gap:10px}
.btn{border:1px solid var(--line);border-radius:999px;padding:10px 18px;font-size:14px;font-weight:500;background:#fff}.btn:hover{border-color:var(--ink)}
.btn.primary{background:var(--ink);color:#fff;border-color:var(--ink)}
.photo{grid-area:photo;padding:0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:#fff}
.photo img{width:88%;height:auto;display:block}
.metric{grid-area:metric;background:var(--accent);border-color:var(--accent);color:#fff}
.metric .big{font-size:44px;font-weight:600;letter-spacing:-.03em;line-height:1;margin:18px 0 6px}.metric p{margin:0;font-size:14px;color:#dcdcff}.metric .label{color:#c7c9ff}
.edu{grid-area:edu}.edu img{width:40px;height:40px;border-radius:10px;margin-bottom:14px}.edu b{display:block;font-weight:600}.edu span{font-size:14px;color:var(--muted)}
.loc{grid-area:loc}.loc b{display:block;font-size:22px;letter-spacing:-.02em;margin-top:18px}.loc span{font-size:14px;color:var(--muted)}
.lens{grid-area:lens;background:#141414;border-color:#141414;color:#fff;background-image:radial-gradient(90% 120% at 100% 0%,#3b3157 0%,#141414 60%);display:flex;flex-direction:column;justify-content:space-between}
.lens .label{color:#a9a9b3}.lens b{font-size:22px;letter-spacing:-.02em}.lens span{color:#bdbdc6;font-size:14px}
section{margin-top:96px}
.sh{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:20px;gap:16px}
h2{font-size:30px;letter-spacing:-.025em;margin:0;font-weight:600}.sh p{margin:0;color:var(--muted);font-size:15px}
.timeline{padding:8px 28px}
.job{display:grid;grid-template-columns:48px 1fr auto;gap:4px 18px;padding:22px 0;border-bottom:1px solid var(--line)}.job:last-child{border-bottom:0}
.job img{width:48px;height:48px;border-radius:12px;object-fit:contain;border:1px solid var(--line);background:#fff;grid-row:span 2}
.job h3{margin:0;font-size:17px;font-weight:600}.job .org{color:var(--muted);font-size:15px}.job .org a:hover{color:var(--accent)}
.job .when{font-size:14px;color:var(--muted);text-align:right;white-space:nowrap}
.job p{grid-column:2/4;margin:4px 0 0;color:var(--muted);font-size:15px;max-width:720px}
.pill{display:inline-block;margin-top:10px;font-size:13px;font-weight:500;color:var(--accent);background:var(--accent-soft);border-radius:999px;padding:3px 10px}
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.pcard{padding:0;overflow:hidden;display:flex;flex-direction:column}
.pcard .img{aspect-ratio:16/10;overflow:hidden;border-bottom:1px solid var(--line);background:#fafafa}.pcard .img img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.pcard:hover .img img{transform:scale(1.03)}
.pcard .c{padding:20px 22px 24px}.pcard h3{margin:6px 0 6px;font-size:18px;letter-spacing:-.01em}.pcard p{margin:0;color:var(--muted);font-size:15px}
.pcard.wide{grid-column:span 2}.pcard.wide .img{aspect-ratio:auto;flex:1;min-height:220px}
.minis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:14px}
.mini{padding:20px 22px}.mini h3{margin:6px 0 4px;font-size:16px}.mini p{margin:0;color:var(--muted);font-size:14px}
.contact{margin:96px 0 28px;background:#111214;color:#fff;border-color:#111214;padding:56px;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.contact h2{font-size:clamp(30px,4.4vw,52px);line-height:1.05;max-width:620px}.contact h2 span{color:#8b8d93}
.contact .btn{background:#fff;color:#111}
.fine{color:var(--muted);font-size:13px;padding:0 0 40px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.fine a{text-decoration:underline;text-underline-offset:3px}
@media (max-width:900px){nav ul{display:none}.bento{grid-template-columns:1fr 1fr;grid-template-areas:"intro intro" "photo metric" "edu loc" "lens lens"}
 .pgrid{grid-template-columns:1fr}.pcard.wide{grid-column:auto}.minis{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.wrap,nav{padding:0 16px}.intro{padding:28px 22px}.tile{padding:22px}.photo,.pcard{padding:0}.timeline{padding:4px 20px}
 .job{grid-template-columns:40px 1fr}.job img{width:40px;height:40px}.job .when{grid-column:2;text-align:left}.job p{grid-column:1/3}
 .minis{grid-template-columns:1fr}.contact{padding:32px 24px}.sh p{display:none}.metric .big{font-size:36px}}
"""

def build_d():
    jobs = "".join(f"""<div class="job"><img src="../images/{x['logo']}" alt="{e(x['org'])} logo" loading="lazy">
      <div><h3>{e(x['role'])}</h3><div class="org"><a href="{x['url']}"{ext(x['url'])}>{e(x['org'])}</a> · {x['place']}</div></div><div class="when">{x['dates']}</div>
      <p>{e(x['summary'])}{f'<br><span class="pill">{e(x["metric"])}</span>' if x['metric'] else ''}</p></div>""" for x in EXPERIENCE)
    feat = [PROJECTS[2], PROJECTS[0], PROJECTS[1], PROJECTS[3]]; rest = PROJECTS[4:]
    cards = "".join(f"""<a class="tile pcard{' wide' if i==0 else ''}" href="{p['url']}"{ext(p['url'])}><div class="img"><img src="../images/{p['img']}" alt="{e(p['name'])}" loading="lazy"></div>
      <div class="c"><div class="label">{e(p['tag'])}</div><h3>{e(p['name'])}</h3><p>{e(p['line'])}</p></div></a>""" for i, p in enumerate(feat))
    minis = "".join(f"""<a class="tile mini" href="{p['url']}"{ext(p['url'])}><div class="label">{e(p['tag'])}</div><h3>{e(p['name'])} ↗</h3><p>{e(p['line'])}</p></a>""" for p in rest)
    body = f"""<nav><div class="bar"><a class="brand" href="#">Sanjit Kumar</a>
  <ul><li><a href="#experience">Experience</a></li><li><a href="#work">Work</a></li><li><a href="{VSCO}" target="_blank" rel="noopener">Photography</a></li></ul>
  <a class="cta" href="mailto:sanjitk2018@gmail.com">Say hi</a></div></nav>
<main class="wrap">
  <div class="bento">
    <div class="tile intro"><div><h1>Sanjit Kumar</h1>
      <p class="sub"><b>Software engineer at Amazon Music</b>, working on subscription growth across voice and mobile. Into full stack and distributed systems.</p></div>
      <div class="btns"><a class="btn primary" href="../data/SanjitKumarResume_FullStack.pdf">Resume</a><a class="btn" href="https://github.com/sanjitk7/" target="_blank" rel="noopener">GitHub</a><a class="btn" href="https://www.linkedin.com/in/sanjitk7/" target="_blank" rel="noopener">LinkedIn</a></div></div>
    <div class="tile photo"><img src="../images/sanjit-profile-pic-circle.jpeg" alt="Sanjit Kumar, software engineer at Amazon" width="400" height="400"></div>
    <div class="tile metric"><div class="label">Impact at Amazon</div><div class="big">150k+</div><p>annualized Amazon Music tier signups</p></div>
    <a class="tile edu" href="https://cs.illinois.edu" target="_blank" rel="noopener"><img src="../images/uofilogoblue2.jpeg" alt="UIUC logo"><b>M.S. Computer Science</b><span>University of Illinois Urbana-Champaign</span></a>
    <div class="tile loc"><div class="label">Based in</div><b>Seattle, WA</b><span>Road bike, books, coffee.</span></div>
    <a class="tile lens" href="{VSCO}" target="_blank" rel="noopener"><div class="label">Photography</div><div><b>Through the lens ↗</b><br><span>Gallery on VSCO</span></div></a>
  </div>
  <section id="experience"><div class="sh"><h2>Experience</h2><p>2020 – present</p></div><div class="tile timeline">{jobs}</div></section>
  <section id="work"><div class="sh"><h2>Selected work</h2><p>Systems, kernels, graphics, data.</p></div><div class="pgrid">{cards}</div><div class="minis">{minis}</div></section>
  <div class="tile contact"><h2>Building something interesting? <span>Let's talk.</span></h2><a class="btn" href="mailto:sanjitk2018@gmail.com">sanjitk2018@gmail.com</a></div>
  <div class="fine"><span>© 2026 Sanjit Kumar</span><span>Published: <a href="{PUBLICATION['url']}" target="_blank" rel="noopener">IoT security survey, AIMV 2021</a></span></div>
</main>"""
    return page("Bento", "family=Inter:wght@400;500;600", CSS_D, body)

# ---------------------------------------------------------------- E: Index (Swiss editorial)
CSS_E = r"""
:root{--paper:#efede6;--ink:#0d0d0d;--muted:#6b6862;--rule:#0d0d0d;--signal:#1f3cff}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 "Inter Tight","Inter",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.mono{font:500 12px/1.4 "IBM Plex Mono",monospace;letter-spacing:.02em;text-transform:uppercase}
.page{padding:0 32px}
.top{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding:18px 0;border-bottom:1px solid var(--rule)}
.top a:hover{color:var(--signal)}.top .r{text-align:right}
.name{font-weight:700;font-size:clamp(64px,16.2vw,260px);line-height:.84;letter-spacing:-.06em;margin:28px 0 0;padding-bottom:20px;border-bottom:1px solid var(--rule)}
.name span{display:block}.name em{font-style:normal;color:var(--signal)}
.row{display:grid;grid-template-columns:repeat(12,1fr);gap:24px;padding:28px 0 64px;border-bottom:1px solid var(--rule)}
.idx{grid-column:1/4}.idx .n{display:block;font:500 13px/1 "IBM Plex Mono",monospace;margin-bottom:10px}
.idx h2{font-size:15px;font-weight:600;margin:0;text-transform:uppercase;letter-spacing:.02em}
.content{grid-column:4/13}
.statement{font-size:clamp(26px,3.2vw,46px);line-height:1.08;letter-spacing:-.03em;font-weight:500;margin:0;max-width:22ch}
.statement a{border-bottom:2px solid var(--signal)}.statement a:hover{color:var(--signal)}
.aboutgrid{display:grid;grid-template-columns:1fr 200px;gap:32px;align-items:start}
.aboutgrid img{width:200px;height:200px;object-fit:cover;filter:grayscale(1) contrast(1.1);mix-blend-mode:multiply;border-radius:0}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px;padding-top:16px;border-top:1px solid var(--rule)}
.facts p{margin:6px 0 0;font-size:15px}
.tbl{width:100%;border-collapse:collapse}
.tbl .tr{display:grid;grid-template-columns:110px 1.4fr 1fr 1fr;gap:20px;padding:18px 0;border-top:1px solid var(--rule);transition:background .15s,color .15s,padding .2s}
.tbl .tr:last-child{border-bottom:1px solid var(--rule)}
.tbl .tr:hover{background:var(--ink);color:var(--paper);padding:18px 12px}.tbl .tr:hover .sum,.tbl .tr:hover .mono{color:#b8b5ad}
.tbl .role{font-size:20px;font-weight:600;letter-spacing:-.015em;line-height:1.2}
.tbl .sum{grid-column:2/5;color:var(--muted);font-size:15px;max-width:720px;margin-top:-6px}
.tbl .kpi{color:var(--signal);font:500 12px/1.4 "IBM Plex Mono",monospace;text-transform:uppercase}
.tbl .tr:hover .kpi{color:#8ea0ff}
.plist .p{display:grid;grid-template-columns:60px 1fr auto;gap:20px;align-items:baseline;padding:16px 0;border-top:1px solid var(--rule);position:relative}
.plist .p:last-child{border-bottom:1px solid var(--rule)}
.plist .t{font-size:clamp(26px,3.4vw,48px);font-weight:600;letter-spacing:-.035em;line-height:1.05;transition:color .15s,padding .25s}
.plist .p:hover .t{color:var(--signal);padding-left:12px}
.plist .d{grid-column:2/4;color:var(--muted);font-size:15px;max-width:640px;margin-top:-4px}
#peek{position:fixed;width:260px;aspect-ratio:16/10;pointer-events:none;opacity:0;transition:opacity .2s;z-index:20;border:1px solid var(--ink);background:#fff center/cover no-repeat;transform:translate(24px,-50%)}
.big{display:block;font-size:clamp(44px,9vw,150px);font-weight:700;letter-spacing:-.05em;line-height:.9;overflow-wrap:anywhere}
.big:hover{color:var(--signal)}
.foot{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding:20px 0 32px}
.foot a:hover{color:var(--signal)}
@media (max-width:860px){.top{grid-template-columns:1fr 1fr}.top .hide{display:none}
 .row{grid-template-columns:1fr;gap:20px;padding:20px 0 48px}.idx,.content{grid-column:1}
 .aboutgrid{grid-template-columns:1fr}.aboutgrid img{width:120px;height:120px;order:-1}.facts{grid-template-columns:1fr}
 .tbl .tr{grid-template-columns:1fr;gap:4px;margin:0;padding:16px 0}.tbl .sum{grid-column:1;margin-top:4px}.tbl .tr:hover{background:none;color:inherit}
 .plist .p{grid-template-columns:36px 1fr}.plist .p .mono.r{display:none}.plist .d{grid-column:2}.foot{grid-template-columns:1fr 1fr}#peek{display:none}}
@media (max-width:520px){.page{padding:0 16px}.name{font-size:21.5vw}}
"""
JS_E = r"""
const pk=document.getElementById('peek');
if(matchMedia('(pointer:fine)').matches){document.querySelectorAll('.plist .p').forEach(r=>{
 r.addEventListener('mouseenter',()=>{pk.style.backgroundImage=`url(${r.dataset.img})`;pk.style.opacity=1});
 r.addEventListener('mouseleave',()=>pk.style.opacity=0)});
 addEventListener('mousemove',ev=>{pk.style.left=ev.clientX+'px';pk.style.top=ev.clientY+'px'})}
"""

def build_e():
    exp = "".join(f"""<a class="tr" href="{x['url']}"{ext(x['url'])}><div class="mono">{x['dates']}</div><div class="role">{e(x['role'])}</div><div>{e(x['org'])}</div><div class="mono">{x['place']}{f'<br><span class="kpi">↑ {e(x["metric"])}</span>' if x['metric'] else ''}</div>
      <div class="sum">{e(x['summary'])}</div></a>""" for x in EXPERIENCE)
    proj = "".join(f"""<a class="p" href="{p['url']}"{ext(p['url'])} data-img="../images/{p['img']}"><span class="mono">{i:02d}</span><span class="t">{e(p['name'])}</span><span class="mono r">{e(p['tag'])} ↗</span>
      <span class="d">{e(p['line'])}</span></a>""" for i, p in enumerate(PROJECTS, 1))
    body = f"""<div class="page">
  <div class="top mono"><span>Sanjit Kumar</span><span class="hide">Software engineer</span><span class="hide">Seattle, 47.6°N 122.3°W</span><span class="r"><a href="mailto:sanjitk2018@gmail.com">Contact ↗</a></span></div>
  <h1 class="name"><span>Sanjit</span><span>Kumar<em>.</em></span></h1>
  <div class="row"><div class="idx"><span class="n">(01)</span><h2>About</h2></div><div class="content">
    <div class="aboutgrid"><p class="statement">Software engineer at <a href="https://music.amazon.com" target="_blank" rel="noopener">Amazon Music</a>, working on subscription growth across voice and mobile.</p>
      <img src="../images/sanjit-profile-pic-circle.jpeg" alt="Sanjit Kumar, software engineer at Amazon" width="200" height="200"></div>
    <div class="facts"><div><span class="mono">Education</span><p>M.S. Computer Science,<br>University of Illinois Urbana-Champaign</p></div>
      <div><span class="mono">Interests</span><p>Full stack development,<br>distributed and networked systems</p></div>
      <div><span class="mono">Off the clock</span><p>Road bike, camera in hand,<br>a new coffee shop and a book</p></div></div></div></div>
  <div class="row"><div class="idx"><span class="n">(02)</span><h2>Experience</h2></div><div class="content"><div class="tbl">{exp}</div></div></div>
  <div class="row"><div class="idx"><span class="n">(03)</span><h2>Selected work</h2></div><div class="content"><div class="plist">{proj}</div></div></div>
  <div class="row"><div class="idx"><span class="n">(04)</span><h2>Photography</h2></div><div class="content"><a class="big" href="{VSCO}" target="_blank" rel="noopener">VSCO ↗</a>
    <p class="mono" style="margin-top:16px;color:var(--muted)">Rides, streets, coffee shops</p></div></div>
  <div class="row"><div class="idx"><span class="n">(05)</span><h2>Contact</h2></div><div class="content"><a class="big" href="mailto:sanjitk2018@gmail.com" style="font-size:clamp(28px,5.4vw,84px)">sanjitk2018@<wbr>gmail.com</a></div></div>
  <div class="foot mono"><a href="../data/SanjitKumarResume_FullStack.pdf">Resume ↗</a><a href="https://github.com/sanjitk7/" target="_blank" rel="noopener">GitHub ↗</a><a href="https://www.linkedin.com/in/sanjitk7/" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{PUBLICATION['url']}" target="_blank" rel="noopener">AIMV 2021 paper ↗</a></div>
</div><div id="peek"></div>"""
    return page("Index", "family=Inter+Tight:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500", CSS_E, body, JS_E)

if __name__ == "__main__":
    (OUT/'d-bento.html').write_text(build_d()); (OUT/'e-index.html').write_text(build_e())
    print("built")
