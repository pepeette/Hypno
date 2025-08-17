# """
# Footer component for the Hypnotherapy website
# Displays contact information, credentials, and links
# """
# import streamlit as st
# import datetime

# class Footer:
#     """Footer component with contact info and credentials"""
    
#     def __init__(self):
#         # Try to import from config
#         try:
#             from utils.config import AppConstants
#             self.contact_info = AppConstants.CONTACT_INFO
#             self.founder_image = AppConstants.IMAGES.get("founder_photo", "")
#         except ImportError:
#             # Fallback values
#             self.contact_info = {
#                 "clinic_name": "Bangkok Hypnotherapy Clinic",
#                 "address": "27 Soi Sukhumvit 10 (Asoke)",
#                 "city": "Bangkok, Thailand",
#                 "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
#                 "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting"
#             }
#             self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
#     def render(self):
#         """Render the complete footer"""
#         # Add spacing before footer
#         st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
        
#         # Horizontal line separator
#         st.markdown("""
#         <div style="border-top: 1px solid var(--border); margin: 2rem 0;"></div>
#         """, unsafe_allow_html=True)
        
#         # Main footer content
#         self._render_main_footer()
        
#         # Copyright section
#         self._render_copyright()
    
#     def _render_main_footer(self):
#         """Render main footer content"""
#         col1, col2 = st.columns([2, 1], gap="large")
        
#         with col1:
#             self._render_founder_section()
        
#         with col2:
#             self._render_contact_section()
    
#     def _render_founder_section(self):
#         """Render founder information section"""
#         subcol1, subcol2 = st.columns([1, 3], gap="medium")
        
#         with subcol1:
#             st.markdown(f"""
#             <img src="{self.founder_image}" 
#                  alt="Laetitia Sheppard"
#                  style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; 
#                         border: 2px solid var(--accent); display: block;">
#             """, unsafe_allow_html=True)
        
#         with subcol2:
#             st.markdown("## Laetitia Sheppard")
#             st.markdown("""
#             Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.
            
#             **Credentials:**
#             - Certified Clinical Hypnotherapist
#             - Advanced Neuro-Linguistic Programming
#             - Specialized in Rapid Transformation Therapy
#             - Member, International Association of Hypnotherapists
#             """)
    
#     def _render_contact_section(self):
#         """Render contact information section"""
#         st.markdown("## Contact")
#         st.markdown(f"**{self.contact_info['clinic_name']}**")
#         st.markdown(f"{self.contact_info['address']}")
#         st.markdown(f"{self.contact_info['city']}")
        
#         st.markdown("**Session Options:**")
#         st.markdown("• In-person (Bangkok clinic)")
#         st.markdown("• Online (worldwide)")
#         st.markdown("• Home visits (Bangkok area)")
        
#         # Action buttons
#         self._render_footer_buttons()
    
#     def _render_footer_buttons(self):
#         """Render footer action buttons"""
#         btn_col1, btn_col2 = st.columns(2, gap="small")
        
#         with btn_col1:
#             st.markdown(f"""
#             <a href="{self.contact_info['maps_url']}" 
#                target="_blank" 
#                style="display: inline-block; background-color: var(--accent); color: white; 
#                       text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
#                       font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
#                       box-sizing: border-box; transition: var(--transition);">
#                 📍 Directions
#             </a>
#             """, unsafe_allow_html=True)
        
#         with btn_col2:
#             st.markdown(f"""
#             <a href="{self.contact_info['calendly_url']}" 
#                target="_blank" 
#                style="display: inline-block; background-color: var(--accent); color: white; 
#                       text-decoration: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); 
#                       font-weight: 600; font-size: 1rem; text-align: center; width: 100%;
#                       box-sizing: border-box; transition: var(--transition);">
#                 📅 Book Now
#             </a>
#             """, unsafe_allow_html=True)
    
#     def _render_copyright(self):
#         """Render copyright and legal information"""
#         current_year = datetime.datetime.now().year
        
#         st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
#         st.markdown(f"""
#         <div style="border-top: 1px solid var(--border); padding-top: 2rem; text-align: center;">
#             <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
#                 <div>
#                     <p style="margin: 0;">© {current_year} Laetitia Sheppard • All Rights Reserved</p>
#                 </div>
#                 <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
#                     <a href="#privacy" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
#                         Privacy Policy
#                     </a>
#                     <a href="#terms" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
#                         Terms of Service
#                     </a>
#                     <a href="#confidentiality" style="color: var(--text-secondary); text-decoration: none; font-size: 0.9rem;">
#                         Confidentiality
#                     </a>
#                 </div>
#             </div>
#             <div style="margin-top: 1rem;">
#                 <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
#                     🔒 All sessions are strictly confidential • Licensed & Insured • Professional Standards Guaranteed
#                 </p>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

# class QuickContact:
#     """Quick contact widget for floating or sidebar use"""
    
#     def __init__(self):
#         try:
#             from utils.config import AppConstants
#             self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "#")
#             self.package_url = AppConstants.CONTACT_INFO.get("package_booking_url", "#")
#         except ImportError:
#             self.discovery_url = "#"
#             self.package_url = "#"
    
#     def render_floating_cta(self):
#         """Render floating call-to-action button"""
#         cta_html = f"""
#         <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
#             <a href="{self.discovery_url}" 
#                target="_blank"
#                style="display: flex; align-items: center; gap: 8px;
#                       background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
#                       color: white; text-decoration: none; padding: 12px 16px;
#                       border-radius: 25px; font-weight: 600; font-size: 0.9rem;
#                       box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4);
#                       transition: all 0.3s ease; animation: pulse 2s infinite;">
#                 <span>📞</span>
#                 <span>Free Call</span>
#             </a>
#         </div>
        
#         <style>
#         @keyframes pulse {{
#             0% {{ box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }}
#             50% {{ box-shadow: 0 4px 25px rgba(76, 161, 163, 0.6); }}
#             100% {{ box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); }}
#         }}
        
#         @media (max-width: 768px) {{
#             .floating-cta {{
#                 bottom: 10px;
#                 right: 10px;
#                 padding: 10px 14px;
#                 font-size: 0.8rem;
#             }}
#         }}
#         </style>
#         """
        
#         st.markdown(cta_html, unsafe_allow_html=True)
    
#     def render_quick_actions(self):
#         """Render quick action buttons"""
#         st.markdown("### Quick Actions")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown(f"""
#             <a href="{self.discovery_url}" target="_blank" 
#                style="display: block; background-color: var(--accent); color: white;
#                       text-decoration: none; padding: 0.8rem; border-radius: var(--radius-sm);
#                       font-weight: 600; text-align: center; margin-bottom: 0.5rem;">
#                 📞 Free Call
#             </a>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown(f"""
#             <a href="{self.package_url}" target="_blank" 
#                style="display: block; background-color: var(--success); color: white;
#                       text-decoration: none; padding: 0.8rem; border-radius: var(--radius-sm);
#                       font-weight: 600; text-align: center; margin-bottom: 0.5rem;">
#                 ⚡ Book Sessions
#             </a>
#             """, unsafe_allow_html=True)

# class SocialProofFooter:
#     """Social proof elements for footer"""
    
#     def render_trust_badges(self):
#         """Render trust and certification badges"""
#         badges_html = """
#         <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; 
#                     margin: 2rem 0; padding: 1.5rem; background: var(--card-bg); 
#                     border-radius: var(--radius-md); border: 1px solid var(--border);">
#             <div style="text-align: center; color: var(--text-secondary);">
#                 <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🏆</div>
#                 <div style="font-size: 0.8rem; font-weight: 600;">Certified</div>
#                 <div style="font-size: 0.7rem;">Clinical Hypnotherapist</div>
#             </div>
#             <div style="text-align: center; color: var(--text-secondary);">
#                 <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔒</div>
#                 <div style="font-size: 0.8rem; font-weight: 600;">Licensed</div>
#                 <div style="font-size: 0.7rem;">& Insured</div>
#             </div>
#             <div style="text-align: center; color: var(--text-secondary);">
#                 <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⭐</div>
#                 <div style="font-size: 0.8rem; font-weight: 600;">10+ Years</div>
#                 <div style="font-size: 0.7rem;">Experience</div>
#             </div>
#             <div style="text-align: center; color: var(--text-secondary);">
#                 <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🤝</div>
#                 <div style="font-size: 0.8rem; font-weight: 600;">500+</div>
#                 <div style="font-size: 0.7rem;">Success Stories</div>
#             </div>
#         </div>
#         """
        
#         st.markdown(badges_html, unsafe_allow_html=True)
    
#     def render_guarantee(self):
#         """Render satisfaction guarantee"""
#         guarantee_html = """
#         <div style="background: rgba(34, 197, 94, 0.1); border: 1px solid var(--success);
#                     border-radius: var(--radius-md); padding: 1.5rem; text-align: center; margin: 2rem 0;">
#             <h3 style="color: var(--success); margin-bottom: 1rem;">💯 Satisfaction Guarantee</h3>
#             <p style="margin: 0; color: var(--text-secondary);">
#                 If you're not completely satisfied after 2 sessions, 
#                 your 3rd session is complimentary. Your transformation is our commitment.
#             </p>
#         </div>
#         """
        
#         st.markdown(guarantee_html, unsafe_allow_html=True)

# # Factory functions for easy import
# def create_footer():
#     """Factory function to create Footer instance"""
#     return Footer()

# def create_quick_contact():
#     """Factory function to create QuickContact instance"""
#     return QuickContact()

# def create_social_proof_footer():
#     """Factory function to create SocialProofFooter instance"""
#     return SocialProofFooter()


"""
Enhanced Footer component with consistent discovery call linking
Professional design with trust signals and clear CTAs
"""
import streamlit as st
import datetime

class EnhancedFooter:
    """Enhanced footer component with discovery call integration"""
    
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
                "discovery_call_url": "https://calendly.com/laetitiasheppard/discovery",
                "package_booking_url": "https://calendly.com/laetitiasheppard/package"
            }
            self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
    def render(self):
        """Render the complete enhanced footer"""
        # Pre-footer CTA section
        self._render_pre_footer_cta()
        
        # Main footer content
        self._render_main_footer()
        
        # Trust signals
        self._render_trust_signals()
        
        # Copyright section
        self._render_copyright()
    
    def _render_pre_footer_cta(self):
        """Render pre-footer call-to-action section"""
        cta_html = f"""
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0 2rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">
                Take the First Step Toward Transformation
            </h2>
            <p style="color: white; opacity: 0.9; font-size: 1.2rem; 
                      max-width: 500px; margin: 0 auto 2rem auto;">
                Every transformation begins with a single decision. 
                Make yours today.
            </p>
            <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                <a href="{self.contact_info['discovery_call_url']}" target="_blank" 
                   style="display: inline-block; background: white; color: var(--accent);
                          text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; font-size: 1.1rem; transition: all 0.3s ease;
                          box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    📞 Free Discovery Call
                </a>
                <a href="{self.contact_info['package_booking_url']}" target="_blank" 
                   style="display: inline-block; background: transparent; color: white;
                          text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; font-size: 1.1rem; border: 2px solid white;
                          transition: all 0.3s ease;">
                    ⚡ Book Sessions
                </a>
            </div>
        </div>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)
    
    def _render_main_footer(self):
        """Render main footer content"""
        # Spacing before footer
        st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
        
        # Horizontal line separator
        st.markdown("""
        <div style="border-top: 2px solid var(--border); margin: 2rem 0;"></div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1], gap="large")
        
        with col1:
            self._render_founder_section()
        
        with col2:
            self._render_contact_section()
    
    def _render_founder_section(self):
        """Render founder information section"""
        founder_html = f"""
        <div style="display: flex; gap: 2rem; align-items: flex-start;">
            <div style="min-width: 100px;">
                <img src="{self.founder_image}" 
                     alt="Laetitia Sheppard - Clinical Hypnotherapist"
                     style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; 
                            border: 3px solid var(--accent); display: block;
                            box-shadow: var(--shadow-md);">
            </div>
            <div style="flex: 1;">
                <h2 style="color: var(--accent); margin-bottom: 1rem;">Laetitia Sheppard</h2>
                <p style="color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6;">
                    Certified Clinical Hypnotherapist with over 10 years of experience in 
                    behavioral change and mental wellness. Helping people break free from 
                    limiting patterns and create lasting transformation.
                </p>
                
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="color: var(--text-primary); margin-bottom: 0.8rem; font-size: 1.1rem;">
                        Professional Credentials:
                    </h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.5rem;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="color: var(--accent);">✓</span>
                            <span style="font-size: 0.9rem;">Certified Clinical Hypnotherapist</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="color: var(--accent);">✓</span>
                            <span style="font-size: 0.9rem;">Advanced NLP Practitioner</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="color: var(--accent);">✓</span>
                            <span style="font-size: 0.9rem;">Rapid Transformation Therapy</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="color: var(--accent);">✓</span>
                            <span style="font-size: 0.9rem;">International Association Member</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(founder_html, unsafe_allow_html=True)
    
    def _render_contact_section(self):
        """Render contact information section"""
        contact_html = f"""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
            <h2 style="color: var(--accent); margin-bottom: 1.5rem; text-align: center;">
                Get Started Today
            </h2>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">📍 Clinic Location</h3>
                <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
                    <strong>{self.contact_info['clinic_name']}</strong>
                </p>
                <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
                    {self.contact_info['address']}
                </p>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                    {self.contact_info['city']}
                </p>
                
                <a href="{self.contact_info['maps_url']}" target="_blank" 
                   style="display: inline-block; background: var(--accent); color: white;
                          text-decoration: none; padding: 0.6rem 1.2rem; border-radius: var(--radius-sm);
                          font-weight: 600; font-size: 0.9rem; transition: all 0.3s ease;">
                    📍 Get Directions
                </a>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">🌍 Session Options</h3>
                <div style="space-y: 0.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
                        <span style="color: var(--accent);">🏢</span>
                        <span style="color: var(--text-secondary);">In-person (Bangkok clinic)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
                        <span style="color: var(--accent);">💻</span>
                        <span style="color: var(--text-secondary);">Online (worldwide via Zoom)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
                        <span style="color: var(--accent);">🏠</span>
                        <span style="color: var(--text-secondary);">Home visits (Bangkok area)</span>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center;">
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">📞 Ready to Begin?</h3>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <a href="{self.contact_info['discovery_call_url']}" target="_blank" 
                       style="display: block; background: var(--accent); color: white;
                              text-decoration: none; padding: 1rem; border-radius: var(--radius-sm);
                              font-weight: 600; text-align: center; transition: all 0.3s ease;">
                        📞 Book Free Discovery Call
                    </a>
                    <a href="{self.contact_info['package_booking_url']}" target="_blank" 
                       style="display: block; background: var(--success); color: white;
                              text-decoration: none; padding: 1rem; border-radius: var(--radius-sm);
                              font-weight: 600; text-align: center; transition: all 0.3s ease;">
                        ⚡ Book Transformation Package
                    </a>
                </div>
            </div>
        </div>
        """
        
        st.markdown(contact_html, unsafe_allow_html=True)
    
    def _render_trust_signals(self):
        """Render trust and credibility signals"""
        trust_html = """
        <div style="background: var(--card-bg); border-radius: var(--radius-md);
                    padding: 2rem; margin: 3rem 0; box-shadow: var(--shadow-sm);
                    border: 1px solid var(--border);">
            <h3 style="text-align: center; color: var(--accent); margin-bottom: 2rem;">
                🛡️ Your Trust & Security
            </h3>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                        gap: 2rem; text-align: center;">
                <div style="padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem; color: var(--accent);">🔒</div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">Confidential</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">
                        Strict client confidentiality<br>Professional standards maintained
                    </p>
                </div>
                
                <div style="padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem; color: var(--accent);">🏆</div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">Licensed</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">
                        Fully licensed & insured<br>International certification
                    </p>
                </div>
                
                <div style="padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem; color: var(--accent);">⭐</div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">Proven</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">
                        500+ successful transformations<br>85% success rate
                    </p>
                </div>
                
                <div style="padding: 1rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem; color: var(--accent);">💯</div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">Guaranteed</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">
                        Satisfaction guarantee<br>3rd session complimentary if needed
                    </p>
                </div>
            </div>
        </div>
        """
        
        st.markdown(trust_html, unsafe_allow_html=True)
    
    def _render_copyright(self):
        """Render copyright and legal information"""
        current_year = datetime.datetime.now().year
        
        copyright_html = f"""
        <div style="border-top: 1px solid var(--border); padding-top: 2rem; margin-top: 2rem;">
            <div style="text-align: center;">
                <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 2rem; margin-bottom: 1.5rem;">
                    <a href="#privacy" style="color: var(--text-secondary); text-decoration: none; 
                                            font-size: 0.9rem; transition: color 0.3s ease;">
                        Privacy Policy
                    </a>
                    <a href="#terms" style="color: var(--text-secondary); text-decoration: none; 
                                           font-size: 0.9rem; transition: color 0.3s ease;">
                        Terms of Service
                    </a>
                    <a href="#confidentiality" style="color: var(--text-secondary); text-decoration: none; 
                                                     font-size: 0.9rem; transition: color 0.3s ease;">
                        Confidentiality Agreement
                    </a>
                    <a href="{self.contact_info['discovery_call_url']}" target="_blank" 
                       style="color: var(--accent); text-decoration: none; font-weight: 600;
                              font-size: 0.9rem; transition: color 0.3s ease;">
                        📞 Contact Us
                    </a>
                </div>
                
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    © {current_year} Laetitia Sheppard • Clinical Hypnotherapist • All Rights Reserved
                </p>
                
                <div style="margin-top: 1rem; padding: 1rem; background: rgba(76, 161, 163, 0.05); 
                            border-radius: var(--radius-sm); border: 1px solid rgba(76, 161, 163, 0.2);">
                    <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                            🔒 All sessions are strictly confidential • Licensed & Insured • Professional Standards Guaranteed
                    </p>
                    <p style="margin: 0.5rem 0 0 0; color: var(--accent); font-weight: 600; font-size: 0.9rem;">
                        Ready to transform your life? 
                        <a href="{self.contact_info['discovery_call_url']}" target="_blank" 
                           style="color: var(--accent); text-decoration: underline;">
                            Start with a free discovery call →
                        </a>
                    </p>
                </div>
            </div>
        </div>
        """
        
        st.markdown(copyright_html, unsafe_allow_html=True)

class QuickContactWidget:
    """Enhanced quick contact widget for floating or sidebar use"""
    
    def __init__(self):
        try:
            from utils.config import AppConstants
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "#")
            self.package_url = AppConstants.CONTACT_INFO.get("package_booking_url", "#")
        except ImportError:
            self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
            self.package_url = "https://calendly.com/laetitiasheppard/package"
    
    def render_floating_cta(self):
        """Render enhanced floating call-to-action button"""
        cta_html = f"""
        <div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
            <div style="display: flex; flex-direction: column; gap: 0.5rem; align-items: flex-end;">
                <a href="{self.discovery_url}" 
                   target="_blank"
                   style="display: flex; align-items: center; gap: 8px;
                          background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                          color: white; text-decoration: none; padding: 12px 16px;
                          border-radius: 25px; font-weight: 600; font-size: 0.9rem;
                          box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4);
                          transition: all 0.3s ease; animation: pulse 3s infinite;">
                    <span>📞</span>
                    <span>Free Call</span>
                </a>
                
                <div style="background: rgba(255,255,255,0.95); padding: 0.5rem 1rem; 
                            border-radius: 15px; font-size: 0.8rem; color: var(--text-secondary);
                            box-shadow: 0 2px 10px rgba(0,0,0,0.1); animation: fadeInUp 1s ease-out 2s both;">
                    15 min • No obligation
                </div>
            </div>
        </div>
        
        <style>
        @keyframes pulse {{
            0% {{ box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); transform: scale(1); }}
            50% {{ box-shadow: 0 4px 25px rgba(76, 161, 163, 0.6); transform: scale(1.02); }}
            100% {{ box-shadow: 0 4px 20px rgba(76, 161, 163, 0.4); transform: scale(1); }}
        }}
        
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @media (max-width: 768px) {{
            .floating-cta {{
                bottom: 15px;
                right: 15px;
                padding: 10px 14px;
                font-size: 0.8rem;
            }}
        }}
        </style>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)
    
    def render_quick_actions(self):
        """Render enhanced quick action buttons"""
        st.markdown("### 🚀 Take Action Now")
        
        action_html = f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
            <a href="{self.discovery_url}" target="_blank" 
               style="display: block; background: var(--accent); color: white;
                      text-decoration: none; padding: 1rem; border-radius: var(--radius-sm);
                      font-weight: 600; text-align: center; transition: all 0.3s ease;
                      box-shadow: var(--shadow-sm);">
                📞 Free Discovery Call
                <div style="font-size: 0.8rem; opacity: 0.9; margin-top: 0.3rem;">
                    15 minutes • No pressure
                </div>
            </a>
            
            <a href="{self.package_url}" target="_blank" 
               style="display: block; background: var(--success); color: white;
                      text-decoration: none; padding: 1rem; border-radius: var(--radius-sm);
                      font-weight: 600; text-align: center; transition: all 0.3s ease;
                      box-shadow: var(--shadow-sm);">
                ⚡ Book Sessions
                <div style="font-size: 0.8rem; opacity: 0.9; margin-top: 0.3rem;">
                    2 sessions • 85% success
                </div>
            </a>
        </div>
        """
        
        st.markdown(action_html, unsafe_allow_html=True)

class SocialProofFooter:
    """Enhanced social proof elements for footer"""
    
    def render_guarantee_section(self):
        """Render enhanced satisfaction guarantee"""
        guarantee_html = """
        <div style="background: rgba(34, 197, 94, 0.1); border: 2px solid var(--success);
                    border-radius: var(--radius-md); padding: 2rem; text-align: center; 
                    margin: 2rem 0; position: relative; overflow: hidden;">
            
            <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px;
                        background: linear-gradient(90deg, var(--success), #10b981);"></div>
            
            <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
                <div style="background: var(--success); color: white; width: 60px; height: 60px;
                            border-radius: 50%; display: flex; align-items: center; 
                            justify-content: center; font-size: 1.8rem;">💯</div>
            </div>
            
            <h3 style="color: var(--success); margin-bottom: 1rem; font-size: 1.5rem;">
                100% Satisfaction Guarantee
            </h3>
            <p style="color: var(--text-secondary); margin-bottom: 1.5rem; font-size: 1.1rem; 
                      max-width: 600px; margin-left: auto; margin-right: auto;">
                If you're not completely satisfied after 2 sessions, your 3rd session is 
                complimentary. Your transformation is our commitment.
            </p>
            
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.5rem;">
                <div style="text-align: center;">
                    <div style="font-weight: bold; color: var(--success); font-size: 1.2rem;">No Risk</div>
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">Money-back assurance</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-weight: bold; color: var(--success); font-size: 1.2rem;">No Pressure</div>
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">Your pace, your choice</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-weight: bold; color: var(--success); font-size: 1.2rem;">Proven Results</div>
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">500+ success stories</div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(guarantee_html, unsafe_allow_html=True)
    
    def render_urgency_element(self):
        """Render subtle urgency element"""
        urgency_html = """
        <div style="background: rgba(76, 161, 163, 0.05); border: 1px solid rgba(76, 161, 163, 0.3);
                    border-radius: var(--radius-sm); padding: 1.5rem; margin: 2rem 0; text-align: center;">
            <p style="color: var(--text-secondary); margin: 0; font-size: 0.95rem;">
                <strong style="color: var(--accent);">Limited Availability:</strong> 
                To maintain quality, Laetitia only accepts a limited number of new clients each month. 
                <a href="#discovery" style="color: var(--accent); font-weight: 600; text-decoration: underline;">
                    Secure your spot today
                </a>
            </p>
        </div>
        """
        
        st.markdown(urgency_html, unsafe_allow_html=True)

# Factory functions for easy import
def create_enhanced_footer():
    """Factory function to create EnhancedFooter instance"""
    return EnhancedFooter()

def create_quick_contact():
    """Factory function to create QuickContactWidget instance"""
    return QuickContactWidget()

def create_social_proof_footer():
    """Factory function to create SocialProofFooter instance"""
    return SocialProofFooter()
