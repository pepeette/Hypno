# """
# Enhanced styling module for the Hypnotherapy website
# Improved spacing, typography, and visual hierarchy
# """
# import streamlit as st

# def apply_global_styles():
#     """Apply all global styles with improved spacing and typography"""
    
#     st.markdown("""
#     <style>
#     /* CSS Variables - Enhanced for better spacing */
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
#         --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
#         --shadow-accent: 0 2px 8px rgba(59, 122, 122, 0.2);
        
#         /* Border radius */
#         --radius-sm: 8px;
#         --radius-md: 12px;
#         --radius-lg: 16px;
        
#         /* Typography - EXACTLY 3 SIZES */
#         --font-size-large: 2.2rem;    /* Only for main titles */
#         --font-size-medium: 1.8rem;   /* For headers */
#         --font-size-normal: 1rem;     /* For all body text */
        
#         --line-height-tight: 1.3;
#         --line-height-normal: 1.6;
        
#         /* Spacing System */
#         --space-xs: 0.5rem;
#         --space-sm: 1rem;
#         --space-md: 1.5rem;
#         --space-lg: 2rem;
#         --space-xl: 3rem;
#         --space-xxl: 4rem;
        
#         /* Transitions */
#         --transition: all 0.3s ease;
#     }
    
#     /* Force light mode */
#     html, body, [class*="st"] {
#         color-scheme: light !important;
#     }
    
#     .stApp {
#         background-color: var(--bg) !important;
#         color: var(--text-primary) !important;
#     }
    
#     /* Main container improvements */
#     .main .block-container {
#         padding-top: var(--space-lg);
#         padding-bottom: var(--space-sm);
#         max-width: 1200px;
#         margin: 0 auto;
#     }
    
#     /* STRICT TYPOGRAPHY - ONLY 3 SIZES, NO TEXT SHADOWS */
#     h1 {
#         font-size: var(--font-size-large) !important;
#         line-height: var(--line-height-tight) !important;
#         margin-bottom: var(--space-md) !important;
#         color: var(--text-primary) !important;
#         font-weight: 700 !important;
#         text-shadow: none !important;
#     }
    
#     h2, h3, h4, h5, h6 {
#         font-size: var(--font-size-medium) !important;
#         line-height: var(--line-height-tight) !important;
#         margin-bottom: var(--space-sm) !important;
#         color: var(--text-primary) !important;
#         font-weight: 600 !important;
#         text-shadow: none !important;
#     }
    
#     p, li, span, div, a, input, textarea, select, label, .stMarkdown, .stText {
#         font-size: var(--font-size-normal) !important;
#         line-height: var(--line-height-normal) !important;
#         color: var(--text-secondary) !important;
#         text-shadow: none !important;
#     }
    
#     /* Exclude buttons from global text color rule */
#     button, button * {
#         color: inherit !important;
#     }

#     /* CTA Button Style - Primary (Accent background) */
#     .cta-button {
#         display: inline-block;
#         background-color: var(--accent);
#         color: #FFFFFF !important;
#         text-decoration: none;
#         /* Match Streamlit button padding and dimensions */
#         padding: var(--space-sm) var(--space-md) !important;
#         border-radius: var(--radius-sm) !important;
#         font-weight: 600 !important;
#         font-size: var(--font-size-normal) !important;
#         transition: var(--transition);
#         box-shadow: var(--shadow-sm);
#         text-align: center;
#         width: 100%;
#         box-sizing: border-box;
#         margin: var(--space-xs) 0 !important;
#         border: 2px solid var(--accent) !important;
#         cursor: pointer;
#         /* Additional Streamlit button properties */
#         min-height: 2.5rem;
#         vertical-align: middle;
#         line-height: 1.6;
#     }
    
#     /* CTA Button Style - Secondary (White background) */
#     .cta-button-secondary {
#         display: inline-block;
#         background-color: white;
#         color: var(--text-primary) !important;
#         text-decoration: none;
#         /* Match Streamlit button padding and dimensions */
#         padding: var(--space-sm) var(--space-md) !important;
#         border-radius: var(--radius-sm) !important;
#         font-weight: 600 !important;
#         font-size: var(--font-size-normal) !important;
#         transition: var(--transition);
#         box-shadow: var(--shadow-sm);
#         text-align: center;
#         width: 100%;
#         box-sizing: border-box;
#         margin: var(--space-xs) 0 !important;
#         border: 2px solid var(--border) !important;
#         cursor: pointer;
#         /* Additional Streamlit button properties */
#         min-height: 2.5rem;
#         vertical-align: middle;
#         line-height: 1.6;
#     }
    
#     /* Global link reset */
#     a {
#         text-decoration: none !important;
#         color: inherit;
#     }
    
#     a:hover {
#         text-decoration: none !important;
#     }

#     /* CTA Button Primary hover effect - light background */
#     .cta-button:hover {
#         background-color: #E1F0F0 !important;
#         color: #273548 !important;
#         border-color: #E1F0F0 !important;
#         transform: translateY(-1px);
#         box-shadow: 0 4px 12px rgba(243,246,248,0.6);
#     }
    
#     /* CTA Button Secondary hover effect - accent background */
#     .cta-button-secondary:hover {
#         background-color: var(--accent) !important;
#         color: #FFFFFF !important;
#         border-color: var(--accent) !important;
#         transform: translateY(-1px);
#         box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
#     }
    
#     /* Improved section spacing */
#     .stMarkdown {
#         margin-bottom: var(--space-sm);
#     }
    
#     .stMarkdown:has(h1), .stMarkdown:has(h2) {
#         margin-bottom: var(--space-md);
#     }
    
#     /* Card Components with better spacing */
#     .card {
#         background: var(--card-bg);
#         border-radius: var(--radius-md);
#         padding: var(--space-lg);
#         box-shadow: var(--shadow-sm);
#         border: 1px solid var(--border);
#         transition: var(--transition);
#         margin-bottom: var(--space-lg);
#     }
    
#     .card:hover {
#         transform: translateY(-2px);
#         box-shadow: var(--shadow-md);
#     }
    
#     .card-elevated {
#         background: var(--card-bg);
#         border-radius: var(--radius-md);
#         padding: var(--space-xl);
#         box-shadow: var(--shadow-md);
#         border: 1px solid var(--border);
#         transition: var(--transition);
#         margin-bottom: var(--space-xl);
#     }
    
#     .card-elevated:hover {
#         transform: translateY(-3px);
#         box-shadow: var(--shadow-lg);
#     }
    
#     /* Hero Section with improved spacing */
#     .hero {
#         background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
#         padding: var(--space-xxl) var(--space-lg);
#         border-radius: var(--radius-lg);
#         text-align: center;
#         margin-bottom: var(--space-xl);
#         box-shadow: var(--shadow-sm);
#     }
    
#     /* Button System - Matching CTA button styles exactly */
#     .stButton {
#         margin: var(--space-xs) 0;
#     }
    
#     .stButton>button {
#         border-radius: var(--radius-sm) !important;
#         transition: var(--transition) !important;
#         font-weight: 600 !important;
#         padding: var(--space-sm) var(--space-md) !important;
#         cursor: pointer !important;
#         font-size: var(--font-size-normal) !important;
#         margin: var(--space-xs) 0 !important;
#         min-height: 2.5rem;
#         vertical-align: middle;
#         line-height: 1.6;
#         box-shadow: var(--shadow-sm);
#         text-align: center;
#         width: 100%;
#         box-sizing: border-box;
#     }
    
#     /* Primary Button - Force text color override */
#     .stButton>button[kind="primary"] {
#         background-color: var(--accent) !important;
#         color: #FFFFFF !important;
#         border: 2px solid var(--accent) !important;
#     }
    
#     /* Force white text on primary buttons - highest specificity */
#     .stButton>button[kind="primary"],
#     .stButton>button[kind="primary"] span,
#     .stButton>button[kind="primary"] div,
#     .stButton>button[kind="primary"] p {
#         color: #FFFFFF !important;
#     }
    
#     .stButton>button[kind="primary"]:hover {
#         background-color: #E1F0F0 !important;
#         color: #273548 !important;
#         border-color: #E1F0F0 !important;
#         transform: translateY(-1px);
#         box-shadow: 0 4px 12px rgba(243,246,248,0.6);
#     }
    
#     /* Force dark text on primary button hover */
#     .stButton>button[kind="primary"]:hover,
#     .stButton>button[kind="primary"]:hover span,
#     .stButton>button[kind="primary"]:hover div,
#     .stButton>button[kind="primary"]:hover p {
#         color: #273548 !important;
#     }
    
#     /* Secondary Button - Force text color override */
#     .stButton>button[kind="secondary"] {
#         background-color: white !important;
#         color: var(--text-primary) !important;
#         border: 2px solid var(--border) !important;
#     }
    
#     /* Force dark text on secondary buttons */
#     .stButton>button[kind="secondary"],
#     .stButton>button[kind="secondary"] span,
#     .stButton>button[kind="secondary"] div,
#     .stButton>button[kind="secondary"] p {
#         color: var(--text-primary) !important;
#     }
    
#     .stButton>button[kind="secondary"]:hover {
#         background-color: var(--accent) !important;
#         color: #FFFFFF !important;
#         border-color: var(--accent) !important;
#         transform: translateY(-1px);
#         box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
#     }
    
#     /* Force white text on secondary button hover */
#     .stButton>button[kind="secondary"]:hover,
#     .stButton>button[kind="secondary"]:hover span,
#     .stButton>button[kind="secondary"]:hover div,
#     .stButton>button[kind="secondary"]:hover p {
#         color: #FFFFFF !important;
#     }
    
#     /* Form Elements with improved spacing */
#     .stForm {
#         margin: var(--space-lg) 0;
#         padding: var(--space-lg);
#         background: var(--card-bg);
#         border-radius: var(--radius-md);
#         border: 1px solid var(--border);
#     }
    
#     .stTextInput, .stSelectbox, .stTextArea {
#         margin-bottom: var(--space-sm);
#     }
    
#     .stTextInput>div>div>input, 
#     .stSelectbox>div>div>select,
#     .stTextArea>div>textarea {
#         background-color: white !important;
#         border: 1px solid var(--border) !important;
#         border-radius: var(--radius-sm) !important;
#         padding: var(--space-sm) var(--space-sm) !important;
#         transition: var(--transition) !important;
#         font-size: var(--font-size-normal) !important;
#     }
    
#     .stTextInput>div>div>input:focus, 
#     .stSelectbox>div>div>select:focus,
#     .stTextArea>div>textarea:focus {
#         border-color: var(--accent) !important;
#         box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
#     }
    
#     /* Column spacing improvements */
#     .stColumns {
#         gap: var(--space-lg);
#     }
    
#     .stColumns[data-testid="column"] {
#         padding: 0 var(--space-xs);
#     }
    
#     /* Testimonial Cards with better spacing */
#     .testimonial-card {
#         border-left: 4px solid var(--accent);
#         background: var(--card-bg);
#         padding: var(--space-lg);
#         border-radius: var(--radius-md);
#         margin: var(--space-lg) 0;
#         box-shadow: var(--shadow-sm);
#     }
    
#     /* Metrics with improved spacing */
#     .stMetric {
#         background: var(--card-bg);
#         padding: var(--space-md);
#         border-radius: var(--radius-sm);
#         border: 1px solid var(--border);
#         text-align: center;
#     }
    
#     /* Info boxes with better spacing */
#     .stInfo, .stSuccess, .stWarning, .stError {
#         margin: var(--space-md) 0;
#         padding: var(--space-md);
#         border-radius: var(--radius-sm);
#     }
    
#     /* Navigation improvements */
#     .streamlit-option-menu {
#         margin-bottom: var(--space-xl);
#     }
    
#     /* Divider spacing */
#     hr {
#         margin: var(--space-xl) 0;
#         border: none;
#         border-top: 1px solid var(--border);
#     }
    
#     /* Hide Streamlit Elements */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
    
#     /* Mobile Typography and Spacing */
#     @media (max-width: 768px) {
#         .main .block-container {
#             padding-left: var(--space-sm);
#             padding-right: var(--space-sm);
#             padding-top: var(--space-sm);
#         }
        
#         h1 {
#             font-size: 1.8rem !important;
#         }
        
#         h2, h3, h4, h5, h6 {
#             font-size: 1.5rem !important;
#         }
        
#         .hero {
#             padding: var(--space-lg) var(--space-md);
#         }
        
#         .card, .card-elevated {
#             padding: var(--space-md);
#             margin-bottom: var(--space-md);
#         }
        
#         .stColumns {
#             gap: var(--space-sm);
#         }
        
#         /* Stack columns on mobile */
#         .stColumns[data-testid="column"] {
#             margin-bottom: var(--space-sm);
#         }
#     }
    
#     /* Tablet adjustments */
#     @media (max-width: 1024px) and (min-width: 769px) {
#         .main .block-container {
#             max-width: 100%;
#             padding-left: var(--space-md);
#             padding-right: var(--space-md);
#         }
#     }
    
#     /* Print styles */
#     @media print {
#         .stButton, .streamlit-option-menu {
#             display: none !important;
#         }
        
#         .main .block-container {
#             max-width: 100%;
#             padding: 0;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)






"""
Enhanced styling module for the Hypnotherapy website
Improved spacing, typography, and visual hierarchy
WITH ASSESSMENT PAGE EXCEPTIONS
"""
import streamlit as st

def apply_global_styles():
    """Apply all global styles with improved spacing and typography - WITH ASSESSMENT PAGE EXCEPTIONS"""
    
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
    
    p, li, span, div, a, input, textarea, select, label, .stMarkdown, .stText {
        font-size: var(--font-size-normal) !important;
        line-height: var(--line-height-normal) !important;
        color: var(--text-secondary) !important;
        text-shadow: none !important;
    }
    
    /* Exclude buttons from global text color rule */
    button, button * {
        color: inherit !important;
    }

    /* CTA Button Style - Primary (Accent background) */
    .cta-button {
        display: inline-block;
        background-color: var(--accent);
        color: #FFFFFF !important;
        text-decoration: none;
        /* Match Streamlit button padding and dimensions */
        padding: var(--space-sm) var(--space-md) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-size: var(--font-size-normal) !important;
        transition: var(--transition);
        box-shadow: var(--shadow-sm);
        text-align: center;
        width: 100%;
        box-sizing: border-box;
        margin: var(--space-xs) 0 !important;
        border: 2px solid var(--accent) !important;
        cursor: pointer;
        /* Additional Streamlit button properties */
        min-height: 2.5rem;
        vertical-align: middle;
        line-height: 1.6;
    }
    
    /* CTA Button Style - Secondary (White background) */
    .cta-button-secondary {
        display: inline-block;
        background-color: white;
        color: var(--text-primary) !important;
        text-decoration: none;
        /* Match Streamlit button padding and dimensions */
        padding: var(--space-sm) var(--space-md) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-size: var(--font-size-normal) !important;
        transition: var(--transition);
        box-shadow: var(--shadow-sm);
        text-align: center;
        width: 100%;
        box-sizing: border-box;
        margin: var(--space-xs) 0 !important;
        border: 2px solid var(--border) !important;
        cursor: pointer;
        /* Additional Streamlit button properties */
        min-height: 2.5rem;
        vertical-align: middle;
        line-height: 1.6;
    }
    
    /* Global link reset */
    a {
        text-decoration: none !important;
        color: inherit;
    }
    
    a:hover {
        text-decoration: none !important;
    }

    /* CTA Button Primary hover effect - light background */
    .cta-button:hover {
        background-color: #E1F0F0 !important;
        color: #273548 !important;
        border-color: #E1F0F0 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(243,246,248,0.6);
    }
    
    /* CTA Button Secondary hover effect - accent background */
    .cta-button-secondary:hover {
        background-color: var(--accent) !important;
        color: #FFFFFF !important;
        border-color: var(--accent) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
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
    
    /* ==========================================
       ASSESSMENT PAGE EXCEPTIONS START HERE
       ========================================== */
    
    /* EXCEPTION: Skip global button styling for assessment containers */
    .assessment-container .stButton > button,
    .question-options .stButton > button {
        /* These will be styled by assessment page CSS */
        all: revert !important;
    }
    
    /* ==========================================
       GLOBAL BUTTON STYLES (NON-ASSESSMENT)
       ========================================== */
    
    /* Button System - Apply to all buttons EXCEPT assessment containers */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) {
        margin: var(--space-xs) 0;
    }
    
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button {
        border-radius: var(--radius-sm) !important;
        transition: var(--transition) !important;
        font-weight: 600 !important;
        padding: var(--space-sm) var(--space-md) !important;
        cursor: pointer !important;
        font-size: var(--font-size-normal) !important;
        margin: var(--space-xs) 0 !important;
        min-height: 2.5rem;
        vertical-align: middle;
        line-height: 1.6;
        box-shadow: var(--shadow-sm);
        text-align: center;
        width: 100%;
        box-sizing: border-box;
    }
    
    /* Primary Button - Force text color override (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"] {
        background-color: var(--accent) !important;
        color: #FFFFFF !important;
        border: 2px solid var(--accent) !important;
    }
    
    /* Force white text on primary buttons - highest specificity (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"],
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"] span,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"] div,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"] p {
        color: #FFFFFF !important;
    }
    
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"]:hover {
        background-color: #E1F0F0 !important;
        color: #273548 !important;
        border-color: #E1F0F0 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(243,246,248,0.6);
    }
    
    /* Force dark text on primary button hover (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"]:hover,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"]:hover span,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"]:hover div,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="primary"]:hover p {
        color: #273548 !important;
    }
    
    /* Secondary Button - Force text color override (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"] {
        background-color: white !important;
        color: var(--text-primary) !important;
        border: 2px solid var(--border) !important;
    }
    
    /* Force dark text on secondary buttons (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"],
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"] span,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"] div,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"] p {
        color: var(--text-primary) !important;
    }
    
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"]:hover {
        background-color: var(--accent) !important;
        color: #FFFFFF !important;
        border-color: var(--accent) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
    }
    
    /* Force white text on secondary button hover (EXCEPT assessment) */
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"]:hover,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"]:hover span,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"]:hover div,
    .stButton:not(.assessment-container .stButton):not(.question-options .stButton) > button[kind="secondary"]:hover p {
        color: #FFFFFF !important;
    }
    
    /* ==========================================
       ASSESSMENT PAGE EXCEPTIONS END HERE
       REST OF GLOBAL STYLES CONTINUE
       ========================================== */
    
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
