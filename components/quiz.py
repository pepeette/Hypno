"""
Enhanced Quiz component with better engagement and animations
30-second suitability assessment with improved UX and visual feedback
"""
import streamlit as st
from utils.config import QuizConfig, AppConstants
from utils.session_state import (
    SessionStateKeys, update_quiz_answer, reset_quiz, 
    set_quiz_score, SessionStateManager
)

class EnhancedQuizProgress:
    """Enhanced progress visualization with animations"""
    
    @staticmethod
    def render_animated_progress(current_step: int, total_steps: int = 3):
        """Render animated progress bar with step indicators"""
        progress_percentage = min((current_step - 1) / total_steps * 100, 100)
        
        progress_html = f"""
        <div style="margin: 2rem 0;" class="fade-in-up">
            <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                <span style="font-weight: 600; color: var(--text-primary);">
                    Question {min(current_step, total_steps)} of {total_steps}
                </span>
                <span style="font-weight: 600; color: var(--accent);">
                    {int(progress_percentage)}% Complete
                </span>
            </div>
            
            <div class="progress-container">
                <div class="progress-bar" 
                     style="width: {progress_percentage}%; animation: progressFill 0.8s ease-out;"></div>
            </div>
            
            <div style="display: flex; justify-content: space-between; margin-top: 1.5rem;">
                {EnhancedQuizProgress._render_step_dots(current_step, total_steps)}
            </div>
        </div>
        
        <style>
        @keyframes progressFill {{
            from {{ width: 0%; }}
            to {{ width: {progress_percentage}%; }}
        }}
        
        @keyframes stepPulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1); }}
        }}
        
        .step-dot {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            transition: all 0.3s ease;
            border: 2px solid var(--border);
            background: var(--card-bg);
            color: var(--text-secondary);
        }}
        
        .step-dot.active {{
            background: var(--accent);
            color: white;
            border-color: var(--accent);
            animation: stepPulse 0.6s ease-out;
        }}
        
        .step-dot.completed {{
            background: var(--success);
            color: white;
            border-color: var(--success);
        }}
        </style>
        """
        
        st.markdown(progress_html, unsafe_allow_html=True)
    
    @staticmethod
    def _render_step_dots(current_step: int, total_steps: int) -> str:
        """Generate step indicator dots"""
        steps = ["🎯", "⏰", "🚀"]
        labels = ["Goal", "Duration", "Readiness"]
        
        dots_html = ""
        for i in range(total_steps):
            step_num = i + 1
            if step_num < current_step:
                class_name = "step-dot completed"
                content = "✓"
            elif step_num == current_step:
                class_name = "step-dot active"
                content = steps[i]
            else:
                class_name = "step-dot"
                content = steps[i]
            
            dots_html += f"""
            <div style="display: flex; flex-direction: column; align-items: center; gap: 0.5rem;">
                <div class="{class_name}">{content}</div>
                <span style="font-size: 0.8rem; color: var(--text-secondary); font-weight: 500;">
                    {labels[i]}
                </span>
            </div>
            """
        
        return dots_html

class EnhancedQuizQuestion:
    """Enhanced quiz question with better visual design"""
    
    def __init__(self, question_id: int, question_data: dict):
        self.question_id = question_id
        self.title = question_data["title"]
        self.options = question_data["options"]
    
    def render(self):
        """Render enhanced quiz question with animations"""
        # Question header with animation
        st.markdown(f"""
        <div class="fade-in-up" style="text-align: center; margin: 2rem 0;">
            <h2 style="color: var(--accent); margin-bottom: 1rem;">{self.title}</h2>
            <p style="color: var(--text-secondary); font-size: 1.1rem;">
                Choose the option that best describes your situation
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Render options with enhanced styling
        for i, (icon, option, description) in enumerate(self.options):
            if self._render_enhanced_option(icon, option, description, i):
                return option
        
        return None
    
    def _render_enhanced_option(self, icon: str, option: str, description: str, index: int) -> bool:
        """Render enhanced option with hover effects and animations"""
        button_key = f"q{self.question_id}o{index}"
        option_id = f"option_{self.question_id}_{index}"
        
        # Enhanced option card
        option_html = f"""
        <div class="quiz-option-wrapper" style="margin-bottom: 1rem;">
            <div class="quiz-option" id="{option_id}" 
                 onclick="document.getElementById('{button_key}').click();"
                 style="position: relative; overflow: hidden;">
                
                <div class="option-content-wrapper" style="display: flex; align-items: center; gap: 1.5rem; z-index: 2; position: relative;">
                    <div class="option-icon" style="font-size: 2.5rem; min-width: 60px; text-align: center;">
                        {icon}
                    </div>
                    <div class="option-text" style="flex: 1;">
                        <div class="option-title" style="font-weight: 600; color: var(--text-primary); 
                                                        font-size: 1.2rem; margin-bottom: 0.5rem;">
                            {option}
                        </div>
                        <div class="option-description" style="color: var(--text-secondary); 
                                                              font-size: 0.95rem; line-height: 1.4;">
                            {description}
                        </div>
                    </div>
                    <div class="option-arrow" style="color: var(--accent); font-size: 1.5rem; 
                                                   opacity: 0; transition: all 0.3s ease; transform: translateX(-10px);">
                        →
                    </div>
                </div>
                
                <div class="option-hover-effect" style="position: absolute; top: 0; left: -100%; 
                                                        width: 100%; height: 100%; 
                                                        background: linear-gradient(90deg, transparent, rgba(76, 161, 163, 0.05), transparent);
                                                        transition: left 0.6s ease; z-index: 1;"></div>
            </div>
        </div>
        
        <style>
        .quiz-option:hover .option-arrow {{
            opacity: 1;
            transform: translateX(0);
        }}
        
        .quiz-option:hover .option-hover-effect {{
            left: 100%;
        }}
        
        .quiz-option:active {{
            transform: translateY(1px);
        }}
        </style>
        """
        
        st.markdown(option_html, unsafe_allow_html=True)
        
        # Hidden button for functionality
        return st.button(
            f"Select {option}",
            key=button_key,
            help=f"Choose: {option}",
            type="primary",
            use_container_width=False,
            label_visibility="hidden"
        )

class EnhancedQuizResults:
    """Enhanced results display with animations and better recommendations"""
    
    def __init__(self, score: int, answers: dict):
        self.score = score
        self.answers = answers
        self.message, self.color, self.icon = self._get_enhanced_suitability_message(score)
        self.recommendations = self._get_personalized_recommendations()
    
    def render(self):
        """Render enhanced quiz results with animations"""
        self._render_animated_score()
        self._render_personalized_insights()
        self._render_action_plan()
        self._render_navigation_buttons()
    
    def _render_animated_score(self):
        """Render animated score reveal"""
        result_html = f"""
        <div class="quiz-results-container fade-in-up" style="text-align: center; margin: 3rem 0;">
            <div style="background: var(--card-bg); border-radius: var(--radius-lg); 
                        padding: 3rem 2rem; box-shadow: var(--shadow-lg); 
                        border: 3px solid {self.color}; position: relative; overflow: hidden;">
                
                <div class="result-decoration" style="position: absolute; top: 0; left: 0; right: 0; 
                                                     height: 6px; background: linear-gradient(90deg, {self.color}, {self.color}88);"></div>
                
                <div class="result-icon" style="font-size: 4rem; margin-bottom: 1rem; 
                                               animation: bounceIn 1s ease-out;">{self.icon}</div>
                
                <div class="result-score" style="font-size: 4rem; font-weight: bold; 
                                               color: {self.color}; margin-bottom: 1rem; 
                                               animation: countUp 1.5s ease-out;">{self.score}%</div>
                
                <div class="result-title" style="font-size: 1.8rem; font-weight: 600; 
                                                color: var(--text-primary); margin-bottom: 1rem;">
                    Suitability Match
                </div>
                
                <div class="result-message" style="font-size: 1.3rem; color: var(--text-secondary); 
                                                  max-width: 500px; margin: 0 auto;">
                    {self.message}
                </div>
            </div>
        </div>
        
        <style>
        @keyframes bounceIn {{
            0% {{ transform: scale(0.3); opacity: 0; }}
            50% {{ transform: scale(1.05); }}
            70% {{ transform: scale(0.9); }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        
        @keyframes countUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        </style>
        """
        
        st.markdown(result_html, unsafe_allow_html=True)
    
    def _render_personalized_insights(self):
        """Render personalized insights based on answers"""
        st.markdown("""
        <div class="fade-in-up" style="margin: 2rem 0;">
            <h2 style="text-align: center; color: var(--accent); margin-bottom: 2rem;">
                Your Personalized Assessment
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            self._render_answer_summary()
        
        with col2:
            self._render_recommendations()
    
    def _render_answer_summary(self):
        """Render summary of user answers"""
        st.markdown("""
        <div class="card">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">📊 Your Profile</h3>
        """, unsafe_allow_html=True)
        
        question_labels = {
            1: ("🎯", "Primary Goal"),
            2: ("⏰", "Duration"),
            3: ("🚀", "Readiness Level")
        }
        
        for i, (icon, label) in question_labels.items():
            answer = self.answers.get(i, "Not answered")
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; 
                        padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                        border-radius: var(--radius-sm); border-left: 4px solid var(--accent);">
                <span style="font-size: 1.5rem;">{icon}</span>
                <div>
                    <div style="font-weight: 600; color: var(--text-primary);">{label}</div>
                    <div style="color: var(--text-secondary);">{answer}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_recommendations(self):
        """Render personalized recommendations"""
        st.markdown("""
        <div class="card">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">💡 Personalized Insights</h3>
        """, unsafe_allow_html=True)
        
        for recommendation in self.recommendations:
            st.markdown(f"""
            <div style="display: flex; align-items: flex-start; gap: 0.8rem; margin-bottom: 1rem;">
                <span style="color: var(--success); font-size: 1.2rem; margin-top: 0.2rem;">✓</span>
                <p style="margin: 0; line-height: 1.5;">{recommendation}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_action_plan(self):
        """Render recommended action plan"""
        next_action = self._get_next_best_action()
        
        action_html = f"""
        <div class="fade-in-up" style="margin: 3rem 0;">
            <div style="background: linear-gradient(135deg, {self.color}15, {self.color}05); 
                        border-radius: var(--radius-lg); padding: 2rem; 
                        border: 2px solid {self.color}; text-align: center;">
                <h3 style="color: {self.color}; margin-bottom: 1rem;">🎯 Recommended Next Step</h3>
                <p style="font-size: 1.2rem; margin-bottom: 2rem; color: var(--text-secondary);">
                    {next_action['message']}
                </p>
                <a href="{next_action['url']}" target="_blank" 
                   style="display: inline-block; background: {self.color}; color: white; 
                          text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm); 
                          font-weight: 600; font-size: 1.1rem; transition: all 0.3s ease;
                          box-shadow: 0 4px 15px {self.color}40;">
                    {next_action['button_text']}
                </a>
            </div>
        </div>
        """
        
        st.markdown(action_html, unsafe_allow_html=True)
    
    def _render_navigation_buttons(self):
        """Render navigation and action buttons"""
        col1, col2, col3 = st.columns(3, gap="medium")
        
        with col1:
            if st.button("🔄 Retake Assessment", use_container_width=True, key="retake_quiz", type="secondary"):
                reset_quiz()
                st.rerun()
        
        with col2:
            discovery_url = AppConstants.CONTACT_INFO["discovery_call_url"]
            st.markdown(f"""
            <a href="{discovery_url}" target="_blank" class="btn" 
               style="display: block; text-align: center; width: 100%; box-sizing: border-box;">
                📞 Free Discovery Call
            </a>
            """, unsafe_allow_html=True)
        
        with col3:
            if self.score >= 70:
                package_url = AppConstants.CONTACT_INFO["package_booking_url"]
                st.markdown(f"""
                <a href="{package_url}" target="_blank" class="btn btn-success"
                   style="display: block; text-align: center; width: 100%; box-sizing: border-box;">
                    ⚡ Book Sessions
                </a>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <a href="{discovery_url}" target="_blank" class="btn"
                   style="display: block; text-align: center; width: 100%; box-sizing: border-box;">
                    💬 Get Guidance
                </a>
                """, unsafe_allow_html=True)
    
    def _get_enhanced_suitability_message(self, score: int) -> tuple:
        """Get enhanced message based on score with more nuanced feedback"""
        if score >= 85:
            return "Excellent candidate! You're ready for transformation", "#22c55e", "🌟"
        elif score >= 75:
            return "Very good fit for our 2-session method", "#65a30d", "✅"
        elif score >= 65:
            return "Good potential with our targeted approach", "#eab308", "🎯"
        elif score >= 50:
            return "Could benefit with the right preparation", "#f97316", "⚡"
        else:
            return "Let's discuss the best approach for you", "#ef4444", "💬"
    
    def _get_personalized_recommendations(self) -> list:
        """Get personalized recommendations based on answers"""
        recommendations = []
        
        # Based on primary concern
        concern = self.answers.get(1, "").lower()
        if "smoking" in concern:
            recommendations.append("Smoking cessation has our highest success rate (90%+)")
            recommendations.append("Most clients never crave cigarettes again after 2 sessions")
        elif "anxiety" in concern:
            recommendations.append("Anxiety often resolves quickly with our root-cause approach")
            recommendations.append("You'll learn to feel naturally calm in triggering situations")
        elif "sleep" in concern:
            recommendations.append("Sleep improvements often happen after just one session")
            recommendations.append("We address both physical and mental sleep barriers")
        elif "habits" in concern:
            recommendations.append("Habit change works by rewiring automatic behavioral patterns")
            recommendations.append("New positive habits will feel natural and effortless")
        
        # Based on duration
        duration = self.answers.get(2, "").lower()
        if "many years" in duration:
            recommendations.append("Long-standing patterns often respond very well to hypnotherapy")
            recommendations.append("Your brain is ready to create new, healthier neural pathways")
        elif "months" in duration:
            recommendations.append("You're at an ideal time for rapid transformation")
            recommendations.append("Recent patterns are easier to rewire than deeply ingrained ones")
        
        # Based on readiness
        readiness = self.answers.get(3, "").lower()
        if "desperate" in readiness:
            recommendations.append("Your high motivation is a key predictor of success")
            recommendations.append("Urgency often accelerates the transformation process")
        elif "exploring" in readiness:
            recommendations.append("A discovery call will help you understand the process better")
            recommendations.append("Many clients find clarity through our initial consultation")
        elif "committed" in readiness:
            recommendations.append("Your commitment level indicates excellent potential for success")
            recommendations.append("You have the mindset needed for lasting transformation")
        
        # Ensure we always have at least 3 recommendations
        if len(recommendations) < 3:
            recommendations.extend([
                "Hypnotherapy works by accessing your subconscious programming",
                "Changes happen at a neural level, making them permanent",
                "Most clients report feeling different immediately after session 1"
            ])
        
        return recommendations[:4]  # Limit to 4 recommendations
    
    def _get_next_best_action(self) -> dict:
        """Determine the next best action based on score and answers"""
        if self.score >= 85:
            return {
                "message": "You're an excellent candidate and ready to book your transformation package",
                "url": AppConstants.CONTACT_INFO["package_booking_url"],
                "button_text": "🎯 Book Your Package Now"
            }
        elif self.score >= 70:
            return {
                "message": "You're a great fit! Book directly or have a quick call to discuss your specific situation",
                "url": AppConstants.CONTACT_INFO["discovery_call_url"],
                "button_text": "📞 Schedule Discovery Call"
            }
        elif self.score >= 55:
            return {
                "message": "You have good potential. A discovery call will help us create the perfect approach",
                "url": AppConstants.CONTACT_INFO["discovery_call_url"],
                "button_text": "💬 Get Personalized Guidance"
            }
        else:
            return {
                "message": "Let's discuss your specific situation and explore the best path forward",
                "url": AppConstants.CONTACT_INFO["discovery_call_url"],
                "button_text": "🤝 Schedule Consultation"
            }

class EnhancedQuiz:
    """Main enhanced quiz component with better engagement"""
    
    def __init__(self):
        self.questions = QuizConfig.QUESTIONS
        self.progress = EnhancedQuizProgress()
    
    def render(self):
        """Render the complete enhanced quiz experience"""
        self._render_quiz_intro()
        
        current_step = st.session_state.get(SessionStateKeys.QUIZ_STEP, 1)
        quiz_completed = st.session_state.get(SessionStateKeys.QUIZ_COMPLETED, False)
        
        if not quiz_completed:
            self._render_active_quiz(current_step)
        else:
            self._render_quiz_results()
    
    def _render_quiz_intro(self):
        """Render engaging quiz introduction"""
        if not st.session_state.get(SessionStateKeys.QUIZ_STARTED, False):
            intro_html = """
            <div class="fade-in-up" style="text-align: center; margin: 2rem 0 3rem 0;">
                <div style="background: var(--card-bg); border-radius: var(--radius-lg); 
                            padding: 3rem 2rem; box-shadow: var(--shadow-md); 
                            border: 1px solid var(--border);">
                    <h1 style="color: var(--accent); margin-bottom: 1rem;">
                        30-Second Suitability Assessment
                    </h1>
                    <p style="font-size: 1.2rem; color: var(--text-secondary); 
                              max-width: 600px; margin: 1rem auto 2rem auto; line-height: 1.6;">
                        Discover your readiness for transformation with our science-based assessment. 
                        Get personalized insights in just 3 questions.
                    </p>
                    <div style="display: flex; justify-content: center; gap: 2rem; margin: 2rem 0; flex-wrap: wrap;">
                        <div style="text-align: center;">
                            <div style="font-size: 2rem; color: var(--accent); margin-bottom: 0.5rem;">⚡</div>
                            <div style="font-weight: 600; color: var(--text-primary);">30 Seconds</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">Quick & Easy</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 2rem; color: var(--accent); margin-bottom: 0.5rem;">🎯</div>
                            <div style="font-weight: 600; color: var(--text-primary);">Personalized</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">Just for You</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 2rem; color: var(--accent); margin-bottom: 0.5rem;">🔬</div>
                            <div style="font-weight: 600; color: var(--text-primary);">Science-Based</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">Proven Method</div>
                        </div>
                    </div>
                </div>
            </div>
            """
            st.markdown(intro_html, unsafe_allow_html=True)
        else:
            # Show compact header for active quiz
            st.markdown("""
            <div style="text-align: center; margin: 1rem 0;">
                <h2 style="color: var(--accent);">Suitability Assessment</h2>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_active_quiz(self, current_step: int):
        """Render the active quiz with enhanced progress"""
        # Progress indicator
        self.progress.render_animated_progress(current_step)
        
        # Question container
        if current_step <= len(self.questions):
            question_data = self.questions[current_step]
            question = EnhancedQuizQuestion(current_step, question_data)
            
            selected_answer = question.render()
            
            if selected_answer:
                # Add a small delay for better UX
                with st.spinner("Processing your answer..."):
                    import time
                    time.sleep(0.5)
                update_quiz_answer(current_step, selected_answer)
                st.rerun()
        
        # Navigation help
        if current_step > 1:
            st.markdown("""
            <div style="text-align: center; margin: 2rem 0;">
                <p style="color: var(--text-secondary); font-size: 0.9rem;">
                    💡 You can go back to change previous answers if needed
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if st.button("← Previous", key="quiz_back", type="secondary"):
                    SessionStateManager.go_to_previous_question()
                    st.rerun()
    
    def _render_quiz_results(self):
        """Render enhanced quiz results"""
        answers = st.session_state.get(SessionStateKeys.QUIZ_ANSWERS, {})
        
        # Calculate score with enhanced algorithm
        score = self._calculate_enhanced_score(answers)
        set_quiz_score(score)
        
        # Show results with celebration
        if not st.session_state.get('results_shown', False):
            st.balloons()
            st.session_state.results_shown = True
        
        results = EnhancedQuizResults(score, answers)
        results.render()
    
    def _calculate_enhanced_score(self, answers: dict) -> int:
        """Enhanced scoring algorithm with better weighting"""
        base_score = 0
        scoring = QuizConfig.SCORING
        
        # Calculate base score
        for question_id, answer in answers.items():
            if question_id in scoring and answer in scoring[question_id]:
                base_score += scoring[question_id][answer]
        
        # Apply enhancement factors
        enhanced_score = base_score
        
        # Bonus for high readiness + serious concern
        if answers.get(3) == "Very ready - I'm committed" and answers.get(1) in ["Quit smoking", "Reduce anxiety"]:
            enhanced_score += 5
        
        # Bonus for long-standing issues (better candidates)
        if answers.get(2) in ["More than 2 years", "Many years"]:
            enhanced_score += 3
        
        return min(enhanced_score, 100)  # Cap at 100%

# Factory function
def create_enhanced_quiz():
    """Factory function to create enhanced quiz instance"""
    return EnhancedQuiz()
