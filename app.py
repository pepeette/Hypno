import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import re

# --- Load Environment Variables ---
load_dotenv()

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2-Step Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CONSTANTS ---
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
EMAIL_FROM = os.getenv('EMAIL_FROM', 'website@laetitiasheppard.com')
EMAIL_TO = os.getenv('EMAIL_TO', 'laetitiasheppard@gmail.com')

# --- UTILITY FUNCTIONS ---
def is_valid_email(email):
    """Validate email format"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def send_email(name, email, concern, message):
    try:
        if not all([name, email, concern != "Select one..."]):
            st.error("Missing required fields")
            return False

        msg = MIMEText(f"Name: {name}\nEmail: {email}\nConcern: {concern}\nMessage: {message}")
        msg['Subject'] = 'New Consultation Request'
        msg['From'] = os.getenv('EMAIL_FROM')
        msg['To'] = os.getenv('EMAIL_TO')

        with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email failed: {str(e)}")
        return False

def reset_quiz():
    """Reset quiz progress"""
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

def handle_quiz_answer(question_id, answer):
    """Store quiz answer and advance to next question"""
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1

# --- STYLING ---
def inject_css():
    """Inject custom CSS styles"""
    st.markdown(f"""
    <style>
    :root {{
        --primary: #212529;
        --accent: #D4AF37;
        --light: #F8F9FA;
        --border: #DEE2E6;
    }}
    
    /* Typography */
    h1 {{
        font-size: 2.5rem !important;
        color: var(--accent) !important;
    }}
    
    /* Progress steps */
    .step {{
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: var(--border);
    }}
    .step.active {{
        background: var(--accent);
    }}
    
    /* Responsive iframes */
    .responsive-iframe {{
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
    }}
    .responsive-iframe iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'quiz_answers' not in st.session_state:
    reset_quiz()

# --- APP LAYOUT ---
inject_css()

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Method", "Success", "Blog", "Book Now"],
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
<div class="hero" style="background:#1C1C1E; padding:2rem; text-align:center; border-radius:12px; margin-bottom:2rem;">
    <h1>Break Free in Just 2 Sessions</h1>
    <p style="font-size:1.2rem; color:#E9ECEF; max-width:700px; margin:0 auto 2rem;">
        Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
    </p>
    <a href="#quiz" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin:0.5rem; text-decoration:none;">Take Our 30-Second Quiz</a>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align:center; margin:3rem 0;">
        <h2>30-Second Suitability Quiz</h2>
        <p>Answer 3 questions to see if our method is right for you</p>
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
    
    # Quiz Questions
    if st.session_state.quiz_step == 1:
        st.markdown("### Q1: What are you looking to change?")
        options = ["Quit smoking", "Reduce anxiety", "Improve sleep", "Other"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q1o{i}"):
                    handle_quiz_answer(1, option)
    
    elif st.session_state.quiz_step == 2:
        st.markdown("### Q2: How long have you struggled with this?")
        options = ["<6 months", "6 months-2 years", ">2 years"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q2o{i}"):
                    handle_quiz_answer(2, option)
    
    elif st.session_state.quiz_step == 3:
        st.markdown("### Q3: How ready are you to make a change?")
        options = ["Just exploring", "Somewhat ready", "Very ready"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q3o{i}"):
                    handle_quiz_answer(3, option)
                    
    if len(st.session_state.quiz_answers) == 3:
        st.success("Our method is a good fit for you!")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Book Consultation", "#discovery")
        with col2:
            if st.button("Retake Quiz"):
                reset_quiz()
            
    # Quiz Results
    if len(st.session_state.quiz_answers) == 3:
        st.success("### Based on your answers, our 2-session method would likely work well for you!")
        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown("""
            <div style="text-align:center; margin:1.5rem 0;">
                <a href="#discovery" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; text-decoration:none;">Book Consultation</a>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("Retake Quiz"):
                reset_quiz()

# --- OTHER PAGE CONTENT WOULD GO HERE ---
# (Method, Success Stories, Blog sections would follow similar patterns)

# --- BOOKING FORM ---
st.markdown("""
<div id="discovery" style="background:white; padding:2rem; border-radius:12px; margin:3rem 0;">
    <h2 style="text-align:center;">Free 15-Minute Discovery Call</h2>
""", unsafe_allow_html=True)

with st.form("booking_form"):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("Your Name*", placeholder="First and last name")
    with cols[1]:
        email = st.text_input("Email*", placeholder="Your email address")
    
    concern = st.selectbox(
        "Primary Concern*",
        ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"]
    )
    
    message = st.text_area("Anything we should know", placeholder="Brief details about your situation")
    
    submitted = st.form_submit_button("Schedule My Free Call")
    
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
st.markdown(f"""
<div style="text-align:center; margin:3rem 0 1rem 0; padding-top:2rem; border-top:1px solid #DEE2E6;">
    <p style="color:#6C757D;">Laetitia Sheppard • Clinical Hypnotherapy • Bangkok</p>
    <p style="color:#6C757D; font-size:0.9rem;">© {datetime.datetime.now().year} All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
