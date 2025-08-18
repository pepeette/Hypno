"""
Enhanced main application file for the Hypnotherapy website
Uses native Streamlit components instead of complex HTML
Improved error handling, component integration, and user experience
"""

import streamlit as st
import sys
import os

# Add current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure page FIRST before any other Streamlit commands
st.set_page_config(
    page_title="Transform Your Life in 2 Sessions | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import modules with proper error handling
def safe_import(module_name, class_name=None):
    """Safely import modules with fallback"""
    try:
        module = __import__(module_name, fromlist=[class_name] if class_name else [])
        return getattr(module, class_name) if class_name else module
    except ImportError as e:
        st.error(f"Import error: {module_name}.{class_name if class_name else ''} - {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected error importing {module_name}: {e}")
        return None

# Import page components
HomePage = safe_import('pages.home', 'HomePage')
MethodPage = safe_import('pages.method', 'MethodPage')
SuccessPage = safe_import('pages.success', 'SuccessPage')
BlogPage = safe_import('pages.blog', 'BlogPage')
BookingPage = safe_import('pages.booking', 'BookingPage')

# Import shared components
Navigation = safe_import('components.navigation', 'Navigation')
Footer = safe_import('components.footer', 'Footer')
BookingForm = safe_import('components.booking_form', 'BookingForm')

# Import utilities
apply_global_styles = safe_import('utils.styling', 'apply_global_styles')
initialize_session_state = safe_import('utils.session_state', 'initialize_session_state')

class HypnotherapyApp:
    """Main application class - SIMPLIFIED"""
    
    def __init__(self):
        """Initialize with minimal setup to avoid errors"""
        self.setup_basic_styling()
        self.setup_session_state()
        
    def setup_basic_styling(self):
        """Apply basic styling with error handling"""
        try:
            if apply_global_styles:
                apply_global_styles()
            else:
                # Fallback basic styling
                st.markdown("""
                <style>
                .stApp {
                    background-color: #F3F6F8 !important;
                    font-family: -apple-system, BlinkMacSystemFont, sans-serif !important;
                }
                h1 { font-size: 2.2rem !important; color: #273548 !important; }
                h2 { font-size: 1.8rem !important; color: #273548 !important; }
                p { font-size: 1rem !important; color: #556D7A !important; }
                </style>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Styling error: {e}")
    
    def setup_session_state(self):
        """Initialize session state with error handling"""
        try:
            if initialize_session_state:
                initialize_session_state()
            else:
                # Fallback session state initialization
                if 'page_initialized' not in st.session_state:
                    st.session_state.page_initialized = True
        except Exception as e:
            st.error(f"Session state error: {e}")
    
    def render_navigation(self):
        """Render navigation with fallback"""
        try:
            if Navigation:
                nav = Navigation()
                return nav.create_menu()
            else:
                # Fallback navigation using selectbox
                return st.selectbox(
                    "Navigate to:",
                    ["Home", "Method", "Success", "Blog", "Book Now"],
                    index=0,
                    key="main_nav"
                )
        except Exception as e:
            st.error(f"Navigation error: {e}")
            return "Home"
    
    def render_page_content(self, selected_page):
        """Render page content with comprehensive error handling"""
        try:
            if selected_page == "Home":
                self.render_home_page()
            elif selected_page == "Method":
                self.render_method_page()
            elif selected_page == "Success":
                self.render_success_page()
            elif selected_page == "Blog":
                self.render_blog_page()
            elif selected_page == "Book Now":
                self.render_booking_page()
            else:
                self.render_fallback_page(selected_page)
        except Exception as e:
            st.error(f"Page rendering error: {e}")
            self.render_emergency_fallback()
    
    def render_home_page(self):
        """Render home page with fallback"""
        if HomePage:
            try:
                page = HomePage()
                page.render()
            except Exception as e:
                st.error(f"Home page error: {e}")
                self.render_fallback_home()
        else:
            self.render_fallback_home()
    
    def render_method_page(self):
        """Render method page with fallback"""
        if MethodPage:
            try:
                page = MethodPage()
                page.render()
            except Exception as e:
                st.error(f"Method page error: {e}")
                self.render_fallback_method()
        else:
            self.render_fallback_method()
    
    def render_success_page(self):
        """Render success page with fallback"""
        if SuccessPage:
            try:
                page = SuccessPage()
                page.render()
            except Exception as e:
                st.error(f"Success page error: {e}")
                self.render_fallback_success()
        else:
            self.render_fallback_success()
    
    def render_blog_page(self):
        """Render blog page with fallback"""
        if BlogPage:
            try:
                page = BlogPage()
                page.render()
            except Exception as e:
                st.error(f"Blog page error: {e}")
                self.render_fallback_blog()
        else:
            self.render_fallback_blog()
    
    def render_booking_page(self):
        """Render booking page with fallback"""
        if BookingPage:
            try:
                page = BookingPage()
                page.render()
            except Exception as e:
                st.error(f"Booking page error: {e}")
                self.render_fallback_booking()
        else:
            self.render_fallback_booking()
    
    def render_fallback_home(self):
        """Emergency fallback home page"""
        st.markdown("# Transform Your Life in Just 2 Sessions")
        st.write("Science-backed clinical hypnotherapy for rapid, lasting change")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        with col2:
            st.metric("Experience", "10+ years", "proven results")
        with col3:
            st.metric("Clients Helped", "500+", "transformations")
        
        st.markdown("## Why Our Method Works")
        st.write("Traditional therapy targets symptoms using willpower (5% success rate). Our method rewires the subconscious patterns that create the behavior (85% success rate).")
        
        if st.button("📞 Book Free Discovery Call", type="primary"):
            st.success("Contact us at: laetitiasheppard@gmail.com")
    
    def render_fallback_method(self):
        """Emergency fallback method page"""
        st.markdown("# Our Proven 2-Step Method")
        
        st.markdown("## Session 1: Deep Analysis (90 minutes)")
        st.write("- Uncover subconscious patterns that drive your behavior")
        st.write("- Map your unique psychological landscape")
        st.write("- Begin positive programming for immediate relief")
        
        st.markdown("## Session 2: Transformation (90 minutes)")
        st.write("- Neural pathway rewiring in deep hypnotic state")
        st.write("- Install new, empowering behavior patterns")
        st.write("- Lock in lasting change at the subconscious level")
        
        st.success("**Result: 85% success rate in just 2 sessions**")
    
    def render_fallback_success(self):
        """Emergency fallback success page"""
        st.markdown("# Real Client Transformations")
        
        st.markdown("### 🌟 Banking Director, Singapore")
        st.write("*'Finally broke free from anxiety patterns that controlled my life for years. 2 sessions changed everything.'*")
        
        st.markdown("### 🚭 Wife, Bangkok")
        st.write("*'My husband smoked 2 packs daily for 20 years. After 2 sessions, he doesn't even think about cigarettes.'*")
        
        st.metric("Success Rate", "85%", "achieve goals in 2 sessions")
    
    def render_fallback_blog(self):
        """Emergency fallback blog page"""
        st.markdown("# Hypnotherapy Insights & FAQ")
        
        st.markdown("## Frequently Asked Questions")
        
        with st.expander("Is hypnotherapy safe?"):
            st.write("Yes, clinical hypnotherapy is completely safe. You remain fully aware and in control throughout the session.")
        
        with st.expander("How many sessions will I really need?"):
            st.write("85% of our clients achieve their goals in just 2 sessions. About 15% choose an optional 3rd session for reinforcement.")
        
        with st.expander("What if I can't be hypnotized?"):
            st.write("This is a common myth. Everyone can be hypnotized because hypnosis is a natural state we enter daily.")
    
    def render_fallback_booking(self):
        """Emergency fallback booking page"""
        st.markdown("# Start Your Transformation Today")
        
        st.markdown("## Contact Information")
        st.write("**Email:** laetitiasheppard@gmail.com")
        st.write("**Location:** Bangkok Hypnotherapy Clinic")
        st.write("**Address:** 27 Soi Sukhumvit 10 (Asoke), Bangkok, Thailand")
        
        st.markdown("## Booking Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📞 Free Discovery Call")
            st.write("15-minute consultation to explore your goals")
            st.markdown("[Schedule Discovery Call](https://calendly.com/laetitiasheppard/discovery)")
        
        with col2:
            st.markdown("### ⚡ Transformation Package")
            st.write("Complete 2-session program (3,000 THB)")
            st.markdown("[Book Sessions](https://calendly.com/laetitiasheppard/package)")
    
    def render_fallback_page(self, page_name):
        """Generic fallback for any page"""
        st.markdown(f"# {page_name}")
        st.write(f"The {page_name} page is being prepared. Please check back soon!")
        
        if st.button("📞 Contact Us", type="primary"):
            st.success("Email: laetitiasheppard@gmail.com")
    
    def render_emergency_fallback(self):
        """Emergency fallback when everything fails"""
        st.markdown("# Bangkok Hypnotherapy Clinic")
        st.write("Transform your life with science-backed hypnotherapy")
        
        st.error("Technical issue detected. Please contact us directly:")
        st.write("📧 **Email:** laetitiasheppard@gmail.com")
        st.write("📞 **Book Discovery Call:** https://calendly.com/laetitiasheppard/discovery")
        st.write("📍 **Location:** Bangkok, Thailand")
    
    def render_simple_footer(self):
        """Simple footer that always works"""
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Laetitia Sheppard**")
            st.write("Certified Clinical Hypnotherapist")
            st.write("10+ Years Experience")
        
        with col2:
            st.write("**Contact**")
            st.write("📧 laetitiasheppard@gmail.com")
            st.write("📍 Bangkok, Thailand")
        
        with col3:
            st.write("**Quick Links**")
            st.markdown("[Free Discovery Call](https://calendly.com/laetitiasheppard/discovery)")
            st.markdown("[Book Sessions](https://calendly.com/laetitiasheppard/package)")
        
        st.markdown("---")
        st.write("© 2025 Laetitia Sheppard • All Rights Reserved")
    
    def run(self):
        """Main application runner with comprehensive error handling"""
        try:
            # Navigation
            selected_page = self.render_navigation()
            
            # Main content
            self.render_page_content(selected_page)
            
            # Simple footer
            self.render_simple_footer()
            
        except Exception as e:
            st.error(f"Application error: {e}")
            self.render_emergency_fallback()

def main():
    """Application entry point with ultimate error handling"""
    try:
        app = HypnotherapyApp()
        app.run()
    except Exception as e:
        st.error("Critical application error")
        st.write("**Contact Information:**")
        st.write("📧 Email: laetitiasheppard@gmail.com")
        st.write("📞 Book Call: https://calendly.com/laetitiasheppard/discovery")
        
        # Show error in development
        if st.checkbox("Show technical details"):
            st.exception(e)

if __name__ == "__main__":
    main()
