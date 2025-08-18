"""
Footer component for the Hypnotherapy website
Displays contact information, credentials, and links
Professional, informative, and engaging footer with clear CTAs
"""
import streamlit as st
import datetime

class EnhancedFooter:
    """Enhanced footer component with better visual hierarchy"""
    
    def __init__(self):
        # Contact information
        self.contact_info = {
            "clinic_name": "Bangkok Hypnotherapy Clinic",
            "address": "27 Soi Sukhumvit 10 (Asoke)",
            "city": "Bangkok, Thailand",
            "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
            "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting",
            "discovery_url": "https://calendly.com/laetitiasheppard/discovery"
        }
        
        # Founder image
        self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
    def render(self):
        """Render the complete enhanced footer"""
        # Separator
        st.markdown("""
        <div style="border-top: 1px solid var(--border); margin: 4rem 0 2rem 0;"></div>
        """, unsafe_allow_html=True)
        
        # Main footer content
        self._render_main_footer()
        
        # Trust indicators
        self._render_trust_section()
        
        # Copyright
        self._render_copyright()
    
    def _render_main_footer(self):
        """Render main footer content with better layout"""
        col1, col2, col3 = st.columns([2, 2, 2], gap="large")
        
        with col1:
            self._render_founder_section()
        
        with col2:
            self._render_contact_section()
        
        with col3:
            self._render_quick_links()
    
    def _render_founder_section(self):
        """Render founder information with professional styling"""
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{self.founder_image}" 
                 alt="Laetitia Sheppard - Clinical Hypnotherapist"
                 style="width: 100px; height: 100px; border-radius: 50%; 
                        object-fit: cover; border: 3px solid var(--accent); 
                        margin-bottom: 1rem; box-shadow: 0 4px 16px rgba(76, 161, 163, 0.2);">
            <h2 style="color: var(--text-primary); margin-bottom: 0.5rem;">
                Laetitia Sheppard
            </h2>
            <p style="color: var(--accent); font-weight: 600; margin-bottom: 1rem;">
                Certified Clinical Hypnotherapist
            </p>
            <div style="background: rgba(76, 161, 163, 0.1); border-radius: 8px; 
                        padding: 1rem; margin-bottom: 1rem;">
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    ✅ 10+ Years Experience<br>
                    ✅ 500+ Successful Transformations<br>
                    ✅ Advanced NLP Certification<br>
                    ✅ Member, International Association of Hypnotherapists
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_contact_section(self):
        """Render contact information with clear hierarchy"""
        st.markdown(f"""
        <div>
            <h2 style="color: var(--text-primary); margin-bottom: 1rem;">📍 Contact & Location</h2>
            <div style="background: var(--card-bg); border-radius: 8px; 
                        padding: 1.5rem; border: 1px solid var(--border);
                        box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <p style="margin-bottom: 0.5rem; font-weight: 600; color: var(--text-primary);">
                    {self.contact_info['clinic_name']}
                </p>
                <p style="margin-bottom: 0.5rem; color: var(--text-secondary);">
                    {self.contact_info['address']}<br>
                    {self.contact_info['city']}
                </p>
                
                <div style="margin: 1.5rem 0;">
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">
                        Session Options:
                    </h3>
                    <p style="margin: 0; color: var(--text-secondary);">
                        🏢 In-person (Bangkok clinic)<br>
                        💻 Online sessions (worldwide)<br>
                        🏠 Home visits (Bangkok area)
                    </p>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <a href="{self.contact_info['maps_url']}" target="_blank" 
                       style="display: block; background-color: var(--accent); color: white;
                              text-decoration: none; padding: 0.75rem; border-radius: 8px;
                              font-weight: 600; text-align: center; transition: all 0.3s ease;">
                        📍 Get Directions
                    </a>
                    <a href="{self.contact_info['discovery_url']}" target="_blank" 
                       style="display: block; background-color: var(--success); color: white;
                              text-decoration: none; padding: 0.75rem; border-radius: 8px;
                              font-weight: 600; text-align: center; transition: all 0.3s ease;">
                        📞 Book Free Call
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_quick_links(self):
        """Render quick links and resources"""
        st.markdown("""
        <div>
            <h2 style="color: var(--text-primary); margin-bottom: 1rem;">🔗 Quick Links</h2>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <a href="#quiz-section" 
                   style="color: var(--accent); text-decoration: none; 
                          padding: 0.5rem; border-radius: 4px; 
                          transition: all 0.3s ease; display: block;">
                    🎯 Take 30-Second Assessment
                </a>
                <a href="#booking" 
                   style="color: var(--accent); text-decoration: none; 
                          padding: 0.5rem; border-radius: 4px; 
                          transition: all 0.3s ease; display: block;">
                    📅 Schedule Sessions
                </a>
                <a href="#method" 
                   style="color: var(--accent); text-decoration: none; 
                          padding: 0.5rem; border-radius: 4px; 
                          transition: all 0.3s ease; display: block;">
                    🧠 Learn Our Method
                </a>
                <a href="#success" 
                   style="color: var(--accent); text-decoration: none; 
                          padding: 0.5rem; border-radius: 4px; 
                          transition: all 0.3s ease; display: block;">
                    ⭐ Read Success Stories
                </a>
            </div>
            
            <div style="margin-top: 2rem; padding: 1rem; 
                        background: rgba(34, 197, 94, 0.1); 
                        border-radius: 8px; border-left: 4px solid var(--success);">
                <h3 style="color: var(--success); margin-bottom: 0.5rem;">
                    ⏰ Operating Hours
                </h3>
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    Monday - Friday: 9:00 - 18:00<br>
                    Saturday: 10:00 - 16:00<br>
                    Sunday: By appointment only<br>
                    <em>Online sessions available 24/7</em>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_trust_section(self):
        """Render trust indicators and social proof"""
        st.markdown("""
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: 12px; 
                    padding: 2rem; margin: 2rem 0; text-align: center;">
            <h2 style="color: var(--accent); margin-bottom: 1.5rem;">
                Why Clients Trust Us
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); 
                        gap: 1.5rem;">
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🏆</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Certified</h3>
                    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                        Clinical Hypnotherapist
                    </p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔒</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Licensed</h3>
                    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                        & Fully Insured
                    </p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⭐</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Experienced</h3>
                    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                        10+ Years Practice
                    </p>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🤝</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Trusted</h3>
                    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                        500+ Success Stories
                    </p>
                </div>
            </div>
            
            <div style="background: white; border-radius: 8px; padding: 1.5rem; 
                        margin-top: 2rem; border: 1px solid var(--border);">
                <h3 style="color: var(--success); margin-bottom: 1rem;">
                    💯 Our Guarantee
                </h3>
                <p style="margin: 0; color: var(--text-secondary);">
                    If you're not completely satisfied after 2 sessions, 
                    your 3rd session is complimentary. Your transformation is our commitment.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_copyright(self):
        """Render copyright and legal information"""
        current_year = datetime.datetime.now().year
        
        st.markdown(f"""
        <div style="border-top: 1px solid var(--border); padding-top: 2rem; 
                    text-align: center; margin-top: 2rem;">
            <div style="display: flex; justify-content: space-between; 
                        align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <p style="margin: 0; color: var(--text-secondary);">
                        © {current_year} Laetitia Sheppard • All Rights Reserved
                    </p>
                </div>
                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">
                        Privacy Guaranteed
                    </span>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">
                        Professional Standards
                    </span>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">
                        Confidential Sessions
                    </span>
                </div>
            </div>
            <div style="margin-top: 1rem;">
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    🔒 All sessions are strictly confidential • Licensed & Insured • 
                    Professional Standards Guaranteed
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_footer():
    """Factory function to create enhanced footer"""
    return EnhancedFooter()
