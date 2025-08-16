"""
Method page component for the Hypnotherapy website
Explains the 2-step process, science, and pricing
"""
import streamlit as st

class MethodHero:
    """Hero section for the method page"""
    
    def render(self):
        """Render method page hero"""
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0 3rem 0;">
            <h1>Why 2 Sessions Work When Years of Trying Haven't</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                The science-backed approach that bypasses willpower and rewires your subconscious mind directly
            </p>
        </div>
        """, unsafe_allow_html=True)

class KeyDifferentiator:
    """Section explaining the key differentiator"""
    
    def render(self):
        """Render the breakthrough difference section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, var(--card-bg) 100%); 
                    border-radius: var(--radius-md); padding: 2rem; margin: 2rem 0; 
                    border-left: 4px solid var(--accent);">
            <h2 style="color: var(--accent); margin-bottom: 1rem;">🧠 The Breakthrough Difference</h2>
            <p style="font-size: 1.1rem; line-height: 1.7;">
                Traditional methods rely on <strong>conscious willpower</strong> (which fails 95% of the time). 
                Our method works directly with your <strong>subconscious programming</strong> - where lasting change actually happens.
            </p>
        </div>
        """, unsafe_allow_html=True)

class VideoSection:
    """Video demonstration section"""
    
    def render(self):
        """Render video section with placeholder"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); text-align: center;">
            <h2 style="margin-bottom: 1rem;">See the Method in Action</h2>
            <div style="background: linear-gradient(135deg, var(--accent) 0%, #3B7A7A 100%); 
                        height: 315px; display: flex; align-items: center; justify-content: center; 
                        border-radius: var(--radius-sm); color: white; font-size: 1.1rem;">
                <div>
                    <div style="font-size: 3rem; margin-bottom: 1rem;">▶️</div>
                    <p><strong>Watch:</strong> How Sarah quit smoking in 2 sessions</p>
                    <p style="font-size: 0.9rem; opacity: 0.9;">after 15 years of failed attempts</p>
                </div>
            </div>
            <p style="margin-top: 1rem; color: var(--text-secondary);">
                <em>Real client transformation (with permission)</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

class TwoStepProcess:
    """Detailed explanation of the 2-step process"""
    
    def __init__(self):
        # Try to import image URLs from config
        try:
            from utils.config import AppConstants
            self.behavior_map_img = AppConstants.IMAGES.get("behavior_map", "")
            self.transformation_img = AppConstants.IMAGES.get("transformation", "")
        except ImportError:
            self.behavior_map_img = "https://github.com/pepeette/Hypno/blob/main/img%2FBehaviourMap.png?raw=true"
            self.transformation_img = "https://github.com/pepeette/Hypno/blob/main/img%2Femo.jpg?raw=true"
    
    def render(self):
        """Render the 2-step process explanation"""
        st.markdown("""
        <div style="text-align: center; margin: 3rem 0 2rem 0;">
            <h2>The Proven 2-Step Process</h2>
            <p style="color: var(--text-secondary);">Each session builds on the last for maximum impact</p>
        </div>
        """, unsafe_allow_html=True)
        
        self._render_session_1()
        self._render_session_2()
        self._render_optional_session()
    
    def _render_session_1(self):
        """Render Session 1 details"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border);">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🔍 Deep Analysis Session")
            st.markdown("**90 minutes • In-person or Zoom**")
            st.markdown("")
            
            st.markdown("**What happens:**")
            st.markdown("• Uncover your unique subconscious triggers")
            st.markdown("• Map your personal behavior patterns") 
            st.markdown("• Identify root causes vs. symptoms")
            st.markdown("• Install initial positive programming")
            st.markdown("• You'll feel different immediately")
            
            st.markdown("")
            st.markdown("**Why it works:**")
            st.markdown("We create a detailed map of your subconscious patterns - the *real* reasons you haven't succeeded before.")
        
        with col2:
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="{self.behavior_map_img}" 
                     alt="Behavior Analysis Mapping" 
                     style="width: 100%; max-width: 300px; border-radius: var(--radius-sm); 
                            box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 0.5rem; font-style: italic;">
                    Example: Personal behavior pattern analysis
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_session_2(self):
        """Render Session 2 details"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border);">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="{self.transformation_img}" 
                     alt="Hypnotherapy Transformation Session" 
                     style="width: 100%; max-width: 300px; border-radius: var(--radius-sm); 
                            box-shadow: var(--shadow-sm); border: 1px solid var(--border);">
                <p style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 0.5rem; font-style: italic;">
                    Deep hypnotic state for subconscious rewiring
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="background: var(--accent); width: 60px; height: 60px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; color: white; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### ⚡ Transformation Session")
            st.markdown("**90 minutes • 3-7 days later**")
            st.markdown("")
            
            st.markdown("**What happens:**")
            st.markdown("• Enter deep hypnotic state for maximum receptivity")
            st.markdown("• Rewire neural pathways at the subconscious level")
            st.markdown("• Replace old patterns with empowering new ones")
            st.markdown("• Lock in your new identity and behaviors")
            st.markdown("• Experience profound internal shifts")
            
            st.markdown("")
            st.markdown("**The result:**")
            st.markdown("Most clients report the old desire/urge simply disappears - the craving is gone, not suppressed.")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    def _render_optional_session(self):
        """Render optional 3rd session"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); opacity: 0.8;">
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="background: var(--border); width: 60px; height: 60px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; 
                            font-weight: bold; color: var(--text-secondary); font-size: 1.2rem; margin: 0 auto 1rem;">+1</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🎯 Reinforcement Session")
            st.markdown("**60 minutes • Optional**")
            st.markdown("")
            
            st.markdown("**When needed (only 15% of clients):**")
            st.markdown("• Fine-tune any remaining patterns")
            st.markdown("• Address lingering blocks or triggers")
            st.markdown("• Strengthen and reinforce new behaviors")
            st.markdown("• Complete confidence building")
            
            st.markdown("")
            st.markdown("**Our guarantee:**")
            st.markdown("If you're not completely satisfied after 2 sessions, the 3rd session is complimentary.")
        
        st.markdown("</div>", unsafe_allow_html=True)

class SuccessStatistics:
    """Success statistics section"""
    
    def render(self):
        """Render success statistics"""
        st.markdown("""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 3rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border); text-align: center;">
            <h2 style="color: var(--accent); margin-bottom: 2rem;">Proven Results</h2>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem;">
                <div>
                    <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">85%</div>
                    <p style="margin: 0; font-weight: 600;">Success in 2 sessions</p>
                </div>
                <div>
                    <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">15%</div>
                    <p style="margin: 0; font-weight: 600;">Need 3rd session</p>
                </div>
                <div>
                    <div style="font-size: 2.5rem; font-weight: bold; color: var(--accent);">0%</div>
                    <p style="margin: 0; font-weight: 600;">Require ongoing therapy</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

class ScienceSection:
    """Science behind the method"""
    
    def render(self):
        """Render science explanation"""
        st.markdown("## 🧬 The Science Behind Rapid Change")
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("""
            **Traditional Therapy:**
            - Talks to conscious mind (5% of decisions)
            - Requires ongoing sessions
            - Relies on willpower
            - High relapse rates
            
            **Problem:** You're fighting your own programming
            """)
        
        with col2:
            st.markdown("""
            **Our Hypnotherapy:**
            - Speaks directly to subconscious (95% of decisions)
            - Creates permanent neural rewiring
            - Works with your natural patterns
            - Lasting transformation
            
            **Result:** Your programming now supports your goals
            """)

class PricingSection:
    """Pricing and investment options"""
    
    def __init__(self):
        # Try to import pricing from config
        try:
            from utils.config import AppConstants
            self.complete_package = AppConstants.PRICING.get("complete_package", 3000)
            self.premium_package = AppConstants.PRICING.get("premium_package", 4000)
            self.currency = AppConstants.PRICING.get("currency", "THB")
        except ImportError:
            self.complete_package = 3000
            self.premium_package = 4000
            self.currency = "THB"
    
    def render(self):
        """Render pricing section"""
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: var(--radius-md); 
                    padding: 2rem; margin: 3rem 0; box-shadow: var(--shadow-sm); 
                    border: 1px solid var(--border);">
            <h2 style="text-align: center; margin-bottom: 2rem;">Investment Options</h2>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 280px; padding: 1.5rem; border: 2px solid var(--accent); 
                            border-radius: var(--radius-sm); text-align: center;">
                    <h3 style="color: var(--accent); margin-bottom: 1rem;">Complete Package</h3>
                    <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">{self.complete_package:,} {self.currency}</div>
                    <p style="margin-bottom: 1.5rem;">Sessions 1 & 2 • Most Popular</p>
                    <ul style="text-align: left; margin-bottom: 2rem;">
                        <li>Analysis Session (90 min)</li>
                        <li>Transformation Session (90 min)</li>
                        <li>Email support between sessions</li>
                        <li>Success rate: 85%</li>
                    </ul>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">
                        <em>Compare to: Years of traditional therapy (60,000+ {self.currency})</em>
                    </p>
                </div>
                <div style="flex: 1; min-width: 280px; padding: 1.5rem; border: 1px solid var(--border); 
                            border-radius: var(--radius-sm); text-align: center;">
                    <h3 style="margin-bottom: 1rem;">Premium Package</h3>
