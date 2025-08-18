"""
UNIFIED Booking form component - Simple, consistent, mobile-friendly
Single form used across all pages
"""
import streamlit as st
import re

class UnifiedBookingForm:
    """Simplified, unified booking form component"""
    
    def __init__(self):
        # Contact URLs
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        self.package_url = "https://calendly.com/laetitiasheppard/package"
        
        # Form options
        self.concern_options = [
            "Select one...", 
            "Quit Smoking", 
            "Reduce Anxiety", 
            "Improve Sleep", 
            "Break Bad Habits",
            "Other"
        ]
    
    def render(self, form_type="discovery"):
        """Render unified booking form"""
        # Create anchor for scrolling
        st.markdown('<div id="booking"></div>', unsafe_allow_html=True)
        
        # Form header
        st.markdown("## 📞 Start Your Transformation Today")
        st.write("Begin your journey with a complimentary 15-minute discovery call")
        
        # Benefits callout
        self._render_benefits()
        
        # Main booking form
        self._render_form(form_type)
    
    def _render_benefits(self):
        """Render discovery call benefits"""
        st.info("""
        **What You'll Get in Your Discovery Call:**
        ✓ Personalized assessment of your situation  
        ✓ Clear explanation of how hypnotherapy works  
        ✓ Honest assessment of your success probability  
        ✓ Answers to all your questions  
        ✓ No pressure, no obligation
        """)
    
    def _render_form(self, form_type):
        """Render the main booking form"""
        with st.form("unified_booking_form", clear_on_submit=False):
            # Basic information
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
            
            # Concern selection
            concern = st.selectbox(
                "What would you most like to change?*",
                self.concern_options,
                help="This helps us prepare for your call"
            )
            
            # Additional context
            col3, col4 = st.columns(2)
            with col3:
                urgency = st.selectbox(
                    "How urgent is this for you?",
                    ["Select one...", "Very urgent - need help now", "Somewhat urgent - within a month", 
                     "Not urgent - just exploring", "Flexible timing"],
                    help="Helps us prioritize scheduling"
                )
            
            with col4:
                experience = st.selectbox(
                    "Previous experience with hypnotherapy?",
                    ["No previous experience", "Some experience", "Experienced", "Prefer not to say"],
                    help="Helps us tailor our explanation"
                )
            
            # Message
            message = st.text_area(
                "Anything specific you'd like to discuss?", 
                placeholder="Optional: Any questions, concerns, or background information",
                help="This helps us make the most of your 15 minutes"
            )
            
            # Session format preference
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
            
            # Handle submission
            if submitted:
                if self._validate_form(name, email, concern, urgency):
                    if self._handle_submission(name, email, concern, urgency, experience, message, contact_method):
                        self._show_success(name)
    
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
        
        # Show errors
        for error in errors:
            st.error(f"❌ {error}")
        
        return len(errors) == 0
    
    def _is_valid_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _handle_submission(self, name, email, concern, urgency, experience, message, contact_method):
        """Handle form submission"""
        try:
            # In production, integrate with email service
            # For now, simulate successful submission
            booking_data = {
                'name': name,
                'email': email,
                'concern': concern,
                'urgency': urgency,
                'experience': experience,
                'message': message,
                'contact_method': contact_method
            }
            
            # Log to console (in production, send email)
            print(f"Booking Request: {name} ({email}) - {concern}")
            return True
            
        except Exception as e:
            st.error("❌ There was an issue submitting your request. Please try again.")
            return False
    
    def _show_success(self, name):
        """Show success message and next steps"""
        st.success(f"✅ Thank you, {name}! Your discovery call request has been submitted.")
        
        # Next steps
        st.markdown("""
        ### What Happens Next:
        1. **📧 Check your email** for confirmation
        2. **📞 We'll contact you** within 24 hours to schedule
        3. **🎯 Your 15-minute discovery call**
        4. **⚡ Decide on next steps** together
        """)
        
        # Direct booking option
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📅 Or Schedule Directly", use_container_width=True, type="secondary"):
                st.success("Opening calendar link...")
                # In production: st.components.v1.html(f'<script>window.open("{self.discovery_url}", "_blank");</script>')
        
        with col2:
            if st.button("📋 Take Assessment", use_container_width=True):
                st.success("Scroll up to take the suitability assessment!")
        
        # Celebration
        st.balloons()
    
    def render_compact(self):
        """Render compact version for sidebar or small spaces"""
        st.markdown("### 📞 Quick Booking")
        
        with st.form("compact_booking"):
            name = st.text_input("Name*", placeholder="Your name")
            email = st.text_input("Email*", placeholder="your@email.com")
            concern = st.selectbox("Primary Concern*", self.concern_options)
            
            if st.form_submit_button("Schedule Call", type="primary", use_container_width=True):
                if name and email and concern != "Select one..." and self._is_valid_email(email):
                    st.success("✅ Request submitted! We'll contact you within 24 hours.")
                else:
                    st.error("Please fill in all required fields correctly.")

def create_booking_form():
    """Factory function to create booking form instance"""
    return UnifiedBookingForm()
