# # Complete Enhanced Clinical Behavioral Pattern Assessment
# # Integrated with algorithmical divide Syndrome screening and analysis
# # Comprehensive implementation with adaptive questioning and pattern detection
# # Optimized for both traditional and digital-native populations

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
#             max-width: 650px !important;
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
#     .progress-container {
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#         margin-bottom: 1.5rem;
#         font-size: 0.75rem;
#         font-weight: normal; 
#         color: #556D7A;
#         padding: 0.5rem;
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
#     .digital-indicator {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         padding: 0.5rem;
#         border-radius: 6px;
#         margin: 0.5rem 0;
#         font-size: 0.85rem;
#         text-align: center;
#     }
#     .pattern-hint {
#         background: #f0f9ff;
#         border-left: 3px solid #0ea5e9;
#         padding: 0.5rem;
#         margin: 0.5rem 0;
#         font-size: 0.85rem;
#         font-style: italic;
#     }
#     .cta-button {
#         display: inline-block;
#         background: linear-gradient(135deg, #4CA1A3 0%, #357a7c 100%);
#         color: white !important;
#         padding: 12px 24px;
#         border-radius: 8px;
#         text-decoration: none;
#         font-weight: 600;
#         margin: 20px auto;
#         text-align: center;
#         transition: transform 0.2s ease;
#     }
#     .cta-button:hover {
#         transform: translateY(-2px);
#         text-decoration: none;
#         color: white !important;
#     }
#     .text-center {
#         text-align: center;
#     }
#     @media (max-width: 768px) {
#         .main .block-container {
#             padding-left: 1rem;
#             padding-right: 1rem;
#             padding-top: 1rem;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # ---- Enhanced Assessment Class ----
# class ComprehensiveBehavioralAssessment:
#     """Clinical-grade behavioral pattern assessment with algorithmical divide Syndrome integration"""
    
#     def __init__(self):
#         self._init_session_state()
#         self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
#         self.patterns = {
#             1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
#             4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
#             7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
#         }
        
#         # Question pools organized by integrated phase system
#         self.age_screening_questions = self._get_age_screening_questions()
#         self.digital_screening_questions = self._get_digital_screening_questions()
#         self.engagement_questions = self._get_engagement_questions()
#         self.trigger_mapping_questions = self._get_trigger_mapping_questions()
#         self.pattern_specific_questions = self._get_pattern_specific_questions()
#         self.integration_questions = self._get_integration_questions()

#     def _init_session_state(self):
#         defaults = {
#             'assessment_responses': {},
#             'current_question': 1,
#             'current_phase': 'age_screening',
#             'phase_progress': {
#                 'age_screening': 0, 'digital_screening': 0, 'engagement': 0, 
#                 'trigger_mapping': 0, 'pattern_specific': 0, 'integration': 0
#             },
#             'is_digital_native': False,
#             'digital_despair_score': 0,
#             'digital_severity': 'MINIMAL',
#             'triggered_patterns': set(),
#             'pattern_scores': {},
#             'risk_flags': [],
#             'assessment_completed': False,
#             'contact_provided': False,
#             'assessment_results': {},
#             'start_time': datetime.now().isoformat(),
#             'intensity_responses': {},
#             'trigger_chain': {},
#             'digital_responses': {},
#             'adaptive_paths': []
#         }
#         for key, value in defaults.items():
#             if key not in st.session_state:
#                 st.session_state[key] = value

#     def _get_age_screening_questions(self):
#         """Phase 0: Age Screening for Digital Native Assessment"""
#         return {
#             0: {
#                 "text": "What is your age range?",
#                 "type": "single_choice",
#                 "options": [
#                     "Under 18", "18-22", "23-27", "28-32", 
#                     "33-37", "38-42", "43-50", "Over 50"
#                 ],
#                 "digital_native_scoring": [3, 5, 4, 3, 2, 1, 0, 0],
#                 "phase": "age_screening",
#                 "determines_flow": True
#             }
#         }

#     def _get_digital_screening_questions(self):
#         """Phase 1: Algorithmic Syndrome Screening (for digital natives)"""
#         return {
#             1: {
#                 "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
#                 "type": "single_choice",
#                 "options": [
#                     "Less than 2 hours", "2-4 hours", "4-6 hours",
#                     "6-8 hours", "8-10 hours", "Over 10 hours"
#                 ],
#                 "digital_despair_weights": [0, 1, 2, 3, 4, 5],
#                 "phase": "digital_screening"
#             },
#             2: {
#                 "text": "Where do you feel most like your authentic self?",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "In offline, face-to-face interactions",
#                     "In online communities and digital spaces", 
#                     "Both online and offline equally",
#                     "Neither - I don't feel authentic anywhere",
#                     "It varies completely depending on the situation"
#                 ],
#                 "digital_despair_indicators": {
#                     1: 3,  # Strong offline dissociation indicator
#                     3: 2,  # Identity fragmentation 
#                     4: 4   # Complete authenticity loss
#                 },
#                 "phase": "digital_screening"
#             },
#             3: {
#                 "text": "When you imagine a successful life, you typically think:",
#                 "type": "single_choice",
#                 "options": [
#                     "Meaningful relationships and personal fulfillment",
#                     "Extraordinary wealth, fame, or achievement",
#                     "Being significantly better than most people at something",
#                     "Just being happy and content with normal life",
#                     "Success feels impossible or meaningless to me"
#                 ],
#                 "digital_despair_patterns": {
#                     1: 4,  # Extraordinary achievement pressure
#                     2: 3,  # Comparative inadequacy 
#                     4: 4   # Nihilistic worldview
#                 },
#                 "phase": "digital_screening"
#             },
#             4: {
#                 "text": "When expressing genuine emotions or enthusiasm:",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "I express them naturally and directly",
#                     "I tend to use humor or irony to deflect",
#                     "I feel embarrassed or 'cringe' about sincerity",
#                     "I mainly express emotions through memes or online references",
#                     "I rarely express genuine emotions at all"
#                 ],
#                 "ironic_detachment_scoring": [0, 2, 3, 3, 4],
#                 "phase": "digital_screening"
#             },
#             5: {
#                 "text": "What primarily influences your daily emotional state?",
#                 "type": "single_choice",
#                 "options": [
#                     "Interactions with family and friends in person",
#                     "Social media feeds and online content",
#                     "Work or school experiences", 
#                     "Internal thoughts and self-reflection",
#                     "Online communities and digital relationships"
#                 ],
#                 "algorithmic_dependency": {
#                     1: 3,  # Social media primary
#                     4: 3   # Digital relationships primary
#                 },
#                 "phase": "digital_screening"
#             },
#             6: {
#                 "text": "You feel more emotionally connected to:",
#                 "type": "single_choice",
#                 "options": [
#                     "People in your physical daily life",
#                     "Online personalities (streamers, influencers, content creators)",
#                     "Online friends and communities",
#                     "Fictional characters or media personalities",
#                     "No significant emotional connections anywhere"
#                 ],
#                 "parasocial_indicators": {
#                     1: 2,  # Online personalities
#                     2: 2,  # Online communities over offline
#                     3: 3,  # Fictional over real
#                     4: 4   # Complete disconnection
#                 },
#                 "phase": "digital_screening"
#             },
#             7: {
#                 "text": "When someone suggests things could get better or offers optimistic perspectives:",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "I feel encouraged and want to believe them",
#                     "I appreciate it but remain cautiously skeptical", 
#                     "I immediately think of reasons why they're wrong",
#                     "I feel annoyed because they don't understand reality",
#                     "I dismiss it as naive or manipulative"
#                 ],
#                 "hope_avoidance_indicators": {
#                     2: 2,  # Automatic negativity
#                     3: 3,  # Irritated by optimism
#                     4: 4   # Complete hope dismissal
#                 },
#                 "phase": "digital_screening"
#             },
#             8: {
#                 "text": "Your attention span for non-digital activities (reading books, conversations, offline tasks):",
#                 "type": "single_choice",
#                 "options": [
#                     "Same as always - can focus for hours when interested",
#                     "Slightly shorter but manageable",
#                     "Noticeably fragmented - need frequent stimulation",
#                     "Very difficult - mind wanders constantly",
#                     "Almost impossible without background digital stimulation"
#                 ],
#                 "attention_fragmentation": [0, 1, 2, 3, 4],
#                 "phase": "digital_screening"
#             }
#         }

#     def _get_engagement_questions(self):
#         """Phase 2: Engagement & Initial Pattern Detection"""
#         return {
#             9: {
#                 "text": "What made you decide to explore hypnotherapy for this particular issue?",
#                 "type": "single_choice",
#                 "options": [
#                     "I've tried other approaches without lasting success",
#                     "I want faster results than traditional methods",
#                     "Something about the subconscious mind approach appeals to me",
#                     "Someone recommended it specifically for my type of issue",
#                     "I'm curious but also skeptical about whether it will work"
#                 ],
#                 "pattern_triggers": {
#                     0: [5], 1: [5], 2: [3], 3: [8], 4: [3]
#                 },
#                 "phase": "engagement"
#             },
#             10: {
#                 "text": "If this issue completely resolved, what would be different about your daily life?",
#                 "type": "text_completion",
#                 "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
#                 "min_chars": 3,
#                 "pattern_analysis": True,
#                 "keywords": {
#                     "productivity": [5], "relationships": [2, 3, 6, 7], "peace": [1], 
#                     "authentic": [6], "happy": [1], "control": [2, 4], "boundaries": [7, 9]
#                 },
#                 "phase": "engagement"
#             },
#             11: {
#                 "text": "How ready are you to completely let go of this pattern?",
#                 "type": "scale_10",
#                 "labels": ["Not ready at all", "Completely ready"],
#                 "follow_up_trigger": 7,  # If 7 or below, ask follow-up
#                 "phase": "engagement"
#             },
#             12: {
#                 "text": "When did this issue most recently show up?",
#                 "type": "single_choice",
#                 "options": [
#                     "Today",
#                     "Yesterday", 
#                     "This week",
#                     "Last week",
#                     "I can't recall the last specific time"
#                 ],
#                 "pattern_triggers": {
#                     4: [1, 6]  # Can't recall suggests normalization or compartmentalization
#                 },
#                 "phase": "engagement"
#             },
#             13: {
#                 "text": "This issue tends to show up more:",
#                 "type": "single_choice",
#                 "options": [
#                     "At work or in professional settings",
#                     "In family or close relationships",
#                     "In social situations with acquaintances", 
#                     "When I'm alone with my thoughts",
#                     "Across all situations equally"
#                 ],
#                 "pattern_triggers": {
#                     0: [5, 8], 1: [7, 8, 9], 2: [2, 3, 6], 3: [1], 4: [1, 4]
#                 },
#                 "phase": "engagement"
#             }
#         }

#     def _get_trigger_mapping_questions(self):
#         """Phase 3: Core Trigger Mapping"""
#         return {
#             14: {
#                 "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
#                 "type": "text_completion",
#                 "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
#                 "min_chars": 5,
#                 "trigger_analysis": True,
#                 "phase": "trigger_mapping"
#             },
#             15: {
#                 "text": "In that situation, what did you notice first?",
#                 "type": "single_choice",
#                 "options": [
#                     "A physical sensation somewhere in my body",
#                     "A specific thought or worry popping up",
#                     "An emotional shift or feeling change",
#                     "Something another person said or did",
#                     "A change in the environment around me"
#                 ],
#                 "chain_mapping": "awareness_point",
#                 "phase": "trigger_mapping"
#             },
#             16: {
#                 "text": "When this pattern activates, the first physical sensation is usually:",
#                 "type": "single_choice_with_intensity",
#                 "options": [
#                     "Chest tightness, racing heart, or breathing changes",
#                     "Stomach drop, nausea, or digestive upset", 
#                     "Muscle tension, jaw clenching, or physical rigidity",
#                     "Hot/cold flashes, sweating, or temperature changes",
#                     "Numbness, disconnection, or feeling 'outside yourself'",
#                     "Restlessness, fidgeting, or urge to move/escape",
#                     "Fatigue, heaviness, or sudden energy drain"
#                 ],
#                 "pattern_indicators": {
#                     0: [1, 3, 4], 1: [1, 3, 4], 2: [2, 5], 3: [2, 5], 
#                     4: [6, 9], 5: [2, 5], 6: [1, 7]
#                 },
#                 "chain_mapping": "physical_response",
#                 "phase": "trigger_mapping"
#             },
#             17: {
#                 "text": "What thought automatically appears when you feel that physical sensation?",
#                 "type": "text_completion",
#                 "placeholder": "The actual words that go through your mind - even if they seem harsh or unreasonable. What does your inner voice say?",
#                 "min_chars": 3,
#                 "pattern_keywords": {
#                     "not good enough": [1], "fight": [2], "can't trust": [3], 
#                     "either or": [4], "must do": [5], "can't be real": [6],
#                     "others need": [7], "should": [8], "can't handle": [9]
#                 },
#                 "chain_mapping": "automatic_thought",
#                 "phase": "trigger_mapping"
#             },
#             18: {
#                 "text": "After that thought, you typically feel:",
#                 "type": "multi_select_weighted",
#                 "max_selections": 3,
#                 "options": [
#                     "Anxious or worried", "Angry or frustrated", "Ashamed or embarrassed",
#                     "Sad or defeated", "Guilty or self-blaming", "Overwhelmed or panicked",
#                     "Numb or disconnected", "Confused or uncertain"
#                 ],
#                 "chain_mapping": "emotional_response",
#                 "phase": "trigger_mapping"
#             },
#             19: {
#                 "text": "When you feel that emotion at that intensity, you typically:",
#                 "type": "single_choice",
#                 "options": [
#                     "Withdraw, avoid, or postpone dealing with it",
#                     "Become more active, busy, or productive",
#                     "Seek reassurance or validation from others",
#                     "Become argumentative or defensive", 
#                     "Try to control or fix the situation",
#                     "Please others or put their needs first",
#                     "Shut down emotionally or 'check out'",
#                     "Analyze or overthink the situation"
#                 ],
#                 "pattern_mapping": {
#                     0: [1, 4, 9], 1: [5], 2: [3, 7], 3: [2], 
#                     4: [2, 5], 5: [7], 6: [6, 9], 7: [4, 5]
#                 },
#                 "chain_mapping": "behavioral_response",
#                 "phase": "trigger_mapping"
#             },
#             20: {
#                 "text": "Right after you respond that way, you usually feel:",
#                 "type": "single_choice",
#                 "options": [
#                     "Temporary relief but underlying tension remains",
#                     "More agitated or upset than before",
#                     "Emotionally numb or disconnected",
#                     "Guilty about how you handled it",
#                     "Justified in your response",
#                     "Confused about what just happened",
#                     "Physically exhausted or drained"
#                 ],
#                 "chain_mapping": "immediate_consequence",
#                 "phase": "trigger_mapping"
#             },
#             21: {
#                 "text": "A few hours later, you're typically:",
#                 "type": "single_choice", 
#                 "options": [
#                     "Have moved on and forgotten about it",
#                     "Still replaying what happened",
#                     "Planning how to avoid it next time",
#                     "Angry at yourself for reacting that way",
#                     "Feeling misunderstood by others involved",
#                     "Resigned that this is just how things are"
#                 ],
#                 "pattern_reinforcement": {
#                     1: [5], 2: [1, 4, 9], 3: [5], 4: [1], 5: [1]
#                 },
#                 "chain_mapping": "longer_term_impact",
#                 "phase": "trigger_mapping"
#             }
#         }

#     def _get_pattern_specific_questions(self):
#         """Phase 4: Adaptive Pattern-Specific Deep Dives"""
#         return {
#             # Pattern 1: Unhappiness Culture
#             "pattern_1": {
#                 22: {
#                     "text": "When something genuinely good happens to you, your first reaction is usually:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Pure enjoyment and celebration",
#                         "Immediately looking for the catch or downside", 
#                         "Feeling guilty or undeserving of good things",
#                         "Minimizing its importance",
#                         "Anxiety about when it will end"
#                     ],
#                     "weights": [0, 3, 3, 2, 2],
#                     "pattern": 1
#                 },
#                 23: {
#                     "text": "Growing up, the message about happiness in your family was:",
#                     "type": "single_choice",
#                     "options": [
#                         "Happiness is natural and should be enjoyed",
#                         "Happiness must be earned through hard work",
#                         "Too much happiness leads to disappointment", 
#                         "Other people's happiness comes first",
#                         "Happiness is selfish or shallow"
#                     ],
#                     "weights": [0, 2, 3, 2, 3],
#                     "pattern": 1
#                 },
#                 24: {
#                     "text": "What would you lose if you allowed yourself to be genuinely happy?",
#                     "type": "text_completion",
#                     "placeholder": "Think about identity, relationships, what others might think, or what might change...",
#                     "min_chars": 3,
#                     "pattern": 1
#                 }
#             },
            
#             # Pattern 2: Power Struggles
#             "pattern_2": {
#                 25: {
#                     "text": "When someone disagrees with you, your nervous system:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Stays curious about their perspective",
#                         "Immediately activates into combat mode",
#                         "Feels threatened or attacked",
#                         "Shuts down to avoid confrontation",
#                         "Searches for ways to prove them wrong"
#                     ],
#                     "weights": [0, 3, 2, 1, 3],
#                     "pattern": 2
#                 },
#                 26: {
#                     "text": "In your family growing up, disagreements typically:",
#                     "type": "single_choice",
#                     "options": [
#                         "Were handled through calm discussion",
#                         "Escalated into arguments or fights",
#                         "Were avoided at all costs",
#                         "Involved guilt, manipulation, or silent treatment",
#                         "Had clear winners and losers"
#                     ],
#                     "weights": [0, 3, 2, 3, 4],
#                     "pattern": 2
#                 }
#             },
            
#             # Pattern 3: Systematic Mistrust
#             "pattern_3": {
#                 27: {
#                     "text": "When meeting new people, you assume they:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Are generally well-intentioned",
#                         "Are judging or evaluating you",
#                         "Want something from you",
#                         "Will eventually disappoint you",
#                         "Are basically indifferent"
#                     ],
#                     "weights": [0, 2, 3, 3, 1],
#                     "pattern": 3
#                 },
#                 28: {
#                     "text": "When someone is unexpectedly kind to you, you:",
#                     "type": "single_choice",
#                     "options": [
#                         "Feel grateful and warmed",
#                         "Wonder what they want from you",
#                         "Feel suspicious of their motives",
#                         "Feel unworthy of their kindness",
#                         "Barely notice or dismiss it"
#                     ],
#                     "weights": [0, 3, 3, 2, 1],
#                     "pattern": 3
#                 }
#             },
            
#             # Pattern 4: Separation/Division
#             "pattern_4": {
#                 29: {
#                     "text": "When facing important decisions, you typically:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "See multiple creative possibilities",
#                         "Feel trapped between two impossible choices",
#                         "Get paralyzed by perfectionist analysis",
#                         "Create artificial deadlines or urgency",
#                         "Defer to what others expect"
#                     ],
#                     "weights": [0, 2, 3, 2, 1],
#                     "pattern": 4
#                 }
#             },
            
#             # Pattern 5: Doing vs Being
#             "pattern_5": {
#                 30: {
#                     "text": "You feel most valuable when you're:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Simply existing as yourself",
#                         "Accomplishing something significant",
#                         "Being productive or busy",
#                         "Helping others achieve their goals",
#                         "Receiving recognition for your work"
#                     ],
#                     "weights": [0, 2, 3, 2, 2],
#                     "pattern": 5
#                 }
#             },
            
#             # Pattern 6: Compartmentalized Authenticity
#             "pattern_6": {
#                 31: {
#                     "text": "Your personality tends to:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Stay consistent across all situations",
#                         "Shift significantly based on who you're with",
#                         "Change between professional and personal settings",
#                         "Adapt to what others seem to want",
#                         "Feel fragmented or inconsistent"
#                     ],
#                     "weights": [0, 2, 2, 3, 4],
#                     "pattern": 6
#                 }
#             },
            
#             # Pattern 7: Self-Sacrifice/Care Avoidance
#             "pattern_7": {
#                 32: {
#                     "text": "When it comes to your own needs versus others' needs:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "I naturally balance both",
#                         "Others' needs usually come first",
#                         "I feel guilty focusing on my own needs",
#                         "I often don't even know what I need",
#                         "Taking care of myself feels selfish"
#                     ],
#                     "weights": [0, 2, 3, 3, 4],
#                     "pattern": 7
#                 }
#             },
            
#             # Pattern 8: Inherited Missions
#             "pattern_8": {
#                 33: {
#                     "text": "Your major life goals are primarily:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Based on your own genuine desires",
#                         "Influenced by family expectations",
#                         "Meant to honor someone's sacrifices",
#                         "Designed to prove your worth",
#                         "A reaction against others' expectations"
#                     ],
#                     "weights": [0, 2, 3, 3, 2],
#                     "pattern": 8
#                 }
#             },
            
#             # Pattern 9: Context-Dependent Weakness
#             "pattern_9": {
#                 34: {
#                     "text": "Your boundaries and limits:",
#                     "type": "single_choice_with_intensity",
#                     "options": [
#                         "Stay pretty consistent across situations",
#                         "Vary significantly based on who you're with",
#                         "Disappear completely in certain contexts",
#                         "Are stronger in some areas than others",
#                         "Feel almost non-existent sometimes"
#                     ],
#                     "weights": [0, 2, 3, 2, 4],
#                     "pattern": 9
#                 }
#             }
#         }

#     def _get_integration_questions(self):
#         """Phase 5: Integration & Change Readiness"""
#         return {
#             35: {
#                 "text": "If you had to guess, this pattern might be trying to:",
#                 "type": "single_choice",
#                 "options": [
#                     "Protect you from emotional pain",
#                     "Keep you safe from rejection or judgment",
#                     "Maintain some sense of control",
#                     "Help you belong or fit in",
#                     "Avoid disappointing important people",
#                     "Ensure you're prepared for worst-case scenarios"
#                 ],
#                 "secondary_gain": True,
#                 "phase": "integration"
#             },
#             36: {
#                 "text": "What would need to be true for you to feel completely safe changing this pattern?",
#                 "type": "text_completion",
#                 "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
#                 "min_chars": 3,
#                 "safety_assessment": True,
#                 "phase": "integration"
#             },
#             37: {
#                 "text": "When learning or changing, you respond best to:",
#                 "type": "single_choice",
#                 "options": [
#                     "Direct, clear guidance and instructions",
#                     "Gentle, permissive suggestions",
#                     "Stories, metaphors, and imagery",
#                     "Logical explanations and understanding",
#                     "Collaborative exploration and discovery"
#                 ],
#                 "hypnotic_preference": True,
#                 "phase": "integration"
#             },
#             38: {
#                 "text": "Imagine you've completely transformed this pattern. What's the first thing you'd do that you can't do now?",
#                 "type": "text_completion",
#                 "placeholder": "Be specific about the first action, conversation, or decision you'd make...",
#                 "min_chars": 5,
#                 "outcome_visualization": True,
#                 "phase": "integration"
#             }
#         }

#     # ---- algorithmical divide Analysis Methods ----
#     def _analyze_digital_despair_indicators(self, responses):
#         """Analyze responses for algorithmical divide Syndrome indicators"""
        
#         # Age factor (digital native status)
#         age_response = responses.get(0, {}).get('response', '')
#         digital_native_score = 0
        
#         age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
#         scoring = [3, 5, 4, 3, 2, 1, 0, 0]
        
#         try:
#             age_index = age_options.index(age_response)
#             digital_native_score = scoring[age_index]
#         except (ValueError, IndexError):
#             digital_native_score = 0
        
#         # Determine if digital native assessment was triggered
#         if digital_native_score < 2:
#             return None  # Skip algorithmical divide analysis for non-digital natives
        
#         # Extract component scores
#         reality_dissociation = self._extract_reality_dissociation_score(responses)
#         binary_thinking = self._extract_binary_success_score(responses) 
#         ironic_detachment = self._extract_ironic_detachment_score(responses)
#         algorithmic_dependency = self._extract_algorithmic_dependency_score(responses)
#         nihilistic_worldview = self._extract_nihilistic_worldview_score(responses)
#         hope_avoidance = self._extract_hope_avoidance_score(responses)
#         attention_fragmentation = self._extract_attention_fragmentation_score(responses)
        
#         # Calculate composite algorithmical divide Score
#         total_possible = 35  # Maximum possible score across all indicators
#         raw_score = (digital_native_score + reality_dissociation + binary_thinking + 
#                      ironic_detachment + algorithmic_dependency + nihilistic_worldview + 
#                      hope_avoidance + attention_fragmentation)
        
#         digital_despair_percentage = (raw_score / total_possible) * 100
        
#         # Severity classification
#         if digital_despair_percentage >= 70:
#             severity = "SEVERE"
#             recommendation = "Specialized digital-native intervention required"
#         elif digital_despair_percentage >= 50:
#             severity = "MODERATE" 
#             recommendation = "Modified approach with digital awareness"
#         elif digital_despair_percentage >= 30:
#             severity = "MILD"
#             recommendation = "Standard approach with digital considerations"
#         else:
#             severity = "MINIMAL"
#             recommendation = "Traditional hypnotherapy approach suitable"
        
#         return {
#             'digital_despair_score': digital_despair_percentage,
#             'severity_level': severity,
#             'clinical_recommendation': recommendation,
#             'component_scores': {
#                 'digital_native_status': digital_native_score,
#                 'reality_dissociation': reality_dissociation,
#                 'binary_success_pressure': binary_thinking,
#                 'ironic_detachment': ironic_detachment, 
#                 'algorithmic_dependency': algorithmic_dependency,
#                 'nihilistic_worldview': nihilistic_worldview,
#                 'hope_avoidance': hope_avoidance,
#                 'attention_fragmentation': attention_fragmentation
#             },
#             'therapeutic_adaptations_needed': self._get_therapeutic_adaptations(severity)
#         }

#     def _get_therapeutic_adaptations(self, severity):
#         """Get required therapeutic adaptations based on algorithmical divide severity"""
        
#         adaptations = {
#             "SEVERE": [
#                 "Attention span optimization: 15-30 minute focused segments",
#                 "Anti-authority language: Collaborative, non-directive approach",
#                 "Ironic armor dissolution: Validate intelligence while accessing authentic emotion",
#                 "Digital bridge-building: Connect online competencies to offline confidence",
#                 "Binary thinking interruption: Install 'both/and' processing patterns",
#                 "Hope introduction protocol: Gradual realistic optimism vs. overwhelming positivity",
#                 "Meaning-making assistance: Personal contribution vs. extraordinary achievement"
#             ],
#             "MODERATE": [
#                 "Modified session length: 45-60 minutes with movement breaks",
#                 "Authority resistance awareness: Reduce directive language", 
#                 "Cynicism validation: Acknowledge systemic problems while building agency",
#                 "Digital competency honor: Validate online achievements and skills",
#                 "Nuanced goal-setting: Meaningful vs. extraordinary success redefinition",
#                 "Gradual hope building: Evidence-based optimism introduction"
#             ],
#             "MILD": [
#                 "Digital literacy integration: Use familiar cultural references",
#                 "Achievement pressure awareness: Expand success definitions",
#                 "Authentic expression permission: Reduce 'cringe' about sincerity",
#                 "Real-world confidence transfer: Apply online skills offline"
#             ],
#             "MINIMAL": [
#                 "Standard approach with generational awareness",
#                 "Technology balance considerations",
#                 "Modern stress factor acknowledgment"
#             ]
#         }
        
#         return adaptations.get(severity, adaptations["MINIMAL"])

#     # Helper functions for extracting specific scores
#     def _extract_reality_dissociation_score(self, responses):
#         """Extract reality dissociation indicators from responses"""
#         score = 0
        
#         # Digital vs offline authenticity (question 2)
#         digital_auth_data = responses.get(2, {})
#         digital_auth = digital_auth_data.get('response', '')
        
#         if 'online communities and digital spaces' in digital_auth:
#             score += 3
#         elif 'don\'t feel authentic anywhere' in digital_auth:
#             score += 4
#         elif 'varies completely depending' in digital_auth:
#             score += 2
            
#         # Add intensity multiplier if available
#         intensity = digital_auth_data.get('intensity', 1)
#         if intensity:
#             score *= (intensity / 4)  # Scale intensity 1-7 to multiplier
        
#         return min(5, score)  # Cap at 5 points for this component

#     def _extract_binary_success_score(self, responses):
#         """Extract binary success framework indicators"""
#         score = 0
        
#         success_def = responses.get(3, {}).get('response', '')
#         if 'Extraordinary wealth, fame, or achievement' in success_def:
#             score += 4
#         elif 'Success feels impossible or meaningless' in success_def:
#             score += 4
#         elif 'significantly better than most people' in success_def:
#             score += 3
            
#         return min(5, score)

#     def _extract_ironic_detachment_score(self, responses):
#         """Extract ironic detachment indicators"""
#         score = 0
        
#         emotion_expr_data = responses.get(4, {})
#         emotion_expr = emotion_expr_data.get('response', '')
        
#         if 'embarrassed or \'cringe\' about sincerity' in emotion_expr:
#             score += 3
#         elif 'through memes or online references' in emotion_expr:
#             score += 3
#         elif 'rarely express genuine emotions' in emotion_expr:
#             score += 4
#         elif 'humor or irony to deflect' in emotion_expr:
#             score += 2
        
#         # Apply intensity multiplier
#         intensity = emotion_expr_data.get('intensity', 1)
#         if intensity:
#             score *= (intensity / 4)
        
#         return min(5, score)

#     def _extract_algorithmic_dependency_score(self, responses):
#         """Extract algorithmic emotional regulation indicators"""
#         score = 0
        
#         emotion_source = responses.get(5, {}).get('response', '')
#         if 'Social media feeds and online content' in emotion_source:
#             score += 3
#         elif 'Online communities and digital relationships' in emotion_source:
#             score += 3
            
#         relationship_invest = responses.get(6, {}).get('response', '')
#         if 'Online personalities' in relationship_invest:
#             score += 2
#         elif 'Online friends and communities' in relationship_invest:
#             score += 2
#         elif 'Fictional characters' in relationship_invest:
#             score += 3
            
#         return min(5, score)

#     def _extract_nihilistic_worldview_score(self, responses):
#         """Extract nihilistic worldview indicators"""  
#         score = 0
        
#         # Check success definition for nihilism
#         success_def = responses.get(3, {}).get('response', '')
#         if 'Success feels impossible or meaningless' in success_def:
#             score += 4
            
#         return min(5, score)

#     def _extract_hope_avoidance_score(self, responses):
#         """Extract hope avoidance indicators"""
#         score = 0
        
#         hope_relation_data = responses.get(7, {})
#         hope_relation = hope_relation_data.get('response', '')
        
#         if 'dismiss it as naive or manipulative' in hope_relation:
#             score += 4
#         elif 'annoyed because they don\'t understand reality' in hope_relation:
#             score += 3  
#         elif 'think of reasons why they\'re wrong' in hope_relation:
#             score += 2
        
#         # Apply intensity multiplier
#         intensity = hope_relation_data.get('intensity', 1)
#         if intensity:
#             score *= (intensity / 4)
        
#         return min(5, score)

#     def _extract_attention_fragmentation_score(self, responses):
#         """Extract attention fragmentation indicators"""
#         score = 0
        
#         focus_capacity = responses.get(8, {}).get('response', '')
#         focus_options = [
#             "Same as always - can focus for hours when interested",
#             "Slightly shorter but manageable", 
#             "Noticeably fragmented - need frequent stimulation",
#             "Very difficult - mind wanders constantly",
#             "Almost impossible without background digital stimulation"
#         ]
#         scoring = [0, 1, 2, 3, 4]
        
#         try:
#             focus_index = focus_options.index(focus_capacity)
#             score = scoring[focus_index]
#         except (ValueError, IndexError):
#             score = 0
        
#         return min(5, score)

#     # ---- Pattern Detection and Scoring ----
#     def _analyze_text_for_patterns(self, text, keywords_dict):
#         """Analyze text response for pattern indicators"""
#         text_lower = text.lower()
#         detected_patterns = set()
        
#         for keyword, patterns in keywords_dict.items():
#             if keyword in text_lower:
#                 detected_patterns.update(patterns)
        
#         return detected_patterns

#     def _update_pattern_scores(self, question_id, response, question):
#         """Update pattern scores based on response"""
#         # Handle different question types
#         if question.get('pattern_triggers') and isinstance(response, str):
#             if 'options' in question:
#                 try:
#                     option_index = question['options'].index(response)
#                     if option_index in question['pattern_triggers']:
#                         patterns = question['pattern_triggers'][option_index]
#                         for pattern in patterns:
#                             self._add_pattern_score(pattern, 1.0)
#                 except (ValueError, IndexError):
#                     pass
        
#         elif question.get('pattern_mapping') and isinstance(response, str):
#             if 'options' in question:
#                 try:
#                     option_index = question['options'].index(response)
#                     if option_index in question['pattern_mapping']:
#                         patterns = question['pattern_mapping'][option_index]
#                         for pattern in patterns:
#                             self._add_pattern_score(pattern, 1.5)
#                 except (ValueError, IndexError):
#                     pass
        
#         elif question.get('pattern_keywords') and isinstance(response, str):
#             detected_patterns = self._analyze_text_for_patterns(response, question['pattern_keywords'])
#             for pattern in detected_patterns:
#                 self._add_pattern_score(pattern, 2.0)
        
#         elif question.get('keywords') and isinstance(response, str):
#             detected_patterns = self._analyze_text_for_patterns(response, question['keywords'])
#             for pattern in detected_patterns:
#                 self._add_pattern_score(pattern, 1.0)
        
#         # Handle pattern-specific questions with weights
#         if question.get('pattern') and question.get('weights'):
#             pattern_id = question['pattern']
#             if isinstance(response, str) and 'options' in question:
#                 try:
#                     option_index = question['options'].index(response)
#                     if option_index < len(question['weights']):
#                         weight = question['weights'][option_index]
#                         if weight > 0:
#                             self._add_pattern_score(pattern_id, weight)
#                 except (ValueError, IndexError):
#                     pass

#     def _add_pattern_score(self, pattern_id, score):
#         """Add score to pattern with intensity multiplier if available"""
#         if pattern_id in st.session_state.pattern_scores:
#             st.session_state.pattern_scores[pattern_id] += score
#         else:
#             st.session_state.pattern_scores[pattern_id] = score

#     def _check_adaptive_triggers(self, question_id, response, question):
#         """Check if response triggers adaptive questioning"""
#         # Trigger pattern-specific questions when scores reach threshold
#         for pattern_id, score in st.session_state.pattern_scores.items():
#             if score >= 3.0 and pattern_id not in st.session_state.triggered_patterns:
#                 st.session_state.triggered_patterns.add(pattern_id)
#                 st.session_state.adaptive_paths.append(f"pattern_{pattern_id}")

#     def _save_response(self, q_id, response, question, intensity=None):
#         """Save response and update scoring"""
#         st.session_state.assessment_responses[q_id] = {
#             'response': response,
#             'intensity': intensity,
#             'question_text': question['text'],
#             'question_type': question['type'],
#             'timestamp': datetime.now().isoformat(),
#             'phase': question.get('phase', 'unknown')
#         }
        
#         if intensity:
#             st.session_state.intensity_responses[q_id] = intensity
        
#         # Update chain mapping for trigger sequence
#         if question.get('chain_mapping'):
#             st.session_state.trigger_chain[question['chain_mapping']] = response
        
#         # Store digital responses separately
#         if question.get('phase') == 'digital_screening':
#             st.session_state.digital_responses[q_id] = response
        
#         # Update pattern scores
#         self._update_pattern_scores(q_id, response, question)
        
#         # Check for adaptive triggers
#         self._check_adaptive_triggers(q_id, response, question)
        
#         # Update phase progress
#         phase = question.get('phase', 'unknown')
#         if phase in st.session_state.phase_progress:
#             st.session_state.phase_progress[phase] += 1

#     # ---- Question Navigation Logic ----
#     def _get_next_question(self):
#         """Determine next question based on current phase and responses"""
#         answered = set(st.session_state.assessment_responses.keys())
        
#         # Phase 0: Age Screening (Question 0)
#         if st.session_state.current_phase == 'age_screening':
#             if 0 not in answered:
#                 return 0, self.age_screening_questions[0]
#             else:
#                 # Determine if digital native
#                 age_response = st.session_state.assessment_responses.get(0, {}).get('response', '')
#                 age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
#                 scoring = [3, 5, 4, 3, 2, 1, 0, 0]
                
#                 try:
#                     age_index = age_options.index(age_response)
#                     digital_native_score = scoring[age_index]
#                     st.session_state.is_digital_native = digital_native_score >= 2
#                 except (ValueError, IndexError):
#                     st.session_state.is_digital_native = False
                
#                 # Move to appropriate next phase
#                 if st.session_state.is_digital_native:
#                     st.session_state.current_phase = 'digital_screening'
#                 else:
#                     st.session_state.current_phase = 'engagement'
        
#         # Phase 1: Digital Screening (Questions 1-8) - Only for digital natives
#         if st.session_state.current_phase == 'digital_screening':
#             for q_id in range(1, 9):
#                 if q_id not in answered:
#                     return q_id, self.digital_screening_questions[q_id]
#             st.session_state.current_phase = 'engagement'
        
#         # Phase 2: Engagement (Questions 9-13)
#         if st.session_state.current_phase == 'engagement':
#             for q_id in range(9, 14):
#                 if q_id not in answered:
#                     return q_id, self.engagement_questions[q_id]
#             st.session_state.current_phase = 'trigger_mapping'
        
#         # Phase 3: Trigger Mapping (Questions 14-21)
#         if st.session_state.current_phase == 'trigger_mapping':
#             for q_id in range(14, 22):
#                 if q_id not in answered:
#                     return q_id, self.trigger_mapping_questions[q_id]
#             st.session_state.current_phase = 'pattern_specific'
        
#         # Phase 4: Pattern-Specific Questions
#         if st.session_state.current_phase == 'pattern_specific':
#             for pattern_id in st.session_state.triggered_patterns:
#                 pattern_key = f"pattern_{pattern_id}"
#                 if pattern_key in self.pattern_specific_questions:
#                     pattern_questions = self.pattern_specific_questions[pattern_key]
#                     for q_id, question in pattern_questions.items():
#                         if q_id not in answered:
#                             return q_id, question
#             st.session_state.current_phase = 'integration'
        
#         # Phase 5: Integration (Questions 35-38)
#         if st.session_state.current_phase == 'integration':
#             for q_id in range(35, 39):
#                 if q_id not in answered:
#                     return q_id, self.integration_questions[q_id]
        
#         return None, None

#     def _estimate_total_questions(self):
#         """Estimate total questions based on triggered patterns and digital native status"""
#         base_questions = 1  # age screening
        
#         if st.session_state.is_digital_native:
#             base_questions += 8  # digital screening
        
#         base_questions += 5 + 8 + 4  # engagement + trigger_mapping + integration
#         pattern_questions = len(st.session_state.triggered_patterns) * 2  # avg 2 questions per pattern
#         return base_questions + pattern_questions

#     def _estimate_time_remaining(self):
#         """Estimate remaining time"""
#         total_q = self._estimate_total_questions()
#         answered = len(st.session_state.assessment_responses)
#         remaining = max(0, total_q - answered)
        
#         # Adjust time estimate based on digital native status
#         if st.session_state.is_digital_native and st.session_state.digital_severity == 'SEVERE':
#             return remaining * 0.8  # Faster pacing for digital natives
#         else:
#             return remaining * 1.0

#     # ---- Response Type Handlers ----
#     def _handle_single_choice(self, q_id, question):
#         """Handle single choice questions"""
#         for i, option in enumerate(question['options']):
#             if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
#                 self._save_response(q_id, option, question)
#                 self._advance_question()
#                 st.rerun()

#     def _handle_single_choice_with_intensity(self, q_id, question):
#         """Handle single choice with intensity rating"""
#         selection_key = f"selected_option_{q_id}"
        
#         for i, option in enumerate(question['options']):
#             if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
#                 st.session_state[selection_key] = option
#                 st.rerun()
        
#         if selection_key in st.session_state:
#             selected_option = st.session_state[selection_key]
#             st.success(f"Selected: {selected_option}")
            
#             st.markdown("**How intense is this experience for you?**")
#             intensity = st.select_slider(
#                 "Intensity level:",
#                 options=[1, 2, 3, 4, 5, 6, 7],
#                 format_func=lambda x: f"{x}/7",
#                 value=4,
#                 key=f"q_{q_id}_intensity"
#             )
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.caption("1 = Very mild")
#             with col2:
#                 st.caption("7 = Extremely intense")
            
#             if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                 self._save_response(q_id, selected_option, question, intensity)
#                 if selection_key in st.session_state:
#                     del st.session_state[selection_key]
#                 self._advance_question()
#                 st.rerun()

#     def _handle_multi_select_weighted(self, q_id, question):
#         """Handle multi-select with intensity weighting"""
#         max_sel = question.get('max_selections', len(question['options']))
#         selected = st.multiselect(
#             "Select all that apply:",
#             question['options'],
#             key=f"q_{q_id}_multi",
#             max_selections=max_sel
#         )
        
#         if selected:
#             st.markdown("**Rate the intensity of each selected emotion:**")
#             intensities = {}
#             for emotion in selected:
#                 safe_key = emotion.replace('/', '_').replace(' ', '_')
#                 intensities[emotion] = st.select_slider(
#                     f"{emotion}:",
#                     options=[1, 2, 3, 4, 5, 6, 7],
#                     format_func=lambda x: f"{x}/7",
#                     value=4,
#                     key=f"q_{q_id}_{safe_key}_intensity"
#                 )
            
#             if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                 weighted_response = {emotion: intensities[emotion] for emotion in selected}
#                 self._save_response(q_id, weighted_response, question)
#                 self._advance_question()
#                 st.rerun()

#     def _handle_text_completion(self, q_id, question):
#         """Handle text completion questions"""
#         min_chars = question.get('min_chars', 3)
#         response = st.text_area(
#             "Your response:",
#             placeholder=question.get('placeholder', 'Please share your thoughts...'),
#             key=f"q_{q_id}_text",
#             height=120
#         )
        
#         char_count = len(response.strip())
#         if char_count > 0:
#             sufficient = char_count >= min_chars
#             color_class = "sufficient" if sufficient else "insufficient"
        
#         if char_count >= min_chars:
#             if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#                 self._save_response(q_id, response.strip(), question)
#                 self._advance_question()
#                 st.rerun()
#         elif char_count > 0:
#             st.info(f"Please provide at least {min_chars - char_count} more characters for a complete response.")

#     def _handle_scale_10(self, q_id, question):
#         """Handle 1-10 scale questions"""
#         labels = question.get('labels', ['Low', 'High'])
#         value = st.select_slider(
#             "Rate your readiness:",
#             options=list(range(1, 11)),
#             format_func=lambda x: f"{x}/10",
#             value=5,
#             key=f"q_{q_id}_scale"
#         )
        
#         col1, col2 = st.columns(2)
#         with col1:
#             st.caption(f"1 = {labels[0]}")
#         with col2:
#             st.caption(f"10 = {labels[1]}")
        
#         # Show follow-up if score is low
#         follow_up = ""
#         if value <= question.get('follow_up_trigger', 5):
#             follow_up = st.text_input(
#                 "What would need to happen to make it a 10?",
#                 key=f"q_{q_id}_followup",
#                 placeholder="What would increase your readiness?"
#             )
        
#         if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
#             response_data = {'rating': value, 'follow_up': follow_up}
#             self._save_response(q_id, response_data, question)
#             self._advance_question()
#             st.rerun()

#     def _advance_question(self):
#         """Move to next question"""
#         st.session_state.current_question += 1

#     def _go_back(self):
#         """Go back one question"""
#         if st.session_state.current_question > 1:
#             st.session_state.current_question -= 1
#             if st.session_state.assessment_responses:
#                 last_key = max(st.session_state.assessment_responses.keys())
#                 del st.session_state.assessment_responses[last_key]
#                 if last_key in st.session_state.intensity_responses:
#                     del st.session_state.intensity_responses[last_key]

#     def _complete_assessment(self):
#         """Complete the assessment and prepare results"""
#         st.session_state.assessment_completed = True
        
#         # Analyze algorithmical divide if digital native
#         digital_analysis = None
#         if st.session_state.is_digital_native:
#             digital_analysis = self._analyze_digital_despair_indicators(st.session_state.assessment_responses)
#             if digital_analysis:
#                 st.session_state.digital_despair_score = digital_analysis['digital_despair_score']
#                 st.session_state.digital_severity = digital_analysis['severity_level']
        
#         # Determine dominant pattern
#         dominant_pattern = None
#         if st.session_state.pattern_scores:
#             dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
#         # Compile results
#         st.session_state.assessment_results = {
#             'pattern_scores': dict(st.session_state.pattern_scores),
#             'dominant_pattern': dominant_pattern,
#             'triggered_patterns': list(st.session_state.triggered_patterns),
#             'risk_flags': st.session_state.risk_flags,
#             'completion_timestamp': datetime.now().isoformat(),
#             'total_questions_answered': len(st.session_state.assessment_responses),
#             'adaptive_paths_triggered': st.session_state.adaptive_paths,
#             'intensity_data': dict(st.session_state.intensity_responses),
#             'trigger_chain': dict(st.session_state.trigger_chain),
#             'phase_completion': dict(st.session_state.phase_progress),
#             'is_digital_native': st.session_state.is_digital_native,
#             'digital_despair_analysis': digital_analysis,
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
#         if not st.session_state.assessment_completed:
#             time_remaining = self._estimate_time_remaining()
            
#             # # Show digital native indicator if applicable
#             # if st.session_state.is_digital_native and st.session_state.current_phase != 'age_screening':
#             #     st.markdown("""
#             #     <div class="digital-indicator">
#             #     🖥️ Digital-native assessment active - specialized approach enabled
#             #     </div>
#             #     """, unsafe_allow_html=True)
            
#             st.info(f"Understanding **your unique behavioral patterns** is the key to **targeted, effective hypnotherapy** that brings rapid, lasting change. This assessment takes about {time_remaining:.0f} minutes to complete.")
#             st.markdown("<h2 style='text-align: center;'>Behavioral pattern assessment</h1>", unsafe_allow_html=True)

#     def _render_current_question(self):
#         """Render the current question with progress tracking"""
#         q_id, question = self._get_next_question()
        
#         if q_id is None:
#             self._complete_assessment()
#             return
        
#         if not question:
#             st.error("Question configuration error")
#             return

#         # Progress tracking
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
#         <div class="time-estimate"> ~ {time_remaining:.0f} minutes remaining</div>
#         """, unsafe_allow_html=True)

#         # Phase indicator
#         current_phase = question.get('phase', 'unknown')
#         phase_names = {
#             'age_screening': 'Initial Screening',
#             'digital_screening': 'Digital Pattern Assessment',
#             'engagement': 'Pattern Discovery',
#             'trigger_mapping': 'Trigger Analysis',
#             'pattern_specific': 'Deep Pattern Exploration',
#             'integration': 'Integration & Planning'
#         }
#         phase_display = phase_names.get(current_phase, current_phase.title())
        
#         # if current_phase != 'age_screening':
#         #     st.caption(f"**Phase:** {phase_display}")

#         # Question display
#         st.markdown(f"### {question['text']}")
        
#         # Show pattern detection hints for engaged users
#         if completed > 8 and st.session_state.pattern_scores:
#             top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
#             if top_pattern[1] >= 2.0:
#                 pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
#                 # Only show hints in later phases to avoid influencing responses

#         # Handle different question types
#         q_type = question['type']
#         if q_type == 'single_choice':
#             self._handle_single_choice(q_id, question)
#         elif q_type == 'single_choice_with_intensity':
#             self._handle_single_choice_with_intensity(q_id, question)
#         elif q_type == 'multi_select_weighted':
#             self._handle_multi_select_weighted(q_id, question)
#         elif q_type == 'text_completion':
#             self._handle_text_completion(q_id, question)
#         elif q_type == 'scale_10':
#             self._handle_scale_10(q_id, question)

#         self._render_navigation(q_id)

#     def _render_navigation(self, current_q_id):
#         """Render navigation controls"""
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
#             # Only allow skipping after age screening
#             if current_q_id > 0:
#                 if st.button("Skip", key="nav_skip", use_container_width=True):
#                     skip_question = {"text": "Skipped", "type": "skip", "phase": "skip"}
#                     self._save_response(current_q_id, "Skipped", skip_question)
#                     self._advance_question()
#                     st.rerun()

#     def _render_contact_form(self):
#         """Render contact form for results with enhanced clinical data"""
#         #st.markdown("### Assessment complete!")
#         st.success("Your comprehensive behavioral pattern analysis is ready!")
        
#         results = st.session_state.assessment_results
        
#         # Show different metrics based on assessment type
#         if st.session_state.is_digital_native:
#             col1, col2, col3, col4 = st.columns(4)
#             with col1:
#                 st.metric("", "Questions answered", results['total_questions_answered'])
#             with col2:
#                 st.metric("", "Patterns detected", len(results.get('pattern_scores', {})))
#             with col3:
#                 digital_score = st.session_state.get('digital_despair_score', 0)
#                 severity = st.session_state.get('digital_severity', 'MINIMAL')
                
#                 # Add severity descriptions
#                 severity_descriptions = {
#                     'SEVERE': 'Specialized intervention required',
#                     'MODERATE': 'Enhanced approach needed',
#                     'MILD': 'Standard with modifications', 
#                     'MINIMAL': 'Traditional approach suitable'
#                 }
#                 description = severity_descriptions.get(severity, 'Assessment incomplete')
                
#                 st.metric("Digital patterns", f"{severity}", f"{digital_score:.0f}%")
#                 st.caption(description)
#             with col4:
#                 completion_rate = results.get('completion_rate', 1.0)
#                 st.metric("", "Completion rate", f"{completion_rate*100:.0f}%")
#         else:
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("", "Questions answered", results['total_questions_answered'])
#             with col2:
#                 st.metric("", "Patterns detected", len(results.get('pattern_scores', {})))
#             with col3:
#                 completion_rate = results.get('completion_rate', 1.0)
#                 st.metric("", "Completion rate", f"{completion_rate*100:.0f}%")
        
#         st.markdown("**Enter your email to receive your personalized analysis and next steps:**")
        
#         with st.form("contact_form"):
#             # ONLY EMAIL IS MANDATORY
#             email = st.text_input("Email*", placeholder="your@email.com")
            
#             # ALL OTHER FIELDS ARE OPTIONAL
#             name = st.text_input("Full name (optional)", placeholder="Your full name")
#             phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")

#             concern = st.text_area(
#                 "What brought you to this assessment? (optional)",
#                 placeholder="Brief description of what motivated you to take this assessment...",
#                 height=100
#             )
            
#             urgency = st.selectbox(
#                 "How urgent is addressing this pattern? (optional)",
#                 ["Not specified", "Extremely urgent - significantly impacting life", 
#                  "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
#                  "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
#             )
            
#             next_step = st.selectbox(
#                 "Preferred next step (optional)",
#                 ["Not specified", "Schedule free consultation call", 
#                  "Information about transformation packages", "Receive analysis and recommendations first", 
#                  "Connect with clinical team directly"]
#             )
            
#             marketing_consent = st.checkbox(
#                 "I consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
#             )
            
#             submit_button_html = """
#             <style>
#             .custom-submit-button {
#                 background-color: #4CA1A3 !important;
#                 color: #FFFFFF !important;
#                 border: 2px solid #4CA1A3 !important;
#                 border-radius: 8px !important;
#                 padding: 12px 24px !important;
#                 font-size: 1rem !important;
#                 font-weight: 600 !important;
#                 width: 100% !important;
#                 margin: 8px 0 !important;
#                 cursor: pointer !important;
#                 transition: all 0.3s ease !important;
#                 text-align: center !important;
#                 min-height: 2.5rem !important;
#             }
            
#             .custom-submit-button:hover {
#                 background-color: #E1F0F0 !important;
#                 color: #273548 !important;
#                 border-color: #E1F0F0 !important;
#                 transform: translateY(-1px) !important;
#                 box-shadow: 0 4px 12px rgba(243,246,248,0.6) !important;
#             }
#             </style>
#             """
#             st.markdown(submit_button_html, unsafe_allow_html=True)
            
#             # Use the regular streamlit submit button but with custom styling
#             submitted = st.form_submit_button("Get my personalized analysis", type="primary", use_container_width=True)


#             if submitted:
#                 errors = []
                
#                 # ONLY EMAIL VALIDATION IS REQUIRED
#                 if not email.strip(): 
#                     errors.append("Email is required")
#                 elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#                     errors.append("Valid email address is required")
                
#                 # MARKETING CONSENT CHECK
#                 if not marketing_consent:
#                     errors.append("Please consent to follow-up communications to receive your results")
                
#                 if errors:
#                     for error in errors:
#                         st.error(f"❌ {error}")
#                 else:
#                     # Save contact info with optional fields defaulting to empty/not specified
#                     st.session_state.contact_info = {
#                         'name': name.strip() if name.strip() else 'Not provided',
#                         'email': email.strip(),
#                         'phone': phone.strip() if phone.strip() else 'Not provided',
#                         'urgency': urgency if urgency != 'Not specified' else 'Not specified',
#                         'primary_concern': concern.strip() if concern.strip() else 'Not provided',
#                         'next_step': next_step if next_step != 'Not specified' else 'Not specified',
#                         'marketing_consent': marketing_consent,
#                         'timestamp': datetime.now().isoformat()
#                     }
                    
#                     # GENERATE COMPREHENSIVE CLINICAL TEMPLATE
#                     clinical_template = self._format_comprehensive_clinical_template()
                    
#                     # Prepare assessment data for email with enhanced clinical template
#                     assessment_data = {
#                         'contact_info': st.session_state.contact_info,
#                         'assessment_results': st.session_state.assessment_results,
#                         'responses': st.session_state.assessment_responses,
#                         'assessment_responses': st.session_state.assessment_responses,
#                         'intensity_responses': st.session_state.intensity_responses,
#                         'adaptive_triggered': st.session_state.adaptive_paths,
#                         'risk_flags': st.session_state.risk_flags,
#                         'pattern_scores': st.session_state.pattern_scores,
#                         'trigger_chain': st.session_state.trigger_chain,
#                         'digital_responses': st.session_state.digital_responses,
#                         'is_digital_native': st.session_state.is_digital_native,
#                         'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis'),
#                         'clinical_template': clinical_template,
#                         'start_time': st.session_state.start_time,
#                         'completion_timestamp': datetime.now().isoformat()
#                     }
                    
#                     # Send comprehensive clinical assessment email
#                     try:
#                         from utils.email_assess import send_clinical_assessment_results
                        
#                         email_success = send_clinical_assessment_results(assessment_data)
                        
#                         if email_success:
#                             st.success("✅ Assessment completed and clinical team notified!")
#                             st.info("📧 Your detailed analysis has been sent to our clinical team for review.")
#                         else:
#                             st.warning("⚠️ Assessment saved, but email notification failed. Our team will still receive your results.")
                            
#                     except ImportError as e:
#                         st.error(f"Email system unavailable: {e}")
#                         st.info("Assessment completed! Our clinical team will review your results.")
#                     except Exception as e:
#                         st.error(f"Email error: {str(e)}")
                    
#                     st.session_state.contact_provided = True
#                     st.rerun()

#     def _format_comprehensive_clinical_template(self):
#         """Format comprehensive clinical template integrating traditional patterns + digital analysis"""
#         # Extract all clinical insights
#         clinical_insights = self._extract_clinical_insights()
        
#         # Get pattern scores and session planning
#         pattern_scores = st.session_state.pattern_scores
#         session_plan = self._generate_session_plan(pattern_scores, clinical_insights)
        
#         # Get top 3 patterns
#         if pattern_scores:
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
#             dominant_pattern = self.patterns.get(sorted_patterns[0][0], "Unknown") if sorted_patterns else "Unknown"
#             dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
            
#             primary_pattern = self.patterns.get(sorted_patterns[1][0], "Unknown") if len(sorted_patterns) > 1 else "None detected"
#             primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
            
#             secondary_pattern = self.patterns.get(sorted_patterns[2][0], "Unknown") if len(sorted_patterns) > 2 else "None detected"
#             secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
#         else:
#             dominant_pattern = primary_pattern = secondary_pattern = "Assessment incomplete"
#             dominant_score = primary_score = secondary_score = 0
        
#         # Get change readiness
#         readiness_score = 5  # Default
#         for response_data in st.session_state.assessment_responses.values():
#             if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
#                 readiness_score = response_data['response']['rating']
#                 break
        
#         # Generate behavioral sequence analysis
#         behavioral_sequence = self._generate_behavioral_sequence_analysis()
        
#         # Build base template
#         template = f"""
# ╔══════════════════════════════════════════════════════════════╗
# ║                    CLINICAL ANALYSIS TEMPLATE                ║
# ║          Enhanced Behavioral Pattern Assessment              ║
# ╚══════════════════════════════════════════════════════════════╝

# **TRADITIONAL PATTERN ANALYSIS:**
# Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
# Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10) 
# Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

# **PSYCHOLOGICAL PROFILE:**
# Core Limiting Belief: {clinical_insights.get('core_limiting_belief', 'Requires session exploration')}
# Hidden Benefits: {clinical_insights.get('hidden_benefits', 'Emotional protection and familiar identity')}
# Systemic Resistance: {clinical_insights.get('systemic_resistance', 'Minimal resistance expected')}
# Identity Threat: {clinical_insights.get('identity_threat', 'Identity evolution requires navigation')}

# **CHANGE READINESS:**
# Readiness Score: {readiness_score}/10
# Motivation Level: {"HIGH" if readiness_score >= 8 else "MODERATE" if readiness_score >= 6 else "REQUIRES BUILDING"}
# """
        
#         # Add digital despair analysis if applicable
#         if st.session_state.is_digital_native:
#             digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
#             if digital_analysis:
#                 digital_score = digital_analysis['digital_despair_score']
#                 severity = digital_analysis['severity_level']
                
#                 template += f"""

# ╔══════════════════════════════════════════════════════════════╗
# ║               DIGITAL DESPAIR SYNDROME ANALYSIS             ║
# ╚══════════════════════════════════════════════════════════════╝

# **SYNDROME ASSESSMENT:**
# Algorithmical divide Score: {digital_score:.1f}% ({severity} severity)
# Clinical Recommendation: {digital_analysis['clinical_recommendation']}

# **SYNDROME COMPONENTS:**"""
                
#                 components = digital_analysis['component_scores']
#                 component_names = {
#                     'digital_native_status': 'Digital Native Conditioning',
#                     'reality_dissociation': 'Online vs Offline Authenticity Gap',
#                     'binary_success_pressure': 'Extraordinary Achievement Pressure',
#                     'ironic_detachment': 'Emotional Protection Through Cynicism',
#                     'algorithmic_dependency': 'Social Media Emotional Regulation',
#                     'nihilistic_worldview': 'Hopelessness and Meaning Crisis',
#                     'hope_avoidance': 'Resistance to Optimism',
#                     'attention_fragmentation': 'Digital Attention Conditioning'
#                 }
                
#                 for comp, score in components.items():
#                     name = component_names.get(comp, comp)
#                     level = "HIGH" if score >= 4 else "MEDIUM" if score >= 2 else "LOW"
#                     template += f"\n• {name}: {level} ({score:.1f}/5)"
                
#                 template += f"""

# **REQUIRED THERAPEUTIC ADAPTATIONS:**
# {"🚨 SPECIALIZED INTERVENTION REQUIRED" if severity in ['SEVERE', 'MODERATE'] else "✅ STANDARD APPROACH WITH MODIFICATIONS"}
# """
                
#                 adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
#                 for i, adaptation in enumerate(adaptations[:5], 1):
#                     template += f"\n{i}. {adaptation}"
                
#                 if severity in ['SEVERE', 'MODERATE']:
#                     template += f"""

# **DIGITAL-NATIVE SESSION MODIFICATIONS:**
# • Session Structure: {"20-minute focused segments" if severity == 'SEVERE' else "45-60 minutes with breaks"}
# • Language Style: Collaborative, non-directive, intelligence-validating
# • Authority Approach: Peer consultant vs traditional therapist-patient
# • Hope Introduction: Evidence-based gradual vs overwhelming positivity
# • Success Framework: Meaningful contribution vs extraordinary achievement
# • Resistance Management: Expect intellectual challenges and cynicism
# """

#         template += f"""

# **SESSION PLANNING:**
# Session 1 Focus: {session_plan.get('session_1_focus', 'Pattern analysis and rapport building')}
# Session 2 Target: {session_plan.get('session_2_target', 'Core transformation and positive programming')}
# Potential Session 3 Need: {session_plan.get('session_3_need', 'Reinforcement if needed')}

# **THERAPEUTIC APPROACH:**
# Intervention Keywords: {clinical_insights.get('intervention_keywords', 'Collaborative, gentle, permissive')}
# Avoid Language: {clinical_insights.get('avoid_language', 'Pressure, criticism, commands')}
# Predicted Resistance: {clinical_insights.get('resistance_points', ['Standard change resistance'])[0] if clinical_insights.get('resistance_points') else 'Standard patterns'}

# {behavioral_sequence}

# **SUCCESS PROBABILITY:**
# Estimated Success Rate: {self._calculate_comprehensive_success_rate()}%
# Based on: Pattern complexity, digital factors, readiness, completion rate

# ╔══════════════════════════════════════════════════════════════╗
# ║                     CLINICAL NOTES                          ║
# ╚══════════════════════════════════════════════════════════════╝

# {"This assessment reveals a digital-native psychology requiring specialized intervention approaches. Traditional methods may fail without proper adaptations." if st.session_state.is_digital_native and st.session_state.assessment_results.get('digital_despair_analysis', {}).get('severity_level') in ['SEVERE', 'MODERATE'] else "This comprehensive analysis provides framework for effective hypnotherapy intervention based on traditional behavioral pattern constellation."}
# """
        
#         return template

#     def _calculate_comprehensive_success_rate(self):
#         """Calculate comprehensive success rate including digital factors"""
#         base_rate = 85  # Standard hypnotherapy success rate
        
#         # Adjust for pattern complexity
#         pattern_count = len(st.session_state.pattern_scores)
#         if pattern_count >= 5:
#             base_rate -= 10
#         elif pattern_count >= 3:
#             base_rate -= 5
        
#         # Adjust for digital despair factors
#         if st.session_state.is_digital_native:
#             digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
#             if digital_analysis:
#                 severity = digital_analysis['severity_level']
#                 if severity == 'SEVERE':
#                     base_rate -= 15
#                     base_rate += 10  # But add back for proper adaptations
#                 elif severity == 'MODERATE':
#                     base_rate -= 8
#                     base_rate += 8   # Adaptations help
        
#         # Adjust for readiness
#         for response_data in st.session_state.assessment_responses.values():
#             if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
#                 readiness = response_data['response']['rating']
#                 if readiness >= 8:
#                     base_rate += 10
#                 elif readiness <= 5:
#                     base_rate -= 10
#                 break
        
#         # Adjust for completion rate
#         completion_rate = st.session_state.assessment_results.get('completion_rate', 0)
#         if completion_rate >= 0.9:
#             base_rate += 5
#         elif completion_rate <= 0.7:
#             base_rate -= 10
        
#         return max(45, min(95, base_rate))

#     # Clinical Insights Methods (simplified versions)
#     def _extract_clinical_insights(self):
#         """Extract basic clinical insights from assessment responses"""
#         # This is a simplified version - in practice would be more comprehensive
#         return {
#             'core_limiting_belief': "Core belief requires session exploration",
#             'hidden_benefits': "Pattern provides emotional protection and familiar identity",
#             'systemic_resistance': "Minimal systemic resistance expected",
#             'identity_threat': "Identity evolution requires careful navigation",
#             'intervention_keywords': "Collaborative, gentle, permissive",
#             'avoid_language': "Pressure, criticism, commands",
#             'resistance_points': ["Standard change resistance", "Possible skepticism about process"]
#         }

#     def _generate_session_plan(self, pattern_scores, clinical_insights):
#         """Generate session planning recommendations"""
#         return {
#             'session_1_focus': "Comprehensive pattern assessment and rapport building",
#             'session_2_target': "Core pattern transformation and positive programming",
#             'session_3_need': "Standard reinforcement if needed"
#         }

#     def _generate_behavioral_sequence_analysis(self):
#         """Generate basic behavioral sequence analysis"""
#         return """
# ╔══════════════════════════════════════════════════════════════╗
# ║            BEHAVIORAL SEQUENCE MAPPING                      ║
# ╚══════════════════════════════════════════════════════════════╝

# Complete behavioral chain analysis available in full clinical template.
# Session 1 will focus on completing any missing sequence components for
# optimal intervention design.
# """

#     def _render_results(self):
#         """Render final results page"""
#         st.markdown("## Your behavioral pattern analysis")
        
#         # Show digital native indicator if applicable
#         if st.session_state.is_digital_native:
#             digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
#             if digital_analysis:
#                 severity = digital_analysis['severity_level']
#                 score = digital_analysis['digital_despair_score']
                
#                 # if severity in ['SEVERE', 'MODERATE']:
#                 #     st.markdown(f"""
#                 #     <div class="digital-indicator">
#                 #     📲 Algorithmic Syndrome Detected: {severity} ({score:.0f}% score) - Specialized intervention required
#                 #     </div>
#                 #     """, unsafe_allow_html=True)
        
#         # Direct to clinical analysis
#         self._render_clinical_analysis_section()
    
#         st.markdown("### Your next steps")
        
#         contact_info = st.session_state.get('contact_info', {})
#         urgency = contact_info.get('urgency', '')
        
#         if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
#             st.warning("⚠️ **Priority contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
#         # Show different messaging for digital natives
#         if st.session_state.is_digital_native:
#             digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
#             if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
#                 st.info("💡 **Specialized approach**: Your assessment indicates algorithmical divide patterns that require adapted hypnotherapy techniques for optimal results.")
        
#         st.markdown("""
#         **What happens next:**
    
#         1. **Clinical review** (24-48 hours): Licensed therapist analyzes your responses
#         2. **Initial contact** (48-72 hours): We have reached out via your preferred method  
#         3. **Personalized protocol** (within 72 hours): Custom hypnotherapy approach designed for your patterns
        
#         **Want to understand our proven method?** Visit **[hypnotherapy.streamlit.app](https://hypnotherapy.streamlit.app)** to learn about our rapid transformation hypnotherapy approach.
        
#         **Questions?** Reply to any email from us or contact our clinical team directly.
#         """)
        
#         # Add bottom CTA button
#         st.markdown(f"""
#         <div class="text-center">
#             <a href="{self.discovery_url}" 
#                target="_blank" 
#                class="cta-button">
#                📞 Schedule your session
#             </a>
#         </div>
#         """, unsafe_allow_html=True)

#     def _render_clinical_analysis_section(self):
#         """Render clinical analysis with paywall integration"""
#         if PAYWALL_AVAILABLE:
#             try:
#                 paywall = create_clinical_paywall()
#                 assessment_data = {
#                     'assessment_results': st.session_state.assessment_results,
#                     'assessment_responses': st.session_state.assessment_responses,
#                     'intensity_responses': st.session_state.intensity_responses,
#                     'is_digital_native': st.session_state.is_digital_native,
#                     'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis')
#                 }
#                 contact_info = st.session_state.get('contact_info', {})
#                 assessment_data.update(contact_info)
                
#                 if paywall.check_payment_status():
#                     paywall.render_premium_analysis(assessment_data)
#                 else:
#                     self._render_analysis_preview()
#                     with st.expander("🔓 Unlock complete clinical analysis", expanded=False):
#                         paywall.render_paywall_interface(assessment_data)
#             except Exception as e:
#                 st.error(f"Error loading premium analysis: {str(e)}")
#                 self._render_analysis_preview()
#         else:
#             st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
#             self._render_analysis_preview()

#     def _render_analysis_preview(self):
#         """Render preview of analysis results"""
#         results = st.session_state.assessment_results
#         pattern_scores = results.get('pattern_scores', {})
        
#         # Show algorithmical divide results if applicable
#         if st.session_state.is_digital_native:
#             digital_analysis = results.get('digital_despair_analysis')
#             if digital_analysis:
#                 severity = digital_analysis['severity_level']
#                 score = digital_analysis['digital_despair_score']
                
#                 st.markdown(f"**📲 Algorithmic syndrome assessment: {severity}** ({score:.0f}% score)")
                
#                 if severity in ['SEVERE', 'MODERATE']:
#                     st.warning(f"⚠️ **Hypnotherapy required** - Traditional approaches may be less effective")
#                 else:
#                     st.success("✅ **Standard approach suitable** with highly targetted analysis")
        
#         # Show traditional patterns
#         if pattern_scores:
#             st.markdown("**🎯 Your top behavioral patterns:**")
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
            
#             # Show only the top pattern
#             if sorted_patterns:
#                 pattern_id, score = sorted_patterns[0]
#                 pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
#                 strength = "High" if score >= 6 else "Moderate" if score >= 3 else "Emerging"
                
#                 st.markdown(f"**1. {pattern_name}** - *{strength} intensity pattern detected*")
                
#                 if pattern_id in descriptions:
#                     st.caption(descriptions[pattern_id])
                
#                 # Show indication of additional patterns if there are more
#                 if len(sorted_patterns) > 1:
#                     remaining = len(sorted_patterns) - 1
#                     st.write(f"**2. ...** *Plus {remaining} additional pattern{'s' if remaining > 1 else ''} identified*")
        
#         # Info section outside the expander
#         st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")


# # ---- Main Application Classes ----
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

# def get_digital_analysis():
#     """Get algorithmical divide analysis if available"""
#     if 'assessment_results' in st.session_state:
#         return st.session_state.assessment_results.get('digital_despair_analysis')
#     return None

# def is_digital_native():
#     """Check if current user is assessed as digital native"""
#     return st.session_state.get('is_digital_native', False)

# def reset_assessment():
#     """Reset assessment state"""
#     keys_to_reset = [
#         'assessment_responses', 'current_question', 'current_phase', 'phase_progress',
#         'is_digital_native', 'digital_despair_score', 'digital_severity',
#         'triggered_patterns', 'pattern_scores', 'risk_flags', 'assessment_completed', 
#         'contact_provided', 'assessment_results', 'intensity_responses', 
#         'trigger_chain', 'digital_responses', 'adaptive_paths'
#     ]
#     for key in keys_to_reset:
#         if key in st.session_state:
#             del st.session_state[key]

# def export_assessment_data():
#     """Export complete assessment data including digital analysis"""
#     if 'assessment_responses' not in st.session_state:
#         return None
    
#     return {
#         'responses': st.session_state.assessment_responses,
#         'pattern_scores': st.session_state.get('pattern_scores', {}),
#         'intensity_data': st.session_state.get('intensity_responses', {}),
#         'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
#         'adaptive_paths': st.session_state.get('adaptive_paths', []),
#         'risk_flags': st.session_state.get('risk_flags', []),
#         'trigger_chain': st.session_state.get('trigger_chain', {}),
#         'digital_responses': st.session_state.get('digital_responses', {}),
#         'is_digital_native': st.session_state.get('is_digital_native', False),
#         'digital_analysis': st.session_state.get('assessment_results', {}).get('digital_despair_analysis'),
#         'phase_progress': st.session_state.get('phase_progress', {}),
#         'results': st.session_state.get('assessment_results', {}),
#         'contact_info': st.session_state.get('contact_info', {}),
#         'completion_timestamp': datetime.now().isoformat()
#     }


# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Enhanced Behavioral Pattern Assessment",
#         page_icon="🧠",
#         layout="centered",
#         initial_sidebar_state="collapsed"
#     )
    
#     assessment_page = create_assess_page()
#     assessment_page.render()







# Enhanced Clinical Behavioral Pattern Assessment
# Advanced pattern detection with comprehensive clinical analysis generation
# Optimized for delivering transformational insights and personalized treatment planning

import streamlit as st
from datetime import datetime
import re
import json

# ---- Paywall Integration ----
try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False

# ---- Enhanced Styling ----
def apply_clinical_styles():
    """Apply enhanced clinical-grade styling with improved UX"""
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
    .insight-preview {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 4px solid #4CA1A3;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 6px 6px 0;
    }
    .pattern-strength-high { color: #dc2626; font-weight: 600; }
    .pattern-strength-moderate { color: #ea580c; font-weight: 600; }
    .pattern-strength-emerging { color: #059669; font-weight: 600; }
    .clinical-indicator {
        background: #fef3c7;
        border: 1px solid #f59e0b;
        padding: 0.75rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    .digital-severity-severe { 
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        color: #991b1b; 
        border-left: 4px solid #dc2626;
    }
    .digital-severity-moderate { 
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        color: #9a3412; 
        border-left: 4px solid #ea580c;
    }
    .digital-severity-mild { 
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        color: #92400e; 
        border-left: 4px solid #f59e0b;
    }
    .analysis-teaser {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 2px dashed #4CA1A3;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
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
    </style>
    """, unsafe_allow_html=True)

# ---- Enhanced Assessment Class ----
class ComprehensiveBehavioralAssessment:
    """Enhanced behavioral pattern assessment with advanced clinical analysis"""
    
    def __init__(self):
        self._init_session_state()
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        self.patterns = {
            1: "Unhappiness culture", 2: "Power struggles", 3: "Systematic mistrust", 
            4: "Separation and division", 5: "Doing versus being", 6: "Compartmentalized authenticity", 
            7: "Self sacrifice and care avoidance", 8: "Inherited missions", 9: "Context dependent weakness"
        }
        
        # Enhanced question pools for deeper clinical insights
        self.questions = self._build_enhanced_question_pool()
        
    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'current_phase': 'screening',
            'is_digital_native': False,
            'digital_despair_score': 0,
            'digital_severity': 'MINIMAL',
            'triggered_patterns': set(),
            'pattern_scores': {},
            'pattern_intensities': {},
            'behavioral_sequence': {},
            'secondary_gains': {},
            'core_beliefs': {},
            'systemic_resistance': {},
            'transformation_blockers': [],
            'readiness_indicators': {},
            'hypnotic_preferences': {},
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'start_time': datetime.now().isoformat(),
            'adaptive_questions': [],
            'clinical_insights': {},
            'session_design': {},
            'success_predictors': {}
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _build_enhanced_question_pool(self):
        """Build comprehensive question pool for maximum clinical insight"""
        return {
            # Phase 1: Initial Screening (1-5)
            1: {
                "text": "What is your age range?",
                "type": "single_choice",
                "options": [
                    "Under 18", "18-22", "23-27", "28-32", 
                    "33-37", "38-42", "43-50", "Over 50"
                ],
                "digital_native_weights": [3, 5, 4, 3, 2, 1, 0, 0],
                "phase": "screening"
            },
            
            2: {
                "text": "What brought you to explore hypnotherapy right now?",
                "type": "single_choice_with_follow_up",
                "options": [
                    "I've tried everything else - therapy, medication, self-help",
                    "I want faster results than traditional approaches offer",
                    "Someone specifically recommended hypnotherapy for my issue",
                    "I'm curious but honestly skeptical about whether it works",
                    "I feel stuck in patterns I can't break on my own"
                ],
                "follow_up_mapping": {
                    0: "What approaches have you tried and what happened?",
                    1: "What timeline are you hoping for?",
                    2: "What did they tell you about hypnotherapy?",
                    3: "What would convince you it's worth trying?",
                    4: "How long have you felt stuck like this?"
                },
                "pattern_indicators": {0: [3, 5], 1: [5], 2: [3], 3: [3], 4: [1, 4]},
                "phase": "screening"
            },
            
            3: {
                "text": "If this issue completely resolved tomorrow, what would be the first thing you'd do differently?",
                "type": "text_with_analysis",
                "placeholder": "Be specific - what exact action, conversation, or decision would you make that you can't make now?",
                "min_chars": 10,
                "analysis_keywords": {
                    "relationship": [2, 3, 6, 7], "work": [5, 8], "family": [7, 8], 
                    "confident": [3, 6], "peaceful": [1], "boundaries": [7, 9],
                    "authentic": [6], "control": [2, 4], "happy": [1], "worthy": [1, 3]
                },
                "outcome_visualization": True,
                "phase": "screening"
            },
            
            4: {
                "text": "How many hours per day do you spend on digital devices for non-essential activities (social media, entertainment, browsing)?",
                "type": "single_choice",
                "options": [
                    "Less than 1 hour", "1-2 hours", "2-4 hours",
                    "4-6 hours", "6-8 hours", "Over 8 hours"
                ],
                "digital_despair_weights": [0, 0, 1, 2, 3, 4],
                "phase": "screening"
            },
            
            5: {
                "text": "When you feel most like your true authentic self, you're usually:",
                "type": "single_choice_with_intensity",
                "options": [
                    "In close, private relationships with people who know me well",
                    "Online in communities where I can be anonymous or selective",
                    "Alone, away from any social expectations or judgments",
                    "In professional settings where I have a clear role",
                    "I rarely feel authentically myself anywhere"
                ],
                "digital_indicators": {1: 2, 4: 3},
                "pattern_mapping": {0: [6, 7], 1: [6], 2: [3, 6], 3: [6], 4: [3, 6]},
                "phase": "screening"
            },
            
            # Phase 2: Pattern Detection & Behavioral Mapping (6-15)
            6: {
                "text": "Think of the last time this issue showed up. What was happening in the 60 seconds right before you noticed it?",
                "type": "detailed_scenario",
                "prompts": [
                    "Where were you physically?",
                    "Who else was present?",
                    "What was being said or discussed?",
                    "What did you see, hear, or notice in the environment?"
                ],
                "trigger_analysis": True,
                "phase": "behavioral_mapping"
            },
            
            7: {
                "text": "In that moment, the very first thing you noticed was:",
                "type": "single_choice_with_intensity",
                "options": [
                    "A physical sensation (chest tightness, stomach drop, tension)",
                    "An automatic thought or worry appearing in your mind",
                    "An emotional shift (anger, fear, sadness, numbness)",
                    "Something another person said or did",
                    "A sudden urge to do something (leave, argue, shut down)"
                ],
                "sequence_mapping": "trigger_point",
                "phase": "behavioral_mapping"
            },
            
            8: {
                "text": "What physical sensation do you feel most often when this pattern activates?",
                "type": "single_choice_with_body_mapping",
                "options": [
                    "Chest tightness, heart racing, or breathing changes",
                    "Stomach knots, nausea, or digestive upset",
                    "Muscle tension, jaw clenching, or body rigidity",
                    "Hot/cold flashes, sweating, or temperature changes",
                    "Numbness, disconnection, or feeling 'outside yourself'",
                    "Restless energy, fidgeting, or need to move/escape",
                    "Sudden fatigue, heaviness, or energy drain"
                ],
                "body_location_follow_up": True,
                "pattern_correlations": {
                    0: [1, 3], 1: [1, 3], 2: [2, 5], 3: [2, 5], 
                    4: [6, 9], 5: [2, 5], 6: [1, 7]
                },
                "phase": "behavioral_mapping"
            },
            
            9: {
                "text": "The automatic thought that appears with that physical sensation is usually something like:",
                "type": "thought_completion",
                "placeholder": "Write the actual words that go through your mind, even if they seem harsh. What does your inner voice say?",
                "thought_categorization": {
                    "inadequacy": [1, 3], "threat": [2, 3], "responsibility": [7, 8],
                    "control": [2, 4, 5], "authenticity": [6], "safety": [3, 9]
                },
                "core_belief_extraction": True,
                "phase": "behavioral_mapping"
            },
            
            10: {
                "text": "After that thought and feeling, your body wants to:",
                "type": "single_choice",
                "options": [
                    "Fight - argue, defend, prove your point, take control",
                    "Flight - leave, avoid, postpone, or escape the situation",
                    "Freeze - shut down, go blank, feel paralyzed or stuck",
                    "Fawn - please others, apologize, or put their needs first",
                    "Collapse - give up, feel defeated, or become resigned"
                ],
                "stress_response_mapping": True,
                "behavioral_pattern_correlation": {
                    0: [2], 1: [1, 4, 9], 2: [4, 6], 3: [7], 4: [1]
                },
                "phase": "behavioral_mapping"
            },
            
            11: {
                "text": "Right after you respond that way, you typically feel:",
                "type": "multiple_choice_weighted",
                "options": [
                    "Temporary relief but the underlying tension remains",
                    "More agitated or upset than before you reacted",
                    "Emotionally numb or disconnected from yourself",
                    "Guilty or ashamed about how you handled it",
                    "Justified and right in your response",
                    "Confused about what just happened to you",
                    "Physically exhausted or completely drained"
                ],
                "max_selections": 2,
                "immediate_consequence_analysis": True,
                "phase": "behavioral_mapping"
            },
            
            12: {
                "text": "A few hours later, you find yourself:",
                "type": "single_choice",
                "options": [
                    "Having completely moved on and forgotten about it",
                    "Still mentally replaying what happened over and over",
                    "Planning how to avoid similar situations in the future",
                    "Angry at yourself for reacting the same way again",
                    "Feeling misunderstood by others who were involved",
                    "Resigned that this is just how things always go"
                ],
                "reinforcement_pattern": {
                    1: "rumination", 2: "avoidance", 3: "self-criticism",
                    4: "victim_mindset", 5: "learned_helplessness"
                },
                "phase": "behavioral_mapping"
            },
            
            # Digital Native Specific Questions (13-18)
            13: {
                "text": "When someone suggests things could get better or offers optimistic perspectives:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I feel genuinely encouraged and want to believe them",
                    "I appreciate it but remain cautiously realistic",
                    "I immediately think of reasons why they're probably wrong",
                    "I feel annoyed because they don't understand how things really are",
                    "I dismiss it as naive thinking or manipulation"
                ],
                "hope_avoidance_indicators": {2: 2, 3: 3, 4: 4},
                "digital_despair_correlation": True,
                "conditional_on": "digital_native",
                "phase": "digital_assessment"
            },
            
            14: {
                "text": "Your attention span for activities without digital stimulation (books, conversations, offline tasks):",
                "type": "single_choice",
                "options": [
                    "Same as it's always been - I can focus for hours",
                    "Slightly shorter but still manageable for important things",
                    "Noticeably fragmented - I need frequent mental breaks",
                    "Very difficult - my mind wanders within minutes",
                    "Almost impossible without some background digital input"
                ],
                "attention_fragmentation_scoring": [0, 1, 2, 3, 4],
                "conditional_on": "digital_native",
                "phase": "digital_assessment"
            },
            
            15: {
                "text": "When expressing genuine emotions or enthusiasm about something:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I express them naturally and directly without self-consciousness",
                    "I tend to use humor or sarcasm to soften the vulnerability",
                    "I feel embarrassed or 'cringe' about being too sincere",
                    "I mainly express emotions through memes, jokes, or cultural references",
                    "I avoid expressing genuine emotions almost entirely"
                ],
                "ironic_detachment_scoring": [0, 2, 3, 3, 4],
                "conditional_on": "digital_native",
                "phase": "digital_assessment"
            },
            
            # Deep Pattern Exploration (16-25) - Adaptive based on triggered patterns
            16: {
                "text": "Growing up, the message about happiness and success in your family was:",
                "type": "single_choice",
                "options": [
                    "Happiness is natural and should be celebrated when it comes",
                    "Happiness must be earned through hard work and achievement",
                    "Too much happiness leads to disappointment or bad luck",
                    "Other people's happiness should come before your own",
                    "Happiness is selfish, shallow, or naive"
                ],
                "family_programming_analysis": True,
                "pattern": 1,
                "conditional_on": "pattern_1_triggered",
                "phase": "pattern_exploration"
            },
            
            17: {
                "text": "When someone disagrees with your opinion or challenges your perspective:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I stay genuinely curious about their different viewpoint",
                    "My nervous system immediately goes into defensive mode",
                    "I feel personally attacked or criticized even if they're being polite",
                    "I shut down or withdraw to avoid confrontation entirely",
                    "I start looking for ways to prove them wrong or change their mind"
                ],
                "conflict_response_pattern": True,
                "pattern": 2,
                "conditional_on": "pattern_2_triggered",
                "phase": "pattern_exploration"
            },
            
            18: {
                "text": "When meeting new people, your default assumption about their intentions toward you is:",
                "type": "single_choice_with_intensity",
                "options": [
                    "They're generally well-intentioned and friendly",
                    "They're judging or evaluating me in some way",
                    "They want something from me or have hidden motives",
                    "They'll eventually disappoint or hurt me somehow",
                    "They're basically indifferent and don't really care"
                ],
                "trust_baseline_assessment": True,
                "pattern": 3,
                "conditional_on": "pattern_3_triggered",
                "phase": "pattern_exploration"
            },
            
            19: {
                "text": "When facing important decisions, you typically:",
                "type": "single_choice_with_intensity",
                "options": [
                    "See multiple creative possibilities and feel excited about options",
                    "Feel trapped between two impossible or conflicting choices",
                    "Get paralyzed by perfectionist analysis of every detail",
                    "Create artificial urgency or pressure to force a decision",
                    "Defer to what others expect or want you to choose"
                ],
                "decision_making_pattern": True,
                "pattern": 4,
                "conditional_on": "pattern_4_triggered",
                "phase": "pattern_exploration"
            },
            
            20: {
                "text": "You feel most valuable and worthy when you are:",
                "type": "single_choice_with_intensity",
                "options": [
                    "Simply existing as yourself without having to do anything",
                    "Accomplishing something significant that others recognize",
                    "Being productive, busy, or actively working toward goals",
                    "Helping others achieve what they want or need",
                    "Receiving praise or recognition for your contributions"
                ],
                "worth_equation_analysis": True,
                "pattern": 5,
                "conditional_on": "pattern_5_triggered",
                "phase": "pattern_exploration"
            },
            
            # Secondary Gain & Resistance Analysis (21-25)
            21: {
                "text": "If you had to guess, this pattern might be trying to protect you from:",
                "type": "single_choice",
                "options": [
                    "Getting hurt, disappointed, or emotionally wounded",
                    "Being rejected, abandoned, or socially excluded",
                    "Losing control or being powerless in situations",
                    "Feeling inadequate, incompetent, or not good enough",
                    "Being taken advantage of or manipulated by others",
                    "Making mistakes or failing at important things"
                ],
                "secondary_gain_analysis": True,
                "protective_function_mapping": True,
                "phase": "resistance_analysis"
            },
            
            22: {
                "text": "What would you potentially lose or give up if this pattern completely disappeared?",
                "type": "text_with_analysis",
                "placeholder": "Consider identity, relationships, familiar ways of being, or what others might think or expect...",
                "loss_analysis": True,
                "identity_threat_assessment": True,
                "phase": "resistance_analysis"
            },
            
            23: {
                "text": "Who in your life might be most surprised or unsettled if you dramatically changed this pattern?",
                "type": "text_with_analysis",
                "placeholder": "Think about family members, partners, friends, or colleagues who are used to you being a certain way...",
                "systemic_resistance_mapping": True,
                "relationship_impact_prediction": True,
                "phase": "resistance_analysis"
            },
            
            # Hypnotic Preference & Session Design (24-28)
            24: {
                "text": "When you're learning something new or making changes, you respond best to:",
                "type": "single_choice",
                "options": [
                    "Direct, clear instructions and specific steps to follow",
                    "Gentle suggestions and permission to go at your own pace",
                    "Stories, metaphors, and imagery that help things click",
                    "Logical explanations and understanding the 'why' behind things",
                    "Collaborative exploration where we figure things out together"
                ],
                "hypnotic_style_preference": True,
                "session_design_input": True,
                "phase": "session_design"
            },
            
            25: {
                "text": "Your ideal pace for transformation would be:",
                "type": "single_choice",
                "options": [
                    "Immediate and dramatic - I want everything to change quickly",
                    "Rapid but sustainable - noticeable shifts within days/weeks",
                    "Gradual and steady - building changes over months",
                    "Very gentle - barely noticeable shifts that feel completely safe",
                    "I'm not sure - whatever works best for my situation"
                ],
                "change_pace_preference": True,
                "phase": "session_design"
            },
            
            26: {
                "text": "On a scale of 1-10, how ready are you to completely let go of this pattern right now?",
                "type": "scale_with_follow_up",
                "scale_range": [1, 10],
                "follow_up_threshold": 7,
                "follow_up_question": "What would need to be different for this to be a 10?",
                "readiness_assessment": True,
                "phase": "session_design"
            },
            
            # Integration & Future Pacing (27-30)
            27: {
                "text": "Imagine it's 6 months from now and this pattern has completely transformed. Describe a typical day:",
                "type": "detailed_future_pacing",
                "prompts": [
                    "How do you start your morning differently?",
                    "How do interactions with others change?",
                    "What do you do that you couldn't do before?",
                    "How do you feel about yourself?"
                ],
                "future_self_visualization": True,
                "outcome_anchoring": True,
                "phase": "integration"
            },
            
            28: {
                "text": "The most important thing for you to remember during the transformation process is:",
                "type": "single_choice",
                "options": [
                    "You have everything within you needed to make this change",
                    "Change can be easier and more natural than you expect",
                    "Your past patterns were protecting you and served a purpose",
                    "Small shifts create surprisingly large life changes",
                    "You deserve to experience life without this limitation"
                ],
                "therapeutic_message_preference": True,
                "core_programming_preparation": True,
                "phase": "integration"
            },
            
            # Final Assessment Questions (29-30)
            29: {
                "text": "What percentage of your mental and emotional energy does this pattern currently consume?",
                "type": "percentage_slider",
                "range": [0, 100],
                "impact_quantification": True,
                "phase": "final_assessment"
            },
            
            30: {
                "text": "If hypnotherapy completely resolved this for you, what would that mean for your life?",
                "type": "text_with_analysis",
                "placeholder": "Think beyond just the problem being gone - what becomes possible? How does your life expand?",
                "transformation_vision": True,
                "motivation_anchoring": True,
                "phase": "final_assessment"
            }
        }

    def _determine_digital_native_status(self, age_response):
        """Enhanced digital native determination"""
        age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
        scoring = [3, 5, 4, 3, 2, 1, 0, 0]
        
        try:
            age_index = age_options.index(age_response)
            digital_score = scoring[age_index]
            return digital_score >= 2
        except (ValueError, IndexError):
            return False

    def _analyze_digital_despair_comprehensive(self, responses):
        """Comprehensive digital despair syndrome analysis"""
        if not st.session_state.is_digital_native:
            return None
            
        # Extract component scores with enhanced analysis
        components = {
            'reality_dissociation': self._calculate_reality_dissociation(responses),
            'achievement_pressure': self._calculate_achievement_pressure(responses),
            'ironic_detachment': self._calculate_ironic_detachment(responses),
            'hope_avoidance': self._calculate_hope_avoidance(responses),
            'attention_fragmentation': self._calculate_attention_fragmentation(responses),
            'digital_dependency': self._calculate_digital_dependency(responses)
        }
        
        # Calculate composite score
        total_score = sum(components.values())
        max_possible = len(components) * 5
        percentage = (total_score / max_possible) * 100
        
        # Enhanced severity classification
        if percentage >= 75:
            severity = "SEVERE"
            clinical_note = "Specialized digital-native intervention protocols required"
            success_adjustment = -15  # Lower base success rate but add back with proper methods
        elif percentage >= 50:
            severity = "MODERATE"
            clinical_note = "Enhanced approach with digital awareness adaptations"
            success_adjustment = -8
        elif percentage >= 25:
            severity = "MILD"
            clinical_note = "Standard approach with digital considerations"
            success_adjustment = -3
        else:
            severity = "MINIMAL"
            clinical_note = "Traditional hypnotherapy methods suitable"
            success_adjustment = 0
        
        return {
            'digital_despair_score': percentage,
            'severity_level': severity,
            'clinical_recommendation': clinical_note,
            'success_rate_adjustment': success_adjustment,
            'component_scores': components,
            'therapeutic_adaptations': self._get_digital_adaptations(severity),
            'session_modifications': self._get_session_modifications(severity)
        }

    def _calculate_reality_dissociation(self, responses):
        """Calculate reality dissociation score"""
        score = 0
        
        # Question 5 - authenticity location
        auth_response = responses.get(5, {}).get('response', '')
        if 'online in communities' in auth_response.lower():
            score += 3
        elif 'rarely feel authentically' in auth_response.lower():
            score += 4
        elif 'alone, away from' in auth_response.lower():
            score += 2
            
        # Add intensity multiplier
        intensity = responses.get(5, {}).get('intensity', 1)
        if intensity:
            score = score * (intensity / 4)
            
        return min(5, score)

    def _calculate_achievement_pressure(self, responses):
        """Enhanced achievement pressure calculation"""
        # This would analyze responses about success definitions, worth equations, etc.
        return 2.5  # Placeholder - implement full analysis

    def _calculate_ironic_detachment(self, responses):
        """Calculate ironic detachment indicators"""
        score = 0
        
        # Question 15 - emotional expression
        emotion_response = responses.get(15, {}).get('response', '')
        if 'cringe' in emotion_response.lower():
            score += 3
        elif 'humor or sarcasm' in emotion_response.lower():
            score += 2
        elif 'memes, jokes' in emotion_response.lower():
            score += 3
        elif 'avoid expressing' in emotion_response.lower():
            score += 4
            
        intensity = responses.get(15, {}).get('intensity', 1)
        if intensity:
            score = score * (intensity / 4)
            
        return min(5, score)

    def _calculate_hope_avoidance(self, responses):
        """Calculate hope avoidance patterns"""
        score = 0
        
        # Question 13 - response to optimism
        hope_response = responses.get(13, {}).get('response', '')
        if 'dismiss it as naive' in hope_response.lower():
            score += 4
        elif 'annoyed because they don\'t understand' in hope_response.lower():
            score += 3
        elif 'reasons why they\'re wrong' in hope_response.lower():
            score += 2
            
        intensity = responses.get(13, {}).get('intensity', 1)
        if intensity:
            score = score * (intensity / 4)
            
        return min(5, score)

    def _calculate_attention_fragmentation(self, responses):
        """Calculate attention fragmentation score"""
        attention_response = responses.get(14, {}).get('response', '')
        options = [
            "Same as it's always been - I can focus for hours",
            "Slightly shorter but still manageable for important things",
            "Noticeably fragmented - I need frequent mental breaks", 
            "Very difficult - my mind wanders within minutes",
            "Almost impossible without some background digital input"
        ]
        scoring = [0, 1, 2, 3, 4]
        
        try:
            option_index = options.index(attention_response)
            return scoring[option_index]
        except (ValueError, IndexError):
            return 0

    def _calculate_digital_dependency(self, responses):
        """Calculate digital dependency indicators"""
        score = 0
        
        # Question 4 - daily digital use
        digital_use = responses.get(4, {}).get('response', '')
        if 'Over 8 hours' in digital_use:
            score += 4
        elif '6-8 hours' in digital_use:
            score += 3
        elif '4-6 hours' in digital_use:
            score += 2
        elif '2-4 hours' in digital_use:
            score += 1
            
        return min(5, score)

    def _get_digital_adaptations(self, severity):
        """Get therapeutic adaptations for digital natives"""
        adaptations = {
            "SEVERE": [
                "20-30 minute focused segments with movement breaks",
                "Anti-authority collaborative language - peer consultation model",
                "Intelligence validation while accessing authentic emotion beneath irony",
                "Digital competency bridge-building to offline confidence transfer",
                "Binary thinking interruption with 'both/and' pattern installation",
                "Gradual hope introduction - evidence-based vs overwhelming positivity",
                "Meaningful contribution focus vs extraordinary achievement pressure"
            ],
            "MODERATE": [
                "45-60 minute sessions with attention management",
                "Reduced directive language - collaborative exploration style",
                "Cynicism validation while building authentic agency",
                "Honor online achievements and transfer skills to offline contexts",
                "Nuanced success redefinition - meaningful vs extraordinary framework",
                "Realistic optimism building with evidence-based foundation"
            ],
            "MILD": [
                "Standard length with digital cultural fluency",
                "Achievement pressure awareness and success redefinition",
                "Authentic expression permission - reduce 'cringe' about sincerity",
                "Real-world confidence transfer from digital competencies"
            ],
            "MINIMAL": [
                "Traditional approach with generational awareness",
                "Technology balance considerations in lifestyle design"
            ]
        }
        return adaptations.get(severity, adaptations["MINIMAL"])

    def _get_session_modifications(self, severity):
        """Get session structure modifications for digital natives"""
        modifications = {
            "SEVERE": {
                "session_length": "90 minutes (3x30 minute segments)",
                "authority_style": "Collaborative peer consultant",
                "language_style": "Intelligence-validating, anti-directive",
                "resistance_expect": "Intellectual challenges, cynical testing",
                "hope_approach": "Gradual evidence-based realistic optimism",
                "success_framework": "Personal contribution vs extraordinary achievement"
            },
            "MODERATE": {
                "session_length": "90 minutes with 10-minute break",
                "authority_style": "Gentle expert guidance",
                "language_style": "Respectful collaboration",
                "resistance_expect": "Skepticism about traditional approaches",
                "hope_approach": "Realistic optimism with systemic awareness",
                "success_framework": "Meaningful accomplishment expansion"
            },
            "MILD": {
                "session_length": "Standard 90 minutes",
                "authority_style": "Professional with cultural awareness",
                "language_style": "Contemporary references when appropriate",
                "resistance_expect": "Standard change resistance",
                "hope_approach": "Standard hope building",
                "success_framework": "Expanded definition of success"
            },
            "MINIMAL": {
                "session_length": "Standard approach",
                "authority_style": "Traditional therapeutic",
                "language_style": "Professional clinical",
                "resistance_expect": "Typical patterns",
                "hope_approach": "Standard optimism",
                "success_framework": "Traditional goal achievement"
            }
        }
        return modifications.get(severity, modifications["MINIMAL"])

    # ---- Enhanced Pattern Detection ----
    def _update_pattern_scores_enhanced(self, question_id, response, question):
        """Enhanced pattern scoring with intensity and context"""
        
        # Handle pattern indicators from single choice questions
        if question.get('pattern_indicators'):
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_indicators']:
                        patterns = question['pattern_indicators'][option_index]
                        base_score = 2.0
                        
                        # Apply intensity multiplier if available
                        intensity = st.session_state.assessment_responses.get(question_id, {}).get('intensity', 1)
                        if intensity:
                            multiplier = intensity / 4  # Scale 1-7 to multiplier
                            base_score *= multiplier
                            
                        for pattern in patterns:
                            self._add_pattern_score(pattern, base_score)
                except (ValueError, IndexError):
                    pass
        
        # Handle pattern mapping (stronger indicators)
        if question.get('pattern_mapping'):
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_mapping']:
                        patterns = question['pattern_mapping'][option_index]
                        for pattern in patterns:
                            self._add_pattern_score(pattern, 3.0)
                except (ValueError, IndexError):
                    pass
        
        # Handle text analysis with keyword detection
        if question.get('analysis_keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['analysis_keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 2.5)
        
        # Handle specific pattern questions
        if question.get('pattern') and question.get('conditional_on'):
            pattern_id = question['pattern']
            if self._should_ask_pattern_question(pattern_id):
                if isinstance(response, str) and 'options' in question:
                    # Pattern-specific scoring logic
                    self._score_pattern_specific_question(pattern_id, response, question)

    def _add_pattern_score(self, pattern_id, score):
        """Add score to pattern with enhanced tracking"""
        if pattern_id in st.session_state.pattern_scores:
            st.session_state.pattern_scores[pattern_id] += score
        else:
            st.session_state.pattern_scores[pattern_id] = score
        
        # Track when patterns get triggered for adaptive questioning
        if score >= 3.0 and pattern_id not in st.session_state.triggered_patterns:
            st.session_state.triggered_patterns.add(pattern_id)

    def _should_ask_pattern_question(self, pattern_id):
        """Determine if pattern-specific question should be asked"""
        current_score = st.session_state.pattern_scores.get(pattern_id, 0)
        return current_score >= 3.0  # Ask deeper questions when pattern is strongly indicated

    def _score_pattern_specific_question(self, pattern_id, response, question):
        """Score pattern-specific questions with enhanced weighting"""
        if 'options' in question:
            try:
                option_index = question['options'].index(response)
                # Each pattern-specific question adds significant weight
                base_weights = [0, 1, 2, 3, 4]  # Adjust based on severity of response
                if option_index < len(base_weights):
                    weight = base_weights[option_index] * 2  # Double weight for specific questions
                    self._add_pattern_score(pattern_id, weight)
            except (ValueError, IndexError):
                pass

    def _analyze_text_for_patterns(self, text, keywords_dict):
        """Enhanced text analysis for pattern detection"""
        text_lower = text.lower()
        detected_patterns = set()
        
        # Enhanced keyword matching with context
        for keyword, patterns in keywords_dict.items():
            if keyword in text_lower:
                # Add context-aware scoring
                context_bonus = 1.0
                if len(text) > 50:  # Longer responses get context bonus
                    context_bonus = 1.5
                if '!' in text or '?' in text:  # Emotional intensity indicators
                    context_bonus *= 1.2
                    
                for pattern in patterns:
                    self._add_pattern_score(pattern, 1.0 * context_bonus)
                detected_patterns.update(patterns)
        
        return detected_patterns

    # ---- Enhanced Clinical Analysis Generation ----
    def _generate_comprehensive_clinical_analysis(self):
        """Generate the complete clinical analysis as outlined in requirements"""
        
        # Extract all clinical insights
        pattern_analysis = self._analyze_pattern_constellation()
        behavioral_sequence = self._map_complete_behavioral_sequence()
        digital_analysis = self._analyze_digital_despair_comprehensive(st.session_state.assessment_responses)
        secondary_gains = self._extract_secondary_gains()
        core_beliefs = self._extract_core_limiting_beliefs()
        systemic_resistance = self._analyze_systemic_resistance()
        session_design = self._design_personalized_sessions()
        success_predictors = self._calculate_success_predictors()
        
        # Build comprehensive analysis
        analysis = {
            'pattern_constellation': pattern_analysis,
            'behavioral_sequence': behavioral_sequence,
            'digital_despair_analysis': digital_analysis,
            'core_limiting_beliefs': core_beliefs,
            'secondary_gains': secondary_gains,
            'systemic_resistance': systemic_resistance,
            'session_design': session_design,
            'success_predictors': success_predictors,
            'transformation_timeline': self._predict_transformation_timeline(),
            'intervention_priorities': self._rank_intervention_priorities(),
            'resistance_points': self._predict_resistance_points(),
            'therapeutic_approach': self._recommend_therapeutic_approach()
        }
        
        return analysis

    def _analyze_pattern_constellation(self):
        """Analyze the constellation of behavioral patterns"""
        if not st.session_state.pattern_scores:
            return {'dominant': 'Unknown', 'supporting': [], 'intensity': 'Unknown'}
            
        sorted_patterns = sorted(st.session_state.pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant = {
            'id': sorted_patterns[0][0],
            'name': self.patterns.get(sorted_patterns[0][0], 'Unknown'),
            'score': sorted_patterns[0][1],
            'intensity': self._classify_pattern_intensity(sorted_patterns[0][1])
        }
        
        supporting = []
        for pattern_id, score in sorted_patterns[1:4]:  # Top 3 supporting patterns
            supporting.append({
                'id': pattern_id,
                'name': self.patterns.get(pattern_id, 'Unknown'),
                'score': score,
                'intensity': self._classify_pattern_intensity(score)
            })
        
        # Analyze pattern interactions
        interactions = self._analyze_pattern_interactions(sorted_patterns[:4])
        
        return {
            'dominant': dominant,
            'supporting': supporting,
            'pattern_interactions': interactions,
            'complexity_level': self._assess_pattern_complexity(sorted_patterns)
        }

    def _classify_pattern_intensity(self, score):
        """Classify pattern intensity based on score"""
        if score >= 8:
            return "Very High"
        elif score >= 6:
            return "High"
        elif score >= 4:
            return "Moderate"
        elif score >= 2:
            return "Emerging"
        else:
            return "Minimal"

    def _analyze_pattern_interactions(self, top_patterns):
        """Analyze how patterns interact and reinforce each other"""
        interactions = []
        
        # Common pattern combinations and their interactions
        pattern_combinations = {
            (1, 5): "Unhappiness culture reinforces achievement addiction - joy feels dangerous so productivity becomes the only acceptable state",
            (2, 4): "Power struggles combined with binary thinking create 'win or lose' mentality in all interactions",
            (3, 6): "Mistrust leads to compartmentalized authenticity - different masks for different people to stay safe",
            (1, 3): "Unhappiness culture reinforces mistrust - 'good things don't last, people disappoint'",
            (5, 8): "Achievement addiction serves inherited missions - working hard to fulfill family expectations",
            (7, 9): "Self-sacrifice pattern weakens boundaries in specific contexts - overgiving in relationships"
        }
        
        for i, (pattern1_id, _) in enumerate(top_patterns[:3]):
            for pattern2_id, _ in top_patterns[i+1:4]:
                combination_key = tuple(sorted([pattern1_id, pattern2_id]))
                if combination_key in pattern_combinations:
                    interactions.append({
                        'patterns': [self.patterns.get(pattern1_id), self.patterns.get(pattern2_id)],
                        'interaction': pattern_combinations[combination_key]
                    })
        
        return interactions

    def _assess_pattern_complexity(self, sorted_patterns):
        """Assess overall pattern complexity for treatment planning"""
        if len(sorted_patterns) >= 5 and sorted_patterns[4][1] >= 4:
            return "Very High - Multiple strong patterns requiring integrated approach"
        elif len(sorted_patterns) >= 3 and sorted_patterns[2][1] >= 5:
            return "High - Several significant patterns with interactions"
        elif len(sorted_patterns) >= 2 and sorted_patterns[1][1] >= 4:
            return "Moderate - Primary pattern with strong secondary pattern"
        else:
            return "Low - Single dominant pattern with minimal complications"

    def _map_complete_behavioral_sequence(self):
        """Map the complete behavioral sequence from trigger to consequence"""
        sequence = {}
        
        # Extract sequence components from responses
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            
            if question.get('trigger_analysis'):
                sequence['environmental_trigger'] = response_data.get('response', 'Not captured')
            elif question.get('sequence_mapping') == 'trigger_point':
                sequence['awareness_point'] = response_data.get('response', 'Not captured')
            elif 'physical sensation' in question.get('text', '').lower():
                sequence['physical_response'] = response_data.get('response', 'Not captured')
            elif question.get('thought_categorization'):
                sequence['automatic_thought'] = response_data.get('response', 'Not captured')
            elif question.get('stress_response_mapping'):
                sequence['behavioral_response'] = response_data.get('response', 'Not captured')
            elif question.get('immediate_consequence_analysis'):
                sequence['immediate_consequence'] = response_data.get('response', 'Not captured')
            elif question.get('reinforcement_pattern'):
                sequence['reinforcement_mechanism'] = response_data.get('response', 'Not captured')
        
        # Analyze sequence for intervention points
        intervention_points = self._identify_intervention_points(sequence)
        
        return {
            'complete_sequence': sequence,
            'intervention_points': intervention_points,
            'sequence_strength': self._assess_sequence_strength(sequence),
            'breaking_points': self._identify_breaking_points(sequence)
        }

    def _identify_intervention_points(self, sequence):
        """Identify optimal intervention points in the behavioral sequence"""
        points = []
        
        if 'physical_response' in sequence:
            points.append({
                'point': 'Physical Sensation',
                'intervention': 'Somatic interruption and new response anchoring',
                'timing': 'Immediate - before thought cascade begins'
            })
        
        if 'automatic_thought' in sequence:
            points.append({
                'point': 'Automatic Thought',
                'intervention': 'Cognitive reframe and belief modification',
                'timing': 'Early - before emotional escalation'
            })
        
        if 'behavioral_response' in sequence:
            points.append({
                'point': 'Behavioral Choice',
                'intervention': 'Alternative behavior installation',
                'timing': 'Critical - moment of action selection'
            })
        
        return points

    def _assess_sequence_strength(self, sequence):
        """Assess how entrenched the behavioral sequence is"""
        strength_indicators = 0
        
        if 'reinforcement_mechanism' in sequence:
            if 'always' in sequence['reinforcement_mechanism'].lower():
                strength_indicators += 2
            elif 'usually' in sequence['reinforcement_mechanism'].lower():
                strength_indicators += 1
        
        if len(sequence) >= 6:  # Complete sequence mapped
            strength_indicators += 1
        
        if strength_indicators >= 3:
            return "Highly Entrenched - Requires sustained intervention"
        elif strength_indicators >= 2:
            return "Moderately Entrenched - Standard intervention suitable"
        else:
            return "Emerging Pattern - Rapid change possible"

    def _identify_breaking_points(self, sequence):
        """Identify the most effective points to break the behavioral sequence"""
        breaking_points = []
        
        # Early intervention points are usually most effective
        if 'physical_response' in sequence:
            breaking_points.append({
                'point': 'Somatic Awareness',
                'effectiveness': 'Very High',
                'description': 'Interrupt pattern at first physical sensation'
            })
        
        if 'automatic_thought' in sequence:
            breaking_points.append({
                'point': 'Thought Interruption', 
                'effectiveness': 'High',
                'description': 'Challenge or reframe the automatic thought'
            })
        
        return breaking_points

    def _extract_secondary_gains(self):
        """Extract what the pattern is trying to protect or provide"""
        gains = {}
        
        # Look for protective function responses
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            
            if question.get('secondary_gain_analysis'):
                gains['primary_protection'] = response_data.get('response', 'Unknown')
            elif question.get('loss_analysis'):
                gains['potential_losses'] = response_data.get('response', 'Unknown')
            elif question.get('protective_function_mapping'):
                gains['protective_function'] = response_data.get('response', 'Unknown')
        
        return gains

    def _extract_core_limiting_beliefs(self):
        """Extract core limiting beliefs from responses"""
        beliefs = {}
        
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            
            if question.get('core_belief_extraction'):
                belief_text = response_data.get('response', '')
                beliefs['primary_belief'] = self._analyze_core_belief(belief_text)
            elif question.get('family_programming_analysis'):
                beliefs['family_programming'] = response_data.get('response', 'Unknown')
            elif question.get('worth_equation_analysis'):
                beliefs['worth_equation'] = response_data.get('response', 'Unknown')
        
        return beliefs

    def _analyze_core_belief(self, belief_text):
        """Analyze the core limiting belief from thought text"""
        belief_patterns = {
            "not good enough": "Core inadequacy belief",
            "can't trust": "Safety and trust belief system",
            "must do": "Performance-based worth belief",
            "should": "Perfectionist expectation belief",
            "can't handle": "Capability and resilience doubt",
            "don't deserve": "Worth and deserving belief",
            "always": "Absolutist thinking pattern",
            "never": "Hopelessness and possibility belief"
        }
        
        for pattern, belief_type in belief_patterns.items():
            if pattern in belief_text.lower():
                return f"{belief_type}: '{belief_text}'"
        
        return f"Custom belief pattern: '{belief_text}'"

    def _analyze_systemic_resistance(self):
        """Analyze potential systemic resistance to change"""
        resistance = {}
        
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            
            if question.get('systemic_resistance_mapping'):
                resistance['family_system'] = response_data.get('response', 'Minimal resistance expected')
            elif question.get('relationship_impact_prediction'):
                resistance['relationship_impact'] = response_data.get('response', 'Positive changes expected')
        
        return resistance

    def _design_personalized_sessions(self):
        """Design personalized session approach"""
        design = {}
        
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            
            if question.get('hypnotic_style_preference'):
                design['preferred_style'] = response_data.get('response', 'Collaborative exploration')
            elif question.get('change_pace_preference'):
                design['preferred_pace'] = response_data.get('response', 'Rapid but sustainable')
            elif question.get('session_design_input'):
                design['approach_preference'] = response_data.get('response', 'Collaborative')
        
        # Add digital adaptations if needed
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                design['digital_adaptations'] = digital_analysis.get('session_modifications', {})
        
        return design

    def _calculate_success_predictors(self):
        """Calculate success predictors and probability"""
        base_success_rate = 85  # Standard hypnotherapy success rate
        
        # Adjust for pattern complexity
        pattern_count = len([score for score in st.session_state.pattern_scores.values() if score >= 4])
        if pattern_count >= 4:
            base_success_rate -= 15
        elif pattern_count >= 2:
            base_success_rate -= 8
        
        # Adjust for readiness score
        readiness_score = 7  # Default
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            if question.get('readiness_assessment'):
                if isinstance(response_data.get('response'), (int, float)):
                    readiness_score = response_data['response']
                break
        
        if readiness_score >= 8:
            base_success_rate += 10
        elif readiness_score <= 5:
            base_success_rate -= 15
        
        # Adjust for digital despair factors
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                adjustment = digital_analysis.get('success_rate_adjustment', 0)
                base_success_rate += adjustment
                # Add back points for proper adaptations
                if digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                    base_success_rate += 10  # Specialized approach increases success
        
        # Completion rate adjustment
        completion_rate = len(st.session_state.assessment_responses) / len(self.questions)
        if completion_rate >= 0.9:
            base_success_rate += 8
        elif completion_rate <= 0.6:
            base_success_rate -= 12
        
        final_rate = max(55, min(96, base_success_rate))
        
        return {
            'predicted_success_rate': final_rate,
            'readiness_score': readiness_score,
            'pattern_complexity': pattern_count,
            'completion_engagement': completion_rate,
            'confidence_level': 'High' if final_rate >= 80 else 'Moderate' if final_rate >= 70 else 'Requires preparation'
        }

    def _predict_transformation_timeline(self):
        """Predict realistic transformation timeline"""
        # Base timeline: 2 sessions for most people
        base_sessions = 2
        
        # Adjust for pattern complexity
        pattern_count = len([score for score in st.session_state.pattern_scores.values() if score >= 4])
        if pattern_count >= 4:
            base_sessions += 1
        
        # Adjust for digital despair severity
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] == 'SEVERE':
                base_sessions += 1
        
        # Adjust for readiness
        readiness_score = 7  # Default
        for q_id, response_data in st.session_state.assessment_responses.items():
            question = self.questions.get(q_id, {})
            if question.get('readiness_assessment'):
                if isinstance(response_data.get('response'), (int, float)):
                    readiness_score = response_data['response']
                break
        
        if readiness_score <= 6:
            base_sessions += 1
        
        timeline = {
            'recommended_sessions': min(4, base_sessions),
            'initial_shifts': "48-72 hours after session 1",
            'significant_changes': "7-14 days after session 2",
            'full_integration': "4-8 weeks post-completion",
            'maintenance': "Optional 6-month check-in"
        }
        
        return timeline

    def _rank_intervention_priorities(self):
        """Rank intervention priorities based on pattern analysis"""
        priorities = []
        
        if st.session_state.pattern_scores:
            sorted_patterns = sorted(st.session_state.pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            # Primary intervention: Dominant pattern
            if sorted_patterns:
                primary_id, primary_score = sorted_patterns[0]
                priorities.append({
                    'priority': 1,
                    'target': self.patterns.get(primary_id, 'Unknown pattern'),
                    'approach': self._get_pattern_intervention_approach(primary_id),
                    'session': 'Session 1 & 2 focus'
                })
            
            # Secondary interventions: Supporting patterns
            for i, (pattern_id, score) in enumerate(sorted_patterns[1:3], 2):
                if score >= 4:  # Only significant secondary patterns
                    priorities.append({
                        'priority': i,
                        'target': self.patterns.get(pattern_id, 'Unknown pattern'),
                        'approach': self._get_pattern_intervention_approach(pattern_id),
                        'session': f'Session {"2" if i == 2 else "3"} integration'
                    })
        
        # Add digital despair intervention if needed
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                priorities.insert(0, {
                    'priority': 0,
                    'target': 'Digital despair syndrome adaptations',
                    'approach': 'Specialized digital-native protocol integration',
                    'session': 'Throughout all sessions'
                })
        
        return priorities

    def _get_pattern_intervention_approach(self, pattern_id):
        """Get specific intervention approach for each pattern"""
        approaches = {
            1: "Permission for natural joy, safety in happiness programming",
            2: "Collaborative strength, curiosity about differences installation", 
            3: "Graduated trust building, authentic connection safety",
            4: "Both/and thinking, creative third option generation",
            5: "Inherent worth recognition, being-state appreciation",
            6: "Authentic self integration across all contexts",
            7: "Balanced care system, self-preservation as service",
            8: "Personal mission clarity separate from inherited expectations",
            9: "Consistent boundary maintenance across all relationships"
        }
        return approaches.get(pattern_id, "Pattern-specific intervention protocol")

    def _predict_resistance_points(self):
        """Predict likely resistance points during transformation"""
        resistance_points = []
        
        # Pattern-based resistance predictions
        top_patterns = sorted(st.session_state.pattern_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
        for pattern_id, score in top_patterns:
            if score >= 5:  # Strong patterns likely to create resistance
                pattern_name = self.patterns.get(pattern_id, 'Unknown')
                resistance_points.append({
                    'source': pattern_name,
                    'resistance_type': self._get_pattern_resistance_type(pattern_id),
                    'management_strategy': self._get_resistance_management_strategy(pattern_id)
                })
        
        # Digital native resistance patterns
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                resistance_points.append({
                    'source': 'Digital despair conditioning',
                    'resistance_type': 'Intellectual superiority, cynicism about traditional approaches',
                    'management_strategy': 'Validate intelligence, use collaborative peer-consultant model'
                })
        
        return resistance_points

    def _get_pattern_resistance_type(self, pattern_id):
        """Get expected resistance type for each pattern"""
        resistance_types = {
            1: "Fear that happiness will lead to disappointment or loss",
            2: "Loss of familiar power/control dynamics in relationships",
            3: "Vulnerability anxiety about trusting others",
            4: "Identity confusion without black-and-white thinking",
            5: "Worth anxiety without constant doing/achieving",
            6: "Fear of authentic self rejection or judgment",
            7: "Guilt about prioritizing own needs over others",
            8: "Family loyalty conflicts and guilt about independence",
            9: "Safety concerns about maintaining boundaries"
        }
        return resistance_types.get(pattern_id, "Standard change resistance")

    def _get_resistance_management_strategy(self, pattern_id):
        """Get strategy for managing pattern-specific resistance"""
        strategies = {
            1: "Gradual happiness permission, safety anchoring with joy",
            2: "Collaborative strength reframe, win-win possibility installation",
            3: "Graduated trust building, discernment vs mistrust distinction",
            4: "Creative third option celebration, both/and excitement",
            5: "Being-state value demonstration, effortless worth experience",
            6: "Authentic self safety testing, genuine connection rewards",
            7: "Balanced care as ultimate service, sustainable giving model",
            8: "Personal mission discovery, family honor through authenticity",
            9: "Boundary strength as relationship gift, respectful firmness"
        }
        return strategies.get(pattern_id, "Standard resistance management")

    def _recommend_therapeutic_approach(self):
        """Recommend overall therapeutic approach"""
        approach = {
            'primary_modality': 'Rapid transformation hypnotherapy',
            'session_structure': '2+1 session protocol',
            'hypnotic_style': 'Collaborative permissive with targeted interventions'
        }
        
        # Adjust for digital native status
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                if severity in ['SEVERE', 'MODERATE']:
                    approach.update({
                        'specialized_protocol': 'Digital-native adapted hypnotherapy',
                        'authority_model': 'Peer consultant collaborative approach',
                        'language_adaptations': 'Intelligence-validating, anti-directive',
                        'session_modifications': digital_analysis.get('session_modifications', {})
                    })
        
        # Adjust for pattern complexity
        pattern_count = len([score for score in st.session_state.pattern_scores.values() if score >= 4])
        if pattern_count >= 4:
            approach['complexity_note'] = 'Multiple pattern integration required'
            approach['session_recommendation'] = '2+1 sessions with possible extension'
        
        return approach

    # ---- Question Navigation & Flow Control ----
    def _get_current_question(self):
        """Get current question based on adaptive flow"""
        answered = set(st.session_state.assessment_responses.keys())
        
        # Always start with screening questions (1-5)
        for q_id in range(1, 6):
            if q_id not in answered:
                return q_id, self.questions[q_id]
        
        # Check if digital native assessment is needed (6-15)
        if st.session_state.is_digital_native:
            for q_id in range(13, 16):  # Digital-specific questions
                if q_id not in answered:
                    question = self.questions[q_id]
                    if question.get('conditional_on') == 'digital_native':
                        return q_id, question
        
        # Core behavioral mapping questions (6-12)
        for q_id in range(6, 13):
            if q_id not in answered:
                return q_id, self.questions[q_id]
        
        # Pattern-specific questions (16-20) - only ask if patterns are triggered
        for q_id in range(16, 21):
            if q_id not in answered:
                question = self.questions[q_id]
                if self._should_ask_pattern_question_by_condition(question):
                    return q_id, question
        
        # Resistance and secondary gain analysis (21-23)
        for q_id in range(21, 24):
            if q_id not in answered:
                return q_id, self.questions[q_id]
        
        # Session design questions (24-26)
        for q_id in range(24, 27):
            if q_id not in answered:
                return q_id, self.questions[q_id]
        
        # Integration questions (27-30)
        for q_id in range(27, 31):
            if q_id not in answered:
                return q_id, self.questions[q_id]
        
        return None, None

    def _should_ask_pattern_question_by_condition(self, question):
        """Check if pattern-specific question should be asked"""
        condition = question.get('conditional_on')
        if not condition:
            return True
        
        if condition == 'digital_native':
            return st.session_state.is_digital_native
        elif condition.startswith('pattern_') and condition.endswith('_triggered'):
            pattern_id = int(condition.split('_')[1])
            return st.session_state.pattern_scores.get(pattern_id, 0) >= 3.0
        
        return True

    def _estimate_total_questions(self):
        """Estimate total questions for progress tracking"""
        base_questions = 20  # Core questions everyone gets
        
        if st.session_state.is_digital_native:
            base_questions += 3  # Digital-specific questions
        
        # Add triggered pattern questions
        triggered_count = len([p for p, score in st.session_state.pattern_scores.items() if score >= 3.0])
        base_questions += min(triggered_count, 5)  # Max 5 pattern-specific questions
        
        return base_questions

    # ---- Response Handling Methods ----
    def _save_response(self, q_id, response, question, intensity=None, additional_data=None):
        """Save response with enhanced data tracking"""
        response_data = {
            'response': response,
            'intensity': intensity,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat(),
            'phase': question.get('phase', 'unknown')
        }
        
        if additional_data:
            response_data.update(additional_data)
        
        st.session_state.assessment_responses[q_id] = response_data
        
        # Update pattern scoring
        self._update_pattern_scores_enhanced(q_id, response, question)
        
        # Handle special question types
        if question.get('trigger_analysis'):
            st.session_state.behavioral_sequence['environmental_trigger'] = response
            st.session_state.trigger_chain['environmental_trigger'] = response
        elif question.get('core_belief_extraction'):
            st.session_state.core_beliefs['primary_automatic_thought'] = response
            st.session_state.trigger_chain['automatic_thought'] = response
        elif question.get('secondary_gain_analysis'):
            st.session_state.secondary_gains['protective_function'] = response
        elif question.get('sequence_mapping') == 'trigger_point':
            st.session_state.trigger_chain['awareness_point'] = response
        elif 'physical sensation' in question.get('text', '').lower():
            st.session_state.trigger_chain['physical_response'] = response
        elif question.get('stress_response_mapping'):
            st.session_state.trigger_chain['behavioral_response'] = response
        elif question.get('immediate_consequence_analysis'):
            st.session_state.trigger_chain['immediate_consequence'] = response
        
        # Store digital responses separately for email handler
        if question.get('phase') == 'digital_assessment' or question.get('conditional_on') == 'digital_native':
            st.session_state.digital_responses[q_id] = response
        
        # Check if we need to determine digital native status
        if q_id == 1:  # Age question
            st.session_state.is_digital_native = self._determine_digital_native_status(response)

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

    def _handle_single_choice_with_follow_up(self, q_id, question):
        """Handle single choice with follow-up questions"""
        selection_key = f"selected_option_{q_id}"
        
        for i, option in enumerate(question['options']):
            if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                st.session_state[selection_key] = (option, i)
                st.rerun()
        
        if selection_key in st.session_state:
            selected_option, option_index = st.session_state[selection_key]
            st.success(f"Selected: {selected_option}")
            
            # Show follow-up if configured
            follow_up_mapping = question.get('follow_up_mapping', {})
            if option_index in follow_up_mapping:
                follow_up_text = st.text_area(
                    follow_up_mapping[option_index],
                    key=f"q_{q_id}_followup",
                    height=80
                )
            else:
                follow_up_text = ""
            
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                additional_data = {'follow_up': follow_up_text} if follow_up_text else None
                self._save_response(q_id, selected_option, question, additional_data=additional_data)
                if selection_key in st.session_state:
                    del st.session_state[selection_key]
                self._advance_question()
                st.rerun()

    def _handle_text_with_analysis(self, q_id, question):
        """Handle text questions with built-in analysis"""
        min_chars = question.get('min_chars', 10)
        response = st.text_area(
            "Your response:",
            placeholder=question.get('placeholder', 'Please share your thoughts...'),
            key=f"q_{q_id}_text",
            height=120
        )
        
        char_count = len(response.strip())
        
        # Show character count
        if char_count > 0:
            sufficient = char_count >= min_chars
            if sufficient:
                st.success(f"✓ {char_count} characters - good detail level")
            else:
                st.info(f"Please add {min_chars - char_count} more characters for complete analysis")
        
        if char_count >= min_chars:
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, response.strip(), question)
                self._advance_question()
                st.rerun()

    def _handle_detailed_scenario(self, q_id, question):
        """Handle detailed scenario questions with multiple prompts"""
        st.markdown("Please provide details for each aspect:")
        
        prompts = question.get('prompts', [])
        responses = {}
        
        for i, prompt in enumerate(prompts):
            responses[f'prompt_{i}'] = st.text_input(
                prompt,
                key=f"q_{q_id}_prompt_{i}",
                placeholder="Be as specific as possible..."
            )
        
        # Check if we have enough detail
        total_chars = sum(len(resp) for resp in responses.values())
        min_total = len(prompts) * 10  # At least 10 chars per prompt
        
        if total_chars >= min_total:
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                # Combine all responses
                combined_response = " | ".join([f"{prompts[i]}: {resp}" for i, resp in enumerate(responses.values())])
                self._save_response(q_id, combined_response, question, additional_data=responses)
                self._advance_question()
                st.rerun()
        elif total_chars > 0:
            st.info(f"Please add more detail ({min_total - total_chars} more characters needed)")

    def _handle_scale_with_follow_up(self, q_id, question):
        """Handle scale questions with conditional follow-up"""
        scale_range = question.get('scale_range', [1, 10])
        value = st.select_slider(
            "Your rating:",
            options=list(range(scale_range[0], scale_range[1] + 1)),
            format_func=lambda x: f"{x}/{scale_range[1]}",
            value=scale_range[1] // 2 + 2,  # Slightly above middle
            key=f"q_{q_id}_scale"
        )
        
        # Show follow-up if below threshold
        follow_up = ""
        threshold = question.get('follow_up_threshold', 7)
        if value <= threshold and question.get('follow_up_question'):
            follow_up = st.text_area(
                question['follow_up_question'],
                key=f"q_{q_id}_followup",
                height=80,
                placeholder="What would make this easier for you?"
            )
        
        if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
            response_data = {'rating': value}
            if follow_up:
                response_data['follow_up'] = follow_up
            self._save_response(q_id, response_data, question)
            self._advance_question()
            st.rerun()

    def _handle_percentage_slider(self, q_id, question):
        """Handle percentage slider questions"""
        value = st.slider(
            "Percentage:",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            key=f"q_{q_id}_percentage",
            format="%d%%"
        )
        
        # Show interpretation
        if value >= 80:
            st.error("🔴 Very high impact - this is consuming most of your energy")
        elif value >= 60:
            st.warning("🟡 High impact - significant energy drain")
        elif value >= 40:
            st.info("🔵 Moderate impact - noticeable but manageable")
        elif value >= 20:
            st.success("🟢 Low impact - minimal energy consumption")
        else:
            st.success("✅ Very low impact")
        
        if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
            self._save_response(q_id, value, question)
            self._advance_question()
            st.rerun()

    def _handle_detailed_future_pacing(self, q_id, question):
        """Handle detailed future pacing questions"""
        st.markdown("**Imagine your transformed life in detail:**")
        
        prompts = question.get('prompts', [])
        responses = {}
        
        for i, prompt in enumerate(prompts):
            responses[f'future_{i}'] = st.text_area(
                prompt,
                key=f"q_{q_id}_future_{i}",
                height=60,
                placeholder="Be specific and vivid..."
            )
        
        total_chars = sum(len(resp) for resp in responses.values())
        min_total = len(prompts) * 15  # More detail for future pacing
        
        if total_chars >= min_total:
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                combined_response = " | ".join([f"{prompts[i]}: {resp}" for i, resp in enumerate(responses.values())])
                self._save_response(q_id, combined_response, question, additional_data=responses)
                self._advance_question()
                st.rerun()
        elif total_chars > 0:
            st.info(f"Please add more vivid details ({min_total - total_chars} more characters)")

    def _advance_question(self):
        """Advance to next question"""
        st.session_state.current_question += 1

    def _go_back(self):
        """Go back one question"""
        if st.session_state.current_question > 1:
            # Remove last response
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
            st.session_state.current_question -= 1

    def _complete_assessment(self):
        """Complete assessment and generate comprehensive analysis"""
        st.session_state.assessment_completed = True
        
        # Generate comprehensive clinical analysis
        clinical_analysis = self._generate_comprehensive_clinical_analysis()
        
        # Store results
        st.session_state.assessment_results = {
            'comprehensive_analysis': clinical_analysis,
            'pattern_scores': dict(st.session_state.pattern_scores),
            'triggered_patterns': list(st.session_state.triggered_patterns),
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'completion_rate': len(st.session_state.assessment_responses) / self._estimate_total_questions(),
            'is_digital_native': st.session_state.is_digital_native
        }
        
        # Add digital analysis if applicable
        if st.session_state.is_digital_native:
            digital_analysis = self._analyze_digital_despair_comprehensive(st.session_state.assessment_responses)
            st.session_state.assessment_results['digital_despair_analysis'] = digital_analysis
        
        st.rerun()

    # ---- Rendering Methods ----
    def render(self):
        """Main render method"""
        apply_clinical_styles()
        
        if not st.session_state.contact_provided:
            if not st.session_state.assessment_completed:
                self._render_assessment()
            else:
                self._render_contact_form()
        else:
            self._render_results()

    def _render_assessment(self):
        """Render the assessment interface"""
        self._render_header()
        
        q_id, question = self._get_current_question()
        
        if q_id is None:
            self._complete_assessment()
            return
        
        self._render_progress()
        self._render_question(q_id, question)
        self._render_navigation()

    def _render_header(self):
        """Render assessment header"""
        time_remaining = self._estimate_time_remaining()
        
        st.info(f"Understanding **your unique behavioral patterns** is the key to **targeted, effective hypnotherapy** that brings rapid, lasting change. This assessment takes about {time_remaining:.0f} minutes to complete.")
        st.markdown("<h2 style='text-align: center;'>Behavioral pattern assessment</h2>", unsafe_allow_html=True)

    def _render_progress(self):
        """Render progress indicator"""
        answered = len(st.session_state.assessment_responses)
        total = self._estimate_total_questions()
        progress = answered / total if total > 0 else 0
        time_remaining = self._estimate_time_remaining()
        
        st.markdown(f"""
        <div class="progress-container">
            <span><strong>Question {answered + 1} of {total}</strong></span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span><strong>{int(progress * 100)}%</strong></span>
        </div>
        <div style="text-align: center; margin-bottom: 1rem; color: #556D7A; font-size: 0.9rem;">
            ~ {time_remaining:.0f} minutes remaining
        </div>
        """, unsafe_allow_html=True)

    def _render_question(self, q_id, question):
        """Render current question"""
        st.markdown(f"### {question['text']}")
        
        # Show clinical insights if patterns are emerging
        if len(st.session_state.assessment_responses) > 8 and st.session_state.pattern_scores:
            self._show_pattern_insights()
        
        # Handle different question types
        q_type = question['type']
        if q_type == 'single_choice':
            self._handle_single_choice(q_id, question)
        elif q_type == 'single_choice_with_intensity':
            self._handle_single_choice_with_intensity(q_id, question)
        elif q_type == 'single_choice_with_follow_up':
            self._handle_single_choice_with_follow_up(q_id, question)
        elif q_type == 'text_with_analysis':
            self._handle_text_with_analysis(q_id, question)
        elif q_type == 'detailed_scenario':
            self._handle_detailed_scenario(q_id, question)
        elif q_type == 'scale_with_follow_up':
            self._handle_scale_with_follow_up(q_id, question)
        elif q_type == 'percentage_slider':
            self._handle_percentage_slider(q_id, question)
        elif q_type == 'detailed_future_pacing':
            self._handle_detailed_future_pacing(q_id, question)

    def _show_pattern_insights(self):
        """Show emerging pattern insights during assessment"""
        if st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
            if top_pattern[1] >= 4:
                pattern_name = self.patterns.get(top_pattern[0], "Unknown")
                intensity = self._classify_pattern_intensity(top_pattern[1])
                
                st.markdown(f"""
                <div class="insight-preview">
                    <strong>💡 Pattern emerging:</strong> {pattern_name} 
                    <span class="pattern-strength-{intensity.lower().replace(' ', '')}">[{intensity} intensity]</span>
                    <br><small>Your responses suggest this may be a primary focus area</small>
                </div>
                """, unsafe_allow_html=True)

    def _render_navigation(self):
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
            pass  # Keep space for symmetry

    def _estimate_time_remaining(self):
        """Estimate remaining time"""
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        
        # Adjust for digital native assessment which may be faster
        if st.session_state.is_digital_native:
            return remaining * 0.9
        else:
            return remaining * 1.0

    def _render_contact_form(self):
        """Render enhanced contact form with clinical preview"""
        st.success("Your comprehensive behavioral pattern analysis is complete!")
        
        # Show preview of analysis
        self._render_analysis_preview()
        
        st.markdown("---")
        st.markdown("**Enter your email to receive your complete personalized analysis:**")
        
        with st.form("contact_form"):
            email = st.text_input("Email*", placeholder="your@email.com")
            name = st.text_input("Full name (optional)", placeholder="Your full name")
            phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
            urgency = st.selectbox(
                "How urgent is addressing this pattern? (optional)",
                ["Not specified", "Extremely urgent - significantly impacting life", 
                 "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
                 "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
            )
            
            marketing_consent = st.checkbox(
                "I consent to receiving follow-up communications about my assessment results and therapeutic services."
            )
            
            submitted = st.form_submit_button("Get my complete clinical analysis", type="primary", use_container_width=True)
            
            if submitted:
                if not email.strip():
                    st.error("❌ Email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    st.error("❌ Valid email address is required")
                elif not marketing_consent:
                    st.error("❌ Please consent to follow-up communications to receive your results")
                else:
                    # Save contact info
                    st.session_state.contact_info = {
                        'name': name.strip() if name.strip() else 'Not provided',
                        'email': email.strip(),
                        'phone': phone.strip() if phone.strip() else 'Not provided',
                        'urgency': urgency,
                        'marketing_consent': marketing_consent,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    # Generate complete clinical report
                    clinical_report = self._generate_complete_clinical_report()
                    
                    # Prepare email data
                    assessment_data = {
                        'contact_info': st.session_state.contact_info,
                        'assessment_results': st.session_state.assessment_results,
                        'responses': st.session_state.assessment_responses,
                        'clinical_report': clinical_report,
                        'completion_timestamp': datetime.now().isoformat()
                    }
                    
                    # Send email
                    try:
                        from utils.email_assess import send_clinical_assessment_results
                        email_success = send_clinical_assessment_results(assessment_data)
                        
                        if email_success:
                            st.success("✅ Complete analysis sent to clinical team!")
                        else:
                            st.warning("⚠️ Assessment saved - our team will contact you directly")
                    except Exception as e:
                        st.info("📧 Assessment completed - our clinical team will review your results")
                    
                    st.session_state.contact_provided = True
                    st.rerun()

    def _render_analysis_preview(self):
        """Render preview of clinical analysis"""
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        
        # Show pattern constellation
        pattern_analysis = analysis.get('pattern_constellation', {})
        if pattern_analysis.get('dominant'):
            dominant = pattern_analysis['dominant']
            st.markdown(f"""
            <div class="clinical-indicator">
                <strong>🎯 Dominant pattern:</strong> {dominant['name']} 
                <span class="pattern-strength-{dominant['intensity'].lower().replace(' ', '')}">[{dominant['intensity']} intensity]</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Show digital analysis if applicable
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                severity_class = f"digital-severity-{severity.lower()}"
                st.markdown(f"""
                <div class="clinical-indicator {severity_class}">
                    <strong>📲 Digital pattern analysis:</strong> {severity} severity ({score:.0f}% score)
                    <br><small>{digital_analysis.get('clinical_recommendation', '')}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Show success predictors
        success_predictors = analysis.get('success_predictors', {})
        if success_predictors:
            success_rate = success_predictors.get('predicted_success_rate', 85)
            confidence = success_predictors.get('confidence_level', 'High')
            
            st.markdown(f"""
            <div class="clinical-indicator">
                <strong>📈 Predicted success rate:</strong> {success_rate}% ({confidence} confidence)
                <br><small>Based on pattern complexity, readiness, and approach optimization</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Teaser for complete analysis
        st.markdown("""
        <div class="analysis-teaser">
            <strong>🔓 Your complete clinical analysis includes:</strong>
            <ul style="text-align: left; margin-top: 0.5rem;">
                <li>Complete behavioral sequence mapping and intervention points</li>
                <li>Core limiting beliefs and subconscious programming analysis</li>
                <li>Secondary gains and transformation resistance predictions</li>
                <li>Personalized hypnotherapy session design and timeline</li>
                <li>Success optimization strategies and maintenance planning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    def _generate_complete_clinical_report(self):
        """Generate complete clinical report for email"""
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        
        # Extract key components
        pattern_analysis = analysis.get('pattern_constellation', {})
        behavioral_sequence = analysis.get('behavioral_sequence', {})
        digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
        core_beliefs = analysis.get('core_limiting_beliefs', {})
        secondary_gains = analysis.get('secondary_gains', {})
        success_predictors = analysis.get('success_predictors', {})
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║                 COMPREHENSIVE CLINICAL ANALYSIS              ║
║              Enhanced Behavioral Pattern Assessment          ║
╚══════════════════════════════════════════════════════════════╝

**CLIENT INFORMATION:**
Name: {st.session_state.contact_info.get('name', 'Not provided')}
Email: {st.session_state.contact_info.get('email', 'Not provided')}
Phone: {st.session_state.contact_info.get('phone', 'Not provided')}
Urgency: {st.session_state.contact_info.get('urgency', 'Not specified')}
Assessment Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**ASSESSMENT METRICS:**
Questions Answered: {len(st.session_state.assessment_responses)}
Completion Rate: {len(st.session_state.assessment_responses) / self._estimate_total_questions() * 100:.1f}%
Assessment Duration: {self._calculate_assessment_duration()}
Engagement Level: {'High' if len(st.session_state.assessment_responses) >= 25 else 'Moderate'}

**PATTERN CONSTELLATION ANALYSIS:**"""

        # Add dominant pattern
        dominant = pattern_analysis.get('dominant', {})
        if dominant:
            report += f"""
Dominant Pattern: {dominant.get('name', 'Unknown')} (Score: {dominant.get('score', 0):.1f}/10)
Intensity Level: {dominant.get('intensity', 'Unknown')}
Clinical Priority: Primary intervention target"""

        # Add supporting patterns
        supporting = pattern_analysis.get('supporting', [])
        if supporting:
            report += f"\n\nSupporting Patterns:"
            for i, pattern in enumerate(supporting[:3], 1):
                report += f"\n{i}. {pattern.get('name', 'Unknown')} (Score: {pattern.get('score', 0):.1f}/10) - {pattern.get('intensity', 'Unknown')} intensity"

        # Add pattern interactions
        interactions = pattern_analysis.get('pattern_interactions', [])
        if interactions:
            report += f"\n\nPattern Interactions:"
            for interaction in interactions[:2]:
                patterns = interaction.get('patterns', [])
                description = interaction.get('interaction', '')
                report += f"\n• {patterns[0]} + {patterns[1]}: {description}"

        # Add complexity assessment
        complexity = pattern_analysis.get('complexity_level', 'Unknown')
        report += f"\n\nPattern Complexity: {complexity}"

        # Add digital despair analysis if applicable
        if st.session_state.is_digital_native and digital_analysis:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║               DIGITAL DESPAIR SYNDROME ANALYSIS             ║
╚══════════════════════════════════════════════════════════════╝

Digital Native Status: Confirmed
Algorithmic Despair Score: {digital_analysis['digital_despair_score']:.1f}% ({digital_analysis['severity_level']} severity)
Clinical Recommendation: {digital_analysis['clinical_recommendation']}

Component Analysis:"""
            
            components = digital_analysis.get('component_scores', {})
            for component, score in components.items():
                level = "HIGH" if score >= 4 else "MODERATE" if score >= 2 else "LOW"
                report += f"\n• {component.replace('_', ' ').title()}: {level} ({score:.1f}/5)"

            # Add therapeutic adaptations
            adaptations = digital_analysis.get('therapeutic_adaptations', [])
            if adaptations:
                report += f"\n\nRequired Therapeutic Adaptations:"
                for i, adaptation in enumerate(adaptations[:5], 1):
                    report += f"\n{i}. {adaptation}"

        # Add behavioral sequence analysis
        sequence = behavioral_sequence.get('complete_sequence', {})
        if sequence:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║              BEHAVIORAL SEQUENCE MAPPING                     ║
╚══════════════════════════════════════════════════════════════╝

Complete Behavioral Chain:"""
            
            sequence_order = [
                ('environmental_trigger', 'Environmental Trigger'),
                ('awareness_point', 'First Awareness Point'),
                ('physical_response', 'Physical Response'),
                ('automatic_thought', 'Automatic Thought'),
                ('behavioral_response', 'Behavioral Response'),
                ('immediate_consequence', 'Immediate Consequence'),
                ('reinforcement_mechanism', 'Reinforcement Pattern')
            ]
            
            for key, label in sequence_order:
                if key in sequence:
                    value = sequence[key]
                    if len(value) > 100:
                        value = value[:97] + "..."
                    report += f"\n→ {label}: {value}"

            # Add intervention points
            intervention_points = behavioral_sequence.get('intervention_points', [])
            if intervention_points:
                report += f"\n\nOptimal Intervention Points:"
                for point in intervention_points[:3]:
                    report += f"\n• {point.get('point', 'Unknown')}: {point.get('intervention', 'Standard intervention')}"

        # Add core beliefs analysis
        if core_beliefs:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║                CORE LIMITING BELIEFS ANALYSIS               ║
╚══════════════════════════════════════════════════════════════╝

Primary Limiting Belief: {core_beliefs.get('primary_belief', 'Requires session exploration')}
Family Programming: {core_beliefs.get('family_programming', 'Not captured')}
Worth Equation: {core_beliefs.get('worth_equation', 'Not captured')}

Subconscious Programming Priority: {'High' if any(core_beliefs.values()) else 'Standard assessment needed'}"""

        # Add secondary gains
        if secondary_gains:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║                 SECONDARY GAINS ANALYSIS                    ║
╚══════════════════════════════════════════════════════════════╝

Protective Function: {secondary_gains.get('primary_protection', 'Emotional protection mechanism')}
Potential Identity Losses: {secondary_gains.get('potential_losses', 'Requires exploration')}
Change Resistance Source: Pattern serves important protective function"""

        # Add success predictors and session design
        if success_predictors:
            success_rate = success_predictors.get('predicted_success_rate', 85)
            readiness = success_predictors.get('readiness_score', 7)
            confidence = success_predictors.get('confidence_level', 'High')
            
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║            SUCCESS PREDICTORS & SESSION DESIGN              ║
╚══════════════════════════════════════════════════════════════╝

Predicted Success Rate: {success_rate}% ({confidence} confidence)
Readiness Score: {readiness}/10
Pattern Complexity: {success_predictors.get('pattern_complexity', 'Unknown')} significant patterns
Completion Engagement: {success_predictors.get('completion_engagement', 0) * 100:.1f}%

Session Design Recommendations:"""
            
            session_design = analysis.get('session_design', {})
            if session_design:
                report += f"\nPreferred Hypnotic Style: {session_design.get('preferred_style', 'Collaborative exploration')}"
                report += f"\nPreferred Change Pace: {session_design.get('preferred_pace', 'Rapid but sustainable')}"
                
                # Add digital adaptations if needed
                digital_adaptations = session_design.get('digital_adaptations', {})
                if digital_adaptations:
                    report += f"\nSession Length: {digital_adaptations.get('session_length', 'Standard 90 minutes')}"
                    report += f"\nAuthority Style: {digital_adaptations.get('authority_style', 'Professional therapeutic')}"
                    report += f"\nLanguage Approach: {digital_adaptations.get('language_style', 'Professional clinical')}"

        # Add intervention priorities
        priorities = analysis.get('intervention_priorities', [])
        if priorities:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║                 INTERVENTION PRIORITIES                     ║
╚══════════════════════════════════════════════════════════════╝

Treatment Prioritization:"""
            for priority in priorities[:4]:
                report += f"\nPriority {priority.get('priority', 'X')}: {priority.get('target', 'Unknown target')}"
                report += f"\n  Approach: {priority.get('approach', 'Standard intervention')}"
                report += f"\n  Session: {priority.get('session', 'TBD')}"

        # Add resistance predictions
        resistance_points = analysis.get('resistance_points', [])
        if resistance_points:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║                RESISTANCE PREDICTION & MANAGEMENT           ║
╚══════════════════════════════════════════════════════════════╝

Predicted Resistance Points:"""
            for resistance in resistance_points[:3]:
                report += f"\nSource: {resistance.get('source', 'Unknown')}"
                report += f"\n  Type: {resistance.get('resistance_type', 'Standard change resistance')}"
                report += f"\n  Management: {resistance.get('management_strategy', 'Standard approach')}\n"

        # Add transformation timeline
        timeline = analysis.get('transformation_timeline', {})
        if timeline:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║                TRANSFORMATION TIMELINE                      ║
╚══════════════════════════════════════════════════════════════╝

Recommended Sessions: {timeline.get('recommended_sessions', 2)}
Initial Shifts: {timeline.get('initial_shifts', '48-72 hours post-session')}
Significant Changes: {timeline.get('significant_changes', '1-2 weeks')}
Full Integration: {timeline.get('full_integration', '4-8 weeks')}
Maintenance: {timeline.get('maintenance', 'Optional check-in')}"""

        # Add therapeutic approach summary
        approach = analysis.get('therapeutic_approach', {})
        if approach:
            report += f"""

╔══════════════════════════════════════════════════════════════╗
║              THERAPEUTIC APPROACH SUMMARY                   ║
╚══════════════════════════════════════════════════════════════╝

Primary Modality: {approach.get('primary_modality', 'Rapid transformation hypnotherapy')}
Session Structure: {approach.get('session_structure', '2+1 session protocol')}
Hypnotic Style: {approach.get('hypnotic_style', 'Collaborative permissive')}"""
            
            if approach.get('specialized_protocol'):
                report += f"\nSpecialized Protocol: {approach['specialized_protocol']}"
            if approach.get('complexity_note'):
                report += f"\nComplexity Note: {approach['complexity_note']}"

        # Add clinical notes and recommendations
        report += f"""

╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL RECOMMENDATIONS                 ║
╚══════════════════════════════════════════════════════════════╝

Priority Actions:
1. Schedule discovery consultation to confirm analysis
2. {"Implement specialized digital-native protocols" if st.session_state.is_digital_native and digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE'] else "Prepare standard hypnotherapy approach"}
3. Address dominant pattern as primary intervention target
4. Plan for predicted resistance patterns

Urgency Level: {st.session_state.contact_info.get('urgency', 'Not specified')}
{"⚠️ PRIORITY CONTACT REQUIRED - High urgency indicated" if 'urgent' in st.session_state.contact_info.get('urgency', '').lower() else "Standard follow-up timeline appropriate"}

Assessment Quality: {'Comprehensive - High confidence in recommendations' if len(st.session_state.assessment_responses) >= 25 else 'Good - Sufficient for initial treatment planning'}

╔══════════════════════════════════════════════════════════════╗
║                      END OF REPORT                          ║
╚══════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Practitioner: Licensed Clinical Hypnotherapist Team
Next Steps: Discovery consultation booking and personalized session scheduling"""

        return report

    def _calculate_assessment_duration(self):
        """Calculate assessment duration"""
        start_time = datetime.fromisoformat(st.session_state.start_time)
        duration = datetime.now() - start_time
        minutes = int(duration.total_seconds() / 60)
        return f"{minutes} minutes"

    def _render_results(self):
        """Render final results page with paywall integration"""
        st.markdown("## Your behavioral pattern analysis")
        
        # Show comprehensive results or paywall
        self._render_clinical_analysis_section()
        
        st.markdown("### Your next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        
        if 'urgent' in urgency.lower():
            st.warning("⚠️ **Priority contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
        st.markdown("""
        **What happens next:**
        
        1. **Clinical review** (24-48 hours): Licensed hypnotherapist analyzes your complete assessment
        2. **Personalized contact** (48-72 hours): Direct outreach via your preferred method  
        3. **Treatment planning** (within 72 hours): Custom hypnotherapy protocol designed for your specific patterns
        
        **Ready to begin transformation?** Visit **[hypnotherapy.streamlit.app](https://hypnotherapy.streamlit.app)** to learn about our proven rapid change methodology.
        
        **Questions about your analysis?** Reply to any email from our team or contact us directly.
        """)
        
        # Add scheduling CTA
        st.markdown(f"""
        <div class="text-center">
            <a href="{self.discovery_url}" 
               target="_blank" 
               class="cta-button">
               📞 Schedule your transformation session
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
                    'is_digital_native': st.session_state.is_digital_native,
                    'comprehensive_analysis': st.session_state.assessment_results.get('comprehensive_analysis', {}),
                    'contact_info': st.session_state.get('contact_info', {})
                }
                
                if paywall.check_payment_status():
                    paywall.render_premium_analysis(assessment_data)
                else:
                    self._render_enhanced_preview()
                    with st.expander("🔓 Unlock complete clinical analysis", expanded=False):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading premium analysis: {str(e)}")
                self._render_enhanced_preview()
        else:
            st.info("💡 **Complete clinical analysis available**: Comprehensive insights, personalized treatment planning, and detailed session design available with premium access.")
            self._render_enhanced_preview()

    def _render_enhanced_preview(self):
        """Render enhanced preview of analysis"""
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        
        # Show pattern constellation preview
        pattern_analysis = analysis.get('pattern_constellation', {})
        if pattern_analysis.get('dominant'):
            dominant = pattern_analysis['dominant']
            supporting = pattern_analysis.get('supporting', [])
            
            st.markdown(f"**🎯 Your behavioral pattern constellation:**")
            
            # Dominant pattern
            intensity_class = dominant['intensity'].lower().replace(' ', '')
            st.markdown(f"""
            <div style="background: #f8fafc; padding: 1rem; border-left: 4px solid #4CA1A3; margin: 0.5rem 0;">
                <strong>Primary pattern:</strong> {dominant['name']}<br>
                <span class="pattern-strength-{intensity_class}">Intensity: {dominant['intensity']} ({dominant['score']:.1f}/10)</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Supporting patterns teaser
            if supporting:
                patterns_preview = ", ".join([p['name'] for p in supporting[:2]])
                remaining = len(supporting) - 2
                if remaining > 0:
                    patterns_preview += f" + {remaining} more"
                
                st.markdown(f"**Supporting patterns:** {patterns_preview}")
        
        # Show digital analysis preview if applicable
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                severity_class = f"digital-severity-{severity.lower()}"
                st.markdown(f"""
                <div class="clinical-indicator {severity_class}" style="margin: 1rem 0;">
                    <strong>📲 Digital pattern analysis:</strong> {severity} severity ({score:.0f}% score)<br>
                    <small>Requires {"specialized intervention protocols" if severity in ['SEVERE', 'MODERATE'] else "standard approach with digital awareness"}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Show success predictor preview
        success_predictors = analysis.get('success_predictors', {})
        if success_predictors:
            success_rate = success_predictors.get('predicted_success_rate', 85)
            confidence = success_predictors.get('confidence_level', 'High')
            
            st.markdown(f"""
            <div style="background: #f0f9ff; padding: 1rem; border-radius: 6px; margin: 1rem 0;">
                <strong>📈 Transformation probability:</strong> {success_rate}% ({confidence.lower()} confidence)<br>
                <small>Based on pattern analysis, readiness assessment, and approach optimization</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Enhanced teaser for complete analysis
        st.markdown("""
        <div class="analysis-teaser">
            <h4>🔓 Your complete clinical analysis reveals:</h4>
            <div style="text-align: left; margin-top: 1rem;">
                <strong>📋 Behavioral Sequence Mapping:</strong><br>
                <small>• Complete trigger-to-consequence chain analysis<br>
                • Optimal intervention points for maximum effectiveness<br>
                • Breaking points for rapid pattern interruption</small>
                
                <br><br><strong>🧠 Subconscious Programming Analysis:</strong><br>
                <small>• Core limiting beliefs driving your patterns<br>
                • Secondary gains and hidden benefits of current behaviors<br>
                • Identity threats and transformation resistance predictions</small>
                
                <br><br><strong>⚡ Personalized Treatment Protocol:</strong><br>
                <small>• Custom hypnotherapy session design for your brain type<br>
                • Specific intervention priorities and sequencing<br>
                • Success optimization strategies and timeline predictions</small>
                
                <br><br><strong>🎯 Session-by-Session Roadmap:</strong><br>
                <small>• Exact therapeutic approach for your pattern constellation<br>
                • Predicted resistance points and management strategies<br>
                • Integration support and long-term maintenance planning</small>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---- Main Application Class ----
class AssessPage:
    """Enhanced assessment page with comprehensive clinical analysis"""
    
    def __init__(self):
        self.assessment = ComprehensiveBehavioralAssessment()
    
    def render(self):
        self.assessment.render()


# ---- Factory Function ----
def create_assess_page():
    """Factory function to create the enhanced assessment page"""
    return AssessPage()


# ---- Helper Functions ----
def get_assessment_summary():
    """Get comprehensive assessment summary"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results
    return None

def get_comprehensive_analysis():
    """Get complete clinical analysis"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results.get('comprehensive_analysis')
    return None

def get_pattern_scores():
    """Get enhanced pattern scores with intensities"""
    if 'pattern_scores' in st.session_state:
        return st.session_state.pattern_scores
    return {}

def get_digital_analysis():
    """Get comprehensive digital despair analysis"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results.get('digital_despair_analysis')
    return None

def is_digital_native():
    """Check digital native status"""
    return st.session_state.get('is_digital_native', False)

def get_behavioral_sequence():
    """Get complete behavioral sequence mapping"""
    if 'assessment_results' in st.session_state:
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        return analysis.get('behavioral_sequence', {})
    return {}

def get_success_predictors():
    """Get success predictors and optimization strategies"""
    if 'assessment_results' in st.session_state:
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        return analysis.get('success_predictors', {})
    return {}

def get_intervention_priorities():
    """Get ranked intervention priorities"""
    if 'assessment_results' in st.session_state:
        analysis = st.session_state.assessment_results.get('comprehensive_analysis', {})
        return analysis.get('intervention_priorities', [])
    return []

def reset_assessment():
    """Reset all assessment state"""
    keys_to_reset = [
        'assessment_responses', 'current_question', 'current_phase',
        'is_digital_native', 'digital_despair_score', 'digital_severity',
        'triggered_patterns', 'pattern_scores', 'pattern_intensities',
        'behavioral_sequence', 'secondary_gains', 'core_beliefs',
        'systemic_resistance', 'transformation_blockers', 'readiness_indicators',
        'hypnotic_preferences', 'assessment_completed', 'contact_provided',
        'assessment_results', 'adaptive_questions', 'clinical_insights',
        'session_design', 'success_predictors'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]

def export_comprehensive_assessment():
    """Export complete assessment data including all analysis"""
    if 'assessment_responses' not in st.session_state:
        return None
    
    return {
        'responses': st.session_state.assessment_responses,
        'comprehensive_analysis': st.session_state.assessment_results.get('comprehensive_analysis', {}),
        'pattern_scores': st.session_state.get('pattern_scores', {}),
        'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
        'behavioral_sequence': st.session_state.get('behavioral_sequence', {}),
        'core_beliefs': st.session_state.get('core_beliefs', {}),
        'secondary_gains': st.session_state.get('secondary_gains', {}),
        'success_predictors': st.session_state.get('success_predictors', {}),
        'is_digital_native': st.session_state.get('is_digital_native', False),
        'digital_analysis': st.session_state.assessment_results.get('digital_despair_analysis'),
        'contact_info': st.session_state.get('contact_info', {}),
        'results': st.session_state.get('assessment_results', {}),
        'completion_timestamp': datetime.now().isoformat()
    }


if __name__ == "__main__":
    st.set_page_config(
        page_title="Enhanced Clinical Behavioral Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render()
