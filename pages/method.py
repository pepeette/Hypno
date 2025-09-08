"""
Method Page - The Science Behind 2-Session Transformation
Reviewed and corrected version with better flow and structure
"""
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from utils.email_handler import send_package_booking_email


class MethodHero:
    """Hero section for method page using consistent styling"""
    
    def render(self):
        """Render method hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">The Science behind Rapid Transformation</h1>
        </div>
        """, unsafe_allow_html=True)

        # Better positioning for description text using Streamlit
        st.write("Traditional therapy relies on willpower and takes months. My analytical hypnotherapy works directly with subconscious patterns - which is why 85% of clients achieve lasting change in just 2 sessions, not years. It's not willpower. It's neuroscience.")

class TwoSessionBreakdown:
    """Detailed breakdown of the 2-session process with 3-column layout"""
    
    def render(self):
        """Render the session-by-session breakdown in 3 columns"""
        st.subheader("The proven 2-session process")
        st.write("Each session has a specific purpose in your transformation journey:")
        
        # 3-column layout: Session 1, Session 2, Optional Session 3
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self._render_session_column(
                session_num=1,
                title="Deep pattern analysis ",
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
                title="Subconscious rewiring",
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
        with st.expander(f"Details for session {session_num}", expanded=False):
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
        st.subheader("Proven results across thousands of sessions")
        
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
                        3rd session Optional
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
        st.subheader("Why traditional methods keep failing you")
        
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

# class InvestmentSection:
#     """Pricing and value proposition"""
    
#     def render(self):
#         """Render investment options"""
#         st.subheader("Invest in your transformation")
#         st.write("One-time investment. Lifetime results. Compare to years of traditional therapy:")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Common Package</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿3,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem;">Sessions 1 & 2 • Most Popular</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("**Includes:**")
#             st.write("✓ Session 1: Deep pattern analysis (90 mins)")
#             st.write("✓Session 2: Subconscious rewiring (90 mins)")
#             st.write("✓ Email support between sessions")
#             st.write("✓ 85% achieve full transformation")
            
#             if st.button("📞 Book Common Package", type="primary", use_container_width=True):
#                 st.success("Excellent choice! Scroll down to book your discovery call.")
        
#         with col2:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <h2 style="color: #273548; margin-bottom: 1rem;">Complete Package</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿4,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem;">All 3 sessions • Peace of Mind</div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.markdown("**Includes:**")
#             st.write("✓ Everything in Common Package")
#             st.write("✓ Session 3: Optional reinforcement (60 mins)")
#             st.write("✓ 100% satisfaction commitment")
#             st.write("✓ Maximum confidence approach")
            
#             if st.button("⭐ Book Complete Package", use_container_width=True):
#                 st.success("Smart choice! Scroll down to book your discovery call.")
        
#         # Value comparison
#         st.info("""
#         *Compare: Traditional therapy often costs ฿60,000+ over months/years*
#         """)

class InvestmentSection:
    """Pricing and value proposition with email integration"""
    
    def __init__(self):
        # Initialize session state for tracking email sends
        if 'email_sent' not in st.session_state:
            st.session_state.email_sent = False
        if 'selected_package' not in st.session_state:
            st.session_state.selected_package = None

    def render(self):
        """Render investment options with email functionality"""
        st.subheader("Invest in your transformation")
        st.write("One-time investment. Lifetime results. Compare to years of traditional therapy:")

        # Show success message if email was sent
        if st.session_state.email_sent and st.session_state.selected_package:
            st.success(f"✅ Your interest in **{st.session_state.selected_package}** has been recorded! We'll contact you within 24 hours.")
            st.info("📞 For immediate assistance, scroll down to book a discovery call.")
            # Reset the flag
            st.session_state.email_sent = False
            st.session_state.selected_package = None

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Common Package</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿3,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem;">Sessions 1 & 2 • Most Popular</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Includes:**")
            st.write("✓ Session 1: Deep pattern analysis (90 mins)")
            st.write("✓ Session 2: Subconscious rewiring (90 mins)")
            st.write("✓ Email support between sessions")
            st.write("✓ 85% achieve full transformation")

            if st.button("📞 Book Common Package", type="primary", use_container_width=True, key="common_pkg"):
                self._handle_package_selection("Common Package (฿3,000)")

        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <h2 style="color: #273548; margin-bottom: 1rem;">Complete Package</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿4,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem;">All 3 sessions • Peace of Mind</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Includes:**")
            st.write("✓ Everything in Common Package")
            st.write("✓ Session 3: Optional reinforcement (60 mins)")
            st.write("✓ 100% satisfaction commitment")
            st.write("✓ Maximum confidence approach")

            if st.button("⭐ Book Complete Package", use_container_width=True, key="complete_pkg"):
                self._handle_package_selection("Complete Package (฿4,000)")

        # Value comparison
        st.info("""
        💡 **Value Comparison:** Traditional therapy often costs ฿60,000+ over months or years. 
        The ongoing cost of your unwanted habit often exceeds our package price within months.
        """)

        # Direct booking links
        st.markdown("### Ready to start? Choose your booking method:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <a href="https://calendly.com/laetitiasheppard/discovery" target="_blank" 
               style="display: inline-block; background-color: var(--accent); color: white;
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: none;">
                📞 Discovery Call First
            </a>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <a href="https://calendly.com/laetitiasheppard/package" target="_blank" 
               style="display: inline-block; background-color: white; color: var(--text-primary);
                      text-decoration: none; padding: 1rem 2rem; border-radius: var(--radius-sm);
                      font-weight: 600; transition: var(--transition);
                      box-shadow: var(--shadow-sm); text-align: center; width: 100%;
                      box-sizing: border-box; margin-bottom: 0.25rem; border: 2px solid var(--border);">
                ⚡ Direct Package Booking
            </a>
            """, unsafe_allow_html=True)

    def _handle_package_selection(self, package_name):
        """Handle package selection and send email"""
        try:
            # Import email handler
            from utils.email_handler import send_package_booking_email
            
            # Prepare booking data
            booking_data = {
                'package_type': package_name,
                'timestamp': st.session_state.get('current_time', 'Unknown'),
                'source': 'Method Page - Package Selection',
                'message': f'Visitor expressed interest in {package_name} package'
            }
            
            # Send email
            email_success = send_package_booking_email(booking_data)
            
            if email_success:
                st.session_state.email_sent = True
                st.session_state.selected_package = package_name
                st.rerun()
            else:
                st.error("❌ There was an issue sending your request. Please try booking directly using the calendar links below.")
                
        except Exception as e:
            st.error("❌ Unable to process your request. Please use the direct booking links below.")
            # Optional: Log error for debugging
            if st.secrets.get("debug_mode", False):
                st.exception(e)


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
