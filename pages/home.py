"""
Home Page
Main landing page using Streamlit components
Features focused hero card and direct path to quiz
"""
import streamlit as st
from utils.styling import render_hero_card, render_section_divider
from utils.config import AppConfig, get_years_of_experience
from utils.session_state import track_page_view
from components.quiz import Quiz

class HomePage:
    """Home page with focused messaging and clear user journey"""
    
    def __init__(self):
        self.config = AppConfig()
    
    def render(self):
        """Render the complete home page"""
        track_page_view("Home")
        
        self._render_hero_card()
        self._render_why_hypnotherapy()
        self._render_quiz_section()
    
    def _render_hero_card(self):
        """Render focused hero card with clear value proposition"""
        render_hero_card(
            title="Transform Your Life in Just 2 Sessions",
            subtitle=f"Science-backed hypnotherapy with {AppConfig.SUCCESS_RATE_2_SESSIONS}% success rate"
        )
        
        # # Key credentials in a subtle way
        # col1, col2, col3 = st.columns(3)
        
        # with col1:
        #     st.metric(
        #         "Success Rate",
        #         f"{AppConfig.SUCCESS_RATE_2_SESSIONS}%",
        #         "in 2 sessions"
        #     )
        
        # with col2:
        #     st.metric(
        #         "Experience",
        #         f"{get_years_of_experience()} years",
        #         f"since {AppConfig.PRACTICE_ESTABLISHED}"
        #     )
        
        # with col3:
        #     st.metric(
        #         "Certified",
        #         "LCCH & DBT",
        #         f"{AppConfig.LCCH_CERTIFICATION} & {AppConfig.DBT_CERTIFICATION}"
        #     )
    
    def _render_why_hypnotherapy(self):
        """Explain why hypnotherapy works - focused and clear"""
        render_section_divider()
        
        st.markdown("## Why Hypnotherapy Succeeds Where Willpower Fails")
        
        # Simple, focused explanation
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### Traditional Methods")
            st.write("Work with your conscious mind")
            st.write("Only 5% of your decisions")
            st.write("Require constant willpower")
            st.write("High failure rates")
            
        with col2:
            st.markdown("### Our Hypnotherapy")
            st.write("Works with your subconscious")
            st.write("Controls 95% of decisions")
            st.write("Natural, lasting change")
            st.write("Proven results")
        
        # Key insight without overwhelming detail
        st.info("""
        The breakthrough: Instead of fighting your programming with willpower, 
        we rewire the subconscious patterns that drive your behavior. 
        This creates effortless, permanent transformation.
        """)
    
    def _render_quiz_section(self):
        """Render quiz section with clear call-to-action"""
        render_section_divider()
        
        st.markdown("## Discover Your Transformation Potential")
        st.write("Take our 3-question assessment to see how hypnotherapy can help you")
        
        # Quiz component - main focus of the page
        quiz = Quiz()
        quiz.render()

# Factory function for easy import
def create_home_page():
    """Create HomePage instance"""
    return HomePage()
