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
        font-size: 0.85rem;
        color: #556D7A;
        padding: 0.5rem;
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
                    1: [5], 2: [5], 4: [3], 5: [8], 6: [3]
                },
                "phase": "engagement"
            },
            2: {
                "text": "If this issue completely resolved, what would be different about your daily life?",
                "type": "text_completion",
                "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
                "min_chars": 50,
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
                "min_chars": 40,
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
                "min_chars": 10,
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
                    "min_chars": 20,
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
                    "min_chars": 20,
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
                    "min_chars": 15,
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
                    "min_chars": 10,
                    "pattern": 4
                },
                25: {
                    "text": "What would become possible if you could embrace 'both/and' instead of 'either/or'?",
                    "type": "text_completion",
                    "placeholder": "Imagine having more options and flexibility in your choices...",
                    "min_chars": 20,
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
                    "min_chars": 15,
                    "pattern": 5
                },
                28: {
                    "text": "Who first taught you that your value depends on what you produce?",
                    "type": "text_completion",
                    "placeholder": "Think about early messages from family, school, or society...",
                    "min_chars": 15,
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
                    "min_chars": 20,
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
                    "min_chars": 20,
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
                    "min_chars": 20,
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
                    "min_chars": 20,
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
                "min_chars": 25,
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
                "min_chars": 30,
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
        min_chars = question.get('min_chars', 10)
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
            st.markdown(f"<div class='char-counter {color_class}'>{char_count}/{min_chars} characters minimum</div>", unsafe_allow_html=True)
        
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
        st.markdown("<h1 style='text-align: center;'>Behavioral Pattern Assessment</h1>", unsafe_allow_html=True)
        
        if not st.session_state.assessment_completed:
            time_remaining = self._estimate_time_remaining()
            st.info(f"🧠 Discover your unique behavioral patterns for targeted rapid-change hypnotherapy. Estimated time: {time_remaining:.0f} minutes.")

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
        <div class="time-estimate">About {time_remaining:.0f} minutes remaining | Phase: {st.session_state.current_phase.replace('_', ' ').title()}</div>
        """, unsafe_allow_html=True)

        # Question display
        st.markdown(f"### {question['text']}")
        
        # Show pattern detection hints for engaged users
        if completed > 5 and st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
            if top_pattern[1] >= 2.0:
                pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
                st.markdown(f"""
                <div class="pattern-hint">
                💡 Pattern emerging: {pattern_name} - this helps us customize your approach
                </div>
                """, unsafe_allow_html=True)

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

    def _render_contact_form(self):
        """Render contact form for results"""
        st.markdown("### Assessment Complete! 🎉")
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

        st.markdown("**Enter your details to receive your personalized analysis and next steps:**")
        
        with st.form("contact_form"):
            name = st.text_input("Full Name*", placeholder="Your full name")
            email = st.text_input("Email*", placeholder="your@email.com")
            phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
            urgency = st.selectbox(
                "How urgent is addressing this pattern?*",
                ["Select urgency level...", "Extremely urgent - significantly impacting life", 
                 "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
                 "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
            )
            
            concern = st.text_area(
                "What brought you to this assessment?*",
                placeholder="Brief description of what motivated you to take this assessment...",
                height=100
            )
            
            next_step = st.selectbox(
                "Preferred next step:*",
                ["Select your preference...", "Schedule free consultation call", 
                 "Information about transformation packages", "Receive analysis and recommendations first", 
                 "Connect with clinical team directly"]
            )
            
            marketing_consent = st.checkbox(
                "I consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
            )
            
            submitted = st.form_submit_button("Get My Personalized Analysis", type="primary", use_container_width=True)

            if submitted:
                errors = []
                if not name.strip(): 
                    errors.append("Name is required")
                if not email.strip(): 
                    errors.append("Email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
                    errors.append("Valid email address is required")
                if not concern.strip(): 
                    errors.append("Please describe what brought you here")
                if urgency == "Select urgency level...": 
                    errors.append("Please select urgency level")
                if next_step == "Select your preference...": 
                    errors.append("Please select your preferred next step")
                if not marketing_consent:
                    errors.append("Please consent to follow-up communications to receive your results")
                
                if errors:
                    for error in errors:
                        st.error(f"❌ {error}")
                else:
                    # Save contact info
                    st.session_state.contact_info = {
                        'name': name.strip(),
                        'email': email.strip(),
                        'phone': phone.strip(),
                        'urgency': urgency,
                        'primary_concern': concern.strip(),
                        'next_step': next_step,
                        'marketing_consent': marketing_consent,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    # Prepare assessment data for email
                    assessment_data = {
                        'contact_info': st.session_state.contact_info,
                        'assessment_results': st.session_state.assessment_results,
                        'assessment_responses': st.session_state.assessment_responses,
                        'intensity_responses': st.session_state.intensity_responses,
                        'adaptive_triggered': st.session_state.adaptive_paths,
                        'risk_flags': st.session_state.risk_flags,
                        'pattern_scores': st.session_state.pattern_scores,
                        'trigger_chain': st.session_state.trigger_chain,
                        'start_time': st.session_state.start_time,
                        'completion_timestamp': datetime.now().isoformat()
                    }
                    
                    # Send comprehensive clinical assessment email
                    try:
                        from utils.email_handler import send_clinical_assessment_results
                        
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
        st.markdown("## Your Behavioral Pattern Analysis")
        
        contact_info = st.session_state.get('contact_info', {})
        st.success(f"Thank you, {contact_info.get('name', 'there')}! Your comprehensive analysis has been generated.")
        
        results = st.session_state.assessment_results
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "Answered")
        with col2:
            patterns_count = len(results.get('pattern_scores', {}))
            st.metric("Patterns", patterns_count, "Detected")
        with col3:
            risk_count = len(results.get('risk_flags', []))
            st.metric("Risk Factors", risk_count, "Identified")
        with col4:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completeness", f"{completion_rate*100:.0f}%", "Assessment")

        self._render_clinical_analysis_section()

        st.markdown("### Your Next Steps")
        
        next_step = contact_info.get('next_step', '')
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            st.warning("⚠️ **Priority Contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
        if 'consultation' in next_step.lower():
            st.info("📅 **Consultation Scheduling**: We'll contact you within 48 hours to schedule your free consultation call.")
        elif 'package' in next_step.lower():
            st.success("📋 **Transformation Packages**: We'll send you detailed information about our personalized programs.")
        elif 'analysis' in next_step.lower():
            st.info("📊 **Analysis First**: We'll email your detailed analysis and specific recommendations.")
        else:
            st.info("🤝 **Clinical Team Contact**: Our team will reach out with personalized next steps.")
        
        st.markdown("""
        **What happens next:**

        1. **Clinical Review** (24-48 hours): Licensed therapist analyzes your responses
        2. **Personalized Protocol** (48-72 hours): Custom hypnotherapy approach designed for your patterns  
        3. **Initial Contact** (48-72 hours): We'll reach out via your preferred method
        4. **Transformation Planning** (1 week): Develop your individualized program
        
        **Questions?** Reply to any email from us or contact our clinical team directly.
        """)

    def _render_clinical_analysis_section(self):
        """Render clinical analysis with paywall integration"""
        st.markdown("### Clinical Pattern Analysis")
        
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
                    with st.expander("🔓 Unlock Complete Clinical Analysis", expanded=True):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading premium analysis: {str(e)}")
                self._render_analysis_preview()
        else:
            st.info("💡 **Premium Analysis Available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
            self._render_analysis_preview()

    def _render_analysis_preview(self):
        """Render preview of analysis results"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            st.markdown("**🎯 Your Top Behavioral Patterns:**")
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
            
            for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
                pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
                strength = "High" if score >= 6 else "Moderate" if score >= 3 else "Emerging"
                
                st.markdown(f"**{i+1}. {pattern_name}** - *{strength} intensity pattern detected*")
                
                if pattern_id in descriptions:
                    st.caption(descriptions[pattern_id])
            
            if len(sorted_patterns) > 3:
                remaining = len(sorted_patterns) - 3
                st.write(f"*Plus {remaining} additional patterns identified...*")
        
        risk_count = len(results.get('risk_flags', []))
        if risk_count > 0:
            st.markdown(f"**⚠️ Clinical Considerations:** {risk_count} factors requiring specialized approach")
        
        st.info("**Complete analysis includes:** Detailed pattern breakdowns, root cause analysis, personalized hypnotherapy protocol, session planning, and progress tracking recommendations.")


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


# ---- Main Execution ----
if __name__ == "__main__":
    st.set_page_config(
        page_title="Behavioral Pattern Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render()
