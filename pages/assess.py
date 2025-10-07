# """
# Enhanced Clinical Behavioral Pattern Assessment
# Mobile-optimized with clean design, comprehensive analytics integration
# """

# import streamlit as st
# from datetime import datetime
# import re
# from typing import Dict, Any, Optional

# # ============================================================================
# # COMPONENT IMPORTS
# # ============================================================================
# try:
#     from utils.config_assess import (
#         AssessmentConfig, 
#         AnalyticsEngine,
#         QuestionRouter,
#         COMPREHENSIVE_QUESTIONS
#     )
#     CONFIG_AVAILABLE = True
# except ImportError:
#     CONFIG_AVAILABLE = False
#     print("WARNING: config_assess not available")

# try:
#     from utils.email_assess import send_assessment_email
#     EMAIL_AVAILABLE = True
# except ImportError:
#     EMAIL_AVAILABLE = False
#     print("WARNING: email_assess not available")

# try:
#     from components.blueprint import create_behavioral_blueprint
#     BLUEPRINT_AVAILABLE = True
# except ImportError:
#     BLUEPRINT_AVAILABLE = False

# try:
#     from components.paywall import create_clinical_paywall
#     PAYWALL_AVAILABLE = True
# except ImportError:
#     PAYWALL_AVAILABLE = False


# # ============================================================================
# # DESIGN SYSTEM
# # ============================================================================
# def apply_clinical_design_system():
#     """Apply professional clinical design system"""
#     st.markdown("""
#     <style>
#         /* Core Design System */
#         :root {
#             --background: #F3F6F8;
#             --card-bg: #FFFFFF;
#             --primary-text: #273548;
#             --secondary-text: #556D7A;
#             --accent: #4CA1A3;
#             --accent-hover: #3B7A7A;
#             --border: #CBD5E1;
#             --success: #22c55e;
#             --warning: #eab308;
#             --error: #ef4444;
#         }
        
#         /* Container Optimization */
#         .main .block-container {
#             padding: 0.75rem 1rem !important;
#             max-width: 100% !important;
#         }
        
#         @media (min-width: 768px) {
#             .main .block-container {
#                 max-width: 600px !important;
#                 margin: 0 auto;
#                 padding: 1.5rem !important;
#             }
#         }
        
#         /* Typography System */
#         h1 { 
#             font-size: 2.2rem !important; 
#             color: var(--primary-text) !important;
#             font-weight: 700 !important;
#             margin-bottom: 0.5rem !important;
#         }
        
#         h2 { 
#             font-size: 1.8rem !important; 
#             color: var(--primary-text) !important;
#             font-weight: 600 !important;
#             margin: 1.5rem 0 0.75rem 0 !important;
#         }
        
#         h3, .stMarkdown strong {
#             font-size: 1rem !important;
#             color: var(--primary-text);
#             font-weight: 600 !important;
#         }
        
#         p, .stMarkdown p {
#             font-size: 1rem !important;
#             color: var(--primary-text) !important;
#             line-height: 1.6 !important;
#         }
        
#         /* Button System */
#         .stButton > button {
#             width: 100% !important;
#             margin-bottom: 0.25rem !important;
#             padding: 0.6rem 1rem !important;
#             text-align: left !important;
#             background-color: var(--card-bg) !important;
#             border: 1px solid var(--border) !important;
#             border-radius: 6px !important;
#             color: var(--primary-text) !important;
#             font-size: 0.95rem !important;
#             transition: all 0.2s ease !important;
#             line-height: 1.3 !important;
#             box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
#         }
        
#         .stButton > button:hover {
#             background-color: #F8FAFC !important;
#             border-color: var(--accent) !important;
#             transform: translateY(-1px) !important;
#             box-shadow: 0 2px 4px rgba(76,161,163,0.1) !important;
#         }
        
#         .stButton > button:active {
#             background-color: #E1F0F0 !important;
#             transform: translateY(0) !important;
#         }
        
#         /* Primary Button Style */
#         .stButton > button[kind="primary"] {
#             background-color: var(--accent) !important;
#             color: white !important;
#             border-color: var(--accent) !important;
#             text-align: center !important;
#             font-weight: 600 !important;
#         }
        
#         .stButton > button[kind="primary"]:hover {
#             background-color: var(--accent-hover) !important;
#             border-color: var(--accent-hover) !important;
#         }
        
#         /* Progress System */
#         .progress-container {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             margin-bottom: 1.5rem;
#             font-size: 0.85rem;
#             color: var(--secondary-text);
#         }
        
#         .progress-bar {
#             flex: 1;
#             height: 4px;
#             background: var(--border);
#             border-radius: 2px;
#             overflow: hidden;
#         }
        
#         .progress-fill {
#             height: 100%;
#             background: var(--accent);
#             transition: width 0.3s ease;
#         }
        
#         /* Input System */
#         .stTextArea textarea, .stTextInput input {
#             border: 1px solid var(--border) !important;
#             border-radius: 6px !important;
#             padding: 0.75rem !important;
#             font-size: 0.95rem !important;
#             background: var(--card-bg) !important;
#             color: var(--primary-text) !important;
#         }
        
#         .stTextArea textarea:focus, .stTextInput input:focus {
#             border-color: var(--accent) !important;
#             box-shadow: 0 0 0 1px var(--accent) !important;
#         }
        
#         /* Slider System */
#         .stSlider > div > div > div {
#             background-color: var(--accent) !important;
#         }
               
#         /* Hide Streamlit Branding */
#         header[data-testid="stHeader"] {
#             display: none !important;
#         }
        
#         .stDeployButton {
#             display: none !important;
#         }
        
#         footer {
#             display: none !important;
#         }
        
#         /* Mobile Optimization */
#         @media (max-width: 767px) {
#             .main .block-container {
#                 padding: 1rem !important;
#             }
            
#             h1 { font-size: 1.8rem !important; }
#             h2 { font-size: 1.5rem !important; }
            
#             .stButton > button {
#                 margin-bottom: 0.2rem !important;
#                 padding: 0.5rem 0.75rem !important;
#             }
#             [data-testid="column"] {
#                 min-width: 30% !important;
#                 flex-shrink: 0 !important;
#             }
#         }
#     </style>
#     """, unsafe_allow_html=True)


# # ============================================================================
# # ASSESSMENT CLASS
# # ============================================================================
# class ClinicalBehavioralAssessment:
#     """Professional clinical assessment with complete integration"""
    
#     def __init__(self):
#         self._init_session_state()
        
#         if CONFIG_AVAILABLE:
#             self.config = AssessmentConfig()
#             self.analytics = self.config.get_analytics_engine()
#             self.router = self.config.get_question_router()
#             self.questions = COMPREHENSIVE_QUESTIONS
#         else:
#             self.analytics = None
#             self.router = None
#             self.questions = []
    
#     def _init_session_state(self):
#         """Initialize session state"""
#         defaults = {
#             'assessment_responses': {},
#             'current_question_index': 0,
#             'assessment_completed': False,
#             'contact_provided': False,
#             'assessment_results': {},
#             'is_digital_native': False,
#             'show_blueprint': False,
#             'premium_access': False,
#             'disclaimer_accepted': False 
#         }
        
#         for key, value in defaults.items():
#             if key not in st.session_state:
#                 st.session_state[key] = value
    
#     def render(self):
#         """Main render method - FIXED with comprehensive error handling"""
#         try:
#             apply_clinical_design_system()
            
#             if not CONFIG_AVAILABLE:
#                 st.error("Assessment configuration not available. Please check utils/config_assess.py")
#                 return
            
#             self._render_header()
            
#             # FIXED: Better state validation
#             if not st.session_state.contact_provided:
#                 if not st.session_state.assessment_completed:
#                     self._render_assessment()
#                 else:
#                     # FIXED: Add validation before rendering contact form
#                     if not hasattr(st.session_state, 'assessment_responses') or not st.session_state.assessment_responses:
#                         st.error("Assessment data not found. Please restart the assessment.")
#                         if st.button("Restart assessment"):
#                             for key in ['assessment_responses', 'current_question_index', 'assessment_completed', 
#                                     'contact_provided', 'assessment_results']:
#                                 if key in st.session_state:
#                                     del st.session_state[key]
#                             st.rerun()
#                     else:
#                         self._render_contact_form()
#             else:
#                 self._render_results()
        
#         except Exception as e:
#             st.error("An error occurred in the assessment.")
            
#             # Show user-friendly error
#             st.error(f"Error details: {str(e)}")
            
#             # Debug information in expander
#             import traceback
#             with st.expander("🔧 Debug information (for support)"):
#                 st.code(traceback.format_exc())
#                 st.write("**Session state:**")
#                 st.json({
#                     'assessment_completed': st.session_state.get('assessment_completed', False),
#                     'contact_provided': st.session_state.get('contact_provided', False),
#                     'responses_count': len(st.session_state.get('assessment_responses', {})),
#                     'current_index': st.session_state.get('current_question_index', 0)
#                 })
            
#             # Offer restart option
#             if st.button("Restart assessment", type="primary"):
#                 for key in list(st.session_state.keys()):
#                     if key.startswith('assessment') or key in ['contact_provided', 'current_question_index']:
#                         del st.session_state[key]
#                 st.rerun()
        
#     def _render_disclaimer_page(self):
#         """Render disclaimer and acceptance page before assessment starts"""
        
#         # Critical disclaimer box
#         st.warning("""
#         ⚠️ **Before you begin, please review this important information**
        
#         This is a **proprietary framework** developed for hypnotherapy session planning. 
        
#         **This assessment:**
#         - Does not diagnose mental health conditions
#         - Is not a substitute for professional psychiatric or psychological care
#         - Should be used alongside, not instead of, evidence-based treatment
#         """)
        
#         # What this is for
#         st.markdown("### What this assessment is designed for")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("""
#             <div style="background: #E1F0F0; padding: 1.5rem; border-radius: 8px; 
#                         border-left: 4px solid #22c55e; height: 100%;">
#                 <h6 style="color: #22c55e; margin-top: 0;">✓ This is appropriate for:</h4>
#                 <ul style="color: #273548; line-height: 1.8;">
#                     <li>Exploring behavioral patterns you'd like to change</li>
#                     <li>Planning focused hypnotherapy intervention</li>
#                     <li>Complementing existing therapy</li>
#                     <li>Personal insight and self-awareness</li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown("""
#             <div style="background: #FEF3C7; padding: 1.5rem; border-radius: 8px; 
#                         border-left: 4px solid #F59E0B; height: 100%;">
#                 <h6 style="color: #F59E0B; margin-top: 0;">✗ This is NOT appropriate for:</h4>
#                 <ul style="color: #273548; line-height: 1.8;">
#                     <li>Diagnosing mental health conditions</li>
#                     <li>Replacing professional psychiatric care</li>
#                     <li>Crisis intervention or severe mental illness</li>
#                     <li>Medical or clinical decision-making</li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)

        
#         # Crisis resources
#         st.error("""
#         🆘 **If you're experiencing a mental health crisis:**
        
#         - **Thailand Mental Health Hotline:** 1323 (24/7)
#         - **Samaritans of Thailand:** 02-713-6793 (24/7)  
#         - **Emergency Services:** 1669
        
#         Please seek immediate professional help if you're experiencing thoughts of self-harm, 
#         severe depression, or psychological crisis.
#         """)

        
#         # Assessment details
#         st.markdown("### What to expect")
        
#         st.info("""
#         **Assessment details:**
#         - Approximately 70-75 questions
#         - Takes 15-20 minutes to complete
#         - You can go back and change answers
#         - Your responses are confidential
#         - Results are for treatment planning purposes only
        
#         **After completion:**
#         - Receive behavioral pattern analysis
#         - Get personalized intervention suggestions
#         - Licensed therapist will review your assessment
#         - Schedule consultation to discuss results
#         """)

        
#         # Acceptance section
#         st.markdown("### Your acknowledgment")
        
#         accept1 = st.checkbox(
#             "I understand this is a proprietary assessment framework, not a clinical diagnostic tool",
#             key="accept_proprietary"
#         )
        
#         accept2 = st.checkbox(
#             "I understand this assessment does not replace professional mental health care",
#             key="accept_not_replacement"
#         )
        
#         accept3 = st.checkbox(
#             "I am not currently experiencing a mental health crisis requiring immediate intervention",
#             key="accept_not_crisis"
#         )
        
#         st.markdown("  ")
        
#         # Continue button - only enabled if all accepted
#         all_accepted = accept1 and accept2 and accept3
        
#         if all_accepted:
#             col1, col2, col3 = st.columns([1, 2, 1])
#             with col2:
#                 if st.button("Begin assessment", type="primary", use_container_width=True):
#                     st.session_state.disclaimer_accepted = True
#                     st.rerun()
#         else:
#             col1, col2, col3 = st.columns([1, 2, 1])
#             with col2:
#                 st.button("Begin assessment", type="primary", use_container_width=True, disabled=True)
#             st.caption("Please check all boxes above to continue")
        
#         st.markdown("  ")
#         st.markdown("  ")
        
#         # Footer
#         st.caption("""
#         **Privacy notice:** Your responses are confidential and used only for treatment planning. 
#         We do not sell or share your personal information. [Privacy Policy Link]
#         """)

#     def _render_header(self):
#         """Render clean header"""
#         # st.markdown("""
#         # <div style="text-align: center; margin-bottom: 1.5rem;">
#         #     <h1>Behavioral pattern assessment</h1>

#         # </div>
#         # """, unsafe_allow_html=True)
#         st.markdown("**BEHAVIORAL ASSESSMENT**")        
#         st.markdown("  ")

#         # st.info("This assessment identifies your specific behavioral patterns "
#         #         "to create a personalized hypnotherapy protocol that targets your exact needs.")
    
#     def _render_assessment(self):
#         # Check if disclaimer accepted
#         if not st.session_state.get('disclaimer_accepted', False):
#             self._render_disclaimer_page()
#             return
        
#         """Render assessment questions"""
#         current_index = st.session_state.current_question_index
        
#         if current_index >= len(self.questions):
#             self._complete_assessment()
#             return
        
#         question = self.questions[current_index]
#         total_questions = len(self.questions)
        
#         # Progress bar
#         progress = current_index / total_questions if total_questions > 0 else 0
#         st.markdown(f"""
#         <div class="progress-container">
#             <span><strong>Q {current_index + 1}/{total_questions}</strong></span>
#             <div class="progress-bar">
#                 <div class="progress-fill" style="width: {progress * 100}%"></div>
#             </div>
#             <span><strong>{int(progress * 100)}%</strong></span>
#         </div>
#         """, unsafe_allow_html=True)

#         st.markdown("  ")
        
#         # # Question text
#         # st.markdown(f"### {question['text']}")
#         # Question text with gradient info box
#         st.markdown(f"""
#         <div style="background: linear-gradient(135deg, #E1F0F0 0%, #F8FAFC 100%); 
#                     padding: 1rem; border-radius: 8px; border-left: 4px solid #4CA1A3; 
#                     margin-bottom: 1.5rem;">
#             <h3 style="color: #000 !important; margin: 0 0 0.5rem 0; font-size: 1.2rem;">
#                 {question['text']}
#             </h3>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Render question type
#         self._render_question_type(question)
        
#         # Navigation
#         self._render_navigation(current_index)
    
#     def _render_question_type(self, question: Dict):
#         """Render different question types with previous answer memory"""
#         qtype = question['type']
#         qid = question['id']
#         question_text = question['text']
        
#         # Check if question was previously answered
#         previous_answer = st.session_state.assessment_responses.get(qid)
        
#         if qtype == 'single_choice':
#             options = question['options']
#             for i, option in enumerate(options):
#                 # Highlight previous answer if exists
#                 button_type = "primary" if previous_answer == option else "secondary"
#                 if st.button(option, key=f"q_{qid}_opt_{i}", use_container_width=True, type=button_type):
#                     self._save_response(qid, option)
#                     self._advance_question()
#                     st.rerun()
        
#         elif qtype == 'slider':
#             min_val = question.get('min', 0)
#             max_val = question.get('max', 10)
#             default = question.get('default', 5)
            
#             # Use previous answer if available
#             initial_value = previous_answer if previous_answer is not None else default
            
#             value = st.slider(
#                 question_text,
#                 min_value=min_val,
#                 max_value=max_val,
#                 value=int(initial_value),  # Ensure it's an integer
#                 key=f"slider_{qid}",
#                 label_visibility="collapsed"
#             )
            
#             if st.button("Continue", key=f"continue_{qid}", type="primary", use_container_width=True):
#                 self._save_response(qid, value)
#                 self._advance_question()
#                 st.rerun()
        
#         elif qtype == 'text_completion':
#             placeholder = question.get('placeholder', 'Your response...')
#             min_chars = question.get('min_chars', 3)
            
#             # Use previous answer if available
#             initial_text = previous_answer if previous_answer else ""
            
#             response = st.text_area(
#                 question_text,
#                 value=initial_text,  # Pre-fill with previous answer
#                 placeholder=placeholder,
#                 key=f"text_{qid}",
#                 height=100,
#                 label_visibility="collapsed"
#             )
            
#             if response.strip() and len(response.strip()) >= min_chars:
#                 if st.button("Continue", key=f"continue_{qid}", type="primary", use_container_width=True):
#                     self._save_response(qid, response.strip())
#                     self._advance_question()
#                     st.rerun()
#             elif response.strip():
#                 st.caption(f"Please provide at least {min_chars} characters")
    
#     def _render_navigation(self, current_index: int):
#         """Render navigation buttons"""
#         # Get current question from index to access question['id']
#         question = self.questions[current_index]
        
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col1:
#             if current_index > 0:
#                 if st.button("← Back", key="nav_back", use_container_width=True):
#                     self._go_back()
#                     st.rerun()
        
#         with col2:
#             # Count only non-skipped responses
#             answered = sum(1 for resp in st.session_state.assessment_responses.values() 
#                         if resp != "Not applicable")
#             st.markdown(f"""
#             <div style="text-align: center; padding: 0.5rem; color: #556D7A; font-size: 0.85rem;">
#                 <strong>{answered}</strong> answered
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             if st.button("Skip", key="nav_skip", use_container_width=True):
#                 self._save_response(question['id'], "Not applicable")
#                 self._advance_question()
#                 st.rerun()
    
#     def _save_response(self, qid: int, response: Any):
#         """Save response"""
#         st.session_state.assessment_responses[qid] = response
    
#     def _advance_question(self):
#         """Advance to next question"""
#         st.session_state.current_question_index += 1
    
#     def _go_back(self):
#         """Go back to previous question - preserves previous answers"""
#         if st.session_state.current_question_index > 0:
#             st.session_state.current_question_index -= 1
#             # Answer is preserved in session_state for when user returns
        
#     def _complete_assessment(self):
#         """Complete assessment and generate analysis - FIXED with validation"""
        
#         # FIXED: Validate we have responses
#         if not st.session_state.assessment_responses:
#             st.error("No responses found. Please complete at least one question.")
#             return
        
#         st.session_state.assessment_completed = True
        
#         # Generate complete analysis with error handling
#         assessment_data = {
#             'responses': st.session_state.assessment_responses,
#             'timestamp': datetime.now().isoformat()
#         }
        
#         try:
#             if self.analytics:
#                 analysis = self.analytics.generate_complete_analysis(assessment_data)
#                 st.session_state.assessment_results = analysis
#                 st.session_state.is_digital_native = analysis.get('is_digital_native', False)
#             else:
#                 # Fallback if analytics not available
#                 st.session_state.assessment_results = {
#                     'pattern_scores': {},
#                     'pattern_analysis': {},
#                     'success_prediction': {'overall_success_rate': 85},
#                     'digital_analysis': {},
#                     'is_digital_native': False
#                 }
#                 st.session_state.is_digital_native = False
#         except Exception as e:
#             # Log error but continue to contact form with fallback data
#             print(f"Analytics generation error: {str(e)}")
#             import traceback
#             print(traceback.format_exc())
            
#             st.session_state.assessment_results = {
#                 'error': str(e),
#                 'pattern_scores': {},
#                 'pattern_analysis': {
#                     'pattern_count': 0,
#                     'dominant_pattern': {},
#                     'primary_patterns': [],
#                     'complexity_assessment': 'Analysis pending'
#                 },
#                 'success_prediction': {
#                     'overall_success_rate': 85,
#                     'timeline_estimate': '2-3 weeks',
#                     'recommended_sessions': 2
#                 },
#                 'digital_analysis': {},
#                 'is_digital_native': False
#             }
#             st.session_state.is_digital_native = False
        
#         st.rerun()
    
#     def _render_contact_form(self):
#         """Render contact form"""
#         st.markdown("### Assessment complete")
#         st.write("Provide your details to receive your behavioral pattern analysis.")
        
#         with st.form("contact_form"):
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 full_name = st.text_input("Full name*", placeholder="Your full name")
            
#             with col2:
#                 email = st.text_input("Email*", placeholder="your@email.com")
            
#             phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
            
#             urgency = st.selectbox(
#                 "How urgent is your concern?*",
#                 ["Select urgency...", "Extremely urgent - same day", "Very urgent - within 24-48 hours",
#                  "Moderately urgent - within a week", "Not urgent - just exploring"],
#                 index=1
#             )
            
#             primary_concern = st.text_area(
#                 "Primary concern (min 3 characters)",
#                 placeholder="What brought you to this assessment?",
#                 height=100
#             )
            
#             additional_info = st.text_area(
#                 "Additional information (optional)",
#                 placeholder="Any other relevant details...",
#                 height=80
#             )
            
#             st.caption("""
#             **Privacy:** Your responses are confidential and used only for treatment planning. 
#             We do not sell or share your data.
#             """)
            
#             submitted = st.form_submit_button("Get my analysis", type="primary", use_container_width=True)
            
#             if submitted:
#                 errors = self._validate_contact_form(full_name, email, urgency, primary_concern)
                
#                 if not errors:
#                     self._save_contact_and_send_email(
#                         full_name, email, phone, urgency, primary_concern, additional_info
#                     )
#                     st.session_state.contact_provided = True
#                     st.rerun()
#                 else:
#                     for error in errors:
#                         st.error(f"❌ {error}")
    
#     def _validate_contact_form(self, name: str, email: str, urgency: str, concern: str) -> list:
#         """Validate contact form"""
#         errors = []

#         if not name.strip():
#             errors.append("Name is required")

#         if not email.strip():
#             errors.append("Email is required")
#         elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#             errors.append("Valid email required")

#         if concern.strip() and len(concern.strip()) < 3:
#             errors.append("Primary concern must be at least 3 characters if provided")

#         return errors
    
#     def _save_contact_and_send_email(self, name: str, email: str, phone: str, 
#                                      urgency: str, concern: str, additional: str):
#         """Save contact info and send email"""
#         contact_info = {
#             'full_name': name,
#             'email': email,
#             'phone': phone or 'Not provided',
#             'urgency': urgency,
#             'primary_concern': concern,
#             'additional_info': additional or 'None provided',
#             'timestamp': datetime.now().isoformat()
#         }
        
#         st.session_state.contact_info = contact_info
        
#         # Send email if available
#         if EMAIL_AVAILABLE:
#             email_data = {
#                 'contact': contact_info,
#                 'analysis': st.session_state.assessment_results,
#                 'responses': st.session_state.assessment_responses
#             }
            
#             success = send_assessment_email(email_data)
#             if success:
#                 st.success("✅ Assessment sent to clinical team")
#             else:
#                 st.warning("⚠️ Assessment completed but email notification failed")
    
#     def _render_results(self):
#         """Render results page with strategic free preview and premium content"""
        
#         # ✅ NEW: Check if user wants to view full blueprint
#         if st.session_state.get('show_full_blueprint', False):
#             self._render_full_blueprint_page()
#             return
    
#         # Get results data
#         results = st.session_state.assessment_results
#         pattern_analysis = results.get('pattern_analysis', {})
#         success_prediction = results.get('success_prediction', {})
#         digital_analysis = results.get('digital_analysis', {})


#         # ✅ NEW: Check payment status
#         payment_verified = st.session_state.get('payment_verified', False)
        
#         # ====================================================================
#         # ✅ NEW: PREMIUM ACCESS BANNER (if paid)
#         # ====================================================================
#         if payment_verified:
#             st.markdown("""
#             <div style="background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
#                         padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; color: white; text-align: center;">
#                 <h3 style="color: white; margin: 0 0 0.5rem 0;">✅ Premium analysis unlocked</h3>
#                 <p style="margin: 0; font-size: 1.1rem;">Your complete 15-20 page transformation blueprint is ready</p>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Prominent CTA button
#             col1, col2, col3 = st.columns([1, 2, 1])
#             with col2:
#                 if st.button(
#                     "📊 View your complete blueprint",
#                     type="primary",
#                     use_container_width=True,
#                     key="view_blueprint_main"
#                 ):
#                     st.session_state.show_full_blueprint = True
#                     st.rerun()
            


#         dominant = pattern_analysis.get('dominant_pattern', {})
#         primary_patterns = pattern_analysis.get('primary_patterns', [])
#         pattern_count = pattern_analysis.get('pattern_count', 0)
        
#         # Calculate completion rate
#         total_questions = len(self.questions)
#         answered = sum(1 for resp in st.session_state.assessment_responses.values() 
#                     if resp != "Not applicable")
#         completion_rate = (answered / total_questions) * 100 if total_questions > 0 else 0
        
#         # ====================================================================
#         # FREE PREVIEW SECTION
#         # ====================================================================

#         # Success Metrics Display
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.metric("Questions answered", answered)

#         with col2:
#             if completion_rate >= 85:
#                 success_rate = success_prediction.get('overall_success_rate', 85)
#                 st.metric("Success probability", f"{success_rate}%")
#             else:
#                 st.metric("Completion rate", f"{completion_rate:.0f}%")

#         with col3:
#             if completion_rate >= 85:
#                 timeline = success_prediction.get('timeline_estimate', '2 weeks')
#                 st.metric("Timeline estimate", timeline)
#             else:
#                 st.metric("Status", "Manual review")
        
#         # FIXED: Check completion rate
#         if completion_rate < 85:
#             st.warning(f"""
#             **Assessment completion: {completion_rate:.0f}%**
            
#             You've answered {answered} out of {total_questions} questions. For accurate pattern analysis, 
#             we recommend completing at least 85% of the assessment.
#             """)
            
#             st.markdown("""
#             ### Primary pattern: not applicable
            
#             **Insufficient data for automated analysis**
            
#             With the current completion rate, our automated pattern analysis cannot provide 
#             reliable results. However, your responses have been sent to our clinical team.

#             """)

#         else:
#             # ORIGINAL: Full pattern analysis display
#             # Primary Pattern Overview (Surface Level Only)
#             if dominant:
#                 pattern_name = dominant.get('name', 'Unknown')
#                 pattern_score = dominant.get('score', 0)
#                 pattern_severity = dominant.get('severity', 'Unknown')

#                 # Build additional patterns list HTML
#                 additional_patterns_html = ""
#                 if primary_patterns:
#                     additional_patterns_html = "<p style='margin: 1rem 0 0.5rem 0;'><strong>Additional patterns detected:</strong></p><ul style='margin: 0.5rem 0; padding-left: 1.5rem;'>"
#                     for pattern in primary_patterns[:2]:  # Show top 2 only
#                         additional_patterns_html += f"<li>{pattern.get('name', 'Unknown')} ({pattern.get('score', 0):.1f}/10)</li>"
#                     additional_patterns_html += "</ul>"

#                 # Build gradient box for primary pattern
#                 st.markdown(f"""
#                 <div style="background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
#                             padding: 2rem; border-radius: 12px; border-left: 4px solid #4CA1A3; margin-bottom: 2rem;">
#                     <h3 style="color: #273548; margin: 0 0 1rem 0;">Primary pattern identified: {pattern_name}</h3>
#                     <p style="margin: 0.5rem 0;"><strong>Intensity:</strong> {pattern_score:.1f}/10 - {pattern_severity.lower()} impact on daily life</p>
#                     <p style="margin: 0.5rem 0;"><strong>Success probability:</strong> {success_prediction.get('overall_success_rate', 85)}% with specialized intervention</p>
#                     {additional_patterns_html}
#                     <p style="margin: 1rem 0 0 0;">Your assessment reveals {pattern_count} interconnected behavioral patterns that developed as protective mechanisms but now limit your life satisfaction.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             # What This Means (General Impact Only)
#             st.markdown("""
#             ### What this means
            
#             These patterns are consuming significant mental and emotional energy. Your success probability 
#             indicates high likelihood of rapid transformation with proper clinical intervention.
#             """)
            
#             # Digital Analysis Preview (if applicable)
#             if st.session_state.is_digital_native and digital_analysis:
#                 severity = digital_analysis.get('severity_level', 'MINIMAL')
#                 if severity in ['SEVERE', 'MODERATE']:
#                     score = digital_analysis.get('digital_despair_score', 0)
#                     st.markdown(f"""
#                     **Digital conditioning detected:** {score:.0f}% ({severity.lower()})  
#                     Specialized digital-native protocol recommended
#                     """)

#         # ====================================================================
#         # PAYWALL SECTION - Improved UX
#         # ====================================================================

#         if not payment_verified:
#             st.markdown("""
#             ### 🔓 Unlock your complete transformation blueprint
            
#             Your surface-level results are shown above. Get the full 15-20 page clinical analysis 
#             with detailed intervention protocols, behavioral chain mapping, and session-by-session roadmap.
#             """)
            
#             # Paywall Integration
#             if PAYWALL_AVAILABLE:
#                 # NOT in an expander - direct display
#                 self._render_paywall_section()
#             else:
#                 st.info("Complete analysis will be provided during your consultation session")
                
#         # ====================================================================
#         # NEXT STEPS (Always Visible)
#         # ====================================================================
        
#         self._render_next_steps()
        
#     def _render_paywall_section(self):
#         """Render paywall section directly (not in expander)"""
        
#         paywall = create_clinical_paywall()
        
#         # Show what's included
#         st.markdown("""
#         **Included in your 1,000 THB purchase:**
        
#         ✅ **Complete pattern analysis** - All 9 patterns with origins and interconnections  
#         ✅ **Behavioral chain mapping** - Your exact 8-step trigger sequence with intervention points  
#         ✅ **Transformation roadmap** - Session-by-session breakdown customized to your patterns  
#         ✅ **Intervention protocols** - Exact therapeutic language and hypnotic keywords  
#         ✅ **Cost analysis** - 5-year projection if unchanged with ROI calculation  
#         ✅ **Downloadable PDF report** - Complete 15-20 page clinical document  
#         """)
        
#         blueprint_data = {
#             'analysis': st.session_state.assessment_results,
#             'responses': st.session_state.assessment_responses,
#             'contact': st.session_state.get('contact_info', {})
#         }
        
#         paywall.render_paywall_interface(blueprint_data, price_thb=1000)

#     def _render_full_blueprint_page(self):
#         """Render full blueprint as dedicated page"""
        
#         # Header with back button
#         col1, col2, col3 = st.columns([1, 4, 1])
        
#         with col1:
#             if st.button("← Back to results", use_container_width=True):
#                 st.session_state.show_full_blueprint = False
#                 st.rerun()
        
#         with col2:
#             st.markdown("""
#             <div style="text-align: center;">
#                 <h2 style="margin: 0;">Your complete transformation blueprint</h2>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             # PDF download button (placeholder)
#             st.button("📥 Download PDF", use_container_width=True, disabled=True)
    
        
#         # Premium badge
#         st.success("✅ Premium analysis unlocked")
        
#         # Render full blueprint
#         if BLUEPRINT_AVAILABLE:
#             blueprint = create_behavioral_blueprint()
            
#             blueprint_data = {
#                 'master_analytics': st.session_state.assessment_results,
#                 'assessment_responses': st.session_state.assessment_responses,
#                 'contact_info': st.session_state.get('contact_info', {})
#             }
            
#             blueprint.render_complete_blueprint(blueprint_data)
#         else:
#             self._render_premium_fallback()
        
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             if st.button("← Back to results summary", use_container_width=True, type="primary"):
#                 st.session_state.show_full_blueprint = False
#                 st.rerun()

#     # def _render_paywall_or_premium_content(self):
#     #     """Render paywall or premium content if unlocked"""
        
#     #     paywall = create_clinical_paywall()
        
#     #     if paywall.check_payment_status() or st.session_state.premium_access:
#     #         # User has paid - show premium content
#     #         st.success("Premium analysis unlocked")
#     #         self._render_premium_content()
#     #     else:
#     #         # Show paywall
#     #         st.markdown("""
#     #         ### Your complete transformation blueprint
            
#     #         **Included in your 1,000 THB purchase:**
            
#     #         ✅ **Complete pattern analysis** - All 9 patterns with origins and interconnections  
#     #         ✅ **Behavioral chain mapping** - Your exact 8-step trigger sequence with intervention points  
#     #         ✅ **Transformation roadmap** - Session-by-session breakdown customized to your patterns  
#     #         ✅ **Intervention protocols** - Exact therapeutic language and hypnotic keywords  
#     #         ✅ **Cost analysis** - 5-year projection if unchanged with ROI calculation  
#     #         ✅ **Downloadable PDF report** - Complete 15-20 page clinical document  
#     #         """)
            
#     #         # Paywall interface with single price
#     #         blueprint_data = {
#     #             'analysis': st.session_state.assessment_results,
#     #             'responses': st.session_state.assessment_responses,
#     #             'contact': st.session_state.get('contact_info', {})
#     #         }
            
#     #         paywall.render_paywall_interface(blueprint_data, price_thb=1000)
    
#     # def _render_premium_content(self):
#     #     """Render full premium content after payment"""
        
#     #     results = st.session_state.assessment_results
        
#     #     st.markdown("## Your complete transformation blueprint")
        
#     #     if BLUEPRINT_AVAILABLE:
#     #         blueprint = create_behavioral_blueprint()
            
#     #         # FIXED: Use correct keys that blueprint expects
#     #         blueprint_data = {
#     #             'master_analytics': results,  # ✅ Correct key
#     #             'assessment_responses': st.session_state.assessment_responses,  # ✅ Correct key
#     #             'contact_info': st.session_state.get('contact_info', {})  # ✅ Correct key
#     #         }
#     #         blueprint.render_complete_blueprint(blueprint_data)
#     #     else:
#     #         self._render_premium_fallback()
        
#     #     # Section 2: Downloadable PDF
#     #     st.markdown("### Download your report")
        
#     #     st.markdown("""
#     #     **Your complete clinical report includes:**
#     #     - All pattern analysis with detailed origins
#     #     - Complete trigger chain mapping
#     #     - Session-by-session transformation roadmap
#     #     - Intervention protocols and language guides
#     #     - Cost analysis and ROI calculations
#     #     - Progress tracking worksheets
        
#     #     PDF generation will be available in your client portal after consultation scheduling.
#     #     """)
    
#     def _render_premium_fallback(self):
#         """Fallback premium content if blueprint unavailable"""
#         results = st.session_state.assessment_results
#         pattern_analysis = results.get('pattern_analysis', {})
#         clinical_summary = results.get('clinical_summary', {})
#         trigger_chain = results.get('trigger_chain_analysis', {})
#         # Dominant Pattern Details
#         dominant = pattern_analysis.get('dominant_pattern', {})
#         if dominant:
#             pattern_desc = dominant.get('description', {})
            
#             st.markdown(f"""
#             **Pattern: {dominant.get('name', 'Unknown')}**
            
#             **Root structure:** {pattern_desc.get('root_structure', 'Not available')}
            
#             **Core belief:** {pattern_desc.get('core_belief', 'Not available')}
            
#             **Protective function:** {pattern_desc.get('protective_function', 'Not available')}
            
#             **Intervention focus:** {pattern_desc.get('intervention_focus', 'Not available')}
#             """)
        
#         # Clinical Summary
#         st.markdown("### Clinical intervention summary")
        
#         st.markdown(f"""
#         **Session 1 focus:** {clinical_summary.get('session_1_focus', 'Pattern exploration')}
        
#         **Session 2 target:** {clinical_summary.get('session_2_target', 'Core transformation')}
        
#         **Change readiness:** {clinical_summary.get('change_readiness_score', '0/10')}
        
#         **Intervention keywords:** {clinical_summary.get('intervention_keywords', 'Not specified')}
        
#         **Avoid language:** {clinical_summary.get('avoid_language', 'Not specified')}
#         """)
        
#         # Trigger Chain Preview
#         chain = trigger_chain.get('trigger_chain', {})
#         if chain:
#             st.markdown("### Your behavioral sequence")
            
#             sequence_items = [
#                 ("Environmental trigger", chain.get('environmental_trigger')),
#                 ("Physical response", chain.get('physical_response')),
#                 ("Automatic thought", chain.get('automatic_thought')),
#                 ("Emotional response", chain.get('emotional_response')),
#                 ("Behavioral response", chain.get('behavioral_response'))
#             ]
            
#             for label, value in sequence_items:
#                 if value and value != 'Not captured':
#                     st.markdown(f"**{label}:** {value}")
    
#     def _render_next_steps(self):
#         """Render next steps section"""

#         contact_info = st.session_state.get('contact_info', {})
#         urgency = contact_info.get('urgency', '').lower()
#         success_prediction = st.session_state.assessment_results.get('success_prediction', {})
#         recommended_sessions = success_prediction.get('recommended_sessions', 2)

#         # Single consolidated timeline based on urgency
#         if 'extremely urgent' in urgency or 'same day' in urgency:
#             timeline_text = "Priority case: We'll contact you within 24 hours"
#             border_color = "#ef4444"
#         elif 'very urgent' in urgency or '24' in urgency:
#             timeline_text = "High priority: Contact within 24-48 hours"
#             border_color = "#eab308"
#         else:
#             timeline_text = "Standard review: Contact within 48-72 hours"
#             border_color = "#4CA1A3"

#         # Gradient box for next steps
#         st.markdown(f"""
#         <div style="background: linear-gradient(135deg, #E1F0F0 0%, #F8FAFC 100%);
#                     padding: 2rem; border-radius: 12px; border-left: 4px solid {border_color}; margin-bottom: 2rem;">
#             <h3 style="color: #273548; margin: 0 0 1rem 0;">Your next steps</h3>
#             <p style="margin: 0.5rem 0; font-size: 1.1rem;"><strong>{timeline_text}</strong></p>
#             <p style="margin: 1rem 0 0.5rem 0;"><strong>Your protocol:</strong></p>
#             <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                 <li>{recommended_sessions} sessions (90 min each) over {success_prediction.get('timeline_estimate', '2-3 weeks')}</li>
#                 <li>Success probability: {success_prediction.get('overall_success_rate', 85)}%</li>
#                 <li>Licensed therapist will review your assessment and contact you to schedule</li>
#             </ul>
#             <p style="margin: 1.5rem 0 0.5rem 0; font-size: 0.9rem; color: #556D7A;">
#                 <strong>About these results:</strong> This analysis is based on a proprietary behavioral pattern
#                 framework designed to guide hypnotherapy treatment planning. It reflects patterns
#                 commonly observed in clinical practice but is not a validated psychological assessment.
#             </p>
#             <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #556D7A;">
#                 Success rates and timelines are estimates based on clinical experience, not controlled
#                 research studies. Individual outcomes vary significantly.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#         # CTAs
#         st.markdown("### Ready to begin transformation?")

#         col1, col2 = st.columns(2)

#         with col1:
#             st.link_button(
#                 "Schedule consultation",
#                 "https://calendly.com/laetitiasheppard/discovery",
#                 use_container_width=True,
#                 type="primary"
#             )

#         with col2:
#             st.link_button(
#                 "Learn about method",
#                 "https://hypnotherapy.streamlit.app/",
#                 use_container_width=True
#             )

#         # Value reminder
#         st.markdown("""
#         **Investment comparison:**

#         Traditional therapy: 18+ months, 15,000-25,000
#         Specialized hypnotherapy: 2-3 sessions, 3,000-4,000

#         Time to initial results: 48-72 hours vs 3-6 months
#         """)


# # ============================================================================
# # PAGE CLASS
# # ============================================================================
# class AssessPage:
#     """Assessment page wrapper"""
    
#     def __init__(self):
#         self.assessment = ClinicalBehavioralAssessment()
    
#     def render(self):
#         """Render the page"""
#         self.assessment.render()


# def create_assess_page():
#     """Factory function"""
#     return AssessPage()












"""
Enhanced Clinical Behavioral Pattern Assessment
Mobile-optimized with clean design, comprehensive analytics integration

🔄 UPDATED: Integrated enhanced analytics from config_assess.py
   - No UI/UX changes
   - No flow changes
   - Only backend data enrichment
"""

import streamlit as st
from datetime import datetime
import re
from typing import Dict, Any, Optional

# ============================================================================
# COMPONENT IMPORTS
# ============================================================================
# ✅ UPDATED: Import enhanced analytics classes
try:
    from utils.config_assess import (
        AssessmentConfig,
        AnalyticsEngine,
        QuestionRouter,
        ClinicalProfileGenerator,  # 🆕 NEW: For generating clinical reports
        COMPLETE_QUESTION_SET
    )
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    print("WARNING: config_assess not available")

try:
    from utils.email_assess import send_assessment_email
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False
    print("WARNING: email_assess not available")

try:
    from components.blueprint import create_behavioral_blueprint
    BLUEPRINT_AVAILABLE = True
except ImportError:
    BLUEPRINT_AVAILABLE = False

try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False


# ============================================================================
# DESIGN SYSTEM - NO CHANGES
# ============================================================================
def apply_clinical_design_system():
    """Apply professional clinical design system"""
    st.markdown("""
    <style>
        /* Core Design System */
        :root {
            --background: #F3F6F8;
            --card-bg: #FFFFFF;
            --primary-text: #273548;
            --secondary-text: #556D7A;
            --accent: #4CA1A3;
            --accent-hover: #3B7A7A;
            --border: #CBD5E1;
            --success: #22c55e;
            --warning: #eab308;
            --error: #ef4444;
        }
        
        /* Container Optimization */
        .main .block-container {
            padding: 0.75rem 1rem !important;
            max-width: 100% !important;
        }
        
        @media (min-width: 768px) {
            .main .block-container {
                max-width: 600px !important;
                margin: 0 auto;
                padding: 1.5rem !important;
            }
        }
        
        /* Typography System */
        h1 { 
            font-size: 2.2rem !important; 
            color: var(--primary-text) !important;
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
        }
        
        h2 { 
            font-size: 1.8rem !important; 
            color: var(--primary-text) !important;
            font-weight: 600 !important;
            margin: 1.5rem 0 0.75rem 0 !important;
        }
        
        h3, .stMarkdown strong {
            font-size: 1rem !important;
            color: var(--primary-text);
            font-weight: 600 !important;
        }
        
        p, .stMarkdown p {
            font-size: 1rem !important;
            color: var(--primary-text) !important;
            line-height: 1.6 !important;
        }
        
        /* Button System */
        .stButton > button {
            width: 100% !important;
            margin-bottom: 0.25rem !important;
            padding: 0.6rem 1rem !important;
            text-align: left !important;
            background-color: var(--card-bg) !important;
            border: 1px solid var(--border) !important;
            border-radius: 6px !important;
            color: var(--primary-text) !important;
            font-size: 0.95rem !important;
            transition: all 0.2s ease !important;
            line-height: 1.3 !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
        }
        
        .stButton > button:hover {
            background-color: #F8FAFC !important;
            border-color: var(--accent) !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 2px 4px rgba(76,161,163,0.1) !important;
        }
        
        .stButton > button:active {
            background-color: #E1F0F0 !important;
            transform: translateY(0) !important;
        }
        
        /* Primary Button Style */
        .stButton > button[kind="primary"] {
            background-color: var(--accent) !important;
            color: white !important;
            border-color: var(--accent) !important;
            text-align: center !important;
            font-weight: 600 !important;
        }
        
        .stButton > button[kind="primary"]:hover {
            background-color: var(--accent-hover) !important;
            border-color: var(--accent-hover) !important;
        }
        
        /* Progress System */
        .progress-container {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 0.85rem;
            color: var(--secondary-text);
        }
        
        .progress-bar {
            flex: 1;
            height: 4px;
            background: var(--border);
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: var(--accent);
            transition: width 0.3s ease;
        }
        
        /* Input System */
        .stTextArea textarea, .stTextInput input {
            border: 1px solid var(--border) !important;
            border-radius: 6px !important;
            padding: 0.75rem !important;
            font-size: 0.95rem !important;
            background: var(--card-bg) !important;
            color: var(--primary-text) !important;
        }
        
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 1px var(--accent) !important;
        }
        
        /* Slider System */
        .stSlider > div > div > div {
            background-color: var(--accent) !important;
        }
               
        /* Hide Streamlit Branding */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        
        .stDeployButton {
            display: none !important;
        }
        
        footer {
            display: none !important;
        }
        
        /* Mobile Optimization */
        @media (max-width: 767px) {
            .main .block-container {
                padding: 1rem !important;
            }
            
            h1 { font-size: 1.8rem !important; }
            h2 { font-size: 1.5rem !important; }
            
            .stButton > button {
                margin-bottom: 0.2rem !important;
                padding: 0.5rem 0.75rem !important;
            }
            [data-testid="column"] {
                min-width: 30% !important;
                flex-shrink: 0 !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# ASSESSMENT CLASS
# ============================================================================
class ClinicalBehavioralAssessment:
    """Professional clinical assessment with complete integration"""
    
    def __init__(self):
        self._init_session_state()
        
        if CONFIG_AVAILABLE:
            self.config = AssessmentConfig()
            self.analytics = self.config.get_analytics_engine()
            self.router = self.config.get_question_router()
            self.questions = COMPLETE_QUESTION_SET
        else:
            self.analytics = None
            self.router = None
            self.questions = []
    
    def _init_session_state(self):
        """Initialize session state"""
        defaults = {
            'assessment_responses': {},
            'current_question_index': 0,
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'is_digital_native': False,
            'show_blueprint': False,
            'premium_access': False,
            'disclaimer_accepted': False 
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    def render(self):
        """Main render method - FIXED with comprehensive error handling"""
        try:
            apply_clinical_design_system()
            
            if not CONFIG_AVAILABLE:
                st.error("Assessment configuration not available. Please check utils/config_assess.py")
                return
            
            self._render_header()
            
            # FIXED: Better state validation
            if not st.session_state.contact_provided:
                if not st.session_state.assessment_completed:
                    self._render_assessment()
                else:
                    # FIXED: Add validation before rendering contact form
                    if not hasattr(st.session_state, 'assessment_responses') or not st.session_state.assessment_responses:
                        st.error("Assessment data not found. Please restart the assessment.")
                        if st.button("Restart assessment"):
                            for key in ['assessment_responses', 'current_question_index', 'assessment_completed', 
                                    'contact_provided', 'assessment_results']:
                                if key in st.session_state:
                                    del st.session_state[key]
                            st.rerun()
                    else:
                        self._render_contact_form()
            else:
                self._render_results()
        
        except Exception as e:
            st.error("An error occurred in the assessment.")
            
            # Show user-friendly error
            st.error(f"Error details: {str(e)}")
            
            # Debug information in expander
            import traceback
            with st.expander("🔧 Debug information (for support)"):
                st.code(traceback.format_exc())
                st.write("**Session state:**")
                st.json({
                    'assessment_completed': st.session_state.get('assessment_completed', False),
                    'contact_provided': st.session_state.get('contact_provided', False),
                    'responses_count': len(st.session_state.get('assessment_responses', {})),
                    'current_index': st.session_state.get('current_question_index', 0)
                })
            
            # Offer restart option
            if st.button("Restart assessment", type="primary"):
                for key in list(st.session_state.keys()):
                    if key.startswith('assessment') or key in ['contact_provided', 'current_question_index']:
                        del st.session_state[key]
                st.rerun()
        
    def _render_disclaimer_page(self):
        """Render disclaimer and acceptance page before assessment starts"""
        
        # Critical disclaimer box
        st.warning("""
        ⚠️ **Before you begin, please review this important information**
        
        This is a **proprietary framework** developed for hypnotherapy session planning. 
        
        **This assessment:**
        - Does not diagnose mental health conditions
        - Is not a substitute for professional psychiatric or psychological care
        - Should be used alongside, not instead of, evidence-based treatment
        """)
        
        # What this is for
        st.markdown("### What this assessment is designed for")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: #E1F0F0; padding: 1.5rem; border-radius: 8px; 
                        border-left: 4px solid #22c55e; height: 100%;">
                <h6 style="color: #22c55e; margin-top: 0;">✓ This is appropriate for:</h4>
                <ul style="color: #273548; line-height: 1.8;">
                    <li>Exploring behavioral patterns you'd like to change</li>
                    <li>Planning focused hypnotherapy intervention</li>
                    <li>Complementing existing therapy</li>
                    <li>Personal insight and self-awareness</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: #FEF3C7; padding: 1.5rem; border-radius: 8px; 
                        border-left: 4px solid #F59E0B; height: 100%;">
                <h6 style="color: #F59E0B; margin-top: 0;">✗ This is NOT appropriate for:</h4>
                <ul style="color: #273548; line-height: 1.8;">
                    <li>Diagnosing mental health conditions</li>
                    <li>Replacing professional psychiatric care</li>
                    <li>Crisis intervention or severe mental illness</li>
                    <li>Medical or clinical decision-making</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        
        # Crisis resources
        st.error("""
        🆘 **If you're experiencing a mental health crisis:**
        
        - **Thailand Mental Health Hotline:** 1323 (24/7)
        - **Samaritans of Thailand:** 02-713-6793 (24/7)  
        - **Emergency Services:** 1669
        
        Please seek immediate professional help if you're experiencing thoughts of self-harm, 
        severe depression, or psychological crisis.
        """)

        
        # Assessment details
        st.markdown("### What to expect")
        
        st.info("""
        **Assessment details:**
        - Approximately 90-100 questions
        - Takes 20-30 minutes to complete
        - You can go back and change answers
        - Your responses are confidential
        - Results are for treatment planning purposes only
        
        **After completion:**
        - Receive behavioral pattern analysis
        - Get personalized intervention suggestions
        - Licensed therapist will review your assessment
        - Schedule consultation to discuss results
        """)

        
        # Acceptance section
        st.markdown("### Your acknowledgment")
        
        accept1 = st.checkbox(
            "I understand this is a proprietary assessment framework, not a clinical diagnostic tool",
            key="accept_proprietary"
        )
        
        accept2 = st.checkbox(
            "I understand this assessment does not replace professional mental health care",
            key="accept_not_replacement"
        )
        
        accept3 = st.checkbox(
            "I am not currently experiencing a mental health crisis requiring immediate intervention",
            key="accept_not_crisis"
        )
        
        st.markdown("  ")
        
        # Continue button - only enabled if all accepted
        all_accepted = accept1 and accept2 and accept3
        
        if all_accepted:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Begin assessment", type="primary", width='stretch'):
                    st.session_state.disclaimer_accepted = True
                    st.rerun()
        else:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.button("Begin assessment", type="primary", width='stretch', disabled=True)
            st.caption("Please check all boxes above to continue")
        
        st.markdown("  ")
        st.markdown("  ")
        
        # Footer
        st.caption("""
        **Privacy notice:** Your responses are confidential and used only for treatment planning. 
        We do not sell or share your personal information.
        """)

    def _render_header(self):
        """Render clean header"""
        st.markdown("**BEHAVIORAL ASSESSMENT**")        
        st.markdown("  ")
    
    def _render_assessment(self):
        # Check if disclaimer accepted
        if not st.session_state.get('disclaimer_accepted', False):
            self._render_disclaimer_page()
            return
        
        """Render assessment questions"""
        current_index = st.session_state.current_question_index
        
        if current_index >= len(self.questions):
            self._complete_assessment()
            return
        
        question = self.questions[current_index]
        total_questions = len(self.questions)
        
        # Progress bar
        progress = current_index / total_questions if total_questions > 0 else 0
        st.markdown(f"""
        <div class="progress-container">
            <span><strong>Q {current_index + 1}/{total_questions}</strong></span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span><strong>{int(progress * 100)}%</strong></span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("  ")
        
        # Question text with gradient info box
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E1F0F0 0%, #F8FAFC 100%); 
                    padding: 1rem; border-radius: 8px; border-left: 4px solid #4CA1A3; 
                    margin-bottom: 1.5rem;">
            <h3 style="color: #000 !important; margin: 0 0 0.5rem 0; font-size: 1.2rem;">
                {question['text']}
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Render question type
        self._render_question_type(question)
        
        # Navigation
        self._render_navigation(current_index)
    
    def _render_question_type(self, question: Dict):
        """Render different question types with previous answer memory"""
        qtype = question['type']
        qid = question['id']
        question_text = question['text']
        
        # Check if question was previously answered
        previous_answer = st.session_state.assessment_responses.get(qid)
        
        if qtype == 'single_choice':
            options = question['options']
            for i, option in enumerate(options):
                # Highlight previous answer if exists
                button_type = "primary" if previous_answer == option else "secondary"
                if st.button(option, key=f"q_{qid}_opt_{i}", width='stretch', type=button_type):
                    self._save_response(qid, option)
                    self._advance_question()
                    st.rerun()
        
        elif qtype == 'slider':
            min_val = question.get('min', 0)
            max_val = question.get('max', 10)
            default = question.get('default', 5)
            
            # Use previous answer if available
            initial_value = previous_answer if previous_answer is not None else default
            
            value = st.slider(
                question_text,
                min_value=min_val,
                max_value=max_val,
                value=int(initial_value),  # Ensure it's an integer
                key=f"slider_{qid}",
                label_visibility="collapsed"
            )
            
            if st.button("Continue", key=f"continue_{qid}", type="primary", width='stretch'):
                self._save_response(qid, value)
                self._advance_question()
                st.rerun()
        
        elif qtype == 'text_completion':
            placeholder = question.get('placeholder', 'Your response...')
            min_chars = question.get('min_chars', 3)

            # Use previous answer if available
            initial_text = previous_answer if previous_answer else ""

            response = st.text_area(
                question_text,
                value=initial_text,  # Pre-fill with previous answer
                placeholder=placeholder,
                key=f"text_{qid}",
                height=100,
                label_visibility="collapsed"
            )

            # Always show button, but enable/disable based on validation
            response_valid = response.strip() and len(response.strip()) >= min_chars

            # Show character count/requirement
            if response.strip():
                char_count = len(response.strip())
                if char_count < min_chars:
                    st.caption(f"⚠️ {char_count}/{min_chars} characters (minimum required)")
                else:
                    st.caption(f"✓ {char_count} characters")
            else:
                st.caption(f"Minimum {min_chars} characters required")

            # Continue button - always visible
            if st.button(
                "Continue",
                key=f"continue_{qid}",
                type="primary",
                width='stretch',
                disabled=not response_valid
            ):
                self._save_response(qid, response.strip())
                self._advance_question()
                st.rerun()

        elif qtype == 'forced_choice_dyad':
            # Binary forced choice questions (A vs B)
            options = question.get('options', [])

            if len(options) >= 2:
                # Show as two prominent buttons
                for i, option in enumerate(options):
                    # Highlight previous answer if exists
                    button_type = "primary" if previous_answer == option else "secondary"
                    if st.button(option, key=f"q_{qid}_dyad_{i}", width='stretch', type=button_type):
                        self._save_response(qid, option)
                        self._advance_question()
                        st.rerun()
            else:
                st.error("Forced choice question must have at least 2 options")

        elif qtype == 'ranking':
            # Ranking questions - select top 3 in order
            options = question.get('options', [])
            rank_count = question.get('rank_count', 3)

            # Initialize or get previous rankings
            current_rankings = previous_answer if previous_answer and isinstance(previous_answer, list) else []

            st.caption(f"Select your top {rank_count} choices in order of importance:")

            # Show ranking interface
            for rank_position in range(rank_count):
                rank_label = ["1st", "2nd", "3rd", "4th", "5th"][rank_position]

                # Filter out already selected options
                available_options = ["(Select option)"] + [opt for opt in options if opt not in current_rankings or
                                                           (rank_position < len(current_rankings) and opt == current_rankings[rank_position])]

                # Get current selection for this position
                current_selection = current_rankings[rank_position] if rank_position < len(current_rankings) else "(Select option)"
                default_index = available_options.index(current_selection) if current_selection in available_options else 0

                selected = st.selectbox(
                    f"{rank_label} choice:",
                    options=available_options,
                    index=default_index,
                    key=f"rank_{qid}_{rank_position}"
                )

                # Update current rankings
                if selected != "(Select option)":
                    if rank_position < len(current_rankings):
                        current_rankings[rank_position] = selected
                    else:
                        current_rankings.append(selected)
                elif rank_position < len(current_rankings):
                    current_rankings = current_rankings[:rank_position]

            # Continue button - enabled when all ranks are selected
            all_ranked = len(current_rankings) == rank_count and "(Select option)" not in current_rankings

            if st.button(
                "Continue",
                key=f"continue_rank_{qid}",
                type="primary",
                width='stretch',
                disabled=not all_ranked
            ):
                self._save_response(qid, current_rankings)
                self._advance_question()
                st.rerun()

            if not all_ranked:
                st.caption(f"Please select all {rank_count} choices to continue")

    def _render_navigation(self, current_index: int):
        """Render navigation buttons"""
        # Get current question from index to access question['id']
        question = self.questions[current_index]
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_index > 0:
                if st.button("← Back", key="nav_back", width='stretch'):
                    self._go_back()
                    st.rerun()
        
        with col2:
            # Count only non-skipped responses
            answered = sum(1 for resp in st.session_state.assessment_responses.values() 
                        if resp != "Not applicable")
            st.markdown(f"""
            <div style="text-align: center; padding: 0.5rem; color: #556D7A; font-size: 0.85rem;">
                <strong>{answered}</strong> answered
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            if st.button("Skip", key="nav_skip", width='stretch'):
                self._save_response(question['id'], "Not applicable")
                self._advance_question()
                st.rerun()
    
    def _save_response(self, qid: int, response: Any):
        """Save response"""
        st.session_state.assessment_responses[qid] = response
    
    def _advance_question(self):
        """Advance to next question"""
        st.session_state.current_question_index += 1
    
    def _go_back(self):
        """Go back to previous question - preserves previous answers"""
        if st.session_state.current_question_index > 0:
            st.session_state.current_question_index -= 1
            # Answer is preserved in session_state for when user returns
    
    # ========================================================================
    # 🔄 CHANGE #1: Complete Assessment - Updated Method Call
    # ========================================================================
    def _complete_assessment(self):
        """
        Complete assessment and generate analysis
        
        🔄 UPDATED: Now calls generate_complete_analytics() with direct responses
        ❌ OLD: generate_complete_analysis(assessment_data)
        ✅ NEW: generate_complete_analytics(responses)
        """
        
        # FIXED: Validate we have responses
        if not st.session_state.assessment_responses:
            st.error("No responses found. Please complete at least one question.")
            return
        
        st.session_state.assessment_completed = True
        
        try:
            if self.analytics:
                # ✅ UPDATED: Call enhanced analytics directly with responses dict
                analysis = self.analytics.generate_complete_analytics(
                    st.session_state.assessment_responses  # Direct responses, not wrapped
                )
                
                st.session_state.assessment_results = analysis
                
                # Extract is_digital_native from new structure
                digital_analysis = analysis.get('digital_analysis', {})
                st.session_state.is_digital_native = digital_analysis.get('is_digital_native', False)
                
            else:
                # Fallback if analytics not available
                st.session_state.assessment_results = {
                    'pattern_scores': {},
                    'pattern_hierarchy': {},  # ✅ UPDATED KEY
                    'success_prediction': {'overall_success_rate': 85},
                    'digital_analysis': {},
                    'is_digital_native': False
                }
                st.session_state.is_digital_native = False
                
        except Exception as e:
            # Log error but continue to contact form with fallback data
            print(f"Analytics generation error: {str(e)}")
            import traceback
            print(traceback.format_exc())
            
            # ✅ UPDATED: Fallback structure with new keys
            st.session_state.assessment_results = {
                'error': str(e),
                'pattern_scores': {},
                'pattern_hierarchy': {  # ✅ UPDATED KEY
                    'pattern_count': 0,
                    'dominant_pattern': {},
                    'primary_patterns': [],
                    'complexity_assessment': 'Analysis pending'
                },
                'success_prediction': {
                    'overall_success_rate': 85,
                    'timeline_estimate': '2-3 weeks',
                    'recommended_sessions': 2
                },
                'digital_analysis': {},
                'trigger_sequence': {},  # 🆕 NEW
                'constellation_analysis': {},  # 🆕 NEW
                'hidden_barriers': {},  # 🆕 NEW
                'readiness_analysis': {},  # 🆕 NEW
                'session_prediction': {},  # 🆕 NEW
                'is_digital_native': False
            }
            st.session_state.is_digital_native = False
        
        st.rerun()
    
    def _render_contact_form(self):
        """Render contact form"""
        st.markdown("### Assessment complete")
        st.write("Provide your details to receive your behavioral pattern analysis.")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                full_name = st.text_input("Full name*", placeholder="Your full name")
            
            with col2:
                email = st.text_input("Email*", placeholder="your@email.com")
            
            phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
            
            urgency = st.selectbox(
                "How urgent is your concern?*",
                ["Select urgency...", "Extremely urgent - same day", "Very urgent - within 24-48 hours",
                 "Moderately urgent - within a week", "Not urgent - just exploring"],
                index=1
            )
            
            primary_concern = st.text_area(
                "Primary concern (min 3 characters)",
                placeholder="What brought you to this assessment?",
                height=100
            )
            
            additional_info = st.text_area(
                "Additional information (optional)",
                placeholder="Any other relevant details...",
                height=80
            )
            
            st.caption("""
            **Privacy:** Your responses are confidential and used only for treatment planning. 
            We do not sell or share your data.
            """)
            
            submitted = st.form_submit_button("Get my analysis", type="primary", width='stretch')
            
            if submitted:
                errors = self._validate_contact_form(full_name, email, urgency, primary_concern)
                
                if not errors:
                    self._save_contact_and_send_email(
                        full_name, email, phone, urgency, primary_concern, additional_info
                    )
                    st.session_state.contact_provided = True
                    st.rerun()
                else:
                    for error in errors:
                        st.error(f"❌ {error}")
    
    def _validate_contact_form(self, name: str, email: str, urgency: str, concern: str) -> list:
        """Validate contact form"""
        errors = []

        if not name.strip():
            errors.append("Name is required")

        if not email.strip():
            errors.append("Email is required")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append("Valid email required")

        if concern.strip() and len(concern.strip()) < 3:
            errors.append("Primary concern must be at least 3 characters if provided")

        return errors
    
    def _save_contact_and_send_email(self, name: str, email: str, phone: str, 
                                     urgency: str, concern: str, additional: str):
        """Save contact info and send email"""
        contact_info = {
            'full_name': name,
            'email': email,
            'phone': phone or 'Not provided',
            'urgency': urgency,
            'primary_concern': concern,
            'additional_info': additional or 'None provided',
            'timestamp': datetime.now().isoformat()
        }
        
        st.session_state.contact_info = contact_info
        
        # Send email if available
        if EMAIL_AVAILABLE:
            email_data = {
                'contact': contact_info,
                'analysis': st.session_state.assessment_results,
                'responses': st.session_state.assessment_responses
            }
            
            success = send_assessment_email(email_data)
            if success:
                st.success("✅ Assessment sent to clinical team")
            else:
                st.warning("⚠️ Assessment completed but email notification failed")
    
    # ========================================================================
    # 🔄 CHANGE #2: Render Results - Updated Key Names
    # ========================================================================
    def _render_results(self):
        """
        Render results page with strategic free preview and premium content
        
        🔄 UPDATED: Changed key from 'pattern_analysis' to 'pattern_hierarchy'
        """
        
        # ✅ NEW: Check if user wants to view full blueprint
        if st.session_state.get('show_full_blueprint', False):
            self._render_full_blueprint_page()
            return
    
        # Get results data
        results = st.session_state.assessment_results
        
        # ✅ UPDATED: Use 'pattern_hierarchy' instead of 'pattern_analysis'
        pattern_analysis = results.get('pattern_hierarchy', {})  # 🔄 CHANGED KEY
        
        success_prediction = results.get('success_prediction', {})
        digital_analysis = results.get('digital_analysis', {})

        # ✅ NEW: Check payment status
        payment_verified = st.session_state.get('payment_verified', False)
        
        # ====================================================================
        # ✅ NEW: PREMIUM ACCESS BANNER (if paid)
        # ====================================================================
        if payment_verified:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
                        padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; color: white; text-align: center;">
                <h3 style="color: white; margin: 0 0 0.5rem 0;">✅ Premium analysis unlocked</h3>
                <p style="margin: 0; font-size: 1.1rem;">Your complete 15-20 page transformation blueprint is ready</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Prominent CTA button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(
                    "📊 View your complete blueprint",
                    type="primary",
                    width='stretch',
                    key="view_blueprint_main"
                ):
                    st.session_state.show_full_blueprint = True
                    st.rerun()

        dominant = pattern_analysis.get('dominant_pattern', {})
        primary_patterns = pattern_analysis.get('primary_patterns', [])
        pattern_count = pattern_analysis.get('pattern_count', 0)

        # Calculate completion rate (excluding text_completion questions)
        # Only count non-text-completion questions for completion threshold
        non_text_questions = [q for q in self.questions if q.get('type') != 'text_completion']
        total_non_text_questions = len(non_text_questions)

        # Count answered non-text-completion questions
        answered_non_text = sum(
            1 for qid, resp in st.session_state.assessment_responses.items()
            if resp != "Not applicable" and any(q['id'] == qid and q.get('type') != 'text_completion' for q in self.questions)
        )

        # Total answered (all types for display)
        answered = sum(1 for resp in st.session_state.assessment_responses.values()
                    if resp != "Not applicable")

        # Completion rate based on non-text-completion questions only
        completion_rate = (answered_non_text / total_non_text_questions) * 100 if total_non_text_questions > 0 else 0
        
        # ====================================================================
        # FREE PREVIEW SECTION
        # ====================================================================

        # Success Metrics Display
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Questions answered", answered)

        with col2:
            if completion_rate >= 80:
                success_rate = success_prediction.get('overall_success_rate', 85)
                st.metric("Success probability", f"{success_rate}%")
            else:
                st.metric("Completion rate", f"{completion_rate:.0f}%")

        with col3:
            if completion_rate >= 80:
                timeline = success_prediction.get('timeline_estimate', '2 weeks')
                st.metric("Timeline estimate", timeline)
            else:
                st.metric("Status", "Manual review")

        # Check completion rate (based on non-text-completion questions)
        if completion_rate < 80:
            st.warning(f"""
            **Assessment completion: {completion_rate:.0f}%**

            You've answered {answered_non_text} of {total_non_text_questions} required questions
            (excluding optional text responses). For accurate pattern analysis,
            we recommend completing at least 80% of the core assessment questions.
            """)
            
            st.markdown("""
            ### Primary pattern: not applicable
            
            **Insufficient data for automated analysis**
            
            With the current completion rate, our automated pattern analysis cannot provide 
            reliable results. However, your responses have been sent to our clinical team.

            """)

        else:
            # ORIGINAL: Full pattern analysis display
            # Primary Pattern Overview (Surface Level Only)
            if dominant:
                pattern_name = dominant.get('name', 'Unknown')
                pattern_score = dominant.get('score', 0)
                pattern_severity = dominant.get('severity', 'Unknown')

                # Build additional patterns list HTML
                additional_patterns_html = ""
                if primary_patterns:
                    additional_patterns_html = "<p style='margin: 1rem 0 0.5rem 0;'><strong>Additional patterns detected:</strong></p><ul style='margin: 0.5rem 0; padding-left: 1.5rem;'>"
                    for pattern in primary_patterns[:2]:  # Show top 2 only
                        additional_patterns_html += f"<li>{pattern.get('name', 'Unknown')} ({pattern.get('score', 0):.1f}/10)</li>"
                    additional_patterns_html += "</ul>"

                # Build gradient box for primary pattern
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
                            padding: 2rem; border-radius: 12px; border-left: 4px solid #4CA1A3; margin-bottom: 2rem;">
                    <h3 style="color: #273548; margin: 0 0 1rem 0;">Primary pattern identified: {pattern_name}</h3>
                    <p style="margin: 0.5rem 0;"><strong>Intensity:</strong> {pattern_score:.1f}/10 - {pattern_severity.lower()} impact on daily life</p>
                    <p style="margin: 0.5rem 0;"><strong>Success probability:</strong> {success_prediction.get('overall_success_rate', 85)}% with specialized intervention</p>
                    {additional_patterns_html}
                    <p style="margin: 1rem 0 0 0;">Your assessment reveals {pattern_count} interconnected behavioral patterns that developed as protective mechanisms but now limit your life satisfaction.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # What This Means (General Impact Only)
            st.markdown("""
            ### What this means
            
            These patterns are consuming significant mental and emotional energy. Your success probability 
            indicates high likelihood of rapid transformation with proper clinical intervention.
            """)
            
            # Digital Analysis Preview (if applicable)
            if st.session_state.is_digital_native and digital_analysis:
                severity = digital_analysis.get('severity_level', 'MINIMAL')
                if severity in ['SEVERE', 'MODERATE']:
                    score = digital_analysis.get('digital_despair_score', 0)
                    st.markdown(f"""
                    **Digital conditioning detected:** {score:.0f}% ({severity.lower()})  
                    Specialized digital-native protocol recommended
                    """)

        # ====================================================================
        # PAYWALL SECTION - Improved UX
        # ====================================================================

        if not payment_verified:
            # Paywall Integration
            if PAYWALL_AVAILABLE:
                with st.expander("**🔓 Unlock your complete transformation blueprint - 1,000 THB**", expanded=False):
                    st.markdown("""
                    Your surface-level results are shown above. Get the full 15-20 page clinical analysis
                    with detailed intervention protocols, behavioral chain mapping, and session-by-session roadmap.
                    """)
                    self._render_paywall_section()
            else:
                st.info("Complete analysis will be provided during your consultation session")
                
        # ====================================================================
        # NEXT STEPS (Always Visible)
        # ====================================================================
        
        self._render_next_steps()
        
    def _render_paywall_section(self):
        """Render paywall section directly (not in expander)"""
        
        paywall = create_clinical_paywall()
        
        # Show what's included
        st.markdown("""
        **Included in your 1,000 THB purchase:**
        
        ✅ **Complete pattern analysis** - All 9 patterns with origins and interconnections  
        ✅ **Behavioral chain mapping** - Your exact 8-step trigger sequence with intervention points  
        ✅ **Transformation roadmap** - Session-by-session breakdown customized to your patterns  
        ✅ **Intervention protocols** - Exact therapeutic language and hypnotic keywords  
        ✅ **Cost analysis** - 5-year projection if unchanged with ROI calculation  
        ✅ **Downloadable PDF report** - Complete 15-20 page clinical document  
        """)
        
        blueprint_data = {
            'analysis': st.session_state.assessment_results,
            'responses': st.session_state.assessment_responses,
            'contact': st.session_state.get('contact_info', {})
        }
        
        paywall.render_paywall_interface(blueprint_data, price_thb=1000)

    def _render_full_blueprint_page(self):
        """Render full blueprint as dedicated page"""
        
        # Header with back button
        col1, col2, col3 = st.columns([1, 4, 1])
        
        with col1:
            if st.button("← Back to results", width='stretch'):
                st.session_state.show_full_blueprint = False
                st.rerun()
        
        with col2:
            st.markdown("""
            <div style="text-align: center;">
                <h2 style="margin: 0;">Your complete transformation blueprint</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # PDF download button (placeholder)
            st.button("📥 Download PDF", width='stretch', disabled=True)
    
        
        # Premium badge
        st.success("✅ Premium analysis unlocked")
        
        # Render full blueprint
        if BLUEPRINT_AVAILABLE:
            blueprint = create_behavioral_blueprint()
            
            blueprint_data = {
                'master_analytics': st.session_state.assessment_results,
                'assessment_responses': st.session_state.assessment_responses,
                'contact_info': st.session_state.get('contact_info', {})
            }
            
            blueprint.render_complete_blueprint(blueprint_data)
        else:
            self._render_premium_fallback()
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("← Back to results summary", width='stretch', type="primary"):
                st.session_state.show_full_blueprint = False
                st.rerun()

    # ========================================================================
    # 🔄 CHANGE #3: Premium Fallback - Enhanced Data Access
    # ========================================================================
    def _render_premium_fallback(self):
        """
        Fallback premium content if blueprint unavailable
        
        🔄 UPDATED: Now accesses enhanced analytics data
        ✅ Display stays the same, but pulls from richer sources
        """
        results = st.session_state.assessment_results
        
        # ✅ UPDATED: Use pattern_hierarchy instead of pattern_analysis
        pattern_hierarchy = results.get('pattern_hierarchy', {})
        
        # 🆕 NEW: Access enhanced analytics
        trigger_sequence = results.get('trigger_sequence', {})
        constellation = results.get('constellation_analysis', {})
        hidden_barriers = results.get('hidden_barriers', {})
        readiness = results.get('readiness_analysis', {})
        session_plan = results.get('session_prediction', {})
        digital_interplay = results.get('digital_interplay', {})
        
        # Dominant Pattern Details (same display, richer data)
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        if dominant:
            pattern_desc = dominant.get('description', {})
            
            st.markdown(f"""
            **Pattern: {dominant.get('name', 'Unknown')}**
            
            **Root structure:** {pattern_desc.get('root_structure', 'Not available')}
            
            **Core belief:** {pattern_desc.get('core_belief', 'Not available')}
            
            **Protective function:** {pattern_desc.get('protective_function', 'Not available')}
            
            **Intervention focus:** {pattern_desc.get('intervention_focus', 'Not available')}
            """)
        
        # 🆕 NEW: Show enhanced trigger sequence if available
        if trigger_sequence:
            chain = trigger_sequence.get('trigger_sequence', {})
            completeness = trigger_sequence.get('sequence_completeness', 0)
            intervention_windows = trigger_sequence.get('intervention_windows', [])
            
            st.markdown("### Your behavioral sequence")
            st.markdown(f"**Sequence completeness:** {completeness:.0f}%")
            
            sequence_items = [
                ("Environmental trigger", chain.get('environmental_trigger')),
                ("Physical response", chain.get('physical_response')),
                ("Automatic thought", chain.get('automatic_thought')),
                ("Emotional response", chain.get('emotional_response')),
                ("Behavioral response", chain.get('behavioral_response')),
                ("Immediate consequence", chain.get('immediate_consequence'))
            ]
            
            for label, value in sequence_items:
                if value and value != 'Not captured':
                    st.markdown(f"**{label}:** {value}")
            
            if intervention_windows:
                st.markdown("**Intervention windows:**")
                for window in intervention_windows:
                    st.markdown(f"- {window.get('description', window)}")
        
        # 🆕 NEW: Pattern constellation info
        if constellation:
            multiplier = constellation.get('constellation_multiplier', 1.0)
            if multiplier > 1.0:
                st.markdown(f"""
                ### Pattern constellation
                
                **Amplification factor:** {multiplier}x
                
                Your patterns are reinforcing each other, creating a {multiplier}x complexity multiplier.
                This requires careful sequencing in the intervention protocol.
                """)
        
        # 🆕 NEW: Hidden barriers preview
        if hidden_barriers:
            secondary_gain = hidden_barriers.get('secondary_gain', '')
            resistance_type = hidden_barriers.get('resistance_type', '')
            
            if secondary_gain and secondary_gain != 'Not identified':
                st.markdown(f"""
                ### What this pattern protects
                
                **Secondary gain:** {secondary_gain[:200]}...
                
                **Resistance type:** {resistance_type}
                """)
        
        # 🆕 NEW: Readiness scoring
        if readiness:
            composite_score = readiness.get('composite_readiness', 5)
            readiness_stage = readiness.get('readiness_stage', 'Unknown')
            
            st.markdown(f"""
            ### Change readiness
            
            **Readiness score:** {composite_score:.1f}/10
            
            **Current stage:** {readiness_stage}
            """)
        
        # 🆕 NEW: Session complexity prediction
        if session_plan:
            complexity_score = session_plan.get('complexity_score', 0)
            session_3_prob = session_plan.get('session_3_probability', 'Unknown')
            
            st.markdown(f"""
            ### Session planning
            
            **Complexity score:** {complexity_score:.1f}/15
            
            **Session 3 probability:** {session_3_prob}
            
            **Reason:** {session_plan.get('structure_reason', 'Based on pattern complexity')}
            """)
    
    def _render_next_steps(self):
        """Render next steps section"""

        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '').lower()
        success_prediction = st.session_state.assessment_results.get('success_prediction', {})
        recommended_sessions = success_prediction.get('recommended_sessions', 2)

        # Single consolidated timeline based on urgency
        if 'extremely urgent' in urgency or 'same day' in urgency:
            timeline_text = "Priority case: We'll contact you within 24 hours"
            border_color = "#ef4444"
            gradient_start = "#fee2e2"  # Light red tint
        elif 'very urgent' in urgency or '24' in urgency:
            timeline_text = "High priority: Contact within 24-48 hours"
            border_color = "#eab308"
            gradient_start = "#fef3c7"  # Light yellow tint
        else:
            timeline_text = "Standard review: Contact within 48-72 hours"
            border_color = "#4CA1A3"
            gradient_start = "#E1F0F0"  # Light teal tint

        # Gradient box for next steps - gradient derives from urgency color
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {gradient_start} 0%, #F8FAFC 100%);
                    padding: 2rem; border-radius: 12px; border-left: 4px solid {border_color}; margin-bottom: 2rem;">
            <h3 style="color: #273548; margin: 0 0 1rem 0;">Your next steps</h3>
            <p style="margin: 0.5rem 0; font-size: 1.1rem;"><strong>{timeline_text}</strong></p>
            <p style="margin: 1rem 0 0.5rem 0;"><strong>Your protocol:</strong></p>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                <li>{recommended_sessions} sessions (90 min each) over {success_prediction.get('timeline_estimate', '2-3 weeks')}</li>
                <li>Success probability: {success_prediction.get('overall_success_rate', 85)}%</li>
                <li>Licensed therapist will review your assessment and contact you to schedule</li>
            </ul>
            <p style="margin: 1.5rem 0 0.5rem 0; font-size: 0.9rem; color: #556D7A;">
                <strong>About these results:</strong> This analysis is based on a proprietary behavioral pattern
                framework designed to guide hypnotherapy treatment planning. It reflects patterns
                commonly observed in clinical practice but is not a validated psychological assessment.
            </p>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #556D7A;">
                Success rates and timelines are estimates based on clinical experience, not controlled
                research studies. Individual outcomes vary significantly.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # CTAs
        st.markdown("### Ready to begin transformation?")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button(
                "Schedule consultation",
                "https://calendly.com/laetitiasheppard/discovery",
                width='stretch',
                type="primary"
            )

        with col2:
            st.link_button(
                "Learn about method",
                "https://hypnotherapy.streamlit.app/",
                width='stretch'
            )

        # Value reminder
        st.markdown("""
        **Investment comparison:**

        Traditional therapy: 18+ months, ฿15,000-25,000  
        Specialized hypnotherapy: 2-3 sessions, ฿3,000-4,000

        Time to initial results: 48-72 hours vs 3-6 months
        """)


# ============================================================================
# PAGE CLASS - NO CHANGES
# ============================================================================
class AssessPage:
    """Assessment page wrapper"""
    
    def __init__(self):
        self.assessment = ClinicalBehavioralAssessment()
    
    def render(self):
        """Render the page"""
        self.assessment.render()


def create_assess_page():
    """Factory function"""
    return AssessPage()
