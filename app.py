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
    --primary-color: #1C1C1E;
    --accent-color: #D4AF37;
    --secondary-color: #3A3A3C;
    --bg-color: #F4F4F6;
    --card-bg: #FFFFFF;
    --text-color: #1C1C1E;
    --text-muted: #6E6E73;
    --border-color: #E2E2E6;
}

[data-theme="dark"] {
    --primary-color: #1C1C1E;
    --accent-color: #F9C74F;
    --secondary-color: #4D4D50;
    --bg-color: #121212;
    --card-bg: #1E1E1E;
    --text-color: #FAFAFA;
    --text-muted: #9A9AA1;
    --border-color: #333333;
}

.stApp {
    font-family: 'Inter', sans-serif;
    color: var(--text-color);
    background-color: var(--bg-color);
    line-height: 1.6;
}

.main-header {
    background: var(--primary-color);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 2rem;
    border-bottom: 4px solid var(--accent-color);
}

.problem-card, .method-step, .testimonial-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.problem-card:hover, .method-step:hover, .testimonial-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.problem-title, .section-title, .testimonial-author {
    color: var(--primary-color);
    font-weight: 600;
}

.problem-result {
    color: var(--accent-color);
    font-weight: 600;
}

.section-title {
    font-size: 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    border-bottom: 2px solid var(--accent-color);
    padding-bottom: 0.5rem;
}

.cta-section {
    background: var(--primary-color);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    border-top: 4px solid var(--accent-color);
    text-align: center;
    margin-top: 3rem;
}

.stButton>button {
    background-color: var(--accent-color);
    color: var(--primary-color);
    border: none;
    padding: 0.75rem 1.25rem;
    font-weight: bold;
    border-radius: 6px;
    transition: background 0.3s ease, transform 0.2s ease;
}

.stButton>button:hover {
    background-color: #C99F2E;
    transform: translateY(-2px);
}

.badge {
    background-color: var(--secondary-color);
    color: white;
    padding: 0.3rem 0.7rem;
    border-radius: 4px;
    font-size: 0.75rem;
    margin: 0.25rem;
}

.credentials, .problem-description, .problem-result {
    color: var(--text-muted);
}

hr {
    border: none;
    height: 1px;
    background-color: var(--border-color);
    margin: 2rem 0;
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
