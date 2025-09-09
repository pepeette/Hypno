# """
# Main application entry point for the Hypnotherapy website
# Fixed version with navigation, method page, and success page enabled
# """
# import streamlit as st

# # Import page modules with error handling
# try:
#     from pages.home import create_home_page
#     HomePage = create_home_page
# except ImportError:
#     HomePage = None

# # Enable method page
# try:
#     from pages.method import create_method_page
#     MethodPage = create_method_page
# except ImportError:
#     MethodPage = None

# # Enable success page
# try:
#     from pages.success import create_success_page
#     SuccessPage = create_success_page
# except ImportError:
#     SuccessPage = None

# try:
#     from pages.blog import create_blog_page
#     BlogPage = create_blog_page
# except ImportError:
#     BlogPage = None

# try:
#     from pages.booking import create_booking_page
#     BookingPage = create_booking_page
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
        
#         # Initialize components - navigation now enabled
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
#                 page_title="Rapid Transformation Hypnotherapy in Bangkok",
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
#                 options = ["Home", "Method", "Blog", "Testimonials", "Book Now"]
#                 icons = ["house", "gear", "book",  "star","calendar"]
            
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
                    
#             elif selected_page == "Testimonials" and SuccessPage:
#                 page_instance = SuccessPage()
#                 page_instance.render()
                    
            
#             elif selected_page == "Blog" and BlogPage:
#                 page_instance = BlogPage()
#                 page_instance.render()

#             # TODO: Enable when other pages are ready
#             elif selected_page == "Book Now" and BookingPage:
#                 page_instance = BookingPage()
#                 page_instance.render()
            
#             else:
#                 # Fallback for pages not yet implemented
#                 st.title(f"{selected_page} - Coming Soon")
#                 st.info(f"The {selected_page} page is being prepared. Please check back soon!")
                    
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
            
#             # Render page content based on selection
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
Enhanced with hidden assessment page accessible only via direct URL
"""
import streamlit as st

# Import page modules with error handling
try:
    from pages.home import create_home_page
    HomePage = create_home_page
except ImportError:
    HomePage = None

try:
    from pages.method import create_method_page
    MethodPage = create_method_page
except ImportError:
    MethodPage = None

try:
    from pages.success import create_success_page
    SuccessPage = create_success_page
except ImportError:
    SuccessPage = None

try:
    from pages.blog import create_blog_page
    BlogPage = create_blog_page
except ImportError:
    BlogPage = None

try:
    from pages.booking import create_booking_page
    BookingPage = create_booking_page
except ImportError:
    BookingPage = None

# Import assessment page (hidden)
try:
    from pages.assess import create_assess_page
    AssessPage = create_assess_page
except ImportError:
    AssessPage = None

# Import shared components with error handling
try:
    from components.navigation import create_navigation
    Navigation = create_navigation
except ImportError:
    Navigation = None

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
        
        # Initialize components
        self.navigation = Navigation() if Navigation else None
        self.footer = Footer() if Footer else None
        self.booking_form = BookingForm() if BookingForm else None
        
        # Check for hidden page access
        self.hidden_page = self._check_hidden_page_access()
        
    def setup_page_config(self):
        """Configure Streamlit page settings using config"""
        if PageConfig:
            PageConfig.setup()
        else:
            # Minimal fallback config
            st.set_page_config(
                page_title="Rapid Transformation Hypnotherapy in Bangkok",
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
    
    def _check_hidden_page_access(self):
        """Check URL parameters for hidden page access"""
        try:
            # Get URL parameters
            query_params = st.experimental_get_query_params()
            
            # Check for assessment page access
            if 'page' in query_params and 'assess' in query_params['page']:
                return 'assess'
                
            # Check for other hidden pages if needed
            # if 'page' in query_params and 'admin' in query_params['page']:
            #     return 'admin'
                
            return None
        except:
            return None
    
    def render_navigation(self):
        """Render the main navigation menu (only for public pages)"""
        if self.hidden_page:
            # Don't show navigation for hidden pages
            return self.hidden_page
            
        if self.navigation:
            return self.navigation.create_menu()
        else:
            # Import navigation options from config
            try:
                from utils.config import AppConstants
                options = AppConstants.NAVIGATION_OPTIONS
                icons = AppConstants.NAVIGATION_ICONS
            except ImportError:
                options = ["Home", "Method", "Blog", "Testimonials", "Book Now"]
                icons = ["house", "gear", "book", "star", "calendar"]
            
            # Simple fallback navigation
            from streamlit_option_menu import option_menu
            
            return option_menu(
                menu_title=None,
                options=options,
                icons=icons,
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "0", "margin": "0 0 2rem 0"},
                    "nav-link": {"font-size": "1rem", "color": "#556D7A"},
                    "nav-link-selected": {"background": "#4CA1A3", "color": "white"}
                }
            )
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        try:
            # Handle hidden pages first
            if selected_page == "assess" and AssessPage:
                self._render_hidden_assessment_page()
                return
                
            # Handle regular navigation pages
            if selected_page == "Home" and HomePage:
                page_instance = HomePage()
                page_instance.render()
                    
            elif selected_page == "Method" and MethodPage:
                page_instance = MethodPage()
                page_instance.render()
                    
            elif selected_page == "Testimonials" and SuccessPage:
                page_instance = SuccessPage()
                page_instance.render()
                    
            elif selected_page == "Blog" and BlogPage:
                page_instance = BlogPage()
                page_instance.render()

            elif selected_page == "Book Now" and BookingPage:
                page_instance = BookingPage()
                page_instance.render()
            
            else:
                # Fallback for pages not yet implemented
                st.title(f"{selected_page} - Coming Soon")
                st.info(f"The {selected_page} page is being prepared. Please check back soon!")
                    
        except Exception as e:
            st.error(f"Error loading {selected_page} page. Please try refreshing.")
            if st.secrets.get("debug_mode", False):
                st.exception(e)
    
    def _render_hidden_assessment_page(self):
        """Render the hidden assessment page"""
        if AssessPage:
            # Add a discrete header indicating this is a hidden page
            st.markdown("""
            <div style="background: #f0f8ff; padding: 0.5rem 1rem; border-radius: 4px; 
                        margin-bottom: 1rem; border-left: 4px solid #4CA1A3;">
                <small style="color: #4CA1A3;">
                    🔒 Confidential assessment portal
                </small>
            </div>
            """, unsafe_allow_html=True)
            
            page_instance = AssessPage()
            page_instance.render()
        else:
            st.error("Assessment page not available. Please contact support.")
    
    def render_booking_form(self, selected_page):
        """Render booking form on public pages only"""
        # Don't show booking form on hidden pages
        if self.hidden_page:
            return
            
        if selected_page != "Book Now" and self.booking_form:
            self.booking_form.render()
    
    def render_footer(self):
        """Render the footer section on public pages only"""
        # Don't show footer on hidden pages
        if self.hidden_page:
            return
            
        if self.footer:
            self.footer.render()
    
    def run(self):
        """Main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Render page content based on selection
            self.render_page_content(selected_page)
            
            # Render booking form (except on hidden pages and Book Now page)
            self.render_booking_form(selected_page)
            
            # Always render footer (except on hidden pages)
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
