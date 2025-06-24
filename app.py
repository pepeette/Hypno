import streamlit as st
import webbrowser
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Neuroscience Performance Solutions | Laetitia Sheppard", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Professional Executive Theme with Dark Mode Support
st.markdown("""
    <style>
    :root {
        --primary-color: #1a365d;
        --primary-dark: #153e75;
        --secondary-color: #047857;
        --secondary-dark: #065f46;
        --text-color: #1f2937;
        --text-light: #6b7280;
        --bg-color: #ffffff;
        --card-bg: #f9fafb;
        --border-color: #e5e7eb;
    }
    
    [data-theme="dark"] {
        --primary-color: #2c5282;
        --primary-dark: #2b6cb0;
        --secondary-color: #047857;
        --secondary-dark: #065f46;
        --text-color: #f3f4f6;
        --text-light: #9ca3af;
        --bg-color: #111827;
        --card-bg: #1f2937;
        --border-color: #374151;
    }
    
    .stApp {
        font-family: 'Inter', 'Helvetica', Arial, sans-serif;
        line-height: 1.6;
        color: var(--text-color);
        background-color: var(--bg-color);
    }
    
    .main-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 4px solid var(--secondary-color);
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
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 4px solid var(--secondary-color);
        margin-bottom: 1rem;
        height: 100%;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .problem-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    
    .problem-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: var(--primary-color);
        margin-bottom: 0.5rem;
    }
    
    .problem-description {
        color: var(--text-light);
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
    }
    
    .problem-result {
        font-weight: 600;
        color: var(--secondary-color);
        font-size: 0.9rem;
    }
    
    .method-step {
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
        height: 100%;
    }
    
    .step-number {
        width: 50px;
        height: 50px;
        background: var(--primary-color);
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
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
    }
    
    .testimonial-author {
        font-weight: 600;
        color: var(--primary-color);
        margin-top: 1rem;
        font-style: normal;
    }
    
    .cta-section {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
        border-top: 4px solid var(--secondary-color);
    }
    
    .stButton>button {
        background: var(--secondary-color);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background: var(--secondary-dark);
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .nav-button {
        background: var(--primary-color);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0 0.5rem;
        transition: background-color 0.3s;
    }
    
    .nav-button:hover {
        background: var(--primary-dark);
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 1.5rem;
        text-align: center;
        border-bottom: 2px solid var(--secondary-color);
        padding-bottom: 0.5rem;
    }
    
    .credentials-list {
        list-style: none;
        padding: 0;
    }
    
    .credentials-list li {
        padding: 0.5rem 0;
        border-bottom: 1px solid var(--border-color);
    }
    
    .credentials-list li:before {
        content: "✓";
        color: var(--secondary-color);
        font-weight: bold;
        margin-right: 1rem;
    }
    
    hr {
        border: none;
        height: 1px;
        background-color: var(--border-color);
        margin: 2rem 0;
    }
    
    .badge {
        display: inline-block;
        background-color: var(--secondary-color);
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .main-subtitle {
            font-size: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
def show_navigation():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("### **Neuroscience Performance Solutions**")
    with col2:
        if st.button("Performance Fixes", key="nav_services"):
            st.session_state.page = "services"
    with col3:
        if st.button("Method", key="nav_method"):
            st.session_state.page = "method"
    with col4:
        if st.button("Credentials", key="nav_about"):
            st.session_state.page = "about"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'services'

# Header Section
def show_header():
    st.markdown("""
    <div class="main-header">
        <div class="main-title">The Neuroscience Performance Fix for Asia's Finance Leaders</div>
        <div class="main-subtitle">Override mental blocks in 2 sessions • Used by hedge fund managers and C-suite executives</div>
        <div class="credentials">Laetitia Sheppard | 13+ Years Financial Markets | Certified Behavioral Performance Specialist</div>
    </div>
    """, unsafe_allow_html=True)

# Services Page
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
            <div class="problem-title">Eliminating Boardroom Freeze</div>
            <div class="problem-description">When presentations to senior management trigger unproductive hesitation, despite your expertise.</div>
            <div class="problem-result">→ Command authority in high-pressure meetings</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Strategic Delegation for Leaders</div>
            <div class="problem-description">When needing to trust your team more to focus on high-value decisions.</div>
            <div class="problem-result">→ Reduce micromanagement by 60-80%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Jet Lag & Sleep Optimization</div>
            <div class="problem-description">When travel fatigue and racing thoughts impact next-day performance.</div>
            <div class="problem-result">→ 90% faster sleep onset for APAC travelers</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Negotiation Pressure Control</div>
            <div class="problem-description">When emotions surface during critical deals or conflict situations.</div>
            <div class="problem-result">→ Maintain strategic composure in any discussion</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="problem-card">
            <div class="problem-title">Stress Resilience Protocol</div>
            <div class="problem-description">When unhealthy coping mechanisms emerge from market volatility stress.</div>
            <div class="problem-result">→ Replace destructive habits with peak performance responses</div>
        </div>
        """, unsafe_allow_html=True)

    # CTA Section
    st.markdown("""
    <div class="cta-section">
        <h3>Limited Availability: 5 Performance Audits/Month</h3>
        <p>Our neuroscience-based method works in 2 sessions for finance professionals across Asia.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Apply for Performance Audit", key="main_cta"):
            webbrowser.open("https://calendly.com/titre/free-session")

# Method Page
def show_method():
    st.markdown('<div class="section-title">The 2-Session Neuroscience Method</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem; font-size: 1.1rem;">
        Developed specifically for finance professionals in Bangkok, Singapore, and Hong Kong
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="method-step">
            <div class="step-number">1</div>
            <h4>Performance Pattern Mapping</h4>
            <p>Precision analysis of when and how your decision-making gets hijacked under pressure.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="method-step">
            <div class="step-number">2</div>
            <h4>Neural Pathway Rewiring</h4>
            <p>Science-based techniques to install new automatic responses at the unconscious level.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="method-step">
            <div class="step-number" style="background-color: var(--secondary-color);">3</div>
            <h4>Reinforcement (If Needed)</h4>
            <p>Optional follow-ups to strengthen new patterns. Most clients achieve results in 2 sessions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # FAQ Section
    st.markdown("### Asia-Specific Questions")
    
    with st.expander("How is this different from executive coaching?"):
        st.write("While coaching discusses strategies, we reprogram the unconscious neural patterns that sabotage your performance. It's what makes top traders and surgeons perform under extreme pressure.")
    
    with st.expander("Why does this work in just 2 sessions?"):
        st.write("We target specific neural pathways rather than exploring your childhood. Our finance clients need efficiency - the average improvement in decision speed is 42% after Session 2.")
    
    with st.expander("Is this confidential?"):
        st.write("Absolutely. Our Bangkok clinic serves private bankers, fund managers, and C-suite executives who require discretion. No records are kept beyond what's legally required.")

# About Page  
def show_about():
    st.markdown('<div class="section-title">Why Finance Leaders Trust This Method</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.info("Professional photo placeholder")
    
    with col2:
        st.markdown("""
        **Built for Asia's financial hubs** - This method was developed through:
        - 13+ years on trading floors (Bloomberg, HSBC, Credit Agricole)
        - Working with 48-person teams across 12 countries
        - Managing $50M portfolios through market crises
        
        **Recognized Credentials:**
        - Certified Behavioral Performance Specialist (London, 2017)
        - Neuroscience-Based Coaching Certification (2023)
        - Fluent in the languages of Asian finance: English, French, Spanish, Italian
        """)

    st.markdown("---")
    
    # Testimonials
    st.markdown('<div class="section-title">Performance Results</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            "From hesitating in board meetings to leading them confidently. The change was measurable in my deal closure rate."
            <div class="testimonial-author">— Sarah M., MD at International Bank (Bangkok)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            "After 2 sessions, my sleep quality improved and I reduced decision fatigue by 70%. Game-changer for APAC travel."
            <div class="testimonial-author">— Marcus L., PE Partner (Singapore)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Contact Section
    st.markdown("### Limited Availability Performance Audit")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Bangkok Performance Clinic:**  
        46/9 Soi Sukhumvit 49 (Wireless Road Area)
        
        **Serving:**  
        - Portfolio Managers  
        - Investment Bankers  
        - C-Suite Expats  
        - Hedge Fund Teams  
        
        **Languages:** English, French, Spanish, Italian
        """)
        
        if st.button("📅 Apply Now (5 Slots/Month)", key="about_cta"):
            webbrowser.open("https://calendly.com/titre/free-session")
    
    with col2:
        try:
            st.image("./img/Map.png", caption="Bangkok Financial District Location")
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
st.markdown("*Neuroscience Performance Solutions | For Finance Leaders in Bangkok, Singapore & Hong Kong*")
