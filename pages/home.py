# """
# Fixed Home page component with better styling and readability
# """
# import streamlit as st

# class HeroSection:
#     """Hero section using Streamlit components"""
    
#     def render(self):
#         """Render hero section with Streamlit components"""
#         # Hero container using Streamlit container
#         with st.container():
#             st.markdown("""
#             <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
#                         border-radius: 16px; padding: 4rem 2rem; text-align: center; margin: 2rem 0;">
#                 <h1 style="color: white;">Stop Fighting Your Mind.<br>Start Working With It.</h1>
#                 <p style="color: white; opacity: 0.95; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">
#                     Most people try to change using willpower. That's why 95% fail. <br>
#                     We bypass your conscious resistance and reprogram your subconscious patterns directly.
#                 </p>
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


#             # Logo and Info message forced to stay on same row even on mobile
#             st.markdown("""
#             <div style="display: flex; gap: 1rem; margin: 1rem 0; align-items: stretch; flex-wrap: nowrap;">
#                 <div style="flex: 0 0 auto; display: flex; align-items: center; justify-content: center; min-width: 120px;">
#                     <img src="https://github.com/pepeette/Hypno/blob/main/img/logo.jpg?raw=true" 
#                          alt="Hypnotherapy Logo" 
#                          style="max-width: 100%; height: auto; border-radius: 8px; 
#                                 max-height: 80px; object-fit: contain;">
#                 </div>
#                 <div style="flex: 1; display: flex; align-items: center;">
#                     <div style="background: rgba(76, 161, 163, 0.1); border: 1px solid #4CA1A3; 
#                                 border-radius: 8px; padding: 1rem; width: 100%;">
#                         <p style="margin: 0; color: #273548; font-size: 1rem; line-height: 1.6;">
#                             💡 Real change happens when you stop fighting yourself and start changing the patterns that drive your behavior.
#                         </p>
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
                
# class QuizSection:
#     """Quiz section using Streamlit components with better UX"""
    
#     def __init__(self):
#         # Initialize session state using Streamlit
#         if 'quiz_answers' not in st.session_state:
#             st.session_state.quiz_answers = {}
#         if 'quiz_step' not in st.session_state:
#             st.session_state.quiz_step = 1
#         if 'quiz_completed' not in st.session_state:
#             st.session_state.quiz_completed = False
#         if 'quiz_score' not in st.session_state:
#             st.session_state.quiz_score = 0
    
#     def render(self):
#         """Render quiz using Streamlit components"""
#         # Section header
#         st.subheader("Find Out If You're Ready for Rapid Change")
#         st.write("3 questions to assess your potential for transformation: (click on the most suited option)")
        
#         if not st.session_state.quiz_completed:
#             self._render_all_questions()
#         else:
#             self._render_results()
    
#     def _render_all_questions(self):
#         """Show all questions with proper collapsing - Q1 expanded by default"""
#         current_step = st.session_state.quiz_step
        
#         # Question 1 - Expanded by default, collapsed after answering
#         q1_expanded = (current_step == 1) or (1 not in st.session_state.quiz_answers)
#         with st.expander("Question 1: What would you most like to change?", expanded=q1_expanded):
#             if 1 not in st.session_state.quiz_answers:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("🚭 Quit Smoking", key="q1_smoking", use_container_width=True):
#                         self._answer_question(1, "Quit Smoking")
#                     if st.button("😴 Improve Sleep", key="q1_sleep", use_container_width=True):
#                         self._answer_question(1, "Improve Sleep")
#                 with col2:
#                     if st.button("😌 Reduce Anxiety", key="q1_anxiety", use_container_width=True):
#                         self._answer_question(1, "Reduce Anxiety")
#                     if st.button("🔄 Break Bad Habits", key="q1_habits", use_container_width=True):
#                         self._answer_question(1, "Break Bad Habits")
#             else:
#                 st.success(f"✅ Selected: {st.session_state.quiz_answers[1]}")
        
#         # Question 2 - Show only if Q1 answered, expand when active
#         if len(st.session_state.quiz_answers) >= 1:
#             q2_expanded = (current_step == 2) and (2 not in st.session_state.quiz_answers)
#             with st.expander("Question 2: How long have you been dealing with this?", expanded=q2_expanded):
#                 if 2 not in st.session_state.quiz_answers:
#                     if st.button("🆕 Less than 6 months", key="q2_new", use_container_width=True):
#                         self._answer_question(2, "Less than 6 months")
#                     if st.button("📅 6 months to 2 years", key="q2_mod", use_container_width=True):
#                         self._answer_question(2, "6 months to 2 years")
#                     if st.button("⏳ More than 2 years", key="q2_long", use_container_width=True):
#                         self._answer_question(2, "More than 2 years")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[2]}")
        
#         # Question 3 - Show only if Q2 answered, expand when active
#         if len(st.session_state.quiz_answers) >= 2:
#             q3_expanded = (current_step == 3) and (3 not in st.session_state.quiz_answers)
#             with st.expander("Question 3: How ready are you to make this change?", expanded=q3_expanded):
#                 if 3 not in st.session_state.quiz_answers:
#                     if st.button("🤔 Just exploring options", key="q3_explore", use_container_width=True):
#                         self._answer_question(3, "Just exploring options")
#                     if st.button("💪 Very ready - I'm committed", key="q3_ready", use_container_width=True):
#                         self._answer_question(3, "Very ready - I'm committed")
#                     if st.button("🔥 Desperate for change", key="q3_determined", use_container_width=True):
#                         self._answer_question(3, "Desperate for change")
#                 else:
#                     st.success(f"✅ Selected: {st.session_state.quiz_answers[3]}")
        
#         # Progress using Streamlit progress bar
#         progress = len(st.session_state.quiz_answers) / 3
#         if progress > 0:
#             st.progress(progress)
#             if progress < 1:
#                 st.caption(f"Question {len(st.session_state.quiz_answers) + 1} of 3")
#             else:
#                 st.caption("Complete!")
    
#     def _answer_question(self, question_id, answer):
#         """Handle question answer"""
#         st.session_state.quiz_answers[question_id] = answer
#         if question_id < 3:
#             st.session_state.quiz_step = question_id + 1
#         else:
#             st.session_state.quiz_completed = True
#             st.session_state.quiz_score = self._calculate_score()
#         st.rerun()
    
#     def _calculate_score(self):
#         """Calculate suitability score"""
#         scoring = {
#             1: {"Quit Smoking": 40, "Reduce Anxiety": 35, "Improve Sleep": 30, "Break Bad Habits": 35},
#             2: {"Less than 6 months": 20, "6 months to 2 years": 25, "More than 2 years": 30},
#             3: {"Just exploring options": 10, "Very ready - I'm committed": 30, "Desperate for change": 25}
#         }
        
#         total_score = 0
#         for q_id, answer in st.session_state.quiz_answers.items():
#             if q_id in scoring and answer in scoring[q_id]:
#                 total_score += scoring[q_id][answer]
        
#         return min(total_score, 100)
    
#     def _render_results(self):
#         """Render quiz results using Streamlit components"""
#         score = st.session_state.quiz_score
        
#         # Determine message based on score
#         if score >= 70:
#             st.success("🌟 Excellent candidate! You have strong indicators for rapid transformation.")
#             st.info("You're ready to book your transformation package or start with a discovery call.")
#         elif score >= 55:
#             st.warning("🎯 Good potential! Hypnotherapy can definitely help with the right approach.")
#             st.info("A discovery call would help us create the perfect strategy for your situation.")
#         else:
#             st.info("💬 Let's talk! Every situation is unique, and a conversation will help us determine the best path forward.")
#             st.info("A free discovery call will help us understand how to best support your goals.")
        
#         # Display score using st.metric with combined value/delta
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.metric("", f"{score}% Suitability Match", "Transformation Readiness")
        
#         # Action buttons using Streamlit columns
#         col1, col2 = st.columns(2)
#         with col1:
#             if st.button("🔄 Retake Assessment", use_container_width=True):
#                 self._reset_quiz()
#         with col2:
#             if st.button("📞 Book Discovery Call", type="primary", use_container_width=True):
#                 st.success("Perfect! Scroll down to book your call.")
    
#     def _reset_quiz(self):
#         """Reset quiz state"""
#         st.session_state.quiz_answers = {}
#         st.session_state.quiz_step = 1
#         st.session_state.quiz_completed = False
#         st.session_state.quiz_score = 0
#         st.rerun()

# class PatternChangeMethod:
#     """Pattern change method explanation using Streamlit components"""
    
#     def render(self):
#         """Render method explanation using Streamlit components"""
#         st.subheader("Pattern Change Hypnotherapy: Why It Works")
        
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
#         st.write("### The Difference Is in the Approach")
        
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
#                     <h2 style="color: #273548;">Identify Your Patterns</h2>
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
#                     <h2 style="color: #273548;">Reprogram Directly</h2>
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
Home page component for the Hypnotherapy website
Improved spacing and visual hierarchy with clean Streamlit components
"""
import streamlit as st

class HeroSection:
    """Hero section with improved spacing and visual hierarchy"""
    
    def render(self):
        """Render hero section with better spacing"""
        # Add top spacing
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        
        # Hero container with gradient background
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; 
                    margin-bottom: 3rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h1 style="color: white; margin-bottom: 1.5rem; font-weight: 700;">
                Transform Your Life in Just 2 Sessions
            </h1>
            <p style="font-size: 1.2rem; color: white; opacity: 0.95; 
                      max-width: 600px; margin: 0 auto 2.5rem auto; line-height: 1.6;">
                Science-backed clinical hypnotherapy to overcome smoking, anxiety, and unwanted habits
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats section with improved spacing
        st.markdown("<div style='margin: 3rem 0 2rem 0;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            st.metric("Success Rate", "85%", "in 2 sessions")
        with col2:
            st.metric("Lives Transformed", "500+", "since 2014")
        with col3:
            st.metric("Years Experience", "10+", "established practice")
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 4rem;'></div>", unsafe_allow_html=True)

class KeyDifferentiator:
    """Key differentiator section with improved visual separation"""
    
    def render(self):
        """Render differentiator with better spacing"""
        # Section spacing
        st.markdown("<div style='margin: 4rem 0 2rem 0;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, #FFFFFF 100%); 
                    border-radius: 12px; padding: 3rem 2rem; margin: 2rem 0; 
                    border-left: 4px solid #4CA1A3; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h2 style="color: #4CA1A3; margin-bottom: 1.5rem; font-weight: 600;">
                🧠 Why Our Method Works
            </h2>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #273548; margin-bottom: 1rem;">
                Traditional therapy focuses on <strong>symptoms</strong> using conscious willpower 
                (which fails 95% of the time).
            </p>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #273548; margin: 0;">
                Our method targets the <strong>root cause</strong> in your subconscious mind - 
                where lasting change actually happens.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

class QuizSection:
    """Enhanced quiz section with better spacing and visual hierarchy"""
    
    def render(self):
        """Render quiz section with improved spacing"""
        # Section header with spacing
        st.markdown("<div style='margin: 5rem 0 3rem 0;'></div>", unsafe_allow_html=True)
        
        # Quiz header
        st.markdown("""
        <div style="text-align: center; margin-bottom: 3rem;">
            <h2 style="color: #273548; margin-bottom: 1rem;">🎯 30-Second Suitability Assessment</h2>
            <p style="font-size: 1.1rem; color: #556D7A; max-width: 500px; margin: 0 auto;">
                Discover your potential for rapid transformation in 3 quick questions
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quiz placeholder with improved styling
        st.markdown("""
        <div style="background: #FFFFFF; border-radius: 12px; padding: 3rem 2rem; 
                    margin: 2rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1.5rem;">🎯</div>
            <h3 style="color: #4CA1A3; margin-bottom: 1rem;">Interactive Assessment Coming Soon!</h3>
            <p style="color: #556D7A; margin-bottom: 2rem;">
                For now, book a free discovery call to assess your suitability
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA button with spacing
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📞 Book Free Discovery Call", key="quiz_cta", type="primary", use_container_width=True):
                # Scroll to booking section
                st.markdown('<script>document.querySelector("#discovery").scrollIntoView({behavior: "smooth"});</script>', 
                          unsafe_allow_html=True)
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 4rem;'></div>", unsafe_allow_html=True)

class BenefitsSection:
    """Benefits section with improved grid layout and spacing"""
    
    def render(self):
        """Render benefits with better visual hierarchy"""
        # Section spacing
        st.markdown("<div style='margin: 5rem 0 3rem 0;'></div>", unsafe_allow_html=True)
        
        # Section header
        st.markdown("""
        <div style="text-align: center; margin-bottom: 4rem;">
            <h2 style="color: #273548; margin-bottom: 1rem;">Why Choose Our 2-Session Method?</h2>
            <p style="color: #556D7A; font-size: 1.1rem;">
                Four key advantages that create lasting transformation
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Benefits grid with improved spacing
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            # Benefit 1
            st.markdown("""
            <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem 2rem; 
                        text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 2rem; height: 280px;
                        display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1.5rem;">⚡</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-weight: 600;">Rapid Results</h3>
                <p style="color: #556D7A; line-height: 1.6; margin: 0;">
                    See transformation in just 2 sessions, not months of therapy
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Benefit 2
            st.markdown("""
            <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem 2rem; 
                        text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 2rem; height: 280px;
                        display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1.5rem;">🎯</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-weight: 600;">Targeted Approach</h3>
                <p style="color: #556D7A; line-height: 1.6; margin: 0;">
                    Personalized sessions designed for your specific challenges
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Benefit 3
            st.markdown("""
            <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem 2rem; 
                        text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 2rem; height: 280px;
                        display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1.5rem;">🧠</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-weight: 600;">Science-Backed</h3>
                <p style="color: #556D7A; line-height: 1.6; margin: 0;">
                    Uses proven neuroplasticity principles to rewire your subconscious
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Benefit 4
            st.markdown("""
            <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem 2rem; 
                        text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                        border: 1px solid #CBD5E1; margin-bottom: 2rem; height: 280px;
                        display: flex; flex-direction: column; justify-content: center;">
                <div style="font-size: 3rem; margin-bottom: 1.5rem;">💯</div>
                <h3 style="color: #273548; margin-bottom: 1rem; font-weight: 600;">High Success Rate</h3>
                <p style="color: #556D7A; line-height: 1.6; margin: 0;">
                    85% of clients achieve their goals in our 2-session program
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 4rem;'></div>", unsafe_allow_html=True)

class TestimonialsSection:
    """Testimonials with improved spacing and visual design"""
    
    def render(self):
        """Render testimonials with better spacing"""
        # Section spacing
        st.markdown("<div style='margin: 5rem 0 3rem 0;'></div>", unsafe_allow_html=True)
        
        # Section header
        st.markdown("""
        <div style="text-align: center; margin-bottom: 4rem;">
            <h2 style="color: #273548; margin-bottom: 1rem;">💬 Client Success Stories</h2>
            <p style="color: #556D7A; font-size: 1.1rem;">
                Real transformations from real people
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 1
        st.markdown("""
        <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem; 
                    margin-bottom: 3rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; border-left: 4px solid #4CA1A3;">
            <div style="display: flex; align-items: flex-start; gap: 2rem;">
                <div style="font-size: 3rem; color: #4CA1A3; min-width: 80px; text-align: center;">🌟</div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; 
                                       color: #273548; margin: 0 0 1.5rem 0; line-height: 1.6;">
                        "Finally broke free from old patterns – 2 sessions changed everything."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A; margin-bottom: 0.8rem;">
                        — Director, Banking, Singapore
                    </div>
                    <div style="display: flex; gap: 1.5rem; font-size: 0.9rem; color: #4CA1A3; flex-wrap: wrap;">
                        <span>🎯 Anxiety patterns</span>
                        <span>⏱️ 2 sessions</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Testimonial 2
        st.markdown("""
        <div style="background: #FFFFFF; border-radius: 12px; padding: 2.5rem; 
                    margin-bottom: 3rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); 
                    border: 1px solid #CBD5E1; border-left: 4px solid #4CA1A3;">
            <div style="display: flex; align-items: flex-start; gap: 2rem;">
                <div style="font-size: 3rem; color: #4CA1A3; min-width: 80px; text-align: center;">🚭</div>
                <div style="flex: 1;">
                    <blockquote style="font-style: italic; font-size: 1.2rem; 
                                       color: #273548; margin: 0 0 1.5rem 0; line-height: 1.6;">
                        "My husband was a heavy smoker... No more addiction."
                    </blockquote>
                    <div style="font-weight: 600; color: #556D7A; margin-bottom: 0.8rem;">
                        — Wife, Bangkok
                    </div>
                    <div style="display: flex; gap: 1.5rem; font-size: 0.9rem; color: #4CA1A3; flex-wrap: wrap;">
                        <span>🎯 Smoking cessation</span>
                        <span>⏱️ 2 sessions</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 4rem;'></div>", unsafe_allow_html=True)

class FinalCTA:
    """Final call-to-action with improved visual impact"""
    
    def render(self):
        """Render final CTA with better spacing"""
        # Section spacing
        st.markdown("<div style='margin: 6rem 0 3rem 0;'></div>", unsafe_allow_html=True)
        
        # CTA container
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                    border-radius: 16px; padding: 4rem 2rem; text-align: center; 
                    margin: 4rem 0; box-shadow: 0 4px 20px rgba(76, 161, 163, 0.3);">
            <h2 style="color: white; margin-bottom: 1.5rem; font-weight: 600;">
                Ready to Transform Your Life?
            </h2>
            <p style="color: white; opacity: 0.9; font-size: 1.2rem; 
                      max-width: 500px; margin: 0 auto 3rem auto; line-height: 1.6;">
                Join hundreds of people who have transformed their lives with our proven method.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CTA buttons with improved spacing
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            subcol1, subcol2, subcol3 = st.columns(3, gap="medium")
            
            with subcol1:
                if st.button("📞 Free Discovery Call", key="final_discovery", use_container_width=True, type="primary"):
                    st.markdown('<script>document.querySelector("#discovery").scrollIntoView({behavior: "smooth"});</script>', 
                              unsafe_allow_html=True)
            
            with subcol2:
                if st.button("🧠 Learn Our Method", key="final_method", use_container_width=True):
                    st.success("Redirecting to Method page...")
            
            with subcol3:
                if st.button("⚡ Book Sessions Now", key="final_book", use_container_width=True):
                    st.success("Great! Let's get started.")
        
        # Bottom spacing
        st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

class HomePage:
    """Main home page with improved spacing and visual hierarchy"""
    
    def __init__(self):
        self.hero = HeroSection()
        self.differentiator = KeyDifferentiator()
        self.quiz = QuizSection()
        self.benefits = BenefitsSection()
        self.testimonials = TestimonialsSection()
        self.final_cta = FinalCTA()
    
    def render(self):
        """Render complete home page with improved spacing"""
        # Hero section
        self.hero.render()
        
        # Key differentiator
        self.differentiator.render()
        
        # Quiz section
        self.quiz.render()
        
        # Benefits section
        self.benefits.render()
        
        # Testimonials
        self.testimonials.render()
        
        # Final CTA
        self.final_cta.render()

def create_home_page():
    """Factory function to create HomePage instance"""
    return HomePage()
