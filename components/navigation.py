"""
Sleek, responsive navigation component
Maintains active state and clean design
"""
from utils import config
import streamlit as st

def show_navigation():
    """Render the main navigation bar"""
    pages = [
        {"name": "Home", "icon": "🏠", "key": "home"},
        {"name": "Method", "icon": "🧠", "key": "method"},
        {"name": "Success", "icon": "🌟", "key": "success"},
        {"name": "Blog", "icon": "📚", "key": "blog"},
        {"name": "Book", "icon": "📅", "key": "booking", "type": "primary"}
    ]
    
    current_page = st.experimental_get_query_params().get("page", ["home"])[0]
    
    # Inject navigation CSS
    st.markdown(f"""
    <style>
    .nav-container {{
        display: flex;
        gap: 0.5rem;
        margin-bottom: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid {config.border};
    }}
    .nav-link {{
        padding: 0.5rem 1rem;
        border-radius: {config.radius_sm};
        text-decoration: none;
        font-weight: 500;
        color: {config.text_secondary};
        transition: {config.transition};
    }}
    .nav-link:hover {{
        background: {config.accent_color}15;
    }}
    .nav-link.active {{
        color: {config.accent_color};
        font-weight: 600;
    }}
    .nav-primary {{
        background: {config.accent_color} !important;
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Render navigation
    cols = st.columns([2,2,2,2,1.5])
    for idx, page in enumerate(pages):
        with cols[idx]:
            if page.get("type") == "primary":
                st.link_button(
                    f"{page['icon']} {page['name']}",
                    f"?page={page['key']}",
                    type="primary",
                    use_container_width=True
                )
            else:
                is_active = current_page == page['key']
                st.markdown(
                    f"""
                    <a href="?page={page['key']}" 
                       class="nav-link {'active' if is_active else ''}">
                       {page['icon']} {page['name']}
                    </a>
                    """,
                    unsafe_allow_html=True
                )
    
    st.markdown("---")
