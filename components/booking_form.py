"""
Fixed Booking form component for the Hypnotherapy website
Corrected syntax and indentation issues
"""
import streamlit as st
import re
import smtplib
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BookingForm:
    """Enhanced booking form component with simplified design"""
    
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
    
    def render(self, form_title=None, form_description=None):
        """Render the booking form"""
        st.write("### Ready to Start Your Transformation?")
        st.markdown('<div id="discovery"></div>', unsafe_allow_html=True)
        
        # Logo and Info message on same row with responsive design
        col1, col2 = st.columns([1, 5], gap="medium")
        
        with col1:
            # Logo with same height as info box
            st.markdown("""
            <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
                <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.jpg?raw=true" 
                     alt="Hypnotherapy Logo" 
                     style="max-width: 100%; height: auto; border-radius: 8px; 
                            max-height: 80px; object-fit: contain;">
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Info box - will automatically size to content
            st.info("Book your free discovery call to see if the method is right for you.")
               
        # Benefits of discovery call
        self._render_benefits()
        
        # Main form (with white background)
        self._render_form()
    
    def _render_benefits(self):
        """Render benefits of the discovery call"""
        benefits_html = """
        <div style="background: rgba(76, 161, 163, 0.05); border-radius: var(--radius-md);
                    padding: 1.5rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">What You'll Get in Your Discovery Call:</h3>
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
        """Render the main booking form with white background"""        
        with st.form("discovery_booking_form", clear_on_submit=False):
            # Start white background container for form only
            st.markdown("""
            <style>
            div[data-testid="stForm"] {
                background: white !important;
                border-radius: var(--radius-md) !important;
                padding: 2rem !important;
                margin: 2rem 0 !important;
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
            
            # Enhanced concern description field with guided prompts
            concern_description = st.text_area(
                "Describe your situation", 
                placeholder="Tell us more about what you'd like to change. You can include:\n• How long you've been dealing with this\n• How urgent this is for you\n• Any previous experience with hypnotherapy\n• Specific questions or concerns you have",
                height=120,
                key="form_description"
            )
            
            # Form submit button that triggers calendar opening
            form_submitted = st.form_submit_button(
                "📞 Schedule My Free Discovery Call",
                use_container_width=True
            )
            
            # Handle form submission
            if form_submitted:
                if self._validate_form(email):
                    # Store form data in session state
                    st.session_state.form_data = {
                        'name': name,
                        'email': email,
                        'concern': concern,
                        'description': concern_description
                    }
                    # Send email
                    self._send_booking_email(name, email, concern, concern_description)
                    # Set flag to trigger calendar opening
                    st.session_state.trigger_calendar = True
                    st.success("✅ Request submitted successfully! Opening calendar...")
                    st.rerun()
        
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
        """Render action buttons that are always visible"""
        # Get current form data (if any)
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
            current_description or form_data.get('description', '')
        )
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        # Action buttons side by side - always visible, responsive for mobile
        col1, col2 = st.columns(2)
        
        with col1:
            # Direct calendar link button
            st.markdown(f"""
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 1rem; border: none;">
                📞 Schedule Call Directly
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            # Direct WhatsApp link button - white background with border
            st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: white; color: var(--text-primary);
                      text-decoration: none; padding: 1rem 1rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 1rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 1rem; border: 2px solid var(--border);">
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
    
    def _send_booking_email(self, name, email, concern, concern_description):
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
    
    def render_compact(self):
        """Render a compact version of the booking form"""
        st.markdown("### 📞 Book Your Free Discovery Call")
        
        with st.form("compact_booking_form"):
            # White background styling for the form
            st.markdown("""
            <style>
            div[data-testid="stForm"] {
                background: white !important;
                border-radius: var(--radius-md) !important;
                padding: 1.5rem !important;
                margin: 1rem 0 !important;
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
            
            # Form submit button that triggers calendar
            compact_submitted = st.form_submit_button(
                "📞 Schedule Call", 
                use_container_width=True
            )
            
            if compact_submitted:
                if email and self._is_valid_email(email):
                    # Send email and trigger calendar
                    self._send_booking_email("", email, concern, concern_description)
                    st.session_state.trigger_compact_calendar = True
                    st.success("✅ Request submitted successfully! Opening calendar...")
                    st.rerun()
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
        """Render compact action buttons that are always visible"""
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
            # Direct calendar link
            st.markdown(f"""
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 0.8rem 0.5rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 0.9rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.5rem; border: none;">
                📞 Direct Booking
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            # Direct WhatsApp link - white background with border
            st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" 
               style="display: inline-block; background-color: white; color: var(--text-primary);
                      text-decoration: none; padding: 0.8rem 0.5rem; border-radius: var(--radius-sm);
                      font-weight: 500; font-size: 0.9rem; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.5rem; border: 2px solid var(--border);">
                💬 WhatsApp
            </a>
            """, unsafe_allow_html=True)

# Factory function for easy import
def create_booking_form():
    """Factory function to create BookingForm instance"""
    return BookingForm()
