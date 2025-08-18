"""
Styling System
Clean, professional styling using Streamlit-friendly CSS
Focus on 3 font sizes, no text shadows, minimal bold usage
"""
import streamlit as st

def apply_styles():
    """Apply clean, professional styling for the hypnotherapy website"""
    st.markdown("""
    <style>
    /* CSS Variables - Professional Color Palette */
    :root {
        --bg: #F3F6F8;
        --card-bg: #FFFFFF;
        --text-primary: #273548;
        --text-secondary: #556D7A;
        --accent: #4CA1A3;
        --accent-hover: #3B7A7A;
        --border: #CBD5E1;
        --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
        --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --transition: all 0.3s ease;
    }
    
    /* Force Light Mode - Even for Dark Mode Users */
    html, body, .stApp {
        color-scheme: light !important;
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    }
    
    /* Typography System - ONLY 3 Sizes, No Text Shadows */
    h1 {
        font-size: 2.5rem !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        line-height: 1.2 !important;
        margin-bottom: 1.5rem !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: 1.875rem !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        text-shadow: none !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
    }
    
    p, li, span, div, a, button, input, textarea, select, label {
        font-size: 1rem !important;
        color: var(--text-secondary) !important;
        line-height: 1.6 !important;
        text-shadow: none !important;
    }
    
    /* Selective Bold Usage - Only When Necessary */
    strong {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }
    
    /* Streamlit Button Styling */
    .stButton>button {
        background-color: var(--accent) !important;
        color: white !important;
        border-radius: var(--radius-sm) !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        font-size: 1rem !important;
        transition: var(--transition) !important;
        cursor: pointer !important;
    }
    
    .stButton>button:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px);
        box-shadow: var(--shadow-accent);
    }
    
    .stButton>button:not([kind="primary"]) {
        background-color: white !important;
        color: var(--accent) !important;
        border: 1px solid var(--accent) !important;
    }
    
    .stButton>button:not([kind="primary"]):hover {
        background-color: #F0FDFA !important;
    }
    
    /* Streamlit Form Elements */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select,
    .stTextArea>div>textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        transition: var(--transition) !important;
    }
    
    .stTextInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
        outline: none !important;
    }
    
    /* Streamlit Metrics */
    .metric-container {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
    }
    
    /* Streamlit Progress Bar */
    .stProgress .st-bo {
        background-color: var(--accent) !important;
    }
    
    /* Streamlit Success/Info/Error */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid #22c55e !important;
        color: #15803d !important;
    }
    
    .stInfo {
        background-color: rgba(76, 161, 163, 0.1) !important;
        border: 1px solid var(--accent) !important;
        color: var(--accent-hover) !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid #ef4444 !important;
        color: #dc2626 !important;
    }
    
    /* Streamlit Expander */
    .streamlit-expanderHeader {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    /* Custom Hero Component */
    .hero-section {
        background: linear-gradient(135deg, var(--accent) 0%, #F0FDFA 100%);
        padding: 4rem 2rem;
        border-radius: var(--radius-lg);
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: var(--shadow-sm);
    }
    
    .hero-section h1 {
        color: white !important;
        margin-bottom: 1rem;
    }
    
    .hero-section p {
        color: white !important;
        opacity: 0.95;
        font-size: 1.2rem !important;
    }
    
    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem !important;
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 1.5rem !important;
        }
        
        .hero-section {
            padding: 2.5rem 1.5rem;
        }
        
        .stButton>button {
            padding: 0.6rem 1.5rem !important;
            font-size: 0.9rem !important;
        }
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    </style>
    """, unsafe_allow_html=True)

def render_hero_section(title, subtitle):
    """Render hero section using minimal HTML + Streamlit"""
    st.markdown(f"""
    <div class="hero-section">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_section_divider():
    """Render clean section divider"""
    st.markdown("---")

def render_highlight_box(content, box_type="info"):
    """Render highlighted content box"""
    if box_type == "info":
        st.info(content)
    elif box_type == "success":
        st.success(content)
    elif box_type == "warning":
        st.warning(content)
    else:
        st.info(content)
