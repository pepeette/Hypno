"""
Home page using the proper styling system
Follows the modular architecture with CSS variables
"""
import streamlit as st

class HeroSection:
    """Hero section that uses CSS variables from styling.py"""
    
    def render(self):
        """Render hero section with proper CSS"""
        st.markdown("""
        <div class="hero">
            <h1 style="color: white;">Transform Your Life in Just 2 Sessions</h1>
            <p style="font-size: 1.2rem; color: white; opacity: 0.95; margin-bottom: 2rem;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
            
            <div style="display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap;">
                <div style="text-align: center; color: white; margin: 1rem;">
                    <div style="font-size: 3rem; font-weight: bold;">85%</div>
                    <div>Success in 2 Sessions</div>
                </div>
                <div style="text-align: center; color: white; margin: 1rem;">
                    <div style="font-size: 3rem; font-weight: bold;">500+</div>
                    <div>Lives Transformed</div>
                </div>
                <div style="text-align: center; color: white; margin: 1rem;">
                    <div style="font-size: 3rem; font-weight: bold;">10+</div>
                    <div>Years Experience</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Button using Streamlit
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                st.success("Redirecting to assessment...")

class KeyBenefits:
    """Benefits section using styling system"""
    
    def render(self):
        """Render benefits with proper styling"""
        st.markdown("---")
        st.markdown("## Why Choose Our 2-Session Method?")
        st.markdown("Traditional therapy focuses on symptoms. We target the root cause in your subconscious mind.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
                <h3>⚡ Rapid Results</h3>
                <p>See transformation in just 2 sessions, not months of therapy</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <h3>🎯 Targeted Approach</h3>
                <p>Personalized sessions designed for your specific challenges</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
                <h3>🧠 Science-Backed</h3>
                <p>Uses proven neuroplasticity principles to rewire your subconscious</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <h3>💯 High Success Rate</h3>
                <p>85% of clients achieve their goals in our 2-session program</p>
            </div>
            """, unsafe_allow_html=True)

class SocialProof:
    """Testimonials using styling system"""
    
    def render(self):
        """Render testimonials with CSS classes"""
        st.markdown("---")
        st.markdown("## Real Transformations from Real People")
        
        # Testimonial 1
        st.markdown("""
        <div class="testimonial-card">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2rem; color: var(--accent);">🌟</div>
                <div>
                    <blockquote style="font-style: italic; margin: 0 0 1rem 0;">
                        "Finally broke free from old patterns – 2 sessions changed everything."
                    </blockquote>
                    <div style="font-weight: 600;">— Director, Banking, Singapore</div>
                    <div style="color: var(--accent); font-size: 0.9rem;">🎯 Anxiety patterns • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 2  
        st.markdown("""
        <div class="testimonial-card">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2rem; color: var(--accent);">🎓</div>
                <div>
                    <blockquote style="font-style: italic; margin: 0 0 1rem 0;">
                        "I was struggling with my studies abroad... now doing my specialization internship."
                    </blockquote>
                    <div style="font-weight: 600;">— Medical Student, Morocco</div>
                    <div style="color: var(--accent); font-size: 0.9rem;">🎯 Study anxiety • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 3
        st.markdown("""
        <div class="testimonial-card">
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <div style="font-size: 2rem; color: var(--accent);">🚭</div>
                <div>
                    <blockquote style="font-style: italic; margin: 0 0 1rem 0;">
                        "My husband was a heavy smoker... No more addiction."
                    </blockquote>
                    <div style="font-weight: 600;">— Wife, Bangkok</div>
                    <div style="color: var(--accent); font-size: 0.9rem;">🎯 Smoking cessation • ⏱️ 2 sessions</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

class ProcessPreview:
    """Process section using styling system"""
    
    def render(self):
        """Render process with cards"""
        st.markdown("---")
        st.markdown("## How It Works")
        st.markdown("Our proven 2-step process that creates lasting transformation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <div style="width: 60px; height: 60px; background: var(--accent); color: white; 
                           border-radius: 50%; display: flex; align-items: center; 
                           justify-content: center; font-size: 1.8rem; font-weight: bold; 
                           margin: 0 auto 1.5rem auto;">1</div>
                <h3>Deep Analysis</h3>
                <p style="font-weight: 600; color: var(--accent);">90 minutes</p>
                <p>Uncover your unique subconscious patterns</p>
                <ul style="text-align: left;">
                    <li>Map personal behavior patterns</li>
                    <li>Identify root causes vs symptoms</li>
                    <li>Install initial positive programming</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <div style="width: 60px; height: 60px; background: var(--accent); color: white; 
                           border-radius: 50%; display: flex; align-items: center; 
                           justify-content: center; font-size: 1.8rem; font-weight: bold; 
                           margin: 0 auto 1.5rem auto;">2</div>
                <h3>Transformation</h3>
                <p style="font-weight: 600; color: var(--accent);">90 minutes • 3-7 days later</p>
                <p>Rewire your mind for lasting change</p>
                <ul style="text-align: left;">
                    <li>Deep hypnotic state for rewiring</li>
                    <li>Replace old patterns with new ones</li>
                    <li>Lock in your new identity</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Call to action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", key="process_discovery", use_container_width=True):
                st.success("Redirecting to booking...")
        with col2:
            if st.button("🧠 Learn More", key="process_method", use_container_width=True):
                st.success("Redirecting to method page...")

class HomePage:
    """Main home page using modular architecture"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.benefits = KeyBenefits()
        self.social_proof = SocialProof()
        self.process = ProcessPreview()
    
    def render(self):
        """Render complete home page"""
        try:
            # Hero section
            self.hero.render()
            
            # Quiz placeholder
            self._render_quiz_placeholder()
            
            # Benefits
            self.benefits.render()
            
            # Process
            self.process.render()
            
            # Social proof
            self.social_proof.render()
            
            # Final CTA
            self._render_final_cta()
            
        except Exception as e:
            st.error(f"Error loading page: {str(e)}")
            st.markdown("## Welcome to 2-Step Hypnotherapy")
            st.write("Transform your life with science-backed hypnotherapy.")
    
    def _render_quiz_placeholder(self):
        """Quiz placeholder"""
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h3>Interactive Assessment Coming Soon!</h3>
            <p>For now, book a free discovery call to assess your suitability.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_placeholder", type="primary", use_container_width=True):
                st.success("We'll contact you within 24 hours!")
    
    def _render_final_cta(self):
        """Final call to action"""
        st.markdown("---")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    padding: 3rem 2rem; border-radius: var(--radius-lg); 
                    text-align: center; margin: 2rem 0;">
            <h2 style="color: white;">Ready to Transform Your Life?</h2>
            <p style="color: white; opacity: 0.9; margin-bottom: 2rem;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True):
                st.success("Excellent choice!")
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                st.success("Redirecting...")
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                st.success("Great!")

def create_home_page():
    return HomePage()
