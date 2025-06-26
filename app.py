import streamlit as st

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

    /* Navigation Buttons */
    .nav-buttons {{
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 1.5rem auto 0 auto;
        max-width: 1200px;
    }}

    .nav-btn {{
        background: var(--primary) !important;
        color: var(--white) !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }}

    .nav-btn:hover {{
        background: rgba(255,255,255,0.1) !important;
    }}

    .nav-btn.active {{
        background: var(--accent) !important;
        color: var(--primary) !important;
        box-shadow: 0 2px 8px var(--shadow-accent) !important;
    }}

    /* Rest of your original CSS remains completely unchanged */
    .stApp {{
        background: var(--light) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        line-height: 1.6;
        color: var(--primary) !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: var(--primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }}
    
    h1 {{
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin: 1rem 0 !important;
    }}
    
    h2 {{
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
        margin: 2rem 0 1rem !important;
        color: var(--primary) !important;
    }}
    
    h3 {{
        font-size: 1rem !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
        margin: 1rem 0 0.5rem !important;
        color: var(--primary) !important;
    }}
    
    p, li, span, div {{
        color: var(--primary) !important;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    .main-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }}

    .hero-title {{ 
        font-size: 1.5rem; 
        font-weight: 700; 
        line-height: 1.2; 
        margin: 0;
        color: var(--white) !important;
    }}
    
    .hero-subtitle {{ 
        font-size: 1rem; 
        font-weight: 400; 
        margin: 1rem 0;
        color: #d1d1d6 !important;
    }}
    
    .section-title {{ 
        font-size: 1.2rem; 
        font-weight: 600; 
        margin: 2rem 0 1rem; 
        color: var(--primary);
    }}
    
    .card-title {{ 
        font-size: 1rem; 
        font-weight: 600; 
        margin: 0 0 0.75rem;
        color: var(--primary);
    }}
    
    .body-text {{ 
        font-size: 1rem; 
        color: var(--primary); 
        line-height: 1.6;
        margin: 0.5rem 0;
    }}
    
    .muted-text {{ 
        color: var(--muted); 
        font-size: 1rem;
    }}

    .hero {{
        background: var(--primary);
        color: white;
        padding: 2rem 1.5rem;
        text-align: center;
        border-radius: 12px;
        margin: 0.5rem 0 2rem 0;
        border-left: 6px solid var(--accent);
    }}
    
    .hero * {{
        color: var(--white) !important;
    }}
    
    .hero .hero-subtitle {{ 
        color: #d1d1d6 !important; 
    }}
    
    .hero .muted-text {{ 
        color: #a1a1a6 !important; 
    }}

    .card {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px var(--shadow);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    
    .card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px var(--shadow-hover);
    }}
    
    .card-accent {{
        border-left: 4px solid var(--accent);
    }}

    .btn {{
        background: var(--accent);
        color: var(--primary);
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        display: inline-block;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 8px var(--shadow-accent);
        margin: 0.5rem 0.5rem 0.5rem 0;
        text-decoration: none;
    }}
    
    .btn:hover {{
        background: #C7A133;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
    }}

    .stats {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }}
    
    .stat {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }}
    
    .stat-number {{
        color: var(--accent) !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
    }}
    
    .stat-label {{
        font-size: 1rem;
        color: var(--muted);
    }}

    .contact {{
        background: var(--primary);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin: 2rem 0;
        border-top: 4px solid var(--accent);
        text-align: center;
    }}
    
    .contact * {{
        color: var(--white) !important;
    }}

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

    .text-center {{ text-align: center; }}
    .mt-1 {{ margin-top: 1rem; }}
    .mt-2 {{ margin-top: 2rem; }}
    .mb-1 {{ margin-bottom: 1rem; }}

    @media (max-width: 768px) {{
        .hero {{
            padding: 1.5rem 1rem;
            margin: 0.5rem 0 1.5rem;
        }}
        
        .hero-title {{
            font-size: 1.2rem;
        }}
        
        .hero-subtitle {{
            font-size: 1rem;
        }}
        
        .section-title {{
            font-size: 1.1rem;
        }}
        
        h1 {{
            font-size: 1.2rem !important;
        }}
        
        h2 {{
            font-size: 1.1rem !important;
        }}
        
        h3 {{
            font-size: 1rem !important;
        }}
        
        .card {{
            padding: 1rem;
        }}
        
        .nav-buttons {{
            flex-wrap: wrap;
        }}
        
        .nav-btn {{
            padding: 0.5rem;
            font-size: 0.9rem;
        }}
        
        .stats {{
            grid-template-columns: repeat(2, 1fr);
            gap: 0.75rem;
        }}
        
        .stat {{
            padding: 1rem;
        }}
        
        .process-step {{
            flex-direction: column;
            text-align: center;
        }}
        
        .btn {{
            width: 100%;
            margin: 0.5rem 0;
        }}
    }}

    @media (max-width: 480px) {{
        .hero-title {{
            font-size: 1.1rem;
        }}
        
        h1 {{
            font-size: 1.1rem !important;
        }}
        
        h2 {{
            font-size: 1rem !important;
        }}
        
        .stats {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1 class="hero-title">Rewire what's holding you back - in 2 sessions</h1>
    <p class="hero-subtitle">Life keeps moving fast, but you are feeling blocked.<br>
    It is not definite, it is a neuro-programming session you need to activate.</p>
    <button class="btn">📅 Book a FREE 15-min Call to see if you're fit for it</button>
    <p class="muted-text mt-1">Neuroscience-backed | Confidential | 13 years in Asian markets</p>
</div>

<div class="nav-buttons">
    <button class="nav-btn {'active' if st.session_state.page == 'problems' else ''}" onclick="window.streamlitSessionState.set('page', 'problems')">🔥 Your Blocks</button>
    <button class="nav-btn {'active' if st.session_state.page == 'method' else ''}" onclick="window.streamlitSessionState.set('page', 'method')">🧠 The Method</button>
    <button class="nav-btn {'active' if st.session_state.page == 'results' else ''}" onclick="window.streamlitSessionState.set('page', 'results')">🏆 Results</button>
    <button class="nav-btn {'active' if st.session_state.page == 'about' else ''}" onclick="window.streamlitSessionState.set('page', 'about')">👤 About</button>
</div>
""", unsafe_allow_html=True)

# --- PAGE CONTENT FUNCTIONS ---
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
            "title": "Performance Anxiety", 
            "desc": "You nailed presentations in London/NYC - but here, your mind blanks mid-sentence. The harder you try to impress, the more you underwhelm.",
            "result": "→ Install bulletproof confidence tailored to Asian boardrooms"
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
                <p class="body-text">Precision hypnotherapy to install new patterns that withstand Bangkok's pressures</p>
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
<div class="text-center muted-text mt-2" style="border-top: 1px solid var(--medium); padding-top: 2rem; margin-top: 3rem;">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
</div>
""", unsafe_allow_html=True)
