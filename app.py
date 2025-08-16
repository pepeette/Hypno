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
/* FORCE LIGHT MODE */
:root {
    color-scheme: light;
}
html, body, [class*="st"] {
    color-scheme: light !important;
}
.stApp {
    background-color: var(--bg) !important;
    color: var(--text-primary) !important;
}

/* STRICT TYPOGRAPHY - ONLY 3 SIZES */
h1 {
    font-size: 2.2rem !important;
    line-height: 1.3 !important;
    margin-bottom: 1.5rem !important;
    color: var(--text-primary) !important;
}

h2 {
    font-size: 1.8rem !important;
    line-height: 1.3 !important;
    margin-bottom: 1.2rem !important;
    color: var(--text-primary) !important;
}

p, li, span, div, a, button, input, textarea, select, label, .text {
    font-size: 1rem !important;
    line-height: 1.6 !important;
    color: var(--text-secondary) !important;
}

/* Force all text to use one of these sizes */
* {
    font-size: inherit !important;
    line-height: inherit !important;
}

/* Convert all other headings to h2 size */
h3, h4, h5, h6 {
    font-size: 1.8rem !important;
}

/* Color variables for light mode */
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

/* STRICT TYPOGRAPHY - ONLY 3 SIZES */
h1 {
    font-size: 2.2rem !important;
    line-height: 1.3 !important;
    margin-bottom: 1.5rem !important;
    color: var(--text-primary) !important;
}

h2 {
    font-size: 1.8rem !important;
    line-height: 1.3 !important;
    margin-bottom: 1.2rem !important;
    color: var(--text-primary) !important;
}

p, li, span, div, a, button, input, textarea, select, label, .text {
    font-size: 1rem !important;
    line-height: 1.6 !important;
    color: var(--text-secondary) !important;
}

/* Force all text to use one of these sizes */
* {
    font-size: inherit !important;
    line-height: inherit !important;
}

/* Convert all other headings to h2 size */
h3, h4, h5, h6 {
    font-size: 1.8rem !important;
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
}

/* Buttons */
.stButton>button {
    border-radius: var(--radius-sm) !important;
    transition: var(--transition) !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    cursor: pointer !important;
}

.stButton>button.primary {
    background-color: var(--accent) !important;
    color: white !important;
    border: none !important;
}

.stButton>button.primary:hover {
    background-color: var(--accent-hover) !important;
    transform: translateY(-1px);
    box-shadow: var(--shadow-accent);
}

/* Form elements */
.stTextInput>div>div>input, 
.stSelectbox>div>div>select,
.stTextArea>div>textarea {
    background-color: white;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm);
    padding: 8px 12px;
}

/* Utility classes */
.text-center {
    text-align: center;
}

.mb-2 {
    margin-bottom: 2rem;
}

/* Navigation */
.st-emotion-cache-1avcm0n {
    background-color: var(--bg) !important;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    h1 {
        font-size: 1.8rem !important;
    }
    
    h2 {
        font-size: 1.5rem !important;
    }
    
    .hero {
        padding: 2rem 1rem;
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
            "container": {"padding": "0", "margin": "0"},
            "nav-link": {
                "font-size": "1rem",
                "padding": "8px 16px",
                "transition": "all 0.3s ease",
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "font-weight": "600",
                "border-bottom": "3px solid #3B7A7A"
            }
        }
    )

selected = create_navigation()

# --- HERO SECTION ---
def show_hero():
    """Display the hero section"""
    st.markdown("""
    <div class="hero">
        <h1>Break Free in Just 2 Sessions</h1>
        <p>Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits</p>
        <a href="#quiz" class="stButton primary">Take the 30-Second Quiz</a>
    </div>
    """, unsafe_allow_html=True)

show_hero()

# --- QUIZ COMPONENT ---
def calculate_suitability_score(answers):
    """Calculate suitability percentage based on quiz answers"""
    score = 0
    
    # Question 1: What are you looking to change? (0-40 points)
    concern_scores = {
        "Quit smoking": 40,
        "Reduce anxiety": 35,
        "Improve sleep": 30,
        "Break bad habits": 35,
        "Other": 25
    }
    score += concern_scores.get(answers.get(1, ""), 0)
    
    # Question 2: How long have you struggled? (0-30 points)
    duration_scores = {
        "Less than 6 months": 20,
        "6 months to 2 years": 25,
        "More than 2 years": 30,
        "Many years": 25
    }
    score += duration_scores.get(answers.get(2, ""), 0)
    
    # Question 3: How ready are you? (0-30 points)
    readiness_scores = {
        "Just exploring options": 10,
        "Somewhat ready": 20,
        "Very ready - I'm committed": 30,
        "Desperate for change": 25
    }
    score += readiness_scores.get(answers.get(3, ""), 0)
    
    return min(score, 100)  # Cap at 100%

def get_suitability_message(score):
    """Get message and color based on suitability score"""
    if score >= 85:
        return "Excellent candidate for hypnotherapy!", "#22c55e", "🌟"
    elif score >= 70:
        return "Very good fit for our 2-session method", "#65a30d", "✅"
    elif score >= 55:
        return "Good potential with hypnotherapy", "#eab308", "🎯"
    elif score >= 40:
        return "May benefit with additional preparation", "#f97316", "⚡"
    else:
        return "Consider a discovery call first", "#ef4444", "💬"

def show_quiz():
    """Display the enhanced quiz component"""
    
    # Quiz header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h1>30-Second Suitability Assessment</h1>
        <p style="font-size: 1.1rem; color: var(--text-secondary);">
            Discover your readiness for transformation in 3 quick questions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    current_step = st.session_state.quiz_step
    progress_percentage = min((current_step - 1) / 3 * 100, 100)
    
    st.markdown(f"""
    <div style="margin: 2rem 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <span style="font-weight: 600;">Question {min(current_step, 3)} of 3</span>
            <span style="font-weight: 600;">{int(progress_percentage)}% Complete</span>
        </div>
        <div style="background-color: var(--border); height: 8px; border-radius: 4px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, var(--accent) 0%, #22c55e 100%); 
                        height: 100%; width: {progress_percentage}%; transition: width 0.5s ease;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
            <div style="display: flex; align-items: center; gap: 0.3rem;">
                <div style="width: 8px; height: 8px; border-radius: 50%; 
                           background: {'var(--accent)' if current_step >= 1 else 'var(--border)'};"></div>
                Goal
            </div>
            <div style="display: flex; align-items: center; gap: 0.3rem;">
                <div style="width: 8px; height: 8px; border-radius: 50%; 
                           background: {'var(--accent)' if current_step >= 2 else 'var(--border)'};"></div>
                Duration
            </div>
            <div style="display: flex; align-items: center; gap: 0.3rem;">
                <div style="width: 8px; height: 8px; border-radius: 50%; 
                           background: {'var(--accent)' if current_step >= 3 else 'var(--border)'};"></div>
                Readiness
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Question content area
    st.markdown("""
    <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                border: 1px solid var(--border); min-height: 300px;">
    """, unsafe_allow_html=True)
    
    # Question 1
    if current_step == 1:
        st.markdown("### 🎯 What would you most like to change or improve?")
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        options = [
            ("🚭", "Quit smoking", "Break free from tobacco addiction"),
            ("😌", "Reduce anxiety", "Find calm and peace of mind"), 
            ("😴", "Improve sleep", "Get better, deeper rest"),
            ("🔄", "Break bad habits", "Change unwanted behaviors"),
            ("❓", "Other", "Something else I'd like to change")
        ]
        
        cols = st.columns(2)
        for i, (icon, option, desc) in enumerate(options):
            col = cols[i % 2]
            with col:
                if st.button(
 

# --- METHOD PAGE ---
def show_method_page():
    """Display the Method page content"""
    st.markdown("""
    <div class="text-center mb-2">
        <h1>Proven 2-Step Method</h1>
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
            list_items = "".join([f"<li>{item}</li>" for item in step_data[i]["items"]])
            st.markdown(f"""
            <div class="card">
                <div style="background:{'var(--accent)' if i < 2 else 'var(--border)'}; 
                width:50px; height:50px; border-radius:50%; display:flex; align-items:center; 
                justify-content:center; font-weight:bold; margin:0 auto 1rem;">{i+1 if i < 2 else '+1'}</div>
                <h2 class="text-center">{step_data[i]['title']}</h2>
                <ul style="text-align:left;">
                    {list_items}
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Pricing
    st.markdown("""
    <div class="card">
        <h2>Pricing Options</h2>
        <p><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p><strong>Premium Package:</strong> 4000 THB (Includes optional reinforcement)</p>
        <p>Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES PAGE ---
def show_success_page():
    """Display the Success Stories page content"""
    st.markdown("""
    <div class="text-center mb-2">
        <h1>Client Transformations</h1>
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
        }
    ]

    for t in testimonials:
        st.markdown(f"""
        <div class="card testimonial-card">
            <div style="font-size:1.8rem; margin-bottom:0.5rem; color:var(--accent);">{t['icon']}</div>
            <p style="font-style:italic;">"{t['quote']}"</p>
            <p style="text-align:right; font-weight:600; margin-bottom:0;">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="text-center">
        <a href="#discovery" class="stButton primary">Book Your Session</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG PAGE ---
def show_blog_page():
    """Display the Blog page content"""
    st.markdown("""
    <div class="text-center mb-2">
        <h1>Hypnotherapy Insights</h1>
        <p>Educational resources and frequently asked questions</p>
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <div style="margin:3rem 0;">
        <h2>Frequently Asked Questions</h2>
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
        <h1>Start Your Transformation</h1>
        <p>Choose your preferred booking option below</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="card">
            <h2>Free Discovery Call</h2>
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
            <h2>Rewiring Package</h2>
            <p class="text-center">Complete 2-session transformation</p>
            <ul>
                <li>Analysis Session (90 mins)</li>
                <li>Transformation Session (90 mins)</li>
                <li>Email support between sessions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Free Discovery Call", "Rewiring Package"])

    with tab1:
        with st.form("discovery_form"):
            st.markdown("""
            <div class="text-center mb-2">
                <h2>Free 15-Minute Discovery Call</h2>
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
                <h2>Rewiring Package</h2>
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
        <h1>Free 15-Minute Discovery Call</h1>
        <p class="text-center">Begin your journey to transformation with a complimentary consultation</p>
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

        message = st.text_area("Anything we should know", 
                             placeholder="Brief details about your situation")

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
                st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
def show_footer():
    """Display the responsive footer section using Streamlit native components"""
    # Add spacing before footer
    st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
    
    # Horizontal line separator
    st.markdown(f"""
    <div style="border-top: 1px solid var(--border); margin: 2rem 0;"></div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit columns for responsive layout
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        # Founder section with image and info
        subcol1, subcol2 = st.columns([1, 3], gap="medium")
        
        with subcol1:
            st.markdown(f"""
            <img src="https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true" 
                 alt="Laetitia Sheppard"
                 style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; 
                        border: 2px solid var(--accent); display: block;">
            """, unsafe_allow_html=True)
        
        with subcol2:
            st.markdown("## Laetitia Sheppard")
            st.markdown("Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.")
    
    with col2:
        st.markdown("## Contact")
        st.markdown("**Bangkok Hypnotherapy Clinic**")
        st.markdown("27 Soi Sukhumvit 10 (Asoke)")
        st.markdown("Bangkok, Thailand")
        
        # Buttons using Streamlit columns for mobile responsiveness
        btn_col1, btn_col2 = st.columns(2, gap="small")
        
        with btn_col1:
            st.markdown("""
            <a href="https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw" 
               target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white; 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                      font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
                      box-sizing: border-box; transition: var(--transition);">
                Directions
            </a>
            """, unsafe_allow_html=True)
        
        with btn_col2:
            st.markdown("""
            <a href="https://calendly.com/laetitiasheppard/new-meeting" 
               target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white; 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                      font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
                      box-sizing: border-box; transition: var(--transition);">
                Book Now
            </a>
            """, unsafe_allow_html=True)
    
    # Copyright section - full width
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="border-top: 1px solid var(--border); padding-top: 2rem; text-align: center;">
        <p>© {datetime.datetime.now().year} Laetitia Sheppard • All Rights Reserved</p>
        <p>Confidentiality Guaranteed</p>
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
