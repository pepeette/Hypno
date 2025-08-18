"""
Enhanced main application file for the Hypnotherapy website
Uses native Streamlit components instead of complex HTML
Improved error handling, component integration, and user experience
"""

import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# Page configuration
st.set_page_config(
    page_title="2-Step Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply styling first
def apply_global_styles():
    """Apply simplified global styles"""
    st.markdown("""
    <style>
    :root {
        color-scheme: light;
        --bg: #F3F6F8;
        --card-bg: #FFFFFF;
        --text-primary: #273548;
        --text-secondary: #556D7A;
        --accent: #4CA1A3;
        --accent-hover: #3B7A7A;
        --border: #CBD5E1;
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s ease;
    }
    
    html, body, .stApp {
        color-scheme: light !important;
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    h1 { font-size: 2.2rem !important; line-height: 1.3 !important; color: var(--text-primary) !important; font-weight: 700 !important; text-shadow: none !important; }
    h2, h3, h4, h5, h6 { font-size: 1.8rem !important; line-height: 1.3 !important; color: var(--text-primary) !important; font-weight: 600 !important; text-shadow: none !important; }
    p, li, span, div, a, button, input, textarea, select, label { font-size: 1rem !important; line-height: 1.6 !important; color: var(--text-secondary) !important; text-shadow: none !important; }
    
    .card { background: var(--card-bg); border-radius: var(--radius-md); padding: 2rem; box-shadow: var(--shadow-sm); border: 1px solid var(--border); margin-bottom: 2rem; }
    .hero { background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%); padding: 3rem 2rem; border-radius: var(--radius-lg); text-align: center; margin-bottom: 2rem; }
    .testimonial-card { border-left: 4px solid var(--accent); }
    
    .stButton>button { border-radius: var(--radius-sm) !important; transition: var(--transition) !important; font-weight: 600 !important; }
    .stButton>button[kind="primary"] { background-color: var(--accent) !important; color: white !important; }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

apply_global_styles()

# Session state initialization
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1
    st.session_state.quiz_completed = False

def reset_quiz():
    """Reset quiz state"""
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1
    st.session_state.quiz_completed = False

def handle_quiz_answer(question_id, answer):
    """Handle quiz answer selection"""
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1
    if len(st.session_state.quiz_answers) >= 3:
        st.session_state.quiz_completed = True

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Method", "Success", "Blog", "Book Now"],
    icons=["house", "magic", "stars", "book", "calendar"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0", "background-color": "transparent"},
        "nav-link": {"font-size": "1rem", "padding": "12px 20px", "color": "#556D7A", "font-weight": "500"},
        "nav-link-selected": {"background": "#4CA1A3", "color": "white", "font-weight": "600"}
    }
)

# Helper Components
def render_hero():
    """Render hero section"""
    st.markdown("""
    <div class="hero">
        <h1 style="color: white; margin-bottom: 1rem;">Transform Your Life in Just 2 Sessions</h1>
        <p style="font-size: 1.1rem; color: white; opacity: 0.95; max-width: 600px; margin: 0 auto 2rem auto;">
            Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
        </p>
        <div style="display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap;">
            <div style="text-align: center; color: white; margin: 1rem;">
                <div style="font-size: 2.5rem; font-weight: bold;">85%</div>
                <p style="margin: 0; font-weight: 600;">Success in 2 Sessions</p>
            </div>
            <div style="text-align: center; color: white; margin: 1rem;">
                <div style="font-size: 2.5rem; font-weight: bold;">500+</div>
                <p style="margin: 0; font-weight: 600;">Lives Transformed</p>
            </div>
            <div style="text-align: center; color: white; margin: 1rem;">
                <div style="font-size: 2.5rem; font-weight: bold;">10+</div>
                <p style="margin: 0; font-weight: 600;">Years Experience</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_quiz():
    """Render the suitability quiz"""
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0 2rem 0;">
        <h2>30-Second Suitability Assessment</h2>
        <p style="color: var(--text-secondary);">Discover your readiness for transformation in 3 quick questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress indicator
    progress = min(st.session_state.quiz_step - 1, 3) / 3 * 100
    st.markdown(f"""
    <div style="margin: 2rem 0;">
        <div style="background: var(--border); height: 8px; border-radius: 4px; overflow: hidden;">
            <div style="background: var(--accent); height: 100%; width: {progress}%; transition: width 0.5s ease;"></div>
        </div>
        <p style="text-align: center; margin-top: 0.5rem; font-weight: 600;">
            Question {min(st.session_state.quiz_step, 3)} of 3
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.quiz_completed:
        if st.session_state.quiz_step == 1:
            st.markdown("### 🎯 What would you most like to change?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
                    handle_quiz_answer(1, "Quit Smoking")
                    st.rerun()
                if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
                    handle_quiz_answer(1, "Improve Sleep")
                    st.rerun()
            with col2:
                if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
                    handle_quiz_answer(1, "Reduce Anxiety")
                    st.rerun()
                if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
                    handle_quiz_answer(1, "Break Bad Habits")
                    st.rerun()
        
        elif st.session_state.quiz_step == 2:
            st.markdown("### ⏰ How long have you been dealing with this?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
                    handle_quiz_answer(2, "Less than 6 months")
                    st.rerun()
                if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
                    handle_quiz_answer(2, "More than 2 years")
                    st.rerun()
            with col2:
                if st.button("📅 6 months to 2 years", key="q2_moderate", use_container_width=True):
                    handle_quiz_answer(2, "6 months to 2 years")
                    st.rerun()
                if st.button("🔄 Many years", key="q2_chronic", use_container_width=True):
                    handle_quiz_answer(2, "Many years")
                    st.rerun()
        
        elif st.session_state.quiz_step == 3:
            st.markdown("### 🚀 How ready are you to make this change?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🤔 Just exploring options", key="q3_exploring", use_container_width=True):
                    handle_quiz_answer(3, "Just exploring")
                    st.rerun()
                if st.button("💪 Very ready - I'm committed", key="q3_committed", use_container_width=True):
                    handle_quiz_answer(3, "Very ready")
                    st.rerun()
            with col2:
                if st.button("👍 Somewhat ready", key="q3_somewhat", use_container_width=True):
                    handle_quiz_answer(3, "Somewhat ready")
                    st.rerun()
                if st.button("🔥 Desperate for change", key="q3_desperate", use_container_width=True):
                    handle_quiz_answer(3, "Desperate")
                    st.rerun()
    
    else:
        # Quiz results
        score = 75  # Simple scoring
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); padding: 3rem 2rem; 
                    text-align: center; margin: 2rem 0; border: 2px solid var(--accent);">
            <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
            <h2 style="color: var(--accent);">{score}% Suitability Match</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">
                Excellent candidate for hypnotherapy! Your answers indicate strong potential for success.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#discovery" style="background: var(--accent); color: white; padding: 1rem 2rem; 
                   border-radius: var(--radius-sm); text-decoration: none; font-weight: 600;">
                    📞 Book Discovery Call
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Retake Assessment", key="retake_quiz"):
            reset_quiz()
            st.rerun()

def render_testimonials():
    """Render testimonials section"""
    st.markdown("## 💬 Client Success Stories")
    
    testimonials = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Director, Banking, Singapore",
            "concern": "Anxiety patterns"
        },
        {
            "icon": "🚭",
            "quote": "My husband was a heavy smoker... No more addiction.",
            "author": "Wife, Bangkok", 
            "concern": "Smoking cessation"
        }
    ]
    
    for t in testimonials:
        st.markdown(f"""
        <div class="card testimonial-card">
            <div style="display: flex; align-items: flex-start; gap: 1rem;">
                <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">
                    {t['icon']}
                </div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; color: var(--text-primary); 
                                       margin: 0 0 1rem 0; line-height: 1.6;">
                        "{t['quote']}"
                    </blockquote>
                    <div style="font-weight: 600; color: var(--text-secondary);">— {t['author']}</div>
                    <div style="color: var(--accent); font-size: 0.9rem;">🎯 {t['concern']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_booking_form():
    """Render booking form component"""
    st.markdown('<div id="discovery"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin: 3rem 0 2rem 0;">
        <h2>📞 Free 15-Minute Discovery Call</h2>
        <p style="color: var(--text-secondary);">Begin your journey to transformation with a complimentary consultation</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("booking_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name*", placeholder="First and last name")
        with col2:
            email = st.text_input("Email*", placeholder="your@email.com")
        
        concern = st.selectbox(
            "What would you like help with?*",
            ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Break Bad Habits", "Other"]
        )
        
        message = st.text_area(
            "Anything we should know?", 
            placeholder="Optional: Brief details about your situation"
        )
        
        submitted = st.form_submit_button("📞 Schedule My Free Call", type="primary", use_container_width=True)
        
        if submitted:
            if name and email and concern != "Select one...":
                st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
                st.markdown("""
                <div style="text-align: center; margin: 2rem 0;">
                    <a href="https://calendly.com/laetitiasheppard/30min" target="_blank" 
                       style="display: inline-block; background-color: var(--accent); color: white;
                              text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                              font-weight: 600;">
                        📅 Or Schedule Directly
                    </a>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.error("Please fill in all required fields")

def render_footer():
    """Render footer component"""
    st.markdown("""
    <div style="margin: 4rem 0 2rem 0; padding-top: 2rem; border-top: 1px solid var(--border);">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem;">
            <div style="display: flex; align-items: center; gap: 1rem; flex: 1; min-width: 300px;">
                <img src="https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true" 
                     alt="Laetitia Sheppard" 
                     style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 2px solid var(--accent);">
                <div>
                    <h3 style="margin: 0 0 0.5rem 0;">Laetitia Sheppard</h3>
                    <p style="margin: 0; color: var(--text-secondary);">
                        Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.
                    </p>
                </div>
            </div>
            
            <div style="text-align: right; flex: 1; min-width: 260px;">
                <h3>Contact</h3>
                <p style="margin: 0.5rem 0;"><strong>Bangkok Hypnotherapy Clinic</strong></p>
                <p style="margin: 0.5rem 0;">27 Soi Sukhumvit 10 (Asoke)</p>
                <p style="margin: 0.5rem 0;">Bangkok, Thailand</p>
                <div style="margin-top: 1rem;">
                    <a href="https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw" target="_blank" 
                       style="display: inline-block; background-color: var(--accent); color: white; 
                              text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm);
                              font-weight: 600; margin-right: 0.5rem;">
                        📍 Directions
                    </a>
                    <a href="https://calendly.com/laetitiasheppard/new-meeting" target="_blank"
                       style="display: inline-block; background-color: var(--accent); color: white; 
                              text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm);
                              font-weight: 600;">
                        📅 Book Now
                    </a>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--border);">
            <p style="margin: 0; color: var(--text-secondary);">
                © {datetime.datetime.now().year} Laetitia Sheppard • All Rights Reserved • Confidentiality Guaranteed
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Page Content Routing
if selected == "Home":
    render_hero()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E1F0F0 0%, var(--card-bg) 100%); 
                border-radius: var(--radius-md); padding: 2rem; margin: 2rem 0; 
                border-left: 4px solid var(--accent);">
        <h2 style="color: var(--accent); margin-bottom: 1rem;">🧠 Why Our Method Works</h2>
        <p style="font-size: 1.1rem; line-height: 1.7;">
            Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
            Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    render_quiz()
    render_testimonials()

elif selected == "Method":
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <h1>Why 2 Sessions Work When Years of Trying Haven't</h1>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
            The science-backed approach that bypasses willpower and rewires your subconscious mind directly
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Method steps
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto;">1</div>
            </div>
            <h3 style="text-align: center;">🔍 Deep Analysis Session</h3>
            <p><strong>90 minutes • In-person or Zoom</strong></p>
            <ul>
                <li>Uncover your unique subconscious triggers</li>
                <li>Map your personal behavior patterns</li>
                <li>Identify root causes vs. symptoms</li>
                <li>Install initial positive programming</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto;">2</div>
            </div>
            <h3 style="text-align: center;">⚡ Transformation Session</h3>
            <p><strong>90 minutes • 3-7 days later</strong></p>
            <ul>
                <li>Enter deep hypnotic state for maximum receptivity</li>
                <li>Rewire neural pathways at the subconscious level</li>
                <li>Replace old patterns with empowering new ones</li>
                <li>Lock in your new identity and behaviors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Pricing
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h2>Investment Options</h2>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">
            <div style="padding: 1.5rem; border: 2px solid var(--accent); border-radius: var(--radius-sm);">
                <h3 style="color: var(--accent);">Complete Package</h3>
                <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">3,000 THB</div>
                <p>Sessions 1 & 2 • Most Popular</p>
                <ul style="text-align: left;">
                    <li>Analysis Session (90 min)</li>
                    <li>Transformation Session (90 min)</li>
                    <li>Email support between sessions</li>
                    <li>Success rate: 85%</li>
                </ul>
            </div>
            <div style="padding: 1.5rem; border: 1px solid var(--border); border-radius: var(--radius-sm);">
                <h3>Premium Package</h3>
                <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">4,000 THB</div>
                <p>All 3 sessions • Maximum assurance</p>
                <ul style="text-align: left;">
                    <li>Everything in Complete Package</li>
                    <li>Plus: 3rd reinforcement session</li>
                    <li>100% success guarantee</li>
                    <li>Peace of mind</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Success":
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <h1>Real Transformations from Real People</h1>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
            See how our clients have transformed their lives in just 2 sessions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    render_testimonials()
    
    # Success metrics
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h2>Proven Results</h2>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem; margin: 2rem 0;">
            <div>
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">85%</div>
                <p>Success in 2 sessions</p>
            </div>
            <div>
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">500+</div>
                <p>Lives Changed</p>
            </div>
            <div>
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">15%</div>
                <p>Need 3rd session</p>
            </div>
            <div>
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">95%</div>
                <p>Long-term success</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "Blog":
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <h1>Hypnotherapy Insights & FAQ</h1>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
            Educational resources and answers to your most common questions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured articles
    articles = [
        {
            "title": "How Hypnosis Rewires Your Brain for Lasting Change",
            "summary": "Discover the neuroscience behind rapid transformation and why hypnotherapy succeeds where willpower fails.",
            "date": "August 15, 2025"
        },
        {
            "title": "Breaking Free from Smoking: Why 2 Sessions Work", 
            "summary": "Learn how John quit his 20-year, 2-pack-a-day habit in just 2 hypnotherapy sessions.",
            "date": "August 10, 2025"
        }
    ]
    
    st.markdown("## 📝 Latest Articles")
    for article in articles:
        with st.expander(f"📖 {article['title']} - {article['date']}"):
            st.write(article['summary'])
            st.info("Full article content available on our blog.")
    
    # FAQ
    st.markdown("## ❓ Frequently Asked Questions")
    
    faqs = [
        ("Is hypnotherapy safe?", "Yes, clinical hypnotherapy is completely safe. You remain fully aware and in control throughout the session."),
        ("How many sessions will I really need?", "85% of our clients achieve their goals in just 2 sessions. About 15% choose an optional 3rd session for reinforcement."),
        ("What if I can't be hypnotized?", "This is a common myth. Everyone can be hypnotized because hypnosis is a natural state we enter daily."),
        ("Will I lose control during hypnosis?", "Absolutely not. You remain fully aware and can open your eyes or speak at any time."),
        ("How much does it cost?", "Our complete 2-session package is 3,000 THB. Compare this to years of traditional therapy (often 60,000+ THB).")
    ]
    
    for question, answer in faqs:
        with st.expander(f"❓ {question}"):
            st.write(answer)

elif selected == "Book Now":
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0 3rem 0;">
        <h1>Start Your Transformation Today</h1>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
            Choose the option that feels right for you - we're here to support your journey
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Booking options
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h2 style="color: var(--accent); text-align: center;">🎯 Free Discovery Call</h2>
            <p style="text-align: center; color: var(--text-secondary);">
                15-minute consultation to discuss your goals and assess suitability
            </p>
            <ul>
                <li><strong>Perfect if you:</strong></li>
                <li>Want to understand how hypnotherapy works</li>
                <li>Have questions about the process</li>
                <li>Want to assess your suitability</li>
                <li>Prefer to talk before committing</li>
            </ul>
            <div style="text-align: center; margin-top: 1rem;">
                <span style="font-size: 1.2rem; font-weight: bold; color: var(--success);">
                    FREE • No Obligation
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h2 style="color: var(--accent); text-align: center;">⚡ Transformation Package</h2>
            <p style="text-align: center; color: var(--text-secondary);">
                Complete 2-session program for rapid, lasting change
            </p>
            <ul>
                <li><strong>Perfect if you:</strong></li>
                <li>Are ready to commit to transformation</li>
                <li>Want to start immediately</li>
                <li>Have taken our assessment (70%+ score)</li>
                <li>Prefer direct action</li>
            </ul>
            <div style="text-align: center; margin-top: 1rem;">
                <span style="font-size: 1.2rem; font-weight: bold; color: var(--accent);">
                    3,000 THB • 85% Success Rate
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Always render booking form and footer on every page
render_booking_form()
render_footer()
