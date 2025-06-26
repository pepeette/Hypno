import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
:root {
    /* Color Palette */
    --primary: #1C1C1E;       /* Main text/dark elements */
    --accent: #D4AF37;        /* Gold for highlights */
    --light: #F4F4F6;         /* Background */
    --medium: #E2E2E6;        /* Borders */
    --muted: #6E6E73;         /* Secondary text */
    --white: #FFFFFF;         /* Cards */
}

/* Base Styles */
.stApp {
    font-family: 'Inter', sans-serif;
    background: var(--light);
    color: var(--primary);
    line-height: 1.6;
    padding: 1rem;
}

/* Typography */
.h1 { font-size: 2rem; font-weight: 700; line-height: 1.2; }
.h2 { font-size: 1.75rem; font-weight: 600; margin: 2rem 0 1rem; }
.h3 { font-size: 1.5rem; font-weight: 600; margin: 1.5rem 0 0.75rem; }
.body { font-size: 1.05rem; color: var(--primary); }
.muted { color: var(--muted); }

/* Cards */
.card {
    background: var(--white);
    border: 1px solid var(--medium);
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.card-accent {
    border-left: 4px solid var(--accent);
}

/* Buttons */
.btn {
    background: var(--accent);
    color: var(--primary);
    padding: 0.8rem 2rem;
    border-radius: 6px;
    font-weight: 600;
    display: inline-block;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(212, 175, 55, 0.2);
    margin: 0.5rem 0;
    text-decoration: none;
}
.btn:hover {
    background: #C7A133;
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
}

/* Hero Section */
.hero {
    background: var(--primary);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    border-radius: 12px;
    margin-bottom: 3rem;
    border-left: 6px solid var(--accent);
}

/* Navigation */
.nav {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 2rem 0;
}
.nav-item {
    font-weight: 600;
    color: var(--muted);
    padding-bottom: 0.5rem;
    border-bottom: 2px solid transparent;
    cursor: pointer;
    transition: all 0.3s ease;
}
.nav-item.active {
    color: var(--primary);
    border-color: var(--accent);
}
.nav-item:hover {
    color: var(--primary);
}

/* Stats Grid */
.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}
.stat {
    background: var(--white);
    border: 1px solid var(--medium);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
}
.stat-number {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--accent);
}
.stat-label {
    font-size: 0.9rem;
    color: var(--muted);
}

/* Contact Card */
.contact {
    background: var(--primary);
    color: white;
    padding: 3rem;
    border-radius: 12px;
    margin: 3rem 0;
    border-top: 4px solid var(--accent);
}

/* Utility Classes */
.text-center { text-align: center; }
.mt-1 { margin-top: 1rem; }
.mt-2 { margin-top: 2rem; }
.mb-1 { margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <h1 class="h1">The Expat's Dilemma</h1>
    <p class="h2 muted">You sacrificed everything for this Bangkok career - so why does success feel like wearing someone else's skin?</p>
    <a href="#contact" class="btn">🧠 Yes, I Want My Breakthrough Session →</a>
    <p class="muted mt-1">Neuroscience-backed | Confidential | 13 years in Asian markets</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown('<div class="nav">', unsafe_allow_html=True)
tabs = [("🔥 Your Blocks", "problems"), ("🧠 The Method", "method"), ("🏆 Results", "results"), ("👤 About", "about")]
for label, page_name in tabs:
    active = "active" if st.session_state.page == page_name else ""
    st.markdown(f'<div class="nav-item {active}" onclick="window.streamlitSessionState.set({page_name: true})">{label}</div>', 
                unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE CONTENT ---
def show_problems():
    st.markdown('<h2 class="h2">The Hidden Blocks We Solve</h2>', unsafe_allow_html=True)
    
    problems = [
        {
            "title": "The Bangkok Glass Ceiling", 
            "desc": "You deliver exceptional work but get passed over for promotions. Your Western directness is suddenly 'too aggressive', while local colleagues advance with half your output.",
            "result": "→ Rewire unconscious self-sabotage and cultural blind spots"
        },
        {
            "title": "The Stress-Weight Spiral", 
            "desc": "Late-night moo ping binges after stressful meetings. Gym memberships gathering dust. That 'temporary' 10kg now feels permanent.",
            "result": "→ Reset your metabolic programming without another fad diet"
        },
        {
            "title": "Performance Anxiety", 
            "desc": "You nailed presentations in London/NYC - but here, your mind blanks mid-sentence. The harder you try to impress, the more you underwhelm.",
            "result": "→ Install bulletproof confidence tailored to Asian boardrooms"
        }
    ]
    
    for p in problems:
        st.markdown(f"""
        <div class="card card-accent">
            <h3 class="h3">{p['title']}</h3>
            <p class="body">{p['desc']}</p>
            <p class="body" style="color: var(--accent); border-top: 1px dashed var(--medium); padding-top: 1rem;">
                {p['result']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="h2 mt-2">Why It Works</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats">
        <div class="stat">
            <div class="stat-number">2</div>
            <div class="stat-label">Sessions for breakthrough</div>
        </div>
        <div class="stat">
            <div class="stat-number">92%</div>
            <div class="stat-label">Report improvement</div>
        </div>
        <div class="stat">
            <div class="stat-number">5-7x</div>
            <div class="stat-label">Faster than therapy</div>
        </div>
        <div class="stat">
            <div class="stat-number">0</div>
            <div class="stat-label">Ongoing sessions</div>
        </div>
    </div>
    
    <div class="text-center mt-2">
        <a href="#contact" class="btn">🚨 Only 3 Spots Left This Month →</a>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown('<h2 class="h2">Why 2 Sessions Work When Nothing Else Did</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3 class="h3">Traditional Therapy Failed You Because:</h3>
        <ul class="body">
            <li>It talks <em>about</em> problems instead of rewriting them</li>
            <li>Progress gets derailed by Bangkok's 60-hour work weeks</li>
            <li>Western methods don't address Asian business culture nuances</li>
        </ul>
    </div>
    
    <div class="card card-accent mt-2">
        <div style="display: flex; align-items: start; gap: 1.5rem;">
            <div style="background: var(--accent); color: var(--primary); width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; font-weight: bold;">1</div>
            <div>
                <h3 class="h3">Session 1: Pattern Mapping</h3>
                <p class="body">We identify the <em>exact</em> neural circuits causing your blocks using fMRI-inspired techniques</p>
            </div>
        </div>
    </div>
    
    <div class="card card-accent mt-1">
        <div style="display: flex; align-items: start; gap: 1.5rem;">
            <div style="background: var(--accent); color: var(--primary); width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; font-weight: bold;">2</div>
            <div>
                <h3 class="h3">Session 2: Neural Rewiring</h3>
                <p class="body">Precision hypnotherapy to install new patterns that withstand Bangkok's pressures</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<h2 class="h2">Client Transformations</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent">
        <p class="body"><em>"After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."</em></p>
        <p class="body" style="font-weight: 600;">— French Tech Director, Fortune 500</p>
    </div>
    
    <div class="card card-accent mt-1">
        <p class="body"><em>"The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."</em></p>
        <p class="body" style="font-weight: 600;">— American PE VP, Bangkok</p>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
    with col2:
        st.markdown('<h2 class="h2">About Laetitia</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="body">
            <p><strong>Bangkok-based specialist</strong> with 13 years in Asian financial hubs (Hong Kong, Singapore, Bangkok)</p>
            <p>Understands the unique pressures of:</p>
            <ul>
                <li>Expat stress meets career ambition</li>
                <li>Thai business culture nuances</li>
                <li>Metabolic impact of Bangkok's environment</li>
            </ul>
            <p>Fellow expat who cracked the code after my own breakdown in Hong Kong</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact" id="contact">
        <div class="text-center">
            <h3 class="h3" style="color: white;">Bangkok Hypnotherapy Clinic</h3>
            <p class="body" style="color: white; margin-bottom: 1.5rem;">46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
            <a href="#" class="btn">📍 Get Directions</a>
            <a href="#" class="btn">📅 Book Discovery Call</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN CONTENT ---
if st.session_state.page == "problems":
    show_problems()
elif st.session_state.page == "method":
    show_method()
elif st.session_state.page == "results":
    show_results()
elif st.session_state.page == "about":
    show_about()

# --- FOOTER ---
st.markdown("""
<div class="text-center muted mt-2">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
