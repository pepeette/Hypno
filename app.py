"""
Enhanced main application file for the Hypnotherapy website
Uses native Streamlit components instead of complex HTML
Improved error handling, component integration, and user experience
"""
import streamlit as st
from streamlit_option_menu import option_menu

# Import enhanced page modules with proper error handling
try:
    from pages.home import EnhancedHomePage as HomePage
except ImportError:
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

# Import enhanced shared components
try:
    from components.navigation import EnhancedNavigation as Navigation, create_quick_action_bar, create_floating_cta
except ImportError:
    try:
        from components.navigation import Navigation
        create_quick_action_bar = None
        create_floating_cta = None
    except ImportError:
        Navigation = None
        create_quick_action_bar = None
        create_floating_cta = None

try:
    from components.footer import EnhancedFooter as Footer
except ImportError:
    try:
        from components.footer import Footer
    except ImportError:
        Footer = None

try:
    from components.booking_form import EnhancedBookingForm as BookingForm
except ImportError:
    try:
        from components.booking_form import BookingForm
    except ImportError:
        BookingForm = None

try:
    from components.quiz import EnhancedQuiz as Quiz, create_quiz_launcher
except ImportError:
    try:
        from components.quiz import Quiz
        create_quiz_launcher = None
    except ImportError:
        Quiz = None
        create_quiz_launcher = None

# Import utilities
try:
    from utils.styling import apply_global_styles
except ImportError:
    def apply_global_styles():
        # Fallback basic styling
        st.markdown("""
        <style>
        .stApp {
            background-color: #F3F6F8 !important;
        }
        </style>
        """, unsafe_allow_html=True)

try:
    from utils.session_state import initialize_session_state, track_page_visit
except ImportError:
    def initialize_session_state():
        pass
    def track_page_visit(page):
        pass

class EnhancedHypnotherapyApp:
    """Enhanced main application class with improved UX and error handling"""
    
    def __init__(self):
        """Initialize the application with enhanced configuration"""
        self.setup_page_config()
        self.setup_styling()
        self.setup_session_state()
        
        # Initialize enhanced components
        self.navigation = Navigation() if Navigation else None
        self.footer = Footer() if Footer else None
        self.booking_form = BookingForm() if BookingForm else None
        self.quiz = Quiz() if Quiz else None
        
        # Initialize helper components
        self.quick_action_bar = create_quick_action_bar() if create_quick_action_bar else None
        self.floating_cta = create_floating_cta() if create_floating_cta else None
        self.quiz_launcher = create_quiz_launcher() if create_quiz_launcher else None
    
    def setup_page_config(self):
        """Configure Streamlit page settings with enhanced options"""
        st.set_page_config(
            page_title="Transform Your Life in 2 Sessions | Laetitia Sheppard",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://calendly.com/laetitiasheppard/discovery',
                'Report a bug': None,  # Disable to keep clean
                'About': "Science-backed hypnotherapy for rapid, lasting transformation"
            }
        )
        
    def setup_styling(self):
        """Apply enhanced global CSS styling"""
        apply_global_styles()
        
        # Additional app-specific styling
        st.markdown("""
        <style>
        /* Hide Streamlit branding and menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }
        
        /* Enhanced button styling */
        .stButton > button {
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        }
        
        /* Form styling improvements */
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus {
            border-color: #4CA1A3 !important;
            box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.2) !important;
        }
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .stContainer {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
    def setup_session_state(self):
        """Initialize session state with enhanced tracking"""
        initialize_session_state()
        
        # Track app initialization
        if 'app_initialized' not in st.session_state:
            st.session_state.app_initialized = True
            st.session_state.session_start_time = st.session_state.get('current_time', 'unknown')
    
    def render_navigation(self):
        """Render enhanced navigation with quick actions"""
        if self.navigation:
            selected = self.navigation.create_menu()
        else:
            # Enhanced fallback navigation
            selected = st.selectbox(
                "🧭 Navigate to:",
                ["Home", "Method", "Success", "Blog", "Book Now"],
                index=0,
                label_visibility="collapsed"
            )
        
        # Add quick action bar below navigation
        if self.quick_action_bar:
            self.quick_action_bar.render()
        
        return selected
    
    def render_page_content(self, selected_page):
        """Render enhanced page content with integrated components"""
        # Track page visit
        track_page_visit(selected_page)
        
        # Render main page content
        if selected_page == "Home":
            self._render_home_page()
        elif selected_page == "Method" and MethodPage:
            page = MethodPage()
            page.render()
        elif selected_page == "Success" and SuccessPage:
            page = SuccessPage()
            page.render()
        elif selected_page == "Blog" and BlogPage:
            page = BlogPage()
            page.render()
        elif selected_page == "Book Now":
            self._render_booking_page()
        else:
            self._render_fallback_content(selected_page)
    
    def _render_home_page(self):
        """Render enhanced home page with integrated quiz"""
        if HomePage:
            # Create home page instance
            home_page = HomePage()
            
            # Render hero and key sections
            home_page.hero.render()
            home_page.key_message.render()
            
            # Integrated quiz section
            if self.quiz:
                st.markdown('<div id="quiz-section"></div>', unsafe_allow_html=True)
                st.markdown("---")
                self.quiz.render()
            elif self.quiz_launcher:
                self.quiz_launcher.render_quiz_teaser()
            
            # Continue with other home page sections
            home_page.value_prop.render()
            home_page.testimonials.render()
            home_page._render_final_cta()
        else:
            self._render_fallback_home()
    
    def _render_booking_page(self):
        """Render dedicated booking page"""
        if BookingPage:
            page = BookingPage()
            page.render()
        elif self.booking_form:
            # Use enhanced booking form as fallback
            self.booking_form.render("Complete Your Booking", show_options=True)
        else:
            self._render_fallback_booking()
    
    def _render_fallback_content(self, page_name):
        """Enhanced fallback content with better UX"""
        st.markdown(f"""
        <div style="text-align: center; padding: 4rem 2rem; 
                    background: var(--card-bg); border-radius: 16px; 
                    margin: 2rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h1 style="color: var(--accent); margin-bottom: 1rem;">
                {page_name} - Coming Soon
            </h1>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                This page is being enhanced with new features. Please check back soon!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show relevant content based on page
        if page_name == "Method":
            st.markdown("""
            ## Our Proven 2-Step Method
            
            **Session 1: Deep Analysis** (90 minutes)
            - Uncover subconscious patterns that drive your behavior
            - Map your unique psychological landscape
            - Begin positive programming for immediate relief
            
            **Session 2: Transformation** (90 minutes)  
            - Neural pathway rewiring in deep hypnotic state
            - Install new, empowering behavior patterns
            - Lock in lasting change at the subconscious level
            
            **Result: 85% success rate in just 2 sessions**
            """)
        elif page_name == "Success":
            st.markdown("""
            ## Real Client Transformations
            
            - **Banking Director, Singapore**: "Finally broke free from anxiety patterns"
            - **Medical Student, Morocco**: "Overcame study anxiety and now excelling"  
            - **Bangkok Resident**: "Husband quit 20-year smoking habit in 2 sessions"
            
            **Success Rate: 85% achieve goals in 2 sessions**
            """)
    
    def _render_fallback_home(self):
        """Enhanced fallback home page"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; 
                    margin: 2rem 0; color: white;">
            <h1 style="color: white; margin-bottom: 1rem;">
                Transform Your Life in Just 2 Sessions
            </h1>
            <p style="color: white; opacity: 0.9; margin-bottom: 2rem;">
                Science-backed clinical hypnotherapy for rapid, lasting change
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        with col2:
            st.metric("Experience", "10+ years", "proven results")
        with col3:
            st.metric("Clients Helped", "500+", "transformations")
    
    def _render_fallback_booking(self):
        """Enhanced fallback booking"""
        st.markdown("""
        ### 📞 Start Your Transformation
        
        **Ready to begin?** Contact us directly:
        
        - **Email**: laetitiasheppard@gmail.com
        - **Discovery Call**: [Schedule Free 15-min Call](https://calendly.com/laetitiasheppard/discovery)
        - **Book Package**: [Start Your 2-Session Program](https://calendly.com/laetitiasheppard/package)
        """)
    
    def render_booking_section(self, selected_page):
        """Render booking section based on page context"""
        # Only show booking form on non-booking pages
        if selected_page != "Book Now":
            if self.booking_form:
                st.markdown("---")
                self.booking_form.render_compact()
            else:
                # Simple booking CTA
                st.markdown("---")
                st.markdown("### 🚀 Ready to Start Your Transformation?")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" 
                       style="display: block; background-color: var(--accent); color: white;
                              text-decoration: none; padding: 1rem; border-radius: 8px;
                              font-weight: 600; text-align: center; margin: 0.5rem 0;">
                        📞 Free Discovery Call
                    </a>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <a href="https://calendly.com/laetitiasheppard/package" target="_blank" 
                       style="display: block; background-color: var(--success); color: white;
                              text-decoration: none; padding: 1rem; border-radius: 8px;
                              font-weight: 600; text-align: center; margin: 0.5rem 0;">
                        ⚡ Book Transformation Package
                    </a>
                    """, unsafe_allow_html=True)
    
    def render_footer(self):
        """Render enhanced footer"""
        if self.footer:
            self.footer.render()
        else:
            # Enhanced fallback footer
            st.markdown("---")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **Laetitia Sheppard**  
                Certified Clinical Hypnotherapist  
                10+ Years Experience  
                500+ Successful Transformations
                """)
            
            with col2:
                st.markdown("""
                **Contact Information**  
                📧 laetitiasheppard@gmail.com  
                📍 Bangkok Hypnotherapy Clinic  
                27 Soi Sukhumvit 10 (Asoke)  
                Bangkok, Thailand
                """)
            
            with col3:
                st.markdown("""
                **Quick Links**  
                🎯 [Take Assessment](#quiz-section)  
                📞 [Free Discovery Call](https://calendly.com/laetitiasheppard/discovery)  
                ⚡ [Book Sessions](https://calendly.com/laetitiasheppard/package)  
                📍 [Directions](https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw)
                """)
            
            st.markdown("---")
            st.markdown(
                f"© {datetime.datetime.now().year} Laetitia Sheppard • All Rights Reserved • "
                "Licensed & Insured • Confidential Sessions Guaranteed"
            )
    
    def render_floating_elements(self):
        """Render floating UI elements"""
        if self.floating_cta:
            self.floating_cta.render()
    
    def run(self):
        """Enhanced main application entry point"""
        try:
            # Render navigation and get selected page
            selected_page = self.render_navigation()
            
            # Render main page content
            self.render_page_content(selected_page)
            
            # Render contextual booking section
            self.render_booking_section(selected_page)
            
            # Render footer
            self.render_footer()
            
            # Render floating elements
            self.render_floating_elements()
            
        except Exception as e:
            # Enhanced error handling
            st.error("🚨 Something went wrong. Please refresh the page.")
            
            # Show user-friendly error in development
            if st.secrets.get("debug_mode", False):
                st.exception(e)
                st.info("Debug mode is enabled. Disable in production.")
            
            # Fallback content
            st.markdown("""
            ### 📞 Need Help?
            If you're experiencing issues, please contact us directly:
            - **Email**: laetitiasheppard@gmail.com
            - **Phone**: Available for urgent matters
            """)

def main():
    """Application entry point with error handling"""
    try:
        app = EnhancedHypnotherapyApp()
        app.run()
    except Exception as e:
        # Ultimate fallback
        st.error("Application failed to start. Please contact support.")
        if st.secrets.get("debug_mode", False):
            st.exception(e)

if __name__ == "__main__":
    main()
