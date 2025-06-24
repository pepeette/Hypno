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

.hero-section {
    background: var(--primary-color);
    color: white;
    padding: 3rem 2rem;
    text-align: center;
    border-radius: 12px;
    border-left: 6px solid var(--accent-color);
    margin-bottom: 2rem;
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #d1d1d6;
    margin-bottom: 2rem;
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

.problem-card, .method-step, .testimonial-card {
    background: var(--card-bg);
    padding: 1.25rem;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    margin-bottom: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.cta-section {
    background: var(--primary-color);
    color: white;
    padding: 2rem;
    text-align: center;
    border-top: 4px solid var(--accent-color);
    border-radius: 10px;
    margin: 2rem 0;
}

.badge {
    display: inline-block;
    background-color: var(--secondary-color);
    color: white;
    padding: 0.3rem 0.75rem;
    border-radius: 4px;
    font-size: 0.75rem;
    margin: 0.25rem;
}

.stButton > button {
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    border-radius: 6px;
    border: none;
    transition: 0.3s ease;
}

.stButton > button:hover {
    background-color: #c7a133;
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 1.75rem;
    }
    .hero-subtitle {
        font-size: 1rem;
    }
    .section-title {
        font-size: 1.5rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --- INIT SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = 'services'

# --- HEADER ---
def show_header():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">Override Mental Blocks in 2 Neuroscience Sessions</div>
        <div class="hero-subtitle">Trusted by hedge fund managers, investment bankers, and C-suite expats in Asia.</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Apply for Performance Audit", key="cta_header"):
            webbrowser.open("https://calendly.com/titre/free-session")

# --- NAVIGATION ---
def show_navigation():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("### **Neuroscience Performance Solutions**")
    with col2:
        if st.button("Fixes", key="nav_services"):
            st.session_state.page = "services"
    with col3:
        if st.button("Method", key="nav_method"):
            st.session_state.page = "method"
    with col4:
        if st.button("About", key="nav_about"):
            st.session_state.page = "about"

# --- SERVICES ---
def show_services():
    st.markdown('<div class="section-title">High-Stakes Performance Fixes</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <span class="badge">Bangkok</span>
        <span class="badge">Singapore</span>
        <span class="badge">Hong Kong</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="problem-card">
            <h4>Boardroom Freeze Elimination</h4>
            <p>Override hesitation and speak with gravitas—even under C-suite pressure.</p>
            <strong style="color: var(--accent-color);">→ Command authority in high-stakes meetings</strong>
        </div>
        <div class="problem-card">
            <h4>Strategic Delegation</h4>
            <p>When performance drops due to micromanagement instincts.</p>
            <strong style="color: var(--accent-color);">→ Reduce micromanagement by 60–80%</strong>
        </div>
        <div class="problem-card">
            <h4>Jet Lag & Sleep Reboot</h4>
            <p>Travel fatigue and racing thoughts disrupting sleep cycles?</p>
            <strong style="color: var(--accent-color);">→ 90% faster sleep onset</strong>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="problem-card">
            <h4>Negotiation Pressure Control</h4>
            <p>Manage emotional responses during critical conflict and deal situations.</p>
            <strong style="color: var(--accent-color);">→ Stay strategically composed</strong>
        </div>
        <div class="problem-card">
            <h4>Stress Resilience Protocol</h4>
            <p>Break the stress-to-habit cycle under volatility or pressure.</p>
            <strong style="color: var(--accent-color);">→ Replace destructive habits with high-performance states</strong>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cta-section">
        <h3>Only 5 Performance Audits Offered Per Month</h3>
        <p>Apply today to reserve your confidential evaluation slot.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Apply Now", key="cta_services"):
            webbrowser.open("https://calendly.com/titre/free-session")

# --- METHOD ---
def show_method():
    st.markdown('<div class="section-title">The 2-Session Neuroscience Method</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="method-step">
            <h4>1. Pattern Mapping</h4>
            <p>Identify how pressure hijacks your decision-making systems.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="method-step">
            <h4>2. Neural Rewiring</h4>
            <p>Install updated, unconscious patterns that withstand high stress.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="method-step">
            <h4>3. Reinforcement (if needed)</h4>
            <p>Optional booster session for long-term performance edge.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Questions from Asia-Based Leaders")
    with st.expander("How is this different from coaching?"):
        st.write("This isn’t coaching—it’s unconscious neural recalibration. Our method targets the wiring behind performance, not surface behavior.")
    with st.expander("Why does it work in 2 sessions?"):
        st.write("We target unconscious circuits precisely. You won’t need 10 sessions to get clarity or control.")
    with st.expander("Is it confidential?"):
        st.write("Absolutely. No records beyond legal requirements. We serve finance leaders across Asia who demand privacy.")

# --- ABOUT ---
def show_about():
    st.markdown('<div class="section-title">Why Finance Leaders Trust This Method</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.info("Image not found")
    with col2:
        st.markdown("""
        **Experience Across Asia’s Financial Hubs**
        - 13+ years on trading floors: Bloomberg, HSBC, CA Indosuez
        - Managed $50M book, coached 48-person teams in 12 countries

        **Credentials:**
        - Certified Behavioral Performance Specialist (UK, 2017)
        - Certified Neuroscience Coach (2023)
        - Fluent: English, French, Spanish, Italian
        """)

    st.markdown('<div class="section-title">Testimonials</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="testimonial-card">
        \"From hesitating in meetings to leading decisively. My deal closures speak for themselves.\"
        <br><strong>— Sarah M., Managing Director, Bangkok</strong>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="testimonial-card">
        \"2 sessions in, my sleep quality jumped and I started winning more board approvals.\"
        <br><strong>— Marcus L., PE Partner, Singapore</strong>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Bangkok Clinic & Contact")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        **Performance Clinic (Bangkok HQ)**
        46/9 Soi Sukhumvit 49 — Wireless Road Area

        **Clients:** Portfolio Managers · Hedge Fund Leaders · C-Suite Expats

        Languages spoken: English, French, Spanish, Italian
        """)
        if st.button("📅 Apply Now (5 Clients/Month)", key="cta_about"):
            webbrowser.open("https://calendly.com/titre/free-session")
    with col2:
        try:
            st.image("./img/Map.png", caption="Bangkok Financial District")
        except:
            st.info("Map placeholder")

# --- MAIN RENDERING ---
show_header()
show_navigation()
if st.session_state.page == "services":
    show_services()
elif st.session_state.page == "method":
    show_method()
elif st.session_state.page == "about":
    show_about()

# --- FOOTER ---
st.markdown("---")
st.markdown("*Neuroscience Performance Solutions | Elite Behavioral Reset for Asia’s Finance Sector*")
