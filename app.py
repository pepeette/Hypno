"""
Main Application Entry Point
Clean architecture with modular imports using Streamlit components
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Transform Your Life in 2 Sessions | Clinical Hypnotherapy Bangkok",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import modules with error handling
try:
    from utils.styling import apply_global_styles
    from utils.session_state import initialize_session_state
    from components.navigation import Navigation
    from components.footer import Footer
    from components.booking_form import BookingForm
    from pages.home import HomePage
    from pages.method import MethodPage
    from pages.success import SuccessPage
    from pages.blog import BlogPage
    from pages.booking import BookingPage
except ImportError as e:
    st.error(f"Module import error: {e}")
    st.stop()

def main():
    """Main application entry point"""
    
    # Apply styling
    apply_global_styles()
    
    # Initialize session state
    initialize_session_state()
    
    # Create navigation
    navigation = Navigation()
    selected_page = navigation.render()
    
    # Route to appropriate page
    if selected_page == "Home":
        page = HomePage()
        page.render()
    elif selected_page == "Method":
        page = MethodPage()
        page.render()
    elif selected_page == "Success Stories":
        page = SuccessPage()
        page.render()
    elif selected_page == "FAQ & Blog":
        page = BlogPage()
        page.render()
    elif selected_page == "Book Now":
        page = BookingPage()
        page.render()
    
    # Always show booking form and footer (except on booking page)
    if selected_page != "Book Now":
        st.markdown("---")
        booking_form = BookingForm()
        booking_form.render_compact()
    
    # Footer on every page
    footer = Footer()
    footer.render()

if __name__ == "__main__":
    main()
