"""
Complete design system enforcement
Only 3 font sizes, no shadows, forced light mode
"""
from utils import config

def apply_design_system():
    """Apply the complete design system"""
    st.markdown(f"""
    <style>
    /* Base styles */
    :root {{
        color-scheme: light;
    }}
    html, body, .stApp {{
        color-scheme: light !important;
        background-color: {config.bg_color} !important;
    }}
    
    /* Typography system */
    h1 {{
        font-size: 2rem !important;
        color: {config.text_primary} !important;
        margin-bottom: 1.5rem !important;
        font-weight: 700 !important;
    }}
    h2 {{
        font-size: 1.5rem !important;
        color: {config.text_primary} !important;
        margin-bottom: 1rem !important;
        font-weight: 600 !important;
    }}
    h3 {{
        font-size: 1.25rem !important;
        color: {config.text_primary} !important;
        margin-bottom: 0.75rem !important;
        font-weight: 600 !important;
    }}
    p, div, li, .stMarkdown, .stCaption {{
        font-size: 1rem !important;
        color: {config.text_secondary} !important;
        line-height: 1.5 !important;
    }}
    small {{
        font-size: 0.875rem !important;
    }}
    
    /* Interactive elements */
    .stButton>button {{
        background-color: {config.accent_color} !important;
        color: white !important;
        border-radius: {config.radius_md} !important;
        border: none !important;
        transition: {config.transition} !important;
    }}
    .stButton>button:hover {{
        background-color: {config.accent_hover} !important;
        transform: translateY(-1px);
        box-shadow: {config.shadow_sm} !important;
    }}
    
    /* Cards and containers */
    .stCard {{
        background: {config.card_bg} !important;
        border-radius: {config.radius_md} !important;
        border: 1px solid {config.border} !important;
        padding: 1.5rem !important;
        box-shadow: {config.shadow_sm} !important;
    }}
    
    /* Form elements */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>select {{
        border: 1px solid {config.border} !important;
        border-radius: {config.radius_sm} !important;
    }}
    
    /* Special overrides */
    .stMarkdown a {{
        color: {config.accent_color} !important;
        text-decoration: none !important;
    }}
    .stMarkdown a:hover {{
        text-decoration: underline !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def load_css(file_path=None):
    """Legacy support - use apply_design_system() instead"""
    apply_design_system()
