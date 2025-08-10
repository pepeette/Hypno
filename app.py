import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Hypnotherapy for Behavioral Change | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS INJECTION ---
def inject_css():
    st.markdown(f"""
    <style>
    :root {{
        --primary: #1C1C1E;
        --accent: #D4AF37;
        --light: #F4F4F6;
        --medium: #E2E2E6;
        --muted: #6E6E73;
        --white: #FFFFFF;
        --shadow: rgba(0,0,0,0.05);
        --shadow-hover: rgba(0,0,0,0.1);
        --shadow-accent: rgba(212, 175, 55, 0.2);
    }}

    /* Force light mode */
    [data-testid="stAppViewContainer"] {{
        background-color: var(--light) !important;
        color-scheme: light !important;
    }}
    
    /* Remove top padding */
    .stApp {{
        background: var(--light) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        line-height: 1.6;
        color: var(--primary) !important;
        padding-top: 0.25rem !important;
    }}
    
    /* Remove header space */
    .st-emotion-cache-1avcm0n {{
        display: none !important;
    }}
    
    /* Remove extra space at top */
    .st-emotion-cache-z5fcl4 {{
        padding-top: 0.25rem !important;
        padding-bottom: 0.25rem !important;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: var(--primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }}
    
    h1 {{
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin: 0.5rem 0 0.5rem 0 !important;
        color: var(--primary) !important;
    }}
    
    h2 {{
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
        margin: 0.5rem 0 0.5rem 0 !important;
        color: var(--primary) !important;
    }}
    
    p, li, span, div {{
        font-size: 1rem !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        color: var(--primary) !important;
        margin: 0.25rem 0 !important;
    }}
    
    strong, b {{
        font-weight: 600 !important;
        color: var(--primary) !important;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    .main-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }}

    .hero-title {{ 
        font-size: 1.5rem !important; 
        font-weight: 700 !important; 
        line-height: 1.2 !important; 
        margin: 0 !important;
        color: var(--white) !important;
    }}
    
    .hero-subtitle {{ 
        font-size: 1rem !important; 
        font-weight: 400 !important; 
        margin: 1rem 0 !important;
        color: #d1d1d6 !important;
    }}
    
    .muted-text {{ 
        color: var(--muted) !important; 
        font-size: 1rem !important;
        font-weight: 400 !important;
    }}

    .hero {{
        background: var(--primary);
        color: white;
        padding: 1rem 1rem;
        text-align: center;
        border-radius: 12px;
        margin: 0.25rem 0 0.25rem 0;
        border-left: 6px solid var(--accent);
    }}
    
    .hero * {{
        color: var(--white) !important;
    }}
    
    .hero .hero-subtitle {{ 
        color: #d1d1d6 !important; 
    }}
    
    .hero .muted-text {{ 
        color: #a1a1a6 !important; 
    }}

    .card {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px var(--shadow);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        min-height: 180px; /* Added minimum height for consistency */
        display: flex;
        flex-direction: column;
    }}

        .card-container {{
        display: grid;
        grid-template-columns: 1fr;
        gap: 1rem;
    }}
    
    .card-content {{
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }}
    
    .card h2 {{
        margin-top: 0 !important;
    }}
    
    .card p:last-child {{
        margin-top: auto;
        padding-top: 0.5rem;
    }}
    
    .card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px var(--shadow-hover);
    }}
    
    .card-accent {{
        border-left: 4px solid var(--accent);
    }}

    .btn {{
        background: var(--accent);
        color: var(--primary);
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        display: inline-block;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 8px var(--shadow-accent);
        margin: 0.5rem 0.5rem 0.5rem 0;
        text-decoration: none;
    }}
    
    .btn:hover {{
        background: #C7A133;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
    }}

    .nav-btn-active {{
        background: var(--accent) !important;
        color: var(--primary) !important;
    }}

    .stats {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.75rem;
        margin: 1rem 0;
    }}
    
    .stat {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }}
    
    .stat-number {{
        color: var(--accent) !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
    }}
    
    .stat-label {{
        font-size: 1rem;
        color: var(--muted);
    }}

    .contact {{
        background: var(--primary);
        color: white;
        padding: 1rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-top: 4px solid var(--accent);
        text-align: center;
    }}
    
    .contact h2 {{
        color: var(--white) !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }}
    
    .contact p {{
        color: var(--white) !important;
        margin-bottom: 1.5rem !important;
    }}

    .process-step {{
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }}
    
    .step-number {{
        background: var(--accent);
        color: var(--primary);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
    }}

    .text-center {{ text-align: center; }}
    .mt-1 {{ margin-top: 1rem; }}
    .mt-2 {{ margin-top: 2rem; }}
    .mb-1 {{ margin-bottom: 1rem; }}
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1 class="hero-title">Reprogram Your Mind, Change Your Life</h1>
    <p class="hero-subtitle">Hypnotherapy doesn't just change what you do—it changes how you do it. In just 2 sessions, it reprograms the patterns holding you back, so you can finally get the results you deserve.</p>
    <button class="btn">📅 Book a FREE 15-min Call</button>
    <p class="muted-text mt-1">Expert-guided | Confidential | Certified in Hypnotherapy and DBT</p>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS ---
cols = st.columns(4)
with cols[0]:
    problems_btn = st.button("🔥 Your Blocks", key="nav_problems", 
                            help="View common problems we solve",
                            type="primary" if st.session_state.page == "problems" else "secondary")
    if problems_btn:
        st.session_state.page = "problems"
        st.rerun()

with cols[1]:
    method_btn = st.button("🧠 The Method", key="nav_method", 
                          help="Learn about our 2-session method",
                          type="primary" if st.session_state.page == "method" else "secondary")
    if method_btn:
        st.session_state.page = "method"
        st.rerun()

with cols[2]:
    results_btn = st.button("🏆 Results", key="nav_results", 
                           help="See client transformations",
                           type="primary" if st.session_state.page == "results" else "secondary")
    if results_btn:
        st.session_state.page = "results"
        st.rerun()

with cols[3]:
    about_btn = st.button("👤 About", key="nav_about", 
                         help="About Laetitia and the clinic",
                         type="primary" if st.session_state.page == "about" else "secondary")
    if about_btn:
        st.session_state.page = "about"
        st.rerun()

# --- PAGE CONTENT FUNCTIONS ---
def show_problems():
    st.markdown('<h2>Common Blocks We Help Overcome</h2>', unsafe_allow_html=True)
    
    problems = [
        {
            "title": "The professional Glass Ceiling", 
            "desc": "Delivering great work but not advancing? Changing efforts alone won't fix it – we reprogram the underlying patterns.",
            "result": "→ Achieve breakthroughs with hypnotherapy"
        },
        {
            "title": "The Stress-Weight Spiral", 
            "desc": "Stress leading to habits that don't change? Reprogramming is key, not just trying harder.",
            "result": "→ Reset behaviors for lasting results"
        },
        {
            "title": "Performance Anxiety", 
            "desc": "Struggling in high-pressure situations? Hypnotherapy redesigns your responses with expert guidance.",
            "result": "→ Build confidence through behavioral change"
        },
        {
            "title": "Emotional Dysregulation", 
            "desc": "Struggling with intense emotions or mood swings? Hypnotherapy helps stabilize emotional responses and improve self-awareness.",
            "result": "→ Find balance and emotional stability"
        },
        {
            "title": "Impulse Control", 
            "desc": "Finding it hard to resist impulses or make thoughtful decisions? Reprogramming can help build self-control and long-term focus.",
            "result": "→ Strengthen impulse control"
        },
        {
            "title": "Self-Harm Tendencies", 
            "desc": "Struggling with self-harm or self-destructive behaviors? Hypnotherapy provides tools to redirect these patterns safely.",
            "result": "→ Replace harmful behaviors with healthy coping"
        }
    ]
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for p in problems:
        st.markdown(f"""
        <div class="card card-accent">
            <div class="card-content">
                <h2>{p['title']}</h2>
                <p>{p['desc']}</p>
                <p><strong>{p['result']}</strong></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # New Self Assessment Questionnaire Section
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h2>Self Assessment Questionnaire</h2>
        <p>Take a moment to reflect on your behavioral patterns:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Text input area
    user_input = st.text_area(
        "Describe what you dislike doing or how you respond in certain situations, and how you feel about it:",
        placeholder="For example: 'I get very anxious when I have to speak in meetings...'",
        height=150,
        key="self_assessment"
    )
    
    # AI output placeholder
    st.markdown("""
    <div style="margin-top: 1rem; font-style: italic; color: var(--muted);">
        <p>Section coming soon - This will provide personalized insights based on your input</p>
    </div>
    """, unsafe_allow_html=True)


def show_method():
    st.markdown('<h2>Our Simple 2-Session Process</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    st.markdown("""
    <div class="card card-accent">
        <div class="card-content">
            <h2>Why Reprogramming Works:</h2>
            <ul>
                <li>Changing inputs (like habits) often fails...</li>
                <li>Hypnotherapy rewires the root cause towards your desired behavioral output.</li>
                <li>Designing the new patterns with the expert framework ensures long-term results.</li>
                <li>Includes 2 sessions for 3000 THB; follow-up is optional and rarely needed.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="process-step">
                <div class="step-number">1</div>
                <div>
                    <h2>Session 1: Analysis</h2>
                    <p>Identify patterns holding you back and design a personalized reprogramming plan.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card card-accent">
        <div class="card-content">
            <div class="process-step">
                <div class="step-number">2</div>
                <div>
                    <h2>Session 2: Hypnosis</h2>
                    <p>Reprogram behaviors with certified expertise for immediate, lasting change.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="process-step">
                <div class="step-number">3</div>
                <div>
                    <h2>Session 3: Reinforcement (Optional)</h2>
                    <p>Optional follow-up to reinforce the new pattern, typically not needed but available at your request.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h2>Why Choose This Approach?</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats">
        <div class="stat">
            <div class="stat-number">2</div>
            <div class="stat-label">Sessions for change</div>
        </div>
        <div class="stat">
            <div class="stat-number">92%</div>
            <div class="stat-label">Report improvement</div>
        </div>
        <div class="stat">
            <div class="stat-number">5-7x</div>
            <div class="stat-label">Faster than therapy</div>
        </div>
        <div class="stat">
            <div class="stat-number">Optional</div>
            <div class="stat-label">Follow-up session</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown("""
    <div class="main-container">
        <h2>Real Client Transformations</h2>
    """, unsafe_allow_html=True)
    
    testimonials = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Client in Bangkok"
        },
        {
            "icon": "🎓", 
            "quote": "I was struggling with my studies abroad, failing my second year of medicine. Laetitia helped me change direction, and I'm now doing my specialization internship.",
            "author": "Medical Student, France"
        },
        {
            "icon": "🚭",
            "quote": "My husband was a heavy smoker. After working with Laetitia, he stopped cigarettes completely and only occasionally smokes weed to relax. No more addiction.",
            "author": "Wife of Former Smoker, UK"
        },
        {
            "icon": "🧘",
            "quote": "The anxiety that controlled my daily life is now manageable. I can finally breathe and think clearly in stressful situations.",
            "author": "Anxiety Patient, Germany"
        }
    ]
    
    st.markdown("""
    <style>
        .testimonial-card {
            background: var(--white);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 4px solid var(--accent);
            box-shadow: 0 4px 12px var(--shadow);
        }
        .testimonial-icon {
            font-size: 1.8rem;
            margin-bottom: 0.8rem;
        }
        .testimonial-quote {
            font-style: italic;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .testimonial-author {
            font-weight: 600;
            text-align: right;
            margin-top: 0.5rem;
        }
    </style>
    <div class="card-container">
    """, unsafe_allow_html=True)
    
    for t in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="testimonial-icon">{t['icon']}</div>
            <div class="testimonial-quote">"{t['quote']}"</div>
            <div class="testimonial-author">— {t['author']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Testimonial submission form
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h3>Share Your Story</h3>
        <p style="margin-bottom: 1rem;">Help others by sharing your transformation:</p>
    """, unsafe_allow_html=True)
    
    with st.form("testimonial_form", clear_on_submit=True):
        cols = st.columns([1, 1])
        with cols[0]:
            name = st.text_input("Your Name (optional)", 
                               placeholder="How you want to be credited")
        with cols[1]:
            session_date = st.date_input("Session 2 Date*", 
                                       help="Required for verification")
        
        testimonial = st.text_area("Your Experience*",
                                 placeholder="Describe your transformation...",
                                 height=150,
                                 help="Minimum 50 characters")
        
        submitted = st.form_submit_button("Submit Testimonial")
        
        if submitted:
            if not session_date:
                st.error("Please provide your session date for verification")
            elif not testimonial or len(testimonial.strip()) < 50:
                st.error("Please share at least 50 characters about your experience")
            else:
                # Process submission (would connect to database in production)
                st.success("Thank you! We'll review your testimonial and contact you if needed.")
                st.balloons()
    
    st.markdown("""
        <p style="font-size: 0.9rem; color: var(--muted); margin-top: 1rem;">
            * Required fields. Testimonials are verified before publication.
        </p>
    </div>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    st.markdown('<h2>About Laetitia Sheppard</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
        except:
            st.info("Image not found")
    
    with col2:
        st.markdown("""
        **Expert in Behavioral Change**
        - 13+ years experience in Asian markets
        - Certified Hypnotherapy (LCCH, 2016)
        - Certified in Dialectical Behavioral Therapy for Borderline Personality Disorder (2023)
        - Fluent: English, French, Spanish, Italian
        """)
    
    st.markdown("""
    <div class="contact">
        <h2>Bangkok Hypnotherapy Clinic</h2>
        <p>46/9 Soi Sukhumvit 49 (Thong Lor) • Confidential Sessions</p>
        <div style="display: flex; justify-content: center; align-items: center;">
            <a href="https://www.google.com/maps/place/46%2F9+Soi+Sukhumvit+49,+Thong+Lor,+Bangkok" target="_blank">
                <button class="btn">📍 Get Directions</button>
            </a>
            <a href="https://calendly.com/laetitia-sheppard-hypnotherapy" target="_blank">
                <button class="btn">📅 Book Now</button>
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
<div class="text-center muted-text mt-2" style="border-top: 1px solid var(--medium); padding-top: 2rem; margin-top: 3rem;">
    <p>Laetitia Sheppard • Hypnotherapy for Change • Bangkok, Thailand</p>
    <p>© 2025 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
</div>
""", unsafe_allow_html=True)








