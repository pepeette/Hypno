"""
Professional Home Page - Streamlit-native with all original features
Maintains quiz integration, testimonials, and CTAs with improved design
"""
from utils import styling, config
from components.footer import show_footer
from components.navigation import show_navigation
import streamlit as st

class HomePage:
    def __init__(self):
        self._init_session_state()
        
    def _init_session_state(self):
        """Ensure all session state variables exist"""
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'show_quiz' not in st.session_state:
            st.session_state.show_quiz = False

    def render(self):
        """Main render method with all sections"""
        self._inject_custom_css()
        show_navigation()
        self._render_hero()
        self._render_quiz_section()
        self._render_differentiators()
        self._render_benefits()
        #self._render_testimonials()
        self._render_final_cta()
        show_footer()

    def _inject_custom_css(self):
        """Inject design system CSS"""
        st.markdown(f"""
        <style>
        /* Hero section styling */
        .hero-gradient {{
            background: linear-gradient(135deg, {config.accent_color} 0%, #E1F0F0 100%);
            padding: 3rem 1rem;
            border-radius: {config.radius_lg};
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: {config.shadow_sm};
        }}
        
        /* Testimonial cards */
        .testimonial-card {{
            background: {config.card_bg};
            border-left: 4px solid {config.accent_color};
            padding: 1.5rem;
            border-radius: {config.radius_md};
            margin-bottom: 1rem;
            box-shadow: {config.shadow_sm};
            transition: {config.transition};
        }}
        .testimonial-card:hover {{
            transform: translateY(-3px);
            box-shadow: {config.shadow_md};
        }}
        
        /* Metrics styling */
        .metric-container {{
            background: {config.card_bg};
            padding: 1rem;
            border-radius: {config.radius_md};
            text-align: center;
            box-shadow: {config.shadow_sm};
        }}
        </style>
        """, unsafe_allow_html=True)

    def _render_hero(self):
        """Enhanced hero section with metrics"""
        with st.container():
            st.markdown("""
            <div class="hero-gradient">
                <h1 style='color:white;'>Transform Your Life in 2 Sessions</h1>
                <h2 style='color:white; opacity:0.9;'>
                    Science-backed hypnotherapy in Bangkok
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # # Metrics in cards
            # cols = st.columns(3)
            # metrics = [
            #     ("✅", "85%", "Success Rate"),
            #     ("🧠", "500+", "Clients Helped"), 
            #     ("⭐", "10", "Years Experience")
            # ]
            
            # for col, (icon, value, label) in zip(cols, metrics):
            #     with col:
            #         st.markdown(f"""
            #         <div class="metric-container">
            #             <p style='font-size:2rem; margin-bottom:0;'>{icon}</p>
            #             <h3 style='margin-top:0;'>{value}</h3>
            #             <p>{label}</p>
            #         </div>
            #         """, unsafe_allow_html=True)

    def _render_differentiators(self):
        """Comparison section with toggle"""
        st.markdown("---")
        st.markdown("## Why Our Method Works")
        
        with st.expander("Compare with Traditional Therapy", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### ❌ Conventional Methods")
                st.write("""
                - Months/years of therapy
                - Focus on symptoms
                - Requires willpower
                - High relapse rates
                """)
            
            with col2:
                st.markdown("### ✅ Our Approach")
                st.write("""
                - Just 2 sessions
                - Targets root causes
                - Works automatically  
                - Long-term results
                """)
        
        st.markdown(f"""
        <div style='background:{config.card_bg}; padding:1rem; border-radius:{config.radius_md};'>
        <p><strong>The Science:</strong> Hypnotherapy accesses the subconscious mind where 95% of decisions originate</p>
        </div>
        """, unsafe_allow_html=True)

    def _render_quiz_section(self):
        """Quiz section with state management"""
        st.markdown("---")
        st.markdown("## Free Suitability Assessment")
        
        if not st.session_state.quiz_completed:
            st.markdown("""
            <div style='background:#f8fafc; padding:1.5rem; border-radius:8px;'>
            <p>Complete this 3-question assessment to see if you're a good candidate:</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Start Assessment", type="primary", key="quiz_start"):
                st.session_state.show_quiz = True
                st.rerun()
        else:
            st.success("✅ You've completed the assessment! Scroll down to book your session.")

    def _render_benefits(self):
        """Benefits with icon cards"""
        st.markdown("---")
        st.markdown("## Key Benefits")
        
        benefits = [
            ("⚡", "Rapid Results", "Most clients see changes after just 1 session"),
            ("🎯", "Precision Focus", "Customized for your specific challenge"),
            ("🧠", "Science-Based", "Uses proven neuroplasticity principles"),
            ("💯", "Proven Success", "85% achievement rate in clinical studies")
        ]
        
        cols = st.columns(2)
        for i, (icon, title, desc) in enumerate(benefits):
            with cols[i % 2]:
                with st.container():
                    st.markdown(f"""
                    <div style='background:{config.card_bg}; padding:1.5rem; border-radius:{config.radius_md};'>
                        <h3>{icon} {title}</h3>
                        <p>{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")

    def _render_testimonials(self):
        """Enhanced testimonials with hover effects"""
        st.markdown("---")
        st.markdown("## Client Success Stories")
        
        testimonials = [
            {
                "icon": "🌟",
                "title": "Banking Executive",
                "quote": "After 10 years of anxiety, I found relief in just 2 sessions",
                "result": "Anxiety management"
            },
            {
                "icon": "🚭", 
                "title": "Long-Term Smoker",
                "quote": "Quit after 15 years without withdrawal symptoms",
                "result": "Smoking cessation"
            }
        ]
        
        for t in testimonials:
            st.markdown(f"""
            <div class="testimonial-card">
                <div style="display:flex; align-items:center; gap:1rem;">
                    <span style="font-size:2rem;">{t['icon']}</span>
                    <div>
                        <h3>{t['title']}</h3>
                        <p><em>"{t['quote']}"</em></p>
                        <p><strong>Result:</strong> {t['result']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    def _render_final_cta(self):
        """Professional CTA section"""
        st.markdown("---")
        
        with st.container():
            st.markdown(f"""
            <div style='background:{config.card_bg}; padding:3rem; text-align:center; border-radius:{config.radius_lg};'>
                <h2>Ready for Transformation?</h2>
                <p style='margin-bottom:2rem;'>Take the first step toward lasting change</p>
                
                <div style='display:flex; justify-content:center; gap:1rem;'>
                    <a href="#quiz">
                        <button class="stButton" style='background:{config.accent_color};color:white;border:none;padding:0.5rem 1rem;border-radius:{config.radius_md};'>
                            Take Assessment
                        </button>
                    </a>
                    <a href="?page=booking">
                        <button class="stButton" style='background:{config.text_primary};color:white;border:none;padding:0.5rem 1rem;border-radius:{config.radius_md};'>
                            Book Now
                        </button>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

def create_home_page():
    """Factory function"""
    return HomePage()
