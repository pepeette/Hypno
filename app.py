import streamlit as st
import webbrowser

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Neuroscience Hypnotherapy | Laetitia Sheppard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
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
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

.main-header {
    background: var(--primary-color);
    color: white;
    padding: 5rem 2rem;
    text-align: center;
    border-radius: 12px;
    border-left: 6px solid var(--accent-color);
    margin-bottom: 3rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.main-title {
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.main-subtitle {
    font-size: 1.4rem;
    color: #d1d1d6;
    margin-bottom: 2rem;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.cta-button {
    background-color: var(--accent-color);
    color: var(--primary-color);
    padding: 1rem 2.5rem;
    font-weight: 700;
    border-radius: 6px;
    border: none;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    margin: 0.5rem;
    display: inline-block;
    box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
}

.cta-button:hover {
    background-color: #c7a133;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
}

.problem-card {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid var(--border-color);
    margin-bottom: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

.problem-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.problem-title {
    font-weight: 700;
    font-size: 1.4rem;
    margin-bottom: 1rem;
    color: var(--primary-color);
}

.problem-description {
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
    color: var(--text-muted);
    line-height: 1.7;
}

.problem-result {
    font-weight: 600;
    color: var(--accent-color);
    border-top: 1px dashed var(--border-color);
    padding-top: 1rem;
    margin-top: 1rem;
    font-size: 1.05rem;
}

.sub-section-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-top: 4rem;
    margin-bottom: 2rem;
    border-left: 4px solid var(--accent-color);
    padding-left: 1rem;
    line-height: 1.3;
}

/* ... (keep other CSS classes the same) ... */
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "problems"

# --- HERO SECTION ---
st.markdown("""
<div class="main-header">
    <div class="main-title">The Expat's Dilemma:</div>
    <div class="main-subtitle">
        "You sacrificed everything for this Bangkok career - so why does success feel like wearing someone else's skin?<br>
        The weight won't budge. Your voice shakes in meetings. That promotion keeps going to less qualified candidates."
    </div>
    <button class="cta-button">🧠 Break Your Pattern in 2 Sessions →</button>
    <div style="margin-top: 1.5rem; font-size: 0.9rem; color: var(--text-muted);">
        <em>Neuroscience-backed | Confidential | 13 years in Asian markets</em>
    </div>
</div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
tabs = [("🔥 Your Blocks", "problems"), ("🧠 The Method", "method"), ("🏆 Results", "results"), ("👤 About", "about")]
cols = st.columns(len(tabs))
for i, (label, page_name) in enumerate(tabs):
    css_class = "nav-button-active" if st.session_state.page == page_name else "nav-button"
    with cols[i]:
        if st.button(f"{label}", key=page_name):
            st.session_state.page = page_name
st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE CONTENT ---
def show_problems():
    st.markdown('<div class="sub-section-title">The Hidden Blocks We Solve</div>', unsafe_allow_html=True)
    
    problems_data = [
        {
            "icon": "🧱",
            "title": "The Bangkok Glass Ceiling", 
            "desc": "You deliver exceptional work but get passed over for promotions. Your Western directness is suddenly 'too aggressive', while local colleagues advance with half your output.",
            "result": "→ Rewire unconscious self-sabotage and cultural blind spots"
        },
        {
            "icon": "⚖️", 
            "title": "The Stress-Weight Spiral", 
            "desc": "Late-night moo ping binges after stressful meetings. Gym memberships gathering dust. That 'temporary' 10kg now feels permanent.",
            "result": "→ Reset your metabolic programming without another fad diet"
        },
        {
            "icon": "🔄",
            "title": "Expat Adaptation Fatigue",
            "description": "The constant cultural code-switching is exhausting. You feel like you're losing your authentic self while navigating Thai business culture.",
            "result": "→ Develop effortless cultural fluency while maintaining core identity"
        },
        {
            "icon": "📉",
            "title": "Performance Anxiety", 
            "desc": "You nailed presentations in London/NYC - but here, your mind blanks mid-sentence. The harder you try to impress, the more you underwhelm.",
            "result": "→ Install bulletproof confidence tailored to Asian boardrooms"
        }
    ]
    
    st.markdown("<div class='problem-grid'>", unsafe_allow_html=True)
    for problem in problems_data:
        st.markdown(f"""
        <div class='problem-card'>
            <div class='problem-icon'>{problem['icon']}</div>
            <div class='problem-title'>{problem['title']}</div>
            <div class='problem-description'>{problem['description']}</div>
            <div class='problem-result'>{problem['result']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">Why It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Sessions for breakthrough</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">92%</div>
            <div class="stat-label">Report significant improvement</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">5-7x</div>
            <div class="stat-label">Faster than traditional therapy</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">0</div>
            <div class="stat-label">Ongoing sessions needed</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

     st.markdown("""
    <div style="text-align: center; margin-top: 3rem;">
        <button class="cta-button">🚨 Only 3 Spots Left This Month →</button>
    </div>
    """, unsafe_allow_html=True)

# --- METHOD SECTION ---  
def show_method():
    st.markdown("""
    <div class="sub-section-title">Why 2 Sessions Work When Nothing Else Did</div>
    
    <div class="problem-card">
        <div class="problem-title">Traditional Therapy Failed You Because:</div>
        <div class="problem-description">
        • It talks <em>about</em> problems instead of rewriting them<br>
        • Progress gets derailed by Bangkok's 60-hour work weeks<br>
        • Western methods don't address Asian business culture nuances
        </div>
    </div>
    
    <div style="margin: 3rem 0;">
        <div class="sub-section-title" style="font-size: 1.6rem;">Our Neuroscience Protocol</div>
        <div class="problem-card">
            <div style="display: flex; align-items: center; gap: 1.5rem;">
                <div style="background: var(--accent-color); color: var(--primary-color); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">1</div>
                <div>
                    <div style="font-weight: 700; margin-bottom: 0.5rem;">Session 1: Pattern Mapping</div>
                    <div style="color: var(--text-muted);">We identify the <em>exact</em> neural circuits causing your blocks using fMRI-inspired techniques</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_results():
    st.markdown('<div class="sub-section-title">Client Transformations</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial-grid">
        <div class="testimonial-card">
            <div class="testimonial-text">
                "After 2 sessions, I went from freezing in regional presentations to delivering my best keynote at the ASEAN summit. Laetitia's method helped me access confidence I didn't know I had."
            </div>
            <div class="testimonial-author">
                — French Tech Director, Fortune 500
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">
                "The weight finally started coming off after years of struggle. More importantly, I stopped stress-eating during high-pressure deals. This changed both my health and career trajectory."
            </div>
            <div class="testimonial-author">
                — American PE VP, Bangkok
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("./img/ID.jpg", width=250, caption="Laetitia Sheppard")
    with col2:
        st.markdown('<div class="sub-section-title">About Laetitia</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-bottom: 2rem;">
            <p><strong>Bangkok-based specialist</strong> with 13 years in Asian financial hubs (Hong Kong, Singapore, Bangkok)</p>
            <p>Understands the unique pressures of:</p>
            <ul>
                <li>Expat stress meets career ambition</li>
                <li>Thai business culture nuances</li>
                <li>Metabolic impact of Bangkok's environment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-card">
        <div style="text-align: center;">
            <h3 style="color: white; margin-bottom: 1rem;">Bangkok Hypnotherapy Clinic</h3>
            <p style="margin-bottom: 1.5rem;">46/9 Soi Sukhumvit 49 (Thong Lor) • Private & Confidential</p>
            <button class="stButton">📍 Get Directions</button>
            <button class="stButton">📅 Book Discovery Call</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN CONTENT ---
if st.session_state.page == "problems":
    show_problems()
elif st.session_state.page == "method":
    show_method()
elif st.session_state.page == "results":
    show_results()
elif st.session_state.page == "about":
    show_about()

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p>Laetitia Sheppard • Neuroscience Hypnotherapy • Bangkok, Thailand</p>
    <p>© 2023 All Rights Reserved | Confidentiality Guaranteed</p>
</div>
""", unsafe_allow_html=True)
