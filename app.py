import streamlit as st
from streamlit_option_menu import option_menu

# Import page modules with error handling
try:
    from pages.home import HomePage
    from pages.method import MethodPage
    from pages.success import SuccessPage
    from pages.blog import BlogPage
    from pages.booking import BookingPage
    from components.navigation import Navigation
    from components.footer import Footer
    from components.booking_form import BookingForm
    from utils.styling import apply_global_styles
    from utils.session_state import initialize_session_state
except ImportError as e:
    st.error(f"Import error: {e}")
    st.stop()

class HypnotherapyApp:
    """Main application class for the Hypnotherapy website"""
    
    def __init__(self):
        """Initialize the application with configuration and styling"""
        if not hasattr(st.session_state, 'app_initialized'):
            self.setup_page_config()
            self.setup_styling()
            self.setup_session_state()
            st.session_state.app_initialized = True
        
        # Initialize components
        self.navigation = Navigation()
        self.footer = Footer()
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="Transform Your Life in 2 Sessions | Laetitia Sheppard",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': None,
                'Report a bug': None,
                'About': "Science-backed hypnotherapy for rapid transformation"
            }
        )
        
    def setup_styling(self):
        """Apply global CSS styling"""
        apply_global_styles()
        
    def setup_session_state(self):
        """Initialize session state variables"""
        initialize_session_state()
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page - SINGLE RENDER"""
        # Clear any existing content to prevent double rendering
        if hasattr(st.session_state, 'current_page') and st.session_state.current_page != selected_page:
            st.rerun()
        
        st.session_state.current_page = selected_page
        
        # Create page instance and render once
        if selected_page == "Home":
            if 'home_page' not in st.session_state:
                st.session_state.home_page = HomePage()
            st.session_state.home_page.render()
            
        elif selected_page == "Method":
            if 'method_page' not in st.session_state:
                st.session_state.method_page = MethodPage()
            st.session_state.method_page.render()
            
        elif selected_page == "Success":
            if 'success_page' not in st.session_state:
                st.session_state.success_page = SuccessPage()
            st.session_state.success_page.render()
            
        elif selected_page == "Blog":
            if 'blog_page' not in st.session_state:
                st.session_state.blog_page = BlogPage()
            st.session_state.blog_page.render()
            
        elif selected_page == "Book Now":
            if 'booking_page' not in st.session_state:
                st.session_state.booking_page = BookingPage()
            st.session_state.booking_page.render()
    
    def render_discovery_cta(self, page_name):
        """Render discovery call CTA on every page except Book Now"""
        if page_name != "Book Now":
            # Floating CTA
            st.markdown("""
            <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
                <a href="#discovery" onclick="document.querySelector('[data-testid=\"stSidebar\"] button').click(); return false;"
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
            </style>
            """, unsafe_allow_html=True)
    
    def run(self):
        """Main application entry point"""
        try:
            # Create navigation menu
            selected_page = self.navigation.create_menu()
            
            # Render page content (single render)
            self.render_page_content(selected_page)
            
            # Add discovery CTA
            self.render_discovery_cta(selected_page)
            
            # Always render footer
            self.footer.render()
            
        except Exception as e:
            st.error("Something went wrong. Please refresh the page.")
            if st.checkbox("Show technical details"):
                st.exception(e)

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
