import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Performance Solutions",
    page_icon="🧠",
    layout="centered",  # responsive, mobile-friendly
    initial_sidebar_state="collapsed",
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
/* Force light mode */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
}
:root {
    color-scheme: light;
}

/* Typography */
h1 {
    font-size: clamp(1.8rem, 5vw, 2.6rem);
    font-weight: 700;
    margin-bottom: 0.6em;
}
h2 {
    font-size: clamp(1.4rem, 4vw, 2rem);
    font-weight: 600;
    margin-bottom: 0.4em;
}
p {
    font-size: clamp(1rem, 2.5vw, 1.15rem);
    line-height: 1.6;
}

/* Brand colors */
:root {
    --brand-gold: #c8a951;
    --brand-dark: #1a1a1a;
}

/* Section titles */
.section-title {
    font-size: clamp(1.4rem, 4vw, 2rem);
    font-weight: 600;
    color: var(--brand-dark);
    margin-top: 2em;
    margin-bottom: 1em;
    border-bottom: 2px solid var(--brand-gold);
    display: inline-block;
    padding-bottom: 0.2em;
}

/* Cards */
.card {
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    padding: 1.2em;
    text-align: center;
}
.card h2 {
    color: var(--brand-gold);
    margin-bottom: 0.4em;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #666666;
    padding: 2em 1em;
    margin-top: 3em;
    border-top: 1px solid #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>Neuroscience Performance Solutions</h1>", unsafe_allow_html=True)
st.markdown("<p>Premium neuroscience-based behavioral rewiring solutions for executives in Asia.</p>", unsafe_allow_html=True)

# --- WHAT WE FIX SECTION ---
st.markdown('<div class="section-title">What We Fix — Fast</div>', unsafe_allow_html=True)
cols = st.columns(3)
with cols[0]:
    st.markdown('<div class="card"><h2>Stress</h2><p>Reduce overwhelm and regain focus in high-pressure roles.</p></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="card"><h2>Burnout</h2><p>Rewire your brain for sustainable energy and resilience.</p></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="card"><h2>Performance</h2><p>Break limits and accelerate decision-making under pressure.</p></div>', unsafe_allow_html=True)

# --- HOW IT WORKS SECTION ---
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
st.markdown("<p>We combine neuroscience, hypnotherapy, and performance coaching to deliver measurable results in weeks, not months. Sessions are tailored for executives and high-achievers in finance, business leadership, and performance-critical roles.</p>", unsafe_allow_html=True)

# --- BOOKING SECTION ---
st.markdown('<div class="section-title">Book Your Session</div>', unsafe_allow_html=True)
st.markdown("<p>Click below to schedule a private, confidential consultation.</p>", unsafe_allow_html=True)
st.link_button("📅 Book Now", "https://calendly.com/your-booking-link")

# --- FOOTER ---
st.markdown('<div class="footer">© 2025 Neuroscience Performance Solutions — Bangkok, Thailand</div>', unsafe_allow_html=True)
