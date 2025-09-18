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
Streamlined for Streamlit Community Cloud deployment
"""
import streamlit as st
import os
from datetime import datetime

# Disable file watching in production
if os.getenv('STREAMLIT_ENV') == 'production':
    st.set_option('server.fileWatcherType', 'none')

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

# Clean import for assessment page
try:
    from pages.assess import create_assess_page
    AssessPage = create_assess_page
    print("✅ Assessment page imported successfully")
except ImportError as e:
    print(f"❌ Failed to import assessment page: {e}")
    AssessPage = None
except Exception as e:
    print(f"❌ Unexpected error importing assessment page: {e}")
    AssessPage = None

# Import admin interface (to be created)
try:
    from pages.admin_interface import AdminInterface
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
        
        # Initialize components
        self.navigation = Navigation() if Navigation else None
        self.footer = Footer() if Footer else None
        self.booking_form = BookingForm() if BookingForm else None
        
        # Check for hidden page access
        self.hidden_page = self._check_hidden_page_access()
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
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
        assessment_defaults = {
            'assessment_session_id': None,
            'assessment_storage': {},  # Store multiple assessments for admin
            'email_queue': [],         # Queue for email notifications
            'admin_authenticated': False  # Admin access flag
        }
        
        for key, value in assessment_defaults.items():
            if key not in st.session_state:
                if key == 'assessment_session_id' and value is None:
                    import uuid
                    st.session_state[key] = str(uuid.uuid4())
                else:
                    st.session_state[key] = value

    def _check_hidden_page_access(self):
        """Check URL parameters for hidden page access"""
        try:
            # Get URL parameters
            query_params = st.query_params
            
            # Check for assessment page access
            if 'page' in query_params:
                page_param = str(query_params['page']).lower()
                if 'assess' in page_param:
                    print(f"🔍 Assessment page access detected: {page_param}")
                    return 'assess'
                elif 'admin' in page_param:
                    print(f"🔍 Admin page access detected: {page_param}")
                    return 'admin'
                
            return None
        except Exception as e:
            print(f"❌ Error checking hidden page access: {e}")
            return None
    
    def render_navigation(self):
        """Render the main navigation menu (only for public pages)"""
        if self.hidden_page:
            # Don't show navigation for hidden pages
            print(f"🔍 Hidden page detected, skipping navigation: {self.hidden_page}")
            return self.hidden_page
            
        if self.navigation:
            return self.navigation.create_menu()
        else:
            # Simple fallback navigation
            try:
                from streamlit_option_menu import option_menu
                
                options = ["Home", "Method", "Blog", "Testimonials", "Book Now"]
                icons = ["house", "gear", "book", "star", "calendar"]
                
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
                return st.selectbox("Navigate to:", ["Home", "Method", "Blog", "Testimonials", "Book Now"])
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        try:
            # Handle hidden pages first
            if selected_page == "assess":
                print(f"🔍 Rendering assessment page. AssessPage available: {AssessPage is not None}")
                self._render_hidden_assessment_page()
                return
                
            elif selected_page == "admin":
                print(f"🔍 Rendering admin page")
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
            print(f"❌ Page render error for {selected_page}: {e}")
            if st.secrets.get("debug_mode", False):
                st.exception(e)
        
    def _render_hidden_assessment_page(self):
        """Render the hidden assessment page"""
        print("🔍 Starting assessment page render")
        
        # Add discrete header for assessment page
        st.markdown("""
        <div style="background: #f0f8ff; padding: 0.5rem 1rem; border-radius: 4px; 
                    margin-bottom: 1rem; border-left: 4px solid #4CA1A3;">
            <small style="color: #4CA1A3;">
                🔒 Confidential Behavioral Pattern Assessment Portal
            </small>
        </div>
        """, unsafe_allow_html=True)
        
        if AssessPage:
            try:
                print("✅ Calling AssessPage function")
                # Call the assessment page creation function
                AssessPage()
                print("✅ Assessment page rendered successfully")
            except Exception as e:
                st.error(f"❌ Error rendering assessment page: {str(e)}")
                print(f"❌ Assessment render error: {e}")
                if st.secrets.get("debug_mode", False):
                    st.exception(e)
        else:
            st.error("❌ Assessment page not available")
            st.info("The assessment module failed to import. Please check the console for import errors.")
            
            # Debug information
            with st.expander("🔧 Debug Information"):
                st.code(f"""
Import Status:
- AssessPage: {AssessPage is not None}
- Module path: pages.assess
                
To fix this issue:
1. Ensure pages/assess.py exists
2. Ensure create_assess_page function is defined in assess.py
3. Check console/logs for import errors
                """)
        
    def _render_admin_page(self):
        """Render the admin interface page"""
        st.markdown("""
        <div style="background: #fff3cd; padding: 0.5rem 1rem; border-radius: 4px; 
                    margin-bottom: 1rem; border-left: 4px solid #ffc107;">
            <small style="color: #856404;">
                ⚠️ Administrative Interface - Authorized Personnel Only
            </small>
        </div>
        """, unsafe_allow_html=True)
        
        if AdminInterface:
            try:
                admin = AdminInterface()
                admin.render()
            except Exception as e:
                st.error(f"Error loading admin interface: {str(e)}")
                print(f"❌ Admin interface error: {e}")
        else:
            st.warning("Admin interface not available")
            st.info("The admin interface will be implemented in pages/admin_interface.py")
    
    def render_booking_form(self, selected_page):
        """Render booking form on public pages only"""
        # Don't show booking form on hidden pages
        if self.hidden_page:
            return
            
        if selected_page != "Book Now" and self.booking_form:
            self.booking_form.render()
    
    def render_footer(self):
        """Render the footer section"""
        # Minimal footer for hidden pages
        if self.hidden_page:
            st.markdown("---")
            st.markdown("""
            <div style="text-align: center; color: #666; font-size: 0.8rem; padding: 1rem 0;">
                © 2025 Laetitia Sheppard • Confidential Portal • All Rights Reserved
            </div>
            """, unsafe_allow_html=True)
            return

        # Regular footer for public pages
        if self.footer:
            self.footer.render()

    def run(self):
        """Main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            print(f"🔍 Selected page: {selected_page}")
            
            # Render page content based on selection
            self.render_page_content(selected_page)
            
            # Render booking form (except on hidden pages and Book Now page)
            self.render_booking_form(selected_page)
            
            # Always render footer
            self.render_footer()
            
        except Exception as e:
            st.error("Application error occurred. Please refresh the page.")
            print(f"❌ Critical application error: {e}")
            if st.secrets.get("debug_mode", False):
                st.exception(e)

def main():
    """Application entry point"""
    try:
        print("🚀 Starting Hypnotherapy App")
        app = HypnotherapyApp()
        app.run()
        
    except Exception as e:
        st.error("Critical application error. Please contact support.")
        print(f"❌ Critical main error: {e}")
        if st.secrets.get("debug_mode", False):
            st.exception(e)

if __name__ == "__main__":
    main()
