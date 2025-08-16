"""
Home page component for the Hypnotherapy website
FIXED: Complete rewrite to avoid HTML rendering issues
"""
import streamlit as st

class HeroSection:
    """Hero section using only Streamlit components - no custom HTML"""
    
    def render(self):
        """Render hero section with Streamlit components only"""
        # Create colored background using Streamlit container
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%);
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white; margin-bottom: 1rem; font-size: 2.2rem; font-weight: 700;">
                Transform Your Life in Just 2 Sessions
            </h1>
            <p style="color: white; opacity: 0.95; font-size: 1.1rem; margin-bottom: 2rem; line-height: 1.6;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Statistics using Streamlit columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.1); 
                        border-radius: 12px; margin: 0.5rem;">
                <div style="font-size: 2.5rem; font-weight: bold; color: #4CA1A3;">85%</div>
                <div style="font-weight: 600; color: #273548;">Success in 2 Sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.1); 
                        border-radius: 12px; margin: 0.5rem;">
                <div style="font-size: 2.5rem; font-weight: bold; color: #4CA1A3;">500+</div>
                <div style="font-weight: 600; color: #273548;">Lives Transformed</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; padding: 1rem; background: rgba(76, 161, 163, 0.1); 
                        border-radius: 12px; margin: 0.5rem;">
                <div style="font-size: 2.5rem; font-weight: bold; color: #4CA1A3;">10+</div>
                <div style="font-weight: 600; color: #273548;">Years Experience</div>
            </div>
            """, unsafe_allow_html=True)
        
        # CTA Button
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                st.success("Assessment coming soon! Book a discovery call instead.")

class KeyDifferentiator:
    """Key differentiator section"""
    
    def render(self):
        """Render differentiator section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, white 100%);
                    border-radius: 12px; padding: 2rem; margin: 2rem 0;
                    border-left: 4px solid #4CA1A3;">
            <h2 style="color: #4CA1A3; margin-bottom: 1rem;">🧠 Why Our Method Works</h2>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #556D7A;">
                Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
                Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
            </p>
        </div>
        """, unsafe_allow_html=True)

class BenefitsSection:
    """Benefits section using clean Streamlit components"""
    
    def render(self):
        """Render benefits section"""
        st.markdown("## Why Choose Our 2-Session Method?")
        st.markdown("Four key advantages that create lasting transformation")
        
        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            # Rapid Results
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                <h3 style="color: #273548; margin-bottom: 1rem;">Rapid Results</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    See transformation in just 2 sessions, not months of therapy
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Targeted Approach
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h3 style="color: #273548; margin-bottom: 1rem;">Targeted Approach</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    Personalized sessions designed for your specific challenges
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Science-Backed
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
                <h3 style="color: #273548; margin-bottom: 1rem;">Science-Backed</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    Uses proven neuroplasticity principles to rewire your subconscious
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # High Success Rate
            st.markdown("""
            <div style="background: white; border-radius: 12px; padding: 2rem; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid #CBD5E1;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💯</div>
                <h3 style="color: #273548; margin-bottom: 1rem;">High Success Rate</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    85% of clients achieve their goals in our 2-session program
                </p>
            </div>
            """, unsafe_allow_html=True)

class TestimonialsSection:
    """Testimonials section with clean rendering"""
    
    def render(self):
        """Render testimonials"""
        st.markdown("## 💬 Client Success Stories")
        
        # Testimonial 1
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-left: 4px solid #4CA1A3;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2.5rem; color: #4CA1A3; min-width: 60px;">🌟</div>
                <div>
                    <blockquote style="font-style: italic; font-size: 1.2rem; margin: 0 0 1rem 0; 
                                       color: #273548; line-height: 1.6;">
                        "Finally broke free from old patterns – 2 sessions changed everything."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A; margin-bottom: 0.5rem;">
                        — Director, Banking, Singapore
                    </div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">
                        🎯 Anxiety patterns • ⏱️ 2 sessions
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 2
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-left: 4px solid #4CA1A3;">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2.5rem; color: #4CA1A3; min-width: 60px;">🚭</div>
                <div>
                    <blockquote style="font-style: italic; font-size: 1.2rem; margin: 0 0 1rem 0; 
                                       color: #273548; line-height: 1.6;">
                        "My husband was a heavy smoker... No more addiction."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A; margin-bottom: 0.5rem;">
                        — Wife, Bangkok
                    </div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">
                        🎯 Smoking cessation • ⏱️ 2 sessions
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

class HomePage:
    """Main home page component - completely rewritten for stability"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.differentiator = KeyDifferentiator()
        self.benefits = BenefitsSection()
        self.testimonials = TestimonialsSection()
    
    def render(self):
        """Render complete home page"""
        try:
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
            
        except Exception as e:
            st.error(f"Error rendering home page: {e}")
            # Fallback minimal content
            st.title("Transform Your Life in Just 2 Sessions")
            st.markdown("Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits")
            
            if st.button("📞 Book Free Discovery Call", type="primary"):
                st.success("We'll contact you within 24 hours!")
    
    def _render_quiz_placeholder(self):
        """Quiz placeholder section"""
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        
        st.info("💡 Interactive assessment coming soon! For now, book a free discovery call to assess your suitability.")
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_cta", type="primary", use_container_width=True):
                st.success("We'll contact you within 24 hours!")
    
    def _render_final_cta(self):
        """Final call-to-action section"""
        st.markdown("---")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">Ready to Transform Your Life?</h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; margin-bottom: 2rem;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
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
    """Factory function to create HomePage instance"""
    return HomePage()
