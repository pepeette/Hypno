# """
# Home Page
# Main landing page using Streamlit components
# Features focused hero card and direct path to quiz
# """
# import streamlit as st
# from utils.styling import render_hero_card, render_section_divider
# from utils.config import AppConfig, get_years_of_experience
# from utils.session_state import track_page_view
# from components.quiz import Quiz

# class HomePage:
#     """Home page with focused messaging and clear user journey"""
    
#     def __init__(self):
#         self.config = AppConfig()
    
#     def render(self):
#         """Render the complete home page"""
#         track_page_view("Home")
        
#         self._render_hero_card()
#         self._render_why_hypnotherapy()
#         self._render_quiz_section()
    
#     def _render_hero_card(self):
#         """Render focused hero card with clear value proposition"""
#         render_hero_card(
#             title="Transform Your Life in Just 2 Sessions",
#             subtitle=f"Science-backed hypnotherapy with {AppConfig.SUCCESS_RATE_2_SESSIONS}% success rate"
#         )
        
#         # # Key credentials in a subtle way
#         # col1, col2, col3 = st.columns(3)
        
#         # with col1:
#         #     st.metric(
#         #         "Success Rate",
#         #         f"{AppConfig.SUCCESS_RATE_2_SESSIONS}%",
#         #         "in 2 sessions"
#         #     )
        
#         # with col2:
#         #     st.metric(
#         #         "Experience",
#         #         f"{get_years_of_experience()} years",
#         #         f"since {AppConfig.PRACTICE_ESTABLISHED}"
#         #     )
        
#         # with col3:
#         #     st.metric(
#         #         "Certified",
#         #         "LCCH & DBT",
#         #         f"{AppConfig.LCCH_CERTIFICATION} & {AppConfig.DBT_CERTIFICATION}"
#         #     )
    
#     def _render_why_hypnotherapy(self):
#         """Explain why hypnotherapy works - focused and clear"""
#         render_section_divider()
        
#         st.markdown("## Why Hypnotherapy Succeeds Where Willpower Fails")
        
#         # Simple, focused explanation
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             st.markdown("### Traditional Methods")
#             st.write("Work with your conscious mind")
#             st.write("Only 5% of your decisions")
#             st.write("Require constant willpower")
#             st.write("High failure rates")
            
#         with col2:
#             st.markdown("### Our Hypnotherapy")
#             st.write("Works with your subconscious")
#             st.write("Controls 95% of decisions")
#             st.write("Natural, lasting change")
#             st.write("Proven results")
        
#         # Key insight without overwhelming detail
#         st.info("""
#         The breakthrough: Instead of fighting your programming with willpower, 
#         we rewire the subconscious patterns that drive your behavior. 
#         This creates effortless, permanent transformation.
#         """)
    
#     def _render_quiz_section(self):
#         """Render quiz section with clear call-to-action"""
#         render_section_divider()
        
#         st.markdown("## Discover Your Transformation Potential")
#         st.write("Take our 3-question assessment to see how hypnotherapy can help you")
        
#         # Quiz component - main focus of the page
#         quiz = Quiz()
#         quiz.render()

# # Factory function for easy import
# def create_home_page():
#     """Create HomePage instance"""
#     return HomePage()


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
