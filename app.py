"""
Streamlit-optimized Home page component
Uses native Streamlit components instead of complex HTML
"""
import streamlit as st

class StreamlitOptimizedHero:
    """Hero section using Streamlit native components"""
    
    def render(self):
        """Render hero with Streamlit components"""
        # Hero background using Streamlit container
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 3rem 2rem; text-align: center; 
                    margin: 2rem 0;">
        """, unsafe_allow_html=True)
        
        st.markdown("# Transform Your Life in Just 2 Sessions", unsafe_allow_html=True)
        st.markdown("""
        <p style="color: white; opacity: 0.95; max-width: 600px; 
                  margin: 0 auto 2rem auto; text-align: center;">
            Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Stats using Streamlit metrics
        st.markdown("### Our Track Record")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        
        with col2:
            st.metric("Lives Changed", "500+", "transformations")
        
        with col3:
            st.metric("Experience", "10+", "years")
        
        # CTA Button
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", 
                        key="hero_cta", type="primary", use_container_width=True):
                st.success("Great! Scroll down to take the assessment.")

class StreamlitKeyMessage:
    """Key message using simple HTML"""
    
    def render(self):
        """Render key differentiator"""
        st.markdown("## Why Our Method Works When Others Don't")
        
        st.info("""
        **Traditional therapy** targets symptoms using willpower (5% success rate).  
        **Our method** rewires the subconscious patterns that create the behavior (85% success rate).
        """)

class StreamlitTestimonials:
    """Testimonials using Streamlit components"""
    
    def render(self):
        """Render testimonials with Streamlit"""
        st.markdown("## What Our Clients Say")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown("### 🌟 Banking Director, Singapore")
                st.write("""
                *"Finally broke free from anxiety patterns that controlled my life for years. 
                2 sessions changed everything."*
                """)
                st.caption("🎯 Anxiety • ⏱️ 2 sessions")
        
        with col2:
            with st.container():
                st.markdown("### 🚭 Wife, Bangkok")
                st.write("""
                *"My husband smoked 2 packs daily for 20 years. After 2 sessions, 
                he doesn't even think about cigarettes."*
                """)
                st.caption("🚭 Smoking • ⏱️ 2 sessions")

class StreamlitValueProp:
    """Value proposition using Streamlit layout"""
    
    def render(self):
        """Render value proposition"""
        st.markdown("## Why Choose Our 2-Session Method?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown("### ⚡ Rapid Results")
                st.write("See transformation in just 2 sessions, not months of therapy")
                
            with st.container():
                st.markdown("### 🧠 Science-Backed")
                st.write("Uses proven neuroplasticity principles to rewire your subconscious")
        
        with col2:
            with st.container():
                st.markdown("### 🎯 Personalized")
                st.write("Customized sessions designed for your specific challenges")
                
            with st.container():
                st.markdown("### 💯 High Success")
                st.write("85% of clients achieve their goals in our 2-session program")

class StreamlitOptimizedHomePage:
    """Main home page using Streamlit components"""
    
    def __init__(self):
        self.hero = StreamlitOptimizedHero()
        self.key_message = StreamlitKeyMessage()
        self.testimonials = StreamlitTestimonials()
        self.value_prop = StreamlitValueProp()
    
    def render(self):
        """Render complete home page"""
        # Hero section
        self.hero.render()
        
        # Key message
        self.key_message.render()
        
        # Quiz section placeholder
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        st.info("Interactive assessment coming soon! For now, book a free discovery call.")
        
        # Value proposition
        self.value_prop.render()
        
        # Testimonials
        self.testimonials.render()
        
        # Final CTA
        self._render_final_cta()
    
    def _render_final_cta(self):
        """Render final CTA using Streamlit"""
        st.markdown("---")
        st.markdown("## Ready to Transform Your Life?")
        st.write("Join hundreds who have transformed their lives with our proven method.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True):
                st.success("Excellent choice! Scroll down to book.")
        
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                st.success("Redirecting to Method page...")
        
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                st.success("Great! Let's get started.")

def create_streamlit_home_page():
    return StreamlitOptimizedHomePage()
