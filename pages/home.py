"""
Home page component for the Hypnotherapy website
FIXED: Using working code from old app.py
"""
import streamlit as st

class HomePage:
    """Main home page component using proven working code"""
    
    def __init__(self):
        # Initialize session state if needed
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
            st.session_state.quiz_step = 1
    
    def reset_quiz(self):
        """Reset quiz state"""
        st.session_state.quiz_answers = {}
        st.session_state.quiz_step = 1

    def handle_quiz_answer(self, question_id, answer):
        """Store quiz answer and advance to next question"""
        st.session_state.quiz_answers[question_id] = answer
        st.session_state.quiz_step += 1

    def calculate_suitability_score(self, answers):
        """Calculate suitability percentage based on quiz answers"""
        score = 0
        
        # Question 1: What are you looking to change? (0-40 points)
        concern_scores = {
            "Quit smoking": 40,
            "Reduce anxiety": 35,
            "Improve sleep": 30,
            "Break bad habits": 35,
            "Other": 25
        }
        score += concern_scores.get(answers.get(1, ""), 0)
        
        # Question 2: How long have you struggled? (0-30 points)
        duration_scores = {
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30,
            "Many years": 25
        }
        score += duration_scores.get(answers.get(2, ""), 0)
        
        # Question 3: How ready are you? (0-30 points)
        readiness_scores = {
            "Just exploring options": 10,
            "Somewhat ready": 20,
            "Very ready - I'm committed": 30,
            "Desperate for change": 25
        }
        score += readiness_scores.get(answers.get(3, ""), 0)
        
        return min(score, 100)  # Cap at 100%

    def get_suitability_message(self, score):
        """Get message and color based on suitability score"""
        if score >= 85:
            return "Excellent candidate for hypnotherapy!", "#22c55e", "🌟"
        elif score >= 70:
            return "Very good fit for our 2-session method", "#65a30d", "✅"
        elif score >= 55:
            return "Good potential with hypnotherapy", "#eab308", "🎯"
        elif score >= 40:
            return "May benefit with additional preparation", "#f97316", "⚡"
        else:
            return "Consider a discovery call first", "#ef4444", "💬"

    def show_hero(self):
        """Display the hero section - WORKING CODE from old app"""
        st.markdown("""
        <div class="hero">
            <h1>Break Free in Just 2 Sessions</h1>
            <p>Clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits</p>
        </div>
        """, unsafe_allow_html=True)

    def show_quiz(self):
        """Display the enhanced quiz component - WORKING CODE from old app"""
        
        # Quiz header
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h1>30-Second Suitability Assessment</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary);">
                Discover your readiness for transformation in 3 quick questions
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        current_step = st.session_state.quiz_step
        progress_percentage = min((current_step - 1) / 3 * 100, 100)
        
        st.markdown(f"""
        <div style="margin: 2rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-weight: 600;">Question {min(current_step, 3)} of 3</span>
                <span style="font-weight: 600;">{int(progress_percentage)}% Complete</span>
            </div>
            <div style="background-color: var(--border); height: 8px; border-radius: 4px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, var(--accent) 0%, #22c55e 100%); 
                            height: 100%; width: {progress_percentage}%; transition: width 0.5s ease;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div style="width: 8px; height: 8px; border-radius: 50%; 
                               background: {'var(--accent)' if current_step >= 1 else 'var(--border)'};"></div>
                    Goal
                </div>
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div style="width: 8px; height: 8px; border-radius: 50%; 
                               background: {'var(--accent)' if current_step >= 2 else 'var(--border)'};"></div>
                    Duration
                </div>
                <div style="display: flex; align-items: center; gap: 0.3rem;">
                    <div style="width: 8px; height: 8px; border-radius: 50%; 
                               background: {'var(--accent)' if current_step >= 3 else 'var(--border)'};"></div>
                    Readiness
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Question content area
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); min-height: 300px;">
        """, unsafe_allow_html=True)
        
        # Question 1
        if current_step == 1:
            st.markdown("### 🎯 What would you most like to change or improve?")
            st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
            
            options = [
                ("🚭", "Quit smoking", "Break free from tobacco addiction"),
                ("😌", "Reduce anxiety", "Find calm and peace of mind"), 
                ("😴", "Improve sleep", "Get better, deeper rest"),
                ("🔄", "Break bad habits", "Change unwanted behaviors"),
                ("❓", "Other", "Something else I'd like to change")
            ]
            
            cols = st.columns(2)
            for i, (icon, option, desc) in enumerate(options):
                col = cols[i % 2]
                with col:
                    if st.button(
                        f"{icon} **{option}**\n\n{desc}",
                        key=f"q1o{i}",
                        use_container_width=True,
                        help=f"Select if you want to {option.lower()}"
                    ):
                        self.handle_quiz_answer(1, option)
                        st.rerun()

        # Question 2  
        elif current_step == 2:
            st.markdown("### ⏰ How long have you been dealing with this challenge?")
            st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
            
            options = [
                ("🆕", "Less than 6 months", "Relatively new challenge"),
                ("📅", "6 months to 2 years", "Moderate duration"),
                ("⏳", "More than 2 years", "Long-standing issue"),
                ("🔄", "Many years", "Deeply ingrained pattern")
            ]
            
            cols = st.columns(2)
            for i, (icon, option, desc) in enumerate(options):
                col = cols[i % 2]
                with col:
                    if st.button(
                        f"{icon} **{option}**\n\n{desc}",
                        key=f"q2o{i}",
                        use_container_width=True
                    ):
                        self.handle_quiz_answer(2, option)
                        st.rerun()

        # Question 3
        elif current_step == 3:
            st.markdown("### 🚀 How ready are you to make this change happen?")
            st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
            
            options = [
                ("🤔", "Just exploring options", "Learning about possibilities"),
                ("👍", "Somewhat ready", "Interested and considering"),
                ("💪", "Very ready - I'm committed", "Fully motivated to change"),
                ("🔥", "Desperate for change", "Need transformation now")
            ]
            
            for i, (icon, option, desc) in enumerate(options):
                if st.button(
                    f"{icon} **{option}**\n\n{desc}",
                    key=f"q3o{i}",
                    use_container_width=True
                ):
                    self.handle_quiz_answer(3, option)
                    st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Show results if quiz is complete
        if len(st.session_state.quiz_answers) == 3:
            score = self.calculate_suitability_score(st.session_state.quiz_answers)
            message, color, icon = self.get_suitability_message(score)
            
            st.markdown(f"""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-md); 
                        border: 2px solid {color}; text-align: center;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
                <h2 style="color: {color}; margin-bottom: 1rem;">
                    {score}% Suitability Match
                </h2>
                <p style="font-size: 1.2rem; color: var(--text-primary); margin-bottom: 2rem;">
                    {message}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Results breakdown
            with st.expander("📊 See Your Assessment Breakdown", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Your Answers:**")
                    st.write(f"🎯 **Goal:** {st.session_state.quiz_answers.get(1, 'Not answered')}")
                    st.write(f"⏰ **Duration:** {st.session_state.quiz_answers.get(2, 'Not answered')}")  
                    st.write(f"🚀 **Readiness:** {st.session_state.quiz_answers.get(3, 'Not answered')}")
                
                with col2:
                    st.markdown("**What This Means:**")
                    if score >= 70:
                        st.success("✅ Excellent fit for our 2-session method")
                        st.info("You show strong indicators for successful hypnotherapy outcomes")
                    elif score >= 55:
                        st.warning("⚡ Good potential with proper approach")
                        st.info("Hypnotherapy can help, may need tailored session planning")
                    else:
                        st.info("💬 A discovery call would be beneficial")
                        st.info("Let's discuss the best approach for your specific situation")
            
            # Action buttons
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if st.button("🔄 Retake Assessment", use_container_width=True):
                    self.reset_quiz()
                    st.rerun()
            
            with col2:
                st.markdown("""
                <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank"
                   style="display: block; background-color: var(--accent); color: white; 
                          text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                          font-weight: 600; text-align: center; transition: var(--transition);">
                    📞 Free Discovery Call
                </a>
                """, unsafe_allow_html=True)
            
            with col3:
                if score >= 70:
                    st.markdown("""
                    <a href="https://calendly.com/laetitiasheppard/package" target="_blank"
                       style="display: block; background-color: #22c55e; color: white; 
                              text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                              font-weight: 600; text-align: center; transition: var(--transition);">
                        🎯 Book Sessions Now
                    </a>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank"
                       style="display: block; background-color: var(--accent); color: white; 
                              text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                              font-weight: 600; text-align: center; transition: var(--transition);">
                        💬 Book Discovery Call
                    </a>
                    """, unsafe_allow_html=True)

        # Back button for non-completed quiz
        elif current_step > 1:
            if st.button("← Back to Previous Question", key="quiz_back"):
                st.session_state.quiz_step -= 1
                # Remove the last answer
                if current_step - 1 in st.session_state.quiz_answers:
                    del st.session_state.quiz_answers[current_step - 1]
                st.rerun()

    def render(self):
        """Render complete home page using working components"""
        try:
            # Hero section
            self.show_hero()
            
            # Main quiz component - the centerpiece
            self.show_quiz()
            
        except Exception as e:
            st.error(f"Error rendering home page: {e}")
            # Minimal fallback only if there's an actual error
            st.title("Transform Your Life in Just 2 Sessions")
            st.markdown("Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits")
            
            if st.button("📞 Book Free Discovery Call", type="primary"):
                st.success("We'll contact you within 24 hours!")

def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
