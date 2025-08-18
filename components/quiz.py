"""
Enhanced Quiz component with better engagement and animations
30-second suitability assessment with improved UX and visual feedback
Uses native Streamlit components for better compatibility
"""

import streamlit as st
from utils.session_state import SessionStateKeys, update_quiz_answer, reset_quiz, set_quiz_score

class StreamlitQuizQuestion:
    """Quiz question using Streamlit native components"""
    
    def __init__(self, question_id: int, question_data: dict):
        self.question_id = question_id
        self.title = question_data["title"]
        self.options = question_data["options"]
    
    def render(self):
        """Render question using Streamlit radio buttons"""
        st.markdown(f"### {self.title}")
        
        # Create option list for radio buttons
        option_labels = []
        option_values = []
        
        for icon, option, description in self.options:
            option_labels.append(f"{icon} {option}")
            option_values.append(option)
        
        # Use radio buttons for selection
        selected_index = st.radio(
            "Choose your answer:",
            range(len(option_labels)),
            format_func=lambda x: option_labels[x],
            key=f"quiz_q{self.question_id}",
            label_visibility="collapsed"
        )
        
        # Show description for selected option
        if selected_index is not None:
            _, _, description = self.options[selected_index]
            st.caption(f"💡 {description}")
        
        # Continue button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Continue ➡️", key=f"continue_q{self.question_id}", 
                        type="primary", use_container_width=True):
                selected_answer = option_values[selected_index]
                return selected_answer
        
        return None

class StreamlitQuizProgress:
    """Progress indicator using Streamlit"""
    
    def render(self, current_step: int, total_steps: int = 3):
        """Render progress using Streamlit progress bar"""
        progress = (current_step - 1) / total_steps
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(progress)
        with col2:
            st.write(f"Step {current_step}/{total_steps}")

class StreamlitQuizResults:
    """Results display using Streamlit components"""
    
    def __init__(self, score: int, answers: dict):
        self.score = score
        self.answers = answers
        self.message = self._get_message(score)
    
    def render(self):
        """Render results using Streamlit"""
        # Results header
        st.markdown("## 🎉 Assessment Complete!")
        
        # Score display
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.metric("Your Suitability Score", f"{self.score}%", self.message)
        
        # Results interpretation
        if self.score >= 70:
            st.success(f"✅ **Excellent!** Your score of {self.score}% indicates you're ready for transformation.")
            st.write("You have all the key factors for success in our 2-session program.")
        elif self.score >= 55:
            st.warning(f"⚡ **Good potential!** Your score of {self.score}% shows promise for our method.")
            st.write("A brief consultation will help us tailor the perfect approach for you.")
        else:
            st.info(f"💬 **Let's talk!** Your score of {self.score}% suggests we should discuss your situation.")
            st.write("Everyone's journey is unique - a conversation will help us find the best path forward.")
        
        # Action buttons
        st.markdown("### What's Next?")
        
        col1, col2 = st.columns(2)
        
        if self.score >= 70:
            with col1:
                if st.button("📞 Free Discovery Call", key="result_discovery", use_container_width=True):
                    st.success("Perfect! We'll contact you within 24 hours.")
            with col2:
                if st.button("⚡ Book Sessions Now", key="result_book", 
                           type="primary", use_container_width=True):
                    st.success("Excellent choice! Redirecting to booking...")
        else:
            with col1:
                if st.button("📞 Schedule Free Consultation", key="result_consult", 
                           type="primary", use_container_width=True):
                    st.success("Great! We'll discuss your situation and options.")
            with col2:
                if st.button("🔄 Retake Assessment", key="retake_quiz"):
                    reset_quiz()
                    st.rerun()
        
        # Results breakdown
        with st.expander("📊 See Your Assessment Details"):
            st.write("**Your Responses:**")
            question_labels = ["🎯 Primary Goal", "⏰ Duration", "🚀 Readiness Level"]
            for i, label in enumerate(question_labels, 1):
                answer = self.answers.get(i, "Not answered")
                st.write(f"- {label}: **{answer}**")
    
    def _get_message(self, score: int) -> str:
        """Get message based on score"""
        if score >= 85:
            return "Ideal candidate!"
        elif score >= 70:
            return "Very good fit"
        elif score >= 55:
            return "Good potential"
        else:
            return "Let's discuss"

class StreamlitOptimizedQuiz:
    """Main quiz component using Streamlit"""
    
    def __init__(self):
        self.questions = {
            1: {
                "title": "🎯 What would you most like to change or improve?",
                "options": [
                    ("🚭", "Quit smoking", "Break free from tobacco addiction"),
                    ("😌", "Reduce anxiety", "Find calm and peace of mind"), 
                    ("😴", "Improve sleep", "Get better, deeper rest"),
                    ("🔄", "Break bad habits", "Change unwanted behaviors"),
                    ("❓", "Other", "Something else I'd like to change")
                ]
            },
            2: {
                "title": "⏰ How long have you been dealing with this challenge?",
                "options": [
                    ("🆕", "Less than 6 months", "Relatively new challenge"),
                    ("📅", "6 months to 2 years", "Moderate duration"),
                    ("⏳", "More than 2 years", "Long-standing issue"),
                    ("🔄", "Many years", "Deeply ingrained pattern")
                ]
            },
            3: {
                "title": "🚀 How ready are you to make this change happen?",
                "options": [
                    ("🤔", "Just exploring options", "Learning about possibilities"),
                    ("👍", "Somewhat ready", "Interested and considering"),
                    ("💪", "Very ready - I'm committed", "Fully motivated to change"),
                    ("🔥", "Desperate for change", "Need transformation now")
                ]
            }
        }
        
        self.scoring = {
            1: {"Quit smoking": 40, "Reduce anxiety": 35, "Improve sleep": 30, 
                "Break bad habits": 35, "Other": 25},
            2: {"Less than 6 months": 20, "6 months to 2 years": 25, 
                "More than 2 years": 30, "Many years": 25},
            3: {"Just exploring options": 10, "Somewhat ready": 20, 
                "Very ready - I'm committed": 30, "Desperate for change": 25}
        }
        
        self.progress = StreamlitQuizProgress()
    
    def render(self):
        """Render complete quiz using Streamlit"""
        st.markdown("## 30-Second Transformation Assessment")
        st.write("Discover how well-suited you are for our proven 2-session method")
        
        current_step = st.session_state.get(SessionStateKeys.QUIZ_STEP, 1)
        quiz_completed = st.session_state.get(SessionStateKeys.QUIZ_COMPLETED, False)
        
        if not quiz_completed:
            self._render_active_quiz(current_step)
        else:
            self._render_quiz_results()
    
    def _render_active_quiz(self, current_step: int):
        """Render active quiz"""
        # Progress indicator
        self.progress.render(current_step)
        
        # Current question
        if current_step <= len(self.questions):
            question_data = self.questions[current_step]
            question = StreamlitQuizQuestion(current_step, question_data)
            
            selected_answer = question.render()
            
            if selected_answer:
                update_quiz_answer(current_step, selected_answer)
                
                # Show confirmation and move to next
                st.success(f"✅ Answer recorded: {selected_answer}")
                
                # Auto-advance after a moment
                if current_step < len(self.questions):
                    st.info("Moving to next question...")
                else:
                    st.info("Calculating your results...")
                
                st.rerun()
        
        # Navigation
        if current_step > 1:
            if st.button("⬅️ Previous Question", key="quiz_back"):
                from utils.session_state import SessionStateManager
                SessionStateManager.go_to_previous_question()
                st.rerun()
    
    def _render_quiz_results(self):
        """Render quiz results"""
        answers = st.session_state.get(SessionStateKeys.QUIZ_ANSWERS, {})
        score = self._calculate_score(answers)
        
        set_quiz_score(score)
        
        results = StreamlitQuizResults(score, answers)
        results.render()
    
    def _calculate_score(self, answers: dict) -> int:
        """Calculate quiz score"""
        score = 0
        for question_id, answer in answers.items():
            if question_id in self.scoring and answer in self.scoring[question_id]:
                score += self.scoring[question_id][answer]
        return min(score, 100)

class StreamlitQuizLauncher:
    """Quiz launcher using Streamlit"""
    
    def render_quiz_teaser(self):
        """Render quiz teaser"""
        st.markdown("### 🎯 Are You Ready for Transformation?")
        st.write("Take our 30-second assessment to discover your potential for rapid change")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Start Assessment Now", key="quiz_launcher", 
                        type="primary", use_container_width=True):
                reset_quiz()
                st.success("Assessment started! Answer the questions below.")
                return True
        return False

def create_streamlit_quiz():
    """Factory function"""
    return StreamlitOptimizedQuiz()

def create_streamlit_quiz_launcher():
    """Factory function"""
    return StreamlitQuizLauncher()
