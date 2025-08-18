"""
FIXED Styling module for the Hypnotherapy website
Enforces ONLY 3 font sizes, no text shadows, consistent variables
"""
import streamlit as st

def apply_global_styles():
    """Apply all global styles with STRICT typography enforcement"""
    
    st.markdown("""
    <style>
    /* FORCE LIGHT MODE FOR ALL USERS */
    :root {
        color-scheme: light !important;
    }
    
    html, body, [class*="st"] {
        color-scheme: light !important;
    }
    
    .stApp {
        background-color: #F3F6F8 !important;
        color: #273548 !important;
    }
    
    /* CSS VARIABLES - CONSISTENT ACROSS ALL COMPONENTS */
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
        --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        
        --transition: all 0.3s ease;
    }
    
    /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO SHADOWS */
    h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        text-shadow: none !important;
        line-height: 1.3 !important;
        margin-bottom: 1.5rem !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        text-shadow: none !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
    }
    
    p, li, span, div, a, button, input, textarea, select, label, 
    .stMarkdown, .stText, .stSelectbox, .stTextInput, .stTextArea {
        font-size: 1rem !important;
        color: var(--text-secondary) !important;
        text-shadow: none !important;
        line-height: 1.6 !important;
    }
    
    /* SELECTIVE BOLD USAGE */
    strong {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }
    
    /* CARD SYSTEM */
    .card {
        background: var(--card-bg) !important;
        border-radius: var(--radius-md) !important;
        padding: 2rem !important;
        box-shadow: var(--shadow-sm) !important;
        border: 1px solid var(--border) !important;
        transition: var(--transition) !important;
        margin-bottom: 2rem !important;
    }
    
    .card:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    /* STREAMLIT BUTTON STYLING */
    .stButton>button {
        background-color: var(--accent) !important;
        color: white !important;
        border-radius: var(--radius-sm) !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        font-size: 1rem !important;
        transition: var(--transition) !important;
    }
    
    .stButton>button:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px) !important;
    }
    
    .stButton>button[kind="primary"] {
        background-color: var(--accent) !important;
    }
    
    .stButton>button[kind="secondary"] {
        background-color: var(--border) !important;
        color: var(--text-primary) !important;
    }
    
    /* FORM ELEMENTS */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>textarea {
        background-color: var(--card-bg) !important;
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
    }
    
    /* METRICS */
    .stMetric {
        background: var(--card-bg) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        border: 1px solid var(--border) !important;
    }
    
    /* COLUMNS AND CONTAINERS */
    .stContainer {
        max-width: 1200px !important;
        margin: 0 auto !important;
    }
    
    /* HIDE STREAMLIT BRANDING */
    #MainMenu, footer, header {
        visibility: hidden !important;
    }
    
    /* MOBILE RESPONSIVENESS */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 1.5rem !important;
        }
        
        .card {
            padding: 1.5rem !important;
        }
        
        .stButton>button {
            padding: 0.6rem 1.5rem !important;
        }
    }
    
    /* PROGRESS BAR */
    .stProgress .st-bo {
        background-color: var(--accent) !important;
    }
    
    /* SUCCESS/ERROR MESSAGES */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border-left: 4px solid var(--success) !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border-left: 4px solid var(--error) !important;
    }
    
    .stWarning {
        background-color: rgba(234, 179, 8, 0.1) !important;
        border-left: 4px solid var(--warning) !important;
    }
    
    .stInfo {
        background-color: rgba(76, 161, 163, 0.1) !important;
        border-left: 4px solid var(--accent) !important;
    }
    
    /* TESTIMONIAL STYLING */
    .testimonial-card {
        border-left: 4px solid var(--accent) !important;
        background: var(--card-bg) !important;
        padding: 1.5rem !important;
        border-radius: var(--radius-md) !important;
        margin: 1rem 0 !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    /* EXPANDER STYLING */
    .streamlit-expanderHeader {
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)
