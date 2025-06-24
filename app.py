import streamlit as st
import webbrowser
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Executive Performance Hypnotherapy | Laetitia Hoquetis", 
    page_icon="🎯", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Professional Executive Theme
st.markdown("""
    <style>
    .stApp {
        font-family: 'Helvetica', Arial, sans-serif;
        line-height: 1.6;
        color: #2c3e50;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    .credentials {
        font-size: 0.9rem;
        opacity: 0.8;
    }
    
    .problem-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
        margin-bottom: 1rem;
        height: 100%;
    }
    
    .problem-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1e3c72;
        margin-bottom: 0.5rem;
    }
    
    .problem-description {
        color: #666;
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
    }
    
    .problem-result {
        font-weight: 600;
        color: #27ae60;
        font-size: 0.9rem;
    }
    
    .method-step {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
        border: 2px solid #e9ecef;
    }
    
    .step-number {
        width: 50px;
        height: 50px;
        background: #2a5298;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 auto 1rem;
    }
    
    .testimonial-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .testimonial-author {
        font-weight: 600;
        color: #1e3c72;
        margin-top: 1rem;
        font-style: normal;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stButton>button {
        background: #27ae60;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    
    .stButton>button:hover {
        background: #219a52;
    }
    
    .nav-button {
        background: #2a5298;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0 0.5rem;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1e3c72;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .credentials-list {
        list-style: none;
        padding: 0;
    }
    
    .credentials-list li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .credentials-list li:before {
        content: "✓";
        color: #27ae60;
        font-weight: bold;
        margin-right: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
def show_navigation():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("### **Executive Performance Hypnotherapy**")
    with col2:
        if st.button("Services", key="nav_services"):
            st.session_state.page = "services"
    with col3:
        if st.button("Method", key="nav_method"):
            st.session_state.page = "method"
    with col4:
        if st.button("About", key="nav_about"):
            st.session_state.page = "about"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'services'

# Header Section
def show_header():
    st.markdown("""
    <div class="main-header">
        <div class="main-title">Executive Performance Hypnotherapy</div>
        <div class="main-subtitle">Rewire Limiting Behaviors. Unlock Peak Performance.</div>
        <div class="credentials">Laetitia Hoquetis | 13+ Years Financial Markets | Certified Hypnotherapist & DBT Specialist</div>
    </div>
    """, unsafe_allow_html=True)

# Services Page
def show_services():
    st.markdown('<div class="section-title">High-Stakes Behavioral Problems I Solve</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Performance Anxiety & Imposter Syndrome</div>
            <div class="problem-description">You freeze in presentations or doubt yourself despite proven success, undermining your leadership presence.</div>
            <div class="problem-result">→ Install unshakeable confidence and eliminate self-doubt</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Perfectionism & Control Issues</div>
            <div class="problem-description">You burn out trying to control everything, micromanaging and losing efficiency.</div>
            <div class="problem-result">→ Install strategic delegation and "good enough" frameworks</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Sleep Anxiety & Executive Burnout</div>
            <div class="problem-description">Racing thoughts keep you awake, affecting decision-making and performance the next day.</div>
            <div class="problem-result">→ Reprogram deep sleep patterns and mental shutdown protocols</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Emotional Regulation in Conflict</div>
            <div class="problem-description">You lose control in difficult conversations or negotiations, damaging professional relationships.</div>
            <div class="problem-result">→ Master strategic emotional responses and conflict navigation</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Smoking & High-Pressure Habits</div>
            <div class="problem-description">Stress-triggered habits (smoking, drinking) that you use to cope with executive pressure.</div>
            <div class="problem-result">→ Eliminate triggers and install healthier stress responses</div>
        </div>
        """, unsafe_allow_html=True)

    # CTA Section
    st.markdown("""
    <div class="cta-section">
        <h3>Ready to Rewire Your Peak Performance?</h3>
        <p>Stop letting behavioral patterns limit your potential. Book a consultation to discuss your specific challenges.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Schedule Executive Consultation", key="main_cta"):
            webbrowser.open("https://calendly.com/titre/free-session")

# Method Page
def show_method():
    st.markdown('<div class="section-title">My 2-Session Behavioral Rewiring Method</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="method-step">
            <div style="display: flex; justify-content: center;">
                <div style="width: 50px; height: 50px; background: #2a5298; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">1</div>
            </div>
            <h4>Pattern Analysis Session</h4>
            <p>Deep dive into your specific behavioral triggers, decision patterns, and unconscious responses. We map exactly where and how your performance gets hijacked.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="method-step">
            <div style="display: flex; justify-content: center;">
                <div style="width: 50px; height: 50px; background: #2a5298; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">2</div>
            </div>
            <h4>Behavioral Reprogramming</h4>
            <p>Using advanced hypnotherapy + DBT techniques, we reprogram new neural pathways for peak performance responses. Install new automatic behaviors.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="method-step">
            <div style="display: flex; justify-content: center;">
                <div style="width: 50px; height: 50px; background: #27ae60; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">3</div>
            </div>
            <h4>Reinforcement (If Needed)</h4>
            <p>Occasional tune-up sessions to strengthen new patterns. Most clients need only the initial 2 sessions for lasting change.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # FAQ Section
    st.markdown("### Frequently Asked Questions")
    
    with st.expander("How is this different from executive coaching?"):
        st.write("Executive coaching works at the conscious level - discussing strategies and goals. Hypnotherapy rewires the unconscious behavioral patterns that sabotage your conscious intentions. It's faster and addresses the root cause, not just symptoms.")
    
    with st.expander("Why only 2 sessions?"):
        st.write("Unlike traditional therapy that can take months, behavioral reprogramming through hypnotherapy targets specific neural pathways directly. Most executive behavioral patterns can be mapped and rewired in 2 focused sessions. Additional sessions are only needed for complex multi-layered issues.")
    
    with st.expander("Is this safe for high-pressure executives?"):
        st.write("Absolutely. Hypnotherapy is a scientifically validated approach used by elite athletes and Fortune 500 executives. You remain in full control - it's simply a focused state similar to deep concentration you already experience in high-stakes situations.")

# About Page  
def show_about():
    st.markdown('<div class="section-title">Why I Understand High-Performance Pressure</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Hoquetis")
        except:
            st.info("Professional photo placeholder")
    
    with col2:
        st.markdown("""
        **I've been where you are.** 13+ years on trading floors, managing $50M portfolios, leading 48-person international teams across multiple jurisdictions.

        I understand the crushing pressure of high-stakes decisions, the isolation of leadership, and the behavioral patterns that can make or break careers.

        Now I combine that real-world experience with advanced therapeutic training to solve the behavioral challenges that traditional coaching can't touch.
        """)
        
        st.markdown("""
        **My Unique Background:**
        - ✓ Certified Hypnotherapist (London College, 2017)
        - ✓ Dialectical Behavior Therapy (DBT Certified, 2024)
        - ✓ 13+ years Financial Markets (Bloomberg, HSBC, Credit Agricole)
        - ✓ Led digital transformation for 2,500+ employees
        - ✓ Managed international teams across 12+ countries
        - ✓ Fluent English, French, Spanish, Italian
        """)

    st.markdown("---")
    
    # Testimonials
    st.markdown('<div class="section-title">Client Results</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            "I went from freezing in board presentations to commanding the room. The change happened faster than I thought possible. Laetitia understands the pressure we face at executive level."
            <div class="testimonial-author">— Sarah M., Managing Director, Investment Banking</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            "My perfectionism was burning me out. After 2 sessions, I delegate effectively and trust my team. My stress levels dropped 70% while performance improved."
            <div class="testimonial-author">— Marcus L., Private Equity Partner</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Contact Section
    st.markdown("### Schedule Your Executive Consultation")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Bangkok Location:**  
        46/9 Soi Sukhumvit 49, Klong Ton Nua, Wattana District
        
        **Languages:** English, French, Spanish, Italian  
        **Specialized Focus:** Executive behavioral patterns, high-performance anxiety, leadership presence
        """)
        
        if st.button("📅 Book Consultation", key="about_cta"):
            webbrowser.open("https://calendly.com/titre/free-session")
    
    with col2:
        try:
            st.image("./img/Map.png", caption="Our Bangkok Location")
        except:
            st.info("Location map placeholder")

# Main App Logic
show_header()
show_navigation()

if st.session_state.page == 'services':
    show_services()
elif st.session_state.page == 'method':
    show_method()
elif st.session_state.page == 'about':
    show_about()

# Footer
st.markdown("---")
st.markdown("*Executive Performance Hypnotherapy | Laetitia Sheppard | Bangkok, Thailand*")
