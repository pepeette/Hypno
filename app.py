# """
# Main application entry point for the Hypnotherapy website
# Clean architecture using proper imports and Streamlit components
# """
# import streamlit as st

# # Import page modules with error handling
# try:
#     from pages.home import HomePage
# except ImportError:
#     HomePage = None

# try:
#     from pages.method import MethodPage  
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
#     from components.navigation import Navigation
# except ImportError:
#     Navigation = None

# try:
#     from components.footer import Footer
# except ImportError:
#     Footer = None

# try:
#     from components.booking_form import BookingForm
# except ImportError:
#     BookingForm = None

# # Import utilities with error handling
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
        
#         # Initialize components with fallbacks
#         self.navigation = Navigation() if Navigation else None
#         self.footer = Footer() if Footer else None
#         self.booking_form = BookingForm() if BookingForm else None
        
#     def setup_page_config(self):
#         """Configure Streamlit page settings"""
#         st.set_page_config(
#             page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
#             page_icon="🧠",
#             layout="wide",
#             initial_sidebar_state="collapsed",
#             menu_items={
#                 'Get Help': 'https://laetitiasheppard.com/help',
#                 'Report a bug': 'https://laetitiasheppard.com/bug-report',
#                 'About': "Transform your life with science-backed hypnotherapy"
#             }
#         )
        
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
#             # Fallback navigation using Streamlit selectbox
#             return st.selectbox(
#                 "Navigation",
#                 ["Home", "Method", "Success", "Blog", "Book Now"],
#                 index=0,
#                 label_visibility="collapsed"
#             )
    
#     def render_page_content(self, selected_page):
#         """Render content based on selected navigation page"""
#         if selected_page == "Home" and HomePage:
#             page = HomePage()
#             page.render()
#         elif selected_page == "Method" and MethodPage:
#             page = MethodPage()
#             page.render()
#         elif selected_page == "Success" and SuccessPage:
#             page = SuccessPage()
#             page.render()
#         elif selected_page == "Blog" and BlogPage:
#             page = BlogPage()
#             page.render()
#         elif selected_page == "Book Now" and BookingPage:
#             page = BookingPage()
#             page.render()
#         else:
#             # Fallback content using Streamlit components
#             self.render_fallback_content(selected_page)
    
#     def render_fallback_content(self, page_name):
#         """Render fallback content if page components are not available"""
#         st.title(f"{page_name} - Coming Soon")
#         st.info(f"The {page_name} page is being prepared. Please check back soon!")
        
#         if page_name == "Home":
#             st.subheader("Welcome to 2-Step Hypnotherapy")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("Success Rate", "85%", "in 2 sessions")
#             with col2:
#                 st.metric("Experience", "10+ years", "certified")
#             with col3:
#                 st.metric("Lives Changed", "500+", "since 2017")
                
#             st.write("Transform your life with our science-backed approach:")
#             st.write("• **85% success rate** in just 2 sessions")
#             st.write("• **Professional certification** and 10+ years experience")
#             st.write("• **Personalized approach** for lasting change")
            
#         elif page_name == "Method":
#             st.subheader("Our Proven 2-Step Method")
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.write("**Session 1: Deep Analysis** (90 minutes)")
#                 st.write("• Uncover subconscious patterns")
#                 st.write("• Map your unique triggers")
#                 st.write("• Begin positive programming")
#             with col2:
#                 st.write("**Session 2: Transformation** (90 minutes)")
#                 st.write("• Neural pathway rewiring")
#                 st.write("• Install new behaviors")
#                 st.write("• Lock in lasting change")
    
#     def render_booking_form(self):
#         """Render booking form on all pages"""
#         if self.booking_form:
#             self.booking_form.render()
#         else:
#             # Simple fallback booking section using Streamlit components
#             st.subheader("📞 Book Your Free Discovery Call")
#             with st.form("simple_booking"):
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     name = st.text_input("Name*")
#                 with col2:
#                     email = st.text_input("Email*")
                
#                 concern = st.selectbox("Primary Concern*", 
#                     ["Select one...", "Quit Smoking", "Reduce Anxiety", "Improve Sleep", "Break Bad Habits", "Other"])
                
#                 if st.form_submit_button("📞 Schedule Call", type="primary", use_container_width=True):
#                     if name and email and concern != "Select one...":
#                         st.success("✅ Request submitted! We'll contact you within 24 hours.")
#                     else:
#                         st.error("Please fill in all required fields.")
    
#     def render_footer(self):
#         """Render the footer section"""
#         if self.footer:
#             self.footer.render()
#         else:
#             # Simple fallback footer using Streamlit components
#             st.divider()
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.subheader("Laetitia Sheppard")
#                 st.write("Certified Clinical Hypnotherapist")
#                 st.write("Bangkok, Thailand")
            
#             with col2:
#                 st.subheader("Contact")
#                 st.write("📧 laetitiasheppard@gmail.com")
#                 st.write("📍 Bangkok Hypnotherapy Clinic")
            
#             st.caption("© 2025 Laetitia Sheppard • All Rights Reserved")
    
#     def run(self):
#         """Main application entry point"""
#         try:
#             # Render navigation and get selected page
#             selected_page = self.render_navigation()
            
#             # Render page content
#             self.render_page_content(selected_page)
            
#             # Always render booking form
#             self.render_booking_form()
            
#             # Always render footer
#             self.render_footer()
            
#         except Exception as e:
#             st.error("Application error occurred. Please refresh the page.")
#             # Only show detailed error in development
#             if st.secrets.get("debug_mode", False):
#                 st.exception(e)

# def main():
#     """Application entry point"""
#     app = HypnotherapyApp()
#     app.run()

# if __name__ == "__main__":
#     main()


"""
Main Streamlit application for the Hypnotherapy website
Improved architecture with better spacing and component integration
"""
import streamlit as st
from streamlit_option_menu import option_menu

# Import page modules with error handling
try:
    from pages.home import create_home_page
    HomePage = create_home_page()
except ImportError:
    HomePage = None

try:
    from pages.method import create_method_page
    MethodPage = create_method_page()
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
    from components.navigation import create_navigation
    Navigation = create_navigation()
except ImportError:
    Navigation = None

try:
    from components.footer import create_footer
    Footer = create_footer()
except ImportError:
    Footer = None

try:
    from components.booking_form import create_booking_form
    BookingForm = create_booking_form()
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
    """Main application class with improved component orchestration"""
    
    def __init__(self):
        """Initialize the application with improved configuration"""
        self.setup_page_config()
        self.setup_styling()
        self.setup_session_state()
        
        # Initialize components
        self.navigation = Navigation
        self.footer = Footer
        self.booking_form = BookingForm
        
        # Page mapping for cleaner routing
        self.pages = {
            "Home": HomePage,
            "Method": MethodPage,
            "Success": SuccessPage() if SuccessPage else None,
            "Blog": BlogPage() if BlogPage else None,
            "Book Now": BookingPage() if BookingPage else None
        }
    
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://calendly.com/laetitiasheppard/new-meeting',
                'Report a bug': None,
                'About': "Transform your life with science-backed hypnotherapy in Bangkok"
            }
        )
    
    def setup_styling(self):
        """Apply global CSS styling"""
        apply_global_styles()
        
        # Additional app-specific styling for improved spacing
        st.markdown("""
        <style>
        /* Improved container spacing */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 1rem;
            max-width: 1200px;
        }
        
        /* Better section spacing */
        .stMarkdown {
            margin-bottom: 1rem;
        }
        
        /* Improved button spacing */
        .stButton {
            margin: 0.5rem 0;
        }
        
        /* Better form spacing */
        .stForm {
            margin: 2rem 0;
        }
        
        /* Responsive improvements */
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            
            .stColumns {
                gap: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
    
    def setup_session_state(self):
        """Initialize session state variables"""
        initialize_session_state()
    
    def render_navigation(self):
        """Render the main navigation menu"""
        if self.navigation:
            return self.navigation.create_menu()
        else:
            # Fallback navigation with improved styling
            return option_menu(
                menu_title=None,
                options=["Home", "Method", "Success", "Blog", "Book Now"],
                icons=["house", "gear", "star", "book", "calendar"],
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {
                        "padding": "0",
                        "margin": "0 0 3rem 0",
                        "background-color": "#F0FDFA",
                        "border-radius": "12px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.05)"
                    },
                    "nav-link": {
                        "font-size": "1rem",
                        "padding": "12px 20px",
                        "color": "#556D7A",
                        "font-weight": "500",
                        "border-radius": "8px",
                        "margin": "0 4px"
                    },
                    "nav-link-selected": {
                        "background": "#4CA1A3",
                        "color": "white",
                        "font-weight": "600"
                    }
                }
            )
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page"""
        page = self.pages.get(selected_page)
        
        if page and hasattr(page, 'render'):
            # Add page-specific spacing
            st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
            page.render()
        else:
            # Improved fallback content
            self.render_enhanced_fallback(selected_page)
    
    def render_enhanced_fallback(self, page_name):
        """Render enhanced fallback content with better spacing"""
        st.markdown(f"""
        <div style="text-align: center; padding: 4rem 2rem; 
                    background: #FFFFFF; border-radius: 12px; 
                    margin: 3rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <div style="font-size: 4rem; margin-bottom: 2rem;">🔧</div>
            <h2 style="color: #273548; margin-bottom: 1rem;">{page_name} - Coming Soon</h2>
            <p style="color: #556D7A; font-size: 1.1rem; max-width: 500px; margin: 0 auto 2rem auto;">
                We're putting the finishing touches on this page. 
                In the meantime, book a free discovery call to get started!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced fallback content based on page
        if page_name == "Method":
            col1, col2 = st.columns(2, gap="large")
            with col1:
                st.markdown("""
                ### 🔍 Session 1: Analysis
                **90 minutes • Deep dive into your patterns**
                - Uncover subconscious triggers
                - Map behavior patterns  
                - Identify root causes
                - Begin positive programming
                """)
            with col2:
                st.markdown("""
                ### ⚡ Session 2: Transformation  
                **90 minutes • Complete rewiring**
                - Deep hypnotic state
                - Neural pathway rewiring
                - Install new patterns
                - Lock in transformation
                """)
        
        elif page_name == "Success":
            st.success("85% success rate in just 2 sessions!")
            st.info("Over 500 lives transformed since 2014")
            st.markdown("Real client testimonials coming soon...")
        
        elif page_name == "Blog":
            st.markdown("""
            ### Coming Soon:
            - How hypnotherapy rewires your brain
            - Breaking free from smoking addiction
            - Overcoming anxiety at the subconscious level
            - Frequently asked questions
            """)
    
    def render_booking_section(self, selected_page):
        """Render booking form with improved spacing"""
        if selected_page != "Book Now" and self.booking_form:
            # Add spacing before booking section
            st.markdown("<div style='margin-top: 6rem;'></div>", unsafe_allow_html=True)
            self.booking_form.render()
        elif selected_page != "Book Now":
            # Simple fallback booking with better styling
            st.markdown("<div style='margin-top: 6rem;'></div>", unsafe_allow_html=True)
            st.markdown("---")
            
            st.markdown("""
            <div style="text-align: center; padding: 3rem 2rem; 
                        background: #FFFFFF; border-radius: 12px; 
                        margin: 2rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">📞 Ready to Transform?</h2>
                <p style="color: #556D7A; margin-bottom: 2rem;">
                    Book your free 15-minute discovery call today
                </p>
                <p style="color: #273548; font-weight: 600;">
                    📧 laetitiasheppard@gmail.com<br>
                    📅 <a href="https://calendly.com/laetitiasheppard/new-meeting" 
                         style="color: #4CA1A3;">Schedule Online</a>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    def render_footer(self):
        """Render the footer section with proper spacing"""
        if self.footer:
            self.footer.render()
        else:
            # Enhanced fallback footer
            st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
            st.markdown("---")
            
            col1, col2 = st.columns([2, 1], gap="large")
            
            with col1:
                col_img, col_text = st.columns([1, 3])
                with col_img:
                    st.image("https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true", width=80)
                with col_text:
                    st.markdown("### Laetitia Sheppard")
                    st.write("Certified Clinical Hypnotherapist")
                    st.write("10+ years transforming lives in Bangkok")
            
            with col2:
                st.markdown("### Contact")
                st.write("**Bangkok Hypnotherapy Clinic**")
                st.write("27 Soi Sukhumvit 10 (Asoke)")
                st.write("Bangkok, Thailand")
                
                if st.button("📍 Get Directions", use_container_width=True):
                    st.success("Opening maps...")
                if st.button("📅 Book Now", use_container_width=True, type="primary"):
                    st.success("Scroll up to book!")
            
            # Copyright
            current_year = 2025
            st.markdown(f"""
            <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; 
                        border-top: 1px solid #CBD5E1; color: #556D7A;">
                <p>© {current_year} Laetitia Sheppard • All Rights Reserved</p>
                <p style="font-size: 0.9rem;">
                    🔒 All sessions strictly confidential • Licensed & Insured
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    def run(self):
        """Main application entry point with improved error handling"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Add some top spacing after navigation
            st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
            
            # Render page content with container
            with st.container():
                self.render_page_content(selected_page)
            
            # Render booking section (conditional)
            self.render_booking_section(selected_page)
            
            # Render footer
            self.render_footer()
            
        except Exception as e:
            # Enhanced error handling
            st.error("🚨 Something went wrong. Please refresh the page.")
            
            # Show error details in development mode only
            if st.secrets.get("debug_mode", False):
                st.exception(e)
                st.info("Debug mode is enabled. Disable in production.")

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
