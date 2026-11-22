import base64
from pathlib import Path

import streamlit as st
from PIL import Image
# ------------------------------------------------------------------ #
#  Page config
# ------------------------------------------------------------------ #
st.set_page_config(
    page_title="Martina Emad | Data Engineer",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
NAME_FIRST = "Martina"
NAME_LAST = "Emad"
st.markdown("""
""", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    image_path = BASE / "profile.jpg"
    image = Image.open(image_path)
    st.markdown(f'<img src="data:image/png;base64,{image_path.read_bytes().hex()}" class="circular-img">', unsafe_allow_html=True)
with col2:
    st.title(f"{NAME_FIRST.title()} {NAME_LAST.title()}")
    st.subheader("Data Engineer")
    st.write("---")
# ------------------------------------------------------------------ #
#  Content (edit everything here)
# ------------------------------------------------------------------ #
NAME_FIRST = "martina"
NAME_LAST = "emad"

EMAIL = "martinaemad197@gmail.com"
PHONE = "01275484464"
WHATSAPP_LINK = "https://wa.me/201275484464"
LINKEDIN_URL = "https://www.linkedin.com/in/martina-emad-aa5411430"
GITHUB_URL = "https://github.com/your-username"             # TODO: replace

ABOUT = (
    "I am a dedicated Software Industry and Multimedia (SIM) student at the "
    "Faculty of Science, Alexandria University, and a Microsoft Data Engineer "
    "trainee at the Digital Egypt Pioneers Initiative (DEPI). I specialize in "
    "designing scalable data architectures, building robust ETL pipelines, and "
    "transforming raw, messy datasets into clean, reliable foundations that "
    "drive smart business decisions. Passionate about leveraging Python, SQL, "
    "and modern data workflows to bridge the gap between complex data systems "
    "and actionable insights."
)

EDUCATION = {
    "degree": "Bachelor's Degree in Software Industry and Multimedia (SIM)",
    "school": "Faculty of Science, Alexandria University",
    "years": "2025 — 2029",
}

CERTIFICATES = [
    {"title": "Database Fundamentals", "image": "assets/certificate.jpg"},
]

SKILLS = ["Python", "SQL", "ETL Pipelines", "Data Modeling", "Pandas", "Git"]  # edit

PROJECTS = [  # edit / add yours
    {
        "title": "Project name",
        "desc": "Short description of what the project does and the tools you used.",
        "tags": ["Python", "SQL"],
        "link": GITHUB_URL,
    },
]

EXPERIENCE = [
    {
        "title": "Advanced Data Analytics Training",
        "year": "2025",
        "org": "DEPI (MCIT)",
        "desc": "Hands-on training in data analytics, pipelines, and modern data tooling.",
    },
    {
        "title": "IT Internship",
        "year": "2025",
        "org": "Petrobel",
        "desc": "Practical experience supporting IT systems and data operations.",
    },
]

# ------------------------------------------------------------------ #
#  Helpers
# ------------------------------------------------------------------ #
def img_b64(rel_path: str) -> str:
    path = BASE / rel_path
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode()


def html(block: str):
    """Render raw HTML (strip indentation/blank lines so Markdown doesn't treat it as code)."""
    cleaned = "\n".join(line.strip() for line in block.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def section_title(num: str, title: str, anchor: str):
    html(f"""
    <div id="{anchor}" class="anchor"></div>
    <div class="section-title"><span class="num">{num}</span><span class="grad">{title}</span></div>
    <div class="underline"></div>
    """)


# ------------------------------------------------------------------ #
#  Styles
# ------------------------------------------------------------------ #
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root{
  --bg:#07070f; --card:rgba(255,255,255,0.03); --border:rgba(255,255,255,0.08);
  --text:#f1f1f6; --muted:#8b8fa8; --cyan:#22d3ee; --blue:#38bdf8; --purple:#a855f7;
  --grad:linear-gradient(90deg,#22d3ee 0%,#6366f1 60%,#a855f7 100%);
}

html, body, [class*="css"], .stApp{ font-family:'Inter',sans-serif; color:var(--text); }
.stApp{
  background:
    radial-gradient(circle at 1px 1px, rgba(129,140,248,.28) 1px, transparent 0) 0 0/46px 46px,
    radial-gradient(900px 500px at 85% 10%, rgba(168,85,247,.12), transparent 60%),
    radial-gradient(800px 500px at 0% 40%, rgba(34,211,238,.08), transparent 60%),
    var(--bg);
}
#MainMenu, footer, header[data-testid="stHeader"]{ visibility:hidden; height:0; }
[data-testid="stSidebar"], [data-testid="collapsedControl"]{ display:none; }
.block-container{ max-width:1000px; padding:4.5rem 1.4rem 3rem 1.4rem !important; }
html{ scroll-behavior:smooth; }

.anchor{ position:relative; top:-90px; visibility:hidden; height:0; }

/* ---------- navbar ---------- */
.navbar{
  position:fixed; top:0; left:0; right:0; z-index:999;
  display:flex; align-items:center; justify-content:space-between;
  padding:16px 28px; backdrop-filter:blur(14px);
  background:rgba(7,7,15,.78); border-bottom:1px solid var(--border);
}
.logo{ font-family:'JetBrains Mono',monospace; font-size:1.35rem; color:#fff; text-decoration:none; }
.logo .chev{ color:var(--cyan); margin-right:10px; }
.logo .dot{ color:var(--purple); }
.nav-links a{
  color:var(--muted); text-decoration:none; margin-left:26px; font-weight:500; font-size:.95rem;
  transition:color .2s;
}
.nav-links a:hover{ color:#fff; }

/* ---------- hero ---------- */
.hero{ padding:40px 0 20px 0; display:flex; flex-wrap:wrap; align-items:center; gap:40px; justify-content:space-between; }
.hero-text{ flex:1 1 420px; }
.badge{
  display:inline-flex; align-items:center; gap:10px; padding:10px 18px;
  border:1px solid var(--border); background:var(--card); border-radius:999px;
  color:#cfd2e4; font-size:.95rem; margin-bottom:26px;
}
.badge .spark{ color:var(--cyan); }
.hero h1{ font-size:clamp(2.8rem,7vw,4.6rem); font-weight:800; line-height:1.05; margin:0 0 6px 0; letter-spacing:-1px; }
.grad{ background:var(--grad); -webkit-background-clip:text; background-clip:text; color:transparent; }
.hero h2{ font-size:1.7rem; font-weight:500; color:#e6e7f2; margin:18px 0 14px 0; }
.hero p{ color:var(--muted); font-size:1.15rem; line-height:1.7; max-width:560px; }
.hero-avatar {
width: 280px;
height: 280px;
border-radius: 50%;
border: 4px solid var(--cyan);
box-shadow: 0 0 30px var(--cyan);
overflow: hidden;
flex-shrink: 0;
}
.hero-avatar img {
width: 100%;
height: 100%;
object-fit: cover;
}
.btns{ display:flex; flex-wrap:wrap; gap:16px; margin-top:30px; }
.btn{
  padding:16px 30px; border-radius:999px; font-weight:600; text-decoration:none !important;
  font-size:1.02rem; transition:transform .2s, box-shadow .2s;
}
.btn:hover{ transform:translateY(-3px); }
.btn-primary{ background:var(--grad); color:#0a0a14 !important; box-shadow:0 10px 30px rgba(99,102,241,.35); }
.btn-ghost{ border:1px solid var(--border); color:#fff !important; background:var(--card); }

.photo-wrap{
  flex:0 1 380px; display:flex; justify-content:center; position:relative;
}
.photo-wrap::before{
  content:""; position:absolute; inset:-30px; border-radius:50%;
  background:radial-gradient(circle, rgba(99,102,241,.45), transparent 65%); filter:blur(30px);
}
.photo{
  position:relative; width:330px; height:330px; border-radius:50%; padding:6px;
  background:var(--grad);
}
.photo div{
  width:100%; height:100%; border-radius:50%; border:6px solid #000; overflow:hidden; background:#fff;
}
.photo img{ width:100%; height:100%; object-fit:cover; object-position:50% 38%; }

/* ---------- sections ---------- */
.section-title{ display:flex; align-items:baseline; gap:18px; margin-top:90px; font-size:2.4rem; font-weight:800; }
.section-title .num{ font-family:'JetBrains Mono',monospace; color:rgba(168,85,247,.28); font-size:2.6rem; }
.underline{ width:140px; height:3px; background:var(--grad); border-radius:3px; margin:14px 0 34px 0; }
.about-text{ color:var(--muted); font-size:1.15rem; line-height:1.85; }

.card{
  background:var(--card); border:1px solid var(--border); border-radius:26px;
  padding:34px 36px; transition:transform .25s, border-color .25s;
}
.card:hover{ border-color:rgba(129,140,248,.4); transform:translateY(-3px); }
.card h3{ margin:0 0 12px 0; font-size:1.75rem; font-weight:700; line-height:1.25; }
.card .school{ color:var(--cyan); font-size:1.15rem; margin-bottom:18px; }
.pill{
  display:inline-block; padding:6px 16px; border:1px solid var(--border); border-radius:999px;
  font-family:'JetBrains Mono',monospace; font-size:.9rem; color:#a9adc4; background:rgba(255,255,255,.02);
}
.sub-title{ display:flex; align-items:center; gap:14px; font-size:1.6rem; font-weight:700; margin:54px 0 22px 0; }
.sub-title .ic{ color:var(--purple); }

.cert{ border-radius:22px; overflow:hidden; border:1px solid var(--border); max-width:520px; }
.cert img{ width:100%; display:block; }
.cert-cap{ color:var(--muted); margin-top:10px; font-size:.95rem; }

.skills{ display:flex; flex-wrap:wrap; gap:12px; }
.skill{
  padding:10px 20px; border-radius:999px; border:1px solid var(--border); background:var(--card);
  font-family:'JetBrains Mono',monospace; font-size:.95rem; color:#dfe1f0;
}
.projects{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:22px; margin-top:26px; }
.projects .card{ padding:26px 28px; }
.projects h3{ font-size:1.3rem; }
.projects p{ color:var(--muted); line-height:1.65; }
.tags{ display:flex; flex-wrap:wrap; gap:8px; margin:14px 0; }
.link{ color:var(--cyan) !important; text-decoration:none !important; font-weight:600; }

/* ---------- timeline ---------- */
.timeline{ position:relative; padding-left:62px; }
.timeline::before{
  content:""; position:absolute; left:11px; top:8px; bottom:8px; width:2px; background:var(--border);
}
.t-item{ position:relative; margin-bottom:46px; }
.t-item::before{
  content:""; position:absolute; left:-62px; top:6px; width:24px; height:24px; border-radius:50%;
  background:linear-gradient(135deg,#22d3ee,#a855f7);
}
.t-head{ display:flex; flex-wrap:wrap; align-items:center; gap:14px; }
.t-head h3{ margin:0; font-size:1.5rem; font-weight:700; }
.t-org{ color:var(--cyan); font-size:1.15rem; margin:14px 0 8px 0; }
.t-desc{ color:var(--muted); font-size:1.08rem; line-height:1.7; }

/* ---------- contact ---------- */
.contact-intro{ color:var(--muted); font-size:1.15rem; line-height:1.7; margin-bottom:26px; }
.c-card{
  display:flex; align-items:center; gap:22px; padding:20px 26px; margin-bottom:16px;
  background:var(--card); border:1px solid var(--border); border-radius:24px;
  text-decoration:none !important; transition:transform .25s, border-color .25s;
}
.c-card:hover{ transform:translateX(6px); border-color:rgba(129,140,248,.5); }
.c-icon{
  width:68px; height:68px; border-radius:20px; display:flex; align-items:center; justify-content:center;
  background:linear-gradient(135deg,#22d3ee,#a855f7); font-size:1.7rem; flex-shrink:0;
}
.c-info{ flex:1; min-width:0; }
.c-label{ color:var(--muted); font-size:.85rem; letter-spacing:2px; text-transform:uppercase; }
.c-value{ color:#fff; font-size:1.25rem; font-weight:500; word-break:break-all; }
.c-arrow{ color:var(--muted); font-size:1.5rem; }

.footer{ text-align:center; color:var(--muted); margin-top:70px; padding-top:26px; border-top:1px solid var(--border); font-size:.95rem; }

@media (max-width:700px){
  .nav-links{ display:none; }
  .photo{ width:260px; height:260px; }
  .section-title{ font-size:1.9rem; margin-top:70px; }
  .card{ padding:26px 24px; }
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ------------------------------------------------------------------ #
#  Navbar
# ------------------------------------------------------------------ #
html(f"""
<div class="navbar">
  <a class="logo" href="#top"><span class="chev">&gt;</span>{NAME_FIRST}<span class="dot">.{NAME_LAST}</span></a>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#education">Education</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#contact">Contact</a>
  </div>
</div>
<div id="top" class="anchor"></div>
""")

# ------------------------------------------------------------------ #
#  Hero
# ------------------------------------------------------------------ #
with open("assets/profile.jpg", "rb") as f:
photo = base64.b64encode(f.read()).decode()

html(f"""
<div class="hero">
  <div class="hero-text">
    <div class="badge"><span class="spark">✦</span> Data Engineer</div>
    <h1>Hi! I'm<br><span class="grad">Martina Emad</span></h1>
    <h2>Welcome to My Data Engineering World!</h2>
    <p>Building scalable data architectures and pipelines. Transforming raw data into
       actionable intelligence with logic and technical precision.</p>
    <div class="btns">
      <a class="btn btn-primary" href="#contact">Get in Touch! →</a>
      <a class="btn btn-ghost" href="#projects">View Projects</a>
    </div>
  </div>
<div class="photo-wrap"><div class="photo"><img src="data:image/jpeg;base64,{photo}"></div></div>
</div>
""")

# ------------------------------------------------------------------ #
#  01 About
# ------------------------------------------------------------------ #
section_title("01", "About Me", "about")
html(f'<div class="about-text">{ABOUT}</div>')

# ------------------------------------------------------------------ #
#  02 Education + Certifications
# ------------------------------------------------------------------ #
section_title("02", "Education", "education")
html(f"""
<div class="card">
  <h3>{EDUCATION['degree']}</h3>
  <div class="school">{EDUCATION['school']}</div>
  <span class="pill">{EDUCATION['years']}</span>
</div>
<div class="sub-title"><span class="ic">🏅</span>Certifications</div>
""")

for cert in CERTIFICATES:
    data = img_b64(cert["image"])
    if data:
        html(f"""
        <div class="cert"><img src="data:image/jpeg;base64,{data}" alt="{cert['title']}"></div>
        <div class="cert-cap">{cert['title']}</div>
        """)

# ------------------------------------------------------------------ #
#  03 Skills & Projects
# ------------------------------------------------------------------ #
section_title("03", "Skills & Projects", "projects")
skills_html = "".join(f'<span class="skill">{s}</span>' for s in SKILLS)
html(f'<div class="skills">{skills_html}</div>')

cards = ""
for p in PROJECTS:
    tags = "".join(f'<span class="pill">{t}</span>' for t in p["tags"])
    cards += f"""
    <div class="card">
      <h3>{p['title']}</h3>
      <p>{p['desc']}</p>
      <div class="tags">{tags}</div>
      <a class="link" href="{p['link']}" target="_blank">View on GitHub ↗</a>
    </div>
    """
html(f'<div class="projects">{cards}</div>')

# ------------------------------------------------------------------ #
#  04 Training & Experience
# ------------------------------------------------------------------ #
section_title("04", "Training & Experience", "experience")
items = ""
for e in EXPERIENCE:
    items += f"""
    <div class="t-item">
      <div class="t-head"><h3>{e['title']}</h3><span class="pill">{e['year']}</span></div>
      <div class="t-org">{e['org']}</div>
      <div class="t-desc">{e['desc']}</div>
    </div>
    """
html(f'<div class="timeline">{items}</div>')

# ------------------------------------------------------------------ #
#  05 Contact
# ------------------------------------------------------------------ #
section_title("05", "Get In Touch", "contact")

contacts = [
    ("✉️", "Email", EMAIL, f"mailto:{EMAIL}"),
    ("in", "LinkedIn", "LinkedIn Profile", LINKEDIN_URL),
    ("⌥", "GitHub", "GitHub Profile", GITHUB_URL),
    ("💬", "WhatsApp", PHONE, WHATSAPP_LINK),
]
c_html = ""
for icon, label, value, link in contacts:
    c_html += f"""
    <a class="c-card" href="{link}" target="_blank">
      <div class="c-icon">{icon}</div>
      <div class="c-info"><div class="c-label">{label}</div><div class="c-value">{value}</div></div>
      <div class="c-arrow">↗</div>
    </a>
    """
html(f"""
<div class="contact-intro">Ready to turn your data into valuable insights? Let's connect and
collaborate to achieve your data engineering goals.</div>
{c_html}
<div class="footer">© 2026 Martina Emad · Built with Streamlit</div>
""")
