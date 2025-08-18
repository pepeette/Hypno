"""
Styling module for the Hypnotherapy website
Clean, professional design with forced light mode and 3 font sizes only
Enforces clean design system with only 3 font sizes and no text shadows
"""

import streamlit as st

def apply_global_styles():
    """Apply all global styles to the Streamlit app - FIXED VERSION"""
    
    st.markdown("""
    <style>
    /* Force light mode and CSS Variables */
    :root {
        color-scheme: light;
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
        --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s ease;
    }
    
    html, body, .stApp {
        color-scheme: light !important;
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO TEXT SHADOWS */
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
    
    p, li, span, div, a, button, input, textarea, select, label {
        font-size: 1rem !important;
        line-height: 1.6 !important;
        color: var(--text-secondary) !important;
        text-shadow: none !important;
    }
    
    /* Card Components */
    .card {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: 2rem;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
        transition: var(--transition);
        margin-bottom: 2rem;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
        padding: 3rem 2rem;
        border-radius: var(--radius-lg);
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-sm);
    }
    
    /* Button System */
    .stButton>button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.5rem !important;
        cursor: pointer !important;
        border: none !important;
        font-size: 1rem !important;
    }
    
    .stButton>button[kind="primary"] {
        background-color: var(--accent) !important;
        color: white !important;
    }
    
    .stButton>button[kind="primary"]:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px);
    }
    
    /* Form Elements */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.5rem 1rem !important;
        transition: var(--transition) !important;
        font-size: 1rem !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
    }
    
    /* Testimonial Cards */
    .testimonial-card {
        border-left: 4px solid var(--accent);
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile Typography */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem !important;
        }
        h2, h3, h4, h5, h6 {
            font-size: 1.5rem !important;
        }
        .hero {
            padding: 2rem 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
