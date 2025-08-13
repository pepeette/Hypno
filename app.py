import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
import base64
import datetime
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2-Step Hypnotherapy Solutions | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMAGE HANDLER WITH ALT TEXT ---
@st.cache_data(show_spinner=False)
def load_optimized_image(image_path, alt_text, caption=None, width=None):
    """Optimized image loader with accessibility features"""
    try:
        img = Image.open(image_path)
        buffer = io.BytesIO()
        img.save(buffer, format="WEBP", quality=85, optimize=True)
        img_str = base64.b64encode(buffer.getvalue()).decode()
        html = f"""
        <figure style="margin:0; text-align:center;">
            <img src="data:image/webp;base64,{img_str}" 
                 {f'width="{width}"' if width else ''}
                 alt="{alt_text}"
                 loading="lazy"
                 style="border-radius:8px; max-width:100%; height:auto;">
            {f'<figcaption style="font-size:0.9rem; margin-top:0.5rem;">{caption}</figcaption>' if caption else ''}
        </figure>
        """
        st.markdown(html, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Image not loaded: {str(e)}")

# --- CSS WITH ACCESSIBILITY ENHANCEMENTS ---
def inject_css():
    st.markdown("""
    <style>
    /* Force light mode */
    [data-testid="stAppViewContainer"] {
        background-color: white !important;
        color-scheme: light !important;
    }
    body {
        color-scheme: light !important;
    }
    /* Dark mode overrides */
    .stApp [data-testid="stAppViewContainer"] {
        background-color: white !important;
    }
    /* Text/input elements */
    .stTextInput, .stTextArea, .stSelectbox, .stSlider {
        background-color: white !important;
        color: #1C1C1E !important;
    }

    :root {{
        --primary: #1C1C1E;  /* AA contrast with light background */
        --accent: #D4AF37;   /* AA contrast with dark text */
        --light: #F4F4F6;    /* AAA contrast with dark text */
    }}
    
    /* Force light mode with accessible contrast */
    [data-testid="stAppViewContainer"] {{
        background-color: var(--light) !important;
        color-scheme: light !important;
    }}
    
    /* Loading spinner */
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    .spinner {{
        animation: spin 1s linear infinite;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(0,0,0,0.1);
        border-radius: 50%;
        border-top-color: var(--accent);
        display: inline-block;
        vertical-align: middle;
        margin-left: 8px;
    }}
    
    /* Interactive quiz styles */
    .quiz-question {{
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}
    .quiz-option {{
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border: 1px solid #E2E2E6;
        cursor: pointer;
        transition: all 0.2s;
    }}
    .quiz-option:hover {{
        background: #f9f9f9;
    }}
    .quiz-option.selected {{
        background: var(--accent);
        color: var(--primary);
        border-color: var(--accent);
    }}
    

    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Method", "Success", "Blog", "Free Session"],
    icons=["house", "magic", "stars", "book", "calendar"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link-selected": {
            "background": "#D4AF37",
            "color": "#1C1C1E",
            "font-weight": "bold",
        },
    }
)

# --- HERO SECTION ---
st.markdown("""
<div class="hero" id="top">
    <h1 class="hero-title">Tired of willpower not working?</h1>
    <p class="hero-subtitle">Our 2-session hypnotherapy approach helps you quit smoking, reduce anxiety, and break unwanted habits - <strong>without relying on willpower</strong></p>
    <a href="#quiz" class="cta">Take Our 30-Second Quiz</a>
    <p style="margin: 1.5rem 0 0 0; color: rgba(255,255,255,0.9);">
        <span style="color: #D4AF37; font-weight: bold;">✓</span> 92% success rate &nbsp;&nbsp;
        <span style="color: #D4AF37; font-weight: bold;">✓</span> No withdrawal symptoms &nbsp;&nbsp;
        <span style="color: #D4AF37; font-weight: bold;">✓</span> English/French/Italian
    </p>
</div>
""", unsafe_allow_html=True)

# --- INTERACTIVE QUIZ ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align: center; margin: 3rem 0;">
        <h2>30-Second Suitability Quiz</h2>
        <p>Answer 3 quick questions to see if our method is right for you</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz_questions = [
        {
            "question": "How long have you been struggling with this issue?",
            "options": [
                "Less than 6 months",
                "6 months to 2 years", 
                "More than 2 years"
            ]
        },
        {
            "question": "What have you tried before?",
            "options": [
                "Nothing yet",
                "Self-help methods",
                "Other therapies"
            ]
        },
        {
            "question": "How ready are you to make a change?",
            "options": [
                "Just exploring",
                "Somewhat ready",
                "Very ready"
            ]
        }
    ]
    
    quiz_answers = []
    
    for i, q in enumerate(quiz_questions):
        st.markdown(f"""
        <div class="quiz-question">
            <h3>Question {i+1}: {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(3)
        for j, option in enumerate(q['options']):
            with cols[j]:
                if st.button(option, key=f"q{i}o{j}"):
                    quiz_answers.append(option)
                    st.session_state[f'quiz_q{i}'] = j
    
    if len(quiz_answers) == len(quiz_questions):
        st.success("Thank you! Based on your answers, our 2-session method would likely work well for you.")
        st.markdown("""
        <div style="text-align: center; margin: 1.5rem 0;">
            <a href="#discovery" class="cta">Book Free Consultation</a>
        </div>
        """, unsafe_allow_html=True)

# --- METHOD PAGE WITH INTERACTIVE ELEMENTS ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Experience Our 2-Step Method</h2>
        <p>See how hypnotherapy creates faster change than traditional therapy</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Process Timeline
    st.markdown("""
    <div style="display: flex; justify-content: center; margin: 2rem 0;">
        <div style="text-align: center; margin: 0 1.5rem;">
            <div style="background: #D4AF37; color: #1C1C1E; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 1rem;">1</div>
            <h3 style="margin: 0 0 0.5rem 0;">Analysis</h3>
            <p style="margin: 0;">Identify root causes</p>
        </div>
        <div style="text-align: center; margin: 0 1.5rem;">
            <div style="background: #D4AF37; color: #1C1C1E; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 1rem;">2</div>
            <h3 style="margin: 0 0 0.5rem 0;">Transformation</h3>
            <p style="margin: 0;">Reprogram patterns</p>
        </div>
        <div style="text-align: center; margin: 0 1.5rem;">
            <div style="background: #f4f4f6; color: #1C1C1E; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 1rem;">+1</div>
            <h3 style="margin: 0 0 0.5rem 0;">Tune-Up</h3>
            <p style="margin: 0;">Optional reinforcement</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Video Explanation
    with st.expander("▶️ Watch 90-Second Explanation", expanded=False):
        st.video("https://youtu.be/example-hypnosis-explainer")
    
    # Interactive Progress Tracker
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 12px; margin: 2rem 0;">
        <h3 style="margin-top: 0;">Your Change Readiness Score</h3>
        <p>Rate these factors to see how quickly you might benefit:</p>
    """, unsafe_allow_html=True)
    
    motivation = st.slider("Motivation Level (1-10)", 1, 10, 7)
    openness = st.slider("Openness to Hypnosis (1-10)", 1, 10, 5)
    
    if st.button("Calculate My Score", key="score_btn"):
        score = motivation + openness
        progress = min(100, score * 5)
        
        st.markdown(f"""
        <div style="margin: 1.5rem 0;">
            <div style="background: #f4f4f6; height: 20px; border-radius: 10px; overflow: hidden;">
                <div style="background: #D4AF37; width: {progress}%; height: 100%;"></div>
            </div>
            <p style="text-align: center; margin: 0.5rem 0;">
                Your readiness: {score}/20 &nbsp;&nbsp; 
                <span style="color: {'#D4AF37' if score > 10 else '#6E6E73'}">
                    {'Great candidate!' if score > 10 else 'Potential candidate'}
                </span>
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- BLOG/FAQ SECTION ---
elif selected == "Blog":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Hypnotherapy Insights</h2>
        <p>Learn how hypnotherapy works and what to expect</p>
    </div>
    """, unsafe_allow_html=True)
    
    faq_items = [
        {
            "question": "Is hypnotherapy safe?",
            "answer": "Yes, clinical hypnotherapy is a safe, non-invasive approach. You remain fully aware and in control at all times."
        },
        {
            "question": "How many sessions will I need?",
            "answer": "Most clients achieve their goals in just 2 sessions. About 15% opt for an optional third session."
        },
        {
            "question": "Can I be hypnotized if I'm skeptical?",
            "answer": "Yes! Hypnosis is a natural state we all experience daily (like when you're absorbed in a book). Skepticism doesn't prevent it from working."
        }
    ]
    
    for item in faq_items:
        with st.expander(f"❓ {item['question']}", expanded=False):
            st.write(item['answer'])
    
    st.markdown("""
    <div style="margin: 3rem 0; text-align: center;">
        <h3>Want to learn more?</h3>
        <p>Subscribe to get our free guide: "How Hypnosis Rewires Your Brain"</p>
        <form>
            <input type="email" placeholder="Your email address" style="padding: 0.8rem; border-radius: 8px; border: 1px solid #E2E2E6; width: 300px; max-width: 100%; margin-right: 0.5rem;">
            <button type="submit" style="background: #D4AF37; color: #1C1C1E; padding: 0.8rem 1.5rem; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Get Free Guide</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# --- ENHANCED DISCOVERY FORM ---
st.markdown("""
<div id="discovery" style="background: white; padding: 2rem; border-radius: 12px; margin: 3rem 0 1rem 0;">
    <h2 style="text-align: center; margin-top: 0;">Free 15-Minute Discovery Call</h2>
    <p style="text-align: center; color: #6E6E73;">Let's discuss your goals and how we can help</p>
""", unsafe_allow_html=True)

with st.form("discovery_form"):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("Your Name*", placeholder="First and last name", 
                           help="We use this to personalize your session")
    with cols[1]:
        email = st.text_input("Email*", placeholder="Your email address",
                            help="We'll send confirmation details here")
    
    concern = st.selectbox(
        "Primary Concern*",
        ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
        help="This helps us prepare for our conversation"
    )
    
    if concern == "Other":
        other_concern = st.text_input("Please specify")
    
    message = st.text_area("Anything specific you'd like us to know", 
                         placeholder="E.g., 'I've tried quitting smoking 3 times before'",
                         help="Optional but helpful for personalization")
    
    submitted = st.form_submit_button("Schedule My Free Call")
    if submitted:
        if not name or not email or concern == "Select one...":
            st.error("Please fill in all required fields")
        else:
            with st.spinner("Scheduling your session..."):
                time.sleep(2)  # Simulate processing
                st.success("✅ Thank you! We'll contact you within 24 hours to confirm your appointment.")
                st.balloons()

st.markdown("""
</div>  <!-- Close discovery form -->
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; margin: 3rem 0 1rem 0; padding-top: 2rem; border-top: 1px solid #E2E2E6;">
    <p style="color: #6E6E73;">Laetitia Sheppard • Clinical Hypnotherapy</p>
    <p style="color: #6E6E73; font-size: 0.9rem;">
        27 Soi Sukhumvit 10, Bangkok • 
        <a href="tel:+66123456789" style="color: #D4AF37; text-decoration: none;">+66 123 456 789</a>
    </p>
    <p style="color: #6E6E73; font-size: 0.8rem; margin-top: 1rem;">
        © {datetime.datetime.now().year} All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)