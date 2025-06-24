import streamlit as st
import webbrowser
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Performance Solutions | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR EXECUTIVE CLARITY & MOBILE RESPONSIVENESS ---
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
    padding: 1rem;
    line-height: 1.6;
}

.main-header {
    background: var(--primary-color);
    color: white;
    padding: 3rem 2rem;
    text-align: center;
    border-radius: 12px;
    border-left: 6px solid var(--accent-color);
    margin-bottom: 2rem;
}

.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.main-subtitle {
    font-size: 1.2rem;
    color: #d1d1d6;
    margin-bottom: 1rem;
}

.credentials {
    font-size: 0.95rem;
    color: var(--text-muted);
}

.section-title {
    font-size: 2rem;
    text-align: center;
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid var(--accent-color);
    padding-bottom: 0.5rem;
    font-weight: 600;
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

.problem-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.06);
}

.problem-title {
    font-weight: bold;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.problem-description {
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.problem-result {
    font-style: italic;
    color: var(--secondary-color);
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
}

.stButton > button:hover {
    background-color: #c7a133;
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .main-title {
        font-size: 1.75rem;
    }
    .main-subtitle {
        font-size: 1rem;
    }
    .section-title {
        font-size: 1.5rem;
    }
    .sub-section-title {
        font-size: 1.25rem;
    }
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if 'page' not in st.session_state:
    st.session_state.page = 'services'

# HEADER
st.markdown("""
<div class="main-header">
    <div class="main-title">Rewire What’s Holding You Back — In 2 Sessions</div>
    <div class="main-subtitle">
        For ambitious professionals ready to break through anxiety, perfectionism, or authority blocks — fast.
    </div>
    <div class="credentials">
        Laetitia Sheppard • 13+ Years Trading Floors • Certified Behavioral Performance Specialist
    </div>
    <br>
    <div style="margin-top: 1rem;">
        <a href="https://calendly.com/titre/free-session" target="_blank">
            <button>📅 Book a Free 15-min Fit Call</button>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# NAVIGATION
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    st.markdown("### **Neuroscience Performance Solutions**")
with col2:
    if st.button("🔧 Solutions", key="nav_services"):
        st.session_state.page = "services"
with col3:
    if st.button("🧬 Method", key="nav_method"):
        st.session_state.page = "method"
with col4:
    if st.button("👤 About", key="nav_about"):
        st.session_state.page = "about"

# SERVICES PAGE
def show_services():
    st.markdown('<div class="section-title">What We Fix — Fast</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    problems = [
        ("Freezing in Presentations or High-Stakes Moments", "Smart, capable professionals lose their voice or presence right when it matters — in boardrooms, on stage, or with clients.", "→ Rewire confidence and command the room in 2 neuroscience-based sessions"),
        ("Perfectionism That Leads to Burnout", "You overwork, overcontrol, and can’t switch off. Your team feels it. So does your nervous system.", "→ Rewire for strategic focus — make high-impact decisions without the mental overload"),
        ("Performance Anxiety & Imposter Syndrome", "You know your stuff, but anxiety strikes before meetings, keynotes, or career moves. Confidence feels manufactured.", "→ Rewire unconscious fear loops and install calm, grounded confidence"),
        ("Losing Emotional Control in Conflict", "Heated discussions, negotiations, or internal politics trigger reactions that cost you leadership capital.", "→ Rewire emotional reactivity and lead with composure under pressure")
    ]
    for i, (title, desc, result) in enumerate(problems):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div class='problem-card'>
                <div class='problem-title'>{title}</div>
                <div class='problem-description'>{desc}</div>
                <div class='problem-result'>{result}</div>
            </div>
            """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <a href="https://calendly.com/titre/free-session" target="_blank">
                <button>📅 Apply Now</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# METHOD PAGE
def show_method():
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-section-title">The 2-Session Neuroscience Method</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='problem-card'>
            <strong>1. Pattern Mapping</strong><br>
            Identify how pressure hijacks your decision-making systems.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='problem-card'>
            <strong>2. Neural Rewiring</strong><br>
            Install updated, unconscious patterns that withstand high stress.
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='problem-card'>
            <strong>3. Reinforcement (Optional)</strong><br>
            Booster session to ensure performance under ongoing pressure.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">Questions from Asia-Based Leaders</div>', unsafe_allow_html=True)
    with st.expander("How is this different from coaching?"):
        st.write("This isn’t coaching—it’s unconscious neural recalibration. We target the source of performance limits, not just surface habits.")
    with st.expander("Why does it work in 2 sessions?"):
        st.write("Our process is precise and rooted in applied neuroscience. No fluff, no long timelines.")
    with st.expander("Is it confidential?"):
        st.write("100%. Trusted by leaders across Asia. No client data is stored beyond legal minimums.")

# ROUTING
if st.session_state.page == "services":
    show_services()
elif st.session_state.page == "method":
    show_method()
# ... you can extend the "about" page as needed here

# FOOTER
st.markdown("---")
st.markdown("*Neuroscience Performance Solutions | Elite Behavioral Reset | Cognitive Pattern Rewiring*")
