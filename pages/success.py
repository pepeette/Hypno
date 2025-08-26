# """
# Success stories page component for the Hypnotherapy website
# Features client testimonials with emotional connection and engagement
# Consistent with the existing architecture and styling
# """
# import streamlit as st

# class SuccessHero:
#     """Hero section for success stories page"""
    
#     def render(self):
#         """Render success hero section"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                     border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#             <h1 style="color: white;">Real People. Real Transformations. Real Results.</h1>
#         </div>
#         """, unsafe_allow_html=True)

#         st.write("See how clients broke free from patterns that controlled their lives for years. In just 2 sessions, they discovered the freedom they thought was impossible.")

# class TestimonialShowcase:
#     """Enhanced testimonial display with emotional impact"""
    
#     def __init__(self):
#         self.testimonials = [
#             {
#                 "icon": "🌟",
#                 "name": "Sarah Chen",
#                 "role": "Banking Director, Singapore",
#                 "concern": "Performance Anxiety",
#                 "before_quote": "I was terrified of presentations. My heart would race, palms would sweat, and I'd avoid important meetings.",
#                 "after_quote": "Now I actually look forward to presenting. I got promoted within 3 months of our sessions.",
#                 "transformation": "From avoiding meetings to leading them confidently",
#                 "sessions": "2 sessions",
#                 "timeline": "10 days apart",
#                 "background": "15 years of career-limiting anxiety",
#                 "breakthrough": "Discovered the anxiety stemmed from a childhood experience of being laughed at in class. Once we rewired that pattern, everything changed.",
#                 "life_impact": "Promoted to Senior Director, leading international presentations, mentoring other women in leadership"
#             },
#             {
#                 "icon": "🎓",
#                 "name": "Ahmed El-Mansouri", 
#                 "role": "Medical Student, Morocco",
#                 "concern": "Study Overwhelm & Focus Issues",
#                 "before_quote": "Medical school was crushing me. I couldn't concentrate, was failing exams, and considered dropping out.",
#                 "after_quote": "I'm now excelling in my specialty internship and feel completely confident about my medical career.",
#                 "transformation": "From nearly dropping out to top of his class",
#                 "sessions": "2 sessions",
#                 "timeline": "2 weeks apart",
#                 "background": "Struggling through 3rd year of medical school",
#                 "breakthrough": "Identified perfectionism patterns creating paralysis. Rewired the 'not good enough' belief into 'learning and growing.'",
#                 "life_impact": "Graduated top 10% of class, accepted into prestigious cardiology program, helps other students with study anxiety"
#             },
#             {
#                 "icon": "🚭",
#                 "name": "Priya & Raj Sharma",
#                 "role": "Bangkok Residents",
#                 "concern": "20-Year Smoking Addiction",
#                 "before_quote": "Raj smoked 2 packs a day for 20 years. We tried everything - patches, gum, medications. Nothing worked.",
#                 "after_quote": "It's been 8 months now. He doesn't even think about cigarettes. We've saved over 40,000 THB already.",
#                 "transformation": "From 40 cigarettes daily to completely smoke-free",
#                 "sessions": "2 sessions",
#                 "timeline": "1 week apart",
#                 "background": "Multiple failed quit attempts over 5 years",
#                 "breakthrough": "Smoking wasn't about nicotine - it was his stress response and identity. We changed both at the subconscious level.",
#                 "life_impact": "Better health, more energy, stronger relationship, planning to start a family, saved enough money for a vacation"
#             },
#             {
#                 "icon": "🌙",
#                 "name": "Lisa Thompson",
#                 "role": "Expat Teacher, Bangkok",
#                 "concern": "Chronic Insomnia",
#                 "before_quote": "I hadn't slept properly in 3 years. I was exhausted, emotional, and my teaching was suffering.",
#                 "after_quote": "I sleep like a baby now. My energy is back, my students love my classes again, and I feel like myself.",
#                 "transformation": "From 3-4 hours broken sleep to 7-8 hours deep rest",
#                 "sessions": "2 sessions + 1 reinforcement",
#                 "timeline": "3 weeks total",
#                 "background": "Insomnia started after moving to Thailand",
#                 "breakthrough": "Sleep issues were masking anxiety about life changes. Once we addressed the root cause, sleep naturally returned.",
#                 "life_impact": "Renewed teaching contract, started dating again, launched a tutoring business, planning to buy a condo"
#             }
#         ]
    
#     def render(self):
#         """Render testimonial showcase"""
#         st.subheader("From Stuck to Thriving: 4 Transformation Stories")
#         st.write("Each story represents years of struggle resolved in days. See how your life could change.")
        
#         for testimonial in self.testimonials:
#             self._render_testimonial_card(testimonial)
    
#     def _render_testimonial_card(self, testimonial):
#         """Render individual testimonial with rich details"""
#         # Main testimonial card
#         testimonial_html = f"""
#         <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                     padding: 2rem; margin: 2rem 0; border-left: 4px solid #4CA1A3;">
#             <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
#                 <div style="font-size: 3rem;">{testimonial['icon']}</div>
#                 <div>
#                     <h2 style="color: #273548; margin: 0; font-size: 1.5rem;">{testimonial['name']}</h2>
#                     <p style="color: #556D7A; margin: 0; font-weight: 600;">{testimonial['role']}</p>
#                     <p style="color: #4CA1A3; margin: 0; font-size: 0.9rem;">Concern: {testimonial['concern']}</p>
#                 </div>
#             </div>
#         </div>
#         """
#         st.markdown(testimonial_html, unsafe_allow_html=True)
        
#         # Before/After transformation
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("**Before:**")
#             st.markdown(f'"{testimonial["before_quote"]}"')
        
#         with col2:
#             st.markdown("**After:**")
#             st.markdown(f'"{testimonial["after_quote"]}"')
        
#         # Transformation summary
#         st.success(f"**Transformation:** {testimonial['transformation']}")
        
#         # Expandable details
#         with st.expander("📖 See Complete Transformation Story", expanded=False):
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.markdown("**The Journey:**")
#                 st.write(f"• **Background:** {testimonial['background']}")
#                 st.write(f"• **Sessions:** {testimonial['sessions']}")
#                 st.write(f"• **Timeline:** {testimonial['timeline']}")
                
#             with col2:
#                 st.markdown("**The Breakthrough:**")
#                 st.write(testimonial['breakthrough'])
            
#             st.markdown("**Life Impact Today:**")
#             st.write(testimonial['life_impact'])

# class SuccessMetrics:
#     """Success metrics with visual impact"""
    
#     def render(self):
#         """Render success statistics"""
#         st.subheader("The Numbers Tell the Story")
#         st.write("Our results speak for themselves. These aren't just statistics - they're lives transformed.")
        
#         # Force 3 columns to stay in one row even on mobile
#         st.markdown("""
#         <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: nowrap; 
#                     justify-content: space-between;">
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 8px; padding: 1rem; text-align: center;">
#                 <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
#                     85%
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Complete Success
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     Transform in 2 sessions
#                 </div>
#             </div>
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 8px; padding: 1rem; text-align: center;">
#                 <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
#                     500+
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Lives Changed
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     Since 2017
#                 </div>
#             </div>
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 8px; padding: 1rem; text-align: center;">
#                 <div style="color: #4CA1A3; font-size: 1.8rem; font-weight: 700; line-height: 1.2;">
#                     95%+
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Still Free
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     1 year later
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.success("**Compare this to traditional methods:** Most conventional approaches have success rates below 30% with high relapse rates.")

# class TestimonialSubmission:
#     """Component for new clients to submit their testimonials"""
    
#     def render(self):
#         """Render testimonial submission form"""
#         st.markdown("---")
#         st.subheader("🌟 Share Your Transformation Story")
#         st.write("Are you a past client who has experienced transformation? Your story could inspire someone to take the first step toward freedom.")
        
#         # Testimonial submission form
#         with st.form("testimonial_submission", clear_on_submit=True):
#             st.markdown("""
#             <style>
#             div[data-testid="stForm"] {
#                 background: white !important;
#                 border-radius: 12px !important;
#                 padding: 2rem !important;
#                 margin: 1rem 0 !important;
#                 box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
#                 border: 1px solid #CBD5E1 !important;
#             }
#             </style>
#             """, unsafe_allow_html=True)
            
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 first_name = st.text_input("First Name*", placeholder="Your first name")
#                 email = st.text_input("Email*", placeholder="your@email.com")
                
#             with col2:
#                 concern_resolved = st.selectbox(
#                     "What did you overcome?*",
#                     ["", "Smoking", "Anxiety", "Insomnia", "Bad Habits", "Phobias", "Other"]
#                 )
#                 session_count = st.selectbox(
#                     "How many sessions?*",
#                     ["", "2 sessions", "3 sessions (with reinforcement)"]
#                 )
            
#             # Before/After experience
#             st.markdown("**Your Transformation:**")
#             before_situation = st.text_area(
#                 "Before: Describe your situation before hypnotherapy",
#                 placeholder="What was your life like? How was this issue affecting you?",
#                 height=80
#             )
            
#             after_situation = st.text_area(
#                 "After: Describe your life now",
#                 placeholder="How has your life changed? What's different now?",
#                 height=80
#             )
            
#             # Additional details
#             most_surprising = st.text_area(
#                 "What surprised you most about the process?",
#                 placeholder="What was unexpected about your experience?",
#                 height=60
#             )
            
#             would_recommend = st.selectbox(
#                 "Would you recommend this to others facing similar challenges?",
#                 ["", "Absolutely - it changed my life", "Yes, definitely", "Yes, with some reservations"]
#             )
            
#             # Permission and privacy
#             st.markdown("**Privacy & Usage:**")
#             anonymous = st.checkbox("Use only my first name and general location (recommended)")
#             permission = st.checkbox("I give permission to use my story to help others (required)*")
            
#             # Submit button
#             submitted = st.form_submit_button("🌟 Share My Story", type="primary", use_container_width=True)
            
#             if submitted:
#                 if self._validate_testimonial_form(first_name, email, concern_resolved, session_count, 
#                                                  before_situation, after_situation, permission):
#                     # Store testimonial data
#                     testimonial_data = {
#                         'name': first_name,
#                         'email': email,
#                         'concern': concern_resolved,
#                         'sessions': session_count,
#                         'before': before_situation,
#                         'after': after_situation,
#                         'surprising': most_surprising,
#                         'recommend': would_recommend,
#                         'anonymous': anonymous
#                     }
                    
#                     if self._submit_testimonial(testimonial_data):
#                         st.success("✅ Thank you for sharing your story! We'll review it and may feature it to inspire others.")
#                         st.balloons()
    
#     def _validate_testimonial_form(self, name, email, concern, sessions, before, after, permission):
#         """Validate testimonial submission"""
#         errors = []
        
#         if not name.strip():
#             errors.append("First name is required")
#         if not email.strip() or '@' not in email:
#             errors.append("Valid email is required")
#         if not concern:
#             errors.append("Please select what you overcame")
#         if not sessions:
#             errors.append("Please select number of sessions")
#         if not before.strip():
#             errors.append("Please describe your situation before")
#         if not after.strip():
#             errors.append("Please describe your situation after")
#         if not permission:
#             errors.append("Permission to use your story is required")
        
#         if errors:
#             for error in errors:
#                 st.error(f"❌ {error}")
#             return False
        
#         return True
    
#     def _submit_testimonial(self, testimonial_data):
#         """Submit testimonial for review"""
#         try:
#             # In production, this would email the testimonial to you for review
#             print(f"New testimonial submitted: {testimonial_data['name']} - {testimonial_data['concern']}")
#             return True
#         except Exception as e:
#             st.error("Sorry, there was an error submitting your story. Please try again.")
#             return False

# class SuccessPage:
#     """Complete success page with emotional engagement"""
    
#     def __init__(self):
#         self.hero = SuccessHero()
#         self.testimonials = TestimonialShowcase()
#         self.metrics = SuccessMetrics()
#         self.submission = TestimonialSubmission()
    
#     def render(self):
#         """Render complete success stories page"""
#         # Hero section
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
        
#         # Testimonials showcase
#         with st.container():
#             self.testimonials.render()
#             st.markdown("    ")
        
#         # Success metrics
#         with st.container():
#             self.metrics.render()
#             st.markdown("    ")
        
#         # Testimonial submission
#         with st.container():
#             self.submission.render()
#             st.markdown("    ")

# # Factory function for clean import
# def create_success_page():
#     return SuccessPage()

"""
Success stories page component for the Hypnotherapy website
Simplified, engaging version with emotional impact
"""
import streamlit as st

class SuccessHero:
    """Hero section for success stories page using consistent styling"""
    
    def render(self):
        """Render success hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white; text-shadow: none;">Real People. Real Results.</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("See how clients broke free from patterns that controlled their lives for years. Your transformation could be next.")

class TestimonialCards:
    """Simple, powerful testimonial display"""
    
    def __init__(self):
        self.testimonials = [
            {
                "icon": "🎓",
                "name": "Yasmina",
                "role": "Medicine Student, Morocco → Shanghai",
                "emotion": "From Fear to Authentic Drive", 
                "before": "Failing to cope with competitive Chinese university system, studying out of obligation",
                "after": "Found her own passion for medicine, excelling with genuine motivation and purpose",
                "breakthrough": "Discovered she was studying to honor her late mother, not herself",
                "sessions": "2 sessions"
            },
            {
                "icon": "🚭",
                "name": "Patrick",
                "role": "Executive, Shanghai → Paris",
                "emotion": "From Isolation to Connection",
                "before": "Pack-a-day smoker, lighting cigarettes in a row, heavy ashtray breath",
                "after": "Smoke-free for 10 months, deeper connection with his wife, genuine intimacy",
                "breakthrough": "Cigarettes were his excuse to escape - rewired to connect instead",
                "sessions": "2 sessions"
            },
            {
                "icon": "🌙",
                "name": "Betsy",
                "role": "A&E Doctor, England (15+ years)",
                "emotion": "From Fear to Trust",
                "before": "Sleepless nights for years, totally exhausted, chaotic sleep patterns",
                "after": "Sleeping peacefully 7-8 hours, renewed energy for patients and family",
                "breakthrough": "Learned to trust herself enough to let go and rest deeply",
                "sessions": "2 sessions + reinforcement"
            }
        ]
    
    def render(self):
        """Render testimonial cards"""
        st.subheader("3 Lives Transformed Through Emotional Breakthroughs")
        st.write("Each transformation began with identifying the deeper emotional pattern driving the surface behavior.")
        
        for testimonial in self.testimonials:
            self._render_card(testimonial)
    
    def _render_card(self, testimonial):
        """Render individual testimonial card with enhanced visual appeal"""
        
        # Map emotions to color themes (no external images for reliability)
        emotion_visuals = {
            "From Fear to Authentic Drive": {
                "color": "#22c55e",
                "gradient": "linear-gradient(135deg, #22c55e 0%, #16a34a 100%)"
            },
            "From Isolation to Connection": {
                "color": "#3b82f6", 
                "gradient": "linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)"
            },
            "From Fear to Trust": {
                "color": "#8b5cf6",
                "gradient": "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)"
            }
        }
        
        visual = emotion_visuals.get(testimonial['emotion'], emotion_visuals["From Fear to Trust"])
        
        with st.container():
            # Hero header with old session div style
            st.markdown(f"""
            <div style="text-align: center; color: {visual['color']; font-weight: 600; margin-top: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">{testimonial['icon']}</div>
                <h2 style="color: #273548; margin: 0; font-size: 1.8rem;">
                    {testimonial['emotion']}
                </h2>
                <p style="color: #556D7A; margin: 0.5rem 0 0 0; font-weight: 600;">
                    {testimonial['role']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Client name without background - simple text
            st.markdown(f"""
            <div style="text-align: center; margin: 1rem 0;">
                <span style="color: #273548; font-weight: 600; font-size: 1rem;">
                    {testimonial['name']}
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # Before/After using st.info with bold text
            col_before, col_after = st.columns(2, gap="large")
            
            with col_before:
                st.info(f"**😔 Before:** {testimonial['before']}")
            
            with col_after:
                st.info(f"**🌟 After:** {testimonial['after']}")
            
            # Breakthrough insight using Streamlit info
            st.info(f"💡 **Key Breakthrough:** {testimonial['breakthrough']}")
            
            # Sessions count without background - simple styling like old session div
            st.markdown(f"""
            <div style="text-align: center; color: #4CA1A3; font-weight: 600; margin-top: 1rem;">
                ✨ {testimonial['sessions']} ✨
            </div>
            """, unsafe_allow_html=True)
            
            # Add spacing between cards
            st.markdown("---")

class QuickStats:
    """Why hypnotherapy succeeds - explanation and metrics"""
    
    def render(self):
        """Render success explanation and statistics"""
        st.subheader("Why Hypnotherapy succeeds where others haven't")
        
        # Opening explanation using Streamlit info box
        st.info("""
        Every unwanted behavior is driven by subconscious patterns you learned years ago. 
        Traditional therapy tries to override these patterns with willpower. We change the patterns themselves.
        When your subconscious programming supports your goals instead of fighting them, 
        change becomes effortless and permanent.
        """)
        
        # Success rate using custom metrics with combined value/delta
        with st.container():
            # Force 3 columns to stay in one row even on mobile
            st.markdown("""
            <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: nowrap; 
                        justify-content: space-between;">
                <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                            border-radius: 8px; padding: 1rem; text-align: center;">
                    <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                        Success Rate
                    </div>
                    <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
                        85% in 2 sessions
                    </div>
                </div>
                <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                            border-radius: 8px; padding: 1rem; text-align: center;">
                    <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                        3rd Session Optional
                    </div>
                    <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
                        15% need Reinforcement
                    </div>
                </div>
                <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
                            border-radius: 8px; padding: 1rem; text-align: center;">
                    <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
                        Rapid pattern rewiring
                    </div>
                    <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
                        for Lasting change
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("Most clients achieve complete transformation in two 90-minute sessions. About 15% choose an optional reinforcement session a few weeks later for additional confidence.")

class ShareYourStory:
    """Simple testimonial submission"""
    
    def render(self):
        """Render story sharing section"""
        st.markdown("---")
        st.subheader("🌟 Share Your Success Story")
        st.write("Transformed by our sessions? Your story could inspire someone to take the first step.")
        
        with st.form("share_story"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("First Name*")
                concern = st.selectbox("What did you overcome?*", 
                    ["", "Smoking", "Anxiety", "Sleep Issues", "Bad Habits", "Other"])
            
            with col2:
                email = st.text_input("Email*")
                sessions = st.selectbox("Sessions needed?*", 
                    ["", "2 sessions", "3 sessions"])
            
            before = st.text_area("Before: Your situation before hypnotherapy*", height=80)
            after = st.text_area("After: How your life changed*", height=80)
            
            col1, col2 = st.columns(2)
            with col1:
                anonymous = st.checkbox("Use only first name (recommended)")
            with col2:
                permission = st.checkbox("Permission to share my story*")
            
            if st.form_submit_button("Share My Story 🌟", type="primary"):
                if name and email and concern and sessions and before and after and permission:
                    st.success("✅ Thank you! We'll review your story and may feature it to inspire others.")
                    st.balloons()
                else:
                    st.error("Please fill in all required fields marked with *")

class SuccessPage:
    """Complete success page - simplified and engaging"""
    
    def __init__(self):
        self.hero = SuccessHero()
        self.testimonials = TestimonialCards()
        self.stats = QuickStats()
        self.share = ShareYourStory()
    
    def render(self):
        """Render complete success stories page"""
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        with st.container():
            self.testimonials.render()
            st.markdown("    ")
        
        with st.container():
            self.stats.render()
            st.markdown("    ")
        
        with st.container():
            self.share.render()
            st.markdown("    ")

# Factory function for clean import
def create_success_page():
    return SuccessPage()
