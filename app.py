import streamlit as st
from streamlit_option_menu import option_menu

# Import page modules
from pages.home import HomePage
from pages.method import MethodPage  
from pages.success import SuccessPage
from pages.blog import BlogPage
from pages.booking import BookingPage

# Import shared components
from components.navigation import Navigation
from components.footer import Footer
from components.quiz import Quiz
from components.booking_form import BookingForm

# Import utilities and config
from utils.config import PageConfig, SMTPConfig
from utils.styling import apply_global_styles
from utils.session_state import initialize_session_state

class HypnotherapyApp:
    """Main application class for the Hypnotherapy website"""
    
    def __init__(self):
        """Initialize the application with configuration and styling"""
        self.setup_page_config()
        self.setup_styling()
        self.setup_session_state()
        self.navigation = Navigation()
        self.footer = Footer()
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        PageConfig.setup()
        
    def setup_styling(self):
        """Apply global CSS styling"""
        apply_global_styles()
        
    def setup_session_state(self):
        """Initialize session state variables"""
        initialize_session_state()
    
    def render_navigation(self):
        """Render the main navigation menu"""
        return self.navigation.create_menu()
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        page_map = {
            "Home": HomePage(),
            #"Method": MethodPage(),
            "Success": SuccessPage(), 
            "Blog": BlogPage(),
            #"Book Now": BookingPage()
        }
        
        if selected_page in page_map:
            page_map[selected_page].render()
        else:
            st.error(f"Page '{selected_page}' not found")
    
    def render_booking_form(self, selected_page):
        """Render booking form on relevant pages"""
        # Show booking form on all pages except the dedicated booking page
        if selected_page != "Book Now":
            booking_form = BookingForm()
            booking_form.render()
    
    def render_footer(self):
        """Render the footer section"""
        self.footer.render()
    
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
            st.error(f"Application error: {str(e)}")
            if st.secrets.get("debug_mode", False):
                st.exception(e)

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
