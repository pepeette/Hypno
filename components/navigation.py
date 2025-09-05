"""
Navigation component using streamlit-option-menu
Clean, responsive navigation for the Hypnotherapy website
"""
import streamlit as st
from streamlit_option_menu import option_menu

class Navigation:
    """Main navigation component using Streamlit components"""
    
    def __init__(self):
        self.options = ["Hypnosis", "Method", "Blog", "Testimonials", "Book Now"]
        self.icons = ["house", "gear", "book", "star", "calendar"]
        
    def create_menu(self):
        """Create and return the main navigation menu using option_menu"""
        try:
            selected = option_menu(
                menu_title=None,
                options=self.options,
                icons=self.icons,
                default_index=0,
                orientation="horizontal",
                styles=self._get_navigation_styles()
            )
            
            # Track page visit for analytics
            self._track_page_visit(selected)
            
            return selected
            
        except Exception as e:
            # Fallback to Streamlit selectbox if option_menu fails
            st.warning("Navigation component failed, using fallback")
            return st.selectbox(
                "Navigation",
                self.options,
                index=0,
                label_visibility="collapsed"
            )
    
    def _get_navigation_styles(self):
        """Get navigation styling configuration"""
        return {
            "container": {
                "padding": "0",
                "margin": "0 0 2rem 0",
                "background-color": "#F0FDFA",
                "border-radius": "12px",
                "box-shadow": "0 2px 8px rgba(0,0,0,0.05)"
            },
            "nav-link": {
                "font-size": "1rem",
                "padding": "12px 20px",
                "transition": "all 0.3s ease",
                "border-radius": "8px",
                "margin": "0 4px",
                "color": "#556D7A",
                "font-weight": "500",
                "--hover-color": "#4CA1A3"
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "font-weight": "600",
                "color": "white",
                "border-bottom": "none",
                "transform": "translateY(-1px)",
                "box-shadow": "0 4px 12px rgba(76, 161, 163, 0.3)"
            }
        }
    
    def _track_page_visit(self, selected_page):
        """Track page visit for analytics"""
        try:
            from utils.session_state import track_page_visit
            track_page_visit(selected_page)
        except ImportError:
            # Simple fallback tracking
            if 'page_visits' not in st.session_state:
                st.session_state.page_visits = []
            st.session_state.page_visits.append(selected_page)
    
    def create_breadcrumb(self, current_page, parent_page=None):
        """Create breadcrumb navigation for sub-pages using Streamlit"""
        if parent_page:
            st.caption(f"{parent_page} / **{current_page}**")
        else:
            st.caption(f"**{current_page}**")

# Factory function for clean import
def create_navigation():
    """Factory function to create Navigation instance"""
    return Navigation()
