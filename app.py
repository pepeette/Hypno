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
    
    /* Typography Hierarchy */
    h1 {{
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin: 2rem 0 1rem 0 !important;
        color: var(--primary) !important;
    }}
    
    h2 {{
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
        margin: 1.5rem 0 1rem 0 !important;
        color: var(--primary) !important;
    }}
    
    p, li, span, div {{
        font-size: 1rem !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        color: var(--primary) !important;
        margin: 0.5rem 0 !important;
    }}
    
    strong, b {{
        font-weight: 600 !important;
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
        font-size: 1.5rem !important; 
        font-weight: 700 !important; 
        line-height: 1.2 !important; 
        margin: 0 !important;
        color: var(--white) !important;
    }}
    
    .hero-subtitle {{ 
        font-size: 1rem !important; 
        font-weight: 400 !important; 
        margin: 1rem 0 !important;
        color: #d1d1d6 !important;
    }}
    
    .muted-text {{ 
        color: var(--muted) !important; 
        font-size: 1rem !important;
        font-weight: 400 !important;
    }}

    .hero {{
        background: var(--primary);
        color: white;
        padding: 1.5rem 1.5rem;
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

    .nav-btn-active {{
        background: var(--accent) !important;
        color: var(--primary) !important;
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
    
    .contact h2 {{
        color: var(--white) !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    .contact p {{
        color: var(--white) !important;
        margin-bottom: 1.5rem !important;
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
    It is not definite, it is a neural pathway that needs to be reprogrammed.</p>
    <button class="btn">📅 Book a FREE 15-min Call to see if you're fit for it</button>
    <p class="muted-text mt-1">Neuroscience-backed | Confidential | 13 years in Asian markets</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS ---
cols = st.columns(4)
with cols[0]:
    problems_btn = st.button("🔥 Your Blocks", key="nav_problems", 
                            help="View common problems we solve",
                            type="primary" if st.session_state.page == "problems" else "secondary")
    if problems_btn:
        st.session_state.page = "problems"
        st.rerun()

with cols[1]:
    method_btn = st.button("🧠 The Method", key="nav_method", 
                          help="Learn about our 2-session method",
                          type="primary" if st.session_state.page == "method" else "secondary")
    if method_btn:
        st.session_state.page = "method"
        st.rerun()

with cols[2]:
    results_btn = st.button("🏆 Results", key="nav_results", 
                           help="See client transformations",
                           type="primary" if st.session_state.page == "results" else "secondary")
    if results_btn:
        st.session_state.page = "results"
        st.rerun()

with cols[3]:
    about_btn = st.button("👤 About", key="nav_about", 
                         help="About Laetitia and the clinic",
                         type="primary" if st.session_state.page == "about" else "secondary")
    if about_btn:
        st.session_state.page = "about"
        st.rerun()

# --- PAGE CONTENT FUNCTIONS ---
def show_problems():
    st.markdown('<h1>The Hidden Blocks We Solve</h1>', unsafe_allow_html=True)
    
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
            <h2>{p['title']}</h2>
            <p>{p['desc']}</p>
            <p><strong>{p['result']}</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<h1>Why It Works</h1>', unsafe_allow_html=True)
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
    """, unsafe_allow_html=True)

    # Add FAQ section
    st.markdown('<h2>Questions from Asia-Based Leaders</h2>', unsafe_allow_html=True)
    with st.expander("How is this different from coaching?"):
        st.write("This isn't coaching—it's unconscious neural recalibration. We target the source of performance limits, not just surface habits.")
    with st.expander("Why does it work in 2 sessions?"):
        st.write("Our process is precise and rooted in applied neuroscience. No fluff, no long timelines.")
    with st.expander("Is it confidential?"):
        st.write("100%. Trusted by leaders across Asia. No client data is stored beyond legal minimums.")
    
    st.markdown("""
    <div class="text-center mt-2">
        <button class="btn">🚨 Only 3 Spots Left This Month →</button>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown('<h1>Why 2 Sessions Work When Nothing Else Did</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h2>Traditional Therapy Failed You Because:</h2>
        <ul>
            <li>It talks <em>about</em> problems instead of rewriting them</li>
            <li>Progress gets derailed by Bangkok's 60-hour work weeks</li>
            <li>Western methods don't address Asian business culture nuances</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent">
        <div class="process-step">
            <div class="step-number">1</div>
            <div>
                <h2>Session 1: Pattern Mapping</h2>
                <p>We identify the <em>exact</em> neural circuits causing your blocks using fMRI-inspired techniques</p>
            </div>
        </div>
    </div>
    
    <div class="card card-accent">
        <div class="process-step">
            <div class="step-number">2</div>
            <div>
                <h2>Session 2: Neural Rewiring</h2>
                <p>Precision hypnotherapy to install new patterns that withstand Bangkok's pressures</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<h1>Client Transformations</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent">
        <p><em>"After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."</em></p>
        <p><strong>— French Tech Director, Fortune 500</strong></p>
    </div>
    
    <div class="card card-accent">
        <p><em>"The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."</em></p>
        <p><strong>— American PE VP, Bangkok</strong></p>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    st.markdown('<h2>Your certified therapist</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.info("Image not found")
    
    with col2:
        st.markdown("""
        **Experience Across Asia's Financial Hubs**
        - 13+ years on trading floors: Bloomberg, HSBC, CA Indosuez
        - Managed $50M book, coached 48-person teams in 12 countries, cross led 2500 employee performance
        
        **Credentials:**
        - Certified Behavioral Performance Specialist & Hypnotherapy (UK, 2017)
        - Certified Neuroscience Coach (Dialectical Behavioral Therapy, 2024)
        - Fluent: English, French, Spanish, Italian
        """)
    
    st.markdown("""
    <div class="contact">
        <h2>Bangkok Hypnotherapy Clinic</h2>
        <p>46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
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
