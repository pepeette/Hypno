# """
# COMPREHENSIVE ASSESSMENT - PRODUCTION VERSION
# ===========================================
# Enhanced Behavioral Pattern Assessment v2 with comprehensive clinical profiling
# User-friendly assessment with beautiful styling and detailed behavioral analysis

# Author: Assessment Enhancement Team
# Version: 3.0.0 - Production Ready
# Date: 2025-01-25
# """

# import streamlit as st
# import sys
# import os
# import datetime

# # Add the utils directory to the path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

# try:
#     from utils.config import EnhancedAssessmentConfig, QuestionnaireStage
# except ImportError as e:
#     st.error(f"Import error: {e}")
#     st.error("Make sure all enhancement modules are available")
#     st.stop()

# # Page configuration
# st.set_page_config(
#     page_title="Comprehensive Assessment - Production Version",
#     page_icon="🎯",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Add comprehensive CSS styling
# st.markdown("""
#     <style>
#     /* Enhanced Assessment Styling with Consistent Layout */
#     .assessment-container {
#         max-width: 800px;
#         margin: 0 auto;
#         padding: 0.5rem;
#         display: flex;
#         flex-direction: column;
#         min-height: calc(100vh - 120px);
#     }

#     /* Fixed Header Area */
#     .assessment-header {
#         background: white;
#         padding: 1rem 0 0.5rem 0;
#         border-bottom: 1px solid #E2E8F0;
#         margin-bottom: 1rem;
#     }

#     .assessment-header h1 {
#         font-size: 1.5rem !important;
#         margin-bottom: 0.5rem !important;
#         line-height: 1.3 !important;
#     }

#     .assessment-header p {
#         margin-bottom: 0 !important;
#         color: #64748B;
#         font-size: 1rem;
#     }

#     /* Fixed Question Area */
#     .question-area {
#         min-height: 160px;
#         max-height: 200px;
#         padding: 0.5rem 0;
#         margin-bottom: 1rem;
#         overflow: hidden;
#     }

#     /* Fixed Answer Area */
#     .answer-area {
#         min-height: 280px;
#         max-height: 380px;
#         overflow-y: auto;
#         padding: 0.5rem 0;
#         margin-bottom: 100px; /* Space for fixed navigation */
#     }

#     /* Fixed Navigation Area */
#     .navigation-area {
#         position: fixed !important;
#         bottom: 0 !important;
#         left: 0 !important;
#         right: 0 !important;
#         width: 100% !important;
#         background: rgba(255, 255, 255, 0.95) !important;
#         backdrop-filter: blur(10px);
#         padding: 1rem !important;
#         border-top: 1px solid #E2E8F0;
#         box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
#         z-index: 9999 !important;
#     }

#     /* Enhanced Question Type Styling */
#     .scenario-instruction {
#         background: #F8FAFC !important;
#         padding: 1rem !important;
#         border-radius: 8px !important;
#         margin-bottom: 1rem !important;
#         border-left: 4px solid #4CA1A3 !important;
#     }

#     .experiential-instruction {
#         background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%) !important;
#         padding: 1.5rem !important;
#         border-radius: 8px !important;
#         margin-bottom: 1rem !important;
#         border: 2px solid #93C5FD !important;
#     }

#     .text-completion-instruction {
#         background: #FEF3C7 !important;
#         padding: 1rem !important;
#         border-radius: 8px !important;
#         margin-bottom: 1rem !important;
#         border-left: 4px solid #F59E0B !important;
#     }

#     /* Pattern Emergence Hints */
#     .pattern-hint {
#         background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%) !important;
#         border: 1px solid #86EFAC !important;
#         border-radius: 8px !important;
#         padding: 0.75rem !important;
#         margin: 0.5rem 0 !important;
#         font-size: 0.9rem !important;
#         color: #166534 !important;
#     }

#     .pattern-hint-title {
#         font-weight: 600 !important;
#         margin-bottom: 0.25rem !important;
#     }

#     /* Target the Streamlit container that holds navigation */
#     .navigation-area .stContainer {
#         position: static !important;
#     }

#     /* Target columns within navigation */
#     .navigation-area .stColumns {
#         margin: 0 !important;
#     }

#     .navigation-buttons {
#         max-width: 800px;
#         margin: 0 auto;
#     }

#     /* Button consistent sizing */
#     .stButton > button {
#         height: 48px !important;
#         font-weight: 500 !important;
#         border-radius: 8px !important;
#         transition: all 0.3s ease !important;
#     }

#     /* Mobile Responsive Adjustments */
#     @media (max-width: 768px) {
#         .assessment-container {
#             padding: 0.25rem;
#             min-height: calc(100vh - 100px);
#         }

#         .assessment-header h1 {
#             font-size: 1.3rem !important;
#         }

#         .question-area {
#             min-height: 140px;
#             max-height: 180px;
#         }

#         .answer-area {
#             min-height: 250px;
#             max-height: 320px;
#             margin-bottom: 90px;
#         }

#         .navigation-area {
#             padding: 0.75rem 0.5rem;
#         }

#         .stButton > button {
#             height: 44px !important;
#             font-size: 0.9rem !important;
#         }
#     }

#     /* Hide Streamlit elements that interfere */
#     .stApp > header {
#         display: none;
#     }

#     .stApp > .main > .block-container {
#         padding-top: 1rem !important;
#         padding-bottom: 100px !important;
#         max-width: 100% !important;
#     }

#     /* Ensure content doesn't scroll behind navigation */
#     .main .block-container {
#         padding-bottom: 120px !important;
#     }

#     .question-header {
#         background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%) !important;
#         padding: 1.5rem !important;
#         border-radius: 12px !important;
#         border-left: 4px solid #4CA1A3 !important;
#         margin-bottom: 1.5rem !important;
#         box-shadow: 0 2px 6px rgba(0,0,0,0.1) !important;
#         display: block !important;
#     }

#     .question-text {
#         color: #273548 !important;
#         font-size: 1.1rem !important;
#         line-height: 1.5 !important;
#         margin: 0 !important;
#         font-weight: 500 !important;
#         padding: 0 !important;
#     }

#     .question-card {
#         background: #FFFFFF;
#         border-radius: 12px;
#         padding: 1.5rem 2rem;
#         box-shadow: 0 4px 20px rgba(39, 53, 72, 0.08);
#         border: 1px solid #CBD5E1;
#         margin-bottom: 1rem;
#         transition: all 0.3s ease;
#     }

#     .stage-header {
#         background: linear-gradient(135deg, #4CA1A3 0%, #5fb3b5 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         margin-bottom: 2rem;
#         text-align: center;
#     }

#     /* Button Styling */
#     .stButton > button {
#         background-color: #4CA1A3;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 0.5rem 1rem;
#         font-weight: 500;
#         transition: all 0.3s ease;
#     }

#     .stButton > button:hover {
#         background-color: #3A8A8C;
#         box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
#     }

#     .stButton > button:focus {
#         box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.5);
#     }

#     /* Primary Button (Next) */
#     .stButton > button[kind="primary"] {
#         background-color: #4CA1A3;
#         border: 2px solid #4CA1A3;
#     }

#     .stButton > button[kind="primary"]:hover {
#         background-color: #3A8A8C;
#         border-color: #3A8A8C;
#     }

#     /* Radio Button Styling - Fixed for Streamlit */
#     .stRadio > div {
#         gap: 0.5rem;
#     }

#     /* Radio button circle styling */
#     .stRadio > div > label > div[data-testid="stMarkdownContainer"] {
#         padding-left: 0.75rem;
#         color: #273548;
#         font-weight: 400;
#     }

#     /* Target the actual radio input */
#     .stRadio input[type="radio"] {
#         width: 18px;
#         height: 18px;
#         border: 2px solid #CBD5E1;
#         border-radius: 50%;
#         background-color: white;
#         appearance: none;
#         -webkit-appearance: none;
#         -moz-appearance: none;
#         cursor: pointer;
#         transition: all 0.2s ease;
#         position: relative;
#         margin-right: 0.5rem;
#     }

#     /* Hover state */
#     .stRadio input[type="radio"]:hover {
#         border-color: #4CA1A3;
#         box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1);
#     }

#     /* Selected state */
#     .stRadio input[type="radio"]:checked {
#         border-color: #4CA1A3;
#         background-color: #4CA1A3;
#     }

#     /* Inner dot for selected state */
#     .stRadio input[type="radio"]:checked::before {
#         content: '';
#         width: 8px;
#         height: 8px;
#         border-radius: 50%;
#         background-color: white;
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-50%, -50%);
#     }

#     /* Focus state for accessibility */
#     .stRadio input[type="radio"]:focus {
#         outline: none;
#         box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.3);
#     }

#     /* Label styling */
#     .stRadio > div > label {
#         display: flex;
#         align-items: center;
#         cursor: pointer;
#         padding: 0.5rem;
#         border-radius: 6px;
#         transition: background-color 0.2s ease;
#     }

#     .stRadio > div > label:hover {
#         background-color: rgba(76, 161, 163, 0.05);
#     }

#     /* Success Message Styling */
#     .stSuccess {
#         background-color: rgba(76, 161, 163, 0.1);
#         border-left: 4px solid #4CA1A3;
#         color: #273548;
#     }

#     /* Progress Bar Styling - Grey background, teal fill */
#     .stProgress > div {
#         background-color: #E5E7EB;
#     }

#     .stProgress > div > div > div {
#         background-color: #4CA1A3;
#     }

#     /* Results styling */
#     .results-container {
#         background: linear-gradient(135deg, #F8FFFE 0%, #F3F6F8 100%);
#         padding: 2rem;
#         border-radius: 12px;
#         margin: 1rem 0;
#         border: 1px solid #CBD5E1;
#     }

#     .pattern-card {
#         background: white;
#         padding: 1rem;
#         border-radius: 8px;
#         margin: 0.5rem 0;
#         border-left: 4px solid #4CA1A3;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }

#     .session-planning {
#         background: linear-gradient(135deg, #E6F7F7 0%, #F0FFFE 100%);
#         padding: 1.5rem;
#         border-radius: 10px;
#         margin: 1rem 0;
#         border: 1px solid #4CA1A3;
#     }

#     .resistance-analysis {
#         background: linear-gradient(135deg, #FFF7E6 0%, #FFFAF0 100%);
#         padding: 1.5rem;
#         border-radius: 10px;
#         margin: 1rem 0;
#         border: 1px solid #D69E2E;
#     }

#     .trigger-mapping {
#         background: linear-gradient(135deg, #F0F4FF 0%, #F7FAFC 100%);
#         padding: 1rem;
#         border-radius: 8px;
#         margin: 0.5rem 0;
#         border-left: 3px solid #4C6EF5;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Initialize enhanced assessment
# @st.cache_resource
# def initialize_assessment():
#     return EnhancedAssessmentConfig()

# def render_stage_introduction(stage_info, current_stage):
#     """Render friendly stage introduction"""
#     stage_title = stage_info.get('title', 'ASSESSMENT STAGE').upper()
#     return stage_title

# def show_pattern_hints(current_scores, question_number):
#     """Show emerging pattern hints with improved timing and engagement"""
#     if question_number < 8:  # Don't show hints too early
#         return

#     # Calculate which patterns are emerging with more nuanced detection
#     strong_patterns = []
#     emerging_patterns = []
#     pattern_names = {
#         'unhappiness_culture': 'Success discomfort',
#         'power_struggles': 'Authority resistance',
#         'systematic_mistrust': 'Trust hesitation',
#         'separation_division': 'Binary thinking',
#         'doing_vs_being': 'Achievement focus',
#         'digital_despair': 'Digital adaptation',
#         'perfectionism': 'Perfectionism',
#         'social_anxiety': 'Social sensitivity',
#         'self_sacrifice': 'Self-sacrifice',
#         'compartmentalized_authenticity': 'Authenticity masking',
#         'inherited_missions': 'Family expectations'
#     }

#     for pattern_id, score in current_scores.items():
#         if isinstance(score, (int, float)):
#             pattern_display_name = pattern_names.get(pattern_id, pattern_id.replace('_', ' ').title())
#             if score >= 5:
#                 strong_patterns.append(pattern_display_name)
#             elif score >= 3:
#                 emerging_patterns.append(pattern_display_name)

#     # Show hints at strategic intervals with different messaging
#     show_hint = False
#     hint_type = "progress"

#     if question_number in [15, 30, 45, 60, 75]:  # Major milestones
#         show_hint = True
#         hint_type = "milestone"
#     elif question_number % 20 == 0:  # Every 20 questions
#         show_hint = True
#         hint_type = "progress"
#     elif len(strong_patterns) >= 2 and question_number % 15 == 0:  # When patterns are clear
#         show_hint = True
#         hint_type = "patterns"

#     if show_hint and (strong_patterns or emerging_patterns):
#         if hint_type == "milestone":
#             icon = "🎯"
#             title = f"Milestone: {question_number//15 * 15}% Complete"
#             color = "#4CA1A3"
#         elif hint_type == "patterns":
#             icon = "🔍"
#             title = "Patterns Emerging"
#             color = "#F59E0B"
#         else:
#             icon = "📊"
#             title = "Assessment Progress"
#             color = "#6366F1"

#         # Create hint message
#         if strong_patterns:
#             hint_message = f"**Strong indicators:** {', '.join(strong_patterns[:2])}"
#             if len(strong_patterns) > 2:
#                 hint_message += f" +{len(strong_patterns)-2} more"
#         elif emerging_patterns:
#             hint_message = f"**Emerging patterns:** {', '.join(emerging_patterns[:2])}"
#             if len(emerging_patterns) > 2:
#                 hint_message += f" +{len(emerging_patterns)-2} more"
#         else:
#             hint_message = "**Analysis:** Patterns becoming clearer with each response"

#         # Add context-appropriate encouragement
#         if question_number >= 60:
#             encouragement = "Nearly complete - your detailed insights are valuable for creating your personalized approach."
#         elif question_number >= 40:
#             encouragement = "Excellent progress - the assessment is building a comprehensive picture of your unique patterns."
#         elif question_number >= 20:
#             encouragement = "Great work - your honest responses are helping us understand your behavioral patterns."
#         else:
#             encouragement = "Thank you for your thoughtful responses - patterns are beginning to emerge."

#         # Use Streamlit native info component instead of HTML
#         st.info(f"{icon} **{title}**\\n\\n{hint_message}\\n\\n*{encouragement}*")

# def render_enhanced_progress_display(question_data, question_number, total_questions, stage_info=None):
#     """Enhanced progress display with stage information and visual improvements"""

#     progress_percentage = (question_number / total_questions) * 100

#     # Determine current stage and progress within stage
#     current_stage = question_data.get('stage')
#     stage_name = ""  # Remove "Assessment in progress" text
#     stage_description = ""
#     estimated_time = ""

#     if stage_info:
#         stage_name = stage_info.get('title', stage_name)
#         stage_description = stage_info.get('description', '')
#         estimated_time = stage_info.get('estimated_time', '')

#     # Use Streamlit native components
#     col1, col2 = st.columns([3, 1])

#     with col1:
#         st.markdown(f"**{stage_name}**")
#         if stage_description:
#             st.caption(stage_description)
#         if estimated_time:
#             st.caption(f"⏱️ Estimated time: {estimated_time}")

#     with col2:
#         pass  # Removed question counter

#     # Progress bar
#     st.progress(progress_percentage / 100, text=f"Progress: {progress_percentage:.0f}% ({int(total_questions - question_number)} remaining)")

# def render_question_card(question_data, question_number, total_questions):
#     """Render individual question in an appealing card format"""

#     # Use Streamlit container for card-like appearance
#     with st.container():
#         if question_data.get('title'):
#             st.markdown(f"**{question_data.get('title', 'Question')}**")

#         if question_data.get('subtitle'):
#             st.caption(question_data.get('subtitle'))

#         # Main question text in gradient container
#         st.markdown(
#             f'''<div style="
#                 background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
#                 padding: 1.5rem;
#                 border-radius: 12px;
#                 border-left: 4px solid #4CA1A3;
#                 margin-bottom: 1.5rem;
#                 box-shadow: 0 2px 6px rgba(0,0,0,0.1);
#             ">
#                 <div style="
#                     color: #273548;
#                     font-size: 1.1rem;
#                     line-height: 1.5;
#                     margin: 0;
#                     font-weight: 500;
#                 ">
#                     {question_data["text"]}
#                 </div>
#             </div>''',
#             unsafe_allow_html=True
#         )

#         # Help text removed - no info boxes for questions


# def render_enhanced_options(options, question_id, question_type="single_choice", key_suffix="", help_text=None):
#     """Render options with enhanced styling based on question type"""

#     # Create a unique key that includes session state to avoid duplicates
#     unique_key = f"{question_type}_{question_id}_{key_suffix}_{st.session_state.current_question}"

#     # Check if we have a previous response for this question
#     previous_response = st.session_state.responses.get(question_id)
#     default_index = 0  # Default to first option

#     if previous_response:
#         # Find the index of the previous response in the options list
#         try:
#             if isinstance(previous_response, str) and previous_response.startswith("CUSTOM:"):
#                 # For custom text responses, find the "Write your..." option
#                 for i, option in enumerate(options):
#                     if str(option).lower().startswith("write your") and str(option).lower().endswith("..."):
#                         default_index = i
#                         break
#             else:
#                 # For regular responses, find exact match
#                 default_index = options.index(previous_response)
#         except (ValueError, TypeError):
#             # If previous response not found in options, default to first option
#             default_index = 0

#     # Handle different question types
#     if question_type == "scenario_based":
#         st.info("📖 **Scenario Question:** Imagine yourself in this situation and choose your most honest response.")

#         return st.radio(
#             "How would you most likely respond?",
#             options=options,
#             index=default_index,
#             key=unique_key,
#             help=help_text,
#             label_visibility="collapsed"
#         )

#     elif question_type == "experiential_advanced":
#         st.warning("🧠 **EXPERIENTIAL TEST**\\n\\nPlease actually perform this exercise before answering. Take your time - this helps us understand your natural hypnotic responsiveness.")

#         # Add a timer for experiential questions
#         if st.button("🕐 I've completed the exercise", key=f"timer_{unique_key}", type="secondary"):
#             st.session_state[f"exercise_completed_{question_id}"] = True

#         if st.session_state.get(f"exercise_completed_{question_id}", False):
#             return st.radio(
#                 "What was your experience?",
#                 options=options,
#                 index=default_index,
#                 key=unique_key,
#                 help=help_text,
#                 label_visibility="collapsed"
#             )
#         else:
#             st.info("Please complete the exercise above first, then click the button to proceed.")
#             return None

#     elif question_type == "text_completion":
#         st.info("✍️ **Reflection Question:** Take a moment to think deeply about this. Your honest insights are valuable.")

#         # Text area for open-ended response
#         text_response = st.text_area(
#             "Your thoughts:",
#             value=previous_response if previous_response and not previous_response.startswith("CUSTOM:") else "",
#             placeholder="Write your honest thoughts here...",
#             height=100,
#             key=f"text_{unique_key}",
#             help=help_text
#         )

#         # Also provide radio options as backup
#         st.markdown("**Or select one of these options:**")
#         radio_response = st.radio(
#             "Quick response options:",
#             options=options,
#             index=default_index,
#             key=f"radio_{unique_key}",
#             label_visibility="collapsed"
#         )

#         # Return combined response
#         if text_response.strip():
#             return f"TEXT: {text_response.strip()}"
#         else:
#             return radio_response

#     elif question_type == "experiential_scale":
#         st.info("🎯 **Experience Rating:** Rate the intensity of your experience.")

#         return st.radio(
#             "Rate your experience level:",
#             options=options,
#             index=default_index,
#             key=unique_key,
#             help=help_text,
#             label_visibility="collapsed"
#         )

#     else:
#         # Default handling for standard single_choice questions
#         # Check if one of the options is a "Write your..." option
#         has_custom_option = any(
#             str(option).lower().startswith("write your") and str(option).lower().endswith("...")
#             for option in options
#         )

#         radio_response = st.radio(
#             "Choose the option that best describes you:",
#             options=options,
#             index=default_index,
#             key=unique_key,
#             help=help_text,
#             label_visibility="collapsed"
#         )

#         # If user selected any "Write your..." option, show text input
#         if has_custom_option and radio_response and str(radio_response).lower().startswith("write your") and str(radio_response).lower().endswith("..."):
#             st.markdown("**Please share your thoughts:**")

#             # Get previous custom text if exists
#             previous_custom_text = ""
#             if previous_response and previous_response.startswith("CUSTOM:"):
#                 # Extract the custom text part after the "|" separator
#                 parts = previous_response.split(" | ", 1)
#                 if len(parts) > 1:
#                     previous_custom_text = parts[1]

#             custom_text = st.text_area(
#                 "Your thoughts:",
#                 value=previous_custom_text,
#                 placeholder="Please describe your specific situation or thoughts...",
#                 key=f"custom_text_{unique_key}",
#                 height=80
#             )

#             # Return combined response if custom text is provided
#             if custom_text.strip():
#                 return f"CUSTOM: {radio_response} | {custom_text.strip()}"
#             else:
#                 # Return radio response even if no custom text yet
#                 return radio_response
#         else:
#             return radio_response

# def extract_response_text(response):
#     """Helper function to extract analyzable text from different response formats"""
#     if not isinstance(response, str):
#         return ""

#     # Handle custom responses (CUSTOM: option | text)
#     if response.startswith("CUSTOM:") and "|" in response:
#         return response.split("|", 1)[1].strip()

#     # Handle text completion responses (TEXT: content)
#     if response.startswith("TEXT:"):
#         return response[5:].strip()

#     # Return original response for standard options
#     return response

# def calculate_urgency_score(responses, pattern_scores):
#     """Calculate urgency score based on responses and pattern intensity"""
#     urgency_indicators = 0

#     # Check for crisis language in text responses
#     crisis_terms = ['desperate', 'can\'t continue', 'breaking point', 'urgent', 'crisis',
#                    'immediately', 'can\'t take it', 'falling apart', 'overwhelmed']

#     for response_id, response in responses.items():
#         if isinstance(response, str):
#             # Use helper function to extract analyzable text
#             analyzable_text = extract_response_text(response)
#             response_lower = analyzable_text.lower()

#             crisis_count = sum(1 for term in crisis_terms if term in response_lower)
#             urgency_indicators += crisis_count * 2

#     # Check urgency-related question responses
#     if 'urgency_feeling' in responses:
#         urgency_response = responses['urgency_feeling']
#         if 'crisis' in urgency_response.lower() or 'need help now' in urgency_response.lower():
#             urgency_indicators += 3
#         elif 'very urgent' in urgency_response.lower() or 'few weeks' in urgency_response.lower():
#             urgency_indicators += 2

#     # High pattern intensity indicates urgency
#     if pattern_scores:
#         max_score = max([score for score in pattern_scores.values() if isinstance(score, (int, float))] + [0])
#         if max_score >= 7:
#             urgency_indicators += 2
#         elif max_score >= 5:
#             urgency_indicators += 1

#     # Check for multiple severe patterns
#     severe_patterns = sum(1 for score in pattern_scores.values()
#                          if isinstance(score, (int, float)) and score >= 5)
#     if severe_patterns >= 3:
#         urgency_indicators += 1

#     return min(urgency_indicators, 5)  # Cap at 5

# def get_contact_timeline(urgency_level):
#     """Get expected contact timeline based on urgency"""
#     if urgency_level >= 4:
#         return "24 hours"
#     elif urgency_level >= 3:
#         return "48 hours"
#     elif urgency_level >= 2:
#         return "3 business days"
#     else:
#         return "5 business days"

# def get_personalized_recommendations(dominant_pattern, secondary_patterns, urgency_level):
#     """Get personalized approach recommendations based on detected patterns"""

#     pattern_recommendations = {
#         'unhappiness_culture': {
#             'approach': 'Standard 2-session transformation focusing on permission installation for positive states',
#             'note': 'Your pattern suggests you may resist good feelings - we have specific techniques for this.',
#             'sessions': '2 sessions (most effective for this pattern type)'
#         },
#         'power_struggles': {
#             'approach': 'Collaborative 2-session approach with empowerment-focused techniques',
#             'note': 'We use collaborative methods that honor your need for autonomy and control.',
#             'sessions': '2 sessions with collaborative approach'
#         },
#         'systematic_mistrust': {
#             'approach': 'Trust-building 3-session comprehensive approach',
#             'note': 'We go slowly to build therapeutic trust - rushing would be counterproductive.',
#             'sessions': '3 sessions (trust-building is essential)'
#         },
#         'digital_despair': {
#             'approach': 'Digital-native 2-session transformation with modern techniques',
#             'note': 'We understand digital-age patterns and use cutting-edge approaches.',
#             'sessions': '2 sessions optimized for digital natives'
#         },
#         'perfectionism': {
#             'approach': 'Precision 2-session approach addressing achievement pressure',
#             'note': 'We work with your high standards while reducing the pressure that maintains suffering.',
#             'sessions': '2 sessions with precision focus'
#         }
#     }

#     default_rec = {
#         'approach': 'Standard 2-session transformation (recommended)',
#         'note': 'Based on your unique pattern combination, we recommend our proven 2-session approach.',
#         'sessions': '2 sessions (our most popular and effective option)'
#     }

#     return pattern_recommendations.get(dominant_pattern, default_rec)

# def show_preliminary_results(enhanced_assessment, responses):
#     """Show preliminary insights and gather enhanced contact information"""

#     # Generate the profile for preliminary insights
#     try:
#         profile = enhanced_assessment.generate_enhanced_profile(responses)
#         # Handle case where profile might not be a dict
#         if not isinstance(profile, dict):
#             st.warning(f"Profile generation returned unexpected type: {type(profile)}. Using fallback.")
#             profile = {'enhanced_pattern_scores': {}}

#         patterns = profile.get('enhanced_pattern_scores', {})
#         # Ensure patterns is a dict
#         if not isinstance(patterns, dict):
#             st.warning(f"Pattern scores returned unexpected type: {type(patterns)}. Using fallback.")
#             patterns = {}

#     except Exception as e:
#         st.error(f"Error generating profile: {str(e)}")
#         # Use comprehensive fallback
#         profile = {
#             'enhanced_pattern_scores': {},
#             'pattern_hierarchy': {'dominant_pattern': {'name': 'general_adaptation', 'score': 3.5}},
#             'session_planning': {'recommended_sessions': 2},
#             'behavioral_analysis': {},
#             'success_prediction': {'probability': 75}
#         }
#         patterns = {}

#     # Get dominant and secondary patterns
#     sorted_patterns = sorted([(k, v) for k, v in patterns.items() if isinstance(v, (int, float))],
#                            key=lambda x: x[1], reverse=True)

#     # Use better fallbacks for pattern display
#     if sorted_patterns:
#         dominant_pattern = sorted_patterns[0][0]
#         dominant_score = sorted_patterns[0][1]
#         secondary_patterns = [p[0] for p in sorted_patterns[1:3]] if len(sorted_patterns) > 1 else []
#     else:
#         # Create a fallback pattern based on responses
#         dominant_pattern = 'general_adaptation'  # Generic pattern
#         dominant_score = 3.5  # Moderate score
#         secondary_patterns = []

#     # Calculate urgency
#     try:
#         urgency_level = calculate_urgency_score(responses, patterns)
#     except Exception as e:
#         st.warning(f"Error calculating urgency: {str(e)}")
#         urgency_level = 2  # Default to moderate urgency

#     st.markdown("#### ASSESSMENT COMPLETE")
#     st.success("Congratulations! You've completed the comprehensive assessment. Here are some key insights from your responses:")

#     # Show 4 key statistics in 2x2 grid
#     # First row
#     col1, col2 = st.columns(2)

#     with col1:
#         # Dominant pattern with better names
#         pattern_names = {
#             'unhappiness_culture': 'Success Discomfort',
#             'power_struggles': 'Authority Resistance',
#             'systematic_mistrust': 'Trust Hesitation',
#             'separation_division': 'Binary Thinking',
#             'doing_vs_being': 'Achievement Focus',
#             'digital_despair': 'Digital Adaptation',
#             'perfectionism': 'Perfectionism',
#             'self_sacrifice': 'Self-Sacrifice',
#             'social_anxiety': 'Social Sensitivity',
#             'general_adaptation': 'General Adaptation Patterns'
#         }

#         pattern_display = pattern_names.get(dominant_pattern, dominant_pattern.replace('_', ' ').title())

#         # Use Streamlit metric instead of HTML
#         st.metric(
#             label="Primary Pattern",
#             value=pattern_display,
#             delta=f"{dominant_score:.1f}/10 intensity"
#         )

#     with col2:
#         # Hypnotic readiness with better calculation
#         hypnotic_indicators = ['hypnotic_responsiveness', 'imagery_capacity', 'absorption_capacity']
#         hypnotic_scores = [patterns.get(indicator, 0) for indicator in hypnotic_indicators if isinstance(patterns.get(indicator, 0), (int, float))]
#         hypnotic_score = (sum(hypnotic_scores) / len(hypnotic_scores) * 20) if hypnotic_scores else 50

#         if hypnotic_score > 70:
#             readiness_text = "High"
#             readiness_color = "#22c55e"
#         elif hypnotic_score > 40:
#             readiness_text = "Moderate"
#             readiness_color = "#eab308"
#         else:
#             readiness_text = "Developing"
#             readiness_color = "#6366f1"

#         # Use Streamlit metric instead of HTML
#         st.metric(
#             label="Hypnotic Readiness",
#             value=readiness_text,
#             delta=f"{hypnotic_score:.0f}% score"
#         )

#     # Second row
#     col3, col4 = st.columns(2)

#     with col3:
#         # Success probability
#         success_prob = calculate_success_probability(patterns)
#         # Use Streamlit metric instead of HTML
#         st.metric(
#             label="Success Probability",
#             value=f"{success_prob}%",
#             delta="Based on similar patterns"
#         )

#     with col4:
#         # Priority Level (moved from separate section)
#         timeline = get_contact_timeline(urgency_level)
#         urgency_labels = {0: "Standard", 1: "Routine", 2: "Priority", 3: "High Priority", 4: "Urgent", 5: "Crisis"}

#         st.metric(
#             label="Priority Level",
#             value=urgency_labels.get(urgency_level, 'Standard'),
#             delta=f"Contact within: {timeline}"
#         )

#     # Personalized insights section
#     st.markdown("---")
#     st.markdown("## Your Personalized Approach")

#     # Get personalized recommendations
#     recommendations = get_personalized_recommendations(dominant_pattern, secondary_patterns, urgency_level)

#     # Just show the recommendations without duplicate Priority Level
#     st.markdown(f"""
#     **Recommended Approach:** {recommendations['approach']}

#     **Why this works for you:** {recommendations['note']}
#     """)

#     st.markdown("---")

#     # Enhanced Contact Form
#     render_enhanced_contact_form(dominant_pattern, recommendations, urgency_level, timeline)

# def calculate_success_probability(patterns, hypnotic_score, urgency_level):
#     """Calculate success probability based on various factors"""
#     base_rate = 85  # Base success rate

#     # Pattern complexity adjustment
#     severe_patterns = sum(1 for score in patterns.values()
#                          if isinstance(score, (int, float)) and score >= 6)
#     base_rate -= (severe_patterns * 5)

#     # Hypnotic readiness adjustment
#     if hypnotic_score > 70:
#         base_rate += 10
#     elif hypnotic_score < 40:
#         base_rate -= 10

#     # Urgency adjustment (very high urgency can indicate instability)
#     if urgency_level >= 4:
#         base_rate -= 10
#     elif urgency_level <= 1:
#         base_rate += 5

#     return max(65, min(95, base_rate))  # Keep between 65-95%

# def render_enhanced_contact_form(dominant_pattern, recommendations, urgency_level, timeline):
#     """Render intelligent contact form with personalization"""

#     st.markdown("## Your Transformation Roadmap is Ready")

#     # Personalized intro based on pattern
#     pattern_intros = {
#         'unhappiness_culture': "Based on your success discomfort pattern, we've created a specialized approach that works with your psychology rather than against it.",
#         'power_struggles': "Your independence and autonomy are valuable - our collaborative approach respects your need for control while creating transformation.",
#         'systematic_mistrust': "We understand your cautious approach to new things. That's why we take time to build trust and go at your pace.",
#         'digital_despair': "As someone navigating modern digital pressures, we use cutting-edge techniques designed specifically for today's challenges.",
#         'perfectionism': "Your high standards are an asset - we'll work with your precision mindset to create lasting change without adding pressure."
#     }

#     intro_text = pattern_intros.get(dominant_pattern,
#         "Based on your unique pattern combination, we've designed a personalized approach specifically for your transformation.")

#     st.info(intro_text)

#     with st.form("enhanced_contact_form"):
#         st.markdown("#### Contact Information")

#         col1, col2 = st.columns(2)
#         with col1:
#             name = st.text_input("Full name*", placeholder="Your name")
#             email = st.text_input("Email*", placeholder="your@email.com")
#         with col2:
#             phone = st.text_input("Phone (WhatsApp preferred)", placeholder="+66 xxx xxx xxx")
#             urgency = st.selectbox("When would you like to start?", [
#                 f"As soon as possible (we'll contact you within {timeline})",
#                 "Within 2 weeks would be ideal",
#                 "Within a month is fine",
#                 "I'm still exploring my options"
#             ])

#         st.markdown("#### Your Personalized Plan")

#         # Show the recommended session plan based on pattern
#         session_plan = st.selectbox("Preferred approach*", [
#             recommendations['sessions'],
#             "Discovery session first to discuss the approach",
#             "I'd like to understand more about how this works"
#         ])

#         st.markdown("#### What Success Looks Like for You")
#         main_concern = st.text_area(
#             "Describe how your daily life would be different after successful transformation*",
#             placeholder="Think about specific situations, relationships, or feelings that would be different...",
#             height=120,
#             help="This helps us understand your specific goals and customize our approach."
#         )

#         # Additional fields based on urgency
#         if urgency_level >= 3:
#             st.markdown("#### Additional Support")
#             immediate_support = st.checkbox("I would appreciate a quick check-in call before our first session")
#             resource_interest = st.checkbox("I'm interested in immediate coping strategies while waiting for our session")

#         st.markdown("#### Communication Preferences")
#         col1, col2 = st.columns(2)
#         with col1:
#             preferred_contact = st.selectbox("Best way to reach you", [
#                 "WhatsApp", "Email", "Phone call", "Any of the above"
#             ])
#         with col2:
#             best_time = st.selectbox("Best time to contact", [
#                 "Morning (9-12)", "Afternoon (12-17)", "Evening (17-20)", "Anytime"
#             ])

#         # Terms and privacy
#         st.markdown("#### Privacy & Terms")
#         privacy_consent = st.checkbox("I consent to my assessment data being used to prepare my personalized session plan*")
#         marketing_consent = st.checkbox("I'm interested in receiving helpful insights about behavioral patterns and transformation techniques")

#         submitted = st.form_submit_button(
#             f"Book My {recommendations['sessions']} 🎯",
#             type="primary",
#             use_container_width=True
#         )

#         if submitted:
#             if not name or not email or not main_concern or not privacy_consent:
#                 st.error("Please fill in all required fields (*)")
#             else:
#                 # Store enhanced contact info
#                 contact_data = {
#                     'name': name,
#                     'email': email,
#                     'phone': phone,
#                     'urgency': urgency,
#                     'session_plan': session_plan,
#                     'main_concern': main_concern,
#                     'preferred_contact': preferred_contact,
#                     'best_time': best_time,
#                     'dominant_pattern': dominant_pattern,
#                     'urgency_level': urgency_level,
#                     'timeline': timeline,
#                     'privacy_consent': privacy_consent,
#                     'marketing_consent': marketing_consent
#                 }

#                 if urgency_level >= 3:
#                     contact_data.update({
#                         'immediate_support': locals().get('immediate_support', False),
#                         'resource_interest': locals().get('resource_interest', False)
#                     })

#                 st.session_state.contact_info = contact_data
#                 st.session_state.assessment_stage = "contact_complete"
#                 st.success(f"✅ Thank you {name}! We'll contact you within {timeline} to schedule your {recommendations['sessions']}.")

#                 # Show next steps
#                 st.markdown("#### What Happens Next")
#                 next_steps = f"""
#                 1. **Within {timeline}**: Our clinical team will contact you via {preferred_contact.lower()}
#                 2. **Session Planning**: We'll discuss your personalized {recommendations['sessions']} approach
#                 3. **Scheduling**: Book your first session at a time that works for you
#                 4. **Preparation**: Receive your pre-session preparation materials
#                 """

#                 if urgency_level >= 4:
#                     next_steps = "🚨 **Priority handling**: Given your urgent timeline, you'll be contacted within 24 hours.\n\n" + next_steps

#                 st.markdown(next_steps)

#                 st.rerun()

# def render_contact_form():
#     """Render contact information form"""
#     from datetime import datetime

#     st.markdown("---")
#     st.markdown("**Get your complete analysis**")
#     st.info("To receive your detailed assessment report and personalized therapeutic recommendations, please provide your contact information below.")

#     with st.form("contact_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             first_name = st.text_input("First Name*", key="contact_first_name")
#             email = st.text_input("Email Address*", key="contact_email")
#         with col2:
#             last_name = st.text_input("Last Name*", key="contact_last_name")
#             phone = st.text_input("Phone Number", key="contact_phone")

#         urgency = st.selectbox(
#             "How urgent is your need for support?*",
#             ["Standard - within a week", "High priority - within 2-3 days", "Very urgent - within 24 hours", "Extremely urgent - same day if possible"]
#         )

#         additional_info = st.text_area(
#             "Additional information or specific concerns:",
#             placeholder="Any additional details that might help us better understand your situation..."
#         )

#         submitted = st.form_submit_button("Get My Complete Analysis", type="primary")

#         if submitted:
#             if first_name and last_name and email:
#                 # Save contact info
#                 st.session_state.contact_info = {
#                     'first_name': first_name,
#                     'last_name': last_name,
#                     'email': email,
#                     'phone': phone,
#                     'urgency': urgency,
#                     'additional_info': additional_info,
#                     'submission_time': datetime.now().isoformat()
#                 }
#                 st.session_state.contact_provided = True
#                 st.rerun()
#             else:
#                 st.error("Please fill in all required fields (marked with *)")

# def render_pattern_recognition_hero(dominant_pattern, secondary_patterns, pattern_scores, profile):
#     """Render the pattern recognition hero section with immediate validation"""

#     pattern_names = {
#         'unhappiness_culture': 'Success Discomfort',
#         'power_struggles': 'Authority Resistance',
#         'systematic_mistrust': 'Trust Hesitation',
#         'separation_division': 'Binary Thinking',
#         'doing_vs_being': 'Achievement Focus',
#         'digital_despair': 'Digital Adaptation',
#         'perfectionism': 'Perfectionism',
#         'self_sacrifice': 'Self-Sacrifice',
#         'social_anxiety': 'Social Sensitivity',
#         'compartmentalized_authenticity': 'Authenticity Masking',
#         'inherited_missions': 'Family Expectations'
#     }

#     pattern_descriptions = {
#         'unhappiness_culture': "You've learned to expect disappointment when things go well, creating an unconscious resistance to positive experiences.",
#         'power_struggles': "Your strong need for autonomy can create automatic resistance to authority or guidance, even when it's beneficial.",
#         'systematic_mistrust': "Your protective skepticism, while valuable in some situations, may be limiting your ability to receive support.",
#         'digital_despair': "Modern digital pressures have created unique stress patterns that traditional approaches often miss.",
#         'perfectionism': "Your high standards drive excellence but may be creating internal pressure that maintains suffering."
#     }

#     pattern_origins = {
#         'unhappiness_culture': "childhood experiences where good things led to disappointment or increased expectations",
#         'power_struggles': "early experiences where submission felt like loss of identity or safety",
#         'systematic_mistrust': "past betrayals or disappointments that created protective skepticism",
#         'digital_despair': "adaptation to modern digital environments creating new stress patterns",
#         'perfectionism': "environments where love or approval was conditional on performance"
#     }

#     # Get pattern info from hierarchy if available
#     if isinstance(profile, dict) and 'pattern_hierarchy' in profile:
#         hierarchy = profile['pattern_hierarchy']
#         dominant_name = pattern_names.get(hierarchy['dominant_pattern']['name'], hierarchy['dominant_pattern']['name'].replace('_', ' ').title())
#         dominant_score = hierarchy['dominant_pattern']['score']
#         dominant_pattern = hierarchy['dominant_pattern']['name']
#     else:
#         dominant_name = pattern_names.get(dominant_pattern, dominant_pattern.replace('_', ' ').title())
#         dominant_score = pattern_scores.get(dominant_pattern, 0) if pattern_scores else 0

#     dominant_description = pattern_descriptions.get(dominant_pattern, "A unique behavioral pattern that influences how you navigate life's challenges.")
#     dominant_origin = pattern_origins.get(dominant_pattern, "experiences that shaped your current responses")

#     st.markdown(f"""
#     <div class="pattern-hero-container" style="
#         background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
#         border-radius: 16px;
#         padding: 2rem;
#         margin: 1.5rem 0;
#         border: 1px solid #BAE6FD;
#         box-shadow: 0 4px 20px rgba(14, 165, 233, 0.1);
#     ">
#         <div class="hero-header" style="text-align: center; margin-bottom: 1.5rem;">
#             <h2 style="color: #0369A1; margin: 0 0 0.5rem 0; font-size: 1.8rem;">What we discovered about you</h2>
#             <p style="color: #0284C7; margin: 0; font-size: 1.1rem; font-weight: 500;">Your unique behavioral pattern constellation</p>
#         </div>

#         <div class="dominant-pattern" style="
#             background: white;
#             border-radius: 12px;
#             padding: 1.5rem;
#             margin-bottom: 1.5rem;
#             border-left: 6px solid #4CA1A3;
#             box-shadow: 0 2px 8px rgba(0,0,0,0.08);
#         ">
#             <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
#                 <h3 style="color: #4CA1A3; margin: 0; font-size: 1.4rem;">Primary pattern: {dominant_name}</h3>
#                 <div style="text-align: right;">
#                     <div style="background: #4CA1A3; color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.9rem; font-weight: 600;">
#                         {dominant_score}/10 intensity
#                     </div>
#                 </div>
#             </div>
#             <p style="color: #374151; margin: 0 0 1rem 0; font-size: 1.05rem; line-height: 1.6;">
#                 {dominant_description}
#             </p>
#             <div style="background: #F8FAFC; padding: 1rem; border-radius: 8px; border-left: 3px solid #6B7280;">
#                 <p style="margin: 0; color: #4B5563; font-size: 0.95rem;">
#                     <strong>Recognition moment:</strong> This pattern typically develops from {dominant_origin}.
#                 </p>
#             </div>
#         </div>

#         <div class="accuracy-indicator" style="
#             background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
#             border: 1px solid #86EFAC;
#             border-radius: 8px;
#             padding: 1rem;
#             text-align: center;
#         ">
#             <p style="margin: 0; color: #166534; font-size: 0.95rem;">
#                 <strong>Assessment accuracy:</strong> Based on 87 comprehensive questions, this analysis reflects your authentic behavioral patterns.
#             </p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# def render_enhanced_paywall():
#     """Render value-driven paywall presentation with assessment-based pricing"""

#     # Get assessment data for personalization
#     if hasattr(st.session_state, 'responses') and st.session_state.responses:
#         try:
#             from utils.config import EnhancedAssessmentConfig
#             temp_assessment = EnhancedAssessmentConfig()
#             profile = temp_assessment.generate_enhanced_profile(st.session_state.responses)

#             # Get pattern data for personalization
#             if 'pattern_hierarchy' in profile:
#                 dominant_pattern = profile['pattern_hierarchy']['dominant_pattern']['name']
#                 pattern_count = len([p for p in profile.get('enhanced_pattern_scores', {}).values() if isinstance(p, (int, float)) and p >= 3])
#                 complexity_level = "High" if pattern_count >= 4 else "Moderate" if pattern_count >= 2 else "Standard"
#             else:
#                 dominant_pattern = "complex_patterns"
#                 pattern_count = 3
#                 complexity_level = "Moderate"
#         except:
#             dominant_pattern = "complex_patterns"
#             pattern_count = 3
#             complexity_level = "Moderate"
#     else:
#         dominant_pattern = "complex_patterns"
#         pattern_count = 3
#         complexity_level = "Moderate"

#     col1, col2 = st.columns([2, 1])

#     with col1:
#         st.markdown(f"""
#         ### 🔓 Unlock your complete transformation blueprint

#         **What you receive immediately:**
#         - **Complete 15-20 page behavioral analysis report** tailored to your {pattern_count}-pattern constellation
#         - **Session-by-session transformation roadmap** with predicted timeline and milestones
#         - **Personalized therapeutic language recommendations** for maximum effectiveness
#         - **Success probability optimization factors** with confidence-building strategies
#         - **5-year cost analysis vs. intervention ROI** showing financial impact projections
#         - **Lifetime downloadable PDF report** for your permanent records
#         - **Priority clinical team contact** within 24-48 hours

#         ---

#         **🎯 Exclusive {complexity_level} Complexity Analysis:**
#         Your assessment reveals {complexity_level.lower()}-level pattern complexity, requiring specialized intervention protocols normally reserved for advanced cases.
#         """)

#         # Social proof with specific numbers
#         st.info("📊 **Based on 500+ successful transformations** with similar {complexity_level.lower()}-complexity patterns")

#         # Urgency without pressure
#         if complexity_level == "High":
#             st.warning("⚠️ **Complex patterns like yours typically solidify further without intervention** - early action prevents escalation")
#         else:
#             st.info("💡 **Patterns like yours respond exceptionally well to targeted intervention** when addressed promptly")

#     with col2:
#         st.markdown("""
#         ## 💰 Investment Analysis

#         **Traditional therapy approach:**
#         - Duration: 18+ months
#         - Cost: ฿15,000-25,000+
#         - Success rate: 30-45%
#         - Time to results: 6-12 months

#         **Specialized hypnotherapy:**
#         - Duration: 2-3 sessions
#         - Cost: ฿3,000-4,000 total
#         - Success rate: 85%+
#         - Time to results: 2-4 weeks

#         ---

#         **⏱️ Time value comparison:**
#         - Traditional: 48-72 hours vs 3-6 months
#         - Weekly therapy commitment: 0 vs 1-2 hours ongoing
#         - Life disruption: Minimal vs Significant

#         ---

#         **🎁 Limited Time Value:**
#         Complete analysis normally ฿2,500
#         **Today: ฿1,500** (40% savings)
#         """)

#         # Dynamic pricing based on complexity
#         if complexity_level == "High":
#             price_text = "฿1,800 (High Complexity)"
#             price_note = "Premium analysis for complex patterns"
#         else:
#             price_text = "฿1,500"
#             price_note = "Complete professional analysis"

#         if st.button(f"🎯 Get Complete Analysis - {price_text}", type="primary", use_container_width=True):
#             handle_enhanced_payment(complexity_level, pattern_count, price_text)

#         # Money-back guarantee using Streamlit success component
#         st.success("💯 **Satisfaction Guarantee:** If your analysis doesn't provide clear transformation insights, full refund within 7 days.")

# def handle_enhanced_payment(complexity_level, pattern_count, price_text):
#     """Handle enhanced Stripe payment with comprehensive assessment metadata"""

#     # Generate comprehensive assessment metadata for Stripe
#     try:
#         if hasattr(st.session_state, 'responses') and st.session_state.responses:
#             from utils.config import EnhancedAssessmentConfig
#             temp_assessment = EnhancedAssessmentConfig()
#             profile = temp_assessment.generate_enhanced_profile(st.session_state.responses)

#             # Extract dominant patterns for metadata
#             pattern_hierarchy = profile.get('pattern_hierarchy', {})
#             dominant_patterns = {}
#             if 'dominant_pattern' in pattern_hierarchy:
#                 dominant_patterns[pattern_hierarchy['dominant_pattern']['name']] = pattern_hierarchy['dominant_pattern']['score']

#             enhanced_scores = profile.get('enhanced_pattern_scores', {})
#             top_patterns = sorted(enhanced_scores.items(), key=lambda x: x[1] if isinstance(x[1], (int, float)) else 0, reverse=True)[:3]
#             for pattern, score in top_patterns:
#                 if isinstance(score, (int, float)) and pattern not in dominant_patterns:
#                     dominant_patterns[pattern] = score
#         else:
#             dominant_patterns = {'complex_patterns': 5.0}
#             profile = {}
#     except:
#         dominant_patterns = {'complex_patterns': 5.0}
#         profile = {}

#     # Calculate pricing based on complexity
#     base_price = 1500 if complexity_level != "High" else 1800

#     # Comprehensive Stripe metadata package
#     assessment_metadata = {
#         "user_id": st.session_state.get("user_id", f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"),
#         "assessment_id": f"assess_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{st.session_state.get('user_id', 'anon')[-6:]}",
#         "product_type": "behavioral_pattern_analysis",
#         "complexity_level": complexity_level,
#         "pattern_count": str(pattern_count),
#         "dominant_patterns": list(dominant_patterns.keys())[:3],
#         "pattern_scores": {k: f"{v:.1f}" for k, v in dominant_patterns.items()},
#         "total_questions_answered": len(st.session_state.get('responses', {})),
#         "completion_time": datetime.now().isoformat(),
#         "urgency_level": determine_urgency_level(dominant_patterns),
#         "success_probability": f"{calculate_success_probability(dominant_patterns):.1f}%",

#         # Pricing and value proposition
#         "base_price": str(base_price),
#         "currency": "THB",
#         "price_text": price_text,
#         "discount_applied": "40%" if base_price == 1500 else "28%",
#         "original_value": "2500",

#         # Clinical recommendations
#         "estimated_sessions": str(get_session_estimate(complexity_level, pattern_count)),
#         "timeline_estimate": get_timeline_estimate(complexity_level),
#         "recommended_approach": get_personalized_approach(dominant_patterns),

#         # Cost analysis summary
#         "weekly_impact_hours": str(calculate_weekly_impact(dominant_patterns)),
#         "five_year_projection": str(calculate_five_year_cost(dominant_patterns)),
#         "roi_multiple": str(calculate_roi_multiple(base_price, dominant_patterns)),

#         # Contact and preferences
#         "contact_email": st.session_state.get("contact_email", ""),
#         "contact_phone": st.session_state.get("contact_phone", ""),
#         "preferred_contact_time": st.session_state.get("preferred_time", ""),
#         "location": st.session_state.get("location", "Bangkok"),
#         "language_preference": "EN",

#         # Therapist dashboard information
#         "priority_flag": "high" if complexity_level == "High" else "standard",
#         "report_complexity": "advanced" if pattern_count >= 4 else "standard",
#         "therapeutic_focus": determine_therapeutic_focus(dominant_patterns),
#         "intervention_urgency": calculate_intervention_urgency(dominant_patterns),

#         # Technical metadata
#         "assessment_version": "2.0",
#         "analysis_engine": "enhanced_clinical_v2",
#         "report_format": "comprehensive_pdf",
#         "delivery_method": "email_download",
#         "guarantee_period": "7_days"
#     }

#     # Store comprehensive metadata in session state
#     st.session_state.payment_metadata = assessment_metadata
#     st.session_state.payment_context = {
#         'complexity_level': complexity_level,
#         'pattern_count': pattern_count,
#         'price_text': price_text,
#         'analysis_type': f'{complexity_level} Complexity Behavioral Pattern Analysis',
#         'timestamp': str(datetime.now()),
#         'metadata': assessment_metadata
#     }

#     # Display processing message with personalization
#     st.success(f"🎉 Processing your {complexity_level.lower()}-complexity analysis...")
#     st.info(f"🔄 Preparing personalized report for {len(dominant_patterns)} dominant patterns...")
#     st.balloons()

#     # Here would be actual Stripe integration:
#     # stripe.checkout.Session.create(
#     #     payment_method_types=['card'],
#     #     line_items=[{
#     #         'price_data': {
#     #             'currency': 'thb',
#     #             'product_data': {
#     #                 'name': f'{complexity_level} Complexity Behavioral Pattern Analysis',
#     #                 'description': f'Complete analysis for {pattern_count}-pattern constellation'
#     #             },
#     #             'unit_amount': base_price * 100,  # Stripe uses cents
#     #         },
#     #         'quantity': 1,
#     #     }],
#     #     metadata=assessment_metadata,
#     #     mode='payment',
#     #     success_url='your_domain.com/success?session_id={CHECKOUT_SESSION_ID}',
#     #     cancel_url='your_domain.com/assessment',
#     #     customer_email=assessment_metadata.get('contact_email'),
#     # )

#     # Generate comprehensive PDF report
#     try:
#         from utils.config import PDFReportGenerator
#         pdf_report = PDFReportGenerator.generate_comprehensive_report(
#             assessment_metadata, profile, st.session_state.get('responses', {})
#         )
#         PDFReportGenerator.save_report_to_session(pdf_report['html_content'], assessment_metadata)
#         st.session_state.pdf_generated = True
#     except Exception as e:
#         st.session_state.pdf_generated = False
#         st.session_state.pdf_error = str(e)

#     # Trigger advanced personalized email notifications
#     try:
#         from utils.config import EmailConfig

#         # Get advanced analytics for personalized emails
#         pattern_scores = enhanced_assessment.pattern_scores
#         dominant_pattern_id = hierarchy.get("dominant_pattern", {}).get("id", 1)

#         # Send personalized client email
#         personalized_client_email = EmailConfig.generate_client_email_personalized(
#             assessment_metadata,
#             dominant_pattern_id,
#             pattern_scores,
#             responses
#         )

#         # Send standard emails (therapist report remains the same for now)
#         email_results = EmailConfig.send_assessment_emails(assessment_metadata, profile)

#         # Store personalized email for demo purposes
#         st.session_state.personalized_client_email = personalized_client_email

#         if email_results['client'] and email_results['therapist']:
#             st.session_state.emails_sent = True
#             st.session_state.email_status = "success"
#         else:
#             st.session_state.email_status = "partial"
#             st.session_state.email_errors = email_results.get('errors', [])
#     except Exception as e:
#         st.session_state.email_status = "failed"
#         st.session_state.email_errors = [str(e)]

#     # For demo: Set payment complete and show results
#     st.session_state.payment_complete = True
#     st.rerun()

# def analyze_pattern_reinforcement_cycles(pattern_scores):
#     """Advanced pattern interaction analysis - identifies how patterns reinforce each other"""
#     interactions = []

#     # Define interaction rules based on clinical observation
#     reinforcement_patterns = {
#         (1, 5): {
#             'description': "Unhappiness culture makes achievement feel dangerous - success triggers guilt",
#             'intervention': "Permission installation before achievement work",
#             'cycle': "Success → Guilt → Self-sabotage → Confirms unworthiness"
#         },
#         (2, 4): {
#             'description': "Power struggles create either/or thinking - compromise feels like defeat",
#             'intervention': "Collaboration training before binary thinking work",
#             'cycle': "Authority challenge → Binary response → Conflict → Reinforces resistance"
#         },
#         (3, 6): {
#             'description': "Systematic mistrust drives mask-wearing - authenticity feels unsafe",
#             'intervention': "Safety building before authenticity integration",
#             'cycle': "Vulnerability → Anticipated rejection → Mask up → Confirms mistrust"
#         },
#         (7, 8): {
#             'description': "Self-sacrifice serves family missions - own needs feel selfish",
#             'intervention': "Family loyalty work before self-care installation",
#             'cycle': "Personal need → Family guilt → Self-denial → Resentment builds"
#         },
#         (1, 6): {
#             'description': "Unhappiness culture drives authenticity hiding - real self feels dangerous",
#             'intervention': "Gradual authenticity permission in safe contexts",
#             'cycle': "Authentic moment → Fear of disappointment → Hide real self → Isolation"
#         },
#         (3, 7): {
#             'description': "Mistrust creates over-giving to prove worthiness",
#             'intervention': "Trust building before boundary work",
#             'cycle': "Mistrust → Over-give to prove value → Burnout → More mistrust"
#         }
#     }

#     # Convert pattern names to IDs for comparison
#     pattern_name_to_id = {
#         'unhappiness_culture': 1, 'power_struggles': 2, 'systematic_mistrust': 3,
#         'separation_division': 4, 'doing_vs_being': 5, 'compartmentalized_authenticity': 6,
#         'self_sacrifice': 7, 'inherited_missions': 8, 'digital_despair': 9,
#         'perfectionism': 10, 'social_anxiety': 11
#     }

#     # Get active patterns (score > 5)
#     active_patterns = {}
#     for pattern_name, score in pattern_scores.items():
#         if isinstance(score, (int, float)) and score > 5:
#             pattern_id = pattern_name_to_id.get(pattern_name)
#             if pattern_id:
#                 active_patterns[pattern_id] = score

#     # Find reinforcement interactions
#     for (pattern1, pattern2), interaction_data in reinforcement_patterns.items():
#         if pattern1 in active_patterns and pattern2 in active_patterns:
#             strength = min(active_patterns[pattern1], active_patterns[pattern2])
#             interactions.append({
#                 'patterns': [pattern1, pattern2],
#                 'strength': round(strength, 1),
#                 'description': interaction_data['description'],
#                 'cycle': interaction_data['cycle'],
#                 'intervention_note': interaction_data['intervention'],
#                 'priority': 'HIGH' if strength > 7 else 'MEDIUM' if strength > 5.5 else 'LOW'
#             })

#     # Sort by strength (highest impact first)
#     interactions.sort(key=lambda x: x['strength'], reverse=True)
#     return interactions

# def calculate_comprehensive_costs(pattern_scores, responses, trigger_chain=None, lifestyle_factors=None):
#     """Advanced cost analysis engine with 5-year projections as per Phase 7 specifications"""

#     # Import numpy for calculations (using basic math if numpy not available)
#     try:
#         import numpy as np
#         np_available = True
#     except ImportError:
#         np_available = False

#     if not pattern_scores:
#         return {
#             'weekly': {'time_hours': 8.0, 'opportunity_count': 1, 'relationship_incidents': 2, 'energy_drain_percent': 35},
#             'five_year': {'lost_opportunities': 15000, 'stress_costs': 12000, 'relationship_costs': 8000, 'total_cost': 35000},
#             'roi': 875
#         }

#     # Convert pattern scores to numeric values
#     numeric_scores = {}
#     for k, v in pattern_scores.items():
#         if isinstance(v, (int, float)):
#             numeric_scores[k] = v
#         elif isinstance(v, str):
#             try:
#                 numeric_scores[k] = float(v)
#             except:
#                 numeric_scores[k] = 0
#         else:
#             numeric_scores[k] = 0

#     if not numeric_scores:
#         return {
#             'weekly': {'time_hours': 8.0, 'opportunity_count': 1, 'relationship_incidents': 2, 'energy_drain_percent': 35},
#             'five_year': {'lost_opportunities': 15000, 'stress_costs': 12000, 'relationship_costs': 8000, 'total_cost': 35000},
#             'roi': 875
#         }

#     # Calculate mean using numpy if available, otherwise basic math
#     if np_available:
#         pattern_mean = np.mean(list(numeric_scores.values()))
#     else:
#         pattern_mean = sum(numeric_scores.values()) / len(numeric_scores) if numeric_scores else 0

#     # Weekly impact calculations (exact formula from CLAUDE.md)
#     time_cost = 8 + (len(numeric_scores) * 1.5) + (pattern_mean * 2)

#     # Opportunity cost (missed chances per week)
#     opportunity_cost = min(len(numeric_scores) / 2, 3)

#     # Relationship strain incidents
#     relationship_cost = min(len(numeric_scores), 5)

#     # Energy drain percentage
#     energy_drain = 30 + (pattern_mean * 10) + (len(numeric_scores) * 5)

#     # 5-year projections (exact formula from CLAUDE.md)
#     five_year_lost_opportunities = len(numeric_scores) * pattern_mean * 2000 * 5
#     five_year_stress_costs = len(numeric_scores) * 1500 * 5
#     five_year_relationship_costs = min(len(numeric_scores) * 800 * 5, 25000)

#     total_five_year_cost = five_year_lost_opportunities + five_year_stress_costs + five_year_relationship_costs

#     # ROI calculation (exact formula from CLAUDE.md)
#     intervention_cost = 4000  # ฿4,000 for 3 sessions
#     roi = ((total_five_year_cost - intervention_cost) / intervention_cost) * 100 if intervention_cost > 0 else 0

#     return {
#         'weekly': {
#             'time_hours': round(time_cost, 1),
#             'opportunity_count': opportunity_cost,
#             'relationship_incidents': relationship_cost,
#             'energy_drain_percent': min(energy_drain, 95)
#         },
#         'five_year': {
#             'lost_opportunities': int(five_year_lost_opportunities),
#             'stress_costs': int(five_year_stress_costs),
#             'relationship_costs': int(five_year_relationship_costs),
#             'total_cost': int(total_five_year_cost)
#         },
#         'roi': int(roi)
#     }

# def analyze_pattern_interactions(pattern_scores):
#     """Pattern interaction analysis as per Phase 7 specifications"""
#     interactions = []

#     # Convert to numeric scores and filter high patterns (>5)
#     numeric_scores = {}
#     for k, v in pattern_scores.items():
#         if isinstance(v, (int, float)):
#             numeric_scores[k] = v
#         elif isinstance(v, str):
#             try:
#                 numeric_scores[k] = float(v)
#             except:
#                 numeric_scores[k] = 0
#         else:
#             numeric_scores[k] = 0

#     high_patterns = {k: v for k, v in numeric_scores.items() if v > 5}

#     # Pattern mapping for interaction rules (exact from CLAUDE.md)
#     pattern_name_to_id = {
#         'unhappiness_culture': 1,
#         'power_struggles': 2,
#         'systematic_mistrust': 3,
#         'binary_thinking': 4,
#         'achievement_addiction': 5,
#         'compartmentalized_authenticity': 6,
#         'self_sacrifice': 7,
#         'inherited_missions': 8
#     }

#     # Reverse mapping
#     id_to_pattern_name = {v: k for k, v in pattern_name_to_id.items()}

#     # Interaction rules (exact from CLAUDE.md)
#     interaction_rules = {
#         (1, 5): "Unhappiness culture reinforces achievement addiction - success feels dangerous",
#         (2, 4): "Power struggles create binary thinking - compromise feels like defeat",
#         (3, 6): "Systematic mistrust drives compartmentalized authenticity - safety through masks",
#         (7, 8): "Self-sacrifice serves inherited missions - others' dreams before own needs"
#     }

#     # Find pattern interactions
#     for (pattern1_id, pattern2_id), description in interaction_rules.items():
#         pattern1_name = id_to_pattern_name.get(pattern1_id)
#         pattern2_name = id_to_pattern_name.get(pattern2_id)

#         if (pattern1_name in high_patterns and pattern2_name in high_patterns):
#             interactions.append({
#                 'patterns': [pattern1_name, pattern2_name],
#                 'mechanism': description,
#                 'strength': min(high_patterns[pattern1_name], high_patterns[pattern2_name])
#             })

#     return interactions

# def refine_success_prediction(pattern_scores, interactions, neuroplasticity_score=None, user_responses=None):
#     """Enhanced success prediction system using pattern interactions and advanced analytics"""

#     # Base success rate
#     base_success_rate = 85.0

#     # Convert pattern scores to numeric
#     numeric_scores = {}
#     for k, v in pattern_scores.items():
#         if isinstance(v, (int, float)):
#             numeric_scores[k] = v
#         elif isinstance(v, str):
#             try:
#                 numeric_scores[k] = float(v)
#             except:
#                 numeric_scores[k] = 0
#         else:
#             numeric_scores[k] = 0

#     if not numeric_scores:
#         return {
#             'probability': 75.0,
#             'confidence_interval': '±15%',
#             'success_category': 'moderate_likelihood',
#             'key_recommendations': ['Standard hypnotherapy protocol', 'Regular follow-up sessions', 'Practice self-awareness exercises']
#         }

#     # Calculate pattern intensity factors
#     severe_patterns = sum(1 for score in numeric_scores.values() if score >= 6.5)
#     moderate_patterns = sum(1 for score in numeric_scores.values() if 4.5 <= score < 6.5)
#     pattern_mean = sum(numeric_scores.values()) / len(numeric_scores)

#     # Adjustment factors
#     severity_adjustment = (severe_patterns * -8) + (moderate_patterns * -4)
#     complexity_adjustment = -2 if len(numeric_scores) >= 5 else 0

#     # Pattern interaction penalties
#     interaction_penalty = len(interactions) * -3 if interactions else 0

#     # Neuroplasticity bonus
#     neuroplasticity_bonus = 0
#     if neuroplasticity_score:
#         if neuroplasticity_score >= 15:
#             neuroplasticity_bonus = 8
#         elif neuroplasticity_score >= 12:
#             neuroplasticity_bonus = 5
#         elif neuroplasticity_score >= 9:
#             neuroplasticity_bonus = 2

#     # Specific pattern adjustments based on clinical success rates
#     pattern_adjustments = {
#         'unhappiness_culture': -5,  # More resistant to change
#         'achievement_addiction': -3,  # Identity-based resistance
#         'power_struggles': -4,  # Behavioral flexibility issues
#         'systematic_mistrust': -6,  # Trust building takes time
#         'self_sacrifice': 2,  # Often motivated to change
#         'binary_thinking': -2,  # Cognitive rigidity
#         'compartmentalized_authenticity': -1,  # Moderate challenge
#         'inherited_missions': -3  # Deep-rooted patterns
#     }

#     specific_adjustment = sum(pattern_adjustments.get(pattern, 0) for pattern in numeric_scores.keys() if numeric_scores[pattern] >= 4)

#     # Calculate final probability
#     final_probability = base_success_rate + severity_adjustment + complexity_adjustment + interaction_penalty + neuroplasticity_bonus + specific_adjustment

#     # Ensure reasonable bounds
#     final_probability = max(60.0, min(95.0, final_probability))

#     # Determine confidence interval based on pattern complexity
#     if pattern_mean >= 6.5 or severe_patterns >= 3:
#         confidence_interval = '±18%'
#     elif pattern_mean >= 5.0 or severe_patterns >= 2:
#         confidence_interval = '±15%'
#     else:
#         confidence_interval = '±12%'

#     # Determine success category
#     if final_probability >= 85:
#         success_category = 'high_likelihood'
#     elif final_probability >= 75:
#         success_category = 'moderate_likelihood'
#     else:
#         success_category = 'requires_intensive_approach'

#     # Generate key recommendations based on analysis
#     recommendations = []

#     if severe_patterns >= 2:
#         recommendations.append('Multi-session approach recommended (3-4 sessions)')
#         recommendations.append('Enhanced resistance management protocols')

#     if interactions:
#         recommendations.append('Address pattern interactions systematically')
#         recommendations.append('Staged intervention approach for complex patterns')

#     if pattern_mean >= 6:
#         recommendations.append('Intensive initial session (120+ minutes)')
#         recommendations.append('Daily reinforcement exercises')

#     # Pattern-specific recommendations
#     if 'systematic_mistrust' in numeric_scores and numeric_scores['systematic_mistrust'] >= 5:
#         recommendations.append('Extended rapport-building phase essential')

#     if 'achievement_addiction' in numeric_scores and numeric_scores['achievement_addiction'] >= 5:
#         recommendations.append('Identity-safe transformation approach required')

#     if 'unhappiness_culture' in numeric_scores and numeric_scores['unhappiness_culture'] >= 5:
#         recommendations.append('Joy/success desensitization protocols')

#     # Default recommendations if none specific
#     if not recommendations:
#         recommendations = [
#             'Standard rapid transformation protocol',
#             'Post-session integration support',
#             'Environmental trigger management'
#         ]

#     return {
#         'probability': round(final_probability, 1),
#         'confidence_interval': confidence_interval,
#         'success_category': success_category,
#         'key_recommendations': recommendations[:3],  # Limit to top 3
#         'analysis_factors': {
#             'base_rate': base_success_rate,
#             'severity_adjustment': severity_adjustment,
#             'interaction_penalty': interaction_penalty,
#             'neuroplasticity_bonus': neuroplasticity_bonus,
#             'final_adjustment': specific_adjustment
#         }
#     }

# def render_advanced_analytics_dashboard(profile, responses):
#     """Comprehensive analytics dashboard for Phase 7 - Streamlit native approach"""

#     st.markdown("---")
#     st.markdown("## ADVANCED ANALYTICS DASHBOARD")
#     st.markdown("**Enhanced analysis using Phase 7 algorithms**")

#     try:
#         # Get pattern scores
#         pattern_scores = profile.get('enhanced_pattern_scores', {})
#         if not pattern_scores:
#             st.info("📈 Analytics require pattern analysis completion")
#             return

#         # 1. Advanced Cost Analysis
#         cost_analysis = calculate_comprehensive_costs(pattern_scores, responses)
#         pattern_interactions = analyze_pattern_interactions(pattern_scores)

#         # 2. Enhanced Success Prediction
#         neuroplasticity = profile.get('neuroplasticity_assessment', {})
#         neuroplasticity_score = neuroplasticity.get('total_score', 12)
#         success_prediction = refine_success_prediction(pattern_scores, pattern_interactions, neuroplasticity_score, responses)

#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("**ENHANCED COST ANALYSIS**")

#             # Weekly impact metrics
#             weekly = cost_analysis['weekly']
#             st.metric("Weekly Time Loss", f"{weekly['time_hours']} hours")
#             st.metric("Missed Opportunities", f"{weekly['opportunity_count']:.1f} per week")
#             st.metric("Energy Drain", f"{weekly['energy_drain_percent']:.0f}%")

#             # Five-year projections
#             st.markdown("**Five-year projections:**")
#             five_year = cost_analysis['five_year']
#             st.write(f"Lost Opportunities: ฿{five_year['lost_opportunities']:,}")
#             st.write(f"Stress Costs: ฿{five_year['stress_costs']:,}")
#             st.write(f"Relationship Costs: ฿{five_year['relationship_costs']:,}")

#             st.metric("Total Cost", f"฿{five_year['total_cost']:,}")
#             st.metric("ROI from Intervention", f"{cost_analysis['roi']:,}%")

#         with col2:
#             st.markdown("**ENHANCED SUCCESS PREDICTION**")

#             prediction = success_prediction

#             # Use simple metric display instead of HTML
#             st.metric("Success Probability", f"{prediction['probability']}%")
#             st.write(f"Confidence: {prediction['confidence_interval']}")
#             st.write(f"Category: {prediction['success_category'].replace('_', ' ').title()}")

#             st.markdown("**Key recommendations:**")
#             for i, rec in enumerate(prediction['key_recommendations'], 1):
#                 st.write(f"{i}. {rec}")

#             # Analysis factors breakdown
#             with st.expander("Prediction Analysis Factors"):
#                 factors = prediction['analysis_factors']
#                 st.write(f"Base Success Rate: {factors['base_rate']}%")
#                 st.write(f"Severity Adjustment: {factors['severity_adjustment']:+}")
#                 st.write(f"Interaction Penalty: {factors['interaction_penalty']:+}")
#                 st.write(f"Neuroplasticity Bonus: {factors['neuroplasticity_bonus']:+}")
#                 st.write(f"Pattern-Specific: {factors['final_adjustment']:+}")

#         # 3. Pattern Interaction Analysis
#         st.markdown("**PATTERN INTERACTION ANALYSIS**")
#         if pattern_interactions:
#             st.info(f"{len(pattern_interactions)} critical pattern interactions detected")

#             for interaction in pattern_interactions:
#                 pattern_names = [p.replace('_', ' ').title() for p in interaction['patterns']]
#                 st.markdown(f"**{pattern_names[0]} ↔ {pattern_names[1]}**")
#                 st.write(f"Mechanism: {interaction['mechanism']}")
#                 st.write(f"Interaction Strength: {interaction['strength']:.1f}/8")
#                 st.divider()

#         else:
#             st.success("No significant pattern interactions detected - simpler intervention possible")

#         # 4. Comparative Analysis
#         st.markdown("**COMPARATIVE INTERVENTION ANALYSIS**")

#         comparison_metrics = [
#             ("Timeline", "12-18 months", f"{get_timeline_estimate('Moderate')}"),
#             ("Success Rate", "45-60%", f"{success_prediction['probability']:.0f}%"),
#             ("Session Count", "24-48 sessions", f"{get_session_estimate('Moderate', len(pattern_scores))}"),
#             ("Total Cost", "฿25,000-40,000", "฿4,000-6,000"),
#             ("Approach", "High complexity", "Targeted precision")
#         ]

#         for metric, traditional, rapid in comparison_metrics:
#             col1, col2, col3 = st.columns([1, 1, 1])
#             with col1:
#                 st.write(f"**{metric}**")
#             with col2:
#                 st.write(traditional)
#             with col3:
#                 st.write(f"✅ {rapid}")

#     except Exception as e:
#         st.error(f"Analytics error: {str(e)}")
#         st.info("Contact support if this persists")

# def render_aha_moment_bridge(profile, dominant_pattern):
#     """Render the aha moment bridge with teaser insights"""

#     # Get dominant pattern from profile if available
#     if isinstance(profile, dict) and 'pattern_hierarchy' in profile:
#         dominant_pattern = profile['pattern_hierarchy']['dominant_pattern']['name']

#     # Hidden mechanism teasers based on pattern
#     mechanism_teasers = {
#         'unhappiness_culture': [
#             "Why your brain sabotages good moments (it's actually trying to protect you)",
#             "The unconscious 'disappointment prevention' system that blocks joy",
#             "How your pattern creates a self-fulfilling prophecy of unhappiness"
#         ],
#         'power_struggles': [
#             "Why collaboration feels dangerous to your nervous system",
#             "The hidden identity protection mechanism that creates resistance",
#             "How your independence actually maintains dependence on old patterns"
#         ],
#         'systematic_mistrust': [
#             "Why trust feels more dangerous than isolation",
#             "The early warning system that's become hypersensitive",
#             "How your protection mechanism now limits your growth"
#         ],
#         'default': [
#             "The unconscious programs running your daily decisions",
#             "Why logical solutions haven't worked (and what will)",
#             "The hidden payoffs that keep your patterns in place"
#         ]
#     }

#     # Future predictions
#     future_predictions = {
#         'unhappiness_culture': "Without intervention, this pattern typically leads to increasing isolation from positive experiences and relationships.",
#         'power_struggles': "This pattern often escalates, creating more conflicts and limiting collaborative opportunities over time.",
#         'systematic_mistrust': "Trust issues generally worsen without intervention, leading to increasing isolation and missed opportunities.",
#         'default': "These patterns tend to solidify over time, creating increasingly limited life experiences."
#     }

#     teasers = mechanism_teasers.get(dominant_pattern, mechanism_teasers['default'])
#     prediction = future_predictions.get(dominant_pattern, future_predictions['default'])

#     st.markdown(f"""
#     <div class="aha-bridge-container" style="
#         background: linear-gradient(135deg, #F3E8FF 0%, #E9D5FF 100%);
#         border-radius: 12px;
#         padding: 2rem;
#         margin: 2rem 0;
#         border: 1px solid #C4B5FD;
#         box-shadow: 0 4px 16px rgba(139, 92, 246, 0.1);
#     ">
#         <div class="bridge-header" style="text-align: center; margin-bottom: 1.5rem;">
#             <h3 style="color: #7C3AED; margin: 0 0 0.5rem 0; font-size: 1.5rem;">🔍 The hidden layer</h3>
#             <p style="color: #8B5CF6; margin: 0; font-size: 1rem;">What your assessment reveals beyond the surface</p>
#         </div>

#         <div class="teaser-insights" style="background: white; border-radius: 10px; padding: 1.5rem; margin-bottom: 1.5rem;">
#             <h4 style="color: #6B21A8; margin: 0 0 1rem 0;">Three protective mechanisms we haven't mentioned yet:</h4>
#             <ul style="margin: 0; padding-left: 1.5rem; color: #581C87;">
#                 {' '.join([f'<li style="margin: 0.5rem 0; line-height: 1.5;">{teaser}</li>' for teaser in teasers])}
#             </ul>
#         </div>

#         <div class="paradox-revelation" style="
#             background: rgba(124, 58, 237, 0.1);
#             border-left: 4px solid #7C3AED;
#             border-radius: 6px;
#             padding: 1.25rem;
#             margin-bottom: 1.5rem;
#         ">
#             <h4 style="color: #6B21A8; margin: 0 0 0.75rem 0;">⚡ The paradox</h4>
#             <p style="color: #581C87; margin: 0; line-height: 1.6;">
#                 Why your logical mind keeps you stuck: <em>The very patterns protecting you are now limiting you.</em>
#                 Your conscious efforts to change often strengthen the unconscious resistance.
#             </p>
#         </div>

#         <div class="future-prediction" style="
#             background: rgba(239, 68, 68, 0.1);
#             border-left: 4px solid #EF4444;
#             border-radius: 6px;
#             padding: 1.25rem;
#             margin-bottom: 1.5rem;
#         ">
#             <h4 style="color: #DC2626; margin: 0 0 0.75rem 0;">📈 Trajectory without intervention</h4>
#             <p style="color: #B91C1C; margin: 0; line-height: 1.6;">{prediction}</p>
#         </div>

#         <div class="missing-pieces" style="text-align: center;">
#             <h4 style="color: #7C3AED; margin: 0 0 1rem 0;">What's missing from this picture</h4>
#             <p style="color: #6B21A8; margin: 0 0 1rem 0;">
#                 This free analysis covers your behavioral patterns. Your complete clinical profile includes:
#             </p>
#             <div style="
#                 background: white;
#                 border-radius: 8px;
#                 padding: 1.25rem;
#                 text-align: left;
#             ">
#                 <ul style="margin: 0; color: #4B5563; line-height: 1.8;">
#                     <li>🧠 Your subconscious belief system map with specific reprogramming protocols</li>
#                     <li>🎯 Exact intervention protocols optimized for your brain type and resistance patterns</li>
#                     <li>📅 Session-by-session transformation roadmap with predicted timeline</li>
#                     <li>📊 Success probability calculator with optimization strategies</li>
#                     <li>💰 Complete cost analysis: 5-year impact vs. intervention ROI</li>
#                     <li>💪 Your transformation readiness profile with empowerment factors</li>
#                 </ul>
#             </div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# def show_comprehensive_results(enhanced_assessment, responses):
#     """Show comprehensive results with enhanced pattern recognition and analysis"""

#     # Generate comprehensive profile
#     profile = enhanced_assessment.generate_enhanced_profile(responses)

#     # Get pattern scores for advanced analytics
#     pattern_scores = enhanced_assessment.pattern_scores

#     # Get dominant pattern ID for personalized content
#     hierarchy = profile.get("pattern_hierarchy", {})
#     dominant_pattern_data = hierarchy.get("dominant_pattern", {})
#     dominant_pattern_id = dominant_pattern_data.get("id", 1)

#     # Enhanced header
#     st.markdown("#### 🎯 COMPREHENSIVE TRANSFORMATION ASSESSMENT")
#     st.markdown("Discover the hidden patterns shaping your daily experience")

#     # Progress bar without separator
#     st.progress(100/100, text="Analysis Complete: 100%")

#     # Add padding between progress and content
#     st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)

#     # Advanced Pattern Recognition Hero Section with cycle analysis
#     reinforcement_cycles = analyze_pattern_reinforcement_cycles(pattern_scores)
#     enhanced_success_prediction = calculate_enhanced_success_probability(profile, responses)
#     pattern_deep_dive = generate_pattern_deep_dive(dominant_pattern_id, pattern_scores, responses)

#     # Pattern Recognition Hero Section
#     render_pattern_recognition_hero(None, None, None, profile)

#     # Pattern Interaction Analysis
#     if reinforcement_cycles:
#         st.markdown("## 🔄 Pattern Reinforcement Cycles")
#         for i, cycle in enumerate(reinforcement_cycles[:3]):  # Show top 3 cycles
#             with st.container():
#                 st.markdown(f"""
#                 <div style='background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
#                            padding: 16px; border-radius: 8px; margin: 8px 0;
#                            border-left: 4px solid #4CA1A3;'>
#                     <h4 style='color: #273548; margin-bottom: 8px;'>Cycle {i+1}: {cycle['cycle_name']}</h4>
#                     <p style='color: #556D7A; margin-bottom: 8px;'><strong>How it works:</strong> {cycle['explanation']}</p>
#                     <p style='color: #556D7A; margin-bottom: 8px;'><strong>Intervention point:</strong> {cycle['intervention_window']}</p>
#                     <p style='color: #4CA1A3; margin: 0;'><strong>Therapeutic priority:</strong> Session {cycle['therapeutic_session']}</p>
#                 </div>
#                 """, unsafe_allow_html=True)

#     # Enhanced Success Prediction with Multi-factors
#     st.markdown("## 📊 Enhanced Success Probability Analysis")
#     col1, col2 = st.columns(2)

#     with col1:
#         success_rate = enhanced_success_prediction.get('final_probability', 85)
#         st.metric(
#             "Transformation Success Rate",
#             f"{success_rate}%",
#             delta=f"+{success_rate-75}% vs baseline",
#             delta_color="normal"
#         )

#         confidence = enhanced_success_prediction.get('confidence_level', 'High')
#         st.metric(
#             "Confidence Level",
#             confidence,
#             delta=enhanced_success_prediction.get('confidence_factors', 'Multiple positive indicators')[:30] + "..."
#         )

#     with col2:
#         timeline = enhanced_success_prediction.get('timeline_estimate', '3-4 weeks')
#         st.metric(
#             "Expected Timeline",
#             timeline,
#             delta=enhanced_success_prediction.get('timeline_confidence', 'Based on pattern complexity')[:30] + "..."
#         )

#         session_count = enhanced_success_prediction.get('recommended_sessions', 2)
#         st.metric(
#             "Recommended Sessions",
#             f"{session_count} sessions",
#             delta=enhanced_success_prediction.get('session_rationale', 'Optimal for your patterns')[:30] + "..."
#         )

#     # Pattern Deep Dive Manifestations
#     if pattern_deep_dive:
#         st.markdown("## 🎯 Your Pattern Deep Dive")

#         main_pattern = pattern_deep_dive.get('main_pattern', {})
#         if main_pattern:
#             with st.container():
#                 st.markdown(f"""
#                 <div style='background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
#                            padding: 20px; border-radius: 12px; margin: 12px 0;'>
#                     <h4 style='color: #273548;'>{main_pattern.get('name', 'Primary Pattern')}</h4>
#                     <p style='color: #556D7A;'><strong>Daily manifestation:</strong> {main_pattern.get('daily_manifestation', 'Not specified')}</p>
#                     <p style='color: #556D7A;'><strong>Origin context:</strong> {main_pattern.get('origin_context', 'Not specified')}</p>
#                     <p style='color: #556D7A;'><strong>Hidden benefit:</strong> {main_pattern.get('hidden_benefit', 'Not specified')}</p>
#                     <p style='color: #4CA1A3;'><strong>Transformation potential:</strong> {main_pattern.get('transformation_potential', 'High with targeted approach')}</p>
#                 </div>
#                 """, unsafe_allow_html=True)

#     # Pattern Hierarchy - Most Important Section
#     st.markdown("## YOUR BEHAVIORAL PATTERN PROFILE")
#     hierarchy = profile["pattern_hierarchy"]

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric(
#             "Dominant Pattern",
#             hierarchy["dominant_pattern"]["name"].replace("_", " ").title(),
#             f"{hierarchy['dominant_pattern']['score']}/8"
#         )
#     with col2:
#         st.metric(
#             "Primary Pattern",
#             hierarchy["primary_pattern"]["name"].replace("_", " ").title(),
#             f"{hierarchy['primary_pattern']['score']}/8"
#         )
#     with col3:
#         st.metric(
#             "Secondary Pattern",
#             hierarchy["secondary_pattern"]["name"].replace("_", " ").title(),
#             f"{hierarchy['secondary_pattern']['score']}/8"
#         )

#     # Session Planning
#     st.markdown("## YOUR TRANSFORMATION PLAN")
#     session_planning = profile["session_planning"]

#     st.write(f"Session 1 focus: {session_planning['session_1_focus']}")
#     st.write(f"Session 2 target: {session_planning['session_2_target']}")
#     st.write(f"Potential session 3 need: {session_planning['potential_session_3_need']}")

#     # Change Readiness
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric("Change Readiness Score", f"{profile['change_readiness_score']}/10")

#     # Behavioral Analysis
#     st.markdown("## UNDERSTANDING YOUR PATTERNS")
#     behavioral = profile["behavioral_analysis"]

#     col1, col2 = st.columns(2)
#     with col1:
#         if behavioral["core_limiting_beliefs"]:
#             st.markdown("**Core limiting beliefs**")
#             for belief in behavioral["core_limiting_beliefs"]:
#                 st.write(f"• {belief}")

#         if behavioral["hidden_benefits"]:
#             st.markdown("**Hidden benefits**")
#             for benefit in behavioral["hidden_benefits"]:
#                 st.write(f"• {benefit}")

#     with col2:
#         if behavioral["systemic_resistance"]:
#             st.markdown("**Potential challenges**")
#             for resistance in behavioral["systemic_resistance"]:
#                 st.write(f"• {resistance}")

#         if behavioral["identity_threats"]:
#             st.markdown("**Identity considerations**")
#             for threat in behavioral["identity_threats"]:
#                 st.write(f"• {threat}")

#     # Trigger-Response Patterns
#     if profile["trigger_response_mapping"]:
#         st.markdown("## YOUR TRIGGER-RESPONSE PATTERNS")
#         for pattern_name, pattern_data in profile["trigger_response_mapping"].items():
#             with st.expander(f"{pattern_name.replace('_', ' ').title()}"):
#                 st.write(f"Trigger: {pattern_data['trigger']}")
#                 st.write(f"Physical response: {pattern_data['physical_response']}")
#                 st.write(f"Automatic thought: {pattern_data['automatic_thought']}")
#                 st.write(f"Emotion: {pattern_data['emotion']}")
#                 st.write(f"Behavior: {pattern_data['behavior']}")
#                 st.write(f"Consequence: {pattern_data['consequence']}")

#     # Resistance Analysis
#     st.markdown("## THERAPEUTIC APPROACH RECOMMENDATIONS")
#     resistance = profile["resistance_analysis"]

#     st.markdown("**Predicted resistance points:**")
#     for i, point in enumerate(resistance["predicted_resistance_points"], 1):
#         st.write(f"{i}. {point}")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.write(f"Effective language: {resistance['intervention_keywords']}")
#     with col2:
#         st.write(f"Avoid using: {resistance['avoid_language']}")

#     # User Journey Summary
#     st.markdown("## YOUR JOURNEY SUMMARY")

#     col1, col2 = st.columns([2, 1])
#     with col1:
#         user_journey = profile.get('user_journey', {})

#         st.markdown("**Key insights**")
#         key_insights = user_journey.get('key_insights', [])
#         for insight in key_insights:
#             st.write(f"• {insight}")

#         st.markdown("**Your strongest patterns**")
#         strongest_patterns = user_journey.get('strongest_patterns_identified', [])
#         for pattern in strongest_patterns:
#             st.write(f"• {pattern}")

#         st.markdown("**Recommended focus areas**")
#         focus_areas = user_journey.get('recommended_focus_areas', [])
#         for area in focus_areas:
#             st.write(f"• {area}")

#         st.markdown("**Your next steps**")
#         next_steps = user_journey.get('next_steps', [])
#         for step in next_steps:
#             st.write(f"• {step}")

#     with col2:
#         st.markdown("**Assessment summary**")
#         st.metric("Questions Answered", profile.get('total_questions_answered', 0))
#         st.metric("Completion Rate", f"{profile.get('assessment_completion', 0):.0f}%")

#     # Success Probability Analysis
#     success_prob = profile.get('success_probability', {})
#     if success_prob:
#         st.markdown("## SUCCESS PROBABILITY ANALYSIS")

#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("Success Probability", f"{success_prob.get('probability', 85)}%")
#         with col2:
#             st.metric("Confidence Interval", success_prob.get('confidence_interval', '±12%'))
#         with col3:
#             success_category = success_prob.get('success_category', 'moderate_likelihood')
#             st.metric("Success Category", success_category.replace('_', ' ').title())

#         # Key recommendations
#         key_recs = success_prob.get('key_recommendations', [])
#         if key_recs:
#             st.markdown("**Key recommendations for success:**")
#             for rec in key_recs[:3]:
#                 st.write(f"• {rec}")

#     # Enhanced Pattern Analysis
#     enhanced_patterns = profile.get('enhanced_pattern_scores', {})
#     if enhanced_patterns:
#         with st.expander("Enhanced Pattern Analysis"):
#             st.markdown("**Advanced pattern detection results:**")
#             for pattern, score in enhanced_patterns.items():
#                 if score > 0:
#                     st.write(f"**{pattern.replace('_', ' ').title()}**: {score:.1f}/8")

#     # Aha Moment Bridge Section
#     st.markdown("---")
#     render_aha_moment_bridge(profile, None)

#     # Pattern Interaction Analysis (NEW)
#     pattern_interactions = profile.get('pattern_interaction_analysis', {})
#     if pattern_interactions:
#         with st.expander("🔗 Pattern Interaction Analysis"):
#             st.markdown(f"Complexity score: {pattern_interactions.get('complexity_score', 0):.1f}")

#             detected_interactions = pattern_interactions.get('detected_interactions', [])
#             if detected_interactions:
#                 st.markdown("**Pattern interactions detected:**")
#                 for interaction in detected_interactions:
#                     patterns = " ↔ ".join([p.replace('_', ' ').title() for p in interaction['patterns']])
#                     st.write(f"• **{patterns}**: {interaction['mechanism']}")

#     # Neuroplasticity Assessment (NEW)
#     neuroplasticity = profile.get('neuroplasticity_assessment', {})
#     if neuroplasticity:
#         with st.expander("🧘 Neuroplasticity Readiness"):
#             readiness_level = neuroplasticity.get('readiness_level', 'moderate_readiness')
#             st.markdown(f"Readiness level: {readiness_level.replace('_', ' ').title()}")

#             total_score = neuroplasticity.get('total_score', 0)
#             st.metric("Neuroplasticity Score", f"{total_score:.1f}/18")

#             recommendations = neuroplasticity.get('enhancement_recommendations', [])
#             if recommendations:
#                 st.markdown("**Enhancement recommendations:**")
#                 for rec in recommendations:
#                     st.write(f"• {rec}")

#     # Session Protocol Details (NEW)
#     session_protocol = profile.get('session_protocol', {})
#     if session_protocol:
#         with st.expander("Personalized Session Protocol"):
#             session_1 = session_protocol.get('session_1', {})
#             st.markdown(f"Hypnotic approach: {session_1.get('hypnotic_approach', 'standard').replace('_', ' ').title()}")
#             st.markdown(f"Session duration: {session_1.get('duration', 90)} minutes")

#             special_considerations = session_1.get('special_considerations', [])
#             if special_considerations:
#                 st.markdown("**Special considerations:**")
#                 for consideration in special_considerations:
#                     st.write(f"• {consideration.replace('_', ' ').title()}")

#     # Clinical Details (for practitioners)
#     with st.expander("🔬 Clinical Assessment Details (For Practitioners)"):
#         st.markdown("**Clinical pattern scores**")
#         clinical_scores = profile.get('clinical_scores', {})

#         for pattern, score in clinical_scores.items():
#             if score > 0:
#                 st.write(f"**{pattern.replace('_', ' ').title()}**: {score:.1f}")

#         st.markdown("**Severity assessment**")
#         severity = profile.get('severity_assessment', {})
#         for pattern, level in severity.items():
#             if level != 'subclinical':
#                 st.write(f"**{pattern.replace('_', ' ').title()}**: {level.title()}")

#         st.markdown("**Clinical recommendations**")
#         recommendations = profile.get('clinical_recommendations', [])
#         for rec in recommendations:
#             st.write(f"• {rec}")

#         # Secondary Gain Analysis (NEW)
#         secondary_gains = profile.get('secondary_gain_analysis', {})
#         if secondary_gains:
#             st.markdown("**Secondary gain analysis**")
#             total_gain = secondary_gains.get('total_secondary_gain', 0)
#             st.write(f"Total secondary gain score: {total_gain}")

#             if secondary_gains.get('identity_protection_level', 0) >= 2:
#                 st.write("High identity protection: Change may feel threatening to sense of self")

#         # Resistance Prediction Details (NEW)
#         resistance_prediction = profile.get('resistance_prediction', {})
#         if resistance_prediction:
#             st.markdown("**Resistance prediction analysis**")
#             st.write(f"Resistance level: {resistance_prediction.get('resistance_level', 'unknown').replace('_', ' ').title()}")
#             st.write(f"Primary type: {resistance_prediction.get('primary_resistance_type', 'unknown').replace('_', ' ').title()}")
#             st.write(f"Intervention approach: {resistance_prediction.get('intervention_approach', 'standard').replace('_', ' ').title()}")

#         # Cultural Adaptation (NEW)
#         cultural_factors = profile.get('cultural_adaptation', {})
#         if cultural_factors:
#             st.markdown("**Cultural adaptation requirements**")
#             adaptations = cultural_factors.get('adaptation_requirements', [])
#             for adaptation in adaptations:
#                 st.write(f"• {adaptation.replace('_', ' ').title()}")

#     # Advanced Analytics Dashboard (Phase 7)
#     render_advanced_analytics_dashboard(profile, responses)

#     # Email Notification Status (NEW)
#     render_email_status_notifications()

# def render_email_status_notifications():
#     """Display email notification status after assessment completion - Streamlit native"""

#     if hasattr(st.session_state, 'emails_sent') and st.session_state.emails_sent:
#         st.markdown("---")
#         st.markdown("## COMMUNICATION STATUS")

#         email_status = st.session_state.get('email_status', 'unknown')

#         if email_status == 'success':
#             st.success("Confirmation emails sent successfully!")

#             st.markdown("**Client confirmation sent with:**")
#             st.write("• Complete analysis summary")
#             st.write("• PDF report download link")
#             st.write("• Next steps timeline")
#             st.write("• Contact information")

#             st.markdown("**Therapist notification sent with:**")
#             st.write("• Priority case details")
#             st.write("• Pattern complexity analysis")
#             st.write("• Recommended intervention approach")
#             st.write("• 24-48 hour response timeline")

#             # PDF Download Section
#             if st.session_state.get('pdf_generated', False) and hasattr(st.session_state, 'latest_report'):
#                 st.markdown("## YOUR COMPREHENSIVE REPORT")

#                 col1, col2 = st.columns([2, 1])

#                 with col1:
#                     st.markdown("**15-20 page comprehensive analysis includes:**")
#                     st.write("• Executive summary with key insights")
#                     st.write("• Detailed pattern breakdown and scores")
#                     st.write("• Personalized transformation roadmap")
#                     st.write("• Clinical recommendations and approach")
#                     st.write("• Success probability analysis")
#                     st.write("• Cost-benefit breakdown")
#                     st.write("• Immediate action steps")

#                 with col2:
#                     report_data = st.session_state.latest_report

#                     # Download button for HTML version (demo)
#                     st.download_button(
#                         label="📥 Download Report",
#                         data=report_data['html_content'],
#                         file_name=report_data['filename'],
#                         mime="text/html",
#                         type="primary",
#                         use_container_width=True
#                     )

#                     st.info("Professional PDF conversion available upon consultation booking")

#             elif not st.session_state.get('pdf_generated', True):
#                 st.warning(f"PDF generation encountered an issue: {st.session_state.get('pdf_error', 'Unknown error')}")
#                 st.info("Contact our team for manual report delivery")

#             # Show generated emails for demo purposes
#             if hasattr(st.session_state, 'generated_emails'):
#                 with st.expander("View Generated Emails (Demo)"):
#                     emails = st.session_state.generated_emails[-2:]  # Last 2 emails

#                     for i, email in enumerate(emails, 1):
#                         email_type = "Client Confirmation" if email['type'] == 'client_confirmation' else "Therapist Report"

#                         st.markdown(f"**Email {i}: {email_type}**")
#                         st.write(f"Subject: {email['subject']}")
#                         st.write(f"Recipient: {email['recipient']}")

#                         if email['type'] == 'therapist_report':
#                             priority = email.get('priority', 'standard')
#                             st.write(f"Priority: {priority.upper()}")

#                         st.text_area(f"{email_type} Content", email['body'], height=200, disabled=True)
#                         st.divider()

#         elif email_status == 'partial':
#             st.warning("Partial email delivery")
#             st.write("Some emails were sent successfully, but there may have been issues with others.")
#             st.write("Our team will follow up manually within 24 hours.")

#             if hasattr(st.session_state, 'email_errors'):
#                 st.error(f"Errors: {'; '.join(st.session_state.email_errors)}")

#         elif email_status == 'failed':
#             st.error("Email delivery failed")
#             st.write("We encountered an issue sending your confirmation emails.")
#             st.write("Don't worry - your assessment data is saved and our team will contact you manually within 24 hours.")

#             if hasattr(st.session_state, 'email_errors'):
#                 st.error(f"Technical details: {'; '.join(st.session_state.email_errors)}")

#         # Contact information backup
#         st.markdown("**Need immediate assistance?**")
#         st.write("Email: info@rapidtransformation-bangkok.com")
#         st.write("Phone: +66-XX-XXX-XXXX (Available 9 AM - 8 PM)")
#         st.write("WhatsApp: Available for urgent inquiries")

# def main():
#     """Main application function"""

#     # Initialize assessment
#     enhanced_assessment = initialize_assessment()

#     # Initialize session state
#     if 'current_question' not in st.session_state:
#         st.session_state.current_question = 0
#     if 'responses' not in st.session_state:
#         st.session_state.responses = {}
#     if 'current_stage' not in st.session_state:
#         st.session_state.current_stage = QuestionnaireStage.STAGE_1_WELCOME

#     # Get all questions
#     all_questions = enhanced_assessment.get_enhanced_questions()
#     total_questions = len(all_questions)

#     # Check if assessment is complete
#     if st.session_state.current_question >= total_questions:
#         # Initialize contact_provided state if not present
#         if 'contact_provided' not in st.session_state:
#             st.session_state.contact_provided = False

#         # Show preliminary results and contact form if contact not provided yet
#         if not st.session_state.contact_provided:
#             try:
#                 show_preliminary_results(enhanced_assessment, st.session_state.responses)
#                 render_contact_form()
#             except Exception as e:
#                 st.error(f"Error loading results: {str(e)}")
#                 st.info("Please try refreshing the page or contact support.")
#                 # Provide fallback contact form
#                 render_contact_form()
#             return

#         # Show full results after contact is provided
#         st.markdown("#### BEHAVIORAL TRANSFORMATION ASSESSMENT")
#         st.markdown("Your detailed behavioral analysis and therapeutic roadmap")
#         st.divider()
#         try:
#             show_comprehensive_results(enhanced_assessment, st.session_state.responses)
#         except Exception as e:
#             st.error(f"Error loading comprehensive results: {str(e)}")
#             st.info("Please try refreshing the page or contact support.")

#         # Reset button
#         if st.button("Take Assessment Again", type="primary"):
#             # Clear session state
#             for key in list(st.session_state.keys()):
#                 if key.startswith(('current_question', 'responses', 'current_stage', 'contact_')):
#                     del st.session_state[key]
#             st.rerun()
#         return

#     # Get current question
#     current_q = all_questions[st.session_state.current_question]
#     current_question_number = st.session_state.current_question + 1

#     # Check if we need to show stage introduction and update header
#     current_stage = QuestionnaireStage(current_q['stage'])
#     stage_title = ""
#     if current_stage != st.session_state.current_stage:
#         st.session_state.current_stage = current_stage
#         stage_info = enhanced_assessment.get_stage_introduction(current_q['stage'])
#         stage_title = f" : {render_stage_introduction(stage_info, current_stage)}"

#     # Main assessment display

#     # Assessment Header
#     header_text = f"### COMPREHENSIVE TRANSFORMATION ASSESSMENT{stage_title}"
#     st.markdown(header_text)

#     # Enhanced Progress Display
#     try:
#         current_stage = current_q.get('stage')
#         stage_info = None
#         if current_stage and hasattr(enhanced_assessment, 'get_stage_info'):
#             stage_info = enhanced_assessment.get_stage_info(current_stage)
#         render_enhanced_progress_display(current_q, current_question_number, total_questions, stage_info)
#     except:
#         pass  # Fallback to basic display if enhanced fails

#     # Add padding between progress bar and question
#     st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

#     # Question Area
#     render_question_card(current_q, current_question_number, total_questions)

#     # Show enhanced pattern hints periodically
#     if hasattr(enhanced_assessment, 'generate_enhanced_profile') and st.session_state.responses:
#         try:
#             current_profile = enhanced_assessment.generate_enhanced_profile(st.session_state.responses)
#             current_scores = current_profile.get('enhanced_pattern_scores', {})
#             show_pattern_hints(current_scores, current_question_number)
#         except:
#             pass  # Ignore errors in pattern hint generation

#     # Answer Options
#     response = render_enhanced_options(
#         current_q['options'],
#         current_q['id'],
#         question_type=current_q.get('question_type', 'single_choice'),
#         key_suffix=str(current_question_number),
#         help_text=current_q.get('help_text')
#     )

#     # Navigation Area
#     col_prev, col_next, col_skip = st.columns([1, 1, 1])

#     with col_prev:
#         if st.session_state.current_question > 0:
#             if st.button("← Previous", use_container_width=True, key="nav_prev"):
#                 st.session_state.current_question -= 1
#                 st.rerun()

#     with col_next:
#         if response:
#             if st.button("Next →", use_container_width=True, type="primary", key="nav_next"):
#                 # Save response
#                 st.session_state.responses[current_q['id']] = response
#                 st.session_state.current_question += 1
#                 st.rerun()

#     with col_skip:
#         if current_q.get('required', True) == False:
#             if st.button("Skip", use_container_width=True, key="nav_skip"):
#                 st.session_state.current_question += 1
#                 st.rerun()

#         # Navigation HTML divs removed - using clean Streamlit components now

# # Helper functions for enhanced Stripe integration
# def determine_urgency_level(pattern_scores):
#     """Determine urgency level based on pattern intensity"""
#     if not pattern_scores:
#         return "moderate"

#     high_intensity_patterns = sum(1 for score in pattern_scores.values() if isinstance(score, (int, float)) and score >= 6.5)
#     avg_intensity = sum(score for score in pattern_scores.values() if isinstance(score, (int, float))) / len([s for s in pattern_scores.values() if isinstance(s, (int, float))])

#     if high_intensity_patterns >= 2 or avg_intensity >= 6:
#         return "high"
#     elif high_intensity_patterns >= 1 or avg_intensity >= 4:
#         return "moderate"
#     else:
#         return "low"

# def calculate_enhanced_success_probability(assessment_data, responses=None):
#     """Advanced success prediction with multi-factor analysis"""
#     base_rate = 85  # Hypnotherapy baseline

#     # Extract pattern scores
#     pattern_scores = assessment_data.get('pattern_scores', {}) if isinstance(assessment_data, dict) else assessment_data

#     # Pattern complexity adjustment
#     active_patterns = len([p for p in pattern_scores.values() if isinstance(p, (int, float)) and p > 5])
#     complexity_adjustment = max(-15, -3 * (active_patterns - 2))

#     # Digital conditioning assessment
#     digital_adjustment = 0
#     if responses:
#         # Check for digital native indicators
#         digital_keywords = ['social media', 'online', 'digital', 'app', 'instagram', 'tiktok', 'facebook']
#         digital_responses = 0
#         total_text_responses = 0

#         for response in responses.values():
#             if isinstance(response, str):
#                 total_text_responses += 1
#                 response_lower = extract_response_text(response).lower()
#                 if any(keyword in response_lower for keyword in digital_keywords):
#                     digital_responses += 1

#         if total_text_responses > 0:
#             digital_ratio = digital_responses / total_text_responses
#             if digital_ratio > 0.3:
#                 digital_adjustment = -5  # High digital conditioning
#             elif digital_ratio > 0.15:
#                 digital_adjustment = 0   # Moderate
#             else:
#                 digital_adjustment = 3   # Low digital conditioning

#     # Readiness factors assessment
#     readiness_indicators = 0
#     if responses:
#         readiness_keywords = ['ready', 'motivated', 'committed', 'determined', 'willing']
#         resistance_keywords = ['skeptical', 'doubt', 'unsure', 'maybe', 'might try']

#         for response in responses.values():
#             if isinstance(response, str):
#                 response_lower = extract_response_text(response).lower()
#                 if any(keyword in response_lower for keyword in readiness_keywords):
#                     readiness_indicators += 1
#                 elif any(keyword in response_lower for keyword in resistance_keywords):
#                     readiness_indicators -= 1

#     readiness_adjustment = min(10, max(-10, readiness_indicators * 2))

#     # Support system assessment
#     support_adjustment = 0
#     if responses:
#         support_keywords = ['family', 'friends', 'partner', 'support', 'help', 'encourage']
#         isolation_keywords = ['alone', 'nobody', 'no one', 'isolated', 'by myself']

#         support_mentions = 0
#         isolation_mentions = 0

#         for response in responses.values():
#             if isinstance(response, str):
#                 response_lower = extract_response_text(response).lower()
#                 if any(keyword in response_lower for keyword in support_keywords):
#                     support_mentions += 1
#                 elif any(keyword in response_lower for keyword in isolation_keywords):
#                     isolation_mentions += 1

#         if support_mentions > isolation_mentions:
#             support_adjustment = 5  # Strong support
#         elif isolation_mentions > support_mentions:
#             support_adjustment = -8  # Weak support
#         # else: neutral (0 adjustment)

#     # Calculate final probability
#     final_probability = max(65, min(98, base_rate + complexity_adjustment + digital_adjustment + readiness_adjustment + support_adjustment))

#     # Determine confidence level
#     total_adjustment = abs(complexity_adjustment) + abs(digital_adjustment) + abs(readiness_adjustment) + abs(support_adjustment)
#     if total_adjustment < 10:
#         confidence_level = "HIGH"
#     elif total_adjustment < 20:
#         confidence_level = "MODERATE"
#     else:
#         confidence_level = "VARIABLE"

#     return {
#         'base_rate': base_rate,
#         'adjustments': {
#             'complexity': complexity_adjustment,
#             'digital_native': digital_adjustment,
#             'readiness': readiness_adjustment,
#             'support': support_adjustment
#         },
#         'final_rate': round(final_probability, 1),
#         'confidence_level': confidence_level,
#         'optimization_factors': identify_success_optimization_factors(pattern_scores, responses)
#     }

# def generate_pattern_deep_dive(dominant_pattern, pattern_scores, responses=None):
#     """Generate comprehensive pattern analysis with manifestations and origins"""

#     # Pattern manifestation database
#     pattern_manifestations = {
#         'unhappiness_culture': {
#             'name': 'Success Discomfort Pattern',
#             'core_belief': 'Happiness leads to disappointment',
#             'manifestations': [
#                 'Automatic worry when things go well',
#                 'Guilt or discomfort with compliments or praise',
#                 'Self-sabotage just before major achievements',
#                 'Expecting the other shoe to drop in good times'
#             ],
#             'origin_context': 'Early experiences where good things led to increased expectations, disappointment, or punishment',
#             'protective_function': 'Protects against disappointment by maintaining low expectations',
#             'hidden_costs': 'Blocks access to joy, motivation, and sustained success',
#             'transformation_potential': 'High - once permission for positivity is installed, dramatic shifts occur'
#         },
#         'power_struggles': {
#             'name': 'Authority Resistance Pattern',
#             'core_belief': 'Submission equals annihilation of self',
#             'manifestations': [
#                 'Automatic defensiveness with authority figures',
#                 'Need to be right even when it hurts relationships',
#                 'Difficulty accepting help or guidance',
#                 'Rebellious reactions to suggestions'
#             ],
#             'origin_context': 'Environments where authority felt oppressive or where submission meant loss of identity',
#             'protective_function': 'Preserves sense of autonomy and prevents perceived domination',
#             'hidden_costs': 'Isolation, missed opportunities, relationship conflict',
#             'transformation_potential': 'High - responds well to collaborative approaches'
#         },
#         'systematic_mistrust': {
#             'name': 'Trust Hesitation Pattern',
#             'core_belief': 'Others will eventually betray or harm me',
#             'manifestations': [
#                 'Default skepticism toward others\' motives',
#                 'Difficulty accepting support or kindness',
#                 'Extensive testing of relationships before trust',
#                 'Assumption of negative intent in ambiguous situations'
#             ],
#             'origin_context': 'Past betrayals or disappointments that created protective skepticism',
#             'protective_function': 'Guards against future betrayal and emotional harm',
#             'hidden_costs': 'Limits intimacy, support systems, and collaborative opportunities',
#             'transformation_potential': 'Moderate - requires careful trust-building process'
#         },
#         'doing_vs_being': {
#             'name': 'Achievement Focus Pattern',
#             'core_belief': 'Worth equals productivity and achievement only',
#             'manifestations': [
#                 'Guilt when not being productive',
#                 'Identity crisis during downtime or rest',
#                 'Value self only through external accomplishments',
#                 'Difficulty enjoying leisure without purpose'
#             ],
#             'origin_context': 'Environments where love/approval was conditional on performance',
#             'protective_function': 'Maintains sense of worth through consistent achievement',
#             'hidden_costs': 'Burnout, inability to rest, conditional self-worth',
#             'transformation_potential': 'High - inherent worth work creates profound relief'
#         },
#         'compartmentalized_authenticity': {
#             'name': 'Authenticity Masking Pattern',
#             'core_belief': 'Real self leads to rejection',
#             'manifestations': [
#                 'Different personality in different contexts',
#                 'Exhaustion from maintaining various personas',
#                 'Fear of being truly seen or known',
#                 'Confusion about true preferences and desires'
#             ],
#             'origin_context': 'Early rejection or criticism of authentic self-expression',
#             'protective_function': 'Prevents rejection by showing only acceptable aspects',
#             'hidden_costs': 'Identity confusion, relationship superficiality, inner isolation',
#             'transformation_potential': 'High - authentic self integration brings tremendous relief'
#         }
#     }

#     # Get pattern details or create generic one
#     pattern_data = pattern_manifestations.get(dominant_pattern, {
#         'name': dominant_pattern.replace('_', ' ').title(),
#         'core_belief': 'Specific limiting belief pattern detected',
#         'manifestations': ['Pattern-specific behaviors identified through assessment'],
#         'origin_context': 'Life experiences that shaped current responses',
#         'protective_function': 'Serves a protective role in your psychology',
#         'hidden_costs': 'Limits potential and wellbeing in specific ways',
#         'transformation_potential': 'Can be transformed with appropriate intervention'
#     })

#     # Get pattern score
#     pattern_score = pattern_scores.get(dominant_pattern, 0)

#     # Calculate intervention sequence
#     intervention_sequence = determine_therapeutic_order(dominant_pattern, pattern_scores)

#     return {
#         'dominant_analysis': {
#             'name': pattern_data['name'],
#             'core_belief': pattern_data['core_belief'],
#             'score': round(pattern_score, 1),
#             'manifestations': pattern_data['manifestations'],
#             'origin_context': pattern_data['origin_context'],
#             'protective_function': pattern_data['protective_function'],
#             'hidden_costs': pattern_data['hidden_costs'],
#             'transformation_potential': pattern_data['transformation_potential']
#         },
#         'pattern_interactions': analyze_pattern_reinforcement_cycles(pattern_scores),
#         'intervention_sequence': intervention_sequence
#     }

# def determine_therapeutic_order(dominant_pattern, pattern_scores):
#     """Determine optimal order for addressing multiple patterns"""

#     # Therapeutic sequencing rules
#     sequencing_rules = {
#         'systematic_mistrust': 1,  # Always address trust first
#         'power_struggles': 2,      # Address authority resistance early
#         'unhappiness_culture': 3,  # Permission work before other changes
#         'compartmentalized_authenticity': 4,  # Safety before authenticity
#         'self_sacrifice': 5,       # Boundaries after safety established
#         'doing_vs_being': 6,       # Worth work after basic safety
#         'inherited_missions': 7,    # Family work after individual clarity
#         'separation_division': 8,   # Thinking patterns after emotional safety
#         'digital_despair': 9       # Digital patterns after core work
#     }

#     # Get active patterns with scores > 4
#     active_patterns = [(pattern, score) for pattern, score in pattern_scores.items()
#                       if isinstance(score, (int, float)) and score > 4]

#     # Sort by therapeutic sequence priority, then by score
#     sorted_patterns = sorted(active_patterns,
#                            key=lambda x: (sequencing_rules.get(x[0], 10), -x[1]))

#     sequence = []
#     for i, (pattern, score) in enumerate(sorted_patterns[:4]):  # Limit to top 4
#         session_focus = "Session 1" if i == 0 else "Session 2" if i == 1 else "Session 3" if i == 2 else "Follow-up"
#         sequence.append({
#             'pattern': pattern.replace('_', ' ').title(),
#             'score': round(score, 1),
#             'session_focus': session_focus,
#             'priority': 'PRIMARY' if i == 0 else 'SECONDARY' if i == 1 else 'TERTIARY'
#         })

#     return sequence

# def identify_success_optimization_factors(pattern_scores, responses=None):
#     """Identify specific factors that can optimize success probability"""
#     factors = []

#     # Pattern-specific optimizations
#     pattern_optimizations = {
#         'unhappiness_culture': "Gradual permission installation for positive states",
#         'power_struggles': "Collaborative language to reduce authority resistance",
#         'systematic_mistrust': "Transparent process to build therapeutic trust",
#         'separation_division': "Both/and language to expand thinking flexibility",
#         'doing_vs_being': "Inherent worth anchoring before productivity work",
#         'compartmentalized_authenticity': "Safe authenticity practice in low-risk contexts",
#         'self_sacrifice': "Self-care reframed as service to others",
#         'inherited_missions': "Honor family while claiming personal path",
#         'digital_despair': "Digital literacy integration in therapeutic language"
#     }

#     # Add pattern-specific factors
#     for pattern_name, score in pattern_scores.items():
#         if isinstance(score, (int, float)) and score > 5:
#             optimization = pattern_optimizations.get(pattern_name)
#             if optimization:
#                 factors.append(optimization)

#     # Digital native optimizations
#     if responses:
#         digital_keywords = ['social media', 'online', 'digital', 'app']
#         is_digital_native = False
#         for response in responses.values():
#             if isinstance(response, str):
#                 response_lower = extract_response_text(response).lower()
#                 if any(keyword in response_lower for keyword in digital_keywords):
#                     is_digital_native = True
#                     break

#         if is_digital_native:
#             factors.extend([
#                 "Digital literacy integration in therapeutic language",
#                 "Shortened attention spans accommodated in session structure",
#                 "Evidence-based approach to counter digital cynicism"
#             ])

#     # Default factors if none identified
#     if not factors:
#         factors.append("Standard protocol optimization with personalized approach")

#     return factors[:3]  # Limit to top 3 most relevant factors

# def calculate_success_probability(pattern_scores):
#     """Calculate success probability based on pattern complexity"""
#     if not pattern_scores:
#         return 75.0

#     # Base success rate
#     base_rate = 85.0

#     # Adjust for pattern complexity
#     severe_patterns = sum(1 for score in pattern_scores.values() if isinstance(score, (int, float)) and score >= 6)
#     moderate_patterns = sum(1 for score in pattern_scores.values() if isinstance(score, (int, float)) and 4 <= score < 6)

#     # Reduce success probability for higher complexity
#     adjustment = (severe_patterns * -5) + (moderate_patterns * -2)

#     return max(65.0, min(95.0, base_rate + adjustment))

# def get_session_estimate(complexity_level, pattern_count):
#     """Get estimated session count"""
#     if complexity_level == "High":
#         return max(3, min(5, pattern_count))
#     elif complexity_level == "Moderate":
#         return max(2, min(4, pattern_count - 1))
#     else:
#         return max(1, min(3, pattern_count - 1))

# def get_timeline_estimate(complexity_level):
#     """Get timeline estimate based on complexity"""
#     if complexity_level == "High":
#         return "4-6 weeks"
#     elif complexity_level == "Moderate":
#         return "3-4 weeks"
#     else:
#         return "2-3 weeks"

# def get_personalized_approach(pattern_scores):
#     """Get personalized therapeutic approach"""
#     if not pattern_scores:
#         return "integrated_hypnotherapy"

#     dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1] if isinstance(x[1], (int, float)) else 0)[0]

#     if 'anxiety' in dominant_pattern or 'worry' in dominant_pattern:
#         return "anxiety_focused_hypnotherapy"
#     elif 'relationship' in dominant_pattern or 'attachment' in dominant_pattern:
#         return "relationship_pattern_therapy"
#     elif 'perfectionism' in dominant_pattern or 'control' in dominant_pattern:
#         return "cognitive_behavioral_hypnotherapy"
#     else:
#         return "integrated_hypnotherapy"

# def calculate_weekly_impact(pattern_scores):
#     """Calculate weekly time impact in hours"""
#     if not pattern_scores:
#         return 8.0

#     base_impact = 6.0
#     avg_score = sum(score for score in pattern_scores.values() if isinstance(score, (int, float))) / len([s for s in pattern_scores.values() if isinstance(s, (int, float))])

#     return base_impact + (avg_score * 1.2)

# def calculate_five_year_cost(pattern_scores):
#     """Calculate 5-year financial impact"""
#     if not pattern_scores:
#         return 35000

#     weekly_hours = calculate_weekly_impact(pattern_scores)
#     hourly_value = 400  # THB per hour opportunity cost
#     annual_impact = weekly_hours * 52 * hourly_value

#     return int(annual_impact * 5 * 0.7)  # 5 years with diminishing effect

# def calculate_roi_multiple(investment, pattern_scores):
#     """Calculate ROI multiple"""
#     five_year_cost = calculate_five_year_cost(pattern_scores)
#     return int(five_year_cost / investment) if investment > 0 else 20

# def determine_therapeutic_focus(pattern_scores):
#     """Determine primary therapeutic focus area"""
#     if not pattern_scores:
#         return "general_patterns"

#     dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1] if isinstance(x[1], (int, float)) else 0)[0]

#     focus_mapping = {
#         'anxiety': 'anxiety_management',
#         'depression': 'mood_regulation',
#         'relationship': 'interpersonal_patterns',
#         'perfectionism': 'cognitive_restructuring',
#         'trauma': 'trauma_processing',
#         'self_esteem': 'self_worth_building',
#         'control': 'control_release',
#         'procrastination': 'motivation_enhancement'
#     }

#     for key, focus in focus_mapping.items():
#         if key in dominant_pattern:
#             return focus

#     return "integrated_approach"

# def calculate_intervention_urgency(pattern_scores):
#     """Calculate intervention urgency score"""
#     if not pattern_scores:
#         return "moderate"

#     severe_count = sum(1 for score in pattern_scores.values() if isinstance(score, (int, float)) and score >= 7)
#     moderate_count = sum(1 for score in pattern_scores.values() if isinstance(score, (int, float)) and 5 <= score < 7)

#     if severe_count >= 2:
#         return "urgent"
#     elif severe_count >= 1 or moderate_count >= 3:
#         return "high"
#     elif moderate_count >= 1:
#         return "moderate"
#     else:
#         return "routine"

# class create_assess_page:
#     """Compatibility wrapper for app.py integration"""

#     def render(self):
#         """Render the assessment page"""
#         main()

# if __name__ == "__main__":
#     main()


















"""
Enhanced Clinical Behavioral Pattern Assessment
Mobile-optimized with clean design, comprehensive analytics integration
"""

import streamlit as st
from datetime import datetime
import re
from typing import Dict, Any, Optional

# ============================================================================
# COMPONENT IMPORTS
# ============================================================================
try:
    from utils.config_assess import (
        AssessmentConfig, 
        AnalyticsEngine,
        QuestionRouter,
        COMPREHENSIVE_QUESTIONS
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
# DESIGN SYSTEM
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
            self.questions = COMPREHENSIVE_QUESTIONS
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
            'premium_access': False
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
    
    def _render_header(self):
        """Render clean header"""
        # st.markdown("""
        # <div style="text-align: center; margin-bottom: 1.5rem;">
        #     <h1>Behavioral pattern assessment</h1>

        # </div>
        # """, unsafe_allow_html=True)
        st.markdown("**BEHAVIORAL ASSESSMENT**")
        st.markdown("  ")
        # st.info("This assessment identifies your specific behavioral patterns "
        #         "to create a personalized hypnotherapy protocol that targets your exact needs.")
    
    def _render_assessment(self):
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
        
        # # Question text
        # st.markdown(f"### {question['text']}")
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
                if st.button(option, key=f"q_{qid}_opt_{i}", use_container_width=True, type=button_type):
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
            
            if st.button("Continue", key=f"continue_{qid}", type="primary", use_container_width=True):
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
            
            if response.strip() and len(response.strip()) >= min_chars:
                if st.button("Continue", key=f"continue_{qid}", type="primary", use_container_width=True):
                    self._save_response(qid, response.strip())
                    self._advance_question()
                    st.rerun()
            elif response.strip():
                st.caption(f"Please provide at least {min_chars} characters")
    
    def _render_navigation(self, current_index: int):
        """Render navigation buttons"""
        # Get current question from index to access question['id']
        question = self.questions[current_index]
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_index > 0:
                if st.button("← Back", key="nav_back", use_container_width=True):
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
            if st.button("Skip", key="nav_skip", use_container_width=True):
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
        
    def _complete_assessment(self):
        """Complete assessment and generate analysis - FIXED with validation"""
        
        # FIXED: Validate we have responses
        if not st.session_state.assessment_responses:
            st.error("No responses found. Please complete at least one question.")
            return
        
        st.session_state.assessment_completed = True
        
        # Generate complete analysis with error handling
        assessment_data = {
            'responses': st.session_state.assessment_responses,
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            if self.analytics:
                analysis = self.analytics.generate_complete_analysis(assessment_data)
                st.session_state.assessment_results = analysis
                st.session_state.is_digital_native = analysis.get('is_digital_native', False)
            else:
                # Fallback if analytics not available
                st.session_state.assessment_results = {
                    'pattern_scores': {},
                    'pattern_analysis': {},
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
            
            st.session_state.assessment_results = {
                'error': str(e),
                'pattern_scores': {},
                'pattern_analysis': {
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
            
            submitted = st.form_submit_button("Get my analysis", type="primary", use_container_width=True)
            
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
    
    def _render_results(self):
        """Render results page with strategic free preview and premium content"""
        
        # Get results data
        results = st.session_state.assessment_results
        pattern_analysis = results.get('pattern_analysis', {})
        success_prediction = results.get('success_prediction', {})
        digital_analysis = results.get('digital_analysis', {})
        
        dominant = pattern_analysis.get('dominant_pattern', {})
        primary_patterns = pattern_analysis.get('primary_patterns', [])
        pattern_count = pattern_analysis.get('pattern_count', 0)
        
        # Calculate completion rate
        total_questions = len(self.questions)
        answered = sum(1 for resp in st.session_state.assessment_responses.values() 
                    if resp != "Not applicable")
        completion_rate = (answered / total_questions) * 100 if total_questions > 0 else 0
        
        # ====================================================================
        # FREE PREVIEW SECTION
        # ====================================================================
        
        # Hero Section
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
                    padding: 2rem; border-radius: 12px; border-left: 4px solid #4CA1A3; margin-bottom: 2rem;">
            <h2 style="color: #273548; margin: 0;">Assessment complete - {answered} questions analyzed</h2>
        </div>
        """, unsafe_allow_html=True)

        # Success Metrics Display (positioned right after hero section)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Questions answered", answered)

        with col2:
            if completion_rate >= 85:
                success_rate = success_prediction.get('overall_success_rate', 85)
                st.metric("Success probability", f"{success_rate}%")
            else:
                st.metric("Completion rate", f"{completion_rate:.0f}%")

        with col3:
            if completion_rate >= 85:
                timeline = success_prediction.get('timeline_estimate', '2 weeks')
                st.metric("Timeline estimate", timeline)
            else:
                st.metric("Status", "Manual review")
        
        # FIXED: Check completion rate
        if completion_rate < 85:
            st.warning(f"""
            **Assessment completion: {completion_rate:.0f}%**
            
            You've answered {answered} out of {total_questions} questions. For accurate pattern analysis, 
            we recommend completing at least 85% of the assessment.
            """)
            
            st.markdown("""
            ### Primary pattern: not applicable
            
            **Insufficient data for automated analysis**
            
            With the current completion rate, our automated pattern analysis cannot provide 
            reliable results. However, your responses have been sent to our clinical team.
            
            **What happens next:**
            
            Our licensed therapist will personally review your responses and contact you within 
            24-48 hours to discuss:
            - A personalized assessment approach
            - Your specific concerns and goals
            - The most appropriate intervention strategy for your situation
            
            For faster service, you may also email us directly at [contact email] with any
            additional context about your situation.
            """)

        else:
            # ORIGINAL: Full pattern analysis display
            # Primary Pattern Overview (Surface Level Only)
            if dominant:
                pattern_name = dominant.get('name', 'Unknown')
                pattern_score = dominant.get('score', 0)
                pattern_severity = dominant.get('severity', 'Unknown')

                # Build markdown with additional patterns inline
                pattern_text = f"""
                ### Primary pattern identified: {pattern_name}

                **Intensity:** {pattern_score:.1f}/10 - {pattern_severity.lower()} impact on daily life
                **Success probability:** {success_prediction.get('overall_success_rate', 85)}% with specialized intervention
                """

                # Add additional patterns right after success probability
                if primary_patterns:
                    pattern_text += "\n**Additional patterns detected:**\n"
                    for pattern in primary_patterns[:2]:  # Show top 2 only
                        pattern_text += f"- {pattern.get('name', 'Unknown')} ({pattern.get('score', 0):.1f}/10)\n"
                    pattern_text += "\n"

                pattern_text += f"""
                Your assessment reveals {pattern_count} interconnected behavioral patterns that developed as
                protective mechanisms but now limit your life satisfaction.
                """

                st.markdown(pattern_text)
            
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
            
            st.markdown("---")

            # Single concise CTA
            st.markdown("""
            ### 📋 Want your complete analysis?

            Your surface-level results are shown above. Unlock your detailed 15-20 page transformation blueprint below.
            """)
            
            # Paywall Integration
            if PAYWALL_AVAILABLE:
                with st.expander("**🔓 Unlock complete analysis - 1,000 THB**", expanded=False):
                    self._render_paywall_or_premium_content()
            else:
                st.info("Complete analysis will be provided during your consultation session")
        
        # ====================================================================
        # NEXT STEPS (Always Visible)
        # ====================================================================
        
        self._render_next_steps()
    
    def _render_paywall_or_premium_content(self):
        """Render paywall or premium content if unlocked"""
        
        paywall = create_clinical_paywall()
        
        if paywall.check_payment_status() or st.session_state.premium_access:
            # User has paid - show premium content
            st.success("Premium analysis unlocked")
            self._render_premium_content()
        else:
            # Show paywall
            st.markdown("""
            ### Your complete transformation blueprint
            
            **Included in your 1,000 THB purchase:**
            
            ✅ **Complete pattern analysis** - All 9 patterns with origins and interconnections  
            ✅ **Behavioral chain mapping** - Your exact 8-step trigger sequence with intervention points  
            ✅ **Transformation roadmap** - Session-by-session breakdown customized to your patterns  
            ✅ **Intervention protocols** - Exact therapeutic language and hypnotic keywords  
            ✅ **Cost analysis** - 5-year projection if unchanged with ROI calculation  
            ✅ **Downloadable PDF report** - Complete 15-20 page clinical document  
            """)
            
            # Paywall interface with single price
            blueprint_data = {
                'analysis': st.session_state.assessment_results,
                'responses': st.session_state.assessment_responses,
                'contact': st.session_state.get('contact_info', {})
            }
            
            paywall.render_paywall_interface(blueprint_data, price_thb=1000)
    
    def _render_premium_content(self):
        """Render full premium content after payment"""
        
        results = st.session_state.assessment_results
        
        st.markdown("## Your complete transformation blueprint")
        
        # Section 1: Complete Pattern Analysis
        st.markdown("## Your complete transformation blueprint")
        st.markdown("### 1. Complete pattern analysis")
        
        if BLUEPRINT_AVAILABLE:
            blueprint = create_behavioral_blueprint()
            
            # FIXED: Use correct keys that blueprint expects
            blueprint_data = {
                'master_analytics': results,  # ✅ Correct key
                'assessment_responses': st.session_state.assessment_responses,  # ✅ Correct key
                'contact_info': st.session_state.get('contact_info', {})  # ✅ Correct key
            }
            blueprint.render_complete_blueprint(blueprint_data)
        else:
            self._render_premium_fallback()
        
        # Section 2: Downloadable PDF
        st.markdown("### Download your report")
        
        st.markdown("""
        **Your complete clinical report includes:**
        - All pattern analysis with detailed origins
        - Complete trigger chain mapping
        - Session-by-session transformation roadmap
        - Intervention protocols and language guides
        - Cost analysis and ROI calculations
        - Progress tracking worksheets
        
        PDF generation will be available in your client portal after consultation scheduling.
        """)
    
    def _render_premium_fallback(self):
        """Fallback premium content if blueprint unavailable"""
        results = st.session_state.assessment_results
        pattern_analysis = results.get('pattern_analysis', {})
        clinical_summary = results.get('clinical_summary', {})
        trigger_chain = results.get('trigger_chain_analysis', {})
        # Dominant Pattern Details
        dominant = pattern_analysis.get('dominant_pattern', {})
        if dominant:
            pattern_desc = dominant.get('description', {})
            
            st.markdown(f"""
            **Pattern: {dominant.get('name', 'Unknown')}**
            
            **Root structure:** {pattern_desc.get('root_structure', 'Not available')}
            
            **Core belief:** {pattern_desc.get('core_belief', 'Not available')}
            
            **Protective function:** {pattern_desc.get('protective_function', 'Not available')}
            
            **Intervention focus:** {pattern_desc.get('intervention_focus', 'Not available')}
            """)
        
        # Clinical Summary
        st.markdown("### Clinical intervention summary")
        
        st.markdown(f"""
        **Session 1 focus:** {clinical_summary.get('session_1_focus', 'Pattern exploration')}
        
        **Session 2 target:** {clinical_summary.get('session_2_target', 'Core transformation')}
        
        **Change readiness:** {clinical_summary.get('change_readiness_score', '0/10')}
        
        **Intervention keywords:** {clinical_summary.get('intervention_keywords', 'Not specified')}
        
        **Avoid language:** {clinical_summary.get('avoid_language', 'Not specified')}
        """)
        
        # Trigger Chain Preview
        chain = trigger_chain.get('trigger_chain', {})
        if chain:
            st.markdown("### Your behavioral sequence")
            
            sequence_items = [
                ("Environmental trigger", chain.get('environmental_trigger')),
                ("Physical response", chain.get('physical_response')),
                ("Automatic thought", chain.get('automatic_thought')),
                ("Emotional response", chain.get('emotional_response')),
                ("Behavioral response", chain.get('behavioral_response'))
            ]
            
            for label, value in sequence_items:
                if value and value != 'Not captured':
                    st.markdown(f"**{label}:** {value}")
    
    def _render_next_steps(self):
        """Render next steps section"""

        st.markdown("### Your next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '').lower()
        success_prediction = st.session_state.assessment_results.get('success_prediction', {})
        recommended_sessions = success_prediction.get('recommended_sessions', 2)
        
        # Single consolidated timeline based on urgency
        if 'extremely urgent' in urgency or 'same day' in urgency:
            timeline_text = "**Priority case:** We'll contact you within 24 hours"
        elif 'very urgent' in urgency or '24' in urgency:
            timeline_text = "**High priority:** Contact within 24-48 hours"
        else:
            timeline_text = "**Standard review:** Contact within 48-72 hours"
        
        st.info(timeline_text)
        
        # Consolidated protocol information
        st.markdown(f"""
        **Your protocol:**
        - {recommended_sessions} sessions (90 min each) over {success_prediction.get('timeline_estimate', '2-3 weeks')}
        - Success probability: {success_prediction.get('overall_success_rate', 85)}%
        - Licensed therapist will review your assessment and contact you to schedule
        """)

        # CTAs
        st.markdown("### Ready to begin transformation?")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.link_button(
                "Schedule consultation",
                "https://calendly.com/laetitiasheppard/discovery",
                use_container_width=True,
                type="primary"
            )
        
        with col2:
            st.link_button(
                "Learn about method",
                "https://hypnotherapy.streamlit.app/",
                use_container_width=True
            )
        
        # Value reminder
        st.markdown("""
        ---
        **Investment comparison:**
        
        Traditional therapy: 18+ months, 15,000-25,000  
        Specialized hypnotherapy: 2-3 sessions, 3,000-4,000
        
        Time to initial results: 48-72 hours vs 3-6 months
        """)


# ============================================================================
# PAGE CLASS
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
