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
    padding: 1rem;
    line-height: 1.6;
}

.main-header {
    background: var(--primary-color);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    border-radius: 12px;
    border-left: 6px solid var(--accent-color);
    margin-bottom: 3rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.main-subtitle {
    font-size: 1.3rem;
    color: #d1d1d6;
    margin-bottom: 1.5rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.credentials {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
}

.nav-bar {
    display: flex;
    justify-content: center;
    margin: 2rem 0 3rem 0;
    gap: 3rem;
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

.nav-button-active {
    color: var(--primary-color);
    border-bottom: 2px solid var(--accent-color);
}

.nav-button:hover {
    color: var(--primary-color);
    transform: translateY(-2px);
}

.problem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.problem-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.problem-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.problem-icon {
    font-size: 2rem;
    color: var(--accent-color);
    margin-bottom: 1rem;
}

.problem-title {
    font-weight: 700;
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

.problem-description {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    color: var(--text-muted);
    line-height: 1.6;
}

.problem-result {
    font-style: italic;
    color: var(--secondary-color);
    border-top: 1px dashed var(--border-color);
    padding-top: 1rem;
    margin-top: 1rem;
    font-size: 1rem;
}

.section-header {
    margin: 4rem 0 2rem 0;
}

.sub-section-title {
    font-size: 1.8rem;
    font-weight: 600;
    color: var(--primary-color);
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    border-left: 4px solid var(--accent-color);
    padding-left: 1rem;
}

.method-timeline {
    background: var(--card-bg);
    padding: 2.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    margin: 2rem 0;
}

.timeline-item {
    display: flex;
    align-items: flex-start;
    margin: 2rem 0;
}

.timeline-number {
    background: var(--accent-color);
    color: var(--primary-color);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 1.5rem;
    flex-shrink: 0;
}

.timeline-content {
    flex: 1;
}

.timeline-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    color: var(--primary-color);
}

.timeline-description {
    color: var(--text-muted);
    line-height: 1.6;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.testimonial-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
    border-left: 4px solid var(--accent-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

.testimonial-text {
    font-style: italic;
    margin-bottom: 1.5rem;
    color: var(--text-color);
}

.testimonial-author {
    font-weight: 600;
    color: var(--primary-color);
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.stat-card {
    background: var(--card-bg);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    text-align: center;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--accent-color);
    margin-bottom: 0.5rem;
}

.stat-label {
    color: var(--text-muted);
    font-size: 0.95rem;
}

.contact-card {
    background: var(--primary-color);
    color: white;
    padding: 3rem;
    border-radius: 12px;
    margin: 3rem 0;
    border-top: 4px solid var(--accent-color);
}

.stButton > button {
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 0.8rem 2rem;
    font-weight: 600;
    border-radius: 6px;
    border: none;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    margin: 0.5rem;
}

.stButton > button:hover {
    background-color: #c7a133;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);
}

.footer {
    text-align: center;
    margin-top: 4rem;
    padding: 2rem 0;
    color: var(--text-muted);
    border-top: 1px solid var(--border-color);
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown("""
<div class="main-header">
    <div class="main-title">Rewire What's Holding You Back - In Just 2 Sessions</div>
    <div class="main-subtitle">
        Neuroscience-based hypnotherapy for ambitious professionals in Bangkok<br>
        Break through stress, weight blocks, and career plateaus with precision
    </div>
    <div>
        <button class="stButton">🧠 Book Your Breakthrough Session</button>
    </div>
    <div class="credentials">
        Certified Clinical Hypnotherapist • DBT Specialist • Neuroscience Coach
    </div>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
tabs = [("🔥 Your Blocks", "problems"), ("🧠 The Method", "method"), ("🏆 Results", "results"), ("👤 About", "about")]
cols = st.columns(len(tabs))
for i, (label, page_name) in enumerate(tabs):
    css_class = "nav-button-active" if st.session_state.page == page_name else "nav-button"
    with cols[i]:
        if st.button(f"{label}", key=page_name):
            st.session_state.page = page_name
st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE CONTENT ---
def show_problems():
    st.markdown('<div class="sub-section-title">The Hidden Blocks We Solve</div>', unsafe_allow_html=True)
    
    problems_data = [
        {
            "icon": "🧱",
            "title": "The Bangkok Glass Ceiling",
            "description": "You're hitting an invisible barrier in your career progression despite your skills. The rules feel different here, and you're not getting the traction you deserve.",
            "result": "→ Rewire subconscious blocks to advancement and align with opportunities"
        },
        {
            "icon": "⚖️", 
            "title": "Stress-Weight Cycle",
            "description": "Bangkok's intense work culture leads to stress eating, disrupted sleep, and weight that won't budge no matter what you try.",
            "result": "→ Break the cortisol cycle and reset your metabolic programming"
        },
        {
            "icon": "🔄",
            "title": "Expat Adaptation Fatigue",
            "description": "The constant cultural code-switching is exhausting. You feel like you're losing your authentic self while navigating Thai business culture.",
            "result": "→ Develop effortless cultural fluency while maintaining core identity"
        },
        {
            "icon": "📉",
            "title": "Performance Plateaus",
            "description": "Your usual strategies aren't working as well in the Bangkok context. Presentations fall flat, negotiations stall, and confidence slips.",
            "result": "→ Install high-performance patterns tailored to Asian business contexts"
        }
    ]
    
    st.markdown("<div class='problem-grid'>", unsafe_allow_html=True)
    for problem in problems_data:
        st.markdown(f"""
        <div class='problem-card'>
            <div class='problem-icon'>{problem['icon']}</div>
            <div class='problem-title'>{problem['title']}</div>
            <div class='problem-description'>{problem['description']}</div>
            <div class='problem-result'>{problem['result']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">Why It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Sessions for breakthrough</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">92%</div>
            <div class="stat-label">Report significant improvement</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">5-7x</div>
            <div class="stat-label">Faster than traditional therapy</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">0</div>
            <div class="stat-label">Ongoing sessions needed</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown('<div class="sub-section-title">The 2-Session Neuroscience Method</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="method-timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content">
                <div class="timeline-title">Pattern Mapping (90 min)</div>
                <div class="timeline-description">
                    Identify how pressure hijacks your systems:
                    <ul>
                        <li>Exact neural pathways maintaining your blocks</li>
                        <li>Bangkok-specific stress triggers</li>
                        <li>Most efficient rewiring strategy</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content">
                <div class="timeline-title">Neural Rewiring (60 min)</div>
                <div class="timeline-description">
                    Using clinical hypnotherapy enhanced with:
                    <ul>
                        <li>DBT techniques for emotional regulation</li>
                        <li>NLP for Bangkok business contexts</li>
                        <li>Somatic markers to anchor new patterns</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<div class="sub-section-title">Client Transformations</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial-grid">
        <div class="testimonial-card">
            <div class="testimonial-text">
                "After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."
            </div>
            <div class="testimonial-author">
                — French Tech Director, Fortune 500
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">
                "The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."
            </div>
            <div class="testimonial-author">
                — American PE VP, Bangkok
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
    with col2:
        st.markdown('<div class="sub-section-title">About Laetitia</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-bottom: 2rem;">
            <p><strong>Bangkok-based specialist</strong> with 13 years in Asian financial hubs (Hong Kong, Singapore, Bangkok)</p>
            <p>Understands the unique pressures of:</p>
            <ul>
                <li>Expat stress meets career ambition</li>
                <li>Thai business culture nuances</li>
                <li>Metabolic impact of Bangkok's environment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-card">
        <div style="text-align: center;">
            <h3 style="color: white; margin-bottom: 1rem;">Bangkok Hypnotherapy Clinic</h3>
            <p style="margin-bottom: 1.5rem;">46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
            <button class="stButton">📍 Get Directions</button>
            <button class="stButton">📅 Book Discovery Call</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
<div class="footer">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
