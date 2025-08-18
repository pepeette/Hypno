"""
Home Page
Main landing page using Streamlit components
Features hero, value proposition, and quiz
"""
import streamlit as st
from utils.styling import render_hero_section, render_section_divider
from utils.config import AppConfig, get_years_of_experience
from utils.session_state import track_page_view
from components.quiz import Quiz

class HomePage:
    """Home page using native Streamlit components"""
    
    def __init__(self):
        self.config = AppConfig()
    
    def render(self):
        """Render the complete home page"""
        track_page_view("Home")
        
        self._render_hero_section()
        self._render_stats_section()
        self._render_value_proposition()
        self._render_quiz_section()
    
    def _render_hero_section(self):
        """Render hero section using styling utility"""
        render_hero_section(
            title="Transform Your Life in Just 2 Sessions",
            subtitle=f"Science-backed clinical hypnotherapy with {AppConfig.SUCCESS_RATE_2_SESSIONS}% success rate"
        )
    
    def _render_stats_section(self):
        """Render key statistics using Streamlit metrics"""
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Success Rate",
                f"{AppConfig.SUCCESS_RATE_2_SESSIONS}%",
                "in 2 sessions",
                help="85% of clients achieve their goals in just 2 sessions"
            )
        
        with col2:
            st.metric(
                "Experience",
                f"{get_years_of_experience()}+ years",
                f"since {AppConfig.PRACTICE_ESTABLISHED}",
                help=f"Professional practice established in {AppConfig.PRACTICE_ESTABLISHED}"
            )
        
        with col3:
            st.metric(
                "Certified",
                "LCCH & DBT",
                f"{AppConfig.LCCH_CERTIFICATION} & {AppConfig.DBT_CERTIFICATION}",
                help="London College of Clinical Hypnotherapy & Dialectical Behavioral Therapy"
            )
    
    def _render_value_proposition(self):
        """Render value proposition using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 🧠 Why Our Method Works")
        st.write("Compare traditional approaches with our proven hypnotherapy method:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ❌ Traditional Methods")
            st.write("• Fight against your programming")
            st.write("• Require constant willpower")
            st.write("• High relapse rates")
            st.write("• Take months or years")
        
        with col2:
            st.markdown("### ✅ Our Hypnotherapy")
            st.write("• Rewires your programming")
            st.write("• Works with natural patterns")
            st.write("• Long-term success")
            st.write("• Results in just 2 sessions")
        
        # Key insight
        st.info("""
        💡 **The Key Difference**: Traditional methods rely on conscious willpower (5% of your mind). 
        Our method works with your subconscious programming (95% of your mind) where lasting change happens.
        """)
    
    def _render_quiz_section(self):
        """Render quiz section using Quiz component"""
        render_section_divider()
        
        # Quiz component
        quiz = Quiz()
        quiz.render()
    
    def _render_final_cta(self):
        """Render final call-to-action using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 🚀 Ready to Begin Your Transformation?")
        st.write("Choose your preferred next step:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(
                "📞 Free Discovery Call",
                type="primary",
                use_container_width=True,
                help="15-minute consultation to discuss your goals"
            ):
                st.success("Excellent choice! Scroll down to book your call.")
        
        with col2:
            if st.button(
                "📖 Learn About Method",
                use_container_width=True,
                help="Understand our proven 2-session approach"
            ):
                st.success("Great! Navigate to Method page to learn more.")

# Factory function for easy import
def create_home_page():
    """Create HomePage instance"""
    return HomePage()
