# """
# Booking page component for the Hypnotherapy website
# Empty page - booking form and footer are handled by app.py
# """
# import streamlit as st

# class BookingPage:
#     """Empty booking page - content handled by app.py"""
    
#     def __init__(self):
#         pass
    
#     def render(self):
#         """Render nothing - app.py handles booking form and footer"""
#         pass

# # Factory function for clean import
# def create_booking_page():
#     return BookingPage()


"""
Booking page component for the Hypnotherapy website
Features different booking options and contact forms with action buttons
"""
import streamlit as st
import re
import urllib.parse

class BookingPage:
    """Booking page component with action buttons"""
    
    def __init__(self):
        # Try to get URLs from config
        try:
            from utils.config import AppConstants
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
            self.package_url = AppConstants.CONTACT_INFO.get("package_booking_url", "https://calendly.com/laetitiasheppard/package")
        except ImportError:
            self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
            self.package_url = "https://calendly.com/laetitiasheppard/package"
        
        # WhatsApp number
        self.whatsapp_number = "+66642439944"
        
        # Try to get concern options from config
        try:
            from utils.config import AppConstants
            self.concern_options = AppConstants.CONCERN_OPTIONS
        except ImportError:
            self.concern_options = [
                "Select one...", 
                "Quit Smoking", 
                "Reduce Anxiety", 
                "Improve Sleep", 
                "Break Bad Habits",
                "Other"
            ]
    
    def render(self):
        """Render the complete booking page"""
        self._render_header()
        self._render_booking_options()
        self._render_forms()
        self._render_contact_info()
    
    def _render_header(self):
        """Render page header"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <h1>Start Your Transformation Today</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                Choose the option that feels right for you - we're here to support your journey
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_booking_options(self):
        """Render booking options overview"""
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            st.markdown("""
            <div class="card-elevated">
                <h2 style="color: var(--accent); text-align: center; margin-bottom: 1rem;">
                    🎯 Free Discovery Call
                </h2>
                <p style="text-align: center; color: var(--text-secondary); margin-bottom: 2rem;">
                    15-minute consultation to discuss your goals and assess suitability
                </p>
                <ul style="margin-bottom: 2rem;">
                    <li><strong>Perfect if you:</strong></li>
                    <li>Want to understand how hypnotherapy works</li>
                    <li>Have questions about the process</li>
                    <li>Want to assess your suitability</li>
                    <li>Prefer to talk before committing</li>
                </ul>
                <div style="text-align: center;">
                    <span style="font-size: 1.2rem; font-weight: bold; color: var(--success);">
                        FREE • No Obligation
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card-elevated">
                <h2 style="color: var(--accent); text-align: center; margin-bottom: 1rem;">
                    ⚡ Transformation Package
                </h2>
                <p style="text-align: center; color: var(--text-secondary); margin-bottom: 2rem;">
                    Complete 2-session program for rapid, lasting change
                </p>
                <ul style="margin-bottom: 2rem;">
                    <li><strong>Perfect if you:</strong></li>
                    <li>Are ready to commit to transformation</li>
                    <li>Want to start immediately</li>
                    <li>Have taken our assessment (70%+ score)</li>
                    <li>Prefer direct action</li>
                </ul>
                <div style="text-align: center;">
                    <span style="font-size: 1.2rem; font-weight: bold; color: var(--accent);">
                        3,000 THB • 85% Success Rate
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_forms(self):
        """Render booking forms"""
        st.markdown("""
        <div style="margin: 4rem 0 2rem 0;">
            <h2 style="text-align: center;">Choose Your Next Step</h2>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["📞 Free Discovery Call", "⚡ Transformation Package"])
        
        with tab1:
            self._render_discovery_form()
        
        with tab2:
            self._render_package_form()
    
    def _render_discovery_form(self):
        """Render discovery call form"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h3>Book Your Free 15-Minute Discovery Call</h3>
            <p style="color: var(--text-secondary);">
                No pressure, no obligation - just helpful information about your transformation journey
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("discovery_form"):
            cols = st.columns(2)
            with cols[0]:
                name = st.text_input("Your Name*", placeholder="First and last name", key="disc_name")
            with cols[1]:
                email = st.text_input("Email*", placeholder="your@email.com", key="disc_email")
            
            concern = st.selectbox(
                "Primary Concern*",
                self.concern_options,
                key="disc_concern"
            )
            
            message = st.text_area(
                "What would you like to discuss?", 
                placeholder="Optional: Any specific questions or concerns you'd like to address",
                key="disc_message"
            )
            
            submitted = st.form_submit_button("📞 Schedule My Free Call", type="primary", use_container_width=True)
            
            if submitted:
                if self._validate_form(name, email, concern):
                    if self._send_email(name, email, concern, message, "Discovery Call"):
                        st.success("✅ Discovery call scheduled! Check your email for confirmation.")
                        # Store form data for action buttons
                        st.session_state.form_data = {
                            'name': name,
                            'email': email,
                            'concern': concern,
                            'description': message
                        }
                        st.balloons()
        
        # Add action buttons below form
        self._render_action_buttons()
    
    def _render_package_form(self):
        """Render package booking form"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h3>Book Your Transformation Package</h3>
            <p style="color: var(--text-secondary);">
                Ready to start your 2-session transformation journey
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quiz score check
        quiz_completed = st.session_state.get('quiz_completed', False)
        quiz_score = st.session_state.get('quiz_score', 0)
        
        if quiz_completed and quiz_score >= 70:
            st.success(f"✅ Great! Your assessment score of {quiz_score}% indicates excellent suitability for our program.")
        elif quiz_completed and quiz_score < 70:
            st.warning(f"⚠️ Your assessment score of {quiz_score}% suggests a discovery call first might be beneficial.")
        else:
            st.info("💡 Consider taking our 30-second assessment first to determine your suitability.")
        
        with st.form("package_form"):
            cols = st.columns(2)
            with cols[0]:
                name = st.text_input("Your Name*", placeholder="First and last name", key="pkg_name")
            with cols[1]:
                email = st.text_input("Email*", placeholder="your@email.com", key="pkg_email")
            
            concern = st.selectbox(
                "Primary Concern*",
                self.concern_options,
                key="pkg_concern"
            )
            
            experience = st.selectbox(
                "Previous experience with hypnotherapy?",
                ["No previous experience", "Some experience", "Experienced", "Prefer not to say"],
                key="pkg_experience"
            )
            
            message = st.text_area(
                "Tell us about your situation", 
                placeholder="Brief description of what you'd like to change and any relevant background",
                key="pkg_message"
            )
            
            # Package options
            st.markdown("**Choose your package:**")
            package_type = st.radio(
                "Package Options",
                ["Complete Package (3,000 THB) - 2 sessions", "Premium Package (4,000 THB) - 3 sessions with guarantee"],
                key="pkg_type"
            )
            
            submitted = st.form_submit_button("⚡ Book My Transformation", type="primary", use_container_width=True)
            
            if submitted:
                if self._validate_form(name, email, concern):
                    package_details = f"Package: {package_type}\nExperience: {experience}\nMessage: {message}"
                    if self._send_email(name, email, concern, package_details, "Transformation Package"):
                        st.success("✅ Transformation package booked! Check your email for next steps.")
                        # Store form data for action buttons
                        st.session_state.form_data = {
                            'name': name,
                            'email': email,
                            'concern': concern,
                            'description': package_details
                        }
                        st.balloons()
        
        # Add action buttons below form
        self._render_action_buttons()
    
    def _render_action_buttons(self):
        """Render action buttons with minimized spacing - same as booking_form.py"""
        # Get current form data (if any)
        form_data = st.session_state.get('form_data', {})
        
        # Create WhatsApp message with current form data
        whatsapp_message = self._create_whatsapp_message(
            form_data.get('name', ''),
            form_data.get('email', ''),
            form_data.get('concern', ''),
            form_data.get('description', '')
        )
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        # Action buttons side by side with minimized spacing
        col1, col2 = st.columns(2)
        
        with col1:
            # Direct calendar link button
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
            # Direct WhatsApp link button - white background with border
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
    
    def _render_contact_info(self):
        """Render contact information"""
        st.markdown("""
        <div style="margin: 4rem 0 2rem 0;">
            <h2 style="text-align: center;">Contact Information</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <h3>📍 Location</h3>
                <p>Bangkok Hypnotherapy Clinic<br>
                27 Soi Sukhumvit 10 (Asoke)<br>
                Bangkok, Thailand</p>
                <a href="https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw" 
                   target="_blank" class="btn btn-secondary" style="text-decoration: none;">
                    Get Directions
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <h3>💬 Online Sessions</h3>
                <p>Available worldwide via<br>
                secure video conferencing<br>
                Same effectiveness as in-person</p>
                <a href="#discovery" class="btn btn-secondary" style="text-decoration: none;">
                    Book Online Session
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <h3>⏰ Hours</h3>
                <p>Monday - Friday: 9:00 - 18:00<br>
                Saturday: 10:00 - 16:00<br>
                Sunday: By appointment</p>
                <a href="#discovery" class="btn btn-secondary" style="text-decoration: none;">
                    Schedule Now
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    def _validate_form(self, name, email, concern):
        """Validate form inputs"""
        if not name or not email or concern == "Select one...":
            st.error("Please fill in all required fields")
            return False
        
        if not self._is_valid_email(email):
            st.error("Please enter a valid email address")
            return False
        
        return True
    
    def _is_valid_email(self, email):
        """Validate email format"""
        return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)
    
    def _send_email(self, name, email, concern, message, booking_type):
        """Send email notification (placeholder for now)"""
        try:
            # Try to import and use email handler
            from utils.email_handler import send_booking_email
            return send_booking_email(name, email, concern, message, booking_type)
        except ImportError:
            # Fallback - in production, implement proper email sending
            print(f"Booking: {booking_type} - {name} ({email}) - {concern}")
            return True  # Simulate success for now

# Factory function for clean import
def create_booking_page():
    return BookingPage()
