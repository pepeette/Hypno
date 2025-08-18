"""
Clean styling module for the Hypnotherapy website
STRICT: Only 3 font sizes, no text shadows, minimal bold, light mode only
"""
import streamlit as st

def apply_global_styles():
    """Apply clean, consistent styling - 3 font sizes only"""
    
    st.markdown("""
    <style>
    /* FORCE LIGHT MODE ONLY */
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
    
    /* CSS VARIABLES */
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
        font-size: 1.875rem !important;
        line-height: 1.3 !important;
        margin-bottom: 1.5rem !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-shadow: none !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: 1.5rem !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }
    
    /* ALL TEXT ELEMENTS USE SAME BASE SIZE */
    p, li, span, div, a, button, input, textarea, select, label, 
    .stMarkdown, .stText, .stSelectbox, .stTextInput, .stTextArea {
        font-size: 1rem !important;
        line-height: 1.6 !important;
        color: var(--text-secondary) !important;
        text-shadow: none !important;
    }
    
    /* MINIMAL BOLD USAGE */
    strong, b {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }
    
    /* CARD COMPONENTS */
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
    
    /* STREAMLIT BUTTON STYLING */
    .stButton>button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
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
    
    .stButton>button[kind="secondary"] {
        background-color: transparent !important;
        color: var(--accent) !important;
        border: 2px solid var(--accent) !important;
    }
    
    .stButton>button[kind="secondary"]:hover {
        background-color: var(--accent) !important;
        color: white !important;
    }
    
    /* FORM ELEMENTS */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.75rem 1rem !important;
        transition: var(--transition) !important;
        font-size: 1rem !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
    }
    
    /* METRIC STYLING */
    .stMetric {
        background: var(--card-bg);
        border-radius: var(--radius-sm);
        padding: 1rem;
        border: 1px solid var(--border);
        text-align: center;
    }
    
    .stMetric [data-testid="metric-value"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: var(--accent) !important;
    }
    
    .stMetric [data-testid="metric-label"] {
        font-size: 1rem !important;
        color: var(--text-secondary) !important;
        font-weight: 600 !important;
    }
    
    /* PROGRESS BAR */
    .stProgress .st-bo {
        background-color: var(--accent) !important;
    }
    
    /* TESTIMONIAL CARDS */
    .testimonial-card {
        border-left: 4px solid var(--accent);
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
    }
    
    /* HIDE STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* MOBILE RESPONSIVE */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 1.25rem !important;
        }
        
        .card {
            padding: 1.5rem;
        }
        
        .stButton>button {
            padding: 0.6rem 1.5rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
