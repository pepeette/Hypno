import streamlit as st

# --- PAGE CONTENT FUNCTIONS (MOVED TO TOP) ---
def show_problems():
    st.markdown('<h2 class="section-title">The Hidden Blocks We Solve</h2>', unsafe_allow_html=True)
    
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
            "title": "Performance Anxiety & Imposter Syndrome", 
            "desc": "You know your stuff, but anxiety strikes before meetings, keynotes, or career moves. Confidence feels manufactured.",
            "result": "→ Install bulletproof confidence tailored to Asian boardrooms"
        },
        {
            "title": "Perfectionism That Leads to Burnout", 
            "desc": "You overwork, overcontrol, and can't switch off. Your team feels it. So does your nervous system.",
            "result": "→ Rewire for strategic focus — make high-impact decisions without the mental overload"
        }
    ]
    
    for p in problems:
        st.markdown(f"""
        <div class="card card-accent">
            <h3 class="card-title">{p['title']}</h3>
            <p class="body-text">{p['desc']}</p>
            <p class="problem-result">
                {p['result']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title mt-2">Why It Works</h2>', unsafe_allow_html=True)
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
        <button class="btn">🚨 Only 3 Spots Left This Month →</button>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown('<h2 class="section-title">Why 2 Sessions Work When Nothing Else Did</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3 class="card-title">Traditional Therapy Failed You Because:</h3>
        <ul class="body-text">
            <li>It talks <em>about</em> problems instead of rewriting them</li>
            <li>Progress gets derailed by Bangkok's 60-hour work weeks</li>
            <li>Western methods don't address Asian business culture nuances</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent mt-2">
        <div class="process-step">
            <div class="step-number">1</div>
            <div>
                <h3 class="card-title">Session 1: Pattern Mapping</h3>
                <p class="body-text">We identify the <em>exact</em> neural circuits causing your blocks using fMRI-inspired techniques</p>
            </div>
        </div>
    </div>
    
    <div class="card card-accent mt-1">
        <div class="process-step">
            <div class="step-number">2</div>
            <div>
                <h3 class="card-title">Session 2: Neural Rewiring</h3>
                <p class="body-text">Precision hypnotherapy to install updated, unconscious patterns that withstand high stress</p>
            </div>
        </div>
    </div>

    <div class="card card-accent mt-2">
        <div class="process-step">
            <div class="step-number">3</div>
            <div>
                <h3 class="card-title">Session 3: Reinforcement (Optional) </h3>
                <p class="body-text">Booster session to ensure performance under ongoing pressure.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<h2 class="section-title">Client Transformations</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent">
        <p class="body-text"><em>"After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."</em></p>
        <p class="body-text" style="font-weight: 600; margin-top: 1rem;">— French Tech Director, Fortune 500</p>
    </div>
    
    <div class="card card-accent mt-1">
        <p class="body-text"><em>"The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."</em></p>
        <p class="body-text" style="font-weight: 600; margin-top: 1rem;">— American PE VP, Bangkok</p>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.markdown('<div style="width: 250px; height: 300px; background: var(--medium); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--muted);">Profile Image</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h2 class="section-title">About Laetitia</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="body-text">
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
    <div class="contact">
        <h3 style="color: white; font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">Bangkok Hypnotherapy Clinic</h3>
        <p style="color: white; margin-bottom: 1.5rem;">46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
        <button class="btn">📍 Get Directions</button>
        <button class="btn">📅 Book Discovery Call</button>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS INJECTION ---
def inject_css():
    st.markdown(f"""
    <style>
    :root {{
        --primary: #1C1C1E;
        --accent: #D4AF37;
        --light: #F4F4F6;
        --medium: #E2E2E6;
        --muted: #6E6E73;
        --white: #FFFFFF;
        --shadow: rgba(0,0,0,0.05);
        --shadow-hover: rgba(0,0,0,0.1);
        --shadow-accent: rgba(212, 175, 55, 0.2);
    }}

    /* Menu Buttons Container */
    .menu-buttons {{
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 1rem auto 2rem auto;
        max-width: 1200px;
        padding: 0 1rem;
    }}

    /* Menu Button Style */
    .menu-btn {{
        background: var(--primary) !important;
        border: none !important;
        color: var(--white) !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.5rem 1rem !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
        min-height: auto !important;
        height: auto !important;
        flex: 1;
    }}

    .menu-btn:hover {{
        background: rgba(255, 255, 255, 0.1) !important;
    }}

    .menu-btn.active {{
        background: var(--accent) !important;
        color: var(--primary) !important;
        box-shadow: 0 2px 8px var(--shadow-accent) !important;
    }}

    /* Rest of your existing CSS... */
    .stApp {{
        background: var(--light) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        line-height: 1.6;
        color: var(--primary) !important;
    }}

    /* Stats Numbers - Gold Color */
    .stat-number {{
        color: var(--accent) !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
    }}

    /* Problem Result Arrows - Gold Color */
    .problem-result {{
        color: var(--accent) !important;
        border-top: 1px dashed var(--medium) !important;
        padding-top: 1rem !important;
        margin-top: 1rem !important;
    }}

    /* Process Steps */
    .process-step {{
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }}
    
    .step-number {{
        background: var(--accent);
        color: var(--primary);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
    }}

    /* Rest of your CSS remains the same... */
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION WITH MENU BUTTONS ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1 class="hero-title">Rewire what's holding you back - in 2 sessions</h1>
    <p class="hero-subtitle">Life keeps moving fast, but you are feeling blocked. <br>
    It is not definite, it is a neuro-programming session you need to activate.</p>
    <div style="margin-top: 1rem;">
        <a href="https://calendly.com/titre/free-session" target="_blank">
            <button class="btn">📅 Book a FREE 15-min Call to if you are fit for it</button>
        </a>
    </div>
    <p class="muted-text mt-1">Neuroscience-backed | Confidential | 13 years in Asian markets</p>
</div>

<div class="menu-buttons">
    <button class="menu-btn {'active' if st.session_state.page == 'problems' else ''}" onclick="window.streamlitSessionState.set('page', 'problems')">🔥 Your Blocks</button>
    <button class="menu-btn {'active' if st.session_state.page == 'method' else ''}" onclick="window.streamlitSessionState.set('page', 'method')">🧠 The Method</button>
    <button class="menu-btn {'active' if st.session_state.page == 'results' else ''}" onclick="window.streamlitSessionState.set('page', 'results')">🏆 Results</button>
    <button class="menu-btn {'active' if st.session_state.page == 'about' else ''}" onclick="window.streamlitSessionState.set('page', 'about')">👤 About</button>
</div>
""", unsafe_allow_html=True)

# --- PAGE CONTENT ---
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
<div class="text-center muted-text mt-2" style="border-top: 1px solid var(--medium); padding-top: 2rem; margin-top: 3rem;">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
</div>
""", unsafe_allow_html=True)
