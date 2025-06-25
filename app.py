import streamlit as st
import webbrowser

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Bangkok Hypnotherapy | Breakthrough in 2 Sessions | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
:root {
    --primary-color: #2c3e50;
    --accent-color: #e74c3c;
    --secondary-color: #3498db;
    --bg-color: #f5f7fa;
    --card-bg: #ffffff;
    --text-color: #2c3e50;
    --text-muted: #7f8c8d;
    --border-color: #dfe6e9;
    --success-color: #27ae60;
}

.stApp {
    font-family: 'Inter', -apple-system, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

.hero-section {
    background: linear-gradient(135deg, var(--primary-color) 0%, #1a2b3c 100%);
    color: white;
    padding: 5rem 2rem;
    text-align: center;
    border-radius: 0 0 20px 20px;
    margin-bottom: 3rem;
    position: relative;
    overflow: hidden;
}

.hero-section::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--accent-color), var(--secondary-color));
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    opacity: 0.9;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.cta-button {
    background: var(--accent-color);
    color: white;
    padding: 1rem 2.5rem;
    border: none;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
    margin: 0.5rem;
}

.cta-button:hover {
    background: #c0392b;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(231, 76, 60, 0.4);
    color: white;
    text-decoration: none;
}

.nav-container {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
    gap: 1rem;
    flex-wrap: wrap;
}

.nav-pill {
    background: white;
    border: 2px solid var(--border-color);
    padding: 0.8rem 1.8rem;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 600;
    color: var(--text-color);
}

.nav-pill-active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.nav-pill:hover {
    border-color: var(--accent-color);
    transform: translateY(-2px);
}

.problem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.problem-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.problem-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
}

.problem-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--accent-color), var(--secondary-color));
}

.problem-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
    color: var(--accent-color);
}

.problem-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

.problem-description {
    font-size: 1rem;
    margin-bottom: 1.5rem;
    color: var(--text-muted);
}

.problem-result {
    font-weight: 600;
    color: var(--success-color);
    font-size: 1rem;
    border-top: 1px dashed var(--border-color);
    padding-top: 1rem;
    margin-top: 1rem;
}

.section-header {
    text-align: center;
    margin: 4rem 0 3rem 0;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 1rem;
    position: relative;
    display: inline-block;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--accent-color), var(--secondary-color));
    border-radius: 2px;
}

.section-subtitle {
    font-size: 1.2rem;
    color: var(--text-muted);
    max-width: 700px;
    margin: 0 auto;
}

.method-timeline {
    background: var(--card-bg);
    padding: 3rem;
    border-radius: 16px;
    margin: 2rem 0;
    position: relative;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
}

.timeline-item {
    display: flex;
    align-items: flex-start;
    margin: 2.5rem 0;
    position: relative;
}

.timeline-number {
    background: var(--accent-color);
    color: white;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 2rem;
    flex-shrink: 0;
    font-size: 1.2rem;
}

.timeline-content {
    flex: 1;
}

.timeline-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

.timeline-description {
    color: var(--text-muted);
    line-height: 1.7;
}

.testimonial-card {
    background: var(--card-bg);
    padding: 2.5rem;
    border-radius: 16px;
    border-left: 4px solid var(--accent-color);
    margin: 1.5rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    position: relative;
}

.testimonial-card::before {
    content: '"';
    position: absolute;
    top: 10px;
    left: 20px;
    font-size: 5rem;
    color: rgba(231, 76, 60, 0.1);
    font-family: serif;
    line-height: 1;
}

.testimonial-text {
    font-size: 1.1rem;
    font-style: italic;
    margin-bottom: 1.5rem;
    color: var(--text-color);
    position: relative;
    z-index: 1;
}

.testimonial-author {
    font-weight: 700;
    color: var(--primary-color);
}

.contact-card {
    background: var(--primary-color);
    color: white;
    padding: 3rem;
    border-radius: 16px;
    margin: 3rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    border-top: 4px solid var(--accent-color);
}

.location-badge {
    display: inline-block;
    background-color: rgba(255,255,255,0.15);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    backdrop-filter: blur(5px);
}

.credential-badge {
    display: inline-flex;
    align-items: center;
    background-color: rgba(231, 76, 60, 0.1);
    color: var(--accent-color);
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid var(--accent-color);
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
    text-align: center;
}

.stat-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
}

.stat-number {
    font-size: 2.8rem;
    font-weight: 800;
    color: var(--accent-color);
    display: block;
    line-height: 1;
}

.stat-label {
    font-size: 1rem;
    color: var(--text-muted);
    margin-top: 1rem;
}

.stButton > button {
    background: var(--accent-color) !important;
    color: white !important;
    padding: 0.8rem 2rem !important;
    border-radius: 50px !important;
    border: none !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3) !important;
}

.stButton > button:hover {
    background: #c0392b !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(231, 76, 60, 0.4) !important;
}

.footer {
    text-align: center;
    margin-top: 4rem;
    padding: 2rem 0;
    color: var(--text-muted);
    font-size: 0.9rem;
    border-top: 1px solid var(--border-color);
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Break Through Your Glass Ceiling in Bangkok — In Just 2 Sessions</div>
    <div class="hero-subtitle">
        Hypnotherapy meets neuroscience to help ambitious professionals overcome stress, weight blocks, 
        and career plateaus in Thailand's competitive environment. Fast, focused, and confidential.
    </div>
    <br>
    <a href="https://calendly.com/titre/discovery-call" class="cta-button">
        🧠 Book Your Breakthrough Session (Bangkok/Online)
    </a>
    <br>
    <div style="margin-top: 1rem;">
        <span class="location-badge">Thong Lor Clinic</span>
        <span class="location-badge">Sukhumvit 49</span>
        <span class="location-badge">Remote Sessions Available</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("<div class=\"nav-container\">", unsafe_allow_html=True)
tabs = [
    ("🔥 Your Blocks", "problems"),
    ("⚡ 2-Session Solution", "method"), 
    ("🏆 Success Stories", "results"),
    ("👩‍⚕️ About Me", "about")
]

cols = st.columns(len(tabs))
for i, (label, page_name) in enumerate(tabs):
    with cols[i]:
        if st.button(label, key=f"nav_{page_name}"):
            st.session_state.page = page_name
st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE CONTENT ---
def show_problems():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">The Hidden Blocks Holding You Back in Bangkok</div>
        <div class="section-subtitle">
            These are the most common patterns I help ambitious professionals overcome through targeted hypnotherapy
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    problems_data = [
        {
            "icon": "🧱",
            "title": "The Bangkok Glass Ceiling",
            "description": "You're hitting an invisible barrier in your career progression despite your skills and efforts. The rules feel different here, and you're not getting the traction you deserve.",
            "result": "→ Rewire subconscious blocks to advancement and align with opportunities"
        },
        {
            "icon": "⚖️", 
            "title": "Stress-Weight Cycle",
            "description": "Bangkok's intense work culture leads to stress eating, disrupted sleep, and weight that won't budge no matter what you try. The harder you push, the worse it gets.",
            "result": "→ Break the cortisol cycle and reset your metabolic programming"
        },
        {
            "icon": "🔄",
            "title": "Expat Adaptation Fatigue",
            "description": "The constant cultural code-switching is exhausting. You feel like you're losing your authentic self while trying to navigate Thai business culture.",
            "result": "→ Develop effortless cultural fluency while maintaining core identity"
        },
        {
            "icon": "📉",
            "title": "Performance Plateaus",
            "description": "Your usual strategies aren't working as well in the Bangkok context. Presentations fall flat, negotiations stall, and your confidence is slipping.",
            "result": "→ Install high-performance patterns tailored to Asian business contexts"
        }
    ]
    
    st.markdown("<div class=\"problem-grid\">", unsafe_allow_html=True)
    for problem in problems_data:
        st.markdown(f"""
        <div class="problem-card">
            <span class="problem-icon">{problem['icon']}</span>
            <div class="problem-title">{problem['title']}</div>
            <div class="problem-description">{problem['description']}</div>
            <div class="problem-result">{problem['result']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Stats section
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Why Hypnotherapy Works When Other Methods Fail</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <span class="stat-number">5-7x</span>
            <div class="stat-label">Faster than traditional therapy</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">92%</span>
            <div class="stat-label">Report significant improvement after 2 sessions</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">2</span>
            <div class="stat-label">Weeks to first measurable results</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">0</span>
            <div class="stat-label">Need for ongoing weekly sessions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">The Precision 2-Session Breakthrough</div>
        <div class="section-subtitle">
            How we create rapid, lasting change for Bangkok professionals
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="method-timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content">
                <div class="timeline-title">Deep Pattern Mapping (90 min)</div>
                <div class="timeline-description">
                    We identify:
                    <ul>
                        <li>The <strong>exact neural pathways</strong> maintaining your blocks</li>
                        <li>How Bangkok-specific stressors interact with your patterns</li>
                        <li>The most efficient rewiring strategy for your brain</li>
                    </ul>
                    <em>Includes pre-session assessment and Bangkok-specific stress profile</em>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content">
                <div class="timeline-title">Targeted Neural Rewiring (60 min)</div>
                <div class="timeline-description">
                    Using clinical hypnotherapy enhanced with:
                    <ul>
                        <li><strong>DBT techniques</strong> for emotional regulation</li>
                        <li><strong>Neuro-linguistic programming</strong> for Bangkok business contexts</li>
                        <li><strong>Somatic markers</strong> to anchor new patterns</li>
                    </ul>
                    <em>Includes custom audio reinforcement for Bangkok living</em>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-header">
        <div class="section-title">Who This Works Best For</div>
    </div>
    
    <div class="problem-grid">
        <div class="problem-card">
            <div class="problem-title">Corporate Leaders</div>
            <div class="problem-description">
                Breaking through senior management barriers in Thai conglomerates or multinationals
            </div>
        </div>
        <div class="problem-card">
            <div class="problem-title">Entrepreneurs</div>
            <div class="problem-description">
                Overcoming growth plateaus in Thailand's competitive startup scene
            </div>
        </div>
        <div class="problem-card">
            <div class="problem-title">Expats</div>
            <div class="problem-description">
                Adapting to Thai business culture without losing your edge
            </div>
        </div>
        <div class="problem-card">
            <div class="problem-title">High-Potentials</div>
            <div class="problem-description">
                Preparing for leadership roles in Asia's fast-moving markets
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Bangkok Success Stories</div>
        <div class="section-subtitle">
            Real breakthroughs from professionals like you
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-text">
                "After 2 sessions, I went from freezing in regional presentations to delivering my best keynote yet at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."
            </div>
            <div class="testimonial-author">
                — French Tech Director, Fortune 500 Company
            </div>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-text">
                "The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and my career trajectory."
            </div>
            <div class="testimonial-author">
                — American Private Equity VP, Bangkok
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-text">
                "I was ready to quit Thailand after 6 frustrating months. Two sessions later, I cracked the cultural code and landed my biggest client. That was 3 years ago - I'm now running the regional office."
            </div>
            <div class="testimonial-author">
                — German Managing Director, Consulting Firm
            </div>
        </div>
        
        <div class="testimonial-card">
            <div class="testimonial-text">
                "The glass ceiling shattered within 3 months. I got the promotion I'd been passed over for twice, with a 40% pay increase. Laetitia's approach is like a secret weapon for corporate Asia."
            </div>
            <div class="testimonial-author">
                — Thai Senior Manager, Multinational Bank
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <a href="https://calendly.com/titre/discovery-call" class="cta-button">
            🧠 Book Your Breakthrough Session
        </a>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">About Laetitia Sheppard</div>
        <div class="section-subtitle">
            Your Bangkok-based Hypnotherapy Specialist
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=500", width=300)
    
    with col2:
        st.markdown("""
        <div style="margin-bottom: 2rem;">
            <h3 style="color: var(--primary-color);">Why I Specialize in Bangkok Professionals</h3>
            <p>With 13 years in Asian financial hubs (Hong Kong, Singapore, Bangkok), I understand the unique pressures you face:</p>
            <ul>
                <li>The intersection of expat stress and career ambition</li>
                <li>Thai business culture nuances that trigger unconscious blocks</li>
                <li>The metabolic impact of Bangkok's work-hard-play-hard environment</li>
            </ul>
        </div>
        
        <div>
            <h3 style="color: var(--primary-color);">Credentials That Matter</h3>
            <div style="margin-bottom: 1rem;">
                <span class="credential-badge">Certified Clinical Hypnotherapist (LCCH, UK)</span>
                <span class="credential-badge">DBT Practitioner</span>
                <span class="credential-badge">Neuroscience Coach</span>
                <span class="credential-badge">Fluent in 4 Languages</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-card">
        <div style="text-align: center;">
            <h2 style="color: white; margin-bottom: 1rem;">Bangkok Hypnotherapy Clinic</h2>
            <p style="margin-bottom: 2rem;">46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
            <a href="https://maps.google.com" class="cta-button" style="background: white; color: var(--accent-color);">
                📍 Get Directions
            </a>
            <a href="https://calendly.com/titre/discovery-call" class="cta-button">
                📅 Book Discovery Call
            </a>
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
    <p>Laetitia Sheppard • Neuroscience-Based Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
