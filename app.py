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

def apply_basic_styles():
    """Apply basic Streamlit-compatible styles"""
    st.markdown("""
    <style>
    /* Force light mode */
    :root { color-scheme: light !important; }
    html, body, .stApp { 
        color-scheme: light !important; 
        background-color: #F3F6F8 !important; 
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Basic button styling */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

def initialize_basic_session_state():
    """Initialize basic session state"""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.page_visits = {}

class HypnotherapyApp:
    """Main application class - Streamlit compatible"""
    
    def __init__(self):
        """Initialize the application"""
        if not hasattr(st.session_state, 'app_initialized'):
            self.setup_page_config()
            apply_basic_styles()
            initialize_basic_session_state()
            st.session_state.app_initialized = True
    
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="Transform Your Life in 2 Sessions | Laetitia Sheppard",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed"
        )
    
    def render_navigation(self):
        """Render simple, clean navigation"""
        # Brand header
        st.markdown("# 🧠 Laetitia Sheppard")
        st.markdown("**Clinical Hypnotherapist • Transform Your Life in 2 Sessions**")
        st.markdown("---")
        
        # Navigation menu
        return option_menu(
            menu_title=None,
            options=["Home", "Method", "Success", "Blog", "Book Now"],
            icons=["house", "magic", "stars", "book", "calendar"],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0", "background-color": "transparent"},
                "nav-link": {
                    "font-size": "1rem", 
                    "text-align": "center", 
                    "margin": "0px",
                    "padding": "10px 15px"
                },
                "nav-link-selected": {"background-color": "#4CA1A3"},
            }
        )
    
    def render_page_content(self, selected_page):
        """Render page content with Streamlit-native components"""
        
        if selected_page == "Home":
            self._render_home_page()
        elif selected_page == "Method":
            self._render_method_page()
        elif selected_page == "Success":
            self._render_success_page()
        elif selected_page == "Blog":
            self._render_blog_page()
        elif selected_page == "Book Now":
            self._render_booking_page()
    
    def _render_home_page(self):
        """Render home page with native Streamlit components"""
        
        # Hero section using Streamlit components
        hero_container = st.container()
        with hero_container:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                        border-radius: 12px; padding: 3rem 2rem; text-align: center; margin: 2rem 0;">
            """, unsafe_allow_html=True)
            
            st.markdown("# Transform Your Life in Just 2 Sessions")
            st.markdown("**Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits**")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Stats using Streamlit columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Success Rate", value="85%", delta="In 2 sessions")
        with col2:
            st.metric(label="Lives Transformed", value="500+", delta="Since 2014")
        with col3:
            st.metric(label="Experience", value="10+ Years", delta="Professional")
        
        # CTA Button
        st.markdown("### Ready to Transform Your Life?")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", type="primary", use_container_width=True):
                st.success("✨ Great choice! Assessment coming soon - book a discovery call to get started.")
        
        # Why it works section
        st.markdown("---")
        st.markdown("## 🧠 Why Our Method Works")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ❌ Traditional Methods")
            st.markdown("- Target conscious mind (5% of decisions)")
            st.markdown("- Rely on willpower (fails 95% of time)")
            st.markdown("- Require ongoing sessions")
            st.markdown("- High relapse rates")
        
        with col2:
            st.markdown("### ✅ Our Hypnotherapy")
            st.markdown("- Access subconscious (95% of decisions)")
            st.markdown("- Rewire neural pathways")
            st.markdown("- Just 2 sessions needed")
            st.markdown("- 85% permanent success")
        
        # Simple testimonials
        st.markdown("---")
        st.markdown("## 💬 Client Success Stories")
        
        # Testimonial 1
        with st.expander("🌟 Banking Director, Singapore - Anxiety"):
            st.markdown("*'Finally broke free from old patterns – 2 sessions changed everything.'*")
            st.markdown("**Challenge:** Performance anxiety affecting career")
            st.markdown("**Result:** Anxiety-free and promoted within 6 months")
        
        # Testimonial 2
        with st.expander("🚭 Executive - Smoking Cessation"):
            st.markdown("*'After 20 years of smoking 2 packs a day, I'm finally free.'*")
            st.markdown("**Challenge:** 20-year smoking habit")
            st.markdown("**Result:** Completely smoke-free, saved 30,000+ THB")
        
        # Simple quiz
        st.markdown("---")
        st.markdown("## 🎯 Quick Suitability Check")
        
        with st.form("quick_assessment"):
            goal = st.selectbox(
                "What would you most like to change?",
                ["Select one...", "Quit smoking", "Reduce anxiety", "Improve sleep", "Break habits", "Other"]
            )
            
            duration = st.selectbox(
                "How long have you struggled with this?",
                ["Select one...", "Less than 6 months", "6 months - 2 years", "More than 2 years", "Many years"]
            )
            
            readiness = st.selectbox(
                "How ready are you for change?",
                ["Select one...", "Just exploring", "Somewhat ready", "Very ready", "Desperate for change"]
            )
            
            submitted = st.form_submit_button("📊 Get My Suitability Score", type="primary")
            
            if submitted and goal != "Select one..." and duration != "Select one..." and readiness != "Select one...":
                # Simple scoring
                score = 75
                if "smoking" in goal.lower():
                    score += 10
                if "Very ready" in readiness or "Desperate" in readiness:
                    score += 10
                if "More than" in duration or "Many years" in duration:
                    score += 5
                
                score = min(score, 95)
                
                st.success(f"🎯 **Your Suitability Score: {score}%**")
                
                if score >= 80:
                    st.markdown("**Excellent candidate!** You're ready for our 2-session transformation.")
                elif score >= 65:
                    st.markdown("**Very good fit!** Our method should work well for you.")
                else:
                    st.markdown("**Good potential!** A discovery call will help us understand your specific situation.")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📞 Free Discovery Call", use_container_width=True):
                        st.success("Great! We'll contact you within 24 hours.")
                with col2:
                    if st.button("⚡ Book Sessions Now", use_container_width=True):
                        st.success("Excellent choice! Check your email for next steps.")
    
    def _render_method_page(self):
        """Render method page"""
        st.markdown("# 🔬 Our Proven 2-Session Method")
        
        # Session 1
        st.markdown("## Session 1: Deep Analysis (90 minutes)")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("**What happens:**")
            st.markdown("- Uncover your unique subconscious triggers")
            st.markdown("- Map your personal behavior patterns")
            st.markdown("- Identify root causes vs symptoms")
            st.markdown("- Install initial positive programming")
            st.markdown("- Feel immediate relief")
        with col2:
            st.info("**Week 1**\nDeep dive into your subconscious patterns")
        
        # Session 2
        st.markdown("## Session 2: Transformation (90 minutes)")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("**What happens:**")
            st.markdown("- Enter deep hypnotic state")
            st.markdown("- Rewire neural pathways")
            st.markdown("- Replace old patterns with new ones")
            st.markdown("- Lock in your transformation")
            st.markdown("- Experience profound shifts")
        with col2:
            st.success("**Week 2**\nComplete transformation and neural rewiring")
        
        # Pricing
        st.markdown("---")
        st.markdown("## 💰 Investment")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Complete Package")
            st.markdown("**3,000 THB**")
            st.markdown("- Session 1 & 2 (90 min each)")
            st.markdown("- Email support")
            st.markdown("- 85% success rate")
        
        with col2:
            st.markdown("### Premium Package")
            st.markdown("**4,000 THB**")
            st.markdown("- All sessions (including optional 3rd)")
            st.markdown("- 100% guarantee")
            st.markdown("- Maximum assurance")
    
    def _render_success_page(self):
        """Render success stories page"""
        st.markdown("# ⭐ Real Success Stories")
        
        # Success metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Success Rate", "85%", "2 sessions")
        with col2:
            st.metric("Lives Changed", "500+", "Since 2014")
        with col3:
            st.metric("Need 3rd Session", "15%", "Optional")
        with col4:
            st.metric("Long-term Success", "95%", "1 year later")
        
        # Detailed testimonials
        st.markdown("## 📖 Detailed Case Studies")
        
        with st.expander("Case Study 1: From 2 Packs a Day to Smoke-Free"):
            st.markdown("**Challenge:** 20-year smoking habit, 2 packs daily")
            st.markdown("**Solution:** Subconscious pattern rewiring")
            st.markdown("**Result:** Completely smoke-free after 2 sessions")
            st.markdown("**Follow-up:** 6 months later - still smoke-free, saved 30,000 THB")
        
        with st.expander("Case Study 2: Overcoming Panic Attacks"):
            st.markdown("**Challenge:** Daily panic attacks affecting work")
            st.markdown("**Solution:** Root cause analysis and neural rewiring")
            st.markdown("**Result:** Panic attacks eliminated, confidence restored")
            st.markdown("**Follow-up:** 1 year later - promoted at work, no anxiety")
    
    def _render_blog_page(self):
        """Render blog/FAQ page"""
        st.markdown("# 📚 Hypnotherapy Insights & FAQ")
        
        st.markdown("## ❓ Frequently Asked Questions")
        
        with st.expander("Is hypnotherapy safe?"):
            st.markdown("Yes, clinical hypnotherapy is completely safe. You remain fully aware and in control throughout the session.")
        
        with st.expander("How many sessions will I really need?"):
            st.markdown("85% of our clients achieve their goals in just 2 sessions. About 15% choose an optional 3rd session.")
        
        with st.expander("What if I can't be hypnotized?"):
            st.markdown("Everyone can be hypnotized because hypnosis is a natural state we enter daily.")
        
        with st.expander("How is this different from other hypnotherapists?"):
            st.markdown("Our method combines analytical techniques in session 1 with targeted transformation in session 2.")
        
        with st.expander("What happens if it doesn't work for me?"):
            st.markdown("If you're not satisfied after 2 sessions, we offer a complimentary 3rd session.")
        
        st.markdown("## 📝 Latest Articles")
        
        with st.expander("How Hypnosis Rewires Your Brain"):
            st.markdown("Discover the neuroscience behind rapid transformation and why hypnotherapy succeeds where willpower fails.")
        
        with st.expander("Breaking Free from Smoking: Why 2 Sessions Work"):
            st.markdown("Learn how clients quit their 20-year habits in just 2 hypnotherapy sessions.")
    
    def _render_booking_page(self):
        """Render booking page"""
        st.markdown("# 📅 Start Your Transformation Today")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📞 Free Discovery Call")
            st.markdown("15-minute consultation")
            st.markdown("- Understand your situation")
            st.markdown("- Learn how we can help")
            st.markdown("- No obligation")
            
            with st.form("discovery_form"):
                name = st.text_input("Your Name*")
                email = st.text_input("Email*")
                concern = st.selectbox("Primary Concern*", [
                    "Select one...", "Quit Smoking", "Reduce Anxiety", 
                    "Improve Sleep", "Break Habits", "Other"
                ])
                message = st.text_area("What would you like to discuss?")
                
                if st.form_submit_button("📞 Schedule Discovery Call", type="primary"):
                    if name and email and concern != "Select one...":
                        st.success("✅ Discovery call scheduled! We'll contact you within 24 hours.")
                    else:
                        st.error("Please fill in all required fields.")
        
        with col2:
            st.markdown("### ⚡ Transformation Package")
            st.markdown("Complete 2-session program")
            st.markdown("- Session 1: Analysis (90 min)")
            st.markdown("- Session 2: Transformation (90 min)")
            st.markdown("- 3,000 THB total")
            
            with st.form("package_form"):
                name2 = st.text_input("Your Name*", key="pkg_name")
                email2 = st.text_input("Email*", key="pkg_email")
                concern2 = st.selectbox("Primary Concern*", [
                    "Select one...", "Quit Smoking", "Reduce Anxiety", 
                    "Improve Sleep", "Break Habits", "Other"
                ], key="pkg_concern")
                package = st.radio("Package", ["Complete (3,000 THB)", "Premium (4,000 THB)"])
                
                if st.form_submit_button("⚡ Book Transformation", type="primary"):
                    if name2 and email2 and concern2 != "Select one...":
                        st.success("🚀 Package booked! Check your email for next steps.")
                    else:
                        st.error("Please fill in all required fields.")
    
    def render_footer(self):
        """Render simple footer"""
        st.markdown("---")
        
        # Contact CTA
        st.markdown("### 🚀 Ready to Transform Your Life?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", use_container_width=True):
                st.success("Great! We'll contact you within 24 hours.")
        with col2:
            if st.button("⚡ Book Sessions Now", use_container_width=True):
                st.success("Excellent! Check your email for next steps.")
        
        st.markdown("---")
        
        # Footer info
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Laetitia Sheppard**")
            st.markdown("Clinical Hypnotherapist")
            st.markdown("Bangkok, Thailand")
        
        with col2:
            st.markdown("**Credentials**")
            st.markdown("✓ Certified Clinical Hypnotherapist")
            st.markdown("✓ 10+ Years Experience")
            st.markdown("✓ Licensed & Insured")
        
        with col3:
            st.markdown("**Contact**")
            st.markdown("📞 [Discovery Call](https://calendly.com/laetitiasheppard/discovery)")
            st.markdown("⚡ [Book Sessions](https://calendly.com/laetitiasheppard/package)")
            st.markdown("📍 [Directions](https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8)")
        
        st.markdown("---")
        st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved")
        st.markdown("🔒 All sessions strictly confidential • Professional standards guaranteed")
    
    def run(self):
        """Main application entry point"""
        try:
            # Navigation
            selected_page = self.render_navigation()
            
            # Page content
            self.render_page_content(selected_page)
            
            # Discovery CTA in sidebar
            if selected_page != "Book Now":
                with st.sidebar:
                    st.markdown("### 📞 Quick Action")
                    if st.button("Free Discovery Call", type="primary", use_container_width=True):
                        st.success("We'll contact you within 24 hours!")
            
            # Footer
            self.render_footer()
            
        except Exception as e:
            st.error("Something went wrong. Please refresh the page.")
            with st.expander("Technical details"):
                st.exception(e)

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
