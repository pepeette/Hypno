"""
Method Page
Detailed explanation of the 2-session method using Streamlit components
"""
import streamlit as st
from utils.styling import render_section_divider
from utils.config import AppConfig, ContentConfig, get_years_of_experience
from utils.session_state import track_page_view

class MethodPage:
    """Method page using native Streamlit components"""
    
    def __init__(self):
        self.config = AppConfig()
        self.content = ContentConfig()
    
    def render(self):
        """Render the complete method page"""
        track_page_view("Method")
        
        self._render_header()
        self._render_key_differentiator()
        self._render_session_breakdown()
        self._render_success_statistics()
        self._render_pricing_section()
        self._render_guarantee()
    
    def _render_header(self):
        """Render page header using Streamlit components"""
        st.title("Our Proven 2-Session Method")
        st.write("Why 2 sessions work when years of trying haven't")
        
        # Key insight
        st.info("""
        🧠 **The Science**: Traditional methods work with your conscious mind (5% of decisions). 
        Our method rewires your subconscious programming (95% of decisions) for lasting change.
        """)
    
    def _render_key_differentiator(self):
        """Render the key differentiator using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 🔬 The Breakthrough Difference")
        
        # Comparison using columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ❌ Traditional Approaches")
            st.error("**Fight Against Your Programming**")
            st.write("• Rely on conscious willpower")
            st.write("• Require constant effort")
            st.write("• High relapse rates")
            st.write("• Take months or years")
            st.write("• Often ineffective long-term")
        
        with col2:
            st.markdown("### ✅ Our Hypnotherapy Method")
            st.success("**Work With Your Programming**")
            st.write("• Rewires subconscious patterns")
            st.write("• Natural, effortless change")
            st.write("• Long-term success")
            st.write("• Results in just 2 sessions")
            st.write("• Permanent transformation")
    
    def _render_session_breakdown(self):
        """Render detailed session breakdown using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 🎯 The 2-Session Process")
        st.write("Each session builds strategically for maximum transformation impact")
        
        # Session 1
        self._render_session_detail(1, ContentConfig.SESSION_1)
        
        # Session 2  
        self._render_session_detail(2, ContentConfig.SESSION_2)
        
        # Optional Session 3
        self._render_optional_session()
    
    def _render_session_detail(self, session_num, session_data):
        """Render individual session details using Streamlit components"""
        st.markdown(f"### {session_num}️⃣ Session {session_num}: {session_data['name']}")
        
        # Session overview
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Duration:** {session_data['duration']}")
            st.write(f"**Focus:** {session_data['description']}")
            
            st.markdown("**What happens:**")
            for feature in session_data['features']:
                st.write(f"• {feature}")
        
        with col2:
            # Visual indicator using metric
            st.metric(
                f"Session {session_num}",
                session_data['name'],
                session_data['duration']
            )
    
    def _render_optional_session(self):
        """Render optional 3rd session using Streamlit components"""
        st.markdown("### 3️⃣ Session 3: Reinforcement (Optional)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Duration:** {ContentConfig.SESSION_3['duration']}")
            st.write(f"**Needed by:** Only {AppConfig.NEED_3RD_SESSION_RATE}% of clients")
            
            st.markdown("**When beneficial:**")
            for feature in ContentConfig.SESSION_3['features']:
                st.write(f"• {feature}")
        
        with col2:
            st.success("""
            **Our Guarantee**
            
            Not satisfied after 2 sessions? 
            Your 3rd session is complimentary.
            """)
    
    def _render_success_statistics(self):
        """Render success statistics using Streamlit metrics"""
        render_section_divider()
        
        st.markdown("## 📊 Proven Results")
        st.write("Our method delivers consistent, measurable outcomes:")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Complete Success",
                f"{AppConfig.SUCCESS_RATE_2_SESSIONS}%",
                "in 2 sessions",
                help="85% of clients achieve their complete goals in just 2 sessions"
            )
        
        with col2:
            st.metric(
                "Need Reinforcement",
                f"{AppConfig.NEED_3RD_SESSION_RATE}%",
                "3rd session",
                help="15% of clients benefit from an optional 3rd reinforcement session"
            )
        
        with col3:
            st.metric(
                "Practice Since",
                str(AppConfig.PRACTICE_ESTABLISHED),
                f"{get_years_of_experience()} years",
                help=f"Professional practice established in {AppConfig.PRACTICE_ESTABLISHED}"
            )
        
        with col4:
            st.metric(
                "Certifications",
                "LCCH & DBT",
                f"{AppConfig.LCCH_CERTIFICATION} & {AppConfig.DBT_CERTIFICATION}",
                help="London College of Clinical Hypnotherapy & Dialectical Behavioral Therapy"
            )
    
    def _render_pricing_section(self):
        """Render pricing using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 💰 Investment in Your Transformation")
        st.write("One-time investment compared to years of traditional therapy:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Complete Package")
            st.metric(
                "Price",
                f"{AppConfig.COMPLETE_PACKAGE_PRICE:,} {AppConfig.CURRENCY}",
                "Sessions 1 & 2"
            )
            
            st.markdown("**Includes:**")
            st.write("✓ Analysis Session (90 min)")
            st.write("✓ Hypnosis Session (90 min)")
            st.write("✓ Email support between sessions")
            st.write(f"✓ {AppConfig.SUCCESS_RATE_2_SESSIONS}% success rate")
            
            if st.button("📞 Book Complete Package", type="primary", use_container_width=True):
                st.success("Great choice! Scroll down to book.")
        
        with col2:
            st.markdown("### Premium Package")
            st.metric(
                "Price", 
                f"{AppConfig.PREMIUM_PACKAGE_PRICE:,} {AppConfig.CURRENCY}",
                "All 3 sessions"
            )
            
            st.markdown("**Includes:**")
            st.write("✓ Everything in Complete Package")
            st.write("✓ Plus: 3rd reinforcement session")
            st.write("✓ Satisfaction guarantee")
            st.write("✓ Maximum peace of mind")
            
            if st.button("⭐ Book Premium Package", use_container_width=True):
                st.success("Excellent choice! Scroll down to book.")
        
        # Value comparison
        st.info(f"""
        💡 **Value Comparison**: Traditional therapy often costs 60,000+ {AppConfig.CURRENCY} 
        over months or years, with uncertain results. Our method delivers transformation 
        in 2 sessions for a fraction of the cost.
        """)
    
    def _render_guarantee(self):
        """Render satisfaction guarantee using Streamlit components"""
        render_section_divider()
        
        st.markdown("## 💯 Our Satisfaction Guarantee")
        
        st.success("""
        **We're confident in our method, but we understand every situation is unique.**
        
        If you're not completely satisfied after your 2 sessions, 
        we'll provide a complimentary 3rd reinforcement session at no additional cost.
        
        Your transformation is our commitment to you.
        """)
        
        # Final CTA
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                "🚀 Start Your Transformation Today",
                type="primary",
                use_container_width=True
            ):
                st.success("Perfect! Scroll down to book your discovery call.")

# Factory function for easy import
def create_method_page():
    """Create MethodPage instance"""
    return MethodPage()
