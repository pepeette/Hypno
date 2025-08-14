import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import re

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2-Step Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONSTANTS ---
SMTP_CONFIG = {
    "server": os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.environ.get("SMTP_PORT", 587)),
    "from_email": os.environ.get("EMAIL_FROM", "website@laetitiasheppard.com"),
    "to_email": os.environ.get("EMAIL_TO", "laetitiasheppard@gmail.com"),
    "username": os.environ.get("SMTP_USERNAME"),
    "password": os.environ.get("SMTP_PASSWORD")
}

# --- UTILITY FUNCTIONS ---
def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

def send_email(name, email, concern, message):
    if not all([name, email, concern != "Select one..."]):
        st.error("Missing required fields")
        return False

    try:
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nConcern: {concern}\nMessage: {message}")
        msg['Subject'] = 'New Consultation Request'
        msg['From'] = SMTP_CONFIG["from_email"]
        msg['To'] = SMTP_CONFIG["to_email"]

        with smtplib.SMTP(SMTP_CONFIG["server"], SMTP_CONFIG["port"]) as server:
            server.starttls()
            server.login(SMTP_CONFIG["username"], SMTP_CONFIG["password"])
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email failed: {str(e)}")
        return False

def reset_quiz():
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

# --- SESSION MANAGEMENT ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

def handle_quiz_answer(question_id, answer):
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1

# --- STYLING ---
st.markdown("""
<style>
/* Force light mode */
:root {
    color-scheme: light;
}
html, body, .stApp {
    color-scheme: light !important;
}
.stApp {
    background-color: var(--bg) !important;
    color: var(--text-primary) !important;
}

/* ================ */
/* Color Variables */
/* ================ */
:root {
    --bg: #F3F6F8;             /* Light cool grayish blue */
    --card-bg: #FFFFFF;        /* Bright white */
    --text-primary: #273548;   /* Dark blue-gray */
    --text-secondary: #556D7A; /* Mid-tone slate blue */
    --accent: #4CA1A3;         /* Teal blue */
    --accent-hover: #3B7A7A;   /* Deeper teal */
    --border: #CBD5E1;         /* Muted slate gray */
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
    --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --transition: all 0.3s ease;
}

/* ================ */
/* Base Styles */
/* ================ */
body {
    background-color: var(--bg);
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ================ */
/* Typography */
/* ================ */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary);
}

p, li {
    color: var(--text-secondary);
}

/* ================ */
/* Components */
/* ================ */
/* Cards */
.card {
    background: var(--card-bg);
    border-radius: var(--radius-md);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border);
    transition: var(--transition);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
}

.testimonial-card {
    border-left: 4px solid var(--accent);
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
    padding: 3rem 2rem;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-sm);
}

/* Progress Steps */
.step {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--border);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 0 0.5rem;
    font-weight: 600;
    color: var(--text-secondary);
}

.step.active {
    background: var(--accent);
    color: white;
}

/* ================ */
/* Buttons */
/* ================ */
/* Base Button Styles */
.stButton>button {
    border-radius: var(--radius-sm) !important;
    transition: var(--transition) !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    cursor: pointer !important;
}

/* Primary Buttons */
.stButton>button.primary,
.stButton>button[type="primary"],
.st-emotion-cache-1avcm0n.e1f1d6gn3 {
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
}

.stButton>button.primary:hover,
.stButton>button[type="primary"]:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

/* Secondary Buttons */
.stButton>button:not(.primary):not([type="primary"]) {
    background-color: white !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
}

.stButton>button:not(.primary):not([type="primary"]):hover {
    border-color: var(--accent) !important;
    color: var(--accent-hover) !important;
}

/* CTA Buttons */
.cta-button {
    display: inline-block !important;
    padding: 0.8rem 2rem !important;
    border-radius: var(--radius-sm) !important;
    text-decoration: none !important;
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
    transition: var(--transition) !important;
}

.cta-button:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-2px);
    box-shadow: var(--shadow-accent);
}

/* Unified primary button styles */
.stButton>button.primary,
.stButton>button[type="primary"],
.st-emotion-cache-1avcm0n.e1f1d6gn3,
button[data-testid="baseButton-primary"] {
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    border-radius: var(--radius-sm) !important;
}

.stButton>button.primary:hover,
.stButton>button[type="primary"]:hover,
.st-emotion-cache-1avcm0n.e1f1d6gn3:hover,
button[data-testid="baseButton-primary"]:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

/* ================ */
/* Form Elements */
/* ================ */
.stTextInput>div>div>input, 
.stSelectbox>div>div>select,
.stTextArea>div>textarea {
    background-color: white;
    border: 1px solid var(--border) !important;
    color: var(--text-primary);
    border-radius: var(--radius-sm);
    padding: 8px 12px;
}

.stTextInput>div>div>input:focus, 
.stSelectbox>div>div>select:focus,
.stTextArea>div>textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.2) !important;
}

.st-bq { /* Help text */
    color: var(--text-secondary) !important;
    font-size: 0.85rem !important;
}

/* ================ */
/* Navigation */
/* ================ */
.st-bh { /* Nav container */
    background-color: var(--bg) !important;
}

.st-c0 { /* Nav links */
    color: var(--text-primary) !important;
    transition: var(--transition) !important;
}

.st-c0:hover {
    color: var(--accent-hover) !important;
}

.st-dn { /* Selected nav item */
    background-color: var(--accent) !important;
    color: white !important;
    font-weight: 600 !important;
}

/* ================ */
/* Utility Classes */
/* ================ */
.wave-divider {
    height: 15px;
    width: 100%;
    background: linear-gradient(90deg, var(--accent) 0%, var(--bg) 100%);
    opacity: 0.3;
    margin: 2rem 0;
}

.text-center {
    text-align: center;
}

.mb-2 {
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Method", "Success", "Blog", "Book Now"],
    icons=["house", "magic", "stars", "book", "calendar"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "background-color": "#F3F6F8",  # Light cool grayish blue background
            "padding": "0",
            "margin": "0"
        },
        "nav-link": {
            "font-size": "16px",
            "font-weight": "400",
            "color": "#273548",  # Dark blue-gray text
            "padding": "8px 16px",
            "transition": "all 0.3s ease",
        },
        "nav-link:hover": {
            "color": "#3B7A7A",  # Deeper teal on hover
            "background-color": "rgba(76, 161, 163, 0.1)"  # Light teal tint
        },
        "nav-link-selected": {
            "background": "#4CA1A3",  # Teal blue background
            "color": "white",  # White text for better contrast
            "font-weight": "600",
            "border-bottom": "3px solid #3B7A7A"  # Deeper teal accent
        },
        "icon": {
            "color": "#4CA1A3",  # Teal icons
            "font-size": "18px"
        },
        "icon-selected": {
            "color": "white"  # White icons for selected state
        }
    }
)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <h2 style="color: var(--text-primary); margin-bottom: 1rem;">Break Free in Just 2 Sessions</h2>
    <p style="font-size:1.2rem; color:var(--text-primary); max-width:700px; margin:0 auto 2rem;">
        Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
    </p>
    <button onclick="document.getElementById('quiz').scrollIntoView()" class="stButton cta-button">
        Take the 30-Second Quiz
    </button>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align:center; margin:2rem 0;">
        <h2 style="color: var(--text-primary);">30-second suitability Quiz</h2>
        <p style="color: var(--text-secondary);">Answer 3 questions to see if the method is right for you</p>
    </div>
    """, unsafe_allow_html=True)

    # Progress indicator
    st.markdown("""
    <div style="display:flex; justify-content:center; gap:1rem; margin:2rem 0;">
        <div class="step {}">1</div>
        <div class="step {}">2</div>
        <div class="step {}">3</div>
    </div>
    """.format(
        "active" if st.session_state.quiz_step == 1 else "",
        "active" if st.session_state.quiz_step == 2 else "",
        "active" if st.session_state.quiz_step == 3 else ""
    ), unsafe_allow_html=True)

    # Question 1
    if st.session_state.quiz_step == 1:
        st.markdown("### Q1: What are you looking to change?")
        options = ["Quit smoking", "Reduce anxiety", "Improve sleep", "Other"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q1o{i}", type="primary" if i == 0 else "secondary"):
                    handle_quiz_answer(1, option)

    # Question 2
    elif st.session_state.quiz_step == 2:
        st.markdown("### Q2: How long have you struggled with this?")
        options = ["Less than 6 months", "6 months to 2 years", "More than 2 years"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q2o{i}", type="primary" if i == 0 else "secondary"):
                    handle_quiz_answer(2, option)

    # Question 3
    elif st.session_state.quiz_step == 3:
        st.markdown("### Q3: How ready are you to make a change?")
        options = ["Just exploring options", "Somewhat ready", "Very ready - I'm committed"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q3o{i}", type="primary" if i == 0 else "secondary"):
                    handle_quiz_answer(3, option)

    # Quiz Results
    if len(st.session_state.quiz_answers) == 3:
        st.markdown("""
        <div class="card" style="text-align:center; padding:2rem; margin:2rem auto; max-width:800px;">
            <h3 style="color: var(--text-primary);">Based on your answers, our 2-session method would likely work well for you!</h3>
        </div>
        """, unsafe_allow_html=True)

        # Show summary of answers
        with st.expander("See your answers", expanded=False):
            st.write(f"1. Goal: {st.session_state.quiz_answers.get(1, 'Not answered')}")
            st.write(f"2. Duration: {st.session_state.quiz_answers.get(2, 'Not answered')}")
            st.write(f"3. Readiness: {st.session_state.quiz_answers.get(3, 'Not answered')}")

        # Action buttons
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("""
            <div style="text-align:center; margin:1.5rem 0;">
                <a href="#discovery" class="stButton cta-button" style="display:inline-block; text-decoration:none;">Book Consultation</a>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("Retake Quiz", key="retake_quiz"):
                reset_quiz()

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2 style="color: var(--text-primary);">Proven 2-Step Method</h2>
        <p style="color: var(--text-secondary);">Why most clients achieve lasting change in just two sessions</p>
    </div>
    """, unsafe_allow_html=True)

    # Video Embed
    st.markdown("""
    <div class="card" style="margin:2rem auto; max-width:800px; padding:1rem; text-align:center;">
        <div style="background:var(--border); height:315px; display:flex; align-items:center; justify-content:center; border-radius:8px;">
            <p style="color:var(--text-secondary);">[Hypnotherapy Method Video]</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Method Steps
    steps = st.columns(3)
    with steps[0]:
        st.markdown("""
        <div class="card">
            <div style="background:var(--accent); color:var(--text-primary); width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">1</div>
            <h3 style="color: var(--text-primary); text-align:center;">Analysis Session</h3>
            <ul style="text-align:left; color:var(--text-secondary);">
                <li>Comprehensive evaluation</li>
                <li>Identify subconscious drivers</li>
                <li>Develop personalized plan</li>
                <li>Around 90 minutes in-person/Zoom</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with steps[1]:
        st.markdown("""
        <div class="card">
            <div style="background:var(--accent); color:var(--text-primary); width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">2</div>
            <h3 style="color: var(--text-primary); text-align:center;">Transformation</h3>
            <ul style="text-align:left; color:var(--text-secondary);">
                <li>Guided hypnosis</li>
                <li>Create new neural pathways</li>
                <li>Anchor positive behaviors</li>
                <li>Around 90 minutes (3-7 days later)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with steps[2]:
        st.markdown("""
        <div class="card">
            <div style="background:var(--border); color:var(--text-primary); width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">+1</div>
            <h3 style="color: var(--text-primary); text-align:center;">Reinforcement</h3>
            <ul style="text-align:left; color:var(--text-secondary);">
                <li>Strengthen new patterns</li>
                <li>Address remaining blocks</li>
                <li>Typically not needed</li>
                <li>Around 60 minutes (optional)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Pricing
    st.markdown("""
    <div class="card" style="margin:2rem auto; max-width:800px;">
        <h3 style="color: var(--text-primary); margin-top:0;">Pricing Options</h3>
        <p style="color:var(--text-secondary);"><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p style="color:var(--text-secondary);"><strong>Premium Package:</strong> 4000 THB (Includes optional reinforcement)</p>
        <p style="font-size:0.9rem; color:var(--text-secondary);">Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES PAGE ---
elif selected == "Success":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2 style="color: var(--text-primary);">Client Transformations</h2>
        <p style="color: var(--text-secondary);">Real people who changed their lives in 2 sessions</p>
    </div>
    """, unsafe_allow_html=True)

    # Testimonials
    testimonials = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Director, Banking, Singapore"
        },
        {
            "icon": "🎓", 
            "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
            "author": "Medical Student, Morocco"
        },
        {
            "icon": "🚭",
            "quote": "My husband was a heavy smoker... No more addiction.",
            "author": "Wife, Bangkok"
        }
    ]

    for t in testimonials:
        st.markdown("""
        <div class="card testimonial-card" style="margin-bottom:1rem;">
            <div style="font-size:1.8rem; margin-bottom:0.5rem; color:var(--accent);">{t['icon']}</div>
            <p style="font-style:italic; font-size:1.1rem; color:var(--text-primary);">"{t['quote']}"</p>
            <p style="text-align:right; font-weight:600; margin-bottom:0; color:var(--text-primary);">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style="text-align:center; margin:2rem 0;">
        <a href="#discovery" class="stButton cta-button" style="display:inline-block; text-decoration:none;">Book Your Session</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG PAGE ---
elif selected == "Blog":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2 style="color: var(--text-primary);">Hypnotherapy Insights</h2>
        <p style="color: var(--text-secondary);">Educational resources and frequently asked questions</p>
    </div>
    """, unsafe_allow_html=True)

    # Featured Articles
    articles = [
        {
            "title": "How Hypnosis Rewires Your Brain",
            "summary": "The neuroscience behind why brief hypnotherapy can create lasting change...",
            "date": "May 15, 2023"
        },
        {
            "title": "Quit Smoking Without Willpower",
            "summary": "How John quit his 20-year smoking habit in just 2 sessions...",
            "date": "April 2, 2023"
        }
    ]

    for article in articles:
        with st.expander(f"📝 {article['title']} - {article['date']}"):
            st.write(article['summary'])
            st.button("Read Article", key=f"article_{article['title']}")

    # FAQ Section
    st.markdown("""
    <div style="margin:3rem 0;">
        <h3 style="color: var(--text-primary);">Frequently Asked Questions</h3>
    </div>
    """, unsafe_allow_html=True)

    faqs = [
        {
            "question": "Is hypnotherapy safe?",
            "answer": "Yes, clinical hypnotherapy is a safe, non-invasive approach. You remain fully aware and in control at all times."
        },
        {
            "question": "How many sessions will I need?",
            "answer": "Most clients achieve their goals in just 2 sessions. About 15% opt for an optional third session."
        }
    ]

    for faq in faqs:
        with st.expander(f"❓ {faq['question']}"):
            st.write(faq['answer'])

# --- BOOK NOW PAGE ---
elif selected == "Book Now":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2 style="color: var(--text-primary);">Start Your Transformation</h2>
        <p style="color: var(--text-secondary);">Choose your preferred booking option below</p>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for the booking options
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: var(--accent); text-align:center;">Free Discovery Call</h3>
            <p style="text-align:center; color:var(--text-secondary);">15-minute consultation to discuss your goals</p>
            <ul style="margin-left:1rem; color:var(--text-secondary);">
                <li>No obligation</li>
                <li>Learn how hypnotherapy can help</li>
                <li>Get your questions answered</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: var(--accent); text-align:center;">Rewiring Package</h3>
            <p style="text-align:center; color:var(--text-secondary);">Complete 2-session transformation</p>
            <ul style="margin-left:1rem; color:var(--text-secondary);">
                <li>Analysis Session (90 mins)</li>
                <li>Transformation Session (90 mins)</li>
                <li>Email support between sessions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # # Create tabs for different booking options
    # tab1, tab2 = st.tabs(["Free Discovery Call", "Rewiring Package"])

    # with tab1:
    #     with st.form("discovery_form"):
    #         st.markdown("""
    #         <div style="text-align:center; margin-bottom:1.5rem;">
    #             <h3 style="color: var(--accent);">Free 15-Minute Discovery Call</h3>
    #             <p style="color: var(--text-secondary);">No obligation consultation to discuss your goals</p>
    #         </div>
    #         """, unsafe_allow_html=True)

    #         cols = st.columns(2)
    #         with cols[0]:
    #             name = st.text_input("Your Name*", key="disc_name")
    #         with cols[1]:
    #             email = st.text_input("Email*", key="disc_email")

    #         concern = st.selectbox(
    #             "Primary Concern*",
    #             ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
    #             key="disc_concern"
    #         )

    #         submitted = st.form_submit_button(
    #             "Book Discovery Call", 
    #             type="primary",  # This will now use our teal color
    #             help="Schedule your free 15-minute consultation"
    #         )

    #         if submitted:
    #             if not name or not email or concern == "Select one...":
    #                 st.error("Please fill in all required fields")
    #             elif not is_valid_email(email):
    #                 st.error("Please enter a valid email address")
    #             else:
    #                 calendly_url = "https://calendly.com/laetitiasheppard/discovery"
    #                 st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
    #                 if send_email(name, email, concern, "Booking type: Discovery Call"):
    #                     st.success("✓ Appointment scheduled!")
    #                 st.balloons()

    # with tab2:
    #     with st.form("package_form"):
    #         st.markdown("""
    #         <div style="text-align:center; margin-bottom:1.5rem;">
    #             <h3 style="color: var(--accent);">Rewiring Package</h3>
    #             <p style="color: var(--text-secondary);">Complete 2-session transformation program</p>
    #         </div>
    #         """, unsafe_allow_html=True)

    #         cols = st.columns(2)
    #         with cols[0]:
    #             name = st.text_input("Your Name*", key="pkg_name")
    #         with cols[1]:
    #             email = st.text_input("Email*", key="pkg_email")

    #         concern = st.selectbox(
    #             "Primary Concern*",
    #             ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
    #             key="pkg_concern"
    #         )

    #         submitted = st.form_submit_button(
    #             "Book Package Now", 
    #             type="primary",  # This will now use our teal color
    #             help="Schedule your complete transformation package"
    #         )

    #         if submitted:
    #             if not name or not email or concern == "Select one...":
    #                 st.error("Please fill in all required fields")
    #             elif not is_valid_email(email):
    #                 st.error("Please enter a valid email address")
    #             else:
    #                 calendly_url = "https://calendly.com/laetitiasheppard/package"
    #                 st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
    #                 if send_email(name, email, concern, "Booking type: Rewiring Package"):
    #                     st.success("✓ Package booked!")
    #                 st.balloons()

# --- BOOKING FORM ---
st.markdown("""
<div id="discovery" class="card" style="margin:3rem 0; padding:2rem; border:1px solid var(--border);">
    <h2 style="color: var(--accent); text-align:center; margin-bottom:1.5rem;">Free 15-Minute Discovery Call</h2>
    <p style="text-align:center; color: var(--text-secondary); margin-bottom:2rem;">Begin your journey to transformation with a complimentary consultation</p>
""", unsafe_allow_html=True)

with st.form("booking_form"):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("Your Name*", 
                           placeholder="First and last name",
                           help="Please enter your full name")
    with cols[1]:
        email = st.text_input("Email*", 
                            placeholder="Your email address",
                            help="We'll send confirmation to this address")

    concern = st.selectbox(
        "Primary Concern*",
        ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
        help="What would you like help with?"
    )

    message = st.text_area("Anything we should know", 
                         placeholder="Brief details about your situation",
                         help="Optional - share anything that might help us prepare")

    submitted = st.form_submit_button(
        "Schedule My Free Call", 
        #type="primary",
        class="stButton cta-button",
        help="You'll be redirected to our booking calendar"
    )
    
    if submitted:
        if not name or not email or concern == "Select one...":
            st.error("Please fill in all required fields")
        elif not is_valid_email(email):
            st.error("Please enter a valid email address")
        else:
            calendly_url = "https://calendly.com/laetitiasheppard/30min"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
            if send_email(name, email, concern, message):
                st.success("✓ Appointment scheduled! Check your email for confirmation.")
            else:
                st.success("✓ Appointment scheduled! (Email confirmation pending)")
            st.balloons()

  
# --- FOOTER ---
st.markdown(""
<div style="text-align:center; margin:3rem 0 1rem 0; padding-top:2rem; border-top:1px solid var(--border);">
    <p style="color:var(--text-secondary);">Laetitia Sheppard • Clinical Hypnotherapy • Bangkok, Thailand</p>
    <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:1rem;">NEW ADDRESS in ASOKE Sukhumvit</p>
    <button onclick="window.open('https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw', '_blank')" 
       class="stButton cta-button">
       Get Directions
    </button>
    <p style="color:var(--text-secondary); font-size:0.9rem;">© {datetime.datetime.now().year} All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)


