# """
# Success stories page component for the Hypnotherapy website
# Simplified, engaging version with emotional impact
# """
# import streamlit as st

# class SuccessHero:
#     """Hero section for success stories page using consistent styling"""
    
#     def render(self):
#         """Render success hero section"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                     border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#             <h1 style="color: white; text-shadow: none;">Real People. Real Results.</h1>
#         </div>
#         """, unsafe_allow_html=True)

#         st.write("See how clients broke free from patterns that controlled their lives for years. Your transformation could be next.")

# class TestimonialCards:
#     """Simple, powerful testimonial display"""
    
#     def __init__(self):
#         self.testimonials = [
#             {
#                 "icon": "🎓",
#                 "name": "Yasmina",
#                 "role": "Medicine Student, Morocco → Shanghai",
#                 "emotion": "From Fear to Authentic Drive", 
#                 "before": "Failing to cope with competitive Chinese university system, studying out of obligation",
#                 "after": "Found her own passion for medicine, excelling with genuine motivation and purpose",
#                 "breakthrough": "Discovered she was studying to honor her late mother, not herself",
#                 "sessions": "2 sessions"
#             },
#             {
#                 "icon": "🚭",
#                 "name": "Patrick",
#                 "role": "Executive, Shanghai → Paris",
#                 "emotion": "From Isolation to Connection",
#                 "before": "Pack-a-day smoker, lighting cigarettes in a row, heavy ashtray breath",
#                 "after": "Smoke-free for 10 months, deeper connection with his wife, genuine intimacy",
#                 "breakthrough": "Cigarettes were his excuse to escape - rewired to connect instead",
#                 "sessions": "2 sessions"
#             },
#             {
#                 "icon": "🌙",
#                 "name": "Betsy",
#                 "role": "A&E Doctor, England (15+ years)",
#                 "emotion": "From Fear to Trust",
#                 "before": "Sleepless nights for years, totally exhausted, chaotic sleep patterns",
#                 "after": "Sleeping peacefully 7-8 hours, renewed energy for patients and family",
#                 "breakthrough": "Learned to trust herself enough to let go and rest deeply",
#                 "sessions": "2 sessions + reinforcement"
#             }
#         ]
    
#     def render(self):
#         """Render testimonial cards"""
#         st.subheader("3 Lives Transformed Through Emotional Breakthroughs")
#         st.write("Each transformation began with identifying the deeper emotional pattern driving the surface behavior.")
        
#         for testimonial in self.testimonials:
#             self._render_card(testimonial)
    
#     def _render_card(self, testimonial):
#         """Render individual testimonial card using Streamlit components"""
#         # Use a clean container approach
#         with st.container():
#             # Create card styling using CSS class that matches your system
#             st.markdown("""
#             <style>
#             .testimonial-card {
#                 background: var(--card-bg);
#                 border: 1px solid var(--border);
#                 border-radius: var(--radius-md);
#                 padding: var(--space-lg);
#                 margin: var(--space-lg) 0;
#                 border-left: 4px solid var(--accent);
#             }
#             </style>
#             """, unsafe_allow_html=True)
            
#             # Header with icon and name using columns
#             col_icon, col_info = st.columns([1, 5])
            
#             with col_icon:
#                 st.markdown(f"<div style='font-size: 2.5rem; text-align: center;'>{testimonial['icon']}</div>", 
#                            unsafe_allow_html=True)
            
#             with col_info:
#                 st.subheader(testimonial['name'])
#                 st.caption(testimonial['role'])
#                 st.markdown(f"*{testimonial['emotion']}*")
            
#             # Before/After using columns
#             col_before, col_after = st.columns(2)
            
#             with col_before:
#                 st.markdown("**Before:**")
#                 st.write(testimonial['before'])
            
#             with col_after:
#                 st.markdown("**After:**")  
#                 st.write(testimonial['after'])
            
#             # Breakthrough insight using info box
#             st.info(f"💡 **Breakthrough:** {testimonial['breakthrough']}")
            
#             # Sessions count
#             st.markdown(f"""
#             <div style="text-align: center; color: var(--accent); font-weight: 600; margin-top: var(--space-sm);">
#                 ✨ {testimonial['sessions']} ✨
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Add spacing after each testimonial
#             st.markdown("<br>", unsafe_allow_html=True)

# class QuickStats:
#     """Simple success metrics using Streamlit components"""
    
#     def render(self):
#         """Render success statistics"""
#         st.subheader("The Results Speak for Themselves")
        
#         # Use Streamlit columns for metrics
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.metric("Complete Success", "85%", "in 2 sessions")
        
#         with col2:
#             st.metric("Lives Changed", "500+", "since 2017")
        
#         with col3:
#             st.metric("Still Free", "95%", "1 year later")

# class ShareYourStory:
#     """Simple testimonial submission"""
    
#     def render(self):
#         """Render story sharing section"""
#         st.markdown("---")
#         st.subheader("🌟 Share Your Success Story")
#         st.write("Transformed by our sessions? Your story could inspire someone to take the first step.")
        
#         with st.form("share_story"):
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 name = st.text_input("First Name*")
#                 concern = st.selectbox("What did you overcome?*", 
#                     ["", "Smoking", "Anxiety", "Sleep Issues", "Bad Habits", "Other"])
            
#             with col2:
#                 email = st.text_input("Email*")
#                 sessions = st.selectbox("Sessions needed?*", 
#                     ["", "2 sessions", "3 sessions"])
            
#             before = st.text_area("Before: Your situation before hypnotherapy*", height=80)
#             after = st.text_area("After: How your life changed*", height=80)
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 anonymous = st.checkbox("Use only first name (recommended)")
#             with col2:
#                 permission = st.checkbox("Permission to share my story*")
            
#             if st.form_submit_button("Share My Story 🌟", type="primary"):
#                 if name and email and concern and sessions and before and after and permission:
#                     st.success("✅ Thank you! We'll review your story and may feature it to inspire others.")
#                     st.balloons()
#                 else:
#                     st.error("Please fill in all required fields marked with *")

# class SuccessPage:
#     """Complete success page - simplified and engaging"""
    
#     def __init__(self):
#         self.hero = SuccessHero()
#         self.testimonials = TestimonialCards()
#         self.stats = QuickStats()
#         self.share = ShareYourStory()
    
#     def render(self):
#         """Render complete success stories page"""
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.testimonials.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.stats.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.share.render()
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
                "role": "Yasmina : Medicine Student, Morocco → Shanghai",
                "emotion": "From trauma to inner drive", 
                "before": "Failing to cope with competitive Chinese university system, studying out of obligation",
                "after": "Found her own passion for medicine, excelling with genuine motivation and purpose",
                "breakthrough": "Discovered she was studying to honor her late mother, not herself",
                "sessions": "6 sessions"
            },
            {
                "icon": "🚭",
                "role": "Patrick : Executive, Shanghai → Paris",
                "emotion": "From smoker to healthier",
                "before": "Pack-a-day smoker, lighting cigarettes in a row, heavy ashtray breath",
                "after": "Smoke-free for 10 months, deeper connection with his wife, genuine intimacy",
                "breakthrough": "Cigarettes were his excuse to escape - rewired to walk instead",
                "sessions": "2 sessions"
            },
            {
                "icon": "🌙",
                "role": "Betty : A&E Doctor, England (15+ years)",
                "emotion": "From fear to trust",
                "before": "Sleepless nights for years, totally exhausted, chaotic sleep patterns",
                "after": "Sleeping peacefully 7-8 hours, renewed energy for patients and family",
                "breakthrough": "Learned to trust herself enough to let go and rest deeply",
                "sessions": "2 sessions + reinforcement"
            }
        ]
    
    def render(self):
        """Render testimonial cards"""
        st.subheader("Lives transformed through emotional breakthroughs / Hypnotherapy")
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
            # Hero header with old session div style - FIXED SYNTAX ERROR
            st.markdown(f"""
            <div style="text-align: center; color: {visual['color']}; font-weight: 600; margin-top: 1rem;">
                <h2 style="color: #273548; margin: 0; font-size: 1.8rem;">
                    {testimonial['icon']}{testimonial['emotion']}
                </h2>
                <p style="color: #556D7A; margin: 0.5rem 0 0 0; font-weight: 600;">
                    {testimonial['role']}
                </p>
            </div>
            """, unsafe_allow_html=True)
                            
            # Before/After using st.info with bold text
            col_before, col_after = st.columns(2, gap="small")
            
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
        st.subheader("🌟 Share your success story")
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
