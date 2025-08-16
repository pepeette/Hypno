import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure the page first
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

# Apply basic styling
def apply_basic_styles():
    """Apply essential styling"""
    st.markdown("""
    <style>
    :root {
        --bg: #F3F6F8;
        --card-bg: #FFFFFF;
        --text-primary: #273548;
        --text-secondary: #556D7A;
        --accent: #4CA1A3;
        --accent-hover: #3B7A7A;
        --border: #CBD5E1;
        --success: #22c55e;
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s ease;
    }
    
    .stApp {
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    h1 {
        color: var(--text-primary) !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    
    h2, h3 {
        color: var(--text-primary) !important;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
    }
    
    .stButton > button {
        background-color: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
    }
    
    .stButton > button:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px) !important;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def create_navigation():
    """Create simple navigation"""
    try:
        from streamlit_option_menu import option_menu
        selected = option_menu(
            menu_title=None,
            options=["Home", "Method", "Success", "Blog", "Book Now"],
            icons=["house", "magic", "stars", "book", "calendar"],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0", "background-color": "transparent"},
                "nav-link": {
                    "font-size": "1rem",
                    "padding": "12px 20px",
                    "color": "#556D7A",
                    "border-radius": "8px"
                },
                "nav-link-selected": {
                    "background": "#4CA1A3",
                    "color": "white"
                }
            }
        )
        return selected
    except ImportError:
        # Fallback to selectbox if option_menu not available
        return st.selectbox("Navigation", ["Home", "Method", "Success", "Blog", "Book Now"], label_visibility="collapsed")

class SimpleHomePage:
    """Simplified home page that will definitely work"""
    
    def render(self):
        """Render the home page"""
        # Hero Section
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%);
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white; margin-bottom: 1rem;">Transform Your Life in Just 2 Sessions</h1>
            <p style="color: white; opacity: 0.95; font-size: 1.1rem; margin-bottom: 2rem;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">
                <div style="text-align: center; color: white;">
                    <div style="font-size: 2.5rem; font-weight: bold;">500+</div>
                    <div>Lives Transformed</div>
                </div>
                <div style="text-align: center; color: white;">
                    <div style="font-size: 2.5rem; font-weight: bold;">10+</div>
                    <div>Years Experience</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                st.success("Assessment coming soon! Book a discovery call instead.")
        
        # Key Differentiator
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, white 100%);
                    border-radius: 12px; padding: 2rem; margin: 2rem 0;
                    border-left: 4px solid #4CA1A3;">
            <h2 style="color: #4CA1A3;">🧠 Why Our Method Works</h2>
            <p style="font-size: 1.1rem; line-height: 1.7;">
                Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
                Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Benefits Section
        st.markdown("## Why Choose Our 2-Session Method?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                <h3>Rapid Results</h3>
                <p>See transformation in just 2 sessions, not months of therapy</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h3>Targeted Approach</h3>
                <p>Personalized sessions designed for your specific challenges</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
                <h3>Science-Backed</h3>
                <p>Uses proven neuroplasticity principles to rewire your subconscious</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💯</div>
                <h3>High Success Rate</h3>
                <p>85% of clients achieve their goals in our 2-session program</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Testimonials
        st.markdown("## 💬 Client Success Stories")
        
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-left: 4px solid #4CA1A3;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2.5rem; color: #4CA1A3;">🌟</div>
                <div>
                    <blockquote style="font-style: italic; font-size: 1.2rem; margin: 0 0 1rem 0;">
                        "Finally broke free from old patterns – 2 sessions changed everything."
                    </blockquote>
                    <div style="font-weight: 600;">— Director, Banking, Singapore</div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">🎯 Anxiety patterns • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-left: 4px solid #4CA1A3;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2.5rem; color: #4CA1A3;">🚭</div>
                <div>
                    <blockquote style="font-style: italic; font-size: 1.2rem; margin: 0 0 1rem 0;">
                        "My husband was a heavy smoker... No more addiction."
                    </blockquote>
                    <div style="font-weight: 600;">— Wife, Bangkok</div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">🎯 Smoking cessation • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Final CTA
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; margin: 4rem 0;">
            <h2 style="color: white;">Ready to Transform Your Life?</h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Final buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True):
                st.success("Excellent choice!")
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                st.success("Redirecting to Method page...")
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                st.success("Great! Let's get started.")

def render_fallback_page(page_name):
    """Render fallback content for other pages"""
    st.title(f"{page_name} - Coming Soon")
    st.info(f"The {page_name} page is being prepared. Please check back soon!")
    
    if page_name == "Method":
        st.markdown("""
        ## Our Proven 2-Step Method
        
        **Session 1: Deep Analysis** (90 minutes)
        - Uncover subconscious patterns
        - Map your unique triggers
        - Begin positive programming
        
        **Session 2: Transformation** (90 minutes)
        - Neural pathway rewiring
        - Install new behaviors
        - Lock in lasting change
        """)
    elif page_name == "Book Now":
        st.markdown("""
        ## Start Your Transformation
        
        **Contact Information:**
        - **Email:** laetitiasheppard@gmail.com
        - **Location:** Bangkok, Thailand
        - **Sessions:** In-person or online worldwide
        
        Book your free discovery call to get started!
        """)

def render_simple_footer():
    """Render a simple footer"""
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Laetitia Sheppard**  
        Certified Clinical Hypnotherapist  
        Bangkok, Thailand
        """)
    
    with col2:
        st.markdown("""
        **Contact**  
        📧 laetitiasheppard@gmail.com  
        📍 Bangkok Hypnotherapy Clinic
        """)
    
    st.markdown("---")
    st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved")

def main():
    """Main application function"""
    try:
        # Apply styling
        apply_basic_styles()
        
        # Create navigation
        selected_page = create_navigation()
        
        # Render page content
        if selected_page == "Home":
            home_page = SimpleHomePage()
            home_page.render()
        else:
            render_fallback_page(selected_page)
        
        # Add some spacing before footer
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Render footer
        render_simple_footer()
        
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.info("Please refresh the page to try again.")
        
        # Show error details in development
        if st.secrets.get("debug_mode", False):
            st.exception(e)

if __name__ == "__main__":
    main()85%</div>
                    <div>Success in 2 Sessions</div>
                </div>
                <div style="text-align: center; color: white;">
                    <div style="font-size: 2.5rem; font-weight: bold;">
