"""
Enhanced styling module for the Hypnotherapy website
Clean, professional design with forced light mode and 3 font sizes only
"""
import streamlit as st

def apply_global_styles():
    """Apply enhanced global styles for professional, engaging design"""
    
    st.markdown("""
    <style>
    /* Force Light Mode - No Dark Mode */
    :root {
        color-scheme: light !important;
    }
    
    html, body, .stApp, [data-testid="stApp"] {
        color-scheme: light !important;
        background-color: #F3F6F8 !important;
    }
    
    /* CSS Variables for Consistency */
    :root {
        /* Core Colors */
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
        
        /* Border Radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        
        /* STRICT TYPOGRAPHY - ONLY 3 SIZES */
        --font-size-h1: 2.2rem;      /* Main titles only */
        --font-size-h2: 1.8rem;      /* Section headers */
        --font-size-body: 1rem;      /* All body text */
        
        --line-height-tight: 1.3;
        --line-height-normal: 1.6;
        
        /* Transitions */
        --transition: all 0.3s ease;
    }
    
    /* App Background */
    .stApp {
        background-color: var(--bg) !important;
        color: var(--text-primary) !important;
    }
    
    /* STRICT TYPOGRAPHY RULES - NO TEXT SHADOWS */
    h1, [data-testid="stMarkdownContainer"] h1 {
        font-size: var(--font-size-h1) !important;
        line-height: var(--line-height-tight) !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        text-shadow: none !important;
    }
    
    h2, h3, h4, h5, h6, 
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4,
    [data-testid="stMarkdownContainer"] h5,
    [data-testid="stMarkdownContainer"] h6 {
        font-size: var(--font-size-h2) !important;
        line-height: var(--line-height-tight) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        margin-bottom: 1.2rem !important;
        text-shadow: none !important;
    }
    
    p, li, span, div, a, button, input, textarea, select, label,
    .stMarkdown, .stText, [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stText"],
    .stSelectbox label, .stTextInput label, .stTextArea label {
        font-size: var(--font-size-body) !important;
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
    
    .card-elevated {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: 2rem;
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border);
        transition: var(--transition);
        margin-bottom: 2rem;
    }
    
    .card-elevated:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-lg);
    }
    
    /* Hero Sections */
    .hero {
        background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
        padding: 3rem 2rem;
        border-radius: var(--radius-lg);
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-sm);
    }
    
    /* Button System - Enhanced */
    .stButton > button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        cursor: pointer !important;
        border: none !important;
        font-size: var(--font-size-body) !important;
        text-shadow: none !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%) !important;
        color: white !important;
        box-shadow: var(--shadow-accent) !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(76, 161, 163, 0.4) !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: var(--card-bg) !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border) !important;
    }
    
    .stButton > button[kind="secondary"]:hover {
        border-color: var(--accent) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Form Elements */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > select,
    .stTextArea > div > textarea {
        background-color: white !important;
        border: 2px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.75rem 1rem !important;
        transition: var(--transition) !important;
        font-size: var(--font-size-body) !important;
    }
    
    .stTextInput > div > div > input:focus, 
    .stSelectbox > div > div > select:focus,
    .stTextArea > div > textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(76, 161, 163, 0.1) !important;
        outline: none !important;
    }
    
    /* Quiz Specific Styles */
    .quiz-option {
        background: var(--card-bg);
        border: 2px solid var(--border);
        border-radius: var(--radius-md);
        padding: 1.5rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
        min-height: 80px;
    }
    
    .quiz-option:hover {
        border-color: var(--accent);
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        background: rgba(76, 161, 163, 0.02);
    }
    
    .progress-container {
        width: 100%;
        height: 8px;
        background: var(--border);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, var(--accent) 0%, var(--accent-hover) 100%);
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Testimonial Cards */
    .testimonial-card {
        border-left: 4px solid var(--accent);
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        margin: 1rem 0;
        box-shadow: var(--shadow-sm);
        border-top: 1px solid var(--border);
        border-right: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
    }
    
    /* Navigation Enhancement */
    .stSelectbox > div > div {
        background-color: var(--card-bg) !important;
    }
    
    /* Success/Error States */
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid var(--success) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid var(--error) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    .stWarning {
        background-color: rgba(234, 179, 8, 0.1) !important;
        border: 1px solid var(--warning) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    .stInfo {
        background-color: rgba(76, 161, 163, 0.1) !important;
        border: 1px solid var(--accent) !important;
        border-radius: var(--radius-sm) !important;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Mobile Responsive */
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
        
        .card, .card-elevated {
            padding: 1.5rem;
        }
        
        .quiz-option {
            padding: 1rem;
            min-height: 60px;
        }
    }
    
    /* Animations for Engagement */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Custom Link Styling */
    a {
        color: var(--accent);
        text-decoration: none;
        transition: var(--transition);
    }
    
    a:hover {
        color: var(--accent-hover);
        text-decoration: underline;
    }
    
    /* Custom Button Classes */
    .btn {
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background: var(--accent);
        color: white;
        border-radius: var(--radius-sm);
        text-decoration: none;
        font-weight: 600;
        transition: var(--transition);
        border: none;
        cursor: pointer;
        font-size: var(--font-size-body);
    }
    
    .btn:hover {
        background: var(--accent-hover);
        transform: translateY(-1px);
        box-shadow: var(--shadow-accent);
        color: white;
        text-decoration: none;
    }
    
    .btn-secondary {
        background: var(--card-bg);
        color: var(--text-primary);
        border: 2px solid var(--border);
    }
    
    .btn-secondary:hover {
        border-color: var(--accent);
        color: var(--accent);
    }
    
    .btn-success {
        background: var(--success);
    }
    
    .btn-success:hover {
        background: #16a34a;
    }
    </style>
    """, unsafe_allow_html=True)
