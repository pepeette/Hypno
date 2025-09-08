"""
Method Page - Streamlined for conversion
Method → Investment → FAQ flow for maximum clarity
"""
import streamlit as st

class MethodHero:
    """Hero section focused on the promise"""
    
    def render(self):
        """Render method hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white;">The neuroscience behind rapid transformation</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("Traditional therapy relies on willpower and takes months or years. My analytical hypnotherapy uses advanced neuroscience to rewire subconscious patterns directly - which is why 85% of clients achieve lasting change in just 2 sessions.")

class UnifiedMethodExplanation:
    """Clear explanation of the 2+1 neuroplasticity method"""
    
    def render(self):
        """Render the method explanation with neuroscience authority"""
        st.subheader("How neuroplasticity creates lasting change: 2 sessions + 1 optional")
        st.write("Proven neuroscience-based process. We work together to map your neural patterns, rewire your brain pathways, and consolidate the changes:")
        
        # 3-column layout showing the complete method
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
                <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">1</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Deep pattern analysis</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes</p>
                <p style="color: #556D7A;">We map your specific neural pathways and identify the subconscious triggers 
                that drive unwanted behaviors. You'll understand the neurological basis of your patterns for the first time.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("What happens in session 1:", expanded=False):
                st.write("• Comprehensive behavioral analysis using proven psychological frameworks")
                st.write("• Map your unique neural triggers and automatic response patterns")
                st.write("• Identify the neurological roots of your unwanted behaviors")
                st.write("• Discover the original conditioning events that created these pathways")
                st.write("• Begin initial positive neural programming in your subconscious mind")
                st.success("**Neuroscience result:** Clear understanding of your brain patterns and immediate relief for many clients.")
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #4CA1A3;">
                <div style="background: #4CA1A3; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">2</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural reset hypnosis</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">90 minutes</p>
                <p style="color: #556D7A;">Using clinical hypnosis to access your subconscious mind, we create new neural pathways 
                and deactivate old automatic responses. Your brain literally rewires itself for success.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("What happens in session 2:", expanded=False):
                st.write("• Enter theta brainwave state for maximum neuroplasticity")
                st.write("• Install new neural pathways that support your desired behaviors")
                st.write("• Deactivate limiting neural circuits and strengthen empowering ones")
                st.write("• Create new synaptic connections that bypass old triggers")
                st.write("• Anchor positive behavioral patterns at the cellular level")
                st.success("**Neuroscience result:** Effortless behavior change as your brain adopts new default patterns.")
        
        with col3:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 1.5rem; text-align: center; margin: 1rem 0; border-left: 4px solid #eab308;">
                <div style="background: #eab308; color: white; width: 50px; height: 50px; 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; font-size: 1.3rem; margin: 0 auto 1rem;">+1</div>
                <h3 style="color: #273548; margin-bottom: 0.5rem;">Neural consolidation</h3>
                <p style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">60 minutes • Only 15% need this</p>
                <p style="color: #556D7A;">Strengthen and consolidate your new neural networks if needed. 
                Ensure complete synaptic integration and long-term potentiation of positive patterns.</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("What happens in session 3 (optional):", expanded=False):
                st.write("• Reinforce new neural pathways through targeted hypnotic suggestion")
                st.write("• Address any remaining weak synaptic connections")
                st.write("• Fine-tune neurotransmitter responses to environmental triggers")
                st.write("• Consolidate long-term memory formation of new behavioral patterns")
                st.success("**Neuroscience result:** Complete neural mastery with permanent synaptic changes. If you're not satisfied after 2 sessions, this session is complimentary.")
        
        # Scientific disclaimer about collaborative neuroplasticity
        st.markdown("""
        <div style="background: rgba(76, 161, 163, 0.1); border-radius: 8px; padding: 1rem; margin: 1.5rem 0; 
                    border-left: 4px solid #4CA1A3;">
            <p style="margin: 0; color: #273548; font-style: italic;">
                * Neuroplasticity requires active collaboration between you and the therapist throughout each session. 
                Your conscious participation enhances the brain's ability to form new neural connections.
            </p>
        </div>
        """, unsafe_allow_html=True)

class InvestmentSection:
    """Simplified pricing directly linked to the neuroscience method"""
    
    def render(self):
        """Render clear, simple investment options"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 1rem 0;">
            <h2 style="color: #273548;">Choose your transformation package</h2>
            <p style="color: #556D7A; font-size: 1.1rem;">One-time investment in your neural rewiring. Lifetime results.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: white; border: 2px solid #4CA1A3; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <div style="background: #4CA1A3; color: white; padding: 0.5rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
                    Most popular choice
                </div>
                <h2 style="color: #4CA1A3; margin-bottom: 1rem;">Standard neuroplasticity program</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿3,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem; font-weight: 600;">Sessions 1 + 2</div>
                <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6;">
                    ✓ Deep pattern analysis (90 min)<br>
                    ✓ Neural reset hypnosis (90 min)<br>
                    ✓ Email support for integration<br>
                    ✓ 85% achieve complete neural rewiring
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Select standard program", type="primary", use_container_width=True, key="standard_pkg"):
                self._select_package("Standard neuroplasticity program (฿3,000) - Sessions 1 + 2")
        
        with col2:
            st.markdown("""
            <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                        padding: 2rem; text-align: center; margin: 1rem 0;">
                <div style="background: #eab308; color: white; padding: 0.5rem 1rem; 
                            border-radius: 20px; font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem;">
                    Maximum confidence
                </div>
                <h2 style="color: #273548; margin-bottom: 1rem;">Complete neural transformation</h2>
                <div style="color: #273548; font-size: 2.5rem; font-weight: 700; margin: 1rem 0;">
                    ฿4,000
                </div>
                <div style="color: #556D7A; margin-bottom: 1.5rem; font-weight: 600;">Sessions 1 + 2 + 3</div>
                <div style="color: #556D7A; font-size: 0.9rem; line-height: 1.6;">
                    ✓ Everything in standard program<br>
                    ✓ Neural consolidation session (60 min)<br>
                    ✓ 100% satisfaction guarantee<br>
                    ✓ Complete synaptic integration
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Select complete transformation", use_container_width=True, key="complete_pkg"):
                self._select_package("Complete neural transformation (฿4,000) - Sessions 1 + 2 + 3")
        
        # Show selection status
        if st.session_state.get('selected_package'):
            st.success(f"✅ You selected: **{st.session_state.selected_package}**")
            st.info("🔄 Scroll down to complete your booking and begin your neural transformation.")
        
        # Scientific value comparison
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0; padding: 1rem; 
                    background: rgba(76, 161, 163, 0.05); border-radius: 8px;">
            <p style="color: #556D7A; margin: 0; font-style: italic;">
                <strong>Neuroscience advantage:</strong> Traditional cognitive therapy takes months to create minimal neural change. 
                Our method uses advanced hypnotherapy to accelerate neuroplasticity, achieving in 2 sessions what takes others years.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _select_package(self, package_name):
        """Store selected package and scroll to booking form"""
        st.session_state.selected_package = package_name
        st.session_state.package_description = f"I'm interested in the {package_name}. Please provide more information about scheduling my neural transformation."
        st.rerun()

class FAQ:
    """FAQ section addressing common objections after investment"""
    
    def __init__(self):
        self.faqs = [
            {
                "question": "Is hypnosis safe?",
                "answer": "Clinical hypnotherapy is completely safe. You remain aware and in control throughout the session. Hypnosis is simply a focused state of relaxation - similar to meditation or being absorbed in a good book."
            },
            {
                "question": "Will I lose control or reveal secrets?",
                "answer": "No. You can't be made to do anything against your will or values. Stage hypnosis entertainment is very different from clinical hypnotherapy. You'll be aware throughout and can open your eyes or speak anytime."
            },
            {
                "question": "What if I can't be hypnotized?",
                "answer": "Everyone can be hypnotized because it's a natural brain state you enter daily. Some people go deeper than others, but therapeutic change can happen at any level. Our approach adapts to your unique response style."
            },
            {
                "question": "How many sessions do I actually need?",
                "answer": "Most clients (85%) achieve their goals in 2 sessions. Some choose a 3rd reinforcement session. This is much faster than traditional therapy because we work directly with your subconscious mind where the patterns are stored."
            },
            {
                "question": "How is this different from other hypnotherapists?",
                "answer": "Our method combines detailed pattern analysis in session 1 with targeted transformation in session 2. Most hypnotherapists use generic scripts - we create a completely personalized approach based on your specific triggers and beliefs."
            },
            {
                "question": "What if it doesn't work for me?",
                "answer": "Our 85% success rate speaks to the effectiveness of personalized hypnotherapy. If you're not satisfied after 2 sessions, we offer a complimentary 3rd session to ensure your success."
            },
            {
                "question": "Do online sessions work as well as in-person?",
                "answer": "Yes. Online sessions are equally effective. We use secure video conferencing and have successfully helped clients worldwide. Many people actually find it easier to relax in their own space."
            },
            {
                "question": "How much does it cost?",
                "answer": "Our 2-session package is 3,000 THB. Compare this to years of traditional therapy (often 60,000+ THB) or the ongoing cost of your unwanted habit. Most clients save money within months of their transformation."
            }
        ]
    
    def render(self):
        """Render FAQ section to address objections"""
        st.subheader("Your questions answered")
        st.write("Common questions about our neuroscience-based approach and what to expect.")
        
        for faq in self.faqs:
            # Ensure white background for FAQ expanders
            with st.expander(f"{faq['question']}", expanded=False):
                st.write(faq['answer'])

class MethodPage:
    """Streamlined method page focused on conversion"""
    
    def __init__(self):
        self.hero = MethodHero()
        self.unified_method = UnifiedMethodExplanation()
        self.investment = InvestmentSection()
        self.faq = FAQ()
    
    def render(self):
        """Render streamlined method page for maximum conversion"""
        # Hero - sets the neuroscience authority and promise
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        # Method - detailed explanation of the process
        with st.container():
            self.unified_method.render()
            st.markdown("    ")

        # Investment - immediate logical next step after understanding method
        with st.container():
            self.investment.render()
            st.markdown("    ")

        # FAQ - addresses objections right when people are deciding
        with st.container():
            self.faq.render()
            st.markdown("    ")

def create_method_page():
    return MethodPage()
