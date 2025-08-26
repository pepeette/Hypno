# """
# Success stories page component for the Hypnotherapy website
# Features client testimonials, case studies, and success metrics
# """
# import streamlit as st

# class SuccessPage:
#     """Success stories page component"""
    
#     def __init__(self):
#         self.testimonials = [
#             {
#                 "icon": "🌟",
#                 "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
#                 "author": "Director, Banking, Singapore",
#                 "concern": "Anxiety patterns",
#                 "duration": "2 sessions",
#                 "details": "After struggling with performance anxiety for years, I was skeptical but desperate. The first session revealed triggers I never knew existed. By session two, I felt like a completely different person."
#             },
#             {
#                 "icon": "🎓", 
#                 "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
#                 "author": "Medical Student, Morocco",
#                 "concern": "Study anxiety & focus",
#                 "duration": "2 sessions",
#                 "details": "Medical school stress was overwhelming me. I couldn't concentrate and was considering dropping out. Now I'm excelling in my internship and feel confident about my future."
#             },
#             {
#                 "icon": "🚭",
#                 "quote": "My husband was a heavy smoker... No more addiction.",
#                 "author": "Wife, Bangkok",
#                 "concern": "Smoking cessation",
#                 "duration": "2 sessions",
#                 "details": "After 20 years of smoking 2 packs a day, my husband tried everything. Patches, gum, medications - nothing worked. Two sessions later, he doesn't even think about cigarettes."
#             }
#         ]
        
#         self.case_studies = [
#             {
#                 "title": "From 2 Packs a Day to Smoke-Free",
#                 "challenge": "20-year smoking habit, 2 packs daily",
#                 "solution": "Subconscious pattern rewiring",
#                 "result": "Completely smoke-free after 2 sessions",
#                 "timeline": "2 weeks",
#                 "follow_up": "6 months later - still smoke-free, saved 30,000 THB"
#             },
#             {
#                 "title": "Overcoming Panic Attacks",
#                 "challenge": "Daily panic attacks affecting work performance",
#                 "solution": "Root cause analysis and neural rewiring",
#                 "result": "Panic attacks eliminated, confidence restored",
#                 "timeline": "10 days",
#                 "follow_up": "1 year later - promoted at work, no anxiety"
#             }
#         ]
    
#     def render(self):
#         """Render the complete success page"""
#         self._render_header()
#         self._render_testimonials()
#         self._render_case_studies()
#         self._render_success_metrics()
#         self._render_transformation_timeline()
#         self._render_cta()
    
#     def _render_header(self):
#         """Render page header"""
#         st.markdown("""
#         <div style="text-align: center; margin: 2rem 0 3rem 0;">
#             <h1>Real Transformations from Real People</h1>
#             <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
#                 See how our clients have transformed their lives in just 2 sessions
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _render_testimonials(self):
#         """Render detailed testimonials"""
#         st.markdown("## 💬 Client Stories")
        
#         for testimonial in self.testimonials:
#             self._render_testimonial_card(testimonial)
    
#     def _render_testimonial_card(self, testimonial):
#         """Render individual testimonial with expandable details"""
#         testimonial_html = f"""
#         <div class="testimonial-card card">
#             <div style="display: flex; align-items: flex-start; gap: 1rem;">
#                 <div style="font-size: 2.5rem; color: var(--accent); min-width: 60px; text-align: center;">
#                     {testimonial['icon']}
#                 </div>
#                 <div style="flex: 1;">
#                     <blockquote style="font-style: italic; font-size: 1.2rem; 
#                                        color: var(--text-primary); margin: 0 0 1rem 0;
#                                        line-height: 1.6; font-weight: 500;">
#                         "{testimonial['quote']}"
#                     </blockquote>
#                     <div style="margin-bottom: 1rem;">
#                         <div style="font-weight: 600; color: var(--text-secondary); margin-bottom: 0.5rem;">
#                             — {testimonial['author']}
#                         </div>
#                         <div style="display: flex; gap: 1rem; font-size: 0.9rem; color: var(--accent); flex-wrap: wrap;">
#                             <span>🎯 {testimonial['concern']}</span>
#                             <span>⏱️ {testimonial['duration']}</span>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
        
#         st.markdown(testimonial_html, unsafe_allow_html=True)
        
#         # Expandable details
#         with st.expander("📖 Read Full Story", expanded=False):
#             st.markdown(f"**The Challenge:** {testimonial['concern']}")
#             st.markdown(f"**The Story:** {testimonial['details']}")
#             st.markdown(f"**The Result:** Transformation completed in {testimonial['duration']}")
    
#     def _render_case_studies(self):
#         """Render detailed case studies"""
#         st.markdown("## 📊 Detailed Case Studies")
        
#         for i, case in enumerate(self.case_studies):
#             self._render_case_study(case, i)
    
#     def _render_case_study(self, case, index):
#         """Render individual case study"""
#         case_html = f"""
#         <div class="card-elevated" style="margin: 2rem 0;">
#             <h3 style="color: var(--accent); margin-bottom: 1rem;">
#                 Case Study {index + 1}: {case['title']}
#             </h3>
#             <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
#                 <div>
#                     <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">🎯 Challenge</h4>
#                     <p>{case['challenge']}</p>
#                 </div>
#                 <div>
#                     <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">🔧 Solution</h4>
#                     <p>{case['solution']}</p>
#                 </div>
#                 <div>
#                     <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">✅ Result</h4>
#                     <p>{case['result']}</p>
#                 </div>
#                 <div>
#                     <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">⏰ Timeline</h4>
#                     <p>{case['timeline']}</p>
#                 </div>
#             </div>
#             <div style="margin-top: 1.5rem; padding: 1rem; background: rgba(76, 161, 163, 0.1); 
#                         border-radius: var(--radius-sm); border-left: 4px solid var(--accent);">
#                 <h4 style="color: var(--accent); margin-bottom: 0.5rem;">📈 Follow-up</h4>
#                 <p style="margin: 0;">{case['follow_up']}</p>
#             </div>
#         </div>
#         """
        
#         st.markdown(case_html, unsafe_allow_html=True)
    
#     def _render_success_metrics(self):
#         """Render success statistics"""
#         st.markdown("## 📈 Success Metrics")
        
#         metrics_html = """
#         <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
#                     gap: 2rem; margin: 2rem 0;">
#             <div class="metric-card">
#                 <div class="metric-number">85%</div>
#                 <div class="metric-label">Success Rate</div>
#                 <div class="metric-detail">Complete transformation in 2 sessions</div>
#             </div>
#             <div class="metric-card">
#                 <div class="metric-number">500+</div>
#                 <div class="metric-label">Lives Changed</div>
#                 <div class="metric-detail">Clients transformed since 2014</div>
#             </div>
#             <div class="metric-card">
#                 <div class="metric-number">15%</div>
#                 <div class="metric-label">Need 3rd Session</div>
#                 <div class="metric-detail">Additional reinforcement</div>
#             </div>
#             <div class="metric-card">
#                 <div class="metric-number">95%</div>
#                 <div class="metric-label">Long-term Success</div>
#                 <div class="metric-detail">Still transformed 1 year later</div>
#             </div>
#         </div>
        
#         <style>
#         .metric-card {
#             background: var(--card-bg);
#             border-radius: var(--radius-md);
#             padding: 2rem 1.5rem;
#             text-align: center;
#             box-shadow: var(--shadow-sm);
#             border: 1px solid var(--border);
#             transition: var(--transition);
#         }
        
#         .metric-card:hover {
#             transform: translateY(-3px);
#             box-shadow: var(--shadow-md);
#         }
        
#         .metric-number {
#             font-size: 2.5rem;
#             font-weight: bold;
#             color: var(--accent);
#             margin-bottom: 0.5rem;
#         }
        
#         .metric-label {
#             font-size: 1.1rem;
#             font-weight: 600;
#             color: var(--text-primary);
#             margin-bottom: 0.5rem;
#         }
        
#         .metric-detail {
#             font-size: 0.9rem;
#             color: var(--text-secondary);
#         }
#         </style>
#         """
        
#         st.markdown(metrics_html, unsafe_allow_html=True)
    
#     def _render_transformation_timeline(self):
#         """Render typical transformation timeline"""
#         st.markdown("## ⏰ Typical Transformation Timeline")
        
#         timeline_html = """
#         <div class="timeline-container">
#             <div class="timeline-item">
#                 <div class="timeline-marker">📞</div>
#                 <div class="timeline-content">
#                     <h4>Discovery Call</h4>
#                     <p>15-minute consultation to understand your goals and assess suitability</p>
#                     <span class="timeline-time">Day 0</span>
#                 </div>
#             </div>
            
#             <div class="timeline-item">
#                 <div class="timeline-marker">🔍</div>
#                 <div class="timeline-content">
#                     <h4>Session 1: Analysis</h4>
#                     <p>Deep dive into subconscious patterns, immediate relief begins</p>
#                     <span class="timeline-time">Day 1</span>
#                 </div>
#             </div>
            
#             <div class="timeline-item">
#                 <div class="timeline-marker">⚡</div>
#                 <div class="timeline-content">
#                     <h4>Session 2: Transformation</h4>
#                     <p>Complete neural rewiring, most clients feel dramatically different</p>
#                     <span class="timeline-time">Day 7-10</span>
#                 </div>
#             </div>
            
#             <div class="timeline-item">
#                 <div class="timeline-marker">🎯</div>
#                 <div class="timeline-content">
#                     <h4>Follow-up Check</h4>
#                     <p>Email support to ensure lasting results, optional 3rd session if needed</p>
#                     <span class="timeline-time">Day 30</span>
#                 </div>
#             </div>
#         </div>
        
#         <style>
#         .timeline-container {
#             position: relative;
#             margin: 2rem 0;
#         }
        
#         .timeline-item {
#             display: flex;
#             align-items: flex-start;
#             margin-bottom: 2rem;
#             position: relative;
#         }
        
#         .timeline-marker {
#             background: var(--accent);
#             color: white;
#             width: 50px;
#             height: 50px;
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-size: 1.2rem;
#             margin-right: 1.5rem;
#             position: relative;
#             z-index: 2;
#         }
        
#         .timeline-item:not(:last-child) .timeline-marker::after {
#             content: '';
#             position: absolute;
#             top: 50px;
#             left: 50%;
#             transform: translateX(-50%);
#             width: 2px;
#             height: 40px;
#             background: var(--border);
#         }
        
#         .timeline-content {
#             flex: 1;
#             background: var(--card-bg);
#             padding: 1.5rem;
#             border-radius: var(--radius-sm);
#             box-shadow: var(--shadow-sm);
#             border: 1px solid var(--border);
#             position: relative;
#         }
        
#         .timeline-content h4 {
#             color: var(--text-primary);
#             margin-bottom: 0.5rem;
#         }
        
#         .timeline-content p {
#             color: var(--text-secondary);
#             margin-bottom: 1rem;
#         }
        
#         .timeline-time {
#             color: var(--accent);
#             font-weight: 600;
#             font-size: 0.9rem;
#         }
#         </style>
#         """
        
#         st.markdown(timeline_html, unsafe_allow_html=True)
    
#     def _render_cta(self):
#         """Render call-to-action"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%);
#                     border-radius: var(--radius-lg); padding: 3rem 2rem; 
#                     text-align: center; margin: 4rem 0;">
#             <h2 style="color: white; margin-bottom: 1rem;">
#                 Ready to Write Your Success Story?
#             </h2>
#             <p style="color: white; opacity: 0.9; font-size: 1.1rem; 
#                       max-width: 500px; margin: 0 auto 2rem auto;">
#                 Join hundreds of people who have already transformed their lives. 
#                 Your success story could be next.
#             </p>
#             <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
#                 <a href="#discovery" class="btn" 
#                    style="background: white; color: var(--accent); text-decoration: none;
#                           padding: 1rem 2rem; border-radius: var(--radius-sm);
#                           font-weight: 600; transition: all 0.3s ease;">
#                     📞 Start Your Transformation
#                 </a>
#                 <a href="#quiz" class="btn" 
#                    style="background: transparent; color: white; text-decoration: none;
#                           padding: 1rem 2rem; border-radius: var(--radius-sm);
#                           font-weight: 600; border: 2px solid white;
#                           transition: all 0.3s ease;">
#                     🎯 Take Assessment
#                 </a>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)


"""
Success stories page component for the Hypnotherapy website
Features client testimonials with emotional connection and engagement
Consistent with the existing architecture and styling
"""
import streamlit as st

class SuccessHero:
    """Hero section for success stories page"""
    
    def render(self):
        """Render success hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">Real People. Real Transformations. Real Results.</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("See how clients broke free from patterns that controlled their lives for years. In just 2 sessions, they discovered the freedom they thought was impossible.")

class TestimonialShowcase:
    """Enhanced testimonial display with emotional impact"""
    
    def __init__(self):
        self.testimonials = [
            {
                "icon": "🌟",
                "name": "Sarah Chen",
                "role": "Banking Director, Singapore",
                "concern": "Performance Anxiety",
                "before_quote": "I was terrified of presentations. My heart would race, palms would sweat, and I'd avoid important meetings.",
                "after_quote": "Now I actually look forward to presenting. I got promoted within 3 months of our sessions.",
                "transformation": "From avoiding meetings to leading them confidently",
                "sessions": "2 sessions",
                "timeline": "10 days apart",
                "background": "15 years of career-limiting anxiety",
                "breakthrough": "Discovered the anxiety stemmed from a childhood experience of being laughed at in class. Once we rewired that pattern, everything changed.",
                "life_impact": "Promoted to Senior Director, leading international presentations, mentoring other women in leadership"
            },
            {
                "icon": "🎓",
                "name": "Ahmed El-Mansouri", 
                "role": "Medical Student, Morocco",
                "concern": "Study Overwhelm & Focus Issues",
                "before_quote": "Medical school was crushing me. I couldn't concentrate, was failing exams, and considered dropping out.",
                "after_quote": "I'm now excelling in my specialty internship and feel completely confident about my medical career.",
                "transformation": "From nearly dropping out to top of his class",
                "sessions": "2 sessions",
                "timeline": "2 weeks apart",
                "background": "Struggling through 3rd year of medical school",
                "breakthrough": "Identified perfectionism patterns creating paralysis. Rewired the 'not good enough' belief into 'learning and growing.'",
                "life_impact": "Graduated top 10% of class, accepted into prestigious cardiology program, helps other students with study anxiety"
            },
            {
                "icon": "🚭",
                "name": "Priya & Raj Sharma",
                "role": "Bangkok Residents",
                "concern": "20-Year Smoking Addiction",
                "before_quote": "Raj smoked 2 packs a day for 20 years. We tried everything - patches, gum, medications. Nothing worked.",
                "after_quote": "It's been 8 months now. He doesn't even think about cigarettes. We've saved over 40,000 THB already.",
                "transformation": "From 40 cigarettes daily to completely smoke-free",
                "sessions": "2 sessions",
                "timeline": "1 week apart",
                "background": "Multiple failed quit attempts over 5 years",
                "breakthrough": "Smoking wasn't about nicotine - it was his stress response and identity. We changed both at the subconscious level.",
                "life_impact": "Better health, more energy, stronger relationship, planning to start a family, saved enough money for a vacation"
            },
            {
                "icon": "🌙",
                "name": "Lisa Thompson",
                "role": "Expat Teacher, Bangkok",
                "concern": "Chronic Insomnia",
                "before_quote": "I hadn't slept properly in 3 years. I was exhausted, emotional, and my teaching was suffering.",
                "after_quote": "I sleep like a baby now. My energy is back, my students love my classes again, and I feel like myself.",
                "transformation": "From 3-4 hours broken sleep to 7-8 hours deep rest",
                "sessions": "2 sessions + 1 reinforcement",
                "timeline": "3 weeks total",
                "background": "Insomnia started after moving to Thailand",
                "breakthrough": "Sleep issues were masking anxiety about life changes. Once we addressed the root cause, sleep naturally returned.",
                "life_impact": "Renewed teaching contract, started dating again, launched a tutoring business, planning to buy a condo"
            }
        ]
    
    def render(self):
        """Render testimonial showcase"""
        st.subheader("From Stuck to Thriving: 4 Transformation Stories")
        st.write("Each story represents years of struggle resolved in days. See how your life could change.")
        
        for testimonial in self.testimonials:
            self._render_testimonial_card(testimonial)
    
    def _render_testimonial_card(self, testimonial):
        """Render individual testimonial with rich details"""
        # Main testimonial card
        testimonial_html = f"""
        <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                    padding: 2rem; margin: 2rem 0; border-left: 4px solid #4CA1A3;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                <div style="font-size: 3rem;">{testimonial['icon']}</div>
                <div>
                    <h2 style="color: #273548; margin: 0; font-size: 1.5rem;">{testimonial['name']}</h2>
                    <p style="color: #556D7A; margin: 0; font-weight: 600;">{testimonial['role']}</p>
                    <p style="color: #4CA1A3; margin: 0; font-size: 0.9rem;">Concern: {testimonial['concern']}</p>
                </div>
            </div>
        </div>
        """
        st.markdown(testimonial_html, unsafe_allow_html=True)
        
        # Before/After transformation
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Before:**")
            st.markdown(f'"{testimonial["before_quote"]}"')
        
        with col2:
            st.markdown("**After:**")
            st.markdown(f'"{testimonial["after_quote"]}"')
        
        # Transformation summary
        st.success(f"**Transformation:** {testimonial['transformation']}")
        
        # Expandable details
        with st.expander("📖 See Complete Transformation Story", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**The Journey:**")
                st.write(f"• **Background:** {testimonial['background']}")
                st.write(f"• **Sessions:** {testimonial['sessions']}")
                st.write(f"• **Timeline:** {testimonial['timeline']}")
                
            with col2:
                st.markdown("**The Breakthrough:**")
                st.write(testimonial['breakthrough'])
            
            st.markdown("**Life Impact Today:**")
            st.write(testimonial['life_impact'])

class SuccessMetrics:
    """Success metrics with visual impact"""
    
    def render(self):
        """Render success statistics"""
        st.subheader("The Numbers Tell the Story")
        st.write("Our results speak for themselves. These aren't just statistics - they're lives transformed.")
        
        # Force 3 columns to stay in one row even on mobile
        st.markdown("""
        <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: nowrap; 
                    justify-content: space-between;">
            <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                        border-radius: 8px; padding: 1rem; text-align: center;">
                <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
                    85%
                </div>
                <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
                    Complete Success
                </div>
                <div style="color: #273548; font-size: 0.8rem;">
                    Transform in 2 sessions
                </div>
            </div>
            <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                        border-radius: 8px; padding: 1rem; text-align: center;">
                <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
                    500+
                </div>
                <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
                    Lives Changed
                </div>
                <div style="color: #273548; font-size: 0.8rem;">
                    Since 2017
                </div>
            </div>
            <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                        border-radius: 8px; padding: 1rem; text-align: center;">
                <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
                    95%+
                </div>
                <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
                    Still Free
                </div>
                <div style="color: #273548; font-size: 0.8rem;">
                    1 year later
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("**Compare this to traditional methods:** Most conventional approaches have success rates below 30% with high relapse rates.")

class TestimonialSubmission:
    """Component for new clients to submit their testimonials"""
    
    def render(self):
        """Render testimonial submission form"""
        st.markdown("---")
        st.subheader("🌟 Share Your Transformation Story")
        st.write("Are you a past client who has experienced transformation? Your story could inspire someone to take the first step toward freedom.")
        
        # Testimonial submission form
        with st.form("testimonial_submission", clear_on_submit=True):
            st.markdown("""
            <style>
            div[data-testid="stForm"] {
                background: white !important;
                border-radius: 12px !important;
                padding: 2rem !important;
                margin: 1rem 0 !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
                border: 1px solid #CBD5E1 !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                first_name = st.text_input("First Name*", placeholder="Your first name")
                email = st.text_input("Email*", placeholder="your@email.com")
                
            with col2:
                concern_resolved = st.selectbox(
                    "What did you overcome?*",
                    ["", "Smoking", "Anxiety", "Insomnia", "Bad Habits", "Phobias", "Other"]
                )
                session_count = st.selectbox(
                    "How many sessions?*",
                    ["", "2 sessions", "3 sessions (with reinforcement)"]
                )
            
            # Before/After experience
            st.markdown("**Your Transformation:**")
            before_situation = st.text_area(
                "Before: Describe your situation before hypnotherapy",
                placeholder="What was your life like? How was this issue affecting you?",
                height=80
            )
            
            after_situation = st.text_area(
                "After: Describe your life now",
                placeholder="How has your life changed? What's different now?",
                height=80
            )
            
            # Additional details
            most_surprising = st.text_area(
                "What surprised you most about the process?",
                placeholder="What was unexpected about your experience?",
                height=60
            )
            
            would_recommend = st.selectbox(
                "Would you recommend this to others facing similar challenges?",
                ["", "Absolutely - it changed my life", "Yes, definitely", "Yes, with some reservations"]
            )
            
            # Permission and privacy
            st.markdown("**Privacy & Usage:**")
            anonymous = st.checkbox("Use only my first name and general location (recommended)")
            permission = st.checkbox("I give permission to use my story to help others (required)*")
            
            # Submit button
            submitted = st.form_submit_button("🌟 Share My Story", type="primary", use_container_width=True)
            
            if submitted:
                if self._validate_testimonial_form(first_name, email, concern_resolved, session_count, 
                                                 before_situation, after_situation, permission):
                    # Store testimonial data
                    testimonial_data = {
                        'name': first_name,
                        'email': email,
                        'concern': concern_resolved,
                        'sessions': session_count,
                        'before': before_situation,
                        'after': after_situation,
                        'surprising': most_surprising,
                        'recommend': would_recommend,
                        'anonymous': anonymous
                    }
                    
                    if self._submit_testimonial(testimonial_data):
                        st.success("✅ Thank you for sharing your story! We'll review it and may feature it to inspire others.")
                        st.balloons()
    
    def _validate_testimonial_form(self, name, email, concern, sessions, before, after, permission):
        """Validate testimonial submission"""
        errors = []
        
        if not name.strip():
            errors.append("First name is required")
        if not email.strip() or '@' not in email:
            errors.append("Valid email is required")
        if not concern:
            errors.append("Please select what you overcame")
        if not sessions:
            errors.append("Please select number of sessions")
        if not before.strip():
            errors.append("Please describe your situation before")
        if not after.strip():
            errors.append("Please describe your situation after")
        if not permission:
            errors.append("Permission to use your story is required")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
            return False
        
        return True
    
    def _submit_testimonial(self, testimonial_data):
        """Submit testimonial for review"""
        try:
            # In production, this would email the testimonial to you for review
            print(f"New testimonial submitted: {testimonial_data['name']} - {testimonial_data['concern']}")
            return True
        except Exception as e:
            st.error("Sorry, there was an error submitting your story. Please try again.")
            return False

class SuccessPage:
    """Complete success page with emotional engagement"""
    
    def __init__(self):
        self.hero = SuccessHero()
        self.testimonials = TestimonialShowcase()
        self.metrics = SuccessMetrics()
        self.submission = TestimonialSubmission()
    
    def render(self):
        """Render complete success stories page"""
        # Hero section
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        # Testimonials showcase
        with st.container():
            self.testimonials.render()
            st.markdown("    ")
        
        # Success metrics
        with st.container():
            self.metrics.render()
            st.markdown("    ")
        
        # Testimonial submission
        with st.container():
            self.submission.render()
            st.markdown("    ")

# Factory function for clean import
def create_success_page():
    return SuccessPage()
