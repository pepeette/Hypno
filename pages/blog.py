# """
# Blog/FAQ page component for the Hypnotherapy website
# Features educational content and frequently asked questions
# """
# import streamlit as st

# class BlogPage:
#     """Blog and FAQ page component"""
    
#     def __init__(self):
#         self.articles = [
#             {
#                 "title": "How Hypnosis Rewires Your Brain for Lasting Change",
#                 "summary": "Discover the neuroscience behind rapid transformation and why hypnotherapy succeeds where willpower fails.",
#                 "content": self._get_article_1_content(),
#                 "date": "August 15, 2025",
#                 "read_time": "5 min read",
#                 "category": "Science"
#             },
#             {
#                 "title": "Breaking Free from Smoking: Why 2 Sessions Work",
#                 "summary": "Learn how John quit his 20-year, 2-pack-a-day habit in just 2 hypnotherapy sessions.",
#                 "content": self._get_article_2_content(),
#                 "date": "August 10, 2025", 
#                 "read_time": "4 min read",
#                 "category": "Case Study"
#             },
#             {
#                 "title": "Anxiety vs. Your Subconscious Mind",
#                 "summary": "Understanding why anxiety persists and how hypnotherapy addresses the root cause.",
#                 "content": self._get_article_3_content(),
#                 "date": "August 5, 2025",
#                 "read_time": "6 min read",
#                 "category": "Mental Health"
#             }
#         ]
        
#         self.faqs = [
#             {
#                 "question": "Is hypnotherapy safe?",
#                 "answer": "Yes, clinical hypnotherapy is completely safe. You remain fully aware and in control throughout the session. Hypnosis is simply a state of focused relaxation that allows access to your subconscious mind for positive change."
#             },
#             {
#                 "question": "How many sessions will I really need?",
#                 "answer": "85% of our clients achieve their goals in just 2 sessions. About 15% choose an optional 3rd session for reinforcement. Unlike traditional therapy, our method creates rapid, lasting change by working directly with your subconscious patterns."
#             },
#             {
#                 "question": "What if I can't be hypnotized?",
#                 "answer": "This is a common myth. Everyone can be hypnotized because hypnosis is a natural state we enter daily (like when driving and arriving without remembering the journey). Our experienced therapist adapts techniques to your unique response style."
#             },
#             {
#                 "question": "Will I lose control during hypnosis?",
#                 "answer": "Absolutely not. You remain fully aware and can open your eyes or speak at any time. Hypnosis is not mind control - it's a collaborative process where you're an active participant in your transformation."
#             },
#             {
#                 "question": "How is this different from other hypnotherapists?",
#                 "answer": "Our method combines advanced analytical techniques in session 1 to map your unique subconscious patterns, followed by targeted transformation in session 2. Most hypnotherapists use generic scripts - we create a personalized approach for each client."
#             },
#             {
#                 "question": "What happens if it doesn't work for me?",
#                 "answer": "We're confident in our method, but if you're not satisfied after 2 sessions, we offer a complimentary 3rd session. Our 85% success rate speaks to the effectiveness of our personalized approach."
#             },
#             {
#                 "question": "Can I do sessions online?",
#                 "answer": "Yes! Online sessions are just as effective as in-person sessions. We use secure video conferencing and have successfully helped clients worldwide achieve their transformation goals remotely."
#             },
#             {
#                 "question": "How much does it cost?",
#                 "answer": "Our complete 2-session package is 3,000 THB. Compare this to years of traditional therapy (often 60,000+ THB) or the ongoing cost of your unwanted habit. Most clients save money within months of their transformation."
#             }
#         ]
    
#     def render(self):
#         """Render the complete blog/FAQ page"""
#         self._render_header()
#         self._render_articles()
#         self._render_faq()
#         self._render_cta()
    
#     def _render_header(self):
#         """Render page header"""
#         st.markdown("""
#         <div style="text-align: center; margin: 2rem 0 3rem 0;">
#             <h1>Hypnotherapy Insights & FAQ</h1>
#             <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
#                 Educational resources and answers to your most common questions
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _render_articles(self):
#         """Render blog articles"""
#         st.markdown("## 📝 Latest Articles")
        
#         for article in self.articles:
#             self._render_article_card(article)
    
#     def _render_article_card(self, article):
#         """Render individual article card"""
#         article_html = f"""
#         <div class="card" style="margin-bottom: 2rem;">
#             <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
#                 <div>
#                     <span class="category-tag">{article['category']}</span>
#                     <span style="color: var(--text-secondary); font-size: 0.9rem; margin-left: 1rem;">
#                         {article['date']} • {article['read_time']}
#                     </span>
#                 </div>
#             </div>
#             <h3 style="color: var(--text-primary); margin-bottom: 1rem; line-height: 1.4;">
#                 {article['title']}
#             </h3>
#             <p style="color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.5rem;">
#                 {article['summary']}
#             </p>
#         </div>
        
#         <style>
#         .category-tag {
#             background: var(--accent);
#             color: white;
#             padding: 0.3rem 0.8rem;
#             border-radius: 20px;
#             font-size: 0.8rem;
#             font-weight: 600;
#         }
#         </style>
#         """
        
#         st.markdown(article_html, unsafe_allow_html=True)
        
#         # Expandable article content
#         with st.expander(f"📖 Read Full Article: {article['title']}", expanded=False):
#             st.markdown(article['content'])
    
#     def _render_faq(self):
#         """Render FAQ section"""
#         st.markdown("""
#         <div style="margin: 4rem 0 2rem 0;">
#             <h2>❓ Frequently Asked Questions</h2>
#             <p style="color: var(--text-secondary); margin-bottom: 2rem;">
#                 Get answers to the most common questions about our hypnotherapy method
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         for faq in self.faqs:
#             self._render_faq_item(faq)
    
#     def _render_faq_item(self, faq):
#         """Render individual FAQ item"""
#         with st.expander(f"❓ {faq['question']}", expanded=False):
#             st.markdown(faq['answer'])
    
#     def _render_cta(self):
#         """Render call-to-action"""
#         st.markdown("""
#         <div style="background: var(--card-bg); border-radius: var(--radius-md);
#                     padding: 3rem 2rem; text-align: center; margin: 4rem 0;
#                     border: 1px solid var(--border); box-shadow: var(--shadow-sm);">
#             <h2 style="color: var(--accent); margin-bottom: 1rem;">
#                 Still Have Questions?
#             </h2>
#             <p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 2rem;">
#                 Get personalized answers in a free 15-minute discovery call
#             </p>
#             <a href="#discovery" class="btn btn-primary" style="text-decoration: none;">
#                 📞 Book Free Discovery Call
#             </a>
#         </div>
#         """, unsafe_allow_html=True)
    
#     def _get_article_1_content(self):
#         """Content for neuroscience article"""
#         return """
#         ## The Neuroscience of Rapid Transformation
        
#         **Why Traditional Methods Fall Short**
        
#         Most people try to change using their conscious mind - the part that makes decisions, sets goals, and uses willpower. But here's the problem: your conscious mind only controls about 5% of your daily decisions and behaviors.
        
#         The other 95% is controlled by your subconscious mind, which operates on autopilot using established neural patterns. This is why willpower alone fails - you're trying to overpower your subconscious programming with just 5% of your mental capacity.
        
#         **How Hypnotherapy Creates Lasting Change**
        
#         Hypnotherapy works by accessing the subconscious mind directly. During the hypnotic state, your brain waves shift from beta (normal waking consciousness) to alpha and theta states, where the subconscious becomes highly receptive to positive suggestions and new programming.
        
#         **The Two-Session Method**
        
#         **Session 1: Mapping Your Neural Patterns**
#         - We identify the specific subconscious triggers and patterns driving your unwanted behavior
#         - This creates a detailed "map" of your unique psychological landscape
#         - Initial positive programming begins, providing immediate relief
        
#         **Session 2: Neural Rewiring**
#         - Deep hypnotic state allows direct communication with your subconscious
#         - Old neural pathways are "interrupted" and new, positive pathways are established
#         - Your brain literally rewires itself to support your desired behaviors
        
#         **The Science Behind the Success**
        
#         Recent neuroscience research shows that the brain has remarkable plasticity - the ability to form new neural connections throughout life. Hypnotherapy accelerates this process by:
        
#         1. **Bypassing Critical Factors**: The conscious mind's resistance is minimized
#         2. **Enhancing Neuroplasticity**: Theta brain waves promote rapid neural rewiring
#         3. **Installing New Programs**: Positive suggestions become new subconscious patterns
#         4. **Creating Identity Shifts**: You don't just change behavior, you become someone who naturally embodies the change
        
#         This is why our clients often report that their old cravings or compulsions simply disappear - we've changed the underlying programming that created them.
#         """
    
#     def _get_article_2_content(self):
#         """Content for smoking cessation case study"""
#         return """
#         ## John's Transformation: From 2 Packs a Day to Smoke-Free
        
#         **The Challenge**
        
#         John, a 45-year-old executive, had been smoking for 20 years. What started as a social habit in college had escalated to 2 packs a day - 40 cigarettes consuming his life and health.
        
#         **Previous Failed Attempts**
#         - Nicotine patches (lasted 3 weeks)
#         - Prescription medications (side effects too severe)
#         - Cold turkey (made it 5 days)
#         - Vaping (just switched addictions)
#         - Traditional counseling (18 months, minimal progress)
        
#         **The Breakthrough Approach**
        
#         **Session 1: Understanding the Real Triggers**
        
#         Through our analytical process, we discovered John's smoking wasn't really about nicotine addiction. The deeper triggers were:
#         - Stress response from childhood (smoking = instant calm)
#         - Identity ("I'm a smoker" was part of his self-image)
#         - Social anxiety in business meetings
#         - Reward system (cigarette = accomplishment celebration)
        
#         **Session 2: Subconscious Rewiring**
        
#         Using targeted hypnotherapy, we:
#         - Installed new stress response patterns (deep breathing instead of smoking)
#         - Shifted his identity to "I'm someone who values health and freedom"
#         - Created new social confidence anchors
#         - Rewired his reward system to healthy alternatives
        
#         **The Results**
        
#         **Immediate (Day 1)**: John threw away his remaining cigarettes without struggle
#         **Week 1**: No cravings, increased energy, better sleep
#         **Month 1**: Saved 4,000 THB, improved breathing, white teeth returning
#         **6 Months Later**: Still completely smoke-free, saved 24,000 THB, ran his first 5K
        
#         **John's Words:**
        
#         *"I've tried everything to quit smoking. The difference with hypnotherapy was that I didn't have to 'fight' anything. The desire to smoke just... disappeared. It's like waking up one day and realizing you're a completely different person - someone who would never choose to smoke."*
        
#         **Why It Worked**
        
#         John's success came from addressing the subconscious programming that maintained his smoking habit, rather than trying to overpower it with willpower. We didn't just help him quit smoking - we helped him become someone who naturally chooses health.
        
#         **Your Transformation Awaits**
        
#         John's story isn't unique. Every week, we help people break free from habits that have controlled them for years. The key is working with your subconscious mind, not against it.
#         """
    
#     def _get_article_3_content(self):
#         """Content for anxiety article"""
#         return """
#         ## Understanding Anxiety: Why It Persists and How to Overcome It
        
#         **The Anxiety Epidemic**
        
#         Anxiety affects millions worldwide, yet traditional treatments often provide only temporary relief. To understand why, we need to look at what anxiety really is - and where it comes from.
        
#         **The Subconscious Origin of Anxiety**
        
#         Most anxiety isn't rational. You know logically that the presentation won't kill you, that the flight is statistically safe, that social rejection isn't life-threatening. But knowing this doesn't stop the racing heart, sweaty palms, or overwhelming dread.
        
#         That's because anxiety originates in your subconscious mind, which operates on emotion and learned patterns, not logic.
        
#         **How Anxiety Patterns Form**
        
#         Your subconscious mind's primary job is to keep you safe. Sometimes, it learns that certain situations are "dangerous" based on:
#         - Past traumatic experiences
#         - Learned behaviors from family
#         - Societal programming
#         - Misinterpreted events
        
#         Once these patterns are established, your subconscious triggers the fight-or-flight response whenever it perceives these "threats," even if they're not actually dangerous.
        
#         **Why Traditional Methods Often Fall Short**
        
#         **Cognitive Behavioral Therapy (CBT)**: Works with conscious thoughts but doesn't address subconscious programming
#         **Medication**: Manages symptoms but doesn't resolve underlying patterns
#         **Exposure Therapy**: Can work but often reinforces fear if not done properly
#         **Breathing Techniques**: Helpful for management but doesn't eliminate root causes
        
#         **The Hypnotherapy Advantage**
        
#         Hypnotherapy accesses the subconscious mind where anxiety patterns are stored. Instead of managing symptoms, we:
        
#         1. **Identify Root Causes**: Discover the original events or beliefs that created anxiety patterns
#         2. **Reframe Past Events**: Help your subconscious reinterpret past experiences as non-threatening
#         3. **Install New Responses**: Replace anxiety responses with calm, confident reactions
#         4. **Build Inner Resources**: Strengthen your natural resilience and coping abilities
        
#         **Sarah's Anxiety Transformation**
        
#         Sarah, a successful marketing director, suffered from crippling social anxiety that was affecting her career. Despite her professional success, she would panic before presentations and avoid networking events.
        
#         **Session 1 Revealed**: Her anxiety stemmed from a childhood experience of being humiliated in front of her class. Her subconscious had generalized this to mean "being seen = danger."
        
#         **Session 2 Resolved**: We helped her subconscious reframe that childhood experience and install new patterns of confidence and ease in social situations.
        
#         **Result**: Sarah now gives presentations confidently and actually enjoys networking events. She was promoted within 3 months of her sessions.
        
#         **The Calm Mind Is Your Natural State**
        
#         Anxiety isn't your natural state - calm confidence is. When we remove the subconscious programming that creates anxiety, your natural state of wellbeing emerges.
        
#         **Take the First Step**
        
#         If anxiety has been controlling your life, remember that it's not a character flaw or permanent condition. It's simply learned programming that can be changed. The question isn't whether you can overcome anxiety - it's how quickly you want to reclaim your natural state of calm confidence.
#         """


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
                "title": "Why Your Willpower Always Fails (And What Actually Works)",
                "summary": "Understanding the 95% vs 5% rule: why conscious effort can't override subconscious programming.",
                "category": "Science",
                "read_time": "3 min read",
                "content": self._get_willpower_content()
            },
            {
                "title": "The Real Reason Habits Are So Hard to Break", 
                "summary": "Neural pathways, emotional triggers, and why your brain resists change - plus how to work with it instead of against it.",
                "category": "Psychology",
                "read_time": "4 min read", 
                "content": self._get_habits_content()
            },
            {
                "title": "What Happens in Your Brain During Hypnosis",
                "summary": "Brain wave states, neuroplasticity, and why theta waves are the key to rapid transformation.",
                "category": "Neuroscience", 
                "read_time": "4 min read",
                "content": self._get_brain_content()
            }
        ]
    
    def render(self):
        """Render articles section"""
        st.subheader("Essential Reading")
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
                
                # Expandable full article
                with st.expander(f"Read Full Article", expanded=False):
                    st.markdown(article['content'])
            
            st.markdown("---")
    
    def _get_willpower_content(self):
        """Content about willpower limitations"""
        return """
        ## The 5% Problem
        
        Here's the uncomfortable truth: your conscious mind - the part that sets New Year's resolutions, makes promises, and tries to "just stop" - only controls about 5% of your daily behaviors.
        
        The other 95% runs on autopilot through your subconscious mind. This includes:
        - Automatic responses to stress
        - Emotional reactions to triggers  
        - Habitual behaviors you do without thinking
        - Deep-seated beliefs about yourself
        
        ## Why Willpower Fails
        
        When you try to change using willpower alone, you're asking 5% of your mind to overpower 95%. It's like trying to row upstream against a powerful current - you might make progress for a while, but eventually, you'll get exhausted and swept back.
        
        This is why:
        - Diets fail after a few weeks
        - People return to smoking after quitting
        - Anxiety comes back despite "knowing better"
        - Self-help books don't create lasting change
        
        ## What Actually Works
        
        Instead of fighting your subconscious, we work with it directly. During hypnosis:
        
        1. **Access the 95%**: We bypass conscious resistance and communicate directly with your subconscious mind
        2. **Identify patterns**: We discover the specific triggers and beliefs driving your unwanted behaviors  
        3. **Install new programming**: We replace old patterns with new ones that support your goals
        4. **Make it automatic**: The change becomes effortless because your subconscious now supports it
        
        When your subconscious and conscious minds are aligned toward the same goal, change becomes natural and permanent.
        
        ## The Bottom Line
        
        You're not weak for struggling with willpower. You're human. The solution isn't more self-discipline - it's working with your mind the way it's actually designed to function.
        """
    
    def _get_habits_content(self):
        """Content about habit formation and breaking"""
        return """
        ## The Habit Loop in Your Brain
        
        Every habit follows the same neurological pattern: Trigger → Routine → Reward. Your brain loves this loop because it's efficient - once established, habits require almost no conscious energy.
        
        But here's the problem: your brain can't distinguish between "good" and "bad" habits. It just sees patterns that have been repeated and reinforced.
        
        ## Why Habits Feel Automatic
        
        When you repeat a behavior enough times, your brain creates a neural pathway - like a well-worn path through a forest. The more you use it, the deeper it becomes.
        
        Eventually, the pathway becomes so established that:
        - The behavior happens before you consciously decide
        - Trying to stop feels like fighting yourself
        - Environmental triggers automatically activate the routine
        - The reward creates craving for the next cycle
        
        ## The Hidden Emotional Layer
        
        Most persistent habits aren't really about the behavior itself - they're meeting an emotional need:
        
        - **Smoking** = instant stress relief, social connection, or identity
        - **Overeating** = comfort, reward, or emotional numbing  
        - **Procrastination** = avoiding fear of failure or judgment
        - **Anxiety patterns** = feeling prepared for danger (even imagined)
        
        ## Why Surface-Level Changes Don't Stick
        
        Traditional approaches try to change the routine (the behavior) without addressing:
        - The emotional trigger that starts the cycle
        - The underlying need the habit is meeting
        - The subconscious belief system supporting the pattern
        
        This is why people can quit smoking but start stress-eating, or stop one anxiety behavior only to develop another.
        
        ## The Hypnotherapy Advantage
        
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
        ## Your Brain Has Different Operating Modes
        
        Throughout the day, your brain operates in different wave patterns, each associated with different states of consciousness:
        
        - **Beta waves** (normal waking): Logical thinking, problem-solving, conscious control
        - **Alpha waves** (relaxed focus): Meditation, light hypnosis, creative states  
        - **Theta waves** (deep hypnosis): Subconscious access, memory consolidation, profound change
        - **Delta waves** (deep sleep): Physical healing, unconscious processing
        
        ## Why Theta is the Key
        
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
        
        ## Neuroplasticity: Your Brain's Superpower
        
        Scientists used to think adult brains were fixed and unchangeable. Now we know the opposite is true - your brain continuously rewires itself based on experience and attention.
        
        Hypnotherapy accelerates this natural process by:
        - **Focused attention**: Directing your brain's rewiring capacity toward specific changes
        - **Reduced interference**: Quieting the conscious mind that often resists change
        - **Emotional engagement**: Creating strong positive associations with new patterns
        - **Repetition and reinforcement**: Strengthening new neural pathways through visualization
        
        ## What Happens During a Session
        
        **Induction (5-10 minutes)**: Gradual shift from beta to alpha waves through relaxation
        
        **Deepening (5-10 minutes)**: Moving into theta state where real transformation occurs
        
        **Transformation work (60-70 minutes)**: Direct communication with subconscious mind to:
        - Identify and release limiting patterns
        - Install new empowering beliefs and behaviors
        - Create strong positive associations with change
        - Rehearse new responses to old triggers
        
        **Emergence (2-3 minutes)**: Gentle return to normal waking consciousness
        
        ## Why It Works So Fast
        
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
        st.subheader("Your Questions Answered")
        st.write("The most common questions about our hypnotherapy approach and what to expect.")
        
        for faq in self.faqs:
            with st.expander(f"{faq['question']}", expanded=False):
                st.write(faq['answer'])

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
