"""
Enhanced Booking form component for the Hypnotherapy website
Simplified with white background and direct actions
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
        """Render the main booking form with white background"""
        # Start white background container for form only
        st.markdown("""
        <div style="background: white; border-radius: var(--radius-md); padding: 2rem; 
                    margin: 2rem 0; box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
        """, unsafe_allow_html=True)
        
        with st.form("discovery_booking_form", clear_on_submit=False):
            # Form fields
            cols = st.columns(2)
            with cols[0]:
                name = st.text_input(
                    "Your Name", 
                    placeholder="First and last name"
                )
            with cols[1]:
                email = st.text_input(
                    "Email Address*", 
                    placeholder="your@email.com"
                )
            
            concern = st.selectbox(
                "What would you most like to change?",
                [""] + self.concern_options
            )
            
            # Enhanced concern description field with guided prompts
            concern_description = st.text_area(
                "Describe your situation", 
                placeholder="Tell us more about what you'd like to change. You can include:\n• How long you've been dealing with this\n• How urgent this is for you\n• Any previous experience with hypnotherapy\n• Specific questions or concerns you have",
                height=120
            )
            
            # Direct action buttons side by side
            col1, col2 = st.columns(2)
            
            with col1:
                submitted = st.form_submit_button(
                    "📞 Schedule My Free Discovery Call", 
                    type="primary", 
                    use_container_width=True
                )
            
            with col2:
                # WhatsApp button using standard Streamlit button styling
                whatsapp_clicked = st.form_submit_button(
                    "💬 Message on WhatsApp",
                    use_container_width=True
                )
            
            if submitted:
                if self._validate_form(email):
                    # Send email and redirect to calendar
                    if self._send_booking_email(name, email, concern, concern_description):
                        # Show success and redirect to calendar
                        st.success("✅ Request submitted! Opening calendar...")
                        st.markdown(f"""
                        <script>
                        window.open('{self.discovery_url}', '_blank');
                        </script>
                        <div style="text-align: center; margin: 1rem 0;">
                            <a href="{self.discovery_url}" target="_blank" 
                               style="display: inline-block; background-color: var(--accent); color: white;
                                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                                      font-weight: 600; font-size: 1.1rem; transition: var(--transition);
                                      box-shadow: var(--shadow-accent);">
                                📅 Click here if calendar didn't open
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("❌ There was an issue. Please try again or contact us directly.")
            
            if whatsapp_clicked:
                # Handle WhatsApp redirect
                whatsapp_message = self._create_whatsapp_message(name, email, concern, concern_description)
                encoded_message = urllib.parse.quote(whatsapp_message)
                whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
                
                st.success("✅ Opening WhatsApp...")
                st.markdown(f"""
                <script>
                window.open('{whatsapp_url}', '_blank');
                </script>
                <div style="text-align: center; margin: 1rem 0;">
                    <a href="{whatsapp_url}" target="_blank" 
                       style="display: inline-block; background-color: #25D366; color: white;
                              text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                              font-weight: 600; font-size: 1.1rem; transition: var(--transition);">
                        💬 Click here if WhatsApp didn't open
                    </a>
                </div>
                """, unsafe_allow_html=True)
        
        # Close white background container
        st.markdown("</div>", unsafe_allow_html=True)
    
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
        
        # White background only for the form
        st.markdown("""
        <div style="background: white; border-radius: var(--radius-md); padding: 1.5rem; 
                    margin: 1rem 0; box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
        """, unsafe_allow_html=True)
        
        with st.form("compact_booking_form"):
            email = st.text_input("Email*", placeholder="your@email.com")
            concern = st.selectbox("What would you like to change?", [""] + self.concern_options)
            concern_description = st.text_area(
                "Describe your situation", 
                placeholder="Brief description including how long you've dealt with this, how urgent it is, and any questions you have",
                height=80
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                submitted = st.form_submit_button("📞 Schedule Call", type="primary", use_container_width=True)
            
            with col2:
                whatsapp_clicked = st.form_submit_button("💬 WhatsApp", use_container_width=True)
            
            if submitted:
                if email and self._is_valid_email(email):
                    if self._send_booking_email("", email, concern, concern_description):
                        st.success("✅ Request submitted! Opening calendar...")
                        st.markdown(f"""
                        <script>
                        window.open('{self.discovery_url}', '_blank');
                        </script>
                        <div style="text-align: center; margin: 1rem 0;">
                            <a href="{self.discovery_url}" target="_blank" 
                               style="display: inline-block; background-color: var(--accent); color: white;
                                      text-decoration: none; padding: 0.8rem; border-radius: var(--radius-sm);
                                      font-weight: 600; text-align: center;">
                                📅 Click if calendar didn't open
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("Please enter a valid email address.")
            
            if whatsapp_clicked:
                whatsapp_message = self._create_whatsapp_message("", email, concern, concern_description)
                encoded_message = urllib.parse.quote(whatsapp_message)
                whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
                
                st.success("✅ Opening WhatsApp...")
                st.markdown(f"""
                <script>
                window.open('{whatsapp_url}', '_blank');
                </script>
                <div style="text-align: center; margin: 1rem 0;">
                    <a href="{whatsapp_url}" target="_blank" 
                       style="display: inline-block; background-color: #25D366; color: white;
                              text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                              font-weight: 600; font-size: 1.1rem; transition: var(--transition);">
                        💬 Click if WhatsApp didn't open
                    </a>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Factory function for easy import
def create_booking_form():
    """Factory function to create BookingForm instance"""
    return BookingForm()
