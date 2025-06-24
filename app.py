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
    .main-title {
        font-size: 1.75rem;
    }
    .main-subtitle {
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
                <button style="background-color: var(--accent-color); color: var(--primary-color); padding: 0.75rem 1.5rem; border: none; border-radius: 6px; font-weight: bold; font-size: 1.1rem;">
                    >> Book a Free 15-min Fit Call
                </button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
def show_navigation():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("### **Neuroscience Performance Solutions**")
    with col2:
        if st.button("Solutions", key="nav_services"):
            st.session_state.page = "services"
    with col3:
        if st.button("Method", key="nav_method"):
            st.session_state.page = "method"
    with col4:
        if st.button("About us", key="nav_about"):
            st.session_state.page = "about"

# --- SERVICES ---
def show_services():
    st.markdown('<div class="section-title">What We Fix — Fast</div>', unsafe_allow_html=True)
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
            <div class="problem-title">Freezing in Presentations or High-Stakes Moments</div>
            <div class="problem-description">
                Smart, capable professionals lose their voice or presence right when it matters — in boardrooms, on stage, or with clients.
            </div>
            <div class="problem-result">
                → Rewire confidence and command the room in 2 neuroscience-based sessions
            </div>
        </div>
        <div class="problem-card">
            <div class="problem-title">Perfectionism That Leads to Burnout</div>
            <div class="problem-description">
                You overwork, overcontrol, and can’t switch off. Your team feels it. So does your nervous system.
            </div>
            <div class="problem-result">
                → Rewire for strategic focus — make high-impact decisions without the mental overload
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Performance Anxiety & Imposter Syndrome</div>
            <div class="problem-description">
                You know your stuff, but anxiety strikes before meetings, keynotes, or career moves. Confidence feels manufactured.
            </div>
            <div class="problem-result">
                → Rewire unconscious fear loops and install calm, grounded confidence
            </div>
        </div>
        <div class="problem-card">
            <div class="problem-title">Losing Emotional Control in Conflict</div>
            <div class="problem-description">
                Heated discussions, negotiations, or internal politics trigger reactions that cost you leadership capital.
            </div>
            <div class="problem-result">
                → Rewire emotional reactivity and lead with composure under pressure
            </div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(">> Apply Now", key="cta_services"):
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
        - Certified Behavioral Performance Specialist & Hypnotherapy (UK, 2017)
        - Certified Neuroscience Coach (Dialectical Behavioral Therapy, 2024)
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
        46/9 Soi Sukhumvit 49 — Thong Lor Area

        **Clients:** Product Managers · Team Leaders · C-Suite 

        Languages spoken: English, French, Spanish, Italian
        """)
        if st.button(">> Apply Now (5 Clients/Month)", key="cta_about"):
            webbrowser.open("https://calendly.com/titre/free-session")
    with col2:
        try:
            st.image("./img/Map.png", caption="Bangkok Khlong Toei District")
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
st.markdown("*Neuroscience Performance Solutions | Elite Behavioral Reset | Cognitive Pattern Rewiring*")
