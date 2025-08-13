import streamlit as st
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Hypnotherapy for Behavioral Change | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS INJECTION ---
def inject_css():
    st.markdown("""
    <style>
    :root {
        --primary: #1C1C1E;
        --accent: #D4AF37;
        --light: #F4F4F6;
        --medium: #E2E2E6;
        --muted: #6E6E73;
        --white: #FFFFFF;
        --shadow: rgba(0,0,0,0.05);
        --shadow-hover: rgba(0,0,0,0.15);
        --shadow-accent: rgba(212, 175, 55, 0.25);
    }
    /* Remove all padding at top */
    html {
        scroll-behavior: smooth;
    }
    body {
        margin: 0;
        padding: 0;
    }
    .stApp {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    /* Remove header completely */
    header {
        display: none !important;
    }
    /* Main container styling */
    .main-container { 
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    /* Hero section at very top */
    #top {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    /* Navigation menu styling */
    div[data-testid="stHorizontalBlock"] {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    /* Process step numbers */
    .step-number {
        background: var(--accent);
        color: var(--primary);
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
        font-size: 1rem;
        margin-right: 0.5rem;
    }
    /* Card expand/collapse */
    .collapsed .card-content {
        display: none;
    }
    .expand-btn {
        background: transparent;
        border: none;
        color: var(--accent);
        cursor: pointer;
        font-weight: 600;
        padding: 0;
        margin-top: 0.5rem;
        text-align: left;
    }
    /* Rest of your CSS */
    [data-testid="stAppViewContainer"] { background-color: var(--light) !important; color-scheme: light !important; }
    #MainMenu, footer, .stDeployButton { visibility: hidden; }
    h1 { font-size: 1.5rem!important; margin: 0.5rem 0!important; }
    h2 { font-size: 1.3rem!important; margin: 0.6rem 0!important; }
    p, li, span, div { font-size: 1rem!important; margin: 0.3rem 0!important; }
    
    /* Hero Section */
    .hero-title { 
        font-size: 1.5rem !important; 
        font-weight: 700 !important; 
        line-height: 1.2 !important; 
        margin: 0 !important;
        color: var(--white) !important;
    }
    .hero-subtitle { 
        font-size: 1rem !important; 
        font-weight: 400 !important; 
        margin: 1rem 0 !important;
        color: #d1d1d6 !important;
    }
    .hero {
        background: var(--primary);
        color: white;
        padding: 1.5rem 1rem;
        text-align: center;
        border-radius: 12px;
        margin: 0 0 0.5rem 0 !important;
        border-left: 6px solid var(--accent);
    }
    .hero * {
        color: var(--white) !important;
    }
    .hero .hero-subtitle { 
        color: #d1d1d6 !important; 
    }
    
    /* Cards */
    .card-container{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px,1fr)); gap:1.5rem; margin:1rem 0 1rem 0; }
    .card{ background: var(--white); border:1px solid var(--medium); border-radius:12px; padding:1.5rem; box-shadow:0 6px 16px var(--shadow); transition: transform 0.4s ease, box-shadow 0.4s ease; }
    .card:hover{ transform: translateY(-5px); box-shadow:0 12px 28px var(--shadow-hover); }
    .result-badge { color: var(--accent); font-weight: 600; margin-top: 1rem; display: inline-block; }
    .card-content { transition: all 0.3s ease; }
    
    /* Process Tracker */
    .process-tracker{ display:flex; justify-content:center; align-items:center; margin:1rem 0; gap:1rem; font-weight:600; color:var(--muted); }
    .process-tracker .active{ color: var(--accent); }
    
    /* Stats */
    .stats{ display:grid; grid-template-columns:repeat(4, 1fr)); gap:0.75rem; margin:1rem 0; }
    .stat{ background: var(--white); border:1px solid var(--medium); border-radius:12px; padding:1.5rem 1rem; text-align:center; transition: all 0.3s ease; }
    .stat:hover{ transform: translateY(-3px); box-shadow:0 8px 16px var(--shadow-hover); }
    .stat-number{ color: var(--accent); font-size:2rem; font-weight:700; }
    
    /* Testimonials */
    .testimonial-card{ background: var(--white); border-radius:12px; padding:1.5rem; margin-bottom:1rem; border-left:4px solid var(--accent); box-shadow:0 4px 12px var(--shadow); }
    .testimonial-icon{ font-size:1.8rem; margin-bottom:0.8rem; }
    
    /* Image Container */
    .card-image-container{ margin-top:1rem; border-radius:8px; overflow:hidden; }
    .card-image-container img{ width:100%; border-radius:8px; transition:transform 0.3s; }
    .card-image-container img:hover{ transform:scale(1.02); }
    
    /* Buttons */
    .btn{ background: var(--accent); color: var(--primary); padding: 0.8rem 1.5rem; border-radius: 8px; font-weight:600; font-size:1rem; border:none; cursor:pointer; margin:0.5rem 0 0 0; transition: all 0.3s ease; }
    .btn:hover{ background:#C7A133; transform: translateY(-2px); box-shadow:0 6px 12px var(--shadow-accent); }
    
    /* Back to top */
    .back-to-top-link{ text-align:center; margin:1rem 0; color:var(--accent); font-weight:600; }
    
    @media(max-width:768px){ 
        .card-container{ grid-template-columns:1fr!important; } 
        .stats{ grid-template-columns:repeat(2, 1fr)!important; }
        .btn{ width:100%!important; } 
    }
    @media(max-width:480px){ 
        .stats{ grid-template-columns:1fr!important; }
    }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- SESSION STATE FOR CARD COLLAPSE ---
if 'cards_collapsed' not in st.session_state:
    st.session_state.cards_collapsed = False

# --- HERO SECTION AT VERY TOP ---
st.markdown("""
<div class="main-container">
<div class="hero" id="top">
    <h1 class="hero-title">Reprogram Your Mind, Change Your Life</h1>
    <p class="hero-subtitle">Hypnotherapy doesn't just change what you do—it changes how you do it. In just 2 sessions, it reprograms the patterns holding you back, so you can finally get the results you deserve.</p>
    <a href="https://calendly.com/laetitiasheppard/30min" target="_blank">
        <button class="btn">📅 Book a FREE 15-min Call</button>
    </a>
    <p style="color: #a1a1a6 !important;">Expert-guided | Confidential | Certified in Hypnotherapy and DBT</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Your Blocks", "The Method", "Results", "About"],
    icons=["exclamation-triangle", "gear", "award", "person"],
    menu_icon="list",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important", 
            "margin": "0!important",
            "background-color": "transparent"
        },
        "nav-link": {
            "font-size": "1rem",
            "font-weight": "normal",
            "padding": "0.5rem 1rem",
        },
        "nav-link-selected": {
            "background-color": "var(--accent)",
            "color": "var(--primary)",
            "font-weight": "600"
        },
    }
)

page_map = {
    "Your Blocks": "problems",
    "The Method": "method",
    "Results": "results",
    "About": "about"
}
st.session_state.page = page_map[selected]

# --- IMAGE HANDLING ---
def load_image(image_path, caption=None):
    try:
        st.image(image_path, caption=caption, use_container_width=True)
    except:
        st.warning(f"Image not found: {image_path}")

def back_to_top():
    st.markdown('<div class="back-to-top-link"><a href="#top">↑ Back to Top</a></div>', unsafe_allow_html=True)

# --- PAGE FUNCTIONS ---
def show_problems():
    st.markdown('<h2 id="problems">Common Challenges We Help You Overcome</h2>', unsafe_allow_html=True)
    
    # Collapse/Expand button
    if st.button(f"{'▼' if st.session_state.cards_collapsed else '▲'} Collapse All Cards", 
                key="toggle_cards",
                help="Show/hide all challenge cards"):
        st.session_state.cards_collapsed = not st.session_state.cards_collapsed
        st.rerun()
    
    problems = [
        {"title":"Overcoming Drinking Challenges","desc":"Struggling with unhealthy drinking habits? We help reprogram your subconscious patterns for lasting change.","result":"→ Empower yourself to regain control"},
        {"title":"Breaking Free from Smoking","desc":"Tobacco addiction can be tough to beat alone. Our hypnotherapy creates new habits that support your freedom.","result":"→ Quit smoking with confidence and ease"},
        {"title":"Preparing Mind and Body for Pregnancy","desc":"Facing challenges with conception? We support your mind-body connection to reduce stress and improve outcomes.","result":"→ Harmonize your mental and physical health"},
        {"title":"Restoring Healthy Sleep","desc":"Difficulty sleeping affects every area of life. Hypnotherapy helps reset patterns for deep, restful nights.","result":"→ Enjoy restorative sleep naturally"},
        {"title":"Healing Intimate Relationships","desc":"Relationship strains or intimacy issues? We assist in uncovering and resolving emotional blocks.","result":"→ Foster trust and intimacy with confidence"},
        {"title":"Adapting to New Surroundings","desc":"Moving or life transitions can be stressful. Reprogram your mindset for resilience.","result":"→ Thrive comfortably in your new environment"},
        {"title":"Embracing Life's Changes","desc":"Change is constant; struggle is optional. Build adaptability and calm in uncertainty.","result":"→ Cultivate flexibility and peace of mind"}
    ]
    
    st.markdown(f'<div class="card-container {"collapsed" if st.session_state.cards_collapsed else ""}">', unsafe_allow_html=True)
    for p in problems:
        st.markdown(f"""
            <div class="card">
              <h2>{p['title']}</h2>
              <div class="card-content">
                <p>{p['desc']}</p>
                <span class="result-badge">{p['result']}</span>
              </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Self Assessment Questionnaire Section
    st.markdown("""
    <div style="margin-top: 1rem;">
        <h2>Self Assessment Questionnaire</h2>
        <p>Take a moment to reflect on your behavioral patterns:</p>
    </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_area(
        "Describe what you dislike doing or how you respond in certain situations, and how you feel about it:",
        placeholder="For example: 'I get very anxious when I have to speak in meetings...'",
        height=150,
        key="self_assessment"
    )
    
    st.markdown("""
    <div style="margin-top: 1rem; font-style: italic; color: var(--muted);">
        <p>Section coming soon - This will provide personalized insights based on your input.</p>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()

def show_method():
    # Why Reprogramming Works section
    st.markdown('<h2>Why Reprogramming Works</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <ul>
            <li>Changing habits alone often fails because the patterns driving behaviors are subconscious</li>
            <li>Hypnotherapy rewires root causes towards your desired behavioral outcomes</li>
            <li>Expert-designed framework for sustainable change within just 2 focused sessions</li>
            <li>All-inclusive price: 3000 THB per 2 sessions; follow-up optional</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Our Simple 2-Session Process section
    st.markdown('<h2 id="method">Our Simple 2-Session Process</h2>', unsafe_allow_html=True)
    st.markdown("""
      <div class="process-tracker">
        <div class="step active">1</div><div>→</div>
        <div class="step active">2</div><div>→</div>
        <div class="step">3 (Optional)</div>
      </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    # Session 1: Analysis
    st.markdown("""
    <div class="card">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div class="step-number">1</div>
            <div>
                <h2>Session 1: Analysis</h2>
                <p>Identify limiting patterns and create a personalized mind reprogramming plan.</p>
            </div>
        </div>
        <div class="card-image-container">
    """, unsafe_allow_html=True)
    load_image("./img/BehaviourMap.png", caption="Behavior Mapping")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Session 2: Hypnosis
    st.markdown("""
    <div class="card">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div class="step-number">2</div>
            <div>
                <h2>Session 2: Hypnosis</h2>
                <p>Reprogram behaviors with certified expertise for rapid, lasting change.</p>
            </div>
        </div>
        <div class="card-image-container">
    """, unsafe_allow_html=True)
    load_image("./img/emo.jpg", caption="Emotional Reprogramming")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Optional Session 3: Reinforcement
    st.markdown("""
    <div class="card">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div class="step-number">3</div>
            <div>
                <h2>Session 3: Reinforcement (Optional)</h2>
                <p>Optional follow-up session to strengthen new patterns, typically not required but available.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close card-container

    # Stats - now 4 cards side by side
    st.markdown('<div class="stats">', unsafe_allow_html=True)
    stats = [("2","Sessions for Change"),("92%","Client Reported Improvement"),("5‑7x","Faster Than Traditional Therapy"),("3000฿","All‑Inclusive Price")]
    for num, label in stats:
        st.markdown(f'<div class="stat"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    back_to_top()

def show_results():
    st.markdown('<h2 id="results">Real Client Transformations</h2>', unsafe_allow_html=True)
    testimonials = [
        ("🌟","Finally broke free from old patterns – 2 sessions changed everything.","Director, Banking, Singapore"),
        ("🎓","I was struggling with my studies abroad... now doing my specialization internship.","Medical Student, Morocco"),
        ("🚭","My husband was a heavy smoker... No more addiction.","Wife, Bangkok"),
        ("🧘","The anxiety that controlled my daily life is now manageable...","Anxiety Patient, France")
    ]
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for icon, quote, author in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="testimonial-icon">{icon}</div>
            <div class="testimonial-quote">"{quote}"</div>
            <div class="testimonial-author">— {author}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Testimonial submission form
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h2>Share Your Story</h2>
        <p style="margin-bottom: 1rem;">Help others by sharing your transformation:</p>
    """, unsafe_allow_html=True)
    
    with st.form("testimonial_form", clear_on_submit=True):
        cols = st.columns([1, 1])
        with cols[0]:
            name = st.text_input("Your Name (optional)", placeholder="How you want to be credited")
        with cols[1]:
            session_date = st.date_input("Session 2 Date*", help="Required for verification")
        
        testimonial = st.text_area("Your Experience*", 
                                 placeholder="Describe your transformation...", 
                                 height=150, 
                                 help="Minimum 50 characters")
        
        submitted = st.form_submit_button("Submit Testimonial")
        
        if submitted:
            if not session_date:
                st.error("Please provide your session date for verification.")
            elif not testimonial or len(testimonial.strip()) < 50:
                st.error("Please share at least 50 characters about your experience.")
            else:
                st.success("Thank you! We'll review your testimonial and contact you if needed.")
                st.balloons()

    st.markdown("""
        <p style="font-size: 0.9rem; color: var(--muted); margin-top: 1rem;">
            * Required fields. Testimonials are verified before publication.
        </p>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()

def show_about():
    st.markdown('<h2 id="about">About Laetitia Sheppard</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        load_image("./img/ID.jpg", caption="Laetitia Sheppard")
    
    with col2:
        st.markdown("""
        <div class="card">
            <h2>Expert in Behavioral Change</h2>
            <ul>
                <li>10+ years of experience in change management</li>
                <li>Certified in Hypnotherapy & Cognitive Behaviour (LCCH, 2016)</li>
                <li>Certified in Dialectical Behavioral Therapy for Borderline Personality Disorder (2023)</li>
                <li>Fluent: English, French, can deliver in Italian if needed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: var(--primary); color: white; padding: 1rem; border-radius: 12px; margin: 1rem 0; border-top: 4px solid var(--accent); text-align: center;">
        <h2 style="color: var(--white) !important;">Bangkok Hypnotherapy Clinic</h2>
        <p style="color: var(--white) !important;">27 Soi Sukhumvit 10 (Asoke) • Confidential Sessions</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
            <a href="https://www.google.com/maps/place/27+Soi+Sukhumvit+10,+Asoke,+Bangkok" target="_blank">
                <button class="btn">📍 Get Directions</button>
            </a>
            <a href="https://calendly.com/laetitiasheppard/new-meeting" target="_blank">
                <button class="btn">📅 Book Now</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()

# --- AUTO-SCROLL TO TOP ---
st.markdown(
    """
    <script>
    window.addEventListener('load', function() {
        window.location.hash = '#top';
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Display selected page
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
<div style="text-align:center; font-size:0.9rem; color:var(--muted); margin:1rem 0; border-top: 1px solid var(--medium); padding-top: 2rem;">
  Laetitia Sheppard • Hypnotherapy for Change • Bangkok, Thailand<br>© 2025 All Rights Reserved | Confidentiality Guaranteed
</div>
</div>  <!-- close main-container -->
""", unsafe_allow_html=True)
