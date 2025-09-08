# """
# Fixed Booking form component for the Hypnotherapy website
# Final version with all requested changes
# """
# import streamlit as st
# import re
# import smtplib
# import urllib.parse
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# class BookingForm:
#     """Enhanced booking form component with simplified design"""
    
#     def __init__(self):
#         # Try to get config values
#         try:
#             from utils.config import AppConstants
#             self.concern_options = AppConstants.CONCERN_OPTIONS
#             self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
#         except ImportError:
#             self.concern_options = [
#                 "Quit Smoking", 
#                 "Reduce Anxiety", 
#                 "Improve Sleep", 
#                 "Break Bad Habits",
#                 "Weight Management",
#                 "Confidence Building",
#                 "Other"
#             ]
#             self.discovery_url = "https://calendly.com/laetitiasheppard/"
        
#         # WhatsApp number
#         self.whatsapp_number = "+66642439944"
        
#         # Email configuration
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587
#         self.sender_email = "laetitiasheppard@gmail.com"
#         self.recipient_email = "laetitiasheppard@gmail.com"
    
#     def render(self, form_title=None, form_description=None):
#         """Render the booking form"""
#         st.write("### Ready for change?")
        
#         # Simple text message (not info box)
#         st.write("Discover if my proven 2-session approach is right for you. Available in-person (Bangkok) or online.")
               
#         # Benefits of discovery call
#         self._render_benefits()
        
#         # Main form (with white background)
#         self._render_form()
    
#     def _render_benefits(self):
#         """Render benefits of the discovery call with minimized spacing"""
#         benefits_html = """
#         <div style="background: rgba(76, 161, 163, 0.05); border-radius: var(--radius-md);
#                     padding: 1.5rem; margin: 0.5rem 0; border-left: 4px solid var(--accent);">
#             <h3 style="color: var(--accent); margin-bottom: 1rem;">What you'll get in your discovery call:</h3>
#             <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">Personalized assessment of your situation</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">Clear explanation of how hypnotherapy works</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">Honest assessment of your success probability</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">Answers to all your questions</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">No pressure, no obligation</span>
#                 </div>
#                 <div style="display: flex; align-items: center; gap: 0.5rem;">
#                     <span style="color: var(--accent); font-size: 1rem;">✓</span>
#                     <span style="font-size: 1rem; line-height: 1.5;">Next steps if you decide to proceed</span>
#                 </div>
#             </div>
#         </div>
#         """
        
#         st.markdown(benefits_html, unsafe_allow_html=True)
    
#     def _render_form(self):
#         """Render the main booking form with white background and minimized spacing"""        
#         with st.form("discovery_booking_form", clear_on_submit=False):
#             # Form styling with minimized margins
#             st.markdown("""
#             <style>
#             div[data-testid="stForm"] {
#                 background: white !important;
#                 border-radius: var(--radius-md) !important;
#                 padding: 2rem !important;
#                 margin: 0.5rem 0 0.5rem 0 !important;
#                 box-shadow: var(--shadow-sm) !important;
#                 border: 1px solid var(--border) !important;
#             }
#             </style>
#             """, unsafe_allow_html=True)
            
#             # Form fields
#             cols = st.columns(2)
#             with cols[0]:
#                 name = st.text_input(
#                     "Your Name", 
#                     placeholder="First and last name",
#                     key="form_name"
#                 )
#             with cols[1]:
#                 email = st.text_input(
#                     "Email Address*", 
#                     placeholder="your@email.com",
#                     key="form_email"
#                 )
            
#             concern = st.selectbox(
#                 "What would you most like to change?",
#                 [""] + self.concern_options,
#                 key="form_concern"
#             )
            
#             # Enhanced concern description field with guided prompts
#             concern_description = st.text_area(
#                 "Describe your situation", 
#                 placeholder="Tell us more about what you'd like to change. You can include:\n• How long you've been dealing with this\n• How urgent this is for you\n• Any previous experience with hypnotherapy\n• Specific questions or concerns you have",
#                 height=120,
#                 key="form_description"
#             )
            
#             # Form submit button - white with border (no type="primary")
#             form_submitted = st.form_submit_button(
#                 "✅ Click to validate privacy",
#                 use_container_width=True
#             )
            
#             # Handle form submission
#             if form_submitted:
#                 if self._validate_form(email):
#                     # Store form data in session state
#                     st.session_state.form_data = {
#                         'name': name,
#                         'email': email,
#                         'concern': concern,
#                         'description': concern_description
#                     }
#                     # Send email
#                     self._send_booking_email(name, email, concern, concern_description)
#                     # Set flag to trigger calendar opening
#                     st.session_state.trigger_calendar = True
#                     st.success("Choose your option below to start...")
#                     st.rerun()
        
#         # Always visible action buttons below the form with minimized spacing
#         self._render_action_buttons()
        
#         # JavaScript to open calendar when triggered
#         if st.session_state.get('trigger_calendar', False):
#             st.markdown(f"""
#             <script>
#             window.open('{self.discovery_url}', '_blank');
#             </script>
#             """, unsafe_allow_html=True)
#             # Clear the trigger
#             st.session_state.trigger_calendar = False
    
#     def _render_action_buttons(self):
#         """Render action buttons with minimized spacing"""
#         # Get current form data (if any)
#         form_data = st.session_state.get('form_data', {})
#         current_name = st.session_state.get('form_name', '')
#         current_email = st.session_state.get('form_email', '')
#         current_concern = st.session_state.get('form_concern', '')
#         current_description = st.session_state.get('form_description', '')
        
#         # Create WhatsApp message with current form data
#         whatsapp_message = self._create_whatsapp_message(
#             current_name or form_data.get('name', ''),
#             current_email or form_data.get('email', ''),
#             current_concern or form_data.get('concern', ''),
#             current_description or form_data.get('description', '')
#         )
#         encoded_message = urllib.parse.quote(whatsapp_message)
#         whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
#         # Action buttons side by side with minimized spacing
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Direct calendar link button
#             st.markdown(f"""
#             <a href="{self.discovery_url}" target="_blank" 
#                style="display: inline-block; background-color: var(--accent); color: white;
#                       text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
#                       font-weight: 500; font-size: 1rem; transition: var(--transition);
#                       box-shadow: var(--shadow-sm); text-align: center; width: 100%;
#                       box-sizing: border-box; margin-bottom: 0.25rem; border: none;">
#                 📞 Schedule your Session
#             </a>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             # Direct WhatsApp link button - white background with border
#             st.markdown(f"""
#             <a href="{whatsapp_url}" target="_blank" 
#                style="display: inline-block; background-color: white; color: var(--text-primary);
#                       text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
#                       font-weight: 500; font-size: 1rem; transition: var(--transition);
#                       box-shadow: var(--shadow-sm); text-align: center; width: 100%;
#                       box-sizing: border-box; margin-bottom: 0.25rem; border: 2px solid var(--border);">
#                 💬 Message on WhatsApp
#             </a>
#             """, unsafe_allow_html=True)
    
#     def _create_whatsapp_message(self, name, email, concern, concern_description):
#         """Create WhatsApp message from form data"""
#         whatsapp_message = "Hi! I'm interested in booking a discovery call for hypnotherapy."
        
#         if name:
#             whatsapp_message += f" My name is {name}."
        
#         if email:
#             whatsapp_message += f" You can reach me at {email}."
        
#         if concern:
#             whatsapp_message += f" I'm looking for help with: {concern}."
        
#         if concern_description:
#             whatsapp_message += f" Details: {concern_description}."
        
#         return whatsapp_message
    
#     def _validate_form(self, email):
#         """Validate form inputs - only email is required"""
#         errors = []
        
#         if not email.strip():
#             errors.append("Email is required")
#         elif not self._is_valid_email(email):
#             errors.append("Please enter a valid email address")
        
#         if errors:
#             for error in errors:
#                 st.error(f"❌ {error}")
#             return False
        
#         return True
    
#     def _is_valid_email(self, email):
#         """Validate email format"""
#         pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#         return re.match(pattern, email) is not None
    
#     def _send_booking_email(self, name, email, concern, concern_description):
#         """Send booking notification email using Gmail SMTP"""
#         try:
#             # Create message
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = "New Discovery Call Booking Request"
            
#             # Email body
#             body = f"""
#             New Discovery Call Booking Request
            
#             Contact Information:
#             Name: {name if name else 'Not provided'}
#             Email: {email}
            
#             Concerns:
#             Primary Concern: {concern if concern else 'Not specified'}
#             Description: {concern_description if concern_description else 'Not provided'}
            
#             Please contact this person within 24 hours to schedule their discovery call.
#             """
            
#             msg.attach(MIMEText(body, 'plain'))
            
#             # Note: In production, you would need to handle SMTP credentials securely
#             # For now, we'll simulate success
#             print(f"Discovery Call Booking: {name} ({email}) - {concern}")
#             return True
            
#         except Exception as e:
#             print(f"Email sending error: {e}")
#             return False
    
#     def render_compact(self):
#         """Render a compact version of the booking form"""
#         st.markdown("### 📞 Book Your Free Discovery Call")
        
#         with st.form("compact_booking_form"):
#             # White background styling for the form with minimized spacing
#             st.markdown("""
#             <style>
#             div[data-testid="stForm"] {
#                 background: white !important;
#                 border-radius: var(--radius-md) !important;
#                 padding: 1.5rem !important;
#                 margin: 0.5rem 0 0.5rem 0 !important;
#                 box-shadow: var(--shadow-sm) !important;
#                 border: 1px solid var(--border) !important;
#             }
#             </style>
#             """, unsafe_allow_html=True)
            
#             email = st.text_input("Email*", placeholder="your@email.com", key="compact_email")
#             concern = st.selectbox("What would you like to change?", [""] + self.concern_options, key="compact_concern")
#             concern_description = st.text_area(
#                 "Describe your situation", 
#                 placeholder="Brief description including how long you've dealt with this, how urgent it is, and any questions you have",
#                 height=80,
#                 key="compact_description"
#             )
            
#             # Form submit button - white with border (no type="primary")
#             compact_submitted = st.form_submit_button(
#                 "📞 Schedule Call", 
#                 use_container_width=True
#             )
            
#             if compact_submitted:
#                 if email and self._is_valid_email(email):
#                     # Send email and trigger calendar
#                     self._send_booking_email("", email, concern, concern_description)
#                     st.session_state.trigger_compact_calendar = True
#                     st.success("✅ Request submitted successfully! Opening calendar...")
#                     st.rerun()
#                 else:
#                     st.error("Please enter a valid email address.")
        
#         # Always visible action buttons for compact version with minimized spacing
#         self._render_compact_action_buttons()
        
#         # JavaScript to open calendar when triggered
#         if st.session_state.get('trigger_compact_calendar', False):
#             st.markdown(f"""
#             <script>
#             window.open('{self.discovery_url}', '_blank');
#             </script>
#             """, unsafe_allow_html=True)
#             # Clear the trigger
#             st.session_state.trigger_compact_calendar = False
    
#     def _render_compact_action_buttons(self):
#         """Render compact action buttons with minimized spacing"""
#         # Get current form data
#         current_email = st.session_state.get('compact_email', '')
#         current_concern = st.session_state.get('compact_concern', '')
#         current_description = st.session_state.get('compact_description', '')
        
#         # Create WhatsApp message with current form data
#         whatsapp_message = self._create_whatsapp_message(
#             "",
#             current_email,
#             current_concern,
#             current_description
#         )
#         encoded_message = urllib.parse.quote(whatsapp_message)
#         whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Direct calendar link
#             st.markdown(f"""
#                 <a href="{self.discovery_url}" 
#                    target="_blank" 
#                    class="cta-button">
#                    📞 Direct Booking
#                 </a>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             # Direct WhatsApp link - white background with border
#             st.markdown(f"""
#             <a href="{whatsapp_url}" target="_blank" 
#                style="display: inline-block; background-color: white; color: var(--text-primary);
#                       text-decoration: none; padding: 0.8rem 0.5rem; border-radius: var(--radius-sm);
#                       font-weight: 500; font-size: 0.9rem; transition: var(--transition);
#                       box-shadow: var(--shadow-sm); text-align: center; width: 100%;
#                       box-sizing: border-box; margin-bottom: 0.25rem; border: 2px solid var(--border);">
#                 💬 WhatsApp
#             </a>
#             """, unsafe_allow_html=True)

# # Factory function for easy import
# def create_booking_form():
#     """Factory function to create BookingForm instance"""
#     return BookingForm()


"""
Fixed Booking form component for the Hypnotherapy website
Updated to handle package prefills and proper email integration
"""
import streamlit as st
import re
import urllib.parse

class BookingForm:
    """Enhanced booking form component with package prefill and email integration"""
    
    def __init__(self):
        # Try to get config values
        try:
            from utils.config import AppConstants
            self.concern_options = AppConstants.CONCERN_OPTIONS
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
        except ImportError:
            self.concern_options = [
                "Quit Smoking", 
                "Reduce Anxiety", 
                "Improve Sleep", 
                "Break Bad Habits",
                "Weight Management",
                "Confidence Building",
                "Other"
            ]
            self.discovery_url = "https://calendly.com/laetitiasheppard/"
        
        # WhatsApp number
        self.whatsapp_number = "+66642439944"
    
    def render(self, form_title=None, form_description=None):
        """Render the booking form with package prefill support"""
        st.write("### Ready for change?")
        
        # Check if package was selected from method page
        selected_package = st.session_state.get('selected_package')
        if selected_package:
            st.success(f"✨ Package Selected: **{selected_package}**")
        
        st.write("Discover if my proven 2-session approach is right for you. Available in-person (Bangkok) or online.")
               
        # Benefits of discovery call
        self._render_benefits()
        
        # Main form (with white background)
        self._render_form()
    
    def _render_benefits(self):
        """Render benefits of the discovery call with minimized spacing"""
        benefits_html = """
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: var(--radius-md);
                    padding: 1.5rem; margin: 0.5rem 0; border-left: 4px solid var(--accent);">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">What you'll get in your discovery call:</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">Personalized assessment of your situation</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">Clear explanation of how hypnotherapy works</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">Honest assessment of your success probability</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">Answers to all your questions</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">No pressure, no obligation</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1rem;">✓</span>
                    <span style="font-size: 1rem; line-height: 1.5;">Next steps if you decide to proceed</span>
                </div>
            </div>
        </div>
        """
        
        st.markdown(benefits_html, unsafe_allow_html=True)
    
    def _render_form(self):
        """Render the main booking form with white background and package prefill"""
        
        # Get prefill data from session state
        selected_package = st.session_state.get('selected_package', '')
        package_description = st.session_state.get('package_description', '')
        
        with st.form("discovery_booking_form", clear_on_submit=False):
            # Form styling
            st.markdown("""
            <style>
            div[data-testid="stForm"] {
                background: white !important;
                border-radius: var(--radius-md) !important;
                padding: 2rem !important;
                margin: 0.5rem 0 0.5rem 0 !important;
                box-shadow: var(--shadow-sm) !important;
                border: 1px solid var(--border) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Form fields
            cols = st.columns(2)
            with cols[0]:
                name = st.text_input(
                    "Your Name", 
                    placeholder="First and last name",
                    key="form_name"
                )
            with cols[1]:
                email = st.text_input(
                    "Email Address*", 
                    placeholder="your@email.com",
                    key="form_email"
                )
            
            concern = st.selectbox(
                "What would you most like to change?",
                [""] + self.concern_options,
                key="form_concern"
            )
            
            # Prefill description if package was selected
            default_description = ""
            if selected_package and package_description:
                default_description = package_description
            elif not selected_package:
                default_description = ""
            
            concern_description = st.text_area(
                "Describe your situation", 
                value=default_description,
                placeholder="Tell us more about what you'd like to change. You can include:\n• How long you've been dealing with this\n• How urgent this is for you\n• Any previous experience with hypnotherapy\n• Specific questions or concerns you have",
                height=120,
                key="form_description"
            )
            
            # Form submit button
            form_submitted = st.form_submit_button(
                "✅ Click to validate privacy",
                use_container_width=True
            )
            
            # Handle form submission
            if form_submitted:
                if self._validate_form(email):
                    # Prepare data for email
                    booking_data = {
                        'name': name or 'Not provided',
                        'email': email,
                        'concern': concern or 'Not specified',
                        'concern_description': concern_description or 'Not provided',
                        'selected_package': selected_package or 'None',
                        'source': 'Booking Form',
                        'form_type': 'Discovery Call Request'
                    }
                    
                    # Store form data in session state
                    st.session_state.form_data = booking_data
                    
                    # Send email using the email handler
                    if self._send_booking_email(booking_data):
                        st.session_state.email_sent = True
                        st.session_state.trigger_calendar = True
                        st.success("✅ Your request has been sent! Choose your preferred next step below:")
                        
                        # Clear package selection after successful submission
                        if 'selected_package' in st.session_state:
                            del st.session_state['selected_package']
                        if 'package_description' in st.session_state:
                            del st.session_state['package_description']
                            
                        st.rerun()
                    else:
                        st.error("❌ There was an issue sending your request. Please try the direct booking options below.")
        
        # Always visible action buttons below the form
        self._render_action_buttons()
        
        # JavaScript to open calendar when triggered
        if st.session_state.get('trigger_calendar', False):
            st.markdown(f"""
            <script>
            window.open('{self.discovery_url}', '_blank');
            </script>
            """, unsafe_allow_html=True)
            # Clear the trigger
            st.session_state.trigger_calendar = False
    
    def _render_action_buttons(self):
        """Render action buttons with current form data"""
        # Get current form data
        form_data = st.session_state.get('form_data', {})
        current_name = st.session_state.get('form_name', '')
        current_email = st.session_state.get('form_email', '')
        current_concern = st.session_state.get('form_concern', '')
        current_description = st.session_state.get('form_description', '')
        
        # Create WhatsApp message with current form data
        whatsapp_message = self._create_whatsapp_message(
            current_name or form_data.get('name', ''),
            current_email or form_data.get('email', ''),
            current_concern or form_data.get('concern', ''),
            current_description or form_data.get('concern_description', '')
        )
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        # Action buttons side by side
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: none;">
                📞 Schedule your Session
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: white; color: var(--text-primary);
                      text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: 2px solid var(--border);">
                💬 Message on WhatsApp
            </a>
            """, unsafe_allow_html=True)
    
    def _create_whatsapp_message(self, name, email, concern, concern_description):
        """Create WhatsApp message from form data"""
        whatsapp_message = "Hi! I'm interested in booking a discovery call for hypnotherapy."
        
        if name:
            whatsapp_message += f" My name is {name}."
        
        if email:
            whatsapp_message += f" You can reach me at {email}."
        
        if concern:
            whatsapp_message += f" I'm looking for help with: {concern}."
        
        if concern_description:
            whatsapp_message += f" Details: {concern_description}."
        
        return whatsapp_message
    
    def _validate_form(self, email):
        """Validate form inputs - only email is required"""
        errors = []
        
        if not email.strip():
            errors.append("Email is required")
        elif not self._is_valid_email(email):
            errors.append("Please enter a valid email address")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _is_valid_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _send_booking_email(self, booking_data):
        """Send booking notification email using the email handler"""
        try:
            # Import email handler
            from utils.email_handler import send_discovery_call_email
            
            # Send email using the centralized email handler
            success = send_discovery_call_email(booking_data)
            
            if success:
                print(f"[SUCCESS] Booking email sent for: {booking_data.get('email', 'Unknown')}")
            else:
                print(f"[ERROR] Failed to send booking email for: {booking_data.get('email', 'Unknown')}")
            
            return success
            
        except ImportError:
            print("[ERROR] Email handler not available")
            return False
        except Exception as e:
            print(f"[ERROR] Unexpected error sending booking email: {e}")
            return False
    
    def render_compact(self):
        """Render a compact version of the booking form"""
        st.markdown("### 📞 Book Your Free Discovery Call")
        
        with st.form("compact_booking_form"):
            st.markdown("""
            <style>
            div[data-testid="stForm"] {
                background: white !important;
                border-radius: var(--radius-md) !important;
                padding: 1.5rem !important;
                margin: 0.5rem 0 0.5rem 0 !important;
                box-shadow: var(--shadow-sm) !important;
                border: 1px solid var(--border) !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            email = st.text_input("Email*", placeholder="your@email.com", key="compact_email")
            concern = st.selectbox("What would you like to change?", [""] + self.concern_options, key="compact_concern")
            concern_description = st.text_area(
                "Describe your situation", 
                placeholder="Brief description including how long you've dealt with this, how urgent it is, and any questions you have",
                height=80,
                key="compact_description"
            )
            
            compact_submitted = st.form_submit_button(
                "📞 Schedule Call", 
                use_container_width=True
            )
            
            if compact_submitted:
                if email and self._is_valid_email(email):
                    booking_data = {
                        'name': 'Not provided',
                        'email': email,
                        'concern': concern or 'Not specified',
                        'concern_description': concern_description or 'Not provided',
                        'selected_package': 'None',
                        'source': 'Compact Booking Form',
                        'form_type': 'Compact Discovery Call Request'
                    }
                    
                    if self._send_booking_email(booking_data):
                        st.session_state.trigger_compact_calendar = True
                        st.success("✅ Request submitted successfully! Opening calendar...")
                        st.rerun()
                    else:
                        st.error("❌ Unable to send request. Please try the direct links below.")
                else:
                    st.error("Please enter a valid email address.")
        
        # Always visible action buttons for compact version
        self._render_compact_action_buttons()
        
                    # JavaScript to open calendar when triggered
        if st.session_state.get('trigger_compact_calendar', False):
            st.markdown(f"""
            <script>
            window.open('{self.discovery_url}', '_blank');
            </script>
            """, unsafe_allow_html=True)
            # Clear the trigger
            st.session_state.trigger_compact_calendar = False
    
    def _render_compact_action_buttons(self):
        """Render compact action buttons with minimized spacing"""
        # Get current form data
        current_email = st.session_state.get('compact_email', '')
        current_concern = st.session_state.get('compact_concern', '')
        current_description = st.session_state.get('compact_description', '')
        
        # Create WhatsApp message with current form data
        whatsapp_message = self._create_whatsapp_message(
            "",
            current_email,
            current_concern,
            current_description
        )
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 0.8rem 0.5rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 0.9rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: none;">
                📞 Direct Booking
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: white; color: var(--text-primary);
                      text-decoration: none; padding: 0.8rem 0.5rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 0.9rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: 2px solid var(--border);">
                💬 WhatsApp
            </a>
            """, unsafe_allow_html=True)

# Factory function for easy import
def create_booking_form():
    """Factory function to create BookingForm instance"""
    return BookingForm()
