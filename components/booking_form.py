"""
Booking form component for the Hypnotherapy website
Reusable booking form for discovery calls and consultations
Uses native Streamlit form components for better compatibility
"""
import streamlit as st
import re

class StreamlitOptimizedBookingForm:
    """Booking form using Streamlit native components"""
    
    def __init__(self):
        self.concern_options = [
            "Select one...", 
            "Quit Smoking", 
            "Reduce Anxiety", 
            "Improve Sleep", 
            "Break Bad Habits",
            "Weight Management",
            "Boost Confidence",
            "Other"
        ]
        
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        self.package_url = "https://calendly.com/laetitiasheppard/package"
    
    def render(self, form_title="Start Your Transformation Journey"):
        """Render booking form using Streamlit components"""
        st.markdown(f"## {form_title}")
        
        # Show booking options
        self._render_booking_options()
        
        # Main form using tabs
        tab1, tab2 = st.tabs(["📞 Free Discovery Call", "⚡ Book Transformation Package"])
        
        with tab1:
            self._render_discovery_form()
        
        with tab2:
            self._render_package_form()
    
    def _render_booking_options(self):
        """Render booking options using Streamlit"""
        st.write("Choose the option that feels right for you:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📞 Free Discovery Call")
            st.write("**Perfect if you:**")
            st.write("- Want to understand how hypnotherapy works")
            st.write("- Have questions about the process")
            st.write("- Want to assess your suitability")
            st.write("- Prefer to talk before committing")
            
            st.success("**100% FREE • No Commitment**")
        
        with col2:
            st.markdown("### ⚡ Transformation Package")
            st.write("**Perfect if you:**")
            st.write("- Are ready to commit to transformation")
            st.write("- Want to start immediately")
            st.write("- Have taken our assessment (70%+ score)")
            st.write("- Prefer direct action")
            
            st.info("**3,000 THB • 85% Success Rate**")
    
    def _render_discovery_form(self):
        """Render discovery call form"""
        st.markdown("### Book Your Free 15-Minute Discovery Call")
        st.write("No pressure, no sales pitch - just helpful information about your transformation journey")
        
        with st.form("discovery_form", clear_on_submit=False):
            # Personal information
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Your Name*", placeholder="First and last name")
            with col2:
                email = st.text_input("Email Address*", placeholder="your@email.com")
            
            # Primary concern
            concern = st.selectbox("What would you most like to change?*", self.concern_options)
            
            # Additional details
            col1, col2 = st.columns(2)
            with col1:
                urgency = st.selectbox(
                    "How urgent is this for you?",
                    ["Select one...", "Very urgent - need help ASAP", 
                     "Moderately urgent - within a month", 
                     "Not urgent - just exploring", "Flexible timing"]
                )
            with col2:
                preferred_time = st.selectbox(
                    "Preferred call time:",
                    ["No preference", "Morning (9-12)", "Afternoon (12-17)", 
                     "Evening (17-20)", "Weekend"]
                )
            
            # Optional message
            message = st.text_area(
                "Questions or concerns you'd like to discuss?", 
                placeholder="Optional: Anything specific you'd like us to know"
            )
            
            # Submit button
            submitted = st.form_submit_button(
                "📞 Schedule My Free Discovery Call", 
                type="primary", 
                use_container_width=True
            )
            
            if submitted:
                if self._validate_form(name, email, concern, urgency):
                    self._handle_discovery_submission(name, email, concern, urgency, preferred_time, message)
    
    def _render_package_form(self):
        """Render package booking form"""
        # Check quiz score
        quiz_score = st.session_state.get('quiz_score', 0)
        quiz_completed = st.session_state.get('quiz_completed', False)
        
        if quiz_completed:
            if quiz_score >= 70:
                st.success(f"✅ Excellent! Your assessment score of {quiz_score}% indicates you're ready for transformation.")
            else:
                st.warning(f"⚠️ Your assessment score of {quiz_score}% suggests a discovery call might be beneficial first.")
        else:
            st.info("💡 Consider taking our 30-second assessment first to confirm you're ready for the full program.")
        
        st.markdown("### Book Your Transformation Package")
        st.write("Ready to commit to your transformation journey")
        
        with st.form("package_form", clear_on_submit=False):
            # Personal information
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Your Name*", placeholder="First and last name")
            with col2:
                email = st.text_input("Email Address*", placeholder="your@email.com")
            
            # Primary concern and experience
            col1, col2 = st.columns(2)
            with col1:
                concern = st.selectbox("Primary Concern*", self.concern_options)
            with col2:
                experience = st.selectbox(
                    "Previous hypnotherapy experience?",
                    ["No previous experience", "Some experience", 
                     "Experienced", "Prefer not to say"]
                )
            
            # Package selection
            st.markdown("**Choose your package:**")
            package_type = st.radio(
                "Package Options",
                [
                    "Complete Package (3,000 THB) - 2 sessions with email support",
                    "Premium Package (4,000 THB) - 3 sessions with satisfaction guarantee"
                ],
                help="Most clients succeed with the Complete Package"
            )
            
            # Session preferences
            session_format = st.radio(
                "Preferred session format:",
                ["In-person (Bangkok clinic)", "Online (Zoom)", "No preference"],
                horizontal=True
            )
            
            # Additional details
            message = st.text_area(
                "Tell us about your situation*", 
                placeholder="Brief description of what you'd like to change and any relevant background"
            )
            
            # Submit button
            submitted = st.form_submit_button(
                "⚡ Book My Transformation Package", 
                type="primary", 
                use_container_width=True
            )
            
            if submitted:
                if self._validate_package_form(name, email, concern, message):
                    self._handle_package_submission(
                        name, email, concern, experience, 
                        package_type, session_format, message
                    )
    
    def _validate_form(self, name, email, concern, urgency):
        """Validate basic form fields"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        if not email.strip():
            errors.append("Email is required")
        elif not self._is_valid_email(email):
            errors.append("Please enter a valid email address")
        if concern == "Select one...":
            errors.append("Please select your primary concern")
        if urgency == "Select one...":
            errors.append("Please indicate urgency level")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        return True
    
    def _validate_package_form(self, name, email, concern, message):
        """Validate package form fields"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        if not email.strip():
            errors.append("Email is required")
        elif not self._is_valid_email(email):
            errors.append("Please enter a valid email address")
        if concern == "Select one...":
            errors.append("Please select your primary concern")
        if not message.strip():
            errors.append("Please tell us about your situation")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        return True
    
    def _is_valid_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    def _handle_discovery_submission(self, name, email, concern, urgency, preferred_time, message):
        """Handle discovery call form submission"""
        st.success("🎉 Discovery Call Requested!")
        st.write(f"Thank you, {name}! We'll contact you within 24 hours to schedule your free consultation.")
        
        # Show next steps
        st.markdown("### What Happens Next:")
        st.write("1. ✅ Check your email for confirmation")
        st.write("2. 📞 We'll contact you to schedule")
        st.write("3. 🎯 Your 15-minute discovery call")
        st.write("4. ⚡ Decide on next steps together")
        
        # Direct scheduling link
        st.markdown(f"""
        **Or schedule directly:** [Choose Your Time Slot]({self.discovery_url})
        """)
        
        st.balloons()
    
    def _handle_package_submission(self, name, email, concern, experience, package_type, session_format, message):
        """Handle package booking form submission"""
        st.success("🎉 Transformation Package Booked!")
        st.write(f"Thank you, {name}! Check your email for next steps and session scheduling information.")
        
        # Show next steps
        st.markdown("### What Happens Next:")
        st.write("1. ✅ Check your email for confirmation")
        st.write("2. 📅 We'll send calendar links for your sessions")
        st.write("3. 💳 Payment details will be provided")
        st.write("4. 🚀 Your transformation begins!")
        
        # Direct scheduling link
        st.markdown(f"""
        **Schedule your sessions now:** [Book Your Sessions]({self.package_url})
        """)
        
        st.balloons()
    
    def render_compact(self):
        """Render compact version using Streamlit"""
        st.markdown("### 📞 Quick Start")
        
        with st.form("compact_booking"):
            name = st.text_input("Name*", placeholder="Your name")
            email = st.text_input("Email*", placeholder="your@email.com")
            concern = st.selectbox("Primary concern*", self.concern_options)
            
            col1, col2 = st.columns(2)
            with col1:
                discovery_submitted = st.form_submit_button("📞 Free Call", use_container_width=True)
            with col2:
                package_submitted = st.form_submit_button("⚡ Book Package", type="primary", use_container_width=True)
            
            if discovery_submitted or package_submitted:
                if name and email and concern != "Select one..." and self._is_valid_email(email):
                    if discovery_submitted:
                        st.success("✅ Discovery call requested! We'll contact you within 24 hours.")
                    else:
                        st.success("✅ Package booking received! Check your email for next steps.")
                else:
                    st.error("Please fill all fields correctly")

def create_streamlit_booking_form():
    """Factory function"""
    return StreamlitOptimizedBookingForm()
