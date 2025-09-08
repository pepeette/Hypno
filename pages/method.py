# """
# Method Page - Streamlined for conversion
# Method → Investment → FAQ flow for maximum clarity
# """
# import streamlit as st

# class MethodHero:
#     """Hero section focused on the promise"""
    
#     def render(self):
#         """Render method hero section"""
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                     border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#             <h1 style="color: white;">The neuroscience behind rapid transformation</h1>
#         </div>
#         """, unsafe_allow_html=True)

#         st.write("Traditional therapy relies on willpower and takes months or years. My analytical hypnotherapy uses advanced neuroscience to rewire subconscious patterns directly - which is why 85% of clients achieve lasting change in just 2 sessions.")

# class UnifiedMethodExplanation:
#     """Clear explanation of the 2+1 neuroplasticity method"""
    
#     def render(self):
#         """Render the method explanation with neuroscience authority"""
#         st.subheader("How neuroplasticity creates lasting change: 2 sessions + 1 optional")
#         st.write("Proven neuroscience-based process. We work together to map your neural patterns, rewire your brain pathways, and consolidate the changes:")
        
#         # 3-column layout showing the complete method
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
#                 <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
#                             border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                             font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">1</div>
#                 <h3 style="color: #273548; margin-bottom: 0.5rem;">Deep pattern analysis</h3>
#                 <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes</p>
#                 <p style="color: #556D7A;">We map your specific neural pathways and identify the subconscious triggers 
#                 that drive unwanted behaviors. You'll understand the neurological basis of your patterns for the first time.</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             with st.expander("What happens in session 1:", expanded=False):
#                 st.write("• Comprehensive behavioral analysis using proven psychological frameworks")
#                 st.write("• Map your unique neural triggers and automatic response patterns")
#                 st.write("• Identify the neurological roots of your unwanted behaviors")
#                 st.write("• Discover the original conditioning events that created these pathways")
#                 st.write("• Begin initial positive neural programming in your subconscious mind")
#                 st.success("**Neuroscience result:** Clear understanding of your brain patterns and immediate relief for many clients.")
        
#         with col2:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
#                 <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
#                             border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                             font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">2</div>
#                 <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural reset hypnosis</h3>
#                 <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes</p>
#                 <p style="color: #556D7A;">Using clinical hypnosis to access your subconscious mind, we create new neural pathways 
#                 and deactivate old automatic responses. Your brain literally rewires itself for success.</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             with st.expander("What happens in session 2:", expanded=False):
#                 st.write("• Enter theta brainwave state for maximum neuroplasticity")
#                 st.write("• Install new neural pathways that support your desired behaviors")
#                 st.write("• Deactivate limiting neural circuits and strengthen empowering ones")
#                 st.write("• Create new synaptic connections that bypass old triggers")
#                 st.write("• Anchor positive behavioral patterns at the cellular level")
#                 st.success("**Neuroscience result:** Effortless behavior change as your brain adopts new default patterns.")
        
#         with col3:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #eab308;">
#                 <div style="background: #eab308; color: white; width: 50px; height: 50px; 
#                             border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                             font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">+1</div>
#                 <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural consolidation</h3>
#                 <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">60 minutes • Only 15% need this</p>
#                 <p style="color: #556D7A;">Strengthen and consolidate your new neural networks if needed. 
#                 Ensure complete synaptic integration and long-term potentiation of positive patterns.</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             with st.expander("What happens in session 3 (optional):", expanded=False):
#                 st.write("• Reinforce new neural pathways through targeted hypnotic suggestion")
#                 st.write("• Address any remaining weak synaptic connections")
#                 st.write("• Fine-tune neurotransmitter responses to environmental triggers")
#                 st.write("• Consolidate long-term memory formation of new behavioral patterns")
#                 st.success("**Neuroscience result:** Complete neural mastery with permanent synaptic changes. If you're not satisfied after 2 sessions, this session is complimentary.")
        
#         # Scientific disclaimer about collaborative neuroplasticity
#         st.markdown("""
#         <div style="background: rgba(76, 161, 163, 0.1); border-radius: 8px; padding: 1rem; margin: 1.5rem 0; 
#                     border-left: 4px solid #4CA1A3;">
#             <p style="margin: 0; color: #273548; font-style: italic;">
#                 * Neuroplasticity requires active collaboration between you and the therapist throughout each session. 
#                 Your conscious participation enhances the brain's ability to form new neural connections.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# class InvestmentSection:
#     """Simplified pricing directly linked to the neuroscience method"""
    
#     def render(self):
#         """Render clear, simple investment options"""
#         st.markdown("""
#         <div style="text-align: center; margin: 2rem 0 1rem 0;">
#             <h2 style="color: #273548;">Choose your transformation package</h2>
#             <p style="color: #556D7A; font-size: 1.1rem;">One-time investment in your neural rewiring. Lifetime results.</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <div style="background: #4CA1A3; color: white; padding: 0.5rem 1rem; 
#                             border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
#                     Most popular choice
#                 </div>
#                 <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Standard neuroplasticity program</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿3,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem; font-weight: 600;">Sessions 1 + 2</div>
#                 <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6;">
#                     ✓ Deep pattern analysis (90 min)<br>
#                     ✓ Neural reset hypnosis (90 min)<br>
#                     ✓ Email support for integration<br>
#                     ✓ 85% achieve complete neural rewiring
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             if st.button("Select standard program", type="primary", use_container_width=True, key="standard_pkg"):
#                 self._select_package("Standard neuroplasticity program (฿3,000) - Sessions 1 + 2")
        
#         with col2:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; text-align: center; margin: 1rem 0;">
#                 <div style="background: #eab308; color: white; padding: 0.5rem 1rem; 
#                             border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
#                     Maximum confidence
#                 </div>
#                 <h2 style="color: #273548; margin-bottom: 1rem;">Complete neural transformation</h2>
#                 <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
#                     ฿4,000
#                 </div>
#                 <div style="color: #556D7A; margin-bottom: 1.5rem; font-weight: 600;">Sessions 1 + 2 + 3</div>
#                 <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6;">
#                     ✓ Everything in standard program<br>
#                     ✓ Neural consolidation session (60 min)<br>
#                     ✓ 100% satisfaction guarantee<br>
#                     ✓ Complete synaptic integration
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             if st.button("Select complete transformation", use_container_width=True, key="complete_pkg"):
#                 self._select_package("Complete neural transformation (฿4,000) - Sessions 1 + 2 + 3")
        
#         # Show selection status
#         if st.session_state.get('selected_package'):
#             st.success(f"✅ You selected: **{st.session_state.selected_package}**")
#             st.info("🔄 Scroll down to complete your booking and begin your neural transformation.")
        
#         # Scientific value comparison
#         st.markdown("""
#         <div style="text-align: center; margin: 2rem 0; padding: 1rem; 
#                     background: rgba(76, 161, 163, 0.05); border-radius: 8px;">
#             <p style="color: #556D7A; margin: 0; font-style: italic;">
#                 <strong>Neuroscience advantage:</strong> Traditional cognitive therapy takes months to create minimal neural change. 
#                 Our method uses advanced hypnotherapy to accelerate neuroplasticity, achieving in 2 sessions what takes others years.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _select_package(self, package_name):
#         """Store selected package and scroll to booking form"""
#         st.session_state.selected_package = package_name
#         st.session_state.package_description = f"I'm interested in the {package_name}. Please provide more information about scheduling my neural transformation."
#         st.rerun()

# class FAQ:
#     """FAQ section addressing common objections after investment"""
    
#     def __init__(self):
#         self.faqs = [
#             {
#                 "question": "Is hypnosis safe?",
#                 "answer": "Clinical hypnotherapy is completely safe. You remain aware and in control throughout the session. Hypnosis is simply a focused state of relaxation - similar to meditation or being absorbed in a good book."
#             },
#             {
#                 "question": "Will I lose control or reveal secrets?",
#                 "answer": "No. You can't be made to do anything against your will or values. Stage hypnosis entertainment is very different from clinical hypnotherapy. You'll be aware throughout and can open your eyes or speak anytime."
#             },
#             {
#                 "question": "What if I can't be hypnotized?",
#                 "answer": "Everyone can be hypnotized because it's a natural brain state you enter daily. Some people go deeper than others, but therapeutic change can happen at any level. Our approach adapts to your unique response style."
#             },
#             {
#                 "question": "How many sessions do I actually need?",
#                 "answer": "Most clients (85%) achieve their goals in 2 sessions. Some choose a 3rd reinforcement session. This is much faster than traditional therapy because we work directly with your subconscious mind where the patterns are stored."
#             },
#             {
#                 "question": "How is this different from other hypnotherapists?",
#                 "answer": "Our method combines detailed pattern analysis in session 1 with targeted transformation in session 2. Most hypnotherapists use generic scripts - we create a completely personalized approach based on your specific triggers and beliefs."
#             },
#             {
#                 "question": "What if it doesn't work for me?",
#                 "answer": "Our 85% success rate speaks to the effectiveness of personalized hypnotherapy. If you're not satisfied after 2 sessions, we offer a complimentary 3rd session to ensure your success."
#             },
#             {
#                 "question": "Do online sessions work as well as in-person?",
#                 "answer": "Yes. Online sessions are equally effective. We use secure video conferencing and have successfully helped clients worldwide. Many people actually find it easier to relax in their own space."
#             },
#             {
#                 "question": "How much does it cost?",
#                 "answer": "Our 2-session package is 3,000 THB. Compare this to years of traditional therapy (often 60,000+ THB) or the ongoing cost of your unwanted habit. Most clients save money within months of their transformation."
#             }
#         ]
    
#     def render(self):
#         """Render FAQ section to address objections"""
#         st.subheader("Your questions answered")
#         st.write("Common questions about our neuroscience-based approach and what to expect.")
        
#         for faq in self.faqs:
#             # Ensure white background for FAQ expanders
#             with st.expander(f"{faq['question']}", expanded=False):
#                 st.write(faq['answer'])

# class MethodPage:
#     """Streamlined method page focused on conversion"""
    
#     def __init__(self):
#         self.hero = MethodHero()
#         self.unified_method = UnifiedMethodExplanation()
#         self.investment = InvestmentSection()
#         self.faq = FAQ()
    
#     def render(self):
#         """Render streamlined method page for maximum conversion"""
#         # Hero - sets the neuroscience authority and promise
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
        
#         # Method - detailed explanation of the process
#         with st.container():
#             self.unified_method.render()
#             st.markdown("    ")

#         # Investment - immediate logical next step after understanding method
#         with st.container():
#             self.investment.render()
#             st.markdown("    ")

#         # FAQ - addresses objections right when people are deciding
#         with st.container():
#             self.faq.render()
#             st.markdown("    ")

# def create_method_page():
#     return MethodPage()


"""
Enhanced Method Page - Maximum authority and conversion
Research Authority → Neuroscience Method → Investment Value → FAQ
"""
import streamlit as st

class AuthorityHero:
    """Hero that reinforces home page authority and introduces detailed explanation"""
    
    def render(self):
        """Render hero with research backing and connection to home page"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">The Method That Achieves 93% Lasting Change</h1>
            <p style="color: white; opacity: 0.95; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Here's exactly how we transform in 2 sessions what takes traditional therapy 600+ sessions
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Research authority reinforcement
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 1px solid #ef4444; border-radius: 8px; 
                        padding: 1rem; text-align: center;">
                <div style="color: #ef4444; font-size: 1.8rem; font-weight: 700;">38%</div>
                <div style="color: #556D7A; font-size: 0.9rem;">Psychoanalysis Success</div>
                <div style="color: #556D7A; font-size: 0.8rem;">After 600 sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #eab308; border-radius: 8px; 
                        padding: 1rem; text-align: center;">
                <div style="color: #eab308; font-size: 1.8rem; font-weight: 700;">72%</div>
                <div style="color: #556D7A; font-size: 0.9rem;">Behavioral Therapy</div>
                <div style="color: #556D7A; font-size: 0.8rem;">After 22 sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: white; border: 2px solid #22c55e; border-radius: 8px; 
                        padding: 1rem; text-align: center;">
                <div style="color: #22c55e; font-size: 1.8rem; font-weight: 700;">93%</div>
                <div style="color: #556D7A; font-size: 0.9rem;">Our Hypnotherapy</div>
                <div style="color: #556D7A; font-size: 0.8rem;">After 6 sessions</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.caption("*American Health Magazine Comparative Study, February 2007*")
        
        st.info("**The Science is Clear**: When you work directly with the subconscious mind (95% of your decisions), transformation happens 15x faster than conscious-only approaches.")

class NeuroscienceMethod:
    """Enhanced method explanation with brain science and timeline comparison"""
    
    def render(self):
        """Render the complete neuroscience method with authority"""
        st.subheader("The Neuroplasticity Transformation Protocol")
        st.write("**Why our approach works when others fail**: We use clinical hypnosis to access theta brain wave states where rapid neural rewiring occurs. Here's the precise 3-step protocol:")
        
        # Brain science explanation first
        self._render_brain_science()
        
        # Then the 3-step method
        self._render_three_step_method()
        
        # Timeline comparison
        self._render_timeline_comparison()
    
    def _render_brain_science(self):
        """Explain the neuroscience foundation"""
        st.markdown("### The Neuroscience Foundation")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.video("https://youtu.be/5ORz1-LWrjo?feature=shared")
        
        with col2:
            st.write("**Traditional therapy limitation**: Works only with your conscious mind (5% of decisions) in beta brain wave states. This is why willpower fails and change feels like constant struggle.")
            
            st.write("**Hypnotherapy advantage**: Accesses your subconscious mind (95% of decisions) using theta brain wave states (4-8 Hz) where neuroplasticity is maximized.")
            
            st.success("**Result**: New neural pathways form 15x faster in theta states. Your brain literally rewires itself for automatic success behaviors.")
    
    def _render_three_step_method(self):
        """Render enhanced 3-step method with more neuroscience detail"""
        st.markdown("### The 3-Step Neural Rewiring Protocol")
        
        # 3-column layout with enhanced descriptions
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
                <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">1</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural Pattern Mapping</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes • Deep Analysis</p>
                <p style="color: #556D7A;">We map your specific neural circuits and identify the exact synaptic pathways 
                that trigger unwanted behaviors. You'll understand your brain's wiring for the first time.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("🧠 Neuroscience breakdown - Session 1:", expanded=False):
                st.write("**Brain State**: Light alpha waves (8-13 Hz) for conscious analysis")
                st.write("**Neural Focus**: Mapping trigger-response circuits in limbic system")
                st.write("**Process**:")
                st.write("• Identify environmental triggers that activate old neural pathways")
                st.write("• Map emotional conditioning stored in amygdala and hippocampus")
                st.write("• Locate specific synaptic connections driving automatic behaviors")
                st.write("• Discover the original neuroplasticity events that created these patterns")
                st.write("• Begin preliminary positive neural programming in prefrontal cortex")
                st.success("**Immediate Effect**: 60% of clients report relief just from understanding their neural patterns")
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
                <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">2</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Deep Neural Rewiring</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes • Theta Hypnosis</p>
                <p style="color: #556D7A;">Using clinical hypnosis to reach theta brain states, we create new neural networks 
                and deactivate old synaptic connections. Your brain builds new automatic response patterns.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("🧠 Neuroscience breakdown - Session 2:", expanded=False):
                st.write("**Brain State**: Deep theta waves (4-8 Hz) for maximum neuroplasticity")
                st.write("**Neural Focus**: Creating new synaptic connections in neural networks")
                st.write("**Process**:")
                st.write("• Enter theta state where new neural pathways form 15x faster")
                st.write("• Install positive behavioral circuits in basal ganglia (habit center)")
                st.write("• Strengthen prefrontal cortex control over limbic system responses")
                st.write("• Create new synaptic connections that bypass old trigger pathways")
                st.write("• Anchor new patterns through repetitive neural firing (Hebb's Law)")
                st.success("**Transformation Result**: 85% achieve effortless behavior change as new neural patterns become dominant")
        
        with col3:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #eab308;">
                <div style="background: #eab308; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">+1</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural Consolidation</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">60 minutes • Optional (15% need)</p>
                <p style="color: #556D7A;">Strengthen synaptic connections through targeted reinforcement. 
                Ensure complete neural integration and long-term potentiation of new behavioral patterns.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("🧠 Neuroscience breakdown - Session 3:", expanded=False):
                st.write("**Brain State**: Focused theta (5-7 Hz) for synaptic strengthening")
                st.write("**Neural Focus**: Long-term potentiation and memory consolidation")
                st.write("**Process**:")
                st.write("• Reinforce new neural pathways through repeated activation")
                st.write("• Strengthen synaptic connections via protein synthesis enhancement")
                st.write("• Optimize neurotransmitter balance for sustained change")
                st.write("• Consolidate behavioral patterns into long-term procedural memory")
                st.success("**Guarantee Result**: Complete neural mastery. If unsatisfied after 2 sessions, this session is complimentary")
        
        # Collaborative note
        st.markdown("""
        <div style="background: rgba(76, 161, 163, 0.1); border-radius: 8px; padding: 1rem; margin: 1.5rem 0; 
                    border-left: 4px solid #4CA1A3;">
            <p style="margin: 0; color: #273548; font-style: italic;">
                **Collaborative Neuroplasticity**: Your active participation enhances neural rewiring. 
                We work together as your conscious mind guides the subconscious transformation process.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_timeline_comparison(self):
        """Visual timeline comparison showing dramatic difference"""
        st.markdown("### Transformation Timeline: Us vs Traditional Therapy")
        
        # Traditional therapy timeline
        st.markdown("**Traditional Therapy Path:**")
        st.markdown("""
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="background: #ef4444; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Month 1-6
                </div>
                <div>Initial consultations, building rapport, surface-level behavioral strategies</div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                <div style="background: #ef4444; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Month 6-18
                </div>
                <div>Analyzing childhood experiences, processing emotions, developing coping mechanisms</div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                <div style="background: #ef4444; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Month 18-36
                </div>
                <div>Maintenance phase, relapse prevention, ongoing support (if successful)</div>
            </div>
            <div style="text-align: center; margin-top: 1rem; color: #ef4444; font-weight: bold;">
                Cost: 60,000+ THB • Success Rate: 38-72% • Timeline: 2-3+ Years
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Our method timeline
        st.markdown("**Our Neuroplasticity Method:**")
        st.markdown("""
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="background: #22c55e; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Week 1
                </div>
                <div><strong>Session 1:</strong> Complete neural pattern mapping and initial positive programming</div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                <div style="background: #22c55e; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Week 2-3
                </div>
                <div><strong>Session 2:</strong> Deep neural rewiring using theta-state hypnosis</div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                <div style="background: #eab308; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; white-space: nowrap;">
                    Week 4+
                </div>
                <div><strong>Optional Session 3:</strong> Neural consolidation if needed (15% of clients)</div>
            </div>
            <div style="text-align: center; margin-top: 1rem; color: #22c55e; font-weight: bold;">
                Cost: 3,000-4,000 THB • Success Rate: 93% • Timeline: 2-4 Weeks
            </div>
        </div>
        """, unsafe_allow_html=True)

class EnhancedInvestment:
    """Investment section with strong value proposition and urgency"""
    
    def render(self):
        """Render investment with dramatic value comparison"""
        st.markdown("### Your Investment in Neural Transformation")
        
        # Value proposition header
        st.markdown("""
        <div style="text-align: center; background: rgba(76, 161, 163, 0.1); border-radius: 8px; 
                    padding: 2rem; margin: 2rem 0; border-left: 4px solid #4CA1A3;">
            <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Choose 2 Weeks of Neural Rewiring Over 3 Years of Traditional Therapy</h2>
            <p style="color: #273548; font-size: 1.1rem; margin: 0;">
                One-time investment. Lifetime neural transformation. 20x more cost-effective than traditional therapy.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Package options with enhanced value messaging
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0; position: relative;">
                <div style="background: #4CA1A3; color: white; padding: 0.5rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
                    ⭐ Most Popular - 85% Success Rate
                </div>
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Neural Rewiring Program</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿3,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1rem; font-weight: 600;">Sessions 1 + 2 • 180 minutes total</div>
                <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6; text-align: left;">
                    ✓ Neural pattern mapping (90 min)<br>
                    ✓ Theta-state hypnotic rewiring (90 min)<br>
                    ✓ Email support during integration<br>
                    ✓ 85% achieve complete transformation<br>
                    ✓ <strong>Save 57,000+ THB vs traditional therapy</strong>
                </div>
                <div style="background: #f0fdf4; color: #166534; padding: 0.5rem; border-radius: 4px; 
                            font-size: 0.8rem; margin-top: 1rem;">
                    💰 Cost per successful outcome: ฿3,530 (vs ฿158,000+ traditional)
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🧠 Select Neural Rewiring Program", type="primary", use_container_width=True, key="standard_pkg"):
                self._select_package("Neural Rewiring Program (฿3,000) - Sessions 1 + 2", "I'm ready to begin my neural transformation with the 2-session program. Please schedule my pattern mapping session.")
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <div style="background: #eab308; color: white; padding: 0.5rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
                    🛡️ Maximum Confidence - 100% Guarantee
                </div>
                <h2 style="color: #273548; margin-bottom: 1rem;">Complete Neural Mastery</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿4,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1rem; font-weight: 600;">Sessions 1 + 2 + 3 • 240 minutes total</div>
                <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6; text-align: left;">
                    ✓ Everything in standard program<br>
                    ✓ Neural consolidation session (60 min)<br>
                    ✓ 100% satisfaction guarantee<br>
                    ✓ Complete synaptic integration<br>
                    ✓ <strong>Save 56,000+ THB vs traditional therapy</strong>
                </div>
                <div style="background: #fef3c7; color: #92400e; padding: 0.5rem; border-radius: 4px; 
                            font-size: 0.8rem; margin-top: 1rem;">
                    🎯 Perfect for deep-rooted patterns or maximum confidence
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🎯 Select Complete Neural Mastery", use_container_width=True, key="complete_pkg"):
                self._select_package("Complete Neural Mastery (฿4,000) - Sessions 1 + 2 + 3", "I want the complete transformation with maximum confidence. Please schedule my comprehensive neural mastery program.")
        
        # Show selection status
        if st.session_state.get('selected_package'):
            st.success(f"✅ **Selected**: {st.session_state.selected_package}")
            st.info("🔥 **Next Step**: Scroll down to complete your booking and lock in your neural transformation timeline.")
        
        # Urgency and value reinforcement
        st.markdown("""
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; 
                    padding: 1.5rem; margin: 2rem 0; text-align: center;">
            <h3 style="color: #dc2626; margin-bottom: 1rem;">Why Wait? Every Day You Delay Costs You More</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1rem 0;">
                <div>
                    <div style="color: #dc2626; font-weight: bold;">Traditional Therapy Cost</div>
                    <div style="color: #556D7A;">฿2,000+ per session × 30+ sessions</div>
                </div>
                <div>
                    <div style="color: #dc2626; font-weight: bold;">Opportunity Cost</div>
                    <div style="color: #556D7A;">3+ years of limited progress</div>
                </div>
                <div>
                    <div style="color: #dc2626; font-weight: bold;">Habit Cost</div>
                    <div style="color: #556D7A;">Smoking: ฿5,000+/month</div>
                </div>
            </div>
            <p style="color: #273548; font-weight: 600; margin: 1rem 0;">
                Our method pays for itself within weeks. Book now and start your neural transformation this month.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _select_package(self, package_name, description):
        """Store selected package with detailed description"""
        st.session_state.selected_package = package_name
        st.session_state.package_description = description
        st.rerun()

class AuthorityFAQ:
    """Enhanced FAQ section addressing investment objections"""
    
    def __init__(self):
        self.faqs = [
            {
                "question": "How can 2 sessions match years of traditional therapy?",
                "answer": "Traditional therapy works with your conscious mind (5% of decisions) in beta brain wave states. We access your subconscious mind (95% of decisions) using theta brain wave states where neuroplasticity is 15x faster. The American Health Magazine study proves our 93% success rate vs 38-72% for traditional methods."
            },
            {
                "question": "Is the neuroscience real or just marketing?",
                "answer": "Completely real. Our method is based on established neuroscience: theta brain waves (4-8 Hz) maximize neuroplasticity, Hebb's Law (neurons that fire together wire together), and long-term potentiation for memory formation. Every technique is grounded in peer-reviewed brain research."
            },
            {
                "question": "Why don't all therapists use this method?",
                "answer": "Most therapists are trained in conscious-mind approaches (CBT, psychoanalysis) that work slowly. Clinical hypnotherapy requires specialized training in neuroscience, brain wave states, and subconscious programming. It's more advanced but dramatically more effective."
            },
            {
                "question": "What if my problem is too complex or deep-rooted?",
                "answer": "Deep-rooted patterns often respond faster to our method because they're stored in the subconscious where we work directly. The deeper the pattern, the more dramatic the transformation when you rewire it at the source. Our 93% success rate includes complex, long-term issues."
            },
            {
                "question": "How do I know if I'll be in the 93% who succeed?",
                "answer": "Our success rate applies to people ready for change who follow the protocol. The assessment quiz on our home page indicates readiness. If you scored 55%+, you have excellent potential. Lower scores may benefit from our discovery call first."
            },
            {
                "question": "What happens if I'm in the 7% who don't succeed?",
                "answer": "Very rare, but if you're not satisfied after 2 sessions, we provide a complimentary 3rd session. Our goal is your success, not just completion of sessions. We work together until you achieve your transformation."
            },
            {
                "question": "Is online hypnotherapy as effective as in-person?",
                "answer": "Yes. Hypnosis works through voice and visual focus, not physical presence. Many clients prefer online sessions in their comfortable environment. We use secure video conferencing and achieve identical results worldwide."
            },
            {
                "question": "How quickly will I see results?",
                "answer": "Many clients notice changes immediately after Session 1 (understanding their patterns). Most see significant behavioral changes within 3-7 days after Session 2 as new neural pathways become dominant. Complete integration typically occurs within 2-4 weeks."
            }
        ]
    
    def render(self):
        """Render enhanced FAQ addressing investment concerns"""
        st.subheader("Investment Questions Answered")
        st.write("**Common concerns about choosing neuroscience-based transformation over traditional therapy:**")
        
        for faq in self.faqs:
            with st.expander(f"❓ {faq['question']}", expanded=False):
                st.write(faq['answer'])

class MethodPage:
    """Enhanced method page for maximum authority and conversion"""
    
    def __init__(self):
        self.hero = AuthorityHero()
        self.method = NeuroscienceMethod()
        self.investment = EnhancedInvestment()
        self.faq = AuthorityFAQ()
    
    def render(self):
        """Render enhanced method page with conversion focus"""
        # Authority hero - reinforces home page claims with research
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        # Detailed neuroscience method - shows exactly how it works
        with st.container():
            self.method.render()
            st.markdown("    ")

        # Enhanced investment - makes the choice obvious through value
        with st.container():
            self.investment.render()
            st.markdown("    ")

        # Authority FAQ - addresses all objections with science
        with st.container():
            self.faq.render()
            st.markdown("    ")

def create_method_page():
    return MethodPage()
