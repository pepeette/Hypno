"""
Simplified styling module for the Hypnotherapy website
Ensures all CSS loads properly without conflicts
"""
import streamlit as st

def apply_global_styles():
    """Apply essential global styles in a single, comprehensive block"""
    
    css_styles = """
    <style>
    /* Reset and base styles */
    * {
        box-sizing: border-box;
    }
    
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
        --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
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
    
    /* Typography */
    h1 {
        color: var(--text-primary) !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        margin-bottom: 1.5rem !important;
    }
    
    h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
        margin-bottom: 1.2rem !important;
    }
    
    p, li, span, div {
        color: var(--text-secondary) !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        transition: var(--transition) !important;
        cursor: pointer !important;
    }
    
    .stButton > button:hover {
        background-color: var(--accent-hover) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Form elements */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Card components */
    .card {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: 2rem;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
        margin-bottom: 2rem;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 1.5rem !important;
        }
        
        .stColumns {
            flex-direction: column !important;
        }
    }
    </style>
    """
    
    st.markdown(css_styles, unsafe_allow_html=True)

def inject_custom_css():
    """Inject additional custom CSS for specific components"""
    st.markdown("""
    <style>
    /* Progress bars and animations */
    .progress-container {
        background: #e5e7eb;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, var(--accent) 0%, var(--accent-hover) 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Testimonial specific styles */
    .testimonial-card {
        background: var(--card-bg);
        border-left: 4px solid var(--accent);
        border-radius: var(--radius-md);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
    }
    
    /* Button variations */
    .btn {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        border-radius: var(--radius-sm);
        text-decoration: none;
        font-weight: 600;
        transition: var(--transition);
        cursor: pointer;
        border: none;
    }
    
    .btn-primary {
        background-color: var(--accent);
        color: white;
    }
    
    .btn-primary:hover {
        background-color: var(--accent-hover);
        transform: translateY(-1px);
    }
    
    .btn-secondary {
        background-color: transparent;
        color: var(--accent);
        border: 2px solid var(--accent);
    }
    
    .btn-secondary:hover {
        background-color: var(--accent);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
