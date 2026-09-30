import sys, json, math
from kit import *

OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
manifest = []

def add(k, date, cat, kind, files, caption_note=""):
    manifest.append(dict(k=k, date=date, cat=cat, theme=CYCLE[k % 3], kind=kind, files=files))

def S(name, html_str):
    render_png(html_str, OUT / f"{name}.png"); return f"{name}.png"

def phone_rows(title, hd, rows):
    r = "".join(f"<div class='row'><div>{a}<small>{b}</small></div><span class='{c}'>{d}</span></div>" for a, b, c, d in rows)
    return f"<div class='hd'>{hd}</div><div class='ttl'>{title}</div>{r}"

only = set(sys.argv[1:])
def want(name): return not only or name in only

# k0 — Oct 1 product (navy)
if want("d01"):
    ui = phone_rows("October payroll", "ZeniaHR · Payroll run", [
        ("Attendance synced", "Biometric · GPS · Excel", "ok", "Done"),
        ("PF · ESI · PT · LWF", "Calculated per state", "ok", "Done"),
        ("Payslips", "Email + employee app", "ok", "Sent"),
        ("Bank sheet + ECR", "Ready to upload", "warn", "Review"),
    ])
    f = S("d01_payroll", product("navy", "Product", "Salary day in <span class='acc'>one screen.</span>", "Attendance to bank sheet in four steps, for every guard at every site.", ui))
    add(0, "2026-10-01", "product", "image", [f])

# k1 — Oct 2 Gandhi Jayanti (mist)
if want("d02"):
    spokes = "".join(f"<line x1='540' y1='540' x2='{540+300*math.cos(i*math.pi/12):.1f}' y2='{540+300*math.sin(i*math.pi/12):.1f}' stroke='#B8672C' stroke-width='3'/>" for i in range(24))
    art = f"""<svg viewBox='0 0 1080 1350' width='1080' height='1350'><g transform='translate(810,420) scale(.72) translate(-540,-540)' opacity='.9'>
      <circle cx='540' cy='540' r='300' fill='none' stroke='#0E1A30' stroke-width='6'/><circle cx='540' cy='540' r='240' fill='none' stroke='#0E1A30' stroke-opacity='.25' stroke-width='2'/>
      {spokes}<circle cx='540' cy='540' r='36' fill='#0E1A30'/></g></svg>"""
    f = S("d02_gandhi", festival("mist", "2 October", "Gandhi Jayanti", "Har kaam izzat ka hai.", "Every shift, every site, every worker. On Gandhi Jayanti we honour the dignity of labour.", art))
    add(1, "2026-10-02", "fest", "image", [f])

# k2 — Oct 3 poll (copper)
if want("d03"):
    f = S("d03_poll", poll("copper", "Poll", "How long does your <span class='serif' style='font-weight:400'>monthly</span> payroll take?", ["Under 1 day", "2–3 days", "A full week", "Don't ask 😅"]))
    add(2, "2026-10-03", "engage", "image", [f])

# k3 — Oct 5 PF carousel (navy)
if want("d05"):
    fs = [
      S("d05_pf_1", number("navy", "PF Monday", "Employer contribution", "12", "%", "Where does the employer's 12% PF actually go?", ["Most of it isn't in the worker's PF account", "It is split between pension and PF", "Swipe for the split →"], pager="1/4")),
      S("d05_pf_2", number("navy", "PF Monday", "Goes to pension (EPS)", "8.33", "%", "of wages up to ₹15,000", ["Capped at ₹1,250 a month", "Builds the worker's monthly pension", "Not withdrawable like PF"], pager="2/4")),
      S("d05_pf_3", number("navy", "PF Monday", "Goes to PF (EPF)", "3.67", "%", "plus everything above the EPS cap", ["Joins the employee's own 12% in EPF", "Earns interest every year", "Withdrawable as per EPFO rules"], pager="3/4")),
      S("d05_pf_4", checklist("navy", "PF Monday", "On top of the 12%, <span class='acc'>employers also pay:</span>", ["EDLI insurance: 0.5% (wages up to ₹15,000)", "EPF admin charges: 0.5% (minimum ₹500)", "All calculated for you in ZeniaHR"], sub="Check current rates on epfindia.gov.in", pager="4/4", left="Save · Share with your accountant")),
    ]
    add(3, "2026-10-05", "pf", "carousel", fs)

# k4 — Oct 6 ESIC carousel (mist)
if want("d06"):
    fs = [
      S("d06_esic_1", number("mist", "ESIC Tuesday", "New contribution period starts", "₹21K", "", "ESIC: the Oct 2026 – Mar 2027 period is here", ["Wage ceiling: ₹21,000 a month (₹25,000 for persons with disability)", "Employee pays 0.75%, employer 3.25%", "Swipe: what happens if wages cross ₹21,000 →"], pager="1/3")),
      S("d06_esic_2", statement("mist", "ESIC Tuesday", "Two periods every year", "Apr–Sep <span class='acc'>&amp;</span><br>Oct–Mar", "Coverage is decided at the start of each contribution period. Wages on 1 October decide who is in for Oct–Mar.", pager="2/3")),
      S("d06_esic_3", statement("mist", "ESIC Tuesday", "Crossed ₹21,000 mid-period?", "Coverage <span class='acc'>continues</span> till 31 March.", "Keep deducting ESIC until the period ends. ZeniaHR tracks each employee's period automatically.", pager="3/3")),
    ]
    add(4, "2026-10-06", "esic", "carousel", fs)

# k5 — Oct 7 GPS (copper)
if want("d07"):
    ui = phone_rows("Night shift · 3 sites", "Live attendance", [
        ("Site 1 · Sargasan", "6 of 6 checked in", "ok", "On site"),
        ("Site 2 · GIFT City", "4 of 5 checked in", "warn", "1 late"),
        ("Site 3 · Infocity", "8 of 8 checked in", "ok", "On site"),
        ("GPS + selfie check-in", "Location verified", "ok", "Live"),
    ])
    f = S("d07_gps", product("copper", "Product", "GPS check-in for <span class='serif' style='font-weight:400'>every</span> guard.", "Mobile attendance with location. No more midnight calls to supervisors.", ui))
    add(5, "2026-10-07", "product", "image", [f])

# k6 — Oct 8 pain MOTION (navy)
if want("d08"):
    t = THEMES["navy"]
    anim = f"""
    .clock{{font-family:Archivo,sans-serif;font-stretch:75%;font-weight:800;font-size:300px;line-height:.85;letter-spacing:-.03em}}
    .colon{{animation:blink 1s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
    .ping{{position:absolute;left:120px;top:830px;width:30px;height:30px;border-radius:50%;background:{t['acc']}}}
    .ping::after{{content:'';position:absolute;inset:0;border-radius:50%;border:4px solid {t['acc']};animation:ping 1.5s ease-out infinite}}
    @keyframes ping{{from{{transform:scale(1);opacity:1}}to{{transform:scale(4);opacity:0}}}}
    .note{{position:absolute;left:80px;right:80px;top:960px;background:#F4F6FA;color:#0E1A30;border-radius:26px;padding:28px 34px;display:flex;gap:26px;align-items:center;
      animation:slide 6s cubic-bezier(.2,.8,.2,1) infinite}}
    @keyframes slide{{0%,30%{{transform:translateY(60px);opacity:0}}42%,92%{{transform:none;opacity:1}}100%{{opacity:0}}}}
    .dot{{width:64px;height:64px;border-radius:18px;background:#1F9D63;display:grid;place-items:center;color:#fff;font-size:36px;font-weight:800;flex:none}}
    .note b{{font-size:34px;display:block}} .note span{{font-size:26px;color:#4F5E7A}}
    .q{{animation:fadeq 6s ease infinite}} @keyframes fadeq{{0%{{opacity:0;transform:translateY(20px)}}12%,100%{{opacity:1;transform:none}}}}
    """
    body = f"""<div class='frame'>{top("Agency Owner Thursday")}
      <p class='disp q' style='font-size:66px;margin-top:70px;line-height:1.05'>Raat ke 2 baje guard site pe hai ya nahi,<br><span class='acc'>aapko kaise pata chalega?</span></p>
      <div class='clock' style='margin-top:40px'>02<span class='colon'>:</span>00</div>
      {foot("See every site live on ZeniaHR")}</div>
      <div class='ping'></div><span class='mono' style='position:absolute;left:180px;top:826px;font-size:26px;color:{t['sub']}'>SITE 2 · GIFT CITY</span>
      <div class='note'><div class='dot'>✓</div><div><b>Guard checked in · GPS verified</b><span>Site 2 · 01:58 AM · selfie matched</span></div></div>"""
    render_motion(page("navy", body, anim), "d08_2am", seconds=6)
    add(6, "2026-10-08", "pain", "motion", ["d08_2am.mp4", "d08_2am.gif", "d08_2am.png"])

# k7 — Oct 9 tender checklist (mist)
if want("d09"):
    f = S("d09_tender", checklist("mist", "Tender Friday", "What security tenders <span class='acc'>ask for</span>", ["PF &amp; ESIC registration certificates", "Last 6–12 months' paid challans", "PSARA licence (security agencies)", "GST registration &amp; returns", "CLRA labour licence", "Wage &amp; attendance registers"]))
    add(7, "2026-10-09", "tender", "image", [f])

# k8 — Oct 10 people quote (copper)
if want("d10"):
    f = S("d10_night", quote("copper", "World Mental Health Day", "Night shift wale bhaiyon ka bhi khayal rakhiye.", "A tea, a check-in call, a working torch. Small things make long night shifts easier for your guards."))
    add(8, "2026-10-10", "people", "image", [f])

# k9 — Oct 11 Navratri MOTION (navy)
if want("d11"):
    def ring(r, n, size, shape, cls):
        els = []
        for i in range(n):
            a = 2*math.pi*i/n; x = 540 + r*math.cos(a); y = 470 + r*math.sin(a)
            if shape == "dot": els.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{size}'/>")
            else:
                d = size; els.append(f"<rect x='{x-d/2:.1f}' y='{y-d/2:.1f}' width='{d}' height='{d}' transform='rotate(45 {x:.1f} {y:.1f})'/>")
        return f"<g class='{cls}' style='transform-origin:540px 470px'>{''.join(els)}</g>"
    art = f"""<svg viewBox='0 0 1080 1350' width='1080' height='1350'>
      <defs><radialGradient id='gl'><stop offset='0' stop-color='#E7A36B' stop-opacity='.55'/><stop offset='1' stop-color='#E7A36B' stop-opacity='0'/></radialGradient></defs>
      <g transform='translate(540,360) scale(.66) translate(-540,-470)'><circle class='glow' cx='540' cy='470' r='360' fill='url(#gl)' style='transform-origin:540px 470px'/>
      <g fill='#E7A36B'>{ring(330,24,9,'dot','r1')}</g>
      <g fill='none' stroke='#E7A36B' stroke-width='3'><circle cx='540' cy='470' r='270'/></g>
      <g fill='#F4F6FA' opacity='.85'>{ring(230,12,26,'dia','r2')}</g>
      <g fill='#E7A36B'>{ring(160,18,7,'dot','r3')}</g>
      <path d='M540 395 C 575 440, 578 480, 540 505 C 502 480, 505 440, 540 395 Z' fill='#E7A36B' class='flame' style='transform-origin:540px 505px'/>
      <rect x='490' y='505' width='100' height='34' rx='17' fill='#F4F6FA'/></g>
    </svg>"""
    anim = """.r1{animation:cw 6s linear infinite}.r2{animation:ccw 6s linear infinite}.r3{animation:cw2 6s linear infinite}
    @keyframes cw{to{transform:rotate(15deg)}} @keyframes ccw{to{transform:rotate(-30deg)}} @keyframes cw2{to{transform:rotate(20deg)}}
    .glow{animation:pulse 3s ease-in-out infinite} @keyframes pulse{50%{transform:scale(1.08);opacity:.7}}
    .flame{animation:fl 1.5s ease-in-out infinite} @keyframes fl{50%{transform:scaleY(1.12) scaleX(.94)}}"""
    render_motion(festival("navy", "Navratri · 11 October", "Shubh Navratri", "Navratri ni khub khub shubhkamnao!", "Aap garba karo, security hamari team sambhalegi. Wishing every agency and every guard on duty a joyful Navratri.", art, anim), "d11_navratri", seconds=6)
    add(9, "2026-10-11", "fest", "motion", ["d11_navratri.mp4", "d11_navratri.gif", "d11_navratri.png"])

# k10 — Oct 12 due date MOTION (mist)
if want("d12"):
    anim = """.cal{animation:pop 6s cubic-bezier(.2,1.4,.4,1) infinite;transform-origin:50% 0}
    @keyframes pop{0%{transform:rotateX(80deg);opacity:0}14%,100%{transform:none;opacity:1}}
    ul li{opacity:0;animation:in 6s ease infinite}
    ul li:nth-child(1){animation-name:in1}ul li:nth-child(2){animation-name:in2}ul li:nth-child(3){animation-name:in3}
    @keyframes in1{0%,20%{opacity:0;transform:translateX(-30px)}28%,100%{opacity:1;transform:none}}
    @keyframes in2{0%,30%{opacity:0;transform:translateX(-30px)}38%,100%{opacity:1;transform:none}}
    @keyframes in3{0%,40%{opacity:0;transform:translateX(-30px)}48%,100%{opacity:1;transform:none}}"""
    render_motion(duedate("mist", "Due-date reminder", "15", "OCT", "September PF &amp; ESIC are due <span class='acc'>this Thursday.</span>", ["New joiners: UAN generated and linked?", "Exits: date of leaving updated?", "Arrears and revised VDA included?"], anim), "d12_due", seconds=6)
    add(10, "2026-10-12", "due", "motion", ["d12_due.mp4", "d12_due.gif", "d12_due.png"])

# k11 — Oct 13 min wages carousel (copper)
if want("d13"):
    fs = [
      S("d13_wage_1", statement("copper", "Labour Law Tuesday", "From 1 October", "Minimum wages <span class='serif' style='font-weight:400'>revised?</span>", "Many states revise the variable dearness allowance (VDA) in April and October. Check before you run October payroll.", pager="1/3")),
      S("d13_wage_2", statement("copper", "Labour Law Tuesday", "Why it changes twice a year", "VDA follows the price index.", "Basic minimum wage + VDA = the minimum you must pay. When the index rises, the VDA and your wage bill rise with it.", pager="2/3")),
      S("d13_wage_3", checklist("copper", "Labour Law Tuesday", "Before October payroll", ["Download your state's latest notification", "Map each role to its skill category", "Update wage rates for every site", "Re-check PF &amp; ESIC on the new wages"], pager="3/3", left="ZeniaHR updates rates per state")),
    ]
    add(11, "2026-10-13", "law", "carousel", fs)

# k12 — Oct 14 statutory calc (navy)
if want("d14"):
    ui = phone_rows("Payslip · Oct 2026", "Statutory breakup", [
        ("Gross wages", "Basic ₹15,000 + allowances", "ok", "₹18,000"),
        ("PF (employee 12%)", "On ₹15,000", "warn", "− ₹1,800"),
        ("ESIC (0.75%)", "On ₹18,000", "warn", "− ₹135"),
        ("Professional tax", "Gujarat slab", "warn", "− ₹200"),
        ("LWF", "Half-yearly (Jun &amp; Dec)", "ok", "—"),
    ])
    f = S("d14_calc", product("navy", "Product", "PF, ESI, PT &amp; LWF. <span class='acc'>Auto.</span>", "Statutory rules built in, per state and per employee. No formulas to break.", ui))
    add(12, "2026-10-14", "product", "image", [f])

# k13 — Oct 15 myth (mist)
if want("d15"):
    f = S("d15_myth", myth("mist", "Agency Owner Thursday", "\"PF sirf permanent staff ka hota hai.\"", "Contract and outsourced workers are covered too. If the contractor doesn't pay, the principal employer is liable.", "Bilkul galat! Contract workers ka bhi PF banta hai."))
    add(13, "2026-10-15", "pain", "image", [f])

mf = OUT / "manifest.json"
old = json.loads(mf.read_text()) if mf.exists() else []
keep = {m["date"]: m for m in old}
for m in manifest: keep[m["date"]] = m
mf.write_text(json.dumps(sorted(keep.values(), key=lambda m: m["date"]), indent=1))
print("built", [m["date"] for m in manifest])
