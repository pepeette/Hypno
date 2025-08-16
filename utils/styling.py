"""
Styling module for the Hypnotherapy website
Centralizes all CSS styling and design system
"""
import streamlit as st

def apply_global_styles():
    """Apply all global styles to the Streamlit app"""
    
    # FIXED: Apply CSS in a single block to ensure it loads
    st.markdown("""
    <style>
    /* CSS Variables - FIXED VERSION */
    :root {
        /* Colors */
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
        
        /* Shadows */
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
        --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
        --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        
        /* Border radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        
        /* Typography - EXACTLY 3 SIZES */
        --font-size-large: 2.2rem;    /* Only for main titles */
        --font-size-medium: 1.8rem;   /* For headers */
        --font-size-normal: 1rem;     /* For all body text */
        
        --line-height-tight: 1.3;
        --line-height-normal: 1.6;
        
        /* Transitions */
        --transition: all 0.3s ease;
    }
    
    /* Force light mode */
    html, body, [class*="st"] {
        color-scheme: light !important;
    }
    
    .stApp {
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO TEXT SHADOWS */
    h1 {
        font-size: var(--font-size-large) !important;
        line-height: var(--line-height-tight) !important;
        margin-bottom: 1.5rem !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-shadow: none !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: var(--font-size-medium) !important;
        line-height: var(--line-height-tight) !important;
        margin-bottom: 1.2rem !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }
    
    p, li, span, div, a, button, input, textarea, select, label, .stMarkdown, .stText {
        font-size: var(--font-size-normal) !important;
        line-height: var(--line-height-normal) !important;
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
        font-size: var(--font-size-normal) !important;
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
        font-size: var(--font-size-normal) !important;
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
