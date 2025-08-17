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
                        <span style="color: #16a34a; font-size: 1.2rem;">⚡</span>
                        <span>Rewire neural pathways permanently</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #16a34a; font-size: 1.2rem;">🎯</span>
                        <span>Just 2 sessions for lasting change</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="color: #16a34a; font-size: 1.2rem;">🔒</span>
                        <span>85% permanent success rate</span>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 1.5rem; padding: 1rem; 
                            background: rgba(34, 197, 94, 0.1); border-radius: var(--radius-sm);">
                    <strong style="color: #16a34a;">Your programming supports your goals</strong>
                </div>
            </div>
            """
            st.markdown(our_method_html, unsafe_allow_html=True)

class InteractiveTestimonials:
    """Enhanced testimonials with interactive elements"""
    
    def __init__(self):
        self.testimonials = [
            {
                "icon": "🌟",
                "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
                "author": "Director, Banking, Singapore",
                "concern": "Anxiety patterns",
                "sessions": "2",
                "timeframe": "10 days",
                "detail": "After years of performance anxiety affecting my career, I was skeptical but desperate. The first session revealed triggers I never knew existed. By session two, I felt like a completely different person. Six months later, I'm still anxiety-free and got promoted."
            },
            {
                "icon": "🎓",
                "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
                "author": "Medical Student, Morocco",
                "concern": "Study anxiety & focus",
                "sessions": "2",
                "timeframe": "1 week",
                "detail": "Medical school stress was overwhelming me. I couldn't concentrate and was considering dropping out. The hypnotherapy sessions helped me understand my stress patterns and gave me tools to stay focused. Now I'm excelling in my internship."
            },
            {
                "icon": "🚭",
                "quote": "My husband was a heavy smoker... No more addiction.",
                "author": "Wife, Bangkok",
                "concern": "Smoking cessation",
                "sessions": "2",
                "timeframe": "3 days",
                "detail": "After 20 years of smoking 2 packs a day, my husband tried everything. Patches, gum, medications - nothing worked. Two sessions later, he doesn't even think about cigarettes. He's saved over 30,000 THB and his health has dramatically improved."
            }
        ]
    
    def render(self):
        """Render interactive testimonials"""
        st.markdown("## 💬 Real Transformation Stories")
        
        for i, testimonial in enumerate(self.testimonials):
            self._render_testimonial_card(testimonial, i)
    
    def _render_testimonial_card(self, testimonial, index):
        """Render individual testimonial with expandable details"""
        testimonial_html = f"""
        <div class="testimonial-card fade-in-up" style="margin: 2rem 0; transition: all 0.3s ease;">
            <div style="display: flex; align-items: flex-start; gap: 1.5rem;">
                <div style="font-size: 3rem; color: var(--accent); min-width: 70px; text-align: center;">
                    {testimonial['icon']}
                </div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.3rem; 
                                       color: var(--text-primary); margin: 0 0 1.5rem 0;
                                       line-height: 1.5; font-weight: 500;">
                        "{testimonial['quote']}"
                    </blockquote>
                    <div style="margin-bottom: 1rem;">
                        <div style="font-weight: 600; color: var(--text-secondary); margin-bottom: 0.8rem; font-size: 1.1rem;">
                            — {testimonial['author']}
                        </div>
                        <div style="display: flex; gap: 1.5rem; font-size: 0.95rem; flex-wrap: wrap;">
                            <span style="color: var(--accent); font-weight: 600;">
                                🎯 {testimonial['concern']}
                            </span>
                            <span style="color: var(--success); font-weight: 600;">
                                ⏱️ {testimonial['sessions']} sessions • {testimonial['timeframe']}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(testimonial_html, unsafe_allow_html=True)
        
        # Expandable details
        with st.expander(f"📖 Read {testimonial['author'].split(',')[0]}'s Full Story", expanded=False):
            st.markdown(f"**The Challenge:** {testimonial['concern']}")
            st.markdown(f"**The Transformation:** {testimonial['detail']}")
            st.markdown(f"**Timeline:** Complete change in {testimonial['timeframe']} with {testimonial['sessions']} sessions")

class QuizIntegration:
    """Integration component for the quiz"""
    
    def render(self):
        """Render quiz section with smooth integration"""
        quiz_intro_html = """
        <div style="margin: 4rem 0 2rem 0;">
            <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                        border-radius: var(--radius-lg); padding: 3rem 2rem; text-align: center;">
                <h2 style="color: white; margin-bottom: 1rem;">
                    Discover Your Transformation Potential
                </h2>
                <p style="color: white; opacity: 0.9; font-size: 1.2rem; 
                          max-width: 600px; margin: 0 auto 2rem auto;">
                    Take our science-based assessment to see how well you match our successful client profile
                </p>
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                    <div style="color: white; text-align: center;">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div>
                        <div>30 seconds</div>
                    </div>
                    <div style="color: white; text-align: center;">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎯</div>
                        <div>Personalized</div>
                    </div>
                    <div style="color: white; text-align: center;">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔬</div>
                        <div>Science-based</div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(quiz_intro_html, unsafe_allow_html=True)
        
        # Render the enhanced quiz
        quiz = create_enhanced_quiz()
        quiz.render()

class CallToActionSection:
    """Final call to action section"""
    
    def render(self):
        """Render compelling CTA section"""
        cta_html = """
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 4rem 2rem; 
                    text-align: center; margin: 4rem 0; position: relative; overflow: hidden;">
            
            <div style="position: relative; z-index: 2;">
                <h2 style="color: white; margin-bottom: 1rem; font-size: 2.2rem;">
                    Ready to Transform Your Life?
                </h2>
                <p style="color: white; opacity: 0.9; font-size: 1.3rem; 
                          max-width: 600px; margin: 0 auto 3rem auto; line-height: 1.5;">
                    Join hundreds of people who have already transformed their lives. 
                    Your success story could be next.
                </p>
                
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 2rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: var(--radius-md); 
                               backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="color: white; font-size: 2rem; font-weight: bold;">85%</div>
                        <div style="color: white; opacity: 0.9;">Success Rate</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: var(--radius-md); 
                               backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="color: white; font-size: 2rem; font-weight: bold;">2</div>
                        <div style="color: white; opacity: 0.9;">Sessions Only</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: var(--radius-md); 
                               backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
                        <div style="color: white; font-size: 2rem; font-weight: bold;">3000</div>
                        <div style="color: white; opacity: 0.9;">THB Total</div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3, gap="medium")
        
        with col1:
            if st.button("📞 Free Discovery Call", 
                        key="final_discovery", 
                        use_container_width=True,
                        type="primary",
                        help="15-minute consultation - no obligation"):
                st.success("✨ Excellent choice! A discovery call is the perfect first step.")
        
        with col2:
            if st.button("🧠 Learn Our Method", 
                        key="final_method", 
                        use_container_width=True,
                        type="secondary",
                        help="Understand the science behind our approach"):
                st.success("🔬 Great! Understanding the method helps build confidence.")
        
        with col3:
            if st.button("⚡ Book Sessions Now", 
                        key="final_book", 
                        use_container_width=True,
                        type="primary",
                        help="Ready to start your transformation"):
                st.success("🚀 Amazing! Let's begin your transformation journey.")

class HomePage:
    """Main home page component - single render architecture"""
    
    def __init__(self):
        # Initialize components once
        self.hero = DynamicHeroSection()
        self.authority = AuthoritySection()
        self.why_it_works = WhyItWorksSection()
        self.testimonials = InteractiveTestimonials()
        self.quiz_integration = QuizIntegration()
        self.cta = CallToActionSection()
        self._rendered = False
    
    def render(self):
        """Render complete home page - SINGLE RENDER ONLY"""
        if self._rendered:
            return
        
        # Hero section with dynamic stats
        self.hero.render()
        
        # Authority and credibility
        self.authority.render()
        
        # Why our method works
        self.why_it_works.render()
        
        # Interactive testimonials
        self.testimonials.render()
        
        # Integrated quiz section
        self.quiz_integration.render()
        
        # Final call to action
        self.cta.render()
        
        # Mark as rendered to prevent double rendering
        self._rendered = True

def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
