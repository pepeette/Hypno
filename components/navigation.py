"""
Navigation component for the Hypnotherapy website
Handles main navigation menu creation and styling
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils.config import AppConstants
from utils.session_state import track_page_visit

class Navigation:
    """Main navigation component"""
    
    def __init__(self):
        self.options = AppConstants.NAVIGATION_OPTIONS
        self.icons = AppConstants.NAVIGATION_ICONS
        
    def create_menu(self) -> str:
        """Create and return the main navigation menu"""
        selected = option_menu(
            menu_title=None,
            options=self.options,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=self._get_navigation_styles()
        )
        
        # Track page visit for analytics
        track_page_visit(selected)
        
        return selected
    
    def _get_navigation_styles(self) -> dict:
        """Get navigation styling configuration"""
        return {
            "container": {
                "padding": "0",
                "margin": "0 0 2rem 0",
                "background-color": "transparent",
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
                "background": "linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%)",
                "font-weight": "600",
                "color": "white",
                "border-bottom": "none",
                "transform": "translateY(-1px)",
                "box-shadow": "0 4px 12px rgba(76, 161, 163, 0.3)"
            }
        }
    
    def create_breadcrumb(self, current_page: str, parent_page: str = None) -> None:
        """Create breadcrumb navigation for sub-pages"""
        breadcrumb_html = f"""
        <div style="margin: 1rem 0; padding: 0.5rem 0; 
                    border-bottom: 1px solid var(--border);">
            <nav style="font-size: 0.9rem; color: var(--text-secondary);">
        """
        
        if parent_page:
            breadcrumb_html += f"""
                <a href="#{parent_page.lower()}" 
                   style="color: var(--accent); text-decoration: none;">
                    {parent_page}
                </a>
                <span style="margin: 0 0.5rem;"> / </span>
            """
        
        breadcrumb_html += f"""
                <span style="color: var(--text-primary); font-weight: 600;">
                    {current_page}
                </span>
            </nav>
        </div>
        """
        
        st.markdown(breadcrumb_html, unsafe_allow_html=True)

class MobileNavigation:
    """Mobile-specific navigation component"""
    
    def __init__(self):
        self.options = AppConstants.NAVIGATION_OPTIONS
        self.icons = AppConstants.NAVIGATION_ICONS
    
    def create_mobile_menu(self) -> str:
        """Create mobile-optimized navigation menu"""
        # Check if we're on mobile (simplified check)
        mobile_styles = {
            "container": {
                "padding": "0",
                "margin": "0 0 1rem 0",
                "background-color": "transparent"
            },
            "nav-link": {
                "font-size": "0.9rem",
                "padding": "8px 12px",
                "transition": "all 0.3s ease",
                "border-radius": "6px",
                "margin": "0 2px",
                "color": "#556D7A"
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "font-weight": "600",
                "color": "white"
            }
        }
        
        return option_menu(
            menu_title=None,
            options=self.options,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=mobile_styles
        )

class NavigationAnalytics:
    """Track navigation analytics and user behavior"""
    
    @staticmethod
    def track_navigation_event(from_page: str, to_page: str):
        """Track navigation between pages"""
        if 'navigation_events' not in st.session_state:
            st.session_state.navigation_events = []
        
        event = {
            'from_page': from_page,
            'to_page': to_page,
            'timestamp': st.session_state.get('current_time', 'unknown')
        }
        
        st.session_state.navigation_events.append(event)
    
    @staticmethod
    def get_most_visited_pages():
        """Get analytics on most visited pages"""
        visited_pages = st.session_state.get('page_visited', set())
        return list(visited_pages)
    
    @staticmethod
    def get_navigation_flow():
        """Get user navigation flow data"""
        return st.session_state.get('navigation_events', [])

class QuickActions:
    """Quick action buttons for key user actions"""
    
    @staticmethod
    def render_floating_cta():
        """Render floating call-to-action button"""
        cta_html = """
        <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
            <a href="#discovery" 
               style="display: flex; align-items: center; gap: 8px;
                      background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                      color: white; text-decoration: none; padding: 12px 16px;
                      border-radius: 25px; font-weight: 600; font-size: 0.9rem;
                      box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4);
                      transition: all 0.3s ease; animation: pulse 2s infinite;">
                <span>📞</span>
                <span>Free Call</span>
            </a>
        </div>
        
        <style>
        @keyframes pulse {
            0% { box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }
            50% { box-shadow: 0 4px 25px rgba(76, 161, 163, 0.6); }
            100% { box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }
        }
        
        @media (max-width: 768px) {
            .floating-cta {
                bottom: 10px;
                right: 10px;
                padding: 10px 14px;
                font-size: 0.8rem;
            }
        }
        </style>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)
    
    @staticmethod
    def render_quick_nav_buttons():
        """Render quick navigation buttons for key actions"""
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎯 Take Quiz", key="quick_quiz", help="30-second assessment"):
                st.experimental_set_query_params(section="quiz")
        
        with col2:
            if st.button("📞 Free Call", key="quick_call", help="15-minute consultation"):
                st.experimental_set_query_params(section="discovery")
        
        with col3:
            if st.button("📅 Book Now", key="quick_book", help="Schedule sessions"):
                st.experimental_set_query_params(section="booking")

def create_navigation():
    """Factory function to create navigation instance"""
    return Navigation()

def create_mobile_navigation():
    """Factory function to create mobile navigation instance"""
    return MobileNavigation()
