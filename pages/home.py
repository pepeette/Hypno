"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
"""
import streamlit as st

class HeroSection:
    """Hero section component for the home page"""
    
    def __init__(self):
        self.title = "Transform Your Life in Just 2 Sessions"
        self.subtitle = "Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits"
        self.cta_text = "Take the 30-Second Assessment"
    
    def render(self):
        """Render the hero section using Streamlit native components"""
        # Apply basic styling
        st.markdown("""
        <style>
        .hero-container {
            background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%);
            padding: 3rem 2rem;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 2rem;
        }
        .hero-title {
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .hero-subtitle {
            color: white;
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        .stat-item {
            text-align: center;
            color: white;
            margin: 1rem;
        }
        .stat-number {
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .stat-label {
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Hero container
        st.markdown('<div class="hero-container">', unsafe_allow_html=True)
        
        # Title and subtitle using Streamlit
        st.markdown(f'<h1 class="hero-title">{self.title}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle">{self.subtitle}</p>', unsafe_allow_html=True)
        
        # Statistics using columns
        st.markdown('<div class="stats-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">85%</div>
                <div class="stat-label">Success in 2 Sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Lives Transformed</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">10+</div>
                <div class="stat-label">Years Experience</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # CTA Button
        st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
        if st.button("🎯 " + self.cta_text, key="hero_cta", type="primary"):
            st.success("Redirecting to assessment...")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Close hero container
        st.markdown('</div>', unsafe_allow_html=True)

class KeyBenefits:
    """Key benefits section component"""
    
    def render(self):
        """Render key benefits using Streamlit components"""
        st.markdown("---")
        st.markdown("## Why Choose Our 2-Session Method?")
        st.markdown("Traditional therapy focuses on symptoms. We target the root cause in your subconscious mind.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⚡ Rapid Results")
            st.write("See transformation in just 2 sessions, not months of therapy")
            
            st.markdown("### 🎯 Targeted Approach")
            st.write("Personalized sessions designed for your specific challenges")
        
        with col2:
            st.markdown("### 🧠 Science-Backed")
            st.write("Uses proven neuroplasticity principles to rewire your subconscious")
            
            st.markdown("### 💯 High Success Rate")
            st.write("85% of clients achieve their goals in our 2-session program")

class SocialProof:
    """Social proof section with testimonials"""
    
    def render(self):
        """Render testimonials using Streamlit components"""
        st.markdown("---")
        st.markdown("## Real Transformations from Real People")
        
        # Testimonial 1
        with st.container():
            st.markdown("### 🌟 Director, Banking, Singapore")
            st.markdown("*\"Finally broke free from old patterns – 2 sessions changed everything.\"*")
            st.caption("Concern: Anxiety patterns • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 2
        with st.container():
            st.markdown("### 🎓 Medical Student, Morocco")
            st.markdown("*\"I was struggling with my studies abroad... now doing my specialization internship.\"*")
            st.caption("Concern: Study anxiety & focus • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 3
        with st.container():
            st.markdown("### 🚭 Wife, Bangkok")
            st.markdown("*\"My husband was a heavy smoker... No more addiction.\"*")
            st.caption("Concern: Smoking cessation • Duration: 2 sessions")

class ProcessPreview:
    """Quick preview of the 2-step process"""
    
    def render(self):
        """Render process preview using Streamlit components"""
        st.markdown("---")
        st.markdown("## How It Works")
        st.markdown("Our proven 2-step process that creates lasting transformation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 1️⃣ Deep Analysis")
            st.markdown("**90 minutes**")
            st.write("Uncover your unique subconscious patterns")
            st.write("• Map personal behavior patterns")
            st.write("• Identify root causes vs symptoms")
            st.write("• Install initial positive programming")
        
        with col2:
            st.markdown("### 2️⃣ Transformation")
            st.markdown("**90 minutes • 3-7 days later**")
            st.write("Rewire your mind for lasting change")
            st.write("• Deep hypnotic state for rewiring")
            st.write("• Replace old patterns with new ones")
            st.write("• Lock in your new identity")
        
        st.markdown("")
        st.markdown("**Ready to start your transformation?**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", key="process_discovery"):
                st.success("Redirecting to booking...")
        with col2:
            if st.button("🧠 Learn More", key="process_method"):
                st.success("Redirecting to method page...")

class HomePage:
    """Main home page component that orchestrates all sections"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.benefits = KeyBenefits()
        self.social_proof = SocialProof()
        self.process = ProcessPreview()
    
    def render(self):
        """Render the complete home page"""
        try:
            # Hero section
            self.hero.render()
            
            # Quiz section placeholder
            self._render_quiz_placeholder()
            
            # Key benefits
            self.benefits.render()
            
            # Process preview
            self.process.render()
            
            # Social proof
            self.social_proof.render()
            
            # Final call-to-action
            self._render_final_cta()
            
        except Exception as e:
            st.error("Error loading home page content.")
            st.markdown("## Welcome to 2-Step Hypnotherapy")
            st.markdown("Transform your life with science-backed hypnotherapy in just 2 sessions.")
            if st.button("📞 Contact Us"):
                st.success("Please email: laetitiasheppard@gmail.com")
    
    def _render_quiz_placeholder(self):
        """Render simple quiz placeholder"""
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        
        st.info("📝 Interactive quiz coming soon! For now, book a free discovery call to assess your suitability.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_placeholder", type="primary"):
                st.success("We'll contact you within 24 hours to schedule your call!")
    
    def _render_final_cta(self):
        """Render final call-to-action section"""
        st.markdown("---")
        
        # Create a colored container using Streamlit
        st.markdown("""
        <style>
        .cta-container {
            background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
            padding: 3rem 2rem;
            border-radius: 16px;
            text-align: center;
            margin: 2rem 0;
        }
        .cta-title {
            color: white;
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .cta-text {
            color: white;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="cta-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="cta-title">Ready to Transform Your Life?</h2>', unsafe_allow_html=True)
        st.markdown('<p class="cta-text">Join hundreds of people who have already transformed their lives with our proven 2-session method.</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery"):
                st.success("Excellent choice! We'll be in touch soon.")
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method"):
                st.success("Redirecting to method page...")
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book"):
                st.success("Great! Let's get started.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Factory function for easy import
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
