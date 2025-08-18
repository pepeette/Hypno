# """
# Clean main application - proper architecture, no double rendering
# """
# import streamlit as st
# from streamlit_option_menu import option_menu

# # ===== IMPORT STYLING FIRST =====
# def apply_global_styles():
#     """Apply clean, consistent styling - 3 font sizes only"""
#     st.markdown("""
#     <style>
#     /* FORCE LIGHT MODE */
#     :root { color-scheme: light !important; }
#     html, body, [class*="st"] { color-scheme: light !important; }
#     .stApp { background-color: #F3F6F8 !important; color: #273548 !important; }
    
#     /* VARIABLES */
#     :root {
#         --bg: #F3F6F8; --card-bg: #FFFFFF; --text-primary: #273548;
#         --text-secondary: #556D7A; --accent: #4CA1A3; --accent-hover: #3B7A7A;
#         --border: #CBD5E1; --success: #22c55e; --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
#         --radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --transition: all 0.3s ease;
#     }
    
#     /* STRICT TYPOGRAPHY - 3 SIZES ONLY, NO SHADOWS */
#     h1 { font-size: 1.875rem !important; color: var(--text-primary) !important; 
#          font-weight: 700 !important; text-shadow: none !important; margin-bottom: 1.5rem !important; }
#     h2, h3, h4, h5, h6 { font-size: 1.5rem !important; color: var(--text-primary) !important; 
#                          font-weight: 600 !important; text-shadow: none !important; margin-bottom: 1.2rem !important; }
#     p, li, span, div, a, button, input, textarea, select, label, .stMarkdown, .stText { 
#         font-size: 1rem !important; color: var(--text-secondary) !important; 
#         text-shadow: none !important; line-height: 1.6 !important; }
    
#     /* BUTTONS */
#     .stButton>button { border-radius: var(--radius-sm) !important; font-weight: 600 !important;
#                        padding: 0.75rem 2rem !important; border: none !important; font-size: 1rem !important; }
#     .stButton>button[kind="primary"] { background-color: var(--accent) !important; color: white !important; }
#     .stButton>button[kind="primary"]:hover { background-color: var(--accent-hover) !important; }
    
#     /* CARDS */
#     .card { background: var(--card-bg); border-radius: var(--radius-md); padding: 2rem;
#             box-shadow: var(--shadow-sm); border: 1px solid var(--border); margin-bottom: 2rem; }
    
#     /* METRICS */
#     .stMetric { background: var(--card-bg); border-radius: var(--radius-sm); 
#                 padding: 1rem; border: 1px solid var(--border); text-align: center; }
#     .stMetric [data-testid="metric-value"] { font-size: 2rem !important; 
#                                             font-weight: 700 !important; color: var(--accent) !important; }
    
#     /* HIDE STREAMLIT BRANDING */
#     #MainMenu, footer, header { visibility: hidden; }
#     </style>
#     """, unsafe_allow_html=True)

# # ===== PAGE CONFIG =====
# st.set_page_config(
#     page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Apply styling immediately
# apply_global_styles()

# # ===== SESSION STATE INITIALIZATION =====
# def initialize_session_state():
#     """Initialize all session state variables"""
#     defaults = {
#         'quiz_answers': {},
#         'quiz_step': 1,
#         'quiz_completed': False,
#         'quiz_score': 0,
#         'form_submitted': False,
#         'current_page': 'Home'
#     }
    
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# initialize_session_state()

# # ===== NAVIGATION =====
# def create_navigation():
#     """Create main navigation menu"""
#     return option_menu(
#         menu_title=None,
#         options=["Home", "Method", "Success", "Blog", "Book Now"],
#         icons=["house", "gear", "star", "book", "calendar"],
#         default_index=0,
#         orientation="horizontal",
#         styles={
#             "container": {
#                 "background-color": "#F0FDFA",
#                 "border-radius": "12px",
#                 "padding": "0",
#                 "margin": "0 0 2rem 0"
#             },
#             "nav-link": {
#                 "font-size": "1rem",
#                 "color": "#556D7A",
#                 "font-weight": "500",
#                 "padding": "12px 20px",
#                 "border-radius": "8px"
#             },
#             "nav-link-selected": {
#                 "background": "#4CA1A3",
#                 "color": "white",
#                 "font-weight": "600"
#             }
#         }
#     )

# # ===== PAGE COMPONENTS =====

# class HeroSection:
#     """Clean hero section"""
#     def render(self):
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                     border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#             <h1 style="color: white;">Transform Your Life in Just 2 Sessions</h1>
#             <p style="color: white; opacity: 0.95; max-width: 600px; margin: 0 auto;">
#                 Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("Success Rate", "85%", "in 2 sessions")
#         with col2:
#             st.metric("Lives Changed", "500+", "since 2017")
#         with col3:
#             st.metric("Experience", "10+ years", "certified")

# class QuizSection:
#     """Simple, engaging quiz"""
#     def render(self):
#         st.markdown("---")
#         st.markdown("## 🎯 30-Second Suitability Assessment")
#         st.write("Discover your potential for rapid transformation in 3 quick questions")
        
#         # Progress bar
#         if st.session_state.quiz_step > 1:
#             progress = min((st.session_state.quiz_step - 1) / 3 * 100, 100)
#             st.progress(progress / 100)
#             st.write(f"Question {min(st.session_state.quiz_step, 3)} of 3")
        
#         if not st.session_state.quiz_completed:
#             self._render_question()
#         else:
#             self._render_results()
    
#     def _render_question(self):
#         if st.session_state.quiz_step == 1:
#             st.markdown("### 🎯 What would you most like to change?")
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
#                     self._answer(1, "Quit Smoking")
#                 if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
#                     self._answer(1, "Improve Sleep")
#             with col2:
#                 if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
#                     self._answer(1, "Reduce Anxiety")
#                 if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
#                     self._answer(1, "Break Bad Habits")
        
#         elif st.session_state.quiz_step == 2:
#             st.markdown("### ⏰ How long have you been dealing with this?")
#             if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
#                 self._answer(2, "Less than 6 months")
#             if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
#                 self._answer(2, "6 months to 2 years")
#             if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
#                 self._answer(2, "More than 2 years")
        
#         elif st.session_state.quiz_step == 3:
#             st.markdown("### 🚀 How ready are you to make this change?")
#             if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
#                 self._answer(3, "Just exploring")
#             if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
#                 self._answer(3, "Very ready")
#             if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
#                 self._answer(3, "Desperate for change")
    
#     def _answer(self, q_id, answer):
#         st.session_state.quiz_answers[q_id] = answer
#         if q_id < 3:
#             st.session_state.quiz_step += 1
#         else:
#             st.session_state.quiz_completed = True
#             st.session_state.quiz_score = self._calculate_score()
#         st.rerun()
    
#     def _calculate_score(self):
#         scoring = {
#             1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
#             2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
#             3: {"Just exploring": 10, "Very ready": 30, "Desperate for change": 25}
#         }
        
#         total = 0
#         for q_id, answer in st.session_state.quiz_answers.items():
#             if q_id in scoring and answer in scoring[q_id]:
#                 total += scoring[q_id][answer]
#         return min(total, 100)
    
#     def _render_results(self):
#         score = st.session_state.quiz_score
        
#         if score >= 70:
#             message, color, icon = "Excellent candidate for hypnotherapy!", "#22c55e", "🌟"
#         elif score >= 55:
#             message, color, icon = "Good potential with hypnotherapy", "#eab308", "🎯"
#         else:
#             message, color, icon = "A discovery call would help determine the best approach", "#ef4444", "💬"
        
#         st.markdown(f"""
#         <div style="background: var(--card-bg); border-radius: 12px; padding: 3rem 2rem; 
#                     text-align: center; border: 2px solid {color}; margin: 2rem 0;">
#             <div style="font-size: 3rem;">{icon}</div>
#             <div style="font-size: 3rem; font-weight: bold; color: {color};">{score}%</div>
#             <h2>Suitability Match</h2>
#             <p>{message}</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("🔄 Retake Assessment", use_container_width=True):
#                 st.session_state.quiz_answers = {}
#                 st.session_state.quiz_step = 1
#                 st.session_state.quiz_completed = False
#                 st.rerun()
#         with col2:
#             if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
#                 st.success("Great choice! Scroll down to book your call.")

# class MethodBenefits:
#     """Why our method works"""
#     def render(self):
#         st.markdown("---")
#         st.markdown("## 🧠 Why Our Method Works When Others Don't")
        
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #E1F0F0 0%, var(--card-bg) 100%); 
#                     border-radius: 12px; padding: 2rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
#             <p style="font-size: 1.1rem; line-height: 1.7;">
#                 Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
#                 Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div class="card">
#                 <h2 style="color: var(--accent); text-align: center;">❌ Traditional Methods</h2>
#                 <p>• Fight against your programming</p>
#                 <p>• Require constant willpower</p>
#                 <p>• 95% relapse rate</p>
#                 <p>• Take months or years</p>
#                 <p>• Focus on symptoms only</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown("""
#             <div class="card">
#                 <h2 style="color: var(--accent); text-align: center;">✅ Our 2-Session Method</h2>
#                 <p>• Rewires your subconscious programming</p>
#                 <p>• Works with natural neural patterns</p>
#                 <p>• 85% success rate in 2 sessions</p>
#                 <p>• Results in just 2 weeks</p>
#                 <p>• Addresses the root cause</p>
#             </div>
#             """, unsafe_allow_html=True)

# class BookingForm:
#     """Simple booking form component"""
#     def render(self):
#         st.markdown("---")
#         st.markdown("## 📞 Book Your Free Discovery Call")
#         st.write("Begin your transformation with a complimentary 15-minute consultation")
        
#         with st.form("booking_form"):
#             col1, col2 = st.columns(2)
#             with col1:
#                 name = st.text_input("Your Name*", placeholder="First and last name")
#             with col2:
#                 email = st.text_input("Email*", placeholder="your@email.com")
            
#             concern = st.selectbox(
#                 "What would you like help with?*",
#                 ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Break Bad Habits", "Other"]
#             )
            
#             message = st.text_area(
#                 "Tell us about your situation (optional)",
#                 placeholder="Any specific details or questions"
#             )
            
#             submitted = st.form_submit_button("📞 Schedule My Free Call", type="primary", use_container_width=True)
            
#             if submitted:
#                 if name and email and concern != "Select one...":
#                     st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
#                     st.balloons()
#                 else:
#                     st.error("Please fill in all required fields")

# class Footer:
#     """Simple footer component"""
#     def render(self):
#         st.markdown("---")
        
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             col_img, col_text = st.columns([1, 3])
#             with col_img:
#                 st.image("https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true", width=100)
#             with col_text:
#                 st.markdown("### Laetitia Sheppard")
#                 st.write("Certified Clinical Hypnotherapist")
#                 st.write("LCCH Certified 2017 • DBT Certified 2023")
#                 st.write("10+ years experience")
        
#         with col2:
#             st.markdown("### Contact")
#             st.write("**Bangkok Hypnotherapy Clinic**")
#             st.write("27 Soi Sukhumvit 10 (Asoke)")
#             st.write("Bangkok, Thailand")
            
#             if st.button("📍 Get Directions", use_container_width=True):
#                 st.markdown("[Open Maps](https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw)")
#             if st.button("📅 Book Now", use_container_width=True):
#                 st.markdown("[Schedule Call](https://calendly.com/laetitiasheppard/new-meeting)")
        
#         st.markdown("""
#         <div style="text-align: center; margin-top: 2rem; color: var(--text-secondary);">
#             © 2025 Laetitia Sheppard • All Rights Reserved • Confidentiality Guaranteed
#         </div>
#         """, unsafe_allow_html=True)

# # ===== PAGE CONTENT FUNCTIONS =====

# def render_home_page():
#     """Render home page - Hero + Quiz + Method Benefits only"""
#     hero = HeroSection()
#     quiz = QuizSection()
#     benefits = MethodBenefits()
    
#     hero.render()
#     quiz.render()
#     benefits.render()

# def render_method_page():
#     """Render method page"""
#     st.title("Our Proven 2-Session Method")
#     st.write("Why 2 sessions work when years of trying haven't")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("### 🔍 Session 1: Analysis")
#         st.write("90 minutes • In-person or online")
#         st.write("• Uncover subconscious triggers")
#         st.write("• Map behavior patterns")
#         st.write("• Identify root causes")
#         st.write("• Begin positive programming")
    
#     with col2:
#         st.markdown("### ⚡ Session 2: Transformation")
#         st.write("90 minutes • 3-7 days later")
#         st.write("• Deep hypnotic state")
#         st.write("• Rewire neural pathways")
#         st.write("• Install new patterns")
#         st.write("• Lock in transformation")
    
#     st.markdown("---")
#     st.markdown("## 💰 Investment Options")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric("Complete Package", "3,000 THB", "Sessions 1 & 2")
#     with col2:
#         st.metric("Premium Package", "4,000 THB", "All 3 sessions")

# def render_success_page():
#     """Render success stories page"""
#     st.title("Real Transformations from Real People")
    
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Success Rate", "85%", "in 2 sessions")
#     with col2:
#         st.metric("Practice Since", "2017", "8 years experience")
#     with col3:
#         st.metric("Client Satisfaction", "High", "positive feedback")
    
#     testimonials = [
#         ("🌟 Banking Director - Singapore", "Performance anxiety → Complete confidence in 2 sessions"),
#         ("🚭 Heavy Smoker - Bangkok", "2 packs/day for 20 years → Completely smoke-free"),
#         ("🎓 Medical Student - Morocco", "Failing due to stress → Excelling in specialization")
#     ]
    
#     for title, result in testimonials:
#         with st.expander(title):
#             st.write(result)

# def render_blog_page():
#     """Render blog/FAQ page"""
#     st.title("Frequently Asked Questions")
    
#     faqs = [
#         ("Is hypnotherapy safe?", "Yes, completely safe. You remain fully aware and in control."),
#         ("How many sessions will I need?", "85% achieve goals in 2 sessions. 15% opt for a 3rd."),
#         ("What if I can't be hypnotized?", "Everyone can be hypnotized - it's a natural state."),
#         ("How much does it cost?", "Complete package: 3,000 THB for 2 sessions.")
#     ]
    
#     for question, answer in faqs:
#         with st.expander(f"❓ {question}"):
#             st.write(answer)

# def render_booking_page():
#     """Render booking page"""
#     st.title("Start Your Transformation Today")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("### 📞 Free Discovery Call")
#         st.write("15-minute consultation")
#         st.write("• No obligation")
#         st.write("• Learn how it works")
#         st.write("• Get questions answered")
    
#     with col2:
#         st.markdown("### ⚡ Transformation Package")
#         st.write("Complete 2-session program")
#         st.write("• Analysis Session (90 min)")
#         st.write("• Transformation Session (90 min)")
#         st.write("• 85% success rate")

# # ===== MAIN APP =====

# def main():
#     """Main application"""
#     # Navigation
#     selected_page = create_navigation()
#     st.session_state.current_page = selected_page
    
#     # Render selected page
#     if selected_page == "Home":
#         render_home_page()
#     elif selected_page == "Method":
#         render_method_page()
#     elif selected_page == "Success":
#         render_success_page()
#     elif selected_page == "Blog":
#         render_blog_page()
#     elif selected_page == "Book Now":
#         render_booking_page()
    
#     # Always show booking form and footer
#     booking_form = BookingForm()
#     booking_form.render()
    
#     footer = Footer()
#     footer.render()

# if __name__ == "__main__":
#     main()


"""
Improved Home page component - More compelling and clear content
"""
import streamlit as st

class HeroSection:
    """Compelling hero section with clear value proposition"""
    
    def render(self):
        """Render hero section with better messaging"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
            <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto 2rem auto; font-size: 1.1rem;">
                Most people try to change using willpower. That's why 95% fail. 
                We bypass your conscious resistance and reprogram your subconscious patterns directly.
            </p>
            <div style="background: rgba(255,255,255,0.2); border-radius: 12px; padding: 1.5rem; margin: 2rem auto; max-width: 500px;">
                <p style="color: white; margin: 0; font-weight: 600; font-size: 1.1rem;">
                    Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

class QuizSection:
    """Improved quiz with clear question numbers and better flow"""
    
    def __init__(self):
        # Initialize session state
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        if 'quiz_step' not in st.session_state:
            st.session_state.quiz_step = 1
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
    
    def render(self):
        """Render the complete quiz section"""
        st.markdown("## Find Out If You're Ready for Rapid Change")
        st.write("Three quick questions to assess your potential for transformation:")
        
        if not st.session_state.quiz_completed:
            self._render_all_questions()
        else:
            self._render_results()
    
    def _render_all_questions(self):
        """Show all 3 questions with clear numbering"""
        current_step = st.session_state.quiz_step
        
        # Question 1
        self._render_question_container(
            1, 
            "What would you most like to change?",
            [
                ("Quit Smoking", "Break free from tobacco addiction"),
                ("Reduce Anxiety", "Find calm and peace of mind"), 
                ("Improve Sleep", "Get better, deeper rest"),
                ("Break Bad Habits", "Change unwanted behaviors")
            ],
            current_step == 1
        )
        
        # Question 2 (show only if Q1 answered)
        if len(st.session_state.quiz_answers) >= 1:
            self._render_question_container(
                2,
                "How long have you been dealing with this?",
                [
                    ("Less than 6 months", "Relatively new challenge"),
                    ("6 months to 2 years", "Moderate duration"),
                    ("More than 2 years", "Long-standing pattern")
                ],
                current_step == 2
            )
        
        # Question 3 (show only if Q2 answered)
        if len(st.session_state.quiz_answers) >= 2:
            self._render_question_container(
                3,
                "How ready are you to make this change?",
                [
                    ("Just exploring options", "Learning about possibilities"),
                    ("Very ready - I'm committed", "Fully motivated to change"),
                    ("Desperate for change", "Need transformation now")
                ],
                current_step == 3
            )
        
        # Progress indicator
        progress = len(st.session_state.quiz_answers) / 3 * 100
        if progress > 0:
            st.progress(progress / 100)
            st.write(f"Question {len(st.session_state.quiz_answers) + 1} of 3" if len(st.session_state.quiz_answers) < 3 else "Complete!")
    
    def _render_question_container(self, question_num, title, options, is_active):
        """Render individual question container"""
        # Determine container style based on state
        if is_active:
            container_style = "background: var(--card-bg); border: 2px solid var(--accent); border-radius: 12px; padding: 2rem; margin: 1.5rem 0;"
        elif question_num in st.session_state.quiz_answers:
            container_style = "background: rgba(76, 161, 163, 0.05); border: 1px solid var(--accent); border-radius: 12px; padding: 2rem; margin: 1.5rem 0; opacity: 0.7;"
        else:
            container_style = "background: #f8f9fa; border: 1px solid var(--border); border-radius: 12px; padding: 2rem; margin: 1.5rem 0; opacity: 0.5;"
        
        st.markdown(f"""
        <div style="{container_style}">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                <div style="background: var(--accent); color: white; width: 40px; height: 40px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.2rem;">
                    {question_num}
                </div>
                <h2 style="margin: 0; color: var(--text-primary);">{title}</h2>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Show options only for active question
        if is_active:
            if question_num <= 2:
                # 2-column layout for first two questions
                col1, col2 = st.columns(2)
                for i, (option, description) in enumerate(options):
                    col = col1 if i % 2 == 0 else col2
                    with col:
                        if st.button(f"{option}", key=f"q{question_num}_{i}", use_container_width=True):
                            self._answer_question(question_num, option)
            else:
                # Single column for last question
                for i, (option, description) in enumerate(options):
                    if st.button(f"{option}", key=f"q{question_num}_{i}", use_container_width=True):
                        self._answer_question(question_num, option)
        
        # Show selected answer if answered
        elif question_num in st.session_state.quiz_answers:
            selected = st.session_state.quiz_answers[question_num]
            st.success(f"✅ Selected: {selected}")
    
    def _answer_question(self, question_id, answer):
        """Handle question answer"""
        st.session_state.quiz_answers[question_id] = answer
        if question_id < 3:
            st.session_state.quiz_step = question_id + 1
        else:
            st.session_state.quiz_completed = True
            st.session_state.quiz_score = self._calculate_score()
        st.rerun()
    
    def _calculate_score(self):
        """Calculate suitability score"""
        scoring = {
            1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
            2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
            3: {"Just exploring options": 10, "Very ready - I'm committed": 30, "Desperate for change": 25}
        }
        
        total_score = 0
        for q_id, answer in st.session_state.quiz_answers.items():
            if q_id in scoring and answer in scoring[q_id]:
                total_score += scoring[q_id][answer]
        
        return min(total_score, 100)
    
    def _render_results(self):
        """Render quiz results"""
        score = st.session_state.quiz_score
        
        # Determine message based on score
        if score >= 70:
            message = "Excellent candidate! You have strong indicators for rapid transformation."
            color = "#22c55e"
            icon = "🌟"
            recommendation = "You're ready to book your transformation package or start with a discovery call."
        elif score >= 55:
            message = "Good potential! Hypnotherapy can definitely help with the right approach."
            color = "#eab308"
            icon = "🎯"
            recommendation = "A discovery call would help us create the perfect strategy for your situation."
        else:
            message = "Let's talk! Every situation is unique, and a conversation will help us determine the best path forward."
            color = "#4CA1A3"
            icon = "💬"
            recommendation = "A free discovery call will help us understand how to best support your goals."
        
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 3rem 2rem; 
                    text-align: center; border: 2px solid {color}; margin: 2rem 0;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <div style="font-size: 3rem; font-weight: bold; color: {color}; margin-bottom: 0.5rem;">
                {score}%
            </div>
            <h2 style="margin-bottom: 1rem;">Transformation Readiness</h2>
            <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem;">
                {message}
            </p>
            <p style="color: var(--text-primary); font-weight: 600;">
                {recommendation}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                self._reset_quiz()
        with col2:
            if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
                st.success("Perfect! Scroll down to book your call.")
    
    def _reset_quiz(self):
        """Reset quiz state"""
        st.session_state.quiz_answers = {}
        st.session_state.quiz_step = 1
        st.session_state.quiz_completed = False
        st.session_state.quiz_score = 0
        st.rerun()

class PatternChangeMethod:
    """Why pattern change hypnotherapy works"""
    
    def render(self):
        """Render method explanation with compelling content"""
        st.markdown("## Pattern Change Hypnotherapy: Why It Works")
        
        # Opening explanation
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, var(--card-bg) 100%); 
                    border-radius: 12px; padding: 2rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
            <p style="font-size: 1.1rem; line-height: 1.7; margin-bottom: 1rem;">
                Every unwanted behavior is driven by subconscious patterns you learned years ago. 
                Traditional therapy tries to override these patterns with willpower. We change the patterns themselves.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.7; margin: 0;">
                When your subconscious programming supports your goals instead of fighting them, 
                change becomes effortless and permanent.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Success rate callout
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 2rem; 
                    text-align: center; border: 2px solid var(--success); margin: 2rem 0;">
            <h2 style="color: var(--success); margin-bottom: 1rem;">85% Success Rate in Just 2 Sessions</h2>
            <p style="font-size: 1.1rem; margin-bottom: 1rem;">
                Most clients achieve complete transformation in two 90-minute sessions. 
                About 15% choose an optional reinforcement session a few weeks later for additional confidence.
            </p>
            <p style="color: var(--text-secondary); margin: 0;">
                Compare this to traditional therapy, which typically requires months or years of ongoing sessions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Method comparison
        st.markdown("### The Difference Is in the Approach")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: #fee2e2; border-radius: 12px; padding: 2rem; border-left: 4px solid #ef4444;">
                <h2 style="color: #dc2626; margin-bottom: 1rem;">Traditional Methods</h2>
                <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
                <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
                <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
                <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
                <p style="margin: 0; font-weight: 600; color: #dc2626;">
                    Result: You know what to do but can't consistently do it
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: #ecfdf5; border-radius: 12px; padding: 2rem; border-left: 4px solid #22c55e;">
                <h2 style="color: #16a34a; margin-bottom: 1rem;">Pattern Change Hypnotherapy</h2>
                <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
                <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
                <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
                <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
                <p style="margin: 0; font-weight: 600; color: #16a34a;">
                    Result: Your subconscious now supports your goals automatically
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # How it works
        st.markdown("### How Pattern Change Actually Works")
        
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 2rem; margin: 2rem 0; border: 1px solid var(--border);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                <div style="text-align: center;">
                    <div style="background: var(--accent); color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
                    <h2>Identify Your Patterns</h2>
                    <p>We map exactly what triggers your unwanted behavior at the subconscious level - 
                    often patterns you learned in childhood that no longer serve you.</p>
                </div>
                <div style="text-align: center;">
                    <div style="background: var(--accent); color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
                    <h2>Reprogram Directly</h2>
                    <p>Using clinical hypnosis, we access your subconscious mind and install new, 
                    empowering patterns that automatically support your goals.</p>
                </div>
                <div style="text-align: center;">
                    <div style="background: var(--accent); color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">3</div>
                    <h2>Live the Change</h2>
                    <p>The old urges and compulsions simply disappear. You naturally make choices 
                    that align with your goals without effort or struggle.</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Real example
        st.markdown("### Why This Works: A Real Example")
        st.markdown("""
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: 12px; padding: 2rem; margin: 2rem 0;">
            <p style="font-style: italic; font-size: 1.1rem; line-height: 1.7; margin-bottom: 1rem;">
                "I tried to quit smoking for 15 years. Patches, gum, medications, willpower - nothing worked. 
                After session 1, I understood that I wasn't addicted to nicotine, I was addicted to the feeling 
                of 'taking a break' and 'having 5 minutes for myself.'
            </p>
            <p style="font-style: italic; font-size: 1.1rem; line-height: 1.7; margin-bottom: 1rem;">
                Session 2 rewired that pattern. Now when I need a break, I naturally want to step outside 
                and take deep breaths instead of reaching for a cigarette. The craving is completely gone - 
                not suppressed, gone."
            </p>
            <p style="font-weight: 600; color: var(--accent); margin: 0;">
                — Banking Executive, Singapore (2 sessions, 6 months smoke-free)
            </p>
        </div>
        """, unsafe_allow_html=True)

class HomePage:
    """Complete home page with improved content"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.quiz = QuizSection()
        self.method = PatternChangeMethod()
    
    def render(self):
        """Render complete home page"""
        # Hero section
        self.hero.render()
        
        # Quiz section
        self.quiz.render()
        
        # Method explanation
        self.method.render()

# Factory function
def create_home_page():
    return HomePage()
