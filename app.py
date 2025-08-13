import streamlit as st
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Hypnotherapy for Behavioral Change | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS INJECTION ---
def inject_css():
    st.markdown("""
    <style>
    /* ===== FORCE LIGHT MODE ===== */
    /* Main container */
    [data-testid="stAppViewContainer"] {
        background-color: white !important;
        color-scheme: light !important;
    }
    
    /* Sidebar (if you have one) */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6 !important;
        color-scheme: light !important;
    }
    
    /* Text elements */
    .stApp, .stMarkdown, .stText, .stAlert, 
    .stButton, .stTextInput, .stTextArea,
    .stSelectbox, .stSlider {
        color: #1C1C1E !important;  /* Your --primary color */
    }
    
    /* Override dark mode inputs */
    .stTextInput input, .stTextArea textarea,
    .stSelectbox select {
        background-color: white !important;
        color: #1C1C1E !important;
        border-color: #E2E2E6 !important;  /* Your --medium color */
    }
    
    :root {
        --primary: #1C1C1E;
        --accent: #D4AF37;
        --light: #F4F4F6;
        --medium: #E2E2E6;
        --muted: #6E6E73;
        --white: #FFFFFF;
        --shadow: rgba(0,0,0,0.05);
        --shadow-hover: rgba(0,0,0,0.15);
        --shadow-accent: rgba(212, 175, 55, 0.25);
    }
    /* Remove all padding at top */
    html {
        scroll-behavior: smooth;
    }
    body {
        margin: 0;
        padding: 0;
    }
    .stApp {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    /* Remove header completely */
    header {
        display: none !important;
    }
    /* Main container styling */
    .main-container { 
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    /* Hero section at very top */
    #top {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Navigation menu styling */
    div[data-testid="stHorizontalBlock"] {
        margin-top: 0.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    /* Selected menu item */
    .st-ae.st-emotion-cache-1aehpvj {
        font-weight: 600 !important;
        color: var(--accent) !important;
    }
    
    /* Collapse toggle button */
    .collapse-toggle {
        display: inline-block;
        margin-left: 0.5rem;
        color: var(--accent);
        cursor: pointer;
        font-weight: 600;
        vertical-align: middle;
    }
    
    /* Process step numbers */
    .step-number {
        background: var(--accent);
        color: var(--primary);
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
        font-size: 1rem;
        margin-right: 0.5rem;
    }
    
    /* Rest of your CSS */
    [data-testid="stAppViewContainer"] { background-color: var(--light) !important; color-scheme: light !important; }
    #MainMenu, footer, .stDeployButton { visibility: hidden; }
    h1 { font-size: 1.5rem!important; margin: 0.5rem 0!important; }
    h2 { 
        font-size: 1.3rem!important; 
        margin: 0.6rem 0 0.2rem 0!important; /* Reduced space below headings */
        display: inline-block;
    }
    p, li, span, div { font-size: 1rem!important; margin: 0.3rem 0!important; }
    
    /* Hero Section */
    .hero-title { 
        font-size: 1.5rem !important; 
        font-weight: 700 !important; 
        line-height: 1.2 !important; 
        margin: 0 !important;
        color: var(--white) !important;
    }
    .hero-subtitle { 
        font-size: 1rem !important; 
        font-weight: 400 !important; 
        margin: 1rem 0 !important;
        color: #d1d1d6 !important;
    }
    .hero {
        background: var(--primary);
        color: white;
        padding: 1.5rem 1rem;
        text-align: center;
        border-radius: 12px;
        margin: 0 0 0.5rem 0 !important;
        border-left: 6px solid var(--accent);
    }
    .hero * {
        color: var(--white) !important;
    }
    .hero .hero-subtitle { 
        color: #d1d1d6 !important; 
    }
    
    /* Cards */
    .card-container{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px,1fr)); gap:1.5rem; margin:0.5rem 0 1rem 0; }
    .card{ background: var(--white); border:1px solid var(--medium); border-radius:12px; padding:1.5rem; box-shadow:0 6px 16px var(--shadow); transition: transform 0.4s ease, box-shadow 0.4s ease; }
    .card:hover{ transform: translateY(-5px); box-shadow:0 12px 28px var(--shadow-hover); }
    .result-badge { color: var(--accent); font-weight: 600; margin-top: 1rem; display: inline-block; }
    
    /* Process Tracker */
    .process-tracker{ display:flex; justify-conte
