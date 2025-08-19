# """
# Main application entry point for the Hypnotherapy website
# Clean architecture ensuring navigation, content, booking_form, and footer render properly
# """
# import streamlit as st

# # Import page modules with error handling
# try:
#     from pages.home import create_home_page
#     HomePage = create_home_page
# except ImportError:
#     HomePage = None

# try:
#     from pages.method import create_method_page
#     MethodPage = create_method_page
# except ImportError:
#     MethodPage = None

# try:
#     from pages.success import SuccessPage
# except ImportError:
#     SuccessPage = None

# try:
#     from pages.blog import BlogPage
# except ImportError:
#     BlogPage = None

# try:
#     from pages.booking import BookingPage
# except ImportError:
#     BookingPage = None

# # Import shared components with error handling
# try:
#     from components.navigation import create_navigation
#     Navigation = create_navigation
# except ImportError:
#     Navigation = None

# try:
#     from components.footer import create_footer
#     Footer = create_footer
# except ImportError:
#     Footer = None

# try:
#     from components.booking_form import create_booking_form
#     BookingForm = create_booking_form
# except ImportError:
#     BookingForm = None

# # Import utilities with error handling
# try:
#     from utils.config import PageConfig
# except ImportError:
#     PageConfig = None

# try:
#     from utils.styling import apply_global_styles
# except ImportError:
#     def apply_global_styles():
#         pass

# try:
#     from utils.session_state import initialize_session_state
# except ImportError:
#     def initialize_session_state():
#         pass

# class HypnotherapyApp:
#     """Main application class for the Hypnotherapy website"""
    
#     def __init__(self):
#         """Initialize the application with configuration and styling"""
#         self.setup_page_config()
#         self.setup_styling()
#         self.setup_session_state()
        
#         # Initialize components - call factory functions properly
#         self.navigation = Navigation() if Navigation else None
#         self.footer = Footer() if Footer else None
#         self.booking_form = BookingForm() if BookingForm else None
        
#     def setup_page_config(self):
#         """Configure Streamlit page settings using config"""
#         if PageConfig:
#             PageConfig.setup()
#         else:
#             # Minimal fallback config
#             st.set_page_config(
#                 page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
#                 page_icon="🧠",
#                 layout="wide",
#                 initial_sidebar_state="collapsed"
#             )
        
#     def setup_styling(self):
#         """Apply global CSS styling"""
#         apply_global_styles()
        
#     def setup_session_state(self):
#         """Initialize session state variables"""
#         initialize_session_state()
    
#     def render_navigation(self):
#         """Render the main navigation menu"""
#         if self.navigation:
#             return self.navigation.create_menu()
#         else:
#             # Import navigation options from config
#             try:
#                 from utils.config import AppConstants
#                 options = AppConstants.NAVIGATION_OPTIONS
#                 icons = AppConstants.NAVIGATION_ICONS
#             except ImportError:
#                 options = ["Home", "Method", "Success", "Blog", "Book Now"]
#                 icons = ["house", "gear", "star", "book", "calendar"]
            
#             # Simple fallback navigation
#             from streamlit_option_menu import option_menu
            
#             return option_menu(
#                 menu_title=None,
#                 options=options,
#                 icons=icons,
#                 default_index=0,
#                 orientation="horizontal",
#                 styles={
#                     "container": {"padding": "0", "margin": "0 0 2rem 0"},
#                     "nav-link": {"font-size": "1rem", "color": "#556D7A"},
#                     "nav-link-selected": {"background": "#4CA1A3", "color": "white"}
#                 }
#             )
    
#     def render_page_content(self, selected_page):
#         """Render content based on selected navigation page"""
#         try:
#             if selected_page == "Home" and HomePage:
#                 page_instance = HomePage()
#                 page_instance.render()
                    
#             elif selected_page == "Method" and MethodPage:
#                 page_instance = MethodPage()
#                 page_instance.render()
                    
#             elif selected_page == "Success" and SuccessPage:
#                 page_instance = SuccessPage()
#                 page_instance.render()
                    
#             elif selected_page == "Blog" and BlogPage:
#                 page_instance = BlogPage()
#                 page_instance.render()
                    
#             elif selected_page == "Book Now" and BookingPage:
#                 page_instance = BookingPage()
#                 page_instance.render()
                    
#         except Exception as e:
#             st.error(f"Error loading {selected_page} page. Please try refreshing.")
#             if st.secrets.get("debug_mode", False):
#                 st.exception(e)
    
#     def render_booking_form(self, selected_page):
#         """Render booking form on all pages except Book Now"""
#         if selected_page != "Book Now" and self.booking_form:
#             self.booking_form.render()
    
#     def render_footer(self):
#         """Render the footer section on all pages"""
#         if self.footer:
#             self.footer.render()
    
#     def run(self):
#         """Main application entry point"""
#         try:
#             # Render navigation and get selected page
#             selected_page = self.render_navigation()
            
#             # Render page content
#             self.render_page_content(selected_page)
            
#             # Render booking form (except on Book Now page)
#             self.render_booking_form(selected_page)
            
#             # Always render footer
#             self.render_footer()
            
#         except Exception as e:
#             st.error("Application error occurred. Please refresh the page.")
#             if st.secrets.get("debug_mode", False):
#                 st.exception(e)

# def main():
#     """Application entry point"""
#     app = HypnotherapyApp()
#     app.run()

# if __name__ == "__main__":
#     main()

"""
Main application entry point for the Hypnotherapy website
Minimal version for development - Home page only with booking form and footer
"""
import streamlit as st

# Import page modules with error handling
try:
    from pages.home import create_home_page
    HomePage = create_home_page
except ImportError:
    HomePage = None

# TODO: Enable these when pages are ready
# try:
#     from pages.method import create_method_page
#     MethodPage = create_method_page
# except ImportError:
#     MethodPage = None

# try:
#     from pages.success import SuccessPage
# except ImportError:
#     SuccessPage = None

# try:
#     from pages.blog import BlogPage
# except ImportError:
#     BlogPage = None

# try:
#     from pages.booking import BookingPage
# except ImportError:
#     BookingPage = None

# Import shared components with error handling
# TODO: Enable navigation when ready
# try:
#     from components.navigation import create_navigation
#     Navigation = create_navigation
# except ImportError:
#     Navigation = None

try:
    from components.footer import create_footer
    Footer = create_footer
except ImportError:
    Footer = None

try:
    from components.booking_form import create_booking_form
    BookingForm = create_booking_form
except ImportError:
    BookingForm = None

# Import utilities with error handling
try:
    from utils.config import PageConfig
except ImportError:
    PageConfig = None

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
        
        # Initialize components - only footer and booking form for now
        # self.navigation = Navigation() if Navigation else None  # TODO: Enable when ready
        self.footer = Footer() if Footer else None
        self.booking_form = BookingForm() if BookingForm else None
        
    def setup_page_config(self):
        """Configure Streamlit page settings using config"""
        if PageConfig:
            PageConfig.setup()
        else:
            # Minimal fallback config
            st.set_page_config(
                page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
                page_icon="🧠",
                layout="wide",
                initial_sidebar_state="collapsed"
            )
        
    def setup_styling(self):
        """Apply global CSS styling"""
        apply_global_styles()
        
    def setup_session_state(self):
        """Initialize session state variables"""
        initialize_session_state()
    
    # TODO: Enable navigation when other pages are ready
    # def render_navigation(self):
    #     """Render the main navigation menu"""
    #     if self.navigation:
    #         return self.navigation.create_menu()
    #     else:
    #         # Import navigation options from config
    #         try:
    #             from utils.config import AppConstants
    #             options = AppConstants.NAVIGATION_OPTIONS
    #             icons = AppConstants.NAVIGATION_ICONS
    #         except ImportError:
    #             options = ["Home", "Method", "Success", "Blog", "Book Now"]
    #             icons = ["house", "gear", "star", "book", "calendar"]
            
    #         # Simple fallback navigation
    #         from streamlit_option_menu import option_menu
            
    #         return option_menu(
    #             menu_title=None,
    #             options=options,
    #             icons=icons,
    #             default_index=0,
    #             orientation="horizontal",
    #             styles={
    #                 "container": {"padding": "0", "margin": "0 0 2rem 0"},
    #                 "nav-link": {"font-size": "1rem", "color": "#556D7A"},
    #                 "nav-link-selected": {"background": "#4CA1A3", "color": "white"}
    #             }
    #         )
    
    def render_page_content(self):
        """Render Home page content only for now"""
        try:
            if HomePage:
                page_instance = HomePage()
                page_instance.render()
            else:
                # Simple fallback if home page not available
                st.title("Welcome to Clinical Hypnotherapy Bangkok")
                st.write("Transform your life in just 2 sessions with science-backed hypnotherapy")
                
        except Exception as e:
            st.error("Error loading page. Please try refreshing.")
            if st.secrets.get("debug_mode", False):
                st.exception(e)
    
    # TODO: Enable when other pages exist
    # def render_page_content(self, selected_page):
    #     """Render content based on selected navigation page"""
    #     try:
    #         if selected_page == "Home" and HomePage:
    #             page_instance = HomePage()
    #             page_instance.render()
                    
    #         elif selected_page == "Method" and MethodPage:
    #             page_instance = MethodPage()
    #             page_instance.render()
                    
    #         elif selected_page == "Success" and SuccessPage:
    #             page_instance = SuccessPage()
    #             page_instance.render()
                    
    #         elif selected_page == "Blog" and BlogPage:
    #             page_instance = BlogPage()
    #             page_instance.render()
                    
    #         elif selected_page == "Book Now" and BookingPage:
    #             page_instance = BookingPage()
    #             page_instance.render()
                    
    #     except Exception as e:
    #         st.error(f"Error loading {selected_page} page. Please try refreshing.")
    #         if st.secrets.get("debug_mode", False):
    #             st.exception(e)
    
    def render_booking_form(self):
        """Render booking form - always show for now"""
        if self.booking_form:
            self.booking_form.render()
    
    # TODO: Enable when other pages exist
    # def render_booking_form(self, selected_page):
    #     """Render booking form on all pages except Book Now"""
    #     if selected_page != "Book Now" and self.booking_form:
    #         self.booking_form.render()
    
    def render_footer(self):
        """Render the footer section on all pages"""
        if self.footer:
            self.footer.render()
    
    def run(self):
        """Main application entry point - simplified for development"""
        try:
            # TODO: Enable navigation when other pages are ready
            # selected_page = self.render_navigation()
            
            # Render Home page content only
            self.render_page_content()
            
            # Always render booking form for now
            self.render_booking_form()
            
            # Always render footer
            self.render_footer()
            
        except Exception as e:
            st.error("Application error occurred. Please refresh the page.")
            if st.secrets.get("debug_mode", False):
                st.exception(e)

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
