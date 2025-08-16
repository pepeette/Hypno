"""
Enhanced Quiz component for the Hypnotherapy website
Handles the 30-second suitability assessment with improved UX
"""
import streamlit as st
from utils.config import QuizConfig, AppConstants
from utils.session_state import (
    SessionStateKeys, update_quiz_answer, reset_quiz, 
    set_quiz_score, SessionStateManager
)

class QuizCalculator:
    """Handles quiz scoring and suitability calculation"""
    
    @staticmethod
    def calculate_suitability_score(answers: dict) -> int:
        """Calculate suitability percentage based on quiz answers"""
        score = 0
        scoring = QuizConfig.SCORING
        
        for question_id, answer in answers.items():
            if question_id in scoring and answer in scoring[question_id]:
                score += scoring[question_id][answer]
        
        return min(score, 100)  # Cap at 100%
    
    @staticmethod
    def get_suitability_message(score: int) -> tuple:
        """Get message, color, and icon based on suitability score"""
        suitability_ranges = QuizConfig.SUITABILITY_MESSAGES
        
        for level, (threshold, message, color, icon) in suitability_ranges.items():
            if score >= threshold:
                return message, color, icon
        
        # Default fallback
        return "Let's discuss your specific situation", "#6B7280", "💬"

class QuizProgress:
    """Handles quiz progress visualization and tracking"""
    
    @staticmethod
    def render_progress_bar(current_step: int, total_steps: int = 3):
        """Render animated progress bar"""
        progress_percentage = min((current_step - 1) / total_steps * 100, 100)
        
        progress_html = f"""
        <div style="margin: 2rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-weight: 600; color: var(--text-primary);">
                    Question {min(current_step, total_steps)} of {total_steps}
                </span>
                <span style="font-weight: 600; color: var(--accent);">
                    {int(progress_percentage)}% Complete
                </span>
            </div>
            
            <div class="progress-container">
                <div class="progress-bar" 
                     style="width: {progress_percentage}%; 
                            transition: width 0.5s ease;"></div>
            </div>
            
            <div style="display: flex; justify-content: space-between; margin-top: 1rem; 
                        font-size: 0.9rem; color: var(--text-secondary);">
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div class="progress-dot {'active' if current_step >= 1 else ''}"></div>
                    Goal
                </div>
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div class="progress-dot {'active' if current_step >= 2 else ''}"></div>
                    Duration
                </div>
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div class="progress-dot {'active' if current_step >= 3 else ''}"></div>
                    Readiness
                </div>
            </div>
        </div>
        
        <style>
        .progress-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--border);
            transition: all 0.3s ease;
        }
        .progress-dot.active {
            background: var(--accent);
            transform: scale(1.2);
        }
        </style>
        """
        
        st.markdown(progress_html, unsafe_allow_html=True)
    
    @staticmethod
    def render_step_indicator(steps: list, current_step: int):
        """Render step-by-step indicator"""
        indicator_html = "<div style='display: flex; justify-content: center; gap: 1rem; margin: 2rem 0;'>"
        
        for i, step_name in enumerate(steps, 1):
            active_class = "active" if i <= current_step else ""
            completed_class = "completed" if i < current_step else ""
            
            indicator_html += f"""
            <div style="display: flex; flex-direction: column; align-items: center; gap: 0.5rem;">
                <div class="step-circle {active_class} {completed_class}">
                    {'✓' if i < current_step else str(i)}
                </div>
                <span style="font-size: 0.8rem; color: var(--text-secondary);">
                    {step_name}
                </span>
            </div>
            """
        
        indicator_html += "</div>"
        
        step_styles = """
        <style>
        .step-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            color: var(--text-secondary);
            transition: all 0.3s ease;
        }
        .step-circle.active {
            background: var(--accent);
            color: white;
            transform: scale(1.1);
        }
        .step-circle.completed {
            background: var(--success);
            color: white;
        }
        </style>
        """
        
        st.markdown(step_styles + indicator_html, unsafe_allow_html=True)

class QuizQuestion:
    """Individual quiz question component"""
    
    def __init__(self, question_id: int, question_data: dict):
        self.question_id = question_id
        self.title = question_data["title"]
        self.options = question_data["options"]
    
    def render(self):
        """Render the quiz question with enhanced styling"""
        # Question title
        st.markdown(f"### {self.title}")
        st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
        
        # Question options
        if len(self.options) <= 4:
            # Use 2-column layout for 4 or fewer options
            cols = st.columns(2)
            for i, (icon, option, description) in enumerate(self.options):
                col = cols[i % 2]
                with col:
                    if self._render_option_button(icon, option, description, i):
                        return option
        else:
            # Use single column for more than 4 options
            for i, (icon, option, description) in enumerate(self.options):
                if self._render_option_button(icon, option, description, i):
                    return option
        
        return None
    
    def _render_option_button(self, icon: str, option: str, description: str, index: int) -> bool:
        """Render individual option button with enhanced styling"""
        button_key = f"q{self.question_id}o{index}"
        
        # Custom button styling
        button_html = f"""
        <div class="quiz-option-container" style="margin-bottom: 1rem;">
            <div class="quiz-option" onclick="document.getElementById('{button_key}').click();">
                <div class="option-icon">{icon}</div>
                <div class="option-content">
                    <div class="option-title">{option}</div>
                    <div class="option-description">{description}</div>
                </div>
                <div class="option-arrow">→</div>
            </div>
        </div>
        
        <style>
        .quiz-option {
            background: var(--card-bg);
            border: 2px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 1rem;
            min-height: 80px;
        }
        
        .quiz-option:hover {
            border-color: var(--accent);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .option-icon {
            font-size: 2rem;
            min-width: 50px;
            text-align: center;
        }
        
        .option-content {
            flex: 1;
        }
        
        .option-title {
            font-weight: 600;
            color: var(--text-primary);
            font-size: 1.1rem;
            margin-bottom: 0.3rem;
        }
        
        .option-description {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        
        .option-arrow {
            color: var(--accent);
            font-weight: bold;
            font-size: 1.2rem;
            opacity: 0;
            transition: all 0.3s ease;
        }
        
        .quiz-option:hover .option-arrow {
            opacity: 1;
            transform: translateX(5px);
        }
        </style>
        """
        
        st.markdown(button_html, unsafe_allow_html=True)
        
        # Hidden button for functionality
        return st.button(
            f"Select {option}",
            key=button_key,
            help=f"Select: {option}",
            type="primary",
            use_container_width=True,
            # Hide the button visually
            label_visibility="collapsed"
        )

class QuizResults:
    """Quiz results display component"""
    
    def __init__(self, score: int, answers: dict):
        self.score = score
        self.answers = answers
        self.message, self.color, self.icon = QuizCalculator.get_suitability_message(score)
    
    def render(self):
        """Render quiz results with recommendations"""
        self._render_score_display()
        self._render_results_breakdown()
        self._render_action_buttons()
    
    def _render_score_display(self):
        """Render the main score display"""
        result_html = f"""
        <div class="quiz-results-container">
            <div class="result-icon">{self.icon}</div>
            <div class="result-score">{self.score}%</div>
            <div class="result-title">Suitability Match</div>
            <div class="result-message">{self.message}</div>
        </div>
        
        <style>
        .quiz-results-container {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            padding: 3rem 2rem;
            margin: 2rem 0;
            text-align: center;
            border: 2px solid {self.color};
            position: relative;
            overflow: hidden;
        }
        
        .quiz-results-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, {self.color} 0%, {self.color}88 100%);
        }
        
        .result-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            animation: bounce 2s infinite;
        }
        
        .result-score {
            font-size: 3rem;
            font-weight: bold;
            color: {self.color};
            margin-bottom: 0.5rem;
        }
        
        .result-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }
        
        .result-message {
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 500px;
            margin: 0 auto;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        </style>
        """
        
        st.markdown(result_html, unsafe_allow_html=True)
    
    def _render_results_breakdown(self):
        """Render detailed results breakdown"""
        with st.expander("📊 See Your Assessment Breakdown", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Your Answers:**")
                question_labels = ["🎯 Goal", "⏰ Duration", "🚀 Readiness"]
                for i, label in enumerate(question_labels, 1):
                    answer = self.answers.get(i, "Not answered")
                    st.write(f"{label}: **{answer}**")
            
            with col2:
                st.markdown("**What This Means:**")
                if self.score >= 70:
                    st.success("✅ Excellent fit for our 2-session method")
                    st.info("You show strong indicators for successful hypnotherapy outcomes")
                elif self.score >= 55:
                    st.warning("⚡ Good potential with proper approach")
                    st.info("Hypnotherapy can help, may need tailored session planning")
                else:
                    st.info("💬 A discovery call would be beneficial")
                    st.info("Let's discuss the best approach for your specific situation")
    
    def _render_action_buttons(self):
        """Render action buttons based on score"""
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Retake Assessment", use_container_width=True, key="retake_quiz"):
                reset_quiz()
                st.rerun()
        
        with col2:
            discovery_url = AppConstants.CONTACT_INFO["discovery_call_url"]
            st.markdown(f"""
            <a href="{discovery_url}" target="_blank" class="btn btn-primary" 
               style="display: block; text-align: center; margin: 0;">
                📞 Free Discovery Call
            </a>
            """, unsafe_allow_html=True)
        
        with col3:
            if self.score >= 70:
                package_url = AppConstants.CONTACT_INFO["package_booking_url"]
                st.markdown(f"""
                <a href="{package_url}" target="_blank" class="btn btn-success"
                   style="display: block; text-align: center; margin: 0;">
                    🎯 Book Sessions Now
                </a>
                """, unsafe_allow_html=True)
            else:
                discovery_url = AppConstants.CONTACT_INFO["discovery_call_url"]
                st.markdown(f"""
                <a href="{discovery_url}" target="_blank" class="btn btn-primary"
                   style="display: block; text-align: center; margin: 0;">
                    💬 Book Discovery Call
                </a>
                """, unsafe_allow_html=True)

class Quiz:
    """Main Quiz component that orchestrates the entire quiz experience"""
    
    def __init__(self):
        self.questions = QuizConfig.QUESTIONS
        self.calculator = QuizCalculator()
        self.progress = QuizProgress()
    
    def render(self):
        """Render the complete quiz experience"""
        self._render_quiz_header()
        
        current_step = st.session_state.get(SessionStateKeys.QUIZ_STEP, 1)
        quiz_completed = st.session_state.get(SessionStateKeys.QUIZ_COMPLETED, False)
        
        if not quiz_completed:
            self._render_active_quiz(current_step)
        else:
            self._render_quiz_results()
    
    def _render_quiz_header(self):
        """Render quiz introduction and header"""
        header_html = """
        <div style="text-align: center; margin: 2rem 0;">
            <h1>30-Second Suitability Assessment</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 1rem auto;">
                Discover your readiness for transformation in 3 quick questions
            </p>
        </div>
        """
        st.markdown(header_html, unsafe_allow_html=True)
    
    def _render_active_quiz(self, current_step: int):
        """Render the active quiz questions"""
        # Progress indicator
        self.progress.render_progress_bar(current_step)
        
        # Question container
        st.markdown("""
        <div class="quiz-question-container">
        """, unsafe_allow_html=True)
        
        # Render current question
        if current_step <= len(self.questions):
            question_data = self.questions[current_step]
            question = QuizQuestion(current_step, question_data)
            
            selected_answer = question.render()
            
            if selected_answer:
                update_quiz_answer(current_step, selected_answer)
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Navigation buttons
        self._render_quiz_navigation(current_step)
    
    def _render_quiz_navigation(self, current_step: int):
        """Render quiz navigation buttons"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_step > 1:
                if st.button("← Previous", key="quiz_back", help="Go to previous question"):
                    SessionStateManager.go_to_previous_question()
                    st.rerun()
        
        with col3:
            # Skip option for non-mandatory questions
            if current_step < len(self.questions):
                if st.button("Skip →", key="quiz_skip", help="Skip this question", type="secondary"):
                    update_quiz_answer(current_step, "Skipped")
                    st.rerun()
    
    def _render_quiz_results(self):
        """Render quiz results when completed"""
        answers = st.session_state.get(SessionStateKeys.QUIZ_ANSWERS, {})
        score = self.calculator.calculate_suitability_score(answers)
        
        # Store score in session state
        set_quiz_score(score)
        
        # Render results
        results = QuizResults(score, answers)
        results.render()
    
    def reset(self):
        """Reset the quiz to initial state"""
        reset_quiz()
        st.rerun()

class QuizAnalytics:
    """Track quiz analytics and completion rates"""
    
    @staticmethod
    def track_quiz_start():
        """Track when user starts the quiz"""
        if 'quiz_analytics' not in st.session_state:
            st.session_state.quiz_analytics = {
                'started': 0,
                'completed': 0,
                'abandoned_at_step': {},
                'completion_rate': 0
            }
        
        st.session_state.quiz_analytics['started'] += 1
    
    @staticmethod
    def track_quiz_completion(score: int):
        """Track quiz completion with score"""
        if 'quiz_analytics' in st.session_state:
            st.session_state.quiz_analytics['completed'] += 1
            
            # Calculate completion rate
            started = st.session_state.quiz_analytics['started']
            completed = st.session_state.quiz_analytics['completed']
            st.session_state.quiz_analytics['completion_rate'] = (completed / started) * 100
    
    @staticmethod
    def track_quiz_abandonment(step: int):
        """Track at which step users abandon the quiz"""
        if 'quiz_analytics' in st.session_state:
            abandoned_at = st.session_state.quiz_analytics.get('abandoned_at_step', {})
            abandoned_at[step] = abandoned_at.get(step, 0) + 1
            st.session_state.quiz_analytics['abandoned_at_step'] = abandoned_at
    
    @staticmethod
    def get_quiz_analytics():
        """Get quiz analytics data"""
        return st.session_state.get('quiz_analytics', {})

class QuizValidation:
    """Validation utilities for quiz answers"""
    
    @staticmethod
    def validate_answer(question_id: int, answer: str) -> bool:
        """Validate if answer is valid for given question"""
        if question_id not in QuizConfig.QUESTIONS:
            return False
        
        valid_options = [option[1] for option in QuizConfig.QUESTIONS[question_id]["options"]]
        return answer in valid_options or answer == "Skipped"
    
    @staticmethod
    def validate_quiz_completion(answers: dict) -> tuple[bool, list]:
        """Validate if quiz is properly completed"""
        errors = []
        
        # Check if we have minimum required answers
        if len(answers) < 2:  # Allow completion with at least 2 answers
            errors.append("At least 2 questions must be answered")
        
        # Validate each answer
        for question_id, answer in answers.items():
            if not QuizValidation.validate_answer(question_id, answer):
                errors.append(f"Invalid answer for question {question_id}")
        
        return len(errors) == 0, errors

class QuizPersonalization:
    """Personalize quiz experience based on user behavior"""
    
    @staticmethod
    def get_personalized_recommendations(score: int, answers: dict) -> list:
        """Get personalized recommendations based on quiz results"""
        recommendations = []
        
        # Based on primary concern
        concern = answers.get(1, "")
        if "smoking" in concern.lower():
            recommendations.append("Consider our specialized smoking cessation program")
        elif "anxiety" in concern.lower():
            recommendations.append("Our anxiety-focused sessions have a 90% success rate")
        elif "sleep" in concern.lower():
            recommendations.append("Sleep improvement often happens after just one session")
        
        # Based on duration
        duration = answers.get(2, "")
        if "many years" in duration.lower():
            recommendations.append("Long-standing patterns often respond very well to hypnotherapy")
        elif "6 months" in duration.lower():
            recommendations.append("You're at an ideal stage for rapid transformation")
        
        # Based on readiness
        readiness = answers.get(3, "")
        if "desperate" in readiness.lower():
            recommendations.append("Your high motivation is a key predictor of success")
        elif "exploring" in readiness.lower():
            recommendations.append("A discovery call would help you understand the process better")
        
        return recommendations
    
    @staticmethod
    def get_next_best_action(score: int, answers: dict) -> dict:
        """Determine the next best action for the user"""
        if score >= 85:
            return {
                "action": "book_package",
                "message": "You're ready to book your transformation package",
                "url": AppConstants.CONTACT_INFO["package_booking_url"],
                "button_text": "Book Your Package Now"
            }
        elif score >= 70:
            return {
                "action": "book_package_or_call",
                "message": "You can book directly or have a quick call first",
                "url": AppConstants.CONTACT_INFO["discovery_call_url"],
                "button_text": "Choose Your Next Step"
            }
        else:
            return {
                "action": "discovery_call",
                "message": "A discovery call will help us create the perfect approach for you",
                "url": AppConstants.CONTACT_INFO["discovery_call_url"],
                "button_text": "Schedule Discovery Call"
            }

# Factory functions for easy import
def create_quiz():
    """Factory function to create Quiz instance"""
    return Quiz()

def calculate_quiz_score(answers: dict) -> int:
    """Calculate quiz score - utility function"""
    return QuizCalculator.calculate_suitability_score(answers)

def get_quiz_recommendations(score: int, answers: dict) -> list:
    """Get personalized recommendations - utility function"""
    return QuizPersonalization.get_personalized_recommendations(score, answers)
