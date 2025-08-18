"""
Navigation Component
Sleek, responsive navigation using streamlit-option-menu
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils.session_state import track_page_view

class Navigation:
    """Clean navigation component using Streamlit components"""
    
    def __init__(self):
        self.pages = ["Home", "Method", "Success Stories", "FAQ & Blog", "Book Now"]
        self.icons = ["house-fill", "gear-fill", "star-fill", "question-circle-fill", "calendar-check-fill"]
    
    def render(self) -> str:
        """Render the main navigation menu"""
        
        selected = option_menu(
            menu_title=None,
            options=self.pages,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=self._get_navigation_styles()
        )
        
        # Track page view
        track_page_view(selected)
        
        return selected
    
    def _get_navigation_styles(self) -> dict:
        """Get navigation styling that matches our design system"""
        return {
            "container": {
                "padding": "0.75rem 0",
                "background": "linear-gradient(90deg, #FFFFFF 0%, #F0FDFA 100%)",
                "border-radius": "12px",
                "box-shadow": "0 2px 8px rgba(0,0,0,0.05)",
                "margin-bottom": "2rem",
                "border": "1px solid #CBD5E1"
            },
            "nav-link": {
                "font-size": "1rem",
                "padding": "0.75rem 1.5rem",
                "color": "#556D7A",
                "font-weight": "500",
                "transition": "all 0.3s ease",
                "border-radius": "8px",
                "margin": "0 0.25rem"
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "color": "white",
                "font-weight": "600",
                "transform": "translateY(-1px)",
                "box-shadow": "0 2px 8px rgba(76, 161, 163, 0.2)"
            },
            "icon": {
                "color": "inherit",
                "font-size": "1.1rem"
            }
        }
    
    def render_breadcrumb(self, current_page: str, parent_page: str = None):
        """Render breadcrumb using Streamlit components"""
        if parent_page:
            st.caption(f"{parent_page} → {current_page}")
        else:
            st.caption(current_page)
    
    def render_page_header(self, title: str, subtitle: str = None):
        """Render consistent page headers"""
        st.title(title)
        if subtitle:
            st.write(subtitle)
        st.markdown("---")

class MobileNavigation:
    """Mobile-optimized navigation fallback"""
    
    def __init__(self):
        self.pages = ["Home", "Method", "Success", "FAQ", "Book"]
    
    def render(self) -> str:
        """Render mobile-friendly navigation"""
        return st.selectbox(
            "Navigate to:",
            self.pages,
            label_visibility="collapsed"
        )
