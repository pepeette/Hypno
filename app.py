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
    }
    [data-testid="stAppViewContainer"] { background-color: var(--light) !important; color-scheme: light !important; }
    .stApp { background: var(--light)!important; font-family: 'Inter', sans-serif!important; color: var(--primary)!important; padding-top: 0!important; }
    #MainMenu, header, footer, .stDeployButton { visibility: hidden; }
    .main-container { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }
    h1 { font-size: 1.5rem!important; margin: 0.5rem 0!important; }
    h2 { font-size: 1.3rem!important; margin: 0.6rem 0!important; }
    p, li, span, div { font-size: 1rem!important; margin: 0.3rem 0!important; }
    .hero{ background: var(--primary); color: var(--white); padding: 1rem; border-radius: 12px; margin: 0.25rem 0; text-align: center; }
    .btn{ background: var(--accent); color: var(--primary); padding: 0.8rem 1.5rem; border-radius: 8px; font-weight:600; font-size:1rem; border:none; cursor:pointer; margin:0.5rem 0 0 0; }
    .btn:hover{ background:#C7A133; }
    .card-container{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px,1fr)); gap:1.5rem; margin:1rem 0 1rem 0; }
    .card{ background: var(--white); border:1px solid var(--medium); border-radius:12px; padding:1.8rem 2rem; box-shadow:0 6px 16px rgba(0,0,0,0.05); }
    .process-tracker{ display:flex; justify-content:center; align-items:center; margin:1rem 0; gap:1rem; font-weight:600; color:var(--muted); }
    .process-tracker .active{ color: var(--accent); }
    .stats{ display:grid; grid-template-columns:repeat(auto-fit, minmax(200px,1fr)); gap:0.75rem; margin:1rem 0; }
    .stat{ background: var(--white); border:1px solid var(--medium); border-radius:12px; padding:1.5rem 1rem; text-align:center; }
    .stat-number{ color: var(--accent); font-size:2rem; font-weight:700; }
    .testimonial-card{ background: var(--white); border-radius:12px; padding:1.5rem; margin-bottom:1rem; border-left:4px solid var(--accent); box-shadow:0 4px 12px rgba(0,0,0,0.05); }
    .back-to-top-link{ text-align:center; margin:1rem 0; color:var(--accent); font-weight:600; }
    @media(max-width:768px){ .card-container, .stats{ grid-template-columns:1fr!important; } .btn{ width:100%!important; } }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- NAVIGATION MENU VIA HAMBURGER ---
selected = option_menu(
    menu_title=None,
    options=["Your Blocks", "The Method", "Results", "About"],
    icons=["exclamation-triangle", "gear", "award", "person"],
    menu_icon="list",
    default_index=0,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "margin": "0!important"}}
)

page_map = {
    "Your Blocks": "problems",
    "The Method": "method",
    "Results": "results",
    "About": "about"
}
st.session_state.page = page_map[selected]

# --- MAIN CONTAINER START ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

def back_to_top():
    st.markdown('<div class="back-to-top-link"><a href="#top">↑ Back to Top</a></div>', unsafe_allow_html=True)

# --- PAGE FUNCTIONS ---
def show_problems():
    st.markdown('<h2 id="problems">Common Challenges We Help You Overcome</h2>', unsafe_allow_html=True)
    problems = [
        {"title":"Overcoming Drinking Challenges","desc":"Struggling with unhealthy drinking habits? We help reprogram your subconscious patterns for lasting change.","result":"→ Empower yourself to regain control"},
        {"title":"Breaking Free from Smoking","desc":"Tobacco addiction can be tough to beat alone. Our hypnotherapy creates new habits that support your freedom.","result":"→ Quit smoking with confidence and ease"},
        {"title":"Preparing Mind and Body for Pregnancy","desc":"Facing challenges with conception? We support your mind-body connection to reduce stress and improve outcomes.","result":"→ Harmonize your mental and physical health"},
        {"title":"Restoring Healthy Sleep","desc":"Difficulty sleeping affects every area of life. Hypnotherapy helps reset patterns for deep, restful nights.","result":"→ Enjoy restorative sleep naturally"},
        {"title":"Healing Intimate Relationships","desc":"Relationship strains or intimacy issues? We assist in uncovering and resolving emotional blocks.","result":"→ Foster trust and intimacy with confidence"},
        {"title":"Adapting to New Surroundings","desc":"Moving or life transitions can be stressful. Reprogram your mindset for resilience.","result":"→ Thrive comfortably in your new environment"},
        {"title":"Embracing Life's Changes","desc":"Change is constant; struggle is optional. Build adaptability and calm in uncertainty.","result":"→ Cultivate flexibility and peace of mind"}
    ]
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for p in problems:
        st.markdown(f"""
            <div class="card">
              <h2>{p['title']}</h2>
              <p>{p['desc']}</p>
              <span class="result-badge">{p['result']}</span>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    back_to_top()

def show_method():
    st.markdown('<h2 id="method">Our Simple 2-Session Process</h2>', unsafe_allow_html=True)
    st.markdown("""
      <div class="process-tracker">
        <div class="step active">1</div><div>→</div>
        <div class="step active">2</div><div>→</div>
        <div class="step">3 (Optional)</div>
      </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    # Session Cards...
    st.markdown("""
        <div class="card">
          <h2>Session 1: Analysis</h2>
          <p>Identify limiting patterns and create a personalized mind reprogramming plan.</p>
        </div>
        <div class="card">
          <h2>Session 2: Hypnosis</h2>
          <p>Reprogram behaviors with certified expertise for rapid, lasting change.</p>
        </div>
        <div class="card">
          <h2>Session 3: Reinforcement (Optional)</h2>
          <p>Optional follow-up session to strengthen new patterns, typically not required but available.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # Stats
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
        st.markdown(f'<div class="testimonial-card"><div class="testimonial-icon">{icon}</div><div class="testimonial-quote">"{quote}"</div><div class="testimonial-author">— {author}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    back_to_top()

def show_about():
    st.markdown('<h2 id="about">About Laetitia Sheppard</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.markdown("""
      <div class="card">
        <h2>Expert in Behavioral Change</h2>
        <ul>
           <li>10+ years of experience</li>
           <li>Certified in Hypnotherapy & DBT</li>
           <li>Fluent: English, French; Italian possible</li>
        </ul>
      </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    back_to_top()

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
<div style="text-align:center; font-size:0.9rem; color:var(--muted); margin:1rem 0;">
  Laetitia Sheppard • Hypnotherapy for Change • Bangkok, Thailand<br>© 2025 All Rights Reserved
</div>
</div>  <!-- close main-container -->
""", unsafe_allow_html=True)
