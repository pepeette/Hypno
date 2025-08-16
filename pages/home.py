"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
USING ONLY STREAMLIT NATIVE COMPONENTS - NO CUSTOM HTML
"""
import streamlit as st

class HeroSection:
    """Hero section component for the home page"""
    
    def __init__(self):
        self.title = "Transform Your Life in Just 2 Sessions"
        self.subtitle = "Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits"
    
    def render(self):
        """Render the hero section using ONLY Streamlit native components"""
        # Create a container for the hero section
        with st.container():
            st.title(self.title)
            st.subheader(self.subtitle)
            
            # Statistics using columns
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Success Rate", value="85%", delta="in 2 sessions")
            
            with col2:
                st.metric(label="Lives Changed", value="500+", delta="since 2014")
            
            with col3:
                st.metric(label="Experience", value="10+", delta="years")
            
            # CTA Button
            st.markdown("")  # Add some space
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🎯 Take the 30-Second Assessment", key="hero_cta", type="primary", use_container_width=True):
                    st.success("Redirecting to assessment...")

class KeyBenefits:
    """Key benefits section component"""
    
    def render(self):
        """Render key benefits using Streamlit components"""
        st.markdown("---")
        st.header("Why Choose Our 2-Session Method?")
        st.write("Traditional therapy focuses on symptoms. We target the root cause in your subconscious mind.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("⚡ Rapid Results")
            st.write("See transformation in just 2 sessions, not months of therapy")
            
            st.subheader("🎯 Targeted Approach")
            st.write("Personalized sessions designed for your specific challenges")
        
        with col2:
            st.subheader("🧠 Science-Backed")
            st.write("Uses proven neuroplasticity principles to rewire your subconscious")
            
            st.subheader("💯 High Success Rate")
            st.write("85% of clients achieve their goals in our 2-session program")

class ProcessPreview:
    """Quick preview of the 2-step process"""
    
    def render(self):
        """Render process preview using Streamlit components"""
        st.markdown("---")
        st.header("How It Works")
        st.write("Our proven 2-step process that creates lasting transformation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("1️⃣ Deep Analysis")
            st.write("**Duration:** 90 minutes")
            st.write("Uncover your unique subconscious patterns")
            st.write("• Map personal behavior patterns")
            st.write("• Identify root causes vs symptoms")
            st.write("• Install initial positive programming")
        
        with col2:
            st.subheader("2️⃣ Transformation")
            st.write("**Duration:** 90 minutes • 3-7 days later")
            st.write("Rewire your mind for lasting change")
            st.write("• Deep hypnotic state for rewiring")
            st.write("• Replace old patterns with new ones")
            st.write("• Lock in your new identity")
        
        st.markdown("")
        st.write("**Ready to start your transformation?**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", key="process_discovery", use_container_width=True):
                st.success("Redirecting to booking...")
        with col2:
            if st.button("🧠 Learn More", key="process_method", use_container_width=True):
                st.success("Redirecting to method page...")

class SocialProof:
    """Social proof section with testimonials"""
    
    def render(self):
        """Render testimonials using Streamlit components"""
        st.markdown("---")
        st.header("Real Transformations from Real People")
        
        # Testimonial 1
        with st.container():
            st.subheader("🌟 Director, Banking, Singapore")
            st.write("*\"Finally broke free from old patterns – 2 sessions changed everything.\"*")
            st.caption("Concern: Anxiety patterns • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 2
        with st.container():
            st.subheader("🎓 Medical Student, Morocco")
            st.write("*\"I was struggling with my studies abroad... now doing my specialization internship.\"*")
            st.caption("Concern: Study anxiety & focus • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 3
        with st.container():
            st.subheader("🚭 Wife, Bangkok")
            st.write("*\"My husband was a heavy smoker... No more addiction.\"*")
            st.caption("Concern: Smoking cessation • Duration: 2 sessions")

class QuizPlaceholder:
    """Quiz placeholder section"""
    
    def render(self):
        """Render simple quiz placeholder"""
        st.markdown("---")
        st.header("30-Second Suitability Assessment")
        
        st.info("📝 Interactive quiz coming soon! For now, book a free discovery call to assess your suitability.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_placeholder", type="primary", use_container_width=True):
                st.success("We'll contact you within 24 hours to schedule your call!")

class FinalCTA:
    """Final call-to-action section"""
    
    def render(self):
        """Render final CTA using Streamlit components"""
        st.markdown("---")
        
        with st.container():
            st.header("Ready to Transform Your Life?")
            st.write("Join hundreds of people who have already transformed their lives with our proven 2-session method.")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True):
                    st.success("Excellent choice! We'll be in touch soon.")
            
            with col2:
                if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                    st.success("Redirecting to method page...")
            
            with col3:
                if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                    st.success("Great! Let's get started.")

class HomePage:
    """Main home page component that orchestrates all sections"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.quiz = QuizPlaceholder()
        self.benefits = KeyBenefits()
        self.process = ProcessPreview()
        self.social_proof = SocialProof()
        self.final_cta = FinalCTA()
    
    def render(self):
        """Render the complete home page using ONLY Streamlit components"""
        try:
            # Hero section
            self.hero.render()
            
            # Quiz placeholder
            self.quiz.render()
            
            # Key benefits
            self.benefits.render()
            
            # Process preview
            self.process.render()
            
            # Social proof
            self.social_proof.render()
            
            # Final call-to-action
            self.final_cta.render()
            
        except Exception as e:
            st.error("Error loading home page content.")
            st.header("Welcome to 2-Step Hypnotherapy")
            st.write("Transform your life with science-backed hypnotherapy in just 2 sessions.")
            if st.button("📞 Contact Us"):
                st.success("Please email: laetitiasheppard@gmail.com")

# Factory function for easy import
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
