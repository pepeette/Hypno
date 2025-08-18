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
Home page component using Streamlit components instead of nested divs
"""
import streamlit as st

class HeroSection:
    """Hero section using Streamlit components"""
    
    def render(self):
        """Render hero section with Streamlit components"""
        # Hero container using Streamlit container
        with st.container():
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                        border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
                <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
                <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
                    Most people try to change using willpower. That's why 95% fail. 
                    We bypass your conscious resistance and reprogram your subconscious patterns directly.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add compelling message using Streamlit info box
            st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")

class QuizSection:
    """Quiz section using Streamlit components"""
    
    def __init__(self):
        # Initialize session state using Streamlit
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        if 'quiz_step' not in st.session_state:
            st.session_state.quiz_step = 1
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
    
    def render(self):
        """Render quiz using Streamlit components"""
        # Section header
        st.subheader("Find Out If You're Ready for Rapid Change")
        st.write("Three quick questions to assess your potential for transformation:")
        
        if not st.session_state.quiz_completed:
            self._render_all_questions()
        else:
            self._render_results()
    
    def _render_all_questions(self):
        """Show all questions using Streamlit components"""
        current_step = st.session_state.quiz_step
        
        # Question 1 using Streamlit expander and columns
        with st.expander("Question 1: What would you most like to change?", expanded=(current_step == 1)):
            if current_step == 1:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
                        self._answer_question(1, "Quit Smoking")
                    if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
                        self._answer_question(1, "Improve Sleep")
                with col2:
                    if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
                        self._answer_question(1, "Reduce Anxiety")
                    if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
                        self._answer_question(1, "Break Bad Habits")
            elif 1 in st.session_state.quiz_answers:
                st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
        # Question 2 (show only if Q1 answered)
        if len(st.session_state.quiz_answers) >= 1:
            with st.expander("Question 2: How long have you been dealing with this?", expanded=(current_step == 2)):
                if current_step == 2:
                    if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
                        self._answer_question(2, "Less than 6 months")
                    if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
                        self._answer_question(2, "6 months to 2 years")
                    if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
                        self._answer_question(2, "More than 2 years")
                elif 2 in st.session_state.quiz_answers:
                    st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
        # Question 3 (show only if Q2 answered)
        if len(st.session_state.quiz_answers) >= 2:
            with st.expander("Question 3: How ready are you to make this change?", expanded=(current_step == 3)):
                if current_step == 3:
                    if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
                        self._answer_question(3, "Just exploring options")
                    if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
                        self._answer_question(3, "Very ready - I'm committed")
                    if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
                        self._answer_question(3, "Desperate for change")
                elif 3 in st.session_state.quiz_answers:
                    st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
        # Progress using Streamlit progress bar
        progress = len(st.session_state.quiz_answers) / 3
        if progress > 0:
            st.progress(progress)
            if progress < 1:
                st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
            else:
                st.caption("Complete!")
    
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
        """Render quiz results using Streamlit components"""
        score = st.session_state.quiz_score
        
        # Determine message based on score
        if score >= 70:
            st.success("🌟 Excellent candidate! You have strong indicators for rapid transformation.")
            st.info("You're ready to book your transformation package or start with a discovery call.")
        elif score >= 55:
            st.warning("🎯 Good potential! Hypnotherapy can definitely help with the right approach.")
            st.info("A discovery call would help us create the perfect strategy for your situation.")
        else:
            st.info("💬 Let's talk! Every situation is unique, and a conversation will help us determine the best path forward.")
            st.info("A free discovery call will help us understand how to best support your goals.")
        
        # Display score using Streamlit metric
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.metric("Transformation Readiness", f"{score}%", "Suitability Match")
        
        # Action buttons using Streamlit columns
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
    """Pattern change method explanation using Streamlit components"""
    
    def render(self):
        """Render method explanation using Streamlit components"""
        st.subheader("Pattern Change Hypnotherapy: Why It Works")
        
        # Opening explanation using Streamlit info box
        st.info("""
        Every unwanted behavior is driven by subconscious patterns you learned years ago. 
        Traditional therapy tries to override these patterns with willpower. We change the patterns themselves.
        When your subconscious programming supports your goals instead of fighting them, 
        change becomes effortless and permanent.
        """)
        
        # Success rate using Streamlit success box and metric
        with st.container():
            st.success("✅ 85% Success Rate in Just 2 Sessions")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Success Rate", "85%", "in 2 sessions")
            with col2:
                st.metric("Need 3rd Session", "15%", "reinforcement")
            with col3:
                st.metric("vs Traditional", "Months", "to years")
            
            st.write("Most clients achieve complete transformation in two 90-minute sessions. About 15% choose an optional reinforcement session a few weeks later for additional confidence.")
        
        # Method comparison using Streamlit columns and containers
        st.write("### The Difference Is in the Approach")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.error("❌ Traditional Methods")
                st.write("**Talk therapy:** Analyzes problems but rarely creates lasting change")
                st.write("**Willpower:** Requires constant effort and usually fails within weeks")
                st.write("**Medications:** Manage symptoms but don't address root causes")
                st.write("**Self-help:** Gives you tools but can't change deep programming")
                st.warning("**Result:** You know what to do but can't consistently do it")
        
        with col2:
            with st.container():
                st.success("✅ Pattern Change Hypnotherapy")
                st.write("**Session 1:** Map your unique subconscious triggers and patterns")
                st.write("**Session 2:** Rewire those patterns at the subconscious level")
                st.write("**Session 3:** Optional reinforcement if needed (15% of clients)")
                st.write("**Follow-up:** Permanent change that feels natural and effortless")
                st.success("**Result:** Your subconscious now supports your goals automatically")
        
        # How it works using Streamlit tabs
        with st.container():
            st.write("### How Pattern Change Actually Works")
            
            tab1, tab2, tab3 = st.tabs(["1️⃣ Identify Patterns", "2️⃣ Reprogram Directly", "3️⃣ Live the Change"])
            
            with tab1:
                st.write("**Identify Your Patterns**")
                st.write("We map exactly what triggers your unwanted behavior at the subconscious level - often patterns you learned in childhood that no longer serve you.")
            
            with tab2:
                st.write("**Reprogram Directly**")
                st.write("Using clinical hypnosis, we access your subconscious mind and install new, empowering patterns that automatically support your goals.")
            
            with tab3:
                st.write("**Live the Change**")
                st.write("The old urges and compulsions simply disappear. You naturally make choices that align with your goals without effort or struggle.")
        
        # Real example using Streamlit quote
        with st.container():
            st.write("### Why This Works: A Real Example")
            st.quote("""
            I tried to quit smoking for 15 years. Patches, gum, medications, willpower - nothing worked. 
            After session 1, I understood that I wasn't addicted to nicotine, I was addicted to the feeling 
            of 'taking a break' and 'having 5 minutes for myself.'
            
            Session 2 rewired that pattern. Now when I need a break, I naturally want to step outside 
            and take deep breaths instead of reaching for a cigarette. The craving is completely gone - 
            not suppressed, gone.
            
            — Banking Executive, Singapore (2 sessions, 6 months smoke-free)
            """)

class HomePage:
    """Complete home page using Streamlit components"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.quiz = QuizSection()
        self.method = PatternChangeMethod()
    
    def render(self):
        """Render complete home page using Streamlit layout"""
        # Use Streamlit containers for clean layout
        with st.container():
            self.hero.render()
        
        with st.container():
            self.quiz.render()
        
        with st.container():
            self.method.render()

# Factory function for clean import
def create_home_page():
    return HomePage()
