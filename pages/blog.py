"""
Blog/FAQ page component for the Hypnotherapy website
Remodeled for consistency and better content structure
"""
import streamlit as st

class BlogHero:
    """Hero section for blog page using consistent styling"""
    
    def render(self):
        """Render blog hero section"""
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
            <h1 style="color: white; text-shadow: none;">Understanding Your Mind</h1>
        </div>
        """, unsafe_allow_html=True)

        st.write("Discover the science behind rapid transformation and get answers to your most pressing questions about hypnotherapy.")

class BlogArticles:
    """Educational articles section"""
    
    def __init__(self):
        self.articles = [
            {
                "title": "Why your willpower always fails (and what actually works)",
                "summary": "Understanding the 95% vs 5% rule: why conscious effort can't override subconscious programming.",
                "category": "Science",
                "read_time": "3 min read",
                "content": self._get_willpower_content()
            },
            {
                "title": "The real reason habits are so hard to break", 
                "summary": "Neural pathways, emotional triggers, and why your brain resists change - plus how to work with it instead of against it.",
                "category": "Psychology",
                "read_time": "4 min read", 
                "content": self._get_habits_content()
            },
            {
                "title": "What happens in your brain during hypnosis",
                "summary": "Brain wave states, neuroplasticity, and why theta waves are the key to rapid transformation.",
                "category": "Neuroscience", 
                "read_time": "4 min read",
                "content": self._get_brain_content()
            }
        ]
    
    def render(self):
        """Render articles section"""
        st.subheader("Essential reading")
        st.write("The science and psychology behind why hypnotherapy works when other methods don't.")
        
        for article in self.articles:
            self._render_article_card(article)
    
    def _render_article_card(self, article):
        """Render individual article card using Streamlit components"""
        # Article container using info box style for consistency
        with st.container():
            col_meta, col_content = st.columns([1, 4])
            
            with col_meta:
                st.markdown(f"""
                <div style="text-align: center; padding: 1rem;">
                    <div style="background: #4CA1A3; color: white; padding: 0.5rem 1rem; 
                               border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-bottom: 0.5rem;">
                        {article['category']}
                    </div>
                    <div style="color: #556D7A; font-size: 0.85rem;">
                        {article['read_time']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_content:
                st.markdown(f"### {article['title']}")
                st.write(article['summary'])
                
                # Force white background for entire expander
                st.markdown("""
                <style>
                .stExpander {
                    background: white !important;
                    border: 1px solid #CBD5E1 !important;
                    border-radius: 8px !important;
                    margin: 1rem 0 !important;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
                }
                .stExpander > div {
                    background: white !important;
                }
                .stExpander > div > div {
                    background: white !important;
                }
                </style>
                """, unsafe_allow_html=True)
                
                # Expandable full article with white background
                with st.expander(f"read full article", expanded=False):
                    st.markdown(f"""
                    <div style="background: white; padding: 1rem; border-radius: 8px;">
                        {article['content']}
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
    
    def _get_willpower_content(self):
        """Content about willpower limitations"""
        return """
        ## The 5% problem
        
        Here's the uncomfortable truth: your conscious mind - the part that sets new year's resolutions, makes promises, and tries to "just stop" - only controls about 5% of your daily behaviors.
        
        The other 95% runs on autopilot through your subconscious mind. This includes:
        - automatic responses to stress
        - emotional reactions to triggers  
        - habitual behaviors you do without thinking
        - deep-seated beliefs about yourself
        
        ## Why willpower fails
        
        When you try to change using willpower alone, you're asking 5% of your mind to overpower 95%. It's like trying to row upstream against a powerful current - you might make progress for a while, but eventually, you'll get exhausted and swept back.
        
        This is why:
        - diets fail after a few weeks
        - people return to smoking after quitting
        - anxiety comes back despite "knowing better"
        - self-help books don't create lasting change
        
        ## What actually works
        
        Instead of fighting your subconscious, we work with it directly. During hypnosis:
        
        1. **Access the 95%**: we bypass conscious resistance and communicate directly with your subconscious mind
        2. **Identify patterns**: we discover the specific triggers and beliefs driving your unwanted behaviors  
        3. **Install new programming**: we replace old patterns with new ones that support your goals
        4. **Make it automatic**: the change becomes effortless because your subconscious now supports it
        
        When your subconscious and conscious minds are aligned toward the same goal, change becomes natural and permanent.
        
        ## The bottom line
        
        You're not weak for struggling with willpower. You're human. The solution isn't more self-discipline - it's working with your mind the way it's actually designed to function.
        """
    
    def _get_habits_content(self):
        """Content about habit formation and breaking"""
        return """
        ## The habit loop in your brain
        
        Every habit follows the same neurological pattern: Trigger → Routine → Reward. Your brain loves this loop because it's efficient - once established, habits require almost no conscious energy.
        
        But here's the problem: your brain can't distinguish between "good" and "bad" habits. It just sees patterns that have been repeated and reinforced.
        
        ## Why habits feel automatic
        
        When you repeat a behavior enough times, your brain creates a neural pathway - like a well-worn path through a forest. The more you use it, the deeper it becomes.
        
        Eventually, the pathway becomes so established that:
        - The behavior happens before you consciously decide
        - Trying to stop feels like fighting yourself
        - Environmental triggers automatically activate the routine
        - The reward creates craving for the next cycle
        
        ## The hidden emotional layer
        
        Most persistent habits aren't really about the behavior itself - they're meeting an emotional need:
        
        - **Smoking** = instant stress relief, social connection, or identity
        - **Overeating** = comfort, reward, or emotional numbing  
        - **Procrastination** = avoiding fear of failure or judgment
        - **Anxiety patterns** = feeling prepared for danger (even imagined)
        
        ## Why surface-level changes don't stick
        
        Traditional approaches try to change the routine (the behavior) without addressing:
        - The emotional trigger that starts the cycle
        - The underlying need the habit is meeting
        - The subconscious belief system supporting the pattern
        
        This is why people can quit smoking but start stress-eating, or stop one anxiety behavior only to develop another.
        
        ## The hypnotherapy advantage
        
        We don't just interrupt the habit loop - we rewire it at the source:
        
        1. **Find the real trigger**: Often it's an emotion or belief, not just a situation
        2. **Understand the need**: What is this habit really providing?
        3. **Install better patterns**: Give your subconscious healthier ways to meet the same need
        4. **Change the story**: Update the beliefs and identity that support the old habit
        
        When you change the programming that creates the habit, the behavior naturally changes too.
        """
    
    def _get_brain_content(self):
        """Content about brain states during hypnosis"""
        return """
        ## Your brain has different operating modes
        
        Throughout the day, your brain operates in different wave patterns, each associated with different states of consciousness:
        
        - **Beta waves** (normal waking): Logical thinking, problem-solving, conscious control
        - **Alpha waves** (relaxed focus): Meditation, light hypnosis, creative states  
        - **Theta waves** (deep hypnosis): Subconscious access, memory consolidation, profound change
        - **Delta waves** (deep sleep): Physical healing, unconscious processing
        
        ## Why theta is the key
        
        In theta state (4-7 Hz), something remarkable happens:
        - Your conscious mind becomes quiet and receptive
        - Your subconscious mind becomes highly active and open to change
        - Critical thinking and resistance are minimized
        - New neural pathways form more easily
        
        This is the same state you naturally enter when:
        - Deeply absorbed in a movie or book
        - Driving a familiar route on autopilot
        - In that drowsy state just before sleep
        - Having a powerful "aha" moment
        
        ## Neuroplasticity: your brain's superpower
        
        Scientists used to think adult brains were fixed and unchangeable. Now we know the opposite is true - your brain continuously rewires itself based on experience and attention.
        
        Hypnotherapy accelerates this natural process by:
        - **Focused attention**: Directing your brain's rewiring capacity toward specific changes
        - **Reduced interference**: Quieting the conscious mind that often resists change
        - **Emotional engagement**: Creating strong positive associations with new patterns
        - **Repetition and reinforcement**: Strengthening new neural pathways through visualization
        
        ## What happens during a session
        
        **Induction (5-10 minutes)**: Gradual shift from beta to alpha waves through relaxation
        
        **Deepening (5-10 minutes)**: Moving into theta state where real transformation occurs
        
        **Transformation work (60-70 minutes)**: Direct communication with subconscious mind to:
        - Identify and release limiting patterns
        - Install new empowering beliefs and behaviors
        - Create strong positive associations with change
        - Rehearse new responses to old triggers
        
        **Emergence (2-3 minutes)**: Gentle return to normal waking consciousness
        
        ## Why it works so fast
        
        In theta state, one hour of focused subconscious work can accomplish what might take months of conscious effort. You're literally rewiring your brain at the source level, not just trying to override existing patterns with willpower.
        
        The changes feel natural and effortless because they're coming from your subconscious mind - the same part that was maintaining the old patterns.
        """

class FAQ:
    """FAQ section with common questions"""
    
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
        """Render FAQ section"""
        st.subheader("Your questions answered")
        st.write("The most common questions about our hypnotherapy approach and what to expect.")
        
        for faq in self.faqs:
            # Force white background for entire FAQ expanders
            st.markdown("""
            <style>
            .stExpander {
                background: white !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 8px !important;
                margin: 0.5rem 0 !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
            }
            .stExpander > div {
                background: white !important;
            }
            .stExpander > div > div {
                background: white !important;
            }
            </style>
            """, unsafe_allow_html=True)
            
            with st.expander(f"{faq['question']}", expanded=False):
                st.markdown(f"""
                <div style="background: white; padding: 1rem; border-radius: 8px;">
                    {faq['answer']}
                </div>
                """, unsafe_allow_html=True)

class BlogPage:
    """Complete blog page with consistent architecture"""
    
    def __init__(self):
        self.hero = BlogHero()
        self.articles = BlogArticles()
        self.faq = FAQ()
    
    def render(self):
        """Render complete blog page"""
        with st.container():
            self.hero.render()
            st.markdown("    ")
        
        with st.container():
            self.articles.render()
            st.markdown("    ")
        
        with st.container():
            self.faq.render()
            st.markdown("    ")

# Factory function for clean import
def create_blog_page():
    return BlogPage()
