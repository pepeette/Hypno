"""
Main application entry point - Streamlit Hypnotherapy Website
Professional, robust, and maintainable architecture
"""
from utils import styling, config
from components.navigation import show_navigation
from components.footer import show_footer
from pages.home import create_home_page
from pages.method import create_method_page
from pages.success import create_success_page
from pages.blog import create_blog_page
from pages.booking import create_booking_page
import streamlit as st

# Initialize app-wide styling
styling.apply_design_system()

def main():
    """Main application controller"""
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Get current page from query params
    query_params = st.experimental_get_query_params()
    current_page = query_params.get('page', ['home'])[0]
    
    # Render navigation and page content
    show_navigation()
    _render_page_content(current_page)
    show_footer()

def _render_page_content(page):
    """Render the appropriate page based on route"""
    page_components = {
        'home': create_home_page(),
        'method': create_method_page(),
        'success': create_success_page(),
        'blog': create_blog_page(),
        'booking': create_booking_page()
    }
    
    # Error handling for invalid routes
    if page not in page_components:
        st.error("Page not found")
        page = 'home'
    
    try:
        with st.spinner(f"Loading {page}..."):
            page_components[page].render()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.session_state.page = 'home'
        st.rerun()

if __name__ == "__main__":
    # Configure Streamlit settings
    st.set_page_config(
        page_title="Clinical Hypnotherapy Bangkok",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Run main app
    main()
