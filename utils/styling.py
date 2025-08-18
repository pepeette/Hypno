"""
Enhanced styling module for the Hypnotherapy website
Clean, professional design with forced light mode and 3 font sizes only
Enforces clean design system with only 3 font sizes and no text shadows
"""
import streamlit as st

def apply_global_styles():
    """Apply enhanced global styles with strict design system"""
    
    st.markdown("""
    <style>
    /* FORCE LIGHT MODE - No Dark Mode Override */
    :root {
        color-scheme: light !important;
    }
    
    html, body, .stApp, [class*="st"] {
        color-scheme: light !important;
        background-color: #F3F6F8 !important;
    }
    
    /* CSS VARIABLES - Clean Design System */
    :root {
        /* Core Colors */
        --bg: #F3F6F8;
        --card-bg: #FFFFFF;
        --text-primary: #273548;
        --text-secondary: #556D7A;
        --accent: #4CA1A3;
        --accent-hover: #3B7A7A;
        --border: #CBD5E1;
