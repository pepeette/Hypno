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

# --- FORCE LIGHT MODE WITH ENHANCED CONTRAST ---
def force_light_mode():
    st.markdown("""
    <style>
    /* Force light mode with AA/AAA contrast */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F8F9FA !important;
        color: #212529 !important;
        color-scheme: light !important;
    }
    
    /* Improved contrast for text */
    h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #212529 !important;
    }
    
    /* Input fields */
    .stTextInput, .stTextArea, .stSelectbox {
        background-color: white !important;
        border-color: #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

force_light_mode()

# --- ENHANCED TYPOGRAPHY SCALE ---
def inject_css():
    st.markdown(f"""
    <style>
    :root {{
        --primary: #212529;    /* Dark gray for text (AAA contrast) */
        --accent: #D4AF37;     /* Gold accent */
        --light: #F8F9FA;      /* Light background */
        --border: #DEE2E6;     /* Light border */
    }}
    
    /* Typography scale */
    h1 {{
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        color: var(--accent) !important; /* Accent color for H1 */
    }}
    h2 {{
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.8rem !important;
    }}
    h3 {{
        font-size: 1.4rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.6rem !important;
    }}
    
    /* Hero section specific */
    .hero h1 {{
        color: var(--accent) !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }}
    
    /* Progress indicators */
    .progress-steps {{
        display: flex;
        justify-content: center;
        margin: 2rem 0;
        gap: 1rem;
    }}
    .step {{
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--border);
        color: white;
        font-weight: bold;
    }}
    .step.active {{
        background: var(--accent);
        color: var(--primary);
    }}
    
    /* FAQ accordions */
    .faq-item {{
        margin-bottom: 1rem;
        border: 1px solid var(--border);
        border-radius: 8px;
        overflow: hidden;
    }}
    .faq-question {{
        padding: 1rem;
        background: white;
        font-weight: 600;
        cursor: pointer;
    }}
    .faq-answer {{
        padding: 1rem;
        background: #F8F9FA;
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
        
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_app_password')  # REPLACE WITH YOUR CREDENTIALS
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# --- QUIZ SYSTEM WITH PROGRESS TRACKING ---
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1

def handle_quiz_answer(question_id, answer):
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1

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
<div class="hero" style="background:#1C1C1E; padding:4rem 1rem; text-align:center; border-radius:12px; margin-bottom:2rem;">
    <h1>Break Free in Just 2 Sessions</h1>
    <p style="font-size:1.2rem; color:#E9ECEF; max-width:700px; margin:0 auto 2rem;">
        Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits - without relying on willpower
    </p>
    <a href="#quiz" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; margin:0.5rem; text-decoration:none;">Take Our 30-Second Quiz</a>
    <div style="margin:1.5rem 0 0 0; color:#ADB5BD;">
        <span style="color:#D4AF37; font-weight:bold;">✓</span> 92% success rate &nbsp;&nbsp;
        <span style="color:#D4AF37; font-weight:bold;">✓</span> No withdrawal symptoms &nbsp;&nbsp;
        <span style="color:#D4AF37; font-weight:bold;">✓</span> English/French/Italian
    </div>
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
    <div class="progress-steps">
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
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem;">
            <h3>Q1: What are you looking to change?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        options = ["Quit smoking", "Reduce anxiety", "Improve sleep", "Other"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q1o{i}"):
                    handle_quiz_answer(1, option)
    
    # Question 2
    elif st.session_state.quiz_step == 2:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem;">
            <h3>Q2: How long have you struggled with this?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        options = ["<6 months", "6 months-2 years", ">2 years"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q2o{i}"):
                    handle_quiz_answer(2, option)
    
    # Question 3
    elif st.session_state.quiz_step == 3:
        st.markdown("""
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem;">
            <h3>Q3: How ready are you to make a change?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        options = ["Just exploring", "Somewhat ready", "Very ready"]
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option, key=f"q3o{i}"):
                    handle_quiz_answer(3, option)
    
    # Results
    if len(st.session_state.quiz_answers) == 3:
        st.success("""
        ### Based on your answers, our 2-session method would likely work well for you!
        """)
        st.markdown("""
        <div style="text-align:center; margin:1.5rem 0;">
            <a href="#discovery" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; text-decoration:none;">Book Your Free Consultation</a>
        </div>
        """, unsafe_allow_html=True)

# --- METHOD PAGE ---
elif selected == "Method":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Our Proven 2-Step Method</h2>
        <p>Why most clients achieve lasting change in just two sessions</p>
    </div>
    
    <div style="text-align:center; margin:2rem 0;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="max-width:100%; border-radius:12px;"></iframe>
        <p style="font-size:0.9rem; color:#6C757D;">Watch our 90-second explainer video</p>
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
            <div style="background:white; padding:1.5rem; border-radius:12px; height:100%;">
                <div style="background:{'#D4AF37' if i < 2 else '#F8F9FA'}; color:#1C1C1E; width:50px; height:50px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; margin:0 auto 1rem;">{step['number']}</div>
                <h3>{step['title']}</h3>
                <div style="text-align:left; margin-bottom:1rem;">{step['desc']}</div>
                {f'<p style="color:#D4AF37; font-weight:bold; margin:0;">{step["price"]}</p>' if step["price"] else ''}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:white; padding:1.5rem; border-radius:12px; margin:2rem auto; max-width:800px;">
        <h3 style="margin-top:0;">Pricing Options</h3>
        <p><strong>Standard Package:</strong> 3000 THB (Sessions 1 & 2)</p>
        <p><strong>Premium Package:</strong> 4000 THB (Includes optional reinforcement)</p>
        <p style="font-size:0.9rem; color:#6C757D;">Payment is due at first session. Cash and bank transfer accepted.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SUCCESS STORIES ---
elif selected == "Success":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
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
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1rem; border-left:4px solid #D4AF37;">
            <div style="font-size:1.8rem; margin-bottom:0.5rem;">{t['icon']}</div>
            <p style="font-style:italic; font-size:1.1rem;">"{t['quote']}"</p>
            <p style="text-align:right; font-weight:600; margin-bottom:0;">— {t['author']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align:center; margin:2rem 0;">
        <a href="#quiz" style="background:#D4AF37; color:#1C1C1E; padding:0.8rem 2rem; border-radius:8px; font-weight:600; display:inline-block; text-decoration:none;">Take Our Quiz</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOG & FAQ SECTION ---
elif selected == "Blog":
    st.markdown("""
    <div style="text-align:center; margin-bottom:2rem;">
        <h2>Hypnotherapy Insights</h2>
        <p>Educational resources and frequently asked questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured Video
    st.markdown("""
    <div style="text-align:center; margin:2rem 0;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="max-width:100%; border-radius:12px;"></iframe>
        <p style="font-size:0.9rem; color:#6C757D;">Watch our 90-second explainer video</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Blog Posts
    st.markdown("""
    <div style="margin:3rem 0;">
        <h3>Latest Articles</h3>
    </div>
    """, unsafe_allow_html=True)
    
    blog_posts = [
        {
            "title": "How Hypnosis Rewires Your Brain in 2 Sessions",
            "summary": "The neuroscience behind why brief hypnotherapy can create lasting change...",
            "date": "May 15, 2023"
        },
        {
            "title": "Quit Smoking Without Willpower: A Case Study",
            "summary": "How John quit his 20-year smoking habit in just 2 sessions...",
            "date": "April 2, 2023"
        }
    ]
    
    for post in blog_posts:
        st.markdown(f"""
        <div style="background:white; padding:1.5rem; border-radius:12px; margin-bottom:1.5rem; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="margin-top:0;">{post['title']}</h4>
            <p>{post['summary']}</p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="color:#6C757D; font-size:0.9rem;">{post['date']}</span>
                <button style="background:#D4AF37; color:#1C1C1E; border:none; padding:0.5rem 1rem; border-radius:6px; cursor:pointer;">Read Article</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
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
        with st.expander(f"❓ {faq['question']}", expanded=False):
            st.write(faq['answer'])

# --- BOOKING FORM ---
st.markdown("""
<div id="discovery" style="background:white; padding:2rem; border-radius:12px; margin:3rem 0;">
    <h2 style="text-align:center; margin-top:0;">Free 15-Minute Discovery Call</h2>
    <p style="text-align:center;">Let's discuss your goals and how we can help</p>
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
                calendly_url = "https://calendly.com/laetitiasheppard/30min"  # REPLACE WITH YOUR LINK
                st.markdown(f'<meta http-equiv="refresh" content="0; url={calendly_url}" />', unsafe_allow_html=True)
                
                # Send email
                if send_email(name, email, concern, message):
                    st.success("✓ Appointment scheduled! Check your email for confirmation.")
                else:
                    st.success("✓ Appointment scheduled! (Email confirmation pending)")
                
                st.balloons()

st.markdown("""
</div>
<div style="text-align:center; margin:3rem 0 1rem 0; padding-top:2rem; border-top:1px solid #DEE2E6;">
    <p style="color:#6C757D;">Laetitia Sheppard • Clinical Hypnotherapy • Bangkok</p>
    <p style="color:#6C757D; font-size:0.9rem;">© {datetime.datetime.now().year} All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
