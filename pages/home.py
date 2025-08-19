# """
# Fixed Home page component with better styling and readability
# """
# import streamlit as st

# class HeroSection:
#     """Hero section using Streamlit components"""
    
#     def render(self):
#         """Render hero section with Streamlit components"""
#         # Hero container using Streamlit container
#         with st.container():
#             st.markdown("""
#             <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                         border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#                 <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
#                 <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
#                     Most people try to change using willpower. That's why 95% fail. 
#                     We bypass your conscious resistance and reprogram your subconscious patterns directly.
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Add compelling message using Streamlit info box
#             st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")

# class QuizSection:
#     """Quiz section using Streamlit components with better UX"""
    
#     def __init__(self):
#         # Initialize session state using Streamlit
#         if 'quiz_answers' not in st.session_state:
#             st.session_state.quiz_answers = {}
#         if 'quiz_step' not in st.session_state:
#             st.session_state.quiz_step = 1
#         if 'quiz_completed' not in st.session_state:
#             st.session_state.quiz_completed = False
#         if 'quiz_score' not in st.session_state:
#             st.session_state.quiz_score = 0
    
#     def render(self):
#         """Render quiz using Streamlit components"""
#         # Section header
#         st.subheader("Find Out If You're Ready for Rapid Change")
#         st.write("Three quick questions to assess your potential for transformation:")
        
#         if not st.session_state.quiz_completed:
#             self._render_all_questions()
#         else:
#             self._render_results()
    
#     def _render_all_questions(self):
#         """Show all questions with proper collapsing - Q1 expanded by default"""
#         current_step = st.session_state.quiz_step
        
#         # Question 1 - Expanded by default, collapsed after answering
#         q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
#         with st.expander("Question 1: What would you most like to change?", expanded=q1_expanded):
#             if 1 not in st.session_state.quiz_answers:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
#                         self._answer_question(1, "Quit Smoking")
#                     if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
#                         self._answer_question(1, "Improve Sleep")
#                 with col2:
#                     if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
#                         self._answer_question(1, "Reduce Anxiety")
#                     if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
#                         self._answer_question(1, "Break Bad Habits")
#             else:
#                 st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
#         # Question 2 - Show only if Q1 answered, expand when active
#         if len(st.session_state.quiz_answers) >= 1:
#             q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
#             with st.expander("Question 2: How long have you been dealing with this?", expanded=q2_expanded):
#                 if 2 not in st.session_state.quiz_answers:
#                     if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
#                         self._answer_question(2, "Less than 6 months")
#                     if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
#                         self._answer_question(2, "6 months to 2 years")
#                     if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
#                         self._answer_question(2, "More than 2 years")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
#         # Question 3 - Show only if Q2 answered, expand when active
#         if len(st.session_state.quiz_answers) >= 2:
#             q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
#             with st.expander("Question 3: How ready are you to make this change?", expanded=q3_expanded):
#                 if 3 not in st.session_state.quiz_answers:
#                     if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
#                         self._answer_question(3, "Just exploring options")
#                     if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
#                         self._answer_question(3, "Very ready - I'm committed")
#                     if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
#                         self._answer_question(3, "Desperate for change")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
#         # Progress using Streamlit progress bar
#         progress = len(st.session_state.quiz_answers) / 3
#         if progress > 0:
#             st.progress(progress)
#             if progress < 1:
#                 st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
#             else:
#                 st.caption("Complete!")
    
#     def _answer_question(self, question_id, answer):
#         """Handle question answer"""
#         st.session_state.quiz_answers[question_id] = answer
#         if question_id < 3:
#             st.session_state.quiz_step = question_id + 1
#         else:
#             st.session_state.quiz_completed = True
#             st.session_state.quiz_score = self._calculate_score()
#         st.rerun()
    
#     def _calculate_score(self):
#         """Calculate suitability score"""
#         scoring = {
#             1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
#             2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
#             3: {"Just exploring options": 10, "Very ready - I'm committed": 30, "Desperate for change": 25}
#         }
        
#         total_score = 0
#         for q_id, answer in st.session_state.quiz_answers.items():
#             if q_id in scoring and answer in scoring[q_id]:
#                 total_score += scoring[q_id][answer]
        
#         return min(total_score, 100)
    
#     def _render_results(self):
#         """Render quiz results using Streamlit components"""
#         score = st.session_state.quiz_score
        
#         # Determine message based on score
#         if score >= 70:
#             st.success("🌟 Excellent candidate! You have strong indicators for rapid transformation.")
#             st.info("You're ready to book your transformation package or start with a discovery call.")
#         elif score >= 55:
#             st.warning("🎯 Good potential! Hypnotherapy can definitely help with the right approach.")
#             st.info("A discovery call would help us create the perfect strategy for your situation.")
#         else:
#             st.info("💬 Let's talk! Every situation is unique, and a conversation will help us determine the best path forward.")
#             st.info("A free discovery call will help us understand how to best support your goals.")
        
#         # Display score using st.metric with combined value/delta
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.metric("", f"{score}% Suitability Match", "Transformation Readiness")
        
#         # Action buttons using Streamlit columns
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("🔄 Retake Assessment", use_container_width=True):
#                 self._reset_quiz()
#         with col2:
#             if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
#                 st.success("Perfect! Scroll down to book your call.")
    
#     def _reset_quiz(self):
#         """Reset quiz state"""
#         st.session_state.quiz_answers = {}
#         st.session_state.quiz_step = 1
#         st.session_state.quiz_completed = False
#         st.session_state.quiz_score = 0
#         st.rerun()

# class PatternChangeMethod:
#     """Pattern change method explanation using Streamlit components"""
    
#     def render(self):
#         """Render method explanation using Streamlit components"""
#         st.subheader("Pattern Change Hypnotherapy: Why It Works")
        
#         # Opening explanation using Streamlit info box
#         st.info("""
#         Every unwanted behavior is driven by subconscious patterns you learned years ago. 
#         Traditional therapy tries to override these patterns with willpower. We change the patterns themselves.
#         When your subconscious programming supports your goals instead of fighting them, 
#         change becomes effortless and permanent.
#         """)
        
#         # Success rate using custom metrics with combined value/delta
#         with st.container():
#             st.success("✅ 85% Success Rate in Just 2 Sessions")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("", "85% in 2 sessions", "Success Rate")
#             with col2:
#                 st.metric("", "15% reinforcement", "Need 3rd Session")
#             with col3:
#                 st.metric("", "Months to years", "vs Traditional")
            
#             st.write("Most clients achieve complete transformation in two 90-minute sessions. About 15% choose an optional reinforcement session a few weeks later for additional confidence.")
        
#         # Method comparison using container cards instead of columns
#         st.write("### The Difference Is in the Approach")
        
#         # Traditional Methods Card
#         with st.container():
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; margin: 1rem 0; border-left: 4px solid #ef4444;">
#                 <h2 style="color: #dc2626; margin-bottom: 1rem;">❌ Traditional Methods</h2>
#                 <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
#                 <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
#                 <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
#                 <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
#                 <p style="margin: 0; font-weight: 600; color: #dc2626;">
#                     Result: You know what to do but can't consistently do it
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         # Pattern Change Hypnotherapy Card  
#         with st.container():
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; margin: 1rem 0; border-left: 4px solid #22c55e;">
#                 <h2 style="color: #16a34a; margin-bottom: 1rem;">✅ Pattern Change Hypnotherapy</h2>
#                 <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
#                 <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
#                 <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
#                 <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
#                 <p style="margin: 0; font-weight: 600; color: #16a34a;">
#                     Result: Your subconscious now supports your goals automatically
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         # How it works using simple columns instead of tabs (avoid background colors)
#         with st.container():
#             st.write("### How Pattern Change Actually Works")
            
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
#                     <h2 style="color: #273548;">Identify Your Patterns</h2>
#                     <p style="color: #556D7A;">We map exactly what triggers your unwanted behavior at the subconscious level - 
#                     often patterns you learned in childhood that no longer serve you.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
#                     <h2 style="color: #273548;">Reprogram Directly</h2>
#                     <p style="color: #556D7A;">Using clinical hypnosis, we access your subconscious mind and install new, 
#                     empowering patterns that automatically support your goals.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">3</div>
#                     <h2 style="color: #273548;">Live the Change</h2>
#                     <p style="color: #556D7A;">The old urges and compulsions simply disappear. You naturally make choices 
#                     that align with your goals without effort or struggle.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
        
#         # Ready to start section
#         st.write("### Ready to Start Your Transformation?")
#         st.info("Book your free discovery call to see if our method is right for you.")

# class HomePage:
#     """Complete home page using Streamlit components"""
    
#     def __init__(self):
#         self.hero = HeroSection()
#         self.quiz = QuizSection()
#         self.method = PatternChangeMethod()
    
#     def render(self):
#         """Render complete home page using Streamlit layout"""
#         # Use Streamlit containers for clean layout
#         with st.container():
#             self.hero.render()
        
#         with st.container():
#             self.quiz.render()
        
#         with st.container():
#             self.method.render()

# # Factory function for clean import
# def create_home_page():
#     return HomePage()


"""
Fixed Home page component with better styling and readability
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
    """Quiz section using Streamlit components with better UX"""
    
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
        """Show all questions with proper collapsing - Q1 expanded by default"""
        current_step = st.session_state.quiz_step
        
        # Question 1 - Expanded by default, collapsed after answering
        q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
        with st.expander("Question 1: What would you most like to change?", expanded=q1_expanded):
            if 1 not in st.session_state.quiz_answers:
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
            else:
                st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
        # Question 2 - Show only if Q1 answered, expand when active
        if len(st.session_state.quiz_answers) >= 1:
            q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
            with st.expander("Question 2: How long have you been dealing with this?", expanded=q2_expanded):
                if 2 not in st.session_state.quiz_answers:
                    if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
                        self._answer_question(2, "Less than 6 months")
                    if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
                        self._answer_question(2, "6 months to 2 years")
                    if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
                        self._answer_question(2, "More than 2 years")
                else:
                    st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
        # Question 3 - Show only if Q2 answered, expand when active
        if len(st.session_state.quiz_answers) >= 2:
            q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
            with st.expander("Question 3: How ready are you to make this change?", expanded=q3_expanded):
                if 3 not in st.session_state.quiz_answers:
                    if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
                        self._answer_question(3, "Just exploring options")
                    if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
                        self._answer_question(3, "Very ready - I'm committed")
                    if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
                        self._answer_question(3, "Desperate for change")
                else:
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
        
        # Display score using st.metric with combined value/delta
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.metric("", f"{score}% Suitability Match", "Transformation Readiness")
        
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
        
        # Success rate using custom metrics with combined value/delta
        with st.container():
            st.success("✅ 85% Success Rate in Just 2 Sessions")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("", "85% in 2 sessions", "Success Rate")
            with col2:
                st.metric("", "15% reinforcement", "Need 3rd Session")
            with col3:
                st.metric("", "Months to years", "vs Traditional")
            
            st.write("Most clients achieve complete transformation in two 90-minute sessions. About 15% choose an optional reinforcement session a few weeks later for additional confidence.")
        
        # Method comparison using 3-column layout with image in center
        st.write("### The Difference Is in the Approach")
        
        # Desktop: 3 columns, Mobile: stacked
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # Column 1: Traditional Methods Card
        with col1:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; margin: 1rem 0; border-left: 4px solid #ef4444; height: 100%;">
                <h2 style="color: #dc2626; margin-bottom: 1rem; text-align: center;">❌ Traditional Methods</h2>
                <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
                <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
                <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
                <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
                <p style="margin: 0; font-weight: 600; color: #dc2626; text-align: center;">
                    Result: You know what to do but can't consistently do it
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Column 2: Comparison Image
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; margin: 1rem 0; text-align: center; height: 100%; 
                        display: flex; flex-direction: column; justify-content: center;">
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">VS</h2>
                <img src="https://github.com/pepeette/Hypno/blob/main/img/Hypnotherapy_compa.jpg?raw=true" 
                     alt="Hypnotherapy Comparison" 
                     style="width: 100%; max-width: 200px; border-radius: 8px; margin: 0 auto;">
                <p style="margin-top: 1rem; color: #556D7A; font-style: italic;">
                    Different approaches, different results
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Column 3: Pattern Change Hypnotherapy Card  
        with col3:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; margin: 1rem 0; border-left: 4px solid #22c55e; height: 100%;">
                <h2 style="color: #16a34a; margin-bottom: 1rem; text-align: center;">✅ Pattern Change Hypnotherapy</h2>
                <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
                <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
                <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
                <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
                <p style="margin: 0; font-weight: 600; color: #16a34a; text-align: center;">
                    Result: Your subconscious now supports your goals automatically
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # How it works using simple columns instead of tabs (avoid background colors)
        with st.container():
            st.write("### How Pattern Change Actually Works")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
                    <h2 style="color: #273548;">Identify Your Patterns</h2>
                    <p style="color: #556D7A;">We map exactly what triggers your unwanted behavior at the subconscious level - 
                    often patterns you learned in childhood that no longer serve you.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
                    <h2 style="color: #273548;">Reprogram Directly</h2>
                    <p style="color: #556D7A;">Using clinical hypnosis, we access your subconscious mind and install new, 
                    empowering patterns that automatically support your goals.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">3</div>
                    <h2 style="color: #273548;">Live the Change</h2>
                    <p style="color: #556D7A;">The old urges and compulsions simply disappear. You naturally make choices 
                    that align with your goals without effort or struggle.</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Ready to start section
        st.write("### Ready to Start Your Transformation?")
        st.info("Book your free discovery call to see if our method is right for you.")

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
