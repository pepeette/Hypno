# """
# Booking Form Component
# Professional booking form using Streamlit components with validation
# """
# import streamlit as st
# import re
# from utils.config import FormConfig
# from utils.session_state import update_user_data, set_form_success, set_form_errors

# class BookingForm:
#     """Professional booking form using native Streamlit components"""
    
#     def __init__(self):
#         self.concern_options = FormConfig.CONCERN_OPTIONS
#         self.urgency_options = FormConfig.URGENCY_OPTIONS
#         self.experience_options = FormConfig.EXPERIENCE_OPTIONS
    
#     def render(self):
#         """Render the main booking form"""
#         st.markdown("## Book Your Free Discovery Call")
#         st.write("Begin your transformation with a complimentary 15-minute consultation")
        
#         # Benefits section using Streamlit components
#         self._render_benefits()
        
#         # Main booking form
#         self._render_main_form()
    
#     def render_compact(self):
#         """Render compact version for footer/sidebar"""
#         st.markdown("### Ready to Transform Your Life?")
#         st.write("Start with a free 15-minute discovery call")
        
#         with st.form("compact_booking_form"):
#             # Basic form fields
#             col1, col2 = st.columns(2)
#             with col1:
#                 name = st.text_input("Name*", placeholder="Your name")
#             with col2:
#                 email = st.text_input("Email*", placeholder="your@email.com")
            
#             concern = st.selectbox("Primary Concern*", self.concern_options)
            
#             submitted = st.form_submit_button(
#                 "Request Free Discovery Call",
#                 type="primary",
#                 use_container_width=True
#             )
            
#             if submitted:
#                 if self._validate_basic_form(name, email, concern):
#                     self._handle_form_submission(name, email, concern, "")
    
#     def _render_benefits(self):
#         """Render benefits using Streamlit components"""
#         st.markdown("### What You'll Get in Your Discovery Call")
        
#         # Benefits using columns
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.write("✓ Personalized assessment of your situation")
#             st.write("✓ Clear explanation of how hypnotherapy works")
#             st.write("✓ Honest assessment of your success probability")
        
#         with col2:
#             st.write("✓ Answers to all your questions")
#             st.write("✓ No pressure, no obligation")
#             st.write("✓ Next steps if you decide to proceed")
    
#     def _render_main_form(self):
#         """Render the main booking form using Streamlit form"""
#         with st.form("discovery_booking_form"):
#             # Personal information section
#             st.markdown("#### 👤 Personal Information")
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 name = st.text_input(
#                     "Your Name*",
#                     placeholder="First and last name",
#                     help="We'll use this to personalize your session"
#                 )
#             with col2:
#                 email = st.text_input(
#                     "Email Address*",
#                     placeholder="your@email.com",
#                     help="For session confirmations and resources"
#                 )
            
#             col3, col4 = st.columns(2)
#             with col3:
#                 phone = st.text_input(
#                     "Phone Number (Optional)",
#                     placeholder="+66 XX XXX XXXX",
#                     help="For quicker communication if needed"
#                 )
#             with col4:
#                 contact_method = st.selectbox(
#                     "Preferred Contact Method*",
#                     ["Phone call", "Video call (Zoom)", "Email first"],
#                     help="How would you like us to reach you?"
#                 )
            
#             # Situation assessment section
#             st.markdown("#### 🎯 Your Situation")
            
#             concern = st.selectbox(
#                 "What would you most like to change?*",
#                 self.concern_options,
#                 help="This helps us prepare for your call"
#             )
            
#             col5, col6 = st.columns(2)
#             with col5:
#                 urgency = st.selectbox(
#                     "How urgent is this for you?*",
#                     self.urgency_options,
#                     help="Helps us prioritize scheduling"
#                 )
#             with col6:
#                 experience = st.selectbox(
#                     "Previous hypnotherapy experience?",
#                     self.experience_options,
#                     help="Helps us tailor our explanation"
#                 )
            
#             message = st.text_area(
#                 "Tell us more about your situation",
#                 placeholder="Optional: Any specific details, questions, or concerns you'd like to discuss",
#                 help="This helps us make the most of your 15 minutes",
#                 height=100
#             )
            
#             # Preferences section
#             st.markdown("#### ⏰ Scheduling Preferences")
            
#             col7, col8 = st.columns(2)
#             with col7:
#                 time_preference = st.selectbox(
#                     "Preferred Time of Day",
#                     ["No preference", "Morning (9AM-12PM)", "Afternoon (12PM-5PM)", "Evening (5PM-8PM)"],
#                     help="Bangkok time (UTC+7)"
#                 )
#             with col8:
#                 day_preference = st.selectbox(
#                     "Preferred Days",
#                     ["Any day works", "Weekdays only", "Weekends only", "Specific days (mention above)"]
#                 )
            
#             # Consent section using Streamlit checkbox
#             st.markdown("#### 🔒 Privacy & Consent")
            
#             consent = st.checkbox(
#                 "I consent to being contacted about hypnotherapy services and understand all information will be kept strictly confidential",
#                 help="Required to proceed with booking"
#             )
            
#             newsletter = st.checkbox(
#                 "I'd like to receive helpful tips about transformation and wellness (optional)"
#             )
            
#             # Submit button
#             submitted = st.form_submit_button(
#                 "📞 Schedule My Free Discovery Call",
#                 type="primary",
#                 use_container_width=True,
#                 help="We'll contact you within 24 hours"
#             )
            
#             if submitted:
#                 form_data = {
#                     'name': name,
#                     'email': email,
#                     'phone': phone,
#                     'contact_method': contact_method,
#                     'concern': concern,
#                     'urgency': urgency,
#                     'experience': experience,
#                     'message': message,
#                     'time_preference': time_preference,
#                     'day_preference': day_preference,
#                     'consent': consent,
#                     'newsletter': newsletter
#                 }
                
#                 if self._validate_discovery_form(form_data):
#                     self._handle_discovery_submission(form_data)
    
#     def _validate_basic_form(self, name, email, concern):
#         """Basic validation for compact form"""
#         errors = []
        
#         if not name.strip():
#             errors.append("Name is required")
        
#         if not email.strip():
#             errors.append("Email is required")
#         elif not self._is_valid_email(email):
#             errors.append("Please enter a valid email address")
        
#         if not concern or concern.startswith("Select"):
#             errors.append("Please select your primary concern")
        
#         if errors:
#             for error in errors:
#                 st.error(f"❌ {error}")
#             return False
        
#         return True
    
#     def _validate_discovery_form(self, form_data):
#         """Comprehensive validation for discovery form"""
#         errors = []
        
#         # Required field validation
#         if not form_data['name'].strip():
#             errors.append("Name is required")
        
#         if not form_data['email'].strip():
#             errors.append("Email is required")
#         elif not self._is_valid_email(form_data['email']):
#             errors.append("Please enter a valid email address")
        
#         if not form_data['concern'] or form_data['concern'].startswith("Select"):
#             errors.append("Please select your primary concern")
        
#         if not form_data['urgency'] or form_data['urgency'].startswith("How urgent"):
#             errors.append("Please indicate urgency level")
        
#         if not form_data['consent']:
#             errors.append("Please consent to being contacted")
        
#         # Phone validation if provided
#         if form_data['phone'] and not self._is_valid_phone(form_data['phone']):
#             errors.append("Please enter a valid phone number")
        
#         if errors:
#             for error in errors:
#                 st.error(f"❌ {error}")
#             return False
        
#         return True
    
#     def _is_valid_email(self, email):
#         """Validate email format"""
#         pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#         return re.match(pattern, email) is not None
    
#     def _is_valid_phone(self, phone):
#         """Validate phone number format"""
#         cleaned = re.sub(r'[\s\-\(\)\+]', '', phone)
#         return len(cleaned) >= 8 and len(cleaned) <= 15 and cleaned.isdigit()
    
#     def _handle_form_submission(self, name, email, concern, message):
#         """Handle basic form submission"""
#         try:
#             # Update user data in session state
#             update_user_data(name=name, email=email, concern=concern)
            
#             # Simulate email sending (replace with actual implementation)
#             success = self._send_booking_email({
#                 'name': name,
#                 'email': email,
#                 'concern': concern,
#                 'message': message
#             })
            
#             if success:
#                 set_form_success(True)
#                 st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
#                 st.balloons()
#             else:
#                 st.error("❌ There was an issue. Please try again or contact us directly.")
                
#         except Exception as e:
#             st.error(f"❌ An error occurred: {str(e)}")
    
#     def _handle_discovery_submission(self, form_data):
#         """Handle comprehensive discovery form submission"""
#         try:
#             # Update user data
#             update_user_data(
#                 name=form_data['name'],
#                 email=form_data['email'],
#                 concern=form_data['concern'],
#                 phone=form_data['phone']
#             )
            
#             # Send detailed booking email
#             success = self._send_discovery_email(form_data)
            
#             if success:
#                 set_form_success(True)
#                 self._render_success_message(form_data['name'])
#             else:
#                 st.error("❌ There was an issue. Please try again or contact us directly.")
                
#         except Exception as e:
#             st.error(f"❌ An error occurred: {str(e)}")
    
#     def _send_booking_email(self, data):
#         """Send booking notification email (implement with actual service)"""
#         # Placeholder for email implementation
#         print(f"Booking: {data}")
#         return True
    
#     def _send_discovery_email(self, data):
#         """Send detailed discovery call booking email"""
#         # Placeholder for email implementation
#         print(f"Discovery Call: {data}")
#         return True
    
#     def _render_success_message(self, name):
#         """Render success message using Streamlit components"""
#         st.success(f"✅ Thank you, {name}! Your discovery call request has been submitted.")
        
#         # Next steps using info box
#         st.info("""
#         **What happens next:**
        
#         1. **Check your email** for confirmation
#         2. **We'll contact you** within 24 hours to schedule
#         3. **Your discovery call** where we assess your situation
#         4. **Next steps** if you decide to proceed
#         """)
        
#         # Direct scheduling option
#         st.markdown("### Or Schedule Directly")
#         if st.button("📅 Choose Your Time Slot", type="primary", use_container_width=True):
#             st.success("Opening calendar...")
        
#         st.balloons()

# # Factory function for easy import
# def create_booking_form():
#     """Create BookingForm instance"""
#     return BookingForm()

"""
Enhanced Booking form component for the Hypnotherapy website
Improved with optional name, WhatsApp integration, and email functionality
"""
import streamlit as st
import re
import smtplib
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BookingForm:
    """Enhanced booking form component with email and WhatsApp integration"""
    
    def __init__(self):
        # Try to get config values
        try:
            from utils.config import AppConstants
            self.concern_options = AppConstants.CONCERN_OPTIONS
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/30min")
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
            self.discovery_url = "https://calendly.com/laetitiasheppard/30min"
        
        # WhatsApp number
        self.whatsapp_number = "+66642439944"
        
        # Email configuration
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "laetitiasheppard@gmail.com"
        self.recipient_email = "laetitiasheppard@gmail.com"
    
    def render(self, form_title="Free 15-Minute Discovery Call", form_description=None):
        """Render the booking form"""
        # Default description if none provided
        if form_description is None:
            form_description = "Begin your journey to transformation with a complimentary consultation"
        
        st.markdown('<div id="discovery"></div>', unsafe_allow_html=True)
        
        form_html = f"""
        <div class="card">
            <h1 style="text-align: center; color: var(--accent); margin-bottom: 1rem;">
                {form_title}
            </h1>
            <p style="text-align: center; color: var(--text-secondary); margin-bottom: 2rem;">
                {form_description}
            </p>
        </div>
        """
        
        st.markdown(form_html, unsafe_allow_html=True)
        
        # Benefits of discovery call
        self._render_benefits()
        
        # Main form
        self._render_form()
    
    def _render_benefits(self):
        """Render benefits of the discovery call"""
        benefits_html = """
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: var(--radius-md);
                    padding: 1.5rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">What You'll Get in Your Discovery Call:</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>Personalized assessment of your situation</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>Clear explanation of how hypnotherapy works</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>Honest assessment of your success probability</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>Answers to all your questions</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>No pressure, no obligation</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--accent); font-size: 1.2rem;">✓</span>
                    <span>Next steps if you decide to proceed</span>
                </div>
            </div>
        </div>
        """
        
        st.markdown(benefits_html, unsafe_allow_html=True)
    
    def _render_form(self):
        """Render the main booking form"""
        with st.form("discovery_booking_form", clear_on_submit=False):
            # Form fields
            cols = st.columns(2)
            with cols[0]:
                name = st.text_input(
                    "Your Name (Optional)", 
                    placeholder="First and last name",
                    help="We'll use this to personalize your session"
                )
            with cols[1]:
                email = st.text_input(
                    "Email Address*", 
                    placeholder="your@email.com",
                    help="Required for session confirmations and resources"
                )
            
            concern = st.selectbox(
                "What would you most like to change? (Optional)",
                [""] + self.concern_options,
                help="This helps us prepare for your call"
            )
            
            # New concern description field
            concern_description = st.text_area(
                "Describe your situation (Optional)", 
                placeholder="Tell us more about what you'd like to change or any specific challenges you're facing",
                help="This helps us understand your unique situation better",
                height=100
            )
            
            # Additional context
            cols2 = st.columns(2)
            with cols2[0]:
                urgency = st.selectbox(
                    "How urgent is this for you?",
                    ["Not specified", "Very urgent - need help now", "Somewhat urgent - within a month", 
                     "Not urgent - just exploring", "Flexible timing"],
                    help="Helps us prioritize scheduling"
                )
            
            with cols2[1]:
                experience = st.selectbox(
                    "Previous experience with hypnotherapy?",
                    ["No previous experience", "Some experience", "Experienced", "Prefer not to say"],
                    help="Helps us tailor our explanation"
                )
            
            message = st.text_area(
                "Additional questions or comments (Optional)", 
                placeholder="Any specific questions, concerns, or background information you'd like to share",
                help="This helps us make the most of your 15 minutes"
            )
            
            # Preferred contact method
            contact_method = st.radio(
                "Preferred session format:",
                ["Video call (Zoom)", "Phone call", "In-person (Bangkok)", "No preference"],
                horizontal=True
            )
            
            # Submit button for email form
            submitted = st.form_submit_button(
                "📞 Schedule My Free Discovery Call", 
                type="primary", 
                use_container_width=True
            )
            
            if submitted:
                if self._validate_form(email):
                    self._handle_form_submission(name, email, concern, concern_description, urgency, experience, message, contact_method)
        
        # WhatsApp button outside form for direct action
        self._render_whatsapp_button(name, email, concern, concern_description, message)
    
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
    
    def _handle_form_submission(self, name, email, concern, concern_description, urgency, experience, message, contact_method):
        """Handle successful form submission"""
        # Try to send email
        if self._send_booking_email(name, email, concern, concern_description, urgency, experience, message, contact_method):
            # Success state
            self._render_success_state(name if name else "")
        else:
            # Error state
            st.error("❌ There was an issue submitting your request. Please try again or contact us directly.")
    
    def _send_booking_email(self, name, email, concern, concern_description, urgency, experience, message, contact_method):
        """Send booking notification email using Gmail SMTP"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "New Discovery Call Booking Request"
            
            # Email body
            body = f"""
            New Discovery Call Booking Request
            
            Contact Information:
            Name: {name if name else 'Not provided'}
            Email: {email}
            
            Concerns:
            Primary Concern: {concern if concern else 'Not specified'}
            Description: {concern_description if concern_description else 'Not provided'}
            
            Additional Information:
            Urgency: {urgency}
            Previous Experience: {experience}
            Preferred Contact Method: {contact_method}
            Additional Message: {message if message else 'None'}
            
            Please contact this person within 24 hours to schedule their discovery call.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Note: In production, you would need to handle SMTP credentials securely
            # For now, we'll simulate success
            print(f"Discovery Call Booking: {name} ({email}) - {concern}")
            return True
            
        except Exception as e:
            print(f"Email sending error: {e}")
            return False
    
    def _render_whatsapp_button(self, name, email, concern, concern_description, message):
        """Render WhatsApp button that opens directly"""
        # Create WhatsApp message
        whatsapp_message = "Hi! I'm interested in booking a discovery call for hypnotherapy."
        
        if name:
            whatsapp_message += f" My name is {name}."
        
        if email:
            whatsapp_message += f" You can reach me at {email}."
        
        if concern:
            whatsapp_message += f" I'm looking for help with: {concern}."
        
        if concern_description:
            whatsapp_message += f" Details: {concern_description}."
        
        if message:
            whatsapp_message += f" Additional info: {message}."
        
        # Encode message for URL
        encoded_message = urllib.parse.quote(whatsapp_message)
        
        # Create WhatsApp URL
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        # Render WhatsApp button with direct link
        st.markdown(f"""
        <div style="text-align: center; margin: 1rem 0;">
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: #25D366; color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; min-width: 200px;">
                💬 Message on WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    def _handle_whatsapp_contact(self, name, email, concern, concern_description, message):
        """Handle WhatsApp contact - now unused, keeping for compatibility"""
        pass
    
    def _render_success_state(self, name):
        """Render success state after form submission"""
        success_name = name if name else "there"
        
        success_html = f"""
        <div style="background: rgba(34, 197, 94, 0.1); border: 2px solid var(--success);
                    border-radius: var(--radius-md); padding: 2rem; text-align: center; margin: 2rem 0;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
            <h2 style="color: var(--success); margin-bottom: 1rem;">Discovery Call Scheduled!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">
                Thank you{', ' + name if name else ''}! We've received your request and will contact you within 24 hours 
                to schedule your free discovery call.
            </p>
            <div style="background: white; border-radius: var(--radius-sm); padding: 1.5rem; margin: 1rem 0;">
                <h3 style="color: var(--text-primary); margin-bottom: 1rem;">What Happens Next:</h3>
                <div style="text-align: left; max-width: 400px; margin: 0 auto;">
                    <div style="margin-bottom: 0.8rem;">📧 <strong>Step 1:</strong> Check your email for confirmation</div>
                    <div style="margin-bottom: 0.8rem;">📞 <strong>Step 2:</strong> We'll contact you to schedule</div>
                    <div style="margin-bottom: 0.8rem;">🎯 <strong>Step 3:</strong> Your 15-minute discovery call</div>
                    <div style="margin-bottom: 0.8rem;">⚡ <strong>Step 4:</strong> Decide on next steps together</div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(success_html, unsafe_allow_html=True)
        
        # Calendar link with proper styling
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                Or schedule directly using our calendar:
            </p>
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1.1rem; transition: var(--transition);
                      box-shadow: var(--shadow-accent);">
                📅 Choose Your Time Slot
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Show balloons animation
        st.balloons()
    
    def render_compact(self):
        """Render a compact version of the booking form"""
        st.markdown("### 📞 Book Your Free Discovery Call")
        
        with st.form("compact_booking_form"):
            email = st.text_input("Email*", placeholder="your@email.com")
            concern = st.selectbox("Primary Concern (Optional)", [""] + self.concern_options)
            concern_description = st.text_area(
                "Describe your situation (Optional)", 
                placeholder="Brief description of what you'd like to change",
                height=80
            )
            
            submitted = st.form_submit_button("Schedule Call", type="primary", use_container_width=True)
            
            if submitted:
                if email and self._is_valid_email(email):
                    if self._send_booking_email("", email, concern, concern_description, "Not specified", "Not specified", "", "No preference"):
                        st.success("✅ Request submitted! We'll contact you within 24 hours.")
                        st.markdown(f"""
                        <a href="{self.discovery_url}" target="_blank" 
                           style="display: block; background-color: var(--accent); color: white;
                                  text-decoration: none; padding: 0.8rem; border-radius: var(--radius-sm);
                                  font-weight: 600; text-align: center; margin-top: 1rem;">
                            📅 Or Schedule Directly
                        </a>
                        """, unsafe_allow_html=True)
                else:
                    st.error("Please enter a valid email address.")
        
        # Direct WhatsApp button for compact form
        self._render_compact_whatsapp_button()
    
    def _render_compact_whatsapp_button(self):
        """Render compact WhatsApp button with direct action"""
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text=Hi! I'm interested in booking a discovery call for hypnotherapy."
        
        st.markdown(f"""
        <div style="text-align: center; margin: 1rem 0;">
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: #25D366; color: white;
                      text-decoration: none; padding: 0.8rem 1.5rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm);">
                💬 WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)

# Factory function for easy import
def create_booking_form():
    """Factory function to create BookingForm instance"""
    return BookingForm()
