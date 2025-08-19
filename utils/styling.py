"""
Fixed styling module with better button colors and readability
"""
import streamlit as st

def apply_global_styles():
    """Apply clean global styles with better button colors"""
    
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
    
    /* FIXED STREAMLIT BUTTON STYLING - Better contrast */
    .stButton>button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        cursor: pointer !important;
        font-size: 1rem !important;
        border: 2px solid var(--border) !important;
    }
    
    /* PRIMARY BUTTONS - Dark background with white text */
    .stButton>button[kind="primary"] {
        background-color: var(--accent) !important;
        color: white !important;
        border: 2px solid var(--accent) !important;
    }
    
    .stButton>button[kind="primary"]:hover {
        background-color: var(--accent-hover) !important;
        border-color: var(--accent-hover) !important;
        transform: translateY(-1px);
    }
    
    /* SECONDARY BUTTONS - White background with dark text */
    .stButton>button[kind="secondary"] {
        background-color: white !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border) !important;
    }
    
    .stButton>button[kind="secondary"]:hover {
        background-color: var(--bg) !important;
        border-color: var(--accent) !important;
        color: var(--accent) !important;
    }
    
    /* DEFAULT BUTTONS - White background with dark text and border */
    .stButton>button:not([kind]) {
        background-color: white !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border) !important;
    }
    
    .stButton>button:not([kind]):hover {
        background-color: var(--bg) !important;
        border-color: var(--accent) !important;
        color: var(--accent) !important;
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
        color: var(--text-primary) !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
    }
    
    /* STREAMLIT METRIC STYLING - Custom override */
    .stMetric {
        background: white !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        border: 1px solid var(--border) !important;
        text-align: center !important;
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
    
    .stMetric [data-testid="metric-delta"] {
        font-size: 1rem !important;
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
    }
    
    /* STREAMLIT PROGRESS BAR */
    .stProgress .st-bo {
        background-color: var(--accent) !important;
    }
    
    /* STREAMLIT EXPANDER - Better styling */
    .streamlit-expanderHeader {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: var(--accent) !important;
    }
    
    /* STREAMLIT SUCCESS/ERROR/WARNING/INFO - Better readability */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid var(--success) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        color: var(--text-primary) !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid var(--error) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        color: var(--text-primary) !important;
    }
    
    .stWarning {
        background-color: rgba(234, 179, 8, 0.1) !important;
        border: 1px solid var(--warning) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        color: var(--text-primary) !important;
    }
    
    .stInfo {
        background-color: rgba(76, 161, 163, 0.1) !important;
        border: 1px solid var(--accent) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
        color: var(--text-primary) !important;
    }
    
    /* STREAMLIT TABS - Remove background colors for readability */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent !important;
        border-bottom: 1px solid var(--border);
        padding: 0.5rem 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: transparent !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        border: 1px solid var(--border) !important;
        margin-right: 8px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        color: var(--accent) !important;
        font-weight: 600 !important;
        border-color: var(--accent) !important;
    }
    
    /* STREAMLIT QUOTE - Better styling */
    .stMarkdown blockquote {
        border-left: 4px solid var(--accent);
        padding: 1rem;
        margin: 1rem 0;
        background-color: rgba(76, 161, 163, 0.05);
        border-radius: var(--radius-sm);
        font-style: italic;
        color: var(--text-primary) !important;
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
        
        .stTabs [data-baseweb="tab"] {
            padding: 8px 12px;
            margin-right: 4px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
