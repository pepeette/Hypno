"""
FIXED Home page - Simplified using Streamlit native components
No complex HTML, consistent styling, mobile-friendly
"""
import streamlit as st

class HomePage:
    """Simplified home page using Streamlit components"""
    
    def render(self):
        """Render complete home page using Streamlit native components"""
        self._render_hero()
        self._render_key_differentiator()
        self._render_quiz_section()
        self._render_benefits()
        self._render_testimonials()
        self._render_final_cta()
    
    def _render_hero(self):
        """Hero section using Streamlit components"""
        # Hero container with gradient background
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    padding: 4rem 2rem; border-radius: 16px; text-align: center; margin-bottom: 3rem;">
            <h1 style="color: white; margin-bottom: 1rem;">Transform Your Life in Just 2 Sessions</h1>
            <p style="color: white; font-size: 1.1rem; opacity: 0.95; margin-bottom: 2rem;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats using Streamlit metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        with col2:
            st.metric("Lives Transformed", "500+", "since 2017")
        with col3:
            st.metric("Experience", "10+ Years", "certified professional")
    
    def _render_key_differentiator(self):
        """Key differentiator section"""
        st.markdown("---")
        st.markdown("## 🧠 Why Our Method Works")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ❌ Traditional Methods")
            st.write("• Fight against your programming")
            st.write("• Require constant willpower")
            st.write("• 95% relapse rate")
            st.write("• Take months or years")
            st.write("• Focus on symptoms only")
        
        with col2:
            st.markdown("### ✅ Our Hypnotherapy")
            st.write("• Rewires your programming")
            st.write("• Works with natural patterns")
            st.write("• 85% long-term success")
            st.write("• Results in just 2 sessions")
            st.write("• Targets root causes")
        
        st.info("🎯 **The Key:** We work with your subconscious mind (95% of decisions) instead of conscious willpower (5% of decisions)")
    
    def _render_quiz_section(self):
        """Quiz section placeholder"""
        st.markdown("---")
        st.markdown("## 🎯 Free 30-Second Assessment")
        st.write("Discover your potential for rapid transformation")
        
        # Quiz component will be rendered here by main app
        # This is just a placeholder that shows the quiz anchor
        st.markdown('<div id="quiz"></div>', unsafe_allow_html=True)
        
        # Placeholder for quiz - will be replaced by actual quiz component
        if not st.session_state.get('quiz_completed', False):
            st.info("📋 **Quick Assessment:** Take our 3-question quiz to discover your suitability for hypnotherapy")
            if st.button("🎯 Start Assessment", type="primary", use_container_width=True):
                st.success("Quiz will load here - component integration in progress!")
        else:
            st.success("✅ Assessment completed! Scroll down to book your discovery call.")
    
    def _render_benefits(self):
        """Benefits section using Streamlit components"""
        st.markdown("---")
        st.markdown("## ⚡ Why Choose Our 2-Session Method?")
        st.write("Four key advantages that create lasting transformation")
        
        # Benefits grid using columns
        col1, col2 = st.columns(2)
        
        with col1:
            # Benefit 1
            st.markdown("### ⚡ Rapid Results")
            st.write("See transformation in just 2 sessions, not months of therapy")
            st.write("")
            
            # Benefit 3
            st.markdown("### 🧠 Science-Backed")
            st.write("Uses proven neuroplasticity principles to rewire your subconscious")
        
        with col2:
            # Benefit 2
            st.markdown("### 🎯 Targeted Approach")
            st.write("Personalized sessions designed for your specific challenges")
            st.write("")
            
            # Benefit 4
            st.markdown("### 💯 High Success Rate")
            st.write("85% of clients achieve their goals in our 2-session program")
    
    def _render_testimonials(self):
        """Testimonials section using Streamlit components"""
        st.markdown("---")
        st.markdown("## 💬 Client Success Stories")
        
        # Testimonial 1
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                st.markdown("### 🌟")
            with col2:
                st.markdown("#### Banking Director, Singapore")
                st.write("*'Finally broke free from old patterns – 2 sessions changed everything.'*")
                st.write("**Challenge:** Anxiety patterns • **Result:** 2 sessions")
        
        st.write("")
        
        # Testimonial 2
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                st.markdown("### 🚭")
            with col2:
                st.markdown("#### Wife, Bangkok")
                st.write("*'My husband was a heavy smoker... No more addiction.'*")
                st.write("**Challenge:** Smoking cessation • **Result:** 2 sessions")
        
        st.write("")
        
        # Testimonial 3
        with st.container():
            col1, col2 = st.columns([1, 5])
            with col1:
                st.markdown("### 🎓")
            with col2:
                st.markdown("#### Medical Student, Morocco")
                st.write("*'I was struggling with my studies abroad... now doing my specialization internship.'*")
                st.write("**Challenge:** Study anxiety • **Result:** 2 sessions")
    
    def _render_final_cta(self):
        """Final call-to-action"""
        st.markdown("---")
        
        # CTA section with gradient background
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    padding: 3rem 2rem; border-radius: 16px; text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">Ready to Transform Your Life?</h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; margin-bottom: 2rem;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA buttons using Streamlit
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📞 Free Discovery Call", use_container_width=True, type="primary"):
                # Scroll to booking section
                st.success("📞 Excellent choice! Scroll down to book your call.")
        
        with col2:
            if st.button("🧠 Learn Our Method", use_container_width=True):
                st.success("🧠 Navigate to Method page to learn more!")
        
        with col3:
            if st.button("⚡ Book Sessions Now", use_container_width=True):
                st.success("⚡ Great! Scroll down to start booking.")

def create_home_page():
    """Factory function"""
    return HomePage()
