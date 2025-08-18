"""
Styling module for the Hypnotherapy website
Clean CSS with only 3 font sizes, no text shadows, light mode only
"""
import streamlit as st

def apply_global_styles():
    """Apply clean global styles - 3 font sizes only, no shadows"""
    
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
        --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        
        /* Border radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        
        /* Transitions */
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
    
    /* STREAMLIT METRIC STYLING */
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
    
    /* STREAMLIT PROGRESS BAR */
    .stProgress .st-bo {
        background-color: var(--accent) !important;
    }
    
    /* STREAMLIT CONTAINERS */
    .stContainer {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* STREAMLIT EXPANDER */
    .streamlit-expanderHeader {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    /* STREAMLIT SUCCESS/ERROR/WARNING/INFO */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: var(--radius-sm) !important;
        border: none !important;
        padding: 1rem !important;
    }
    
    /* STREAMLIT TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--card-bg);
        border-radius: var(--radius-sm);
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: transparent;
        border-radius: var(--radius-sm);
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--accent) !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    /* STREAMLIT QUOTE */
    .stMarkdown blockquote {
        border-left: 4px solid var(--accent);
        padding: 1rem;
        margin: 1rem 0;
        background-color: rgba(76, 161, 163, 0.05);
        border-radius: var(--radius-sm);
        font-style: italic;
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
        
        .stButton>button {
            padding: 0.6rem 1.5rem !important;
        }
        
        .stMetric {
            padding: 0.75rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)
