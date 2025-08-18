"""
FIXED Navigation component with proper fallbacks
Ensures site works even without streamlit_option_menu
"""
import streamlit as st

class Navigation:
    """Main navigation component with fallback support"""
    
    def __init__(self):
        self.options = ["Home", "Method", "Success", "Blog", "Book Now"]
        self.icons = ["🏠", "⚡", "⭐", "📚", "📅"]
        
    def create_menu(self) -> str:
        """Create navigation menu with fallback"""
        try:
            # Try to use streamlit_option_menu if available
            from streamlit_option_menu import option_menu
            return self._create_fancy_menu()
        except ImportError:
            # Fallback to simple Streamlit selectbox
            return self._create_fallback_menu()
    
    def _create_fancy_menu(self) -> str:
        """Create fancy menu with streamlit_option_menu"""
        try:
            from streamlit_option_menu import option_menu
            
            selected = option_menu(
                menu_title=None,
                options=self.options,
                icons=["house", "magic", "star", "book", "calendar"],
                default_index=0,
                orientation="horizontal",
                styles={
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
                        "font-weight": "500"
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%)",
                        "font-weight": "600",
                        "color": "white",
                        "transform": "translateY(-1px)",
                        "box-shadow": "0 4px 12px rgba(76, 161, 163, 0.3)"
                    }
                }
            )
            return selected
        except Exception:
            return self._create_fallback_menu()
    
    def _create_fallback_menu(self) -> str:
        """Fallback menu using Streamlit selectbox"""
        st.markdown("""
        <div style="background: #F0FDFA; padding: 1rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
            <p style="margin: 0; color: #556D7A; font-weight: 600;">Navigate:</p>
        </div>
        """, unsafe_allow_html=True)
        
        selected = st.selectbox(
            "Choose a page:",
            self.options,
            index=0,
            format_func=lambda x: f"{self.icons[self.options.index(x)]} {x}",
            label_visibility="collapsed"
        )
        return selected
    
    def create_breadcrumb(self, current_page: str) -> None:
        """Create simple breadcrumb"""
        st.markdown(f"""
        <div style="margin: 1rem 0; padding: 0.5rem 0; border-bottom: 1px solid #CBD5E1;">
            <span style="color: #4CA1A3; font-weight: 600;">📍 {current_page}</span>
        </div>
        """, unsafe_allow_html=True)

def create_navigation():
    """Factory function to create navigation instance"""
    return Navigation()
