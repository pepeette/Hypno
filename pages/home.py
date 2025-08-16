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
        """Render the hero section using Streamlit native components"""
        # Apply basic styling
        st.markdown("""
        <style>
        .hero-container {
            background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%);
            padding: 3rem 2rem;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 2rem;
        }
        .hero-title {
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .hero-subtitle {
            color: white;
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        .stat-item {
            text-align: center;
            color: white;
            margin: 1rem;
        }
        .stat-number {
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .stat-label {
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Hero container
        st.markdown('<div class="hero-container">', unsafe_allow_html=True)
        
        # Title and subtitle using Streamlit
        st.markdown(f'<h1 class="hero-title">{self.title}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle">{self.subtitle}</p>', unsafe_allow_html=True)
        
        # Statistics using columns
        st.markdown('<div class="stats-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">85%</div>
                <div class="stat-label">Success in 2 Sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Lives Transformed</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="stat-item">
                <div class="stat-number">10+</div>
                <div class="stat-label">Years Experience</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # CTA Button
        st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
        if st.button("🎯 " + self.cta_text, key="hero_cta", type="primary"):
            st.markdown("Redirecting to assessment...")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Close hero container
        st.markdown('</div>', unsafe_allow_html=True)

class KeyBenefits:
    """Key benefits section component"""
    
    def render(self):
        """Render key benefits using Streamlit components"""
        st.markdown("---")
        st.markdown("## Why Choose Our 2-Session Method?")
        st.markdown("Traditional therapy focuses on symptoms. We target the root cause in your subconscious mind.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⚡ Rapid Results")
            st.write("See transformation in just 2 sessions, not months of therapy")
            
            st.markdown("### 🎯 Targeted Approach")
            st.write("Personalized sessions designed for your specific challenges")
        
        with col2:
            st.markdown("### 🧠 Science-Backed")
            st.write("Uses proven neuroplasticity principles to rewire your subconscious")
            
            st.markdown("### 💯 High Success Rate")
            st.write("85% of clients achieve their goals in our 2-session program")

class SocialProof:
    """Social proof section with testimonials"""
    
    def render(self):
        """Render testimonials using Streamlit components"""
        st.markdown("---")
        st.markdown("## Real Transformations from Real People")
        
        # Testimonial 1
        with st.container():
            st.markdown("### 🌟 Director, Banking, Singapore")
            st.markdown("*\"Finally broke free from old patterns – 2 sessions changed everything.\"*")
            st.caption("Concern: Anxiety patterns • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 2
        with st.container():
            st.markdown("### 🎓 Medical Student, Morocco")
            st.markdown("*\"I was struggling with my studies abroad... now doing my specialization internship.\"*")
            st.caption("Concern: Study anxiety & focus • Duration: 2 sessions")
        
        st.markdown("")
        
        # Testimonial 3
        with st.container():
            st.markdown("### 🚭 Wife, Bangkok")
            st.markdown("*\"My husband was a heavy smoker... No more addiction.\"*")
            st.caption("Concern: Smoking cessation • Duration: 2 sessions")

class ProcessPreview:
    """Quick preview of the 2-step process"""
    
    def render(self):
        """Render process preview using Streamlit components"""
        st.markdown("---")
        st.markdown("## How It Works")
        st.markdown("Our proven 2-step process that creates lasting transformation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 1️⃣ Deep Analysis")
            st.markdown("**90 minutes**")
            st.write("Uncover your unique subconscious patterns")
            st.write("• Map personal behavior patterns")
            st.write("• Identify root causes vs symptoms")
            st.write("• Install initial positive programming")
        
        with col2:
            st.markdown("### 2️⃣ Transformation")
            st.markdown("**90 minutes • 3-7 days later**")
            st.write("Rewire your mind for lasting change")
            st.write("• Deep hypnotic state for rewiring")
            st.write("• Replace old patterns with new ones")
            st.write("• Lock in your new identity")
        
        st.markdown("")
        st.markdown("**Ready to start your transformation?**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📞 Free Discovery Call", key="process_discovery"):
                st.success("Redirecting to booking...")
        with col2:
            if st.button("🧠 Learn More", key="process_method"):
                st.success("Redirecting to method page...")

class HomePage:
    """Main home page component that orchestrates all sections"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.benefits = KeyBenefits()
        self.social_proof = SocialProof()
        self.process = ProcessPreview()
    
    def render(self):
        """Render the complete home page"""
        try:
            # Hero section
            self.hero.render()
            
            # Quiz section placeholder
            self._render_quiz_placeholder()
            
            # Key benefits
            self.benefits.render()
            
            # Process preview
            self.process.render()
            
            # Social proof
            self.social_proof.render()
            
            # Final call-to-action
            self._render_final_cta()
            
        except Exception as e:
            st.error("Error loading home page content.")
            st.markdown("## Welcome to 2-Step Hypnotherapy")
            st.markdown("Transform your life with science-backed hypnotherapy in just 2 sessions.")
            if st.button("📞 Contact Us"):
                st.success("Please email: laetitiasheppard@gmail.com")
    
    def _render_quiz_placeholder(self):
        """Render simple quiz placeholder"""
        st.markdown("---")
        st.markdown("## 30-Second Suitability Assessment")
        
        st.info("📝 Interactive quiz coming soon! For now, book a free discovery call to assess your suitability.")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_placeholder", type="primary"):
                st.success("We'll contact you within 24 hours to schedule your call!")
    
    def _render_final_cta(self):
        """Render final call-to-action section"""
        st.markdown("---")
        
        # Create a colored container using Streamlit
        st.markdown("""
        <style>
        .cta-container {
            background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
            padding: 3rem 2rem;
            border-radius: 16px;
            text-align: center;
            margin: 2rem 0;
        }
        .cta-title {
            color: white;
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .cta-text {
            color: white;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="cta-container">', unsafe_allow_html=True)
        st.markdown('<h2 class="cta-title">Ready to Transform Your Life?</h2>', unsafe_allow_html=True)
        st.markdown('<p class="cta-text">Join hundreds of people who have already transformed their lives with our proven 2-session method.</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("📞 Free Discovery Call", key="final_discovery"):
                st.success("Excellent choice! We'll be in touch soon.")
        with col2:
            if st.button("🧠 Learn Our Method", key="final_method"):
                st.success("Redirecting to method page...")
        with col3:
            if st.button("⚡ Book Sessions Now", key="final_book"):
                st.success("Great! Let's get started.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Factory function for easy import
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()

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
        try:
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
            
        except Exception as e:
            st.error("Error loading home page content. Please refresh the page.")
            # Fallback content
            st.markdown("## Welcome to 2-Step Hypnotherapy")
            st.markdown("Transform your life with science-backed hypnotherapy in just 2 sessions.")
    
    def _render_quiz(self):
        """Render quiz with fallback if component not available"""
        try:
            from components.quiz import Quiz
            quiz = Quiz()
            quiz.render()
        except ImportError:
            # Fallback quiz placeholder
            st.markdown("""
            <div style="background: #FFFFFF; border-radius: 12px;
                        padding: 3rem 2rem; text-align: center; margin: 2rem 0;
                        border: 1px solid #CBD5E1; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <h2 style="color: #273548; margin-bottom: 1rem;">30-Second Suitability Assessment</h2>
                <p style="font-size: 1.1rem; color: #556D7A; margin: 1rem 0;">
                    Interactive quiz coming soon! For now, book a free discovery call to assess your suitability.
                </p>
                <a href="#discovery" 
                   style="display: inline-block; background-color: #4CA1A3; color: white;
                          text-decoration: none; padding: 1rem 2rem; border-radius: 8px;
                          font-weight: 600; transition: all 0.3s ease;">
                    📞 Book Free Discovery Call
                </a>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.info("Assessment tool is loading. Please try again in a moment.")
    
    def _render_final_cta(self):
        """Render final call-to-action section"""
        try:
            cta_html = """
            <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                        border-radius: 16px; padding: 3rem 2rem; 
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
                    <a href="#discovery" 
                       style="background: white; color: #4CA1A3; text-decoration: none;
                              padding: 1rem 2rem; border-radius: 8px;
                              font-weight: 600; transition: all 0.3s ease;">
                        📞 Free Discovery Call
                    </a>
                    <a href="#method" 
                       style="background: transparent; color: white; text-decoration: none;
                              padding: 1rem 2rem; border-radius: 8px;
                              font-weight: 600; border: 2px solid white;
                              transition: all 0.3s ease;">
                        🧠 Learn Our Method
                    </a>
                </div>
            </div>
            """
            
            st.markdown(cta_html, unsafe_allow_html=True)
        except Exception:
            # Simple fallback CTA
            st.markdown("---")
            st.markdown("### Ready to Get Started?")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("📞 **Free Discovery Call**")
                st.markdown("15-minute consultation")
            with col2:
                st.markdown("⚡ **Book Sessions**")
                st.markdown("2-session transformation")

# Factory function for easy import
def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
