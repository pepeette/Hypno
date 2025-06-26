import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS ---
CSS = """
<style>
:root {
    --primary: #1C1C1E;
    --accent: #D4AF37;
    --light: #F4F4F6;
    --medium: #E2E2E6;
    --muted: #6E6E73;
    --white: #FFFFFF;
    --shadow: rgba(0,0,0,0.05);
    --shadow-hover: rgba(0,0,0,0.1);
    --shadow-accent: rgba(212, 175, 55, 0.2);
}
body, .stApp {
    background: var(--light) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--primary) !important;
}
h1, h2, h3, h4, h5, h6, p, li, span, div {
    color: var(--primary) !important;
}
#MainMenu, footer, header, .stDeployButton {
    visibility: hidden;
}
.nav-container {
    display: flex; gap: 0.5rem; padding: 1rem 1rem 0;
}
.nav-btn {
    background: none; border: none; color: var(--white); font-weight: 600;
    font-size: 1rem; padding: 0.5rem 1rem; border-radius: 8px;
    cursor: pointer; transition: all 0.3s ease;
}
.nav-btn:hover {
    background: rgba(255, 255, 255, 0.1);
}
.nav-btn.active {
    background: var(--accent); color: var(--primary);
    box-shadow: 0 2px 8px var(--shadow-accent);
}
.hero {
    background: var(--primary); padding: 2rem; color: var(--white);
    text-align: center; border-radius: 12px; margin: 1rem 0 2rem;
    border-left: 6px solid var(--accent);
}
.card {
    background: var(--white); border: 1px solid var(--medium);
    border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;
    box-shadow: 0 4px 12px var(--shadow);
}
.card-accent {
    border-left: 4px solid var(--accent);
}
.section-title {
    font-size: 1.2rem; font-weight: 600; margin: 2rem 0 1rem;
}
.stats {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem; margin: 2rem 0;
}
.stat-number {
    font-size: 1.5rem; font-weight: 700; color: var(--accent);
}
.contact {
    background: var(--primary); padding: 2rem;
    border-radius: 12px; margin: 2rem 0;
    text-align: center; border-top: 4px solid var(--accent);
    color: var(--white);
}
.btn {
    background: var(--accent); color: var(--primary);
    padding: 0.8rem 1.5rem; border-radius: 8px;
    font-weight: 600; font-size: 1rem;
    margin: 0.5rem 0.5rem 0 0; border: none; cursor: pointer;
    box-shadow: 0 4px 8px var(--shadow-accent);
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# --- SESSION STATE ---
st.session_state.setdefault("page", "problems")

# --- NAVIGATION ---
tabs = [
    ("🔥 Your Blocks", "problems"),
    ("🧠 The Method", "method"),
    ("🏆 Results", "results"),
    ("👤 About", "about"),
]

st.markdown('<div class="nav-container">', unsafe_allow_html=True)
cols = st.columns(len(tabs))
for i, (label, key) in enumerate(tabs):
    with cols[i]:
        active = st.session_state.page == key
        btn_class = "nav-btn active" if active else "nav-btn"
        if st.button(f"<span class='{btn_class}'>{label}</span>", key=f"nav_{key}", help=f"Go to {label}", use_container_width=True):
            st.session_state.page = key
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <h1>The Expat's Dilemma</h1>
    <p>You sacrificed everything for this Bangkok career - so why does success feel like wearing someone else's skin?</p>
    <button class="btn">🧠 Yes, I Want My Breakthrough Session →</button>
    <p class="muted-text mt-1">Neuroscience-backed • Confidential • 13 years in Asian markets</p>
</div>
""", unsafe_allow_html=True)

# --- PAGE FUNCTIONS ---
def show_problems():
    st.markdown('<h2 class="section-title">The Hidden Blocks We Solve</h2>', unsafe_allow_html=True)
    problems = [
        ("The Bangkok Glass Ceiling", "You deliver exceptional work but get passed over...", "→ Rewire unconscious self-sabotage..."),
        ("The Stress-Weight Spiral", "Late-night moo ping binges after stressful meetings...", "→ Reset your metabolic programming..."),
        ("Performance Anxiety", "You nailed presentations in London/NYC - but here...", "→ Install bulletproof confidence...")
    ]
    for title, desc, result in problems:
        st.markdown(f"""
        <div class="card card-accent">
            <h3>{title}</h3>
            <p>{desc}</p>
            <p style="color: var(--accent); border-top: 1px dashed var(--medium); padding-top: 1rem;">
                {result}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Why It Works</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats">
        <div><div class="stat-number">2</div><p>Sessions for breakthrough</p></div>
        <div><div class="stat-number">92%</div><p>Report improvement</p></div>
        <div><div class="stat-number">5-7x</div><p>Faster than therapy</p></div>
        <div><div class="stat-number">0</div><p>Ongoing sessions</p></div>
    </div>
    <div class="text-center"><button class="btn">🚨 Only 3 Spots Left This Month →</button></div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown('<h2 class="section-title">Why 2 Sessions Work When Nothing Else Did</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Traditional Therapy Failed You Because:</h3>
        <ul>
            <li>It talks <em>about</em> problems instead of rewriting them</li>
            <li>Progress gets derailed by Bangkok's 60-hour work weeks</li>
            <li>Western methods don't address Asian business culture nuances</li>
        </ul>
    </div>
    <div class="card card-accent">
        <div class="process-step">
            <div class="step-number">1</div>
            <div><h3>Session 1: Pattern Mapping</h3><p>We identify neural circuits using fMRI-inspired techniques</p></div>
        </div>
    </div>
    <div class="card card-accent">
        <div class="process-step">
            <div class="step-number">2</div>
            <div><h3>Session 2: Neural Rewiring</h3><p>Install new patterns that withstand Bangkok's pressures</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<h2 class="section-title">Client Transformations</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card card-accent">
        <p><em>"After 2 sessions... at the ASEAN summit."</em></p>
        <p><strong>— French Tech Director, Fortune 500</strong></p>
    </div>
    <div class="card card-accent">
        <p><em>"The weight finally started coming off... during high-pressure deals."</em></p>
        <p><strong>— American PE VP, Bangkok</strong></p>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
    with col2:
        st.markdown('<h2 class="section-title">About Laetitia</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p><strong>Bangkok-based specialist</strong> with 13 years in Asian financial hubs</p>
        <ul>
            <li>Expat stress meets career ambition</li>
            <li>Thai business culture nuances</li>
            <li>Metabolic impact of Bangkok</li>
        </ul>
        <p>Fellow expat who cracked the code after my own breakdown in Hong Kong</p>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div class="contact">
        <h3>Bangkok Hypnotherapy Clinic</h3>
        <p>46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
        <button class="btn">📍 Get Directions</button>
        <button class="btn">📅 Book Discovery Call</button>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE ROUTER ---
pages = {
    "problems": show_problems,
    "method": show_method,
    "results": show_results,
    "about": show_about,
}
pages[st.session_state.page]()

# --- FOOTER ---
st.markdown("""
<div class="text-center muted-text mt-2" style="border-top: 1px solid var(--medium); padding-top: 2rem; margin-top: 3rem;">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
