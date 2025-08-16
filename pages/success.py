"""
Success stories page component for the Hypnotherapy website
Features client testimonials, case studies, and success metrics
"""
import streamlit as st

class SuccessPage:
    """Success stories page component"""
    
    def __init__(self):
        self.testimonials = [
            {
                "icon": "🌟",
                "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
                "author": "Director, Banking, Singapore",
                "concern": "Anxiety patterns",
                "duration": "2 sessions",
                "details": "After struggling with performance anxiety for years, I was skeptical but desperate. The first session revealed triggers I never knew existed. By session two, I felt like a completely different person."
            },
            {
                "icon": "🎓", 
                "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
                "author": "Medical Student, Morocco",
                "concern": "Study anxiety & focus",
                "duration": "2 sessions",
                "details": "Medical school stress was overwhelming me. I couldn't concentrate and was considering dropping out. Now I'm excelling in my internship and feel confident about my future."
            },
            {
                "icon": "🚭",
                "quote": "My husband was a heavy smoker... No more addiction.",
                "author": "Wife, Bangkok",
                "concern": "Smoking cessation",
                "duration": "2 sessions",
                "details": "After 20 years of smoking 2 packs a day, my husband tried everything. Patches, gum, medications - nothing worked. Two sessions later, he doesn't even think about cigarettes."
            }
        ]
        
        self.case_studies = [
            {
                "title": "From 2 Packs a Day to Smoke-Free",
                "challenge": "20-year smoking habit, 2 packs daily",
                "solution": "Subconscious pattern rewiring",
                "result": "Completely smoke-free after 2 sessions",
                "timeline": "2 weeks",
                "follow_up": "6 months later - still smoke-free, saved 30,000 THB"
            },
            {
                "title": "Overcoming Panic Attacks",
                "challenge": "Daily panic attacks affecting work performance",
                "solution": "Root cause analysis and neural rewiring",
                "result": "Panic attacks eliminated, confidence restored",
                "timeline": "10 days",
                "follow_up": "1 year later - promoted at work, no anxiety"
            }
        ]
    
    def render(self):
        """Render the complete success page"""
        self._render_header()
        self._render_testimonials()
        self._render_case_studies()
        self._render_success_metrics()
        self._render_transformation_timeline()
        self._render_cta()
    
    def _render_header(self):
        """Render page header"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <h1>Real Transformations from Real People</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                See how our clients have transformed their lives in just 2 sessions
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_testimonials(self):
        """Render detailed testimonials"""
        st.markdown("## 💬 Client Stories")
        
        for testimonial in self.testimonials:
            self._render_testimonial_card(testimonial)
    
    def _render_testimonial_card(self, testimonial):
        """Render individual testimonial with expandable details"""
        testimonial_html = f"""
        <div class="testimonial-card card">
            <div style="display: flex; align-items: flex-start; gap: 1rem;">
                <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">
                    {testimonial['icon']}
                </div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; 
                                       color: var(--text-primary); margin: 0 0 1rem 0;
                                       line-height: 1.6; font-weight: 500;">
                        "{testimonial['quote']}"
                    </blockquote>
                    <div style="margin-bottom: 1rem;">
                        <div style="font-weight: 600; color: var(--text-secondary); margin-bottom: 0.5rem;">
                            — {testimonial['author']}
                        </div>
                        <div style="display: flex; gap: 1rem; font-size: 0.9rem; color: var(--accent); flex-wrap: wrap;">
                            <span>🎯 {testimonial['concern']}</span>
                            <span>⏱️ {testimonial['duration']}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(testimonial_html, unsafe_allow_html=True)
        
        # Expandable details
        with st.expander("📖 Read Full Story", expanded=False):
            st.markdown(f"**The Challenge:** {testimonial['concern']}")
            st.markdown(f"**The Story:** {testimonial['details']}")
            st.markdown(f"**The Result:** Transformation completed in {testimonial['duration']}")
    
    def _render_case_studies(self):
        """Render detailed case studies"""
        st.markdown("## 📊 Detailed Case Studies")
        
        for i, case in enumerate(self.case_studies):
            self._render_case_study(case, i)
    
    def _render_case_study(self, case, index):
        """Render individual case study"""
        case_html = f"""
        <div class="card-elevated" style="margin: 2rem 0;">
            <h3 style="color: var(--accent); margin-bottom: 1rem;">
                Case Study {index + 1}: {case['title']}
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
                <div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">🎯 Challenge</h4>
                    <p>{case['challenge']}</p>
                </div>
                <div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">🔧 Solution</h4>
                    <p>{case['solution']}</p>
                </div>
                <div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">✅ Result</h4>
                    <p>{case['result']}</p>
                </div>
                <div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">⏰ Timeline</h4>
                    <p>{case['timeline']}</p>
                </div>
            </div>
            <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(76, 161, 163, 0.1); 
                        border-radius: var(--radius-sm); border-left: 4px solid var(--accent);">
                <h4 style="color: var(--accent); margin-bottom: 0.5rem;">📈 Follow-up</h4>
                <p style="margin: 0;">{case['follow_up']}</p>
            </div>
        </div>
        """
        
        st.markdown(case_html, unsafe_allow_html=True)
    
    def _render_success_metrics(self):
        """Render success statistics"""
        st.markdown("## 📈 Success Metrics")
        
        metrics_html = """
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                    gap: 2rem; margin: 2rem 0;">
            <div class="metric-card">
                <div class="metric-number">85%</div>
                <div class="metric-label">Success Rate</div>
                <div class="metric-detail">Complete transformation in 2 sessions</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">500+</div>
                <div class="metric-label">Lives Changed</div>
                <div class="metric-detail">Clients transformed since 2014</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">15%</div>
                <div class="metric-label">Need 3rd Session</div>
                <div class="metric-detail">Additional reinforcement</div>
            </div>
            <div class="metric-card">
                <div class="metric-number">95%</div>
                <div class="metric-label">Long-term Success</div>
                <div class="metric-detail">Still transformed 1 year later</div>
            </div>
        </div>
        
        <style>
        .metric-card {
            background: var(--card-bg);
            border-radius: var(--radius-md);
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border);
            transition: var(--transition);
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }
        
        .metric-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        
        .metric-detail {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        </style>
        """
        
        st.markdown(metrics_html, unsafe_allow_html=True)
    
    def _render_transformation_timeline(self):
        """Render typical transformation timeline"""
        st.markdown("## ⏰ Typical Transformation Timeline")
        
        timeline_html = """
        <div class="timeline-container">
            <div class="timeline-item">
                <div class="timeline-marker">📞</div>
                <div class="timeline-content">
                    <h4>Discovery Call</h4>
                    <p>15-minute consultation to understand your goals and assess suitability</p>
                    <span class="timeline-time">Day 0</span>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-marker">🔍</div>
                <div class="timeline-content">
                    <h4>Session 1: Analysis</h4>
                    <p>Deep dive into subconscious patterns, immediate relief begins</p>
                    <span class="timeline-time">Day 1</span>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-marker">⚡</div>
                <div class="timeline-content">
                    <h4>Session 2: Transformation</h4>
                    <p>Complete neural rewiring, most clients feel dramatically different</p>
                    <span class="timeline-time">Day 7-10</span>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-marker">🎯</div>
                <div class="timeline-content">
                    <h4>Follow-up Check</h4>
                    <p>Email support to ensure lasting results, optional 3rd session if needed</p>
                    <span class="timeline-time">Day 30</span>
                </div>
            </div>
        </div>
        
        <style>
        .timeline-container {
            position: relative;
            margin: 2rem 0;
        }
        
        .timeline-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 2rem;
            position: relative;
        }
        
        .timeline-marker {
            background: var(--accent);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            margin-right: 1.5rem;
            position: relative;
            z-index: 2;
        }
        
        .timeline-item:not(:last-child) .timeline-marker::after {
            content: '';
            position: absolute;
            top: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            height: 40px;
            background: var(--border);
        }
        
        .timeline-content {
            flex: 1;
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border);
            position: relative;
        }
        
        .timeline-content h4 {
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        
        .timeline-content p {
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }
        
        .timeline-time {
            color: var(--accent);
            font-weight: 600;
            font-size: 0.9rem;
        }
        </style>
        """
        
        st.markdown(timeline_html, unsafe_allow_html=True)
    
    def _render_cta(self):
        """Render call-to-action"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
                    border-radius: var(--radius-lg); padding: 3rem 2rem; 
                    text-align: center; margin: 4rem 0;">
            <h2 style="color: white; margin-bottom: 1rem;">
                Ready to Write Your Success Story?
            </h2>
            <p style="color: white; opacity: 0.9; font-size: 1.1rem; 
                      max-width: 500px; margin: 0 auto 2rem auto;">
                Join hundreds of people who have already transformed their lives. 
                Your success story could be next.
            </p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <a href="#discovery" class="btn" 
                   style="background: white; color: var(--accent); text-decoration: none;
                          padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; transition: all 0.3s ease;">
                    📞 Start Your Transformation
                </a>
                <a href="#quiz" class="btn" 
                   style="background: transparent; color: white; text-decoration: none;
                          padding: 1rem 2rem; border-radius: var(--radius-sm);
                          font-weight: 600; border: 2px solid white;
                          transition: all 0.3s ease;">
                    🎯 Take Assessment
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
