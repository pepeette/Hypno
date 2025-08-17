"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
"""
import streamlit as st
from components.quiz import create_enhanced_quiz

class DynamicHeroSection:
    """Enhanced hero section with dynamic elements"""
    
    def __init__(self):
        self.rendered = False
    
    def render(self):
        """Render hero section once with dynamic content"""
        if self.rendered:
            return
        
        hero_html = """
        <div class="hero fade-in-up" style="position: relative; overflow: hidden;">
            <div style="position: relative; z-index: 2;">
                <h1 style="color: white; margin-bottom: 1rem; text-shadow: none;">
                    Transform Your Life in Just 2 Sessions
                </h1>
                <p style="font-size: 1.2rem; color: white; opacity: 0.95; 
                          max-width: 700px; margin: 0 auto 2rem auto; line-height: 1.6;">
                    Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits. 
                    <strong>85% success rate</strong> in our proven 2-session method.
                </p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); 
                        gap: 2rem; margin: 3rem 0; max-width: 600px; margin-left: auto; margin-right: auto;">
                <div class="stat-item" style="text-align: center; color: white;">
                    <div style="font-size: 3rem; font-weight: bold; margin-bottom: 0.5rem; 
                               animation: countUp 2s ease-out;">85%</div>
                    <p style="margin: 0; font-weight: 600; font-size: 1.1rem;">Success in 2 Sessions</p>
                </div>
                <div class="stat-item" style="text-align: center; color: white;">
                    <div style="font-size: 3rem; font-weight: bold; margin-bottom: 0.5rem; 
                               animation: countUp 2s ease-out 0.3s both;">500+</div>
                    <p style="margin: 0; font-weight: 600; font-size: 1.1rem;">Lives Transformed</p>
                </div>
                <div class="stat-item" style="text-align: center; color: white;">
                    <div style="font-size: 3rem; font-weight: bold; margin-bottom: 0.5rem; 
                               animation: countUp 2s ease-out 0.6s both;">10+</div>
                    <p style="margin: 0; font-weight: 600; font-size: 1.1rem;">Years Experience</p>
                </div>
            </div>
        </div>
        
        <style>
        @keyframes countUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """
        
        st.markdown(hero_html, unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎯 Take the 30-Second Assessment", 
                        key="hero_cta", 
                        type="primary", 
                        use_container_width=True,
                        help="Discover your suitability for transformation"):
                st.session_state.scroll_to_quiz = True
                st.success("✨ Scroll down to start your assessment!")
        
        self.rendered = True

class AuthoritySection:
    """Section highlighting expertise and authority"""
    
    def render(self):
        """Render authority and credibility section"""
        authority_html = """
        <div style="background: var(--card-bg); border-radius: var(--radius-lg); 
                    padding: 2rem; margin: 3rem 0; box-shadow: var(--shadow-md); 
                    border: 1px solid var(--border);">
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: var(--accent); margin-bottom: 1rem;">🏆 Proven Expertise</h2>
                <p style="color: var(--text-secondary); font-size: 1.1rem;">
                    Certified clinical hypnotherapist with 10+ years transforming lives
                </p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                        gap: 2rem; margin: 2rem 0;">
                <div style="text-align: center; padding: 1.5rem; background: rgba(76, 161, 163, 0.05); 
                            border-radius: var(--radius-sm); border: 1px solid rgba(76, 161, 163, 0.2);">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">🎓</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Certified</h3>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem;">
                        Clinical Hypnotherapist<br>Advanced NLP Practitioner
                    </p>
                </div>
                
                <div style="text-align: center; padding: 1.5rem; background: rgba(76, 161, 163, 0.05); 
                            border-radius: var(--radius-sm); border: 1px solid rgba(76, 161, 163, 0.2);">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔬</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Science-Based</h3>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem;">
                        Neuroplasticity Principles<br>Rapid Transformation Therapy
                    </p>
                </div>
                
                <div style="text-align: center; padding: 1.5rem; background: rgba(76, 161, 163, 0.05); 
                            border-radius: var(--radius-sm); border: 1px solid rgba(76, 161, 163, 0.2);">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">🌍</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">International</h3>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem;">
                        Bangkok Clinic<br>Worldwide Online Sessions
                    </p>
                </div>
                
                <div style="text-align: center; padding: 1.5rem; background: rgba(76, 161, 163, 0.05); 
                            border-radius: var(--radius-sm); border: 1px solid rgba(76, 161, 163, 0.2);">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔒</div>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Licensed</h3>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem;">
                        Fully Insured<br>Professional Standards
                    </p>
                </div>
            </div>
        </div>
        """
        
        st.markdown(authority_html, unsafe_allow_html=True)

class WhyItWorksSection:
    """Enhanced section explaining why the method works"""
    
    def render(self):
        """Render the science-backed explanation"""
        st.markdown("## 🧠 Why Our Method Works When Others Don't")
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            traditional_html = """
            <div style="background: rgba(239, 68, 68, 0.05); border-radius: var(--radius-md); 
                        padding: 2rem; border: 2px solid rgba(239, 68, 68, 0.2);">
                <h3 style="color: #dc2626; margin-bottom: 1rem; text-align: center;">
                    ❌ Traditional Methods
                </h3>
                <div style="space-y: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #dc2626; font-size: 1.2rem;">🧠</span>
                        <span>Target conscious mind (5% of decisions)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #dc2626; font-size: 1.2rem;">💪</span>
                        <span>Rely on willpower (fails 95% of the time)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #dc2626; font-size: 1.2rem;">🔄</span>
                        <span>Require ongoing sessions for months/years</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #dc2626; font-size: 1.2rem;">📈</span>
                        <span>High relapse rates (60-80%)</span>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 1.5rem; padding: 1rem; 
                            background: rgba(239, 68, 68, 0.1); border-radius: var(--radius-sm);">
                    <strong style="color: #dc2626;">You're fighting your own programming</strong>
                </div>
            </div>
            """
            st.markdown(traditional_html, unsafe_allow_html=True)
        
        with col2:
            our_method_html = """
            <div style="background: rgba(34, 197, 94, 0.05); border-radius: var(--radius-md); 
                        padding: 2rem; border: 2px solid rgba(34, 197, 94, 0.2);">
                <h3 style="color: #16a34a; margin-bottom: 1rem; text-align: center;">
                    ✅ Our Hypnotherapy Method
                </h3>
                <div style="space-y: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #16a34a; font-size: 1.2rem;">🎯</span>
                        <span>Direct access to subconscious (95% of decisions)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #16a34a; font-size: 1.2rem;">⚡</span
