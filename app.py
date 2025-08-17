import streamlit as st
from streamlit_option_menu import option_menu

# Import page modules with proper error handling
HomePage = None
MethodPage = None
SuccessPage = None
BlogPage = None
BookingPage = None
Navigation = None
Footer = None
BookingForm = None

try:
    from pages.home import HomePage
except ImportError:
    pass

try:
    from pages.method import MethodPage
except ImportError:
    pass

try:
    from pages.success import SuccessPage
except ImportError:
    pass

try:
    from pages.blog import BlogPage
except ImportError:
    pass

try:
    from pages.booking import BookingPage
except ImportError:
    pass

try:
    from components.navigation import Navigation
except ImportError:
    pass

try:
    from components.footer import Footer
except ImportError:
    pass

try:
    from components.booking_form import BookingForm
except ImportError:
    pass

try:
    from utils.styling import apply_global_styles
except ImportError:
    def apply_global_styles():
        st.markdown("""
        <style>
        :root {
            color-scheme: light !important;
        }
        html, body, .stApp {
            color-scheme: light !important;
            background-color: #F3F6F8 !important;
        }
        </style>
        """, unsafe_allow_html=True)

try:
    from utils.session_state import initialize_session_state
except ImportError:
    def initialize_session_state():
        if 'initialized' not in st.session_state:
            st.session_state.initialized = True

class HypnotherapyApp:
    """Main application class for the Hypnotherapy website"""
    
    def __init__(self):
        """Initialize the application with configuration and styling"""
        if not hasattr(st.session_state, 'app_initialized'):
            self.setup_page_config()
            self.setup_styling()
            self.setup_session_state()
            st.session_state.app_initialized = True
        
        # Initialize components with fallbacks
        self.navigation = Navigation() if Navigation else None
        self.footer = Footer() if Footer else None
        
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
    
    def render_navigation(self):
        """Render navigation with fallback"""
        if self.navigation:
            return self.navigation.create_menu()
        else:
            # Fallback navigation using streamlit_option_menu
            return option_menu(
                menu_title=None,
                options=["Home", "Method", "Success", "Blog", "Book Now"],
                icons=["house", "magic", "stars", "book", "calendar"],
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "0", "background-color": "transparent"},
                    "nav-link": {"font-size": "1rem", "text-align": "center", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#4CA1A3"},
                }
            )
    
    def render_page_content(self, selected_page):
        """Render content based on selected navigation page - with fallbacks"""
        
        # Prevent double rendering
        if hasattr(st.session_state, 'current_page') and st.session_state.current_page == selected_page:
            if hasattr(st.session_state, f'{selected_page.lower()}_rendered'):
                return
        
        st.session_state.current_page = selected_page
        
        # Create page instance and render once
        if selected_page == "Home":
            if HomePage:
                if f'home_rendered' not in st.session_state:
                    home_page = HomePage()
                    home_page.render()
                    st.session_state.home_rendered = True
            else:
                self._render_fallback_home()
                
        elif selected_page == "Method":
            if MethodPage:
                if f'method_rendered' not in st.session_state:
                    method_page = MethodPage()
                    method_page.render()
                    st.session_state.method_rendered = True
            else:
                self._render_fallback_method()
                
        elif selected_page == "Success":
            if SuccessPage:
                if f'success_rendered' not in st.session_state:
                    success_page = SuccessPage()
                    success_page.render()
                    st.session_state.success_rendered = True
            else:
                self._render_fallback_success()
                
        elif selected_page == "Blog":
            if BlogPage:
                if f'blog_rendered' not in st.session_state:
                    blog_page = BlogPage()
                    blog_page.render()
                    st.session_state.blog_rendered = True
            else:
                self._render_fallback_blog()
                
        elif selected_page == "Book Now":
            if BookingPage:
                if f'booking_rendered' not in st.session_state:
                    booking_page = BookingPage()
                    booking_page.render()
                    st.session_state.booking_rendered = True
            else:
                self._render_fallback_booking()
    
    def _render_fallback_home(self):
        """Fallback home page content"""
        st.markdown("""
        # 🧠 Transform Your Life in Just 2 Sessions
        
        **Science-backed clinical hypnotherapy for rapid, lasting change**
        
        ## Why Our Method Works
        
        Traditional therapy targets your conscious mind (5% of decisions). 
        Our hypnotherapy method works directly with your subconscious (95% of decisions).
        
        ### ✨ Results You Can Expect
        
        - **85% success rate** in just 2 sessions
        - **500+ lives** transformed since 2014
        - **Licensed & certified** clinical hypnotherapist
        - **Money-back guarantee** if not satisfied
        
        ### 🎯 We Help With
        
        - Quit smoking permanently
        - Reduce anxiety and stress
        - Improve sleep quality
        - Break unwanted habits
        - Build confidence
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", type="primary", use_container_width=True):
                st.success("Great choice! We'll contact you within 24 hours.")
        with col2:
            if st.button("⚡ Book Sessions Now", type="secondary", use_container_width=True):
                st.success("Excellent! Let's begin your transformation.")
    
    def _render_fallback_method(self):
        """Fallback method page content"""
        st.markdown("""
        # 🔬 Our Proven 2-Session Method
        
        ## Session 1: Deep Analysis (90 minutes)
        - Uncover your subconscious patterns
        - Map your unique triggers
        - Begin positive programming
        - Feel immediate relief
        
        ## Session 2: Transformation (90 minutes)  
        - Deep hypnotic state access
        - Neural pathway rewiring
        - Install new behaviors
        - Lock in lasting change
        
        ## Investment: 3,000 THB
        Complete 2-session package
        
        **85% of clients succeed in just 2 sessions**
        """)
    
    def _render_fallback_success(self):
        """Fallback success page content"""
        st.markdown("""
        # ⭐ Real Success Stories
        
        ## Client Testimonials
        
        ### 🚭 Smoking Cessation
        *"After 20 years of smoking, I'm finally free. Two sessions changed everything."*
        — Executive, Singapore
        
        ### 😌 Anxiety Relief  
        *"I haven't had a panic attack since my sessions. Life is so much better."*
        — Student, Morocco
        
        ### 😴 Sleep Improvement
        *"I sleep through the night now. Amazing results!"*
        — Professional, Bangkok
        
        ## Success Statistics
        - **85%** complete transformation in 2 sessions
        - **15%** need optional 3rd session
        - **95%** still transformed 1 year later
        """)
    
    def _render_fallback_blog(self):
        """Fallback blog page content"""
        st.markdown("""
        # 📚 Hypnotherapy Insights
        
        ## Frequently Asked Questions
        
        ### Is hypnotherapy safe?
        Yes, completely safe. You remain in control throughout the session.
        
        ### How many sessions will I need?
        85% of clients achieve their goals in just 2 sessions.
        
        ### What if I can't be hypnotized?
        Everyone can be hypnotized - it's a natural state we enter daily.
        
        ### How is this different from other methods?
        We work with your subconscious mind where real change happens.
        
        ## Latest Articles
        
        ### The Science of Rapid Change
        Understanding how hypnotherapy creates lasting transformation...
        
        ### Breaking Free from Smoking
        Why willpower fails and hypnotherapy succeeds...
        """)
    
    def _render_fallback_booking(self):
        """Fallback booking page content"""
        st.markdown("""
        # 📅 Book Your Transformation
        
        ## Choose Your Option
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📞 Free Discovery Call
            15-minute consultation
            - Understand your situation
            - Learn how we can help
            - No obligation
            """)
            if st.button("Schedule Discovery Call", type="primary", use_container_width=True):
                st.success("✅ We'll contact you within 24 hours!")
        
        with col2:
            st.markdown("""
            ### ⚡ Transformation Package
            Complete 2-session program
            - Session 1: Analysis (90 min)
            - Session 2: Transformation (90 min)
            - 3,000 THB total
            """)
            if st.button("Book Sessions Now", type="secondary", use_container_width=True):
                st.success("🚀 Excellent choice! Check your email for next steps.")
    
    def render_discovery_cta(self, page_name):
        """Render discovery call CTA on every page except Book Now"""
        if page_name != "Book Now":
            # Simple floating CTA that works without complex CSS
            if st.sidebar.button("📞 Free Discovery Call", type="primary"):
                st.sidebar.success("✨ Great! We'll contact you within 24 hours.")
                st.sidebar.markdown("**Next Steps:**")
                st.sidebar.markdown("• Check your email")
                st.sidebar.markdown("• We'll schedule your call")
                st.sidebar.markdown("• Start your transformation")
    
    def render_footer(self):
        """Render footer with fallback"""
        if self.footer:
            self.footer.render()
        else:
            # Simple fallback footer
            st.markdown("---")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **Laetitia Sheppard**  
                Clinical Hypnotherapist  
                Bangkok, Thailand
                """)
            
            with col2:
                st.markdown("""
                **Quick Links**  
                📞 [Free Discovery Call](https://calendly.com/laetitiasheppard/discovery)  
                ⚡ [Book Sessions](https://calendly.com/laetitiasheppard/package)  
                📍 [Directions](https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8)
                """)
            
            with col3:
                st.markdown("""
                **Credentials**  
                ✓ Certified Clinical Hypnotherapist  
                ✓ 10+ Years Experience  
                ✓ Licensed & Insured  
                ✓ 500+ Success Stories
                """)
            
            st.markdown("---")
            st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved")
            st.markdown("🔒 All sessions strictly confidential • Professional standards guaranteed")
    
    def run(self):
        """Main application entry point"""
        try:
            # Create navigation menu
            selected_page = self.render_navigation()
            
            # Render page content (single render with fallbacks)
            self.render_page_content(selected_page)
            
            # Add discovery CTA
            self.render_discovery_cta(selected_page)
            
            # Always render footer
            self.render_footer()
            
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
