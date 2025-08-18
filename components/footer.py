# """
# Footer Component
# Professional footer with founder info, contact details, and credentials
# Using Streamlit components instead of complex HTML
# """
# import streamlit as st
# import datetime
# from utils.config import AppConfig, get_years_of_experience

# class Footer:
#     """Professional footer component using Streamlit elements"""
    
#     def __init__(self):
#         self.config = AppConfig()
    
#     def render(self):
#         """Render the complete footer using Streamlit components"""
#         st.markdown("---")
        
#         # Main footer content
#         self._render_main_footer()
        
#         # Trust indicators
#         self._render_trust_indicators()
        
#         # Copyright
#         self._render_copyright()
    
#     def _render_main_footer(self):
#         """Render main footer content using Streamlit columns"""
#         col1, col2 = st.columns([2, 1], gap="large")
        
#         with col1:
#             self._render_founder_section()
        
#         with col2:
#             self._render_contact_section()
    
#     def _render_founder_section(self):
#         """Render founder information using Streamlit components"""
#         # Founder image and info
#         col_img, col_text = st.columns([1, 3])
        
#         with col_img:
#             st.image(
#                 AppConfig.FOUNDER_IMAGE,
#                 width=100,
#                 caption="Laetitia Sheppard"
#             )
        
#         with col_text:
#             st.markdown("### Laetitia Sheppard")
#             st.write("Certified Clinical Hypnotherapist")
#             st.write(f"Practice established {AppConfig.PRACTICE_ESTABLISHED}")
            
#             # Credentials
#             st.markdown("**Certifications:**")
#             st.write(f"• LCCH Certified {AppConfig.LCCH_CERTIFICATION}")
#             st.write(f"• DBT Certified {AppConfig.DBT_CERTIFICATION}")
#             st.write(f"• {get_years_of_experience()}+ years experience")
    
#     def _render_contact_section(self):
#         """Render contact information using Streamlit components"""
#         st.markdown("### Contact Information")
        
#         # Clinic details
#         st.write(f"**{AppConfig.PRACTICE_NAME}**")
#         st.write(AppConfig.CLINIC_ADDRESS)
#         st.write(AppConfig.CLINIC_CITY)
        
#         # Session options
#         st.markdown("**Session Options:**")
#         st.write("• In-person (Bangkok clinic)")
#         st.write("• Online (worldwide via Zoom)")
#         st.write("• Home visits (Bangkok area)")
        
#         # Action buttons using Streamlit
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("📍 Get Directions", use_container_width=True):
#                 st.success("Opening maps...")
#                 # In production: st.link_button or redirect
        
#         with col2:
#             if st.button("📅 Book Now", use_container_width=True, type="primary"):
#                 st.success("Scroll up to book!")
    
#     def _render_trust_indicators(self):
#         """Render trust badges using Streamlit metrics"""
#         st.markdown("### 🏆 Professional Standards")
        
#         col1, col2, col3, col4 = st.columns(4)
        
#         with col1:
#             st.metric(
#                 "Certified",
#                 "LCCH",
#                 f"Since {AppConfig.LCCH_CERTIFICATION}",
#                 help="London College of Clinical Hypnotherapy"
#             )
        
#         with col2:
#             st.metric(
#                 "Licensed",
#                 "Insured",
#                 "Professional",
#                 help="Professional indemnity insurance"
#             )
        
#         with col3:
#             st.metric(
#                 "Experience",
#                 f"{get_years_of_experience()}+ years",
#                 "Established practice",
#                 help=f"Practice established {AppConfig.PRACTICE_ESTABLISHED}"
#             )
        
#         with col4:
#             st.metric(
#                 "Success Rate",
#                 "85%",
#                 "2 sessions",
#                 help="85% of clients achieve goals in 2 sessions"
#             )
        
#         # Guarantee
#         st.success("💯 Satisfaction Guarantee: Not satisfied after 2 sessions? 3rd session is complimentary.")
    
#     def _render_copyright(self):
#         """Render copyright using Streamlit components"""
#         current_year = datetime.datetime.now().year
        
#         # Legal links using columns
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.caption("Privacy Policy")
#         with col2:
#             st.caption("Terms of Service")
#         with col3:
#             st.caption("Confidentiality Agreement")
        
#         # Copyright notice
#         st.markdown(f"""
#         <div style="text-align: center; margin-top: 2rem; color: #556D7A;">
#             © {current_year} {AppConfig.PRACTITIONER_NAME} • All Rights Reserved<br>
#             🔒 All sessions strictly confidential • Licensed & Insured • Professional Standards Guaranteed
#         </div>
#         """, unsafe_allow_html=True)

# class QuickContact:
#     """Quick contact component for floating or emergency use"""
    
#     def render_emergency_notice(self):
#         """Render emergency contact notice"""
#         st.error("""
#         🚨 **Crisis Support**: If you're experiencing a mental health crisis, 
#         please contact emergency services immediately. Our services are for 
#         transformation and improvement, not crisis intervention.
#         """)
    
#     def render_quick_actions(self):
#         """Render quick action buttons"""
#         st.markdown("### Quick Actions")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             if st.button("📞 Free Discovery Call", type="primary", use_container_width=True):
#                 st.success("Scroll up to book your call!")
        
#         with col2:
#             if st.button("🎯 Take Assessment", use_container_width=True):
#                 st.success("Scroll up to start the quiz!")

# # Factory function for easy import
# def create_footer():
#     """Create Footer instance"""
#     return Footer()


"""
Clean footer component for the Hypnotherapy website
"""
import streamlit as st
import datetime

class Footer:
    """Simple, clean footer component"""
    
    def __init__(self):
        # Contact info and image URL
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
        st.markdown("---")
        
        # Main footer content
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Founder section
            col_img, col_text = st.columns([1, 3])
            
            with col_img:
                st.image(self.founder_image, width=100)
            
            with col_text:
                st.markdown("### Laetitia Sheppard")
                st.write("Certified Clinical Hypnotherapist")
                st.write("LCCH Certified 2017 • DBT Certified 2023")
                st.write("10+ years experience helping people transform their lives")
        
        with col2:
            # Contact section
            st.markdown("### Contact")
            st.write(f"**{self.contact_info['clinic_name']}**")
            st.write(f"{self.contact_info['address']}")
            st.write(f"{self.contact_info['city']}")
            st.write("")
            st.write("**Session Options:**")
            st.write("• In-person (Bangkok clinic)")
            st.write("• Online (worldwide)")
            st.write("• Home visits (Bangkok area)")
            
            # Action buttons
            if st.button("📍 Get Directions", use_container_width=True):
                st.markdown(f"[Open Maps]({self.contact_info['maps_url']})")
            
            if st.button("📅 Book Now", use_container_width=True, type="primary"):
                st.markdown(f"[Schedule Call]({self.contact_info['calendly_url']})")
        
        # Copyright section
        current_year = datetime.datetime.now().year
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; 
                    border-top: 1px solid var(--border); color: var(--text-secondary);">
            <p>© {current_year} Laetitia Sheppard • All Rights Reserved</p>
            <p style="font-size: 0.9rem;">
                🔒 All sessions are strictly confidential • Licensed & Insured • Professional Standards Guaranteed
            </p>
        </div>
        """, unsafe_allow_html=True)

class BookingForm:
    """Clean booking form component"""
    
    def __init__(self):
        self.concern_options = [
            "Select one...", 
            "Quit Smoking", 
            "Reduce Anxiety", 
            "Improve Sleep", 
            "Break Bad Habits",
            "Other"
        ]
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
    
    def render(self):
        """Render the booking form"""
        st.markdown("---")
        st.markdown("## 📞 Book Your Free Discovery Call")
        st.write("Begin your transformation with a complimentary 15-minute consultation")
        
        # Benefits of discovery call
        st.markdown("""
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: 12px;
                    padding: 1.5rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
            <h3 style="color: var(--accent);">What You'll Get in Your Discovery Call:</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <div>✓ Personalized assessment of your situation</div>
                <div>✓ Clear explanation of how hypnotherapy works</div>
                <div>✓ Honest assessment of your success probability</div>
                <div>✓ Answers to all your questions</div>
                <div>✓ No pressure, no obligation</div>
                <div>✓ Next steps if you decide to proceed</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Booking form
        with st.form("discovery_booking_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Your Name*", placeholder="First and last name")
            with col2:
                email = st.text_input("Email*", placeholder="your@email.com")
            
            concern = st.selectbox("What would you most like to change?*", self.concern_options)
            
            message = st.text_area(
                "Anything specific you'd like to discuss?", 
                placeholder="Optional: Any questions, concerns, or background information"
            )
            
            submitted = st.form_submit_button("📞 Schedule My Free Discovery Call", type="primary", use_container_width=True)
            
            if submitted:
                if self._validate_form(name, email, concern):
                    st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
                    st.markdown(f"""
                    <div style="text-align: center; margin: 2rem 0;">
                        <a href="{self.discovery_url}" target="_blank" 
                           style="display: inline-block; background-color: var(--accent); color: white;
                                  text-decoration: none; padding: 1rem 2rem; border-radius: 8px;
                                  font-weight: 600;">
                            📅 Or Choose Your Time Slot Directly
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.error("Please fill in all required fields with valid information.")
    
    def _validate_form(self, name, email, concern):
        """Simple form validation"""
        if not name or not email or concern == "Select one...":
            return False
        
        # Basic email validation
        if "@" not in email or "." not in email:
            return False
        
        return True

# Factory functions
def create_footer():
    return Footer()

def create_booking_form():
    return BookingForm()
