"""
Footer component for the Hypnotherapy website
Displays contact information, credentials, and links
"""
import streamlit as st
import datetime

class Footer:
    """Footer component with contact info and credentials"""
    
    def __init__(self):
        # Try to import from config
        try:
            from utils.config import AppConstants
            self.contact_info = AppConstants.CONTACT_INFO
            self.founder_image = AppConstants.IMAGES.get("founder_photo", "")
        except ImportError:
            # Fallback values
            self.contact_info = {
                "clinic_name": "Bangkok Hypnotherapy Clinic",
                "address": "27 Soi Sukhumvit 10 (Asoke)",
                "city": "Bangkok, Thailand",
                "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
                "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting"
            }
            self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
    def render(self):
        """Render the complete footer"""
        # Add spacing before footer
        st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
        
        # Horizontal line separator
        st.markdown("""
        <div style="border-top: 1px solid var(--border); margin: 2rem 0;"></div>
        """, unsafe_allow_html=True)
        
        # Main footer content
        self._render_main_footer()
        
        # Copyright section
        self._render_copyright()
    
    def _render_main_footer(self):
        """Render main footer content"""
        col1, col2 = st.columns([2, 1], gap="large")
        
        with col1:
            self._render_founder_section()
        
        with col2:
            self._render_contact_section()
    
    def _render_founder_section(self):
        """Render founder information section"""
        subcol1, subcol2 = st.columns([1, 3], gap="medium")
        
        with subcol1:
            st.markdown(f"""
            <img src="{self.founder_image}" 
                 alt="Laetitia Sheppard"
                 style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; 
                        border: 2px solid var(--accent); display: block;">
            """, unsafe_allow_html=True)
        
        with subcol2:
            st.markdown("## Laetitia Sheppard")
            st.markdown("""
            Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.
            
            **Credentials:**
            - Certified Clinical Hypnotherapist
            - Advanced Neuro-Linguistic Programming
            - Specialized in Rapid Transformation Therapy
            - Member, International Association of Hypnotherapists
            """)
    
    def _render_contact_section(self):
        """Render contact information section"""
        st.markdown("## Contact")
        st.markdown(f"**{self.contact_info['clinic_name']}**")
        st.markdown(f"{self.contact_info['address']}")
        st.markdown(f"{self.contact_info['city']}")
        
        st.markdown("**Session Options:**")
        st.markdown("• In-person (Bangkok clinic)")
        st.markdown("• Online (worldwide)")
        st.markdown("• Home visits (Bangkok area)")
        
        # Action buttons
        self._render_footer_buttons()
    
    def _render_footer_buttons(self):
        """Render footer action buttons"""
        btn_col1, btn_col2 = st.columns(2, gap="small")
        
        with btn_col1:
            st.markdown(f"""
            <a href="{self.contact_info['maps_url']}" 
               target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white; 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                      font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
                      box-sizing: border-box; transition: var(--transition);">
                📍 Directions
            </a>
            """, unsafe_allow_html=True)
        
        with btn_col2:
            st.markdown(f"""
            <a href="{self.contact_info['calendly_url']}" 
               target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white; 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
                      font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
                      box-sizing: border-box; transition: var(--transition);">
                📅 Book Now
            </a>
            """, unsafe_allow_html=True)
    
    def _render_copyright(self):
        """Render copyright and legal information"""
        current_year = datetime.datetime.now().year
        
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="border-top: 1px solid var(--border); padding-top: 2rem; text-align: center;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <p style="margin: 0;">© {current_year} Laetitia Sheppard • All Rights Reserved</p>
                </div>
                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <a href="#privacy" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
                        Privacy Policy
                    </a>
                    <a href="#terms" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
                        Terms of Service
                    </a>
                    <a href="#confidentiality" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
                        Confidentiality
                    </a>
                </div>
            </div>
            <div style="margin-top: 1rem;">
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    🔒 All sessions are
