"""
Booking Form Component
Professional booking form using Streamlit components with validation
"""
import streamlit as st
import re
from utils.config import FormConfig
from utils.session_state import update_user_data, set_form_success, set_form_errors

class BookingForm:
    """Professional booking form using native Streamlit components"""
    
    def __init__(self):
        self.concern_options = FormConfig.CONCERN_OPTIONS
        self.urgency_options = FormConfig.URGENCY_OPTIONS
        self.experience_options = FormConfig.EXPERIENCE_OPTIONS
    
    def render(self):
        """Render the main booking form"""
        st.markdown("## Book Your Free Discovery Call")
        st.write("Begin your transformation with a complimentary 15-minute consultation")
        
        # Benefits section using Streamlit components
        self._render_benefits()
        
        # Main booking form
        self._render_main_form()
    
    def render_compact(self):
        """Render compact version for footer/sidebar"""
        st.markdown("### Ready to Transform Your Life?")
        st.write("Start with a free 15-minute discovery call")
        
        with st.form("compact_booking_form"):
            # Basic form fields
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name*", placeholder="Your name")
            with col2:
                email = st.text_input("Email*", placeholder="your@email.com")
            
            concern = st.selectbox("Primary Concern*", self.concern_options)
            
            submitted = st.form_submit_button(
                "Request Free Discovery Call",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                if self._validate_basic_form(name, email, concern):
                    self._handle_form_submission(name, email, concern, "")
    
    def _render_benefits(self):
        """Render benefits using Streamlit components"""
        st.markdown("### What You'll Get in Your Discovery Call")
        
        # Benefits using columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("✓ Personalized assessment of your situation")
            st.write("✓ Clear explanation of how hypnotherapy works")
            st.write("✓ Honest assessment of your success probability")
        
        with col2:
            st.write("✓ Answers to all your questions")
            st.write("✓ No pressure, no obligation")
            st.write("✓ Next steps if you decide to proceed")
    
    def _render_main_form(self):
        """Render the main booking form using Streamlit form"""
        with st.form("discovery_booking_form"):
            # Personal information section
            st.markdown("#### 👤 Personal Information")
            
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input(
                    "Your Name*",
                    placeholder="First and last name",
                    help="We'll use this to personalize your session"
                )
            with col2:
                email = st.text_input(
                    "Email Address*",
                    placeholder="your@email.com",
                    help="For session confirmations and resources"
                )
            
            col3, col4 = st.columns(2)
            with col3:
                phone = st.text_input(
                    "Phone Number (Optional)",
                    placeholder="+66 XX XXX XXXX",
                    help="For quicker communication if needed"
                )
            with col4:
                contact_method = st.selectbox(
                    "Preferred Contact Method*",
                    ["Phone call", "Video call (Zoom)", "Email first"],
                    help="How would you like us to reach you?"
                )
            
            # Situation assessment section
            st.markdown("#### 🎯 Your Situation")
            
            concern = st.selectbox(
                "What would you most like to change?*",
                self.concern_options,
                help="This helps us prepare for your call"
            )
            
            col5, col6 = st.columns(2)
            with col5:
                urgency = st.selectbox(
                    "How urgent is this for you?*",
                    self.urgency_options,
                    help="Helps us prioritize scheduling"
                )
            with col6:
                experience = st.selectbox(
                    "Previous hypnotherapy experience?",
                    self.experience_options,
                    help="Helps us tailor our explanation"
                )
            
            message = st.text_area(
                "Tell us more about your situation",
                placeholder="Optional: Any specific details, questions, or concerns you'd like to discuss",
                help="This helps us make the most of your 15 minutes",
                height=100
            )
            
            # Preferences section
            st.markdown("#### ⏰ Scheduling Preferences")
            
            col7, col8 = st.columns(2)
            with col7:
                time_preference = st.selectbox(
                    "Preferred Time of Day",
                    ["No preference", "Morning (9AM-12PM)", "Afternoon (12PM-5PM)", "Evening (5PM-8PM)"],
                    help="Bangkok time (UTC+7)"
                )
            with col8:
                day_preference = st.selectbox(
                    "Preferred Days",
                    ["Any day works", "Weekdays only", "Weekends only", "Specific days (mention above)"]
                )
            
            # Consent section using Streamlit checkbox
            st.markdown("#### 🔒 Privacy & Consent")
            
            consent = st.checkbox(
                "I consent to being contacted about hypnotherapy services and understand all information will be kept strictly confidential",
                help="Required to proceed with booking"
            )
            
            newsletter = st.checkbox(
                "I'd like to receive helpful tips about transformation and wellness (optional)"
            )
            
            # Submit button
            submitted = st.form_submit_button(
                "📞 Schedule My Free Discovery Call",
                type="primary",
                use_container_width=True,
                help="We'll contact you within 24 hours"
            )
            
            if submitted:
                form_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'contact_method': contact_method,
                    'concern': concern,
                    'urgency': urgency,
                    'experience': experience,
                    'message': message,
                    'time_preference': time_preference,
                    'day_preference': day_preference,
                    'consent': consent,
                    'newsletter': newsletter
                }
                
                if self._validate_discovery_form(form_data):
                    self._handle_discovery_submission(form_data)
    
    def _validate_basic_form(self, name, email, concern):
        """Basic validation for compact form"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        
        if not email.strip():
            errors.append("Email is required")
        elif not self._is_valid_email(email):
            errors.append("Please enter a valid email address")
        
        if not concern or concern.startswith("Select"):
            errors.append("Please select your primary concern")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _validate_discovery_form(self, form_data):
        """Comprehensive validation for discovery form"""
        errors = []
        
        # Required field validation
        if not form_data['name'].strip():
            errors.append("Name is required")
        
        if not form_data['email'].strip():
            errors.append("Email is required")
        elif not self._is_valid_email(form_data['email']):
            errors.append("Please enter a valid email address")
        
        if not form_data['concern'] or form_data['concern'].startswith("Select"):
            errors.append("Please select your primary concern")
        
        if not form_data['urgency'] or form_data['urgency'].startswith("How urgent"):
            errors.append("Please indicate urgency level")
        
        if not form_data['consent']:
            errors.append("Please consent to being contacted")
        
        # Phone validation if provided
        if form_data['phone'] and not self._is_valid_phone(form_data['phone']):
            errors.append("Please enter a valid phone number")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _is_valid_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _is_valid_phone(self, phone):
        """Validate phone number format"""
        cleaned = re.sub(r'[\s\-\(\)\+]', '', phone)
        return len(cleaned) >= 8 and len(cleaned) <= 15 and cleaned.isdigit()
    
    def _handle_form_submission(self, name, email, concern, message):
        """Handle basic form submission"""
        try:
            # Update user data in session state
            update_user_data(name=name, email=email, concern=concern)
            
            # Simulate email sending (replace with actual implementation)
            success = self._send_booking_email({
                'name': name,
                'email': email,
                'concern': concern,
                'message': message
            })
            
            if success:
                set_form_success(True)
                st.success("✅ Discovery call request submitted! We'll contact you within 24 hours.")
                st.balloons()
            else:
                st.error("❌ There was an issue. Please try again or contact us directly.")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
    
    def _handle_discovery_submission(self, form_data):
        """Handle comprehensive discovery form submission"""
        try:
            # Update user data
            update_user_data(
                name=form_data['name'],
                email=form_data['email'],
                concern=form_data['concern'],
                phone=form_data['phone']
            )
            
            # Send detailed booking email
            success = self._send_discovery_email(form_data)
            
            if success:
                set_form_success(True)
                self._render_success_message(form_data['name'])
            else:
                st.error("❌ There was an issue. Please try again or contact us directly.")
                
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
    
    def _send_booking_email(self, data):
        """Send booking notification email (implement with actual service)"""
        # Placeholder for email implementation
        print(f"Booking: {data}")
        return True
    
    def _send_discovery_email(self, data):
        """Send detailed discovery call booking email"""
        # Placeholder for email implementation
        print(f"Discovery Call: {data}")
        return True
    
    def _render_success_message(self, name):
        """Render success message using Streamlit components"""
        st.success(f"✅ Thank you, {name}! Your discovery call request has been submitted.")
        
        # Next steps using info box
        st.info("""
        **What happens next:**
        
        1. **Check your email** for confirmation
        2. **We'll contact you** within 24 hours to schedule
        3. **Your discovery call** where we assess your situation
        4. **Next steps** if you decide to proceed
        """)
        
        # Direct scheduling option
        st.markdown("### Or Schedule Directly")
        if st.button("📅 Choose Your Time Slot", type="primary", use_container_width=True):
            st.success("Opening calendar...")
        
        st.balloons()

# Factory function for easy import
def create_booking_form():
    """Create BookingForm instance"""
    return BookingForm()
