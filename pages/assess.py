# # Enhanced Clinical Behavioral Pattern Assessment - Complete Redesign
# # Comprehensive implementation with adaptive questioning and pattern detection
# # Optimized for engagement, honesty, and complete behavioral mapping

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
#     """Clinical-grade behavioral pattern assessment with adaptive questioning flow"""
    
#     def __init__(self):
#         self._init_session_state()
#         self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
#         self.patterns = {
#             1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
#             4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
#             7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
#         }
        
#         # Question pools organized by phase
#         self.engagement_questions = self._get_engagement_questions()
#         self.trigger_mapping_questions = self._get_trigger_mapping_questions()
#         self.pattern_specific_questions = self._get_pattern_specific_questions()
#         self.integration_questions = self._get_integration_questions()

#     def _init_session_state(self):
#         defaults = {
#             'assessment_responses': {},
#             'current_question': 1,
#             'current_phase': 'engagement',
#             'phase_progress': {'engagement': 0, 'trigger_mapping': 0, 'pattern_specific': 0, 'integration': 0},
#             'triggered_patterns': set(),
#             'pattern_scores': {},
#             'risk_flags': [],
#             'assessment_completed': False,
#             'contact_provided': False,
#             'assessment_results': {},
#             'start_time': datetime.now().isoformat(),
#             'intensity_responses': {},
#             'motivation_data': {},
#             'trigger_chain': {},
#             'response_chain': {},
#             'adaptive_paths': []
#         }
#         for key, value in defaults.items():
#             if key not in st.session_state:
#                 st.session_state[key] = value

#     def _get_engagement_questions(self):
#         """Phase 1: Engagement & Initial Pattern Detection"""
#         return {
#             1: {
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
#             2: {
#                 "text": "If this issue completely resolved, what would be different about your daily life?",
#                 "type": "text_completion",
#                 "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
#                 "min_chars": 5,
#                 "pattern_analysis": True,
#                 "keywords": {
#                     "productivity": [5], "relationships": [2, 3, 6, 7], "peace": [1], 
#                     "authentic": [6], "happy": [1], "control": [2, 4], "boundaries": [7, 9]
#                 },
#                 "phase": "engagement"
#             },
#             3: {
#                 "text": "How ready are you to completely let go of this pattern? (1-10 scale)",
#                 "type": "scale_10",
#                 "labels": ["Not ready at all", "Completely ready"],
#                 "follow_up_trigger": 7,  # If 7 or below, ask follow-up
#                 "phase": "engagement"
#             },
#             4: {
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
#             5: {
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
#         """Phase 2: Core Trigger Mapping"""
#         return {
#             6: {
#                 "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
#                 "type": "text_completion",
#                 "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
#                 "min_chars": 5,
#                 "trigger_analysis": True,
#                 "phase": "trigger_mapping"
#             },
#             7: {
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
#             8: {
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
#             9: {
#                 "text": "What thought automatically appears when you feel that physical sensation?",
#                 "type": "text_completion",
#                 "placeholder": "The actual words that go through your mind - even if they seem harsh or unreasonable. What does your inner voice say?",
#                 "min_chars": 5,
#                 "pattern_keywords": {
#                     "not good enough": [1], "fight": [2], "can't trust": [3], 
#                     "either or": [4], "must do": [5], "can't be real": [6],
#                     "others need": [7], "should": [8], "can't handle": [9]
#                 },
#                 "chain_mapping": "automatic_thought",
#                 "phase": "trigger_mapping"
#             },
#             10: {
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
#             11: {
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
#             12: {
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
#             13: {
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
#         """Phase 3: Adaptive Pattern-Specific Deep Dives"""
#         return {
#             # Pattern 1: Unhappiness Culture
#             "pattern_1": {
#                 14: {
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
#                 15: {
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
#                 16: {
#                     "text": "What would you lose if you allowed yourself to be genuinely happy?",
#                     "type": "text_completion",
#                     "placeholder": "Think about identity, relationships, what others might think, or what might change...",
#                     "min_chars": 5,
#                     "pattern": 1
#                 }
#             },
            
#             # Pattern 2: Power Struggles
#             "pattern_2": {
#                 17: {
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
#                 18: {
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
#                 },
#                 19: {
#                     "text": "What are you most afraid would happen if you stopped fighting for your position?",
#                     "type": "text_completion",
#                     "placeholder": "Consider what you might lose, how others might treat you, or what might change...",
#                     "min_chars": 5,
#                     "pattern": 2
#                 }
#             },
            
#             # Pattern 3: Systematic Mistrust
#             "pattern_3": {
#                 20: {
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
#                 21: {
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
#                 },
#                 22: {
#                     "text": "What's the worst thing that could happen if you trusted someone completely?",
#                     "type": "text_completion",
#                     "placeholder": "What specific betrayal, hurt, or loss do you fear most?",
#                     "min_chars": 5,
#                     "pattern": 3
#                 }
#             },
            
#             # Pattern 4: Separation/Division
#             "pattern_4": {
#                 23: {
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
#                 },
#                 24: {
#                     "text": "Complete this sentence: 'If I don't choose perfectly, then...'",
#                     "type": "text_completion",
#                     "placeholder": "What catastrophic outcome do you imagine?",
#                     "min_chars": 5,
#                     "pattern": 4
#                 },
#                 25: {
#                     "text": "What would become possible if you could embrace 'both/and' instead of 'either/or'?",
#                     "type": "text_completion",
#                     "placeholder": "Imagine having more options and flexibility in your choices...",
#                     "min_chars": 5,
#                     "pattern": 4
#                 }
#             },
            
#             # Pattern 5: Doing vs Being
#             "pattern_5": {
#                 26: {
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
#                 },
#                 27: {
#                     "text": "If you stopped being productive for a month, you'd worry that:",
#                     "type": "text_completion",
#                     "placeholder": "Complete the thought: you'd worry that others would think... or that you would...",
#                     "min_chars": 5,
#                     "pattern": 5
#                 },
#                 28: {
#                     "text": "Who first taught you that your value depends on what you produce?",
#                     "type": "text_completion",
#                     "placeholder": "Think about early messages from family, school, or society...",
#                     "min_chars": 5,
#                     "pattern": 5
#                 }
#             },
            
#             # Pattern 6: Compartmentalized Authenticity
#             "pattern_6": {
#                 29: {
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
#                 },
#                 30: {
#                     "text": "The 'real you' is:",
#                     "type": "single_choice",
#                     "options": [
#                         "Pretty much what people see",
#                         "Only visible to very close friends",
#                         "Something you're still discovering",
#                         "Different depending on the situation",
#                         "Hidden to protect yourself"
#                     ],
#                     "weights": [0, 1, 2, 3, 3],
#                     "pattern": 6
#                 },
#                 31: {
#                     "text": "What would you risk losing if you showed up authentically everywhere?",
#                     "type": "text_completion",
#                     "placeholder": "Consider relationships, opportunities, safety, or acceptance you might lose...",
#                     "min_chars": 5,
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
#                 },
#                 33: {
#                     "text": "When someone offers to help you, you typically:",
#                     "type": "single_choice",
#                     "options": [
#                         "Accept gratefully",
#                         "Feel uncomfortable accepting",
#                         "Immediately think of how to reciprocate",
#                         "Worry about being a burden",
#                         "Decline even when you need help"
#                     ],
#                     "weights": [0, 2, 2, 3, 3],
#                     "pattern": 7
#                 },
#                 34: {
#                     "text": "What would others lose if you started prioritizing your own wellbeing?",
#                     "type": "text_completion",
#                     "placeholder": "Think about who depends on your self-sacrifice and what they'd have to give up...",
#                     "min_chars": 5,
#                     "pattern": 7
#                 }
#             },
            
#             # Pattern 8: Inherited Missions
#             "pattern_8": {
#                 35: {
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
#                 },
#                 36: {
#                     "text": "When you imagine disappointing your family:",
#                     "type": "single_choice",
#                     "options": [
#                         "It doesn't significantly concern you",
#                         "You feel guilty but would survive it",
#                         "It feels like betraying their love",
#                         "You worry about losing their approval",
#                         "It's almost unthinkable"
#                     ],
#                     "weights": [0, 1, 3, 2, 4],
#                     "pattern": 8
#                 },
#                 37: {
#                     "text": "What would pursuing your own path cost your family relationships?",
#                     "type": "text_completion",
#                     "placeholder": "Consider how they might react, what they might lose, or how relationships might change...",
#                     "min_chars": 5,
#                     "pattern": 8
#                 }
#             },
            
#             # Pattern 9: Context-Dependent Weakness
#             "pattern_9": {
#                 38: {
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
#                 },
#                 39: {
#                     "text": "There are certain people or situations where you:",
#                     "type": "single_choice",
#                     "options": [
#                         "Stay true to your values",
#                         "Become someone you don't recognize",
#                         "Lose all sense of personal power",
#                         "Can't access your usual strength",
#                         "Feel completely overwhelmed"
#                     ],
#                     "weights": [0, 2, 3, 3, 4],
#                     "pattern": 9
#                 },
#                 40: {
#                     "text": "What is it about these specific contexts that overwhelms your usual coping?",
#                     "type": "text_completion",
#                     "placeholder": "Think about the people, environments, or dynamics that make you lose yourself...",
#                     "min_chars": 5,
#                     "pattern": 9
#                 }
#             }
#         }

#     def _get_integration_questions(self):
#         """Phase 4: Integration & Change Readiness"""
#         return {
#             41: {
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
#             42: {
#                 "text": "What would need to be true for you to feel completely safe changing this pattern?",
#                 "type": "text_completion",
#                 "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
#                 "min_chars": 5,
#                 "safety_assessment": True,
#                 "phase": "integration"
#             },
#             43: {
#                 "text": "If you were transforming this pattern, your support system is:",
#                 "type": "single_choice",
#                 "options": [
#                     "Strong - multiple people who'd encourage change",
#                     "Moderate - some people who'd support you",
#                     "Mixed - some would support, others might resist",
#                     "Weak - mostly dealing with this alone",
#                     "Unsure - haven't thought about who would support change"
#                 ],
#                 "support_assessment": True,
#                 "risk_weights": [0, 0, 1, 2, 1],
#                 "phase": "integration"
#             },
#             44: {
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
#             45: {
#                 "text": "Imagine you've completely transformed this pattern. What's the first thing you'd do that you can't do now?",
#                 "type": "text_completion",
#                 "placeholder": "Be specific about the first action, conversation, or decision you'd make...",
#                 "min_chars": 5,
#                 "outcome_visualization": True,
#                 "phase": "integration"
#             }
#         }

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
        
#         # Phase 1: Engagement (Questions 1-5)
#         if st.session_state.current_phase == 'engagement':
#             for q_id in range(1, 6):
#                 if q_id not in answered:
#                     return q_id, self.engagement_questions[q_id]
#             st.session_state.current_phase = 'trigger_mapping'
        
#         # Phase 2: Trigger Mapping (Questions 6-13)
#         if st.session_state.current_phase == 'trigger_mapping':
#             for q_id in range(6, 14):
#                 if q_id not in answered:
#                     return q_id, self.trigger_mapping_questions[q_id]
#             st.session_state.current_phase = 'pattern_specific'
        
#         # Phase 3: Pattern-Specific Questions
#         if st.session_state.current_phase == 'pattern_specific':
#             for pattern_id in st.session_state.triggered_patterns:
#                 pattern_key = f"pattern_{pattern_id}"
#                 if pattern_key in self.pattern_specific_questions:
#                     pattern_questions = self.pattern_specific_questions[pattern_key]
#                     for q_id, question in pattern_questions.items():
#                         if q_id not in answered:
#                             return q_id, question
#             st.session_state.current_phase = 'integration'
        
#         # Phase 4: Integration (Questions 41-45)
#         if st.session_state.current_phase == 'integration':
#             for q_id in range(41, 46):
#                 if q_id not in answered:
#                     return q_id, self.integration_questions[q_id]
        
#         return None, None

#     def _estimate_total_questions(self):
#         """Estimate total questions based on triggered patterns"""
#         base_questions = 5 + 8 + 5  # engagement + trigger_mapping + integration
#         pattern_questions = len(st.session_state.triggered_patterns) * 3  # 3 questions per pattern
#         return base_questions + pattern_questions

#     def _estimate_time_remaining(self):
#         """Estimate remaining time"""
#         total_q = self._estimate_total_questions()
#         answered = len(st.session_state.assessment_responses)
#         remaining = max(0, total_q - answered)
#         return remaining * 1.0  # 1 minute per question average

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
#         min_chars = question.get('min_chars', 5)
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
#             #st.markdown(f"<div class='char-counter {color_class}'>{char_count}/{min_chars} characters minimum</div>", unsafe_allow_html=True)
        
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
#         if value <= question.get('follow_up_trigger', 5):
#             follow_up = st.text_input(
#                 "What would need to happen to make it a 10?",
#                 key=f"q_{q_id}_followup",
#                 placeholder="What would increase your readiness?"
#             )
#         else:
#             follow_up = ""
        
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
#             st.info(f"Understanding **your unique behavioral patterns** is the key to **targeted, effective hypnotherapy** that brings rapid, lasting change. This assessment takes about {time_remaining:.0f} minutes to complete.")

#         st.markdown("<h2 style='text-align: center;'>Behavioral pattern assessment</h1>", unsafe_allow_html=True)

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

#         # Question display
#         st.markdown(f"### {question['text']}")
        
#         # Show pattern detection hints for engaged users
#         if completed > 5 and st.session_state.pattern_scores:
#             top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
#             if top_pattern[1] >= 2.0:
#                 pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
#                 # st.markdown(f"""
#                 # <div class="pattern-hint">
#                 # Pattern emerging: {pattern_name} - this helps us customize your approach
#                 # </div>
#                 # """, unsafe_allow_html=True)

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
#             if st.button("Skip", key="nav_skip", use_container_width=True):
#                 skip_question = {"text": "Skipped", "type": "skip", "phase": "skip"}
#                 self._save_response(current_q_id, "Skipped", skip_question)
#                 self._advance_question()
#                 st.rerun()

#     def _generate_behavioral_sequence_analysis(self):
#         """Generate comprehensive behavioral sequence mapping for clinical email"""
#         trigger_chain = st.session_state.get('trigger_chain', {})
#         responses = st.session_state.get('assessment_responses', {})
#         intensity_responses = st.session_state.get('intensity_responses', {})
        
#         # Build comprehensive sequence analysis
#         sequence_analysis = """
# ╔══════════════════════════════════════════════════════════════╗
# ║            COMPLETE BEHAVIORAL SEQUENCE MAPPING             ║
# ╚══════════════════════════════════════════════════════════════╝

# 🎯 TRIGGER (Awareness Point)
# """
        
#         # Extract trigger information
#         trigger_info = trigger_chain.get('awareness_point', 'Not captured')
#         if trigger_info != 'Not captured':
#             sequence_analysis += f"""
# Captured: "{trigger_info}"

# Clinical Notes:
# - Trigger type: {self._analyze_trigger_type(trigger_info)}
# - Activation pattern: {self._analyze_activation_pattern(trigger_info)}
# - Environmental factors: {self._extract_environmental_factors(responses)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: Specific trigger identification needed
# Clinical Impact: Session 1 priority - complete trigger mapping
# """
    
#         # Physical Response Analysis
#         sequence_analysis += """

# 💓 PHYSICAL RESPONSE
# """
        
#         physical_response = trigger_chain.get('physical_response', 'Not captured')
#         if physical_response != 'Not captured':
#             intensity = self._get_response_intensity('physical_response')
#             sequence_analysis += f"""
# Captured: "{physical_response}"

# Clinical Analysis:
# - Somatic location: {self._analyze_somatic_location(physical_response)}
# - Activation system: {self._analyze_activation_system(physical_response)}
# - Intensity level: {intensity}/7
# - Clinical significance: {self._get_somatic_significance(physical_response)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: Physical sensation mapping needed
# Clinical Impact: Essential for somatic intervention design
# """
    
#         # Automatic Thought Analysis
#         sequence_analysis += """

# 💭 AUTOMATIC THOUGHT
# """
        
#         automatic_thought = trigger_chain.get('automatic_thought', 'Not captured')
#         if automatic_thought != 'Not captured' and automatic_thought != 'Skipped':
#             sequence_analysis += f"""
# Captured: "{automatic_thought}"

# Clinical Analysis:
# - Cognitive distortion type: {self._analyze_cognitive_distortion(automatic_thought)}
# - Core belief indicator: {self._extract_core_belief_from_thought(automatic_thought)}
# - Therapeutic target: {self._get_thought_intervention_target(automatic_thought)}
# - Language pattern: {self._analyze_language_pattern(automatic_thought)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: The specific automatic thoughts that occur between physical sensation and behavioral response
# Clinical Impact: This gap needs filling in Session 1 for complete intervention mapping
# """
    
#         # Emotional Response Analysis
#         sequence_analysis += """

# ❤️ EMOTIONAL RESPONSE
# """
        
#         emotional_response = trigger_chain.get('emotional_response', 'Not captured')
#         if emotional_response != 'Not captured':
#             if isinstance(emotional_response, dict):
#                 emotions_list = [f"{emotion} (intensity: {intensity}/7)" for emotion, intensity in emotional_response.items()]
#                 emotions_text = ", ".join(emotions_list)
#             else:
#                 emotions_text = str(emotional_response)
                
#             sequence_analysis += f"""
# Captured: {emotions_text}

# Clinical Analysis:
# - Emotional constellation: {self._analyze_emotional_constellation(emotional_response)}
# - Regulation capacity: {self._assess_regulation_capacity(emotional_response)}
# - Intervention approach: {self._get_emotional_intervention(emotional_response)}
# """
#         else:
#             sequence_analysis += """
# Status: PARTIALLY CAPTURED - implied through consequences
# Inferred from consequences: Agitation, upset, possibly anxiety
# Missing specifics: Exact emotions, intensity levels, emotional progression
# """
    
#         # Behavioral Response Analysis
#         sequence_analysis += """

# 🏃 BEHAVIORAL RESPONSE
# """
        
#         behavioral_response = trigger_chain.get('behavioral_response', 'Not captured')
#         if behavioral_response != 'Not captured':
#             sequence_analysis += f"""
# Captured: "{behavioral_response}"

# Clinical Analysis:
# - Response pattern: {self._analyze_behavioral_pattern(behavioral_response)}
# - Function analysis: {self._analyze_behavioral_function(behavioral_response)}
# - Pattern fit: {self._assess_pattern_alignment(behavioral_response)}
# - Intervention point: {self._get_behavioral_intervention_point(behavioral_response)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: Specific behavioral response to emotional activation
# Clinical Impact: Cannot design behavioral intervention without this data
# """
    
#         # Immediate Consequences
#         sequence_analysis += """

# ⚡ IMMEDIATE CONSEQUENCES
# """
        
#         immediate_consequence = trigger_chain.get('immediate_consequence', 'Not captured')
#         if immediate_consequence != 'Not captured':
#             sequence_analysis += f"""
# Captured: "{immediate_consequence}"

# Clinical Analysis:
# - Consequence type: {self._analyze_consequence_type(immediate_consequence)}
# - Reinforcement pattern: {self._analyze_reinforcement_pattern(immediate_consequence)}
# - Intervention timing: {self._get_consequence_intervention_timing(immediate_consequence)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: Immediate aftermath of behavioral response
# Clinical Impact: Cannot assess pattern reinforcement cycle
# """
    
#         # Longer-term Impact
#         sequence_analysis += """

# 📈 LONGER-TERM IMPACT
# """
        
#         longer_impact = trigger_chain.get('longer_term_impact', 'Not captured')
#         if longer_impact != 'Not captured':
#             sequence_analysis += f"""
# Captured: "{longer_impact}"

# Clinical Analysis:
# - Pattern reinforcement: {self._analyze_pattern_reinforcement(longer_impact)}
# - Cycle completion: {self._assess_cycle_completion(longer_impact)}
# - Breaking point identification: {self._identify_breaking_points(longer_impact)}
# """
#         else:
#             sequence_analysis += """
# Status: NOT CAPTURED in this assessment
# Missing Data: Long-term pattern impact and reinforcement
# Clinical Impact: Cannot assess full cycle for intervention design
# """
    
#         # Add chain completion assessment
#         completion_percentage = self._calculate_chain_completeness()
#         sequence_analysis += f"""

# 📊 CHAIN COMPLETION ANALYSIS

# Overall Chain Completeness: {completion_percentage}%

# {"✅ SUFFICIENT for initial intervention design" if completion_percentage >= 60 else "❌ INSUFFICIENT - Session 1 must prioritize chain completion"}

# Missing Chain Components for Session 1 Exploration:

# 🔍 Critical Gaps to Fill:
# """
        
#         # Identify missing components
#         missing_components = self._identify_missing_components()
#         for component in missing_components:
#             sequence_analysis += f"• {component}\n"
        
#         if not missing_components:
#             sequence_analysis += "• No critical gaps identified - proceed with intervention\n"
    
#         sequence_analysis += """

# Session 1 Chain Completion Protocol:

# Priority Mapping Areas:
# - Thought Content: "When you feel that physical sensation, what thought goes through your mind?"
# - Emotional Bridge: "Between feeling the sensation and taking action, what emotions show up?"
# - Trigger Details: "What specific situations or thoughts tend to set this whole sequence in motion?"

# Chain Intervention Strategy:

# Based on captured elements, primary intervention points would be:
# - Somatic Interruption: Work with physical sensations as early warning system
# - Cognitive Reframing: Address automatic thought patterns
# - Emotional Regulation: Install healthy emotional processing
# - Behavioral Redirection: Replace maladaptive responses with healthy alternatives
# - Consequence Reframing: Address reinforcement patterns directly

# Clinical Assessment Quality

# Strengths:
# - Clear behavioral sequence foundation established
# - Physical response well-defined for somatic work
# - Pattern scores provide intervention direction

# Areas for Session 1 Completion:
# - Complete missing chain elements
# - Intensify successful components
# - Validate sequence accuracy with client
# """
        
#         return sequence_analysis

#     def _render_contact_form(self):
#         """Render contact form for results with enhanced clinical data"""
#         st.markdown("### Assessment Complete!")
#         st.success("Your comprehensive behavioral pattern analysis is ready!")
        
#         results = st.session_state.assessment_results
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.metric("Questions", results['total_questions_answered'], "Answered")
#         with col2:
#             st.metric("Patterns", len(results.get('pattern_scores', {})), "Detected")
#         with col3:
#             completion_rate = results.get('completion_rate', 1.0)
#             st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")
    
#         st.markdown("**Enter your email to receive your personalized analysis and next steps:**")
        
#         with st.form("contact_form"):
#             # ONLY EMAIL IS MANDATORY
#             email = st.text_input("Email*", placeholder="your@email.com")
            
#             # ALL OTHER FIELDS ARE OPTIONAL
#             name = st.text_input("Full name (optional)", placeholder="Your full name")
#             phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
#             urgency = st.selectbox(
#                 "How urgent is addressing this pattern? (optional)",
#                 ["Not specified", "Extremely urgent - significantly impacting life", 
#                  "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
#                  "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
#             )
            
#             concern = st.text_area(
#                 "What brought you to this assessment? (optional)",
#                 placeholder="Brief description of what motivated you to take this assessment...",
#                 height=100
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
                    
#                     # GENERATE CLINICAL TEMPLATE
#                     clinical_template = self._format_clinical_template()
                    
#                     # Prepare assessment data for email with clinical template
#                     assessment_data = {
#                         'contact_info': st.session_state.contact_info,
#                         'assessment_results': st.session_state.assessment_results,
#                         'assessment_responses': st.session_state.assessment_responses,
#                         'intensity_responses': st.session_state.intensity_responses,
#                         'adaptive_triggered': st.session_state.adaptive_paths,
#                         'risk_flags': st.session_state.risk_flags,
#                         'pattern_scores': st.session_state.pattern_scores,
#                         'trigger_chain': st.session_state.trigger_chain,
#                         'clinical_template': clinical_template,  # ADD THIS LINE
#                         'start_time': st.session_state.start_time,
#                         'completion_timestamp': datetime.now().isoformat()
#                     }
                    
#                     # Send comprehensive clinical assessment email
#                     try:
#                         #from utils.email_handler import send_clinical_assessment_results
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

#     def _render_results(self):
#         """Render final results page"""
#         st.markdown("## Your behavioral pattern analysis")
        
#         # Direct to clinical analysis without success message or metrics
#         self._render_clinical_analysis_section()
    
#         st.markdown("### Your next steps")
        
#         contact_info = st.session_state.get('contact_info', {})
#         next_step = contact_info.get('next_step', '')
#         urgency = contact_info.get('urgency', '')
        
#         if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
#             st.warning("⚠️ **Priority contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
#         st.markdown("""
#         **What happens next:**
    
#         1. **Clinical review** (24-48 hours): Licensed therapist analyzes your responses
#         2. **Personalized protocol** (48-72 hours): Custom hypnotherapy approach designed for your patterns  
#         3. **Initial contact** (within 72 hours): We'll reach out via your preferred method
        
#         **Want to understand our proven method?** Visit [hypnotherapy.streamlit.app](https://hypnotherapy.streamlit.app) to learn about our rapid transformation hypnotherapy approach.
        
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
    
#     #Enhanced Clinical Analysis Methods for assess.py
#     #Add these methods to the ComprehensiveBehavioralAssessment class
    
#     def _extract_clinical_insights(self):
#         """Extract comprehensive clinical insights from assessment responses"""
#         results = st.session_state.assessment_results
#         responses = st.session_state.assessment_responses
#         pattern_scores = st.session_state.pattern_scores
        
#         # Initialize clinical insights
#         clinical_insights = {}
        
#         # Extract Core Limiting Belief
#         clinical_insights['core_limiting_belief'] = self._extract_core_limiting_belief(responses, pattern_scores)
        
#         # Extract Hidden Benefits (Secondary Gains)
#         clinical_insights['hidden_benefits'] = self._extract_hidden_benefits(responses)
        
#         # Extract Systemic Resistance
#         clinical_insights['systemic_resistance'] = self._extract_systemic_resistance(responses, pattern_scores)
        
#         # Extract Identity Threat
#         clinical_insights['identity_threat'] = self._extract_identity_threat(responses, pattern_scores)
        
#         # Extract Intervention Keywords
#         clinical_insights['intervention_keywords'] = self._extract_intervention_keywords(pattern_scores)
        
#         # Extract Language to Avoid
#         clinical_insights['avoid_language'] = self._extract_avoid_language(pattern_scores)
        
#         # Extract Predicted Resistance Points
#         clinical_insights['resistance_points'] = self._extract_resistance_points(responses, pattern_scores)
        
#         return clinical_insights
    
#     def _extract_core_limiting_belief(self, responses, pattern_scores):
#         """Extract the core limiting belief from text responses"""
#         belief_indicators = {
#             "not good enough": "I am fundamentally inadequate/unworthy",
#             "can't trust": "Others will inevitably betray or harm me", 
#             "must be perfect": "Any mistake proves my worthlessness",
#             "others first": "My needs and wants are less important than others'",
#             "can't handle": "I am too weak/fragile to cope with life's challenges",
#             "should": "I must meet external expectations to be acceptable",
#             "either or": "Life offers only extreme choices with no middle ground",
#             "not real": "Showing my true self will lead to rejection",
#             "must do": "My value depends entirely on what I accomplish"
#         }
        
#         # Analyze text responses for belief patterns
#         text_responses = []
#         for response_data in responses.values():
#             if isinstance(response_data.get('response'), str):
#                 text_responses.append(response_data['response'].lower())
        
#         combined_text = ' '.join(text_responses)
        
#         # Check for belief indicators
#         for indicator, belief in belief_indicators.items():
#             if indicator in combined_text:
#                 return belief
        
#         # Fallback based on dominant pattern
#         if pattern_scores:
#             dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
#             pattern_beliefs = {
#                 1: "Happiness and positive emotions are dangerous or undeserved",
#                 2: "I must fight to maintain control or I'll be powerless",
#                 3: "Others cannot be trusted with my vulnerability or truth",
#                 4: "Life is black and white - there are no good compromises",
#                 5: "I am only valuable when I'm being productive or achieving",
#                 6: "Showing my real self will result in rejection or judgment",
#                 7: "Others' needs matter more than my own wellbeing",
#                 8: "I must fulfill family expectations to maintain love/belonging",
#                 9: "I am powerless in certain situations or with certain people"
#             }
#             return pattern_beliefs.get(dominant_pattern, "Core belief requires further exploration")
        
#         return "Core belief requires further exploration"
    
#     def _extract_hidden_benefits(self, responses):
#         """Extract secondary gains and hidden benefits of the pattern"""
#         # Look for responses about what would be lost if pattern changed
#         benefit_keywords = {
#             "safe": "Maintains emotional safety and predictability",
#             "control": "Provides sense of control over outcomes",
#             "protect": "Protects from emotional pain or vulnerability", 
#             "avoid": "Avoids confronting deeper fears or truths",
#             "belonging": "Maintains connection/belonging to family/group",
#             "identity": "Preserves familiar sense of self/identity",
#             "attention": "Ensures attention and care from others",
#             "excuse": "Provides excuse for not taking risks",
#             "blame": "Allows blame of others rather than self-responsibility"
#         }
        
#         text_responses = []
#         for response_data in responses.values():
#             if isinstance(response_data.get('response'), str):
#                 text_responses.append(response_data['response'].lower())
        
#         combined_text = ' '.join(text_responses)
        
#         found_benefits = []
#         for keyword, benefit in benefit_keywords.items():
#             if keyword in combined_text:
#                 found_benefits.append(benefit)
        
#         if found_benefits:
#             return " | ".join(found_benefits[:3])  # Top 3 benefits
#         else:
#             return "Pattern provides emotional protection and familiar identity structure"
    
#     def _extract_systemic_resistance(self, responses, pattern_scores):
#         """Extract family/system resistance to change"""
#         resistance_indicators = {
#             "family": "Family system may resist change to maintain homeostasis",
#             "disappoint": "Fear of disappointing family members or authority figures",
#             "loyalty": "Conflicted loyalty between personal growth and family expectations",
#             "tradition": "Challenge to cultural or generational traditions",
#             "role": "Change threatens established family role or identity",
#             "guilt": "Guilt about changing when others haven't changed",
#             "betrayal": "Fear that personal change represents betrayal of family values"
#         }
        
#         text_responses = []
#         for response_data in responses.values():
#             if isinstance(response_data.get('response'), str):
#                 text_responses.append(response_data['response'].lower())
        
#         combined_text = ' '.join(text_responses)
        
#         for indicator, resistance in resistance_indicators.items():
#             if indicator in combined_text:
#                 return resistance
        
#         # Pattern-based resistance
#         if pattern_scores:
#             dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
#             pattern_resistance = {
#                 7: "Family may resist if client stops over-giving and care-taking",
#                 8: "Strong family pressure to maintain traditional expectations",
#                 2: "Others may escalate conflict when client stops engaging in power struggles",
#                 9: "Certain people may resist client's newfound boundaries and strength"
#             }
#             return pattern_resistance.get(dominant_pattern, "Minimal systemic resistance expected")
        
#         return "Minimal systemic resistance expected"
    
#     def _extract_identity_threat(self, responses, pattern_scores):
#         """Extract identity threats associated with change"""
#         if not pattern_scores:
#             return "Identity shift requires exploration during sessions"
        
#         dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
#         identity_threats = {
#             1: "Fear: 'If I'm happy, I won't be the deep/thoughtful person I am'",
#             2: "Fear: 'If I stop fighting, I'll become weak and people will walk all over me'", 
#             3: "Fear: 'If I trust, I'll become naive and people will take advantage of me'",
#             4: "Fear: 'If I see nuance, I'll lose my moral clarity and convictions'",
#             5: "Fear: 'If I stop doing, I'll become lazy and worthless'",
#             6: "Fear: 'If I'm consistent, I'll be boring and people will lose interest'",
#             7: "Fear: 'If I prioritize myself, I'll become selfish and people will leave'",
#             8: "Fear: 'If I follow my path, I'll lose my family's love and belonging'",
#             9: "Fear: 'If I'm strong everywhere, I'll lose the special care and understanding I get'"
#         }
        
#         return identity_threats.get(dominant_pattern, "Identity evolution requires careful navigation")
    
#     def _extract_intervention_keywords(self, pattern_scores):
#         """Extract keywords that will be effective in hypnotherapy"""
#         if not pattern_scores:
#             return "Collaborative, gentle, permissive"
        
#         dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
#         intervention_keywords = {
#             1: "Permission, gentle, allowing, natural, ease, comfort, safe joy",
#             2: "Collaboration, choice, partnership, respect, empowerment, mutual",
#             3: "Transparency, evidence, clear, step-by-step, gradual, your pace",
#             4: "Integration, both/and, possibilities, options, flexibility, nuance",
#             5: "Being, presence, inherent worth, natural value, simply existing",
#             6: "Authentic, genuine, consistent, true self, unified, wholeness",
#             7: "Balance, strength through self-care, energy, sustainable, healthy boundaries",
#             8: "Personal truth, individual path, respectful autonomy, honoring both",
#             9: "Consistent strength, reliable self, universal power, steady boundaries"
#         }
        
#         return intervention_keywords.get(dominant_pattern, "Adaptive, responsive, individualized")
    
#     def _extract_avoid_language(self, pattern_scores):
#         """Extract language patterns to avoid in therapy"""
#         if not pattern_scores:
#             return "Authoritarian commands, pressure, criticism"
        
#         dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
#         avoid_language = {
#             1: "Forced positivity, 'just be happy', minimizing pain, overwhelming enthusiasm",
#             2: "Commands, authority, 'you must', domination, control, surrender completely",
#             3: "Hidden agendas, unclear processes, 'trust me', unexplained techniques",
#             4: "Either/or choices, black/white thinking, 'you have to choose', extremes",
#             5: "Performance pressure, achievement focus, productivity language, 'earn it'",
#             6: "Role expectations, 'be consistent', contextual shoulds, fitting in",
#             7: "Guilt about self-focus, 'be selfish', minimizing others' needs",
#             8: "Family rejection themes, 'disappointing others', complete rebellion",
#             9: "Universal weakness, 'you're always', situational helplessness"
#         }
        
#         return avoid_language.get(dominant_pattern, "Pressure, criticism, one-size-fits-all approaches")
    
#     def _extract_resistance_points(self, responses, pattern_scores):
#         """Extract predicted resistance points during therapy"""
#         resistance_points = []
        
#         # Check readiness score
#         readiness_responses = [r for r in responses.values() if 'rating' in str(r.get('response', {}))]
#         if readiness_responses:
#             try:
#                 readiness_data = readiness_responses[0]['response']
#                 if isinstance(readiness_data, dict) and readiness_data.get('rating', 0) < 7:
#                     resistance_points.append("Low change readiness - may require motivation building")
#             except:
#                 pass
        
#         # Pattern-specific resistance
#         if pattern_scores:
#             sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
#             for pattern_id, score in sorted_patterns[:2]:
#                 pattern_resistance = {
#                     1: "May resist positive suggestions as 'fake' or temporary",
#                     2: "May challenge therapist authority or collaborative process",
#                     3: "May question therapist motives or seek excessive explanations",
#                     4: "May get stuck in perfectionist analysis of 'right' choice",
#                     5: "May resist 'being' focused work as unproductive",
#                     6: "May present differently in therapy than in assessment",
#                     7: "May prioritize therapist's needs over their own growth",
#                     8: "May feel guilty about changing family dynamics",
#                     9: "May lose boundaries/strength when triggered during session"
#                 }
#                 if pattern_id in pattern_resistance:
#                     resistance_points.append(pattern_resistance[pattern_id])
        
#         # Default resistance points if none found
#         if not resistance_points:
#             resistance_points = [
#                 "Standard change resistance - fear of unknown",
#                 "Possible skepticism about hypnotherapy effectiveness"
#             ]
        
#         return resistance_points[:3]  # Maximum 3 points
    
#     def _generate_session_plan(self, pattern_scores, clinical_insights):
#         """Generate detailed session planning recommendations"""
#         if not pattern_scores:
#             return {
#                 'session_1_focus': "Comprehensive pattern assessment and initial rapport building",
#                 'session_2_target': "Core pattern transformation and positive programming", 
#                 'session_3_need': "Standard reinforcement if needed"
#             }
        
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
#         primary_pattern = sorted_patterns[0][0] if sorted_patterns else 1
        
#         session_plans = {
#             1: {
#                 'session_1_focus': "Unhappiness Culture mapping + permission for joy + gentle positive anchoring",
#                 'session_2_target': "Deep joy permission installation + reframe happiness beliefs + positive emotion anchors",
#                 'session_3_need': "Joy maintenance if relapse into pessimism or guilt about happiness"
#             },
#             2: {
#                 'session_1_focus': "Power struggle pattern analysis + collaboration establishment + shared control",
#                 'session_2_target': "Transform win/lose to win/win mindset + install collaboration reflexes + peace anchors", 
#                 'session_3_need': "Conflict de-escalation if old fighting patterns resurface"
#             },
#             3: {
#                 'session_1_focus': "Trust violation history + safety establishment + graduated vulnerability",
#                 'session_2_target': "Install healthy discernment vs. systematic mistrust + trust capacity building",
#                 'session_3_need': "Trust maintenance if cynicism returns or trust betrayal occurs"
#             },
#             4: {
#                 'session_1_focus': "Binary thinking identification + both/and introduction + cognitive flexibility",
#                 'session_2_target': "Install nuanced thinking + creative option generation + decision confidence",
#                 'session_3_need': "Flexibility maintenance if black/white thinking resurfaces under stress"
#             },
#             5: {
#                 'session_1_focus': "Achievement addiction mapping + inherent worth establishment + being practice",
#                 'session_2_target': "Install worth independence from productivity + being/doing balance + rest permission",
#                 'session_3_need': "Worth maintenance if productivity pressure returns or achievement addiction resurfaces"
#             },
#             6: {
#                 'session_1_focus': "Authentic self identification + consistency across contexts + integration work",
#                 'session_2_target': "Install unified authentic self + consistent expression + context independence",
#                 'session_3_need': "Authenticity maintenance if compartmentalization returns under social pressure"
#             },
#             7: {
#                 'session_1_focus': "Self-sacrifice pattern mapping + self-care as strength reframe + boundary establishment",
#                 'session_2_target': "Install healthy balance + self-care habits + boundary maintenance reflexes",
#                 'session_3_need': "Balance maintenance if caretaking patterns resurface or guilt about self-care"
#             },
#             8: {
#                 'session_1_focus': "Family mission identification + personal desire differentiation + loyalty vs. autonomy",
#                 'session_2_target': "Install personal path confidence + family respect integration + autonomous choice",
#                 'session_3_need': "Autonomy maintenance if family pressure increases or guilt about independence"
#             },
#             9: {
#                 'session_1_focus': "Context-dependent weakness mapping + universal strength identification + boundary work",
#                 'session_2_target': "Install consistent boundaries + context-independent strength + situational confidence",
#                 'session_3_need': "Strength maintenance if old contexts trigger boundary collapse"
#             }
#         }
        
#         return session_plans.get(primary_pattern, session_plans[1])
    
#     def _format_clinical_template(self):
#         """Format comprehensive clinical template for email"""
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
        
#         # Format resistance points
#         resistance_points = clinical_insights.get('resistance_points', [])
#         resistance_text = ""
#         for i, point in enumerate(resistance_points[:3], 1):
#             resistance_text += f"{i}. {point}\n"
#         if not resistance_text:
#             resistance_text = "1. Standard change resistance\n2. Possible skepticism about process\n"
        
#         # Generate behavioral sequence analysis
#         behavioral_sequence = self._generate_behavioral_sequence_analysis()
        
#         # Build comprehensive template
#         template = f"""
# ╔══════════════════════════════════════════════════════════════╗
# ║                    CLINICAL ANALYSIS TEMPLATE                ║
# ║                   Behavioral Pattern Assessment              ║
# ╚══════════════════════════════════════════════════════════════╝

# **PATTERN ANALYSIS:**
# Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
# Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10) 
# Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

# **PSYCHOLOGICAL PROFILE:**
# Core Limiting Belief: {clinical_insights.get('core_limiting_belief', 'Requires session exploration')}
# Hidden Benefits: {clinical_insights.get('hidden_benefits', 'Emotional protection and familiar identity')}
# Systemic Resistance: {clinical_insights.get('systemic_resistance', 'Minimal resistance expected')}
# Identity Threat: {clinical_insights.get('identity_threat', 'Identity evolution requires navigation')}

# **SESSION PLANNING:**
# Session 1 Focus: {session_plan.get('session_1_focus', 'Pattern analysis and rapport building')}
# Session 2 Target: {session_plan.get('session_2_target', 'Core transformation and positive programming')}
# Potential Session 3 Need: {session_plan.get('session_3_need', 'Reinforcement if needed')}

# **THERAPEUTIC APPROACH:**
# Change Readiness Score: {readiness_score}/10
# Predicted Resistance Points:
# {resistance_text}
# Intervention Keywords: {clinical_insights.get('intervention_keywords', 'Collaborative, gentle, permissive')}
# Avoid Language: {clinical_insights.get('avoid_language', 'Pressure, criticism, commands')}

# {behavioral_sequence}

# ╔══════════════════════════════════════════════════════════════╗
# ║                     CLINICAL NOTES                          ║
# ╚══════════════════════════════════════════════════════════════╝

# This comprehensive analysis provides the therapeutic framework for rapid, effective hypnotherapy intervention based on the client's unique behavioral pattern constellation and complete behavioral sequence mapping.
# """
        
#         return template

#     # ---- Analysis Helper Methods ----
#     def _analyze_trigger_type(self, trigger_info):
#         """Analyze the type of trigger"""
#         trigger_lower = trigger_info.lower()
#         if any(word in trigger_lower for word in ['thought', 'worry', 'thinking']):
#             return "Cognitive trigger - internal rumination pattern"
#         elif any(word in trigger_lower for word in ['said', 'person', 'someone']):
#             return "Interpersonal trigger - social activation"
#         elif any(word in trigger_lower for word in ['situation', 'environment', 'place']):
#             return "Environmental trigger - contextual activation"
#         else:
#             return "Mixed trigger - requires clarification"

#     def _analyze_activation_pattern(self, trigger_info):
#         """Analyze activation pattern"""
#         if 'sudden' in trigger_info.lower() or 'immediately' in trigger_info.lower():
#             return "Rapid activation - acute stress response"
#         elif 'gradual' in trigger_info.lower() or 'slowly' in trigger_info.lower():
#             return "Gradual activation - building tension pattern"
#         else:
#             return "Standard activation - typical response timing"

#     def _extract_environmental_factors(self, responses):
#         """Extract environmental factors from responses"""
#         # Look through responses for environmental context
#         for response_data in responses.values():
#             response = response_data.get('response', '')
#             if isinstance(response, str) and any(word in response.lower() for word in ['work', 'home', 'family', 'social']):
#                 return "Context-dependent activation identified"
#         return "Environmental factors require exploration"

#     def _get_response_intensity(self, response_type):
#         """Get intensity rating for specific response type"""
#         intensities = st.session_state.get('intensity_responses', {})
#         # Find intensity for this response type
#         for q_id, intensity in intensities.items():
#             response_data = st.session_state.get('assessment_responses', {}).get(q_id, {})
#             if response_data.get('chain_mapping') == response_type:
#                 return intensity
#         return "Not rated"

#     def _analyze_somatic_location(self, physical_response):
#         """Analyze somatic response location"""
#         response_lower = physical_response.lower()
#         if any(word in response_lower for word in ['chest', 'heart', 'breathing']):
#             return "Cardiac/respiratory system - anxiety/stress activation"
#         elif any(word in response_lower for word in ['stomach', 'nausea', 'digestive']):
#             return "Digestive system - gut-brain connection"
#         elif any(word in response_lower for word in ['muscle', 'tension', 'jaw']):
#             return "Muscular system - fight/flight preparation"
#         else:
#             return "Multi-system activation"

#     def _analyze_activation_system(self, physical_response):
#         """Analyze which system is being activated"""
#         response_lower = physical_response.lower()
#         if any(word in response_lower for word in ['racing', 'fast', 'pounding']):
#             return "Sympathetic nervous system activation"
#         elif any(word in response_lower for word in ['numb', 'disconnect', 'freeze']):
#             return "Dorsal vagal shutdown response"
#         else:
#             return "Mixed autonomic response"

#     def _get_somatic_significance(self, physical_response):
#         """Get clinical significance of somatic response"""
#         return "Primary intervention target - somatic regulation essential"

#     def _analyze_cognitive_distortion(self, thought):
#         """Analyze type of cognitive distortion"""
#         thought_lower = thought.lower()
#         if any(phrase in thought_lower for phrase in ['not good enough', 'inadequate', 'failure']):
#             return "Negative self-evaluation"
#         elif any(phrase in thought_lower for phrase in ['must', 'should', 'have to']):
#             return "Demanding/perfectionist thinking"
#         elif any(phrase in thought_lower for phrase in ['always', 'never', 'everyone']):
#             return "All-or-nothing thinking"
#         else:
#             return "Complex cognitive pattern"

#     def _extract_core_belief_from_thought(self, thought):
#         """Extract core belief indicated by automatic thought"""
#         thought_lower = thought.lower()
#         if 'not good enough' in thought_lower:
#             return "Core inadequacy belief"
#         elif any(word in thought_lower for word in ['danger', 'threat', 'bad']):
#             return "Safety/threat belief system"
#         elif any(word in thought_lower for word in ['reject', 'abandon', 'leave']):
#             return "Attachment/abandonment fears"
#         else:
#             return "Requires deeper exploration"

#     def _get_thought_intervention_target(self, thought):
#         """Get intervention target for thought pattern"""
#         return "Cognitive restructuring with pattern-specific reframes"

#     def _analyze_language_pattern(self, thought):
#         """Analyze language patterns in thought"""
#         thought_lower = thought.lower()
#         if any(word in thought_lower for word in ['must', 'should', 'have to']):
#             return "Demanding language - rigid expectations"
#         elif any(word in thought_lower for word in ['can\'t', 'won\'t', 'impossible']):
#             return "Limitation language - learned helplessness"
#         else:
#             return "Standard self-talk pattern"

#     def _analyze_emotional_constellation(self, emotional_response):
#         """Analyze emotional response constellation"""
#         if isinstance(emotional_response, dict):
#             emotions = list(emotional_response.keys())
#             if len(emotions) > 3:
#                 return "Complex emotional constellation - high activation"
#             elif any('anxious' in emotion.lower() for emotion in emotions):
#                 return "Anxiety-centered constellation"
#             elif any('angry' in emotion.lower() for emotion in emotions):
#                 return "Anger-centered constellation"
#             else:
#                 return "Mixed emotional activation"
#         else:
#             return "Single emotion focus"

#     def _assess_regulation_capacity(self, emotional_response):
#         """Assess emotional regulation capacity"""
#         if isinstance(emotional_response, dict):
#             high_intensity = [emotion for emotion, intensity in emotional_response.items() if intensity >= 6]
#             if len(high_intensity) >= 2:
#                 return "Low regulation capacity - overwhelm pattern"
#             else:
#                 return "Moderate regulation capacity"
#         else:
#             return "Regulation capacity requires assessment"

#     def _get_emotional_intervention(self, emotional_response):
#         """Get emotional intervention approach"""
#         return "Emotional regulation training with somatic anchoring"

#     def _analyze_behavioral_pattern(self, behavioral_response):
#         """Analyze behavioral response pattern"""
#         response_lower = behavioral_response.lower()
#         if any(word in response_lower for word in ['avoid', 'withdraw', 'escape']):
#             return "Avoidance pattern - flight response"
#         elif any(word in response_lower for word in ['busy', 'active', 'do']):
#             return "Hyperactivity pattern - doing addiction"
#         elif any(word in response_lower for word in ['argue', 'fight', 'defend']):
#             return "Confrontation pattern - fight response"
#         else:
#             return "Complex behavioral response"

#     def _analyze_behavioral_function(self, behavioral_response):
#         """Analyze function of behavioral response"""
#         response_lower = behavioral_response.lower()
#         if 'avoid' in response_lower:
#             return "Emotional avoidance and safety-seeking"
#         elif any(word in response_lower for word in ['busy', 'productive']):
#             return "Distraction and control-seeking"
#         else:
#             return "Multiple functions - requires exploration"

#     def _assess_pattern_alignment(self, behavioral_response):
#         """Assess how behavior aligns with dominant patterns"""
#         pattern_scores = st.session_state.get('pattern_scores', {})
#         if not pattern_scores:
#             return "Pattern alignment requires completion"
        
#         dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
#         response_lower = behavioral_response.lower()
        
#         alignments = {
#             1: ['avoid', 'withdraw', 'pessimistic'],
#             2: ['argue', 'fight', 'control'],
#             3: ['suspicious', 'test', 'withdraw'],
#             4: ['paralyzed', 'either', 'stuck'],
#             5: ['busy', 'productive', 'work'],
#             6: ['different', 'adapt', 'change'],
#             7: ['others', 'help', 'sacrifice'],
#             8: ['should', 'family', 'expect'],
#             9: ['weak', 'powerless', 'context']
#         }
        
#         pattern_keywords = alignments.get(dominant_pattern, [])
#         if any(keyword in response_lower for keyword in pattern_keywords):
#             return f"Strong alignment with Pattern {dominant_pattern}"
#         else:
#             return "Partial pattern alignment"

#     def _get_behavioral_intervention_point(self, behavioral_response):
#         """Get behavioral intervention point"""
#         return "Response substitution with healthier alternatives"

#     def _analyze_consequence_type(self, consequence):
#         """Analyze type of consequence"""
#         consequence_lower = consequence.lower()
#         if any(word in consequence_lower for word in ['worse', 'agitated', 'escalate']):
#             return "Escalating consequence - pattern amplification"
#         elif any(word in consequence_lower for word in ['relief', 'better', 'calm']):
#             return "Reinforcing consequence - pattern maintenance"
#         else:
#             return "Mixed consequence pattern"

#     def _analyze_reinforcement_pattern(self, consequence):
#         """Analyze reinforcement pattern"""
#         consequence_lower = consequence.lower()
#         if 'temporary' in consequence_lower and 'relief' in consequence_lower:
#             return "Intermittent reinforcement - strong pattern maintenance"
#         elif any(word in consequence_lower for word in ['worse', 'agitated']):
#             return "Negative reinforcement - pattern should extinguish but may be maintained by other factors"
#         else:
#             return "Complex reinforcement - requires analysis"

#     def _get_consequence_intervention_timing(self, consequence):
#         """Get intervention timing for consequences"""
#         return "Immediate post-response intervention with pattern interruption"

#     def _analyze_pattern_reinforcement(self, longer_impact):
#         """Analyze how longer-term impact reinforces pattern"""
#         impact_lower = longer_impact.lower()
#         if any(word in impact_lower for word in ['replay', 'ruminate', 'think']):
#             return "Cognitive reinforcement through rumination"
#         elif any(word in impact_lower for word in ['avoid', 'prevent', 'plan']):
#             return "Behavioral reinforcement through preparation"
#         else:
#             return "Multi-modal reinforcement pattern"

#     def _assess_cycle_completion(self, longer_impact):
#         """Assess if the cycle completes back to trigger"""
#         impact_lower = longer_impact.lower()
#         if any(word in impact_lower for word in ['ready', 'next', 'again']):
#             return "Complete cycle - primes for re-activation"
#         else:
#             return "Incomplete cycle data"

#     def _identify_breaking_points(self, longer_impact):
#         """Identify potential breaking points in cycle"""
#         return "Multiple intervention windows identified"

#     def _calculate_chain_completeness(self):
#         """Calculate what percentage of the chain is complete"""
#         trigger_chain = st.session_state.get('trigger_chain', {})
#         total_components = 6  # trigger, physical, thought, emotion, behavior, consequence
        
#         completed_components = 0
#         for component in ['awareness_point', 'physical_response', 'automatic_thought', 'emotional_response', 'behavioral_response', 'immediate_consequence']:
#             if trigger_chain.get(component) and trigger_chain.get(component) != 'Not captured' and trigger_chain.get(component) != 'Skipped':
#                 completed_components += 1
        
#         return int((completed_components / total_components) * 100)

#     def _identify_missing_components(self):
#         """Identify missing components in the behavioral chain"""
#         trigger_chain = st.session_state.get('trigger_chain', {})
#         missing = []
        
#         components = {
#             'awareness_point': 'Trigger identification and specificity',
#             'automatic_thought': 'Specific thought content during activation',
#             'emotional_response': 'Complete emotional sequence and intensity',
#             'behavioral_response': 'Exact behavioral response pattern',
#             'immediate_consequence': 'Immediate aftermath and reinforcement',
#             'longer_term_impact': 'Pattern completion and cycle reinforcement'
#         }
        
#         for component, description in components.items():
#             value = trigger_chain.get(component)
#             if not value or value == 'Not captured' or value == 'Skipped':
#                 missing.append(description)
        
#         return missing


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

# def reset_assessment():
#     """Reset assessment state"""
#     keys_to_reset = [
#         'assessment_responses', 'current_question', 'current_phase', 'phase_progress',
#         'triggered_patterns', 'pattern_scores', 'risk_flags', 'assessment_completed', 
#         'contact_provided', 'assessment_results', 'intensity_responses', 'motivation_data',
#         'trigger_chain', 'response_chain', 'adaptive_paths'
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
#         'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
#         'adaptive_paths': st.session_state.get('adaptive_paths', []),
#         'risk_flags': st.session_state.get('risk_flags', []),
#         'trigger_chain': st.session_state.get('trigger_chain', {}),
#         'phase_progress': st.session_state.get('phase_progress', {}),
#         'results': st.session_state.get('assessment_results', {}),
#         'contact_info': st.session_state.get('contact_info', {}),
#         'completion_timestamp': datetime.now().isoformat()
#     }

# def get_behavioral_chain():
#     """Get the complete behavioral chain mapping"""
#     if 'trigger_chain' not in st.session_state:
#         return None
    
#     return {
#         'trigger_sequence': st.session_state.get('trigger_chain', {}),
#         'pattern_activations': st.session_state.get('pattern_scores', {}),
#         'intensity_levels': st.session_state.get('intensity_responses', {}),
#         'response_patterns': {
#             'dominant_pattern': st.session_state.get('assessment_results', {}).get('dominant_pattern'),
#             'secondary_patterns': list(st.session_state.get('triggered_patterns', set()))
#         }
#     }

# def get_hypnotherapy_recommendations():
#     """Generate hypnotherapy recommendations based on assessment"""
#     if 'pattern_scores' not in st.session_state or not st.session_state.pattern_scores:
#         return None
    
#     dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
    
#     recommendations = {
#         1: {
#             "approach": "Permission-based, gentle positive installation",
#             "language": "Collaborative, non-directive, allowing language",
#             "avoid": "Overwhelming positivity, forced happiness",
#             "induction": "Progressive relaxation with permission phrases"
#         },
#         2: {
#             "approach": "Collaborative empowerment, shared control",
#             "language": "Partnership language, choice-focused",
#             "avoid": "Authoritarian commands, directive language",
#             "induction": "Self-guided with therapist facilitation"
#         },
#         3: {
#             "approach": "Trust-building, transparent process",
#             "language": "Clear explanations, evidence-based",
#             "avoid": "Hidden agendas, unexplained techniques",
#             "induction": "Fully explained, client-controlled depth"
#         },
#         4: {
#             "approach": "Integration therapy, both/and thinking",
#             "language": "Possibility expansion, option creation",
#             "avoid": "Either/or choices, black-and-white language",
#             "induction": "Creative visualization with multiple pathways"
#         },
#         5: {
#             "approach": "Being-centered work, inherent worth",
#             "language": "Presence-focused, non-performance based",
#             "avoid": "Achievement language, productivity focus",
#             "induction": "Mindfulness-based, present-moment awareness"
#         },
#         6: {
#             "approach": "Authentic self integration",
#             "language": "Consistency across contexts, authentic expression",
#             "avoid": "Role-based language, contextual expectations",
#             "induction": "Core self connection, identity integration"
#         },
#         7: {
#             "approach": "Self-care strength reframing",
#             "language": "Balanced care, strength through self-care",
#             "avoid": "Guilt-inducing self-focus language",
#             "induction": "Nurturing self-care as service to others"
#         },
#         8: {
#             "approach": "Personal desire differentiation",
#             "language": "Individual path honoring, respectful autonomy",
#             "avoid": "Family rejection themes, complete rebellion",
#             "induction": "Personal truth with family love integration"
#         },
#         9: {
#             "approach": "Context-independent strength building",
#             "language": "Consistent boundary language, universal strength",
#             "avoid": "Situational weakness reinforcement",
#             "induction": "Anchor strong self across all contexts"
#         }
#     }
    
#     return recommendations.get(dominant_pattern, {
#         "approach": "Individualized based on assessment findings",
#         "language": "Supportive, adaptive to client needs",
#         "avoid": "Generic approaches without personalization",
#         "induction": "Tailored to client's response patterns"
#     })


# # # ---- Main Execution ----
# # if __name__ == "__main__":
# #     st.set_page_config(
# #         page_title="Behavioral Pattern Assessment",
# #         page_icon="🧠",
# #         layout="centered",
# #         initial_sidebar_state="collapsed"
# #     )
    
# #     assessment_page = create_assess_page()
# #     assessment_page.render()













# Complete Enhanced Clinical Behavioral Pattern Assessment
# Integrated with Digital Despair Syndrome screening and analysis
# Comprehensive implementation with adaptive questioning and pattern detection
# Optimized for both traditional and digital-native populations

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
    .digital-indicator {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        font-size: 0.85rem;
        text-align: center;
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
    """Clinical-grade behavioral pattern assessment with Digital Despair Syndrome integration"""
    
    def __init__(self):
        self._init_session_state()
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        self.patterns = {
            1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
            4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
            7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
        }
        
        # Question pools organized by integrated phase system
        self.age_screening_questions = self._get_age_screening_questions()
        self.digital_screening_questions = self._get_digital_screening_questions()
        self.engagement_questions = self._get_engagement_questions()
        self.trigger_mapping_questions = self._get_trigger_mapping_questions()
        self.pattern_specific_questions = self._get_pattern_specific_questions()
        self.integration_questions = self._get_integration_questions()

    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'current_phase': 'age_screening',
            'phase_progress': {
                'age_screening': 0, 'digital_screening': 0, 'engagement': 0, 
                'trigger_mapping': 0, 'pattern_specific': 0, 'integration': 0
            },
            'is_digital_native': False,
            'digital_despair_score': 0,
            'digital_severity': 'MINIMAL',
            'triggered_patterns': set(),
            'pattern_scores': {},
            'risk_flags': [],
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'start_time': datetime.now().isoformat(),
            'intensity_responses': {},
            'trigger_chain': {},
            'digital_responses': {},
            'adaptive_paths': []
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _get_age_screening_questions(self):
        """Phase 0: Age Screening for Digital Native Assessment"""
        return {
            0: {
                "text": "What is your age range?",
                "type": "single_choice",
                "options": [
                    "Under 18", "18-22", "23-27", "28-32", 
                    "33-37", "38-42", "43-50", "Over 50"
                ],
                "digital_native_scoring": [3, 5, 4, 3, 2, 1, 0, 0],
                "phase": "age_screening",
                "determines_flow": True
            }
        }

    def _get_digital_screening_questions(self):
        """Phase 1: Digital Despair Syndrome Screening (for digital natives)"""
        return {
            1: {
                "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
                "type": "single_choice",
                "options": [
                    "Less than 2 hours", "2-4 hours", "4-6 hours",
                    "6-8 hours", "8-10 hours", "Over 10 hours"
                ],
                "digital_despair_weights": [0, 1, 2, 3, 4, 5],
                "phase": "digital_screening"
            },
            2: {
                "text": "Where do you feel most like your authentic self?",
                "type": "single_choice_with_intensity",
                "options": [
                    "In offline, face-to-face interactions",
                    "In online communities and digital spaces", 
                    "Both online and offline equally",
                    "Neither - I don't feel authentic anywhere",
                    "It varies completely depending on the situation"
                ],
                "digital_despair_indicators": {
                    1: 3,  # Strong offline dissociation indicator
                    3: 2,  # Identity fragmentation 
                    4: 4   # Complete authenticity loss
                },
                "phase": "digital_screening"
            },
            3: {
                "text": "When you imagine a successful life, you typically think:",
                "type": "single_choice",
                "options": [
                    "Meaningful relationships and personal fulfillment",
                    "Extraordinary wealth, fame, or achievement",
                    "Being significantly better than most people at something",
                    "Just being happy and content with normal life",
                    "Success feels impossible or meaningless to me"
                ],
                "digital_despair_patterns": {
                    1: 4,  # Extraordinary achievement pressure
                    2: 3,  # Comparative inadequacy 
                    4: 4   # Nihilistic worldview
                },
                "phase": "digital_screening"
            },
            4: {
                "text": "When expressing genuine emotions or enthusiasm:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I express them naturally and directly",
                    "I tend to use humor or irony to deflect",
                    "I feel embarrassed or 'cringe' about sincerity",
                    "I mainly express emotions through memes or online references",
                    "I rarely express genuine emotions at all"
                ],
                "ironic_detachment_scoring": [0, 2, 3, 3, 4],
                "phase": "digital_screening"
            },
            5: {
                "text": "What primarily influences your daily emotional state?",
                "type": "single_choice",
                "options": [
                    "Interactions with family and friends in person",
                    "Social media feeds and online content",
                    "Work or school experiences", 
                    "Internal thoughts and self-reflection",
                    "Online communities and digital relationships"
                ],
                "algorithmic_dependency": {
                    1: 3,  # Social media primary
                    4: 3   # Digital relationships primary
                },
                "phase": "digital_screening"
            },
            6: {
                "text": "You feel more emotionally connected to:",
                "type": "single_choice",
                "options": [
                    "People in your physical daily life",
                    "Online personalities (streamers, influencers, content creators)",
                    "Online friends and communities",
                    "Fictional characters or media personalities",
                    "No significant emotional connections anywhere"
                ],
                "parasocial_indicators": {
                    1: 2,  # Online personalities
                    2: 2,  # Online communities over offline
                    3: 3,  # Fictional over real
                    4: 4   # Complete disconnection
                },
                "phase": "digital_screening"
            },
            7: {
                "text": "When someone suggests things could get better or offers optimistic perspectives:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I feel encouraged and want to believe them",
                    "I appreciate it but remain cautiously skeptical", 
                    "I immediately think of reasons why they're wrong",
                    "I feel annoyed because they don't understand reality",
                    "I dismiss it as naive or manipulative"
                ],
                "hope_avoidance_indicators": {
                    2: 2,  # Automatic negativity
                    3: 3,  # Irritated by optimism
                    4: 4   # Complete hope dismissal
                },
                "phase": "digital_screening"
            },
            8: {
                "text": "Your attention span for non-digital activities (reading books, conversations, offline tasks):",
                "type": "single_choice",
                "options": [
                    "Same as always - can focus for hours when interested",
                    "Slightly shorter but manageable",
                    "Noticeably fragmented - need frequent stimulation",
                    "Very difficult - mind wanders constantly",
                    "Almost impossible without background digital stimulation"
                ],
                "attention_fragmentation": [0, 1, 2, 3, 4],
                "phase": "digital_screening"
            }
        }

    def _get_engagement_questions(self):
        """Phase 2: Engagement & Initial Pattern Detection"""
        return {
            9: {
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
            10: {
                "text": "If this issue completely resolved, what would be different about your daily life?",
                "type": "text_completion",
                "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
                "min_chars": 20,
                "pattern_analysis": True,
                "keywords": {
                    "productivity": [5], "relationships": [2, 3, 6, 7], "peace": [1], 
                    "authentic": [6], "happy": [1], "control": [2, 4], "boundaries": [7, 9]
                },
                "phase": "engagement"
            },
            11: {
                "text": "How ready are you to completely let go of this pattern?",
                "type": "scale_10",
                "labels": ["Not ready at all", "Completely ready"],
                "follow_up_trigger": 7,  # If 7 or below, ask follow-up
                "phase": "engagement"
            },
            12: {
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
            13: {
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
        """Phase 3: Core Trigger Mapping"""
        return {
            14: {
                "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
                "type": "text_completion",
                "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
                "min_chars": 20,
                "trigger_analysis": True,
                "phase": "trigger_mapping"
            },
            15: {
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
            16: {
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
            17: {
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
            18: {
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
            19: {
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
            20: {
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
            21: {
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
        """Phase 4: Adaptive Pattern-Specific Deep Dives"""
        return {
            # Pattern 1: Unhappiness Culture
            "pattern_1": {
                22: {
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
                23: {
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
                24: {
                    "text": "What would you lose if you allowed yourself to be genuinely happy?",
                    "type": "text_completion",
                    "placeholder": "Think about identity, relationships, what others might think, or what might change...",
                    "min_chars": 15,
                    "pattern": 1
                }
            },
            
            # Pattern 2: Power Struggles
            "pattern_2": {
                25: {
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
                26: {
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
                }
            },
            
            # Pattern 3: Systematic Mistrust
            "pattern_3": {
                27: {
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
                28: {
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
                }
            },
            
            # Pattern 4: Separation/Division
            "pattern_4": {
                29: {
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
                }
            },
            
            # Pattern 5: Doing vs Being
            "pattern_5": {
                30: {
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
                }
            },
            
            # Pattern 6: Compartmentalized Authenticity
            "pattern_6": {
                31: {
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
                }
            },
            
            # Pattern 8: Inherited Missions
            "pattern_8": {
                33: {
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
                }
            },
            
            # Pattern 9: Context-Dependent Weakness
            "pattern_9": {
                34: {
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
                }
            }
        }

    def _get_integration_questions(self):
        """Phase 5: Integration & Change Readiness"""
        return {
            35: {
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
            36: {
                "text": "What would need to be true for you to feel completely safe changing this pattern?",
                "type": "text_completion",
                "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
                "min_chars": 15,
                "safety_assessment": True,
                "phase": "integration"
            },
            37: {
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
            38: {
                "text": "Imagine you've completely transformed this pattern. What's the first thing you'd do that you can't do now?",
                "type": "text_completion",
                "placeholder": "Be specific about the first action, conversation, or decision you'd make...",
                "min_chars": 15,
                "outcome_visualization": True,
                "phase": "integration"
            }
        }

    # ---- Digital Despair Analysis Methods ----
    def _analyze_digital_despair_indicators(self, responses):
        """Analyze responses for Digital Despair Syndrome indicators"""
        
        # Age factor (digital native status)
        age_response = responses.get(0, {}).get('response', '')
        digital_native_score = 0
        
        age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
        scoring = [3, 5, 4, 3, 2, 1, 0, 0]
        
        try:
            age_index = age_options.index(age_response)
            digital_native_score = scoring[age_index]
        except (ValueError, IndexError):
            digital_native_score = 0
        
        # Determine if digital native assessment was triggered
        if digital_native_score < 2:
            return None  # Skip digital despair analysis for non-digital natives
        
        # Extract component scores
        reality_dissociation = self._extract_reality_dissociation_score(responses)
        binary_thinking = self._extract_binary_success_score(responses) 
        ironic_detachment = self._extract_ironic_detachment_score(responses)
        algorithmic_dependency = self._extract_algorithmic_dependency_score(responses)
        nihilistic_worldview = self._extract_nihilistic_worldview_score(responses)
        hope_avoidance = self._extract_hope_avoidance_score(responses)
        attention_fragmentation = self._extract_attention_fragmentation_score(responses)
        
        # Calculate composite Digital Despair Score
        total_possible = 35  # Maximum possible score across all indicators
        raw_score = (digital_native_score + reality_dissociation + binary_thinking + 
                     ironic_detachment + algorithmic_dependency + nihilistic_worldview + 
                     hope_avoidance + attention_fragmentation)
        
        digital_despair_percentage = (raw_score / total_possible) * 100
        
        # Severity classification
        if digital_despair_percentage >= 70:
            severity = "SEVERE"
            recommendation = "Specialized digital-native intervention required"
        elif digital_despair_percentage >= 50:
            severity = "MODERATE" 
            recommendation = "Modified approach with digital awareness"
        elif digital_despair_percentage >= 30:
            severity = "MILD"
            recommendation = "Standard approach with digital considerations"
        else:
            severity = "MINIMAL"
            recommendation = "Traditional hypnotherapy approach suitable"
        
        return {
            'digital_despair_score': digital_despair_percentage,
            'severity_level': severity,
            'clinical_recommendation': recommendation,
            'component_scores': {
                'digital_native_status': digital_native_score,
                'reality_dissociation': reality_dissociation,
                'binary_success_pressure': binary_thinking,
                'ironic_detachment': ironic_detachment, 
                'algorithmic_dependency': algorithmic_dependency,
                'nihilistic_worldview': nihilistic_worldview,
                'hope_avoidance': hope_avoidance,
                'attention_fragmentation': attention_fragmentation
            },
            'therapeutic_adaptations_needed': self._get_therapeutic_adaptations(severity)
        }

    def _get_therapeutic_adaptations(self, severity):
        """Get required therapeutic adaptations based on Digital Despair severity"""
        
        adaptations = {
            "SEVERE": [
                "Attention span optimization: 15-30 minute focused segments",
                "Anti-authority language: Collaborative, non-directive approach",
                "Ironic armor dissolution: Validate intelligence while accessing authentic emotion",
                "Digital bridge-building: Connect online competencies to offline confidence",
                "Binary thinking interruption: Install 'both/and' processing patterns",
                "Hope introduction protocol: Gradual realistic optimism vs. overwhelming positivity",
                "Meaning-making assistance: Personal contribution vs. extraordinary achievement"
            ],
            "MODERATE": [
                "Modified session length: 45-60 minutes with movement breaks",
                "Authority resistance awareness: Reduce directive language", 
                "Cynicism validation: Acknowledge systemic problems while building agency",
                "Digital competency honor: Validate online achievements and skills",
                "Nuanced goal-setting: Meaningful vs. extraordinary success redefinition",
                "Gradual hope building: Evidence-based optimism introduction"
            ],
            "MILD": [
                "Digital literacy integration: Use familiar cultural references",
                "Achievement pressure awareness: Expand success definitions",
                "Authentic expression permission: Reduce 'cringe' about sincerity",
                "Real-world confidence transfer: Apply online skills offline"
            ],
            "MINIMAL": [
                "Standard approach with generational awareness",
                "Technology balance considerations",
                "Modern stress factor acknowledgment"
            ]
        }
        
        return adaptations.get(severity, adaptations["MINIMAL"])

    # Helper functions for extracting specific scores
    def _extract_reality_dissociation_score(self, responses):
        """Extract reality dissociation indicators from responses"""
        score = 0
        
        # Digital vs offline authenticity (question 2)
        digital_auth_data = responses.get(2, {})
        digital_auth = digital_auth_data.get('response', '')
        
        if 'online communities and digital spaces' in digital_auth:
            score += 3
        elif 'don\'t feel authentic anywhere' in digital_auth:
            score += 4
        elif 'varies completely depending' in digital_auth:
            score += 2
            
        # Add intensity multiplier if available
        intensity = digital_auth_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)  # Scale intensity 1-7 to multiplier
        
        return min(5, score)  # Cap at 5 points for this component

    def _extract_binary_success_score(self, responses):
        """Extract binary success framework indicators"""
        score = 0
        
        success_def = responses.get(3, {}).get('response', '')
        if 'Extraordinary wealth, fame, or achievement' in success_def:
            score += 4
        elif 'Success feels impossible or meaningless' in success_def:
            score += 4
        elif 'significantly better than most people' in success_def:
            score += 3
            
        return min(5, score)

    def _extract_ironic_detachment_score(self, responses):
        """Extract ironic detachment indicators"""
        score = 0
        
        emotion_expr_data = responses.get(4, {})
        emotion_expr = emotion_expr_data.get('response', '')
        
        if 'embarrassed or \'cringe\' about sincerity' in emotion_expr:
            score += 3
        elif 'through memes or online references' in emotion_expr:
            score += 3
        elif 'rarely express genuine emotions' in emotion_expr:
            score += 4
        elif 'humor or irony to deflect' in emotion_expr:
            score += 2
        
        # Apply intensity multiplier
        intensity = emotion_expr_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)
        
        return min(5, score)

    def _extract_algorithmic_dependency_score(self, responses):
        """Extract algorithmic emotional regulation indicators"""
        score = 0
        
        emotion_source = responses.get(5, {}).get('response', '')
        if 'Social media feeds and online content' in emotion_source:
            score += 3
        elif 'Online communities and digital relationships' in emotion_source:
            score += 3
            
        relationship_invest = responses.get(6, {}).get('response', '')
        if 'Online personalities' in relationship_invest:
            score += 2
        elif 'Online friends and communities' in relationship_invest:
            score += 2
        elif 'Fictional characters' in relationship_invest:
            score += 3
            
        return min(5, score)

    def _extract_nihilistic_worldview_score(self, responses):
        """Extract nihilistic worldview indicators"""  
        score = 0
        
        # Check success definition for nihilism
        success_def = responses.get(3, {}).get('response', '')
        if 'Success feels impossible or meaningless' in success_def:
            score += 4
            
        return min(5, score)

    def _extract_hope_avoidance_score(self, responses):
        """Extract hope avoidance indicators"""
        score = 0
        
        hope_relation_data = responses.get(7, {})
        hope_relation = hope_relation_data.get('response', '')
        
        if 'dismiss it as naive or manipulative' in hope_relation:
            score += 4
        elif 'annoyed because they don\'t understand reality' in hope_relation:
            score += 3  
        elif 'think of reasons why they\'re wrong' in hope_relation:
            score += 2
        
        # Apply intensity multiplier
        intensity = hope_relation_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)
        
        return min(5, score)

    def _extract_attention_fragmentation_score(self, responses):
        """Extract attention fragmentation indicators"""
        score = 0
        
        focus_capacity = responses.get(8, {}).get('response', '')
        focus_options = [
            "Same as always - can focus for hours when interested",
            "Slightly shorter but manageable", 
            "Noticeably fragmented - need frequent stimulation",
            "Very difficult - mind wanders constantly",
            "Almost impossible without background digital stimulation"
        ]
        scoring = [0, 1, 2, 3, 4]
        
        try:
            focus_index = focus_options.index(focus_capacity)
            score = scoring[focus_index]
        except (ValueError, IndexError):
            score = 0
        
        return min(5, score)

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
        
        # Store digital responses separately
        if question.get('phase') == 'digital_screening':
            st.session_state.digital_responses[q_id] = response
        
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
        
        # Phase 0: Age Screening (Question 0)
        if st.session_state.current_phase == 'age_screening':
            if 0 not in answered:
                return 0, self.age_screening_questions[0]
            else:
                # Determine if digital native
                age_response = st.session_state.assessment_responses.get(0, {}).get('response', '')
                age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
                scoring = [3, 5, 4, 3, 2, 1, 0, 0]
                
                try:
                    age_index = age_options.index(age_response)
                    digital_native_score = scoring[age_index]
                    st.session_state.is_digital_native = digital_native_score >= 2
                except (ValueError, IndexError):
                    st.session_state.is_digital_native = False
                
                # Move to appropriate next phase
                if st.session_state.is_digital_native:
                    st.session_state.current_phase = 'digital_screening'
                else:
                    st.session_state.current_phase = 'engagement'
        
        # Phase 1: Digital Screening (Questions 1-8) - Only for digital natives
        if st.session_state.current_phase == 'digital_screening':
            for q_id in range(1, 9):
                if q_id not in answered:
                    return q_id, self.digital_screening_questions[q_id]
            st.session_state.current_phase = 'engagement'
        
        # Phase 2: Engagement (Questions 9-13)
        if st.session_state.current_phase == 'engagement':
            for q_id in range(9, 14):
                if q_id not in answered:
                    return q_id, self.engagement_questions[q_id]
            st.session_state.current_phase = 'trigger_mapping'
        
        # Phase 3: Trigger Mapping (Questions 14-21)
        if st.session_state.current_phase == 'trigger_mapping':
            for q_id in range(14, 22):
                if q_id not in answered:
                    return q_id, self.trigger_mapping_questions[q_id]
            st.session_state.current_phase = 'pattern_specific'
        
        # Phase 4: Pattern-Specific Questions
        if st.session_state.current_phase == 'pattern_specific':
            for pattern_id in st.session_state.triggered_patterns:
                pattern_key = f"pattern_{pattern_id}"
                if pattern_key in self.pattern_specific_questions:
                    pattern_questions = self.pattern_specific_questions[pattern_key]
                    for q_id, question in pattern_questions.items():
                        if q_id not in answered:
                            return q_id, question
            st.session_state.current_phase = 'integration'
        
        # Phase 5: Integration (Questions 35-38)
        if st.session_state.current_phase == 'integration':
            for q_id in range(35, 39):
                if q_id not in answered:
                    return q_id, self.integration_questions[q_id]
        
        return None, None

    def _estimate_total_questions(self):
        """Estimate total questions based on triggered patterns and digital native status"""
        base_questions = 1  # age screening
        
        if st.session_state.is_digital_native:
            base_questions += 8  # digital screening
        
        base_questions += 5 + 8 + 4  # engagement + trigger_mapping + integration
        pattern_questions = len(st.session_state.triggered_patterns) * 2  # avg 2 questions per pattern
        return base_questions + pattern_questions

    def _estimate_time_remaining(self):
        """Estimate remaining time"""
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        
        # Adjust time estimate based on digital native status
        if st.session_state.is_digital_native and st.session_state.digital_severity == 'SEVERE':
            return remaining * 0.8  # Faster pacing for digital natives
        else:
            return remaining * 1.0

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
        follow_up = ""
        if value <= question.get('follow_up_trigger', 5):
            follow_up = st.text_input(
                "What would need to happen to make it a 10?",
                key=f"q_{q_id}_followup",
                placeholder="What would increase your readiness?"
            )
        
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
        
        # Analyze digital despair if digital native
        digital_analysis = None
        if st.session_state.is_digital_native:
            digital_analysis = self._analyze_digital_despair_indicators(st.session_state.assessment_responses)
            if digital_analysis:
                st.session_state.digital_despair_score = digital_analysis['digital_despair_score']
                st.session_state.digital_severity = digital_analysis['severity_level']
        
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
            'is_digital_native': st.session_state.is_digital_native,
            'digital_despair_analysis': digital_analysis,
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
            
            # Show digital native indicator if applicable
            if st.session_state.is_digital_native and st.session_state.current_phase != 'age_screening':
                st.markdown("""
                <div class="digital-indicator">
                🖥️ Digital-native assessment active - specialized approach enabled
                </div>
                """, unsafe_allow_html=True)
            
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

        # Phase indicator
        current_phase = question.get('phase', 'unknown')
        phase_names = {
            'age_screening': 'Initial Screening',
            'digital_screening': 'Digital Pattern Assessment',
            'engagement': 'Pattern Discovery',
            'trigger_mapping': 'Trigger Analysis',
            'pattern_specific': 'Deep Pattern Exploration',
            'integration': 'Integration & Planning'
        }
        phase_display = phase_names.get(current_phase, current_phase.title())
        
        if current_phase != 'age_screening':
            st.caption(f"**Phase:** {phase_display}")

        # Question display
        st.markdown(f"### {question['text']}")
        
        # Show pattern detection hints for engaged users
        if completed > 8 and st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
            if top_pattern[1] >= 2.0:
                pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
                # Only show hints in later phases to avoid influencing responses

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
            # Only allow skipping after age screening
            if current_q_id > 0:
                if st.button("Skip", key="nav_skip", use_container_width=True):
                    skip_question = {"text": "Skipped", "type": "skip", "phase": "skip"}
                    self._save_response(current_q_id, "Skipped", skip_question)
                    self._advance_question()
                    st.rerun()

    def _render_contact_form(self):
        """Render contact form for results with enhanced clinical data"""
        st.markdown("### Assessment complete!")
        st.success("Your comprehensive behavioral pattern analysis is ready!")
        
        results = st.session_state.assessment_results
        
        # Show different metrics based on assessment type
        if st.session_state.is_digital_native:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Questions", results['total_questions_answered'], "Answered")
            with col2:
                st.metric("Patterns", len(results.get('pattern_scores', {})), "Detected")
            with col3:
                digital_score = st.session_state.get('digital_despair_score', 0)
                st.metric("Digital Score", f"{digital_score:.0f}%", st.session_state.get('digital_severity', 'MINIMAL'))
            with col4:
                completion_rate = results.get('completion_rate', 1.0)
                st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")
        else:
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
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
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
                    
                    # GENERATE COMPREHENSIVE CLINICAL TEMPLATE
                    clinical_template = self._format_comprehensive_clinical_template()
                    
                    # Prepare assessment data for email with enhanced clinical template
                    assessment_data = {
                        'contact_info': st.session_state.contact_info,
                        'assessment_results': st.session_state.assessment_results,
                        'assessment_responses': st.session_state.assessment_responses,
                        'intensity_responses': st.session_state.intensity_responses,
                        'adaptive_triggered': st.session_state.adaptive_paths,
                        'risk_flags': st.session_state.risk_flags,
                        'pattern_scores': st.session_state.pattern_scores,
                        'trigger_chain': st.session_state.trigger_chain,
                        'digital_responses': st.session_state.digital_responses,
                        'is_digital_native': st.session_state.is_digital_native,
                        'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis'),
                        'clinical_template': clinical_template,
                        'start_time': st.session_state.start_time,
                        'completion_timestamp': datetime.now().isoformat()
                    }
                    
                    # Send comprehensive clinical assessment email
                    try:
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

    def _format_comprehensive_clinical_template(self):
        """Format comprehensive clinical template integrating traditional patterns + digital analysis"""
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
        
        # Generate behavioral sequence analysis
        behavioral_sequence = self._generate_behavioral_sequence_analysis()
        
        # Build base template
        template = f"""
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║          Enhanced Behavioral Pattern Assessment              ║
╚══════════════════════════════════════════════════════════════╝

**TRADITIONAL PATTERN ANALYSIS:**
Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10) 
Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: {clinical_insights.get('core_limiting_belief', 'Requires session exploration')}
Hidden Benefits: {clinical_insights.get('hidden_benefits', 'Emotional protection and familiar identity')}
Systemic Resistance: {clinical_insights.get('systemic_resistance', 'Minimal resistance expected')}
Identity Threat: {clinical_insights.get('identity_threat', 'Identity evolution requires navigation')}

**CHANGE READINESS:**
Readiness Score: {readiness_score}/10
Motivation Level: {"HIGH" if readiness_score >= 8 else "MODERATE" if readiness_score >= 6 else "REQUIRES BUILDING"}
"""
        
        # Add digital despair analysis if applicable
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                digital_score = digital_analysis['digital_despair_score']
                severity = digital_analysis['severity_level']
                
                template += f"""

╔══════════════════════════════════════════════════════════════╗
║               DIGITAL DESPAIR SYNDROME ANALYSIS             ║
╚══════════════════════════════════════════════════════════════╝

**SYNDROME ASSESSMENT:**
Digital Despair Score: {digital_score:.1f}% ({severity} severity)
Clinical Recommendation: {digital_analysis['clinical_recommendation']}

**SYNDROME COMPONENTS:**"""
                
                components = digital_analysis['component_scores']
                component_names = {
                    'digital_native_status': 'Digital Native Conditioning',
                    'reality_dissociation': 'Online vs Offline Authenticity Gap',
                    'binary_success_pressure': 'Extraordinary Achievement Pressure',
                    'ironic_detachment': 'Emotional Protection Through Cynicism',
                    'algorithmic_dependency': 'Social Media Emotional Regulation',
                    'nihilistic_worldview': 'Hopelessness and Meaning Crisis',
                    'hope_avoidance': 'Resistance to Optimism',
                    'attention_fragmentation': 'Digital Attention Conditioning'
                }
                
                for comp, score in components.items():
                    name = component_names.get(comp, comp)
                    level = "HIGH" if score >= 4 else "MEDIUM" if score >= 2 else "LOW"
                    template += f"\n• {name}: {level} ({score:.1f}/5)"
                
                template += f"""

**REQUIRED THERAPEUTIC ADAPTATIONS:**
{"🚨 SPECIALIZED INTERVENTION REQUIRED" if severity in ['SEVERE', 'MODERATE'] else "✅ STANDARD APPROACH WITH MODIFICATIONS"}
"""
                
                adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
                for i, adaptation in enumerate(adaptations[:5], 1):
                    template += f"\n{i}. {adaptation}"
                
                if severity in ['SEVERE', 'MODERATE']:
                    template += f"""

**DIGITAL-NATIVE SESSION MODIFICATIONS:**
• Session Structure: {"20-minute focused segments" if severity == 'SEVERE' else "45-60 minutes with breaks"}
• Language Style: Collaborative, non-directive, intelligence-validating
• Authority Approach: Peer consultant vs traditional therapist-patient
• Hope Introduction: Evidence-based gradual vs overwhelming positivity
• Success Framework: Meaningful contribution vs extraordinary achievement
• Resistance Management: Expect intellectual challenges and cynicism
"""

        template += f"""

**SESSION PLANNING:**
Session 1 Focus: {session_plan.get('session_1_focus', 'Pattern analysis and rapport building')}
Session 2 Target: {session_plan.get('session_2_target', 'Core transformation and positive programming')}
Potential Session 3 Need: {session_plan.get('session_3_need', 'Reinforcement if needed')}

**THERAPEUTIC APPROACH:**
Intervention Keywords: {clinical_insights.get('intervention_keywords', 'Collaborative, gentle, permissive')}
Avoid Language: {clinical_insights.get('avoid_language', 'Pressure, criticism, commands')}
Predicted Resistance: {clinical_insights.get('resistance_points', ['Standard change resistance'])[0] if clinical_insights.get('resistance_points') else 'Standard patterns'}

{behavioral_sequence}

**SUCCESS PROBABILITY:**
Estimated Success Rate: {self._calculate_comprehensive_success_rate()}%
Based on: Pattern complexity, digital factors, readiness, completion rate

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL NOTES                          ║
╚══════════════════════════════════════════════════════════════╝

{"This assessment reveals a digital-native psychology requiring specialized intervention approaches. Traditional methods may fail without proper adaptations." if st.session_state.is_digital_native and st.session_state.assessment_results.get('digital_despair_analysis', {}).get('severity_level') in ['SEVERE', 'MODERATE'] else "This comprehensive analysis provides framework for effective hypnotherapy intervention based on traditional behavioral pattern constellation."}
"""
        
        return template

    def _calculate_comprehensive_success_rate(self):
        """Calculate comprehensive success rate including digital factors"""
        base_rate = 85  # Standard hypnotherapy success rate
        
        # Adjust for pattern complexity
        pattern_count = len(st.session_state.pattern_scores)
        if pattern_count >= 5:
            base_rate -= 10
        elif pattern_count >= 3:
            base_rate -= 5
        
        # Adjust for digital despair factors
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                if severity == 'SEVERE':
                    base_rate -= 15
                    base_rate += 10  # But add back for proper adaptations
                elif severity == 'MODERATE':
                    base_rate -= 8
                    base_rate += 8   # Adaptations help
        
        # Adjust for readiness
        for response_data in st.session_state.assessment_responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                readiness = response_data['response']['rating']
                if readiness >= 8:
                    base_rate += 10
                elif readiness <= 5:
                    base_rate -= 10
                break
        
        # Adjust for completion rate
        completion_rate = st.session_state.assessment_results.get('completion_rate', 0)
        if completion_rate >= 0.9:
            base_rate += 5
        elif completion_rate <= 0.7:
            base_rate -= 10
        
        return max(45, min(95, base_rate))

    # Clinical Insights Methods (simplified versions)
    def _extract_clinical_insights(self):
        """Extract basic clinical insights from assessment responses"""
        # This is a simplified version - in practice would be more comprehensive
        return {
            'core_limiting_belief': "Core belief requires session exploration",
            'hidden_benefits': "Pattern provides emotional protection and familiar identity",
            'systemic_resistance': "Minimal systemic resistance expected",
            'identity_threat': "Identity evolution requires careful navigation",
            'intervention_keywords': "Collaborative, gentle, permissive",
            'avoid_language': "Pressure, criticism, commands",
            'resistance_points': ["Standard change resistance", "Possible skepticism about process"]
        }

    def _generate_session_plan(self, pattern_scores, clinical_insights):
        """Generate session planning recommendations"""
        return {
            'session_1_focus': "Comprehensive pattern assessment and rapport building",
            'session_2_target': "Core pattern transformation and positive programming",
            'session_3_need': "Standard reinforcement if needed"
        }

    def _generate_behavioral_sequence_analysis(self):
        """Generate basic behavioral sequence analysis"""
        return """
╔══════════════════════════════════════════════════════════════╗
║            BEHAVIORAL SEQUENCE MAPPING                      ║
╚══════════════════════════════════════════════════════════════╝

Complete behavioral chain analysis available in full clinical template.
Session 1 will focus on completing any missing sequence components for
optimal intervention design.
"""

    def _render_results(self):
        """Render final results page"""
        st.markdown("## Your behavioral pattern analysis")
        
        # Show digital native indicator if applicable
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                if severity in ['SEVERE', 'MODERATE']:
                    st.markdown(f"""
                    <div class="digital-indicator">
                    🖥️ Digital Despair Syndrome Detected: {severity} ({score:.0f}% score) - Specialized intervention required
                    </div>
                    """, unsafe_allow_html=True)
        
        # Direct to clinical analysis
        self._render_clinical_analysis_section()
    
        st.markdown("### Your next steps")
        
        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            st.warning("⚠️ **Priority contact**: Given your urgency level, our clinical team will contact you within 24 hours.")
        
        # Show different messaging for digital natives
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                st.info("💡 **Specialized Approach**: Your assessment indicates digital-native psychology patterns that require adapted hypnotherapy techniques for optimal results.")
        
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
                    'is_digital_native': st.session_state.is_digital_native,
                    'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis')
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
        
        # Show digital despair results if applicable
        if st.session_state.is_digital_native:
            digital_analysis = results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                st.markdown(f"**🖥️ Digital Despair Syndrome Assessment: {severity}** ({score:.0f}% score)")
                
                if severity in ['SEVERE', 'MODERATE']:
                    st.warning(f"⚠️ **Specialized intervention required** - Traditional approaches may be less effective without digital-native adaptations")
                else:
                    st.success("✅ **Standard approach suitable** with digital considerations")
        
        # Show traditional patterns
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

def get_digital_analysis():
    """Get digital despair analysis if available"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results.get('digital_despair_analysis')
    return None

def is_digital_native():
    """Check if current user is assessed as digital native"""
    return st.session_state.get('is_digital_native', False)

def reset_assessment():
    """Reset assessment state"""
    keys_to_reset = [
        'assessment_responses', 'current_question', 'current_phase', 'phase_progress',
        'is_digital_native', 'digital_despair_score', 'digital_severity',
        'triggered_patterns', 'pattern_scores', 'risk_flags', 'assessment_completed', 
        'contact_provided', 'assessment_results', 'intensity_responses', 
        'trigger_chain', 'digital_responses', 'adaptive_paths'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]

def export_assessment_data():
    """Export complete assessment data including digital analysis"""
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
        'digital_responses': st.session_state.get('digital_responses', {}),
        'is_digital_native': st.session_state.get('is_digital_native', False),
        'digital_analysis': st.session_state.get('assessment_results', {}).get('digital_despair_analysis'),
        'phase_progress': st.session_state.get('phase_progress', {}),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }


if __name__ == "__main__":
    st.set_page_config(
        page_title="Enhanced Behavioral Pattern Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render()
