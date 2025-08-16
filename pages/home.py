"""
Home page component for the Hypnotherapy website
FIXED: One div per st.markdown call
"""
import streamlit as st

class HeroSection:
    """Hero section with proper div separation"""
    
    def render(self):
        """Render hero section with separate div calls"""
        # Opening hero container
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 2rem 0; box-shadow: var(--shadow-sm);">
        """, unsafe_allow_html=True)
        
        # Title
        st.markdown("""
        <h1 style="color: white; margin-bottom: 1rem;">Transform Your Life in Just 2 Sessions</h1>
        """, unsafe_allow_html=True)
        
        # Subtitle
        st.markdown("""
        <p style="font-size: 1.1rem; color: white; opacity: 0.95; 
                  max-width: 600px; margin: 0 auto 2rem auto;">
            Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
        </p>
        """, unsafe_allow_html=True)
        
        # Stats container opening
        st.markdown("""
        <div style="display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap;">
        """, unsafe_allow_html=True)
        
        # Individual stat items
        st.markdown("""
        <div style="text-align: center; color: white; margin: 1rem;">
            <div style="font-size: 2.5rem; font-weight: bold;">85%</div>
            <p style="margin: 0; font-weight: 600;">Success in 2 Sessions</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; color: white; margin: 1rem;">
            <div style="font-size: 2.5rem; font-weight: bold;">500+</div>
            <p style="margin: 0; font-weight: 600;">Lives Transformed</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; color: white; margin: 1rem;">
            <div style="font-size: 2.5rem; font-weight: bold;">10+</div>
            <p style="margin: 0; font-weight: 600;">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Close stats container
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Close hero container
        st.markdown("</div>", unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                st.success("Assessment coming soon! Book a discovery call instead.")

class KeyDifferentiator:
    """Key differentiator with single div"""
    
    def render(self):
        """Render differentiator with proper div separation"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, var(--card-bg) 100%); 
                    border-radius: var(--radius-md); padding: 2rem; margin: 2rem 0; 
                    border-left: 4px solid var(--accent);">
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <h2 style="color: var(--accent); margin-bottom: 1rem;">🧠 Why Our Method Works</h2>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style="font-size: 1.1rem; line-height: 1.7;">
            Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
            Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

class BenefitsSection:
    """Benefits section with proper div structure"""
    
    def render(self):
        """Render benefits with separate divs"""
        # Header
        st.markdown("""
        <div style="text-align: center; margin: 3rem 0 2rem 0;">
        """, unsafe_allow_html=True)
        
        st.markdown("<h2>Why Choose Our 2-Session Method?</h2>", unsafe_allow_html=True)
        st.markdown('<p style="color: var(--text-secondary);">Four key advantages that create lasting transformation</p>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Benefits using Streamlit columns instead of complex grid
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border); margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Rapid Results</h3>
                <p style="color: var(--text-secondary); line-height: 1.6;">
                    See transformation in just 2 sessions, not months of therapy
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border); margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Targeted Approach</h3>
                <p style="color: var(--text-secondary); line-height: 1.6;">
                    Personalized sessions designed for your specific challenges
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border); margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Science-Backed</h3>
                <p style="color: var(--text-secondary); line-height: 1.6;">
                    Uses proven neuroplasticity principles to rewire your subconscious
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border); margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💯</div>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">High Success Rate</h3>
                <p style="color: var(--text-secondary); line-height: 1.6;">
                    85% of clients achieve their goals in our 2-session program
                </p>
            </div>
            """, unsafe_allow_html=True)

class TestimonialsSection:
    """Testimonials with single divs"""
    
    def render(self):
        """Render testimonials properly"""
        st.markdown("## 💬 Client Success Stories")
        
        # Testimonial 1
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 1.5rem; margin: 1rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); border-left: 4px solid var(--accent);">
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">🌟</div>
            <div style="flex: 1;">
                <blockquote style="font-style: italic; font-size: 1.2rem; 
                                   color: var(--text-primary); margin: 0 0 1rem 0; line-height: 1.6;">
                    "Finally broke free from old patterns – 2 sessions changed everything."
                </blockquote>
                <div style="font-weight: 600; color: var(--text-secondary);">— Director, Banking, Singapore</div>
                <div style="color: var(--accent); font-size: 0.9rem;">🎯 Anxiety patterns • ⏱️ 2 sessions</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Testimonial 2
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 1.5rem; margin: 1rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); border-left: 4px solid var(--accent);">
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
            <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">🚭</div>
            <div style="flex: 1;">
                <blockquote style="font-style: italic; font-size: 1.2rem; 
                                   color: var(--text-primary); margin: 0 0 1rem 0; line-height: 1.6;">
                    "My husband was a heavy smoker... No more addiction."
                </blockquote>
                <div style="font-weight: 600; color: var(--text-secondary);">— Wife, Bangkok</div>
                <div style="color: var(--accent); font-size: 0.9rem;">🎯 Smoking cessation • ⏱️ 2 sessions</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

class HomePage:
    """Main home page with proper div structure"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.differentiator = KeyDifferentiator()
        self.benefits = BenefitsSection()
        self.testimonials = TestimonialsSection()
    
    def render(self):
        """Render complete home page"""
        # Hero section
        self.hero.render()
        
        # Key differentiator
        self.differentiator.render()
        
        # Quiz placeholder
        self._render_quiz_placeholder()
        
        # Benefits
        self.benefits.render()
        
        # Testimonials
        self.testimonials.render()
        
        # Final CTA
        self._render_final_cta()
    
    def _render_quiz_placeholder(self):
        """Quiz placeholder with single div"""
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); text-align: center;">
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Interactive Assessment Coming Soon!</h3>", unsafe_allow_html=True)
        st.markdown('<p style="color: var(--text-secondary);">For now, book a free discovery call to assess your suitability</p>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_cta", type="primary", use_container_width=True):
                st.success("We'll contact you within 24 hours!")
    
    def _render_final_cta(self):
        """Final CTA with single div"""
        st.markdown("---")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0;">
        """, unsafe_allow_html=True)
        
        st.markdown('<h2 style="color: white; margin-bottom: 1rem;">Ready to Transform Your Life?</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <p style="color: white; opacity: 0.9; font-size: 1.1rem; margin-bottom: 2rem;">
            Join hundreds of people who have transformed their lives with our proven method.
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # CTA Buttons
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

def create_home_page():
    return HomePage()
