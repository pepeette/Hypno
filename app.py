import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import smtplib
from email.mime.text import MIMEText
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2-Step Hypnotherapy | Laetitia Sheppard",
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
    }}
    
    /* Force light mode */
    [data-testid="stAppViewContainer"] {{
        background-color: var(--light) !important;
        color-scheme: light !important;
    }}
    
    /* Checkmark styling that works in both modes */
    .checkmark {{
        color: var(--accent) !important;
        font-weight: bold;
    }}
    
    /* Quiz styling */
    .quiz-question {{
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }}
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {{
        .hero-title {{ font-size: 1.8rem !important; }}
    }}
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --- EMAIL FUNCTION ---
def send_email(name, email, concern, message):
    try:
        msg = MIMEText(f"""
        New Consultation Request:
        Name: {name}
        Email: {email}
        Concern: {concern}
        Message: {message}
        """)
        
        msg['Subject'] = 'New Hypnotherapy Consultation Request'
        msg['From'] = 'website@laetitiasheppard.com'
        msg['To'] = 'laetitiasheppard@gmail.com'
        
        # Configure your SMTP settings (example using Gmail)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_app_password')
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# --- QUIZ DATA HANDLING ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}

def handle_quiz_answer(question_id, answer):
    st.session_state.quiz_answers[question_id] = answer

# --- NAVIGATION ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Method", "Success", "Book Now"],
    icons=["house", "magic", "stars", "calendar"],
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
    <h1 class="hero-title">Break Free in Just 2 Sessions</h1>
    <p class="hero-subtitle">Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits - without relying on willpower</p>
    <a href="#quiz" class="cta">Take Our 30-Second Quiz</a>
    <p style="margin: 1.5rem 0 0 0;">
        <span class="checkmark">✓</span> <span style="font-weight:500;">92% success rate</span> &nbsp;&nbsp;
        <span class="checkmark">✓</span> <span style="font-weight:500;">No withdrawal symptoms</span> &nbsp;&nbsp;
        <span class="checkmark">✓</span> <span style="font-weight:500;">English/French/Italian</span>
    </p>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align: center; margin: 3rem 0;">
        <h2>30-Second Suitability Quiz</h2>
        <p>Answer 3 questions to see if our method is right for you</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quiz Questions
    questions = [
        {
            "id": 1,
            "question": "What are you looking to change?",
            "options": ["Quit smoking", "Reduce anxiety", "Improve sleep", "Other"]
        },
        {
            "id": 2,
            "question": "How long have you struggled with this?",
            "options": ["<6 months", "6 months-2 years", ">2 years"]
        },
        {
            "id": 3,
            "question": "How ready are you to make a change?",
            "options": ["Just exploring", "Somewhat ready", "Very ready"]
        }
    ]
    
    for q in questions:
        st.markdown(f"""
        <div class="quiz-question">
            <h3>Q{q['id']}: {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(len(q['options']))
        for i, option in enumerate(q['options']):
            with cols[i]:
                if st.button(option, key=f"q{q['id']}o{i}"):
                    handle_quiz_answer(q['id'], option)
    
    # Quiz Results
    if len(st.session_state.quiz_answers) == len(questions):
        st.success("### Based on your answers, our 2-session method would likely work well for you!")
        st.markdown("""
        <div style="text-align: center; margin: 1.5rem 0;">
            <a href="#discovery" class="cta">Book Your Free Consultation</a>
        </div>
        """, unsafe_allow_html=True)

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Our Proven 2-Step Method</h2>
        <p>Why most clients achieve lasting change in just two sessions</p>
    </div>
    """, unsafe_allow_html=True)
    
    steps = [
        {
            "number": "1",
            "title": "Analysis Session",
            "desc": """
            - Comprehensive evaluation of your specific patterns
            - Identify subconscious drivers of your behavior
            - Develop personalized hypnosis plan
            - 90 minutes in-person or via Zoom
            """,
            "price": ""
        },
        {
            "number": "2",
            "title": "Transformation Session",
            "desc": """
            - Guided hypnosis to reprogram patterns
            - Create new neural pathways
            - Anchor positive behaviors
            - 90 minutes (scheduled 3-7 days after Session 1)
            """,
            "price": ""
        },
        {
            "number": "+1",
            "title": "Reinforcement (Optional)",
            "desc": """
            - Strengthen new patterns
            - Address any remaining blocks
            - Typically not needed (85% of clients)
            - 60 minutes (available within 30 days)
            """,
            "price": "+1000 THB"
        }
    ]
    
    cols = st.columns(3)
    for i, step in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; height: 100%;">
                <div style="background: {'var(--accent)' if i < 2 else '#f4f4f6'}; color: var(--primary); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 1rem;">{step['number']}</div>
                <h3 style="margin: 0 0 1rem 0;">{step['title']}</h3>
                <div style="text-align: left; margin-bottom: 1rem;">{step['desc']}</div>
                {f'<p style="color: var(--accent); font-weight: bold; margin: 0;">{step["price"]}</p>' if step["price"] else ''}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 12px; margin: 2rem auto; max-width: 800px;">
        <h3 style="margin-top: 0;">Pricing Options</h3>
        <p><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p><strong>Premium Package:</strong> 4000 THB (Sessions 1, 2 + optional reinforcement)</p>
        <p style="font-size: 0.9rem; color: #6E6E73;">Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES ---
elif selected == "Success":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2>Client Transformations</h2>
        <p>Real people who changed their lives in 2 sessions</p>
    </div>
    """, unsafe_allow_html=True)
    
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
        },
        {
            "icon": "🧘",
            "quote": "The anxiety that controlled my daily life is now manageable...",
            "author": "Anxiety Patient, France"
        }
    ]
    
    for t in testimonials:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; border-left: 4px solid var(--accent);">
            <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">{t['icon']}</div>
            <p style="font-style: italic; font-size: 1.1rem;">"{t['quote']}"</p>
            <p style="text-align: right; font-weight: 600; margin-bottom: 0;">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="#quiz" class="cta">Take Our Quiz</a>
    </div>
    """, unsafe_allow_html=True)

# --- BOOKING FORM ---
st.markdown("""
<div id="discovery" style="background: white; padding: 2rem; border-radius: 12px; margin: 3rem 0;">
    <h2 style="text-align: center; margin-top: 0;">Free 15-Minute Discovery Call</h2>
    <p style="text-align: center;">Let's discuss your goals and how we can help</p>
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
    
    col1, col2 = st.columns([1,2])
    with col1:
        submitted = st.form_submit_button("Schedule My Free Call")
    with col2:
        if submitted:
            if not name or not email or concern == "Select one...":
                st.error("Please fill in all required fields")
            else:
                # Send to Calendly
                calendly_url = "https://calendly.com/laetitiasheppard/30min"
                st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
                
                # Send email
                if send_email(name, email, concern, message):
                    st.success("✓ Appointment scheduled! Check your email for confirmation.")
                else:
                    st.success("✓ Appointment scheduled! (Email confirmation pending)")
                
                st.balloons()

st.markdown("""
</div>
<div style="text-align: center; margin: 3rem 0 1rem 0; padding-top: 2rem; border-top: 1px solid #E2E2E6;">
    <p style="color: #6E6E73;">Laetitia Sheppard • Clinical Hypnotherapy • Bangkok</p>
    <p style="color: #6E6E73; font-size: 0.9rem;">© {datetime.datetime.now().year} All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
