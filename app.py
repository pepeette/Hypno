import streamlit as st
import sys
import os

# Add current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class HypnotherapyApp:
    """Main application class that orchestrates all components"""
    
    def __init__(self):
        """Initialize the application with proper component loading"""
        self.setup_page_config()
        self.load_utilities()
        self.load_components()
        
    def setup_page_config(self):
        """Configure Streamlit page settings"""
        try:
            from utils.config import PageConfig
            PageConfig.setup()
        except ImportError:
            # Fallback page config
            st.set_page_config(
                page_title="2-Step Hypnotherapy | Laetitia Sheppard",
                page_icon="🧠",
                layout="wide",
                initial_sidebar_state="collapsed",
                menu_items={
                    'Get Help': 'https://laetitiasheppard.com/help',
                    'Report a bug': 'https://laetitiasheppard.com/bug-report',
                    'About': "Transform your life with science-backed hypnotherapy"
                }
            )
    
    def load_utilities(self):
        """Load utility modules with error handling"""
        # Load styling
        try:
            from utils.styling import apply_global_styles
            apply_global_styles()
            self.styling_loaded = True
        except ImportError:
            st.warning("⚠️ Styling module not found. Using fallback styles.")
            self._apply_fallback_styles()
            self.styling_loaded = False
        except Exception as e:
            st.error(f"❌ Error loading styling: {e}")
            self._apply_fallback_styles()
            self.styling_loaded = False
        
        # Initialize session state
        try:
            from utils.session_state import initialize_session_state
            initialize_session_state()
            self.session_state_loaded = True
        except ImportError:
            st.warning("⚠️ Session state module not found. Using basic initialization.")
            self._init_basic_session_state()
            self.session_state_loaded = False
        except Exception as e:
            st.error(f"❌ Error initializing session state: {e}")
            self._init_basic_session_state()
            self.session_state_loaded = False
    
    def _apply_fallback_styles(self):
        """Apply basic fallback CSS if main styling fails"""
        st.markdown("""
        <style>
        :root {
            --accent: #4CA1A3;
            --accent-hover: #3B7A7A;
            --text-primary: #273548;
            --text-secondary: #556D7A;
            --border: #CBD5E1;
            --bg: #F3F6F8;
            --card-bg: #FFFFFF;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
            --radius-md: 12px;
        }
        
        .stApp {
            background-color: var(--bg);
            color: var(--text-primary);
        }
        
        h1, h2, h3 { color: var(--text-primary); }
        
        .stButton > button {
            background-color: var(--accent);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }
        
        .stButton > button:hover {
            background-color: var(--accent-hover);
        }
        
        #MainMenu, footer, header { visibility: hidden; }
        </style>
        """, unsafe_allow_html=True)
    
    def _init_basic_session_state(self):
        """Basic session state initialization fallback"""
        if 'app_initialized' not in st.session_state:
            st.session_state.app_initialized = True
            st.session_state.current_page = "Home"
    
    def load_components(self):
        """Load all components with proper error handling"""
        # Navigation component
        try:
            from components.navigation import Navigation
            self.navigation = Navigation()
            self.navigation_loaded = True
        except ImportError:
            st.warning("⚠️ Navigation component not found. Using fallback navigation.")
            self.navigation = None
            self.navigation_loaded = False
        except Exception as e:
            st.error(f"❌ Error loading navigation: {e}")
            self.navigation = None
            self.navigation_loaded = False
        
        # Footer component
        try:
            from components.footer import Footer
            self.footer = Footer()
            self.footer_loaded = True
        except ImportError:
            st.warning("⚠️ Footer component not found. Using fallback footer.")
            self.footer = None
            self.footer_loaded = False
        except Exception as e:
            st.error(f"❌ Error loading footer: {e}")
            self.footer = None
            self.footer_loaded = False
    
    def create_navigation(self):
        """Create navigation menu with fallback"""
        if self.navigation_loaded and self.navigation:
            try:
                return self.navigation.create_menu()
            except Exception as e:
                st.error(f"❌ Error creating navigation menu: {e}")
                return self._fallback_navigation()
        else:
            return self._fallback_navigation()
    
    def _fallback_navigation(self):
        """Fallback navigation menu"""
        try:
            from streamlit_option_menu import option_menu
            return option_menu(
                menu_title=None,
                options=["Home", "Method", "Success", "Blog", "Book Now"],
                icons=["house", "magic", "stars", "book", "calendar"],
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "0", "background-color": "transparent"},
                    "nav-link": {"color": "#556D7A", "border-radius": "8px"},
                    "nav-link-selected": {"background": "#4CA1A3", "color": "white"}
                }
            )
        except ImportError:
            return st.selectbox(
                "Navigation", 
                ["Home", "Method", "Success", "Blog", "Book Now"],
                label_visibility="collapsed"
            )
    
    def load_page_component(self, page_name):
        """Dynamically load page components with error handling"""
        try:
            if page_name == "Home":
                from pages.home import HomePage
                return HomePage()
            elif page_name == "Method":
                from pages.method import MethodPage
                return MethodPage()
            elif page_name == "Success":
                from pages.success import SuccessPage
                return SuccessPage()
            elif page_name == "Blog":
                from pages.blog import BlogPage
                return BlogPage()
            elif page_name == "Book Now":
                from pages.booking import BookingPage
                return BookingPage()
            else:
                return None
        except ImportError as e:
            st.warning(f"⚠️ {page_name} page component not found: {e}")
            return None
        except Exception as e:
            st.error(f"❌ Error loading {page_name} page: {e}")
            return None
    
    def render_page_content(self, selected_page):
            """Render the selected page content"""
            page_component = self.load_page_component(selected_page)
            
            if page_component:
                try:
                    page_component.render()
                    return  # ← ADD THIS LINE - STOPS FALLBACK FROM SHOWING
                except Exception as e:
                    st.error(f"❌ Error rendering {selected_page} page: {e}")
                    self._render_fallback_content(selected_page)
            else:
                self._render_fallback_content(selected_page)
    
    def _render_fallback_content(self, page_name):
        """Render fallback content if page component fails"""
        st.title(f"{page_name}")
        
        if page_name == "Home":
            st.markdown("""
            ## Welcome to 2-Step Hypnotherapy
            
            Transform your life with our science-backed approach:
            - **85% success rate** in just 2 sessions
            - **Professional certification** and 10+ years experience
            - **Personalized approach** for lasting change
            
            🎯 Take our 30-second assessment to see if you're a good fit!
            """)
            
            if st.button("📞 Book Free Discovery Call", type="primary", use_container_width=True):
                st.success("✅ Great! We'll contact you within 24 hours.")
                
        elif page_name == "Method":
            st.markdown("""
            ## Our Proven 2-Step Method
            
            **Session 1: Deep Analysis** (90 minutes)
            - Uncover subconscious patterns driving your behavior
            - Map your unique triggers and responses
            - Begin positive programming and immediate relief
            
            **Session 2: Transformation** (90 minutes) 
            - Complete neural pathway rewiring
            - Install new, empowering behaviors
            - Lock in lasting change at the subconscious level
            
            **Results:** 85% of clients achieve their goals in just these 2 sessions.
            """)
            
        elif page_name == "Success":
            st.markdown("""
            ## Real Success Stories
            
            ### 🌟 "Finally broke free from old patterns"
            *Director, Banking, Singapore*  
            **Challenge:** Anxiety patterns affecting work performance  
            **Result:** Complete transformation in 2 sessions
            
            ### 🚭 "No more addiction" 
            *Wife describing her husband's transformation, Bangkok*  
            **Challenge:** 20-year smoking habit, 2 packs daily  
            **Result:** Completely smoke-free after 2 sessions
            
            ### 📈 Our Success Metrics
            - **85%** achieve goals in 2 sessions
            - **15%** choose optional 3rd session
            - **500+** lives transformed since 2014
            """)
            
        elif page_name == "Blog":
            st.markdown("""
            ## Hypnotherapy Insights & FAQ
            
            ### 🧠 How Hypnosis Rewires Your Brain
            Discover the neuroscience behind rapid transformation and why hypnotherapy succeeds where willpower fails.
            
            ### ❓ Frequently Asked Questions
            
            **Is hypnotherapy safe?**  
            Yes, completely safe. You remain aware and in control throughout.
            
            **How many sessions will I need?**  
            85% of clients achieve their goals in just 2 sessions.
            
            **What if I can't be hypnotized?**  
            Everyone can be hypnotized - it's a natural state we enter daily.
            
            **Will I lose control?**  
            Absolutely not. You're an active participant in your transformation.
            """)
            
        elif page_name == "Book Now":
            st.markdown("""
            ## Start Your Transformation Today
            
            ### 📞 Free 15-Minute Discovery Call
            Perfect if you want to:
            - Understand how hypnotherapy works
            - Assess your suitability
            - Ask questions about the process
            
            ### ⚡ Complete Transformation Package
            **3,000 THB** - 2 sessions that change everything
            - Session 1: Deep analysis (90 min)
            - Session 2: Transformation (90 min)
            - Email support between sessions
            - 85% success rate
            
            ### 📍 Contact Information
            **Bangkok Hypnotherapy Clinic**  
            27 Soi Sukhumvit 10 (Asoke)  
            Bangkok, Thailand  
            
            **Email:** laetitiasheppard@gmail.com  
            **Sessions:** In-person or online worldwide
            """)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📞 Free Discovery Call", use_container_width=True):
                    st.success("✅ We'll contact you within 24 hours!")
            with col2:
                if st.button("⚡ Book Package Now", use_container_width=True):
                    st.success("✅ Great choice! Check your email for next steps.")
    
    def render_booking_section(self, selected_page):
        """Render booking form on relevant pages"""
        if selected_page != "Book Now":
            try:
                from components.booking_form import BookingForm
                booking_form = BookingForm()
                st.markdown("---")
                booking_form.render_compact()
            except ImportError:
                st.markdown("---")
                st.markdown("### 📞 Ready to Start?")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Free Discovery Call", key=f"compact_discovery_{selected_page}"):
                        st.success("We'll contact you soon!")
                with col2:
                    if st.button("Book Sessions Now", key=f"compact_book_{selected_page}"):
                        st.success("Great choice!")
            except Exception as e:
                st.error(f"Error loading booking form: {e}")
    
    def render_footer(self):
        """Render footer with fallback"""
        if self.footer_loaded and self.footer:
            try:
                self.footer.render()
            except Exception as e:
                st.error(f"❌ Error rendering footer: {e}")
                self._render_fallback_footer()
        else:
            self._render_fallback_footer()
    
    def _render_fallback_footer(self):
        """Fallback footer if main footer fails"""
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Laetitia Sheppard**  
            Certified Clinical Hypnotherapist  
            10+ Years Experience  
            Bangkok, Thailand
            """)
        
        with col2:
            st.markdown("""
            **Contact Information**  
            📧 laetitiasheppard@gmail.com  
            📍 Bangkok Hypnotherapy Clinic  
            27 Soi Sukhumvit 10 (Asoke)
            """)
        
        st.markdown("---")
        st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved • 🔒 Confidential & Professional")
    
    def run(self):
        """Main application entry point"""
        try:
            # Create navigation and get selected page
            selected_page = self.create_navigation()
            
            # Track page visit if session state is loaded
            if self.session_state_loaded:
                try:
                    from utils.session_state import track_page_visit
                    track_page_visit(selected_page)
                except:
                    pass
            
            # Render main page content
            self.render_page_content(selected_page)
            
            # Add booking section (except on booking page)
            self.render_booking_section(selected_page)
            
            # Render footer
            self.render_footer()
            
        except Exception as e:
            st.error("❌ Application error occurred. Please refresh the page.")
            st.exception(e)
            
            # Show debug info if in development
            if st.secrets.get("debug_mode", False):
                with st.expander("🔧 Debug Information"):
                    st.write("**Component Status:**")
                    st.write(f"- Styling loaded: {getattr(self, 'styling_loaded', False)}")
                    st.write(f"- Session state loaded: {getattr(self, 'session_state_loaded', False)}")
                    st.write(f"- Navigation loaded: {getattr(self, 'navigation_loaded', False)}")
                    st.write(f"- Footer loaded: {getattr(self, 'footer_loaded', False)}")

def main():
    """Application entry point"""
    app = HypnotherapyApp()
    app.run()

if __name__ == "__main__":
    main()
