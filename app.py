import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import re

# --- CONSTANTS ---
SMTP_CONFIG = {
    "server": os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.environ.get("SMTP_PORT", 587)),
    "from_email": os.environ.get("EMAIL_FROM", "website@laetitiasheppard.com"),
    "to_email": os.environ.get("EMAIL_TO", "laetitiasheppard@gmail.com"),
    "username": os.environ.get("SMTP_USERNAME"),
    "password": os.environ.get("SMTP_PASSWORD")
}

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="2-Step Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UTILITY FUNCTIONS ---
def is_valid_email(email):
    """Validate email format using regex"""
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

def send_email(name, email, concern, message):
    """Send email with form data"""
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
    """Reset quiz state"""
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

def handle_quiz_answer(question_id, answer):
    """Store quiz answer and advance to next question"""
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1

# --- SESSION MANAGEMENT ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

# --- STYLING ---
st.markdown("""
<style>
:root {
    --bg: #F3F6F8;
    --card-bg: #FFFFFF;
    --text-primary: #273548;
    --text-secondary: #556D7A;
    --accent: #4CA1A3;
    --accent-hover: #3B7A7A;
    --border: #CBD5E1;
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
    --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --transition: all 0.3s ease;
}

/* Base styles */
html, body, .stApp {
    background-color: var(--bg) !important;
    color: var(--text-primary) !important;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Typography */
h1 {
    font-size: 2.2rem;
    line-height: 1.3;
    margin-bottom: 1.5rem;
}

h2 {
    font-size: 1.8rem;
    line-height: 1.3;
    margin-bottom: 1.2rem;
}

p, li {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--text-secondary);
    margin-bottom: 1rem;
}

/* Layout components */
.card {
    background: var(--card-bg);
    border-radius: var(--radius-md);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border);
    transition: var(--transition);
    margin-bottom: 1.5rem;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
}

.testimonial-card {
    border-left: 4px solid var(--accent);
}

.hero {
    background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
    padding: 3rem 2rem;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-sm);
}

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

/* Buttons */
.stButton>button {
    border-radius: var(--radius-sm) !important;
    transition: var(--transition) !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    cursor: pointer !important;
}

.stButton>button.primary,
.stButton>button[type="primary"],
.st-emotion-cache-1avcm0n.e1f1d6gn3,
button[data-testid="baseButton-primary"] {
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
}

.stButton>button.primary:hover,
.stButton>button[type="primary"]:hover,
.st-emotion-cache-1avcm0n.e1f1d6gn3:hover,
button[data-testid="baseButton-primary"]:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

.stButton>button:not(.primary):not([type="primary"]) {
    background-color: white !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border) !important;
}

.stButton>button:not(.primary):not([type="primary"]):hover {
    border-color: var(--accent) !important;
    color: var(--accent-hover) !important;
}

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

/* Form elements */
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

/* Utility classes */
.text-center {
    text-align: center;
}

.mb-2 {
    margin-bottom: 2rem;
}

.wave-divider {
    height: 15px;
    width: 100%;
    background: linear-gradient(90deg, var(--accent) 0%, var(--bg) 100%);
    opacity: 0.3;
    margin: 2rem 0;
}

/* Navigation */
.st-emotion-cache-1avcm0n {
    background-color: var(--bg) !important;
}

/* Footer */
.footer {
    margin: 4rem 0 2rem 0;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.5;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
}

.footer-founder {
    flex: 1 1 300px;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.footer-founder img {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--accent);
}

.footer-founder-text {
    max-width: 400px;
}

.footer-contact {
    flex: 1 1 260px;
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
    text-align: right;
}

.footer-contact p {
    margin: 0;
    color: var(--text-secondary);
}

.footer-button {
    margin-top: 0.5rem;
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
    padding: 0.5rem 1.2rem !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: var(--transition) !important;
    text-decoration: none !important;
    display: inline-block !important;
    font-size: 0.9rem !important;
}

.footer-button:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

.footer-copy {
    flex-basis: 100%;
    text-align: center;
    color: var(--text-secondary);
    font-size: 0.8rem;
    margin-top: 1.5rem;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    h1 {
        font-size: 1.8rem;
    }
    
    h2 {
        font-size: 1.5rem;
    }
    
    .hero {
        padding: 2rem 1rem;
    }
    
    .footer {
        flex-direction: column;
        gap: 1rem;
    }
    
    .footer-founder {
        flex-direction: column;
        text-align: center;
    }
    
    .footer-contact {
        text-align: center;
        align-items: center;
    }
    
    .footer-founder-text {
        max-width: 100%;
    }
    
    .card {
        padding: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
def create_navigation():
    """Create the top navigation menu"""
    return option_menu(
        menu_title=None,
        options=["Home", "Method", "Success", "Blog", "Book Now"],
        icons=["house", "magic", "stars", "book", "calendar"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "background-color": "#F3F6F8",
                "padding": "0",
                "margin": "0"
            },
            "nav-link": {
                "font-size": "16px",
                "font-weight": "400",
                "color": "#273548",
                "padding": "8px 16px",
                "transition": "all 0.3s ease",
            },
            "nav-link:hover": {
                "color": "#3B7A7A",
                "background-color": "rgba(76, 161, 163, 0.1)"
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "color": "white",
                "font-weight": "600",
                "border-bottom": "3px solid #3B7A7A"
            },
            "icon": {
                "color": "#4CA1A3",
                "font-size": "18px"
            },
            "icon-selected": {
                "color": "white"
            }
        }
    )

selected = create_navigation()

# --- HERO SECTION ---
def show_hero():
    """Display the hero section"""
    st.markdown("""
    <div class="hero">
        <h2>Break Free in Just 2 Sessions</h2>
        <p>Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits</p>
        <a href="#quiz" class="stButton cta-button">Take the 30-Second Quiz</a>
    </div>
    """, unsafe_allow_html=True)

show_hero()

# --- QUIZ COMPONENT ---
def show_quiz():
    """Display the quiz component"""
    st.markdown("""
    <div id="quiz" class="text-center mb-2">
        <h2>30-Second Suitability Quiz</h2>
        <p>Answer 3 questions to see if the method is right for you</p>
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
        <div class="card text-center">
            <h3>Based on your answers, our 2-session method would likely work well for you!</h3>
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
            <div class="text-center">
                <a href="#discovery" class="stButton cta-button">Book Consultation</a>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("Retake Quiz", key="retake_quiz"):
                reset_quiz()

# --- METHOD PAGE ---
def show_method_page():
    """Display the Method page content"""
    st.markdown("""
    <div class="text-center mb-2">
        <h2>Proven 2-Step Method</h2>
        <p>Why most clients achieve lasting change in just two sessions</p>
    </div>
    """, unsafe_allow_html=True)

    # Video Embed
    st.markdown("""
    <div class="card text-center">
        <div style="background:var(--border); height:315px; display:flex; align-items:center; justify-content:center; border-radius:8px;">
            <p>[Hypnotherapy Method Video]</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Method Steps
    steps = st.columns(3)
    step_data = [
        {
            "title": "Analysis Session",
            "items": [
                "Comprehensive evaluation",
                "Identify subconscious drivers",
                "Develop personalized plan",
                "Around 90 minutes in-person/Zoom"
            ]
        },
        {
            "title": "Transformation",
            "items": [
                "Guided hypnosis",
                "Create new neural pathways",
                "Anchor positive behaviors",
                "Around 90 minutes (3-7 days later)"
            ]
        },
        {
            "title": "Reinforcement",
            "items": [
                "Strengthen new patterns",
                "Address remaining blocks",
                "Typically not needed",
                "Around 60 minutes (optional)"
            ]
        }
    ]

    for i, step in enumerate(steps):
        with step:
            # Build the list items string first
            list_items = "".join([f"<li>{item}</li>" for item in step_data[i]["items"]])
            
            st.markdown(f"""
            <div class="card">
                <div style="background:{'var(--accent)' if i < 2 else 'var(--border)'}; color:var(--text-primary); 
                width:50px; height:50px; border-radius:50%; display:flex; align-items:center; 
                justify-content:center; font-weight:bold; margin:0 auto 1rem;">{i+1 if i < 2 else '+1'}</div>
                <h3 class="text-center">{step_data[i]['title']}</h3>
                <ul style="text-align:left;">
                    {list_items}
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Pricing
    st.markdown("""
    <div class="card">
        <h3 style="margin-top:0;">Pricing Options</h3>
        <p><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p><strong>Premium Package:</strong> 4000 THB (Includes optional reinforcement)</p>
        <p style="font-size:0.9rem;">Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES PAGE ---
def show_success_page():
    """Display the Success Stories page content"""
    st.markdown("""
    <div class="text-center mb-2">
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
        <div class="card testimonial-card">
            <div style="font-size:1.8rem; margin-bottom:0.5rem; color:var(--accent);">{t['icon']}</div>
            <p style="font-style:italic; font-size:1.1rem;">"{t['quote']}"</p>
            <p style="text-align:right; font-weight:600; margin-bottom:0;">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div class="text-center">
        <a href="#discovery" class="stButton cta-button">Book Your Session</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG PAGE ---
def show_blog_page():
    """Display the Blog page content"""
    st.markdown("""
    <div class="text-center mb-2">
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

# --- BOOK NOW PAGE ---
def show_booking_page():
    """Display the Book Now page content"""
    st.markdown("""
    <div class="text-center mb-2">
        <h2>Start Your Transformation</h2>
        <p>Choose your preferred booking option below</p>
    </div>
    """, unsafe_allow_html=True)

    # Booking options cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: var(--accent); text-align:center;">Free Discovery Call</h3>
            <p class="text-center">15-minute consultation to discuss your goals</p>
            <ul>
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
            <p class="text-center">Complete 2-session transformation</p>
            <ul>
                <li>Analysis Session (90 mins)</li>
                <li>Transformation Session (90 mins)</li>
                <li>Email support between sessions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Booking forms in tabs
    tab1, tab2 = st.tabs(["Free Discovery Call", "Rewiring Package"])

    with tab1:
        with st.form("discovery_form"):
            st.markdown("""
            <div class="text-center mb-2">
                <h3 style="color: var(--accent);">Free 15-Minute Discovery Call</h3>
                <p>No obligation consultation to discuss your goals</p>
            </div>
            """, unsafe_allow_html=True)

            cols = st.columns(2)
            with cols[0]:
                name = st.text_input("Your Name*", key="disc_name")
            with cols[1]:
                email = st.text_input("Email*", key="disc_email")

            concern = st.selectbox(
                "Primary Concern*",
                ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
                key="disc_concern"
            )

            submitted = st.form_submit_button("Book Discovery Call", type="primary")

            if submitted:
                if not name or not email or concern == "Select one...":
                    st.error("Please fill in all required fields")
                elif not is_valid_email(email):
                    st.error("Please enter a valid email address")
                else:
                    calendly_url = "https://calendly.com/laetitiasheppard/discovery"
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
                    if send_email(name, email, concern, "Booking type: Discovery Call"):
                        st.success("✓ Appointment scheduled!")
                    st.balloons()

    with tab2:
        with st.form("package_form"):
            st.markdown("""
            <div class="text-center mb-2">
                <h3 style="color: var(--accent);">Rewiring Package</h3>
                <p>Complete 2-session transformation program</p>
            </div>
            """, unsafe_allow_html=True)

            cols = st.columns(2)
            with cols[0]:
                name = st.text_input("Your Name*", key="pkg_name")
            with cols[1]:
                email = st.text_input("Email*", key="pkg_email")

            concern = st.selectbox(
                "Primary Concern*",
                ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Other"],
                key="pkg_concern"
            )

            submitted = st.form_submit_button("Book Package Now", type="primary")

            if submitted:
                if not name or not email or concern == "Select one...":
                    st.error("Please fill in all required fields")
                elif not is_valid_email(email):
                    st.error("Please enter a valid email address")
                else:
                    calendly_url = "https://calendly.com/laetitiasheppard/package"
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
                    if send_email(name, email, concern, "Booking type: Rewiring Package"):
                        st.success("✓ Package booked!")
                    st.balloons()

# --- BOOKING FORM ---
def show_booking_form():
    """Display the booking form section"""
    st.markdown("""
    <div id="discovery" class="card">
        <h2 style="color: var(--accent); text-align:center;">Free 15-Minute Discovery Call</h2>
        <p class="text-center">Begin your journey to transformation with a complimentary consultation</p>
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

        submitted = st.form_submit_button("Schedule My Free Call", type="primary")

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

    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
def show_footer():
    """Display the footer section"""
    st.markdown(f"""
    <div class="footer">
        <div class="footer-founder">
            <img src="https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true" alt="Laetitia Sheppard">
            <div class="footer-founder-text">
                <strong>Laetitia Sheppard</strong>  
                <br>Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.<br>
                Certified in Hypnotherapy & Cognitive Behavioural Therapy (LCCH, 2016) and Dialectical Behavioral Therapy (2023).
            </div>
        </div>

        <div class="footer-contact">
            <p><strong>Bangkok Hypnotherapy Clinic</strong></p>
            <p>27 Soi Sukhumvit 10 (Asoke), Bangkok, Thailand</p>
            <div>
                <a href="https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw" target="_blank" class="footer-button">Get Directions</a>
                <a href="https://calendly.com/laetitiasheppard/new-meeting" target="_blank" class="footer-button">Book Now</a>
            </div>
        </div>

        <div class="footer-copy">© {datetime.datetime.now().year} Laetitia Sheppard • All Rights Reserved • Confidentiality Guaranteed</div>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE CONTENT ---
if selected == "Home":
    show_quiz()
elif selected == "Method":
    show_method_page()
elif selected == "Success":
    show_success_page()
elif selected == "Blog":
    show_blog_page()
elif selected == "Book Now":
    show_booking_page()

# Show booking form on all pages except Book Now
if selected != "Book Now":
    show_booking_form()

show_footer()
