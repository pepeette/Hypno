"""
Home page component for the Hypnotherapy website
Features hero section, quiz, testimonials, and key information
"""
import streamlit as st

class HeroSection:
    """Hero section component for the home page"""
    
    def __init__(self):
        self.title = "Transform Your Life in Just 2 Sessions"
        self.subtitle = "Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits"
        self.cta_text = "Take the 30-Second Assessment"
    
    def render(self):
        """Render the hero section with enhanced styling"""
        # Get success rates from constants (with fallback)
        try:
            from utils.config import AppConstants
            success_rate = AppConstants.SUCCESS_RATES.get("two_sessions", 85)
        except ImportError:
            success_rate = 85
            
        # Create the HTML with proper escaping for CSS
        hero_html = f"""
        <div class="hero">
            <div class="hero-content">
                <h1 style="color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                    {self.title}
                </h1>
                <p style="font-size: 1.2rem; color: white; opacity: 0.95; 
                          max-width: 600px; margin: 1.5rem auto; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
                    {self.subtitle}
                </p>
                
                <div class="hero-stats" style="display: flex; justify-content: center; gap: 3rem; 
                                                margin: 2rem 0; flex-wrap: wrap;">
                    <div class="stat-item">
                        <div class="stat-number">{success_rate}%</div>
                        <div class="stat-label">Success in 2 Sessions</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">500+</div>
                        <div class="stat-label">Lives Transformed</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">10+</div>
                        <div class="stat-label">Years Experience</div>
                    </div>
                </div>
                
                <div style="margin-top: 2rem;">
                    <a href="#quiz" class="btn btn-primary" 
                       style="font-size: 1.1rem; padding: 1rem 2rem; 
                              background: white; color: var(--accent); 
                              box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                              text-decoration: none; border-radius: var(--radius-sm);
                              display: inline-block; font-weight: 600;
                              transition: all 0.3s ease;">
                        🎯 {self.cta_text}
                    </a>
                </div>
            </div>
        </div>
        """
        
        # Add the CSS separately to avoid f-string conflicts
        hero_css = """
        <style>
        .stat-item {
            text-align: center;
            color: white;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            margin-top: 0.5rem;
        }
        
        .hero a:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        
        @media (max-width: 768px) {
            .hero-stats {
                gap: 1.5rem;
            }
            
            .stat-number {
                font-size: 2rem;
            }
            
            .hero a {
                font-size: 1rem;
                padding: 0.8rem 1.5rem;
            }
        }
        </style>
        """
        
        st.markdown(hero_html, unsafe_allow_html=True)
        st.markdown(hero_css, unsafe_allow_html=True)

class KeyBenefits:
    """Key benefits section component"""
    
    def __init__(self):
        self.benefits = [
            {
                "icon": "⚡",
                "title": "Rapid Results",
                "description": "See transformation in just 2 sessions, not months of therapy"
            },
            {
                "icon": "🧠",
                "title": "Science-Backed",
                "description": "Uses proven neuroplasticity principles to rewire your subconscious"
            },
            {
                "icon": "🎯",
                "title": "Targeted Approach",
                "description": "Personalized sessions designed for your specific challenges"
            },
            {
                "icon": "💯",
                "title": "High Success Rate",
                "description": "85% of clients achieve their goals in our 2-session program"
            }
        ]
    
    def render(self):
        """Render the key benefits section"""
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0 3rem 0;">
            <h2>Why Choose Our 2-Session Method?</h2>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 1rem auto;">
                Traditional therapy focuses on symptoms. We target the root cause in your subconscious mind.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create benefit cards
        cols = st.columns(2 if len(self.benefits) == 4 else len(self.benefits))
        
        for i, benefit in enumerate(self.benefits):
            col_index = i % 2 if len(self.benefits) == 4 else i
            with cols[col_index]:
                self._render_benefit_card(benefit)
    
    def _render_benefit_card(self, benefit: dict):
        """Render individual benefit card"""
        card_html = f"""
        <div class="benefit-card">
            <div class="benefit-icon">{benefit['icon']}</div>
            <h3 class="benefit-title">{benefit['title']}</h3>
            <p class="benefit-description">{benefit['description']}</p>
        </div>
        
        <style>
        .benefit-card {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border);
            transition: var(--transition);
            margin-bottom: 2rem;
            height: 100%;
        }
        
        .benefit-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
            border-color: var(--accent);
        }
        
        .benefit-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .benefit-title {
            color: var(--text-primary);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }
        
        .benefit-description {
            color: var(--text-secondary);
            line-height: 1.6;
        }
        </style>
        """
        
        st.markdown(card_html, unsafe_allow_html=True)

class SocialProof:
    """Social proof section with testimonials and trust indicators"""
    
    def __init__(self):
        # Fallback testimonials if config not available
        self.testimonials = [
            {
                "icon": "🌟",
                "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
                "author": "Director, Banking, Singapore",
                "concern": "Anxiety",
                "duration": "2 sessions"
            },
            {
                "icon": "🎓", 
                "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
                "author": "Medical Student, Morocco",
                "concern": "Study anxiety",
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
        
        # Try to import from config if available
        try:
            from utils.config import TestimonialConfig
            self.testimonials = TestimonialConfig.TESTIMONIALS
        except ImportError:
            pass  # Use fallback testimonials above
            
        self.trust_indicators = [
            "✓ Certified Clinical Hypnotherapist",
            "✓ 10+ Years Experience",
            "✓ 500+ Successful Transformations",
            "✓ Confidentiality Guaranteed"
        ]
    
    def render(self):
        """Render the social proof section"""
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0 2rem 0;">
            <h2>Real Transformations from Real People</h2>
            <p style="font-size: 1.1rem; color: var(--text-secondary);">
                See what clients say about their life-changing experiences
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Render testimonials
        self._render_testimonials()
        
        # Render trust indicators
        self._render_trust_indicators()
    
    def _render_testimonials(self):
        """Render testimonial cards"""
        # Display testimonials in a single column for better readability
        for testimonial in self.testimonials:
            self._render_testimonial_card(testimonial)
    
    def _render_testimonial_card(self, testimonial: dict):
        """Render individual testimonial card"""
        testimonial_html = f"""
        <div class="testimonial-card card">
            <div style="display: flex; align-items: flex-start; gap: 1rem;">
                <div style="font-size: 2rem; color: var(--accent); 
                           min-width: 50px; text-align: center;">
                    {testimonial['icon']}
                </div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.1rem; 
                                       color: var(--text-primary); margin: 0 0 1rem 0;
                                       line-height: 1.6;">
                        "{testimonial['quote']}"
                    </blockquote>
                    <div style="display: flex; justify-content: space-between; 
                                align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div style="font-weight: 600; color: var(--text-secondary);">
                            — {testimonial['author']}
                        </div>
                        <div style="display: flex; gap: 1rem; font-size: 0.9rem; 
                                    color: var(--accent);">
                            <span>🎯 {testimonial.get('concern', 'General')}</span>
                            <span>⏱️ {testimonial.get('duration', '2 sessions')}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(testimonial_html, unsafe_allow_html=True)
    
    def _render_trust_indicators(self):
        """Render trust indicators"""
        trust_html = """
        <div style="background: var(--card-bg); border-radius: var(--radius-md);
                    padding: 2rem; margin: 3rem 0; text-align: center;
                    border: 1px solid var(--border);">
            <h3 style="color: var(--accent); margin-bottom: 2rem;">Why Trust Our Method?</h3>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;">
        """
        
        for indicator in self.trust_indicators:
            trust_html += f"""
                <div style="color: var(--text-secondary); font-weight: 500;">
                    {indicator}
                </div>
            """
        
        trust_html += """
            </div>
        </div>
        """
        
        st.markdown(trust_html, unsafe_allow_html=True)

class ProcessPreview:
    """Quick preview of the 2-step process"""
    
    def __init__(self):
        self.steps = [
            {
                "number": "1",
                "title": "Deep Analysis",
                "description": "Uncover your unique subconscious patterns",
                "duration": "90 minutes"
            },
            {
                "number": "2", 
                "title": "Transformation",
                "description": "Rewire your mind for lasting change",
                "duration": "90 minutes"
            }
        ]
    
    def render(self):
        """Render the process preview"""
        st.markdown("""
        <div style="text-align: center; margin: 4rem 0 2rem 0;">
            <h2>How It Works</h2>
            <p style="font-size: 1.1rem; color: var(--text-secondary);">
                Our proven 2-step process that creates lasting transformation
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(len(self.steps))
        
        for i, step in enumerate(self.steps):
            with cols[i]:
                self._render_step_card(step)
        
        # Call-to-action
        st.markdown("""
        <div style="text-align: center; margin: 3rem 0;">
            <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 2rem;">
                Ready to start your transformation?
            </p>
            <a href="#method" class="btn btn-secondary" 
               style="text-decoration: none; margin-right: 1rem;">
                Learn More About Our Method
            </a>
            <a href="#discovery" class="btn btn-primary" style="text-decoration: none;">
                Book Your Free Discovery Call
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_step_card(self, step: dict):
        """Render individual step card"""
        step_html = f"""
        <div class="process-step-card">
            <div class="step-number">{step['number']}</div>
            <h3 class="step-title">{step['title']}</h3>
            <p class="step-description">{step['description']}</p>
            <div class="step-duration">{step['duration']}</div>
        </div>
        
        <style>
        .process-step-card {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border);
            transition: var(--transition);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }
        
        .process-step-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }
        
        .step-number {
            width: 60px;
            height: 60px;
            background: var(--accent);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: bold;
            margin: 0 auto 1.5rem auto;
        }
        
        .step-title {
            color: var(--text-primary);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }
        
        .step-description {
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        .step-duration {
            color: var(--accent);
            font-weight: 600;
            font-size: 0.9rem;
        }
        </style>
        """
        
        st.markdown(step_html, unsafe_allow_html=True)

class HomePage:
    """Main home page component that orchestrates all sections"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.benefits = KeyBenefits()
        self.social_proof = SocialProof()
        self.process = ProcessPreview()
    
    def render(self):
        """Render the complete home page"""
        # Hero section
        self.hero.render()
        
        # Quiz section (main focal point) - import locally to avoid circular imports
        st.markdown('<div id="quiz"></div>', unsafe_allow_html=True)
        self._render_quiz()
        
        # Key benefits
        self.benefits.render()
        
        # Process preview
        self.process.render()
        
        # Social proof
        self.social_proof.render()
        
        # Final call-to-action
        self._render_final_cta()
    
    def _render_quiz(self):
        """Render quiz with fallback if component not available"""
        try:
            from components.quiz import Quiz
            quiz = Quiz()
            quiz.render()
        except ImportError:
            # Fallback quiz placeholder
            st.markdown("""
            <div style="background: var(--card-bg); border-radius: var(--radius-md);
                        padding: 3rem 2rem; text-align: center; margin: 2rem 0;
                        border: 1px solid var(--border);">
                <h2>30-Second Suitability Assessment</h2>
                <p style="font-size: 1.1rem; color: var(--text-secondary); margin: 1rem 0;">
                    Interactive quiz coming soon! For now, book a free discovery call to assess your suitability.
                </p>
                <a href="#discovery" class="btn btn-primary" style="text-decoration: none;">
                    📞 Book Free Discovery Call
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_final_cta(self):
        """Render final call-to-action section"""
        cta_html = """
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">
                Ready to Transform Your Life?
            </h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; 
                      max-width: 500px; margin: 0 auto 2rem auto;">
                Join hundreds of people who have already transformed their lives 
                with our proven 2-session method.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#discovery" class="btn" 
                   style="background: white; color: var(--accent); text-decoration: none;
                          padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; transition: all 0.3s ease;">
                    📞 Free Discovery Call
                </a>
                <a href="#method" class="btn" 
                   style="background: transparent; color: white; text-decoration: none;
                          padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; border: 2px solid white;
                          transition: all 0.3s ease;">
                    🧠 Learn Our Method
                </a>
            </div>
        </div>
        """
        
        st.markdown(cta_html, unsafe_allow_html=True)

# Factory function for easy import
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
