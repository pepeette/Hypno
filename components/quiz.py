"""
Quiz Component
30-second suitability assessment using Streamlit components
Enhanced UX with progress tracking and personalized results
"""
import streamlit as st
from utils.config import QuizConfig
from utils.session_state import (
    reset_quiz, update_quiz_answer, calculate_quiz_score, 
    get_quiz_recommendation
)

class Quiz:
    """Enhanced quiz component using native Streamlit elements"""
    
    def __init__(self):
        self.questions = QuizConfig.QUESTIONS
        self.total_questions = len(self.questions)
    
    def render(self):
        """Render the complete quiz experience"""
        self._render_quiz_header()
        
        if not st.session_state.quiz_completed:
            self._render_active_quiz()
        else:
            self._render_quiz_results()
    
    def _render_quiz_header(self):
        """Render quiz introduction using Streamlit components"""
        st.markdown("## 🎯 Free 30-Second Assessment")
        st.write("Discover your potential for rapid transformation in 3 quick questions")
        
        # Show progress if quiz started
        if st.session_state.quiz_started or st.session_state.quiz_completed:
            current_step = min(st.session_state.quiz_step, self.total_questions)
            progress = (current_step - 1) / self.total_questions
            
            st.progress(progress, text=f"Question {current_step} of {self.total_questions}")
    
    def _render_active_quiz(self):
        """Render current quiz question using Streamlit buttons"""
        current_step = st.session_state.quiz_step
        
        if current_step <= self.total_questions:
            question_data = self.questions[current_step]
            
            # Question title
            st.markdown(f"### {question_data['title']}")
            
            # Render options using Streamlit columns and buttons
            if len(question_data['options']) == 4:
                # 2x2 grid for 4 options
                col1, col2 = st.columns(2)
                
                for i, (icon, option) in enumerate(question_data['options']):
                    col = col1 if i % 2 == 0 else col2
                    
                    with col:
                        if st.button(
                            f"{icon} {option}",
                            key=f"q{current_step}_option_{i}",
                            use_container_width=True,
                            help=f"Select: {option}"
                        ):
                            update_quiz_answer(current_step, option)
                            st.rerun()
            else:
                # Single column for other layouts
                for i, (icon, option) in enumerate(question_data['options']):
                    if st.button(
                        f"{icon} {option}",
                        key=f"q{current_step}_option_{i}",
                        use_container_width=True,
                        help=f"Select: {option}"
                    ):
                        update_quiz_answer(current_step, option)
                        st.rerun()
    
    def _render_quiz_results(self):
        """Render quiz results using Streamlit components"""
        score = st.session_state.quiz_score
        recommendation = get_quiz_recommendation(score)
        
        # Results header
        st.success("🎉 Assessment Complete!")
        
        # Score display using metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Your Score", f"{score}%")
        with col2:
            st.metric("Assessment", recommendation['title'])
        with col3:
            st.metric("Recommendation", recommendation['level'].title())
        
        # Recommendation message
        st.info(f"💡 {recommendation['message']}")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if score >= 65:
                if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
                    st.success("Great choice! Scroll down to book.")
            else:
                if st.button("💬 Schedule Consultation", type="primary", use_container_width=True):
                    st.success("Perfect! Scroll down to book.")
        
        with col2:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                reset_quiz()
                st.rerun()
        
        # Show quiz summary
        with st.expander("📊 View Your Responses"):
            st.write("Your answers:")
            for q_id, answer in st.session_state.quiz_answers.items():
                question_title = self.questions[q_id]['title']
                st.write(f"**{question_title}** {answer}")
    
    def render_compact(self):
        """Render a compact version for sidebars or small spaces"""
        st.markdown("### 🎯 Quick Assessment")
        
        if not st.session_state.quiz_completed:
            if st.button("Start 30-Second Assessment", type="primary", use_container_width=True):
                st.session_state.quiz_started = True
                st.rerun()
        else:
            score = st.session_state.quiz_score
            recommendation = get_quiz_recommendation(score)
            
            st.metric("Your Score", f"{score}%")
            st.write(recommendation['message'])
            
            if st.button("View Full Results", use_container_width=True):
                # Scroll to main quiz section
                st.success("Scroll up to see full results!")

class QuizAnalytics:
    """Simple analytics for quiz completion"""
    
    @staticmethod
    def track_quiz_start():
        """Track quiz start event"""
        if 'quiz_stats' not in st.session_state:
            st.session_state.quiz_stats = {'started': 0, 'completed': 0}
        st.session_state.quiz_stats['started'] += 1
    
    @staticmethod
    def track_quiz_completion():
        """Track quiz completion event"""
        if 'quiz_stats' in st.session_state:
            st.session_state.quiz_stats['completed'] += 1
    
    @staticmethod
    def get_completion_rate():
        """Get quiz completion rate"""
        if 'quiz_stats' not in st.session_state:
            return 0
        
        stats = st.session_state.quiz_stats
        if stats['started'] == 0:
            return 0
        
        return (stats['completed'] / stats['started']) * 100
