import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Hypnotherapy for Behavioral Change | Laetitia Sheppard",
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
        --shadow-hover: rgba(0,0,0,0.15);
        --shadow-accent: rgba(212, 175, 55, 0.25);
    }}
    /* Force light mode */
    [data-testid="stAppViewContainer"] {{
        background-color: var(--light) !important;
        color-scheme: light !important;
    }}
    .stApp {{
        background: var(--light) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        line-height: 1.6;
        color: var(--primary) !important;
        padding-top: 0.25rem !important;
    }}
    /* Remove header space and menus */
    .st-emotion-cache-1avcm0n, .st-emotion-cache-z5fcl4 {{
        display: none !important;
        padding-top: 0.25rem !important;
        padding-bottom: 0.25rem !important;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: var(--primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }}
    h1 {{
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin: 0.5rem 0 !important;
    }}
    h2 {{
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        margin: 0.6rem 0 !important;
    }}
    p, li, span, div {{
        font-size: 1rem !important;
        line-height: 1.6 !important;
        margin: 0.3rem 0 !important;
    }}
    strong, b {{ font-weight: 600 !important; }}
    #MainMenu, footer, header, .stDeployButton {{ visibility: hidden; }}
    .main-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }}
    .hero-title {{ font-size: 1.5rem !important; margin: 0 !important; color: var(--white) !important; }}
    .hero-subtitle {{ font-size: 1rem !important; margin: 1rem 0 !important; color: #d1d1d6 !important; }}
    .muted-text {{ color: var(--muted) !important; font-size: 1rem !important; }}
    .hero {{
        background: var(--primary);
        color: white;
        padding: 1rem;
        text-align: center;
        border-radius: 12px;
        margin: 0.25rem 0;
        border-left: 6px solid var(--accent);
    }}
    .hero * {{ color: var(--white) !important; }}
    .hero .hero-subtitle {{ color: #d1d1d6 !important; }}
    .hero .muted-text {{ color: #a1a1a6 !important; }}

    /* Stats Section */
    .stats {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.75rem;
        margin: 1rem 0 2rem 0;
    }}
    .stat {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1.5rem 1rem;
        text-align: center;
        box-shadow: 0 4px 12px var(--shadow);
        transition: all 0.3s ease;
    }}
    .stat:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 16px var(--shadow-hover);
    }}
    .stat-number {{
        color: var(--accent) !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        margin: 0.5rem 0 !important;
        line-height: 1 !important;
    }}
    .stat-label {{
        font-size: 1rem !important;
        color: var(--muted) !important;
        margin: 0.5rem 0 0 0 !important;
    }}

    /* Card Layout */
    .card-container {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
    }}
    .card {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1.8rem 2rem;
        margin-bottom: 1rem;
        box-shadow: 0 6px 16px var(--shadow);
        transition: transform 0.4s ease, box-shadow 0.4s ease, background-color 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 220px;
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 28px var(--shadow-hover);
        background-color: #fff9e6;
    }}
    .card h2 {{
        margin-top: 0 !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
        color: var(--primary) !important;
    }}
    .card p {{
        margin: 0.5rem 0 0 0 !important;
        flex-grow: 1;
    }}
    .result-badge {{
        background-color: var(--accent);
        color: var(--primary);
        font-weight: 700;
        padding: 0.25rem 0.8rem;
        margin-top: 1rem;
        border-radius: 8px;
        display: inline-block;
        font-size: 0.9rem;
        align-self: flex-start;
        box-shadow: 0 2px 6px var(--shadow-accent);
        transition: background-color 0.3s ease;
    }}
    .card:hover .result-badge {{
        background-color: #b58f24;
        color: var(--white);
        box-shadow: 0 4px 12px rgba(181, 143, 36, 0.6);
    }}

    /* Button Style */
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
        text-align: center;
        user-select: none;
    }}
    .btn:hover {{
        background: #C7A133;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
    }}

    /* Process Step Icons */
    .process-step {{
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 1rem;
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
        font-size: 1.1rem;
        box-shadow: 0 2px 6px var(--shadow-accent);
    }}

    .card-image-container {{
        margin-top: 1rem;
        border-radius: 8px;
        overflow: hidden;
    }}
    .card-image-container img {{
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s;
    }}
    .card-image-container img:hover {{
        transform: scale(1.02);
    }}

    /* Testimonial Card */
    .testimonial-card {{
        background: var(--white);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid var(--accent);
        box-shadow: 0 4px 12px var(--shadow);
    }}
    .testimonial-icon {{
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
    }}
    .testimonial-quote {{
        font-style: italic;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }}
    .testimonial-author {{
        font-weight: 600;
        text-align: right;
        margin-top: 0.5rem;
    }}

    /* Contact Section */
    .contact {{
        background: var(--primary);
        color: white;
        padding: 1rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-top: 4px solid var(--accent);
        text-align: center;
    }}
    .contact h2 {{
        font-size: 1.2rem !important; font-weight: 600 !important; margin-bottom: 0.5rem !important;
    }}
    .contact p {{ color: var(--white) !important; margin-bottom: 1.5rem !important; }}
    .contact a {{ margin-right: 1rem; }}

    /* Back to Top */
    .back-to-top-link {{
        display: block;
        text-align: center;
        margin-top: 2rem;
        color: var(--accent) !important;
        font-weight: 600;
    }}
    .back-to-top-link:hover {{ text-decoration: underline; }}

    .text-center {{ text-align: center; }}

    /* Responsive */
    @media (max-width: 768px) {{
        .card-container {{ grid-template-columns: 1fr !important; }}
        .stats {{ grid-template-columns: 1fr 1fr !important; }}
        .hero-title {{ font-size: 1.3rem !important; }}
        .hero-subtitle {{ font-size: 0.9rem !important; }}
        [data-testid="column"] {{ min-width: 50% !important; flex: 1 1 50% !important; }}
        .stButton button {{ width: 90% !important; margin: 0.25rem auto !important; }}
    }}
    @media (max-width: 480px) {{
        .stats {{ grid-template-columns: 1fr !important; }}
        [data-testid="column"] {{ min-width: 100% !important; flex: 1 1 100% !important; }}
        .stButton button {{ width: 100% !important; margin: 0.25rem 0 !important; }}
    }}

    /* Sticky Navbar */
    .navbar-sticky {{
        position: sticky;
        top: 0;
        background-color: var(--light);
        z-index: 1000;
        padding: 0.5rem 0;
        border-bottom: 1px solid var(--medium);
    }}

    /* Process Tracker */
    .process-tracker {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 1rem 0;
        gap: 1rem;
        font-weight: 600;
        color: var(--muted);
    }}
    .process-tracker .step {{
        display: flex;
        align-items: center;
    }}
    .process-tracker .arrow {{
        margin: 0 0.5rem;
    }}
    .process-tracker .active {{
        color: var(--accent);
    }}

    /* Section spacing */
    section {{
        margin-top: 2rem;
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
<div class="hero" id="top">
    <h1 class="hero-title">Reprogram Your Mind, Change Your Life</h1>
    <p class="hero-subtitle">Hypnotherapy doesn't just change what you do—it changes how you do it. In just 2 sessions, it reprograms the patterns holding you back, so you can finally get the results you deserve.</p>
    <a href="https://calendly.com/laetitiasheppard/30min" target="_blank">
        <button class="btn">📅 Book a FREE 15-min Call</button>
    </a>
    <p class="muted-text">Expert-guided | Confidential | Certified in Hypnotherapy and DBT</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS (Sticky) ---
st.markdown('<div class="navbar-sticky">', unsafe_allow_html=True)
cols = st.columns(4)
button_style = """
<style>
    @media (max-width: 768px) {
        .stButton>button {
            width: 100%;
            margin: 0.25rem 0;
        }
    }
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)
with cols[0]:
    problems_btn = st.button("🔥 Your Blocks", key="nav_problems",
                            help="View common problems we solve",
                            type="primary" if st.session_state.page == "problems" else "secondary")
    if problems_btn:
        st.session_state.page = "problems"; st.rerun()
with cols[1]:
    method_btn = st.button("🧠 The Method", key="nav_method",
                           help="Learn about our 2-session method",
                           type="primary" if st.session_state.page == "method" else "secondary")
    if method_btn:
        st.session_state.page = "method"; st.rerun()
with cols[2]:
    results_btn = st.button("🏆 Results", key="nav_results",
                            help="See client transformations",
                            type="primary" if st.session_state.page == "results" else "secondary")
    if results_btn:
        st.session_state.page = "results"; st.rerun()
with cols[3]:
    about_btn = st.button("👤 About", key="nav_about",
                          help="About Laetitia and the clinic",
                          type="primary" if st.session_state.page == "about" else "secondary")
    if about_btn:
        st.session_state.page = "about"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- Back to top link ---
def back_to_top():
    st.markdown("""
    <div class="back-to-top-link">
        <a href="#top">↑ Back to Top</a>
    </div>
    """, unsafe_allow_html=True)

# --- IMAGE HANDLING ---
def load_image(image_path, width=None, caption=None):
    try:
        st.image(image_path, width=width, caption=caption, use_container_width=True if width is None else False)
    except FileNotFoundError:
        st.warning(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")

# --- PAGE CONTENT FUNCTIONS ---
def show_problems():
    st.markdown('<section id="problems">', unsafe_allow_html=True)
    st.markdown('<h2>Common Challenges We Help You Overcome</h2>', unsafe_allow_html=True)
    problems = [
        # … same as original …
    ]
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for p in problems:
        st.markdown(f"""
        <div class="card">
            <div class="card-content">
                <h2>{p['title']}</h2>
                <p>{p['desc']}</p>
                <span class="result-badge">{p['result']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # Self-assessment section …
    back_to_top()
    st.markdown('</section>', unsafe_allow_html=True)

def show_method():
    st.markdown('<section id="method">', unsafe_allow_html=True)
    st.markdown('<h2>Our Simple 2-Session Process</h2>', unsafe_allow_html=True)

    # Process tracker
    st.markdown("""
    <div class="process-tracker">
        <div class="step active">1</div>
        <div class="arrow">→</div>
        <div class="step active">2</div>
        <div class="arrow">→</div>
        <div class="step">3 (Optional)</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    # ... same content for the three cards ...
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h2>Why Choose This Approach?</h2>', unsafe_allow_html=True)
    # Stats …
    back_to_top()
    st.markdown('</section>', unsafe_allow_html=True)

def show_results():
    st.markdown('<section id="results">', unsafe_allow_html=True)
    st.markdown('<h2>Real Client Transformations</h2>', unsafe_allow_html=True)
    # … same testimonial cards and form …
    back_to_top()
    st.markdown('</section>', unsafe_allow_html=True)

def show_about():
    st.markdown('<section id="about">', unsafe_allow_html=True)
    st.markdown('<h2>About Laetitia Sheppard</h2>', unsafe_allow_html=True)
    # … profile and contact section …
    back_to_top()
    st.markdown('</section>', unsafe_allow_html=True)

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
<div class="text-center muted-text" style="border-top: 1px solid var(--medium); padding-top: 2rem; margin-top: 3rem;">
    <p>Laetitia Sheppard • Hypnotherapy for Change • Bangkok, Thailand</p>
    <p>© 2025 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
</div>  <!-- Close main-container -->
""", unsafe_allow_html=True)
