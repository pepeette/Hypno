"""
Booking page component for the Hypnotherapy website
Empty page - booking form and footer are handled by app.py
"""
import streamlit as st

class BookingPage:
    """Empty booking page - content handled by app.py"""
    
    def __init__(self):
        pass
    
    def render(self):
        """Render nothing - app.py handles booking form and footer"""
        pass

# Factory function for clean import
def create_booking_page():
    return BookingPage()
