"""
Enhanced Quiz Component for 4-question assessment
Integrates with existing architecture
"""
import streamlit as st
from utils.config import QuizConfig, AppConstants
from utils.session_state import (
    reset_quiz, update_quiz_answer, calculate_quiz_score, 
    get_quiz_recommendation
)

class Quiz:
    """Enhanced 4-question quiz component"""
    
    def __init__(self):
        self.questions = QuizConfig.QUESTIONS
        self.total_questions = len(self.questions)
        self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
    
    def render(self):
        """Render the complete quiz experience"""
        self._render_quiz_header()
        
        if not st.session_state.quiz_completed:
            self._render_active_quiz()
        else:
            self._render_quiz_results()
    
    def _render_quiz_header(self):
        """Render quiz introduction"""
        st.subheader("Test: Do you need rapid change?")
        st.write("4 questions to assess if our method is right for your situation:")
        
        # Show progress if quiz started
        if st.session_state.quiz_step > 1 or st.session_state.quiz_completed:
            current_step = min(st.session_state.quiz_step, self.total_questions)
            progress = (len(st.session_state.quiz_answers)) / self.total_questions
            
            st.progress(progress)
            if not st.session_state.quiz_completed:
                st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of {self.total_questions}")
            else:
                st.caption("Assessment complete!")
    
    def _render_active_quiz(self):
        """Render current quiz question using expandable sections"""
        current_step = st.session_state.quiz_step
        
        # Render all questions with proper expansion logic
        for q_num in range(1, self.total_questions + 1):
            if q_num <= current_step:
                question_data = self.questions[q_num]
                
                # Determine if this question should be expanded
                is_current = (q_num == current_step and q_num not in st.session_state.quiz_answers)
                is_answered = (q_num in st.session_state.quiz_answers)
                
                with st.expander(f"Question {q_num}: {question_data['title']}", expanded=is_current):
                    if not is_answered:
                        # Show options for unanswered questions
                        self._render_question_options(q_num, question_data)
                    else:
                        # Show selected answer for answered questions
                        selected = st.session_state.quiz_answers[q_num]
                        st.success(f"✅ Selected: {selected.split(chr(10))[0]}")  # Show main answer only
    
    def _render_question_options(self, q_num, question_data):
        """Render options for a specific question"""
        options = question_data['options']
        
        if len(options) > 4:
            # 2x3 grid for 6 options (Question 1)
            col1, col2 = st.columns(2)
            for i, (icon, option) in enumerate(options):
                col = col1 if i % 2 == 0 else col2
                
                with col:
                    if st.button(
                        f"{icon} {option}",
                        key=f"q{q_num}_option_{i}",
                        use_container_width=True
                    ):
                        update_quiz_answer(q_num, option)
                        st.rerun()
        elif len(options) == 4:
            # 2x2 grid for 4 options
            col1, col2 = st.columns(2)
            for i, (icon, option) in enumerate(options):
                col = col1 if i % 2 == 0 else col2
                
                with col:
                    if st.button(
                        f"{icon} {option}",
                        key=f"q{q_num}_option_{i}",
                        use_container_width=True
                    ):
                        update_quiz_answer(q_num, option)
                        st.rerun()
        else:
            # Single column for 3 or fewer options
            for i, (icon, option) in enumerate(options):
                if st.button(
                    f"{icon} {option}",
                    key=f"q{q_num}_option_{i}",
                    use_container_width=True
                ):
                    update_quiz_answer(q_num, option)
                    st.rerun()
    
    def _render_quiz_results(self):
        """Render quiz results with white background"""
        score = st.session_state.quiz_score
        recommendation = get_quiz_recommendation(score)
        
        # White background results container
        st.markdown("""
        <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                    padding: 2rem; margin: 2rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        """, unsafe_allow_html=True)
        
        # Results display
        if score >= 75:
            st.success("🌟 High suitability for rapid transformation!")
        elif score >= 55:
            st.warning("🎯 Good potential for transformation!")
        elif score >= 35:
            st.info("💭 Assessment recommended")
        else:
            st.info("🌱 Preparation phase suggested")
        
        # Display metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Transformation Readiness", f"{score}%", "Suitability Score")
        with col2:
            st.metric("Focus Area", st.session_state.unwanted_pattern, "Primary Pattern")
        
        # Pattern-specific insights
        self._render_pattern_insights()
        
        st.info(f"**Recommendation**: {recommendation['message']}")
        st.write(f"**Next step**: {recommendation['action']}")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: #4CA1A3; color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: 8px;
                      font-weight: 600; text-align: center; width: 100%;
                      box-sizing: border-box;">
                📞 Book Discovery Call
            </a>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                reset_quiz()
                st.rerun()
        
        # Close white background container
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Show quiz summary in expander
        with st.expander("View Your Assessment Details"):
            st.write("**Your responses:**")
            for q_id, answer in st.session_state.quiz_answers.items():
                question_title = self.questions[q_id]['title']
                main_answer = answer.split('\n')[0]
                st.write(f"**{question_title}** {main_answer}")
    
    def _render_pattern_insights(self):
        """Render insights based on user's specific pattern combination"""
        pattern = st.session_state.unwanted_pattern
        mechanism = st.session_state.blocking_mechanism
        
        # Pattern-specific success info
        pattern_insights = {
            "Quit smoking": "Smoking is one of our highest success areas. Most clients become smoke-free after 2 sessions.",
            "Reduce anxiety": "Anxiety responds well to subconscious pattern work. We address the root triggers, not just symptoms.",
            "Improve sleep": "Sleep issues often stem from subconscious stress patterns that we can identify and resolve.",
            "Control drinking": "Drinking patterns usually have deeper emotional triggers that hypnotherapy can effectively address.",
            "Stop overeating": "Emotional eating involves subconscious reward patterns that respond well to our method.",
            "Break bad habits": "Most habits run on autopilot from the subconscious - exactly where we work."
        }
        
        # Blocking mechanism insights
        mechanism_insights = {
            "Force and control": "You tend to use force when resistance appears, creating internal battles. Our method works with your mind, not against it.",
            "Mistrust and defensiveness": "Your security system stays hyperactive, treating change as danger. We create safety for transformation.",
            "All-or-nothing thinking": "Your mind categorizes everything as perfect or failure. We help you find the middle ground where growth happens.",
            "Doing addiction": "Your worth feels tied to productivity. We help you find value in being, not just doing."
        }
        
        if pattern in pattern_insights:
            st.write(f"**Your pattern**: {pattern_insights[pattern]}")
            
        if mechanism in mechanism_insights:
            st.write(f"**Your approach**: {mechanism_insights[mechanism]}")

# Factory function for easy import
def create_quiz():
    """Factory function to create Quiz instance"""
    return Quiz()
