# """
# Fixed styling module with better button colors and readability
# """
# import streamlit as st

# def apply_global_styles():
#     """Apply clean global styles with better button colors"""
    
#     st.markdown("""
#     <style>
#     /* FORCE LIGHT MODE ONLY */
#     :root {
#         color-scheme: light !important;
#     }
    
#     html, body, [class*="st"] {
#         color-scheme: light !important;
#     }
    
#     .stApp {
#         background-color: #F3F6F8 !important;
#         color: #273548 !important;
#     }
    
#     /* CSS VARIABLES */
#     :root {
#         /* Colors */
#         --bg: #F3F6F8;
#         --card-bg: #FFFFFF;
#         --text-primary: #273548;
#         --text-secondary: #556D7A;
#         --accent: #4CA1A3;
#         --accent-hover: #3B7A7A;
#         --border: #CBD5E1;
#         --success: #22c55e;
#         --warning: #eab308;
#         --error: #ef4444;
        
#         /* Shadows */
#         --shadow-sm: 0 2px 8px rgba(0,0,0,0.05);
#         --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
#         --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        
#         /* Border radius */
#         --radius-sm: 8px;
#         --radius-md: 12px;
#         --radius-lg: 16px;
        
#         /* Transitions */
#         --transition: all 0.3s ease;
#     }
    
#     /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO SHADOWS */
#     h1 {
#         font-size: 1.875rem !important;
#         line-height: 1.3 !important;
#         margin-bottom: 1.5rem !important;
#         color: var(--text-primary) !important;
#         font-weight: 700 !important;
#         text-shadow: none !important;
#     }
    
#     h2, h3, h4, h5, h6 {
#         font-size: 1.5rem !important;
#         line-height: 1.3 !important;
#         margin-bottom: 1.2rem !important;
#         color: var(--text-primary) !important;
#         font-weight: 600 !important;
#         text-shadow: none !important;
#     }
    
#     /* ALL TEXT ELEMENTS USE SAME BASE SIZE */
#     p, li, span, div, a, button, input, textarea, select, label, 
#     .stMarkdown, .stText, .stSelectbox, .stTextInput, .stTextArea {
#         font-size: 1rem !important;
#         line-height: 1.6 !important;
#         color: var(--text-secondary) !important;
#         text-shadow: none !important;
#     }
    
#     /* MINIMAL BOLD USAGE */
#     strong, b {
#         font-weight: 600 !important;
#         color: var(--text-primary) !important;
#     }
 
#     /* FIXED STREAMLIT BUTTON STYLING - Better contrast */
#     .stButton>button {
#         border-radius: var(--radius-sm) !important;
#         transition: var(--transition) !important;
#         font-weight: 600 !important;
#         padding: 0.75rem 2rem !important;
#         cursor: pointer !important;
#         font-size: 1rem !important;
#         border: 2px solid var(--border) !important;
#     }
    
#     /* PRIMARY BUTTONS - Dark background with WHITE text (FIXED) */
#     .stButton>button[kind="primary"] {
#         background-color: var(--accent) !important;
#         color: white !important;
#         border: 2px solid var(--accent) !important;
#     }
    
#     .stButton>button[kind="primary"]:hover {
#         background-color: var(--accent-hover) !important;
#         border-color: var(--accent-hover) !important;
#         color: white !important;
#         transform: translateY(-1px);
#     }
    
#     /* SECONDARY BUTTONS - White background with dark text */
#     .stButton>button[kind="secondary"] {
#         background-color: white !important;
#         color: var(--text-primary) !important;
#         border: 2px solid var(--border) !important;
#     }
    
#     .stButton>button[kind="secondary"]:hover {
#         background-color: var(--bg) !important;
#         border-color: var(--accent) !important;
#         color: var(--accent) !important;
#     }
    
#     /* DEFAULT BUTTONS - White background with dark text and border */
#     .stButton>button:not([kind]) {
#         background-color: white !important;
#         color: var(--text-primary) !important;
#         border: 2px solid var(--border) !important;
#     }
    
#     .stButton>button:not([kind]):hover {
#         background-color: var(--bg) !important;
#         border-color: var(--accent) !important;
#         color: var(--accent) !important;
#     }
    
#     /* FORM ELEMENTS */
#     .stTextInput>div>div>input, 
#     .stSelectbox>div>div>select,
#     .stTextArea>div>textarea {
#         background-color: white !important;
#         border: 1px solid var(--border) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 0.75rem 1rem !important;
#         transition: var(--transition) !important;
#         font-size: 1rem !important;
#         color: var(--text-primary) !important;
#     }
    
#     .stTextInput>div>div>input:focus, 
#     .stSelectbox>div>div>select:focus,
#     .stTextArea>div>textarea:focus {
#         border-color: var(--accent) !important;
#         box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
#     }
    
#     /* STREAMLIT METRIC STYLING - Custom override */
#     .stMetric {
#         background: white !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#         border: 1px solid var(--border) !important;
#         text-align: center !important;
#     }
    
#     .stMetric [data-testid="metric-value"] {
#         font-size: 2rem !important;
#         font-weight: 700 !important;
#         color: var(--accent) !important;
#     }
    
#     .stMetric [data-testid="metric-label"] {
#         font-size: 1rem !important;
#         color: var(--text-secondary) !important;
#         font-weight: 600 !important;
#     }
    
#     .stMetric [data-testid="metric-delta"] {
#         font-size: 1rem !important;
#         color: var(--text-secondary) !important;
#         font-weight: 500 !important;
#     }
    
#     /* STREAMLIT PROGRESS BAR */
#     .stProgress .st-bo {
#         background-color: var(--accent) !important;
#     }
    
#     /* STREAMLIT EXPANDER - Better styling */
#     .streamlit-expanderHeader {
#         background-color: white !important;
#         border: 1px solid var(--border) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#     }
    
#     .streamlit-expanderHeader:hover {
#         border-color: var(--accent) !important;
#     }
    
#     /* STREAMLIT SUCCESS/ERROR/WARNING/INFO - Better readability */
#     .stSuccess {
#         background-color: rgba(34, 197, 94, 0.1) !important;
#         border: 1px solid var(--success) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#         color: var(--text-primary) !important;
#     }
    
#     .stError {
#         background-color: rgba(239, 68, 68, 0.1) !important;
#         border: 1px solid var(--error) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#         color: var(--text-primary) !important;
#     }
    
#     .stWarning {
#         background-color: rgba(234, 179, 8, 0.1) !important;
#         border: 1px solid var(--warning) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#         color: var(--text-primary) !important;
#     }
    
#     .stInfo {
#         background-color: white !important;
#         border: 1px solid var(--accent) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: 1rem !important;
#         color: var(--text-primary) !important;
#     }
    
#     /* STREAMLIT TABS - Remove background colors for readability */
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 8px;
#         background-color: transparent !important;
#         border-bottom: 1px solid var(--border);
#         padding: 0.5rem 0;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         height: 50px;
#         padding: 0px 24px;
#         background-color: transparent !important;
#         border-radius: var(--radius-sm) !important;
#         color: var(--text-secondary) !important;
#         font-weight: 500 !important;
#         border: 1px solid var(--border) !important;
#         margin-right: 8px;
#     }
    
#     .stTabs [aria-selected="true"] {
#         background-color: white !important;
#         color: var(--accent) !important;
#         font-weight: 600 !important;
#         border-color: var(--accent) !important;
#     }
    
#     /* STREAMLIT QUOTE - Better styling */
#     .stMarkdown blockquote {
#         border-left: 4px solid var(--accent);
#         padding: 1rem;
#         margin: 1rem 0;
#         background-color: rgba(76, 161, 163, 0.05);
#         border-radius: var(--radius-sm);
#         font-style: italic;
#         color: var(--text-primary) !important;
#     }
    
#     /* HIDE STREAMLIT ELEMENTS */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
    
#     /* MOBILE RESPONSIVE */
#     @media (max-width: 768px) {
#         h1 {
#             font-size: 1.5rem !important;
#         }
        
#         h2, h3, h4, h5, h6 {
#             font-size: 1.25rem !important;
#         }
        
#         .stButton>button {
#             padding: 0.6rem 1.5rem !important;
#         }
        
#         .stMetric {
#             padding: 0.75rem;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             padding: 8px 12px;
#             margin-right: 4px;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)



"""
Enhanced styling module for the Hypnotherapy website
Improved spacing, typography, and visual hierarchy
"""
import streamlit as st

def apply_global_styles():
    """Apply all global styles with improved spacing and typography"""
    
    st.markdown("""
    <style>
    /* CSS Variables - Enhanced for better spacing */
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
        
        /* Spacing System */
        --space-xs: 0.5rem;
        --space-sm: 1rem;
        --space-md: 1.5rem;
        --space-lg: 2rem;
        --space-xl: 3rem;
        --space-xxl: 4rem;
        
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
    
    /* Main container improvements */
    .main .block-container {
        padding-top: var(--space-lg);
        padding-bottom: var(--space-sm);
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO TEXT SHADOWS */
    h1 {
        font-size: var(--font-size-large) !important;
        line-height: var(--line-height-tight) !important;
        margin-bottom: var(--space-md) !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-shadow: none !important;
    }
    
    h2, h3, h4, h5, h6 {
        font-size: var(--font-size-medium) !important;
        line-height: var(--line-height-tight) !important;
        margin-bottom: var(--space-sm) !important;
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
    
    /* Improved section spacing */
    .stMarkdown {
        margin-bottom: var(--space-sm);
    }
    
    .stMarkdown:has(h1), .stMarkdown:has(h2) {
        margin-bottom: var(--space-md);
    }
    
    /* Card Components with better spacing */
    .card {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: var(--space-lg);
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
        transition: var(--transition);
        margin-bottom: var(--space-lg);
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    .card-elevated {
        background: var(--card-bg);
        border-radius: var(--radius-md);
        padding: var(--space-xl);
        box-shadow: var(--shadow-md);
        border: 1px solid var(--border);
        transition: var(--transition);
        margin-bottom: var(--space-xl);
    }
    
    .card-elevated:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-lg);
    }
    
    /* Hero Section with improved spacing */
    .hero {
        background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
        padding: var(--space-xxl) var(--space-lg);
        border-radius: var(--radius-lg);
        text-align: center;
        margin-bottom: var(--space-xl);
        box-shadow: var(--shadow-sm);
    }
    
    /* Button System with better spacing */
    .stButton {
        margin: var(--space-xs) 0;
    }
    
    .stButton>button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: var(--space-sm) var(--space-md) !important;
        cursor: pointer !important;
        border: none !important;
        font-size: var(--font-size-normal) !important;
        margin: var(--space-xs) 0 !important;
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
    
    /* Form Elements with improved spacing */
    .stForm {
        margin: var(--space-lg) 0;
        padding: var(--space-lg);
        background: var(--card-bg);
        border-radius: var(--radius-md);
        border: 1px solid var(--border);
    }
    
    .stTextInput, .stSelectbox, .stTextArea {
        margin-bottom: var(--space-sm);
    }
    
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>textarea {
        background-color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: var(--space-sm) var(--space-sm) !important;
        transition: var(--transition) !important;
        font-size: var(--font-size-normal) !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stSelectbox>div>div>select:focus,
    .stTextArea>div>textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
    }
    
    /* Column spacing improvements */
    .stColumns {
        gap: var(--space-lg);
    }
    
    .stColumns[data-testid="column"] {
        padding: 0 var(--space-xs);
    }
    
    /* Testimonial Cards with better spacing */
    .testimonial-card {
        border-left: 4px solid var(--accent);
        background: var(--card-bg);
        padding: var(--space-lg);
        border-radius: var(--radius-md);
        margin: var(--space-lg) 0;
        box-shadow: var(--shadow-sm);
    }
    
    /* Metrics with improved spacing */
    .stMetric {
        background: var(--card-bg);
        padding: var(--space-md);
        border-radius: var(--radius-sm);
        border: 1px solid var(--border);
        text-align: center;
    }
    
    /* Info boxes with better spacing */
    .stInfo, .stSuccess, .stWarning, .stError {
        margin: var(--space-md) 0;
        padding: var(--space-md);
        border-radius: var(--radius-sm);
    }
    
    /* Navigation improvements */
    .streamlit-option-menu {
        margin-bottom: var(--space-xl);
    }
    
    /* Divider spacing */
    hr {
        margin: var(--space-xl) 0;
        border: none;
        border-top: 1px solid var(--border);
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile Typography and Spacing */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: var(--space-sm);
            padding-right: var(--space-sm);
            padding-top: var(--space-sm);
        }
        
        h1 {
            font-size: 1.8rem !important;
        }
        
        h2, h3, h4, h5, h6 {
            font-size: 1.5rem !important;
        }
        
        .hero {
            padding: var(--space-lg) var(--space-md);
        }
        
        .card, .card-elevated {
            padding: var(--space-md);
            margin-bottom: var(--space-md);
        }
        
        .stColumns {
            gap: var(--space-sm);
        }
        
        /* Stack columns on mobile */
        .stColumns[data-testid="column"] {
            margin-bottom: var(--space-sm);
        }
    }
    
    /* Tablet adjustments */
    @media (max-width: 1024px) and (min-width: 769px) {
        .main .block-container {
            max-width: 100%;
            padding-left: var(--space-md);
            padding-right: var(--space-md);
        }
    }
    
    /* Print styles */
    @media print {
        .stButton, .streamlit-option-menu {
            display: none !important;
        }
        
        .main .block-container {
            max-width: 100%;
            padding: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)
