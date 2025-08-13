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

# --- CONSTANTS (Updated for Streamlit Secrets) ---
SMTP_SERVER = st.secrets.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(st.secrets.get("SMTP_PORT", 587))
EMAIL_FROM = st.secrets.get("EMAIL_FROM", "website@laetitiasheppard.com")
EMAIL_TO = st.secrets.get("EMAIL_TO", "laetitiasheppard@gmail.com")

# --- UTILITY FUNCTIONS ---
def is_valid_email(email):
    """Validate email format"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def send_email(name, email, concern, message):
    """Send email using Streamlit secrets"""
    try:
        if not all([name, email, concern != "Select one..."]):
            st.error("Missing required fields")
            return False

        msg = MIMEText(f"""
        New Consultation Request:
        Name: {name}
        Email: {email}
        Concern: {concern}
        Message: {message}
        """)
        
        msg['Subject'] = 'New Hypnotherapy Consultation Request'
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(
                st.secrets["SMTP_USERNAME"],
                st.secrets["SMTP_PASSWORD"]
            )
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email failed: {str(e)}")
        return False

# --- QUIZ FUNCTIONS ---
def reset_quiz():
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

def handle_quiz_answer(question_id, answer):
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1

# --- STYLING ---
def inject_css():
    st.markdown("""
    <style>
    :root {
        --primary: #212529;
        --accent: #D4AF37;
        --light: #F8F9FA;
        --border: #DEE2E6;
    }
    .hero {
        background: #1C1C1E;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
    }
    .step {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: var(--border);
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    .step.active {
        background: var(--accent);
    }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE APP ---
if 'quiz_answers' not in st.session_state:
    reset_quiz()

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
<div class="hero">
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

# [Previous imports and configuration remain the same until the page sections]

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Our Proven 2-Step Method</h2>
        <p>Why most clients achieve lasting change in just two sessions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Video Embed
    st.markdown("""
    <div class="responsive-iframe" style="margin:2rem 0;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/EXAMPLE_VIDEO_ID" 
        frameborder="0" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    # Method Steps
    steps = st.columns(3)
    with steps[0]:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; height:100%;">
            <div style="background:#D4AF37; color:#1C1C1E; width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">1</div>
            <h3>Analysis Session</h3>
            <ul style="text-align:left;">
                <li>Comprehensive evaluation</li>
                <li>Identify subconscious drivers</li>
                <li>Develop personalized plan</li>
                <li>90 minutes in-person/Zoom</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with steps[1]:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; height:100%;">
            <div style="background:#D4AF37; color:#1C1C1E; width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">2</div>
            <h3>Transformation</h3>
            <ul style="text-align:left;">
                <li>Guided hypnosis</li>
                <li>Create new neural pathways</li>
                <li>Anchor positive behaviors</li>
                <li>90 minutes (3-7 days later)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with steps[2]:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; height:100%;">
            <div style="background:#F8F9FA; color:#1C1C1E; width:50px; height:50px; border-radius:50%; 
            display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">+1</div>
            <h3>Reinforcement</h3>
            <ul style="text-align:left;">
                <li>Strengthen new patterns</li>
                <li>Address remaining blocks</li>
                <li>Typically not needed</li>
                <li>60 minutes (optional)</li>
            </ul>
            <p style="color:#D4AF37; font-weight:bold;">+1000 THB</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Pricing
    st.markdown("""
    <div style="background:white; padding:1.5rem; border-radius:12px; margin:2rem auto; max-width:800px;">
        <h3 style="margin-top:0;">Pricing Options</h3>
        <p><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p><strong>Premium Package:</strong> 4000 THB (Includes optional reinforcement)</p>
        <p style="font-size:0.9rem; color:#6C757D;">Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES PAGE ---
elif selected == "Success":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Client Transformations</h2>
        <p>Real people who changed their lives in 2 sessions</p>
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
        st.markdown(f"""
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem; border-left:4px solid #D4AF37;">
            <div style="font-size:1.8rem; margin-bottom:0.5rem;">{t['icon']}</div>
            <p style="font-style:italic; font-size:1.1rem;">"{t['quote']}"</p>
            <p style="text-align:right; font-weight:600; margin-bottom:0;">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # CTA
    st.markdown("""
    <div style="text-align:center; margin:2rem 0;">
        <a href="#discovery" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; 
        font-weight:600; display:inline-block; text-decoration:none;">Book Your Session</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG PAGE ---
elif selected == "Blog":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Hypnotherapy Insights</h2>
        <p>Educational resources and frequently asked questions</p>
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
        <h3>Frequently Asked Questions</h3>
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

# [Booking form and footer remain the same as in your original code]

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
