"""
Styling module for the Hypnotherapy website
Centralizes all CSS styling and design system
"""
import streamlit as st

class DesignTokens:
    """Design system tokens and variables"""
    
    CSS_VARIABLES = """
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
        --radius-full: 50%;
        
        /* Spacing */
        --space-xs: 0.5rem;
        --space-sm: 1rem;
        --space-md: 1.5rem;
        --space-lg: 2rem;
        --space-xl: 3rem;
        
        /* Typography */
        --font-size-sm: 0.875rem;
        --font-size-base: 1rem;
        --font-size-lg: 1.125rem;
        --font-size-xl: 1.25rem;
        --font-size-2xl: 1.5rem;
        --font-size-3xl: 1.875rem;
        --font-size-4xl: 2.25rem;
        
        --line-height-tight: 1.25;
        --line-height-normal: 1.5;
        --line-height-relaxed: 1.75;
        
        /* Transitions */
        --transition: all 0.3s ease;
        --transition-fast: all 0.15s ease;
        --transition-slow: all 0.5s ease;
    }
    """

class BaseStyles:
    """Base styling for the application"""
    
    @staticmethod
    def get_base_styles():
        return f"""
        <style>
        {DesignTokens.CSS_VARIABLES}
        
        /* Force light mode */
        :root {{
            color-scheme: light;
        }}
        
        html, body, [class*="st"] {{
            color-scheme: light !important;
        }}
        
        .stApp {{
            background-color: var(--bg) !important;
            color: var(--text-primary) !important;
        }}
        
        /* Typography System */
        h1 {{
            font-size: var(--font-size-4xl) !important;
            line-height: var(--line-height-tight) !important;
            margin-bottom: var(--space-lg) !important;
            color: var(--text-primary) !important;
            font-weight: 700 !important;
        }}
        
        h2 {{
            font-size: var(--font-size-3xl) !important;
            line-height: var(--line-height-tight) !important;
            margin-bottom: var(--space-md) !important;
            color: var(--text-primary) !important;
            font-weight: 600 !important;
        }}
        
        h3 {{
            font-size: var(--font-size-2xl) !important;
            line-height: var(--line-height-tight) !important;
            margin-bottom: var(--space-sm) !important;
            color: var(--text-primary) !important;
            font-weight: 600 !important;
        }}
        
        p, li, span, div, a, button, input, textarea, select, label, .text {{
            font-size: var(--font-size-base) !important;
            line-height: var(--line-height-normal) !important;
            color: var(--text-secondary) !important;
        }}
        
        /* Mobile Typography */
        @media (max-width: 768px) {{
            h1 {{
                font-size: var(--font-size-3xl) !important;
            }}
            
            h2 {{
                font-size: var(--font-size-2xl) !important;
            }}
            
            h3 {{
                font-size: var(--font-size-xl) !important;
            }}
        }}
        </style>
        """

class ComponentStyles:
    """Styling for reusable components"""
    
    @staticmethod
    def get_component_styles():
        return """
        <style>
        /* Card Component */
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
            box-shadow: var(--shadow-md);
        }
        
        .card-elevated:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--accent) 0%, #E1F0F0 100%);
            padding: var(--space-xl) var(--space-lg);
            border-radius: var(--radius-lg);
            text-align: center;
            margin-bottom: var(--space-lg);
            box-shadow: var(--shadow-sm);
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="white" opacity="0.1"/><circle cx="80" cy="40" r="3" fill="white" opacity="0.1"/><circle cx="40" cy="80" r="1" fill="white" opacity="0.1"/></svg>');
            pointer-events: none;
        }
        
        /* Button System */
        .btn {
            display: inline-block;
            padding: var(--space-xs) var(--space-md);
            border-radius: var(--radius-sm);
            text-decoration: none;
            font-weight: 600;
            text-align: center;
            transition: var(--transition);
            cursor: pointer;
            border: none;
            font-size: var(--font-size-base);
        }
        
        .btn-primary {
            background-color: var(--accent);
            color: white;
        }
        
        .btn-primary:hover {
            background-color: var(--accent-hover);
            transform: translateY(-1px);
            box-shadow: var(--shadow-accent);
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
        
        .btn-success {
            background-color: var(--success);
            color: white;
        }
        
        .btn-success:hover {
            background-color: #16a34a;
            transform: translateY(-1px);
        }
        
        /* Streamlit Button Overrides */
        .stButton>button {
            border-radius: var(--radius-sm) !important;
            transition: var(--transition) !important;
            font-weight: 600 !important;
            padding: var(--space-xs) var(--space-md) !important;
            cursor: pointer !important;
            border: none !important;
        }
        
        .stButton>button[kind="primary"] {
            background-color: var(--accent) !important;
            color: white !important;
        }
        
        .stButton>button[kind="primary"]:hover {
            background-color: var(--accent-hover) !important;
            transform: translateY(-1px);
            box-shadow: var(--shadow-accent);
        }
        
        /* Form Elements */
        .stTextInput>div>div>input, 
        .stSelectbox>div>div>select,
        .stTextArea>div>textarea {
            background-color: white !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-sm) !important;
            padding: var(--space-xs) var(--space-sm) !important;
            transition: var(--transition) !important;
        }
        
        .stTextInput>div>div>input:focus, 
        .stSelectbox>div>div>select:focus,
        .stTextArea>div>textarea:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1) !important;
        }
        
        /* Progress Bar */
        .progress-container {
            background-color: var(--border);
            height: 8px;
            border-radius: var(--radius-sm);
            overflow: hidden;
            margin: var(--space-sm) 0;
        }
        
        .progress-bar {
            background: linear-gradient(90deg, var(--accent) 0%, var(--success) 100%);
            height: 100%;
            transition: width var(--transition-slow);
            border-radius: var(--radius-sm);
        }
        
        /* Testimonial Cards */
        .testimonial-card {
            border-left: 4px solid var(--accent);
            position: relative;
        }
        
        .testimonial-card::before {
            content: '"';
            position: absolute;
            top: -10px;
            left: var(--space-md);
            font-size: 4rem;
            color: var(--accent);
            opacity: 0.2;
            font-family: Georgia, serif;
        }
        
        /* Utility Classes */
        .text-center { text-align: center; }
        .text-left { text-align: left; }
        .text-right { text-align: right; }
        
        .mb-xs { margin-bottom: var(--space-xs); }
        .mb-sm { margin-bottom: var(--space-sm); }
        .mb-md { margin-bottom: var(--space-md); }
        .mb-lg { margin-bottom: var(--space-lg); }
        .mb-xl { margin-bottom: var(--space-xl); }
        
        .mt-xs { margin-top: var(--space-xs); }
        .mt-sm { margin-top: var(--space-sm); }
        .mt-md { margin-top: var(--space-md); }
        .mt-lg { margin-top: var(--space-lg); }
        .mt-xl { margin-top: var(--space-xl); }
        
        /* Loading States */
        .loading {
            opacity: 0.6;
            pointer-events: none;
        }
        
        /* Success States */
        .success-message {
            background-color: rgba(34, 197, 94, 0.1);
            border: 1px solid var(--success);
            color: var(--success);
            padding: var(--space-sm);
            border-radius: var(--radius-sm);
            margin: var(--space-sm) 0;
        }
        
        /* Error States */
        .error-message {
            background-color: rgba(239, 68, 68, 0.1);
            border: 1px solid var(--error);
            color: var(--error);
            padding: var(--space-sm);
            border-radius: var(--radius-sm);
            margin: var(--space-sm) 0;
        }
        
        /* Navigation Styles */
        .st-emotion-cache-1avcm0n {
            background-color: var(--bg) !important;
        }
        
        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        </style>
        """

def apply_global_styles():
    """Apply all global styles to the Streamlit app"""
    base_styles = BaseStyles.get_base_styles()
    component_styles = ComponentStyles.get_component_styles()
    
    st.markdown(base_styles, unsafe_allow_html=True)
    st.markdown(component_styles, unsafe_allow_html=True)
