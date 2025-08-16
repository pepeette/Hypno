"""
Home page component for the Hypnotherapy website
COMPLETE: Includes quiz component integration
"""
import streamlit as st

class HeroSection:
    """Hero section with consistent pattern"""
    
    def render(self):
        """Render hero section"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <h1>Transform Your Life in Just 2 Sessions</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
        </div>
        """, unsafe_allow_html=True)

class StatsSection:
    """Statistics section with consistent styling"""
    
    def render(self):
        """Render statistics section"""
        stats_html = """
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                    gap: 2rem; margin: 2rem 0;">
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border);">
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent); margin-bottom: 0.5rem;">85%</div>
                <div style="font-weight: 600; color: var(--text-primary);">Success in 2 Sessions</div>
                <div style="color: var(--text-secondary); font-size: 0.9rem;">Complete transformation</div>
            </div>
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border);">
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent); margin-bottom: 0.5rem;">500+</div>
                <div style="font-weight: 600; color: var(--text-primary);">Lives Transformed</div>
                <div style="color: var(--text-secondary); font-size: 0.9rem;">Since 2014</div>
            </div>
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem 1.5rem; text-align: center; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border);">
                <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent); margin-bottom: 0.5rem;">10+</div>
                <div style="font-weight: 600; color: var(--text-primary);">Years Experience</div>
                <div style="color: var(--text-secondary); font-size: 0.9rem;">Professional certification</div>
            </div>
        </div>
        """
        
        st.markdown(stats_html, unsafe_allow_html=True)

class KeyDifferentiator:
    """Key differentiator section"""
    
    def render(self):
        """Render differentiator section"""
        st.markdown("## 🧠 Why Our Method Works")
        
        differentiator_html = """
        <div style="background: rgba(76, 161, 163, 0.1); border-radius: var(--radius-md);
                    padding: 1.5rem; margin: 2rem 0; border-left: 4px solid var(--accent);">
            <p style="font-size: 1.1rem; line-height: 1.7;">
                Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower (which fails 95% of the time). 
                Our method targets the <strong>root cause</strong> in your subconscious mind - where lasting change actually happens.
            </p>
        </div>
        """
        
        st.markdown(differentiator_html, unsafe_allow_html=True)

class QuizSection:
    """Quiz section - integrates with quiz component"""
    
    def render(self):
        """Render quiz section with proper integration"""
        st.markdown("## 🎯 30-Second Suitability Assessment")
        st.markdown("Discover your readiness for transformation in 3 quick questions")
        
        # Try to load the quiz component
        try:
            from components.quiz import Quiz
            quiz = Quiz()
            quiz.render()
        except ImportError:
            # Fallback if quiz component not available
            self._render_quiz_fallback()
        except Exception as e:
            st.error(f"Error loading quiz: {e}")
            self._render_quiz_fallback()
    
    def _render_quiz_fallback(self):
        """Fallback quiz if component fails to load"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); text-align: center;">
            <h3>Interactive Assessment Coming Soon!</h3>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                For now, book a free discovery call to assess your suitability
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <div style="background: rgba(76, 161, 163, 0.1); padding: 1rem; border-radius: var(--radius-sm); 
                            border: 1px solid var(--accent); min-width: 200px;">
                    <div style="font-weight: 600; color: var(--accent); margin-bottom: 0.5rem;">Quick Questions:</div>
                    <div style="font-size: 0.9rem; color: var(--text-secondary);">
                        • What would you like to change?<br>
                        • How long have you struggled?<br>
                        • How ready are you to change?
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_fallback_cta", type="primary", use_container_width=True):
                st.success("Great! We'll assess your suitability during the call.")

class ProcessOverview:
    """Process overview section"""
    
    def render(self):
        """Render process overview"""
        st.markdown("## Our Proven 2-Step Process")
        
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem; box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
                <div style="text-align: center; margin-bottom: 1rem;">
                    <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto;">1</div>
                </div>
                <h3 style="text-align: center; margin-bottom: 1rem;">🔍 Deep Analysis</h3>
                <p style="text-align: center; color: var(--text-secondary); margin-bottom: 1.5rem;">90 minutes</p>
                <ul style="margin: 0; padding-left: 1rem;">
                    <li>Uncover subconscious patterns</li>
                    <li>Map your unique triggers</li>
                    <li>Begin positive programming</li>
                    <li>Immediate relief starts</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 2rem; box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
                <div style="text-align: center; margin-bottom: 1rem;">
                    <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto;">2</div>
                </div>
                <h3 style="text-align: center; margin-bottom: 1rem;">⚡ Transformation</h3>
                <p style="text-align: center; color: var(--text-secondary); margin-bottom: 1.5rem;">90 minutes</p>
                <ul style="margin: 0; padding-left: 1rem;">
                    <li>Neural pathway rewiring</li>
                    <li>Install new behaviors</li>
                    <li>Lock in lasting change</li>
                    <li>Complete transformation</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

class TestimonialsSection:
    """Testimonials section with consistent styling"""
    
    def render(self):
        """Render testimonials"""
        st.markdown("## 💬 Real Success Stories")
        
        testimonials = [
            {
                "icon": "🌟",
                "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
                "author": "Director, Banking, Singapore",
                "concern": "Anxiety patterns",
                "duration": "2 sessions"
            },
            {
                "icon": "🚭",
                "quote": "My husband was a heavy smoker... No more addiction.",
                "author": "Wife, Bangkok",
                "concern": "Smoking cessation",
                "duration": "2 sessions"
            }
        ]
        
        for testimonial in testimonials:
            testimonial_html = f"""
            <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                        padding: 1.5rem; margin: 1rem 0; box-shadow: var(--shadow-sm); 
                        border: 1px solid var(--border); border-left: 4px solid var(--accent);">
                <div style="display: flex; align-items: flex-start; gap: 1rem;">
                    <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">
                        {testimonial['icon']}
                    </div>
                    <div style="flex: 1;">
                        <blockquote style="font-style: italic; font-size: 1.2rem; 
                                           color: var(--text-primary); margin: 0 0 1rem 0; line-height: 1.6;">
                            "{testimonial['quote']}"
                        </blockquote>
                        <div style="font-weight: 600; color: var(--text-secondary); margin-bottom: 0.5rem;">
                            — {testimonial['author']}
                        </div>
                        <div style="color: var(--accent); font-size: 0.9rem;">
                            🎯 {testimonial['concern']} • ⏱️ {testimonial['duration']}
                        </div>
                    </div>
                </div>
            </div>
            """
            st.markdown(testimonial_html, unsafe_allow_html=True)

class CallToAction:
    """Call to action section"""
    
    def render(self):
        """Render call to action"""
        st.markdown("## Ready to Transform Your Life?")
        
        cta_html = """
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">
                Join hundreds who have transformed their lives
            </h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; 
                      max-width: 500px; margin: 0 auto 2rem auto;">
                Your success story could be next. Start with a free discovery call.
            </p>
        </div>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📞 Free Discovery Call", key="cta_discovery", use_container_width=True):
                st.success("Great! We'll contact you within 24 hours.")
        
        with col2:
            if st.button("🎯 Retake Assessment", key="cta_retake", use_container_width=True):
                # Reset quiz state if available
                try:
                    from utils.session_state import reset_quiz
                    reset_quiz()
                    st.success("Assessment reset! Scroll up to retake.")
                    st.rerun()
                except ImportError:
                    st.info("Scroll up to retake the assessment!")
        
        with col3:
            if st.button("⚡ Book Sessions Now", key="cta_book", use_container_width=True):
                st.success("Excellent choice! Check your email for next steps.")

class HomePage:
    """Main home page component - includes quiz integration"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.stats = StatsSection()
        self.differentiator = KeyDifferentiator()
        self.quiz = QuizSection()
        self.process = ProcessOverview()
        self.testimonials = TestimonialsSection()
        self.cta = CallToAction()
    
    def render(self):
        """Render complete home page with quiz"""
        try:
            # Hero section
            self.hero.render()
            
            # Statistics
            self.stats.render()
            
            # Key differentiator
            self.differentiator.render()
            
            # 30-Second Quiz - THE MISSING COMPONENT!
            self.quiz.render()
            
            # Process overview
            self.process.render()
            
            # Testimonials
            self.testimonials.render()
            
            # Call to action
            self.cta.render()
            
        except Exception as e:
            st.error(f"Error rendering home page: {e}")
            # Minimal fallback
            st.title("Transform Your Life in Just 2 Sessions")
            st.markdown("Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits")
            
            # Quiz fallback
            st.markdown("## 🎯 30-Second Assessment")
            st.info("Take our quick assessment to see if you're a good fit for our program!")
            
            if st.button("📞 Book Free Discovery Call", type="primary"):
                st.success("We'll contact you within 24 hours!")

def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
