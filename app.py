import streamlit as st
import webbrowser
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Performance Solutions | Laetitia Sheppard", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS: EXECUTIVE NEUROSCIENCE THEME ---
st.markdown("""
    <style>
    :root {
        --primary-color: #1C1C1E;
        --accent-color: #D4AF37;
        --secondary-color: #3A3A3C;
        --bg-color: #F4F4F6;
        --card-bg: #FFFFFF;
        --text-color: #1C1C1E;
        --text-muted: #6E6E73;
        --border-color: #E2E2E6;
    }

    .stApp {
        font-family: 'Inter', sans-serif;
        color: var(--text-color);
        background-color: var(--bg-color);
        line-height: 1.6;
    }

    .hero-section {
        background: var(--primary-color);
        color: white;
        padding: 3rem 2rem;
        text-align: center;
        border-radius: 12px;
        border-left: 6px solid var(--accent-color);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 2.75rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: var(--text-muted);
        margin-bottom: 2rem;
    }

    .stButton>button {
        background-color: var(--accent-color);
        color: var(--primary-color);
        border: none;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        border-radius: 6px;
        font-size: 1rem;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .stButton>button:hover {
        background-color: #C99F2E;
        transform: translateY(-2px);
    }

    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: var(--primary-color);
        text-align: center;
        margin-top: 3rem;
        border-bottom: 2px solid var(--accent-color);
        padding-bottom: 0.5rem;
    }

    .problem-card, .method-step, .testimonial-card {
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .problem-card:hover, .method-step:hover, .testimonial-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }

    .badge {
        background-color: var(--secondary-color);
        color: white;
        padding: 0.3rem 0.7rem;
        border-radius: 4px;
        font-size: 0.75rem;
        margin: 0.25rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
def show_header():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">Unlock Elite Performance in 2 Sessions</div>
        <div class="hero-subtitle">For Finance Leaders in Bangkok, Singapore, and Hong Kong<br>Rewire pressure responses using neuroscience, not talk therapy.</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("📅 Apply for Performance Audit", key="hero_cta"):
            webbrowser.open("https://calendly.com/titre/free-session")
    st.markdown("</div>", unsafe_allow_html=True)

# --- NAVIGATION ---
def show_navigation():
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.markdown("### **Neuroscience Performance Solutions**")
    with col2:
        if st.button("Fixes", key="nav_services"):
            st.session_state.page = "services"
    with col3:
        if st.button("Method", key="nav_method"):
            st.session_state.page = "method"
    with col4:
        if st.button("About", key="nav_about"):
            st.session_state.page = "about"

# --- SESSION STATE INIT ---
if 'page' not in st.session_state:
    st.session_state.page = 'services'

# --- MAIN DISPLAY LOGIC ---
show_header()
show_navigation()

if st.session_state.page == 'services':
    st.markdown('<div class="section-title">High-Stakes Performance Fixes</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <span class="badge">Bangkok</span>
        <span class="badge">Singapore</span>
        <span class="badge">Hong Kong</span>
    </div>
    """, unsafe_allow_html=True)
    # ... Keep existing problem cards

elif st.session_state.page == 'method':
    st.markdown('<div class="section-title">The 2-Session Neuroscience Method</div>', unsafe_allow_html=True)
    # ... Keep method steps and expanders

elif st.session_state.page == 'about':
    st.markdown('<div class="section-title">Why Finance Leaders Trust This Method</div>', unsafe_allow_html=True)
    # ... Keep about section and testimonials

# --- FOOTER ---
st.markdown("---")
st.markdown("*Neuroscience Performance Solutions | Confidential Support for Asia’s Finance Leaders*")
