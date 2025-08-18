"""
SIMPLIFIED Quiz component - Essential 3-question flow using Streamlit buttons
Reduced from 400+ lines to <150 lines, mobile-friendly
"""
import streamlit as st

class SimpleQuiz:
    """Simplified 3-question quiz using Streamlit native components"""
    
    def __init__(self):
        self.questions = {
            1: {
                "title": "🎯 What would you most like to change?",
                "options": [
                    ("🚭 Quit Smoking", 40),
                    ("😌 Reduce Anxiety", 35),
                    ("😴 Improve Sleep", 30),
                    ("🔄 Break Bad Habits", 35),
                    ("❓ Other", 25)
                ]
            },
            2: {
                "title": "⏰ How long have you been dealing with this?",
                "options": [
                    ("🆕 Less than 6 months", 20),
                    ("📅 6 months to 2 years", 25),
                    ("⏳ More than 2 years", 30),
                    ("🔄 Many years", 25)
                ]
            },
            3: {
                "title": "🚀 How ready are you to make this change?",
                "options": [
                    ("🤔 Just exploring options", 10),
                    ("👍 Somewhat ready", 20),
                    ("💪 Very ready - I'm committed", 30),
                    ("🔥 Desperate for change", 25)
                ]
            }
        }
        
        # Initialize session state
        if 'quiz_step' not in st.session_state:
            st.session_state.quiz_step = 1
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
    
    def render(self):
        """Render the complete quiz experience"""
        # Quiz header
        st.markdown("## 🎯 30-Second Suitability Assessment")
        st.write("Discover your readiness for transformation in 3 quick questions")
        
        if not st.session_state.quiz_completed:
            self._render_active_quiz()
        else:
            self._render_results()
    
    def _render_active_quiz(self):
        """Render the active quiz"""
        current_step = st.session_state.quiz_step
        
        # Progress bar
        progress = min((current_step - 1) / 3 * 100, 100)
        st.progress(progress / 100)
        st.write(f"Question {min(current_step, 3)} of 3")
        
        # Current question
        if current_step <= 3:
            question_data = self.questions[current_step]
            self._render_question(current_step, question_data)
        
        # Navigation
        self._render_navigation(current_step)
    
    def _render_question(self, step_num, question_data):
        """Render individual question using Streamlit buttons"""
        st.markdown(f"### {question_data['title']}")
        st.write("")
        
        # Use columns for better layout
        if len(question_data['options']) <= 4:
            cols = st.columns(2)
            for i, (option_text, score) in enumerate(question_data['options']):
                col = cols[i % 2]
                with col:
                    if st.button(option_text, key=f"q{step_num}_{i}", use_container_width=True):
                        self._handle_answer(step_num, option_text, score)
        else:
            # Single column for more options
            for i, (option_text, score) in enumerate(question_data['options']):
                if st.button(option_text, key=f"q{step_num}_{i}", use_container_width=True):
                    self._handle_answer(step_num, option_text, score)
    
    def _handle_answer(self, step_num, answer, score):
        """Handle quiz answer selection"""
        st.session_state.quiz_answers[step_num] = {
            'answer': answer,
            'score': score
        }
        
        if step_num < 3:
            st.session_state.quiz_step = step_num + 1
        else:
            # Calculate final score
            total_score = sum(ans['score'] for ans in st.session_state.quiz_answers.values())
            st.session_state.quiz_score = min(total_score, 100)
            st.session_state.quiz_completed = True
        
        st.rerun()
    
    def _render_navigation(self, current_step):
        """Render navigation buttons"""
        if current_step > 1:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if st.button("← Previous", key="quiz_back"):
                    st.session_state.quiz_step = current_step - 1
                    # Remove current answer
                    if current_step in st.session_state.quiz_answers:
                        del st.session_state.quiz_answers[current_step]
                    st.rerun()
    
    def _render_results(self):
        """Render quiz results"""
        score = st.session_state.quiz_score
        
        # Results display
        if score >= 85:
            result_color = "#22c55e"
            result_icon = "🌟"
            result_message = "Excellent candidate for hypnotherapy!"
            recommendation = "You're ready to book your transformation package"
        elif score >= 70:
            result_color = "#65a30d"
            result_icon = "✅"
            result_message = "Very good fit for our 2-session method"
            recommendation = "You can book directly or have a quick call first"
        elif score >= 55:
            result_color = "#eab308"
            result_icon = "🎯"
            result_message = "Good potential with hypnotherapy"
            recommendation = "A discovery call would help us create the perfect approach"
        else:
            result_color = "#f97316"
            result_icon = "💬"
            result_message = "Consider a discovery call first"
            recommendation = "Let's discuss the best approach for your situation"
        
        # Score display
        st.markdown(f"""
        <div style="background: white; border: 2px solid {result_color}; border-radius: 12px; 
                    padding: 2rem; text-align: center; margin: 2rem 0;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{result_icon}</div>
            <div style="font-size: 2.5rem; font-weight: bold; color: {result_color}; margin-bottom: 0.5rem;">
                {score}%
            </div>
            <h3 style="margin-bottom: 1rem;">Suitability Match</h3>
            <p style="font-size: 1.1rem; margin-bottom: 1rem;">{result_message}</p>
            <p style="color: #556D7A;">{recommendation}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                self.reset_quiz()
        
        with col2:
            if st.button("📞 Free Discovery Call", use_container_width=True, type="primary"):
                st.success("📞 Great choice! Scroll down to book your call.")
        
        with col3:
            if score >= 70:
                if st.button("🎯 Book Sessions Now", use_container_width=True):
                    st.success("🎯 Excellent! Scroll down to book your sessions.")
            else:
                if st.button("💬 Learn More", use_container_width=True):
                    st.success("💬 Navigate to Method page to learn more!")
        
        # Show answers breakdown
        with st.expander("📊 See Your Assessment Breakdown"):
            for i, answer_data in st.session_state.quiz_answers.items():
                question_labels = ["🎯 Goal", "⏰ Duration", "🚀 Readiness"]
                st.write(f"**{question_labels[i-1]}:** {answer_data['answer']}")
    
    def reset_quiz(self):
        """Reset quiz to beginning"""
        st.session_state.quiz_step = 1
        st.session_state.quiz_answers = {}
        st.session_state.quiz_completed = False
        st.session_state.quiz_score = 0
        st.rerun()

def create_quiz():
    """Factory function to create quiz instance"""
    return SimpleQuiz()
