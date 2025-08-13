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
        --shadow-hover: rgba(0,0,0,0.15);
        --shadow-accent: rgba(212, 175, 55, 0.25);
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
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
        margin: 0.6rem 0 0.6rem 0 !important;
        color: var(--primary) !important;
    }}
    p, li, span, div {{
        font-size: 1rem !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        color: var(--primary) !important;
        margin: 0.3rem 0 !important;
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

    /* Responsive grid for cards */
    .card-container {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
    }}
    .card {{
        background: var(--white);
        border: 1px solid var(--medium);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        box-shadow: 0 6px 16px var(--shadow);
        transition: transform 0.4s ease, box-shadow 0.4s ease, background-color 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 220px;
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 28px var(--shadow-hover);
        background-color: #fff9e6;
    }}
    .card h2 {{
        margin-top: 0 !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
        color: var(--primary) !important;
    }}
    .card p {{
        margin: 0.5rem 0 0 0 !important;
        flex-grow: 1;
    }}
    /* Result badge inside card */
    .result-badge {{
        background-color: var(--accent);
        color: var(--primary);
        font-weight: 700;
        padding: 0.25rem 0.8rem;
        margin-top: 1rem;
        border-radius: 8px;
        display: inline-block;
        font-size: 0.9rem;
        align-self: flex-start;
        box-shadow: 0 2px 6px var(--shadow-accent);
        transition: background-color 0.3s ease;
    }}
    .card:hover .result-badge {{
        background-color: #b58f24;
        color: var(--white);
        box-shadow: 0 4px 12px rgba(181, 143, 36, 0.6);
    }}

    /* Button style */
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
        text-align: center;
        user-select: none;
    }}
    .btn:hover {{
        background: #C7A133;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(212, 175, 55, 0.3);
        color: var(--primary);
    }}

    /* Process step styling */
    .process-step {{
        display: flex;
        align-items: flex-start;
        gap: 1rem;
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
        font-size: 1.1rem;
        box-shadow: 0 2px 6px var(--shadow-accent);
    }}

    .card-image-container {{
        margin-top: 1rem;
        border-radius: 8px;
        overflow: hidden;
    }}
    .card-image-container img {{
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s;
    }}
    .card-image-container img:hover {{
        transform: scale(1.02);
    }}

    /* Testimonial card */
    .testimonial-card {{
        background: var(--white);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid var(--accent);
        box-shadow: 0 4px 12px var(--shadow);
    }}
    .testimonial-icon {{
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
    }}
    .testimonial-quote {{
        font-style: italic;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }}
    .testimonial-author {{
        font-weight: 600;
        text-align: right;
        margin-top: 0.5rem;
    }}

    /* Contact Section */
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
    .contact a {{
        margin-right: 1rem;
    }}

    /* Back to top link styling */
    .back-to-top-link {{
        display: block;
        text-align: center;
        margin-top: 2rem;
        color: var(--accent) !important;
        font-weight: 600;
        text-decoration: none;
    }}
    .back-to-top-link:hover {{
        text-decoration: underline;
    }}

    /* Text Center Utility */
    .text-center {{ text-align: center; }}

    /* Responsive adjustments */
    @media (max-width: 768px) {{
        .card-container {{
            grid-template-columns: 1fr !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)
inject_css()

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<div class="hero" id="top">
    <h1 class="hero-title">Reprogram Your Mind, Change Your Life</h1>
    <p class="hero-subtitle">Hypnotherapy doesn't just change what you do—it changes how you do it. In just 2 sessions, it reprograms the patterns holding you back, so you can finally get the results you deserve.</p>
    <a href="https://calendly.com/laetitiasheppard/30min" target="_blank">
        <button class="btn">📅 Book a FREE 15-min Call</button>
    </a>
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
        st.experimental_rerun()
with cols[1]:
    method_btn = st.button("🧠 The Method", key="nav_method",
                          help="Learn about our 2-session method",
                          type="primary" if st.session_state.page == "method" else "secondary")
    if method_btn:
        st.session_state.page = "method"
        st.experimental_rerun()
with cols[2]:
    results_btn = st.button("🏆 Results", key="nav_results",
                           help="See client transformations",
                           type="primary" if st.session_state.page == "results" else "secondary")
    if results_btn:
        st.session_state.page = "results"
        st.experimental_rerun()
with cols[3]:
    about_btn = st.button("👤 About", key="nav_about",
                         help="About Laetitia and the clinic",
                         type="primary" if st.session_state.page == "about" else "secondary")
    if about_btn:
        st.session_state.page = "about"
        st.experimental_rerun()

# --- Back to top link ---
def back_to_top():
    st.markdown("""
    <div class="back-to-top-link">
        <a href="#top">↑ Back to Top</a>
    </div>
    """, unsafe_allow_html=True)


# --- PAGE CONTENT FUNCTIONS ---
def show_problems():
    st.markdown('<h2>Common Challenges We Help You Overcome</h2>', unsafe_allow_html=True)
    
    problems = [
        {
            "title": "Overcoming Drinking Challenges",
            "desc": "Struggling with unhealthy drinking habits? We help reprogram your subconscious patterns for lasting change.",
            "result": "→ Empower yourself to regain control"
        },
        {
            "title": "Breaking Free from Smoking",
            "desc": "Tobacco addiction can be tough to beat alone. Our hypnotherapy creates new habits that support your freedom.",
            "result": "→ Quit smoking with confidence and ease"
        },
        {
            "title": "Preparing Mind and Body for Pregnancy",
            "desc": "Facing challenges with conception? We support your mind-body connection to reduce stress and improve outcomes.",
            "result": "→ Harmonize your mental and physical health"
        },
        {
            "title": "Restoring Healthy Sleep",
            "desc": "Difficulty sleeping affects every area of life. Hypnotherapy helps reset patterns for deep, restful nights.",
            "result": "→ Enjoy restorative sleep naturally"
        },
        {
            "title": "Healing Intimate Relationships",
            "desc": "Relationship strains or intimacy issues? We assist in uncovering and resolving emotional blocks to deepen connection.",
            "result": "→ Foster trust and intimacy with confidence"
        },
        {
            "title": "Adapting to New Surroundings",
            "desc": "Moving or life transitions can be stressful. Reprogram your mindset for resilience and positive adjustment.",
            "result": "→ Thrive comfortably in your new environment"
        },
        {
            "title": "Embracing Life’s Changes",
            "desc": "Change is constant; struggle is optional. Hypnotherapy helps build adaptability and calm in uncertainty.",
            "result": "→ Cultivate flexibility and peace of mind"
        }
    ]
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for p in problems:
        st.markdown(f"""
        <div class="card card-accent">
            <div class="card-content">
                <h2>{p['title']}</h2>
                <p>{p['desc']}</p>
                <span class="result-badge">{p['result']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Self Assessment Questionnaire Section
    st.markdown("""
    <div style="margin-top: 1rem;">
        <h2>Self Assessment Questionnaire</h2>
        <p>Take a moment to reflect on your behavioral patterns:</p>
    </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_area(
        "Describe what you dislike doing or how you respond in certain situations, and how you feel about it:",
        placeholder="For example: 'I get very anxious when I have to speak in meetings...'",
        height=150,
        key="self_assessment"
    )
    
    st.markdown("""
    <div style="margin-top: 1rem; font-style: italic; color: var(--muted);">
        <p>Section coming soon - This will provide personalized insights based on your input.</p>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()


def show_method():
    st.markdown('<h2>Our Simple 2-Session Process</h2>', unsafe_allow_html=True)

    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # Why Reprogramming Works card
    st.markdown("""
    <div class="card card-accent">
        <div class="card-content">
            <h2>Why Reprogramming Works</h2>
            <ul>
                <li>Changing habits alone often fails because the patterns driving behaviors are subconscious.</li>
                <li>Hypnotherapy rewires root causes towards your desired behavioral outcomes.</li>
                <li>Expert-designed framework for sustainable change within just 2 focused sessions.</li>
                <li>All-inclusive price: 3000 THB per 2 sessions; follow-up optional.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Session 1: Analysis
    with st.container():
        st.markdown("""
        <div class="card">
            <div class="card-content">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <div>
                        <h2>Session 1: Analysis</h2>
                        <p>Identify limiting patterns and create a personalized mind reprogramming plan.</p>
                    </div>
                </div>
                <div class="card-image-container">
        """, unsafe_allow_html=True)

        try:
            st.image("img/BehaviourMap.png", caption="Behavior Mapping", use_container_width=True)
        except FileNotFoundError:
            st.error("Image BehaviourMap.png not found in img directory")

        st.markdown("""
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Session 2: Hypnosis
    with st.container():
        st.markdown("""
        <div class="card card-accent">
            <div class="card-content">
                <div class="process-step">
                    <div class="step-number">2</div>
                    <div>
                        <h2>Session 2: Hypnosis</h2>
                        <p>Reprogram behaviors with certified expertise for rapid, lasting change.</p>
                    </div>
                </div>
                <div class="card-image-container">
        """, unsafe_allow_html=True)

        try:
            st.image("img/emo.jpg", caption="Emotional Reprogramming", use_container_width=True)
        except FileNotFoundError:
            st.error("Image emo.jpg not found in img directory")

        st.markdown("""
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Optional Session 3: Reinforcement
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="process-step">
                <div class="step-number">3</div>
                <div>
                    <h2>Session 3: Reinforcement (Optional)</h2>
                    <p>Optional follow-up session to strengthen new patterns, typically not required but available.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close card-container

    st.markdown('<h2>Why Choose This Approach?</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-container">
        <div class="card text-center">
            <h2>2</h2>
            <p><strong>Sessions for Change</strong></p>
        </div>
        <div class="card text-center">
            <h2>92%</h2>
            <p><strong>Client Reported Improvement</strong></p>
        </div>
        <div class="card text-center">
            <h2>5-7x</h2>
            <p><strong>Faster Results Than Traditional Therapy</strong></p>
        </div>
        <div class="card text-center">
            <h2>Optional</h2>
            <p><strong>Follow-up Session</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()


def show_results():
    st.markdown('<h2>Real Client Transformations</h2>', unsafe_allow_html=True)
    
    testimonials = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Director, Banking, Singapore"
        },
        {
            "icon": "🎓", 
            "quote": "I was struggling with my studies abroad, failing my second year of medicine. Laetitia helped me change direction, and I'm now doing my specialization internship.",
            "author": "Medical Student, Morocco"
        },
        {
            "icon": "🚭",
            "quote": "My husband was a heavy smoker. After working with Laetitia, he stopped cigarettes completely and only occasionally smokes weed to relax. No more addiction.",
            "author": "Wife, Bangkok"
        },
        {
            "icon": "🧘",
            "quote": "The anxiety that controlled my daily life is now manageable. I can finally breathe and think clearly in stressful situations.",
            "author": "Anxiety Patient, France"
        }
    ]
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    for t in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="testimonial-icon">{t['icon']}</div>
            <div class="testimonial-quote">"{t['quote']}"</div>
            <div class="testimonial-author">— {t['author']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Testimonial submission form
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h2>Share Your Story</h2>
        <p style="margin-bottom: 1rem;">Help others by sharing your transformation:</p>
    """, unsafe_allow_html=True)
    
    with st.form("testimonial_form", clear_on_submit=True):
        cols = st.columns([1, 1])
        with cols[0]:
            name = st.text_input("Your Name (optional)", placeholder="How you want to be credited")
        with cols[1]:
            session_date = st.date_input("Session 2 Date*", help="Required for verification")
        
        testimonial = st.text_area("Your Experience*", placeholder="Describe your transformation...", height=150, help="Minimum 50 characters")
        
        submitted = st.form_submit_button("Submit Testimonial")
        
        if submitted:
            if not session_date:
                st.error("Please provide your session date for verification.")
            elif not testimonial or len(testimonial.strip()) < 50:
                st.error("Please share at least 50 characters about your experience.")
            else:
                # Placeholder for actual submission logic
                st.success("Thank you! We'll review your testimonial and contact you if needed.")
                st.balloons()

    st.markdown("""
        <p style="font-size: 0.9rem; color: var(--muted); margin-top: 1rem;">
            * Required fields. Testimonials are verified before publication.
        </p>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()


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
        - 10+ years of experience in change management  
        - Certified in Hypnotherapy & Cognitive Behaviour (LCCH, 2016)  
        - Certified in Dialectical Behavioral Therapy for Borderline Personality Disorder (2023)  
        - Fluent: English, French, can deliver in Italian if needed  
        """)
    
    st.markdown("""
    <div class="contact">
        <h2>Bangkok Hypnotherapy Clinic</h2>
        <p>27 Soi Sukhumvit 10 (Asoke) • Confidential Sessions</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <a href="https://www.google.com/maps/place/27+Soi+Sukhumvit+10,+Asoke,+Bangkok" target="_blank">
                <button class="btn">📍 Get Directions</button>
            </a>
            <a href="https://calendly.com/laetitiasheppard/new-meeting" target="_blank">
                <button class="btn">📅 Book Now</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    back_to_top()


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
