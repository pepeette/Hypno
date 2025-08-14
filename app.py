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
    st.session_state.quiz_complete = False

def handle_quiz_answer(question_id, answer):
    st.session_state.quiz_answers[question_id] = answer
    if st.session_state.quiz_step < 3:
        st.session_state.quiz_step += 1
    else:
        st.session_state.quiz_complete = True

def reset_quiz():
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1
    st.session_state.quiz_complete = False

# --- STYLING ---
st.markdown("""
<style>
:root {
    --bg: #FAF9F7;
    --card-bg: #FFFFFF;
    --text-primary: #222222;
    --text-secondary: #6B7280;
    --accent: #CBAACB;
    --accent-hover: #A67AA9;
    --border: #E5E7EB;
}

body {
    background-color: var(--bg);
    color: var(--text-primary);
}

.stButton>button {
    background-color: var(--accent);
    color: var(--text-primary);
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    transition: all 0.3s ease;
    font-weight: 500;
}

.stButton>button:hover {
    background-color: var(--accent-hover);
    color: white;
}

.hero {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
    padding: 3rem;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 2rem;
    color: white;
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
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.step.active {
    background: var(--accent);
    color: white;
}

.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    color: var(--text-primary);
}

.stMarkdown p {
    color: var(--text-secondary);
}

.stSelectbox, .stTextInput, .stTextArea {
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 8px !important;
}

.css-1aumxhk {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

/* Navigation styling */
.st-bh, .st-cg, .st-ch, .st-ci, .st-cj, .st-ck {
    color: var(--text-primary) !important;
}

[data-testid="stHorizontalBlock"] > div:nth-child(1) > div > div > div > div > div {
    background-color: var(--card-bg);
    border-radius: 8px;
    padding: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

[data-testid="stHorizontalBlock"] > div:nth-child(1) > div > div > div > div > div > a {
    color: var(--text-primary);
    font-weight: 500;
}

[data-testid="stHorizontalBlock"] > div:nth-child(1) > div > div > div > div > div > a:hover {
    color: var(--accent-hover);
}

[data-testid="stHorizontalBlock"] > div:nth-child(1) > div > div > div > div > div > a[aria-selected="true"] {
    background-color: var(--accent);
    color: white !important;
    border-radius: 8px;
}

.testimonial-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}

.consultation-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-top: 2rem;
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
            "background-color": "#FFFFFF",
            "padding": "0.5rem",
            "border-radius": "8px",
            "box-shadow": "0 2px 4px rgba(0,0,0,0.05)"
        },
        "nav-link": {
            "color": "#222222",
            "font-weight": "500",
            "margin": "0 0.5rem",
        },
        "nav-link-selected": {
            "background": "#CBAACB",
            "color": "white",
            "font-weight": "bold",
            "border-radius": "8px"
        },
    }
)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <h2 style="color: white;">Break Free in Just 2 Sessions</h2>
    <p style="font-size:1.2rem; color:white; max-width:700px; margin:0 auto 2rem;">
        Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
    </p>
    <a href="#quiz" style="background:white; color:#A67AA9; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin:0.5rem; text-decoration:none;">Take the 30-Second Quiz</a>
</div>
""", unsafe_allow_html=True)

# --- HOME PAGE ---
if selected == "Home":
    st.markdown("""
    <div id="quiz" style="text-align:center; margin:3rem 0;">
        <h2>30-Second Suitability Quiz</h2>
        <p style="color: var(--text-secondary);">Answer 3 questions to see if the method is right for you</p>
    </div>
    """, unsafe_allow_html=True)

    # Progress indicator
    st.markdown(f"""
    <div style="display:flex; justify-content:center; gap:1rem; margin:2rem 0;">
        <div class="step {'active' if st.session_state.quiz_step == 1 else ''}">1</div>
        <div class="step {'active' if st.session_state.quiz_step == 2 else ''}">2</div>
        <div class="step {'active' if st.session_state.quiz_step == 3 else ''}">3</div>
    </div>
    """, unsafe_allow_html=True)

    # Question 1
    if st.session_state.quiz_step == 1 and not st.session_state.quiz_complete:
        st.markdown("### Q1: What are you looking to change?")
        options = ["Quit smoking", "Reduce anxiety", "Improve sleep", "Other"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q1o{i}"):
                    handle_quiz_answer(1, option)

    # Question 2
    elif st.session_state.quiz_step == 2 and not st.session_state.quiz_complete:
        st.markdown("### Q2: How long have you struggled with this?")
        options = ["Less than 6 months", "6 months to 2 years", "More than 2 years"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q2o{i}"):
                    handle_quiz_answer(2, option)

    # Question 3
    elif st.session_state.quiz_step == 3 and not st.session_state.quiz_complete:
        st.markdown("### Q3: Have you tried other methods before?")
        options = ["Yes, nothing worked", "Yes, with limited success", "No, this is my first attempt"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q3o{i}"):
                    handle_quiz_answer(3, option)

    # Results
    if st.session_state.quiz_complete:
        st.markdown("""
        <div style="text-align:center; padding:2rem; background-color:var(--card-bg); border-radius:12px; margin-top:2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 style="color:var(--accent-hover);">You're a great candidate!</h3>
            <p style="color:var(--text-secondary);">Based on your answers, the 2-step method would likely work well for you.</p>
            <p style="color:var(--text-secondary);">Book a free consultation to learn more.</p>
            <a href="#book-now" style="background:var(--accent); color:white; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin:1rem; text-decoration:none;">Book Consultation</a>
            <div style="margin-top:1rem;">
                <button onclick="window.location.href='#quiz'" style="background:none; border:none; color:var(--accent); cursor:pointer; font-weight:500;">Retake quiz</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Retake quiz", key="retake_quiz"):
            reset_quiz()
            st.rerun()

    # Additional Content
    st.markdown("""
    <div style="margin-top:4rem;">
        <h2>Why Choose This Approach?</h2>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:2rem; margin:2rem 0;">
            <div style="background-color:var(--card-bg); padding:1.5rem; border-radius:8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h4 style="color:var(--accent-hover);">Evidence-Based</h4>
                <p style="color:var(--text-secondary);">Combining proven techniques from clinical hypnotherapy and cognitive behavioral therapy</p>
            </div>
            <div style="background-color:var(--card-bg); padding:1.5rem; border-radius:8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h4 style="color:var(--accent-hover);">Fast Results</h4>
                <p style="color:var(--text-secondary);">Most clients see significant improvement in just 2-3 sessions</p>
            </div>
            <div style="background-color:var(--card-bg); padding:1.5rem; border-radius:8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <h4 style="color:var(--accent-hover);">Personalized</h4>
                <p style="color:var(--text-secondary);">Each session is tailored to your specific needs and goals</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="background-color:var(--card-bg); padding:2rem; border-radius:12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h2>The 2-Step Hypnotherapy Method</h2>
        <p style="color:var(--text-secondary);">A proven approach combining clinical hypnotherapy with cognitive techniques</p>
        
        <div style="display:flex; gap:2rem; margin:3rem 0;">
            <div style="flex:1; background-color:var(--bg); padding:1.5rem; border-radius:8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="width:50px; height:50px; background-color:var(--accent); color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">1</div>
                <h3 style="color:var(--accent-hover);">Assessment</h3>
                <p style="color:var(--text-secondary);">We identify the root causes and triggers of your issue through in-depth discussion and analysis.</p>
                <ul style="color:var(--text-secondary); padding-left:1.2rem;">
                    <li>Comprehensive history taking</li>
                    <li>Identifying subconscious patterns</li>
                    <li>Understanding your unique psychology</li>
                </ul>
            </div>
            <div style="flex:1; background-color:var(--bg); padding:1.5rem; border-radius:8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                <div style="width:50px; height:50px; background-color:var(--accent); color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">2</div>
                <h3 style="color:var(--accent-hover);">Transformation</h3>
                <p style="color:var(--text-secondary);">Using hypnosis, we rewire subconscious patterns and install new, positive behaviors.</p>
                <ul style="color:var(--text-secondary); padding-left:1.2rem;">
                    <li>Customized hypnotic suggestions</li>
                    <li>Cognitive restructuring</li>
                    <li>Anchoring positive states</li>
                </ul>
            </div>
        </div>
        
        <div style="background-color:var(--bg); padding:1.5rem; border-radius:8px; margin-top:2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color:var(--accent-hover);">What Makes This Different?</h3>
            <p style="color:var(--text-secondary);">Traditional therapy often focuses solely on conscious understanding, while our approach works directly with the subconscious mind where habits and emotional patterns are stored. This leads to faster, more lasting change.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS PAGE ---
elif selected == "Success":
    st.markdown("""
    <div style="background-color:var(--card-bg); padding:2rem; border-radius:12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h2>Success Stories</h2>
        <p style="color:var(--text-secondary);">Real people who transformed their lives with the 2-step method</p>
        
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:2rem; margin:3rem 0;">
            <div class="testimonial-card">
                <div style="display:flex; align-items:center; margin-bottom:1rem;">
                    <div style="width:50px; height:50px; background-color:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; margin-right:1rem;">S</div>
                    <div>
                        <h4 style="color:var(--accent-hover); margin:0;">Sarah, 34</h4>
                        <p style="color:var(--text-secondary); margin:0; font-size:0.9rem;">Former smoker</p>
                    </div>
                </div>
                <p style="color:var(--text-secondary);">"After 10 years of smoking, I quit in just two sessions. I haven't touched a cigarette in 6 months! The cravings disappeared completely after the first session."</p>
                <div style="color:var(--accent); font-size:0.9rem;">★★★★★</div>
            </div>
            
            <div class="testimonial-card">
                <div style="display:flex; align-items:center; margin-bottom:1rem;">
                    <div style="width:50px; height:50px; background-color:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; margin-right:1rem;">M</div>
                    <div>
                        <h4 style="color:var(--accent-hover); margin:0;">Michael, 42</h4>
                        <p style="color:var(--text-secondary); margin:0; font-size:0.9rem;">Anxiety relief</p>
                    </div>
                </div>
                <p style="color:var(--text-secondary);">"My anxiety levels dropped dramatically after just one session. I finally feel in control of my emotions and can handle stressful situations calmly."</p>
                <div style="color:var(--accent); font-size:0.9rem;">★★★★★</div>
            </div>
            
            <div class="testimonial-card">
                <div style="display:flex; align-items:center; margin-bottom:1rem;">
                    <div style="width:50px; height:50px; background-color:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; margin-right:1rem;">E</div>
                    <div>
                        <h4 style="color:var(--accent-hover); margin:0;">Emma, 28</h4>
                        <p style="color:var(--text-secondary); margin:0; font-size:0.9rem;">Insomnia recovery</p>
                    </div>
                </div>
                <p style="color:var(--text-secondary);">"The insomnia that plagued me for years disappeared after just one session. I now fall asleep naturally and wake up refreshed. It's life-changing."</p>
                <div style="color:var(--accent); font-size:0.9rem;">★★★★★</div>
            </div>
        </div>
        
        <div style="background-color:var(--bg); padding:1.5rem; border-radius:8px; margin-top:2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color:var(--accent-hover);">Ready for Your Transformation?</h3>
            <p style="color:var(--text-secondary);">Book a free consultation to discuss how we can help you achieve similar results.</p>
            <a href="#book-now" style="background:var(--accent); color:white; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin-top:1rem; text-decoration:none;">Book Consultation</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG PAGE ---
elif selected == "Blog":
    st.markdown("""
    <div style="background-color:var(--card-bg); padding:2rem; border-radius:12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h2>Latest Articles</h2>
        <p style="color:var(--text-secondary);">Insights on hypnotherapy and mental wellbeing</p>
        
        <div style="display:grid; gap:2rem; margin:3rem 0;">
            <div style="border-bottom:1px solid var(--border); padding-bottom:2rem;">
                <h3 style="color:var(--accent-hover);">How Hypnosis Rewires Your Brain</h3>
                <p style="color:var(--text-secondary); font-size:0.9rem;">Published on May 15, 2023</p>
                <p style="color:var(--text-secondary);">The neuroscience behind why hypnotherapy works for habit change. Learn how hypnosis creates new neural pathways that support your desired changes.</p>
                <a href="#" style="color:var(--accent); font-weight:500; display:inline-block; margin-top:0.5rem;">Read more →</a>
            </div>
            
            <div style="border-bottom:1px solid var(--border); padding-bottom:2rem;">
                <h3 style="color:var(--accent-hover);">5 Signs You're Ready for Change</h3>
                <p style="color:var(--text-secondary); font-size:0.9rem;">Published on April 28, 2023</p>
                <p style="color:var(--text-secondary);">How to know when you're truly prepared to transform your habits. Recognizing these signs can help you succeed in your change journey.</p>
                <a href="#" style="color:var(--accent); font-weight:500; display:inline-block; margin-top:0.5rem;">Read more →</a>
            </div>
            
            <div style="padding-bottom:1rem;">
                <h3 style="color:var(--accent-hover);">Anxiety Relief Without Medication</h3>
                <p style="color:var(--text-secondary); font-size:0.9rem;">Published on March 10, 2023</p>
                <p style="color:var(--text-secondary);">Natural approaches to calm your nervous system. Discover how hypnotherapy can help regulate your stress response without drugs.</p>
                <a href="#" style="color:var(--accent); font-weight:500; display:inline-block; margin-top:0.5rem;">Read more →</a>
            </div>
        </div>
        
        <div style="background-color:var(--bg); padding:1.5rem; border-radius:8px; margin-top:2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color:var(--accent-hover);">Subscribe to Our Newsletter</h3>
            <p style="color:var(--text-secondary);">Get the latest articles and hypnotherapy tips delivered to your inbox.</p>
            
            <div style="display:flex; gap:1rem; margin-top:1rem;">
                <input type="email" placeholder="Your email address" style="flex:1; padding:0.8rem; border:1px solid var(--border); border-radius:8px;">
                <button style="background:var(--accent); color:white; border:none; padding:0 1.5rem; border-radius:8px; font-weight:500; cursor:pointer;">Subscribe</button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BOOK NOW PAGE ---
elif selected == "Book Now":
    st.markdown("""
    <div id="book-now" style="background-color:var(--card-bg); padding:2rem; border-radius:12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h2>Book Your Free Consultation</h2>
        <p style="color:var(--text-secondary);">30 minutes to discuss your goals and see if we're a good fit</p>
        
        <div style="display:flex; gap:3rem; margin-top:2rem;">
            <div style="flex:1;">
                <h3 style="color:var(--accent-hover);">What to Expect</h3>
                <ul style="color:var(--text-secondary); padding-left:1.2rem;">
                    <li>Confidential discussion of your concerns</li>
                    <li>Explanation of how hypnotherapy can help</li>
                    <li>Personalized recommendations</li>
                    <li>All your questions answered</li>
                    <li>No pressure or obligation</li>
                </ul>
                
                <div style="margin-top:2rem;">
                    <h3 style="color:var(--accent-hover);">Availability</h3>
                    <p style="color:var(--text-secondary);">Monday - Friday: 9am - 6pm</p>
                    <p style="color:var(--text-secondary);">Saturday: 10am - 2pm</p>
                </div>
            </div>
            
            <div style="flex:1;">
    """, unsafe_allow_html=True)

    with st.form("consultation_form", clear_on_submit=True):
        cols = st.columns(2)
        with cols[0]:
            name = st.text_input("Full Name*", key="book_name")
        with cols[1]:
            email = st.text_input("Email*", key="book_email")
        
        concern = st.selectbox(
            "Primary Concern*",
            ["Select one...", "Quit Smoking", "Anxiety Relief", "Sleep Improvement", "Weight Management", "Other"],
            key="book_concern"
        )
        
        message = st.text_area("What would you like to achieve through hypnotherapy?", key="book_message")
        
        submitted = st.form_submit_button("Submit Request")
        
        if submitted:
            if not all([name, email, concern != "Select one..."]):
                st.error("Please fill in all required fields")
            elif not is_valid_email(email):
                st.error("Please enter a valid email address")
            elif send_email(name, email, concern, message):
                st.success("Request sent successfully! We'll contact you within 24 hours to schedule your consultation.")
            else:
                st.error("There was an error submitting your request. Please try again.")

    st.markdown("""
            </div>
        </div>
        
        <div style="background-color:var(--bg); padding:1.5rem; border-radius:8px; margin-top:3rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color:var(--accent-hover);">Have Questions?</h3>
            <p style="color:var(--text-secondary);">Email us directly at <a href="mailto:contact@laetitiasheppard.com" style="color:var(--accent);">contact@laetitiasheppard.com</a> or call <a href="tel:+1234567890" style="color:var(--accent);">(123) 456-7890</a></p>
        </div>
    </div>
    """, unsafe_allow_html=True)