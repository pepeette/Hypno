"""
Footer Component
Professional footer with founder info, contact details, and credentials
Using Streamlit components instead of complex HTML
"""
import streamlit as st
import datetime
from utils.config import AppConfig, get_years_of_experience

class Footer:
    """Professional footer component using Streamlit elements"""
    
    def __init__(self):
        self.config = AppConfig()
    
    def render(self):
        """Render the complete footer using Streamlit components"""
        st.markdown("---")
        
        # Main footer content
        self._render_main_footer()
        
        # Trust indicators
        self._render_trust_indicators()
        
        # Copyright
        self._render_copyright()
    
    def _render_main_footer(self):
        """Render main footer content using Streamlit columns"""
        col1, col2 = st.columns([2, 1], gap="large")
        
        with col1:
            self._render_founder_section()
        
        with col2:
            self._render_contact_section()
    
    def _render_founder_section(self):
        """Render founder information using Streamlit components"""
        # Founder image and info
        col_img, col_text = st.columns([1, 3])
        
        with col_img:
            st.image(
                AppConfig.FOUNDER_IMAGE,
                width=100,
                caption="Laetitia Sheppard"
            )
        
        with col_text:
            st.markdown("### Laetitia Sheppard")
            st.write("Certified Clinical Hypnotherapist")
            st.write(f"Practice established {AppConfig.PRACTICE_ESTABLISHED}")
            
            # Credentials
            st.markdown("**Certifications:**")
            st.write(f"• London College of Clinical Hypnotherapy Certified {AppConfig.LCCH_CERTIFICATION}")
            st.write(f"• Dialectical Behavioral Therapy Certified {AppConfig.DBT_CERTIFICATION}")
            st.write(f"• {get_years_of_experience()}+ years experience")
    
    def _render_contact_section(self):
        """Render contact information using Streamlit components"""
        st.markdown("### Contact Information")
        
        # Clinic details
        st.write(f"**{AppConfig.PRACTICE_NAME}**")
        st.write(AppConfig.CLINIC_ADDRESS)
        st.write(AppConfig.CLINIC_CITY)
        
        # Session options
        st.markdown("**Session Options:**")
        st.write("• In-person (Bangkok clinic)")
        st.write("• Online (worldwide via Zoom)")
        st.write("• Home visits (Bangkok area)")
        
        # Action buttons using Streamlit
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📍 Get Directions", use_container_width=True):
                st.success("Opening maps...")
                # In production: st.link_button or redirect
        
        with col2:
            if st.button("📅 Book Now", use_container_width=True, type="primary"):
                st.success("Scroll up to book!")
    
    def _render_trust_indicators(self):
        """Render trust badges using Streamlit metrics"""
        st.markdown("### 🏆 Professional Standards")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Certified",
                "LCCH",
                f"Since {AppConfig.LCCH_CERTIFICATION}",
                help="London College of Clinical Hypnotherapy"
            )
        
        with col2:
            st.metric(
                "Licensed",
                "Insured",
                "Professional",
                help="Professional indemnity insurance"
            )
        
        with col3:
            st.metric(
                "Experience",
                f"{get_years_of_experience()}+ years",
                "Established practice",
                help=f"Practice established {AppConfig.PRACTICE_ESTABLISHED}"
            )
        
        with col4:
            st.metric(
                "Success Rate",
                "85%",
                "2 sessions",
                help="85% of clients achieve goals in 2 sessions"
            )
        
        # Guarantee
        st.success("💯 Satisfaction Guarantee: Not satisfied after 2 sessions? 3rd session is complimentary.")
    
    def _render_copyright(self):
        """Render copyright using Streamlit components"""
        current_year = datetime.datetime.now().year
        
        # Legal links using columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.caption("Privacy Policy")
        with col2:
            st.caption("Terms of Service")
        with col3:
            st.caption("Confidentiality Agreement")
        
        # Copyright notice
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem; color: #556D7A;">
            © {current_year} {AppConfig.PRACTITIONER_NAME} • All Rights Reserved<br>
            🔒 All sessions strictly confidential • Licensed & Insured • Professional Standards Guaranteed
        </div>
        """, unsafe_allow_html=True)

class QuickContact:
    """Quick contact component for floating or emergency use"""
    
    def render_emergency_notice(self):
        """Render emergency contact notice"""
        st.error("""
        🚨 **Crisis Support**: If you're experiencing a mental health crisis, 
        please contact emergency services immediately. Our services are for 
        transformation and improvement, not crisis intervention.
        """)
    
    def render_quick_actions(self):
        """Render quick action buttons"""
        st.markdown("### Quick Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📞 Free Discovery Call", type="primary", use_container_width=True):
                st.success("Scroll up to book your call!")
        
        with col2:
            if st.button("🎯 Take Assessment", use_container_width=True):
                st.success("Scroll up to start the quiz!")

# Factory function for easy import
def create_footer():
    """Create Footer instance"""
    return Footer()
