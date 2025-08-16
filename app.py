import streamlit as st
from streamlit_option_menu import option_menu

# Import page modules with error handling
try:
    from pages.home import HomePage
except ImportError:
    HomePage = None

try:
    from pages.method import MethodPage  
except ImportError:
    MethodPage = None

try:
    from pages.success import SuccessPage
except ImportError:
    SuccessPage = None

try:
    from pages.blog import BlogPage
except ImportError:
    BlogPage = None

try:
    from pages.booking import BookingPage
except ImportError:
    BookingPage = None

# Import shared components with error handling
try:
    from components.navigation import Navigation
except ImportError:
    Navigation = None

try:
    from components.footer import Footer
except ImportError:
    Footer = None

try:
    from components.booking_form import BookingForm
except ImportError:
    BookingForm = None

# Import utilities with error handling
try:
    from utils.styling import apply_global_styles
except ImportError:
    def apply_global_styles():
        pass

try:
    from utils.session_state import initialize_session_state
except ImportError:
    def initialize_session_state():
        pass

class HypnotherapyApp:
    """Main application class for the Hypnotherapy website"""
    
    def __init__(self):
        """Initialize the application with configuration and styling"""
        self.setup_page_config()
        self.setup_styling()
        self.setup_session_state()
        
        # Initialize components with fallbacks
        self.navigation = Navigation() if Navigation else None
        self.footer = Footer() if Footer else None
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="2-Step Hypnotherapy | Laetitia Sheppard",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://laetitiasheppard.com/help',
                'Report a bug': 'https://laetitiasheppard.com/bug-report',
                'About': "Transform your life with science-backed hypnotherapy"
            }
        )
        
    def setup_styling(self):
        """Apply global CSS styling"""
        apply_global_styles()
        
    def setup_session_state(self):
        """Initialize session state variables"""
        initialize_session_state()
    
    def render_navigation(self):
        """Render the main navigation menu"""
        if self.navigation:
            return self.navigation.create_menu()
        else:
            # Fallback navigation
            return st.selectbox(
                "Navigation",
                ["Home", "Method", "Success", "Blog", "Book Now"],
                index=0,
                label_visibility="collapsed"
            )
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        if selected_page == "Home" and HomePage:
            page = HomePage()
            page.render()
        elif selected_page == "Method" and MethodPage:
            page = MethodPage()
            page.render()
        elif selected_page == "Success" and SuccessPage:
            page = SuccessPage()
            page.render()
        elif selected_page == "Blog" and BlogPage:
            page = BlogPage()
            page.render()
        elif selected_page == "Book Now" and BookingPage:
            page = BookingPage()
            page.render()
        else:
            # Fallback content
            self.render_fallback_content(selected_page)
    
    def render_fallback_content(self, page_name):
        """Render fallback content if page components are not available"""
        st.title(f"{page_name} - Coming Soon")
        st.info(f"The {page_name} page is being prepared. Please check back soon!")
        
        if page_name == "Home":
            st.markdown("""
            ## Welcome to 2-Step Hypnotherapy
            
            Transform your life with our science-backed approach:
            - **85% success rate** in just 2 sessions
            - **Professional certification** and 10+ years experience
            - **Personalized approach** for lasting change
            
            Book your free discovery call to get started!
            """)
        elif page_name == "Method":
            st.markdown("""
            ## Our Proven 2-Step Method
            
            **Session 1: Deep Analysis** (90 minutes)
            - Uncover subconscious patterns
            - Map your unique triggers
            - Begin positive programming
            
            **Session 2: Transformation** (90 minutes)
            - Neural pathway rewiring
            - Install new behaviors
            - Lock in lasting change
            """)
    
    def render_booking_form(self, selected_page):
        """Render booking form on relevant pages"""
        if selected_page != "Book Now" and BookingForm:
            booking_form = BookingForm()
            booking_form.render_compact()
        elif selected_page != "Book Now":
            # Simple fallback booking section
            st.markdown("---")
            st.markdown("### 📞 Book Your Free Discovery Call")
            st.markdown("Contact us at: **laetitiasheppard@gmail.com**")
            st.markdown("Or call: **+66 XXX XXX XXXX**")
    
    def render_footer(self):
        """Render the footer section"""
        if self.footer:
            self.footer.render()
        else:
            # Simple fallback footer
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Laetitia Sheppard**")
                st.markdown("Certified Clinical Hypnotherapist")
                st.markdown("Bangkok, Thailand")
            
            with col2:
                st.markdown("**Contact**")
                st.markdown("📧 laetitiasheppard@gmail.com")
                st.markdown("📍 Bangkok Hypnotherapy Clinic")
            
            st.markdown("---")
            st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved")
    
    def run(self):
        """Main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Render page content
            self.render_page_content(selected_page)
            
            # Render booking form (conditional)
            self.render_booking_form(selected_page)
            
            # Render footer
            self.render_footer()
            
        except Exception as e:
            st.error("Application error occurred. Please refresh the page.")
            # Only show detailed error in development
            if st.secrets.get("debug_mode", False):
                st.exception(e)

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
