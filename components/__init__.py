"""
Components package initialization
Exports main component classes for easy import
"""

# Import and export main component classes
try:
    from .navigation import Navigation
    from .footer import Footer  
    from .booking_form import BookingForm
    from .quiz import Quiz
except ImportError as e:
    # Fallback classes in case of import issues
    class Navigation:
        def create_menu(self):
            import streamlit as st
            return st.selectbox("Navigation", ["Home", "Method", "Success", "Blog", "Book Now"])
    
    class Footer:
        def render(self):
            import streamlit as st
            st.markdown("© 2025 Laetitia Sheppard • All Rights Reserved")
    
    class BookingForm:
        def render(self):
            import streamlit as st
            st.markdown("### Contact Form")
            st.text_input("Name")
            st.text_input("Email") 
            st.form_submit_button("Submit")
    
    class Quiz:
        def render(self):
            import streamlit as st
            st.markdown("### Quiz Coming Soon")

__all__ = ['Navigation', 'Footer', 'BookingForm', 'Quiz']
