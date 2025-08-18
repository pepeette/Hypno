from utils.styling import apply_design_system
from components.navigation import show_navigation
from components.footer import show_footer
import streamlit as st

# Import all page classes
from pages.home import HomePage
from pages.method import MethodPage
from pages.success import SuccessPage
from pages.blog import BlogPage
from pages.booking import BookingPage

def main():
    # Apply design system first
    apply_design_system()
    
    # Initialize navigation
    show_navigation()
    
    # Get current page from query params
    query_params = st.experimental_get_query_params()
    current_page = query_params.get("page", ["home"])[0]
    
    # Render the appropriate page
    if current_page == "home":
        HomePage().render()
    elif current_page == "method":
        MethodPage().render()
    elif current_page == "success":
        SuccessPage().render()
    elif current_page == "blog":
        BlogPage().render()
    elif current_page == "booking":
        BookingPage().render()
    else:
        st.error("Page not found")
        HomePage().render()
    
    # Show footer on all pages
    show_footer()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Clinical Hypnotherapy Bangkok",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    main()
