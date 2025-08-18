"""
Navigation component for the Hypnotherapy website
Enhanced Navigation component for the Hypnotherapy website
Cleaner design, better mobile responsiveness, improved UX
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils.session_state import track_page_visit

class EnhancedNavigation:
    """Enhanced main navigation component"""
    
    def __init__(self):
        self.options = ["Home", "Method", "Success", "Blog", "Book Now"]
        self.icons = ["house", "magic", "stars", "book", "calendar"]
        
    def create_menu(self) -> str:
        """Create and return the enhanced navigation menu"""
        selected = option_menu(
            menu_title=None,
            options=self.options,
            icons=self.icons,
            default_index=0,
            orientation="horizontal",
            styles=self._get_clean_navigation_styles()
        )
        
        # Track page visit for analytics
        track_page_visit(selected)
        
        return selected
    
    def _get_clean_navigation_styles(self) -> dict:
        """Get clean, professional navigation styling"""
        return {
            "container": {
                "padding": "0.5rem 0",
                "margin": "0 0 2rem 0",
                "background-color": "#FFFFFF",
                "border-radius": "12px",
                "box-shadow": "0 2px 8px rgba(0,0,0,0.05)",
                "border": "1px solid #CBD5E1"
            },
            "nav-link": {
                "font-size": "1rem",
                "padding": "0.75rem 1.5rem",
                "transition": "all 0.3s ease",
                "border-radius": "8px",
                "margin": "0 0.25rem",
                "color": "#556D7A",
                "font-weight": "500",
                "text-align": "center"
            },
            "nav-link-selected": {
                "background": "#4CA1A3",
                "font-weight": "600",
                "color": "white",
                "transform": "translateY(-1px)",
                "box-shadow": "0 4px 12px rgba(76, 161, 163, 0.3)"
            },
            "icon": {
                "font-size": "1.1rem",
                "margin-right": "0.5rem"
            }
        }

class QuickActionBar:
    """Quick action bar for key CTAs"""
    
    def render(self):
        """Render quick action bar below navigation"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, #F3F6F8 100%); 
                    border-radius: 8px; padding: 1rem; margin-bottom: 1rem; 
                    text-align: center; border: 1px solid #CBD5E1;">
            <p style="margin: 0; color: #556D7A; font-size: 0.9rem;">
                ⚡ <strong>Quick Start:</strong> Take our 30-second assessment or book a free call
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns([1, 1.5, 0.5, 1.5, 1])
        
        with col2:
            if st.button("🎯 Take Assessment", key="quick_assessment", use_container_width=True):
                st.success("Scrolling to assessment...")
        
        with col4:
            if st.button("📞 Free Call", key="quick_call", use_container_width=True):
                st.success("Scrolling to booking...")

class MobileOptimizedNav:
    """Mobile-optimized navigation for smaller screens"""
    
    def render_mobile_menu(self):
        """Render mobile-friendly navigation"""
        # Simplified mobile navigation
        selected = st.selectbox(
            "Navigate to:",
            ["Home", "Method", "Success", "Blog", "Book Now"],
            index=0,
            key="mobile_nav"
        )
        
        return selected

class NavigationWithBranding:
    """Navigation with integrated branding"""
    
    def render_header(self):
        """Render header with branding and navigation"""
        # Header with logo/branding
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h2 style="color: #4CA1A3; margin: 0;">🧠</h2>
                <p style="margin: 0; font-size: 0.8rem; color: #556D7A;">
                    Laetitia Sheppard
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Navigation would go here
            pass

class FloatingCTA:
    """Floating call-to-action for mobile engagement"""
    
    def render(self):
        """Render floating CTA button"""
        cta_html = """
        <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
            <a href="#booking" 
               style="display: flex; align-items: center; gap: 8px;
                      background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                      color: white; text-decoration: none; padding: 12px 16px;
                      border-radius: 25px; font-weight: 600; font-size: 0.9rem;
                      box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4);
                      transition: all 0.3s ease;">
                <span>📞</span>
                <span>Free Call</span>
            </a>
        </div>
        
        <style>
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

def create_navigation():
    """Factory function to create enhanced navigation"""
    return EnhancedNavigation()

def create_quick_action_bar():
    """Factory function for quick action bar"""
    return QuickActionBar()

def create_floating_cta():
    """Factory function for floating CTA"""
    return FloatingCTA()
