import streamlit as st
import webbrowser

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuro-Hypnotherapy Solutions | Laetitia Sheppard | Bangkok",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
:root {
    --primary-color: #1a365d;
    --accent-color: #5e35b1;
    --secondary-color: #3949ab;
    --bg-color: #f8f9fa;
    --card-bg: #ffffff;
    --text-color: #1f2937;
    --text-muted: #6b7280;
    --border-color: #e5e7eb;
    --success-color: #2e7d32;
}

[data-theme="dark"] {
    --primary-color: #5e35b1;
    --accent-color: #7e57c2;
    --secondary-color: #3949ab;
    --bg-color: #111827;
    --card-bg: #1f2937;
    --text-color: #f3f4f6;
    --text-muted: #9ca3af;
    --border-color: #374151;
    --success-color: #4caf50;
}

.stApp {
    font-family: 'Inter', -apple-system, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

.hero-section {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    padding: 4rem 2rem;
    text-align: center;
    border-radius: 16px;
    margin-bottom: 3rem;
    border-bottom: 4px solid var(--accent-color);
}

.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
}

.hero-subtitle {
    font-size: 1.4rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

.credentials-badge {
    background: rgba(255,255,255,0.15);
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    display: inline-block;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
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
    text-decoration: none;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(94, 53, 177, 0.3);
}

.cta-button:hover {
    background: #4527a0;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(94, 53, 177, 0.4);
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
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.nav-pill-active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.nav-pill:hover {
    border-color: var(--accent-color);
    transform: translateY(-1px);
}

.problem-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
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

.problem-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--accent-color), var(--primary-color));
}

.problem-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
}

.problem-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
}

.problem-title {
    font-size: 1.3rem;
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
    font-size: 0.95rem;
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
    border-bottom: 2px solid var(--accent-color);
    display: inline-block;
    padding-bottom: 0.5rem;
}

.section-subtitle {
    font-size: 1.2rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto;
}

.testimonial-card {
    background: var(--card-bg);
    padding: 2.5rem;
    border-radius: 16px;
    border-left: 4px solid var(--accent-color);
    margin: 1.5rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.testimonial-text {
    font-size: 1.1rem;
    font-style: italic;
    margin-bottom: 1rem;
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
    text-align: center;
}

.stat-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--accent-color);
    display: block;
}

.stat-label {
    font-size: 1rem;
    color: var(--text-muted);
    margin-top: 0.5rem;
}

.method-timeline {
    background: var(--card-bg);
    padding: 3rem;
    border-radius: 16px;
    margin: 2rem 0;
    position: relative;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.timeline-item {
    display: flex;
    align-items: center;
    margin: 2rem 0;
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
}

.timeline-content {
    flex: 1;
}

.timeline-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--primary-color);
}

.timeline-description {
    color: var(--text-muted);
}

.contact-section {
    background: var(--primary-color);
    color: white;
    padding: 4rem 2rem;
    border-radius: 16px;
    text-align: center;
    margin: 3rem 0;
    border-top: 4px solid var(--accent-color);
}

.location-badge {
    display: inline-block;
    background-color: var(--accent-color);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

.credential-badge {
    display: inline-flex;
    align-items: center;
    background-color: rgba(94, 53, 177, 0.1);
    color: var(--accent-color);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid var(--accent-color);
}

.stButton > button {
    background: var(--accent-color) !important;
    color: white !important;
    padding: 0.8rem 2rem !important;
    border-radius: 25px !important;
    border: none !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: #4527a0 !important;
    transform: translateY(-2px) !important;
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Unlock Your Potential: Rapid Neural Rewiring</div>
    <div class="hero-subtitle">
        Break free from what's holding you back – often in just 2 sessions.<br>
        Find your path of least resistance to overcome burnout, stagnation, and cultural fatigue,<br>
        with targeted neural reprogramming for ambitious global professionals.
    </div>
    <div class="credentials-badge">
        🇫🇷🇬🇧 Certified Hypnotherapist (LCCH) • DBT Specialist • MIT-Trained Innovator
    </div>
    <br>
    <a href="https://calendly.com/titre/discovery-call" class="cta-button">
        🧠 Book Your Breakthrough Session
    </a>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
tabs = [
    ("🔥 Your Challenges", "problems"),
    ("🧠 The 2-Session Path", "method"), 
    ("📜 My Expertise", "about"),
    ("📍 Thong Lor Clinic", "contact")
]

cols = st.columns(len(tabs))
for i, (label, page_name) in enumerate(tabs):
    with cols[i]:
        if st.button(label, key=f"nav_{page_name}"):
            st.session_state.page = page_name

st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE CONTENT ---
def show_problems():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Are You Experiencing These Challenges?</div>
        <div class="section-subtitle">
            For global professionals, your unique journey can sometimes lead to unexpected blocks.
        </div>
    </div>
    
    <div style="text-align: center; margin-bottom: 2rem;">
        <span class="location-badge">Bangkok</span>
        <span class="location-badge">Singapore</span>
        <span class="location-badge">Hong Kong</span>
    </div>
    """, unsafe_allow_html=True)
    
    problems_data = [
        {
            "icon": "🪞",
            "title": "Hitting an Invisible Wall?",
            "description": "You're skilled and hardworking, yet feel stuck, unable to advance despite your efforts. It's like an invisible barrier is holding you back.",
            "result": "→ Discover your path of least resistance to career growth and personal freedom."
        },
        {
            "icon": "🔥", 
            "title": "The Burnout-Boredom Cycle (The '3B' State)",
            "description": "Feeling exhausted, uninspired, or disconnected from your purpose? You might be cycling between burnout, boredom, and a sense of 'brown out'.",
            "result": "→ Re-energize your drive and find sustainable engagement."
        },
        {
            "icon": "🌐",
            "title": "Cultural Fatigue?",
            "description": "Constantly adapting your communication style across cultures can be draining, diluting your authentic leadership presence.",
            "result": "→ Build mental resilience and communicate authentically without exhaustion."
        },
        {
            "icon": "🔄",
            "title": "Effort vs. Reward Imbalance?",
            "description": "Working harder than others but seeing less recognition or results. The easy path seems blocked, and you're left feeling undervalued.",
            "result": "→ Align your efforts with tangible rewards and unlock your natural flow."
        }
    ]
    
    st.markdown('<div class="problem-grid">', unsafe_allow_html=True)
    for problem in problems_data:
        st.markdown(f"""
        <div class="problem-card">
            <span class="problem-icon">{problem['icon']}</span>
            <div class="problem-title">{problem['title']}</div>
            <div class="problem-description">{problem['description']}</div>
            <div class="problem-result">{problem['result']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Stats section
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Real Results, Lasting Change</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <span class="stat-number">2</span>
            <div class="stat-label">Targeted sessions for initial breakthrough</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">89%</span>
            <div class="stat-label">Report reduced 3B symptoms in 3 weeks</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">6</span>
            <div class="stat-label">Months average between reinforcement sessions</div>
        </div>
        <div class="stat-card">
            <span class="stat-number">72%</span>
            <div class="stat-label">Career advancement within 1 year</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_method():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">The Precision 2-Session Protocol</div>
        <div class="section-subtitle">
            Neuroscience meets clinical hypnotherapy for lasting change
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="method-timeline">
        <div class="timeline-item">
            <div class="timeline-number">1</div>
            <div class="timeline-content">
                <div class="timeline-title">Pattern Mapping (90 min)</div>
                <div class="timeline-description">
                    <strong>Understanding Your Brain's Blueprint:</strong> Through neuro-linguistic analysis, we identify:
                    <ul>
                        <li>The exact thought patterns and beliefs holding you back.</li>
                        <li>Any hidden benefits you might unconsciously gain from your current patterns.</li>
                        <li>The most effective strategy to 'rewire' your brain for success.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">2</div>
            <div class="timeline-content">
                <div class="timeline-title">Precision Rewiring (60 min)</div>
                <div class="timeline-description">
                    <strong>Installing New Pathways:</strong> Using clinical hypnotherapy and DBT techniques, we:
                    <ul>
                        <li>Create new, empowering neural circuits for breakthrough.</li>
                        <li>Anchor these positive changes to real-world situations.</li>
                        <li>Develop automatic access to a 'flow state' for peak performance.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="timeline-number">3+</div>
            <div class="timeline-content">
                <div class="timeline-title">Stepped Reinforcement (Optional)</div>
                <div class="timeline-description">
                    <strong>Sustaining Your Success:</strong> Every 3-6 months for:
                    <ul>
                        <li>Achieving new levels of performance.</li>
                        <li>Addressing new or unrelated challenges.</li>
                        <li>Evolving your leadership capabilities.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FAQ Section
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Questions from Global Professionals</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🧠 Why combine hypnotherapy with neuroscience?"):
        st.write("""
        **Hypnotherapy accesses unconscious patterns** - The root of your 3B state and glass ceiling feelings.  
        **Neuroscience provides precision** - We target specific neural circuits (like the default mode network for burnout).  
        **Together they create rapid, lasting change** - Typically in just 2 sessions with my method.
        """)
    
    with st.expander("🌏 Why does this work for third culture professionals?"):
        st.write("""
        **I specialize in cross-cultural neural patterns** - The unique ways global mindsets can create:
        - Hidden self-sabotage programs  
        - Cultural value conflicts  
        - Mismatched reward systems  
        
        **My clients include:**
        - Corporate leaders feeling "stuck" abroad  
        - Entrepreneurs with global teams  
        - Professionals navigating hybrid cultures  
        """)
    
    with st.expander("⏳ What's the maintenance schedule?"):
        st.write("""
        **Initial 2-session protocol** - Addresses your primary challenge  
        **Optional reinforcement every 3-6 months** - For:
        - New career levels  
        - Different challenge areas  
        - Leadership evolution  
        
        **72% of clients return** for unrelated issues after initial success.
        """)

def show_about():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">My Expertise for Global Professionals</div>
        <div class="section-subtitle">
            Blending clinical expertise with corporate experience
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            st.image("./img/ID.jpg", width=300, caption="Laetitia Sheppard | Bangkok")
        except:
            st.info("📸 Professional headshot placeholder")
    
    with col2:
        st.markdown("""
        ### Clinical Credentials
        
        <div style="margin-bottom: 1rem;">
            <span class="credential-badge">🎓 Cognitive Behavioral Hypnotherapy (LCCH, 2017)</span>
            <span class="credential-badge">🧠 DBT Certified (2024)</span>
            <span class="credential-badge">💡 MIT Innovation & Design Thinking (2016)</span>
        </div>
        
        **13 years in financial markets** gave me firsthand experience with:
        - Cross-cultural leadership challenges  
        - High-performance burnout cycles  
        - The glass ceiling phenomenon  
        
        **Languages:** English (native), French (native), Spanish, Italian  
        """)
    
    # Testimonials
    st.markdown("""
    <div class="section-header">
        <div class="section-title">What Clients Say</div>
    </div>
    """, unsafe_allow_html=True)
    
    testimonials = [
        {
            "text": "After years of feeling stuck despite stellar performance, two sessions rewired my self-presentation. I received a promotion I'd been passed over for three times.",
            "author": "— Regional Director, Tech Firm (French/American in Bangkok)"
        },
        {
            "text": "The cultural code-switching fatigue vanished. I now lead with authentic presence whether in Tokyo, London, or Singapore.",  
            "author": "— Investment Banker (Japanese/British)"
        },
        {
            "text": "From chronic burnout to sustainable high performance. My productivity increased while working 20% fewer hours.",
            "author": "— Startup Founder (Indian/Australian)"
        }
    ]
    
    for testimonial in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="testimonial-text">"{testimonial['text']}"</div>
            <div class="testimonial-author">{testimonial['author']}</div>
        </div>
        """, unsafe_allow_html=True)

def show_contact():
    st.markdown("""
    <div class="section-header">
        <div class="section-title">Thong Lor Neuro-Clinic</div>
        <div class="section-subtitle">
            Designed for discretion and focus
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📍 **Wireless Road Executive Suite**
        46/9 Soi Sukhumvit 49  
        Bangkok 10110  
        
        **For Global Professionals:**  
        - Soundproofed session rooms  
        - Discreet entrance/exit  
        - International charging stations  
        - Multilingual support staff  
        
        ### 🕒 **Session Times**  
        **Early/Late for Busy Schedules:**  
        - 7-9 AM before work  
        - 6-8 PM after hours  
        - Weekend intensive slots  
        
        ### 🌐 **Cultural Specialization**  
        - Third culture professionals  
        - Expat leaders  
        - Global hybrid teams  
        """)
        
        st.markdown("""
        <div class="contact-section">
            <h3>Ready for Your Breakthrough?</h3>
            <p>Currently accepting 8 new clients monthly</p>
            <br>
            <a href="https://calendly.com/titre/discovery-call" class="cta-button">
                🧠 Book Your Neural Audit
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st.image("./img/Map.png", caption="Thong Lor Global Business District")
        except:
            st.info("🗺️ Map placeholder - Wireless Road area")
        
        st.markdown("""
        ### 🎯 **Ideal Clients**  
        
        **Experiencing:**  
        - The 3B cycle (burned, bored, brown out)  
        - Glass ceiling frustration  
        - Cultural value conflicts at work  
        
        **Typically:**  
        - 35-55 year old professionals  
        - Earning $150K+ annually  
        - Managing global teams/projects  
        - Multilingual and multicultural  
        """)

# --- RENDER CURRENT PAGE ---
if st.session_state.page == "problems":
    show_problems()
elif st.session_state.page == "method":
    show_method()
elif st.session_state.page == "about":
    show_about()
elif st.session_state.page == "contact":
    show_contact()

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: var(--text-muted); padding: 2rem;'>
    <strong>Neuro-Hypnotherapy Solutions</strong> | Laetitia Sheppard | Bangkok<br>
    For third culture professionals breaking through glass ceilings
</div>
""", unsafe_allow_html=True)

