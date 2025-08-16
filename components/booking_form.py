"""
Booking form component for the Hypnotherapy website
Reusable booking form for discovery calls and consultations
"""
import streamlit as st
import re

class BookingForm:
    """Reusable booking form component"""
    
    def __init__(self):
        # Try to get config values
        try:
            from utils.config import AppConstants
            self.concern_options = AppConstants.CONCERN_OPTIONS
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/30min")
        except ImportError:
            self.concern_options = [
                "Select one...", 
                "Quit Smoking", 
                "Reduce Anxiety", 
                "Improve Sleep", 
                "Break Bad Habits",
                "Other"
            ]
            self.discovery_url = "https://calendly.com/laetitiasheppard/30min"
    
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
                    "Your Name*", 
                    placeholder="First and last name",
                    help="We'll use this to personalize your session"
                )
            with cols[1]:
                email = st.text_input(
                    "Email Address*", 
                    placeholder="your@email.com",
                    help="For session confirmations and resources"
                )
            
            concern = st.selectbox(
                "What would you most like to change?*",
                self.concern_options,
                help="This helps us prepare for your call"
            )
            
            # Additional context
            cols2 = st.columns(2)
            with cols2[0]:
                urgency = st.selectbox(
                    "How urgent is this for you?",
                    ["Select one...", "Very urgent - need help now", "Somewhat urgent - within a month", 
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
                "Anything specific you'd like to discuss?", 
                placeholder="Optional: Any questions, concerns, or background information you'd like to share",
                help="This helps us make the most of your 15 minutes"
            )
            
            # Preferred contact method
            contact_method = st.radio(
                "Preferred session format:",
                ["Video call (Zoom)", "Phone call", "In-person (Bangkok)", "No preference"],
                horizontal=True
            )
            
            # Submit button
            submitted = st.form_submit_button(
                "📞 Schedule My Free Discovery Call", 
                type="primary", 
                use_container_width=True
            )
            
            if submitted:
                if self._validate_form(name, email, concern, urgency):
                    self._handle_form_submission(name, email, concern, urgency, experience, message, contact_method)
    
    def _validate_form(self, name, email, concern, urgency):
        """Validate form inputs"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        
        if not email.strip():
            errors.append("Email is required")
        elif not self._is_valid_email(email):
            errors.append("Please enter a valid email address")
        
        if concern == "Select one...":
            errors.append("Please select what you'd like to change")
        
        if urgency == "Select one...":
            errors.append("Please indicate how urgent this is for you")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _is_valid_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _handle_form_submission(self, name, email, concern, urgency, experience, message, contact_method):
        """Handle successful form submission"""
        # Try to send email
        if self._send_booking_email(name, email, concern, urgency, experience, message, contact_method):
            # Success state
            self._render_success_state(name)
        else:
            # Error state
            st.error("❌ There was an issue submitting your request. Please try again or contact us directly.")
    
    def _send_booking_email(self, name, email, concern, urgency, experience, message, contact_method):
        """Send booking notification email"""
        try:
            # Try to import email handler
            from utils.email_handler import send_discovery_call_email
            
            booking_data = {
                'name': name,
                'email': email,
                'concern': concern,
                'urgency': urgency,
                'experience': experience,
                'message': message,
                'contact_method': contact_method
            }
            
            return send_discovery_call_email(booking_data)
            
        except ImportError:
            # Fallback - log to console (in production, implement proper email)
            print(f"Discovery Call Booking: {name} ({email}) - {concern} - {urgency}")
            return True  # Simulate success
    
    def _render_success_state(self, name):
        """Render success state after form submission"""
        success_html = f"""
        <div style="background: rgba(34, 197, 94, 0.1); border: 2px solid var(--success);
                    border-radius: var(--radius-md); padding: 2rem; text-align: center; margin: 2rem 0;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
            <h2 style="color: var(--success); margin-bottom: 1rem;">Discovery Call Scheduled!</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">
                Thank you, {name}! We've received your request and will contact you within 24 hours 
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
        
        # Calendar link
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                Or schedule directly using our calendar:
            </p>
            <a href="{self.discovery_url}" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; font-size: 1.1rem; transition: var(--transition);">
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
            name = st.text_input("Name*", placeholder="Your name")
            email = st.text_input("Email*", placeholder="your@email.com")
            concern = st.selectbox("Primary Concern*", self.concern_options)
            
            submitted = st.form_submit_button("Schedule Call", type="primary", use_container_width=True)
            
            if submitted:
                if name and email and concern != "Select one..." and self._is_valid_email(email):
                    if self._send_booking_email(name, email, concern, "Not specified", "Not specified", "", "No preference"):
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
                    st.error("Please fill in all required fields with valid information.")

# Factory function for easy import
def create_booking_form():
    """Factory function to create BookingForm instance"""
    return BookingForm()
