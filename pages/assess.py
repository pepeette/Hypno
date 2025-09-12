# # Enhanced Clinical Behavioral Pattern Assessment - Complete Final Version
# # Comprehensive implementation with all optimizations and full functionality

# import streamlit as st
# from datetime import datetime
# import re

# # ---- Paywall Integration ----
# try:
#     from components.paywall import create_clinical_paywall
#     PAYWALL_AVAILABLE = True
# except ImportError:
#     PAYWALL_AVAILABLE = False

# # ---- Styling Functions ----
# def apply_clinical_styles():
#     """Apply expert clinical-grade styling with enhanced UX elements"""
#     st.markdown("""
#     <style>
#     .main .block-container {
#         padding-top: 0.75rem !important;
#         padding-bottom: 0.75rem !important;
#         max-width: 100% !important;
#     }
#     @media (min-width: 768px) {
#         .main .block-container {
#             max-width: 600px !important;
#             margin: 0 auto;
#         }
#     }
#     .stButton > button {
#         width: 100% !important;
#         margin-bottom: 0.25rem !important;
#         padding: 0.6rem 1rem !important;
#         text-align: left !important;
#         background-color: #F8FAFC !important;
#         border: 1px solid #E2E8F0 !important;
#         border-radius: 6px !important;
#         color: #374151 !important;
#         font-size: 0.95rem !important;
#         transition: all 0.2s ease !important;
#         line-height: 1.3 !important;
#     }
#     .stButton > button:hover {
#         background-color: #F1F5F9 !important;
#         border-color: #4CA1A3 !important;
#         transform: translateY(-1px) !important;
#     }
#     .stButton > button:focus {
#         background-color: #E1F0F0 !important;
#         border-color: #4CA1A3 !important;
#         outline: none !important;
#     }
#     .clinical-question {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 1.5rem;
#         border-radius: 12px;
#         margin-bottom: 1.5rem;
#         color: white;
#     }
#     .safety-notice {
#         background-color: #fff3cd;
#         border: 1px solid #ffeaa7;
#         border-radius: 8px;
#         padding: 1rem;
#         margin: 1rem 0;
#         font-size: 0.9rem;
#     }
#     .clinical-insight {
#         background-color: #e3f2fd;
#         border-left: 4px solid #2196f3;
#         padding: 0.75rem;
#         margin: 0.5rem 0;
#         font-size: 0.85rem;
#     }
#     .progress-container {
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#         margin-bottom: 1.5rem;
#         font-size: 0.85rem;
#         color: #556D7A;
#         padding: 0.5rem;
#         border-radius: 6px;
#         border: 1px solid #E2E8F0;
#     }
#     .progress-bar {
#         flex: 1;
#         height: 4px;
#         background: #E2E8F0;
#         border-radius: 2px;
#         overflow: hidden;
#     }
#     .progress-fill {
#         height: 100%;
#         background: #4CA1A3;
#         transition: width 0.3s ease;
#     }
#     .time-estimate {
#         font-size: 0.8rem;
#         color: #64748b;
#         text-align: center;
#         margin-top: 0.5rem;
#     }
#     .char-counter {
#         font-size: 0.8rem;
#         margin-top: 0.5rem;
#         text-align: right;
#     }
#     .char-counter.sufficient {
#         color: #059669;
#     }
#     .char-counter.insufficient {
#         color: #dc2626;
#     }
#     @media (max-width: 768px) {
#         .main .block-container {
#             padding-left: 1rem;
#             padding-right: 1rem;
#             padding-top: 1rem;
#         }
#         .clinical-question {
#             padding: 1rem;
#             margin-bottom: 1rem;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ---- Enhanced Assessment Class ----
# class ComprehensiveBehavioralAssessment:
#     """Clinical-grade behavioral pattern assessment optimized for completion and accuracy"""
    
#     def __init__(self):
#         self._init_session_state()
#         self.patterns = {
#             1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 4: "Separation and Division",
#             5: "Doing versus Being", 6: "Compartmentalized Authenticity", 7: "Self Sacrifice and Care Avoidance",
#             8: "Inherited Missions", 9: "Context Dependent Weakness"
#         }
#         self.core_questions = self._get_core_questions()
#         self.adaptive_pools = self._get_adaptive_question_pools()
#         self.safety_questions = self._get_safety_questions()
#         self.hypnotic_questions = self._get_hypnotic_responsiveness_questions()

#     def _init_session_state(self):
#         defaults = {
#             'assessment_responses': {},
#             'current_question': 1,
#             'question_sequence': [],
#             'adaptive_triggered': [],
#             'assessment_completed': False,
#             'contact_provided': False,
#             'assessment_results': {},
#             'pattern_scores': {},
#             'risk_flags': [],
#             'start_time': datetime.now().isoformat(),
#             'intensity_responses': {}
#         }
#         for key, value in defaults.items():
#             if key not in st.session_state:
#                 st.session_state[key] = value

#     def _get_core_questions(self):
#         """Optimized core questions balancing clinical depth with user experience"""
#         return {
#             1: {
#                 "text": "What specific behavior or pattern would you most like to transform?",
#                 "type": "text_completion",
#                 "placeholder": "Describe the exact behavior, feeling, or situation you want to change (e.g., 'procrastination on important tasks', 'anxiety in social situations', 'perfectionism that prevents me from finishing projects')...",
#                 "patterns": "presenting_problem",
#                 "min_chars": 5,
#                 "adaptive_triggers": ["behavioral_specificity"],
#                 "clinical_insight": "Primary therapeutic target identification"
#             },
#             2: {
#                 "text": "How long has this pattern been affecting your life?",
#                 "type": "single_choice",
#                 "options": [
#                     "Less than 6 months",
#                     "6 months to 2 years", 
#                     "2-5 years",
#                     "5-10 years",
#                     "Over 10 years or as long as I can remember"
#                 ],
#                 "patterns": "chronicity",
#                 "weights": [1, 2, 3, 4, 5],
#                 "adaptive_triggers": ["pattern_entrenchment"],
#                 "clinical_insight": "Pattern entrenchment assessment"
#             },
#             3: {
#                 "text": "Rate how much this pattern interferes with your daily life:",
#                 "type": "scale_7",
#                 "labels": ["Minimal disruption", "Completely overwhelming"],
#                 "patterns": "interference_level",
#                 "clinical_insight": "Functional impact measurement"
#             },
#             4: {
#                 "text": "Describe a typical situation that triggers this pattern:",
#                 "type": "text_completion",
#                 "placeholder": "What happens right before the pattern occurs? Who is involved? Where are you? What time of day? Be specific about the context...",
#                 "patterns": "trigger_mapping",
#                 "min_chars": 5,
#                 "adaptive_triggers": ["trigger_specificity"],
#                 "clinical_insight": "Environmental trigger identification"
#             },
#             5: {
#                 "text": "When this pattern gets triggered, your first physical sensation is:",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "Chest tightness, heart racing, or breathing changes",
#                     "Stomach drop, nausea, or digestive discomfort",
#                     "Muscle tension, clenching, or physical rigidity",
#                     "Hot flash, sweating, or temperature changes",
#                     "Numbness, disconnection, or dissociative feelings",
#                     "Restlessness, agitation, or urge to move/escape",
#                     "No noticeable physical response"
#                 ],
#                 "patterns": "somatic_response",
#                 "weights": [3, 3, 2, 2, 4, 3, 0],
#                 "adaptive_triggers": ["somatic_awareness"],
#                 "clinical_insight": "Somatic awareness mapping"
#             },
#             6: {
#                 "text": "What emotions surface immediately after the physical sensation?",
#                 "type": "multi_select_weighted",
#                 "max_selections": 4,
#                 "options": [
#                     "Anxiety/Fear", "Anger/Rage", "Shame/Embarrassment", 
#                     "Sadness/Grief", "Guilt/Self-blame", "Frustration/Irritation", 
#                     "Overwhelm/Panic", "Numbness/Emptiness", "Confusion/Disorientation"
#                 ],
#                 "patterns": "emotional_chain",
#                 "clinical_insight": "Emotional sequence mapping"
#             },
#             7: {
#                 "text": "Your inner voice typically says:",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "\"I'm not good enough / I'm inadequate\"",
#                     "\"Something bad will happen / Danger is coming\"",
#                     "\"I can't handle this / I'm powerless\"",
#                     "\"They'll reject, judge, or abandon me\"",
#                     "\"I should be doing more / I'm lazy\"",
#                     "\"This is hopeless / Nothing will change\"",
#                     "\"I need to control this situation\""
#                 ],
#                 "patterns": [1, 3, 7, 3, 5, 1, 2],
#                 "weights": [3, 2, 3, 2, 2, 3, 3],
#                 "adaptive_triggers": ["core_beliefs"],
#                 "clinical_insight": "Core cognitive distortion identification"
#             },
#             8: {
#                 "text": "Your typical behavioral response is:",
#                 "type": "single_choice",
#                 "options": [
#                     "Avoidance, withdrawal, or procrastination",
#                     "Compulsive action, repetition, or checking behaviors",
#                     "Seeking reassurance or approval from others",
#                     "Self-critical internal dialogue or self-punishment",
#                     "Overcompensation, perfectionism, or over-preparation",
#                     "Aggressive behavior, arguing, or attempts to control"
#                 ],
#                 "patterns": [7, 5, 3, 1, 5, 2],
#                 "weights": [2, 3, 2, 3, 2, 3],
#                 "adaptive_triggers": ["behavioral_pattern"],
#                 "clinical_insight": "Behavioral response identification"
#             },
#             9: {
#                 "text": "What happens after this behavioral response?",
#                 "type": "single_choice",
#                 "options": [
#                     "Temporary relief followed by guilt or shame",
#                     "The pattern escalates or gets worse over time",
#                     "Emotional exhaustion and numbness",
#                     "Conflict or problems in relationships", 
#                     "The pattern reinforces itself for next time",
#                     "I feel more anxious and out of control"
#                 ],
#                 "patterns": "consequence_chain",
#                 "weights": [2, 3, 2, 2, 3, 2],
#                 "clinical_insight": "Pattern reinforcement cycle analysis"
#             },
#             10: {
#                 "text": "Are you currently receiving any medical or mental health care?",
#                 "type": "single_choice",
#                 "options": [
#                     "No medical or mental health care currently",
#                     "Physical health care only",
#                     "Mental health counseling or therapy only",
#                     "Both physical and mental health care",
#                     "Psychiatric medication management only",
#                     "Prefer not to disclose"
#                 ],
#                 "risk_assessment": True,
#                 "clinical_insight": "Medical contraindication screening"
#             },
#             11: {
#                 "text": "Rate your experience with intense emotional states:",
#                 "type": "single_choice",
#                 "options": [
#                     "Rarely experience intense emotions",
#                     "Occasional intense emotions, easily managed",
#                     "Regular intense emotions, usually manageable",
#                     "Frequent overwhelming emotions, hard to manage",
#                     "Constant emotional intensity, feels uncontrollable"
#                 ],
#                 "risk_assessment": True,
#                 "weights": [0, 1, 2, 3, 4],
#                 "clinical_insight": "Emotional regulation capacity assessment"
#             },
#             12: {
#                 "text": "Have you experienced dissociation, panic attacks, or thoughts of self-harm?",
#                 "type": "single_choice",
#                 "options": [
#                     "Never experienced any of these",
#                     "Very rarely and easily manageable",
#                     "Occasionally but I have coping strategies",
#                     "Frequently and they significantly impact my life",
#                     "Currently experiencing these regularly"
#                 ],
#                 "risk_assessment": True,
#                 "weights": [0, 1, 2, 3, 4],
#                 "clinical_insight": "Crisis risk assessment"
#             },
#             13: {
#                 "text": "Do you use any substances to cope with this pattern?",
#                 "type": "single_choice",
#                 "options": [
#                     "Never use substances for coping",
#                     "Occasional alcohol (1-2 drinks socially)",
#                     "Regular alcohol use to manage emotions",
#                     "Prescription medication as prescribed", 
#                     "Recreational drugs or misused prescriptions"
#                 ],
#                 "risk_assessment": True,
#                 "weights": [0, 1, 2, 1, 3],
#                 "clinical_insight": "Substance use patterns assessment"
#             },
#             14: {
#                 "text": "When something wonderful happens in your life, your immediate reaction is:",
#                 "type": "single_choice",
#                 "options": [
#                     "Genuine enjoyment and celebration",
#                     "Immediately searching for potential problems",
#                     "Feeling undeserving or guilty",
#                     "Minimizing its importance or downplaying it",
#                     "Emotional numbness or disconnection from joy"
#                 ],
#                 "patterns": [None, 1, 1, 1, 1],
#                 "weights": [0, 3, 3, 2, 4],
#                 "adaptive_triggers": ["unhappiness_deep"],
#                 "clinical_insight": "Pleasure reception capacity"
#             },
#             15: {
#                 "text": "During interpersonal conflict, your nervous system response is:",
#                 "type": "single_choice",
#                 "options": [
#                     "Generally calm and able to think clearly",
#                     "Fight response - tension, anger, need to argue",
#                     "Flight response - strong urge to escape",
#                     "Freeze response - numbness, shutdown, unable to speak",
#                     "Fawn response - immediate people-pleasing and apologizing"
#                 ],
#                 "patterns": [None, 2, 2, 2, 7],
#                 "weights": [0, 3, 2, 3, 2],
#                 "adaptive_triggers": ["conflict_trauma"],
#                 "clinical_insight": "Autonomic nervous system patterns"
#             },
#             16: {
#                 "text": "Your default assumption about new people's intentions toward you is:",
#                 "type": "single_choice",
#                 "options": [
#                     "Generally well-meaning until proven otherwise",
#                     "Probably judging or critically evaluating me",
#                     "Wanting something from me or likely to use me",
#                     "Will reject me once they discover my flaws",
#                     "Indifferent or uninterested in connecting"
#                 ],
#                 "patterns": [None, 3, 3, 3, 3],
#                 "weights": [0, 2, 3, 3, 1],
#                 "adaptive_triggers": ["trust_trauma"],
#                 "clinical_insight": "Relational expectation patterns"
#             },
#             17: {
#                 "text": "When facing important life decisions, you typically feel:",
#                 "type": "single_choice",
#                 "options": [
#                     "Multiple creative options and possibilities exist",
#                     "Trapped between two impossible either/or choices",
#                     "Only extreme alternatives with no middle ground",
#                     "Paralyzed by black and white thinking",
#                     "Overwhelmed by too many complex options"
#                 ],
#                 "patterns": [None, 4, 4, 4, 4],
#                 "weights": [0, 2, 3, 3, 2],
#                 "adaptive_triggers": ["binary_thinking"],
#                 "clinical_insight": "Cognitive flexibility assessment"
#             },
#             18: {
#                 "text": "Complete this sentence: 'I feel most valuable when I...'",
#                 "type": "single_choice",
#                 "options": [
#                     "Simply exist as I am, without proving anything",
#                     "Accomplish something important or significant",
#                     "Help other people or make them happy", 
#                     "Prove my worth through performance",
#                     "Receive external validation or recognition"
#                 ],
#                 "patterns": [None, 5, 7, 5, 5],
#                 "weights": [0, 2, 2, 3, 2],
#                 "adaptive_triggers": ["performance_anxiety"],
#                 "clinical_insight": "Self-worth conditioning analysis"
#             },
#             19: {
#                 "text": "Your personality and behavior change significantly based on:",
#                 "type": "single_choice",
#                 "options": [
#                     "They stay consistent across all situations",
#                     "Which group of people I'm with",
#                     "Professional versus personal settings",
#                     "Whether I'm in control or following others",
#                     "My current emotional state or stress level"
#                 ],
#                 "patterns": [None, 6, 6, 6, 6],
#                 "weights": [0, 2, 2, 3, 2],
#                 "adaptive_triggers": ["identity_fragmentation"],
#                 "clinical_insight": "Identity consistency patterns"
#             },
#             20: {
#                 "text": "When it comes to your own health, self-care, and wellbeing:",
#                 "type": "single_choice",
#                 "options": [
#                     "I naturally prioritize it alongside caring for others",
#                     "I know what I should do but struggle to follow through",
#                     "I care for everyone else first, no energy left for me",
#                     "I feel selfish or guilty focusing on my own needs",
#                     "I completely neglect my own needs"
#                 ],
#                 "patterns": [None, 7, 7, 7, 7],
#                 "weights": [0, 2, 3, 3, 4],
#                 "adaptive_triggers": ["self_neglect"],
#                 "clinical_insight": "Self-care capacity patterns"
#             },
#             21: {
#                 "text": "Your major life goals are primarily influenced by:",
#                 "type": "single_choice",
#                 "options": [
#                     "What I genuinely desire for my own fulfillment",
#                     "What my family expected or dreamed for me",
#                     "Honoring someone who died or sacrificed",
#                     "Proving I'm worthy of someone's love",
#                     "Rebelling against others' expectations"
#                 ],
#                 "patterns": [None, 8, 8, 8, 8],
#                 "weights": [0, 2, 3, 3, 2],
#                 "adaptive_triggers": ["family_loyalty"],
#                 "clinical_insight": "Autonomy versus loyalty conflicts"
#             },
#             22: {
#                 "text": "With certain people or situations, you tend to:",
#                 "type": "single_choice",
#                 "options": [
#                     "Stay true to your values and boundaries",
#                     "Become someone you don't recognize",
#                     "Lose all your usual boundaries",
#                     "Can't say no even when you want to",
#                     "Completely lose sense of self"
#                 ],
#                 "patterns": [None, 9, 9, 9, 9],
#                 "weights": [0, 2, 3, 3, 4],
#                 "adaptive_triggers": ["boundary_collapse"],
#                 "clinical_insight": "Context-dependent self-regulation"
#             },
#             23: {
#                 "text": "What would you lose if this pattern completely disappeared tomorrow?",
#                 "type": "text_completion",
#                 "placeholder": "Consider: What protection does it provide? What identity might change? How might relationships shift?",
#                 "patterns": "secondary_gain",
#                 "min_chars": 5,
#                 "adaptive_triggers": ["resistance_mapping"],
#                 "clinical_insight": "Secondary gain identification"
#             },
#             24: {
#                 "text": "How easily can you become completely absorbed in movies, books, or daydreams?",
#                 "type": "single_choice",
#                 "options": [
#                     "Very easily - completely lose track of time",
#                     "Moderately easily - can get quite absorbed",
#                     "Sometimes - depends on my mood",
#                     "Rarely - usually remain aware of surroundings",
#                     "Almost never - always maintain awareness"
#                 ],
#                 "patterns": "absorption_capacity",
#                 "weights": [5, 4, 3, 2, 1],
#                 "clinical_insight": "Natural trance capacity assessment"
#             },
#             25: {
#                 "text": "What type of therapeutic guidance appeals most to you?",
#                 "type": "single_choice",
#                 "options": [
#                     "Direct, clear instructions and guidance",
#                     "Gentle, permissive suggestions",
#                     "Metaphorical stories and symbolic approaches",
#                     "Collaborative exploration together",
#                     "Scientific explanations and logical understanding"
#                 ],
#                 "patterns": "therapeutic_preference",
#                 "clinical_insight": "Therapeutic modality optimization"
#             }
#         }

#     def _get_adaptive_question_pools(self):
#         """Targeted follow-up questions triggered by specific responses"""
#         return {
#             "unhappiness_deep": {
#                 26: {
#                     "text": "What messages did you receive in your family about happiness and success?",
#                     "type": "single_choice",
#                     "options": [
#                         "Happiness is natural and should be celebrated",
#                         "Happiness must be earned through achievement",
#                         "Too much happiness leads to disappointment",
#                         "Others' happiness is more important than your own",
#                         "Happiness is selfish or frivolous"
#                     ],
#                     "patterns": [None, 5, 1, 7, 1],
#                     "weights": [0, 2, 3, 2, 3],
#                     "clinical_insight": "Intergenerational happiness patterns"
#                 }
#             },
#             "conflict_trauma": {
#                 27: {
#                     "text": "During childhood conflicts, the adults around you typically:",
#                     "type": "single_choice",
#                     "options": [
#                         "Modeled healthy conflict resolution",
#                         "Escalated conflicts with yelling or aggression",
#                         "Completely avoided conflict",
#                         "Used guilt or manipulation",
#                         "Were unpredictable in responses"
#                     ],
#                     "patterns": [None, 2, 2, 2, 2],
#                     "weights": [0, 3, 2, 3, 4],
#                     "clinical_insight": "Early conflict modeling"
#                 }
#             },
#             "trust_trauma": {
#                 28: {
#                     "text": "Your earliest trust violation involved:",
#                     "type": "single_choice",
#                     "options": [
#                         "No significant early violations",
#                         "Broken promises from caregivers",
#                         "Betrayal by close friends",
#                         "Emotional unavailability",
#                         "Abuse or severe neglect"
#                     ],
#                     "patterns": [None, 3, 3, 3, 3],
#                     "weights": [0, 2, 2, 3, 4],
#                     "clinical_insight": "Trust development history"
#                 }
#             },
#             "binary_thinking": {
#                 29: {
#                     "text": "Where did you learn that choices had to be either/or?",
#                     "type": "text_completion",
#                     "placeholder": "Consider family rules, religious teachings, school experiences...",
#                     "patterns": "cognitive_conditioning",
#                     "min_chars": 5,
#                     "clinical_insight": "Rigid thinking pattern origins"
#                 }
#             },
#             "performance_anxiety": {
#                 30: {
#                     "text": "What childhood experiences linked your worth to performance?",
#                     "type": "text_completion",
#                     "placeholder": "Think about school, activities, family expectations...",
#                     "patterns": "worth_conditioning",
#                     "min_chars": 5,
#                     "clinical_insight": "Performance-based worth conditioning"
#                 }
#             },
#             "identity_fragmentation": {
#                 31: {
#                     "text": "When did you learn to show different selves to different people?",
#                     "type": "text_completion",
#                     "placeholder": "Consider family dynamics, social groups, safety concerns...",
#                     "patterns": "identity_development",
#                     "min_chars": 5,
#                     "clinical_insight": "Authentic self-expression patterns"
#                 }
#             },
#             "self_neglect": {
#                 32: {
#                     "text": "Who modeled self-sacrifice as virtue in your upbringing?",
#                     "type": "single_choice",
#                     "options": [
#                         "No one specifically modeled self-sacrifice",
#                         "Primary caregiver",
#                         "Extended family member",
#                         "Religious or cultural community",
#                         "Multiple people - it was the norm"
#                     ],
#                     "patterns": [None, 7, 7, 7, 7],
#                     "weights": [0, 2, 2, 2, 3],
#                     "clinical_insight": "Self-sacrifice modeling"
#                 }
#             },
#             "family_loyalty": {
#                 33: {
#                     "text": "What unspoken family rules still govern your choices?",
#                     "type": "text_completion",
#                     "placeholder": "Consider career expectations, relationship choices, values...",
#                     "patterns": "family_rules",
#                     "min_chars": 5,
#                     "clinical_insight": "Family system dynamics"
#                 }
#             },
#             "boundary_collapse": {
#                 34: {
#                     "text": "When did you learn that others' needs come before your own?",
#                     "type": "text_completion",
#                     "placeholder": "Think about early caretaking roles, family dynamics...",
#                     "patterns": "boundary_development",
#                     "min_chars": 5,
#                     "clinical_insight": "Boundary formation history"
#                 }
#             }
#         }

#     def _get_safety_questions(self):
#         """Safety assessment triggered by risk indicators"""
#         return {
#             "support_system": {
#                 35: {
#                     "text": "If you were in emotional crisis right now, you would:",
#                     "type": "single_choice",
#                     "options": [
#                         "Have multiple trusted people to reach out to",
#                         "Have one reliable person to contact",
#                         "Try to handle it alone first",
#                         "Not feel comfortable reaching out",
#                         "Have no one available"
#                     ],
#                     "risk_assessment": True,
#                     "weights": [0, 0, 1, 2, 3],
#                     "clinical_insight": "Crisis support system"
#                 }
#             },
#             "safety_planning": {
#                 36: {
#                     "text": "Do you have strategies for managing overwhelming emotions?",
#                     "type": "single_choice",
#                     "options": [
#                         "Yes, multiple effective strategies",
#                         "Some strategies that work",
#                         "Basic strategies but don't always help",
#                         "Few strategies, rarely effective",
#                         "No strategies - feel helpless"
#                     ],
#                     "risk_assessment": True,
#                     "weights": [0, 0, 1, 2, 3],
#                     "clinical_insight": "Emotional regulation capacity"
#                 }
#             }
#         }

#     def _get_hypnotic_responsiveness_questions(self):
#         """Hypnotic susceptibility assessment"""
#         return {
#             "hypnotic_profile": {
#                 37: {
#                     "text": "How do you typically process information most effectively?",
#                     "type": "single_choice",
#                     "options": [
#                         "Through visual imagery and pictures",
#                         "Through physical sensations and feelings",
#                         "Through auditory guidance and words",
#                         "Through logical understanding",
#                         "Through metaphorical and symbolic meaning"
#                     ],
#                     "patterns": "processing_style",
#                     "clinical_insight": "Representational system preference"
#                 }
#             },
#             "trance_experience": {
#                 38: {
#                     "text": "Have you experienced hypnotic or trance-like states before?",
#                     "type": "single_choice",
#                     "options": [
#                         "Frequently in meditation or relaxation",
#                         "Occasionally in daydreaming or flow states",
#                         "Rarely but open to experiencing it",
#                         "Never but curious to try",
#                         "Skeptical or apprehensive about it"
#                     ],
#                     "patterns": "trance_familiarity",
#                     "weights": [4, 3, 2, 1, 0],
#                     "clinical_insight": "Hypnotic experience level"
#                 }
#             }
#         }

#     # ---- Navigation and Response Logic ----
#     def _get_current_question_id(self):
#         answered = set(st.session_state.assessment_responses.keys())
        
#         # Core questions first
#         for qid in sorted(self.core_questions.keys()):
#             if qid not in answered:
#                 return qid
        
#         # Adaptive questions
#         for pool_name in st.session_state.adaptive_triggered:
#             pool = self.adaptive_pools.get(pool_name, {})
#             for qid in sorted(pool.keys()):
#                 if qid not in answered:
#                     return qid
        
#         # Safety questions
#         if st.session_state.risk_flags:
#             for pool in self.safety_questions.values():
#                 for qid in sorted(pool.keys()):
#                     if qid not in answered:
#                         return qid
        
#         # Hypnotic questions
#         for pool in self.hypnotic_questions.values():
#             for qid in sorted(pool.keys()):
#                 if qid not in answered:
#                     return qid
        
#         return None

#     def _estimate_total_questions(self):
#         base = len(self.core_questions)
#         adaptive = len(st.session_state.adaptive_triggered)
#         safety = len(st.session_state.risk_flags)
#         hypnotic = sum(len(pool) for pool in self.hypnotic_questions.values())
#         return base + adaptive + safety + hypnotic

#     def _estimate_time_remaining(self):
#         total_q = self._estimate_total_questions()
#         answered = len(st.session_state.assessment_responses)
#         remaining = max(0, total_q - answered)
#         return remaining * 1.25

#     def _get_question_by_id(self, q_id):
#         if q_id in self.core_questions:
#             return self.core_questions[q_id]
#         for pool in self.adaptive_pools.values():
#             if q_id in pool:
#                 return pool[q_id]
#         for pool in self.safety_questions.values():
#             if q_id in pool:
#                 return pool[q_id]
#         for pool in self.hypnotic_questions.values():
#             if q_id in pool:
#                 return pool[q_id]
#         return None

#     def _save_response(self, q_id, response, question, intensity=None):
#         st.session_state.assessment_responses[q_id] = {
#             'response': response,
#             'intensity': intensity,
#             'question_text': question['text'],
#             'question_type': question['type'],
#             'timestamp': datetime.now().isoformat()
#         }
        
#         if intensity:
#             st.session_state.intensity_responses[q_id] = intensity
        
#         # Process adaptive triggers
#         if 'adaptive_triggers' in question:
#             for trigger in question['adaptive_triggers']:
#                 if trigger not in st.session_state.adaptive_triggered:
#                     st.session_state.adaptive_triggered.append(trigger)
        
#         # Process risk assessment
#         if question.get('risk_assessment'):
#             weights = question.get('weights', [0])
#             if isinstance(response, str) and 'options' in question:
#                 try:
#                     option_index = question['options'].index(response)
#                     if option_index < len(weights) and weights[option_index] >= 2:
#                         risk_flag = f"risk_q_{q_id}"
#                         if risk_flag not in st.session_state.risk_flags:
#                             st.session_state.risk_flags.append(risk_flag)
#                 except (ValueError, IndexError):
#                     pass
        
#         # Process pattern scoring
#         if 'patterns' in question and question['patterns'] is not None:
#             patterns = question['patterns']
#             weights = question.get('weights', [1])
            
#             if isinstance(patterns, list) and isinstance(response, str) and 'options' in question:
#                 try:
#                     option_index = question['options'].index(response)
#                     if option_index < len(patterns) and patterns[option_index] is not None:
#                         pattern_id = patterns[option_index]
#                         weight = weights[option_index] if option_index < len(weights) else 1
#                         if intensity:
#                             weight *= (intensity / 5.0)
                        
#                         if pattern_id in st.session_state.pattern_scores:
#                             st.session_state.pattern_scores[pattern_id] += weight
#                         else:
#                             st.session_state.pattern_scores[pattern_id] = weight
#                 except (ValueError, IndexError):
#                     pass
#             elif isinstance(patterns, (int, str)):
#                 weight = weights[0] if weights else 1
#                 if intensity:
#                     weight *= (intensity / 5.0)
                
#                 if patterns in st.session_state.pattern_scores:
#                     st.session_state.pattern_scores[patterns] += weight
#                 else:
#                     st.session_state.pattern_scores[patterns] = weight

#     def _advance_question(self):
#         st.session_state.current_question += 1

#     def _go_back(self):
#         if st.session_state.current_question > 1:
#             st.session_state.current_question -= 1
#             if st.session_state.assessment_responses:
#                 last_key = max(st.session_state.assessment_responses.keys())
#                 del st.session_state.assessment_responses[last_key]
#                 if last_key in st.session_state.intensity_responses:
#                     del st.session_state.intensity_responses[last_key]

#     def _complete_assessment(self):
#         st.session_state.assessment_completed = True
        
#         dominant_pattern = None
#         if st.session_state.pattern_scores:
#             dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
#         st.session_state.assessment_results = {
#             'pattern_scores': dict(st.session_state.pattern_scores),
#             'dominant_pattern': dominant_pattern,
#             'risk_flags': st.session_state.risk_flags,
#             'completion_timestamp': datetime.now().isoformat(),
#             'total_questions_answered': len(st.session_state.assessment_responses),
#             'adaptive_paths_triggered': st.session_state.adaptive_triggered,
#             'intensity_data': dict(st.session_state.intensity_responses),
#             'completion_rate': len(st.session_state.assessment_responses) / self._estimate_total_questions() if self._estimate_total_questions() > 0 else 1.0
#         }
#         st.rerun()

#     # ---- Rendering Functions ----
#     def render(self):
#         apply_clinical_styles()
#         self._render_header()
        
#         if not st.session_state.contact_provided:
#             if not st.session_state.assessment_completed:
#                 self._render_current_question()
#             else:
#                 self._render_contact_form()
#         else:
#             self._render_results()

#     def _render_header(self):
#         st.markdown("<h1 style='text-align: center;'>Behavioral Pattern Assessment</h1>", unsafe_allow_html=True)
        
#         if not st.session_state.assessment_completed:
#             total_q = self._estimate_total_questions()
#             time_remaining = self._estimate_time_remaining()
#             st.info(f"Identify your unique neural and behavioral patterns to enable targeted, rapid-change hypnotherapy. Estimated time: {time_remaining:.0f} minutes.")

#     def _render_current_question(self):
#         current_q_id = self._get_current_question_id()
#         if current_q_id is None:
#             self._complete_assessment()
#             return
            
#         question = self._get_question_by_id(current_q_id)
#         if not question:
#             st.error("Question configuration error")
#             return

#         total_questions = self._estimate_total_questions()
#         completed = len(st.session_state.assessment_responses)
#         progress = completed / total_questions if total_questions > 0 else 0
#         time_remaining = self._estimate_time_remaining()

#         st.markdown(f"""
#         <div class="progress-container">
#             <span><strong>Question {completed + 1} of {total_questions}</strong></span>
#             <div class="progress-bar">
#                 <div class="progress-fill" style="width: {progress * 100}%"></div>
#             </div>
#             <span><strong>{int(progress * 100)}%</strong></span>
#         </div>
#         <div class="time-estimate">About {time_remaining:.0f} minutes remaining</div>
#         """, unsafe_allow_html=True)

#         st.markdown(f"### {question['text']}")
        
#         # if 'clinical_insight' in question:
#         #     with st.expander("Clinical Context", expanded=False):
#         #         st.markdown(f"**Purpose:** {question['clinical_insight']}")

#         self._handle_response_types(current_q_id, question)
#         self._render_navigation(current_q_id)

#     def _handle_response_types(self, q_id, question):
#         q_type = question['type']
        
#         if q_type == 'single_choice':
#             for i, option in enumerate(question['options']):
#                 if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
#                     self._save_response(q_id, option, question)
#                     self._advance_question()
#                     st.rerun()
        
#         elif q_type == 'single_choice_with_intensity':
#             selection_key = f"selected_option_{q_id}"
            
#             for i, option in enumerate(question['options']):
#                 if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
#                     st.session_state[selection_key] = option
#                     st.rerun()
            
#             if selection_key in st.session_state:
#                 selected_option = st.session_state[selection_key]
#                 st.success(f"Selected: {selected_option}")
                
#                 st.markdown("**How intense is this experience for you?**")
#                 intensity = st.select_slider(
#                     "Intensity level:",
#                     options=[1, 2, 3, 4, 5, 6, 7],
#                     format_func=lambda x: f"{x}/7",
#                     value=4,
#                     key=f"q_{q_id}_intensity"
#                 )
                
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.caption("1 = Very mild")
#                 with col2:
#                     st.caption("7 = Extremely intense")
                
#                 if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                     self._save_response(q_id, selected_option, question, intensity)
#                     if selection_key in st.session_state:
#                         del st.session_state[selection_key]
#                     self._advance_question()
#                     st.rerun()
                    
#         elif q_type == 'multi_select_weighted':
#             max_sel = question.get('max_selections', len(question['options']))
#             selected = st.multiselect(
#                 "Select all that apply:",
#                 question['options'],
#                 key=f"q_{q_id}_multi",
#                 max_selections=max_sel
#             )
            
#             if selected:
#                 st.markdown("**Rate the intensity of each selected emotion:**")
#                 intensities = {}
#                 for emotion in selected:
#                     intensities[emotion] = st.select_slider(
#                         f"{emotion}:",
#                         options=[1, 2, 3, 4, 5, 6, 7],
#                         format_func=lambda x: f"{x}/7",
#                         value=4,
#                         key=f"q_{q_id}_{emotion.replace('/', '_')}_intensity"
#                     )
                
#                 if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                     weighted_response = {emotion: intensities[emotion] for emotion in selected}
#                     self._save_response(q_id, weighted_response, question)
#                     self._advance_question()
#                     st.rerun()
                    
#         elif q_type == 'text_completion':
#             min_chars = question.get('min_chars', 5)
#             response = st.text_area(
#                 "Your response:",
#                 placeholder=question.get('placeholder', 'Please provide your response...'),
#                 key=f"q_{q_id}_text",
#                 height=120
#             )
            
#             char_count = len(response.strip())
#             if char_count > 0:
#                 sufficient = char_count >= min_chars
#                 color_class = "sufficient" if sufficient else "insufficient"
#                 st.markdown(f"<div class='char-counter {color_class}'>{char_count}/{min_chars} characters minimum</div>", unsafe_allow_html=True)
            
#             if char_count >= min_chars:
#                 if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                     self._save_response(q_id, response.strip(), question)
#                     self._advance_question()
#                     st.rerun()
#             elif char_count > 0:
#                 st.info(f"Please provide at least {min_chars - char_count} more characters for a complete response.")
                    
#         elif q_type == 'scale_7':
#             labels = question.get('labels', ['Low', 'High'])
#             value = st.select_slider(
#                 "Rate your experience:",
#                 options=[1, 2, 3, 4, 5, 6, 7],
#                 format_func=lambda x: f"{x}/7",
#                 value=4,
#                 key=f"q_{q_id}_scale"
#             )
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.caption(f"1 = {labels[0]}")
#             with col2:
#                 st.caption(f"7 = {labels[1]}")
                
#             if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                 self._save_response(q_id, value, question)
#                 self._advance_question()
#                 st.rerun()

#     def _render_navigation(self, current_q_id):
#         col1, col2, col3 = st.columns([1, 2, 1])
        
#         with col1:
#             if len(st.session_state.assessment_responses) > 0:
#                 if st.button("← Back", key="nav_back", use_container_width=True):
#                     self._go_back()
#                     st.rerun()
                    
#         with col2:
#             answered_count = len(st.session_state.assessment_responses)
#             total_count = self._estimate_total_questions()
#             st.markdown(f"""
#             <div style="text-align: center; padding: 0.25rem; color: #556D7A; font-size: 0.8rem;">
#                 <strong>{answered_count}/{total_count}</strong> completed
#             </div>
#             """, unsafe_allow_html=True)
            
#         with col3:
#             if st.button("Skip", key="nav_skip", use_container_width=True):
#                 skip_question = {"patterns": None, "weights": [0], "text": "Skipped", "type": "skip"}
#                 self._save_response(current_q_id, "Skipped", skip_question)
#                 self._advance_question()
#                 st.rerun()

#     def _render_contact_form(self):
#         st.markdown("### Assessment Complete")
#         st.success("Your personalized behavioral analysis is ready!")
        
#         results = st.session_state.assessment_results
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("Questions", results['total_questions_answered'], "Completed")
#         with col2:
#             st.metric("Patterns", len(results.get('pattern_scores', {})), "Identified")
#         with col3:
#             completion_rate = results.get('completion_rate', 1.0)
#             st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")

#         st.markdown("**Provide your details to receive your comprehensive behavioral pattern analysis:**")
        
#         with st.form("contact_form"):
#             name = st.text_input("Full Name*", placeholder="Your full name")
#             email = st.text_input("Email*", placeholder="your@email.com")
#             phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
#             urgency = st.selectbox(
#                 "How urgent is addressing this pattern?*",
#                 ["Select urgency level...", "Extremely urgent - significantly impacting life", 
#                  "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
#                  "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
#             )
            
#             concern = st.text_area(
#                 "What brought you to this assessment?*",
#                 placeholder="Brief description of what motivated you to take this assessment...",
#                 height=100
#             )
            
#             next_step = st.selectbox(
#                 "Preferred next step:*",
#                 ["Select your preference...", "Schedule free consultation call", 
#                  "Information about transformation packages", "Receive analysis and recommendations first", 
#                  "Connect with clinical team directly"]
#             )
            
#             marketing_consent = st.checkbox(
#                 "I consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
#             )
            
#             submitted = st.form_submit_button("Get My Personalized Analysis", type="primary", use_container_width=True)

#             if submitted:
#                 errors = []
#                 if not name.strip(): 
#                     errors.append("Name is required")
#                 if not email.strip(): 
#                     errors.append("Email is required")
#                 elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#                     errors.append("Valid email address is required")
#                 if not concern.strip(): 
#                     errors.append("Please describe what brought you here")
#                 if urgency == "Select urgency level...": 
#                     errors.append("Please select urgency level")
#                 if next_step == "Select your preference...": 
#                     errors.append("Please select your preferred next step")
#                 if not marketing_consent:
#                     errors.append("Please consent to follow-up communications to receive your results")
                
#                 if errors:
#                     for error in errors:
#                         st.error(f"❌ {error}")
#                 else:
#                     # Save contact info
#                     st.session_state.contact_info = {
#                         'name': name.strip(),
#                         'email': email.strip(),
#                         'phone': phone.strip(),
#                         'urgency': urgency,
#                         'primary_concern': concern.strip(),
#                         'next_step': next_step,
#                         'marketing_consent': marketing_consent,
#                         'timestamp': datetime.now().isoformat()
#                     }
                    
#                     # FIXED: Build properly structured assessment data for email handler
#                     # Ensure all data is in the expected locations
#                     enhanced_assessment_results = {
#                         **st.session_state.get('assessment_results', {}),
#                         'risk_flags': st.session_state.get('risk_flags', []),
#                         'adaptive_paths_triggered': st.session_state.get('adaptive_triggered', []),
#                         'pattern_scores': st.session_state.get('pattern_scores', {}),
#                         'total_questions_answered': len(st.session_state.get('assessment_responses', {})),
#                         'completion_rate': st.session_state.get('assessment_results', {}).get('completion_rate', 1.0)
#                     }
                    
#                     assessment_data = {
#                         'contact_info': st.session_state.contact_info,
#                         'assessment_results': enhanced_assessment_results,
#                         'assessment_responses': st.session_state.get('assessment_responses', {}),
#                         'intensity_responses': st.session_state.get('intensity_responses', {}),
#                         'adaptive_triggered': st.session_state.get('adaptive_triggered', []),
#                         'risk_flags': st.session_state.get('risk_flags', []),
#                         'pattern_scores': st.session_state.get('pattern_scores', {}),
#                         'start_time': st.session_state.get('start_time'),
#                         'completion_timestamp': datetime.now().isoformat()
#                     }
                    
#                     # Send comprehensive clinical assessment email
#                     try:
#                         from utils.email_handler import send_clinical_assessment_results
                        
#                         print(f"[DEBUG] Assessment data structure:")
#                         print(f"[DEBUG] - Contact info keys: {list(assessment_data['contact_info'].keys())}")
#                         print(f"[DEBUG] - Assessment results keys: {list(assessment_data['assessment_results'].keys())}")
#                         print(f"[DEBUG] - Risk flags count: {len(assessment_data['risk_flags'])}")
#                         print(f"[DEBUG] - Pattern scores count: {len(assessment_data['pattern_scores'])}")
#                         print(f"[DEBUG] - Responses count: {len(assessment_data['assessment_responses'])}")
                        
#                         email_success = send_clinical_assessment_results(assessment_data)
                        
#                         if email_success:
#                             st.success("✅ Assessment completed and clinical team notified!")
#                             st.info("📧 Your detailed analysis has been sent to our clinical team for review.")
#                         else:
#                             st.warning("⚠️ Assessment saved, but email notification failed. Our team will still receive your results.")
#                     except ImportError as e:
#                         st.error(f"📋 Import error: {e}")
#                         st.info("Assessment completed! Our clinical team will review your results.")
#                     except Exception as e:
#                         st.error(f"❌ Email error: {str(e)}")
#                         import traceback
#                         st.text("Debug trace:")
#                         st.text(traceback.format_exc())
                    
#                     st.session_state.contact_provided = True
#                     st.rerun()

    
#     def _render_results(self):
#         st.markdown("## Your Behavioral Pattern Analysis")
        
#         contact_info = st.session_state.get('contact_info', {})
#         st.success(f"Thank you, {contact_info.get('name', 'there')}! Your comprehensive analysis has been generated.")
        
#         results = st.session_state.assessment_results
        
#         col1, col2, col3, col4 = st.columns(4)
#         with col1:
#             st.metric("Questions", results['total_questions_answered'], "Answered")
#         with col2:
#             patterns_count = len(results.get('pattern_scores', {}))
#             st.metric("Patterns", patterns_count, "Detected")
#         with col3:
#             risk_count = len(results.get('risk_flags', []))
#             st.metric("Risk Factors", risk_count, "Identified")
#         with col4:
#             completion_rate = results.get('completion_rate', 1.0)
#             st.metric("Completeness", f"{completion_rate*100:.0f}%", "Assessment")

#         self._render_clinical_analysis_section()

#         st.markdown("### Your Next Steps")
        
#         next_step = contact_info.get('next_step', '')
#         urgency = contact_info.get('urgency', '')
        
#         if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
#             st.warning("⚠️ **Priority Contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
#         if 'consultation' in next_step.lower():
#             st.info("📅 **Consultation Scheduling**: We'll contact you within 48 hours to schedule your free consultation call.")
#         elif 'package' in next_step.lower():
#             st.success("📋 **Transformation Packages**: We'll send you detailed information about our personalized programs.")
#         elif 'analysis' in next_step.lower():
#             st.info("📊 **Analysis First**: We'll email your detailed analysis and specific recommendations.")
#         else:
#             st.info("🤝 **Clinical Team Contact**: Our team will reach out with personalized next steps.")
        
#         st.markdown("""
#         **What happens next:**

#         1. **Clinical Review** (24-48 hours): Licensed therapist analyzes your responses
#         2. **Personalized Protocol** (48-72 hours): Custom hypnotherapy approach designed for your patterns  
#         3. **Initial Contact** (48-72 hours): We'll reach out via your preferred method
#         4. **Transformation Planning** (1 week): Develop your individualized program
        
#         **Questions?** Reply to any email from us or contact our clinical team directly.
#         """)

#     def _render_clinical_analysis_section(self):
#         st.markdown("### Clinical Pattern Analysis")
        
#         if PAYWALL_AVAILABLE:
#             try:
#                 paywall = create_clinical_paywall()
#                 assessment_data = {
#                     'assessment_results': st.session_state.assessment_results,
#                     'assessment_responses': st.session_state.assessment_responses,
#                     'intensity_responses': st.session_state.intensity_responses,
#                 }
#                 contact_info = st.session_state.get('contact_info', {})
#                 assessment_data.update(contact_info)
                
#                 if paywall.check_payment_status():
#                     paywall.render_premium_analysis(assessment_data)
#                 else:
#                     self._render_analysis_preview()
#                     with st.expander("🔓 Unlock Complete Clinical Analysis", expanded=True):
#                         paywall.render_paywall_interface(assessment_data)
#             except Exception as e:
#                 st.error(f"Error loading premium analysis: {str(e)}")
#                 self._render_analysis_preview()
#         else:
#             st.info("💡 **Premium Analysis Available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
#             self._render_analysis_preview()

#     def _render_analysis_preview(self):
#         results = st.session_state.assessment_results
#         pattern_scores = results.get('pattern_scores', {})
        
#         if pattern_scores:
#             st.markdown("**🎯 Your Top Behavioral Patterns:**")
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
#             descriptions = {
#                 1: "Difficulty accepting or maintaining positive emotional states",
#                 2: "Recurring conflicts and power struggles in relationships", 
#                 3: "Default skepticism and difficulty trusting others' intentions",
#                 4: "Black-and-white thinking patterns that limit options",
#                 5: "Self-worth tied to productivity and achievement",
#                 6: "Inconsistent sense of identity across different contexts",
#                 7: "Prioritizing others' needs while neglecting self-care",
#                 8: "Life choices driven by family expectations",
#                 9: "Context-dependent loss of personal boundaries"
#             }
            
#             for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
#                 pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
#                 strength = "High" if score >= 5 else "Moderate" if score >= 3 else "Mild"
                
#                 st.markdown(f"**{i+1}. {pattern_name}** - *{strength} intensity pattern detected*")
                
#                 if pattern_id in descriptions:
#                     st.caption(descriptions[pattern_id])
            
#             if len(sorted_patterns) > 3:
#                 remaining = len(sorted_patterns) - 3
#                 st.write(f"*Plus {remaining} additional patterns identified...*")
        
#         risk_count = len(results.get('risk_flags', []))
#         if risk_count > 0:
#             st.markdown(f"**⚠️ Clinical Considerations:** {risk_count} factors requiring specialized approach")
        
#         st.info("**Complete analysis includes:** Detailed pattern breakdowns, root cause analysis, personalized hypnotherapy protocol, session planning, and progress tracking recommendations.")


# # ---- Main Application Class ----
# class AssessPage:
#     """Main application wrapper maintaining compatibility with original interface"""
    
#     def __init__(self):
#         self.assessment = ComprehensiveBehavioralAssessment()
    
#     def render(self):
#         self.assessment.render()


# # ---- Page Factory Function ----
# def create_assess_page():
#     """Factory function to create the assessment page"""
#     return AssessPage()


# # ---- Helper Functions ----
# def get_assessment_summary():
#     """Get current assessment summary"""
#     if 'assessment_results' in st.session_state:
#         return st.session_state.assessment_results
#     return None

# def get_pattern_scores():
#     """Get current pattern scores"""
#     if 'pattern_scores' in st.session_state:
#         return st.session_state.pattern_scores
#     return {}

# def reset_assessment():
#     """Reset assessment state"""
#     keys_to_reset = [
#         'assessment_responses', 'current_question', 'question_sequence',
#         'adaptive_triggered', 'assessment_completed', 'contact_provided',
#         'assessment_results', 'pattern_scores', 'risk_flags', 'intensity_responses'
#     ]
#     for key in keys_to_reset:
#         if key in st.session_state:
#             del st.session_state[key]

# def export_assessment_data():
#     """Export complete assessment data"""
#     if 'assessment_responses' not in st.session_state:
#         return None
    
#     return {
#         'responses': st.session_state.assessment_responses,
#         'pattern_scores': st.session_state.get('pattern_scores', {}),
#         'intensity_data': st.session_state.get('intensity_responses', {}),
#         'adaptive_triggered': st.session_state.get('adaptive_triggered', []),
#         'risk_flags': st.session_state.get('risk_flags', []),
#         'results': st.session_state.get('assessment_results', {}),
#         'contact_info': st.session_state.get('contact_info', {}),
#         'completion_timestamp': datetime.now().isoformat()
#     }


# # ---- Main Execution ----
# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Behavioral Pattern Assessment",
#         page_icon="🧠",
#         layout="centered",
#         initial_sidebar_state="collapsed"
#     )
    
#     assessment_page = create_assess_page()
#     assessment_page.render()








# Enhanced Clinical Behavioral Pattern Assessment - Complete Redesign
# Comprehensive implementation with adaptive questioning and pattern detection
# Optimized for engagement, honesty, and complete behavioral mapping

import streamlit as st
from datetime import datetime
import re

# ---- Paywall Integration ----
try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False

# ---- Styling Functions ----
def apply_clinical_styles():
    """Apply expert clinical-grade styling with enhanced UX elements"""
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 0.75rem !important;
        padding-bottom: 0.75rem !important;
        max-width: 100% !important;
    }
    @media (min-width: 768px) {
        .main .block-container {
            max-width: 650px !important;
            margin: 0 auto;
        }
    }
    .stButton > button {
        width: 100% !important;
        margin-bottom: 0.25rem !important;
        padding: 0.6rem 1rem !important;
        text-align: left !important;
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 6px !important;
        color: #374151 !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        line-height: 1.3 !important;
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
    .progress-container {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        font-size: 0.75rem;
        font-weight: normal; 
        color: #556D7A;
        padding: 0.5rem;
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
    .time-estimate {
        font-size: 0.8rem;
        color: #64748b;
        text-align: center;
        margin-top: 0.5rem;
    }
    .char-counter {
        font-size: 0.8rem;
        margin-top: 0.5rem;
        text-align: right;
    }
    .char-counter.sufficient {
        color: #059669;
    }
    .char-counter.insufficient {
        color: #dc2626;
    }
    .pattern-hint {
        background: #f0f9ff;
        border-left: 3px solid #0ea5e9;
        padding: 0.5rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
        font-style: italic;
    }
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #4CA1A3 0%, #357a7c 100%);
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        margin: 20px auto;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .cta-button:hover {
        transform: translateY(-2px);
        text-decoration: none;
        color: white !important;
    }
    .text-center {
        text-align: center;
    }
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ---- Enhanced Assessment Class ----
class ComprehensiveBehavioralAssessment:
    """Clinical-grade behavioral pattern assessment with adaptive questioning flow"""
    
    def __init__(self):
        self._init_session_state()
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        self.patterns = {
            1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
            4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
            7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
        }
        
        # Question pools organized by phase
        self.engagement_questions = self._get_engagement_questions()
        self.trigger_mapping_questions = self._get_trigger_mapping_questions()
        self.pattern_specific_questions = self._get_pattern_specific_questions()
        self.integration_questions = self._get_integration_questions()

    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'current_phase': 'engagement',
            'phase_progress': {'engagement': 0, 'trigger_mapping': 0, 'pattern_specific': 0, 'integration': 0},
            'triggered_patterns': set(),
            'pattern_scores': {},
            'risk_flags': [],
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'start_time': datetime.now().isoformat(),
            'intensity_responses': {},
            'motivation_data': {},
            'trigger_chain': {},
            'response_chain': {},
            'adaptive_paths': []
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _get_engagement_questions(self):
        """Phase 1: Engagement & Initial Pattern Detection"""
        return {
            1: {
                "text": "What made you decide to explore hypnotherapy for this particular issue?",
                "type": "single_choice",
                "options": [
                    "I've tried other approaches without lasting success",
                    "I want faster results than traditional methods",
                    "Something about the subconscious mind approach appeals to me",
                    "Someone recommended it specifically for my type of issue",
                    "I'm curious but also skeptical about whether it will work"
                ],
                "pattern_triggers": {
                    0: [5], 1: [5], 2: [3], 3: [8], 4: [3]
                },
                "phase": "engagement"
            },
            2: {
                "text": "If this issue completely resolved, what would be different about your daily life?",
                "type": "text_completion",
                "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
                "min_chars": 5,
                "pattern_analysis": True,
                "keywords": {
                    "productivity": [5], "relationships": [2, 3, 6, 7], "peace": [1], 
                    "authentic": [6], "happy": [1], "control": [2, 4], "boundaries": [7, 9]
                },
                "phase": "engagement"
            },
            3: {
                "text": "How ready are you to completely let go of this pattern? (1-10 scale)",
                "type": "scale_10",
                "labels": ["Not ready at all", "Completely ready"],
                "follow_up_trigger": 7,  # If 7 or below, ask follow-up
                "phase": "engagement"
            },
            4: {
                "text": "When did this issue most recently show up?",
                "type": "single_choice",
                "options": [
                    "Today",
                    "Yesterday", 
                    "This week",
                    "Last week",
                    "I can't recall the last specific time"
                ],
                "pattern_triggers": {
                    4: [1, 6]  # Can't recall suggests normalization or compartmentalization
                },
                "phase": "engagement"
            },
            5: {
                "text": "This issue tends to show up more:",
                "type": "single_choice",
                "options": [
                    "At work or in professional settings",
                    "In family or close relationships",
                    "In social situations with acquaintances", 
                    "When I'm alone with my thoughts",
                    "Across all situations equally"
                ],
                "pattern_triggers": {
                    0: [5, 8], 1: [7, 8, 9], 2: [2, 3, 6], 3: [1], 4: [1, 4]
                },
                "phase": "engagement"
            }
        }

    def _get_trigger_mapping_questions(self):
        """Phase 2: Core Trigger Mapping"""
        return {
            6: {
                "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
                "type": "text_completion",
                "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
                "min_chars": 5,
                "trigger_analysis": True,
                "phase": "trigger_mapping"
            },
            7: {
                "text": "In that situation, what did you notice first?",
                "type": "single_choice",
                "options": [
                    "A physical sensation somewhere in my body",
                    "A specific thought or worry popping up",
                    "An emotional shift or feeling change",
                    "Something another person said or did",
                    "A change in the environment around me"
                ],
                "chain_mapping": "awareness_point",
                "phase": "trigger_mapping"
            },
            8: {
                "text": "When this pattern activates, the first physical sensation is usually:",
                "type": "single_choice_with_intensity",
                "options": [
                    "Chest tightness, racing heart, or breathing changes",
                    "Stomach drop, nausea, or digestive upset", 
                    "Muscle tension, jaw clenching, or physical rigidity",
                    "Hot/cold flashes, sweating, or temperature changes",
                    "Numbness, disconnection, or feeling 'outside yourself'",
                    "Restlessness, fidgeting, or urge to move/escape",
                    "Fatigue, heaviness, or sudden energy drain"
                ],
                "pattern_indicators": {
                    0: [1, 3, 4], 1: [1, 3, 4], 2: [2, 5], 3: [2, 5], 
                    4: [6, 9], 5: [2, 5], 6: [1, 7]
                },
                "chain_mapping": "physical_response",
                "phase": "trigger_mapping"
            },
            9: {
                "text": "What thought automatically appears when you feel that physical sensation?",
                "type": "text_completion",
                "placeholder": "The actual words that go through your mind - even if they seem harsh or unreasonable. What does your inner voice say?",
                "min_chars": 5,
                "pattern_keywords": {
                    "not good enough": [1], "fight": [2], "can't trust": [3], 
                    "either or": [4], "must do": [5], "can't be real": [6],
                    "others need": [7], "should": [8], "can't handle": [9]
                },
                "chain_mapping": "automatic_thought",
                "phase": "trigger_mapping"
            },
            10: {
                "text": "After that thought, you typically feel:",
                "type": "multi_select_weighted",
                "max_selections": 3,
                "options": [
                    "Anxious or worried", "Angry or frustrated", "Ashamed or embarrassed",
                    "Sad or defeated", "Guilty or self-blaming", "Overwhelmed or panicked",
                    "Numb or disconnected", "Confused or uncertain"
                ],
                "chain_mapping": "emotional_response",
                "phase": "trigger_mapping"
            },
            11: {
                "text": "When you feel that emotion at that intensity, you typically:",
                "type": "single_choice",
                "options": [
                    "Withdraw, avoid, or postpone dealing with it",
                    "Become more active, busy, or productive",
                    "Seek reassurance or validation from others",
                    "Become argumentative or defensive", 
                    "Try to control or fix the situation",
                    "Please others or put their needs first",
                    "Shut down emotionally or 'check out'",
                    "Analyze or overthink the situation"
                ],
                "pattern_mapping": {
                    0: [1, 4, 9], 1: [5], 2: [3, 7], 3: [2], 
                    4: [2, 5], 5: [7], 6: [6, 9], 7: [4, 5]
                },
                "chain_mapping": "behavioral_response",
                "phase": "trigger_mapping"
            },
            12: {
                "text": "Right after you respond that way, you usually feel:",
                "type": "single_choice",
                "options": [
                    "Temporary relief but underlying tension remains",
                    "More agitated or upset than before",
                    "Emotionally numb or disconnected",
                    "Guilty about how you handled it",
                    "Justified in your response",
                    "Confused about what just happened",
                    "Physically exhausted or drained"
                ],
                "chain_mapping": "immediate_consequence",
                "phase": "trigger_mapping"
            },
            13: {
                "text": "A few hours later, you're typically:",
                "type": "single_choice", 
                "options": [
                    "Have moved on and forgotten about it",
                    "Still replaying what happened",
                    "Planning how to avoid it next time",
                    "Angry at yourself for reacting that way",
                    "Feeling misunderstood by others involved",
                    "Resigned that this is just how things are"
                ],
                "pattern_reinforcement": {
                    1: [5], 2: [1, 4, 9], 3: [5], 4: [1], 5: [1]
                },
                "chain_mapping": "longer_term_impact",
                "phase": "trigger_mapping"
            }
        }

    def _get_pattern_specific_questions(self):
        """Phase 3: Adaptive Pattern-Specific Deep Dives"""
        return {
            # Pattern 1: Unhappiness Culture
            "pattern_1": {
                14: {
                    "text": "When something genuinely good happens to you, your first reaction is usually:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Pure enjoyment and celebration",
                        "Immediately looking for the catch or downside", 
                        "Feeling guilty or undeserving of good things",
                        "Minimizing its importance",
                        "Anxiety about when it will end"
                    ],
                    "weights": [0, 3, 3, 2, 2],
                    "pattern": 1
                },
                15: {
                    "text": "Growing up, the message about happiness in your family was:",
                    "type": "single_choice",
                    "options": [
                        "Happiness is natural and should be enjoyed",
                        "Happiness must be earned through hard work",
                        "Too much happiness leads to disappointment", 
                        "Other people's happiness comes first",
                        "Happiness is selfish or shallow"
                    ],
                    "weights": [0, 2, 3, 2, 3],
                    "pattern": 1
                },
                16: {
                    "text": "What would you lose if you allowed yourself to be genuinely happy?",
                    "type": "text_completion",
                    "placeholder": "Think about identity, relationships, what others might think, or what might change...",
                    "min_chars": 5,
                    "pattern": 1
                }
            },
            
            # Pattern 2: Power Struggles
            "pattern_2": {
                17: {
                    "text": "When someone disagrees with you, your nervous system:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stays curious about their perspective",
                        "Immediately activates into combat mode",
                        "Feels threatened or attacked",
                        "Shuts down to avoid confrontation",
                        "Searches for ways to prove them wrong"
                    ],
                    "weights": [0, 3, 2, 1, 3],
                    "pattern": 2
                },
                18: {
                    "text": "In your family growing up, disagreements typically:",
                    "type": "single_choice",
                    "options": [
                        "Were handled through calm discussion",
                        "Escalated into arguments or fights",
                        "Were avoided at all costs",
                        "Involved guilt, manipulation, or silent treatment",
                        "Had clear winners and losers"
                    ],
                    "weights": [0, 3, 2, 3, 4],
                    "pattern": 2
                },
                19: {
                    "text": "What are you most afraid would happen if you stopped fighting for your position?",
                    "type": "text_completion",
                    "placeholder": "Consider what you might lose, how others might treat you, or what might change...",
                    "min_chars": 5,
                    "pattern": 2
                }
            },
            
            # Pattern 3: Systematic Mistrust
            "pattern_3": {
                20: {
                    "text": "When meeting new people, you assume they:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Are generally well-intentioned",
                        "Are judging or evaluating you",
                        "Want something from you",
                        "Will eventually disappoint you",
                        "Are basically indifferent"
                    ],
                    "weights": [0, 2, 3, 3, 1],
                    "pattern": 3
                },
                21: {
                    "text": "When someone is unexpectedly kind to you, you:",
                    "type": "single_choice",
                    "options": [
                        "Feel grateful and warmed",
                        "Wonder what they want from you",
                        "Feel suspicious of their motives",
                        "Feel unworthy of their kindness",
                        "Barely notice or dismiss it"
                    ],
                    "weights": [0, 3, 3, 2, 1],
                    "pattern": 3
                },
                22: {
                    "text": "What's the worst thing that could happen if you trusted someone completely?",
                    "type": "text_completion",
                    "placeholder": "What specific betrayal, hurt, or loss do you fear most?",
                    "min_chars": 5,
                    "pattern": 3
                }
            },
            
            # Pattern 4: Separation/Division
            "pattern_4": {
                23: {
                    "text": "When facing important decisions, you typically:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "See multiple creative possibilities",
                        "Feel trapped between two impossible choices",
                        "Get paralyzed by perfectionist analysis",
                        "Create artificial deadlines or urgency",
                        "Defer to what others expect"
                    ],
                    "weights": [0, 2, 3, 2, 1],
                    "pattern": 4
                },
                24: {
                    "text": "Complete this sentence: 'If I don't choose perfectly, then...'",
                    "type": "text_completion",
                    "placeholder": "What catastrophic outcome do you imagine?",
                    "min_chars": 5,
                    "pattern": 4
                },
                25: {
                    "text": "What would become possible if you could embrace 'both/and' instead of 'either/or'?",
                    "type": "text_completion",
                    "placeholder": "Imagine having more options and flexibility in your choices...",
                    "min_chars": 5,
                    "pattern": 4
                }
            },
            
            # Pattern 5: Doing vs Being
            "pattern_5": {
                26: {
                    "text": "You feel most valuable when you're:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Simply existing as yourself",
                        "Accomplishing something significant",
                        "Being productive or busy",
                        "Helping others achieve their goals",
                        "Receiving recognition for your work"
                    ],
                    "weights": [0, 2, 3, 2, 2],
                    "pattern": 5
                },
                27: {
                    "text": "If you stopped being productive for a month, you'd worry that:",
                    "type": "text_completion",
                    "placeholder": "Complete the thought: you'd worry that others would think... or that you would...",
                    "min_chars": 5,
                    "pattern": 5
                },
                28: {
                    "text": "Who first taught you that your value depends on what you produce?",
                    "type": "text_completion",
                    "placeholder": "Think about early messages from family, school, or society...",
                    "min_chars": 5,
                    "pattern": 5
                }
            },
            
            # Pattern 6: Compartmentalized Authenticity
            "pattern_6": {
                29: {
                    "text": "Your personality tends to:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stay consistent across all situations",
                        "Shift significantly based on who you're with",
                        "Change between professional and personal settings",
                        "Adapt to what others seem to want",
                        "Feel fragmented or inconsistent"
                    ],
                    "weights": [0, 2, 2, 3, 4],
                    "pattern": 6
                },
                30: {
                    "text": "The 'real you' is:",
                    "type": "single_choice",
                    "options": [
                        "Pretty much what people see",
                        "Only visible to very close friends",
                        "Something you're still discovering",
                        "Different depending on the situation",
                        "Hidden to protect yourself"
                    ],
                    "weights": [0, 1, 2, 3, 3],
                    "pattern": 6
                },
                31: {
                    "text": "What would you risk losing if you showed up authentically everywhere?",
                    "type": "text_completion",
                    "placeholder": "Consider relationships, opportunities, safety, or acceptance you might lose...",
                    "min_chars": 5,
                    "pattern": 6
                }
            },
            
            # Pattern 7: Self-Sacrifice/Care Avoidance
            "pattern_7": {
                32: {
                    "text": "When it comes to your own needs versus others' needs:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "I naturally balance both",
                        "Others' needs usually come first",
                        "I feel guilty focusing on my own needs",
                        "I often don't even know what I need",
                        "Taking care of myself feels selfish"
                    ],
                    "weights": [0, 2, 3, 3, 4],
                    "pattern": 7
                },
                33: {
                    "text": "When someone offers to help you, you typically:",
                    "type": "single_choice",
                    "options": [
                        "Accept gratefully",
                        "Feel uncomfortable accepting",
                        "Immediately think of how to reciprocate",
                        "Worry about being a burden",
                        "Decline even when you need help"
                    ],
                    "weights": [0, 2, 2, 3, 3],
                    "pattern": 7
                },
                34: {
                    "text": "What would others lose if you started prioritizing your own wellbeing?",
                    "type": "text_completion",
                    "placeholder": "Think about who depends on your self-sacrifice and what they'd have to give up...",
                    "min_chars": 5,
                    "pattern": 7
                }
            },
            
            # Pattern 8: Inherited Missions
            "pattern_8": {
                35: {
                    "text": "Your major life goals are primarily:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Based on your own genuine desires",
                        "Influenced by family expectations",
                        "Meant to honor someone's sacrifices",
                        "Designed to prove your worth",
                        "A reaction against others' expectations"
                    ],
                    "weights": [0, 2, 3, 3, 2],
                    "pattern": 8
                },
                36: {
                    "text": "When you imagine disappointing your family:",
                    "type": "single_choice",
                    "options": [
                        "It doesn't significantly concern you",
                        "You feel guilty but would survive it",
                        "It feels like betraying their love",
                        "You worry about losing their approval",
                        "It's almost unthinkable"
                    ],
                    "weights": [0, 1, 3, 2, 4],
                    "pattern": 8
                },
                37: {
                    "text": "What would pursuing your own path cost your family relationships?",
                    "type": "text_completion",
                    "placeholder": "Consider how they might react, what they might lose, or how relationships might change...",
                    "min_chars": 5,
                    "pattern": 8
                }
            },
            
            # Pattern 9: Context-Dependent Weakness
            "pattern_9": {
                38: {
                    "text": "Your boundaries and limits:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stay pretty consistent across situations",
                        "Vary significantly based on who you're with",
                        "Disappear completely in certain contexts",
                        "Are stronger in some areas than others",
                        "Feel almost non-existent sometimes"
                    ],
                    "weights": [0, 2, 3, 2, 4],
                    "pattern": 9
                },
                39: {
                    "text": "There are certain people or situations where you:",
                    "type": "single_choice",
                    "options": [
                        "Stay true to your values",
                        "Become someone you don't recognize",
                        "Lose all sense of personal power",
                        "Can't access your usual strength",
                        "Feel completely overwhelmed"
                    ],
                    "weights": [0, 2, 3, 3, 4],
                    "pattern": 9
                },
                40: {
                    "text": "What is it about these specific contexts that overwhelms your usual coping?",
                    "type": "text_completion",
                    "placeholder": "Think about the people, environments, or dynamics that make you lose yourself...",
                    "min_chars": 5,
                    "pattern": 9
                }
            }
        }

    def _get_integration_questions(self):
        """Phase 4: Integration & Change Readiness"""
        return {
            41: {
                "text": "If you had to guess, this pattern might be trying to:",
                "type": "single_choice",
                "options": [
                    "Protect you from emotional pain",
                    "Keep you safe from rejection or judgment",
                    "Maintain some sense of control",
                    "Help you belong or fit in",
                    "Avoid disappointing important people",
                    "Ensure you're prepared for worst-case scenarios"
                ],
                "secondary_gain": True,
                "phase": "integration"
            },
            42: {
                "text": "What would need to be true for you to feel completely safe changing this pattern?",
                "type": "text_completion",
                "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
                "min_chars": 5,
                "safety_assessment": True,
                "phase": "integration"
            },
            43: {
                "text": "If you were transforming this pattern, your support system is:",
                "type": "single_choice",
                "options": [
                    "Strong - multiple people who'd encourage change",
                    "Moderate - some people who'd support you",
                    "Mixed - some would support, others might resist",
                    "Weak - mostly dealing with this alone",
                    "Unsure - haven't thought about who would support change"
                ],
                "support_assessment": True,
                "risk_weights": [0, 0, 1, 2, 1],
                "phase": "integration"
            },
            44: {
                "text": "When learning or changing, you respond best to:",
                "type": "single_choice",
                "options": [
                    "Direct, clear guidance and instructions",
                    "Gentle, permissive suggestions",
                    "Stories, metaphors, and imagery",
                    "Logical explanations and understanding",
                    "Collaborative exploration and discovery"
                ],
                "hypnotic_preference": True,
                "phase": "integration"
            },
            45: {
                "text": "Imagine you've completely transformed this pattern. What's the first thing you'd do that you can't do now?",
                "type": "text_completion",
                "placeholder": "Be specific about the first action, conversation, or decision you'd make...",
                "min_chars": 5,
                "outcome_visualization": True,
                "phase": "integration"
            }
        }

    # ---- Pattern Detection and Scoring ----
    def _analyze_text_for_patterns(self, text, keywords_dict):
        """Analyze text response for pattern indicators"""
        text_lower = text.lower()
        detected_patterns = set()
        
        for keyword, patterns in keywords_dict.items():
            if keyword in text_lower:
                detected_patterns.update(patterns)
        
        return detected_patterns

    def _update_pattern_scores(self, question_id, response, question):
        """Update pattern scores based on response"""
        # Handle different question types
        if question.get('pattern_triggers') and isinstance(response, str):
            if 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_triggers']:
                        patterns = question['pattern_triggers'][option_index]
                        for pattern in patterns:
                            self._add_pattern_score(pattern, 1.0)
                except (ValueError, IndexError):
                    pass
        
        elif question.get('pattern_mapping') and isinstance(response, str):
            if 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_mapping']:
                        patterns = question['pattern_mapping'][option_index]
                        for pattern in patterns:
                            self._add_pattern_score(pattern, 1.5)
                except (ValueError, IndexError):
                    pass
        
        elif question.get('pattern_keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['pattern_keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 2.0)
        
        elif question.get('keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 1.0)
        
        # Handle pattern-specific questions with weights
        if question.get('pattern') and question.get('weights'):
            pattern_id = question['pattern']
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(question['weights']):
                        weight = question['weights'][option_index]
                        if weight > 0:
                            self._add_pattern_score(pattern_id, weight)
                except (ValueError, IndexError):
                    pass

    def _add_pattern_score(self, pattern_id, score):
        """Add score to pattern with intensity multiplier if available"""
        if pattern_id in st.session_state.pattern_scores:
            st.session_state.pattern_scores[pattern_id] += score
        else:
            st.session_state.pattern_scores[pattern_id] = score

    def _check_adaptive_triggers(self, question_id, response, question):
        """Check if response triggers adaptive questioning"""
        # Trigger pattern-specific questions when scores reach threshold
        for pattern_id, score in st.session_state.pattern_scores.items():
            if score >= 3.0 and pattern_id not in st.session_state.triggered_patterns:
                st.session_state.triggered_patterns.add(pattern_id)
                st.session_state.adaptive_paths.append(f"pattern_{pattern_id}")

    def _save_response(self, q_id, response, question, intensity=None):
        """Save response and update scoring"""
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'intensity': intensity,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat(),
            'phase': question.get('phase', 'unknown')
        }
        
        if intensity:
            st.session_state.intensity_responses[q_id] = intensity
        
        # Update chain mapping for trigger sequence
        if question.get('chain_mapping'):
            st.session_state.trigger_chain[question['chain_mapping']] = response
        
        # Update pattern scores
        self._update_pattern_scores(q_id, response, question)
        
        # Check for adaptive triggers
        self._check_adaptive_triggers(q_id, response, question)
        
        # Update phase progress
        phase = question.get('phase', 'unknown')
        if phase in st.session_state.phase_progress:
            st.session_state.phase_progress[phase] += 1

    # ---- Question Navigation Logic ----
    def _get_next_question(self):
        """Determine next question based on current phase and responses"""
        answered = set(st.session_state.assessment_responses.keys())
        
        # Phase 1: Engagement (Questions 1-5)
        if st.session_state.current_phase == 'engagement':
            for q_id in range(1, 6):
                if q_id not in answered:
                    return q_id, self.engagement_questions[q_id]
            st.session_state.current_phase = 'trigger_mapping'
        
        # Phase 2: Trigger Mapping (Questions 6-13)
        if st.session_state.current_phase == 'trigger_mapping':
            for q_id in range(6, 14):
                if q_id not in answered:
                    return q_id, self.trigger_mapping_questions[q_id]
            st.session_state.current_phase = 'pattern_specific'
        
        # Phase 3: Pattern-Specific Questions
        if st.session_state.current_phase == 'pattern_specific':
            for pattern_id in st.session_state.triggered_patterns:
                pattern_key = f"pattern_{pattern_id}"
                if pattern_key in self.pattern_specific_questions:
                    pattern_questions = self.pattern_specific_questions[pattern_key]
                    for q_id, question in pattern_questions.items():
                        if q_id not in answered:
                            return q_id, question
            st.session_state.current_phase = 'integration'
        
        # Phase 4: Integration (Questions 41-45)
        if st.session_state.current_phase == 'integration':
            for q_id in range(41, 46):
                if q_id not in answered:
                    return q_id, self.integration_questions[q_id]
        
        return None, None

    def _estimate_total_questions(self):
        """Estimate total questions based on triggered patterns"""
        base_questions = 5 + 8 + 5  # engagement + trigger_mapping + integration
        pattern_questions = len(st.session_state.triggered_patterns) * 3  # 3 questions per pattern
        return base_questions + pattern_questions

    def _estimate_time_remaining(self):
        """Estimate remaining time"""
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        return remaining * 1.0  # 1 minute per question average

    # ---- Response Type Handlers ----
    def _handle_single_choice(self, q_id, question):
        """Handle single choice questions"""
        for i, option in enumerate(question['options']):
            if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                self._save_response(q_id, option, question)
                self._advance_question()
                st.rerun()

    def _handle_single_choice_with_intensity(self, q_id, question):
        """Handle single choice with intensity rating"""
        selection_key = f"selected_option_{q_id}"
        
        for i, option in enumerate(question['options']):
            if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                st.session_state[selection_key] = option
                st.rerun()
        
        if selection_key in st.session_state:
            selected_option = st.session_state[selection_key]
            st.success(f"Selected: {selected_option}")
            
            st.markdown("**How intense is this experience for you?**")
            intensity = st.select_slider(
                "Intensity level:",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: f"{x}/7",
                value=4,
                key=f"q_{q_id}_intensity"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption("1 = Very mild")
            with col2:
                st.caption("7 = Extremely intense")
            
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, selected_option, question, intensity)
                if selection_key in st.session_state:
                    del st.session_state[selection_key]
                self._advance_question()
                st.rerun()

    def _handle_multi_select_weighted(self, q_id, question):
        """Handle multi-select with intensity weighting"""
        max_sel = question.get('max_selections', len(question['options']))
        selected = st.multiselect(
            "Select all that apply:",
            question['options'],
            key=f"q_{q_id}_multi",
            max_selections=max_sel
        )
        
        if selected:
            st.markdown("**Rate the intensity of each selected emotion:**")
            intensities = {}
            for emotion in selected:
                safe_key = emotion.replace('/', '_').replace(' ', '_')
                intensities[emotion] = st.select_slider(
                    f"{emotion}:",
                    options=[1, 2, 3, 4, 5, 6, 7],
                    format_func=lambda x: f"{x}/7",
                    value=4,
                    key=f"q_{q_id}_{safe_key}_intensity"
                )
            
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                weighted_response = {emotion: intensities[emotion] for emotion in selected}
                self._save_response(q_id, weighted_response, question)
                self._advance_question()
                st.rerun()

    def _handle_text_completion(self, q_id, question):
        """Handle text completion questions"""
        min_chars = question.get('min_chars', 5)
        response = st.text_area(
            "Your response:",
            placeholder=question.get('placeholder', 'Please share your thoughts...'),
            key=f"q_{q_id}_text",
            height=120
        )
        
        char_count = len(response.strip())
        if char_count > 0:
            sufficient = char_count >= min_chars
            color_class = "sufficient" if sufficient else "insufficient"
            #st.markdown(f"<div class='char-counter {color_class}'>{char_count}/{min_chars} characters minimum</div>", unsafe_allow_html=True)
        
        if char_count >= min_chars:
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, response.strip(), question)
                self._advance_question()
                st.rerun()
        elif char_count > 0:
            st.info(f"Please provide at least {min_chars - char_count} more characters for a complete response.")

    def _handle_scale_10(self, q_id, question):
        """Handle 1-10 scale questions"""
        labels = question.get('labels', ['Low', 'High'])
        value = st.select_slider(
            "Rate your readiness:",
            options=list(range(1, 11)),
            format_func=lambda x: f"{x}/10",
            value=5,
            key=f"q_{q_id}_scale"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.caption(f"1 = {labels[0]}")
        with col2:
            st.caption(f"10 = {labels[1]}")
        
        # Show follow-up if score is low
        if value <= question.get('follow_up_trigger', 5):
            follow_up = st.text_input(
                "What would need to happen to make it a 10?",
                key=f"q_{q_id}_followup",
                placeholder="What would increase your readiness?"
            )
        else:
            follow_up = ""
        
        if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
            response_data = {'rating': value, 'follow_up': follow_up}
            self._save_response(q_id, response_data, question)
            self._advance_question()
            st.rerun()

    def _advance_question(self):
        """Move to next question"""
        st.session_state.current_question += 1

    def _go_back(self):
        """Go back one question"""
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
                if last_key in st.session_state.intensity_responses:
                    del st.session_state.intensity_responses[last_key]

    def _complete_assessment(self):
        """Complete the assessment and prepare results"""
        st.session_state.assessment_completed = True
        
        # Determine dominant pattern
        dominant_pattern = None
        if st.session_state.pattern_scores:
            dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
        # Compile results
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': dominant_pattern,
            'triggered_patterns': list(st.session_state.triggered_patterns),
            'risk_flags': st.session_state.risk_flags,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'adaptive_paths_triggered': st.session_state.adaptive_paths,
            'intensity_data': dict(st.session_state.intensity_responses),
            'trigger_chain': dict(st.session_state.trigger_chain),
            'phase_completion': dict(st.session_state.phase_progress),
            'completion_rate': len(st.session_state.assessment_responses) / self._estimate_total_questions() if self._estimate_total_questions() > 0 else 1.0
        }
        st.rerun()

    # ---- Rendering Functions ----
    def render(self):
        apply_clinical_styles()
        self._render_header()
        
        if not st.session_state.contact_provided:
            if not st.session_state.assessment_completed:
                self._render_current_question()
            else:
                self._render_contact_form()
        else:
            self._render_results()

    def _render_header(self):
        if not st.session_state.assessment_completed:
            time_remaining = self._estimate_time_remaining()
            st.info(f"Understanding **your unique behavioral patterns** is the key to **targeted, effective hypnotherapy** that brings rapid, lasting change. This assessment takes about {time_remaining:.0f} minutes to complete.")

        st.markdown("<h2 style='text-align: center;'>Behavioral pattern assessment</h1>", unsafe_allow_html=True)

    def _render_current_question(self):
        """Render the current question with progress tracking"""
        q_id, question = self._get_next_question()
        
        if q_id is None:
            self._complete_assessment()
            return
        
        if not question:
            st.error("Question configuration error")
            return

        # Progress tracking
        total_questions = self._estimate_total_questions()
        completed = len(st.session_state.assessment_responses)
        progress = completed / total_questions if total_questions > 0 else 0
        time_remaining = self._estimate_time_remaining()

        st.markdown(f"""
        <div class="progress-container">
            <span><strong>Question {completed + 1} of {total_questions}</strong></span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span><strong>{int(progress * 100)}%</strong></span>
        </div>
        <div class="time-estimate"> ~ {time_remaining:.0f} minutes remaining</div>
        """, unsafe_allow_html=True)

        # Question display
        st.markdown(f"### {question['text']}")
        
        # Show pattern detection hints for engaged users
        if completed > 5 and st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
            if top_pattern[1] >= 2.0:
                pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
                # st.markdown(f"""
                # <div class="pattern-hint">
                # Pattern emerging: {pattern_name} - this helps us customize your approach
                # </div>
                # """, unsafe_allow_html=True)

        # Handle different question types
        q_type = question['type']
        if q_type == 'single_choice':
            self._handle_single_choice(q_id, question)
        elif q_type == 'single_choice_with_intensity':
            self._handle_single_choice_with_intensity(q_id, question)
        elif q_type == 'multi_select_weighted':
            self._handle_multi_select_weighted(q_id, question)
        elif q_type == 'text_completion':
            self._handle_text_completion(q_id, question)
        elif q_type == 'scale_10':
            self._handle_scale_10(q_id, question)

        self._render_navigation(q_id)

    def _render_navigation(self, current_q_id):
        """Render navigation controls"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if len(st.session_state.assessment_responses) > 0:
                if st.button("← Back", key="nav_back", use_container_width=True):
                    self._go_back()
                    st.rerun()
        
        with col2:
            answered_count = len(st.session_state.assessment_responses)
            total_count = self._estimate_total_questions()
            st.markdown(f"""
            <div style="text-align: center; padding: 0.25rem; color: #556D7A; font-size: 0.8rem;">
                <strong>{answered_count}/{total_count}</strong> completed
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            if st.button("Skip", key="nav_skip", use_container_width=True):
                skip_question = {"text": "Skipped", "type": "skip", "phase": "skip"}
                self._save_response(current_q_id, "Skipped", skip_question)
                self._advance_question()
                st.rerun()

    def _generate_behavioral_sequence_analysis(self):
        """Generate comprehensive behavioral sequence mapping for clinical email"""
        trigger_chain = st.session_state.get('trigger_chain', {})
        responses = st.session_state.get('assessment_responses', {})
        intensity_responses = st.session_state.get('intensity_responses', {})
        
        # Build comprehensive sequence analysis
        sequence_analysis = """
╔══════════════════════════════════════════════════════════════╗
║            COMPLETE BEHAVIORAL SEQUENCE MAPPING             ║
╚══════════════════════════════════════════════════════════════╝

🎯 TRIGGER (Awareness Point)
"""
        
        # Extract trigger information
        trigger_info = trigger_chain.get('awareness_point', 'Not captured')
        if trigger_info != 'Not captured':
            sequence_analysis += f"""
Captured: "{trigger_info}"

Clinical Notes:
- Trigger type: {self._analyze_trigger_type(trigger_info)}
- Activation pattern: {self._analyze_activation_pattern(trigger_info)}
- Environmental factors: {self._extract_environmental_factors(responses)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: Specific trigger identification needed
Clinical Impact: Session 1 priority - complete trigger mapping
"""
    
        # Physical Response Analysis
        sequence_analysis += """

💓 PHYSICAL RESPONSE
"""
        
        physical_response = trigger_chain.get('physical_response', 'Not captured')
        if physical_response != 'Not captured':
            intensity = self._get_response_intensity('physical_response')
            sequence_analysis += f"""
Captured: "{physical_response}"

Clinical Analysis:
- Somatic location: {self._analyze_somatic_location(physical_response)}
- Activation system: {self._analyze_activation_system(physical_response)}
- Intensity level: {intensity}/7
- Clinical significance: {self._get_somatic_significance(physical_response)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: Physical sensation mapping needed
Clinical Impact: Essential for somatic intervention design
"""
    
        # Automatic Thought Analysis
        sequence_analysis += """

💭 AUTOMATIC THOUGHT
"""
        
        automatic_thought = trigger_chain.get('automatic_thought', 'Not captured')
        if automatic_thought != 'Not captured' and automatic_thought != 'Skipped':
            sequence_analysis += f"""
Captured: "{automatic_thought}"

Clinical Analysis:
- Cognitive distortion type: {self._analyze_cognitive_distortion(automatic_thought)}
- Core belief indicator: {self._extract_core_belief_from_thought(automatic_thought)}
- Therapeutic target: {self._get_thought_intervention_target(automatic_thought)}
- Language pattern: {self._analyze_language_pattern(automatic_thought)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: The specific automatic thoughts that occur between physical sensation and behavioral response
Clinical Impact: This gap needs filling in Session 1 for complete intervention mapping
"""
    
        # Emotional Response Analysis
        sequence_analysis += """

❤️ EMOTIONAL RESPONSE
"""
        
        emotional_response = trigger_chain.get('emotional_response', 'Not captured')
        if emotional_response != 'Not captured':
            if isinstance(emotional_response, dict):
                emotions_list = [f"{emotion} (intensity: {intensity}/7)" for emotion, intensity in emotional_response.items()]
                emotions_text = ", ".join(emotions_list)
            else:
                emotions_text = str(emotional_response)
                
            sequence_analysis += f"""
Captured: {emotions_text}

Clinical Analysis:
- Emotional constellation: {self._analyze_emotional_constellation(emotional_response)}
- Regulation capacity: {self._assess_regulation_capacity(emotional_response)}
- Intervention approach: {self._get_emotional_intervention(emotional_response)}
"""
        else:
            sequence_analysis += """
Status: PARTIALLY CAPTURED - implied through consequences
Inferred from consequences: Agitation, upset, possibly anxiety
Missing specifics: Exact emotions, intensity levels, emotional progression
"""
    
        # Behavioral Response Analysis
        sequence_analysis += """

🏃 BEHAVIORAL RESPONSE
"""
        
        behavioral_response = trigger_chain.get('behavioral_response', 'Not captured')
        if behavioral_response != 'Not captured':
            sequence_analysis += f"""
Captured: "{behavioral_response}"

Clinical Analysis:
- Response pattern: {self._analyze_behavioral_pattern(behavioral_response)}
- Function analysis: {self._analyze_behavioral_function(behavioral_response)}
- Pattern fit: {self._assess_pattern_alignment(behavioral_response)}
- Intervention point: {self._get_behavioral_intervention_point(behavioral_response)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: Specific behavioral response to emotional activation
Clinical Impact: Cannot design behavioral intervention without this data
"""
    
        # Immediate Consequences
        sequence_analysis += """

⚡ IMMEDIATE CONSEQUENCES
"""
        
        immediate_consequence = trigger_chain.get('immediate_consequence', 'Not captured')
        if immediate_consequence != 'Not captured':
            sequence_analysis += f"""
Captured: "{immediate_consequence}"

Clinical Analysis:
- Consequence type: {self._analyze_consequence_type(immediate_consequence)}
- Reinforcement pattern: {self._analyze_reinforcement_pattern(immediate_consequence)}
- Intervention timing: {self._get_consequence_intervention_timing(immediate_consequence)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: Immediate aftermath of behavioral response
Clinical Impact: Cannot assess pattern reinforcement cycle
"""
    
        # Longer-term Impact
        sequence_analysis += """

📈 LONGER-TERM IMPACT
"""
        
        longer_impact = trigger_chain.get('longer_term_impact', 'Not captured')
        if longer_impact != 'Not captured':
            sequence_analysis += f"""
Captured: "{longer_impact}"

Clinical Analysis:
- Pattern reinforcement: {self._analyze_pattern_reinforcement(longer_impact)}
- Cycle completion: {self._assess_cycle_completion(longer_impact)}
- Breaking point identification: {self._identify_breaking_points(longer_impact)}
"""
        else:
            sequence_analysis += """
Status: NOT CAPTURED in this assessment
Missing Data: Long-term pattern impact and reinforcement
Clinical Impact: Cannot assess full cycle for intervention design
"""
    
        # Add chain completion assessment
        completion_percentage = self._calculate_chain_completeness()
        sequence_analysis += f"""

📊 CHAIN COMPLETION ANALYSIS

Overall Chain Completeness: {completion_percentage}%

{"✅ SUFFICIENT for initial intervention design" if completion_percentage >= 60 else "❌ INSUFFICIENT - Session 1 must prioritize chain completion"}

Missing Chain Components for Session 1 Exploration:

🔍 Critical Gaps to Fill:
"""
        
        # Identify missing components
        missing_components = self._identify_missing_components()
        for component in missing_components:
            sequence_analysis += f"• {component}\n"
        
        if not missing_components:
            sequence_analysis += "• No critical gaps identified - proceed with intervention\n"
    
        sequence_analysis += """

Session 1 Chain Completion Protocol:

Priority Mapping Areas:
- Thought Content: "When you feel that physical sensation, what thought goes through your mind?"
- Emotional Bridge: "Between feeling the sensation and taking action, what emotions show up?"
- Trigger Details: "What specific situations or thoughts tend to set this whole sequence in motion?"

Chain Intervention Strategy:

Based on captured elements, primary intervention points would be:
- Somatic Interruption: Work with physical sensations as early warning system
- Cognitive Reframing: Address automatic thought patterns
- Emotional Regulation: Install healthy emotional processing
- Behavioral Redirection: Replace maladaptive responses with healthy alternatives
- Consequence Reframing: Address reinforcement patterns directly

Clinical Assessment Quality

Strengths:
- Clear behavioral sequence foundation established
- Physical response well-defined for somatic work
- Pattern scores provide intervention direction

Areas for Session 1 Completion:
- Complete missing chain elements
- Intensify successful components
- Validate sequence accuracy with client
"""
        
        return sequence_analysis

    def _render_contact_form(self):
        """Render contact form for results with enhanced clinical data"""
        st.markdown("### Assessment Complete!")
        st.success("Your comprehensive behavioral pattern analysis is ready!")
        
        results = st.session_state.assessment_results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "Answered")
        with col2:
            st.metric("Patterns", len(results.get('pattern_scores', {})), "Detected")
        with col3:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")
    
        st.markdown("**Enter your email to receive your personalized analysis and next steps:**")
        
        with st.form("contact_form"):
            # ONLY EMAIL IS MANDATORY
            email = st.text_input("Email*", placeholder="your@email.com")
            
            # ALL OTHER FIELDS ARE OPTIONAL
            name = st.text_input("Full name (optional)", placeholder="Your full name")
            phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
            urgency = st.selectbox(
                "How urgent is addressing this pattern? (optional)",
                ["Not specified", "Extremely urgent - significantly impacting life", 
                 "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
                 "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
            )
            
            concern = st.text_area(
                "What brought you to this assessment? (optional)",
                placeholder="Brief description of what motivated you to take this assessment...",
                height=100
            )
            
            next_step = st.selectbox(
                "Preferred next step (optional)",
                ["Not specified", "Schedule free consultation call", 
                 "Information about transformation packages", "Receive analysis and recommendations first", 
                 "Connect with clinical team directly"]
            )
            
            marketing_consent = st.checkbox(
                "I consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
            )
            
            submitted = st.form_submit_button("Get my personalized analysis", type="primary", use_container_width=True)
    
            if submitted:
                errors = []
                
                # ONLY EMAIL VALIDATION IS REQUIRED
                if not email.strip(): 
                    errors.append("Email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
                    errors.append("Valid email address is required")
                
                # MARKETING CONSENT CHECK
                if not marketing_consent:
                    errors.append("Please consent to follow-up communications to receive your results")
                
                if errors:
                    for error in errors:
                        st.error(f"❌ {error}")
                else:
                    # Save contact info with optional fields defaulting to empty/not specified
                    st.session_state.contact_info = {
                        'name': name.strip() if name.strip() else 'Not provided',
                        'email': email.strip(),
                        'phone': phone.strip() if phone.strip() else 'Not provided',
                        'urgency': urgency if urgency != 'Not specified' else 'Not specified',
                        'primary_concern': concern.strip() if concern.strip() else 'Not provided',
                        'next_step': next_step if next_step != 'Not specified' else 'Not specified',
                        'marketing_consent': marketing_consent,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    # GENERATE CLINICAL TEMPLATE
                    clinical_template = self._format_clinical_template()
                    
                    # Prepare assessment data for email with clinical template
                    assessment_data = {
                        'contact_info': st.session_state.contact_info,
                        'assessment_results': st.session_state.assessment_results,
                        'assessment_responses': st.session_state.assessment_responses,
                        'intensity_responses': st.session_state.intensity_responses,
                        'adaptive_triggered': st.session_state.adaptive_paths,
                        'risk_flags': st.session_state.risk_flags,
                        'pattern_scores': st.session_state.pattern_scores,
                        'trigger_chain': st.session_state.trigger_chain,
                        'clinical_template': clinical_template,  # ADD THIS LINE
                        'start_time': st.session_state.start_time,
                        'completion_timestamp': datetime.now().isoformat()
                    }
                    
                    # Send comprehensive clinical assessment email
                    try:
                        #from utils.email_handler import send_clinical_assessment_results
                        from utils.email_assess import send_clinical_assessment_results
                        
                        email_success = send_clinical_assessment_results(assessment_data)
                        
                        if email_success:
                            st.success("✅ Assessment completed and clinical team notified!")
                            st.info("📧 Your detailed analysis has been sent to our clinical team for review.")
                        else:
                            st.warning("⚠️ Assessment saved, but email notification failed. Our team will still receive your results.")
                            
                    except ImportError as e:
                        st.error(f"Email system unavailable: {e}")
                        st.info("Assessment completed! Our clinical team will review your results.")
                    except Exception as e:
                        st.error(f"Email error: {str(e)}")
                    
                    st.session_state.contact_provided = True
                    st.rerun()

    def _render_results(self):
        """Render final results page"""
        st.markdown("## Your behavioral pattern analysis")
        
        # Direct to clinical analysis without success message or metrics
        self._render_clinical_analysis_section()
    
        st.markdown("### Your next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        next_step = contact_info.get('next_step', '')
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            st.warning("⚠️ **Priority contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
        st.markdown("""
        **What happens next:**
    
        1. **Clinical review** (24-48 hours): Licensed therapist analyzes your responses
        2. **Personalized protocol** (48-72 hours): Custom hypnotherapy approach designed for your patterns  
        3. **Initial contact** (within 72 hours): We'll reach out via your preferred method
        
        **Want to understand our proven method?** Visit [hypnotherapy.streamlit.app](https://hypnotherapy.streamlit.app) to learn about our rapid transformation hypnotherapy approach.
        
        **Questions?** Reply to any email from us or contact our clinical team directly.
        """)
        
        # Add bottom CTA button
        st.markdown(f"""
        <div class="text-center">
            <a href="{self.discovery_url}" 
               target="_blank" 
               class="cta-button">
               📞 Schedule your session
            </a>
        </div>
        """, unsafe_allow_html=True)

    def _render_clinical_analysis_section(self):
        """Render clinical analysis with paywall integration"""
        if PAYWALL_AVAILABLE:
            try:
                paywall = create_clinical_paywall()
                assessment_data = {
                    'assessment_results': st.session_state.assessment_results,
                    'assessment_responses': st.session_state.assessment_responses,
                    'intensity_responses': st.session_state.intensity_responses,
                }
                contact_info = st.session_state.get('contact_info', {})
                assessment_data.update(contact_info)
                
                if paywall.check_payment_status():
                    paywall.render_premium_analysis(assessment_data)
                else:
                    self._render_analysis_preview()
                    with st.expander("🔓 Unlock complete clinical analysis", expanded=False):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading premium analysis: {str(e)}")
                self._render_analysis_preview()
        else:
            st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
            self._render_analysis_preview()

    def _render_analysis_preview(self):
        """Render preview of analysis results"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            st.markdown("**🎯 Your top behavioral patterns:**")
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            descriptions = {
                1: "Difficulty accepting or maintaining positive emotional states",
                2: "Recurring conflicts and power struggles in relationships", 
                3: "Default skepticism and difficulty trusting others' intentions",
                4: "Black-and-white thinking patterns that limit options",
                5: "Self-worth tied to productivity and achievement",
                6: "Inconsistent sense of identity across different contexts",
                7: "Prioritizing others' needs while neglecting self-care",
                8: "Life choices driven by family expectations",
                9: "Context-dependent loss of personal boundaries"
            }
            
            # Show only the top pattern
            if sorted_patterns:
                pattern_id, score = sorted_patterns[0]
                pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
                strength = "High" if score >= 6 else "Moderate" if score >= 3 else "Emerging"
                
                st.markdown(f"**1. {pattern_name}** - *{strength} intensity pattern detected*")
                
                if pattern_id in descriptions:
                    st.caption(descriptions[pattern_id])
                
                # Show indication of additional patterns if there are more
                if len(sorted_patterns) > 1:
                    remaining = len(sorted_patterns) - 1
                    st.write(f"**2. ...** *Plus {remaining} additional pattern{'s' if remaining > 1 else ''} identified*")
        
        # Info section outside the expander
        st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
    
    #Enhanced Clinical Analysis Methods for assess.py
    #Add these methods to the ComprehensiveBehavioralAssessment class
    
    def _extract_clinical_insights(self):
        """Extract comprehensive clinical insights from assessment responses"""
        results = st.session_state.assessment_results
        responses = st.session_state.assessment_responses
        pattern_scores = st.session_state.pattern_scores
        
        # Initialize clinical insights
        clinical_insights = {}
        
        # Extract Core Limiting Belief
        clinical_insights['core_limiting_belief'] = self._extract_core_limiting_belief(responses, pattern_scores)
        
        # Extract Hidden Benefits (Secondary Gains)
        clinical_insights['hidden_benefits'] = self._extract_hidden_benefits(responses)
        
        # Extract Systemic Resistance
        clinical_insights['systemic_resistance'] = self._extract_systemic_resistance(responses, pattern_scores)
        
        # Extract Identity Threat
        clinical_insights['identity_threat'] = self._extract_identity_threat(responses, pattern_scores)
        
        # Extract Intervention Keywords
        clinical_insights['intervention_keywords'] = self._extract_intervention_keywords(pattern_scores)
        
        # Extract Language to Avoid
        clinical_insights['avoid_language'] = self._extract_avoid_language(pattern_scores)
        
        # Extract Predicted Resistance Points
        clinical_insights['resistance_points'] = self._extract_resistance_points(responses, pattern_scores)
        
        return clinical_insights
    
    def _extract_core_limiting_belief(self, responses, pattern_scores):
        """Extract the core limiting belief from text responses"""
        belief_indicators = {
            "not good enough": "I am fundamentally inadequate/unworthy",
            "can't trust": "Others will inevitably betray or harm me", 
            "must be perfect": "Any mistake proves my worthlessness",
            "others first": "My needs and wants are less important than others'",
            "can't handle": "I am too weak/fragile to cope with life's challenges",
            "should": "I must meet external expectations to be acceptable",
            "either or": "Life offers only extreme choices with no middle ground",
            "not real": "Showing my true self will lead to rejection",
            "must do": "My value depends entirely on what I accomplish"
        }
        
        # Analyze text responses for belief patterns
        text_responses = []
        for response_data in responses.values():
            if isinstance(response_data.get('response'), str):
                text_responses.append(response_data['response'].lower())
        
        combined_text = ' '.join(text_responses)
        
        # Check for belief indicators
        for indicator, belief in belief_indicators.items():
            if indicator in combined_text:
                return belief
        
        # Fallback based on dominant pattern
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            pattern_beliefs = {
                1: "Happiness and positive emotions are dangerous or undeserved",
                2: "I must fight to maintain control or I'll be powerless",
                3: "Others cannot be trusted with my vulnerability or truth",
                4: "Life is black and white - there are no good compromises",
                5: "I am only valuable when I'm being productive or achieving",
                6: "Showing my real self will result in rejection or judgment",
                7: "Others' needs matter more than my own wellbeing",
                8: "I must fulfill family expectations to maintain love/belonging",
                9: "I am powerless in certain situations or with certain people"
            }
            return pattern_beliefs.get(dominant_pattern, "Core belief requires further exploration")
        
        return "Core belief requires further exploration"
    
    def _extract_hidden_benefits(self, responses):
        """Extract secondary gains and hidden benefits of the pattern"""
        # Look for responses about what would be lost if pattern changed
        benefit_keywords = {
            "safe": "Maintains emotional safety and predictability",
            "control": "Provides sense of control over outcomes",
            "protect": "Protects from emotional pain or vulnerability", 
            "avoid": "Avoids confronting deeper fears or truths",
            "belonging": "Maintains connection/belonging to family/group",
            "identity": "Preserves familiar sense of self/identity",
            "attention": "Ensures attention and care from others",
            "excuse": "Provides excuse for not taking risks",
            "blame": "Allows blame of others rather than self-responsibility"
        }
        
        text_responses = []
        for response_data in responses.values():
            if isinstance(response_data.get('response'), str):
                text_responses.append(response_data['response'].lower())
        
        combined_text = ' '.join(text_responses)
        
        found_benefits = []
        for keyword, benefit in benefit_keywords.items():
            if keyword in combined_text:
                found_benefits.append(benefit)
        
        if found_benefits:
            return " | ".join(found_benefits[:3])  # Top 3 benefits
        else:
            return "Pattern provides emotional protection and familiar identity structure"
    
    def _extract_systemic_resistance(self, responses, pattern_scores):
        """Extract family/system resistance to change"""
        resistance_indicators = {
            "family": "Family system may resist change to maintain homeostasis",
            "disappoint": "Fear of disappointing family members or authority figures",
            "loyalty": "Conflicted loyalty between personal growth and family expectations",
            "tradition": "Challenge to cultural or generational traditions",
            "role": "Change threatens established family role or identity",
            "guilt": "Guilt about changing when others haven't changed",
            "betrayal": "Fear that personal change represents betrayal of family values"
        }
        
        text_responses = []
        for response_data in responses.values():
            if isinstance(response_data.get('response'), str):
                text_responses.append(response_data['response'].lower())
        
        combined_text = ' '.join(text_responses)
        
        for indicator, resistance in resistance_indicators.items():
            if indicator in combined_text:
                return resistance
        
        # Pattern-based resistance
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            pattern_resistance = {
                7: "Family may resist if client stops over-giving and care-taking",
                8: "Strong family pressure to maintain traditional expectations",
                2: "Others may escalate conflict when client stops engaging in power struggles",
                9: "Certain people may resist client's newfound boundaries and strength"
            }
            return pattern_resistance.get(dominant_pattern, "Minimal systemic resistance expected")
        
        return "Minimal systemic resistance expected"
    
    def _extract_identity_threat(self, responses, pattern_scores):
        """Extract identity threats associated with change"""
        if not pattern_scores:
            return "Identity shift requires exploration during sessions"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        identity_threats = {
            1: "Fear: 'If I'm happy, I won't be the deep/thoughtful person I am'",
            2: "Fear: 'If I stop fighting, I'll become weak and people will walk all over me'", 
            3: "Fear: 'If I trust, I'll become naive and people will take advantage of me'",
            4: "Fear: 'If I see nuance, I'll lose my moral clarity and convictions'",
            5: "Fear: 'If I stop doing, I'll become lazy and worthless'",
            6: "Fear: 'If I'm consistent, I'll be boring and people will lose interest'",
            7: "Fear: 'If I prioritize myself, I'll become selfish and people will leave'",
            8: "Fear: 'If I follow my path, I'll lose my family's love and belonging'",
            9: "Fear: 'If I'm strong everywhere, I'll lose the special care and understanding I get'"
        }
        
        return identity_threats.get(dominant_pattern, "Identity evolution requires careful navigation")
    
    def _extract_intervention_keywords(self, pattern_scores):
        """Extract keywords that will be effective in hypnotherapy"""
        if not pattern_scores:
            return "Collaborative, gentle, permissive"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        intervention_keywords = {
            1: "Permission, gentle, allowing, natural, ease, comfort, safe joy",
            2: "Collaboration, choice, partnership, respect, empowerment, mutual",
            3: "Transparency, evidence, clear, step-by-step, gradual, your pace",
            4: "Integration, both/and, possibilities, options, flexibility, nuance",
            5: "Being, presence, inherent worth, natural value, simply existing",
            6: "Authentic, genuine, consistent, true self, unified, wholeness",
            7: "Balance, strength through self-care, energy, sustainable, healthy boundaries",
            8: "Personal truth, individual path, respectful autonomy, honoring both",
            9: "Consistent strength, reliable self, universal power, steady boundaries"
        }
        
        return intervention_keywords.get(dominant_pattern, "Adaptive, responsive, individualized")
    
    def _extract_avoid_language(self, pattern_scores):
        """Extract language patterns to avoid in therapy"""
        if not pattern_scores:
            return "Authoritarian commands, pressure, criticism"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        avoid_language = {
            1: "Forced positivity, 'just be happy', minimizing pain, overwhelming enthusiasm",
            2: "Commands, authority, 'you must', domination, control, surrender completely",
            3: "Hidden agendas, unclear processes, 'trust me', unexplained techniques",
            4: "Either/or choices, black/white thinking, 'you have to choose', extremes",
            5: "Performance pressure, achievement focus, productivity language, 'earn it'",
            6: "Role expectations, 'be consistent', contextual shoulds, fitting in",
            7: "Guilt about self-focus, 'be selfish', minimizing others' needs",
            8: "Family rejection themes, 'disappointing others', complete rebellion",
            9: "Universal weakness, 'you're always', situational helplessness"
        }
        
        return avoid_language.get(dominant_pattern, "Pressure, criticism, one-size-fits-all approaches")
    
    def _extract_resistance_points(self, responses, pattern_scores):
        """Extract predicted resistance points during therapy"""
        resistance_points = []
        
        # Check readiness score
        readiness_responses = [r for r in responses.values() if 'rating' in str(r.get('response', {}))]
        if readiness_responses:
            try:
                readiness_data = readiness_responses[0]['response']
                if isinstance(readiness_data, dict) and readiness_data.get('rating', 0) < 7:
                    resistance_points.append("Low change readiness - may require motivation building")
            except:
                pass
        
        # Pattern-specific resistance
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            for pattern_id, score in sorted_patterns[:2]:
                pattern_resistance = {
                    1: "May resist positive suggestions as 'fake' or temporary",
                    2: "May challenge therapist authority or collaborative process",
                    3: "May question therapist motives or seek excessive explanations",
                    4: "May get stuck in perfectionist analysis of 'right' choice",
                    5: "May resist 'being' focused work as unproductive",
                    6: "May present differently in therapy than in assessment",
                    7: "May prioritize therapist's needs over their own growth",
                    8: "May feel guilty about changing family dynamics",
                    9: "May lose boundaries/strength when triggered during session"
                }
                if pattern_id in pattern_resistance:
                    resistance_points.append(pattern_resistance[pattern_id])
        
        # Default resistance points if none found
        if not resistance_points:
            resistance_points = [
                "Standard change resistance - fear of unknown",
                "Possible skepticism about hypnotherapy effectiveness"
            ]
        
        return resistance_points[:3]  # Maximum 3 points
    
    def _generate_session_plan(self, pattern_scores, clinical_insights):
        """Generate detailed session planning recommendations"""
        if not pattern_scores:
            return {
                'session_1_focus': "Comprehensive pattern assessment and initial rapport building",
                'session_2_target': "Core pattern transformation and positive programming", 
                'session_3_need': "Standard reinforcement if needed"
            }
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        primary_pattern = sorted_patterns[0][0] if sorted_patterns else 1
        
        session_plans = {
            1: {
                'session_1_focus': "Unhappiness Culture mapping + permission for joy + gentle positive anchoring",
                'session_2_target': "Deep joy permission installation + reframe happiness beliefs + positive emotion anchors",
                'session_3_need': "Joy maintenance if relapse into pessimism or guilt about happiness"
            },
            2: {
                'session_1_focus': "Power struggle pattern analysis + collaboration establishment + shared control",
                'session_2_target': "Transform win/lose to win/win mindset + install collaboration reflexes + peace anchors", 
                'session_3_need': "Conflict de-escalation if old fighting patterns resurface"
            },
            3: {
                'session_1_focus': "Trust violation history + safety establishment + graduated vulnerability",
                'session_2_target': "Install healthy discernment vs. systematic mistrust + trust capacity building",
                'session_3_need': "Trust maintenance if cynicism returns or trust betrayal occurs"
            },
            4: {
                'session_1_focus': "Binary thinking identification + both/and introduction + cognitive flexibility",
                'session_2_target': "Install nuanced thinking + creative option generation + decision confidence",
                'session_3_need': "Flexibility maintenance if black/white thinking resurfaces under stress"
            },
            5: {
                'session_1_focus': "Achievement addiction mapping + inherent worth establishment + being practice",
                'session_2_target': "Install worth independence from productivity + being/doing balance + rest permission",
                'session_3_need': "Worth maintenance if productivity pressure returns or achievement addiction resurfaces"
            },
            6: {
                'session_1_focus': "Authentic self identification + consistency across contexts + integration work",
                'session_2_target': "Install unified authentic self + consistent expression + context independence",
                'session_3_need': "Authenticity maintenance if compartmentalization returns under social pressure"
            },
            7: {
                'session_1_focus': "Self-sacrifice pattern mapping + self-care as strength reframe + boundary establishment",
                'session_2_target': "Install healthy balance + self-care habits + boundary maintenance reflexes",
                'session_3_need': "Balance maintenance if caretaking patterns resurface or guilt about self-care"
            },
            8: {
                'session_1_focus': "Family mission identification + personal desire differentiation + loyalty vs. autonomy",
                'session_2_target': "Install personal path confidence + family respect integration + autonomous choice",
                'session_3_need': "Autonomy maintenance if family pressure increases or guilt about independence"
            },
            9: {
                'session_1_focus': "Context-dependent weakness mapping + universal strength identification + boundary work",
                'session_2_target': "Install consistent boundaries + context-independent strength + situational confidence",
                'session_3_need': "Strength maintenance if old contexts trigger boundary collapse"
            }
        }
        
        return session_plans.get(primary_pattern, session_plans[1])
    
    def _format_clinical_template(self):
        """Format comprehensive clinical template for email"""
        # Extract all clinical insights
        clinical_insights = self._extract_clinical_insights()
        
        # Get pattern scores and session planning
        pattern_scores = st.session_state.pattern_scores
        session_plan = self._generate_session_plan(pattern_scores, clinical_insights)
        
        # Get top 3 patterns
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            dominant_pattern = self.patterns.get(sorted_patterns[0][0], "Unknown") if sorted_patterns else "Unknown"
            dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
            
            primary_pattern = self.patterns.get(sorted_patterns[1][0], "Unknown") if len(sorted_patterns) > 1 else "None detected"
            primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
            
            secondary_pattern = self.patterns.get(sorted_patterns[2][0], "Unknown") if len(sorted_patterns) > 2 else "None detected"
            secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
        else:
            dominant_pattern = primary_pattern = secondary_pattern = "Assessment incomplete"
            dominant_score = primary_score = secondary_score = 0
        
        # Get change readiness
        readiness_score = 5  # Default
        for response_data in st.session_state.assessment_responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                readiness_score = response_data['response']['rating']
                break
        
        # Format resistance points
        resistance_points = clinical_insights.get('resistance_points', [])
        resistance_text = ""
        for i, point in enumerate(resistance_points[:3], 1):
            resistance_text += f"{i}. {point}\n"
        if not resistance_text:
            resistance_text = "1. Standard change resistance\n2. Possible skepticism about process\n"
        
        # Generate behavioral sequence analysis
        behavioral_sequence = self._generate_behavioral_sequence_analysis()
        
        # Build comprehensive template
        template = f"""
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║                   Behavioral Pattern Assessment              ║
╚══════════════════════════════════════════════════════════════╝

**PATTERN ANALYSIS:**
Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10) 
Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: {clinical_insights.get('core_limiting_belief', 'Requires session exploration')}
Hidden Benefits: {clinical_insights.get('hidden_benefits', 'Emotional protection and familiar identity')}
Systemic Resistance: {clinical_insights.get('systemic_resistance', 'Minimal resistance expected')}
Identity Threat: {clinical_insights.get('identity_threat', 'Identity evolution requires navigation')}

**SESSION PLANNING:**
Session 1 Focus: {session_plan.get('session_1_focus', 'Pattern analysis and rapport building')}
Session 2 Target: {session_plan.get('session_2_target', 'Core transformation and positive programming')}
Potential Session 3 Need: {session_plan.get('session_3_need', 'Reinforcement if needed')}

**THERAPEUTIC APPROACH:**
Change Readiness Score: {readiness_score}/10
Predicted Resistance Points:
{resistance_text}
Intervention Keywords: {clinical_insights.get('intervention_keywords', 'Collaborative, gentle, permissive')}
Avoid Language: {clinical_insights.get('avoid_language', 'Pressure, criticism, commands')}

{behavioral_sequence}

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL NOTES                          ║
╚══════════════════════════════════════════════════════════════╝

This comprehensive analysis provides the therapeutic framework for rapid, effective hypnotherapy intervention based on the client's unique behavioral pattern constellation and complete behavioral sequence mapping.
"""
        
        return template

    # ---- Analysis Helper Methods ----
    def _analyze_trigger_type(self, trigger_info):
        """Analyze the type of trigger"""
        trigger_lower = trigger_info.lower()
        if any(word in trigger_lower for word in ['thought', 'worry', 'thinking']):
            return "Cognitive trigger - internal rumination pattern"
        elif any(word in trigger_lower for word in ['said', 'person', 'someone']):
            return "Interpersonal trigger - social activation"
        elif any(word in trigger_lower for word in ['situation', 'environment', 'place']):
            return "Environmental trigger - contextual activation"
        else:
            return "Mixed trigger - requires clarification"

    def _analyze_activation_pattern(self, trigger_info):
        """Analyze activation pattern"""
        if 'sudden' in trigger_info.lower() or 'immediately' in trigger_info.lower():
            return "Rapid activation - acute stress response"
        elif 'gradual' in trigger_info.lower() or 'slowly' in trigger_info.lower():
            return "Gradual activation - building tension pattern"
        else:
            return "Standard activation - typical response timing"

    def _extract_environmental_factors(self, responses):
        """Extract environmental factors from responses"""
        # Look through responses for environmental context
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and any(word in response.lower() for word in ['work', 'home', 'family', 'social']):
                return "Context-dependent activation identified"
        return "Environmental factors require exploration"

    def _get_response_intensity(self, response_type):
        """Get intensity rating for specific response type"""
        intensities = st.session_state.get('intensity_responses', {})
        # Find intensity for this response type
        for q_id, intensity in intensities.items():
            response_data = st.session_state.get('assessment_responses', {}).get(q_id, {})
            if response_data.get('chain_mapping') == response_type:
                return intensity
        return "Not rated"

    def _analyze_somatic_location(self, physical_response):
        """Analyze somatic response location"""
        response_lower = physical_response.lower()
        if any(word in response_lower for word in ['chest', 'heart', 'breathing']):
            return "Cardiac/respiratory system - anxiety/stress activation"
        elif any(word in response_lower for word in ['stomach', 'nausea', 'digestive']):
            return "Digestive system - gut-brain connection"
        elif any(word in response_lower for word in ['muscle', 'tension', 'jaw']):
            return "Muscular system - fight/flight preparation"
        else:
            return "Multi-system activation"

    def _analyze_activation_system(self, physical_response):
        """Analyze which system is being activated"""
        response_lower = physical_response.lower()
        if any(word in response_lower for word in ['racing', 'fast', 'pounding']):
            return "Sympathetic nervous system activation"
        elif any(word in response_lower for word in ['numb', 'disconnect', 'freeze']):
            return "Dorsal vagal shutdown response"
        else:
            return "Mixed autonomic response"

    def _get_somatic_significance(self, physical_response):
        """Get clinical significance of somatic response"""
        return "Primary intervention target - somatic regulation essential"

    def _analyze_cognitive_distortion(self, thought):
        """Analyze type of cognitive distortion"""
        thought_lower = thought.lower()
        if any(phrase in thought_lower for phrase in ['not good enough', 'inadequate', 'failure']):
            return "Negative self-evaluation"
        elif any(phrase in thought_lower for phrase in ['must', 'should', 'have to']):
            return "Demanding/perfectionist thinking"
        elif any(phrase in thought_lower for phrase in ['always', 'never', 'everyone']):
            return "All-or-nothing thinking"
        else:
            return "Complex cognitive pattern"

    def _extract_core_belief_from_thought(self, thought):
        """Extract core belief indicated by automatic thought"""
        thought_lower = thought.lower()
        if 'not good enough' in thought_lower:
            return "Core inadequacy belief"
        elif any(word in thought_lower for word in ['danger', 'threat', 'bad']):
            return "Safety/threat belief system"
        elif any(word in thought_lower for word in ['reject', 'abandon', 'leave']):
            return "Attachment/abandonment fears"
        else:
            return "Requires deeper exploration"

    def _get_thought_intervention_target(self, thought):
        """Get intervention target for thought pattern"""
        return "Cognitive restructuring with pattern-specific reframes"

    def _analyze_language_pattern(self, thought):
        """Analyze language patterns in thought"""
        thought_lower = thought.lower()
        if any(word in thought_lower for word in ['must', 'should', 'have to']):
            return "Demanding language - rigid expectations"
        elif any(word in thought_lower for word in ['can\'t', 'won\'t', 'impossible']):
            return "Limitation language - learned helplessness"
        else:
            return "Standard self-talk pattern"

    def _analyze_emotional_constellation(self, emotional_response):
        """Analyze emotional response constellation"""
        if isinstance(emotional_response, dict):
            emotions = list(emotional_response.keys())
            if len(emotions) > 3:
                return "Complex emotional constellation - high activation"
            elif any('anxious' in emotion.lower() for emotion in emotions):
                return "Anxiety-centered constellation"
            elif any('angry' in emotion.lower() for emotion in emotions):
                return "Anger-centered constellation"
            else:
                return "Mixed emotional activation"
        else:
            return "Single emotion focus"

    def _assess_regulation_capacity(self, emotional_response):
        """Assess emotional regulation capacity"""
        if isinstance(emotional_response, dict):
            high_intensity = [emotion for emotion, intensity in emotional_response.items() if intensity >= 6]
            if len(high_intensity) >= 2:
                return "Low regulation capacity - overwhelm pattern"
            else:
                return "Moderate regulation capacity"
        else:
            return "Regulation capacity requires assessment"

    def _get_emotional_intervention(self, emotional_response):
        """Get emotional intervention approach"""
        return "Emotional regulation training with somatic anchoring"

    def _analyze_behavioral_pattern(self, behavioral_response):
        """Analyze behavioral response pattern"""
        response_lower = behavioral_response.lower()
        if any(word in response_lower for word in ['avoid', 'withdraw', 'escape']):
            return "Avoidance pattern - flight response"
        elif any(word in response_lower for word in ['busy', 'active', 'do']):
            return "Hyperactivity pattern - doing addiction"
        elif any(word in response_lower for word in ['argue', 'fight', 'defend']):
            return "Confrontation pattern - fight response"
        else:
            return "Complex behavioral response"

    def _analyze_behavioral_function(self, behavioral_response):
        """Analyze function of behavioral response"""
        response_lower = behavioral_response.lower()
        if 'avoid' in response_lower:
            return "Emotional avoidance and safety-seeking"
        elif any(word in response_lower for word in ['busy', 'productive']):
            return "Distraction and control-seeking"
        else:
            return "Multiple functions - requires exploration"

    def _assess_pattern_alignment(self, behavioral_response):
        """Assess how behavior aligns with dominant patterns"""
        pattern_scores = st.session_state.get('pattern_scores', {})
        if not pattern_scores:
            return "Pattern alignment requires completion"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        response_lower = behavioral_response.lower()
        
        alignments = {
            1: ['avoid', 'withdraw', 'pessimistic'],
            2: ['argue', 'fight', 'control'],
            3: ['suspicious', 'test', 'withdraw'],
            4: ['paralyzed', 'either', 'stuck'],
            5: ['busy', 'productive', 'work'],
            6: ['different', 'adapt', 'change'],
            7: ['others', 'help', 'sacrifice'],
            8: ['should', 'family', 'expect'],
            9: ['weak', 'powerless', 'context']
        }
        
        pattern_keywords = alignments.get(dominant_pattern, [])
        if any(keyword in response_lower for keyword in pattern_keywords):
            return f"Strong alignment with Pattern {dominant_pattern}"
        else:
            return "Partial pattern alignment"

    def _get_behavioral_intervention_point(self, behavioral_response):
        """Get behavioral intervention point"""
        return "Response substitution with healthier alternatives"

    def _analyze_consequence_type(self, consequence):
        """Analyze type of consequence"""
        consequence_lower = consequence.lower()
        if any(word in consequence_lower for word in ['worse', 'agitated', 'escalate']):
            return "Escalating consequence - pattern amplification"
        elif any(word in consequence_lower for word in ['relief', 'better', 'calm']):
            return "Reinforcing consequence - pattern maintenance"
        else:
            return "Mixed consequence pattern"

    def _analyze_reinforcement_pattern(self, consequence):
        """Analyze reinforcement pattern"""
        consequence_lower = consequence.lower()
        if 'temporary' in consequence_lower and 'relief' in consequence_lower:
            return "Intermittent reinforcement - strong pattern maintenance"
        elif any(word in consequence_lower for word in ['worse', 'agitated']):
            return "Negative reinforcement - pattern should extinguish but may be maintained by other factors"
        else:
            return "Complex reinforcement - requires analysis"

    def _get_consequence_intervention_timing(self, consequence):
        """Get intervention timing for consequences"""
        return "Immediate post-response intervention with pattern interruption"

    def _analyze_pattern_reinforcement(self, longer_impact):
        """Analyze how longer-term impact reinforces pattern"""
        impact_lower = longer_impact.lower()
        if any(word in impact_lower for word in ['replay', 'ruminate', 'think']):
            return "Cognitive reinforcement through rumination"
        elif any(word in impact_lower for word in ['avoid', 'prevent', 'plan']):
            return "Behavioral reinforcement through preparation"
        else:
            return "Multi-modal reinforcement pattern"

    def _assess_cycle_completion(self, longer_impact):
        """Assess if the cycle completes back to trigger"""
        impact_lower = longer_impact.lower()
        if any(word in impact_lower for word in ['ready', 'next', 'again']):
            return "Complete cycle - primes for re-activation"
        else:
            return "Incomplete cycle data"

    def _identify_breaking_points(self, longer_impact):
        """Identify potential breaking points in cycle"""
        return "Multiple intervention windows identified"

    def _calculate_chain_completeness(self):
        """Calculate what percentage of the chain is complete"""
        trigger_chain = st.session_state.get('trigger_chain', {})
        total_components = 6  # trigger, physical, thought, emotion, behavior, consequence
        
        completed_components = 0
        for component in ['awareness_point', 'physical_response', 'automatic_thought', 'emotional_response', 'behavioral_response', 'immediate_consequence']:
            if trigger_chain.get(component) and trigger_chain.get(component) != 'Not captured' and trigger_chain.get(component) != 'Skipped':
                completed_components += 1
        
        return int((completed_components / total_components) * 100)

    def _identify_missing_components(self):
        """Identify missing components in the behavioral chain"""
        trigger_chain = st.session_state.get('trigger_chain', {})
        missing = []
        
        components = {
            'awareness_point': 'Trigger identification and specificity',
            'automatic_thought': 'Specific thought content during activation',
            'emotional_response': 'Complete emotional sequence and intensity',
            'behavioral_response': 'Exact behavioral response pattern',
            'immediate_consequence': 'Immediate aftermath and reinforcement',
            'longer_term_impact': 'Pattern completion and cycle reinforcement'
        }
        
        for component, description in components.items():
            value = trigger_chain.get(component)
            if not value or value == 'Not captured' or value == 'Skipped':
                missing.append(description)
        
        return missing


# ---- Main Application Classes ----
class AssessPage:
    """Main application wrapper maintaining compatibility with original interface"""
    
    def __init__(self):
        self.assessment = ComprehensiveBehavioralAssessment()
    
    def render(self):
        self.assessment.render()


# ---- Page Factory Function ----
def create_assess_page():
    """Factory function to create the assessment page"""
    return AssessPage()


# ---- Helper Functions ----
def get_assessment_summary():
    """Get current assessment summary"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results
    return None

def get_pattern_scores():
    """Get current pattern scores"""
    if 'pattern_scores' in st.session_state:
        return st.session_state.pattern_scores
    return {}

def reset_assessment():
    """Reset assessment state"""
    keys_to_reset = [
        'assessment_responses', 'current_question', 'current_phase', 'phase_progress',
        'triggered_patterns', 'pattern_scores', 'risk_flags', 'assessment_completed', 
        'contact_provided', 'assessment_results', 'intensity_responses', 'motivation_data',
        'trigger_chain', 'response_chain', 'adaptive_paths'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]

def export_assessment_data():
    """Export complete assessment data"""
    if 'assessment_responses' not in st.session_state:
        return None
    
    return {
        'responses': st.session_state.assessment_responses,
        'pattern_scores': st.session_state.get('pattern_scores', {}),
        'intensity_data': st.session_state.get('intensity_responses', {}),
        'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
        'adaptive_paths': st.session_state.get('adaptive_paths', []),
        'risk_flags': st.session_state.get('risk_flags', []),
        'trigger_chain': st.session_state.get('trigger_chain', {}),
        'phase_progress': st.session_state.get('phase_progress', {}),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }

def get_behavioral_chain():
    """Get the complete behavioral chain mapping"""
    if 'trigger_chain' not in st.session_state:
        return None
    
    return {
        'trigger_sequence': st.session_state.get('trigger_chain', {}),
        'pattern_activations': st.session_state.get('pattern_scores', {}),
        'intensity_levels': st.session_state.get('intensity_responses', {}),
        'response_patterns': {
            'dominant_pattern': st.session_state.get('assessment_results', {}).get('dominant_pattern'),
            'secondary_patterns': list(st.session_state.get('triggered_patterns', set()))
        }
    }

def get_hypnotherapy_recommendations():
    """Generate hypnotherapy recommendations based on assessment"""
    if 'pattern_scores' not in st.session_state or not st.session_state.pattern_scores:
        return None
    
    dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
    
    recommendations = {
        1: {
            "approach": "Permission-based, gentle positive installation",
            "language": "Collaborative, non-directive, allowing language",
            "avoid": "Overwhelming positivity, forced happiness",
            "induction": "Progressive relaxation with permission phrases"
        },
        2: {
            "approach": "Collaborative empowerment, shared control",
            "language": "Partnership language, choice-focused",
            "avoid": "Authoritarian commands, directive language",
            "induction": "Self-guided with therapist facilitation"
        },
        3: {
            "approach": "Trust-building, transparent process",
            "language": "Clear explanations, evidence-based",
            "avoid": "Hidden agendas, unexplained techniques",
            "induction": "Fully explained, client-controlled depth"
        },
        4: {
            "approach": "Integration therapy, both/and thinking",
            "language": "Possibility expansion, option creation",
            "avoid": "Either/or choices, black-and-white language",
            "induction": "Creative visualization with multiple pathways"
        },
        5: {
            "approach": "Being-centered work, inherent worth",
            "language": "Presence-focused, non-performance based",
            "avoid": "Achievement language, productivity focus",
            "induction": "Mindfulness-based, present-moment awareness"
        },
        6: {
            "approach": "Authentic self integration",
            "language": "Consistency across contexts, authentic expression",
            "avoid": "Role-based language, contextual expectations",
            "induction": "Core self connection, identity integration"
        },
        7: {
            "approach": "Self-care strength reframing",
            "language": "Balanced care, strength through self-care",
            "avoid": "Guilt-inducing self-focus language",
            "induction": "Nurturing self-care as service to others"
        },
        8: {
            "approach": "Personal desire differentiation",
            "language": "Individual path honoring, respectful autonomy",
            "avoid": "Family rejection themes, complete rebellion",
            "induction": "Personal truth with family love integration"
        },
        9: {
            "approach": "Context-independent strength building",
            "language": "Consistent boundary language, universal strength",
            "avoid": "Situational weakness reinforcement",
            "induction": "Anchor strong self across all contexts"
        }
    }
    
    return recommendations.get(dominant_pattern, {
        "approach": "Individualized based on assessment findings",
        "language": "Supportive, adaptive to client needs",
        "avoid": "Generic approaches without personalization",
        "induction": "Tailored to client's response patterns"
    })


# # ---- Main Execution ----
# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Behavioral Pattern Assessment",
#         page_icon="🧠",
#         layout="centered",
#         initial_sidebar_state="collapsed"
#     )
    
#     assessment_page = create_assess_page()
#     assessment_page.render()
