# """
# Enhanced Behavioral Pattern Assessment - FIXED Mobile-Optimized UX
# Improved spacing, alignment, and email integration
# """
# import streamlit as st
# from datetime import datetime
# import re

# try:
#     from components.paywall import create_clinical_paywall
#     PAYWALL_AVAILABLE = True
# except ImportError:
#     PAYWALL_AVAILABLE = False
#     print("Paywall component not available")

# class AdaptiveBehavioralAssessment:
#     """FIXED Mobile-optimized behavioral pattern assessment with improved UX"""
    
#     def __init__(self):
#         self._init_session_state()
        
#         # Pattern definitions
#         self.patterns = {
#             1: "Unhappiness culture",
#             2: "Power struggles", 
#             3: "Systematic mistrust",
#             4: "Separation and division",
#             5: "Doing versus being",
#             6: "Compartmentalized authenticity",
#             7: "Self sacrifice and care avoidance",
#             8: "Inherited missions",
#             9: "Context dependent weakness"
#         }
        
#         # Core questions (everyone gets these)
#         self.core_questions = self._get_core_questions()
        
#         # Adaptive question pools
#         self.adaptive_pools = self._get_adaptive_question_pools()
        
#         # Risk assessment questions
#         self.safety_questions = self._get_safety_questions()
        
#     def _init_session_state(self):
#         """Initialize session state variables"""
#         if 'assessment_responses' not in st.session_state:
#             st.session_state.assessment_responses = {}
#         if 'current_question' not in st.session_state:
#             st.session_state.current_question = 1
#         if 'question_sequence' not in st.session_state:
#             st.session_state.question_sequence = []
#         if 'adaptive_triggered' not in st.session_state:
#             st.session_state.adaptive_triggered = []
#         if 'assessment_completed' not in st.session_state:
#             st.session_state.assessment_completed = False
#         if 'contact_provided' not in st.session_state:
#             st.session_state.contact_provided = False
#         if 'assessment_results' not in st.session_state:
#             st.session_state.assessment_results = {}
#         if 'pattern_scores' not in st.session_state:
#             st.session_state.pattern_scores = {}
#         if 'risk_flags' not in st.session_state:
#             st.session_state.risk_flags = []

#     def _get_core_questions(self):
#         """Core 25 questions with compact, mobile-friendly options"""
#         return {
#             1: {
#                 "text": "When something genuinely wonderful happens to you, your first thought is usually:",
#                 "type": "single_choice",
#                 "options": [
#                     "I feel genuinely happy and want to celebrate",
#                     "This won't last or something bad will balance it", 
#                     "I don't really deserve this good thing",
#                     "I should downplay it so others don't feel bad",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 1, 1, 1, None],
#                 "weights": [0, 3, 3, 2, 0],
#                 "adaptive_triggers": ["unhappiness_deep"]
#             },
            
#             2: {
#                 "text": "In disagreements, your body typically:",
#                 "type": "single_choice", 
#                 "options": [
#                     "Stays calm while I listen to understand",
#                     "Tenses up immediately, ready to defend",
#                     "Goes numb and I want to escape",
#                     "Gets hot with racing heart",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 2, 3, 2, None],
#                 "weights": [0, 3, 2, 3, 0],
#                 "adaptive_triggers": ["conflict_trauma"]
#             },

#             3: {
#                 "text": "Your default assumption about new people's intentions:",
#                 "type": "single_choice",
#                 "options": [
#                     "Most people are generally well-meaning",
#                     "They're probably judging me somehow",
#                     "They want something or will try to use me",
#                     "They'll reject me once they see my flaws",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 3, 3, 3, None],
#                 "weights": [0, 2, 3, 2, 0],
#                 "adaptive_triggers": ["trust_trauma"]
#             },

#             4: {
#                 "text": "When facing important life choices, you typically:",
#                 "type": "single_choice",
#                 "options": [
#                     "Look for creative solutions honoring multiple values",
#                     "Feel trapped between impossible either-or options", 
#                     "See only two extreme alternatives",
#                     "Get paralyzed by black and white thinking",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 4, 4, 4, None],
#                 "weights": [0, 2, 3, 3, 0],
#                 "adaptive_triggers": ["binary_thinking"]
#             },

#             5: {
#                 "text": "Complete this: 'I feel valuable when I...'",
#                 "type": "single_choice",
#                 "options": [
#                     "Simply exist as I am",
#                     "Accomplish something important",
#                     "Help or please other people", 
#                     "Prove my worth through performance",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 5, 7, 5, None],
#                 "weights": [0, 2, 2, 3, 0],
#                 "adaptive_triggers": ["performance_anxiety"]
#             },

#             6: {
#                 "text": "Your personality changes significantly based on:",
#                 "type": "single_choice",
#                 "options": [
#                     "It stays consistent across all contexts",
#                     "Which group of people I'm with",
#                     "Professional versus personal settings",
#                     "Whether I'm in control or following",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 6, 6, 6, None],
#                 "weights": [0, 2, 2, 3, 0],
#                 "adaptive_triggers": ["identity_fragmentation"]
#             },

#             7: {
#                 "text": "When it comes to your own health and wellbeing:",
#                 "type": "single_choice",
#                 "options": [
#                     "I naturally prioritize alongside others'",
#                     "I know what to do but can't make myself",
#                     "I care for everyone else first, no energy left",
#                     "I feel selfish focusing on my own needs",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 7, 7, 7, None],
#                 "weights": [0, 2, 3, 3, 0],
#                 "adaptive_triggers": ["self_neglect"]
#             },

#             8: {
#                 "text": "Your major life goals are primarily:",
#                 "type": "single_choice",
#                 "options": [
#                     "Genuinely what I desire for my own life",
#                     "What my family expected or dreamed for me",
#                     "Honoring someone who died or sacrificed",
#                     "Proving I'm worthy of someone's love",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 8, 8, 8, None],
#                 "weights": [0, 2, 3, 3, 0],
#                 "adaptive_triggers": ["family_loyalty"]
#             },

#             9: {
#                 "text": "With certain people or situations, you:",
#                 "type": "single_choice",
#                 "options": [
#                     "Stay true to my values and boundaries",
#                     "Become someone I don't respect",
#                     "Lose all my usual boundaries",
#                     "Can't say no even when I want to",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 9, 9, 9, None],
#                 "weights": [0, 2, 3, 3, 0],
#                 "adaptive_triggers": ["boundary_collapse"]
#             },

#             10: {
#                 "text": "When you enter a room of strangers:",
#                 "type": "single_choice",
#                 "options": [
#                     "These seem like interesting people to meet",
#                     "They're probably thinking something critical",
#                     "I don't belong here",
#                     "I need to figure out dynamics quickly",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 3, 4, 3, None],
#                 "weights": [0, 2, 2, 2, 0],
#                 "adaptive_triggers": ["social_anxiety"]
#             },

#             11: {
#                 "text": "During disagreements, you're most likely to:",
#                 "type": "single_choice",
#                 "options": [
#                     "Listen to understand their perspective",
#                     "Attack their position aggressively",
#                     "Withdraw and shut down emotionally",
#                     "Submit but feel resentful internally",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 2, 2, 2, None],
#                 "weights": [0, 3, 2, 2, 0],
#                 "adaptive_triggers": ["conflict_trauma"]
#             },

#             12: {
#                 "text": "Complete: 'In life, I have to choose between security _____ freedom'",
#                 "type": "single_choice",
#                 "options": [
#                     "AND (I can have both)",
#                     "OR (I must choose one)",
#                     "This doesn't resonate with me",
#                     "Both seem impossible to achieve",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 4, None, 4, None],
#                 "weights": [0, 3, 0, 2, 0],
#                 "adaptive_triggers": ["binary_thinking"]
#             },

#             13: {
#                 "text": "Different life areas where you feel capable vs powerless:",
#                 "type": "single_choice",
#                 "options": [
#                     "I feel consistently myself everywhere",
#                     "I'm like two completely different people",
#                     "Strong professionally but weak personally",
#                     "Confident socially but insecure privately",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 6, 6, 6, None],
#                 "weights": [0, 3, 2, 2, 0],
#                 "adaptive_triggers": ["compartmentalization"]
#             },

#             14: {
#                 "text": "You consistently have energy and motivation for:",
#                 "type": "single_choice",
#                 "options": [
#                     "Both personal and external responsibilities",
#                     "Other people's goals but not my own",
#                     "Work projects but not personal care",
#                     "Helping others but not helping myself",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 7, 7, 7, None],
#                 "weights": [0, 2, 2, 3, 0],
#                 "adaptive_triggers": ["energy_imbalance"]
#             },

#             15: {
#                 "text": "When thinking about what YOU actually want:",
#                 "type": "single_choice",
#                 "options": [
#                     "I can access it clearly and confidently",
#                     "I honestly don't know anymore",
#                     "I feel guilty for wanting something different",
#                     "I'd be betraying someone important",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 8, 8, 8, None],
#                 "weights": [0, 2, 2, 3, 0],
#                 "adaptive_triggers": ["authentic_self"]
#             },

#             16: {
#                 "text": "Growing up, which phrase did you hear most?",
#                 "type": "single_choice",
#                 "options": [
#                     "You can achieve anything you set mind to",
#                     "Life is tough, get used to it",
#                     "Don't get your hopes up",
#                     "We're not here to have fun",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 1, 1, 1, None],
#                 "weights": [0, 2, 3, 2, 0],
#                 "adaptive_triggers": ["family_messages"]
#             },

#             17: {
#                 "text": "What scares you most about solving your main problem?",
#                 "type": "single_choice",
#                 "options": [
#                     "Nothing really scares me about solving it",
#                     "I wouldn't know who I am anymore",
#                     "People might expect too much from me",
#                     "I'd lose connections with similar strugglers",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 8, 5, 4, None],
#                 "weights": [0, 2, 2, 2, 0],
#                 "adaptive_triggers": ["change_resistance"]
#             },

#             18: {
#                 "text": "Complete: 'People like me don't get to have...'",
#                 "type": "text_completion",
#                 "placeholder": "Complete with what first comes to mind...",
#                 "patterns": "limiting_belief",
#                 "adaptive_triggers": ["core_belief"]
#             },

#             19: {
#                 "text": "When someone offers genuine help or kindness:",
#                 "type": "single_choice",
#                 "options": [
#                     "I can receive it gracefully",
#                     "I wonder what they want in return",
#                     "I feel uncomfortable, try to reciprocate",
#                     "I assume they pity me or see weakness",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 3, 3, 3, None],
#                 "weights": [0, 2, 2, 2, 0],
#                 "adaptive_triggers": ["trust_issues"]
#             },

#             20: {
#                 "text": "With social pressure to do something you don't want:",
#                 "type": "single_choice",
#                 "options": [
#                     "I say no clearly and maintain boundaries",
#                     "I go along to avoid conflict or rejection",
#                     "I feel paralyzed and unable to speak up",
#                     "I do it but feel resentful afterward",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 9, 9, 9, None],
#                 "weights": [0, 2, 2, 3, 0],
#                 "adaptive_triggers": ["boundary_issues"]
#             },

#             21: {
#                 "text": "Your current life path feels:",
#                 "type": "single_choice",
#                 "options": [
#                     "Like it genuinely reflects who I am",
#                     "Like fulfilling someone else's dreams",
#                     "Like honoring a debt I owe",
#                     "Like the 'right' thing but not authentic",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 8, 8, 8, None],
#                 "weights": [0, 2, 3, 2, 0],
#                 "adaptive_triggers": ["authenticity_gap"]
#             },

#             22: {
#                 "text": "When achieving something important, you often:",
#                 "type": "single_choice",
#                 "options": [
#                     "Feel excited and push through completion",
#                     "Find ways to sabotage or delay it",
#                     "Become overwhelmed and want to quit",
#                     "Focus on everything that could go wrong",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 1, 1, 1, None],
#                 "weights": [0, 3, 2, 2, 0],
#                 "adaptive_triggers": ["success_sabotage"]
#             },

#             23: {
#                 "text": "Specific people around whom you make regrettable choices:",
#                 "type": "single_choice",
#                 "options": [
#                     "I make similar choices regardless of who's around",
#                     "Yes, I know who but can't seem to stop",
#                     "I become weak-willed around certain types",
#                     "I desperately want their approval",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 9, 9, 9, None],
#                 "weights": [0, 2, 3, 3, 0],
#                 "adaptive_triggers": ["context_weakness"]
#             },

#             24: {
#                 "text": "When efforts go unnoticed or unappreciated:",
#                 "type": "single_choice",
#                 "options": [
#                     "My worth isn't dependent on external recognition",
#                     "I feel invisible and unimportant",
#                     "I work even harder to get attention",
#                     "I question whether what I did mattered",
#                     "Not applicable"
#                 ],
#                 "patterns": [None, 5, 5, 5, None],
#                 "weights": [0, 2, 2, 2, 0],
#                 "adaptive_triggers": ["recognition_needs"]
#             },

#             25: {
#                 "text": "How urgently do you need to resolve your main concern?",
#                 "type": "single_choice",
#                 "options": [
#                     "Extremely urgent - affecting daily life significantly",
#                     "Very urgent - need change within few months",
#                     "Moderately urgent - within 6 months",
#                     "Somewhat urgent - exploring gradual options",
#                     "Not urgent - just curious"
#                 ],
#                 "patterns": "readiness",
#                 "weights": [5, 4, 3, 2, 1],
#                 "adaptive_triggers": ["urgency_high"]
#             }
#         }

#     def _get_adaptive_question_pools(self):
#         """Simplified adaptive pools"""
#         return {
#             "unhappiness_deep": {
#                 26: {
#                     "text": "When good things happen to others, you typically:",
#                     "type": "single_choice",
#                     "options": [
#                         "Feel genuinely happy for them",
#                         "Wonder why good things don't happen to me",
#                         "Feel it proves I'm not worthy of good things",
#                         "Get suspicious about what will balance it",
#                         "Not applicable"
#                     ],
#                     "patterns": [None, 1, 1, 1, None],
#                     "weights": [0, 2, 3, 2, 0]
#                 }
#             },

#             "conflict_trauma": {
#                 27: {
#                     "text": "Growing up, family conflicts usually ended with:",
#                     "type": "single_choice",
#                     "options": [
#                         "Everyone talking through until resolved",
#                         "Someone angry, others going silent",
#                         "Long periods of tension and not speaking",
#                         "Someone apologizing to keep peace",
#                         "Not applicable"
#                     ],
#                     "patterns": [None, 2, 2, 7, None],
#                     "weights": [0, 3, 2, 2, 0]
#                 }
#             },

#             "family_loyalty": {
#                 28: {
#                     "text": "If you lived authentically, which relationship most threatened:",
#                     "type": "single_choice",
#                     "options": [
#                         "None - relationships would likely improve",
#                         "Parents who sacrificed for specific dreams",
#                         "Memory or legacy of someone who died",
#                         "Family with different success definitions",
#                         "Not applicable"
#                     ],
#                     "patterns": [None, 8, 8, 8, None],
#                     "weights": [0, 2, 3, 2, 0]
#                 }
#             },

#             "self_neglect": {
#                 29: {
#                     "text": "When thinking about taking time for yourself:",
#                     "type": "single_choice",
#                     "options": [
#                         "I see it as necessary and plan for it",
#                         "I feel guilty like I should be productive",
#                         "I think of people who need me more",
#                         "I feel selfish and undeserving",
#                         "Not applicable"
#                     ],
#                     "patterns": [None, 7, 7, 7, None],
#                     "weights": [0, 2, 3, 3, 0]
#                 }
#             }
#         }

#     def _get_safety_questions(self):
#         """Safety assessment questions"""
#         return {
#             "support_assessment": {
#                 30: {
#                     "text": "If you were in crisis right now, you have:",
#                     "type": "single_choice",
#                     "options": [
#                         "Multiple people I could reach out to",
#                         "One or two people I might contact",
#                         "People but wouldn't want to burden them",
#                         "No one I'd feel comfortable contacting",
#                         "Professional support available"
#                     ],
#                     "risk_assessment": True
#                 }
#             }
#         }

#     def render(self):
#         """Render with FIXED mobile-optimized UX"""
#         # Apply IMPROVED mobile styles
#         self._apply_improved_mobile_styles()
        
#         self._render_header()
        
#         if not st.session_state.contact_provided:
#             if not st.session_state.assessment_completed:
#                 self._render_current_question()
#             else:
#                 self._render_contact_form()
#         else:
#             self._render_results()

#     def _apply_improved_mobile_styles(self):
#         """Apply IMPROVED mobile-optimized CSS styles with better spacing and alignment"""
#         st.markdown("""
#         <style>
#         /* Remove default Streamlit padding */
#         .main .block-container {
#             padding-top: 1rem !important;
#             padding-bottom: 1rem !important;
#             max-width: 100% !important;
#         }
        
#         /* Responsive container */
#         @media (min-width: 768px) {
#             .main .block-container {
#                 max-width: 600px !important;
#                 margin: 0 auto;
#             }
#         }
        
#         /* IMPROVED: Style Streamlit buttons to be mobile-friendly with BETTER SPACING */
#         .stButton > button {
#             width: 100% !important;
#             margin-bottom: 0.25rem !important; /* REDUCED from 0.5rem */
#             padding: 0.6rem 1rem !important; /* REDUCED from 0.75rem */
#             text-align: left !important; /* FIXED: Left alignment */
#             background-color: #F8FAFC !important;
#             border: 1px solid #E2E8F0 !important;
#             border-radius: 6px !important;
#             color: #374151 !important;
#             font-size: 0.95rem !important;
#             transition: all 0.2s ease !important;
#             line-height: 1.3 !important; /* IMPROVED: Better line height */
#         }
        
#         .stButton > button:hover {
#             background-color: #F1F5F9 !important;
#             border-color: #4CA1A3 !important;
#             transform: translateY(-1px) !important;
#         }
        
#         .stButton > button:focus {
#             background-color: #E1F0F0 !important;
#             border-color: #4CA1A3 !important;
#             outline: none !important;
#         }
        
#         /* IMPROVED: Better grid layout for larger screens */
#         @media (min-width: 768px) {
#             .question-options {
#                 display: grid !important;
#                 grid-template-columns: 1fr 1fr !important;
#                 gap: 0.25rem !important; /* REDUCED gap */
#                 margin-bottom: 1rem !important;
#             }
#         }
        
#         /* IMPROVED: Mobile single column with minimal spacing */
#         @media (max-width: 767px) {
#             .question-options .stButton {
#                 margin-bottom: 0.15rem !important; /* MINIMAL spacing on mobile */
#             }
#         }
        
#         /* Text area styling */
#         .stTextArea textarea {
#             border: 1px solid #E2E8F0 !important;
#             border-radius: 6px !important;
#             padding: 0.75rem !important;
#             font-size: 0.95rem !important;
#         }
        
#         /* Navigation button styling */
#         .nav-buttons .stButton > button {
#             background-color: white !important;
#             border: 1px solid #D1D5DB !important;
#             color: #374151 !important;
#             text-align: center !important;
#             padding: 0.5rem 1rem !important;
#             margin-bottom: 0.25rem !important;
#         }
        
#         .nav-buttons .stButton > button:hover {
#             background-color: #F9FAFB !important;
#             border-color: #9CA3AF !important;
#         }
        
#         /* Primary button styling */
#         .stButton > button[kind="primary"] {
#             background-color: #4CA1A3 !important;
#             color: white !important;
#             border-color: #4CA1A3 !important;
#         }
        
#         .stButton > button[kind="primary"]:hover {
#             background-color: #3B7A7A !important;
#         }
        
#         /* Hide Streamlit elements */
#         header[data-testid="stHeader"] {
#             display: none !important;
#         }
        
#         .stDeployButton {
#             display: none !important;
#         }
        
#         /* Progress bar styling */
#         .progress-container {
#             display: flex;
#             align-items: center;
#             gap: 0.5rem;
#             margin-bottom: 1.5rem;
#             font-size: 0.85rem;
#             color: #556D7A;
#             padding: 0.5rem;
#             background: white;
#             border-radius: 6px;
#             border: 1px solid #E2E8F0;
#         }
        
#         .progress-bar {
#             flex: 1;
#             height: 4px;
#             background: #E2E8F0;
#             border-radius: 2px;
#             overflow: hidden;
#         }
        
#         .progress-fill {
#             height: 100%;
#             background: #4CA1A3;
#             transition: width 0.3s ease;
#         }
#         </style>
#         """, unsafe_allow_html=True)

#     def _render_header(self):
#         """Render compact header"""
#         st.markdown("""
#         <div style="text-align: center; margin-bottom: 1.5rem;">
#             <h1 style="font-size: 1.8rem; margin-bottom: 0.5rem; color: #273548;">
#                 Behavioral pattern assessment
#             </h1>
#             <p style="color: #556D7A; font-size: 1rem; margin: 0;">
#                 Personalized analysis for transformation planning
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

#     def _render_current_question(self):
#         """Render current question with IMPROVED mobile layout"""
#         current_q_id = self._get_current_question_id()
        
#         if current_q_id is None:
#             st.session_state.assessment_completed = True
#             self._calculate_final_results()
#             st.rerun()
#             return

#         question = self._get_question_by_id(current_q_id)
#         if not question:
#             st.error("Question not found")
#             return

#         # Calculate progress
#         total_questions = self._estimate_total_questions()
#         completed = len(st.session_state.assessment_responses)
#         progress = completed / total_questions if total_questions > 0 else 0

#         # COMPACT progress bar
#         st.markdown(f"""
#         <div class="progress-container">
#             <span><strong>Q {completed + 1}/{total_questions}</strong></span>
#             <div class="progress-bar">
#                 <div class="progress-fill" style="width: {progress * 100}%"></div>
#             </div>
#             <span><strong>{int(progress * 100)}%</strong></span>
#         </div>
#         """, unsafe_allow_html=True)

#         # Question text - larger and clear
#         st.markdown(f"""
#         <div style="margin-bottom: 1.5rem;">
#             <h3 style="color: #273548; font-size: 1.2rem; line-height: 1.4; margin-bottom: 1rem;">
#                 {question["text"]}
#             </h3>
#         </div>
#         """, unsafe_allow_html=True)

#         # Handle different question types
#         if question['type'] == 'single_choice':
#             self._render_single_choice_improved(current_q_id, question)
#         elif question['type'] == 'text_completion':
#             self._render_text_completion(current_q_id, question)

#         # Navigation
#         self._render_navigation(current_q_id)

#     def _render_single_choice_improved(self, q_id, question):
#         """Render single choice with IMPROVED spacing and alignment"""
#         options = question['options']
        
#         # Use container div for better control
#         st.markdown('<div class="question-options">', unsafe_allow_html=True)
        
#         for i, option in enumerate(options):
#             if st.button(
#                 option, 
#                 key=f"q_{q_id}_opt_{i}",
#                 use_container_width=True
#             ):
#                 self._save_response(q_id, option, question)
#                 self._advance_question()
#                 st.rerun()
        
#         st.markdown('</div>', unsafe_allow_html=True)

#     def _render_text_completion(self, q_id, question):
#         """Render text completion"""
#         response = st.text_area(
#             "",
#             placeholder=question.get('placeholder', 'Your response...'),
#             key=f"q_{q_id}_text",
#             height=80,
#             label_visibility="collapsed"
#         )
        
#         # Continue button
#         if response.strip():
#             if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                 self._save_response(q_id, response.strip(), question)
#                 self._advance_question()
#                 st.rerun()
#         else:
#             st.info("Please provide your response to continue.")

#     def _render_navigation(self, current_q_id):
#         """Render navigation"""
#         # Navigation buttons in columns
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col1:
#             if len(st.session_state.assessment_responses) > 0:
#                 st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
#                 if st.button("← Back", key="nav_back", use_container_width=True):
#                     self._go_back()
#                     st.rerun()
#                 st.markdown('</div>', unsafe_allow_html=True)
        
#         with col2:
#             # Progress info
#             answered_count = len(st.session_state.assessment_responses)
#             st.markdown(f"""
#             <div style="text-align: center; padding: 0.5rem; color: #556D7A; font-size: 0.9rem;">
#                 <strong>{answered_count}</strong> answered
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
#             if st.button("Skip", key="nav_skip", use_container_width=True, help="If not applicable"):
#                 self._save_response(current_q_id, "Not applicable", {"patterns": None, "weights": [0]})
#                 self._advance_question()
#                 st.rerun()
#             st.markdown('</div>', unsafe_allow_html=True)

#     def _get_current_question_id(self):
#         """Get the ID of the current question to display"""
#         answered_questions = set(st.session_state.assessment_responses.keys())
        
#         # Check core questions first
#         for q_id in range(1, 26):
#             if q_id not in answered_questions:
#                 return q_id
        
#         # Check adaptive questions
#         for pool_name in st.session_state.adaptive_triggered:
#             if pool_name in self.adaptive_pools:
#                 for q_id in self.adaptive_pools[pool_name]:
#                     if q_id not in answered_questions:
#                         return q_id
        
#         # Check safety questions if risk flags triggered
#         if st.session_state.risk_flags:
#             for pool_name in ["support_assessment"]:
#                 if pool_name in self.safety_questions:
#                     for q_id in self.safety_questions[pool_name]:
#                         if q_id not in answered_questions:
#                             return q_id
        
#         return None  # Assessment complete

#     def _get_question_by_id(self, q_id):
#         """Get question data by ID from any pool"""
#         # Check core questions
#         if q_id in self.core_questions:
#             return self.core_questions[q_id]
        
#         # Check adaptive pools
#         for pool in self.adaptive_pools.values():
#             if q_id in pool:
#                 return pool[q_id]
        
#         # Check safety questions
#         for pool in self.safety_questions.values():
#             if q_id in pool:
#                 return pool[q_id]
        
#         return None

#     def _save_response(self, q_id, response, question):
#         """Save response and trigger adaptive logic"""
#         # Save response
#         st.session_state.assessment_responses[q_id] = {
#             'response': response,
#             'question_text': question['text'],
#             'question_type': question['type'],
#             'timestamp': datetime.now().isoformat()
#         }
        
#         # Update pattern scores
#         self._update_pattern_scores(q_id, response, question)
        
#         # Check for adaptive triggers
#         self._check_adaptive_triggers(q_id, response, question)
        
#         # Check for risk flags
#         self._check_risk_flags(q_id, response, question)

#     def _update_pattern_scores(self, q_id, response, question):
#         """Update pattern scores based on response"""
#         if 'patterns' not in question or question['patterns'] is None:
#             return
        
#         if question['type'] == 'single_choice':
#             patterns = question.get('patterns', [])
#             weights = question.get('weights', [])
            
#             if isinstance(patterns, list) and isinstance(weights, list):
#                 # Find selected option index
#                 options = question.get('options', [])
#                 try:
#                     option_index = options.index(response)
#                     if option_index < len(patterns) and patterns[option_index] is not None:
#                         pattern_id = patterns[option_index]
#                         weight = weights[option_index] if option_index < len(weights) else 1
                        
#                         if pattern_id not in st.session_state.pattern_scores:
#                             st.session_state.pattern_scores[pattern_id] = 0
#                         st.session_state.pattern_scores[pattern_id] += weight
#                 except ValueError:
#                     pass  # Response not in options

#     def _check_adaptive_triggers(self, q_id, response, question):
#         """Check if response triggers adaptive question pools"""
#         adaptive_triggers = question.get('adaptive_triggers', [])
        
#         if question['type'] == 'single_choice':
#             options = question.get('options', [])
#             try:
#                 option_index = options.index(response)
                
#                 # Check specific option triggers
#                 for trigger in adaptive_triggers:
#                     if trigger not in st.session_state.adaptive_triggered:
#                         # Add trigger logic based on response patterns
#                         if self._should_trigger_adaptive_pool(trigger, option_index, response):
#                             st.session_state.adaptive_triggered.append(trigger)
                            
#             except ValueError:
#                 pass
#         elif question['type'] == 'text_completion':
#             # Trigger adaptive pools for text responses
#             for trigger in adaptive_triggers:
#                 if trigger not in st.session_state.adaptive_triggered:
#                     st.session_state.adaptive_triggered.append(trigger)

#     def _should_trigger_adaptive_pool(self, trigger, option_index, response):
#         """Determine if adaptive pool should be triggered"""
#         # Skip "Not applicable" responses (typically index 4)
#         if option_index >= 4:
#             return False
            
#         trigger_conditions = {
#             "unhappiness_deep": option_index in [1, 2, 3],
#             "conflict_trauma": option_index in [1, 2, 3],
#             "family_loyalty": option_index in [1, 2, 3],
#             "self_neglect": option_index in [1, 2, 3],
#             "trust_trauma": option_index in [1, 2, 3],
#             "performance_anxiety": option_index in [1, 2, 3],
#             "identity_fragmentation": option_index in [1, 2, 3],
#             "binary_thinking": option_index in [1, 2, 3],
#             "boundary_collapse": option_index in [1, 2, 3],
#             "social_anxiety": option_index in [1, 2, 3],
#             "success_sabotage": option_index in [1, 2, 3],
#             "context_weakness": option_index in [1, 2, 3],
#             "recognition_needs": option_index in [1, 2, 3],
#             "urgency_high": option_index in [0, 1],
#             "authenticity_gap": option_index in [1, 2, 3],
#             "energy_imbalance": option_index in [1, 2, 3],
#             "family_messages": option_index in [1, 2, 3],
#             "change_resistance": option_index in [1, 2, 3],
#             "trust_issues": option_index in [1, 2, 3],
#             "boundary_issues": option_index in [1, 2, 3],
#             "compartmentalization": option_index in [1, 2, 3],
#             "authentic_self": option_index in [1, 2, 3],
#             "core_belief": True  # Text completion always triggers
#         }
        
#         return trigger_conditions.get(trigger, False)

#     def _check_risk_flags(self, q_id, response, question):
#         """Check for risk indicators"""
#         if hasattr(question, 'risk_assessment') and question.get('risk_assessment'):
#             options = question.get('options', [])
#             try:
#                 option_index = options.index(response)
#                 if option_index >= 3:  # Options indicating isolation or lack of support
#                     if 'social_isolation' not in st.session_state.risk_flags:
#                         st.session_state.risk_flags.append('social_isolation')
#             except ValueError:
#                 pass

#     def _advance_question(self):
#         """Advance to next question"""
#         st.session_state.current_question += 1

#     def _go_back(self):
#         """Go back to previous question"""
#         if st.session_state.current_question > 1:
#             st.session_state.current_question -= 1
#             # Remove last response
#             if st.session_state.assessment_responses:
#                 last_key = max(st.session_state.assessment_responses.keys())
#                 del st.session_state.assessment_responses[last_key]

#     def _estimate_total_questions(self):
#         """Estimate total questions based on current triggers"""
#         base_questions = 25
#         adaptive_questions = len(st.session_state.adaptive_triggered) * 1  # 1 per pool
#         safety_questions = len(st.session_state.risk_flags) * 1
        
#         return base_questions + adaptive_questions + safety_questions

#     def _calculate_final_results(self):
#         """Calculate final assessment results"""
#         # Calculate pattern dominance
#         sorted_patterns = sorted(
#             st.session_state.pattern_scores.items(), 
#             key=lambda x: x[1], 
#             reverse=True
#         )
        
#         # Extract clinical insights
#         clinical_insights = self._extract_clinical_insights()
        
#         # Calculate readiness metrics
#         readiness_metrics = self._calculate_readiness_metrics()
        
#         # Generate resistance predictions
#         resistance_predictions = self._predict_resistance_points()
        
#         # Store comprehensive results
#         st.session_state.assessment_results = {
#             'pattern_scores': dict(st.session_state.pattern_scores),
#             'dominant_pattern': sorted_patterns[0] if sorted_patterns else (None, 0),
#             'secondary_patterns': sorted_patterns[1:3] if len(sorted_patterns) > 1 else [],
#             'clinical_insights': clinical_insights,
#             'readiness_metrics': readiness_metrics,
#             'resistance_predictions': resistance_predictions,
#             'risk_flags': st.session_state.risk_flags,
#             'adaptive_triggered': st.session_state.adaptive_triggered,
#             'completion_timestamp': datetime.now().isoformat(),
#             'total_questions_answered': len(st.session_state.assessment_responses)
#         }

#     def _extract_clinical_insights(self):
#         """Extract insights from text responses"""
#         insights = {}
        
#         for q_id, response_data in st.session_state.assessment_responses.items():
#             if response_data.get('question_type') == 'text_completion':
#                 question = self._get_question_by_id(q_id)
#                 if question and 'patterns' in question:
#                     pattern_type = question['patterns']
#                     insights[pattern_type] = response_data['response']
        
#         return insights

#     def _calculate_readiness_metrics(self):
#         """Calculate transformation readiness"""
#         readiness_score = 5  # Default
        
#         # Extract from urgency question
#         for response_data in st.session_state.assessment_responses.values():
#             response = response_data.get('response', '')
#             if 'Extremely urgent' in response:
#                 readiness_score = 10
#             elif 'Very urgent' in response:
#                 readiness_score = 8
#             elif 'Moderately urgent' in response:
#                 readiness_score = 6
#             elif 'Somewhat urgent' in response:
#                 readiness_score = 4
#             elif 'Not urgent' in response:
#                 readiness_score = 2
        
#         return {
#             'urgency_level': readiness_score,
#             'risk_level': 'High' if st.session_state.risk_flags else 'Low',
#             'complexity': 'High' if len(st.session_state.adaptive_triggered) > 3 else 'Medium'
#         }

#     def _predict_resistance_points(self):
#         """Predict resistance based on patterns"""
#         predictions = []
#         pattern_scores = st.session_state.pattern_scores
        
#         if pattern_scores.get(1, 0) > 5:
#             predictions.append("Will resist positive suggestions as 'fake' or 'temporary'")
        
#         if pattern_scores.get(3, 0) > 5:
#             predictions.append("May be skeptical of therapist intentions")
        
#         if pattern_scores.get(8, 0) > 5:
#             predictions.append("Change may feel like betraying family expectations")
        
#         return predictions[:3]

#     def _render_contact_form(self):
#         """Render contact form with mobile optimization"""
#         st.markdown("### Assessment complete")
#         st.write("Provide your details to receive your behavioral pattern analysis.")
        
#         with st.form("assessment_contact_form"):
#             # Compact form layout
#             name = st.text_input("Full name*", placeholder="Your full name")
#             email = st.text_input("Email*", placeholder="your@email.com")
#             phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
            
#             urgency = st.selectbox(
#                 "How urgent is your concern?",
#                 ["Select urgency...", "Extremely urgent", "Very urgent", "Moderately urgent", "Not urgent"]
#             )
            
#             concern = st.text_area(
#                 "Primary concern*",
#                 placeholder="What brought you to this assessment?",
#                 height=80
#             )
            
#             next_step = st.selectbox(
#                 "Preferred next step:",
#                 ["Select preference...", "Schedule discovery call", "Book transformation package", "Request analysis first"]
#             )
            
#             submitted = st.form_submit_button("Get my analysis", type="primary", use_container_width=True)
            
#             if submitted:
#                 if self._validate_contact_form(name, email, concern, urgency, next_step):
#                     self._save_contact_info(name, email, phone, urgency, concern, next_step)
#                     self._send_assessment_results()
#                     st.session_state.contact_provided = True
#                     st.rerun()

#     def _validate_contact_form(self, name, email, concern, urgency, next_step):
#         """Validate contact form with CORRECTED email regex"""
#         errors = []
        
#         if not name.strip():
#             errors.append("Name is required")
#         if not email.strip():
#             errors.append("Email is required")
#         elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#             errors.append("Valid email required")
#         if not concern.strip():
#             errors.append("Primary concern required")
#         if urgency == "Select urgency...":
#             errors.append("Please select urgency level")
#         if next_step == "Select preference...":
#             errors.append("Please select next step")
        
#         for error in errors:
#             st.error(f"❌ {error}")
        
#         return len(errors) == 0

#     def _save_contact_info(self, name, email, phone, urgency, concern, next_step):
#         """Save contact information"""
#         st.session_state.contact_info = {
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'urgency': urgency,
#             'primary_concern': concern,
#             'next_step': next_step,
#             'timestamp': datetime.now().isoformat()
#         }

#     def _send_assessment_results(self):
#         """Send assessment results via email"""
#         try:
#             from utils.enhanced_email_handler import send_assessment_results_email
            
#             # Prepare data package
#             assessment_data = {
#                 'name': st.session_state.contact_info['name'],
#                 'email': st.session_state.contact_info['email'],
#                 'phone': st.session_state.contact_info.get('phone', 'Not provided'),
#                 'urgency': st.session_state.contact_info['urgency'],
#                 'primary_concern': st.session_state.contact_info['primary_concern'],
#                 'next_step': st.session_state.contact_info['next_step'],
#                 'form_type': 'Mobile-Optimized Behavioral Assessment',
#                 'assessment_results': st.session_state.assessment_results,
#                 'raw_responses': st.session_state.assessment_responses,
#                 'clinical_template': self._generate_clinical_template(),
#                 'response_transcript': self._generate_response_transcript(),
#                 'total_questions': len(st.session_state.assessment_responses),
#                 'completion_rate': '100%',
#                 'timestamp': datetime.now().isoformat()
#             }
            
#             success = send_assessment_results_email(assessment_data)
            
#             if success:
#                 st.success("✅ Assessment results sent successfully!")
#             else:
#                 st.warning("⚠️ Assessment completed, but email notification failed.")
                
#         except Exception as e:
#             st.error(f"Error sending results: {str(e)}")

#     def _generate_clinical_template(self):
#         """Generate clinical template"""
#         results = st.session_state.assessment_results
#         contact = st.session_state.contact_info
        
#         # Get top patterns
#         pattern_scores = results.get('pattern_scores', {})
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
#         dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
#         secondary = sorted_patterns[1] if len(sorted_patterns) > 1 else (None, 0)
        
#         template = f"""
# MOBILE-OPTIMIZED BEHAVIORAL ASSESSMENT - CLINICAL TEMPLATE
# Client: {contact['name']} | Date: {datetime.now().strftime('%Y-%m-%d')}

# DOMINANT PATTERNS:
# Primary: {self.patterns.get(dominant[0], 'None')} (Score: {dominant[1]}/8)
# Secondary: {self.patterns.get(secondary[0], 'None')} (Score: {secondary[1]}/8)

# SESSION PLANNING:
# Session 1: Map {self.patterns.get(dominant[0], 'primary')} patterns
# Session 2: Rewire {self.patterns.get(dominant[0], 'primary pattern')}
# Session 3: Reinforcement if needed

# READINESS: {results.get('readiness_metrics', {}).get('urgency_level', 5)}/10
# COMPLEXITY: {results.get('readiness_metrics', {}).get('complexity', 'Medium')}
# ADAPTIVE POOLS: {len(results.get('adaptive_triggered', []))}
#         """
        
#         return template

#     def _generate_response_transcript(self):
#         """Generate response transcript"""
#         transcript = []
        
#         for q_id in sorted(st.session_state.assessment_responses.keys()):
#             response_data = st.session_state.assessment_responses[q_id]
            
#             transcript.append({
#                 'question_id': q_id,
#                 'question_text': response_data['question_text'],
#                 'response': response_data['response'],
#                 'question_type': response_data['question_type'],
#                 'timestamp': response_data['timestamp'],
#                 'clinical_relevance': f"Question {q_id} assessment data"
#             })
        
#         return transcript

#     def _render_results(self):
#         """Render assessment results"""
#         st.markdown("## Assessment analysis complete")
#         st.success("Your behavioral pattern analysis has been sent to our clinical team.")
        
#         # Basic summary
#         results = st.session_state.assessment_results
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.metric("Questions", results['total_questions_answered'], "Completed")
        
#         with col2:
#             urgency = results.get('readiness_metrics', {}).get('urgency_level', 5)
#             st.metric("Readiness", f"{urgency}/10", "Level")
        
#         with col3:
#             complexity = results.get('readiness_metrics', {}).get('complexity', 'Medium')
#             st.metric("Complexity", complexity, "Assessment")

#         # Clinical analysis with paywall
#         self._render_clinical_analysis_section()
        
#         # Next steps
#         st.markdown("### Your next steps")
        
#         contact_info = st.session_state.get('contact_info', {})
#         next_step = contact_info.get('next_step', '')
        
#         if 'discovery call' in next_step.lower():
#             st.info("We'll contact you to schedule a discovery call.")
#         elif 'package' in next_step.lower():
#             st.success("We'll contact you with scheduling options.")
#         else:
#             st.info("We'll review and contact you with recommendations.")
        
#         st.markdown("""
#         **What happens next:**
        
#         1. **Clinical review** (24 hours): Analysis for optimal approach
#         2. **Personal contact** (48 hours): Specific recommendations  
#         3. **Discovery call** (Optional): Discuss results
#         4. **Transformation sessions**: Begin your personalized program
#         """)

#     def _render_clinical_analysis_section(self):
#         """Render clinical analysis with paywall"""
#         st.markdown("### Clinical pattern analysis")
        
#         if PAYWALL_AVAILABLE:
#             try:
#                 paywall = create_clinical_paywall()
                
#                 assessment_data = {
#                     'assessment_results': st.session_state.assessment_results,
#                     'assessment_responses': st.session_state.assessment_responses,
#                 }
                
#                 contact_info = st.session_state.get('contact_info', {})
#                 assessment_data.update(contact_info)
                
#                 if paywall.check_payment_status():
#                     paywall.render_premium_analysis(assessment_data)
#                 else:
#                     self._render_analysis_preview()
#                     with st.expander("Unlock complete analysis", expanded=False):
#                         paywall.render_paywall_interface(assessment_data)
#             except Exception as e:
#                 st.error(f"Error loading analysis: {str(e)}")
#                 self._render_analysis_preview()
#         else:
#             self._render_analysis_preview()

#     def _render_analysis_preview(self):
#         """Render analysis preview"""
#         results = st.session_state.assessment_results
#         pattern_scores = results.get('pattern_scores', {})
        
#         if pattern_scores:
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
#             st.markdown("**Preview - Your dominant patterns:**")
#             for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
#                 pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
#                 st.write(f"• {pattern_name}: Pattern detected")
            
#             if len(sorted_patterns) > 2:
#                 remaining = len(sorted_patterns) - 2
#                 st.write(f"• Plus {remaining} additional patterns analyzed...")
        
#         st.info("Unlock complete analysis for detailed insights and transformation roadmap.")


# class AssessPage:
#     """FIXED Mobile-optimized assessment page"""
    
#     def __init__(self):
#         self.assessment = AdaptiveBehavioralAssessment()
    
#     def render(self):
#         """Render the assessment page"""
#         self.assessment.render()


# def create_assess_page():
#     """Factory function"""
#     return AssessPage()











"""
Enhanced Behavioral Pattern Assessment - FIXED Mobile-Optimized UX
Improved spacing, alignment, and email integration
"""
import streamlit as st
from datetime import datetime
import re

try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False
    print("Paywall component not available")

class AdaptiveBehavioralAssessment:
    """FIXED Mobile-optimized behavioral pattern assessment with improved UX"""
    
    def __init__(self):
        self._init_session_state()
        
        # Pattern definitions
        self.patterns = {
            1: "Unhappiness culture",
            2: "Power struggles", 
            3: "Systematic mistrust",
            4: "Separation and division",
            5: "Doing versus being",
            6: "Compartmentalized authenticity",
            7: "Self sacrifice and care avoidance",
            8: "Inherited missions",
            9: "Context dependent weakness"
        }
        
        # Core questions (everyone gets these)
        self.core_questions = self._get_core_questions()
        
        # Adaptive question pools
        self.adaptive_pools = self._get_adaptive_question_pools()
        
        # Risk assessment questions
        self.safety_questions = self._get_safety_questions()
        
    def _init_session_state(self):
        """Initialize session state variables"""
        if 'assessment_responses' not in st.session_state:
            st.session_state.assessment_responses = {}
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 1
        if 'question_sequence' not in st.session_state:
            st.session_state.question_sequence = []
        if 'adaptive_triggered' not in st.session_state:
            st.session_state.adaptive_triggered = []
        if 'assessment_completed' not in st.session_state:
            st.session_state.assessment_completed = False
        if 'contact_provided' not in st.session_state:
            st.session_state.contact_provided = False
        if 'assessment_results' not in st.session_state:
            st.session_state.assessment_results = {}
        if 'pattern_scores' not in st.session_state:
            st.session_state.pattern_scores = {}
        if 'risk_flags' not in st.session_state:
            st.session_state.risk_flags = []

    def _get_core_questions(self):
        """Core 25 questions with compact, mobile-friendly options"""
        return {
            1: {
                "text": "When something genuinely wonderful happens to you, your first thought is usually:",
                "type": "single_choice",
                "options": [
                    "I feel genuinely happy and want to celebrate",
                    "This won't last or something bad will balance it", 
                    "I don't really deserve this good thing",
                    "I should downplay it so others don't feel bad",
                    "Not applicable"
                ],
                "patterns": [None, 1, 1, 1, None],
                "weights": [0, 3, 3, 2, 0],
                "adaptive_triggers": ["unhappiness_deep"]
            },
            
            2: {
                "text": "In disagreements, your body typically:",
                "type": "single_choice", 
                "options": [
                    "Stays calm while I listen to understand",
                    "Tenses up immediately, ready to defend",
                    "Goes numb and I want to escape",
                    "Gets hot with racing heart",
                    "Not applicable"
                ],
                "patterns": [None, 2, 3, 2, None],
                "weights": [0, 3, 2, 3, 0],
                "adaptive_triggers": ["conflict_trauma"]
            },

            3: {
                "text": "Your default assumption about new people's intentions:",
                "type": "single_choice",
                "options": [
                    "Most people are generally well-meaning",
                    "They're probably judging me somehow",
                    "They want something or will try to use me",
                    "They'll reject me once they see my flaws",
                    "Not applicable"
                ],
                "patterns": [None, 3, 3, 3, None],
                "weights": [0, 2, 3, 2, 0],
                "adaptive_triggers": ["trust_trauma"]
            },

            4: {
                "text": "When facing important life choices, you typically:",
                "type": "single_choice",
                "options": [
                    "Look for creative solutions honoring multiple values",
                    "Feel trapped between impossible either-or options", 
                    "See only two extreme alternatives",
                    "Get paralyzed by black and white thinking",
                    "Not applicable"
                ],
                "patterns": [None, 4, 4, 4, None],
                "weights": [0, 2, 3, 3, 0],
                "adaptive_triggers": ["binary_thinking"]
            },

            5: {
                "text": "Complete this: 'I feel valuable when I...'",
                "type": "single_choice",
                "options": [
                    "Simply exist as I am",
                    "Accomplish something important",
                    "Help or please other people", 
                    "Prove my worth through performance",
                    "Not applicable"
                ],
                "patterns": [None, 5, 7, 5, None],
                "weights": [0, 2, 2, 3, 0],
                "adaptive_triggers": ["performance_anxiety"]
            },

            6: {
                "text": "Your personality changes significantly based on:",
                "type": "single_choice",
                "options": [
                    "It stays consistent across all contexts",
                    "Which group of people I'm with",
                    "Professional versus personal settings",
                    "Whether I'm in control or following",
                    "Not applicable"
                ],
                "patterns": [None, 6, 6, 6, None],
                "weights": [0, 2, 2, 3, 0],
                "adaptive_triggers": ["identity_fragmentation"]
            },

            7: {
                "text": "When it comes to your own health and wellbeing:",
                "type": "single_choice",
                "options": [
                    "I naturally prioritize alongside others'",
                    "I know what to do but can't make myself",
                    "I care for everyone else first, no energy left",
                    "I feel selfish focusing on my own needs",
                    "Not applicable"
                ],
                "patterns": [None, 7, 7, 7, None],
                "weights": [0, 2, 3, 3, 0],
                "adaptive_triggers": ["self_neglect"]
            },

            8: {
                "text": "Your major life goals are primarily:",
                "type": "single_choice",
                "options": [
                    "Genuinely what I desire for my own life",
                    "What my family expected or dreamed for me",
                    "Honoring someone who died or sacrificed",
                    "Proving I'm worthy of someone's love",
                    "Not applicable"
                ],
                "patterns": [None, 8, 8, 8, None],
                "weights": [0, 2, 3, 3, 0],
                "adaptive_triggers": ["family_loyalty"]
            },

            9: {
                "text": "With certain people or situations, you:",
                "type": "single_choice",
                "options": [
                    "Stay true to my values and boundaries",
                    "Become someone I don't respect",
                    "Lose all my usual boundaries",
                    "Can't say no even when I want to",
                    "Not applicable"
                ],
                "patterns": [None, 9, 9, 9, None],
                "weights": [0, 2, 3, 3, 0],
                "adaptive_triggers": ["boundary_collapse"]
            },

            10: {
                "text": "When you enter a room of strangers:",
                "type": "single_choice",
                "options": [
                    "These seem like interesting people to meet",
                    "They're probably thinking something critical",
                    "I don't belong here",
                    "I need to figure out dynamics quickly",
                    "Not applicable"
                ],
                "patterns": [None, 3, 4, 3, None],
                "weights": [0, 2, 2, 2, 0],
                "adaptive_triggers": ["social_anxiety"]
            },

            11: {
                "text": "During disagreements, you're most likely to:",
                "type": "single_choice",
                "options": [
                    "Listen to understand their perspective",
                    "Attack their position aggressively",
                    "Withdraw and shut down emotionally",
                    "Submit but feel resentful internally",
                    "Not applicable"
                ],
                "patterns": [None, 2, 2, 2, None],
                "weights": [0, 3, 2, 2, 0],
                "adaptive_triggers": ["conflict_trauma"]
            },

            12: {
                "text": "Complete: 'In life, I have to choose between security _____ freedom'",
                "type": "single_choice",
                "options": [
                    "AND (I can have both)",
                    "OR (I must choose one)",
                    "This doesn't resonate with me",
                    "Both seem impossible to achieve",
                    "Not applicable"
                ],
                "patterns": [None, 4, None, 4, None],
                "weights": [0, 3, 0, 2, 0],
                "adaptive_triggers": ["binary_thinking"]
            },

            13: {
                "text": "Different life areas where you feel capable vs powerless:",
                "type": "single_choice",
                "options": [
                    "I feel consistently myself everywhere",
                    "I'm like two completely different people",
                    "Strong professionally but weak personally",
                    "Confident socially but insecure privately",
                    "Not applicable"
                ],
                "patterns": [None, 6, 6, 6, None],
                "weights": [0, 3, 2, 2, 0],
                "adaptive_triggers": ["compartmentalization"]
            },

            14: {
                "text": "You consistently have energy and motivation for:",
                "type": "single_choice",
                "options": [
                    "Both personal and external responsibilities",
                    "Other people's goals but not my own",
                    "Work projects but not personal care",
                    "Helping others but not helping myself",
                    "Not applicable"
                ],
                "patterns": [None, 7, 7, 7, None],
                "weights": [0, 2, 2, 3, 0],
                "adaptive_triggers": ["energy_imbalance"]
            },

            15: {
                "text": "When thinking about what YOU actually want:",
                "type": "single_choice",
                "options": [
                    "I can access it clearly and confidently",
                    "I honestly don't know anymore",
                    "I feel guilty for wanting something different",
                    "I'd be betraying someone important",
                    "Not applicable"
                ],
                "patterns": [None, 8, 8, 8, None],
                "weights": [0, 2, 2, 3, 0],
                "adaptive_triggers": ["authentic_self"]
            },

            16: {
                "text": "Growing up, which phrase did you hear most?",
                "type": "single_choice",
                "options": [
                    "You can achieve anything you set mind to",
                    "Life is tough, get used to it",
                    "Don't get your hopes up",
                    "We're not here to have fun",
                    "Not applicable"
                ],
                "patterns": [None, 1, 1, 1, None],
                "weights": [0, 2, 3, 2, 0],
                "adaptive_triggers": ["family_messages"]
            },

            17: {
                "text": "What scares you most about solving your main problem?",
                "type": "single_choice",
                "options": [
                    "Nothing really scares me about solving it",
                    "I wouldn't know who I am anymore",
                    "People might expect too much from me",
                    "I'd lose connections with similar strugglers",
                    "Not applicable"
                ],
                "patterns": [None, 8, 5, 4, None],
                "weights": [0, 2, 2, 2, 0],
                "adaptive_triggers": ["change_resistance"]
            },

            18: {
                "text": "Complete: 'People like me don't get to have...'",
                "type": "text_completion",
                "placeholder": "Complete with what first comes to mind...",
                "patterns": "limiting_belief",
                "adaptive_triggers": ["core_belief"]
            },

            19: {
                "text": "When someone offers genuine help or kindness:",
                "type": "single_choice",
                "options": [
                    "I can receive it gracefully",
                    "I wonder what they want in return",
                    "I feel uncomfortable, try to reciprocate",
                    "I assume they pity me or see weakness",
                    "Not applicable"
                ],
                "patterns": [None, 3, 3, 3, None],
                "weights": [0, 2, 2, 2, 0],
                "adaptive_triggers": ["trust_issues"]
            },

            20: {
                "text": "With social pressure to do something you don't want:",
                "type": "single_choice",
                "options": [
                    "I say no clearly and maintain boundaries",
                    "I go along to avoid conflict or rejection",
                    "I feel paralyzed and unable to speak up",
                    "I do it but feel resentful afterward",
                    "Not applicable"
                ],
                "patterns": [None, 9, 9, 9, None],
                "weights": [0, 2, 2, 3, 0],
                "adaptive_triggers": ["boundary_issues"]
            },

            21: {
                "text": "Your current life path feels:",
                "type": "single_choice",
                "options": [
                    "Like it genuinely reflects who I am",
                    "Like fulfilling someone else's dreams",
                    "Like honoring a debt I owe",
                    "Like the 'right' thing but not authentic",
                    "Not applicable"
                ],
                "patterns": [None, 8, 8, 8, None],
                "weights": [0, 2, 3, 2, 0],
                "adaptive_triggers": ["authenticity_gap"]
            },

            22: {
                "text": "When achieving something important, you often:",
                "type": "single_choice",
                "options": [
                    "Feel excited and push through completion",
                    "Find ways to sabotage or delay it",
                    "Become overwhelmed and want to quit",
                    "Focus on everything that could go wrong",
                    "Not applicable"
                ],
                "patterns": [None, 1, 1, 1, None],
                "weights": [0, 3, 2, 2, 0],
                "adaptive_triggers": ["success_sabotage"]
            },

            23: {
                "text": "Specific people around whom you make regrettable choices:",
                "type": "single_choice",
                "options": [
                    "I make similar choices regardless of who's around",
                    "Yes, I know who but can't seem to stop",
                    "I become weak-willed around certain types",
                    "I desperately want their approval",
                    "Not applicable"
                ],
                "patterns": [None, 9, 9, 9, None],
                "weights": [0, 2, 3, 3, 0],
                "adaptive_triggers": ["context_weakness"]
            },

            24: {
                "text": "When efforts go unnoticed or unappreciated:",
                "type": "single_choice",
                "options": [
                    "My worth isn't dependent on external recognition",
                    "I feel invisible and unimportant",
                    "I work even harder to get attention",
                    "I question whether what I did mattered",
                    "Not applicable"
                ],
                "patterns": [None, 5, 5, 5, None],
                "weights": [0, 2, 2, 2, 0],
                "adaptive_triggers": ["recognition_needs"]
            },

            25: {
                "text": "How urgently do you need to resolve your main concern?",
                "type": "single_choice",
                "options": [
                    "Extremely urgent - affecting daily life significantly",
                    "Very urgent - need change within few months",
                    "Moderately urgent - within 6 months",
                    "Somewhat urgent - exploring gradual options",
                    "Not urgent - just curious"
                ],
                "patterns": "readiness",
                "weights": [5, 4, 3, 2, 1],
                "adaptive_triggers": ["urgency_high"]
            }
        }

    def _get_adaptive_question_pools(self):
        """Simplified adaptive pools"""
        return {
            "unhappiness_deep": {
                26: {
                    "text": "When good things happen to others, you typically:",
                    "type": "single_choice",
                    "options": [
                        "Feel genuinely happy for them",
                        "Wonder why good things don't happen to me",
                        "Feel it proves I'm not worthy of good things",
                        "Get suspicious about what will balance it",
                        "Not applicable"
                    ],
                    "patterns": [None, 1, 1, 1, None],
                    "weights": [0, 2, 3, 2, 0]
                }
            },

            "conflict_trauma": {
                27: {
                    "text": "Growing up, family conflicts usually ended with:",
                    "type": "single_choice",
                    "options": [
                        "Everyone talking through until resolved",
                        "Someone angry, others going silent",
                        "Long periods of tension and not speaking",
                        "Someone apologizing to keep peace",
                        "Not applicable"
                    ],
                    "patterns": [None, 2, 2, 7, None],
                    "weights": [0, 3, 2, 2, 0]
                }
            },

            "family_loyalty": {
                28: {
                    "text": "If you lived authentically, which relationship most threatened:",
                    "type": "single_choice",
                    "options": [
                        "None - relationships would likely improve",
                        "Parents who sacrificed for specific dreams",
                        "Memory or legacy of someone who died",
                        "Family with different success definitions",
                        "Not applicable"
                    ],
                    "patterns": [None, 8, 8, 8, None],
                    "weights": [0, 2, 3, 2, 0]
                }
            },

            "self_neglect": {
                29: {
                    "text": "When thinking about taking time for yourself:",
                    "type": "single_choice",
                    "options": [
                        "I see it as necessary and plan for it",
                        "I feel guilty like I should be productive",
                        "I think of people who need me more",
                        "I feel selfish and undeserving",
                        "Not applicable"
                    ],
                    "patterns": [None, 7, 7, 7, None],
                    "weights": [0, 2, 3, 3, 0]
                }
            }
        }

    def _get_safety_questions(self):
        """Safety assessment questions"""
        return {
            "support_assessment": {
                30: {
                    "text": "If you were in crisis right now, you have:",
                    "type": "single_choice",
                    "options": [
                        "Multiple people I could reach out to",
                        "One or two people I might contact",
                        "People but wouldn't want to burden them",
                        "No one I'd feel comfortable contacting",
                        "Professional support available"
                    ],
                    "risk_assessment": True
                }
            }
        }

    def render(self):
        """Render with FIXED mobile-optimized UX"""
        # Apply IMPROVED mobile styles
        self._apply_improved_mobile_styles()
        
        self._render_header()
        
        if not st.session_state.contact_provided:
            if not st.session_state.assessment_completed:
                self._render_current_question()
            else:
                self._render_contact_form()
        else:
            self._render_results()

    def _apply_improved_mobile_styles(self):
        """Apply IMPROVED mobile-optimized CSS styles with better spacing and alignment"""
        st.markdown("""
        <style>
        /* Remove default Streamlit padding */
        .main .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            max-width: 100% !important;
        }
        
        /* Responsive container */
        @media (min-width: 768px) {
            .main .block-container {
                max-width: 600px !important;
                margin: 0 auto;
            }
        }
        
        /* IMPROVED: Style Streamlit buttons to be mobile-friendly with BETTER SPACING */
        .stButton > button {
            width: 100% !important;
            margin-bottom: 0.25rem !important; /* REDUCED from 0.5rem */
            padding: 0.6rem 1rem !important; /* REDUCED from 0.75rem */
            text-align: left !important; /* FIXED: Left alignment */
            background-color: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 6px !important;
            color: #374151 !important;
            font-size: 0.95rem !important;
            transition: all 0.2s ease !important;
            line-height: 1.3 !important; /* IMPROVED: Better line height */
        }
        
        .stButton > button:hover {
            background-color: #F1F5F9 !important;
            border-color: #4CA1A3 !important;
            transform: translateY(-1px) !important;
        }
        
        .stButton > button:focus {
            background-color: #E1F0F0 !important;
            border-color: #4CA1A3 !important;
            outline: none !important;
        }
        
        /* IMPROVED: Better grid layout for larger screens */
        @media (min-width: 768px) {
            .question-options {
                display: grid !important;
                grid-template-columns: 1fr 1fr !important;
                gap: 0.25rem !important; /* REDUCED gap */
                margin-bottom: 1rem !important;
            }
        }
        
        /* IMPROVED: Mobile single column with minimal spacing */
        @media (max-width: 767px) {
            .question-options .stButton {
                margin-bottom: 0.15rem !important; /* MINIMAL spacing on mobile */
            }
        }
        
        /* Text area styling */
        .stTextArea textarea {
            border: 1px solid #E2E8F0 !important;
            border-radius: 6px !important;
            padding: 0.75rem !important;
            font-size: 0.95rem !important;
        }
        
        /* Navigation button styling */
        .nav-buttons .stButton > button {
            background-color: white !important;
            border: 1px solid #D1D5DB !important;
            color: #374151 !important;
            text-align: center !important;
            padding: 0.5rem 1rem !important;
            margin-bottom: 0.25rem !important;
        }
        
        .nav-buttons .stButton > button:hover {
            background-color: #F9FAFB !important;
            border-color: #9CA3AF !important;
        }
        
        /* Primary button styling */
        .stButton > button[kind="primary"] {
            background-color: #4CA1A3 !important;
            color: white !important;
            border-color: #4CA1A3 !important;
        }
        
        .stButton > button[kind="primary"]:hover {
            background-color: #3B7A7A !important;
        }
        
        /* Hide Streamlit elements */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        
        .stDeployButton {
            display: none !important;
        }
        
        /* Progress bar styling */
        .progress-container {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 0.85rem;
            color: #556D7A;
            padding: 0.5rem;
            background: white;
            border-radius: 6px;
            border: 1px solid #E2E8F0;
        }
        
        .progress-bar {
            flex: 1;
            height: 4px;
            background: #E2E8F0;
            border-radius: 2px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: #4CA1A3;
            transition: width 0.3s ease;
        }
        </style>
        """, unsafe_allow_html=True)

    def _render_header(self):
        """Render compact header"""
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <h1 style="font-size: 1.8rem; margin-bottom: 0.5rem; color: #273548;">
                Behavioral pattern assessment
            </h1>
            <p style="color: #556D7A; font-size: 1rem; margin: 0;">
                Personalized analysis for transformation planning
            </p>
        </div>
        """, unsafe_allow_html=True)

    def _render_current_question(self):
        """Render current question with IMPROVED mobile layout"""
        current_q_id = self._get_current_question_id()
        
        if current_q_id is None:
            st.session_state.assessment_completed = True
            self._calculate_final_results()
            st.rerun()
            return

        question = self._get_question_by_id(current_q_id)
        if not question:
            st.error("Question not found")
            return

        # Calculate progress
        total_questions = self._estimate_total_questions()
        completed = len(st.session_state.assessment_responses)
        progress = completed / total_questions if total_questions > 0 else 0

        # COMPACT progress bar
        st.markdown(f"""
        <div class="progress-container">
            <span><strong>Q {completed + 1}/{total_questions}</strong></span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span><strong>{int(progress * 100)}%</strong></span>
        </div>
        """, unsafe_allow_html=True)

        # Question text - larger and clear
        st.markdown(f"""
        <div style="margin-bottom: 1.5rem;">
            <h3 style="color: #273548; font-size: 1.2rem; line-height: 1.4; margin-bottom: 1rem;">
                {question["text"]}
            </h3>
        </div>
        """, unsafe_allow_html=True)

        # Handle different question types
        if question['type'] == 'single_choice':
            self._render_single_choice_improved(current_q_id, question)
        elif question['type'] == 'text_completion':
            self._render_text_completion(current_q_id, question)

        # Navigation
        self._render_navigation(current_q_id)

    def _render_single_choice_improved(self, q_id, question):
        """Render single choice with IMPROVED spacing and alignment"""
        options = question['options']
        
        # Use container div with assessment-specific class for maximum CSS specificity
        st.markdown('<div class="assessment-container"><div class="question-options">', unsafe_allow_html=True)
        
        for i, option in enumerate(options):
            if st.button(
                option, 
                key=f"q_{q_id}_opt_{i}",
                use_container_width=True
            ):
                self._save_response(q_id, option, question)
                self._advance_question()
                st.rerun()
        
        st.markdown('</div></div>', unsafe_allow_html=True)

    def _render_text_completion(self, q_id, question):
        """Render text completion"""
        response = st.text_area(
            "",
            placeholder=question.get('placeholder', 'Your response...'),
            key=f"q_{q_id}_text",
            height=80,
            label_visibility="collapsed"
        )
        
        # Continue button
        if response.strip():
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, response.strip(), question)
                self._advance_question()
                st.rerun()
        else:
            st.info("Please provide your response to continue.")

    def _render_navigation(self, current_q_id):
        """Render compact navigation"""
        # Navigation area
        st.markdown('<div class="navigation-area">', unsafe_allow_html=True)
        
        # Navigation buttons in columns
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if len(st.session_state.assessment_responses) > 0:
                st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
                if st.button("← Back", key="nav_back", use_container_width=True):
                    self._go_back()
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            # Progress info - compact
            answered_count = len(st.session_state.assessment_responses)
            st.markdown(f"""
            <div style="text-align: center; padding: 0.25rem; color: #556D7A; font-size: 0.8rem;">
                <strong>{answered_count}</strong> answered
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
            if st.button("Skip", key="nav_skip", use_container_width=True, help="If not applicable"):
                self._save_response(current_q_id, "Not applicable", {"patterns": None, "weights": [0]})
                self._advance_question()
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    def _get_current_question_id(self):
        """Get the ID of the current question to display"""
        answered_questions = set(st.session_state.assessment_responses.keys())
        
        # Check core questions first
        for q_id in range(1, 26):
            if q_id not in answered_questions:
                return q_id
        
        # Check adaptive questions
        for pool_name in st.session_state.adaptive_triggered:
            if pool_name in self.adaptive_pools:
                for q_id in self.adaptive_pools[pool_name]:
                    if q_id not in answered_questions:
                        return q_id
        
        # Check safety questions if risk flags triggered
        if st.session_state.risk_flags:
            for pool_name in ["support_assessment"]:
                if pool_name in self.safety_questions:
                    for q_id in self.safety_questions[pool_name]:
                        if q_id not in answered_questions:
                            return q_id
        
        return None  # Assessment complete

    def _get_question_by_id(self, q_id):
        """Get question data by ID from any pool"""
        # Check core questions
        if q_id in self.core_questions:
            return self.core_questions[q_id]
        
        # Check adaptive pools
        for pool in self.adaptive_pools.values():
            if q_id in pool:
                return pool[q_id]
        
        # Check safety questions
        for pool in self.safety_questions.values():
            if q_id in pool:
                return pool[q_id]
        
        return None

    def _save_response(self, q_id, response, question):
        """Save response and trigger adaptive logic"""
        # Save response
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Update pattern scores
        self._update_pattern_scores(q_id, response, question)
        
        # Check for adaptive triggers
        self._check_adaptive_triggers(q_id, response, question)
        
        # Check for risk flags
        self._check_risk_flags(q_id, response, question)

    def _update_pattern_scores(self, q_id, response, question):
        """Update pattern scores based on response"""
        if 'patterns' not in question or question['patterns'] is None:
            return
        
        if question['type'] == 'single_choice':
            patterns = question.get('patterns', [])
            weights = question.get('weights', [])
            
            if isinstance(patterns, list) and isinstance(weights, list):
                # Find selected option index
                options = question.get('options', [])
                try:
                    option_index = options.index(response)
                    if option_index < len(patterns) and patterns[option_index] is not None:
                        pattern_id = patterns[option_index]
                        weight = weights[option_index] if option_index < len(weights) else 1
                        
                        if pattern_id not in st.session_state.pattern_scores:
                            st.session_state.pattern_scores[pattern_id] = 0
                        st.session_state.pattern_scores[pattern_id] += weight
                except ValueError:
                    pass  # Response not in options

    def _check_adaptive_triggers(self, q_id, response, question):
        """Check if response triggers adaptive question pools"""
        adaptive_triggers = question.get('adaptive_triggers', [])
        
        if question['type'] == 'single_choice':
            options = question.get('options', [])
            try:
                option_index = options.index(response)
                
                # Check specific option triggers
                for trigger in adaptive_triggers:
                    if trigger not in st.session_state.adaptive_triggered:
                        # Add trigger logic based on response patterns
                        if self._should_trigger_adaptive_pool(trigger, option_index, response):
                            st.session_state.adaptive_triggered.append(trigger)
                            
            except ValueError:
                pass
        elif question['type'] == 'text_completion':
            # Trigger adaptive pools for text responses
            for trigger in adaptive_triggers:
                if trigger not in st.session_state.adaptive_triggered:
                    st.session_state.adaptive_triggered.append(trigger)

    def _should_trigger_adaptive_pool(self, trigger, option_index, response):
        """Determine if adaptive pool should be triggered"""
        # Skip "Not applicable" responses (typically index 4)
        if option_index >= 4:
            return False
            
        trigger_conditions = {
            "unhappiness_deep": option_index in [1, 2, 3],
            "conflict_trauma": option_index in [1, 2, 3],
            "family_loyalty": option_index in [1, 2, 3],
            "self_neglect": option_index in [1, 2, 3],
            "trust_trauma": option_index in [1, 2, 3],
            "performance_anxiety": option_index in [1, 2, 3],
            "identity_fragmentation": option_index in [1, 2, 3],
            "binary_thinking": option_index in [1, 2, 3],
            "boundary_collapse": option_index in [1, 2, 3],
            "social_anxiety": option_index in [1, 2, 3],
            "success_sabotage": option_index in [1, 2, 3],
            "context_weakness": option_index in [1, 2, 3],
            "recognition_needs": option_index in [1, 2, 3],
            "urgency_high": option_index in [0, 1],
            "authenticity_gap": option_index in [1, 2, 3],
            "energy_imbalance": option_index in [1, 2, 3],
            "family_messages": option_index in [1, 2, 3],
            "change_resistance": option_index in [1, 2, 3],
            "trust_issues": option_index in [1, 2, 3],
            "boundary_issues": option_index in [1, 2, 3],
            "compartmentalization": option_index in [1, 2, 3],
            "authentic_self": option_index in [1, 2, 3],
            "core_belief": True  # Text completion always triggers
        }
        
        return trigger_conditions.get(trigger, False)

    def _check_risk_flags(self, q_id, response, question):
        """Check for risk indicators"""
        if hasattr(question, 'risk_assessment') and question.get('risk_assessment'):
            options = question.get('options', [])
            try:
                option_index = options.index(response)
                if option_index >= 3:  # Options indicating isolation or lack of support
                    if 'social_isolation' not in st.session_state.risk_flags:
                        st.session_state.risk_flags.append('social_isolation')
            except ValueError:
                pass

    def _advance_question(self):
        """Advance to next question"""
        st.session_state.current_question += 1

    def _go_back(self):
        """Go back to previous question"""
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            # Remove last response
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]

    def _estimate_total_questions(self):
        """Estimate total questions based on current triggers"""
        base_questions = 25
        adaptive_questions = len(st.session_state.adaptive_triggered) * 1  # 1 per pool
        safety_questions = len(st.session_state.risk_flags) * 1
        
        return base_questions + adaptive_questions + safety_questions

    def _calculate_final_results(self):
        """Calculate final assessment results"""
        # Calculate pattern dominance
        sorted_patterns = sorted(
            st.session_state.pattern_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Extract clinical insights
        clinical_insights = self._extract_clinical_insights()
        
        # Calculate readiness metrics
        readiness_metrics = self._calculate_readiness_metrics()
        
        # Generate resistance predictions
        resistance_predictions = self._predict_resistance_points()
        
        # Store comprehensive results
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': sorted_patterns[0] if sorted_patterns else (None, 0),
            'secondary_patterns': sorted_patterns[1:3] if len(sorted_patterns) > 1 else [],
            'clinical_insights': clinical_insights,
            'readiness_metrics': readiness_metrics,
            'resistance_predictions': resistance_predictions,
            'risk_flags': st.session_state.risk_flags,
            'adaptive_triggered': st.session_state.adaptive_triggered,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses)
        }

    def _extract_clinical_insights(self):
        """Extract insights from text responses"""
        insights = {}
        
        for q_id, response_data in st.session_state.assessment_responses.items():
            if response_data.get('question_type') == 'text_completion':
                question = self._get_question_by_id(q_id)
                if question and 'patterns' in question:
                    pattern_type = question['patterns']
                    insights[pattern_type] = response_data['response']
        
        return insights

    def _calculate_readiness_metrics(self):
        """Calculate transformation readiness"""
        readiness_score = 5  # Default
        
        # Extract from urgency question
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            if 'Extremely urgent' in response:
                readiness_score = 10
            elif 'Very urgent' in response:
                readiness_score = 8
            elif 'Moderately urgent' in response:
                readiness_score = 6
            elif 'Somewhat urgent' in response:
                readiness_score = 4
            elif 'Not urgent' in response:
                readiness_score = 2
        
        return {
            'urgency_level': readiness_score,
            'risk_level': 'High' if st.session_state.risk_flags else 'Low',
            'complexity': 'High' if len(st.session_state.adaptive_triggered) > 3 else 'Medium'
        }

    def _predict_resistance_points(self):
        """Predict resistance based on patterns"""
        predictions = []
        pattern_scores = st.session_state.pattern_scores
        
        if pattern_scores.get(1, 0) > 5:
            predictions.append("Will resist positive suggestions as 'fake' or 'temporary'")
        
        if pattern_scores.get(3, 0) > 5:
            predictions.append("May be skeptical of therapist intentions")
        
        if pattern_scores.get(8, 0) > 5:
            predictions.append("Change may feel like betraying family expectations")
        
        return predictions[:3]

    def _render_contact_form(self):
        """Render contact form with mobile optimization"""
        st.markdown("### Assessment complete")
        st.write("Provide your details to receive your behavioral pattern analysis.")
        
        with st.form("assessment_contact_form"):
            # Compact form layout
            name = st.text_input("Full name*", placeholder="Your full name")
            email = st.text_input("Email*", placeholder="your@email.com")
            phone = st.text_input("Phone (optional)", placeholder="+66 xxx xxx xxx")
            
            urgency = st.selectbox(
                "How urgent is your concern?",
                ["Select urgency...", "Extremely urgent", "Very urgent", "Moderately urgent", "Not urgent"]
            )
            
            concern = st.text_area(
                "Primary concern*",
                placeholder="What brought you to this assessment?",
                height=80
            )
            
            next_step = st.selectbox(
                "Preferred next step:",
                ["Select preference...", "Schedule discovery call", "Book transformation package", "Request analysis first"]
            )
            
            submitted = st.form_submit_button("Get my analysis", type="primary", use_container_width=True)
            
            if submitted:
                if self._validate_contact_form(name, email, concern, urgency, next_step):
                    self._save_contact_info(name, email, phone, urgency, concern, next_step)
                    self._send_assessment_results()
                    st.session_state.contact_provided = True
                    st.rerun()

    def _validate_contact_form(self, name, email, concern, urgency, next_step):
        """Validate contact form with CORRECTED email regex"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        if not email.strip():
            errors.append("Email is required")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
            errors.append("Valid email required")
        if not concern.strip():
            errors.append("Primary concern required")
        if urgency == "Select urgency...":
            errors.append("Please select urgency level")
        if next_step == "Select preference...":
            errors.append("Please select next step")
        
        for error in errors:
            st.error(f"❌ {error}")
        
        return len(errors) == 0

    def _save_contact_info(self, name, email, phone, urgency, concern, next_step):
        """Save contact information"""
        st.session_state.contact_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'urgency': urgency,
            'primary_concern': concern,
            'next_step': next_step,
            'timestamp': datetime.now().isoformat()
        }

    def _send_assessment_results(self):
        """Send assessment results via email"""
        try:
            from utils.enhanced_email_handler import send_assessment_results_email
            
            # Prepare data package
            assessment_data = {
                'name': st.session_state.contact_info['name'],
                'email': st.session_state.contact_info['email'],
                'phone': st.session_state.contact_info.get('phone', 'Not provided'),
                'urgency': st.session_state.contact_info['urgency'],
                'primary_concern': st.session_state.contact_info['primary_concern'],
                'next_step': st.session_state.contact_info['next_step'],
                'form_type': 'Mobile-Optimized Behavioral Assessment',
                'assessment_results': st.session_state.assessment_results,
                'raw_responses': st.session_state.assessment_responses,
                'clinical_template': self._generate_clinical_template(),
                'response_transcript': self._generate_response_transcript(),
                'total_questions': len(st.session_state.assessment_responses),
                'completion_rate': '100%',
                'timestamp': datetime.now().isoformat()
            }
            
            success = send_assessment_results_email(assessment_data)
            
            if success:
                st.success("✅ Assessment results sent successfully!")
            else:
                st.warning("⚠️ Assessment completed, but email notification failed.")
                
        except Exception as e:
            st.error(f"Error sending results: {str(e)}")

    def _generate_clinical_template(self):
        """Generate clinical template"""
        results = st.session_state.assessment_results
        contact = st.session_state.contact_info
        
        # Get top patterns
        pattern_scores = results.get('pattern_scores', {})
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
        secondary = sorted_patterns[1] if len(sorted_patterns) > 1 else (None, 0)
        
        template = f"""
MOBILE-OPTIMIZED BEHAVIORAL ASSESSMENT - CLINICAL TEMPLATE
Client: {contact['name']} | Date: {datetime.now().strftime('%Y-%m-%d')}

DOMINANT PATTERNS:
Primary: {self.patterns.get(dominant[0], 'None')} (Score: {dominant[1]}/8)
Secondary: {self.patterns.get(secondary[0], 'None')} (Score: {secondary[1]}/8)

SESSION PLANNING:
Session 1: Map {self.patterns.get(dominant[0], 'primary')} patterns
Session 2: Rewire {self.patterns.get(dominant[0], 'primary pattern')}
Session 3: Reinforcement if needed

READINESS: {results.get('readiness_metrics', {}).get('urgency_level', 5)}/10
COMPLEXITY: {results.get('readiness_metrics', {}).get('complexity', 'Medium')}
ADAPTIVE POOLS: {len(results.get('adaptive_triggered', []))}
        """
        
        return template

    def _generate_response_transcript(self):
        """Generate response transcript"""
        transcript = []
        
        for q_id in sorted(st.session_state.assessment_responses.keys()):
            response_data = st.session_state.assessment_responses[q_id]
            
            transcript.append({
                'question_id': q_id,
                'question_text': response_data['question_text'],
                'response': response_data['response'],
                'question_type': response_data['question_type'],
                'timestamp': response_data['timestamp'],
                'clinical_relevance': f"Question {q_id} assessment data"
            })
        
        return transcript

    def _render_results(self):
        """Render assessment results"""
        st.markdown("## Assessment analysis complete")
        st.success("Your behavioral pattern analysis has been sent to our clinical team.")
        
        # Basic summary
        results = st.session_state.assessment_results
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Questions", results['total_questions_answered'], "Completed")
        
        with col2:
            urgency = results.get('readiness_metrics', {}).get('urgency_level', 5)
            st.metric("Readiness", f"{urgency}/10", "Level")
        
        with col3:
            complexity = results.get('readiness_metrics', {}).get('complexity', 'Medium')
            st.metric("Complexity", complexity, "Assessment")

        # Clinical analysis with paywall
        self._render_clinical_analysis_section()
        
        # Next steps
        st.markdown("### Your next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        next_step = contact_info.get('next_step', '')
        
        if 'discovery call' in next_step.lower():
            st.info("We'll contact you to schedule a discovery call.")
        elif 'package' in next_step.lower():
            st.success("We'll contact you with scheduling options.")
        else:
            st.info("We'll review and contact you with recommendations.")
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical review** (24 hours): Analysis for optimal approach
        2. **Personal contact** (48 hours): Specific recommendations  
        3. **Discovery call** (Optional): Discuss results
        4. **Transformation sessions**: Begin your personalized program
        """)

    def _render_clinical_analysis_section(self):
        """Render clinical analysis with paywall"""
        st.markdown("### Clinical pattern analysis")
        
        if PAYWALL_AVAILABLE:
            try:
                paywall = create_clinical_paywall()
                
                assessment_data = {
                    'assessment_results': st.session_state.assessment_results,
                    'assessment_responses': st.session_state.assessment_responses,
                }
                
                contact_info = st.session_state.get('contact_info', {})
                assessment_data.update(contact_info)
                
                if paywall.check_payment_status():
                    paywall.render_premium_analysis(assessment_data)
                else:
                    self._render_analysis_preview()
                    with st.expander("Unlock complete analysis", expanded=False):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading analysis: {str(e)}")
                self._render_analysis_preview()
        else:
            self._render_analysis_preview()

    def _render_analysis_preview(self):
        """Render analysis preview"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            st.markdown("**Preview - Your dominant patterns:**")
            for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
                pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
                st.write(f"• {pattern_name}: Pattern detected")
            
            if len(sorted_patterns) > 2:
                remaining = len(sorted_patterns) - 2
                st.write(f"• Plus {remaining} additional patterns analyzed...")
        
        st.info("Unlock complete analysis for detailed insights and transformation roadmap.")


class AssessPage:
    """FIXED Mobile-optimized assessment page"""
    
    def __init__(self):
        self.assessment = AdaptiveBehavioralAssessment()
    
    def render(self):
        """Render the assessment page"""
        self.assessment.render()


def create_assess_page():
    """Factory function"""
    return AssessPage()
