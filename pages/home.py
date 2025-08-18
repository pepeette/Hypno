"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
Complete Home page component - Streamlit-native, no complex divs
Uses Streamlit components properly for better compatibility
"""

import streamlit as st

class HomePage:
    """Simple, reliable home page"""
    
    def render(self):
        """Render home page with Streamlit native components"""
        # Hero section
        st.markdown("# Transform Your Life in Just 2 Sessions")
        st.write("Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits")
        
        # Stats
        st.markdown("### Our Track Record")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        
        with col2:
            st.metric("Lives Changed", "500+", "transformations")
        
        with col3:
            st.metric("Experience", "10+", "years")
        
        # Key message
        st.markdown("---")
        st.markdown("## Why Our Method Works When Others Don't")
        
        st.info("""
        **Traditional therapy** targets symptoms using willpower (5% success rate).  
        **Our method** rewires the subconscious patterns that create the behavior (85% success rate).
        """)
        
        # Quiz placeholder
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        st.info("Interactive assessment coming soon! For now, book a free discovery call to assess your suitability.")
        
        if st.button("📞 Book Free Discovery Call", type="primary", use_container_width=True):
            st.success("Excellent choice! Contact us at: laetitiasheppard@gmail.com")
        
        # Value proposition
        st.markdown("---")
        st.markdown("## Why Choose Our 2-Session Method?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⚡ Rapid Results")
            st.write("See transformation in just 2 sessions, not months of therapy")
            
            st.markdown("### 🧠 Science-Backed")
            st.write("Uses proven neuroplasticity principles to rewire your subconscious")
        
        with col2:
            st.markdown("### 🎯 Personalized")
            st.write("Customized sessions designed for your specific challenges")
            
            st.markdown("### 💯 High Success")
            st.write("85% of clients achieve their goals in our 2-session program")
        
        # Testimonials
        st.markdown("---")
        st.markdown("## What Our Clients Say")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🌟 Banking Director, Singapore")
            st.write("""
            *"Finally broke free from anxiety patterns that controlled my life for years. 
            2 sessions changed everything."*
            """)
            st.caption("🎯 Anxiety • ⏱️ 2 sessions")
        
        with col2:
            st.markdown("### 🚭 Wife, Bangkok")
            st.write("""
            *"My husband smoked 2 packs daily for 20 years. After 2 sessions, 
            he doesn't even think about cigarettes."*
            """)
            st.caption("🚭 Smoking • ⏱️ 2 sessions")
        
        # Final CTA
        st.markdown("---")
        st.markdown("## Ready to Transform Your Life?")
        st.write("Join hundreds who have transformed their lives with our proven method.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True):
                st.success("Perfect! Email: laetitiasheppard@gmail.com")
        
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                st.success("See our Method page for details!")
        
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                st.success("Great! Contact us to get started.")

def create_home_page():
    """Factory function"""
    return HomePage()
