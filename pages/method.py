# """
# Method Page - The Science Behind 2-Session Transformation
# Detailed explanation using Streamlit components with consistent styling
# """
# import streamlit as st

# class MethodHero:
#     """Hero section for method page using consistent styling"""
    
#     def render(self):
#         """Render method hero section"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                     border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#             <h1 style="color: white;">The Science Behind Rapid Transformation</h1>
#             <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
#                 Discover why our 2-session method succeeds where traditional approaches fail. <br>
#                 It's not willpower. It's neuroscience.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# class WhyItWorks:
#     """Core science explanation section"""
    
#     def render(self):
#         """Render the core science behind the method"""
#         st.subheader("Why Traditional Methods Keep Failing You")
        
#         # Key insight with visual emphasis
#         st.markdown("""
#         <div style="display: flex; gap: 1rem; margin: 2rem 0; align-items: stretch; flex-wrap: nowrap;">
#             <div style="flex: 0 0 auto; display: flex; align-items: center; justify-content: center; min-width: 120px;">
#                 <img src="https://github.com/pepeette/Hypno/blob/main/img/brain_conscious.jpg?raw=true" 
#                      alt="Conscious vs Subconscious Brain" 
#                      style="max-width: 100%; height: auto; border-radius: 8px; 
#                             max-height: 100px; object-fit: contain;">
#             </div>
#             <div style="flex: 1; display: flex; align-items: center;">
#                 <div style="background: rgba(76, 161, 163, 0.1); border: 1px solid #4CA1A3; 
#                             border-radius: 8px; padding: 1rem; width: 100%;">
#                     <p style="margin: 0; color: #273548; font-size: 1rem; line-height: 1.6;">
#                         🧠 <strong>The Problem:</strong> Your conscious mind (5% of decisions) fights your subconscious programming (95% of decisions). 
#                         Guess who wins? The subconscious. Every time.
#                     </p>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # The breakthrough approach
#         st.info("""
#         **Our Breakthrough:** Instead of fighting your subconscious, we work directly with it. 
#         We identify your specific patterns and rewire them at the source. When your subconscious 
#         supports your goals instead of sabotaging them, change becomes effortless.
#         """)

# class TwoSessionBreakdown:
#     """Detailed breakdown of the 2-session process"""
    
#     def render(self):
#         """Render the session-by-session breakdown"""
#         st.subheader("The Proven 2-Session Process")
#         st.write("Each session has a specific purpose in your transformation journey:")
        
#         # Session 1
#         self._render_session_card(
#             session_num=1,
#             title="Analysis & Pattern Mapping",
#             duration="90 minutes",
#             icon="🔍",
#             description="We dive deep to understand exactly what drives your unwanted behavior",
#             what_happens=[
#                 "Comprehensive behavioral analysis using proven psychological frameworks",
#                 "Identify your unique subconscious triggers and response patterns", 
#                 "Map the emotional and environmental factors that activate old behaviors",
#                 "Discover the positive intent behind negative patterns (every behavior serves a purpose)",
#                 "Begin initial positive programming to start shifting your mindset"
#             ],
#             outcome="You'll understand WHY you do what you do, often for the first time. Many clients feel immediate relief just from this clarity.",
#             image_url="https://github.com/pepeette/Hypno/blob/main/img/session1_analysis.jpg?raw=true"
#         )
        
#         # Session 2  
#         self._render_session_card(
#             session_num=2,
#             title="Subconscious Rewiring",
#             duration="90 minutes", 
#             icon="⚡",
#             description="We reprogram your subconscious mind for automatic positive choices",
#             what_happens=[
#                 "Enter deep hypnotic state for maximum subconscious receptivity",
#                 "Install new neural pathways that support your desired behaviors",
#                 "Replace limiting beliefs with empowering ones at the identity level",
#                 "Create new automatic responses to old triggers",
#                 "Anchor your new patterns with powerful positive emotional associations"
#             ],
#             outcome="The old urges simply disappear. You naturally make choices aligned with your goals without effort or internal struggle.",
#             image_url="https://github.com/pepeette/Hypno/blob/main/img/session2_hypnosis.jpg?raw=true"
#         )
        
#         # Optional Session 3
#         self._render_optional_session()
    
#     def _render_session_card(self, session_num, title, duration, icon, description, what_happens, outcome, image_url):
#         """Render individual session card"""
#         st.markdown(f"""
#         <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                     padding: 2rem; margin: 2rem 0; border-left: 4px solid #4CA1A3;">
#             <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
#                 <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
#                             border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                             font-weight: bold; font-size: 1.5rem;">{session_num}</div>
#                 <div>
#                     <h2 style="color: #273548; margin: 0;">{icon} Session {session_num}: {title}</h2>
#                     <p style="color: #556D7A; margin: 0; font-weight: 600;">{duration} • {description}</p>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             st.markdown("**What happens during this session:**")
#             for item in what_happens:
#                 st.write(f"• {item}")
                
#             st.success(f"**Outcome:** {outcome}")
        
#         with col2:
#             if image_url:
#                 st.markdown(f"""
#                 <img src="{image_url}" 
#                      alt="Session {session_num}" 
#                      style="width: 100%; border-radius: 8px; border: 1px solid #CBD5E1;">
#                 """, unsafe_allow_html=True)
    
#     def _render_optional_session(self):
#         """Render optional 3rd session information"""
#         st.markdown("""
#         <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                     padding: 2rem; margin: 2rem 0; border-left: 4px solid #eab308; opacity: 0.9;">
#             <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
#                 <div style="background: #eab308; color: white; width: 50px; height: 50px; 
#                             border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                             font-weight: bold; font-size: 1.2rem;">+1</div>
#                 <div>
#                     <h2 style="color: #273548; margin: 0;">🎯 Session 3: Reinforcement (Optional)</h2>
#                     <p style="color: #556D7A; margin: 0; font-weight: 600;">60 minutes • Only needed by 15% of clients</p>
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("**When this session helps:**")
#             st.write("• Strengthen any remaining weak spots in your new patterns")
#             st.write("• Address unexpected triggers that emerge in real-world situations")
#             st.write("• Fine-tune your responses for complete confidence")
#             st.write("• Provide additional tools for long-term maintenance")
        
#         with col2:
#             st.info("""
#             **Our Guarantee**
            
#             If you're not completely satisfied after 2 sessions, 
#             your 3rd reinforcement session is complimentary.
            
#             We're that confident in our method.
#             """)

# class SuccessMetrics:
#     """Success rates and statistics"""
    
#     def render(self):
#         """Render success metrics with visual impact"""
#         st.subheader("Proven Results Across Thousands of Sessions")
        
#         # Force 3 columns to stay in one row
#         st.markdown("""
#         <div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: nowrap; 
#                     justify-content: space-between;">
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #22c55e;">
#                 <div style="color: #22c55e; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
#                     85%
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Complete Success
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     Achieve all goals in 2 sessions
#                 </div>
#             </div>
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #eab308;">
#                 <div style="color: #eab308; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
#                     15%
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Need Reinforcement
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     Benefit from optional 3rd session
#                 </div>
#             </div>
#             <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                         border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #4CA1A3;">
#                 <div style="color: #4CA1A3; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
#                     95%+
#                 </div>
#                 <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
#                     Long-term Success
#                 </div>
#                 <div style="color: #273548; font-size: 0.8rem;">
#                     Still transformed 1 year later
#                 </div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.success("**Compare this to traditional methods:** Most conventional approaches have success rates below 30%, require ongoing sessions, and have high relapse rates.")

# class CaseStudyShowcase:
#     """Real client transformation stories"""
    
#     def render(self):
#         """Render compelling case studies"""
#         st.subheader("Real Transformations: Before & After")
        
#         # Case Study 1
#         self._render_case_study(
#             title="Sarah's Smoking Freedom",
#             before="2 packs daily for 15 years. Tried patches, gum, cold turkey - always relapsed within weeks.",
#             process="Session 1 revealed smoking was her stress response learned in college. Session 2 installed new stress management patterns.",
#             after="Hasn't smoked in 8 months. No cravings. Saved ฿24,000. Runs 5K regularly.",
#             icon="🚭",
#             timeline="2 sessions over 10 days"
#         )
        
#         # Case Study 2  
#         self._render_case_study(
#             title="Michael's Anxiety Breakthrough", 
#             before="Panic attacks before presentations. Avoiding career opportunities. Taking anxiety medication.",
#             process="Session 1 uncovered perfectionist patterns from childhood. Session 2 rewired confidence and self-acceptance.",
#             after="Gave presentation to 200 people last month. Promoted to senior manager. Medication-free.",
#             icon="😌",
#             timeline="2 sessions over 1 week"
#         )
    
#     def _render_case_study(self, title, before, process, after, icon, timeline):
#         """Render individual case study"""
#         st.markdown(f"""
#         <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                     padding: 2rem; margin: 2rem 0;">
#             <h2 style="color: #4CA1A3; margin-bottom: 1rem;">{icon} {title}</h2>
#             <div style="font-size: 0.9rem; color: #556D7A; margin-bottom: 1rem; font-weight: 600;">
#                 {timeline}
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.markdown("**Before:**")
#             st.write(before)
        
#         with col2:
#             st.markdown("**Process:**") 
#             st.write(process)
        
#         with col3:
#             st.markdown("**After:**")
#             st.write(after)

# class InvestmentSection:
#     """Pricing and value proposition"""
    
#     def render(self):
#         """Render investment options"""
#         st.subheader("Invest in Your Transformation")
#         st.write("One-time investment. Lifetime results. Compare to years of traditional therapy:")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Complete Package</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿3,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem;">Sessions 1 & 2 • Most Popular</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("**Includes:**")
#             st.write("✓ Analysis Session (90 minutes)")
#             st.write("✓ Transformation Session (90 minutes)")
#             st.write("✓ Email support between sessions")
#             st.write("✓ 85% success rate")
            
#             if st.button("📞 Book Complete Package", type="primary", use_container_width=True):
#                 st.success("Excellent choice! Scroll down to book your discovery call.")
        
#         with col2:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <h2 style="color: #273548; margin-bottom: 1rem;">Premium Package</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿4,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem;">All 3 sessions • Peace of Mind</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("**Includes:**")
#             st.write("✓ Everything in Complete Package")
#             st.write("✓ Plus: 3rd reinforcement session")
#             st.write("✓ 100% satisfaction guarantee")
#             st.write("✓ Maximum confidence")
            
#             if st.button("⭐ Book Premium Package", use_container_width=True):
#                 st.success("Smart choice! Scroll down to book your discovery call.")
        
#         # Value comparison
#         st.info("""
#         💡 **Value Comparison:** Traditional therapy often costs ฿60,000+ over months or years. 
#         The ongoing cost of your unwanted habit (smoking, stress eating, etc.) often exceeds our entire package price within months.
#         """)

# class FinalCTA:
#     """Call to action section"""
    
#     def render(self):
#         """Render compelling call to action"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
#                     border-radius: 16px; padding: 3rem 2rem; text-align: center; 
#                     margin: 4rem 0 2rem 0;">
#             <h2 style="color: white; margin-bottom: 1rem;">Ready to Stop Fighting Yourself?</h2>
#             <p style="color: white; opacity: 0.9; font-size: 1.1rem; 
#                       max-width: 500px; margin: 0 auto 2rem auto;">
#                 Every day you wait is another day living with patterns that don't serve you. 
#                 Your transformation starts with a simple conversation.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             if st.button("🎯 Start Your Transformation Journey", type="primary", use_container_width=True):
#                 st.success("Perfect! Scroll down to book your free discovery call.")

# class MethodPage:
#     """Complete method page"""
    
#     def __init__(self):
#         self.hero = MethodHero()
#         self.why_it_works = WhyItWorks()
#         self.session_breakdown = TwoSessionBreakdown()
#         self.success_metrics = SuccessMetrics()
#         self.case_studies = CaseStudyShowcase()
#         self.investment = InvestmentSection()
#         self.final_cta = FinalCTA()
    
#     def render(self):
#         """Render complete method page"""
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
            
#         with st.container():
#             self.why_it_works.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.session_breakdown.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.success_metrics.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.case_studies.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.investment.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.final_cta.render()
#             st.markdown("    ")

# # Factory function for clean import
# def create_method_page():
#     return MethodPage()



"""
Method Page - The Science Behind 2-Session Transformation
Reviewed and corrected version with better flow and structure
"""
import streamlit as st

class MethodHero:
    """Hero section for method page using consistent styling"""
    
    def render(self):
        """Render method hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">The Science Behind Rapid Transformation</h1>
        </div>
        """, unsafe_allow_html=True)

        # Better positioning for description text using Streamlit
        st.write("Discover why our 2-session method succeeds where traditional approaches fail. It's not willpower. It's neuroscience.")

class TwoSessionBreakdown:
    """Detailed breakdown of the 2-session process with 3-column layout"""
    
    def render(self):
        """Render the session-by-session breakdown in 3 columns"""
        st.subheader("The Proven 2-Session Process")
        st.write("Each session has a specific purpose in your transformation journey:")
        
        # 3-column layout: Session 1, Session 2, Optional Session 3
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self._render_session_column(
                session_num=1,
                title="Pattern Analysis & Mapping",
                duration="90 minutes",
                icon="🔍",
                preview="Discover your patterns",
                what_happens=[
                    "Comprehensive behavioral analysis using proven psychological frameworks",
                    "Identify your unique subconscious triggers and response patterns", 
                    "Map the emotional and environmental factors that activate old behaviors",
                    "Discover the positive intent behind negative patterns",
                    "Begin initial positive programming to start shifting your mindset"
                ],
                outcome="You'll understand WHY you do what you do, often for the first time. Many clients feel immediate relief just from this clarity.",
                image_url=None, #"https://github.com/pepeette/Hypno/blob/main/img/session1_analysis.jpg?raw=true",
                border_color="#4CA1A3"
            )
        
        with col2:
            self._render_session_column(
                session_num=2,
                title="Subconscious Rewiring",
                duration="90 minutes",
                icon="⚡",
                preview="Rewire your mind",
                what_happens=[
                    "Enter deep hypnotic state for maximum subconscious receptivity",
                    "Install new neural pathways that support your desired behaviors",
                    "Replace limiting beliefs with empowering ones at the identity level",
                    "Create new automatic responses to old triggers",
                    "Anchor your new patterns with powerful positive emotional associations"
                ],
                outcome="The old urges simply disappear. You naturally make choices aligned with your goals without effort or internal struggle.",
                image_url=None, #"https://github.com/pepeette/Hypno/blob/main/img/session2_hypnosis.jpg?raw=true",
                border_color="#4CA1A3"
            )
        
        with col3:
            self._render_session_column(
                session_num="+1",
                title="Reinforcement",
                duration="60 minutes",
                icon="🎯",
                preview="Optional (15% need)",
                what_happens=[
                    "Strengthen any remaining weak spots in your new patterns",
                    "Address unexpected triggers that emerge in real-world situations",
                    "Fine-tune your responses for complete confidence",
                    "Provide additional tools for long-term maintenance"
                ],
                outcome="Complete confidence and mastery. Our guarantee: If you're not satisfied after 2 sessions, this session is complimentary.",
                image_url=None,
                border_color="#eab308",
                is_optional=True
            )
    
    def _render_session_column(self, session_num, title, duration, icon, preview, what_happens, outcome, image_url, border_color, is_optional=False):
        """Render individual session column with collapsible details"""
        
        # Session header card
        session_label = f"+{session_num}" if is_optional else str(session_num)
        optional_text = " (Optional)" if is_optional else ""
        
        st.markdown(f"""
        <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                    padding: 1.5rem; margin-bottom: 1rem; border-left: 4px solid {border_color}; 
                    text-align: center;">
            <div style="background: {border_color}; color: white; width: 40px; height: 40px; 
                        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                        font-weight: bold; font-size: 1.2rem; margin: 0 auto 1rem;">{session_label}</div>
            <h3 style="color: #273548; margin-bottom: 0.5rem; font-size: 1.1rem;">{icon} {title}{optional_text}</h3>
            <p style="color: #556D7A; margin: 0; font-size: 0.9rem; font-weight: 600;">{duration}</p>
            <p style="color: #556D7A; margin: 0.5rem 0 0 0; font-size: 0.85rem;">{preview}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Expandable details
        with st.expander(f"Details for Session {session_num}", expanded=False):
            if image_url:
                st.image(image_url, caption=f"Session {session_num}")
            
            st.markdown("**What happens during this session:**")
            for item in what_happens:
                st.write(f"• {item}")
            
            st.success(f"**Outcome:** {outcome}")

class SuccessMetrics:
    """Success rates and statistics"""
    
    def render(self):
        """Render success metrics with visual impact"""
        st.subheader("Proven Results Across Thousands of Sessions")
        
        # # Force 3 columns to stay in one row
        # st.markdown("""
        # <div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: nowrap; 
        #             justify-content: space-between;">
        #     <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
        #                 border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #22c55e;">
        #         <div style="color: #22c55e; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
        #             85%
        #         </div>
        #         <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
        #             Complete Success
        #         </div>
        #         <div style="color: #273548; font-size: 0.8rem;">
        #             Achieve all goals in 2 sessions
        #         </div>
        #     </div>
        #     <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
        #                 border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #eab308;">
        #         <div style="color: #eab308; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
        #             15%
        #         </div>
        #         <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
        #             Need Reinforcement
        #         </div>
        #         <div style="color: #273548; font-size: 0.8rem;">
        #             Benefit from optional 3rd session
        #         </div>
        #     </div>
        #     <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
        #                 border-radius: 12px; padding: 2rem; text-align: center; border-left: 4px solid #4CA1A3;">
        #         <div style="color: #4CA1A3; font-size: 2.5rem; font-weight: 700; line-height: 1.2;">
        #             95%+
        #         </div>
        #         <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin: 0.5rem 0;">
        #             Long-term Success
        #         </div>
        #         <div style="color: #273548; font-size: 0.8rem;">
        #             Still transformed 1 year later
        #         </div>
        #     </div>
        # </div>
        # """, unsafe_allow_html=True)

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
            
        st.success("**Compare this to traditional methods:** Most conventional approaches have success rates below 30%, require ongoing sessions, and have high relapse rates.")

class WhyItWorks:
    """Core science explanation section"""
    
    def render(self):
        """Render the core science behind the method"""
        st.subheader("Why Traditional Methods Keep Failing You")
        
        # Use normal Streamlit components for better readability
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.video("https://youtu.be/5ORz1-LWrjo?feature=shared")
        
        with col2:
            st.markdown("**The Problem:** Your conscious mind (5% of decisions) fights your subconscious programming (95% of decisions). Guess who wins? The subconscious. Every time.")
        
        st.info("""
        **Our Breakthrough:** Instead of fighting your subconscious, we work directly with it. 
        We identify your specific patterns and rewire them at the source. When your subconscious 
        supports your goals instead of sabotaging them, change becomes effortless.
        """)

class InvestmentSection:
    """Pricing and value proposition"""
    
    def render(self):
        """Render investment options"""
        st.subheader("Investment in Your Transformation")
        st.write("One-time investment. Lifetime results. Compare to years of traditional therapy:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Complete Package</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿3,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem;">Sessions 1 & 2 • Most Popular</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Includes:**")
            st.write("✓ Analysis Session (90 minutes)")
            st.write("✓ Transformation Session (90 minutes)")
            st.write("✓ Email support between sessions")
            st.write("✓ 85% success rate")
            
            if st.button("📞 Book Complete Package", type="primary", use_container_width=True):
                st.success("Excellent choice! Scroll down to book your discovery call.")
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <h2 style="color: #273548; margin-bottom: 1rem;">Premium Package</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿4,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem;">All 3 sessions • Peace of Mind</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Includes:**")
            st.write("✓ Everything in Complete Package")
            st.write("✓ Plus: 3rd reinforcement session")
            st.write("✓ 100% satisfaction guarantee")
            st.write("✓ Maximum confidence")
            
            if st.button("⭐ Book Premium Package", use_container_width=True):
                st.success("Smart choice! Scroll down to book your discovery call.")
        
        # Value comparison
        st.info("""
        💡 **Value Comparison:** Traditional therapy often costs ฿60,000+ over months or years. 
        The ongoing cost of your unwanted habit (smoking, stress eating, etc.) often exceeds our entire package price within months.
        """)

class MethodPage:
    """Complete method page with improved flow"""
    
    def __init__(self):
        self.hero = MethodHero()
        self.session_breakdown = TwoSessionBreakdown()
        self.success_metrics = SuccessMetrics()
        self.why_it_works = WhyItWorks()
        self.investment = InvestmentSection()
    
    def render(self):
        """Render complete method page with logical flow"""
        # 1. Hero - introduce the page
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        # 2. Process breakdown - show what we do
        with st.container():
            self.session_breakdown.render()
            st.markdown("    ")

        # 3. Science explanation - explain why it works
        with st.container():
            self.why_it_works.render()
            st.markdown("    ")
                
        # 4. Success metrics - prove it works
        with st.container():
            self.success_metrics.render()
            st.markdown("    ")
                
        # 5. Investment - show the value
        with st.container():
            self.investment.render()
            st.markdown("    ")

# Factory function for clean import
def create_method_page():
    return MethodPage()
