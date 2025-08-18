"""
FIXED Footer component - Simplified and reliable
Uses Streamlit native components, reliable image hosting
"""
import streamlit as st
import datetime

class Footer:
    """Simplified footer component using Streamlit native elements"""
    
    def __init__(self):
        # Reliable contact info
        self.contact_info = {
            "clinic_name": "Bangkok Hypnotherapy Clinic",
            "address": "27 Soi Sukhumvit 10 (Asoke)",
            "city": "Bangkok, Thailand",
            "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
            "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting"
        }
        # Base64 encoded small founder image (reliable)
        self.founder_image_b64 = "data:image/jpeg;base64,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"
    
    def render(self):
        """Render simplified footer using Streamlit components"""
        # Add spacing before footer
        st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
        
        # Separator line
        st.markdown("---")
        
        # Main footer content using Streamlit columns
        col1, col2 = st.columns([2, 1], gap="large")
        
        with col1:
            self._render_founder_section()
        
        with col2:
            self._render_contact_section()
        
        # Action buttons
        self._render_action_buttons()
        
        # Copyright
        self._render_copyright()
    
    def _render_founder_section(self):
        """Render founder section using Streamlit components"""
        subcol1, subcol2 = st.columns([1, 3])
        
        with subcol1:
            # Use base64 image for reliability
            st.markdown(f"""
            <img src="{self.founder_image_b64}" 
                 alt="Laetitia Sheppard"
                 style="width: 80px; height: 80px; border-radius: 50%; 
                        border: 2px solid #4CA1A3; display: block;">
            """, unsafe_allow_html=True)
        
        with subcol2:
            st.markdown("### Laetitia Sheppard")
            st.write("**Certified Clinical Hypnotherapist**")
            st.write("10+ years experience in behavioral change")
            st.write("🏆 LCCH Certified • 📈 85% Success Rate")
    
    def _render_contact_section(self):
        """Render contact information"""
        st.markdown("### Contact")
        st.write(f"**{self.contact_info['clinic_name']}**")
        st.write(f"{self.contact_info['address']}")
        st.write(f"{self.contact_info['city']}")
        st.write("")
        st.write("**Session Options:**")
        st.write("• In-person (Bangkok clinic)")
        st.write("• Online (worldwide)")
        st.write("• Home visits (Bangkok area)")
    
    def _render_action_buttons(self):
        """Render action buttons using Streamlit"""
        st.markdown("### Quick Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📍 Get Directions", use_container_width=True):
                st.success("Opening Google Maps...")
                # In production: st.components.v1.html(f'<script>window.open("{self.contact_info["maps_url"]}", "_blank");</script>')
        
        with col2:
            if st.button("📅 Book Now", use_container_width=True, type="primary"):
                st.success("Opening booking calendar...")
                # In production: st.components.v1.html(f'<script>window.open("{self.contact_info["calendly_url"]}", "_blank");</script>')
    
    def _render_copyright(self):
        """Render copyright section"""
        current_year = datetime.datetime.now().year
        
        st.markdown("---")
        
        # Trust indicators
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("🏆 **Certified**")
            st.write("Clinical Hypnotherapist")
        with col2:
            st.write("🔒 **Licensed**")
            st.write("& Insured")
        with col3:
            st.write("⭐ **10+ Years**")
            st.write("Experience")
        with col4:
            st.write("🤝 **500+**")
            st.write("Success Stories")
        
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem; color: #556D7A;">
            <p>© {current_year} Laetitia Sheppard • All Rights Reserved</p>
            <p style="font-size: 0.9rem;">🔒 All sessions strictly confidential • Professional Standards Guaranteed</p>
        </div>
        """, unsafe_allow_html=True)

def create_footer():
    """Factory function to create Footer instance"""
    return Footer()
