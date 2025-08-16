"""
Home page component for the Hypnotherapy website
FIXED: Proper HTML rendering and complete styling
"""
import streamlit as st

class HeroSection:
    """Hero section with proper HTML structure"""
    
    def render(self):
        """Render hero section with complete HTML and CSS"""
        hero_html = """
        <style>
        .hero-container {
            background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%);
            border-radius: 16px;
            padding: 3rem 2rem;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .hero-title {
            color: white;
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            line-height: 1.3;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
            color: white;
            opacity: 0.95;
            max-width: 600px;
            margin: 0 auto 2rem auto;
            line-height: 1.6;
        }
        
        .hero-stats {
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .stat-item {
            text-align: center;
            color: white;
            margin: 1rem;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            font-weight: 600;
            font-size: 1rem;
        }
        
        .hero-cta {
            margin-top: 2rem;
        }
        
        .hero-btn {
            font-size: 1.1rem;
            padding: 1rem 2rem;
            background: white;
            color: #4CA1A3;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            text-decoration: none;
            border-radius: 8px;
            display: inline-block;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
            border: none;
        }
        
        .hero-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        @media (max-width: 768px) {
            .hero-title {
                font-size: 1.8rem;
            }
            .hero-stats {
                gap: 1rem;
            }
            .stat-number {
                font-size: 2rem;
            }
        }
        </style>
        
        <div class="hero-container">
            <h1 class="hero-title">Transform Your Life in Just 2 Sessions</h1>
            <p class="hero-subtitle">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
            
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">85%</div>
                    <div class="stat-label">Success in 2 Sessions</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">500+</div>
                    <div class="stat-label">Lives Transformed</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">10+</div>
                    <div class="stat-label">Years Experience</div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(hero_html, unsafe_allow_html=True)
        
        # CTA Button using Streamlit button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                st.success("Assessment coming soon! Book a discovery call instead.")

class KeyDifferentiator:
    """Key differentiator section"""
    
    def render(self):
        """Render differentiator section"""
        differentiator_html = """
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, #FFFFFF 100%); 
                    border-radius: 12px; padding: 2rem; margin: 2rem 0; 
                    border-left: 4px solid #4CA1A3;">
            <h2 style="color: #4CA1A3; margin-bottom: 1rem; font-size: 1.8rem;">🧠 Why Our Method Works</h2>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #556D7A;">
                Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
                Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
            </p>
        </div>
        """
        st.markdown(differentiator_html, unsafe_allow_html=True)

class BenefitsSection:
    """Benefits section with cards"""
    
    def render(self):
        """Render benefits section"""
        # Header
        st.markdown("""
        <div style="text-align: center; margin: 3rem 0 2rem 0;">
            <h2 style="color: #273548; font-size: 1.8rem;">Why Choose Our 2-Session Method?</h2>
            <p style="color: #556D7A; font-size: 1rem;">Four key advantages that create lasting transformation</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Benefits cards using Streamlit columns
        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            st.markdown("""
            <div style="background: white; border-radius: 12px; 
                        padding: 2rem 1.5rem; text-align: center; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-size: 1.3rem;">Rapid Results</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    See transformation in just 2 sessions, not months of therapy
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: white; border-radius: 12px; 
                        padding: 2rem 1.5rem; text-align: center; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-size: 1.3rem;">Targeted Approach</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    Personalized sessions designed for your specific challenges
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: white; border-radius: 12px; 
                        padding: 2rem 1.5rem; text-align: center; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-size: 1.3rem;">Science-Backed</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    Uses proven neuroplasticity principles to rewire your subconscious
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: white; border-radius: 12px; 
                        padding: 2rem 1.5rem; text-align: center; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💯</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-size: 1.3rem;">High Success Rate</h3>
                <p style="color: #556D7A; line-height: 1.6;">
                    85% of clients achieve their goals in our 2-session program
                </p>
            </div>
            """, unsafe_allow_html=True)

class TestimonialsSection:
    """Testimonials section"""
    
    def render(self):
        """Render testimonials"""
        st.markdown('<h2 style="color: #273548; font-size: 1.8rem; margin: 2rem 0 1rem 0;">💬 Client Success Stories</h2>', 
                   unsafe_allow_html=True)
        
        # Testimonial 1
        st.markdown("""
        <div style="background: white; border-radius: 12px; 
                    padding: 1.5rem; margin: 1rem 0; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; 
                    border-left: 4px solid #4CA1A3;">
            <div style="display: flex; align-items: flex-start; gap: 1rem;">
                <div style="font-size: 2.5rem; color: #4CA1A3; min-width: 60px; text-align: center;">🌟</div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; 
                                       color: #273548; margin: 0 0 1rem 0; line-height: 1.6;">
                        "Finally broke free from old patterns – 2 sessions changed everything."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A;">— Director, Banking, Singapore</div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">🎯 Anxiety patterns • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 2
        st.markdown("""
        <div style="background: white; border-radius: 12px; 
                    padding: 1.5rem; margin: 1rem 0; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; 
                    border-left: 4px solid #4CA1A3;">
            <div style="display: flex; align-items: flex-start; gap: 1rem;">
                <div style="font-size: 2.5rem; color: #4CA1A3; min-width: 60px; text-align: center;">🚭</div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; 
                                       color: #273548; margin: 0 0 1rem 0; line-height: 1.6;">
                        "My husband was a heavy smoker... No more addiction."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A;">— Wife, Bangkok</div>
                    <div style="color: #4CA1A3; font-size: 0.9rem;">🎯 Smoking cessation • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

class HomePage:
    """Main home page component"""
    
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
        """Quiz placeholder section"""
        st.markdown("---")
        st.markdown('<h2 style="color: #273548; font-size: 1.8rem;">30-Second Suitability Assessment</h2>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: white; border-radius: 12px; 
                    padding: 2rem; margin: 2rem 0; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; text-align: center;">
            <h3 style="color: #273548; margin-bottom: 1rem;">Interactive Assessment Coming Soon!</h3>
            <p style="color: #556D7A;">For now, book a free discovery call to assess your suitability</p>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_cta", type="primary", use_container_width=True):
                st.success("We'll contact you within 24 hours!")
    
    def _render_final_cta(self):
        """Final call-to-action section"""
        st.markdown("---")
        
        final_cta_html = """
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    border-radius: 16px; padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem; font-size: 1.8rem;">Ready to Transform Your Life?</h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; margin-bottom: 2rem;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """
        
        st.markdown(final_cta_html, unsafe_allow_html=True)
        
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

# Also export the individual components for flexibility
__all__ = ['HomePage', 'HeroSection', 'KeyDifferentiator', 'BenefitsSection', 'TestimonialsSection', 'create_home_page']
