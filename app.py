"""
Main application entry point for the Hypnotherapy website
Clean architecture using proper imports and Streamlit components
"""
import streamlit as st

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
        self.booking_form = BookingForm() if BookingForm else None
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
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
            # Fallback navigation using Streamlit selectbox
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
            # Fallback content using Streamlit components
            self.render_fallback_content(selected_page)
    
    def render_fallback_content(self, page_name):
        """Render fallback content if page components are not available"""
        st.title(f"{page_name} - Coming Soon")
        st.info(f"The {page_name} page is being prepared. Please check back soon!")
        
        if page_name == "Home":
            st.subheader("Welcome to 2-Step Hypnotherapy")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Success Rate", "85%", "in 2 sessions")
            with col2:
                st.metric("Experience", "10+ years", "certified")
            with col3:
                st.metric("Lives Changed", "500+", "since 2017")
                
            st.write("Transform your life with our science-backed approach:")
            st.write("• **85% success rate** in just 2 sessions")
            st.write("• **Professional certification** and 10+ years experience")
            st.write("• **Personalized approach** for lasting change")
            
        elif page_name == "Method":
            st.subheader("Our Proven 2-Step Method")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Session 1: Deep Analysis** (90 minutes)")
                st.write("• Uncover subconscious patterns")
                st.write("• Map your unique triggers")
                st.write("• Begin positive programming")
            with col2:
                st.write("**Session 2: Transformation** (90 minutes)")
                st.write("• Neural pathway rewiring")
                st.write("• Install new behaviors")
                st.write("• Lock in lasting change")
    
    def render_booking_form(self):
        """Render booking form on all pages"""
        if self.booking_form:
            self.booking_form.render()
        else:
            # Simple fallback booking section using Streamlit components
            st.subheader("📞 Book Your Free Discovery Call")
            with st.form("simple_booking"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("Name*")
                with col2:
                    email = st.text_input("Email*")
                
                concern = st.selectbox("Primary Concern*", 
                    ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Break Bad Habits", "Other"])
                
                if st.form_submit_button("📞 Schedule Call", type="primary", use_container_width=True):
                    if name and email and concern != "Select one...":
                        st.success("✅ Request submitted! We'll contact you within 24 hours.")
                    else:
                        st.error("Please fill in all required fields.")
    
    def render_footer(self):
        """Render the footer section"""
        if self.footer:
            self.footer.render()
        else:
            # Simple fallback footer using Streamlit components
            st.divider()
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Laetitia Sheppard")
                st.write("Certified Clinical Hypnotherapist")
                st.write("Bangkok, Thailand")
            
            with col2:
                st.subheader("Contact")
                st.write("📧 laetitiasheppard@gmail.com")
                st.write("📍 Bangkok Hypnotherapy Clinic")
            
            st.caption("© 2025 Laetitia Sheppard • All Rights Reserved")
    
    def run(self):
        """Main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Render page content
            self.render_page_content(selected_page)
            
            # Always render booking form
            self.render_booking_form()
            
            # Always render footer
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

