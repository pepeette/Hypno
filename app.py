# """
# Main application entry point for the Hypnotherapy website
# Enhanced with hidden assessment page accessible only via direct URL
# """
# import streamlit as st
# import os

# # Disable file watching in production
# if os.getenv('STREAMLIT_ENV') == 'production':
#     st.set_option('server.fileWatcherType', 'none')
    
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

# # Import assessment page (hidden)
# try:
#     from pages.assess import create_assess_page
#     AssessPage = create_assess_page
# except ImportError:
#     AssessPage = None

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
        
#         # Initialize components
#         self.navigation = Navigation() if Navigation else None
#         self.footer = Footer() if Footer else None
#         self.booking_form = BookingForm() if BookingForm else None
        
#         # Check for hidden page access
#         self.hidden_page = self._check_hidden_page_access()
        
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

#     def _check_hidden_page_access(self):
#         """Check URL parameters for hidden page access"""
#         try:
#             # Get URL parameters - FIXED: Using new st.query_params
#             query_params = st.query_params
            
#             # Check for assessment page access
#             if 'page' in query_params and 'assess' in query_params['page']:
#                 return 'assess'
                
#             # Check for other hidden pages if needed
#             # if 'page' in query_params and 'admin' in query_params['page']:
#             #     return 'admin'
                
#             return None
#         except:
#             return None
        
    
#     def render_navigation(self):
#         """Render the main navigation menu (only for public pages)"""
#         if self.hidden_page:
#             # Don't show navigation for hidden pages
#             return self.hidden_page
            
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
#                 icons = ["house", "gear", "book", "star", "calendar"]
            
#             # Simple fallback navigation
#             from streamlit_option_menu import option_menu
            
#             return option_menu(
#                 menu_title=None,
#                 options=options,
#                 icons=icons,
#                 default_index=0,
#                 key="main_navigation",
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
#             # Handle hidden pages first
#             if selected_page == "assess" and AssessPage:
#                 self._render_hidden_assessment_page()
#                 return
                
#             # Handle regular navigation pages
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
    
#     def _render_hidden_assessment_page(self):
#         """Render the hidden assessment page"""
#         if AssessPage:
#             # Add a discrete header indicating this is a hidden page
#             st.markdown("""
#             <div style="background: #f0f8ff; padding: 0.5rem 1rem; border-radius: 4px; 
#                         margin-bottom: 1rem; border-left: 4px solid #4CA1A3;">
#                 <small style="color: #4CA1A3;">
#                     🔒 Confidential assessment portal
#                 </small>
#             </div>
#             """, unsafe_allow_html=True)
            
#             page_instance = AssessPage()
#             page_instance.render()
#         else:
#             st.error("Assessment page not available. Please contact support.")
    
#     def render_booking_form(self, selected_page):
#         """Render booking form on public pages only"""
#         # Don't show booking form on hidden pages
#         if self.hidden_page:
#             return
            
#         if selected_page != "Book Now" and self.booking_form:
#             self.booking_form.render()
    
#     def render_footer(self):
#         """Render the footer section on public pages only"""
#         # Don't show footer on hidden pages
#         if self.hidden_page:
#             return
            
#         if self.footer:
#             self.footer.render()
    
#     def run(self):
#         """Main application entry point"""
#         try:
#             # Render navigation and get selected page
#             selected_page = self.render_navigation()
            
#             # Render page content based on selection
#             self.render_page_content(selected_page)
            
#             # Render booking form (except on hidden pages and Book Now page)
#             self.render_booking_form(selected_page)
            
#             # Always render footer (except on hidden pages)
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
Updated with storage client and admin interface integration
"""
import streamlit as st
import os

from datetime import datetime

# Disable file watching in production
if os.getenv('STREAMLIT_ENV') == 'production':
    st.set_option('server.fileWatcherType', 'none')

# Import storage utilities with error handling
try:
    from utils.storage_factory import create_storage_client
except ImportError:
    def create_storage_client():
        return None

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

# Import admin interface (hidden)
try:
    from utils.admin_interface import render_admin_interface
    AdminInterface = render_admin_interface
except ImportError:
    AdminInterface = None

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
        self.setup_storage()
        
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
        
        # Initialize assessment-specific session state
        if 'assessment_session_id' not in st.session_state:
            import uuid
            st.session_state.assessment_session_id = str(uuid.uuid4())
    
    def setup_storage(self):
        """Initialize storage client for assessment data"""
        try:
            if 'storage_client' not in st.session_state:
                st.session_state.storage_client = create_storage_client()
        except Exception as e:
            if st.secrets.get("debug_mode", False):
                st.sidebar.error(f"Storage setup error: {str(e)}")

    def _check_hidden_page_access(self):
        """Check URL parameters for hidden page access"""
        try:
            # Get URL parameters - Using st.query_params
            query_params = st.query_params
            
            # Check for assessment page access
            if 'page' in query_params and 'assess' in query_params['page']:
                return 'assess'
                
            # Check for admin page access
            if 'page' in query_params and 'admin' in query_params['page']:
                return 'admin'
                
            return None
        except:
            return None
    
    def _render_admin_sidebar(self):
        """Render admin controls in sidebar for assessment pages"""
        if self.hidden_page == 'assess' or self.hidden_page == 'admin':
            with st.sidebar:
                st.markdown("---")
                st.markdown("### 🔧 Admin Tools")
                
                # Admin access toggle
                if st.button("⚙️ Admin Access", help="Access admin interface"):
                    st.session_state.show_admin = not st.session_state.get('show_admin', False)
                
                # Storage info
                storage_type = st.secrets.get("storage", {}).get("storage_type", "session")
                st.caption(f"Storage: {storage_type.title()}")
                
                # Show session storage stats
                if hasattr(st.session_state, 'cloud_storage'):
                    storage_count = len(st.session_state.cloud_storage)
                    if storage_count > 0:
                        st.caption(f"Stored items: {storage_count}")
                
                # Show admin interface if toggled
                if st.session_state.get('show_admin', False) and AdminInterface:
                    st.markdown("---")
                    AdminInterface()
    
    def render_navigation(self):
        """Render the main navigation menu (only for public pages)"""
        if self.hidden_page:
            # Don't show navigation for hidden pages, just return the hidden page name
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
            try:
                from streamlit_option_menu import option_menu
                
                return option_menu(
                    menu_title=None,
                    options=options,
                    icons=icons,
                    default_index=0,
                    key="main_navigation",
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "0", "margin": "0 0 2rem 0"},
                        "nav-link": {"font-size": "1rem", "color": "#556D7A"},
                        "nav-link-selected": {"background": "#4CA1A3", "color": "white"}
                    }
                )
            except ImportError:
                # Fallback to selectbox if option_menu not available
                return st.selectbox("Navigate to:", options, key="main_navigation_fallback")
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        try:
            # Handle hidden pages first
            if selected_page == "assess" and AssessPage:
                self._render_hidden_assessment_page()
                return
                
            elif selected_page == "admin" and AdminInterface:
                self._render_admin_page()
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
            
            # Show storage status
            storage_type = st.secrets.get("storage", {}).get("storage_type", "session")
            if storage_type == "session":
                st.info("💾 Assessment data will be stored in your browser session and available for download.")
            
            page_instance = AssessPage()
            page_instance.render()
        else:
            st.error("Assessment page not available. Please contact support.")
    
    def _render_admin_page(self):
        """Render the admin interface page"""
        if AdminInterface:
            st.markdown("""
            <div style="background: #fff3cd; padding: 0.5rem 1rem; border-radius: 4px; 
                        margin-bottom: 1rem; border-left: 4px solid #ffc107;">
                <small style="color: #856404;">
                    ⚠️ Administrative interface - authorized personnel only
                </small>
            </div>
            """, unsafe_allow_html=True)
            
            AdminInterface()
        else:
            st.error("Admin interface not available.")
    
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
            # Instead show minimal footer for hidden pages
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; color: #556D7A; font-size: 0.8rem; padding: 1rem;">
                Rapid Transformation Hypnotherapy &copy; 2024 | Confidential Portal
            </div>
            """, unsafe_allow_html=True)
            return
            
        if self.footer:
            self.footer.render()

    def run(self):
        """Main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Render admin sidebar for hidden pages
            self._render_admin_sidebar()
            
            # Render page content based on selection
            self.render_page_content(selected_page)
            
            # Render booking form (except on hidden pages and Book Now page)
            self.render_booking_form(selected_page)
            
            # Always render footer (with special handling for hidden pages)
            self.render_footer()
            
        except Exception as e:
            st.error("Application error occurred. Please refresh the page.")
            if st.secrets.get("debug_mode", False):
                st.exception(e)

def main():
    """Application entry point with storage initialization"""
    try:
        # Initialize storage client at app level
        if 'storage_client' not in st.session_state:
            st.session_state.storage_client = create_storage_client()
        
        # Run the main application
        app = HypnotherapyApp()
        app.run()
        
    except Exception as e:
        st.error("Critical application error. Please contact support.")
        if st.secrets.get("debug_mode", False):
            st.exception(e)

if __name__ == "__main__":
    main()
