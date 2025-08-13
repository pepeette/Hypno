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
    margin-bottom: 2rem;
}
.step {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: var(--border);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 0 0.5rem;
}
.step.active {
    background: var(--accent);
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
    <h2 style="color: var(--accent);">Break Free in Just 2 Sessions</h2>
    <p style="font-size:1.2rem; color:#E9ECEF; max-width:700px; margin:0 auto 2rem;">
        Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
    </p>
    <a href="#quiz" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin:0.5rem; text-decoration:none;">Take the 30-Second Quiz</a>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align:center; margin:3rem 0;">
        <h2>30-Second Suitability Quiz</h2>
        <p>Answer 3 questions to see if the method is right for you</p>
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
                if st.button(option, key=f"q1o{i}"):
                    handle_quiz_answer(1, option)
    
    # Question 2
    elif st.session_state.quiz_step == 2:
        st.markdown("### Q2: How long have you struggled with this?")
        options = ["Less than 6 months", "6 months to 2 years", "More than 2 years"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q2o{i}"):
                    handle_quiz_answer(2, option)
    
    # Question 3
    elif st.session_state.quiz_step == 3:
        st.markdown("### Q3: How ready are you to make a change?")
        options = ["Just exploring options", "Somewhat ready", "Very ready - I'm committed"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q3o{i}"):
                    handle_quiz_answer(3, option)
    
    # Quiz Results
    if len(st.session_state.quiz_answers) == 3:
        st.success("### Based on your answers, our 2-session method would likely work well for you!")
        
        # Show summary of answers
        with st.expander("See your answers"):
            st.write(f"1. Goal: {st.session_state.quiz_answers.get(1, 'Not answered')}")
            st.write(f"2. Duration: {st.session_state.quiz_answers.get(2, 'Not answered')}")
            st.write(f"3. Readiness: {st.session_state.quiz_answers.get(3, 'Not answered')}")
        
        # Action buttons
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

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Proven 2-Step Method</h2>
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
                <li>Around 90 minutes in-person/Zoom</li>
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
                <li>Around 90 minutes (3-7 days later)</li>
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
                <li>Around 60 minutes (optional)</li>
            </ul>
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
elif selected == "Book Now":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Start Your Transformation</h2>
        <p>Choose your preferred booking option below</p>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for the booking options
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div style="background:#F8F9FA; padding:1.5rem; border-radius:12px; height:100%;">
            <h3 style="color:#D4AF37; text-align:center;">Free Discovery Call</h3>
            <p style="text-align:center;">15-minute consultation to discuss your goals</p>
            <ul style="margin-left:1rem;">
                <li>No obligation</li>
                <li>Learn how hypnotherapy can help</li>
                <li>Get your questions answered</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background:#F8F9FA; padding:1.5rem; border-radius:12px; height:100%;">
            <h3 style="color:#D4AF37; text-align:center;">Rewiring Package</h3>
            <p style="text-align:center;">Complete 2-session transformation</p>
            <ul style="margin-left:1rem;">
                <li>Analysis Session (90 mins)</li>
                <li>Transformation Session (90 mins)</li>
                <li>Email support between sessions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Booking form (same for both options)
    st.markdown("""
    <div id="discovery" style="background:white; padding:2rem; border-radius:12px; margin:3rem 0;">
        <h3 style="text-align:center;">Book Your Session</h3>
    """, unsafe_allow_html=True)

    with st.form("booking_form"):
        booking_type = st.radio(
            "Session Type*",
            ["Free Discovery Call (15 mins)", "Rewiring Package (2 sessions)"],
            horizontal=True
        )
        
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
        
        submitted = st.form_submit_button(f"Book My {'Discovery Call' if 'Discovery' in booking_type else 'Package'}")
        
        if submitted:
            if not name or not email or concern == "Select one...":
                st.error("Please fill in all required fields")
            elif not is_valid_email(email):
                st.error("Please enter a valid email address")
            else:
                # Different Calendly links for each type
                calendly_url = (
                    "https://calendly.com/laetitiasheppard/discovery" 
                    if "Discovery" in booking_type else
                    "https://calendly.com/laetitiasheppard/package"
                )
                
                # Send email with booking type
                email_success = send_email(
                    name, email, concern, 
                    f"Booking type: {booking_type}\n\n{message}"
                )
                
                # Redirect to Calendly
                st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', 
                           unsafe_allow_html=True)
                
                if email_success:
                    st.success("✓ Appointment scheduled! Check your email for confirmation.")
                else:
                    st.success("✓ Appointment scheduled! (Email confirmation pending)")
                
                st.balloons()
                
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
    <p style="color:#6C757D;">Laetitia Sheppard • Clinical Hypnotherapy • Bangkok, Thailand</p>
    <p style="color:#6C757D; font-size:0.9rem; margin-bottom:1rem;">NEW ADDRESS in ASOKE Sukhumvit</p>
    <a href="https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw" 
       target="_blank"
       style="background:#D4AF37; color:#1C1C1E; padding:0.5rem 1.5rem; border-radius:8px; 
       font-weight:600; display:inline-block; text-decoration:none; margin:0.5rem;">
       Get Directions
    </a>
    <p style="color:#6C757D; font-size:0.9rem;">© {datetime.datetime.now().year} All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
