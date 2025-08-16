"""
Styling module for the Hypnotherapy website
EXACTLY 3 font sizes, NO text shadows
"""
import streamlit as st

def apply_global_styles():
    """Apply global styles - 3 font sizes only, no shadows"""
    
    st.markdown("""
    <style>
    /* CSS Variables */
    :root {
        --bg: #F3F6F8;
        --card-bg: #FFFFFF;
        --text-primary: #273548;
        --text-secondary: #556D7A;
        --accent: #4CA1A3;
        --accent-hover: #3B7A7A;
        --border: #CBD5E1;
        --success: #22c55e;
        --warning: #eab308;
        --error: #ef4444;
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s ease;
    }
    
    /* Force light mode */
    .stApp {
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    /* EXACTLY 3 FONT SIZES - NO SHADOWS */
    h1 {
        font-size: 2.2rem !important;
        line-height: 1.3 !important;
        margin-bottom: 1.5rem !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-shadow: none !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: 1.8rem !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }
    
    p, li, span, div, a, button, input, textarea, select, label, 
    .stMarkdown, .stText, blockquote {
        font-size: 1rem !important;
        line-height: 1.6 !important;
        color: var(--text-secondary) !important;
        text-shadow: none !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        text-shadow: none !important;
        transition: var(--transition) !important;
    }
    
    .stButton > button:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Forms */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 1rem !important;
        text-shadow: none !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile - keep 3 sizes */
    @media (max-width: 768px) {
        h1 { font-size: 1.8rem !important; }
        h2, h3, h4, h5, h6 { font-size: 1.5rem !important; }
        /* p, etc. stay 1rem */
    }
    </style>
    """, unsafe_allow_html=True)
