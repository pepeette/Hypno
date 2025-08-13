import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
import base64
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Break Free in 2 Sessions | Laetitia Sheppard Hypnotherapy",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMAGE OPTIMIZATION ---
@st.cache_data(show_spinner=False)
def load_optimized_image(image_path, caption=None, width=None):
    try:
        img = Image.open(image_path)
        buffer = io.BytesIO()
        img.save(buffer, format="WEBP", quality=85)
        img_str = base64.b64encode(buffer.getvalue()).decode()
        html = f"""
        <img src="data:image/webp;base64,{img_str}" 
             {f'width="{width}"' if width else ''}
             alt="{caption if caption else 'therapy image'}"
             loading="lazy"
             style="border-radius:8px; max-width:100%; height:auto;">
        {f'<p style="text-align:center; margin-top:0.5rem;">{caption}</p>' if caption else ''}
        """
        st.markdown(html, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Image not loaded: {str(e)}")

# --- CSS INJECTION ---
def inject_css():
    st.markdown(f"""
    <style>
    :root {{
        --primary: #1C1C1E;
        --accent: #D4AF37;
        --light: #F4F4F6;
    }}
    
    /* Force light mode */
    [data-testid="stAppViewContainer"] {{
        background-color: var(--light) !important;
        color-scheme: light !important;
    }}
    
    /* Hero Section */
    .hero {{
        background: linear-gradient(135deg, #1C1C1E 0%, #2E2E32 100%);
        color: white;
        padding: 3rem 1rem;
        text-align: center;
        border-radius: 12px;
        margin: 0 0 2rem 0;
        border-left: 6px solid var(--accent);
    }}
    .hero-title {{
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        margin: 0 0 1rem 0 !important;
        line-height: 1.2;
    }}
    .hero-subtitle {{
        font-size: 1.3rem !important;
        max-width: 700px;
        margin: 0 auto 2rem !important;
        line-height: 1.5;
        font-weight: 400;
    }}
    
    /* CTA Buttons */
    .cta {{
        background: var(--accent);
        color: var(--primary) !important;
        padding: 1rem 2.5rem;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 0.5rem;
        text-decoration: none !important;
    }}
    .cta:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }}
    
    /* Interactive Elements */
    .discovery-form {{
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 2rem auto;
        max-width: 600px;
    }}
    
    /* Mobile Responsiveness */
    @media (max-width: 768px) {{
        .hero-title {{ font-size: 1.8rem !important; }}
        .hero-subtitle {{ font-size: 1.1rem !important; }}
    }}
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "The Method", "Success Stories", "Free Consultation"],
    icons=["house-heart", "magic", "stars", "calendar-check"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "margin": "0.5rem auto 1.5rem"},
        "nav-link-selected": {
            "background": "var(--accent)",
            "color": "var(--primary)",
            "font-weight": "bold",
        },
    }
)

# --- HERO SECTION ---
st.markdown("""
<div class="hero" id="top">
    <h1 class="hero-title">Stuck in patterns that hold you back?</h1>
    <p class="hero-subtitle">Our 2-session hypnotherapy approach helps you break free from smoking, anxiety, and unwanted habits - with lasting results you can feel immediately</p>
    <a href="#discovery" class="cta">Book Your Free Discovery Call</a>
    <p style="margin: 1.5rem 0 0 0; color: rgba(255,255,255,0.8);">
        <span style="color: var(--accent); font-weight: bold;">✓</span> No willpower required &nbsp;&nbsp;
        <span style="color: var(--accent); font-weight: bold;">✓</span> 92% success rate &nbsp;&nbsp;
        <span style="color: var(--accent); font-weight: bold;">✓</span> English/French/Italian
    </p>
</div>
""", unsafe_allow_html=True)

# --- PAGE CONTENT ---
if selected == "Home":
    # Pain Points Section
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <h2>What's keeping you stuck?</h2>
        <p style="max-width: 700px; margin: 0 auto;">We help with these common challenges (and many more)</p>
    </div>
    """, unsafe_allow_html=True)
    
    pain_points = [
        {"icon": "🚬", "title": "Quit Smoking", "desc": "Break nicotine addiction without withdrawal"},
        {"icon": "😰", "title": "Reduce Anxiety", "desc": "Calm your nervous system naturally"},
        {"icon": "🛌", "title": "Sleep Better", "desc": "Fall asleep faster and stay asleep"},
        {"icon": "🍽️", "title": "Healthy Eating", "desc": "Transform your relationship with food"},
        {"icon": "💑", "title": "Relationship Blocks", "desc": "Overcome intimacy and trust issues"},
        {"icon": "🔄", "title": "Life Transitions", "desc": "Adapt to change with confidence"}
    ]
    
    cols = st.columns(3)
    for i, point in enumerate(pain_points):
        with cols[i%3]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem; margin-bottom: 1rem; background: white; border-radius: 12px;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{point['icon']}</div>
                <h3 style="margin: 0.5rem 0;">{point['title']}</h3>
                <p style="margin: 0.5rem 0 1rem 0;">{point['desc']}</p>
                <a href="#discovery" class="cta" style="padding: 0.7rem 1.5rem; font-size: 0.9rem;">Learn How</a>
            </div>
            """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("""
    <div style="text-align: center; margin: 4rem 0 2rem 0;">
        <h2>How our 2-step method works</h2>
    </div>
    """, unsafe_allow_html=True)
    
    steps = [
        {"num": "1", "title": "Discover the Root Cause", "desc": "We identify the subconscious patterns driving your behavior"},
        {"num": "2", "title": "Reprogram Your Mind", "desc": "Guided hypnosis creates new neural pathways"},
        {"num": "+1", "title": "Optional Tune-Up", "desc": "One follow-up session if needed (rarely required)"}
    ]
    
    cols = st.columns(3)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem; background: white; border-radius: 12px; height: 100%;">
                <div style="background: var(--accent); color: var(--primary); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">{step['num']}</div>
                <h3 style="margin: 0 0 1rem 0;">{step['title']}</h3>
                <p style="margin: 0;">{step['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <a href="#discovery" class="cta">See If This Is Right For You</a>
    </div>
    """, unsafe_allow_html=True)

elif selected == "The Method":
    # Educational Content
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Why 2 Sessions Work Better Than Months of Therapy</h2>
        <p style="max-width: 700px; margin: 0 auto;">Traditional therapy talks about problems. We target the subconscious mind where change actually happens.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Method Explanation
    with st.expander("🧠 How Hypnotherapy Rewires Your Brain", expanded=True):
        st.markdown("""
        - **Direct Access**: Hypnosis allows us to bypass your critical conscious mind
        - **Pattern Interrupt**: We identify and reprogram automatic behaviors
        - **Neuroplasticity**: Your brain creates new pathways in just 1-2 sessions
        """)
        
        if st.button("Watch 2-min Explanation Video", key="video_btn"):
            st.video("https://youtu.be/example-hypnosis-explainer")
    
    with st.expander("📅 What to Expect in Your Sessions"):
        st.markdown("""
        **First Session (90 mins):**
        - Comprehensive analysis of your specific patterns
        - Custom therapy plan development
        - Light hypnosis introduction
        
        **Second Session (90 mins):**
        - Deep hypnotic reprogramming
        - Anchoring new behaviors
        - Future pacing for lasting results
        """)
    
    # Interactive Self-Assessment
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 12px; margin: 2rem 0;">
        <h3 style="margin-top: 0;">Quick Self-Assessment</h3>
        <p>How would you rate these areas of your life?</p>
    """, unsafe_allow_html=True)
    
    sliders = {
        "Stress Levels": st.slider("Stress Levels", 1, 10, 5),
        "Sleep Quality": st.slider("Sleep Quality", 1, 10, 5),
        "Impulse Control": st.slider("Impulse Control", 1, 10, 5)
    }
    
    if st.button("Get Personalized Recommendations", key="assessment_btn"):
        total = sum(sliders.values())
        if total <= 12:
            st.success("Our 2-session approach could make a dramatic difference for you. Let's discuss how we can help.")
        else:
            st.info("You're doing well, but most clients see improvement even from strong baselines. Worth exploring?")
        
        st.markdown('<a href="#discovery" class="cta">Discuss Your Results</a>', unsafe_allow_html=True)

elif selected == "Success Stories":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Real People, Lasting Changes</h2>
        <p>What our clients say about their 2-session transformations</p>
    </div>
    """, unsafe_allow_html=True)
    
    testimonials = [
        {
            "name": "James R.",
            "result": "Quit smoking after 18 years",
            "quote": "I'd tried everything before - patches, gum, willpower. After 2 sessions, I simply forgot to smoke one day... and never looked back.",
            "before_after": "From 20/day to 0"
        },
        {
            "name": "Sophie L.",
            "result": "Overcame public speaking anxiety",
            "quote": "Went from panic attacks to delivering confident presentations. My career trajectory completely changed.",
            "before_after": "From dread to confidence"
        }
    ]
    
    for t in testimonials:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 12px; margin-bottom: 1.5rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <h3 style="margin: 0;">{t['name']}</h3>
                <div style="color: var(--accent); font-weight: bold;">{t['before_after']}</div>
            </div>
            <p style="font-style: italic; font-size: 1.1rem;">"{t['quote']}"</p>
            <div style="color: var(--accent); font-weight: bold; text-align: right;">{t['result']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <h3>Could this work for you?</h3>
        <a href="#discovery" class="cta">Let's Find Out Together</a>
    </div>
    """, unsafe_allow_html=True)

# --- DISCOVERY FORM (All Pages) ---
st.markdown("""
<div id="discovery" class="discovery-form">
    <h2 style="text-align: center; margin-top: 0;">Free 15-Minute Discovery Call</h2>
    <p style="text-align: center;">Let's discuss your specific situation and how we can help</p>
""", unsafe_allow_html=True)

with st.form("discovery_form"):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("Your Name*", placeholder="First and last name")
    with cols[1]:
        email = st.text_input("Email*", placeholder="Your email address")
    
    concern = st.selectbox(
        "Primary Concern*",
        ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"]
    )
    
    st.markdown("""
    <div style="font-size: 0.9rem; margin: 0.5rem 0 1.5rem 0;">
        <p>* Required fields</p>
    </div>
    """, unsafe_allow_html=True)
    
    submitted = st.form_submit_button("Schedule Your Free Call")
    if submitted:
        if not name or not email or concern == "Select one...":
            st.error("Please fill in all required fields")
        else:
            st.success("Thank you! We'll contact you within 24 hours to schedule your call.")
            # Here you would add your form submission logic

st.markdown("""
</div>  <!-- Close discovery-form -->
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; margin: 3rem 0 1rem 0; padding-top: 2rem; border-top: 1px solid #E2E2E6;">
    <p style="color: #6E6E73;">Laetitia Sheppard • Clinical Hypnotherapy</p>
    <p style="color: #6E6E73; font-size: 0.9rem;">
        27 Soi Sukhumvit 10, Bangkok • 
        <a href="tel:+66123456789" style="color: var(--accent); text-decoration: none;">+66 123 456 789</a>
    </p>
    <p style="color: #6E6E73; font-size: 0.8rem; margin-top: 1rem;">
        © {datetime.datetime.now().year} All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)