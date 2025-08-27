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
Minimal page - only displays action buttons
"""
import streamlit as st
import urllib.parse

class BookingPage:
    """Minimal booking page with action buttons only"""
    
    def __init__(self):
        # Try to get URLs from config
        try:
            from utils.config import AppConstants
            self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
        except ImportError:
            self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        
        # WhatsApp number
        self.whatsapp_number = "+66642439944"
    
    def render(self):
        """Render only the action buttons"""
        # # Simple header
        # st.markdown("""
        # <div style="text-align: center; margin: 2rem 0 3rem 0;">
        #     <h1>Ready to Transform Your Life?</h1>
        #     <p style="color: var(--text-secondary);">
        #         Choose your preferred way to get started
        #     </p>
        # </div>
        # """, unsafe_allow_html=True)
        
        # Action buttons
        self._render_action_buttons()
    
    def _render_action_buttons(self):
        """Render the two action buttons"""
        # Get form data if available for WhatsApp message
        form_data = st.session_state.get('form_data', {})
        
        # Create WhatsApp message
        whatsapp_message = self._create_whatsapp_message(
            form_data.get('name', ''),
            form_data.get('email', ''),
            form_data.get('concern', ''),
            form_data.get('description', '')
        )
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{self.whatsapp_number.replace('+', '')}?text={encoded_message}"
        
        # Action buttons side by side
        col1, col2 = st.columns(2)
        
        with col1:
            # Schedule Session button (primary accent color)
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
            # WhatsApp button (white with border)
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

# Factory function for clean import
def create_booking_page():
    return BookingPage()
