# """
# Fixed Home page component with better styling and readability
# """
# import streamlit as st
# from utils.config import AppConstants

# class HeroSection:
#     """Hero section using Streamlit components"""
    
#     def render(self):
#         """Render hero section with Streamlit components"""
#         # Break free from limitations... Experience transformative change...
#         # Hero container using Streamlit container
#         # with st.container():
#         #     st.markdown("""
#         #     <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#         #                 border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#         #         <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
#         #         # <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
#         #         #     Most people try to change using willpower. That's why 95% fail. <br>
#         #         #     We bypass your conscious resistance and reprogram your subconscious patterns directly.
#         #         # </p>
#         #     </div>
#         #     """, unsafe_allow_html=True)
#         with st.container():
#             st.markdown(f"""
#             <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
#                 <img src="https://raw.githubusercontent.com/pepeette/Hypno/main/img/hero_title_1.png" 
#                      alt="Stop Fighting Your Mind. Start Working With It." 
#                      style="max-width: 100%; height: auto; border-radius: 16px;">
#             </div>
#             """, unsafe_allow_html=True)
            
#             # # Add compelling message using Streamlit info box
#             # st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")

#             # # Logo and Info message on same row with responsive design
#             # col1, col2 = st.columns([1, 2], gap="medium")
            
#             # with col1:
#             #     # Logo with same height as info box
#             #     st.markdown("""
#             #     <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
#             #         <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.jpg?raw=true" 
#             #              alt="Hypnotherapy Logo" 
#             #              style="max-width: 100%; height: auto; border-radius: 8px; 
#             #                     max-height: 80px; object-fit: contain;">
#             #     </div>
#             #     """, unsafe_allow_html=True)
            
#             # with col2:
#             #     # Info box - will automatically size to content
#             #     st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")


#             # Starting lines 
#             st.write("Most people try to change using willpower. That's why 95% fail. We bypass your conscious resistance and reprogram your subconscious patterns directly.")
            
#             # Logo and Info message forced to stay on same row even on mobile
#             st.markdown("""
#             <div style="display: flex; gap: 1rem; margin: 1rem 0; align-items: stretch; flex-wrap: nowrap;">
#                 <div style="flex: 0 0 auto; display: flex; align-items: center; justify-content: center; min-width: 120px;">
#                     <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.png?raw=true" 
#                          alt="Hypnotherapy Logo" 
#                          style="max-width: 100%; height: auto; border-radius: 8px; 
#                                 max-height: 80px; object-fit: contain;">
#                 </div>
#                 <div style="flex: 1; display: flex; align-items: center;">
#                     <div style="background: rgba(76, 161, 163, 0.1); border: 1px solid #4CA1A3; 
#                                 border-radius: 8px; padding: 1rem; width: 100%;">
#                         <p style="margin: 0; color: #273548; font-size: 1rem; line-height: 1.6;">
#                             💡 True change begins when you stop resisting yourself and start rewiring the patterns controlling your behavior.<br>
#                             → Book your hypnotherapy at our new address in BANGKOK to break free from unwanted habits. 2 sessions only needed.
#                         </p>
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
                
# class QuizSection:
#     # """Quiz section using Streamlit components with better UX"""
    
#     # def __init__(self):
#     #     # Initialize session state using Streamlit
#     #     if 'quiz_answers' not in st.session_state:
#     #         st.session_state.quiz_answers = {}
#     #     if 'quiz_step' not in st.session_state:
#     #         st.session_state.quiz_step = 1
#     #     if 'quiz_completed' not in st.session_state:
#     #         st.session_state.quiz_completed = False
#     #     if 'quiz_score' not in st.session_state:
#     #         st.session_state.quiz_score = 0
#     #     if 'primary_pattern' not in st.session_state:
#     #         st.session_state.primary_pattern = ""
    
#     # def render(self):
#     #     """Render quiz using Streamlit components"""
#     #     # Section header
#     #     st.subheader("Are you ready for your Hypnotherapy Rapid change?")
#     #     st.write("3 questions to assess your potential for transformation: (click on the most suited option)")
        
#     #     if not st.session_state.quiz_completed:
#     #         self._render_all_questions()
#     #     else:
#     #         self._render_results()
    
#     # def _render_all_questions(self):
#     #     """Show all questions with proper collapsing - Q1 expanded by default"""
#     #     current_step = st.session_state.quiz_step
        
#     #     # Question 1 - Expanded by default, collapsed after answering
#     #     q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
#     #     with st.expander("Question 1: What would you most like to change?", expanded=q1_expanded):
#     #         if 1 not in st.session_state.quiz_answers:
#     #             col1, col2 = st.columns(2)
#     #             with col1:
#     #                 if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
#     #                     self._answer_question(1, "Quit Smoking")
#     #                 if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
#     #                     self._answer_question(1, "Improve Sleep")
#     #             with col2:
#     #                 if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
#     #                     self._answer_question(1, "Reduce Anxiety")
#     #                 if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
#     #                     self._answer_question(1, "Break Bad Habits")
#     #         else:
#     #             st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
#     #     # Question 2 - Show only if Q1 answered, expand when active
#     #     if len(st.session_state.quiz_answers) >= 1:
#     #         q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
#     #         with st.expander("Question 2: How long have you been dealing with this?", expanded=q2_expanded):
#     #             if 2 not in st.session_state.quiz_answers:
#     #                 if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
#     #                     self._answer_question(2, "Less than 6 months")
#     #                 if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
#     #                     self._answer_question(2, "6 months to 2 years")
#     #                 if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
#     #                     self._answer_question(2, "More than 2 years")
#     #             else:
#     #                 st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
#     #     # Question 3 - Show only if Q2 answered, expand when active
#     #     if len(st.session_state.quiz_answers) >= 2:
#     #         q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
#     #         with st.expander("Question 3: How ready are you to make this change?", expanded=q3_expanded):
#     #             if 3 not in st.session_state.quiz_answers:
#     #                 if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
#     #                     self._answer_question(3, "Just exploring options")
#     #                 if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
#     #                     self._answer_question(3, "Very ready - I'm committed")
#     #                 if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
#     #                     self._answer_question(3, "Desperate for change")
#     #             else:
#     #                 st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
#     #     # Progress using Streamlit progress bar
#     #     progress = len(st.session_state.quiz_answers) / 3
#     #     if progress > 0:
#     #         st.progress(progress)
#     #         if progress < 1:
#     #             st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
#     #         else:
#     #             st.caption("Complete!")
    
#     # def _answer_question(self, question_id, answer):
#     #     """Handle question answer"""
#     #     st.session_state.quiz_answers[question_id] = answer
#     #     if question_id < 3:
#     #         st.session_state.quiz_step = question_id + 1
#     #     else:
#     #         st.session_state.quiz_completed = True
#     #         st.session_state.quiz_score = self._calculate_score()
#     #     st.rerun()
    
#     # def _calculate_score(self):
#     #     """Calculate suitability score"""
#     #     scoring = {
#     #         1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
#     #         2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
#     #         3: {"Just exploring options": 10, "Very ready - I'm committed": 30, "Desperate for change": 25}
#     #     }
        
#     #     total_score = 0
#     #     for q_id, answer in st.session_state.quiz_answers.items():
#     #         if q_id in scoring and answer in scoring[q_id]:
#     #             total_score += scoring[q_id][answer]
        
#     #     return min(total_score, 100)
    
#     # def _render_results(self):
#     #     """Render quiz results using Streamlit components"""
#     #     score = st.session_state.quiz_score
#     #     primary_pattern = st.session_state.primary_pattern
        
#     #     # Determine message based on score
#     #     if score >= 70:
#     #         st.success("🌟 Excellent candidate! You have strong indicators for rapid transformation.")
#     #         st.info("You're ready to book your transformation package or start with a discovery call.")
#     #     elif score >= 55:
#     #         st.warning("🎯 Good potential! Hypnotherapy can definitely help with the right approach.")
#     #         st.info("A discovery call would help us create the perfect strategy for your situation.")
#     #     else:
#     #         st.info("💬 Let's talk! Every situation is unique, and a conversation will help us determine the best path forward.")
#     #         st.info("A free discovery call will help us understand how to best support your goals.")
        
#     #     # Display score using st.metric with combined value/delta
#     #     col1, col2, col3 = st.columns([1, 2, 1])
#     #     with col2:
#     #         st.metric("", f"{score}% Suitability Match", "Transformation Readiness")
        
#     #     # Action buttons using Streamlit columns
#     #     col1, col2 = st.columns(2)
#     #     with col1:
#     #         if st.button("🔄 Retake Assessment", use_container_width=True):
#     #             self._reset_quiz()
#     #     with col2:
#     #         if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
#     #             st.success("Perfect! Scroll down to book your call.")
    
#     # def _reset_quiz(self):
#     #     """Reset quiz state"""
#     #     st.session_state.quiz_answers = {}
#     #     st.session_state.quiz_step = 1
#     #     st.session_state.quiz_completed = False
#     #     st.session_state.quiz_score = 0
#     #     st.rerun()
    
    
#     """Quiz section identifying internal blocking mechanisms and positioning hypnotherapy as solution"""
    
#     def __init__(self):
#         # Initialize session state
#         if 'quiz_answers' not in st.session_state:
#             st.session_state.quiz_answers = {}
#         if 'quiz_step' not in st.session_state:
#             st.session_state.quiz_step = 1
#         if 'quiz_completed' not in st.session_state:
#             st.session_state.quiz_completed = False
#         if 'quiz_score' not in st.session_state:
#             st.session_state.quiz_score = 0
#         if 'dominant_blocking_mechanism' not in st.session_state:
#             st.session_state.dominant_blocking_mechanism = ""
    
#     def render(self):
#         """Render the complete quiz experience"""
#         # Section header
#         st.subheader("Discover what's blocking your authentic change")
#         st.write("3 questions to identify your internal thought system patterns and transformation readiness:")
        
#         if not st.session_state.quiz_completed:
#             self._render_all_questions()
#         else:
#             self._render_transformation_results()
    
#     def _render_all_questions(self):
#         """Show all questions with proper progression"""
#         current_step = st.session_state.quiz_step
        
#         # Question 1 - Identify dominant blocking mechanism
#         q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
#         with st.expander("Question 1: which internal pattern most limits your growth?", expanded=q1_expanded):
#             if 1 not in st.session_state.quiz_answers:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("⚔️ Force and control\n'I must push through resistance'", key="q1_force", use_container_width=True):
#                         self._answer_question(1, "Force and control")
#                     if st.button("🔒 Mistrust and defensiveness\n'I can't let my guard down'", key="q1_mistrust", use_container_width=True):
#                         self._answer_question(1, "Mistrust and defensiveness")
#                 with col2:
#                     if st.button("⚖️ All-or-nothing thinking\n'It's either perfect or failure'", key="q1_binary", use_container_width=True):
#                         self._answer_question(1, "All-or-nothing thinking")
#                     if st.button("🏃 Doing addiction\n'My worth depends on productivity'", key="q1_doing", use_container_width=True):
#                         self._answer_question(1, "Doing addiction")
#             else:
#                 st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
#         # Question 2 - Change attempts and frustration
#         if len(st.session_state.quiz_answers) >= 1:
#             q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
#             with st.expander("Question 2: how do you typically try to create change?", expanded=q2_expanded):
#                 if 2 not in st.session_state.quiz_answers:
#                     if st.button("💪 Push harder with willpower and discipline", key="q2_willpower", use_container_width=True):
#                         self._answer_question(2, "Push harder with willpower")
#                     if st.button("📚 Learn more techniques and strategies", key="q2_techniques", use_container_width=True):
#                         self._answer_question(2, "Learn more techniques")
#                     if st.button("🔄 Change external circumstances or people", key="q2_external", use_container_width=True):
#                         self._answer_question(2, "Change external circumstances")
#                     if st.button("😤 Get frustrated and give up temporarily", key="q2_frustrated", use_container_width=True):
#                         self._answer_question(2, "Get frustrated and give up")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
#         # Question 3 - Readiness for internal transformation
#         if len(st.session_state.quiz_answers) >= 2:
#             q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
#             with st.expander("Question 3: how ready are you to examine your thought system?", expanded=q3_expanded):
#                 if 3 not in st.session_state.quiz_answers:
#                     if st.button("🤔 Curious but cautious about internal work", key="q3_curious", use_container_width=True):
#                         self._answer_question(3, "Curious but cautious")
#                     if st.button("🎯 Ready to explore how my thinking creates problems", key="q3_ready", use_container_width=True):
#                         self._answer_question(3, "Ready to explore thinking")
#                     if st.button("🔥 Desperate for a different approach to change", key="q3_desperate", use_container_width=True):
#                         self._answer_question(3, "Desperate for different approach")
#                     if st.button("🛡️ Prefer focusing on external solutions first", key="q3_external", use_container_width=True):
#                         self._answer_question(3, "Prefer external solutions")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
#         # Progress indicator
#         progress = len(st.session_state.quiz_answers) / 3
#         if progress > 0:
#             st.progress(progress)
#             if progress < 1:
#                 st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
#             else:
#                 st.caption("Complete!")
    
#     def _answer_question(self, question_id, answer):
#         """Handle question answers and progression"""
#         st.session_state.quiz_answers[question_id] = answer
#         if question_id == 1:
#             st.session_state.dominant_blocking_mechanism = answer
        
#         if question_id < 3:
#             st.session_state.quiz_step = question_id + 1
#         else:
#             st.session_state.quiz_completed = True
#             st.session_state.quiz_score = self._calculate_transformation_readiness()
#         st.rerun()
    
#     def _calculate_transformation_readiness(self):
#         """Calculate readiness based on d'Ansembourg principles"""
#         scoring = {
#             1: {  # Blocking mechanism awareness
#                 "Force and control": 25,
#                 "Mistrust and defensiveness": 20,
#                 "All-or-nothing thinking": 30,
#                 "Doing addiction": 35
#             },
#             2: {  # Change approach recognition
#                 "Push harder with willpower": 15,
#                 "Learn more techniques": 25,
#                 "Change external circumstances": 10,
#                 "Get frustrated and give up": 30  # Paradoxically high - shows awareness of futility
#             },
#             3: {  # Internal transformation readiness
#                 "Curious but cautious": 25,
#                 "Ready to explore thinking": 35,
#                 "Desperate for different approach": 30,
#                 "Prefer external solutions": 10
#             }
#         }
        
#         total_score = 0
#         for q_id, answer in st.session_state.quiz_answers.items():
#             if q_id in scoring and answer in scoring[q_id]:
#                 total_score += scoring[q_id][answer]
        
#         return min(total_score, 100)
    
#     def _render_transformation_results(self):
#         """Render results focusing on internal transformation readiness"""
#         score = st.session_state.quiz_score
#         blocking_mechanism = st.session_state.dominant_blocking_mechanism
        
#         # Blocking mechanism insights
#         mechanism_insights = {
#             "Force and control": {
#                 "description": "You tend to use force when resistance appears, creating internal battles that exhaust you. True change happens through alignment, not overpowering.",
#                 "transformation": "Hypnotherapy helps you access cooperation from your subconscious mind instead of fighting it. When all parts of you want the same thing, change becomes effortless.",
#                 "d_ansembourg_principle": "Moving from 'gourdin vs grotte' (club vs cave) to genuine inner meeting and collaboration."
#             },
#             "Mistrust and defensiveness": {
#                 "description": "Your internal security system stays hyperactive, treating change as potential danger. This prevents the vulnerability needed for transformation.",
#                 "transformation": "Hypnotherapy creates a safe space for your subconscious to update its threat assessment. When you feel internally secure, change becomes an adventure rather than a threat.",
#                 "d_ansembourg_principle": "Transforming systematic mistrust into grounded confidence and inner security."
#             },
#             "All-or-nothing thinking": {
#                 "description": "Your mind divides experience into perfect/failure, good/bad, which eliminates the middle ground where growth actually happens.",
#                 "transformation": "Hypnotherapy rewires binary thinking into flexible, nuanced responses. You learn to embrace progress over perfection and growth over fixed outcomes.",
#                 "d_ansembourg_principle": "Healing the separation and division that fragments your experience of life."
#             },
#             "Doing addiction": {
#                 "description": "Your worth feels tied to constant productivity and achievement. This creates exhausting cycles where rest feels like failure.",
#                 "transformation": "Hypnotherapy separates your inherent value from your actions. You discover that being yourself naturally generates inspired action without compulsive doing.",
#                 "d_ansembourg_principle": "Shifting from 'doing for validation' to 'being that naturally expresses through action.'"
#             }
#         }
        
#         # Results display
#         if score >= 75:
#             st.success("🌟 High readiness for authentic transformation! Your awareness of internal patterns indicates excellent potential for rapid, lasting change.")
#             readiness_level = "high"
#         elif score >= 55:
#             st.warning("🎯 Good transformation potential! You show strong indicators for successful internal pattern rewiring with proper support.")
#             readiness_level = "moderate"
#         elif score >= 35:
#             st.info("💬 Guided transformation recommended. Your situation would benefit from professional support to navigate internal resistance safely.")
#             readiness_level = "guided"
#         else:
#             st.info("🌱 Preparation phase recommended. Building awareness and readiness will optimize your transformation when you're ready.")
#             readiness_level = "preparation"
        
#         # Display transformation readiness score
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.metric("", f"{score}% Internal transformation readiness", "Thought system rewiring potential")
        
#         # Mechanism-specific insight
#         if blocking_mechanism in mechanism_insights:
#             insight = mechanism_insights[blocking_mechanism]
            
#             st.markdown("### Your dominant internal pattern")
#             st.info(f"**{blocking_mechanism}:** {insight['description']}")
            
#             st.markdown("### How hypnotherapy transforms this pattern")
#             st.success(insight['transformation'])
            
#             st.markdown("### The d'Ansembourg principle")
#             st.write(f"*{insight['d_ansembourg_principle']}*")
        
#         # Customized recommendations based on readiness
#         st.markdown("### Your transformation pathway")
        
#         if readiness_level == "high":
#             st.write("You demonstrate strong awareness of how internal thought systems create external problems. This insight positions you perfectly for the 2-session hypnotherapy method that rewires thinking patterns at their source.")
            
#         elif readiness_level == "moderate":
#             st.write("You recognize that change requires more than willpower, which is crucial wisdom. A discovery call would help determine the best approach for transforming your specific thought patterns into supportive ones.")
            
#         elif readiness_level == "guided":
#             st.write("You're beginning to see how internal patterns might be influencing your experience. Professional guidance can help you explore this safely and effectively, building confidence in your ability to change from within.")
            
#         else:
#             st.write("Developing awareness of internal patterns is the first step toward authentic change. A discovery call can help you understand how hypnotherapy works and whether you're ready for internal transformation.")
        
#         # Action buttons
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("🔄 Retake assessment", use_container_width=True):
#                 self._reset_quiz()
#         with col2:
#             if st.button("📞 Book discovery call", type="primary", use_container_width=True):
#                 st.success("Perfect! Scroll down to explore how we transform thought systems.")
    
#     def _reset_quiz(self):
#         """Reset all quiz state"""
#         st.session_state.quiz_answers = {}
#         st.session_state.quiz_step = 1
#         st.session_state.quiz_completed = False
#         st.session_state.quiz_score = 0
#         st.session_state.dominant_blocking_mechanism = ""
#         st.rerun()

# class PatternChangeMethod:
#     """Pattern change method explanation using Streamlit components"""
    
#     def render(self):
#         """Render method explanation using Streamlit components"""
#         st.subheader("Why Hypnotherapy succeeds where others haven't")
        
#         # Opening explanation using Streamlit info box
#         st.info("""
#         Every unwanted behavior is driven by subconscious patterns you learned years ago. 
#         Traditional therapy tries to override these patterns with willpower. We change the patterns themselves.
#         When your subconscious programming supports your goals instead of fighting them, 
#         change becomes effortless and permanent.
#         """)
        
#         # Success rate using custom metrics with combined value/delta
#         with st.container():
#             # Force 3 columns to stay in one row even on mobile
#             st.markdown("""
#             <div style="display: flex; gap: 0.5rem; margin: 1rem 0; flex-wrap: nowrap; 
#                         justify-content: space-between;">
#                 <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                             border-radius: 8px; padding: 1rem; text-align: center;">
#                     <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
#                         Success Rate
#                     </div>
#                     <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
#                         85% in 2 sessions
#                     </div>
#                 </div>
#                 <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                             border-radius: 8px; padding: 1rem; text-align: center;">
#                     <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
#                         3rd Session Optional
#                     </div>
#                     <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
#                         15% need Reinforcement
#                     </div>
#                 </div>
#                 <div style="flex: 1; min-width: 0; background: white; border: 1px solid #CBD5E1; 
#                             border-radius: 8px; padding: 1rem; text-align: center;">
#                     <div style="color: #556D7A; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem;">
#                         Rapid pattern rewiring
#                     </div>
#                     <div style="color: #4CA1A3; font-size: 1.5rem; font-weight: 700; line-height: 1.2;">
#                         for Lasting change
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             st.success("Most clients achieve complete transformation in two 90-minute sessions. About 15% choose an optional reinforcement session a few weeks later for additional confidence.")
        
#         # Method comparison using 3-column layout with image in center
#         st.write("### The key is in the method")
        
#         # Desktop: 3 columns, Mobile: stacked
#         col1, col2, col3 = st.columns([1, 1, 1])
        
#         # Column 1: Traditional Methods Card
#         with col1:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; margin: 1rem 0; border-left: 4px solid #ef4444; height: 100%;">
#                 <h2 style="color: #dc2626; margin-bottom: 1rem; text-align: center;">❌ Traditional Methods</h2>
#                 <p><strong>Talk therapy:</strong> Analyzes problems but rarely creates lasting change</p>
#                 <p><strong>Willpower:</strong> Requires constant effort and usually fails within weeks</p>
#                 <p><strong>Medications:</strong> Manage symptoms but don't address root causes</p>
#                 <p><strong>Self-help:</strong> Gives you tools but can't change deep programming</p>
#                 <p style="margin: 0; font-weight: 600; color: #dc2626; text-align: center;">
#                     Result: You know what to do but can't consistently do it
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         # Column 2: Comparison Image - Full image, no text
#         with col2:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         margin: 1rem 0; height: 100%; padding: 0; overflow: hidden;
#                         display: flex; align-items: center; justify-content: center;">
#                 <img src="https://github.com/pepeette/Hypno/blob/main/img/Hypnotherapy_compa.jpg?raw=true" 
#                      alt="Hypnotherapy Comparison" 
#                      style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
#             </div>
#             """, unsafe_allow_html=True)
        
#         # Column 3: Pattern Change Hypnotherapy Card  
#         with col3:
#             st.markdown("""
#             <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                         padding: 2rem; margin: 1rem 0; border-left: 4px solid #22c55e; height: 100%;">
#                 <h2 style="color: #16a34a; margin-bottom: 1rem; text-align: center;">✅ Hypnotherapy</h2>
#                 <p><strong>Session 1:</strong> Map your unique subconscious triggers and patterns</p>
#                 <p><strong>Session 2:</strong> Rewire those patterns at the subconscious level</p>
#                 <p><strong>Session 3:</strong> Optional reinforcement if needed (15% of clients)</p>
#                 <p><strong>Follow-up:</strong> Permanent change that feels natural and effortless</p>
#                 <p style="margin: 0; font-weight: 600; color: #16a34a; text-align: center;">
#                     Result: Your subconscious now supports your goals automatically
#                 </p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         # How it works using simple columns instead of tabs (avoid background colors)
#         with st.container():
#             st.write("### How the method works : 2 + 1")
            
#             col1, col2, col3 = st.columns(3)
            
#             with col1:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
#                     <h2 style="color: #273548;">Deep pattern analysis</h2>
#                     <p style="color: #556D7A;">We map exactly what triggers your unwanted behavior at the subconscious level - 
#                     often patterns you learned in childhood that no longer serve you.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
#                     <h2 style="color: #273548;">Neural Reset Hypnosis</h2>
#                     <p style="color: #556D7A;">Using clinical hypnosis, we access your subconscious mind and install new, 
#                     empowering patterns that automatically support your goals.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             with col3:
#                 st.markdown("""
#                 <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
#                             padding: 2rem; text-align: center; margin: 1rem 0;">
#                     <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
#                                 border-radius: 50%; display: flex; align-items: center; justify-content: center; 
#                                 font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">3</div>
#                     <h2 style="color: #273548;">Live the Change</h2>
#                     <p style="color: #556D7A;">The old urges and compulsions simply disappear. You naturally make choices 
#                     that align with your goals without effort or struggle.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
#         st.markdown("""
#         <p>* "we" clearly indicates that it is a binding work between the client and the therapist, throughout each session.</p>
#                                     </div>
#                 """, unsafe_allow_html=True)
        

# class HomePage:
#     """Complete home page using Streamlit components"""
    
#     def __init__(self):
#         self.hero = HeroSection()
#         self.quiz = QuizSection()
#         self.method = PatternChangeMethod()
    
#     def render(self):
#         """Render complete home page using Streamlit layout"""
#         # Use Streamlit containers for clean layout
#         with st.container():
#             self.hero.render()
#             st.markdown("    ")
            
#         with st.container():
#             self.quiz.render()
#             st.markdown("    ")
        
#         with st.container():
#             self.method.render()
#             st.markdown("    ")

# # Factory function for clean import
# def create_home_page():
#     return HomePage()


"""
Fixed Home page component with better styling and readability
"""
import streamlit as st
from utils.config import AppConstants

class HeroSection:
    """Hero section using Streamlit components"""
    
    def render(self):
        """Render hero section with Streamlit components"""
        # Break free from limitations... Experience transformative change...
        # Hero container using Streamlit container
        # with st.container():
        #     st.markdown("""
        #     <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
        #                 border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
        #         <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
        #         # <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
        #         #     Most people try to change using willpower. That's why 95% fail. <br>
        #         #     We bypass your conscious resistance and reprogram your subconscious patterns directly.
        #         # </p>
        #     </div>
        #     """, unsafe_allow_html=True)
        with st.container():
            st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
                <img src="https://raw.githubusercontent.com/pepeette/Hypno/main/img/hero_title_1.png" 
                     alt="Stop Fighting Your Mind. Start Working With It." 
                     style="max-width: 100%; height: auto; border-radius: 16px;">
            </div>
            """, unsafe_allow_html=True)
            
            # # Add compelling message using Streamlit info box
            # st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")

            # # Logo and Info message on same row with responsive design
            # col1, col2 = st.columns([1, 2], gap="medium")
            
            # with col1:
            #     # Logo with same height as info box
            #     st.markdown("""
            #     <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
            #         <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.jpg?raw=true" 
            #              alt="Hypnotherapy Logo" 
            #              style="max-width: 100%; height: auto; border-radius: 8px; 
            #                     max-height: 80px; object-fit: contain;">
            #     </div>
            #     """, unsafe_allow_html=True)
            
            # with col2:
            #     # Info box - will automatically size to content
            #     st.info("💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.")


            # Starting lines 
            st.write("Most people try to change using willpower. That's why 95% fail. We bypass your conscious resistance and reprogram your subconscious patterns directly.")
            
            # Logo and Info message forced to stay on same row even on mobile
            st.markdown("""
            <div style="display: flex; gap: 1rem; margin: 1rem 0; align-items: stretch; flex-wrap: nowrap;">
                <div style="flex: 0 0 auto; display: flex; align-items: center; justify-content: center; min-width: 120px;">
                    <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.png?raw=true" 
                         alt="Hypnotherapy Logo" 
                         style="max-width: 100%; height: auto; border-radius: 8px; 
                                max-height: 80px; object-fit: contain;">
                </div>
                <div style="flex: 1; display: flex; align-items: center;">
                    <div style="background: rgba(76, 161, 163, 0.1); border: 1px solid #4CA1A3; 
                                border-radius: 8px; padding: 1rem; width: 100%;">
                        <p style="margin: 0; color: #273548; font-size: 1rem; line-height: 1.6;">
                            💡 True change begins when you stop resisting yourself and start rewiring the patterns controlling your behavior.<br>
                            → Book your hypnotherapy at our new address in BANGKOK to break free from unwanted habits. 2 sessions only needed.
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
                
class QuizSection:
    # """Quiz section using Streamlit components with better UX"""
    
    # def __init__(self):
    #     # Initialize session state using Streamlit
    #     if 'quiz_answers' not in st.session_state:
    #         st.session_state.quiz_answers = {}
    #     if 'quiz_step' not in st.session_state:
    #         st.session_state.quiz_step = 1
    #     if 'quiz_completed' not in st.session_state:
    #         st.session_state.quiz_completed = False
    #     if 'quiz_score' not in st.session_state:
    #         st.session_state.quiz_score = 0
    #     if 'primary_pattern' not in st.session_state:
    #         st.session_state.primary_pattern = ""
    
    # def render(self):
    #     """Render quiz using Streamlit components"""
    #     # Section header
    #     st.subheader("Are you ready for your Hypnotherapy Rapid change?")
    #     st.write("3 questions to assess your potential for transformation: (click on the most suited option)")
        
    #     if not st.session_state.quiz_completed:
    #         self._render_all_questions()
    #     else:
    #         self._render_results()
    
    # def _render_all_questions(self):
    #     """Show all questions with proper collapsing - Q1 expanded by default"""
    #     current_step = st.session_state.quiz_step
        
    #     # Question 1 - Expanded by default, collapsed after answering
    #     q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
    #     with st.expander("Question 1: What would you most like to change?", expanded=q1_expanded):
    #         if 1 not in st.session_state.quiz_answers:
    #             col1, col2 = st.columns(2)
    #             with col1:
    #                 if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
    #                     self._answer_question(1, "Quit Smoking")
    #                 if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
    #                     self._answer_question(1, "Improve Sleep")
    #             with col2:
    #                 if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
    #                     self._answer_question(1, "Reduce Anxiety")
    #                 if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
    #                     self._answer_question(1, "Break Bad Habits")
    #         else:
    #             st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
    #     # Question 2 - Show only if Q1 answered, expand when active
    #     if len(st.session_state.quiz_answers) >= 1:
    #         q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
    #         with st.expander("Question 2: How long have you been dealing with this?", expanded=q2_expanded):
    #             if 2 not in st.session_state.quiz_answers:
    #                 if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
    #                     self._answer_question(2, "Less than 6 months")
    #                 if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
    #                     self._answer_question(2, "6 months to 2 years")
    #                 if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
    #                     self._answer_question(2, "More than 2 years")
    #             else:
    #                 st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
    #     # Question 3 - Show only if Q2 answered, expand when active
    #     if len(st.session_state.quiz_answers) >= 2:
    #         q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
    #         with st.expander("Question 3: How ready are you to make this change?", expanded=q3_expanded):
    #             if 3 not in st.session_state.quiz_answers:
    #                 if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
    #                     self._answer_question(3, "Just exploring options")
    #                 if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
    #                     self._answer_question(3, "Very ready - I'm committed")
    #                 if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
    #                     self._answer_question(3, "Desperate for change")
    #             else:
    #                 st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
    #     # Progress using Streamlit progress bar
    #     progress = len(st.session_state.quiz_answers) / 3
    #     if progress > 0:
    #         st.progress(progress)
    #         if progress < 1:
    #             st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
    #         else:
    #             st.caption("Complete!")
    
    # def _answer_question(self, question_id, answer):
    #     """Handle question answer"""
    #     st.session_state.quiz_answers[question_id] = answer
    #     if question_id < 3:
    #         st.session_state.quiz_step = question_id + 1
    #     else:
    #         st.session_state.quiz_completed = True
    #         st.session_state.quiz_score = self._calculate_score()
    #     st.rerun()
    
    # def _calculate_score(self):
    #     """Calculate suitability score"""
    #     scoring = {
    #         1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
    #         2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
    #         3: {"Just exploring options": 10, "Very ready - I'm committed": 30, "Desperate for change": 25}
    #     }
        
    #     total_score = 0
    #     for q_id, answer in st.session_state.quiz_answers.items():
    #         if q_id in scoring and answer in scoring[q_id]:
    #             total_score += scoring[q_id][answer]
        
    #     return min(total_score, 100)
    
    # def _render_results(self):
    #     """Render quiz results using Streamlit components"""
    #     score = st.session_state.quiz_score
    #     primary_pattern = st.session_state.primary_pattern
        
    #     # Determine message based on score
    #     if score >= 70:
    #         st.success("🌟 Excellent candidate! You have strong indicators for rapid transformation.")
    #         st.info("You're ready to book your transformation package or start with a discovery call.")
    #     elif score >= 55:
    #         st.warning("🎯 Good potential! Hypnotherapy can definitely help with the right approach.")
    #         st.info("A discovery call would help us create the perfect strategy for your situation.")
    #     else:
    #         st.info("💬 Let's talk! Every situation is unique, and a conversation will help us determine the best path forward.")
    #         st.info("A free discovery call will help us understand how to best support your goals.")
        
    #     # Display score using st.metric with combined value/delta
    #     col1, col2, col3 = st.columns([1, 2, 1])
    #     with col2:
    #         st.metric("", f"{score}% Suitability Match", "Transformation Readiness")
        
    #     # Action buttons using Streamlit columns
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         if st.button("🔄 Retake Assessment", use_container_width=True):
    #             self._reset_quiz()
    #     with col2:
    #         if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
    #             st.success("Perfect! Scroll down to book your call.")
    
    # def _reset_quiz(self):
    #     """Reset quiz state"""
    #     st.session_state.quiz_answers = {}
    #     st.session_state.quiz_step = 1
    #     st.session_state.quiz_completed = False
    #     st.session_state.quiz_score = 0
    #     st.rerun()
    
    
    """Quiz section identifying internal blocking mechanisms and positioning hypnotherapy as solution"""
    
    def __init__(self):
        # Initialize session state
        if 'quiz_answers' not in st.session_state:
            st.session_state.quiz_answers = {}
        if 'quiz_step' not in st.session_state:
            st.session_state.quiz_step = 1
        if 'quiz_completed' not in st.session_state:
            st.session_state.quiz_completed = False
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
        if 'dominant_blocking_mechanism' not in st.session_state:
            st.session_state.dominant_blocking_mechanism = ""
        
        # Get discovery URL from config
        self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
    
    def render(self):
        """Render the complete quiz experience"""
        # Section header
        st.subheader("Discover what's blocking your authentic change")
        st.write("3 questions to identify your internal thought system patterns and transformation readiness:")
        
        if not st.session_state.quiz_completed:
            self._render_all_questions()
        else:
            self._render_transformation_results()
    
    def _render_all_questions(self):
        """Show all questions with proper progression"""
        current_step = st.session_state.quiz_step
        
        # Question 1 - Identify dominant blocking mechanism
        q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
        with st.expander("Question 1: which internal pattern most limits your growth?", expanded=q1_expanded):
            if 1 not in st.session_state.quiz_answers:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⚔️ Force and control\n'I must push through resistance'", key="q1_force", use_container_width=True):
                        self._answer_question(1, "Force and control")
                    if st.button("🔒 Mistrust and defensiveness\n'I can't let my guard down'", key="q1_mistrust", use_container_width=True):
                        self._answer_question(1, "Mistrust and defensiveness")
                with col2:
                    if st.button("⚖️ All-or-nothing thinking\n'It's either perfect or failure'", key="q1_binary", use_container_width=True):
                        self._answer_question(1, "All-or-nothing thinking")
                    if st.button("🏃 Doing addiction\n'My worth depends on productivity'", key="q1_doing", use_container_width=True):
                        self._answer_question(1, "Doing addiction")
            else:
                st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
        # Question 2 - Change attempts and frustration
        if len(st.session_state.quiz_answers) >= 1:
            q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
            with st.expander("Question 2: how do you typically try to create change?", expanded=q2_expanded):
                if 2 not in st.session_state.quiz_answers:
                    if st.button("💪 Push harder with willpower and discipline", key="q2_willpower", use_container_width=True):
                        self._answer_question(2, "Push harder with willpower")
                    if st.button("📚 Learn more techniques and strategies", key="q2_techniques", use_container_width=True):
                        self._answer_question(2, "Learn more techniques")
                    if st.button("🔄 Change external circumstances or people", key="q2_external", use_container_width=True):
                        self._answer_question(2, "Change external circumstances")
                    if st.button("😤 Get frustrated and give up temporarily", key="q2_frustrated", use_container_width=True):
                        self._answer_question(2, "Get frustrated and give up")
                else:
                    st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
        # Question 3 - Readiness for internal transformation
        if len(st.session_state.quiz_answers) >= 2:
            q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
            with st.expander("Question 3: how ready are you to examine your thought system?", expanded=q3_expanded):
                if 3 not in st.session_state.quiz_answers:
                    if st.button("🤔 Curious but cautious about internal work", key="q3_curious", use_container_width=True):
                        self._answer_question(3, "Curious but cautious")
                    if st.button("🎯 Ready to explore how my thinking creates problems", key="q3_ready", use_container_width=True):
                        self._answer_question(3, "Ready to explore thinking")
                    if st.button("🔥 Desperate for a different approach to change", key="q3_desperate", use_container_width=True):
                        self._answer_question(3, "Desperate for different approach")
                    if st.button("🛡️ Prefer focusing on external solutions first", key="q3_external", use_container_width=True):
                        self._answer_question(3, "Prefer external solutions")
                else:
                    st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
        # Progress indicator
        progress = len(st.session_state.quiz_answers) / 3
        if progress > 0:
            st.progress(progress)
            if progress < 1:
                st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
            else:
                st.caption("Complete!")
    
    def _answer_question(self, question_id, answer):
        """Handle question answers and progression"""
        st.session_state.quiz_answers[question_id] = answer
        if question_id == 1:
            st.session_state.dominant_blocking_mechanism = answer
        
        if question_id < 3:
            st.session_state.quiz_step = question_id + 1
        else:
            st.session_state.quiz_completed = True
            st.session_state.quiz_score = self._calculate_transformation_readiness()
        st.rerun()
    
    def _calculate_transformation_readiness(self):
        """Calculate readiness based on d'Ansembourg principles"""
        scoring = {
            1: {  # Blocking mechanism awareness
                "Force and control": 25,
                "Mistrust and defensiveness": 20,
                "All-or-nothing thinking": 30,
                "Doing addiction": 35
            },
            2: {  # Change approach recognition
                "Push harder with willpower": 15,
                "Learn more techniques": 25,
                "Change external circumstances": 10,
                "Get frustrated and give up": 30  # Paradoxically high - shows awareness of futility
            },
            3: {  # Internal transformation readiness
                "Curious but cautious": 25,
                "Ready to explore thinking": 35,
                "Desperate for different approach": 30,
                "Prefer external solutions": 10
            }
        }
        
        total_score = 0
        for q_id, answer in st.session_state.quiz_answers.items():
            if q_id in scoring and answer in scoring[q_id]:
                total_score += scoring[q_id][answer]
        
        return min(total_score, 100)
    
    def _render_transformation_results(self):
        """Render results focusing on internal transformation readiness"""
        score = st.session_state.quiz_score
        blocking_mechanism = st.session_state.dominant_blocking_mechanism
        
        # Blocking mechanism insights
        mechanism_insights = {
            "Force and control": {
                "description": "You tend to use force when resistance appears, creating internal battles that exhaust you. True change happens through alignment, not overpowering.",
                "transformation": "Hypnotherapy helps you access cooperation from your subconscious mind instead of fighting it. When all parts of you want the same thing, change becomes effortless.",
                "d_ansembourg_principle": "Moving from 'gourdin vs grotte' (club vs cave) to genuine inner meeting and collaboration."
            },
            "Mistrust and defensiveness": {
                "description": "Your internal security system stays hyperactive, treating change as potential danger. This prevents the vulnerability needed for transformation.",
                "transformation": "Hypnotherapy creates a safe space for your subconscious to update its threat assessment. When you feel internally secure, change becomes an adventure rather than a threat.",
                "d_ansembourg_principle": "Transforming systematic mistrust into grounded confidence and inner security."
            },
            "All-or-nothing thinking": {
                "description": "Your mind divides experience into perfect/failure, good/bad, which eliminates the middle ground where growth actually happens.",
                "transformation": "Hypnotherapy rewires binary thinking into flexible, nuanced responses. You learn to embrace progress over perfection and growth over fixed outcomes.",
                "d_ansembourg_principle": "Healing the separation and division that fragments your experience of life."
            },
            "Doing addiction": {
                "description": "Your worth feels tied to constant productivity and achievement. This creates exhausting cycles where rest feels like failure.",
                "transformation": "Hypnotherapy separates your inherent value from your actions. You discover that being yourself naturally generates inspired action without compulsive doing.",
                "d_ansembourg_principle": "Shifting from 'doing for validation' to 'being that naturally expresses through action.'"
            }
        }
        
        # Results display
        if score >= 75:
            st.success("🌟 High readiness for authentic transformation! Your awareness of internal patterns indicates excellent potential for rapid, lasting change.")
            readiness_level = "high"
        elif score >= 55:
            st.warning("🎯 Good transformation potential! You show strong indicators for successful internal pattern rewiring with proper support.")
            readiness_level = "moderate"
        elif score >= 35:
            st.info("💬 Guided transformation recommended. Your situation would benefit from professional support to navigate internal resistance safely.")
            readiness_level = "guided"
        else:
            st.info("🌱 Preparation phase recommended. Building awareness and readiness will optimize your transformation when you're ready.")
            readiness_level = "preparation"
        
        # Display transformation readiness score
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.metric("", f"{score}% Internal transformation readiness", "Thought system rewiring potential")
        
        # Mechanism-specific insight
        if blocking_mechanism in mechanism_insights:
            insight = mechanism_insights[blocking_mechanism]
            
            st.markdown("### Your dominant internal pattern")
            st.info(f"**{blocking_mechanism}:** {insight['description']}")
            
            st.markdown("### How hypnotherapy transforms this pattern")
            st.success(insight['transformation'])
            
            st.markdown("### The d'Ansembourg principle")
            st.write(f"*{insight['d_ansembourg_principle']}*")
        
        # Customized recommendations based on readiness
        st.markdown("### Your transformation pathway")
        
        if readiness_level == "high":
            st.write("You demonstrate strong awareness of how internal thought systems create external problems. This insight positions you perfectly for the 2-session hypnotherapy method that rewires thinking patterns at their source.")
            
        elif readiness_level == "moderate":
            st.write("You recognize that change requires more than willpower, which is crucial wisdom. A discovery call would help determine the best approach for transforming your specific thought patterns into supportive ones.")
            
        elif readiness_level == "guided":
            st.write("You're beginning to see how internal patterns might be influencing your experience. Professional guidance can help you explore this safely and effectively, building confidence in your ability to change from within.")
            
        else:
            st.write("Developing awareness of internal patterns is the first step toward authentic change. A discovery call can help you understand how hypnotherapy works and whether you're ready for internal transformation.")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retake assessment", use_container_width=True):
                self._reset_quiz()
        with col2:
            # Modified button with URL redirect functionality
            if st.button("📞 Book discovery call", type="primary", use_container_width=True):
                # Show success message and open URL in new tab
                st.success("Perfect! Scroll down to explore how we transform thought systems.")
                # JavaScript to open URL in new tab
                st.markdown(f"""
                <script>
                    window.open('{self.discovery_url}', '_blank');
                </script>
                """, unsafe_allow_html=True)
    
    def _reset_quiz(self):
        """Reset all quiz state"""
        st.session_state.quiz_answers = {}
        st.session_state.quiz_step = 1
        st.session_state.quiz_completed = False
        st.session_state.quiz_score = 0
        st.session_state.dominant_blocking_mechanism = ""
        st.rerun()

class PatternChangeMethod:
    """Pattern change method explanation using Streamlit components"""
    
    def render(self):
        """Render method explanation using Streamlit components"""
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
        
        # Method comparison using 3-column layout with image in center
        st.write("### The key is in the method")
        
        # Desktop: 3 columns, Mobile: stacked
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # Column 1: Traditional Methods Card
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
        
        # Column 2: Comparison Image - Full image, no text
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
        
        # Column 3: Pattern Change Hypnotherapy Card  
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
        
        # How it works using simple columns instead of tabs (avoid background colors)
        with st.container():
            st.write("### How the method works : 2 + 1")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">1</div>
                    <h2 style="color: #273548;">Deep pattern analysis</h2>
                    <p style="color: #556D7A;">We map exactly what triggers your unwanted behavior at the subconscious level - 
                    often patterns you learned in childhood that no longer serve you.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">2</div>
                    <h2 style="color: #273548;">Neural Reset Hypnosis</h2>
                    <p style="color: #556D7A;">Using clinical hypnosis, we access your subconscious mind and install new, 
                    empowering patterns that automatically support your goals.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div style="background: white; border: 1px solid #CBD5E1; border-radius: 12px; 
                            padding: 2rem; text-align: center; margin: 1rem 0;">
                    <div style="background: #4CA1A3; color: white; width: 60px; height: 60px; 
                                border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                                font-weight: bold; font-size: 1.5rem; margin: 0 auto 1rem;">3</div>
                    <h2 style="color: #273548;">Live the Change</h2>
                    <p style="color: #556D7A;">The old urges and compulsions simply disappear. You naturally make choices 
                    that align with your goals without effort or struggle.</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("""
        <p>* "we" clearly indicates that it is a binding work between the client and the therapist, throughout each session.</p>
                                    </div>
                """, unsafe_allow_html=True)
        

class HomePage:
    """Complete home page using Streamlit components"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.quiz = QuizSection()
        self.method = PatternChangeMethod()
        # Initialize discovery URL from config
        self.discovery_url = AppConstants.CONTACT_INFO.get("discovery_call_url", "https://calendly.com/laetitiasheppard/discovery")
    
    def render(self):
        """Render complete home page using Streamlit layout"""
        # Use Streamlit containers for clean layout
        with st.container():
            self.hero.render()
            st.markdown("    ")
            
        with st.container():
            self.quiz.render()
            st.markdown("    ")
        
        with st.container():
            self.method.render()
            st.markdown("    ")
        
        # Additional discovery call button at the bottom of the page
        with st.container():
            st.markdown("### Ready to get started?")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("📞 Book discovery call", type="primary", use_container_width=True, key="bottom_discovery_call"):
                    # Show success message and open URL in new tab
                    st.success("Perfect! Opening your discovery call booking page...")
                    # JavaScript to open URL in new tab
                    st.markdown(f"""
                    <script>
                        window.open('{self.discovery_url}', '_blank');
                    </script>
                    """, unsafe_allow_html=True)

# Factory function for clean import
def create_home_page():
    return HomePage()
