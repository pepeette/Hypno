import streamlit as st
import webbrowser

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
    --primary-color: #1C1C1E;
    --accent-color: #D4AF37;
    --secondary-color: #3A3A3C;
    --bg-color: #F4F4F6;
    --card-bg: #FFFFFF;
    --text-color: #1C1C1E;
    --text-muted: #6E6E73;
    --border-color: #E2E2E6;
}

.stApp {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-color);
    color: var(--text-color);
    padding: 0 !important;
    margin: 0 !important;
    line-height: 1.6;
}

.main-header {
    background: var(--primary-color);
    color: white;
    padding: 3rem 2rem;
    text-align: center;
    border-radius: 0 0 12px 12px;
    border-left: 6px solid var(--accent-color);
    margin-bottom: 0;
}

.main-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.main-subtitle {
    font-size: 1.2rem;
    color: #d1d1d6;
    margin-bottom: 1rem;
}

.nav-bar {
    display: flex;
    justify-content: center;
    margin: 1rem 0 2rem 0;
    gap: 2rem;
    padding: 0 1rem;
}

.nav-button {
    background-color: transparent;
    border: none;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-muted);
    border-bottom: 2px solid transparent;
    padding: 0.5rem 0;
    cursor: pointer;
    transition: all 0.3s ease;
}

.nav-button:hover {
    color: var(--primary-color);
}

.nav-button-active {
    color: var(--primary-color) !important;
    border-bottom: 2px solid var(--accent-color) !important;
}

.problem-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.problem-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}

.problem-title {
    font-weight: bold;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.problem-description {
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
    color: var(--text-color);
}

.problem-result {
    font-style: italic;
    color: var(--accent-color) !important;
    border-top: 1px dashed var(--border-color);
    padding-top: 0.5rem;
    margin-top: 0.5rem;
}

.sub-section-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--primary-color);
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-left: 4px solid var(--accent-color);
    padding-left: 0.75rem;
}

.stButton > button {
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    border-radius: 6px;
    border: none;
    font-size: 1.1rem;
    transition: 0.3s ease;
    margin-top: 1rem;
}

.stButton > button:hover {
    background-color: #c7a133;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3);
}

.stat-number {
    color: var(--accent-color) !important;
    font-size: 1.5rem;
    font-weight: 700;
}

.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

@media (max-width: 768px) {
    .main-title {
        font-size: 1.5rem;
    }
    .main-subtitle {
        font-size: 1rem;
    }
    .nav-bar {
        flex-direction: column;
        gap: 0.5rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HEADER ---
st.markdown("""
<div class="main-header">
    <div class="main-title">The Expat's Dilemma</div>
    <div class="main-subtitle">
        You sacrificed everything for this Bangkok career - so why does success feel like wearing someone else's skin?
    </div>
    <div style="margin-top: 1rem;">
        <button>🧠 Yes, I Want My Breakthrough Session →</button>
    </div>
    <p style="color: #a1a1a6; margin-top: 1rem;">Neuroscience-backed | Confidential | 13 years in Asian markets</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION BAR ---
st.markdown('<div class="main-container"><div class="nav-bar">', unsafe_allow_html=True)
tabs = [("🔥 Your Blocks", "problems"), ("🧠 The Method", "method"), ("🏆 Results", "results"), ("👤 About", "about")]
for label, page_name in tabs:
    css_class = "nav-button-active" if st.session_state.page == page_name else "nav-button"
    if st.button(label, key=page_name):
        st.session_state.page = page_name
st.markdown('</div></div>', unsafe_allow_html=True)

# --- CONTENT AREAS ---
def show_problems():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-section-title">The Hidden Blocks We Solve</div>', unsafe_allow_html=True)
    
    problems = [
        ("The Bangkok Glass Ceiling", 
         "You deliver exceptional work but get passed over for promotions. Your Western directness is suddenly 'too aggressive', while local colleagues advance with half your output.",
         "→ Rewire unconscious self-sabotage and cultural blind spots"),
        
        ("The Stress-Weight Spiral", 
         "Late-night moo ping binges after stressful meetings. Gym memberships gathering dust. That 'temporary' 10kg now feels permanent.",
         "→ Reset your metabolic programming without another fad diet"),
        
        ("Performance Anxiety", 
         "You nailed presentations in London/NYC - but here, your mind blanks mid-sentence. The harder you try to impress, the more you underwhelm.",
         "→ Install bulletproof confidence tailored to Asian boardrooms")
    ]
    
    for title, desc, result in problems:
        st.markdown(f"""
        <div class='problem-card'>
            <div class='problem-title'>{title}</div>
            <div class='problem-description'>{desc}</div>
            <div class='problem-result'>{result}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">Why It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
        <div class='problem-card' style='text-align: center;'>
            <div class='stat-number'>2</div>
            <div>Sessions for breakthrough</div>
        </div>
        <div class='problem-card' style='text-align: center;'>
            <div class='stat-number'>92%</div>
            <div>Report improvement</div>
        </div>
        <div class='problem-card' style='text-align: center;'>
            <div class='stat-number'>5-7x</div>
            <div>Faster than therapy</div>
        </div>
        <div class='problem-card' style='text-align: center;'>
            <div class='stat-number'>0</div>
            <div>Ongoing sessions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <button>🚨 Only 3 Spots Left This Month →</button>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_method():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-section-title">Why 2 Sessions Work When Nothing Else Did</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='problem-card'>
        <strong>Traditional Therapy Failed You Because:</strong><br>
        <ul>
            <li>It talks <em>about</em> problems instead of rewriting them</li>
            <li>Progress gets derailed by Bangkok's 60-hour work weeks</li>
            <li>Western methods don't address Asian business culture nuances</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='problem-card'>
            <strong>1. Pattern Mapping</strong><br>
            We identify the <em>exact</em> neural circuits causing your blocks using fMRI-inspired techniques
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='problem-card'>
            <strong>2. Neural Rewiring</strong><br>
            Precision hypnotherapy to install new patterns that withstand Bangkok's pressures
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_results():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-section-title">Client Transformations</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class='problem-card'>
        <em>"After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."</em>
        <div style="font-weight: 600; margin-top: 1rem;">— French Tech Director, Fortune 500</div>
    </div>
    
    <div class='problem-card'>
        <em>"The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."</em>
        <div style="font-weight: 600; margin-top: 1rem;">— American PE VP, Bangkok</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_about():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="sub-section-title">About Laetitia</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.markdown('<div style="width: 250px; height: 300px; background: var(--border-color); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--text-muted);">Profile Image</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div>
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
    
    st.markdown('<div class="sub-section-title">Bangkok Hypnotherapy Clinic</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class='problem-card'>
        <div style="color: var(--primary-color); font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">46/9 Soi Sukhumvit 49 (Thong Lor)</div>
        <p>Private & Confidential</p>
        <button>📍 Get Directions</button>
        <button>📅 Book Discovery Call</button>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
<div class="main-container">
    <div style="text-align: center; border-top: 1px solid var(--border-color); padding-top: 2rem; margin-top: 3rem; color: var(--text-muted);">
        <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
        <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
    </div>
</div>
""", unsafe_allow_html=True)
