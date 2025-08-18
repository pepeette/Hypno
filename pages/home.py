"""
Optimized Home Page - Streamlit-native with enforced design system
3 font sizes only (H1, H2, P), no text shadows, forced light mode
"""
from utils import styling, config
import streamlit as st

class HomePage:
    def render(self):
        """Render home page with strict design system enforcement"""
        self._inject_css()
        self._render_hero()
        self._render_differentiators()
        self._render_quiz_section()
        self._render_benefits()
        self._render_testimonials()
        self._render_final_cta()
    
    def _inject_css(self):
        """Force light mode and enforce design system"""
        st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {config.bg_color};
        }}
        .hero-container {{
            background: linear-gradient(135deg, {config.accent_color} 0%, #E1F0F0 100%);
            padding: 3rem 1rem;
            border-radius: {config.radius_lg};
            margin-bottom: 2rem;
            text-align: center;
        }}
        .testimonial-card {{
            background: {config.card_bg};
            border-left: 4px solid {config.accent_color};
            padding: 1.5rem;
            border-radius: {config.radius_md};
            margin-bottom: 1rem;
        }}
        </style>
        """, unsafe_allow_html=True)
    
    def _render_hero(self):
        """Hero section using pure Streamlit components"""
        with st.container():
            st.markdown(f"""
            <div class="hero-container">
                <h1 style='color:white;'>Transform Your Life in 2 Sessions</h1>
                <h2 style='color:white; opacity:0.9;'>
                    Science-backed hypnotherapy in Bangkok
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            # # Metrics using config colors
            # cols = st.columns(3)
            # metrics_style = f"color: {config.text_primary}; font-size: 1rem;"
            # with cols[0]:
            #     st.markdown(f"<p style='{metrics_style}'>✅ <strong>85%</strong> Success Rate</p>", unsafe_allow_html=True)
            # with cols[1]:
            #     st.markdown(f"<p style='{metrics_style}'>🧠 <strong>500+</strong> Clients Helped</p>", unsafe_allow_html=True)
            # with cols[2]:
            #     st.markdown(f"<p style='{metrics_style}'>⭐ <strong>10</strong> Years Experience</p>", unsafe_allow_html=True)
    
    def _render_differentiators(self):
        """Key differentiators with enforced typography"""
        st.markdown("---")
        st.markdown("## Why Our Method Works")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Traditional Therapy")
            st.write("""
            - Requires months/years
            - Focuses on symptoms
            - High relapse rates
            - Depends on willpower
            """)
        
        with col2:
            st.markdown("### Our Hypnotherapy")
            st.write("""
            - Just 2 sessions needed
            - Targets root causes
            - Long-term results
            - Works automatically
            """)
        
        st.markdown(f"""
        <div style='background:{config.card_bg}; padding:1rem; border-radius:{config.radius_md};'>
        <p><strong>Key Difference:</strong> We reprogram your subconscious mind (where 95% of decisions originate)</p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_quiz_section(self):
        """Quiz section placeholder"""
        st.markdown("---")
        st.markdown("## Free Suitability Assessment")
        st.write("Discover your potential for change in 30 seconds")
        
        # Quiz anchor for main app to inject component
        st.markdown('<div id="quiz"></div>', unsafe_allow_html=True)
        
        if not st.session_state.get('quiz_completed'):
            if st.button("Start Quick Assessment", type="primary"):
                st.session_state.show_quiz = True
    
    def _render_benefits(self):
        """Benefits with consistent styling"""
        st.markdown("---")
        st.markdown("## Key Benefits")
        
        benefits = [
            ("⚡", "Rapid Results", "See changes in just 2 sessions"),
            ("🎯", "Precision Focus", "Targets your specific challenge"),
            ("🧠", "Science-Based", "Uses proven neuroplasticity"),
            ("💯", "High Success", "85% achieve their goals")
        ]
        
        cols = st.columns(2)
        for i, (emoji, title, desc) in enumerate(benefits):
            with cols[i % 2]:
                st.markdown(f"### {emoji} {title}")
                st.write(desc)
    
    def _render_testimonials(self):
        """Testimonials with card styling"""
        st.markdown("---")
        st.markdown("## Client Experiences")
        
        testimonials = [
            {
                "title": "Banking Director",
                "quote": "Finally broke free from old patterns in just 2 sessions",
                "result": "Overcame anxiety"
            },
            {
                "title": "Medical Student",
                "quote": "Went from failing to top of my class after therapy",
                "result": "Solved study anxiety"
            }
        ]
        
        for t in testimonials:
            st.markdown(f"""
            <div class="testimonial-card">
                <h3>{t['title']}</h3>
                <p><em>"{t['quote']}"</em></p>
                <p>Result: {t['result']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_final_cta(self):
        """Final CTA with accent color"""
        st.markdown("---")
        st.markdown("## Ready for Change?")
        
        st.markdown(f"""
        <div style='background:{config.card_bg}; padding:2rem; text-align:center; border-radius:{config.radius_md};'>
            <h2>Take the First Step Today</h2>
            <p>Book your free discovery call to discuss your goals</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Book Free Consultation", type="primary", use_container_width=True):
            st.session_state.show_booking = True

def create_home_page():
    return HomePage()
