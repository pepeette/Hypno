# """
# Clean footer component for the Hypnotherapy website
# """
# import streamlit as st
# import datetime

# class Footer:
#     """Simple, clean footer component"""
    
#     def __init__(self):
#         # Contact info and image URL
#         self.contact_info = {
#             "clinic_name": "Bangkok Hypnotherapy Clinic",
#             "address": "27 Soi Sukhumvit 10 (Asoke)",
#             "city": "Bangkok, Thailand",
#             "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
#             "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting"
#         }
#         self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
#     def render(self):
#         """Render the complete footer"""
#         st.markdown("---")
        
#         # Main footer content
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             # Founder section
#             col_img, col_text = st.columns([1, 3])
            
#             with col_img:
#                 st.image(self.founder_image, width=100)
            
#             with col_text:
#                 st.markdown("### Laetitia Sheppard")
#                 st.write("Certified Clinical Hypnotherapist")
#                 st.write("LCCH Certified 2017 • DBT Certified 2023")
#                 st.write("10+ years experience helping people transform their lives")
        
#         with col2:
#             # Contact section
#             st.markdown("### Contact")
#             st.write(f"**{self.contact_info['clinic_name']}**")
#             st.write(f"{self.contact_info['address']}")
#             st.write(f"{self.contact_info['city']}")
#             st.write("")
#             st.write("**Session Options:**")
#             st.write("• In-person (Bangkok clinic)")
#             st.write("• Online (worldwide)")
#             st.write("• Home visits (Bangkok area)")
            
#             # Action buttons
#             if st.button("📍 Get Directions", use_container_width=True):
#                 st.markdown(f"[Open Maps]({self.contact_info['maps_url']})")
            
#             if st.button("📅 Book Now", use_container_width=True, type="primary"):
#                 st.markdown(f"[Schedule Call]({self.contact_info['calendly_url']})")
        
#         # Copyright section
#         current_year = datetime.datetime.now().year
#         st.markdown(f"""
#         <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; 
#                     border-top: 1px solid var(--border); color: var(--text-secondary);">
#             <p>© {current_year} Laetitia Sheppard • All Rights Reserved</p>
#             <p style="font-size: 0.9rem;">
#                 🔒 All sessions are strictly confidential • Licensed & Insured • Professional Standards Guaranteed
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# class BookingForm:
#     """Clean booking form component"""
    
#     def __init__(self):
#         self.concern_options = [
#             "Select one...", 
#             "Quit Smoking", 
#             "Reduce Anxiety", 
#             "Improve Sleep", 
#             "Break Bad Habits",
#             "Other"
#         ]
#         self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
    
#     def render(self):
#         """Render the booking form"""
#         st.markdown("---")
#         st.markdown("## 📞 Book Your Free Discovery Call")
#         st.write("Begin your transformation with a complimentary 15-minute consultation")
        
#         # Benefits of discovery call
#         st.markdown("""
#         <div style="background: rgba(76, 161, 163, 0.05); border-radius: 12px;
#                     padding: 1.5rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
#             <h3 style="color: var(--accent);">What You'll Get in Your Discovery Call:</h3>
#             <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
#                 <div>✓ Personalized assessment of your situation</div>
#                 <div>✓ Clear explanation of how hypnotherapy works</div>
#                 <div>✓ Honest assessment of your success probability</div>
#                 <div>✓ Answers to all your questions</div>
#                 <div>✓ No pressure, no obligation</div>
#                 <div>✓ Next steps if you decide to proceed</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Booking form
#         with st.form("discovery_booking_form"):
#             col1, col2 = st.columns(2)
#             with col1:
#                 name = st.text_input("Your Name*", placeholder="First and last name")
#             with col2:
#                 email = st.text_input("Email*", placeholder="your@email.com")
            
#             concern = st.selectbox("What would you most like to change?*", self.concern_options)
            
#             message = st.text_area(
#                 "Anything specific you'd like to discuss?", 
#                 placeholder="Optional: Any questions, concerns, or background information"
#             )
            
#             submitted = st.form_submit_button("📞 Schedule My Free Discovery Call", type="primary", use_container_width=True)
            
#             if submitted:
#                 if self._validate_form(name, email, concern):
#                     st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
#                     st.markdown(f"""
#                     <div style="text-align: center; margin: 2rem 0;">
#                         <a href="{self.discovery_url}" target="_blank" 
#                            style="display: inline-block; background-color: var(--accent); color: white;
#                                   text-decoration: none; padding: 1rem 2rem; border-radius: 8px;
#                                   font-weight: 600;">
#                             📅 Or Choose Your Time Slot Directly
#                         </a>
#                     </div>
#                     """, unsafe_allow_html=True)
#                     st.balloons()
#                 else:
#                     st.error("Please fill in all required fields with valid information.")
    
#     def _validate_form(self, name, email, concern):
#         """Simple form validation"""
#         if not name or not email or concern == "Select one...":
#             return False
        
#         # Basic email validation
#         if "@" not in email or "." not in email:
#             return False
        
#         return True

# # Factory functions
# def create_footer():
#     return Footer()

# def create_booking_form():
#     return BookingForm()



"""
Footer component for the Hypnotherapy website
Displays contact information, credentials, and links
Clean design using Streamlit components with minimal HTML
"""
import streamlit as st
import datetime

class Footer:
    """Professional footer component using Streamlit elements"""
    
    def __init__(self):
        # Try to import from config, with fallbacks
        try:
            from utils.config import AppConstants
            self.contact_info = AppConstants.CONTACT_INFO
            self.founder_image = AppConstants.IMAGES.get("founder_photo", "")
        except ImportError:
            # Fallback values
            self.contact_info = {
                "clinic_name": "NEW ADDRESS in BANGKOK",
                "address": "27 Soi Sukhumvit 10 (Asoke)",
                "city": "Bangkok, Thailand",
                "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
                "calendly_url": "https://calendly.com/laetitiasheppard/"
            }
            self.founder_image = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
    def render(self):
        """Render the complete footer using Streamlit components"""
        # Add spacing before footer
        st.markdown("<div style='margin-top: 4rem;'></div>", unsafe_allow_html=True)
        
        # Horizontal separator
        st.markdown("   ")
        
        # Main footer content
        self._render_main_footer()
        
        # Trust indicators
        self._render_trust_indicators()
        
        # Copyright section
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
        # Founder image and info in columns
        col_img, col_text = st.columns([1, 3], gap="medium")
        
        with col_img:
            # Use markdown for better control over the circular image
            st.markdown(f"""
            <img src="{self.founder_image}" 
                 alt="Laetitia Sheppard"
                 style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; 
                        border: 2px solid var(--accent); display: block;">
            """, unsafe_allow_html=True)
        
        with col_text:
            st.markdown("## Laetitia Sheppard")
            st.write("Certified Clinical Hypnotherapist with over 10 years of experience in behavioral change and mental wellness.")
            
            # Credentials using simple text
            st.markdown("**Credentials:**")
            st.write("• Certified Clinical Hypnotherapist")
            st.write("• Advanced Neuro-Linguistic Programming")
            st.write("• Specialized in Rapid Transformation Therapy")
            st.write("• Member, British Society of Clinical Hypnosis")
    
    def _render_contact_section(self):
        """Render contact information using Streamlit components"""
        st.markdown("## Contact")
        st.write(f"**{self.contact_info['clinic_name']}**")
        st.write(f"{self.contact_info['address']}")
        st.write(f"{self.contact_info['city']}")
                
        # Action buttons using styled markdown links for better compatibility
        st.markdown("""
        <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, gap="small")
        
        with col1:
            st.markdown(f"""
            <a href="{self.contact_info['maps_url']}" 
               target="_blank" 
               style="display: block; background-color: var(--border); color: var(--text-primary); 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: 8px; 
                      font-weight: 600; text-align: center; transition: all 0.3s ease;">
                📍 Directions
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <a href="{self.contact_info['calendly_url']}" 
               target="_blank" 
               style="display: block; background-color: var(--accent); color: white; 
                      text-decoration: none; padding: 0.5rem 1rem; border-radius: 8px; 
                      font-weight: 600; text-align: center; transition: all 0.3s ease;">
                📅 Book Now
            </a>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_trust_indicators(self):
        """Render trust badges using Streamlit metrics and simple layout"""
        st.markdown("### 🏆 Professional Standards")
        
        # Use columns for trust indicators
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("**🏆 Certified**")
            st.write("Clinical Hypnotherapist")
            st.caption("Professional qualification")
        
        with col2:
            st.markdown("**🔒 Licensed**")
            st.write("& Insured")
            st.caption("Professional standards")
        
        with col3:
            st.markdown("**⭐ 10+ Years**")
            st.write("Experience")
            st.caption("Established practice")
        
        with col4:
            st.markdown("**🤝 500+**")
            st.write("Success Stories")
            st.caption("Proven results")
        
        # Satisfaction guarantee
        st.success("💯 Satisfaction Guarantee: If you're not completely satisfied after 2 sessions, your 3rd session is complimentary.")
    
    def _render_copyright(self):
        """Render copyright and legal information"""
        current_year = datetime.datetime.now().year
        
        # Legal links using columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.caption("[Privacy Policy](#privacy)")
        with col2:
            st.caption("[Terms of Service](#terms)")
        with col3:
            st.caption("[Confidentiality](#confidentiality)")
        
        # Copyright notice with clean styling
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; 
                    border-top: 1px solid var(--border); color: var(--text-secondary);">
            <p style="margin: 0;">© {current_year} Laetitia Sheppard • All Rights Reserved</p>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                🔒 All sessions are strictly confidential • Licensed & Insured • Professional Standards Guaranteed
            </p>
        </div>
        """, unsafe_allow_html=True)

class QuickContact:
    """Quick contact widget for floating or sidebar use"""
    
    def __init__(self):
        try:
            from utils.config import AppConstants
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "#")
            self.package_url = AppConstants.CONTACT_INFO.get("package_booking_url", "#")
        except ImportError:
            self.discovery_url = "#"
            self.package_url = "#"
    
    def render_quick_actions(self):
        """Render quick action buttons"""
        st.markdown("### Quick Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📞 Free Call", use_container_width=True, type="primary", key="quick_call"):
                # Scroll to booking form
                st.markdown('<script>document.querySelector("#discovery").scrollIntoView();</script>', 
                          unsafe_allow_html=True)
        
        with col2:
            if st.button("⚡ Book Sessions", use_container_width=True, key="quick_book"):
                st.markdown(f'<meta http-equiv="refresh" content="0; url={self.package_url}">', 
                          unsafe_allow_html=True)

class SocialProofFooter:
    """Social proof elements for footer"""
    
    def render_guarantee(self):
        """Render satisfaction guarantee"""
        st.info("""
        💯 **Satisfaction Guarantee**: If you're not completely satisfied after 2 sessions, 
        your 3rd session is complimentary. Your transformation is our commitment.
        """)

# Factory functions for easy import
def create_footer():
    """Factory function to create Footer instance"""
    return Footer()

def create_quick_contact():
    """Factory function to create QuickContact instance"""
    return QuickContact()

def create_social_proof_footer():
    """Factory function to create SocialProofFooter instance"""
    return SocialProofFooter()
