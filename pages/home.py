# """
# Complete Home page with enhanced 4-question quiz built-in
# Hero → Quiz → Method Teaser → CTA
# """
# import streamlit as st

# class HeroSection:
#     """Hero section with value proposition and comparison"""
    
#     def render(self):
#         """Render hero section with comparison"""
#         with st.container():
#             # Hero banner image
#             st.markdown("""
#             <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
#                 <img src="https://raw.githubusercontent.com/pepeette/Hypno/main/img/herobanner.jpg" 
#                      alt="Stop Fighting Your Mind. Start Working With It." 
#                      style="max-width: 100%; height: auto; border-radius: 16px;">
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Key message and value proposition
#             st.write("Most people try to change using willpower. That's why 95% fail. We bypass your conscious resistance and reprogram your subconscious patterns directly.")
            
#             st.write("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")
            
#             st.info("→ Book your hypnotherapy at our new address in Bangkok to break free from unwanted habits. 2 sessions only needed.")

#             # Value proposition with comparison
#             st.markdown("## Transform in 2 sessions what takes traditional therapy longer")
            
#             # 3-column comparison
#             col1, col2, col3 = st.columns([1, 1, 1])
            
#             with col1:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; margin: 1rem 0; border-left: 4px solid #ef4444; height: 100%;">
#                     <h2 style="color: #dc2626; margin-bottom: 1rem; text-align: center;">❌ Traditional Methods</h2>
#                     <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
#                     <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
#                     <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
#                     <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
#                     <p style="margin: 0; font-weight: 600; color: #dc2626; text-align: center;">
#                         Result: You know what to do but can't consistently do it
#                     </p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             margin: 1rem 0; height: 100%; padding: 0; overflow: hidden;
#                             display: flex; align-items: center; justify-content: center;">
#                     <img src="https://github.com/pepeette/Hypno/blob/main/img/Hypnotherapy_compa.jpg?raw=true" 
#                          alt="Hypnotherapy Comparison" 
#                          style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; margin: 1rem 0; border-left: 4px solid #22c55e; height: 100%;">
#                     <h2 style="color: #16a34a; margin-bottom: 1rem; text-align: center;">✅ Hypnotherapy</h2>
#                     <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
#                     <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
#                     <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
#                     <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
#                     <p style="margin: 0; font-weight: 600; color: #16a34a; text-align: center;">
#                         Result: Your subconscious now supports your goals automatically
#                     </p>
#                 </div>
#                 """, unsafe_allow_html=True)

# class EnhancedQuizSection:
#     """Complete 4-question quiz with proper styling and blocking mechanisms"""
    
#     def __init__(self):
#         # Initialize session state for quiz
#         if 'quiz_answers' not in st.session_state:
#             st.session_state.quiz_answers = {}
#         if 'quiz_step' not in st.session_state:
#             st.session_state.quiz_step = 1
#         if 'quiz_completed' not in st.session_state:
#             st.session_state.quiz_completed = False
#         if 'quiz_score' not in st.session_state:
#             st.session_state.quiz_score = 0
#         if 'unwanted_pattern' not in st.session_state:
#             st.session_state.unwanted_pattern = ""
#         if 'pattern_duration' not in st.session_state:
#             st.session_state.pattern_duration = ""
#         if 'blocking_mechanism' not in st.session_state:
#             st.session_state.blocking_mechanism = ""
#         if 'readiness_level' not in st.session_state:
#             st.session_state.readiness_level = ""
        
#         # Discovery URL
#         self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
    
#     def render(self):
#         """Render the complete quiz experience"""
#         st.subheader("Test: Are you ready for your rapid change with hypnotherapy?")
#         st.write("4 questions to assess if our method is right for your situation:")
        
#         if not st.session_state.quiz_completed:
#             self._render_all_questions()
#         else:
#             self._render_quiz_results()
    
#     def _render_all_questions(self):
#         """Show all 4 questions with proper progression"""
#         current_step = st.session_state.quiz_step
        
#         # Question 1 - Unwanted pattern
#         q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
#         with st.expander("Question 1: What unwanted pattern would you most like to eliminate?", expanded=q1_expanded):
#             if 1 not in st.session_state.quiz_answers:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("🚭 Quit smoking\nBreak nicotine addiction permanently", key="q1_smoking", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Quit smoking")
#                     if st.button("😰 Reduce anxiety\nStop panic attacks and overthinking", key="q1_anxiety", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Reduce anxiety")
#                     if st.button("🍷 Control drinking\nHealthy relationship with alcohol", key="q1_drinking", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Control drinking")
#                 with col2:
#                     if st.button("😴 Improve sleep\nEnd insomnia and sleep anxiety", key="q1_sleep", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Improve sleep")
#                     if st.button("🍕 Stop overeating\nBreak emotional eating patterns", key="q1_eating", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Stop overeating")
#                     if st.button("📱 Break bad habits\nEliminate destructive behaviors", key="q1_habits", use_container_width=True, type="secondary"):
#                         self._answer_question(1, "Break bad habits")
#             else:
#                 st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
#         # Question 2 - Duration
#         if len(st.session_state.quiz_answers) >= 1:
#             q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
#             with st.expander("Question 2: How long have you been dealing with this pattern?", expanded=q2_expanded):
#                 if 2 not in st.session_state.quiz_answers:
#                     if st.button("🆕 Less than 6 months - Recent development", key="q2_recent", use_container_width=True, type="secondary"):
#                         self._answer_question(2, "Less than 6 months")
#                     if st.button("📅 6 months to 2 years - Established pattern", key="q2_established", use_container_width=True, type="secondary"):
#                         self._answer_question(2, "6 months to 2 years")
#                     if st.button("⏳ More than 2 years - Deep-rooted habit", key="q2_deeprooted", use_container_width=True, type="secondary"):
#                         self._answer_question(2, "More than 2 years")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
#         # Question 3 - Blocking mechanism
#         if len(st.session_state.quiz_answers) >= 2:
#             q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
#             with st.expander("Question 3: Which internal pattern most blocks your progress?", expanded=q3_expanded):
#                 if 3 not in st.session_state.quiz_answers:
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         if st.button("⚔️ Force and control\n'I must push through resistance'", key="q3_force", use_container_width=True, type="secondary"):
#                             self._answer_question(3, "Force and control")
#                         if st.button("🔒 Mistrust and defensiveness\n'I can't let my guard down'", key="q3_mistrust", use_container_width=True, type="secondary"):
#                             self._answer_question(3, "Mistrust and defensiveness")
#                     with col2:
#                         if st.button("⚖️ All-or-nothing thinking\n'It's either perfect or failure'", key="q3_binary", use_container_width=True, type="secondary"):
#                             self._answer_question(3, "All-or-nothing thinking")
#                         if st.button("🏃 Doing addiction\n'My worth depends on productivity'", key="q3_doing", use_container_width=True, type="secondary"):
#                             self._answer_question(3, "Doing addiction")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
#         # Question 4 - Readiness
#         if len(st.session_state.quiz_answers) >= 3:
#             q4_expanded = (current_step == 4) and (4 not in st.session_state.quiz_answers)
#             with st.expander("Question 4: How ready are you to transform this pattern?", expanded=q4_expanded):
#                 if 4 not in st.session_state.quiz_answers:
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         if st.button("🤔 Curious but cautious\nWant to understand the approach first", key="q4_curious", use_container_width=True, type="secondary"):
#                             self._answer_question(4, "Curious but cautious")
#                         if st.button("🎯 Ready to commit\nPrepared to do the inner work", key="q4_ready", use_container_width=True, type="secondary"):
#                             self._answer_question(4, "Ready to commit")
#                     with col2:
#                         if st.button("🔥 Desperate for change\nThis pattern must end now", key="q4_desperate", use_container_width=True, type="secondary"):
#                             self._answer_question(4, "Desperate for change")
#                         if st.button("🛡️ Prefer gradual approach\nWant to try other methods first", key="q4_gradual", use_container_width=True, type="secondary"):
#                             self._answer_question(4, "Prefer gradual approach")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[4]}")
        
#         # Progress indicator
#         progress = len(st.session_state.quiz_answers) / 4
#         if progress > 0:
#             st.progress(progress)
#             if progress < 1:
#                 st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 4")
#             else:
#                 st.caption("Assessment complete!")
    
#     def _answer_question(self, question_id, answer):
#         """Handle question answers and store patterns"""
#         st.session_state.quiz_answers[question_id] = answer
        
#         # Store specific patterns for results
#         if question_id == 1:
#             st.session_state.unwanted_pattern = answer
#         elif question_id == 2:
#             st.session_state.pattern_duration = answer
#         elif question_id == 3:
#             st.session_state.blocking_mechanism = answer
#         elif question_id == 4:
#             st.session_state.readiness_level = answer
        
#         # Progress through quiz
#         if question_id < 4:
#             st.session_state.quiz_step = question_id + 1
#         else:
#             st.session_state.quiz_completed = True
#             st.session_state.quiz_score = self._calculate_score()
#         st.rerun()
    
#     def _calculate_score(self):
#         """Calculate transformation readiness score"""
#         scoring = {
#             1: {  # Unwanted patterns
#                 "Quit smoking": 30,
#                 "Reduce anxiety": 25,
#                 "Improve sleep": 20,
#                 "Control drinking": 25,
#                 "Stop overeating": 20,
#                 "Break bad habits": 25
#             },
#             2: {  # Duration
#                 "Less than 6 months": 15,
#                 "6 months to 2 years": 20,
#                 "More than 2 years": 25
#             },
#             3: {  # Blocking mechanisms
#                 "Force and control": 20,
#                 "Mistrust and defensiveness": 15,
#                 "All-or-nothing thinking": 25,
#                 "Doing addiction": 30
#             },
#             4: {  # Readiness levels
#                 "Curious but cautious": 15,
#                 "Ready to commit": 30,
#                 "Desperate for change": 25,
#                 "Prefer gradual approach": 5
#             }
#         }
        
#         total_score = 0
#         for q_id, answer in st.session_state.quiz_answers.items():
#             if q_id in scoring and answer in scoring[q_id]:
#                 total_score += scoring[q_id][answer]
        
#         return min(total_score, 100)
    
#     def _render_quiz_results(self):
#         """Render results using Streamlit components with proper styling"""
#         score = st.session_state.quiz_score
        
#         # Results header
#         st.success("✅ Assessment Complete!")
        
#         # Results based on score with proper styling
#         if score >= 75:
#             st.success("🌟 High suitability for rapid transformation!")
#             recommendation = "You show strong indicators for success with our 2-session method."
#             action = "Book your transformation package or start with a discovery call."
#         elif score >= 55:
#             st.warning("🎯 Good potential for transformation!")
#             recommendation = "You have solid foundations for change with proper support."
#             action = "A discovery call will help us tailor the approach to your situation."
#         elif score >= 35:
#             st.info("💭 Assessment recommended")
#             recommendation = "Your situation would benefit from personalized evaluation."
#             action = "A free discovery call will determine the best path forward."
#         else:
#             st.info("🌱 Preparation phase suggested")
#             recommendation = "Building readiness first may optimize your success."
#             action = "Let's discuss your situation and explore when you might be ready."
        
#         # Display metrics using Streamlit components
#         col1, col2 = st.columns(2)
#         with col1:
#             st.metric("Transformation Readiness", f"{score}%", "Suitability Score")
#         with col2:
#             st.metric("Focus Area", st.session_state.unwanted_pattern, "Primary Pattern")
        
#         # Pattern insights using clean text
#         pattern_insights = {
#             "Quit smoking": "Smoking is one of our highest success areas. Most clients become smoke-free after 2 sessions.",
#             "Reduce anxiety": "Anxiety responds well to subconscious pattern work. We address root triggers, not just symptoms.",
#             "Improve sleep": "Sleep issues often stem from subconscious stress patterns we can identify and resolve.",
#             "Control drinking": "Drinking patterns usually have deeper emotional triggers that hypnotherapy addresses effectively.",
#             "Stop overeating": "Emotional eating involves subconscious reward patterns that respond well to our method.",
#             "Break bad habits": "Most habits run on autopilot from the subconscious - exactly where we work."
#         }
        
#         mechanism_insights = {
#             "Force and control": "You tend to use force when resistance appears, creating internal battles. Our method works with your mind, not against it.",
#             "Mistrust and defensiveness": "Your security system stays hyperactive, treating change as danger. We create safety for transformation.",
#             "All-or-nothing thinking": "Your mind categorizes everything as perfect or failure. We help you find the middle ground where growth happens.",
#             "Doing addiction": "Your worth feels tied to productivity. We help you find value in being, not just doing."
#         }
        
#         # Display insights using standard Streamlit components
#         if st.session_state.unwanted_pattern in pattern_insights:
#             st.write(f"**Your pattern:** {pattern_insights[st.session_state.unwanted_pattern]}")
            
#         if st.session_state.blocking_mechanism in mechanism_insights:
#             st.write(f"**Your approach:** {mechanism_insights[st.session_state.blocking_mechanism]}")
        
#         # Recommendation and action using info box
#         st.info(f"**Recommendation:** {recommendation}")
#         st.write(f"**Next step:** {action}")
        
#         # Action buttons using proper styling
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown(f"""
#                 <a href="{self.discovery_url}" 
#                    target="_blank" 
#                    class="cta-button">
#                    📞 Book Discovery Call
#                 </a>
#                 """, unsafe_allow_html=True)
#         with col2:
#             if st.button("🔄 Retake Assessment", use_container_width=True, type="secondary"):
#                 self._reset_quiz()
    
#     def _reset_quiz(self):
#         """Reset all quiz state"""
#         st.session_state.quiz_answers = {}
#         st.session_state.quiz_step = 1
#         st.session_state.quiz_completed = False
#         st.session_state.quiz_score = 0
#         st.session_state.unwanted_pattern = ""
#         st.session_state.pattern_duration = ""
#         st.session_state.blocking_mechanism = ""
#         st.session_state.readiness_level = ""
#         st.rerun()
        
# class MethodTeaserWithVideo:
#     """Method overview with video and link to method page"""
    
#     def render(self):
#         """Render method teaser"""
#         st.subheader("Why hypnotherapy succeeds where others haven't")
        
#         # Video and explanation side by side
#         col1, col2 = st.columns([1, 2])
        
#         with col1:
#             st.video("https://youtu.be/5ORz1-LWrjo?feature=shared")
        
#         with col2:
#             st.write("""
#             **The problem:** Your conscious mind (5% of decisions) fights your subconscious programming (95% of decisions). 
#             The subconscious always wins.
#             """)
            
#             st.write("""
#             **Our breakthrough:** Instead of fighting your subconscious, we work directly with it. 
#             We identify your specific patterns and rewire them at the source.
#             """)
            
#             st.info("When your subconscious programming supports your goals instead of fighting them, change becomes effortless and permanent.")
        
#         # Call to action for method page
#         st.markdown("---")
        
#         col1, col2 = st.columns([3, 1])
        
#         with col1:
#             st.write("**Want to understand the complete neuroscience behind our method?** ")
#             st.write("See the detailed breakdown of how neuroplasticity creates lasting change, brain wave states, and clinical evidence.")
        
#         with col2:
#             st.markdown("""
#                 <a href="https://hypnotherapy.streamlit.app/#deep-pattern-analysis" 
#                    target="_blank" 
#                    class="cta-button">
#                    👉 swipe to 2+1 Method page
#                 </a>
#                 """, unsafe_allow_html=True)

# class HomePage:
#     """Complete home page with integrated 4-question quiz"""
    
#     def __init__(self):
#         self.hero = HeroSection()
#         self.quiz = EnhancedQuizSection()
#         self.method_teaser = MethodTeaserWithVideo()
    
#     def render(self):
#         """Render complete home page"""
#         # Hero - value proposition and comparison
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
        
#         # Quiz - 4-question assessment with blocking mechanisms
#         with st.container():
#             self.quiz.render()
#             st.markdown("    ")
        
#         # Method teaser - credibility and next steps
#         with st.container():
#             self.method_teaser.render()
#             st.markdown("    ")

# # Factory function for clean import
# def create_home_page():
#     return HomePage()




import streamlit as st

class HeroSection:
    """Hero section with value proposition and comparison"""
    
    def render(self):
        """Render hero section with comparison"""
        with st.container():
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
                <img src="https://raw.githubusercontent.com/pepeette/Hypno/main/img/herobanner.jpg" 
                     alt="Stop Fighting Your Mind. Start Working With It." 
                     style="max-width: 100%; height: auto; border-radius: 16px;">
            </div>
            """, unsafe_allow_html=True)
            
            st.write("Most people try to change using willpower. That's why 95% fail. We bypass your conscious resistance and reprogram your subconscious patterns directly.")
            
            st.write("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")
            
            st.info("→ Book your hypnotherapy at our new address in Bangkok to break free from unwanted habits. 2 sessions only needed.")
            
            st.markdown("## Transform in 2 sessions what takes traditional therapy longer")
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; margin: 1rem 0; border-left: 4px solid #ef4444; height: 100%;">
                    <h2 style="color: #dc2626; margin-bottom: 1rem; text-align: center;">❌ Traditional Methods</h2>
                    <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
                    <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
                    <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
                    <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
                    <p style="margin: 0; font-weight: 600; color: #dc2626; text-align: center;">
                        Result: You know what to do but can't consistently do it
                    </p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            margin: 1rem 0; height: 100%; padding: 0; overflow: hidden;
                            display: flex; align-items: center; justify-content: center;">
                    <img src="https://github.com/pepeette/Hypno/blob/main/img/Hypnotherapy_compa.jpg?raw=true" 
                         alt="Hypnotherapy Comparison" 
                         style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; margin: 1rem 0; border-left: 4px solid #22c55e; height: 100%;">
                    <h2 style="color: #16a34a; margin-bottom: 1rem; text-align: center;">✅ Hypnotherapy</h2>
                    <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
                    <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
                    <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
                    <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
                    <p style="margin: 0; font-weight: 600; color: #16a34a; text-align: center;">
                        Result: Your subconscious now supports your goals automatically
                    </p>
                </div>
                """, unsafe_allow_html=True)

class EnhancedQuizSection:
    def __init__(self):
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        if 'quiz_step' not in st.session_state:
            st.session_state.quiz_step = 1
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0

        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"

    def render(self):
        st.subheader("30-second self-assessment: is hypnotherapy right for you?")
        st.write("quickly assess if hypnotherapy can help you transform emotional patterns and subconscious blocks.")

        if not st.session_state.quiz_completed:
            self._render_all_questions()
        else:
            self._render_quiz_results()

    def _render_all_questions(self):
        current_step = st.session_state.quiz_step

        # question 1 (two-column layout, as before)
        q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
        with st.expander("question 1: which issue most interferes with your daily wellbeing?", expanded=q1_expanded):
            if 1 not in st.session_state.quiz_answers:
                col1, col2 = st.columns(2)
                choices = [
                    ("😰 chronic stress or anxiety limiting peace and calm", "chronic stress or anxiety"),
                    ("🔄 repetitive negative habits or addictions (including smoking)", "repetitive negative habits or addictions"),
                    ("⚡ heightened emotional reactivity blocking focus", "heightened emotional reactivity"),
                    ("🤔 persistent self-doubt undermining confidence", "persistent self-doubt"),
                    ("⏳ procrastination and difficulty initiating actions", "procrastination"),
                    ("🌀 vertigo or physical discomfort disrupting daily life", "vertigo or physical discomfort"),
                    ("🚭 want to quit smoking/permanent nicotine addiction break", "quit smoking"),
                    ("😞 feelings of overwhelm or stuckness", "feeling stuck or overwhelmed"),
                ]
                half = len(choices) // 2
                for i, (label, value) in enumerate(choices):
                    container = col1 if i < half else col2
                    container.button(
                        label,
                        key=f"q1_{i}",
                        use_container_width=True,
                        type="secondary",
                        on_click=self._answer_question,
                        args=(1, value)
                    )
            else:
                st.success(f"✅ selected: {st.session_state.quiz_answers[1]}")
                st.info("these issues often have subconscious triggers hypnotherapy can effectively address.")

        # expert expanded question 2: broader relatable triggers, two columns, button single click
        if len(st.session_state.quiz_answers) >= 1:
            q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
            with st.expander("question 2: which inner experience or mindset most often keeps you from lasting change?", expanded=q2_expanded):
                if 2 not in st.session_state.quiz_answers:
                    col1, col2 = st.columns(2)
                    q2_choices = [
                        ("⚔️ trying to force change through sheer willpower, leaving you exhausted", "force and control"),
                        ("🔒 feeling unsafe or guarded, finding it hard to trust change or others", "defensive mistrust"),
                        ("⚖️ viewing things in black and white: perfectionism or all-or-nothing", "all-or-nothing thinking"),
                        ("🏃 driven to constantly prove worth by doing, often leading to burnout", "doing addiction"),
                        ("🗣 persistent self-critical thoughts that undermine confidence", "self-critical inner voice"),
                        ("🚪 avoidance or numbness towards difficult feelings, blocking progress", "emotional avoidance")
                    ]
                    half = len(q2_choices) // 2
                    for i, (label, value) in enumerate(q2_choices):
                        container = col1 if i < half else col2
                        container.button(
                            label,
                            key=f"q2_{i}",
                            use_container_width=True,
                            type="secondary",
                            on_click=self._answer_question,
                            args=(2, value)
                        )
                else:
                    st.success(f"✅ selected: {st.session_state.quiz_answers[2]}")
                    st.info("recognizing your limited beliefs opens the way to lasting transformation.")

        # question 3 unchanged
        if len(st.session_state.quiz_answers) >= 2:
            q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
            with st.expander("question 3: how ready are you to fully commit to inner transformation?", expanded=q3_expanded):
                if 3 not in st.session_state.quiz_answers:
                    col1, col2 = st.columns(2)
                    col1.button(
                        "🤔 curious but cautious\nwant to learn more before committing",
                        key="q3_curious",
                        use_container_width=True,
                        type="secondary",
                        on_click=self._answer_question,
                        args=(3, "curious but cautious"),
                    )
                    col1.button(
                        "🎯 ready to commit\nprepared to do the inner work",
                        key="q3_ready",
                        use_container_width=True,
                        type="secondary",
                        on_click=self._answer_question,
                        args=(3, "ready to commit"),
                    )
                    col2.button(
                        "🔥 desperate for change\nthis must end now",
                        key="q3_desperate",
                        use_container_width=True,
                        type="secondary",
                        on_click=self._answer_question,
                        args=(3, "desperate for change"),
                    )
                    col2.button(
                        "🛡️ prefer gradual approach\nwant to try other methods first",
                        key="q3_gradual",
                        use_container_width=True,
                        type="secondary",
                        on_click=self._answer_question,
                        args=(3, "prefer gradual approach"),
                    )
                else:
                    st.success(f"✅ selected: {st.session_state.quiz_answers[3]}")
                    st.info("readiness strongly influences hypnotherapy success.")

        progress = len(st.session_state.quiz_answers) / 3
        if progress > 0:
            st.progress(progress)
            if progress < 1:
                st.caption(f"question {len(st.session_state.quiz_answers) + 1} of 3")
            else:
                st.caption("assessment complete!")

    def _answer_question(self, question_id, answer):
        st.session_state.quiz_answers[question_id] = answer

        if question_id < 3:
            st.session_state.quiz_step = question_id + 1
        else:
            st.session_state.quiz_completed = True
            st.session_state.quiz_score = self._calculate_score()

    def _calculate_score(self):
        scoring = {
            1: {
                "chronic stress or anxiety": 30,
                "repetitive negative habits or addictions": 30,
                "heightened emotional reactivity": 20,
                "persistent self-doubt": 20,
                "procrastination": 20,
                "vertigo or physical discomfort": 15,
                "quit smoking": 30,
                "feeling stuck or overwhelmed": 25,
            },
            2: {
                "force and control": 25,
                "defensive mistrust": 20,
                "all-or-nothing thinking": 25,
                "doing addiction": 30,
                "self-critical inner voice": 20,
                "emotional avoidance": 20
            },
            3: {
                "curious but cautious": 10,
                "ready to commit": 30,
                "desperate for change": 30,
                "prefer gradual approach": 10,
            },
        }
        total_score = 0
        for qid, answer in st.session_state.quiz_answers.items():
            total_score += scoring.get(qid, {}).get(answer, 0)
        return min(total_score, 100)

    def _render_quiz_results(self):
        score = st.session_state.quiz_score

        if score >= 75:
            message = "✅ Assessment complete! 💫 You are highly suited for rapid transformation with hypnotherapy."
        elif score >= 50:
            message = "✅ Assessment complete! ✨ You have good potential for transformation with proper support."
        else:
            message = "✅ Assessment complete! 🌱 You may benefit from preparation or alternative approaches before hypnotherapy."

        st.success(message)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(" ")
            st.markdown(
                f"""
                <a href="{self.discovery_url}" target="_blank" class="cta-button">
                📞 Book discovery call
                </a>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            if st.button("🔄 Retake assessment", use_container_width=True, type="secondary"):
                self._reset_quiz()

    def _reset_quiz(self):
        st.session_state.quiz_answers = {}
        st.session_state.quiz_step = 1
        st.session_state.quiz_completed = False
        st.session_state.quiz_score = 0
        st.rerun()

class MethodTeaserWithVideo:
    """Method overview with video and link to method page"""
    
    def render(self):
        st.subheader("Why hypnotherapy succeeds where others haven't")

        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.video("https://youtu.be/5ORz1-LWrjo?feature=shared")
        
        with col2:
            st.write("""
            **The problem:** Your conscious mind (5% of decisions) fights your subconscious programming (95% of decisions). 
            The subconscious always wins.
            """)
            
            st.write("""
            **Our breakthrough:** Instead of fighting your subconscious, we work directly with it. 
            We identify your specific patterns and rewire them at the source.
            """)
            
            st.info("When your subconscious programming supports your goals instead of fighting them, change becomes effortless and permanent.")
        
        st.markdown("---")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**Want to understand the complete neuroscience behind our method?** ")
            st.write("See the detailed breakdown of how neuroplasticity creates lasting change, brain wave states, and clinical evidence.")
        
        with col2:
            st.markdown("""
                <a href="https://hypnotherapy.streamlit.app/#deep-pattern-analysis" 
                   target="_blank" 
                   class="cta-button">
                   👉 swipe to 2+1 Method page
                </a>
            """, unsafe_allow_html=True)

class HomePage:
    """Complete home page with integrated improved quiz"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.quiz = EnhancedQuizSection()
        self.method_teaser = MethodTeaserWithVideo()
    
    def render(self):
        with st.container():
            self.hero.render()
            st.markdown("    ")
        with st.container():
            self.quiz.render()
            st.markdown("    ")
        with st.container():
            self.method_teaser.render()
            st.markdown("    ")

def create_home_page():
    return HomePage()
