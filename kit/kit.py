"""ZeniaHR Instagram design kit: themes, templates, renderer (static PNG + motion MP4/GIF)."""
import os, json, subprocess, html
from pathlib import Path
ROOT = Path(__file__).parent
FONTS = ROOT / "node_modules"
W, H = 1080, 1350

THEMES = {
  "navy":   dict(bg="#0E1A30", fg="#F4F6FA", sub="#A9B5CC", acc="#E7A36B", line="rgba(255,255,255,.14)", card="rgba(255,255,255,.06)", chipbg="rgba(231,163,107,.14)", chipfg="#E7A36B", invbg="#E7A36B", invfg="#0E1A30"),
  "mist":   dict(bg="#E6EBF2", fg="#0E1A30", sub="#4F5E7A", acc="#B8672C", line="rgba(14,26,48,.14)", card="#F6F8FB", chipbg="#0E1A30", chipfg="#F4F6FA", invbg="#0E1A30", invfg="#F4F6FA"),
  "copper": dict(bg="#C8793B", fg="#0E1A30", sub="#3A2A1C", acc="#0E1A30", line="rgba(14,26,48,.22)", card="rgba(255,255,255,.16)", chipbg="#0E1A30", chipfg="#F1C9A4", invbg="#0E1A30", invfg="#F4F6FA"),
}
CYCLE = ["navy", "mist", "copper"]

def font_css():
    f = lambda p: (FONTS / p).as_uri()
    return f"""
@font-face{{font-family:Archivo;src:url({f('@fontsource-variable/archivo/files/archivo-latin-wdth-normal.woff2')}) format('woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:Archivo;src:url({f('@fontsource-variable/archivo/files/archivo-latin-ext-wdth-normal.woff2')}) format('woff2');font-weight:100 900;font-stretch:62% 125%;unicode-range:U+0100-02AF,U+20A0-20CF}}
@font-face{{font-family:Manrope;src:url({f('@fontsource/manrope/files/manrope-latin-500-normal.woff2')});font-weight:500}}
@font-face{{font-family:Manrope;src:url({f('@fontsource/manrope/files/manrope-latin-700-normal.woff2')});font-weight:700}}
@font-face{{font-family:Manrope;src:url({f('@fontsource/manrope/files/manrope-latin-800-normal.woff2')});font-weight:800}}
@font-face{{font-family:Mono;src:url({f('@fontsource/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2')});font-weight:500}}
@font-face{{font-family:Serif;src:url({f('@fontsource/instrument-serif/files/instrument-serif-latin-400-italic.woff2')});font-style:italic}}
"""

def base_css(t):
    return font_css() + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:{t['bg']};color:{t['fg']};font-family:Manrope,'DejaVu Sans',sans-serif;position:relative}}
.disp{{font-family:Archivo,'DejaVu Sans',sans-serif;font-stretch:112%;font-weight:800;letter-spacing:-.02em;line-height:.98}}
.cond{{font-family:Archivo,'DejaVu Sans',sans-serif;font-stretch:75%;font-weight:800;letter-spacing:-.01em;line-height:.9}}
.serif{{font-family:Serif,Georgia,serif;font-style:italic;font-weight:400;letter-spacing:0}}
.mono{{font-family:Mono,'DejaVu Sans Mono',monospace;letter-spacing:.04em}}
.acc{{color:{t['acc']}}}
.sub{{color:{t['sub']}}}
.frame{{position:absolute;inset:0;padding:84px 80px 76px;display:flex;flex-direction:column}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;padding-block:40px}}
.main>*:first-child{{margin-top:0!important}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.chip{{font-family:Mono,monospace;font-size:22px;letter-spacing:.12em;text-transform:uppercase;background:{t['chipbg']};color:{t['chipfg']};padding:10px 18px;border-radius:6px}}
.handle{{font-family:Mono,monospace;font-size:22px;letter-spacing:.06em;color:{t['sub']}}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid {t['line']};padding-top:26px;font-size:26px;font-weight:700}}
.foot .u{{font-family:Mono,monospace;font-weight:500;letter-spacing:.06em;color:{t['acc']}}}
.pager{{font-family:Mono,monospace;font-weight:500;font-size:24px;color:{t['sub']}}}
.card{{background:{t['card']};border:2px solid {t['line']};border-radius:22px}}
.inv{{background:{t['invbg']};color:{t['invfg']}}}
"""

def page(theme, body, extra_css=""):
    t = THEMES[theme]
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{base_css(t)}{extra_css}</style></head><body>{body}</body></html>"

def top(chip, t=None):
    return f"<div class='top'><span class='chip'>{chip}</span><span class='handle'>@zenia_hr</span></div>"

def foot(left="Book a free demo", pager=None):
    right = f"<span class='pager'>{pager}</span>" if pager else "<span class='u'>zeniahr.com</span>"
    return f"<div class='foot'><span>{left}</span>{right}</div>"

e = html.escape

# ---------- TEMPLATES ----------
def statement(theme, chip, kicker, headline_html, sub, left="Book a free demo", pager=None, anim=""):
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <div style='margin-top:120px;font-size:26px' class='mono sub' >{kicker}</div>
    <h1 class='disp' style='font-size:118px;margin-top:28px'>{headline_html}</h1>
    <p style='font-size:36px;line-height:1.4;margin-top:44px;max-width:860px;font-weight:500' class='sub'>{sub}</p>
    </div>{foot(left, pager)}</div>"""
    return page(theme, body, anim)

def number(theme, chip, kicker, big, unit, label, points, pager=None):
    pts = "".join(f"<li><span class='acc mono'>{i+1:02d}</span><span>{p}</span></li>" for i, p in enumerate(points))
    css = """.big{font-size:330px;line-height:.82;letter-spacing:-.04em}
    ul{list-style:none;display:grid;gap:22px;margin-top:40px}
    li{display:grid;grid-template-columns:70px 1fr;font-size:34px;line-height:1.35;font-weight:500}
    li .mono{font-size:26px;padding-top:6px}"""
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <div class='mono sub' style='margin-top:70px;font-size:26px'>{kicker}</div>
    <div style='display:flex;align-items:flex-end;gap:18px;margin-top:10px'><span class='cond big'>{big}</span><span class='disp acc' style='font-size:64px;padding-bottom:22px'>{unit}</span></div>
    <h2 class='disp' style='font-size:58px;margin-top:26px;max-width:900px'>{label}</h2>
    <ul>{pts}</ul></div>{foot(pager=pager)}</div>"""
    return page(theme, body, css)

def checklist(theme, chip, headline_html, items, sub=None, pager=None, left="Save this for your next bid"):
    li = "".join(f"<li><span class='box'>✓</span><span>{x}</span></li>" for x in items)
    t = THEMES[theme]
    css = f"""ul{{list-style:none;display:grid;gap:18px;margin-top:48px}}
    li{{display:flex;gap:26px;align-items:center;font-size:36px;font-weight:700;padding:22px 26px;border-radius:18px;background:{t['card']};border:2px solid {t['line']}}}
    .box{{flex:none;width:52px;height:52px;border-radius:12px;display:grid;place-items:center;font-size:30px;background:{t['invbg']};color:{t['invfg']}}}"""
    s = f"<p class='sub' style='font-size:32px;margin-top:26px;font-weight:500'>{sub}</p>" if sub else ""
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <h1 class='disp' style='font-size:92px;margin-top:80px'>{headline_html}</h1>{s}
    <ul>{li}</ul></div>{foot(left, pager)}</div>"""
    return page(theme, body, css)

def myth(theme, chip, myth_txt, fact_txt, note):
    t = THEMES[theme]
    css = f""".half{{border-radius:24px;padding:40px 44px;display:grid;gap:14px}}
    .lab{{font-family:Mono,monospace;font-size:24px;letter-spacing:.14em;text-transform:uppercase}}
    .m{{background:{t['card']};border:2px dashed {t['line']}}}
    .m p{{text-decoration:line-through;text-decoration-thickness:5px;text-decoration-color:{t['acc']}}}
    .f{{background:{t['invbg']};color:{t['invfg']}}}"""
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <h1 class='cond' style='font-size:150px;margin-top:60px'>MYTH <span class='serif acc' style='font-size:120px;font-weight:400'>vs</span> FACT</h1>
    <div style='display:grid;gap:22px;margin-top:40px'>
      <div class='half m'><span class='lab sub'>Myth</span><p class='disp' style='font-size:54px'>{myth_txt}</p></div>
      <div class='half f'><span class='lab' style='opacity:.8'>Fact</span><p style='font-size:38px;line-height:1.35;font-weight:700'>{fact_txt}</p></div>
    </div>
    <p class='sub' style='font-size:28px;margin-top:26px;font-weight:500'>{note}</p>
    </div>{foot()}</div>"""
    return page(theme, body, css)

def product(theme, chip, headline_html, sub, ui_html, left="See it live: book a demo"):
    t = THEMES[theme]
    css = f""".phone{{position:absolute;right:80px;bottom:190px;width:470px;height:720px;border-radius:56px;background:#0B1428;border:12px solid #1D2A48;box-shadow:0 40px 80px rgba(0,0,0,.35);overflow:hidden;padding:36px 28px;display:grid;gap:18px;align-content:start;color:#EAF0FA}}
    .row{{display:flex;justify-content:space-between;align-items:center;background:#15213C;border-radius:18px;padding:18px 20px;font-size:24px;font-weight:700}}
    .row small{{display:block;font-size:19px;font-weight:500;color:#8FA0C0}}
    .ok{{font-family:Mono,monospace;font-size:18px;padding:6px 12px;border-radius:999px;background:rgba(111,207,151,.16);color:#7FDCA6}}
    .warn{{font-family:Mono,monospace;font-size:18px;padding:6px 12px;border-radius:999px;background:rgba(231,163,107,.18);color:#F0B27E}}
    .hd{{font-family:Mono,monospace;font-size:18px;letter-spacing:.1em;color:#8FA0C0;text-transform:uppercase}}
    .ttl{{font-family:Archivo,sans-serif;font-stretch:110%;font-weight:800;font-size:34px}}
    .demo{{position:absolute;right:92px;bottom:150px;font-family:Mono,monospace;font-size:17px;color:{t['sub']}}}"""
    body = f"""<div class='frame'>{top(chip)}
    <h1 class='disp' style='font-size:96px;margin-top:80px;max-width:560px'>{headline_html}</h1>
    <p class='sub' style='font-size:32px;line-height:1.4;margin-top:34px;max-width:470px;font-weight:500'>{sub}</p>
    {foot(left)}</div><div class='phone'>{ui_html}</div><div class='demo'>Illustrative screen</div>"""
    return page(theme, body, css)

def quote(theme, chip, hook, eng, left="@zenia_hr"):
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <div class='serif acc' style='font-size:260px;line-height:.6;margin-top:110px'>“</div>
    <p class='disp' style='font-size:100px;line-height:1.02;margin-top:10px'>{hook}</p>
    <p class='sub' style='font-size:32px;line-height:1.4;margin-top:40px;max-width:860px;font-weight:500'>{eng}</p>
    </div>{foot(left)}</div>"""
    return page(theme, body)

def poll(theme, chip, q_html, opts, cta="Vote in the comments 👇"):
    t = THEMES[theme]
    o = "".join(f"<div class='opt'><span class='mono acc'>{chr(65+i)}</span><span>{x}</span></div>" for i, x in enumerate(opts))
    css = f""".opt{{display:flex;gap:30px;align-items:center;font-size:40px;font-weight:700;padding:28px 34px;border-radius:999px;border:3px solid {t['fg']}}}
    .opt .mono{{font-size:30px}}"""
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <h1 class='disp' style='font-size:100px;margin-top:90px'>{q_html}</h1>
    <div style='display:grid;gap:20px;margin-top:60px'>{o}</div>
    </div>{foot(cta)}</div>"""
    return page(theme, body, css)

def duedate(theme, chip, day, mon, headline_html, items, anim=""):
    li = "".join(f"<li>{x}</li>" for x in items)
    t = THEMES[theme]
    css = f""".cal{{width:360px;border-radius:28px;overflow:hidden;background:{t['card']};border:2px solid {t['line']};text-align:center}}
    .cal .m{{background:{t['invbg']};color:{t['invfg']};font-family:Mono,monospace;font-size:34px;letter-spacing:.2em;padding:18px}}
    .cal .d{{font-family:Archivo,sans-serif;font-stretch:75%;font-weight:800;font-size:250px;line-height:1.05}}
    ul{{margin-top:40px;display:grid;gap:14px;padding-left:36px;font-size:34px;font-weight:600;line-height:1.35}}
    li::marker{{color:{t['acc']}}}""" + anim
    body = f"""<div class='frame'>{top(chip)}<div class='main'>
    <div style='display:flex;gap:50px;align-items:center;margin-top:80px'>
      <div class='cal'><div class='m'>{mon}</div><div class='d'>{day}</div></div>
      <h1 class='disp' style='font-size:72px;flex:1'>{headline_html}</h1></div>
    <ul>{li}</ul></div>{foot("Automate it with ZeniaHR")}</div>"""
    return page(theme, body, css)

def festival(theme, chip, title_html, line1, line2, art_svg, anim=""):
    body = f"""<div style='position:absolute;inset:0'>{art_svg}</div><div class='frame'>{top(chip)}
    <div style='margin-top:auto;margin-bottom:40px'>
      <p class='serif acc' style='font-size:64px'>{line1}</p>
      <h1 class='disp' style='font-size:128px;margin-top:6px'>{title_html}</h1>
      <p class='sub' style='font-size:32px;line-height:1.4;margin-top:26px;max-width:860px;font-weight:500'>{line2}</p></div>
    {foot("From all of us at ZeniaHR")}</div>"""
    return page(theme, body, anim+'.foot{margin-top:0}')

# ---------- RENDER ----------
def render_png(html_str, out):
    from playwright.sync_api import sync_playwright
    p = ROOT / "build" / (Path(out).stem + ".html"); p.parent.mkdir(exist_ok=True); p.write_text(html_str)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(p.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=(a.effect.getComputedTiming().endTime===Infinity?4000:a.effect.getComputedTiming().endTime)})")
        pg.screenshot(path=str(out)); b.close()

def render_motion(html_str, out_stem, seconds=6, fps=30):
    """Scrub CSS animations frame by frame -> MP4 (1080x1350) + GIF (540w) + poster PNG."""
    from playwright.sync_api import sync_playwright
    p = ROOT / "build" / (out_stem + ".html"); p.parent.mkdir(exist_ok=True); p.write_text(html_str)
    fdir = ROOT / "build" / (out_stem + "_frames"); fdir.mkdir(exist_ok=True)
    for f in fdir.glob("*.png"): f.unlink()
    n = seconds * fps
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(p.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i in range(n):
            t = i * 1000 / fps
            pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t})")
            pg.screenshot(path=str(fdir / f"f{i:04d}.png"))
        b.close()
    out = ROOT / "out"; out.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",str(fdir/"f%04d.png"),"-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-movflags","+faststart",str(out/f"{out_stem}.mp4")],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",str(fdir/"f%04d.png"),"-vf","fps=15,scale=540:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4",str(out/f"{out_stem}.gif")],check=True)
    import shutil; shutil.copy(fdir / f"f{n-1:04d}.png", out / f"{out_stem}.png")
