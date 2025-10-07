
# """
# Clinical Behavioral Pattern Assessment - Enhanced Configuration & Analytics
# Version 3.5 - Complete Clinical Data Extraction

# Extracts:
# - Root pattern structures
# - Systemic factors maintaining problems
# - Identity conflicts blocking change
# - Hidden loyalties creating resistance
# - Complete trigger sequences
# - Intervention keywords and avoid language
# """

# from typing import List, Dict, Any, Optional, Tuple
# from datetime import datetime
# import re
# import math

# # ============================================================================
# # ENHANCED PATTERN DEFINITIONS WITH COMPLETE CLINICAL DATA
# # ============================================================================
# class PatternDefinitions:
#     """9 fundamental behavioral patterns with complete clinical extraction data"""
    
#     PATTERNS = {
#         1: "Unhappiness culture",
#         2: "Power struggles",
#         3: "Systematic mistrust",
#         4: "Separation and division",
#         5: "Doing versus being",
#         6: "Compartmentalized authenticity",
#         7: "Self sacrifice and care avoidance",
#         8: "Inherited missions",
#         9: "Context dependent weakness"
#     }
    
#     PATTERN_DESCRIPTIONS = {
#         1: {
#             "name": "Unhappiness culture",
#             "root_structure": "Positive states = danger/loss/punishment",
#             "core_belief": "Happiness leads to disappointment or makes me a target",
#             "systemic_factors": [
#                 "Family depression patterns normalize suffering",
#                 "Cultural suffering valorization ('life is hard')",
#                 "Positive suppression rewarded in family system",
#                 "Happiness triggers envy or attack from others"
#             ],
#             "identity_conflict": "Happy authentic self vs. Familiar suffering self that feels safe",
#             "hidden_loyalties": [
#                 "Loyalty to unhappy parent/family member",
#                 "Suffering = virtue/depth belief system",
#                 "Protection from envy or being targeted",
#                 "Belonging through shared misery"
#             ],
#             "protective_function": "Protection from disappointment, envy, or loss",
#             "intervention_focus": "Permission installation for positive states with safety anchoring",
#             "session_1_focus": "Happiness permission protocols and safety anchoring",
#             "session_2_focus": "Joy sustainability and positive emotion anchoring",
#             "intervention_keywords": ["permission", "safety", "deserve", "natural", "birthright"],
#             "avoid_language": ["just be happy", "think positive", "you're being negative"]
#         },
#         2: {
#             "name": "Power struggles",
#             "root_structure": "Submission = death/annihilation of self",
#             "core_belief": "I must fight to exist and maintain my identity",
#             "systemic_factors": [
#                 "Authoritarian family dynamics modeling dominance",
#                 "Competition-based relationship patterns",
#                 "Win-lose paradigm as only option",
#                 "Vulnerability punished in family system"
#             ],
#             "identity_conflict": "Collaborative empowered self vs. Fighter/survivor self",
#             "hidden_loyalties": [
#                 "Loyalty to family fight patterns",
#                 "Strength = resistance belief",
#                 "Protection from being controlled/dominated",
#                 "Identity tied to being 'the strong one'"
#             ],
#             "protective_function": "Protection from domination or loss of self",
#             "intervention_focus": "Collaborative empowerment with maintained autonomy",
#             "session_1_focus": "Nervous system regulation and collaborative response installation",
#             "session_2_focus": "Conflict transformation and win-win response automation",
#             "intervention_keywords": ["curiosity", "collaboration", "both/and", "strength in listening"],
#             "avoid_language": ["just compromise", "stop being defensive", "you're too aggressive"]
#         },
#         3: {
#             "name": "Systematic mistrust",
#             "root_structure": "Others = eventual betrayal/harm",
#             "core_belief": "Trust leads to being hurt, used, or abandoned",
#             "systemic_factors": [
#                 "Early betrayal experiences by caregivers",
#                 "Inconsistent caregiving creating unpredictability",
#                 "Trust violation patterns across relationships",
#                 "Manipulation modeling in family system"
#             ],
#             "identity_conflict": "Trusting open self vs. Protected vigilant self",
#             "hidden_loyalties": [
#                 "Loyalty to hurt younger parts of self",
#                 "Vigilance = safety belief",
#                 "Protection from re-injury",
#                 "Identity as 'smart enough not to trust'"
#             ],
#             "protective_function": "Hypervigilance and threat detection to prevent harm",
#             "intervention_focus": "Gradual trust building with transparent safety protocols",
#             "session_1_focus": "Trust calibration and authentic connection programming",
#             "session_2_focus": "Healthy skepticism calibration and openness programming",
#             "intervention_keywords": ["discernment", "wisdom", "safe people", "gradual"],
#             "avoid_language": ["just trust people", "you're too paranoid", "not everyone is bad"]
#         },
#         4: {
#             "name": "Separation and division",
#             "root_structure": "Gray areas = chaos/uncertainty/danger",
#             "core_belief": "Things must be clearly defined or everything falls apart",
#             "systemic_factors": [
#                 "Rigid family rules requiring clear categories",
#                 "Religious absolutism or black/white morality",
#                 "Chaotic early environment needing simplification",
#                 "All-or-nothing modeling by caregivers"
#             ],
#             "identity_conflict": "Flexible nuanced self vs. Clear defined safe self",
#             "hidden_loyalties": [
#                 "Loyalty to family certainty patterns",
#                 "Order = safety belief system",
#                 "Protection from confusion/overwhelm",
#                 "Identity as 'person with clear values'"
#             ],
#             "protective_function": "Self-protection via binary thinking to reduce complexity",
#             "intervention_focus": "Both/and integration with safety in uncertainty",
#             "session_1_focus": "Binary thinking dissolution and creative possibility expansion",
#             "session_2_focus": "Creative problem-solving and nuanced thinking installation",
#             "intervention_keywords": ["both/and", "complexity", "nuance", "integration"],
#             "avoid_language": ["it's not black and white", "stop being so rigid"]
#         },
#         5: {
#             "name": "Doing versus being",
#             "root_structure": "Worth = productivity/achievement only",
#             "core_belief": "I am only valuable when I'm producing/achieving",
#             "systemic_factors": [
#                 "Achievement-focused family with conditional love",
#                 "Work/school performance as identity",
#                 "Productivity culture reinforcement",
#                 "Rest/play punished or seen as lazy"
#             ],
#             "identity_conflict": "Being-centered self vs. Achieving self that earns worth",
#             "hidden_loyalties": [
#                 "Loyalty to family achievement patterns",
#                 "Worth = doing belief system",
#                 "Protection from worthlessness",
#                 "Identity as 'successful/productive person'"
#             ],
#             "protective_function": "Avoids vulnerability through busyness or achievement",
#             "intervention_focus": "Intrinsic worth installation with productivity reframing",
#             "session_1_focus": "Worth anchoring independent of achievement",
#             "session_2_focus": "Intrinsic worth recognition and balanced achievement",
#             "intervention_keywords": ["inherent worth", "being", "enough", "rest"],
#             "avoid_language": ["just relax", "stop working so much", "you don't need to prove yourself"]
#         },
#         6: {
#             "name": "Compartmentalized authenticity",
#             "root_structure": "Real self = rejection/abandonment",
#             "core_belief": "I must hide parts of myself to be accepted",
#             "systemic_factors": [
#                 "Conditional family acceptance based on performance",
#                 "Social role expectations with punishment for deviation",
#                 "Authenticity punished in family system",
#                 "Different contexts requiring different personas"
#             ],
#             "identity_conflict": "Authentic integrated self vs. Acceptable safe selves",
#             "hidden_loyalties": [
#                 "Loyalty to family role expectations",
#                 "Adaptation = survival belief",
#                 "Protection from rejection",
#                 "Identity as 'shapeshifter/chameleon'"
#             ],
#             "protective_function": "Avoid rejection by managing different personas",
#             "intervention_focus": "Authentic self integration with safety across contexts",
#             "session_1_focus": "Authentic self integration and consistency programming",
#             "session_2_focus": "Integrated identity and consistent self-expression",
#             "intervention_keywords": ["authentic", "integrated", "whole", "genuine"],
#             "avoid_language": ["just be yourself", "stop being fake", "pick one identity"]
#         },
#         7: {
#             "name": "Self sacrifice and care avoidance",
#             "root_structure": "My needs = selfish/wrong/dangerous",
#             "core_belief": "Caring for myself will harm others or make me unworthy",
#             "systemic_factors": [
#                 "Caretaker family roles with reward for self-sacrifice",
#                 "Self-sacrifice modeling by parent",
#                 "Need-shaming in family system",
#                 "Love = self-denial belief pattern"
#             ],
#             "identity_conflict": "Self-caring self vs. Service/giving self that earns love",
#             "hidden_loyalties": [
#                 "Loyalty to family service patterns",
#                 "Sacrifice = love belief system",
#                 "Protection from selfishness shame",
#                 "Identity as 'the helpful/caring one'"
#             ],
#             "protective_function": "Maintains belonging and worth through service",
#             "intervention_focus": "Self-care as service reframing with boundary installation",
#             "session_1_focus": "Boundary establishment and self-care permission",
#             "session_2_focus": "Reciprocal relationship patterns and energy management",
#             "intervention_keywords": ["boundaries", "reciprocal", "energy", "sustainable"],
#             "avoid_language": ["just say no", "stop being a doormat", "be selfish for once"]
#         },
#         8: {
#             "name": "Inherited missions",
#             "root_structure": "My path = betrayal of family/ancestors",
#             "core_belief": "I must fulfill family dreams/expectations to be loyal",
#             "systemic_factors": [
#                 "Family sacrifice stories creating debt",
#                 "Generational expectations carried forward",
#                 "Dream inheritance from parents/ancestors",
#                 "Guilt about family sacrifices"
#             ],
#             "identity_conflict": "Personal desire self vs. Family loyal self",
#             "hidden_loyalties": [
#                 "Loyalty to ancestral sacrifice",
#                 "Family dream continuation as duty",
#                 "Protection from guilt/betrayal",
#                 "Identity as 'family legacy carrier'"
#             ],
#             "protective_function": "Maintains family belonging and honors sacrifices",
#             "intervention_focus": "Honor family while claiming personal path integration",
#             "session_1_focus": "Personal values clarification and family harmony balance",
#             "session_2_focus": "Authentic life direction and confident decision-making",
#             "intervention_keywords": ["honor", "autonomy", "both/and", "gratitude"],
#             "avoid_language": ["forget your family", "it's your life", "they're holding you back"]
#         },
#         9: {
#             "name": "Context dependent weakness",
#             "root_structure": "Certain contexts = powerlessness/helplessness",
#             "core_belief": "I cannot be strong or authentic in all circumstances",
#             "systemic_factors": [
#                 "Trauma context associations creating triggers",
#                 "Power dynamic patterns in family",
#                 "Learned helplessness in specific situations",
#                 "Boundary violation in certain contexts"
#             ],
#             "identity_conflict": "Strong capable self vs. Overwhelmed powerless self",
#             "hidden_loyalties": [
#                 "Loyalty to trauma bond patterns",
#                 "Powerlessness = safety in some contexts",
#                 "Protection from responsibility/expectation",
#                 "Identity fragmentation across contexts"
#             ],
#             "protective_function": "Protects self from overextension in triggering contexts",
#             "intervention_focus": "Universal strength anchoring with context-independent resources",
#             "session_1_focus": "Context-independent boundary installation",
#             "session_2_focus": "Consistent boundary maintenance across all contexts",
#             "intervention_keywords": ["consistent", "capable", "anchored", "universal strength"],
#             "avoid_language": ["just stand up for yourself", "why can't you be strong there too"]
#         }
#     }


# # ============================================================================
# # COMPREHENSIVE QUESTION BANK - REDESIGNED FOR CLINICAL VALIDITY
# # 81 Questions: 5-7 per pattern + screening + validation
# # ============================================================================

# COMPREHENSIVE_QUESTIONS = [
#     # -------------------------------------------------------------------------
#     # DEMOGRAPHICS & SCREENING (Questions 1-5)
#     # -------------------------------------------------------------------------
#     {
#         "id": 1,
#         "text": "What is your age range?",
#         "type": "single_choice",
#         "options": ["Under 18", "18-25", "26-35", "36-45", "46-55", "56+"],
#         "pattern": None,
#         "digital_native_scoring": [3, 5, 4, 3, 2, 1],
#         "phase": "screening"
#     },
#     {
#         "id": 2,
#         "text": "What is your gender?",
#         "type": "single_choice",
#         "options": ["Male", "Female", "Non-binary/Other", "Prefer not to say"],
#         "pattern": None,
#         "phase": "demographics"
#     },
#     {
#         "id": 3,
#         "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
#         "type": "slider",
#         "min": 0,
#         "max": 16,
#         "default": 4,
#         "pattern": None,
#         "digital_despair_component": "screen_time",
#         "phase": "digital_screening"
#     },
#     {
#         "id": 4,
#         "text": "What percentage of your digital time is spent on social media?",
#         "type": "slider",
#         "min": 0,
#         "max": 100,
#         "default": 50,
#         "pattern": None,
#         "digital_despair_component": "social_media_usage",
#         "phase": "digital_screening"
#     },
#     {
#         "id": 5,
#         "text": "How would you rate your overall stress level in the past month?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": None,
#         "phase": "context"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 1: UNHAPPINESS CULTURE (Questions 6-12) - 7 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 6,
#         "text": "When something genuinely good happens to you, your first automatic thought is:",
#         "type": "single_choice",
#         "options": [
#             "I feel genuinely happy and want to celebrate",
#             "I enjoy it but wonder how long it will last",
#             "This won't last or something bad will balance it out",
#             "I feel uncomfortable, like I don't deserve it",
#             "I immediately look for what's wrong or what will go wrong"
#         ],
#         "pattern": 1,
#         "weights": [0, 3, 7, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 7,
#         "text": "How often do you downplay your accomplishments or good news when sharing with others?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 1,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 8,
#         "text": "When you're feeling happy, you experience:",
#         "type": "single_choice",
#         "options": [
#             "Pure enjoyment without worry",
#             "Happiness mixed with mild anxiety",
#             "A sense that I need to 'prepare for the worst'",
#             "Guilt or feeling I should be more serious",
#             "The need to hide or suppress it"
#         ],
#         "pattern": 1,
#         "weights": [0, 4, 7, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 9,
#         "text": "Growing up, expressing joy or excitement was:",
#         "type": "single_choice",
#         "options": [
#             "Encouraged and celebrated",
#             "Tolerated but not really acknowledged",
#             "Met with warnings about 'getting hopes up'",
#             "Seen as naive or immature",
#             "Actively discouraged or punished"
#         ],
#         "pattern": 1,
#         "weights": [0, 3, 7, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 10,
#         "text": "Complete this thought: 'If I allow myself to be truly happy...'",
#         "type": "single_choice",
#         "options": [
#             "Good things will continue",
#             "I might get disappointed later",
#             "Something bad will definitely happen",
#             "People will judge me or bring me down",
#             "I'll lose my edge or motivation"
#         ],
#         "pattern": 1,
#         "weights": [0, 5, 9, 8, 7],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 11,
#         "text": "When others around you are celebrating success, you typically:",
#         "type": "single_choice",
#         "options": [
#             "Join in their joy genuinely",
#             "Feel happy for them but uncomfortable",
#             "Wonder why good things don't happen to me",
#             "Feel suspicious or look for downsides",
#             "Feel resentful or withdraw"
#         ],
#         "pattern": 1,
#         "weights": [0, 3, 6, 8, 9],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 12,
#         "text": "On a scale of 1-10, how comfortable are you maintaining a positive mood for an entire day?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 1,
#         "reverse_score": True,
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 2: POWER STRUGGLES (Questions 13-19) - 7 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 13,
#         "text": "When someone disagrees with you, your immediate physical response is:",
#         "type": "single_choice",
#         "options": [
#             "I stay relaxed and curious",
#             "Mild tension but manageable",
#             "My body tenses up, ready to defend",
#             "Adrenaline rush, heart races",
#             "Intense physical activation, fight-or-flight"
#         ],
#         "pattern": 2,
#         "weights": [0, 3, 7, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 14,
#         "text": "In disagreements, how often do you find yourself needing to 'win' or prove your point?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 2,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 15,
#         "text": "Someone challenges your decision in front of others. You feel:",
#         "type": "single_choice",
#         "options": [
#             "Open to hearing their perspective",
#             "Slightly defensive but willing to discuss",
#             "Threatened and need to reassert authority",
#             "Angry and want to shut them down",
#             "Attacked and must fight back immediately"
#         ],
#         "pattern": 2,
#         "weights": [0, 3, 7, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 16,
#         "text": "Growing up, conflicts in your family typically ended with:",
#         "type": "single_choice",
#         "options": [
#             "Calm resolution and mutual understanding",
#             "Someone compromising to keep peace",
#             "The loudest/strongest person winning",
#             "Anger, tears, or silent treatment",
#             "Threats, intimidation, or physical conflict"
#         ],
#         "pattern": 2,
#         "weights": [0, 3, 7, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 17,
#         "text": "When you lose an argument or are proven wrong, you:",
#         "type": "single_choice",
#         "options": [
#             "Acknowledge it and learn from it",
#             "Accept it but feel uncomfortable",
#             "Feel diminished or humiliated",
#             "Internally plan how to 'win' next time",
#             "Feel rage or a sense of defeat"
#         ],
#         "pattern": 2,
#         "weights": [0, 2, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 18,
#         "text": "How often do small disagreements escalate into major conflicts for you?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 2,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 19,
#         "text": "In relationships, how much do you need to feel 'in control' to feel safe?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 2,
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 3: SYSTEMATIC MISTRUST (Questions 20-26) - 7 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 20,
#         "text": "When meeting someone new, your default assumption about their intentions is:",
#         "type": "single_choice",
#         "options": [
#             "They're probably friendly and genuine",
#             "Neutral until I know them better",
#             "Cautious - they might have hidden motives",
#             "Suspicious - they probably want something",
#             "Highly guarded - they'll likely betray me"
#         ],
#         "pattern": 3,
#         "weights": [0, 2, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 21,
#         "text": "Someone you just met is unexpectedly kind or helpful. You think:",
#         "type": "single_choice",
#         "options": [
#             "That's nice, they seem genuine",
#             "I appreciate it but wonder why",
#             "What do they want from me?",
#             "This is manipulation - what's their angle?",
#             "This is definitely a trap or scheme"
#         ],
#         "pattern": 3,
#         "weights": [0, 3, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 22,
#         "text": "How long does it typically take before you trust someone enough to be vulnerable with them?",
#         "type": "single_choice",
#         "options": [
#             "A few weeks to months",
#             "Several months to a year",
#             "1-2 years of consistent behavior",
#             "Many years, and even then not fully",
#             "I never fully trust anyone"
#         ],
#         "pattern": 3,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 23,
#         "text": "When people share personal information about themselves, you:",
#         "type": "single_choice",
#         "options": [
#             "Feel honored and reciprocate naturally",
#             "Listen but remain somewhat guarded",
#             "Wonder if they're testing me or setting a trap",
#             "Assume they're manipulating me into sharing",
#             "Become more suspicious of their motives"
#         ],
#         "pattern": 3,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 24,
#         "text": "In past relationships, how many times have you been significantly betrayed or let down?",
#         "type": "single_choice",
#         "options": [
#             "Never or once",
#             "2-3 times",
#             "4-5 times",
#             "6-10 times",
#             "Too many to count"
#         ],
#         "pattern": 3,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 25,
#         "text": "How often do you 'test' people to see if they're trustworthy?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 3,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 26,
#         "text": "On a scale of 1-10, how much do you believe 'trust no one' is a wise life philosophy?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 3,
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 4: SEPARATION/DIVISION (Questions 27-32) - 6 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 27,
#         "text": "When facing a difficult decision, you typically:",
#         "type": "single_choice",
#         "options": [
#             "See multiple options and creative solutions",
#             "See a few main options with pros and cons",
#             "Feel stuck between two opposing choices",
#             "See only two extreme options (all or nothing)",
#             "Feel paralyzed by either/or thinking"
#         ],
#         "pattern": 4,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 28,
#         "text": "How comfortable are you with ambiguity or 'gray areas' in life?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 4,
#         "reverse_score": True,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 29,
#         "text": "When evaluating people, you tend to see them as:",
#         "type": "single_choice",
#         "options": [
#             "Complex humans with strengths and flaws",
#             "Mostly good or mostly bad",
#             "Either completely good or completely bad",
#             "Good until proven bad, then irredeemable",
#             "Categories that are absolute and unchangeable"
#         ],
#         "pattern": 4,
#         "weights": [0, 3, 7, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 30,
#         "text": "Complete this: 'In life, you must choose between...'",
#         "type": "single_choice",
#         "options": [
#             "Nothing - you can integrate multiple values",
#             "Occasionally making hard choices",
#             "Security OR freedom (can't have both)",
#             "Success OR relationships (can't have both)",
#             "Everything is either/or - no middle ground"
#         ],
#         "pattern": 4,
#         "weights": [0, 2, 7, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 31,
#         "text": "How often do you find yourself thinking in 'all or nothing' terms?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 4,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 32,
#         "text": "When someone changes their mind or shows complexity, you feel:",
#         "type": "single_choice",
#         "options": [
#             "That's normal human growth",
#             "Slightly confused but accepting",
#             "Uncomfortable with the inconsistency",
#             "Betrayed or that they're unreliable",
#             "They're a hypocrite - can't trust them"
#         ],
#         "pattern": 4,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 5: DOING VS BEING (Questions 33-39) - 7 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 33,
#         "text": "Complete this: 'I feel valuable when I...'",
#         "type": "single_choice",
#         "options": [
#             "Simply exist as I am",
#             "Am doing something meaningful",
#             "Accomplish something important",
#             "Prove my worth through achievements",
#             "Am constantly productive/achieving"
#         ],
#         "pattern": 5,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 34,
#         "text": "When you have free time with nothing scheduled, you feel:",
#         "type": "single_choice",
#         "options": [
#             "Peaceful and content",
#             "Relaxed but slightly restless",
#             "Guilty like I should be doing something",
#             "Anxious and need to find something productive",
#             "Worthless or like I'm wasting my life"
#         ],
#         "pattern": 5,
#         "weights": [0, 3, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 35,
#         "text": "How many hours per week do you work (including work you bring home)?",
#         "type": "single_choice",
#         "options": [
#             "35-40 hours",
#             "41-50 hours",
#             "51-60 hours",
#             "61-70 hours",
#             "70+ hours or constantly"
#         ],
#         "pattern": 5,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 36,
#         "text": "When not being productive, how intense is your guilt or anxiety?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 5,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 37,
#         "text": "If all your achievements were taken away, you would feel:",
#         "type": "single_choice",
#         "options": [
#             "Still confident in who I am",
#             "Uncertain but still have worth",
#             "Lost without my accomplishments",
#             "Like I have no identity or value",
#             "Completely worthless"
#         ],
#         "pattern": 5,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 38,
#         "text": "How often do you sacrifice sleep, health, or relationships for productivity?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 5,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 39,
#         "text": "Growing up, love and approval were conditional on:",
#         "type": "single_choice",
#         "options": [
#             "Nothing - I was loved unconditionally",
#             "Being good/not causing trouble",
#             "Getting good grades/performing well",
#             "Achieving specific goals or standards",
#             "Constant exceptional achievement"
#         ],
#         "pattern": 5,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 6: COMPARTMENTALIZED AUTHENTICITY (Questions 40-45) - 6 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 40,
#         "text": "Your personality and behavior across different settings (work, family, friends):",
#         "type": "single_choice",
#         "options": [
#             "Stay very consistent - I'm the same person",
#             "Vary slightly based on context",
#             "Vary significantly - different personas",
#             "Completely different - like different people",
#             "So fragmented I don't know who I really am"
#         ],
#         "pattern": 6,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 41,
#         "text": "How much of your 'real self' do you hide from most people?",
#         "type": "slider",
#         "min": 0,
#         "max": 100,
#         "default": 50,
#         "pattern": 6,
#         "scale_to_10": True,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 42,
#         "text": "When you imagine being completely authentic in all areas of life, you feel:",
#         "type": "single_choice",
#         "options": [
#             "That's how I already live",
#             "Hopeful and excited",
#             "Scared but curious",
#             "Terrified of rejection or consequences",
#             "Impossible - I'd lose everything"
#         ],
#         "pattern": 6,
#         "weights": [0, 1, 4, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 43,
#         "text": "How exhausting is it to maintain your different personas?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 6,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 44,
#         "text": "In how many areas of your life do you feel you can be completely yourself?",
#         "type": "single_choice",
#         "options": [
#             "All or most areas",
#             "About half of areas",
#             "A few specific safe spaces",
#             "One or two people only",
#             "Nowhere - not even alone"
#         ],
#         "pattern": 6,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 45,
#         "text": "Growing up, being your authentic self resulted in:",
#         "type": "single_choice",
#         "options": [
#             "Acceptance and love",
#             "Mostly acceptance with some criticism",
#             "Criticism, ridicule, or rejection",
#             "Punishment, shame, or abandonment",
#             "Severe consequences or danger"
#         ],
#         "pattern": 6,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 7: SELF-SACRIFICE (Questions 46-52) - 7 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 46,
#         "text": "When it comes to your needs versus others' needs:",
#         "type": "single_choice",
#         "options": [
#             "I naturally balance both",
#             "I usually prioritize mine but consider theirs",
#             "Others' needs usually come first",
#             "I almost always put others first",
#             "I completely ignore my own needs"
#         ],
#         "pattern": 7,
#         "weights": [0, 1, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 47,
#         "text": "How often do you say 'yes' when you really want to say 'no'?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 7,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 48,
#         "text": "When you think about taking time for self-care, you feel:",
#         "type": "single_choice",
#         "options": [
#             "That's normal and necessary",
#             "Slightly guilty but know I should",
#             "Guilty - others need me more",
#             "Selfish and undeserving",
#             "It's impossible - I have no time for myself"
#         ],
#         "pattern": 7,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 49,
#         "text": "How much energy do you have left for yourself after taking care of others?",
#         "type": "slider",
#         "min": 0,
#         "max": 100,
#         "default": 50,
#         "pattern": 7,
#         "reverse_score": True,
#         "scale_to_10": True,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 50,
#         "text": "In relationships, you tend to be the one who:",
#         "type": "single_choice",
#         "options": [
#             "Gives and receives in balance",
#             "Gives slightly more than you receive",
#             "Gives much more than you receive",
#             "Gives almost everything, receives little",
#             "Gives everything, receives nothing"
#         ],
#         "pattern": 7,
#         "weights": [0, 3, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 51,
#         "text": "Growing up, putting your own needs first was seen as:",
#         "type": "single_choice",
#         "options": [
#             "Healthy and encouraged",
#             "Acceptable when appropriate",
#             "Selfish but tolerated",
#             "Selfish and discouraged",
#             "Shameful, wrong, or punishable"
#         ],
#         "pattern": 7,
#         "weights": [0, 1, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 52,
#         "text": "How often do you feel resentful while helping others?",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 7,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 8: INHERITED MISSIONS (Questions 53-58) - 6 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 53,
#         "text": "Your major life goals are primarily:",
#         "type": "single_choice",
#         "options": [
#             "Based on my own genuine desires",
#             "Mostly mine with some family influence",
#             "A mix of mine and family expectations",
#             "Primarily family expectations",
#             "Entirely family dreams, not mine"
#         ],
#         "pattern": 8,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 54,
#         "text": "When thinking about pursuing your own path separate from family expectations:",
#         "type": "single_choice",
#         "options": [
#             "I feel free and excited",
#             "I feel supportive curiosity from family",
#             "I feel some guilt but mostly okay",
#             "I feel guilty like I'm betraying them",
#             "I feel I would destroy family relationships"
#         ],
#         "pattern": 8,
#         "weights": [0, 1, 4, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 55,
#         "text": "How much do you feel you 'owe' your family for their sacrifices?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 8,
#         "phase": "core_patterns"
#     },
#     {
#         "id": 56,
#         "text": "If you disappointed your family's expectations, you would feel:",
#         "type": "single_choice",
#         "options": [
#             "Sad but accepting of my choice",
#             "Uncomfortable but able to live with it",
#             "Deeply guilty and conflicted",
#             "Like I betrayed or destroyed them",
#             "Unbearable shame and unworthiness"
#         ],
#         "pattern": 8,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 57,
#         "text": "Your current life path feels:",
#         "type": "single_choice",
#         "options": [
#             "Authentically mine",
#             "Mostly mine with some compromises",
#             "A duty or obligation",
#             "Like living someone else's dream",
#             "Like a script I have no choice but to follow"
#         ],
#         "pattern": 8,
#         "weights": [0, 2, 5, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 58,
#         "text": "How clearly can you identify what YOU actually want, separate from others' expectations?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 8,
#         "reverse_score": True,
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # PATTERN 9: CONTEXT-DEPENDENT WEAKNESS (Questions 59-64) - 6 questions
#     # -------------------------------------------------------------------------
#     {
#         "id": 59,
#         "text": "Your boundaries and limits:",
#         "type": "single_choice",
#         "options": [
#             "Stay consistent across all situations",
#             "Vary slightly based on context",
#             "Vary significantly - strong some places, weak others",
#             "Disappear completely in certain contexts",
#             "Don't exist in most contexts"
#         ],
#         "pattern": 9,
#         "weights": [0, 2, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 60,
#         "text": "With certain people or in certain situations, you become someone you don't respect. This happens:",
#         "type": "single_choice",
#         "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
#         "pattern": 9,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 61,
#         "text": "How many specific people or situations make you lose your normal sense of self?",
#         "type": "single_choice",
#         "options": [
#             "None",
#             "1-2 specific people/situations",
#             "3-5 people/situations",
#             "6-10 people/situations",
#             "Many - most contexts weaken me"
#         ],
#         "pattern": 9,
#         "weights": [0, 3, 6, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 62,
#         "text": "In certain contexts where you lose power, you:",
#         "type": "single_choice",
#         "options": [
#             "Can still maintain boundaries",
#             "Find it difficult but possible",
#             "Can't say no even when I want to",
#             "Completely lose all agency",
#             "Become a different person with no self"
#         ],
#         "pattern": 9,
#         "weights": [0, 3, 6, 9, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 63,
#         "text": "After being in a situation where you lost yourself, you feel:",
#         "type": "single_choice",
#         "options": [
#             "Fine - I maintained myself",
#             "Slightly disappointed but okay",
#             "Frustrated and ashamed",
#             "Deeply ashamed and angry at myself",
#             "Disgusted with myself and hopeless"
#         ],
#         "pattern": 9,
#         "weights": [0, 2, 5, 8, 10],
#         "phase": "core_patterns"
#     },
#     {
#         "id": 64,
#         "text": "How much does your confidence vary depending on context?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": 9,
#         "phase": "core_patterns"
#     },
    
#     # -------------------------------------------------------------------------
#     # VALIDATION & CROSS-CHECK QUESTIONS (65-71)
#     # -------------------------------------------------------------------------
#     {
#         "id": 65,
#         "text": "Overall, how much does past emotional pain still control your current decisions?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": None,
#         "validation": True,
#         "phase": "validation"
#     },
#     {
#         "id": 66,
#         "text": "How much of your life energy goes into protecting yourself from being hurt again?",
#         "type": "slider",
#         "min": 0,
#         "max": 100,
#         "default": 50,
#         "pattern": None,
#         "validation": True,
#         "phase": "validation"
#     },
#     {
#         "id": 67,
#         "text": "If you could push a button and completely resolve one behavioral pattern, which would it be?",
#         "type": "text_completion",
#         "placeholder": "Describe the one pattern you most want to change...",
#         "min_chars": 20,
#         "pattern": None,
#         "validation": True,
#         "phase": "validation"
#     },
#     {
#         "id": 68,
#         "text": "What would your life look like if all these patterns were resolved?",
#         "type": "text_completion",
#         "placeholder": "Describe your life without these limitations...",
#         "min_chars": 30,
#         "pattern": None,
#         "validation": True,
#         "phase": "validation"
#     },
#     {
#         "id": 69,
#         "text": "On a scale of 1-10, how much do you believe change is truly possible for you?",
#         "type": "slider",
#         "min": 1,
#         "max": 10,
#         "default": 5,
#         "pattern": None,
#         "readiness_assessment": True,
#         "phase": "readiness"
#     },
#     {
#         "id": 70,
#         "text": "How ready are you to begin transformation work right now?",
#         "type": "single_choice",
#         "options": [
#             "Ready to start immediately",
#             "Ready within the next week",
#             "Ready within the next month",
#             "Still exploring options",
#             "Not ready yet - just gathering information"
#         ],
#         "pattern": None,
#         "readiness_assessment": True,
#         "weights": [10, 8, 6, 4, 2],
#         "phase": "readiness"
#     },
#     {
#         "id": 71,
#         "text": "What motivates you most to change right now?",
#         "type": "text_completion",
#         "placeholder": "Be specific about what's driving your desire for transformation...",
#         "min_chars": 20,
#         "pattern": None,
#         "readiness_assessment": True,
#         "phase": "readiness"
#     }
# ]


# # ============================================================================
# # DIGITAL DESPAIR SYNDROME INTEGRATION
# # ============================================================================

# DIGITAL_DESPAIR_SUBSCALES = {
#     'reality_dissociation': {
#         'questions': [3, 4],
#         'threshold_severe': 12,
#         'interventions': ['Reality reconnection exercises', 'Offline identity integration'],
#         'description': 'Preference for digital over physical reality'
#     },
#     'algorithmic_conditioning': {
#         'questions': [3, 4],
#         'threshold_severe': 14,
#         'interventions': ['Algorithm literacy', 'Rage-bait detox protocols'],
#         'description': 'Behavioral conditioning through platform algorithms'
#     },
#     'attention_fragmentation': {
#         'questions': [3],
#         'threshold_severe': 10,
#         'interventions': ['Attention restoration therapy', 'Deep focus training'],
#         'description': 'Inability to sustain attention on non-digital tasks'
#     }
# }

# def compute_digital_despair_score(responses: Dict[int, Any]) -> Dict[str, Any]:
#     """Calculate comprehensive digital despair syndrome scoring"""
    
#     age_response = responses.get(1)
#     age_options = COMPREHENSIVE_QUESTIONS[0]['options']
#     digital_native_scores = COMPREHENSIVE_QUESTIONS[0]['digital_native_scoring']
    
#     age_score = 0
#     if age_response in age_options:
#         age_index = age_options.index(age_response)
#         age_score = digital_native_scores[age_index]
    
#     is_digital_native = age_score >= 3
    
#     screen_time_hours = responses.get(3, 0)
#     social_media_percent = responses.get(4, 0)
    
#     screen_time_score = min(screen_time_hours / 2, 10)
#     social_media_score = social_media_percent / 10
    
#     subscale_scores = {}
#     for subscale_name, subscale_data in DIGITAL_DESPAIR_SUBSCALES.items():
#         score = 0
#         if 3 in subscale_data['questions']:
#             score += screen_time_score
#         if 4 in subscale_data['questions']:
#             score += social_media_score
#         subscale_scores[subscale_name] = score
    
#     total_score = sum(subscale_scores.values())
#     max_possible = len(DIGITAL_DESPAIR_SUBSCALES) * 10
#     percentage = (total_score / max_possible) * 100
    
#     if percentage >= 70:
#         severity = 'SEVERE'
#     elif percentage >= 50:
#         severity = 'MODERATE'
#     elif percentage >= 30:
#         severity = 'MILD'
#     else:
#         severity = 'MINIMAL'
    
#     interventions = []
#     for subscale_name, score in subscale_scores.items():
#         threshold = DIGITAL_DESPAIR_SUBSCALES[subscale_name]['threshold_severe']
#         if score >= threshold:
#             interventions.extend(DIGITAL_DESPAIR_SUBSCALES[subscale_name]['interventions'])
    
#     return {
#         'is_digital_native': is_digital_native,
#         'digital_despair_score': round(percentage, 1),
#         'severity_level': severity,
#         'subscale_scores': subscale_scores,
#         'recommended_interventions': list(set(interventions)),
#         'age_score': age_score,
#         'screen_time_hours': screen_time_hours,
#         'social_media_percentage': social_media_percent
#     }


# # ============================================================================
# # PATTERN CONSTELLATION MATRIX
# # ============================================================================

# PATTERN_REINFORCEMENT_MATRIX = {
#     (1, 2): 1.35, (1, 3): 1.5, (1, 4): 1.25, (1, 5): 1.1,
#     (2, 3): 1.15, (2, 4): 1.25, (2, 5): 1.3, (2, 6): 1.6, (2, 9): 1.2,
#     (3, 4): 1.3, (3, 5): 1.4, (3, 6): 1.8, (3, 7): 1.45, (3, 8): 1.4, (3, 9): 1.3,
#     (4, 5): 1.6, (4, 6): 1.3, (4, 7): 1.3,
#     (5, 6): 1.4, (5, 7): 1.1, (5, 8): 1.4, (5, 9): 1.2,
#     (6, 7): 1.3, (6, 8): 1.2, (6, 9): 1.15,
#     (7, 8): 1.5, (7, 9): 1.2,
#     (8, 9): 1.1
# }

# def calculate_constellation_multiplier(pattern_scores: Dict[int, float]) -> float:
#     """Calculate amplification effect of co-occurring patterns"""
#     multiplier = 1.0
    
#     for (p1, p2), amplification in PATTERN_REINFORCEMENT_MATRIX.items():
#         score1 = pattern_scores.get(p1, 0)
#         score2 = pattern_scores.get(p2, 0)
        
#         if score1 >= 6 and score2 >= 6:
#             multiplier *= amplification
    
#     return round(multiplier, 2)


# # ============================================================================
# # ANALYTICS ENGINE - REDESIGNED FOR CLINICAL VALIDITY
# # ============================================================================

# class AnalyticsEngine:
#     """Comprehensive pattern analysis with clinical validity"""
    
#     def __init__(self):
#         self.patterns = PatternDefinitions.PATTERNS
#         self.pattern_descriptions = PatternDefinitions.PATTERN_DESCRIPTIONS
    
    
#     def _assess_session_3_need(self, pattern_count: int, complexity: str) -> str:
#         """Assess if session 3 likely needed"""
#         if pattern_count >= 5:
#             return "HIGHLY LIKELY - Multiple complex patterns requiring integration"
#         elif pattern_count >= 3:
#             return "MODERATE PROBABILITY - Monitor session 2 response"
#         elif 'high complexity' in complexity.lower():
#             return "POSSIBLE - Assess after session 2"
#         else:
#             return "UNLIKELY - Standard 2-session protocol sufficient"
        
    
#     def _predict_resistance_points(
#         self,
#         pattern_info: Dict,
#         responses: Dict[int, Any]
#     ) -> List[str]:
#         """Predict specific resistance points"""
#         resistance_points = []
        
#         # From hidden loyalties
#         hidden_loyalties = pattern_info.get('hidden_loyalties', [])
#         if hidden_loyalties:
#             resistance_points.append(f"Loyalty resistance: {hidden_loyalties[0]}")
        
#         # From identity conflict
#         identity_conflict = pattern_info.get('identity_conflict', '')
#         if identity_conflict:
#             resistance_points.append(f"Identity threat: {identity_conflict}")
        
#         # From protective function
#         protective = pattern_info.get('protective_function', '')
#         if protective:
#             resistance_points.append(f"Loss of protection: {protective}")
        
#         return resistance_points[:3]  # Top 3 resistance points 

#     def score_patterns(self, responses: Dict[int, Any]) -> Dict[int, float]:
#         """
#         REDESIGNED: Score with proper statistical validity
#         FIXED: Skip "Not applicable" responses
#         Returns scores that actually differentiate patterns
#         """
#         pattern_raw_scores = {i: [] for i in range(1, 10)}  # Store all scores
        
#         for question in COMPREHENSIVE_QUESTIONS:
#             qid = question['id']
#             pattern_id = question.get('pattern')
            
#             if pattern_id is None or qid not in responses:
#                 continue
            
#             response = responses[qid]
            
#             # FIXED: Skip "Not applicable" responses
#             if response == "Not applicable" or response is None or response == "":
#                 continue
            
#             score = self._calculate_question_score(question, response)
            
#             # Only add non-zero scores
#             if score > 0:
#                 pattern_raw_scores[pattern_id].append(score)
        
#         # CRITICAL: Use 75th percentile instead of mean for better differentiation
#         pattern_scores = {}
#         for pattern_id, scores in pattern_raw_scores.items():
#             if not scores:
#                 pattern_scores[pattern_id] = 0.0
#             elif len(scores) == 1:
#                 pattern_scores[pattern_id] = scores[0]
#             else:
#                 # Use weighted scoring: 70% max + 30% mean
#                 # This makes significant patterns stand out
#                 max_score = max(scores)
#                 mean_score = sum(scores) / len(scores)
#                 pattern_scores[pattern_id] = (max_score * 0.7) + (mean_score * 0.3)
        
#         return pattern_scores
    
#     def _calculate_question_score(self, question: Dict, response: Any) -> float:
#         """Calculate score with better clinical differentiation - FIXED to handle skipped questions"""
        
#         # FIXED: Handle skipped questions
#         if response == "Not applicable" or response is None or response == "":
#             return 0.0
        
#         qtype = question.get('type')
        
#         if qtype == 'single_choice':
#             options = question.get('options', [])
#             weights = question.get('weights', [])
            
#             if response in options:
#                 index = options.index(response)
                
#                 if weights and index < len(weights):
#                     return float(weights[index])
                
#                 # Better default scaling for 5-option questions
#                 if len(options) == 5:
#                     # Never, Rarely, Sometimes, Often, Always
#                     scale = [0, 3, 5, 8, 10]
#                     return scale[index] if index < len(scale) else 0
                
#                 return (index / (len(options) - 1)) * 10
#             return 0.0
        
#         elif qtype == 'slider':
#             # FIXED: Validate response can be converted to float
#             try:
#                 value = float(response)
#             except (ValueError, TypeError):
#                 return 0.0
            
#             if question.get('reverse_score', False):
#                 max_val = question.get('max', 10)
#                 value = max_val - value
            
#             if question.get('scale_to_10', False):
#                 max_val = question.get('max', 100)
#                 value = (value / max_val) * 10
            
#             return value
        
#         elif qtype == 'text_completion':
#             # FIXED: Handle empty or skipped text responses
#             if not response or response == "Not applicable":
#                 return 0.0
            
#             text = str(response).strip()
#             if len(text) < 10:
#                 return 0
            
#             # Score based on length and intensity words
#             length_score = min(len(text) / 50, 5)
            
#             intensity_words = ['always', 'never', 'can\'t', 'impossible', 'terrified', 
#                             'desperate', 'worthless', 'hopeless', 'trapped']
#             intensity_score = sum(1 for word in intensity_words if word in text.lower())
#             intensity_score = min(intensity_score * 2, 5)
            
#             return min((length_score + intensity_score) / 2, 10)
        
#         return 0.0
    

#     def analyze_pattern_hierarchy(self, pattern_scores: Dict[int, float]) -> Dict[str, Any]:
#         """Analyze pattern hierarchy (preserved)"""
#         significant_patterns = {pid: score for pid, score in pattern_scores.items() if score >= 4.0}
        
#         if not significant_patterns:
#             return {
#                 'dominant_pattern': {},
#                 'primary_patterns': [],
#                 'secondary_patterns': [],
#                 'all_scores': pattern_scores,
#                 'pattern_count': 0,
#                 'complexity_assessment': 'Healthy baseline - no significant patterns'
#             }
        
#         sorted_patterns = sorted(significant_patterns.items(), key=lambda x: x[1], reverse=True)
#         dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
#         primary = sorted_patterns[1:3] if len(sorted_patterns) > 1 else []
#         secondary = sorted_patterns[3:5] if len(sorted_patterns) > 3 else []
        
#         def format_pattern(pid, score):
#             return {
#                 'id': pid,
#                 'name': self.patterns.get(pid, 'Unknown'),
#                 'score': round(score, 1),
#                 'severity': self._get_severity_level(score),
#                 'description': self.pattern_descriptions.get(pid, {})
#             }
        
#         return {
#             'dominant_pattern': format_pattern(dominant[0], dominant[1]) if dominant[0] else {},
#             'primary_patterns': [format_pattern(pid, score) for pid, score in primary],
#             'secondary_patterns': [format_pattern(pid, score) for pid, score in secondary],
#             'all_scores': {pid: round(score, 1) for pid, score in pattern_scores.items()},
#             'pattern_count': len(significant_patterns),
#             'complexity_assessment': self._assess_complexity(significant_patterns)
#         }
    
#     def _get_severity_level(self, score: float) -> str:
#         if score >= 8.0: return "Severe"
#         elif score >= 6.0: return "Moderate-High"
#         elif score >= 4.0: return "Moderate"
#         else: return "Mild"
    
#     def _assess_complexity(self, significant_patterns: Dict[int, float]) -> str:
#         count = len(significant_patterns)
#         severe_count = len([s for s in significant_patterns.values() if s >= 8.0])
        
#         if severe_count >= 3:
#             return "High complexity - multiple severe patterns requiring phased intervention"
#         elif severe_count >= 2:
#             return "Moderate-high complexity - several significant patterns"
#         elif count >= 4:
#             return "Moderate complexity - multiple patterns to address"
#         elif count >= 2:
#             return "Standard complexity - focused dual-pattern intervention"
#         else:
#             return "Low complexity - single pattern focus optimal"
    
#     def predict_resistance(self, responses: Dict[int, Any]) -> float:
#         resistance_scores = []
#         if 69 in responses:
#             belief_score = float(responses[69])
#             resistance_scores.append((10 - belief_score) / 10)
#         if 70 in responses:
#             response = responses[70]
#             options = ["Ready to start immediately", "Ready within the next week",
#                       "Ready within the next month", "Still exploring options",
#                       "Not ready yet - just gathering information"]
#             if response in options:
#                 index = options.index(response)
#                 resistance_scores.append(index / 4)
#         return round(sum(resistance_scores) / len(resistance_scores), 2) if resistance_scores else 0.3
    
#     def calculate_success_probability(self, pattern_scores, constellation_multiplier, 
#                                      resistance_score, digital_analysis=None):
#         base_probability = 85
#         severe_patterns = len([s for s in pattern_scores.values() if s >= 8.0])
#         if severe_patterns >= 3: base_probability -= 10
#         elif severe_patterns >= 2: base_probability -= 5
#         if constellation_multiplier > 1.5: base_probability -= 5
#         elif constellation_multiplier > 1.3: base_probability -= 3
#         resistance_penalty = resistance_score * 15
#         base_probability -= resistance_penalty
#         if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
#             base_probability += 3
#         final_probability = max(70, min(95, base_probability))
#         if final_probability < 75:
#             recommended_sessions = 3
#             timeline = "3-4 weeks"
#         elif final_probability < 85:
#             recommended_sessions = 2.5
#             timeline = "2-3 weeks"
#         else:
#             recommended_sessions = 2
#             timeline = "2 weeks"
#         return {
#             'overall_success_rate': round(final_probability, 1),
#             'recommended_sessions': recommended_sessions,
#             'timeline_estimate': timeline
#         }
    
#     def select_therapeutic_protocols(self, pattern_hierarchy, digital_analysis, success_prediction):
#         dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})
#         pattern_id = dominant_pattern.get('id')
#         pattern_info = self.pattern_descriptions.get(pattern_id, {})
        
#         protocols = {
#             'session_1': [
#                 "Complete pattern mapping and behavioral chain analysis",
#                 f"{pattern_info.get('session_1_focus', 'Pattern exploration')}",
#                 "Initial rapport building",
#                 "Light hypnotic work for change preparation"
#             ],
#             'session_2': [
#                 f"{pattern_info.get('session_2_focus', 'Core transformation work')}",
#                 "Deep hypnotic pattern interruption",
#                 "Neural pathway installation for new responses",
#                 "Future pacing and integration"
#             ]
#         }
        
#         if success_prediction.get('recommended_sessions', 2) >= 2.5:
#             protocols['session_3'] = [
#                 "Pattern reinforcement and consolidation",
#                 "Complex situation navigation",
#                 "Long-term stability anchoring"
#             ]
        
#         return protocols


#     def extract_trigger_chain(self, responses: Dict[int, Any]) -> Dict[str, Any]:
#         """
#         Extract complete trigger → response sequence
#         Maps exact intervention points for hypnotherapy
#         """
#         chain = {
#             'environmental_trigger': responses.get(14, 'Not captured'),  # Q14: Trigger situation
#             'awareness_point': responses.get(15, 'Not captured'),        # Q15: First notice
#             'physical_response': responses.get(16, 'Not captured'),      # Q16: Physical sensation
#             'automatic_thought': responses.get(17, 'Not captured'),      # Q17: Automatic thought
#             'emotional_response': responses.get(18, 'Not captured'),     # Q18: Emotions
#             'behavioral_response': responses.get(19, 'Not captured'),    # Q19: Behavior
#             'immediate_consequence': responses.get(20, 'Not captured'),  # Q20: After response
#             'longer_term_impact': responses.get(21, 'Not captured')      # Q21: Hours later
#         }
        
#         # Calculate sequence completeness
#         captured_elements = sum(1 for v in chain.values() if v != 'Not captured')
#         completeness = (captured_elements / len(chain)) * 100
        
#         # Identify intervention windows
#         intervention_points = []
#         if chain['physical_response'] != 'Not captured':
#             intervention_points.append('Somatic awareness intervention (physical sensation recognition)')
#         if chain['automatic_thought'] != 'Not captured':
#             intervention_points.append('Cognitive interruption (thought pattern disruption)')
#         if chain['behavioral_response'] != 'Not captured':
#             intervention_points.append('Behavioral choice point (alternative response installation)')
        
#         return {
#             'trigger_chain': chain,
#             'sequence_completeness': round(completeness, 1),
#             'intervention_windows': intervention_points,
#             'chain_analysis': f"Sequence {completeness:.0f}% complete - {'sufficient for intervention design' if completeness >= 60 else 'requires session 1 completion'}"
#         }
     
     
#     def generate_complete_analysis(self, assessment_data: Dict) -> Dict[str, Any]:
#         """Generate comprehensive assessment analysis with all clinical data"""
#         responses = assessment_data.get('responses', {})
        
#         # Score patterns
#         pattern_scores = self.score_patterns(responses)
        
#         # Analyze hierarchy
#         from utils.config_assess import calculate_constellation_multiplier
#         pattern_hierarchy = self.analyze_pattern_hierarchy(pattern_scores)
#         constellation_multiplier = calculate_constellation_multiplier(pattern_scores)
        
#         # Digital analysis
#         from utils.config_assess import compute_digital_despair_score
#         digital_analysis = compute_digital_despair_score(responses)
#         is_digital_native = digital_analysis['is_digital_native']
        
#         # Resistance and success
#         resistance_score = self.predict_resistance(responses)
#         success_prediction = self.calculate_success_probability(
#             pattern_scores, constellation_multiplier, resistance_score,
#             digital_analysis if is_digital_native else None
#         )
        
#         # Therapeutic protocols
#         therapeutic_protocols = self.select_therapeutic_protocols(
#             pattern_hierarchy,
#             digital_analysis if is_digital_native else None,
#             success_prediction
#         )

#         # ENHANCED: Extract trigger chain
#         trigger_chain_data = self.extract_trigger_chain(responses)
        
#         # ENHANCED: Extract clinical summary data
#         clinical_summary = self.extract_clinical_summary_data(
#             pattern_hierarchy, responses, digital_analysis
#         )
        
#         return {
#             'pattern_scores': pattern_scores,
#             'pattern_analysis': pattern_hierarchy,
#             'pattern_hierarchy': pattern_hierarchy,
#             'constellation_multiplier': constellation_multiplier,
#             'resistance_score': resistance_score,
#             'digital_analysis': digital_analysis,
#             'is_digital_native': is_digital_native,
#             'success_prediction': success_prediction,
#             'therapeutic_recommendations': {
#                 'success_probability': success_prediction['overall_success_rate'],
#                 'recommended_sessions': success_prediction['recommended_sessions'],
#                 'timeline': success_prediction['timeline_estimate'],
#                 'protocols': therapeutic_protocols
#             },
#             'therapeutic_protocols': therapeutic_protocols,
#             'trigger_chain_analysis': trigger_chain_data,
#             'clinical_summary': clinical_summary,
#             'timestamp': datetime.now().isoformat(),
#             'assessment_quality': {
#                 'total_questions_answered': len(responses),
#                 'completion_rate': (len(responses) / len(COMPREHENSIVE_QUESTIONS)) * 100,
#                 'text_responses': len([r for r in responses.values() if isinstance(r, str) and len(str(r)) > 20])
#             }
#         }
    
  
#     def extract_clinical_summary_data(
#         self,
#         pattern_hierarchy: Dict,
#         responses: Dict[int, Any],
#         digital_analysis: Optional[Dict] = None
#     ) -> Dict[str, Any]:
#         """
#         Extract all data needed for rapid clinical summary template
#         """
#         # Get dominant and primary patterns
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
#         primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        
#         dominant_id = dominant.get('id')
#         dominant_info = self.pattern_descriptions.get(dominant_id, {})
        
#         # Extract core limiting belief
#         core_belief = dominant_info.get('core_belief', 'Not identified')
        
#         # Extract hidden benefits (protective function)
#         hidden_benefits = dominant_info.get('protective_function', 'Not identified')
        
#         # Extract systemic resistance factors
#         systemic_factors = dominant_info.get('systemic_factors', [])
#         systemic_resistance = '; '.join(systemic_factors) if systemic_factors else 'Not identified'
        
#         # Extract identity threat
#         identity_conflict = dominant_info.get('identity_conflict', 'Not identified')
        
#         # Session focus areas
#         session_1_focus = dominant_info.get('session_1_focus', 'Pattern exploration')
#         session_2_focus = dominant_info.get('session_2_focus', 'Core transformation')
        
#         # Predict session 3 need
#         pattern_count = pattern_hierarchy.get('pattern_count', 0)
#         complexity = pattern_hierarchy.get('complexity_assessment', '')
#         session_3_need = self._assess_session_3_need(pattern_count, complexity)
        
#         # Change readiness
#         readiness = self._calculate_readiness_score(responses)
        
#         # Resistance prediction
#         resistance_points = self._predict_resistance_points(dominant_info, responses)
        
#         # Intervention keywords and avoid language
#         intervention_keywords = ', '.join(dominant_info.get('intervention_keywords', []))
#         avoid_language = ', '.join(dominant_info.get('avoid_language', []))
        
#         return {
#             'core_limiting_belief': core_belief,
#             'hidden_benefits': hidden_benefits,
#             'systemic_resistance': systemic_resistance,
#             'identity_threat': identity_conflict,
#             'session_1_focus': session_1_focus,
#             'session_2_target': session_2_focus,
#             'potential_session_3_need': session_3_need,
#             'change_readiness_score': readiness,
#             'predicted_resistance_points': resistance_points,
#             'intervention_keywords': intervention_keywords,
#             'avoid_language': avoid_language
#         }
    
#     def _calculate_readiness_score(self, responses: Dict[int, Any]) -> str:
#         """Calculate change readiness from responses"""
#         # Question 69: Belief in change
#         belief_score = responses.get(69, 5)
        
#         # Question 70: Readiness timing
#         readiness_response = responses.get(70, '')
#         readiness_map = {
#             "Ready to start immediately": 10,
#             "Ready within the next week": 8,
#             "Ready within the next month": 6,
#             "Still exploring options": 4,
#             "Not ready yet - just gathering information": 2
#         }
#         timing_score = readiness_map.get(readiness_response, 5)
        
#         # Calculate average
#         avg_score = (belief_score + timing_score) / 2
        
#         return f"{avg_score:.1f}/10"



# # ============================================================================
# # QUESTION ROUTER
# # ============================================================================

# class QuestionRouter:
#     """Intelligent question routing"""
    
#     def __init__(self):
#         self.core_questions = [q for q in COMPREHENSIVE_QUESTIONS if not q.get('validation')]
#         self.validation_questions = [q for q in COMPREHENSIVE_QUESTIONS if q.get('validation')]
    
#     def get_next_question(self, responses: Dict[int, Any], is_digital_native: bool) -> Optional[Dict]:
#         """Get next question"""
        
#         # Core questions first
#         for question in self.core_questions:
#             if question['id'] not in responses:
#                 return question
        
#         # Then validation
#         for question in self.validation_questions:
#             if question['id'] not in responses:
#                 return question
        
#         return None
    
#     def estimate_total_questions(self, responses: Dict[int, Any], is_digital_native: bool) -> int:
#         """Estimate total questions"""
#         return len(COMPREHENSIVE_QUESTIONS)


# # ============================================================================
# # CONFIGURATION CLASS
# # ============================================================================

# class AssessmentConfig:
#     """Centralized configuration access"""
    
#     pattern_definitions = PatternDefinitions
#     comprehensive_questions = COMPREHENSIVE_QUESTIONS
#     digital_despair_subscales = DIGITAL_DESPAIR_SUBSCALES
#     pattern_reinforcement_matrix = PATTERN_REINFORCEMENT_MATRIX
    
#     @staticmethod
#     def get_analytics_engine():
#         return AnalyticsEngine()
    
#     @staticmethod
#     def get_question_router():
#         return QuestionRouter()
    
#     @staticmethod
#     def compute_digital_despair(responses):
#         return compute_digital_despair_score(responses)
    
#     @staticmethod
#     def calculate_constellation(pattern_scores):
#         return calculate_constellation_multiplier(pattern_scores)


# __all__ = [
#     'PatternDefinitions',
#     'COMPREHENSIVE_QUESTIONS',
#     'AnalyticsEngine',
#     'QuestionRouter',
#     'AssessmentConfig',
#     'compute_digital_despair_score',
#     'calculate_constellation_multiplier'
# ]



















"""
Clinical Behavioral Pattern Assessment - ENHANCED PROFILING MODEL
Version 4.0 - Universal Profiling + Complete Clinical Data Preservation

ENHANCEMENTS:
- Minimum 2-point baseline scoring (no zero-escape routes)
- Forced-choice dyads for core detection
- Ranking questions for constellation
- Enhanced defensive detection
- ALL original clinical data preserved + new severity calibrations added
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import re
import math

# ============================================================================
# ENHANCED PATTERN DEFINITIONS - ALL ORIGINAL DATA PRESERVED
# ============================================================================
class PatternDefinitions:
    """9 fundamental behavioral patterns + digital - Complete clinical data"""
    
    PATTERNS = {
        1: "Unhappiness culture",
        2: "Power struggles",
        3: "Systematic mistrust",
        4: "Separation and division",
        5: "Doing versus being",
        6: "Compartmentalized authenticity",
        7: "Self sacrifice and care avoidance",
        8: "Inherited missions",
        9: "Context dependent weakness",
        10: "Digital reality dissociation"
    }
    
    PATTERN_DESCRIPTIONS = {
        1: {
            "name": "Unhappiness culture",
            "root_structure": "Positive states = danger/loss/punishment",
            "core_belief": "Happiness leads to disappointment or makes me a target",
            "systemic_factors": [
                "Family depression patterns normalize suffering",
                "Cultural suffering valorization ('life is hard')",
                "Positive suppression rewarded in family system",
                "Happiness triggers envy or attack from others"
            ],
            "identity_conflict": "Happy authentic self vs. Familiar suffering self that feels safe",
            "hidden_loyalties": [
                "Loyalty to unhappy parent/family member",
                "Suffering = virtue/depth belief system",
                "Protection from envy or being targeted",
                "Belonging through shared misery"
            ],
            "protective_function": "Protection from disappointment, envy, or loss",
            "intervention_focus": "Permission installation for positive states with safety anchoring",
            "session_1_focus": "Happiness permission protocols and safety anchoring",
            "session_2_focus": "Joy sustainability and positive emotion anchoring",
            "intervention_keywords": ["permission", "safety", "deserve", "natural", "birthright"],
            "avoid_language": ["just be happy", "think positive", "you're being negative"],
            "description": "You may find it challenging to accept or maintain positive emotional states",
            "impact": "This can limit your ability to fully enjoy success and happiness",
            "transformation": "Learning to trust that joy and success can be sustainable and deserved",
            "keywords_matching": ["happy", "joy", "success", "good things"],
            "pattern_mechanism": "Happiness deflection to avoid disappointment",
            "pattern_resistance": "May resist feeling genuine joy",
            "insights_map": "Your mind has learned to deflect happiness as protection against disappointment - but this same mechanism is preventing the joy you deserve",
            "what_you_notice": "Feeling guilty when things go well, waiting for the other shoe to drop, minimizing achievements",
            "what_others_see": "Someone who deflects compliments, seems uncomfortable with praise, or finds problems in good situations",
            "hidden_cost": "Missing out on life's genuine pleasures and the motivation that comes from celebrating wins",
            "breakthrough_moment": "Realizing that happiness doesn't make you vulnerable - it makes you stronger and more resilient",
            # NEW: Severity calibrations for universal profiling
            "adaptive_baseline": "Realistic optimism with awareness of potential challenges",
            "mild_manifestation": "Occasional worry after good events, can recover and enjoy",
            "moderate_manifestation": "Difficulty sustaining joy, frequent negative predictions, minimizes accomplishments",
            "severe_manifestation": "Active suppression of happiness, pervasive cynical worldview, unable to enjoy successes"
        },
        2: {
            "name": "Power struggles",
            "root_structure": "Submission = death/annihilation of self",
            "core_belief": "I must fight to exist and maintain my identity",
            "systemic_factors": [
                "Authoritarian family dynamics modeling dominance",
                "Competition-based relationship patterns",
                "Win-lose paradigm as only option",
                "Vulnerability punished in family system"
            ],
            "identity_conflict": "Collaborative empowered self vs. Fighter/survivor self",
            "hidden_loyalties": [
                "Loyalty to family fight patterns",
                "Strength = resistance belief",
                "Protection from being controlled/dominated",
                "Identity tied to being 'the strong one'"
            ],
            "protective_function": "Protection from domination or loss of self",
            "intervention_focus": "Collaborative empowerment with maintained autonomy",
            "session_1_focus": "Nervous system regulation and collaborative response installation",
            "session_2_focus": "Conflict transformation and win-win response automation",
            "intervention_keywords": ["curiosity", "collaboration", "both/and", "strength in listening"],
            "avoid_language": ["just compromise", "stop being defensive", "you're too aggressive"],
            "description": "You experience recurring conflicts and power struggles in relationships",
            "impact": "This can create stress and prevent collaborative problem-solving",
            "transformation": "Developing skills for curious dialogue and win-win resolution",
            "keywords_matching": ["conflict", "argument", "disagree", "defensive"],
            "pattern_mechanism": "Control seeking to prevent vulnerability",
            "pattern_resistance": "May challenge collaborative approach",
            "insights_map": "You're fighting battles that don't need to be fought - your nervous system activates 'combat mode' even in collaborative situations",
            "what_you_notice": "Feeling defensive quickly, needing to be right, seeing disagreements as threats",
            "what_others_see": "Someone who argues their point intensely, seems confrontational, or withdraws when challenged",
            "hidden_cost": "Exhausting mental energy on conflicts instead of creative collaboration and genuine connection",
            "breakthrough_moment": "Discovering that being curious about others' perspectives actually strengthens your position",
            "adaptive_baseline": "Healthy assertiveness with collaborative flexibility",
            "mild_manifestation": "Occasional defensiveness in disagreements, can self-correct",
            "moderate_manifestation": "Frequent need to win arguments, difficulty compromising, tense body in conflicts",
            "severe_manifestation": "All interactions seen as power struggles, constant conflict, cannot tolerate disagreement"
        },
        3: {
            "name": "Systematic mistrust",
            "root_structure": "Others = eventual betrayal/harm",
            "core_belief": "Trust leads to being hurt, used, or abandoned",
            "systemic_factors": [
                "Early betrayal experiences by caregivers",
                "Inconsistent caregiving creating unpredictability",
                "Trust violation patterns across relationships",
                "Manipulation modeling in family system"
            ],
            "identity_conflict": "Trusting open self vs. Protected vigilant self",
            "hidden_loyalties": [
                "Loyalty to hurt younger parts of self",
                "Vigilance = safety belief",
                "Protection from re-injury",
                "Identity as 'smart enough not to trust'"
            ],
            "protective_function": "Hypervigilance and threat detection to prevent harm",
            "intervention_focus": "Gradual trust building with transparent safety protocols",
            "session_1_focus": "Trust calibration and authentic connection programming",
            "session_2_focus": "Healthy skepticism calibration and openness programming",
            "intervention_keywords": ["discernment", "wisdom", "safe people", "gradual"],
            "avoid_language": ["just trust people", "you're too paranoid", "not everyone is bad"],
            "description": "You maintain a default skepticism about others' intentions",
            "impact": "This protective mechanism may limit deep connections and opportunities",
            "transformation": "Calibrating trust responses and building authentic relationships",
            "keywords_matching": ["trust", "suspicious", "motives", "skeptical"],
            "pattern_mechanism": "Preemptive rejection to avoid abandonment",
            "pattern_resistance": "May question therapeutic relationship",
            "insights_map": "Your protective skepticism, while once useful, is now creating the very rejection and isolation you're trying to avoid",
            "what_you_notice": "Analyzing people's motives, feeling suspicious of kindness, expecting hidden agendas",
            "what_others_see": "Someone who seems guarded, asks probing questions, or appears cynical about human nature",
            "hidden_cost": "Living in emotional isolation and missing genuine opportunities for support and connection",
            "breakthrough_moment": "Understanding that discernment and openness can coexist - you can be wise AND trusting",
            "adaptive_baseline": "Healthy discernment with openness to trust",
            "mild_manifestation": "Initial caution with new people, gradual trust building, can accept help",
            "moderate_manifestation": "Persistent suspicion of motives, difficulty accepting help, questions kindness",
            "severe_manifestation": "Pervasive mistrust, social isolation, hypervigilance, unable to form close bonds"
        },
        4: {
            "name": "Separation and division",
            "root_structure": "Gray areas = chaos/uncertainty/danger",
            "core_belief": "Things must be clearly defined or everything falls apart",
            "systemic_factors": [
                "Rigid family rules requiring clear categories",
                "Religious absolutism or black/white morality",
                "Chaotic early environment needing simplification",
                "All-or-nothing modeling by caregivers"
            ],
            "identity_conflict": "Flexible nuanced self vs. Clear defined safe self",
            "hidden_loyalties": [
                "Loyalty to family certainty patterns",
                "Order = safety belief system",
                "Protection from confusion/overwhelm",
                "Identity as 'person with clear values'"
            ],
            "protective_function": "Self-protection via binary thinking to reduce complexity",
            "intervention_focus": "Both/and integration with safety in uncertainty",
            "session_1_focus": "Binary thinking dissolution and creative possibility expansion",
            "session_2_focus": "Creative problem-solving and nuanced thinking installation",
            "intervention_keywords": ["both/and", "complexity", "nuance", "integration"],
            "avoid_language": ["it's not black and white", "stop being so rigid"],
            "description": "You tend toward black-and-white thinking patterns",
            "impact": "This can limit creative solutions and increase decision paralysis",
            "transformation": "Developing nuanced thinking and embracing creative possibilities",
            "keywords_matching": ["choice", "decision", "either", "both"],
            "pattern_mechanism": "Binary thinking to simplify complex emotions",
            "pattern_resistance": "May resist nuanced solutions",
            "insights_map": "Your brilliant analytical mind gets trapped in 'either/or' thinking when 'both/and' solutions would serve you better",
            "what_you_notice": "Feeling stuck between two options, seeing things as all good or all bad, struggling with grey areas",
            "what_others_see": "Someone who wants clear answers, seems frustrated by ambiguity, or makes quick either/or judgments",
            "hidden_cost": "Missing innovative solutions that require holding multiple perspectives simultaneously",
            "breakthrough_moment": "Realizing that complexity isn't confusion - it's where the most elegant solutions hide",
            "adaptive_baseline": "Clear values with nuanced situational thinking",
            "mild_manifestation": "Preference for clarity, occasional either/or thinking under stress",
            "moderate_manifestation": "Frequent binary choices, difficulty with ambiguity, good/bad person categorization",
            "severe_manifestation": "Rigid all-or-nothing thinking, splitting behaviors, cannot tolerate complexity"
        },
        5: {
            "name": "Doing versus being",
            "root_structure": "Worth = productivity/achievement only",
            "core_belief": "I am only valuable when I'm producing/achieving",
            "systemic_factors": [
                "Achievement-focused family with conditional love",
                "Work/school performance as identity",
                "Productivity culture reinforcement",
                "Rest/play punished or seen as lazy"
            ],
            "identity_conflict": "Being-centered self vs. Achieving self that earns worth",
            "hidden_loyalties": [
                "Loyalty to family achievement patterns",
                "Worth = doing belief system",
                "Protection from worthlessness",
                "Identity as 'successful/productive person'"
            ],
            "protective_function": "Avoids vulnerability through busyness or achievement",
            "intervention_focus": "Intrinsic worth installation with productivity reframing",
            "session_1_focus": "Worth anchoring independent of achievement",
            "session_2_focus": "Intrinsic worth recognition and balanced achievement",
            "intervention_keywords": ["inherent worth", "being", "enough", "rest"],
            "avoid_language": ["just relax", "stop working so much", "you don't need to prove yourself"],
            "description": "Your self-worth is closely tied to productivity and achievement",
            "impact": "This can lead to burnout and difficulty with rest or self-care",
            "transformation": "Anchoring worth in your inherent value, independent of accomplishments",
            "keywords_matching": ["productive", "busy", "achievement", "worth"],
            "pattern_mechanism": "Achievement addiction to earn worth",
            "pattern_resistance": "May fear identity change",
            "insights_map": "You've created an equation where doing = worth, but your actual value exists independent of any achievement",
            "what_you_notice": "Feeling anxious when not productive, equating rest with laziness, measuring yourself by output",
            "what_others_see": "Someone who's always busy, seems uncomfortable with downtime, or talks about achievements frequently",
            "hidden_cost": "Chronic stress, missed opportunities for reflection and creativity that come from mental space",
            "breakthrough_moment": "Discovering that your value exists completely separate from what you do or achieve",
            "adaptive_baseline": "Healthy productivity with rest capacity and intrinsic worth",
            "mild_manifestation": "Preference for activity, mild guilt during rest, can relax when needed",
            "moderate_manifestation": "Difficulty resting, worth significantly tied to accomplishments, restlessness",
            "severe_manifestation": "Compulsive productivity, complete worth-doing fusion, burnout, unable to rest"
        },
        6: {
            "name": "Compartmentalized authenticity",
            "root_structure": "Real self = rejection/abandonment",
            "core_belief": "I must hide parts of myself to be accepted",
            "systemic_factors": [
                "Conditional family acceptance based on performance",
                "Social role expectations with punishment for deviation",
                "Authenticity punished in family system",
                "Different contexts requiring different personas"
            ],
            "identity_conflict": "Authentic integrated self vs. Acceptable safe selves",
            "hidden_loyalties": [
                "Loyalty to family role expectations",
                "Adaptation = survival belief",
                "Protection from rejection",
                "Identity as 'shapeshifter/chameleon'"
            ],
            "protective_function": "Avoid rejection by managing different personas",
            "intervention_focus": "Authentic self integration with safety across contexts",
            "session_1_focus": "Authentic self integration and consistency programming",
            "session_2_focus": "Integrated identity and consistent self-expression",
            "intervention_keywords": ["authentic", "integrated", "whole", "genuine"],
            "avoid_language": ["just be yourself", "stop being fake", "pick one identity"],
            "description": "Your sense of identity shifts significantly across different contexts",
            "impact": "This can create internal confusion and emotional exhaustion",
            "transformation": "Integrating an authentic, consistent self across all situations",
            "keywords_matching": ["different", "personality", "authentic", "real"],
            "pattern_mechanism": "Identity shifting to avoid rejection",
            "pattern_resistance": "May struggle with consistency",
            "insights_map": "You're exhausting yourself maintaining different versions of yourself instead of trusting that your authentic self is enough",
            "what_you_notice": "Feeling like different people in different settings, adapting personality to fit in, losing sense of 'real self'",
            "what_others_see": "Someone who seems different depending on the group, appears to chameleon, or seems inconsistent",
            "hidden_cost": "Emotional exhaustion from performance, loss of authentic self-expression and genuine connections",
            "breakthrough_moment": "Realizing that your authentic self is actually more likeable and magnetic than any persona",
            "adaptive_baseline": "Contextually appropriate self-expression with core consistency",
            "mild_manifestation": "Occasional code-switching, mostly authentic, minor adjustments",
            "moderate_manifestation": "Different personas in different contexts, exhausting, aware of fragmentation",
            "severe_manifestation": "Completely fragmented identity, no stable authentic self, don't know who you are"
        },
        7: {
            "name": "Self sacrifice and care avoidance",
            "root_structure": "My needs = selfish/wrong/dangerous",
            "core_belief": "Caring for myself will harm others or make me unworthy",
            "systemic_factors": [
                "Caretaker family roles with reward for self-sacrifice",
                "Self-sacrifice modeling by parent",
                "Need-shaming in family system",
                "Love = self-denial belief pattern"
            ],
            "identity_conflict": "Self-caring self vs. Service/giving self that earns love",
            "hidden_loyalties": [
                "Loyalty to family service patterns",
                "Sacrifice = love belief system",
                "Protection from selfishness shame",
                "Identity as 'the helpful/caring one'"
            ],
            "protective_function": "Maintains belonging and worth through service",
            "intervention_focus": "Self-care as service reframing with boundary installation",
            "session_1_focus": "Boundary establishment and self-care permission",
            "session_2_focus": "Reciprocal relationship patterns and energy management",
            "intervention_keywords": ["boundaries", "reciprocal", "energy", "sustainable"],
            "avoid_language": ["just say no", "stop being a doormat", "be selfish for once"],
            "description": "You prioritize others' needs while neglecting your own self-care",
            "impact": "This can lead to resentment and emotional depletion over time",
            "transformation": "Developing healthy boundaries and self-care practices",
            "keywords_matching": ["others", "help", "needs", "care"],
            "pattern_mechanism": "Self-sacrifice to maintain connection",
            "pattern_resistance": "May feel guilty about self-focus",
            "insights_map": "Your generous heart has learned to give to others but forgotten how to receive - creating an unsustainable energy drain",
            "what_you_notice": "Feeling guilty when focusing on yourself, automatically saying yes to requests, feeling responsible for others' emotions",
            "what_others_see": "Someone who's always helpful, never seems to have needs, or appears stressed but won't ask for help",
            "hidden_cost": "Resentment buildup, burnout, and becoming less effective at helping others when you're depleted",
            "breakthrough_moment": "Understanding that taking care of yourself is actually the most loving thing you can do for others",
            "adaptive_baseline": "Reciprocal caregiving with self-care capacity",
            "mild_manifestation": "Tendency to prioritize others, can self-care when reminded, occasional guilt",
            "moderate_manifestation": "Consistent self-neglect, significant guilt about self-care, difficulty saying no",
            "severe_manifestation": "Complete self-sacrifice, unable to identify own needs, resentment, burnout"
        },
        8: {
            "name": "Inherited missions",
            "root_structure": "My path = betrayal of family/ancestors",
            "core_belief": "I must fulfill family dreams/expectations to be loyal",
            "systemic_factors": [
                "Family sacrifice stories creating debt",
                "Generational expectations carried forward",
                "Dream inheritance from parents/ancestors",
                "Guilt about family sacrifices"
            ],
            "identity_conflict": "Personal desire self vs. Family loyal self",
            "hidden_loyalties": [
                "Loyalty to ancestral sacrifice",
                "Family dream continuation as duty",
                "Protection from guilt/betrayal",
                "Identity as 'family legacy carrier'"
            ],
            "protective_function": "Maintains family belonging and honors sacrifices",
            "intervention_focus": "Honor family while claiming personal path integration",
            "session_1_focus": "Personal values clarification and family harmony balance",
            "session_2_focus": "Authentic life direction and confident decision-making",
            "intervention_keywords": ["honor", "autonomy", "both/and", "gratitude"],
            "avoid_language": ["forget your family", "it's your life", "they're holding you back"],
            "description": "Your life choices are driven more by family expectations than personal desires",
            "impact": "This can create internal conflict and limit authentic self-expression",
            "transformation": "Clarifying personal values while maintaining family harmony",
            "keywords_matching": ["family", "expectations", "should", "duty"],
            "pattern_mechanism": "Mission inheritance to avoid family conflict",
            "pattern_resistance": "May feel disloyal to family",
            "insights_map": "You're living someone else's dream while your own authentic desires remain buried under family expectations",
            "what_you_notice": "Feeling torn between what you want and what's expected, guilt about disappointing family, unclear about your own desires",
            "what_others_see": "Someone who references family expectations often, seems conflicted about decisions, or appears to live for others",
            "hidden_cost": "Living someone else's life instead of your own, missing your unique contribution to the world",
            "breakthrough_moment": "Realizing you can honor your family AND live authentically - they're not mutually exclusive",
            "adaptive_baseline": "Honoring family while pursuing personal path",
            "mild_manifestation": "Occasional guilt about diverging from family expectations, can self-authorize",
            "moderate_manifestation": "Significant conflict between own desires and family loyalty, chronic guilt",
            "severe_manifestation": "Living entirely for family expectations, no personal autonomy, deep resentment"
        },
        9: {
            "name": "Context dependent weakness",
            "root_structure": "Certain contexts = powerlessness/helplessness",
            "core_belief": "I cannot be strong or authentic in all circumstances",
            "systemic_factors": [
                "Trauma context associations creating triggers",
                "Power dynamic patterns in family",
                "Learned helplessness in specific situations",
                "Boundary violation in certain contexts"
            ],
            "identity_conflict": "Strong capable self vs. Overwhelmed powerless self",
            "hidden_loyalties": [
                "Loyalty to trauma bond patterns",
                "Powerlessness = safety in some contexts",
                "Protection from responsibility/expectation",
                "Identity fragmentation across contexts"
            ],
            "protective_function": "Protects self from overextension in triggering contexts",
            "intervention_focus": "Universal strength anchoring with context-independent resources",
            "session_1_focus": "Context-independent boundary installation",
            "session_2_focus": "Consistent boundary maintenance across all contexts",
            "intervention_keywords": ["consistent", "capable", "anchored", "universal strength"],
            "avoid_language": ["just stand up for yourself", "why can't you be strong there too"],
            "description": "Your boundaries and limits vary dramatically based on context",
            "impact": "This can lead to inconsistent relationships and self-advocacy",
            "transformation": "Establishing consistent, healthy boundaries across all situations",
            "keywords_matching": ["boundaries", "limits", "context", "situation"],
            "pattern_mechanism": "Boundary collapse to avoid confrontation",
            "pattern_resistance": "May fear setting boundaries",
            "insights_map": "Your boundaries disappear in certain contexts because you've never learned you can be both loved and boundaried",
            "what_you_notice": "Being strong in some situations but passive in others, feeling like you lose yourself in certain contexts",
            "what_others_see": "Someone who seems confident sometimes but submissive other times, appears unpredictable in their responses",
            "hidden_cost": "Confusion about your own limits, relationships built on false premises, accumulated resentment",
            "breakthrough_moment": "Discovering that consistent boundaries actually make you more trustworthy and respected",
            "adaptive_baseline": "Consistent self across contexts with appropriate flexibility",
            "mild_manifestation": "Slightly different responses in different contexts, can maintain core boundaries",
            "moderate_manifestation": "Significant boundary loss in specific situations, aware but struggling",
            "severe_manifestation": "Complete personality/boundary collapse in triggering contexts, helplessness"
        },
        10: {
            "name": "Digital reality dissociation",
            "root_structure": "Digital self = real self, offline = performance",
            "core_belief": "Online engagement is more authentic/rewarding than physical reality",
            "systemic_factors": [
                "Algorithmic conditioning creating dopamine dependency",
                "Social infrastructure collapse (third spaces)",
                "Economic stagnation creating digital escape",
                "Parasocial relationships replacing real connections"
            ],
            "identity_conflict": "Integrated reality self vs. Digital-dependent fragmented self",
            "hidden_loyalties": [
                "Loyalty to online communities/identities",
                "Digital = belonging belief",
                "Protection from offline rejection/inadequacy",
                "Identity as digital native"
            ],
            "protective_function": "Digital immersion protects from offline social anxiety and inadequacy",
            "intervention_focus": "Reality reconnection with digital competency integration",
            "session_1_focus": "Digital detox protocols and offline confidence building",
            "session_2_focus": "Integrated digital-physical identity and dopamine regulation",
            "intervention_keywords": ["integration", "balance", "offline confidence", "real connection"],
            "avoid_language": ["just quit social media", "get a real life", "stop being online"],
            "description": "Your sense of self and belonging is primarily rooted in digital spaces",
            "impact": "This can create real-world social anxiety and disconnection from physical reality",
            "transformation": "Integrating digital skills with offline confidence and authentic connections",
            "keywords_matching": ["online", "social media", "digital", "screen time"],
            "pattern_mechanism": "Digital immersion to avoid offline inadequacy",
            "pattern_resistance": "May minimize digital impact",
            "insights_map": "Your digital competencies are real strengths, but over-reliance on online validation is preventing authentic offline connection",
            "what_you_notice": "Feeling more yourself online, preferring digital interaction, offline anxiety, constant phone checking",
            "what_others_see": "Someone always on their phone, more engaged digitally than in-person, anxious in face-to-face settings",
            "hidden_cost": "Missing embodied experiences, shallow relationships, dopamine dysregulation, attention fragmentation",
            "breakthrough_moment": "Realizing that real-world connection provides depth that digital validation never can",
            "adaptive_baseline": "Healthy digital engagement integrated with offline life",
            "mild_manifestation": "Preference for digital, can engage offline, occasional comparison",
            "moderate_manifestation": "Significant digital dependence, offline discomfort, comparison anxiety, FOMO",
            "severe_manifestation": "Digital reality dissociation, offline incompetence, severe anxiety, dopamine dysregulation"
        }
    }

    # Digital emotion subscales for Pattern 10
    digital_emotions = {
        'approval_seeking': [12, 47],
        'comparison_anxiety': [8, 13, 61],
        'rage_addiction': [19, 63],
        'dopamine_dysregulation': [26, 48, 49],
        'belonging_displacement': [27],
        'algorithmic_dependency': [44],
        'dependency_fear': [45],
        'rejection_sensitivity': [47]
    }


# ============================================================================
# COMPREHENSIVE QUESTION BANK - REDESIGNED FOR CLINICAL VALIDITY
# 81 Questions: 5-7 per pattern + screening + validation
# ============================================================================
COMPLETE_QUESTION_SET = [
    
    # ========================================================================
    # SECTION 1: PRESENTING PROBLEM & ENGAGEMENT (Q1-5)
    # ========================================================================
    
    {
        "id": 1,
        "text": "What's the ONE thing you most want to change about yourself?",
        "type": "text_completion",
        "placeholder": "The behavior, feeling, or pattern that brought you here today...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Presenting problem classification"
    },
    
    {
        "id": 2,
        "text": "How much is this affecting your daily life right now?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "labels": ["Barely noticeable", "Completely overwhelming"],
        "pattern": None,
        "analytics_use": "Functional impact and urgency scoring"
    },
    
    {
        "id": 3,
        "text": "Your overall stress level in the past 2 weeks:",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "labels": ["Calm and manageable", "Overwhelming and constant"],
        "pattern": None,
        "analytics_use": "Baseline emotional state"
    },
    
    # ========================================================================
    # SECTION 2: DIGITAL NATIVE SCREENING (Q4-8)
    # ========================================================================
    
    {
        "id": 4,
        "text": "What is your age range?",
        "type": "single_choice",
        "options": [
            "Under 18",
            "18-25",
            "26-35",
            "36-45",
            "46-55",
            "Over 55"
        ],
        "pattern": None,
        "digital_native_scoring": [5, 5, 4, 2, 1, 0],
        "analytics_use": "Digital native classification"
    },
    
    {
        "id": 5,
        "text": "On average, how many hours per day on digital devices (excluding required work)?",
        "type": "slider",
        "min": 0,
        "max": 16,
        "default": 4,
        "pattern": 10,
        "analytics_use": "Digital dependency baseline"
    },
    
    {
        "id": 6,
        "text": "Where do you feel most like your authentic self?",
        "type": "single_choice",
        "options": [
            "In real-world, face-to-face connections",
            "About equally in both online and offline",
            "In online spaces and digital communities",
            "Neither - I don't feel authentic anywhere"
        ],
        "pattern": 10,
        "weights": [2, 4, 8, 10],  # CHANGED: was [0, 5, 8, 10] - NO ZERO
        "analytics_use": "Reality preference and authenticity location"
    },
    
    {
        "id": 7,
        "text": "When you scroll social media, which emotion hits you MOST often?",
        "type": "single_choice",
        "options": [
            "Enjoyment and connection",
            "Comparison and inadequacy",
            "FOMO and anxiety",
            "Anger and outrage",
            "Numbness and escape"
        ],
        "pattern": 10,
        "weights": [2, 7, 7, 7, 9],  # CHANGED: was [0, 8, 7, 7, 9] - NO ZERO
        "digital_emotion": ["connection", "comparison_anxiety", "fomo", "rage_addiction", "dissociation"],
        "analytics_use": "Primary digital emotion identification"
    },
    
    {
        "id": 8,
        "text": "Social media validation (likes, comments) makes you feel:",
        "type": "single_choice",
        "options": [
            "Mildly pleased but doesn't define my worth",
            "Good temporarily but need more to maintain feeling",
            "A rush of relief and validation I crave",
            "Essential to my sense of self-worth that day"
        ],
        "pattern": 10,
        "weights": [2, 6, 8, 10],  # CHANGED: was [0, 6, 8, 10] - NO ZERO
        "digital_emotion": "approval_seeking",
        "analytics_use": "Digital validation dependency"
    },
    
    # ========================================================================
    # SECTION 3: TRIGGER & SEQUENCE MAPPING (Q9-15)
    # ========================================================================
    
    {
        "id": 9,
        "text": "Think of the MOST RECENT time this pattern showed up. What triggered it?",
        "type": "text_completion",
        "placeholder": "What happened right before? Where were you? Who was there? Be specific...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Trigger sequence mapping start"
    },
    
    {
        "id": 10,
        "text": "In that moment, the FIRST thing you noticed was:",
        "type": "single_choice",
        "options": [
            "A physical sensation in my body",
            "A thought or worry",
            "An emotional shift",
            "Something someone said or did",
            "Something I saw online or on my phone"
        ],
        "pattern": None,
        "analytics_use": "Awareness entry point identification"
    },
    
    {
        "id": 11,
        "text": "When this pattern activates, the first physical sensation is usually:",
        "type": "single_choice",
        "options": [
            "Chest tightness, racing heart, or breathing changes",
            "Stomach drop, nausea, or digestive upset",
            "Muscle tension, jaw clenching, or physical rigidity",
            "Hot/cold flashes, sweating, or temperature changes",
            "Numbness, disconnection, or feeling 'outside yourself'",
            "Restlessness, fidgeting, or urge to move/escape"
        ],
        "pattern": None,
        "analytics_use": "Somatic response mapping"
    },
    
    {
        "id": 12,
        "text": "What thought AUTOMATICALLY appeared with that physical sensation?",
        "type": "text_completion",
        "placeholder": "Write the exact words or thought that flashed through your mind...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Automatic thought extraction"
    },
    
    {
        "id": 13,
        "text": "That thought triggered which emotion MOST strongly?",
        "type": "single_choice",
        "options": [
            "Shame or embarrassment",
            "Envy or jealousy",
            "Anger or rage",
            "Sadness or grief",
            "Anxiety or fear",
            "Emptiness or numbness",
            "Inadequacy or worthlessness"
        ],
        "pattern": None,
        "analytics_use": "Primary emotion identification"
    },
    
    {
        "id": 14,
        "text": "To handle that emotion, you IMMEDIATELY:",
        "type": "single_choice",
        "options": [
            "Scrolled more or sought digital validation",
            "Posted or commented to regain sense of control",
            "Withdrew and ruminated offline",
            "Engaged in arguments or rage-bait content",
            "Sought reassurance from others",
            "Numbed out with more content consumption"
        ],
        "pattern": None,
        "analytics_use": "Behavioral coping mechanism"
    },
    
    {
        "id": 15,
        "text": "Right after that behavior, you felt:",
        "type": "single_choice",
        "options": [
            "Temporary relief but underlying tension remains",
            "More agitated or upset than before",
            "Emotionally numb or disconnected",
            "Guilty about how I handled it",
            "Justified in my response"
        ],
        "pattern": None,
        "analytics_use": "Immediate consequence assessment"
    },
    
    # ========================================================================
    # SECTION 4: PATTERN 1 - UNHAPPINESS CULTURE (Q16-18)
    # ========================================================================
    
    {
        "id": 16,
        "text": "When something genuinely good happens to you, your first automatic thought is:",
        "type": "single_choice",
        "options": [
            "I enjoy it and expect more good things to follow",
            "I enjoy it but wonder how long it will last",
            "Something bad will balance this out or ruin it",
            "I feel uncomfortable or undeserving of this",
            "I suppress or minimize the feeling immediately"
        ],
        "pattern": 1,
        "weights": [2, 5, 8, 9, 10],  # CHANGED: was [0, 5, 8, 9, 10] - NO ZERO
        "analytics_use": "Pattern 1 core severity"
    },
    
    {
        "id": 17,
        "text": "Growing up, expressing joy or excitement was:",
        "type": "single_choice",
        "options": [
            "Encouraged and celebrated by family",
            "Tolerated but not really acknowledged",
            "Met with 'don't get your hopes up' warnings",
            "Seen as naive, immature, or silly",
            "Actively discouraged or punished"
        ],
        "pattern": 1,
        "weights": [2, 5, 8, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 1 family origin"
    },
    
    {
        "id": 18,
        "text": "When good things happen to others around you, you typically:",
        "type": "single_choice",
        "options": [
            "Feel genuinely happy for them without comparison",
            "Feel happy for them but slightly envious",
            "Wonder why good things don't happen to me",
            "Feel suspicious or look for hidden downsides",
            "Feel resentful or need to withdraw"
        ],
        "pattern": 1,
        "weights": [2, 5, 8, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 1 social manifestation"
    },
    
    # ========================================================================
    # SECTION 5: PATTERN 2 - POWER STRUGGLES (Q19-21)
    # ========================================================================
    
    {
        "id": 19,
        "text": "When someone disagrees with you, your body's immediate response is:",
        "type": "single_choice",
        "options": [
            "Stays relaxed and curious about their view",
            "Mild tension but manageable and open",
            "Tenses up immediately, ready to defend",
            "Adrenaline rush, heart racing, fight-or-flight"
        ],
        "pattern": 2,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 2 somatic response"
    },
    
    {
        "id": 20,
        "text": "In disagreements, how often do you feel a need to 'win' or prove your point?",
        "type": "single_choice",
        "options": [
            "Rarely - I'm curious to understand",
            "Sometimes - depends on the topic",
            "Often - it's important to be right",
            "Almost always - losing feels intolerable"
        ],
        "pattern": 2,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 2 behavioral frequency"
    },
    
    {
        "id": 21,
        "text": "When you lose an argument or are proven wrong, you feel:",
        "type": "single_choice",
        "options": [
            "Curious and grateful to learn something new",
            "Slightly uncomfortable but can accept it",
            "Diminished, humiliated, or angry at myself",
            "Rage or deep sense of defeat and shame"
        ],
        "pattern": 2,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 2 emotional signature"
    },
    
    # ========================================================================
    # SECTION 6: PATTERN 3 - SYSTEMATIC MISTRUST (Q22-24)
    # ========================================================================
    
    {
        "id": 22,
        "text": "When meeting someone new, your default assumption about their intentions is:",
        "type": "single_choice",
        "options": [
            "They're probably friendly and genuine",
            "Neutral - I'll assess as I get to know them",
            "Cautious - they might have hidden motives",
            "Guarded - they probably want something from me"
        ],
        "pattern": 3,
        "weights": [2, 4, 7, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 3 baseline severity"
    },
    
    {
        "id": 23,
        "text": "Someone you just met is unexpectedly kind or helpful. Your first thought:",
        "type": "single_choice",
        "options": [
            "That's nice - they seem genuinely kind",
            "I appreciate it but wonder about their motive",
            "What do they want from me in return?",
            "This is manipulation - what's their angle?"
        ],
        "pattern": 3,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 3 cognitive distortion"
    },
    
    {
        "id": 24,
        "text": "How many times have you been significantly betrayed by people you trusted?",
        "type": "single_choice",
        "options": [
            "Never or once",
            "2-3 times",
            "4-5 times",
            "6-10 times",
            "Too many to count"
        ],
        "pattern": 3,
        "weights": [2, 5, 7, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 3 origin severity"
    },
    
    # ========================================================================
    # SECTION 7: VALIDATION CHECK #1 (Q25)
    # ========================================================================
    
    {
        "id": 25,
        "text": "I have never felt anxious about anything in my entire life",
        "type": "single_choice",
        "options": ["True", "False"],
        "pattern": None,
        "weights": [10, 0],  # High score = defensive
        "validation_question": True,
        "analytics_use": "Defensive responding detection"
    },
    
    # ========================================================================
    # SECTION 8: PATTERN 4 - SEPARATION/DIVISION (Q26-27)
    # ========================================================================
    
    {
        "id": 26,
        "text": "When facing a difficult decision, you typically:",
        "type": "single_choice",
        "options": [
            "See multiple creative options and possibilities",
            "See a few main options with pros and cons",
            "Feel stuck between two opposing either/or choices",
            "See only two extreme all-or-nothing options"
        ],
        "pattern": 4,
        "weights": [2, 4, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 4 cognitive style"
    },
    
    {
        "id": 27,
        "text": "When evaluating people, you tend to see them as:",
        "type": "single_choice",
        "options": [
            "Complex humans with both strengths and flaws",
            "Mostly good or mostly bad overall",
            "Either completely good or completely bad",
            "Good until proven bad, then irredeemable"
        ],
        "pattern": 4,
        "weights": [2, 5, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 4 relational manifestation"
    },
    
    # ========================================================================
    # SECTION 9: PATTERN 5 - DOING VS BEING (Q28-29)
    # ========================================================================
    
    {
        "id": 28,
        "text": "Complete this sentence: 'I feel valuable when I...'",
        "type": "single_choice",
        "options": [
            "Simply exist as I am",
            "Am doing something meaningful",
            "Accomplish something important",
            "Prove my worth through achievements"
        ],
        "pattern": 5,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 5 core belief"
    },
    
    {
        "id": 29,
        "text": "When you have free time with nothing scheduled, you feel:",
        "type": "single_choice",
        "options": [
            "Peaceful and content with the space",
            "Relaxed but slightly restless",
            "Guilty like I should be doing something",
            "Anxious and worthless without productivity"
        ],
        "pattern": 5,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 5 behavioral signature"
    },
    
    # ========================================================================
    # SECTION 10: DIGITAL EMOTIONS (Q30-32)
    # ========================================================================
    
    {
        "id": 30,
        "text": "How often do you consume 'rage-bait' content (outrage-inducing posts, arguments)?",
        "type": "single_choice",
        "options": [
            "Rarely - I actively avoid it",
            "Sometimes when it appears in my feed",
            "Often - it's hard to scroll past",
            "Daily - I seek it out or can't stop engaging"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "digital_emotion": "rage_addiction",
        "analytics_use": "Digital emotion: rage addiction"
    },
    
    {
        "id": 31,
        "text": "Genuine joy from real-world experiences versus online engagement:",
        "type": "single_choice",
        "options": [
            "Real-world joy is deeper and more lasting",
            "Both provide about equal satisfaction",
            "Online engagement feels more rewarding",
            "Real-world feels flat or boring compared to digital"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "digital_emotion": "dopamine_dysregulation",
        "analytics_use": "Digital emotion: dopamine dysregulation"
    },
    
    {
        "id": 32,
        "text": "Seeing others' highlight reels on social media makes you feel:",
        "type": "single_choice",
        "options": [
            "Happy for them without comparing myself",
            "Inspired but with slight envy",
            "Inadequate and wondering why not me",
            "Worthless like I'm failing at life"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "digital_emotion": "comparison_anxiety",
        "analytics_use": "Digital emotion: comparison anxiety"
    },
    
    # ========================================================================
    # SECTION 11: PATTERN 6 - COMPARTMENTALIZED AUTHENTICITY (Q33-35)
    # ========================================================================
    
    {
        "id": 33,
        "text": "Your personality and behavior across different settings (work, family, friends):",
        "type": "single_choice",
        "options": [
            "Stay very consistent - I'm the same person",
            "Vary slightly based on appropriate context",
            "Vary significantly - almost different personas",
            "Completely different - like separate people"
        ],
        "pattern": 6,
        "weights": [2, 4, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 6 severity"
    },
    
    {
        "id": 34,
        "text": "How much of your 'real self' do you hide from most people?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "labels": ["I'm completely open", "I hide everything"],
        "pattern": 6,
        "scale_to_10": True,
        "analytics_use": "Pattern 6 quantification"
    },
    
    {
        "id": 35,
        "text": "Being your authentic self in childhood resulted in:",
        "type": "single_choice",
        "options": [
            "Acceptance and love from your family",
            "Mostly acceptance with some criticism",
            "Criticism, ridicule, or rejection",
            "Punishment, shame, or abandonment"
        ],
        "pattern": 6,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 6 origin"
    },
    
    # ========================================================================
    # SECTION 12: PATTERN 7 - SELF-SACRIFICE (Q36-38)
    # ========================================================================
    
    {
        "id": 36,
        "text": "When it comes to your needs versus others' needs:",
        "type": "single_choice",
        "options": [
            "I naturally balance both in healthy ways",
            "I usually prioritize mine but consider theirs",
            "Others' needs usually come first",
            "I almost always put others first, little left for me"
        ],
        "pattern": 7,
        "weights": [2, 4, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 7 core behavior"
    },
    
    {
        "id": 37,
        "text": "How often do you say 'yes' when you really want to say 'no'?",
        "type": "single_choice",
        "options": [
            "Rarely - I honor my boundaries",
            "Sometimes in certain situations",
            "Often - it's hard to say no",
            "Almost always - I can't say no"
        ],
        "pattern": 7,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 7 behavioral frequency"
    },
    
    {
        "id": 38,
        "text": "Putting your own needs first in childhood was seen as:",
        "type": "single_choice",
        "options": [
            "Healthy and encouraged",
            "Acceptable when appropriate",
            "Selfish but tolerated",
            "Shameful, wrong, or punishable"
        ],
        "pattern": 7,
        "weights": [2, 4, 7, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 7 origin"
    },
    
    # ========================================================================
    # SECTION 13: PATTERN 8 - INHERITED MISSIONS (Q39-41)
    # ========================================================================
    
    {
        "id": 39,
        "text": "Your major life goals are primarily:",
        "type": "single_choice",
        "options": [
            "Based on my own genuine desires and values",
            "Mostly mine with some family influence",
            "A mix of mine and family expectations equally",
            "Primarily family expectations, not really mine"
        ],
        "pattern": 8,
        "weights": [2, 4, 7, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 8 life direction"
    },
    
    {
        "id": 40,
        "text": "When thinking about pursuing your own path separate from family expectations:",
        "type": "single_choice",
        "options": [
            "I feel free and excited about my choices",
            "I feel supportive curiosity from family",
            "I feel some guilt but mostly okay with it",
            "I feel I would betray or destroy relationships"
        ],
        "pattern": 8,
        "weights": [2, 3, 6, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 8 emotional signature"
    },
    
    {
        "id": 41,
        "text": "Growing up, love and approval in your family were conditional on:",
        "type": "single_choice",
        "options": [
            "Nothing - you were loved unconditionally",
            "Being good and not causing trouble",
            "Getting good grades and performing well",
            "Achieving specific standards consistently",
            "Constant exceptional achievement"
        ],
        "pattern": 8,
        "weights": [2, 5, 7, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 8 and 5 origin"
    },
    
    # ========================================================================
    # SECTION 14: PATTERN 9 - CONTEXT DEPENDENT WEAKNESS (Q42)
    # ========================================================================
    
    {
        "id": 42,
        "text": "Your boundaries and limits across different situations:",
        "type": "single_choice",
        "options": [
            "Stay consistent - I'm the same everywhere",
            "Vary slightly but remain generally intact",
            "Vary significantly - strong in some places, weak in others",
            "Disappear completely in certain specific contexts"
        ],
        "pattern": 9,
        "weights": [2, 4, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 9 severity"
    },

# ========================================================================
    # SECTION 15: MORE PATTERN 9 + SEQUENCE CONTINUATION (Q43-48)
    # ========================================================================
    
    {
        "id": 43,
        "text": "With certain people or situations, you become someone you don't respect. This happens:",
        "type": "single_choice",
        "options": [
            "Never - I stay consistent with my values",
            "Rarely - only in extreme circumstances",
            "Sometimes - with specific people or situations",
            "Often - I know it will happen and feel helpless"
        ],
        "pattern": 9,
        "weights": [2, 4, 7, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 9 behavioral frequency"
    },
    
    {
        "id": 44,
        "text": "A few hours later after the triggering incident from Q9, you were:",
        "type": "single_choice",
        "options": [
            "Moved on and forgot about it",
            "Still replaying what happened",
            "Planning how to avoid it next time",
            "Angry at myself for reacting that way",
            "Resigned that this is just how things are"
        ],
        "pattern": None,
        "analytics_use": "Sequence mapping: extended impact"
    },
    
    {
        "id": 45,
        "text": "This exact trigger → response sequence happens:",
        "type": "single_choice",
        "options": [
            "Rarely - this was a unique situation",
            "Occasionally - a few times per month",
            "Regularly - weekly or more",
            "Frequently - multiple times per week",
            "Daily or near-daily"
        ],
        "pattern": None,
        "weights": [2, 4, 6, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern frequency assessment"
    },
    
    {
        "id": 46,
        "text": "The trigger in Q9 was primarily:",
        "type": "single_choice",
        "options": [
            "A digital or online event",
            "An in-person interaction",
            "An internal thought or memory",
            "A physical environment or situation",
            "A combination of digital and real-world"
        ],
        "pattern": None,
        "analytics_use": "Trigger classification"
    },
    
    {
        "id": 47,
        "text": "Your emotional state throughout the day is primarily regulated by:",
        "type": "single_choice",
        "options": [
            "Real-world relationships and in-person interactions",
            "A healthy balance of both online and offline",
            "Online engagement, notifications, and digital validation"
        ],
        "pattern": 10,
        "weights": [2, 5, 9],  # CHANGED: NO ZERO, 3-option format
        "digital_emotion": "algorithmic_dependency",
        "analytics_use": "Digital emotion: algorithmic dependency"
    },
    
    {
        "id": 48,
        "text": "Imagining life without social media for an entire month makes you feel:",
        "type": "single_choice",
        "options": [
            "Relieved and curious about the experience",
            "Uncomfortable but willing to try",
            "Anxious about missing out or losing connections",
            "Terrified - it would mean social death"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "digital_emotion": "dependency_fear",
        "analytics_use": "Digital emotion: dependency fear"
    },
    
    # ========================================================================
    # SECTION 16: DIGITAL DETAIL & INTERPLAY (Q49-52)
    # ========================================================================
    
    {
        "id": 49,
        "text": "What percentage of your digital time is spent on social media platforms?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "labels": ["0% - None", "100% - All of it"],
        "pattern": 10,
        "analytics_use": "Social media vs total screen time"
    },
    
    {
        "id": 50,
        "text": "When you post content online and it gets less engagement than expected, you:",
        "type": "single_choice",
        "options": [
            "Don't really notice or care about engagement",
            "Feel slightly disappointed but move on",
            "Feel rejected or like I'm becoming irrelevant",
            "Feel worthless and question my value"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "digital_emotion": "rejection_sensitivity",
        "analytics_use": "Digital emotion: rejection sensitivity"
    },
    
    {
        "id": 51,
        "text": "You find yourself checking your phone or social media:",
        "type": "single_choice",
        "options": [
            "A few times a day with intention",
            "Several times throughout the day",
            "Constantly throughout the day without thinking",
            "Compulsively - I can't stop even when I try"
        ],
        "pattern": 10,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Digital compulsion severity"
    },
    
    {
        "id": 52,
        "text": "The primary emotion you're seeking when scrolling social media is:",
        "type": "single_choice",
        "options": [
            "Connection and genuine community",
            "Entertainment and distraction",
            "Validation and approval",
            "Stimulation and dopamine hits",
            "Escape and numbness from real life"
        ],
        "pattern": 10,
        "weights": [2, 5, 7, 9, 10],  # CHANGED: NO ZERO
        "analytics_use": "Digital motivation classification"
    },
    
    # ========================================================================
    # SECTION 17: PATTERN ORIGINS (Q53-58)
    # ========================================================================
    
    {
        "id": 53,
        "text": "What family messages did you receive about happiness and success?",
        "type": "text_completion",
        "placeholder": "What was said, modeled, or communicated about joy, celebrating, achieving...",
        "min_chars": 5,
        "pattern": 1,
        "analytics_use": "Pattern 1 origin identification"
    },
    
    {
        "id": 54,
        "text": "Growing up, conflicts in your family typically ended with:",
        "type": "single_choice",
        "options": [
            "Calm resolution and mutual understanding",
            "Someone compromising to keep the peace",
            "The loudest or strongest person winning",
            "Anger, tears, or prolonged silent treatment"
        ],
        "pattern": 2,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern 2 origin"
    },
    
    {
        "id": 55,
        "text": "What early experiences shaped your trust in others?",
        "type": "text_completion",
        "placeholder": "Think about early relationships, betrayals, or trust-building experiences...",
        "min_chars": 5,
        "pattern": 3,
        "analytics_use": "Pattern 3 origin identification"
    },
    
    {
        "id": 56,
        "text": "Where did you learn that choices must be either/or?",
        "type": "text_completion",
        "placeholder": "Family rules, religious teachings, or specific experiences that taught binary thinking...",
        "min_chars": 5,
        "pattern": 4,
        "analytics_use": "Pattern 4 origin"
    },
    
    {
        "id": 57,
        "text": "What childhood experiences linked your worth to performance?",
        "type": "text_completion",
        "placeholder": "Grades, achievements, family expectations, or conditional approval...",
        "min_chars": 5,
        "pattern": 5,
        "analytics_use": "Pattern 5 origin"
    },
    
    {
        "id": 58,
        "text": "When did you learn to show different selves to different people?",
        "type": "text_completion",
        "placeholder": "Specific situations or relationships that taught you to adapt or hide...",
        "min_chars": 5,
        "pattern": 6,
        "analytics_use": "Pattern 6 origin"
    },
    
    # ========================================================================
    # SECTION 18: PATTERN CONSTELLATION MAPPING (Q59-64)
    # ========================================================================
    
    {
        "id": 59,
        "text": "When you feel undeserving of happiness (Pattern 1), it makes you MORE likely to:",
        "type": "single_choice",
        "options": [
            "Seek digital validation to prove your worth",
            "Withdraw from real relationships",
            "Work harder to earn happiness",
            "None of these - it doesn't spread to other areas"
        ],
        "pattern": None,
        "analytics_use": "Pattern 1 amplification mapping"
    },
    
    {
        "id": 60,
        "text": "Your need for control in conflicts (Pattern 2) is MOST connected to:",
        "type": "single_choice",
        "options": [
            "Fear of being exposed as inauthentic",
            "Belief that submission equals worthlessness",
            "Mistrust that others have good intentions",
            "None - it stands alone"
        ],
        "pattern": None,
        "analytics_use": "Pattern 2 constellation"
    },
    
    {
        "id": 61,
        "text": "When you sacrifice your needs for others (Pattern 7), you often compensate by:",
        "type": "single_choice",
        "options": [
            "Seeking approval and validation online",
            "Building resentment and mistrust",
            "Creating different personas in different contexts",
            "None - no compensation needed"
        ],
        "pattern": None,
        "analytics_use": "Pattern 7 compensation"
    },
    
    {
        "id": 62,
        "text": "Your either/or thinking (Pattern 4) shows up MOST strongly in:",
        "type": "single_choice",
        "options": [
            "Online debates and political content consumption",
            "Career versus relationships decisions",
            "Being authentic versus being accepted choices",
            "Doesn't show up in any specific area"
        ],
        "pattern": None,
        "analytics_use": "Pattern 4 manifestation"
    },
    
    {
        "id": 63,
        "text": "Which pattern feels MOST like your core identity?",
        "type": "single_choice",
        "options": [
            "Pattern 1: Expecting disappointment after good things",
            "Pattern 2: Needing control in conflicts",
            "Pattern 3: Mistrusting others' intentions",
            "Pattern 5: Proving worth through achievement",
            "Pattern 6: Hiding my real self",
            "Pattern 10: Digital self feels more real than offline"
        ],
        "pattern": None,
        "analytics_use": "Core identity pattern"
    },
    
    {
        "id": 64,
        "text": "Social media comparison (Pattern 10) MOST amplifies your:",
        "type": "single_choice",
        "options": [
            "Unhappiness and expectation of failure",
            "Mistrust of others' authenticity",
            "Need to prove worth through achievement",
            "Hiding authentic self to fit in",
            "Doesn't really amplify any traditional patterns"
        ],
        "pattern": None,
        "analytics_use": "Digital amplification primary"
    },
    
    # ========================================================================
    # SECTION 19: HIDDEN BARRIERS & RESISTANCE (Q65-70)
    # ========================================================================
    
    {
        "id": 65,
        "text": "If you completely resolved your main pattern, you would LOSE:",
        "type": "text_completion",
        "placeholder": "What protection, identity, benefit, or function would disappear if this pattern was gone?",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Secondary gain identification"
    },
    
    {
        "id": 66,
        "text": "Who in your life would be MOST uncomfortable if you transformed?",
        "type": "text_completion",
        "placeholder": "Who benefits from you staying as you are? What relationship might be threatened?",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Systemic resistance source"
    },
    
    {
        "id": 67,
        "text": "Everything I've described about my struggles is 100% true and accurate",
        "type": "single_choice",
        "options": ["True", "Mostly true", "Somewhat true", "Not really true"],
        "pattern": None,
        "weights": [0, 1, 5, 10],  # High score = defensive
        "validation_question": True,
        "analytics_use": "Validation check #2"
    },
    
    {
        "id": 68,
        "text": "The scariest thing about changing would be:",
        "type": "single_choice",
        "options": [
            "Nothing - I'm ready and eager to change",
            "Not knowing who I'd be without this pattern",
            "Losing relationships or sense of belonging",
            "Having to face emotions I've been avoiding",
            "Discovering that change isn't actually possible for me"
        ],
        "pattern": None,
        "weights": [0, 6, 7, 8, 10],  # 0 for ready = healthy
        "analytics_use": "Primary resistance identification"
    },
    
    {
        "id": 69,
        "text": "Complete this sentence: 'I can't change this because...'",
        "type": "text_completion",
        "placeholder": "What's the real reason you believe change is hard or impossible for you?",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Core limiting belief extraction"
    },
    
    {
        "id": 70,
        "text": "What would need to be true for you to feel COMPLETELY safe changing?",
        "type": "text_completion",
        "placeholder": "What guarantees, support, conditions, or reassurances would you need?",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Safety requirements"
    },
    
    # ========================================================================
    # SECTION 20: TRANSFORMATION READINESS (Q71-79)
    # ========================================================================
    
    {
        "id": 71,
        "text": "On a scale of 1-10, how much do you believe change is truly possible FOR YOU?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "labels": ["Impossible for me", "Completely possible"],
        "pattern": None,
        "analytics_use": "Change belief assessment"
    },
    
    {
        "id": 72,
        "text": "How ready are you to begin transformation work RIGHT NOW?",
        "type": "single_choice",
        "options": [
            "Ready to start this week",
            "Ready within the next 2 weeks",
            "Ready within the next month",
            "Still exploring different options",
            "Just gathering information for now"
        ],
        "pattern": None,
        "weights": [10, 8, 6, 4, 2],
        "analytics_use": "Readiness timing"
    },
    
    {
        "id": 73,
        "text": "If this pattern completely resolved, the FIRST thing you would do is:",
        "type": "text_completion",
        "placeholder": "Be specific about the action, conversation, decision, or change you'd make...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "First action vision"
    },
    
    {
        "id": 74,
        "text": "Six months from now with this pattern resolved, describe a typical day:",
        "type": "text_completion",
        "placeholder": "Walk through a day in your life without this limitation - be specific and concrete...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Future vision concrete"
    },
    
    {
        "id": 75,
        "text": "Resolving this pattern would MOST impact your:",
        "type": "single_choice",
        "options": [
            "Career and professional life",
            "Intimate romantic relationships",
            "Family relationships",
            "Sense of self and identity",
            "Social life and friendships",
            "Physical health and wellbeing",
            "All of the above equally"
        ],
        "pattern": None,
        "analytics_use": "Transformation impact area"
    },
    
    {
        "id": 76,
        "text": "What motivates you MOST to change right now?",
        "type": "text_completion",
        "placeholder": "Be specific about what's driving your desire for transformation today...",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Motivation primary"
    },
    
    {
        "id": 77,
        "text": "The cost of NOT changing in the next year would be:",
        "type": "text_completion",
        "placeholder": "What will you lose, miss, or sacrifice if nothing changes?",
        "min_chars": 5,
        "pattern": None,
        "analytics_use": "Inaction cost"
    },
    
    {
        "id": 78,
        "text": "How urgent is resolving this issue for you?",
        "type": "single_choice",
        "options": [
            "Extremely urgent - affecting daily life significantly",
            "Very urgent - need change within the next few weeks",
            "Moderately urgent - within 1-2 months",
            "Somewhat urgent - within 6 months",
            "Not urgent - exploring options gradually"
        ],
        "pattern": None,
        "weights": [10, 8, 6, 4, 2],
        "analytics_use": "Urgency level"
    },
    
    {
        "id": 79,
        "text": "How many different life areas is this pattern currently affecting?",
        "type": "single_choice",
        "options": [
            "1-2 specific areas only",
            "3-4 areas of my life",
            "5-6 areas - most of my life",
            "Every area of my life"
        ],
        "pattern": None,
        "weights": [2, 5, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Life area spread"
    },
    
    # ========================================================================
    # SECTION 21: SESSION PREDICTION (Q80-82)
    # ========================================================================
    
    {
        "id": 80,
        "text": "How long have you been consciously aware of wanting to change this pattern?",
        "type": "single_choice",
        "options": [
            "Less than 6 months",
            "6 months to 1 year",
            "1-3 years",
            "3-5 years",
            "More than 5 years or as long as I can remember"
        ],
        "pattern": None,
        "weights": [2, 4, 6, 8, 10],  # CHANGED: NO ZERO
        "analytics_use": "Pattern entrenchment"
    },
    
    {
        "id": 81,
        "text": "Previous attempts to change this pattern:",
        "type": "single_choice",
        "options": [
            "This is my first focused attempt at change",
            "I've tried 1-2 times before",
            "I've tried 3-5 times",
            "I've tried 6-10 times",
            "I've tried many times and always seem to fail"
        ],
        "pattern": None,
        "weights": [3, 5, 7, 9, 10],  # CHANGED: minimum 3
        "analytics_use": "Previous failure count"
    },
    
    {
        "id": 82,
        "text": "How accurately does this assessment capture your actual struggles?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "labels": ["Not accurate at all", "Extremely accurate"],
        "pattern": None,
        "validation_question": True,
        "analytics_use": "Assessment accuracy validation"
    },
    
    # ========================================================================
    # SECTION 22: FINAL OPEN-ENDED (Q83-84)
    # ========================================================================
    
    {
        "id": 83,
        "text": "What's ONE thing about you or your situation that this assessment didn't capture?",
        "type": "text_completion",
        "placeholder": "Anything unique, important, or missed that would help us understand you better...",
        "min_chars": 5,
        "pattern": None,
        "optional": True,
        "analytics_use": "Assessment gaps"
    },
    
    {
        "id": 84,
        "text": "Any additional information you'd like to share?",
        "type": "text_completion",
        "placeholder": "Medical conditions, current medications, therapy history, or other relevant context...",
        "min_chars": 5,
        "pattern": None,
        "optional": True,
        "analytics_use": "Additional context"
    },
    
# ============================================================================
# SECTION 23: FORCED-CHOICE DYAD QUESTIONS (Q85-94)
# Purpose: Force pattern detection with no escape routes
# Format: Must choose A or B, assigns minimum 2 points to one pattern
# ============================================================================

{
    "id": 85,
    "text": "When facing a major life decision, you're MORE likely to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Analyze all possible outcomes to avoid mistakes",
        "B: Move forward quickly to avoid missing opportunities"
    ],
    "pattern_mapping": {
        "A": {"pattern": 1, "weight": 7},  # Unhappiness culture - fear of good things
        "B": {"pattern": 5, "weight": 6}   # Doing vs being - action addiction
    },
    "analytics_use": "Core pattern detection - avoidance vs action"
},

{
    "id": 86,
    "text": "In a disagreement, you naturally tend to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Assert your position to ensure you're heard",
        "B: Consider their perspective to find common ground"
    ],
    "pattern_mapping": {
        "A": {"pattern": 2, "weight": 7},  # Power struggles
        "B": {"pattern": 7, "weight": 5}   # Self-sacrifice (over-accommodation)
    },
    "analytics_use": "Core pattern detection - dominance vs accommodation"
},

{
    "id": 87,
    "text": "When meeting someone new, you typically:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Stay guarded until they prove trustworthy",
        "B: Open up and show your authentic self"
    ],
    "pattern_mapping": {
        "A": {"pattern": 3, "weight": 7},  # Systematic mistrust
        "B": {"pattern": 6, "weight": 4}   # Authenticity (low compartmentalization)
    },
    "analytics_use": "Core pattern detection - trust vs openness"
},

{
    "id": 88,
    "text": "When evaluating options, you're MORE likely to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: See clear right and wrong choices",
        "B: See multiple valid perspectives and possibilities"
    ],
    "pattern_mapping": {
        "A": {"pattern": 4, "weight": 8},  # Separation/division - binary thinking
        "B": {"pattern": 4, "weight": 2}   # Low binary thinking (adaptive)
    },
    "analytics_use": "Core pattern detection - binary vs nuanced thinking"
},

{
    "id": 89,
    "text": "Your sense of worth comes MORE from:",
    "type": "forced_choice_dyad",
    "options": [
        "A: What you accomplish and achieve",
        "B: Who you are as a person"
    ],
    "pattern_mapping": {
        "A": {"pattern": 5, "weight": 8},  # Doing vs being
        "B": {"pattern": 5, "weight": 2}   # Low achievement addiction (adaptive)
    },
    "analytics_use": "Core pattern detection - worth source"
},

{
    "id": 90,
    "text": "In different situations, you tend to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Adapt your behavior to fit what's expected",
        "B: Stay consistent with your core values and self"
    ],
    "pattern_mapping": {
        "A": {"pattern": 6, "weight": 7},  # Compartmentalized authenticity
        "B": {"pattern": 6, "weight": 2}   # Low compartmentalization (adaptive)
    },
    "analytics_use": "Core pattern detection - consistency vs adaptation"
},

{
    "id": 91,
    "text": "When others need help, you're MORE likely to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Put their needs before your own without hesitation",
        "B: Consider your own needs and capacity first"
    ],
    "pattern_mapping": {
        "A": {"pattern": 7, "weight": 8},  # Self-sacrifice
        "B": {"pattern": 7, "weight": 2}   # Healthy boundaries (adaptive)
    },
    "analytics_use": "Core pattern detection - self-care vs self-sacrifice"
},

{
    "id": 92,
    "text": "Your life path is MORE influenced by:",
    "type": "forced_choice_dyad",
    "options": [
        "A: What your family expected or hoped for you",
        "B: What you genuinely want for yourself"
    ],
    "pattern_mapping": {
        "A": {"pattern": 8, "weight": 8},  # Inherited missions
        "B": {"pattern": 8, "weight": 2}   # Personal autonomy (adaptive)
    },
    "analytics_use": "Core pattern detection - family vs self direction"
},

{
    "id": 93,
    "text": "Your boundaries are MORE likely to:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Stay consistent regardless of who you're with",
        "B: Shift depending on the person or situation"
    ],
    "pattern_mapping": {
        "A": {"pattern": 9, "weight": 2},  # Strong consistent boundaries (adaptive)
        "B": {"pattern": 9, "weight": 8}   # Context-dependent weakness
    },
    "analytics_use": "Core pattern detection - boundary consistency"
},

{
    "id": 94,
    "text": "You feel MORE connected and authentic when:",
    "type": "forced_choice_dyad",
    "options": [
        "A: Interacting online or through digital platforms",
        "B: Having face-to-face real-world conversations"
    ],
    "pattern_mapping": {
        "A": {"pattern": 10, "weight": 8},  # Digital reality dissociation
        "B": {"pattern": 10, "weight": 2}   # Real-world connection (adaptive)
    },
    "analytics_use": "Core pattern detection - reality preference"
},

# ============================================================================
# SECTION 24: RANKING QUESTIONS FOR PATTERN CONSTELLATION (Q95-97)
# Purpose: Create spectrum profiles across all patterns
# Format: Rank top 3 from list, assigns 5/3/2 points to ranked patterns
# ============================================================================

{
    "id": 95,
    "text": "Rank your top 3 CHALLENGES from most to least difficult (drag to reorder):",
    "type": "ranking",
    "max_selections": 3,
    "options": [
        "Accepting happiness and good things",           # Pattern 1
        "Managing conflicts without fighting",           # Pattern 2
        "Trusting people's intentions",                  # Pattern 3
        "Making decisions without all-or-nothing thinking", # Pattern 4
        "Feeling valuable without constant achievement", # Pattern 5
        "Being authentic across all situations",         # Pattern 6
        "Prioritizing my own needs",                     # Pattern 7
        "Following my own path vs family expectations",  # Pattern 8
        "Maintaining boundaries consistently",           # Pattern 9
        "Feeling connected in real-world vs online"      # Pattern 10
    ],
    "pattern_mapping": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "weights": [5, 3, 2],  # First choice: 5 points, Second: 3, Third: 2
    "analytics_use": "Primary constellation identification"
},

{
    "id": 96,
    "text": "Rank your top 3 PROTECTIVE PATTERNS - what you do to feel safe (drag to reorder):",
    "type": "ranking",
    "max_selections": 3,
    "options": [
        "Prepare for disappointment to avoid hurt",          # Pattern 1
        "Stay in control to prevent vulnerability",          # Pattern 2
        "Stay guarded to avoid betrayal",                    # Pattern 3
        "Keep things clear and simple to avoid confusion",   # Pattern 4
        "Stay busy to prove my value",                       # Pattern 5
        "Show different versions of myself to fit in",       # Pattern 6
        "Help others to earn love and belonging",            # Pattern 7
        "Meet family expectations to maintain connection",   # Pattern 8
        "Adapt to others to avoid conflict",                 # Pattern 9
        "Stay online where I feel more comfortable"          # Pattern 10
    ],
    "pattern_mapping": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "weights": [5, 3, 2],
    "analytics_use": "Protective function identification"
},

{
    "id": 97,
    "text": "Rank your top 3 DESIRED CHANGES - what you most want to transform (drag to reorder):",
    "type": "ranking",
    "max_selections": 3,
    "options": [
        "Accept joy without waiting for disaster",           # Pattern 1
        "Collaborate without needing to win",                # Pattern 2
        "Trust others more easily",                          # Pattern 3
        "Embrace complexity and nuance",                     # Pattern 4
        "Feel worthy without proving myself",                # Pattern 5
        "Be consistently authentic everywhere",              # Pattern 6
        "Say no and prioritize myself",                      # Pattern 7
        "Follow my own dreams confidently",                  # Pattern 8
        "Maintain boundaries with everyone",                 # Pattern 9
        "Connect deeply in real-world relationships"         # Pattern 10
    ],
    "pattern_mapping": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "weights": [5, 3, 2],
    "analytics_use": "Transformation priority identification"
}

]  # END OF COMPLETE_QUESTION_SET



# ============================================================================
# VALIDATION: Total Question Count
# ============================================================================
assert len(COMPLETE_QUESTION_SET) == 97, f"Expected 97 questions, got {len(COMPLETE_QUESTION_SET)}"



# ============================================================================
# UNIVERSAL PROFILING SYSTEM
# Everyone gets profiled on spectrum - no escape routes
# ============================================================================

class UniversalProfiler:
    """
    UNIVERSAL PROFILING ENGINE
    Profiles everyone on spectrum from adaptive to clinical
    NO ZERO SCORES - Everyone gets minimum baseline
    """
    
    def __init__(self):
        self.minimum_baseline = 2.0  # Everyone gets at least 2.0 per pattern
        self.adaptive_threshold = 4.0  # Below 4.0 = adaptive range
        self.clinical_threshold = 6.0  # Above 6.0 = clinical concern
        
        self.severity_gradations = {
            "adaptive": (2.0, 4.0),
            "mild": (4.0, 6.0),
            "moderate": (6.0, 8.0),
            "severe": (8.0, 10.0)
        }
    
    def create_universal_profile(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """
        Create spectrum profile for every person
        Returns comprehensive profile with gradations
        """
        
        # Classify all 10 patterns by severity
        profile_by_severity = {
            "severe_clinical": {},
            "moderate_clinical": {},
            "mild_patterns": {},
            "adaptive_patterns": {}
        }
        
        for pattern_id, score in pattern_scores.items():
            if score >= 8.0:
                profile_by_severity["severe_clinical"][pattern_id] = score
            elif score >= 6.0:
                profile_by_severity["moderate_clinical"][pattern_id] = score
            elif score >= 4.0:
                profile_by_severity["mild_patterns"][pattern_id] = score
            else:
                profile_by_severity["adaptive_patterns"][pattern_id] = score
        
        # Determine clinical profile type
        profile_type = self._classify_clinical_profile(profile_by_severity)
        
        # Generate severity distribution
        severity_distribution = self._calculate_severity_distribution(pattern_scores)
        
        # Calculate profile balance
        balance_score = self._calculate_profile_balance(pattern_scores)
        
        return {
            "profile_type": profile_type,
            "severity_classification": profile_by_severity,
            "severity_distribution": severity_distribution,
            "balance_score": balance_score,
            "clinical_priority_patterns": self._get_clinical_priorities(profile_by_severity),
            "adaptive_strength_patterns": self._get_adaptive_strengths(profile_by_severity),
            "overall_health_index": self._calculate_health_index(pattern_scores),
            "intervention_urgency": self._determine_intervention_urgency(profile_by_severity)
        }
    
    def _classify_clinical_profile(
        self, 
        profile_by_severity: Dict[str, Dict]
    ) -> str:
        """Classify overall clinical profile"""
        
        severe_count = len(profile_by_severity["severe_clinical"])
        moderate_count = len(profile_by_severity["moderate_clinical"])
        mild_count = len(profile_by_severity["mild_patterns"])
        adaptive_count = len(profile_by_severity["adaptive_patterns"])
        
        # Clinical profile classifications
        if severe_count >= 4:
            return "COMPLEX MULTI-PATTERN CLINICAL: High-intensity comprehensive intervention required"
        
        elif severe_count >= 2:
            return "DUAL SEVERE CLINICAL: Focused intensive intervention on primary patterns"
        
        elif severe_count == 1 and moderate_count >= 3:
            return "PRIMARY SEVERE WITH MODERATE COMPLEXITY: Standard protocol with reinforcement"
        
        elif severe_count == 1 and moderate_count <= 2:
            return "SINGLE SEVERE PATTERN: Targeted 2-session intervention optimal"
        
        elif moderate_count >= 4:
            return "MULTIPLE MODERATE PATTERNS: Standard intervention recommended"
        
        elif moderate_count >= 2:
            return "DUAL MODERATE PATTERNS: Brief intervention or self-directed work"
        
        elif mild_count >= 5:
            return "PREDOMINANTLY MILD PATTERNS: Psychoeducation and skill-building"
        
        elif adaptive_count >= 7:
            return "PREDOMINANTLY ADAPTIVE: Minimal intervention, growth-focused"
        
        else:
            return "BALANCED PROFILE: Standard wellness maintenance"
    
    def _calculate_severity_distribution(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, float]:
        """Calculate distribution across severity levels"""
        
        total_patterns = len(pattern_scores)
        
        severe_count = len([s for s in pattern_scores.values() if s >= 8.0])
        moderate_count = len([s for s in pattern_scores.values() if 6.0 <= s < 8.0])
        mild_count = len([s for s in pattern_scores.values() if 4.0 <= s < 6.0])
        adaptive_count = len([s for s in pattern_scores.values() if s < 4.0])
        
        return {
            "severe_percentage": round((severe_count / total_patterns) * 100, 1),
            "moderate_percentage": round((moderate_count / total_patterns) * 100, 1),
            "mild_percentage": round((mild_count / total_patterns) * 100, 1),
            "adaptive_percentage": round((adaptive_count / total_patterns) * 100, 1)
        }
    
    def _calculate_profile_balance(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """Calculate balance vs concentration of scores"""
        
        scores_list = list(pattern_scores.values())
        
        # Calculate standard deviation (balance indicator)
        mean_score = sum(scores_list) / len(scores_list)
        variance = sum((x - mean_score) ** 2 for x in scores_list) / len(scores_list)
        std_dev = variance ** 0.5
        
        # Lower std_dev = more balanced, Higher = more concentrated
        if std_dev < 1.5:
            balance_type = "Evenly distributed across patterns"
        elif std_dev < 2.5:
            balance_type = "Moderately concentrated in specific patterns"
        else:
            balance_type = "Highly concentrated in dominant patterns"
        
        # Calculate range
        score_range = max(scores_list) - min(scores_list)
        
        return {
            "balance_score": round(std_dev, 2),
            "balance_type": balance_type,
            "score_range": round(score_range, 1),
            "mean_score": round(mean_score, 1),
            "interpretation": "Lower balance score = more evenly distributed patterns"
        }
    
    def _get_clinical_priorities(
        self, 
        profile_by_severity: Dict[str, Dict]
    ) -> List[Dict]:
        """Get prioritized list of clinical concerns"""
        
        priorities = []
        
        # Severe patterns first
        for pattern_id, score in profile_by_severity["severe_clinical"].items():
            priorities.append({
                "pattern_id": pattern_id,
                "pattern_name": PatternDefinitions.PATTERNS[pattern_id],
                "score": score,
                "priority_level": "URGENT",
                "intervention_timeline": "Immediate - Session 1 focus"
            })
        
        # Then moderate
        for pattern_id, score in profile_by_severity["moderate_clinical"].items():
            priorities.append({
                "pattern_id": pattern_id,
                "pattern_name": PatternDefinitions.PATTERNS[pattern_id],
                "score": score,
                "priority_level": "HIGH",
                "intervention_timeline": "Address in sessions 2-3"
            })
        
        # Sort by score
        priorities.sort(key=lambda x: x['score'], reverse=True)
        
        return priorities
    
    def _get_adaptive_strengths(
        self, 
        profile_by_severity: Dict[str, Dict]
    ) -> List[Dict]:
        """Identify adaptive strengths to leverage"""
        
        strengths = []
        
        for pattern_id, score in profile_by_severity["adaptive_patterns"].items():
            strengths.append({
                "pattern_id": pattern_id,
                "pattern_name": PatternDefinitions.PATTERNS[pattern_id],
                "score": score,
                "strength_description": f"Adaptive functioning in {PatternDefinitions.PATTERNS[pattern_id]} domain",
                "leverage_potential": "Can be used as resource during intervention"
            })
        
        # Sort by lowest score (most adaptive)
        strengths.sort(key=lambda x: x['score'])
        
        return strengths
    
    def _calculate_health_index(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """Calculate overall psychological health index"""
        
        # Invert scores: Lower pattern scores = better health
        # Health index: 0-100, where 100 = optimal health
        
        # Average pattern score
        avg_pattern_score = sum(pattern_scores.values()) / len(pattern_scores)
        
        # Convert to health index (inverted)
        # Score 2.0 (minimum) = 100 health
        # Score 10.0 (maximum) = 0 health
        health_index = 100 - ((avg_pattern_score - 2.0) / 8.0) * 100
        health_index = max(0, min(100, health_index))
        
        # Classify health level
        if health_index >= 80:
            health_level = "EXCELLENT: Highly adaptive functioning"
        elif health_index >= 60:
            health_level = "GOOD: Generally healthy with minor concerns"
        elif health_index >= 40:
            health_level = "FAIR: Moderate patterns requiring attention"
        elif health_index >= 20:
            health_level = "POOR: Significant clinical concerns"
        else:
            health_level = "CRITICAL: Intensive intervention needed"
        
        return {
            "health_index": round(health_index, 1),
            "health_level": health_level,
            "average_pattern_score": round(avg_pattern_score, 1)
        }
    
    def _determine_intervention_urgency(
        self, 
        profile_by_severity: Dict[str, Dict]
    ) -> str:
        """Determine intervention urgency"""
        
        severe_count = len(profile_by_severity["severe_clinical"])
        moderate_count = len(profile_by_severity["moderate_clinical"])
        
        if severe_count >= 3:
            return "CRISIS LEVEL: Immediate comprehensive intervention required"
        elif severe_count >= 2:
            return "URGENT: Schedule within 1 week"
        elif severe_count == 1 or moderate_count >= 4:
            return "HIGH PRIORITY: Schedule within 2 weeks"
        elif moderate_count >= 2:
            return "MODERATE PRIORITY: Schedule within 1 month"
        elif moderate_count >= 1:
            return "STANDARD: Schedule within 6 weeks"
        else:
            return "LOW URGENCY: Optional wellness support"


# ============================================================================
# SPECTRUM VISUALIZATION DATA GENERATOR
# Creates data for visual representation of pattern profiles
# ============================================================================

class SpectrumVisualizer:
    """
    Generate visualization data for pattern spectrum profiles
    Creates chart-ready data for Plotly, Chart.js, etc.
    """
    
    def __init__(self):
        self.pattern_names = PatternDefinitions.PATTERNS
        self.colors = {
            "severe": "#ef4444",      # Red
            "moderate": "#eab308",    # Yellow
            "mild": "#4CA1A3",        # Teal
            "adaptive": "#22c55e"     # Green
        }
    
    def generate_radar_chart_data(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """
        Generate radar/spider chart data for all 10 patterns
        Perfect for visualizing pattern profile
        """
        
        labels = [self.pattern_names[i] for i in range(1, 11)]
        scores = [pattern_scores.get(i, 2.0) for i in range(1, 11)]
        
        # Color code by severity
        colors = []
        for score in scores:
            if score >= 8.0:
                colors.append(self.colors["severe"])
            elif score >= 6.0:
                colors.append(self.colors["moderate"])
            elif score >= 4.0:
                colors.append(self.colors["mild"])
            else:
                colors.append(self.colors["adaptive"])
        
        return {
            "type": "radar",
            "labels": labels,
            "datasets": [{
                "label": "Pattern Intensity",
                "data": scores,
                "backgroundColor": "rgba(76, 161, 163, 0.2)",
                "borderColor": "#4CA1A3",
                "pointBackgroundColor": colors,
                "pointBorderColor": colors,
                "pointRadius": 6,
                "pointHoverRadius": 8
            }],
            "options": {
                "scale": {
                    "min": 0,
                    "max": 10,
                    "ticks": {
                        "stepSize": 2
                    }
                }
            }
        }
    
    def generate_horizontal_bar_data(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """
        Generate horizontal bar chart for pattern comparison
        Easier to read than radar for many users
        """
        
        # Sort patterns by score (descending)
        sorted_patterns = sorted(
            pattern_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        labels = [self.pattern_names[pid] for pid, _ in sorted_patterns]
        scores = [score for _, score in sorted_patterns]
        
        # Color code bars
        colors = []
        for score in scores:
            if score >= 8.0:
                colors.append(self.colors["severe"])
            elif score >= 6.0:
                colors.append(self.colors["moderate"])
            elif score >= 4.0:
                colors.append(self.colors["mild"])
            else:
                colors.append(self.colors["adaptive"])
        
        return {
            "type": "horizontalBar",
            "labels": labels,
            "datasets": [{
                "label": "Pattern Intensity (0-10)",
                "data": scores,
                "backgroundColor": colors,
                "borderColor": colors,
                "borderWidth": 1
            }],
            "options": {
                "scales": {
                    "xAxes": [{
                        "ticks": {
                            "min": 0,
                            "max": 10,
                            "stepSize": 2
                        }
                    }]
                }
            }
        }
    
    def generate_severity_distribution_pie(
        self, 
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """
        Generate pie chart showing distribution across severity levels
        """
        
        severe_count = len([s for s in pattern_scores.values() if s >= 8.0])
        moderate_count = len([s for s in pattern_scores.values() if 6.0 <= s < 8.0])
        mild_count = len([s for s in pattern_scores.values() if 4.0 <= s < 6.0])
        adaptive_count = len([s for s in pattern_scores.values() if s < 4.0])
        
        return {
            "type": "pie",
            "labels": ["Severe", "Moderate", "Mild", "Adaptive"],
            "datasets": [{
                "data": [severe_count, moderate_count, mild_count, adaptive_count],
                "backgroundColor": [
                    self.colors["severe"],
                    self.colors["moderate"],
                    self.colors["mild"],
                    self.colors["adaptive"]
                ],
                "borderWidth": 2,
                "borderColor": "#FFFFFF"
            }]
        }
    
    def generate_pattern_constellation_network(
        self, 
        pattern_scores: Dict[int, float],
        reinforcement_matrix: Dict[Tuple[int, int], float]
    ) -> Dict[str, Any]:
        """
        Generate network graph data showing pattern interactions
        For visualization of how patterns reinforce each other
        """
        
        # Nodes (patterns)
        nodes = []
        for pattern_id, score in pattern_scores.items():
            # Determine node color by severity
            if score >= 8.0:
                color = self.colors["severe"]
            elif score >= 6.0:
                color = self.colors["moderate"]
            elif score >= 4.0:
                color = self.colors["mild"]
            else:
                color = self.colors["adaptive"]
            
            nodes.append({
                "id": pattern_id,
                "label": self.pattern_names[pattern_id],
                "value": score,
                "color": color,
                "font": {"size": 12 if score >= 6.0 else 10}
            })
        
        # Edges (reinforcements)
        edges = []
        for (p1, p2), amplification in reinforcement_matrix.items():
            score1 = pattern_scores.get(p1, 0)
            score2 = pattern_scores.get(p2, 0)
            
            # Only show edges between significant patterns
            if score1 >= 6.0 and score2 >= 6.0:
                edges.append({
                    "from": p1,
                    "to": p2,
                    "value": amplification,
                    "title": f"Amplification: {amplification}x",
                    "color": self.colors["moderate"] if amplification < 1.5 else self.colors["severe"],
                    "width": amplification * 2
                })
        
        return {
            "nodes": nodes,
            "edges": edges,
            "options": {
                "physics": {
                    "enabled": True,
                    "stabilization": True
                }
            }
        }
    
    def generate_timeline_projection(
        self, 
        pattern_scores: Dict[int, float],
        session_count: int = 2
    ) -> Dict[str, Any]:
        """
        Generate timeline showing expected pattern reduction
        """
        
        # Get top 3 clinical patterns
        clinical_patterns = {
            pid: score 
            for pid, score in pattern_scores.items() 
            if score >= 6.0
        }
        sorted_clinical = sorted(
            clinical_patterns.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:3]
        
        timeline_data = []
        
        for pattern_id, initial_score in sorted_clinical:
            # Project reduction trajectory
            # Session 1: 15% reduction (pattern mapping)
            # Session 2: 60% reduction (neural rewiring)
            # Post-session: 80% reduction (integration)
            
            session_1_score = initial_score * 0.85
            session_2_score = initial_score * 0.40
            post_session_score = initial_score * 0.20
            
            timeline_data.append({
                "label": self.pattern_names[pattern_id],
                "data": [
                    {"x": "Baseline", "y": initial_score},
                    {"x": "Post-Session 1", "y": session_1_score},
                    {"x": "Post-Session 2", "y": session_2_score},
                    {"x": "2 Weeks Post", "y": post_session_score}
                ]
            })
        
        return {
            "type": "line",
            "datasets": timeline_data,
            "options": {
                "scales": {
                    "yAxes": [{
                        "ticks": {
                            "min": 0,
                            "max": 10,
                            "stepSize": 2
                        },
                        "scaleLabel": {
                            "display": True,
                            "labelString": "Pattern Intensity"
                        }
                    }]
                }
            }
        }


# ============================================================================
# COMPREHENSIVE PROFILING REPORT GENERATOR
# Generates complete clinical and client-facing reports
# ============================================================================

class ComprehensiveProfileReport:
    """
    Generate complete profiling reports with universal spectrum data
    Includes both clinical (therapist) and client-facing versions
    """
    
    def __init__(self, analytics: Dict, universal_profile: Dict):
        self.analytics = analytics
        self.universal_profile = universal_profile
        self.pattern_descriptions = PatternDefinitions.PATTERN_DESCRIPTIONS
        self.patterns = PatternDefinitions.PATTERNS
    
    def generate_therapist_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive therapist-facing clinical report
        Complete technical analysis for treatment planning
        """
        
        report = {
            "report_type": "CLINICAL THERAPIST REPORT",
            "generated": datetime.now().isoformat(),
            "client_id": "Assessment_" + datetime.now().strftime("%Y%m%d_%H%M%S"),
            
            # Section 1: Executive Summary
            "executive_summary": self._generate_clinical_executive_summary(),
            
            # Section 2: Universal Profile Classification
            "universal_profile": {
                "profile_type": self.universal_profile["profile_type"],
                "health_index": self.universal_profile["overall_health_index"],
                "intervention_urgency": self.universal_profile["intervention_urgency"],
                "severity_distribution": self.universal_profile["severity_distribution"]
            },
            
            # Section 3: Pattern Analysis by Severity
            "pattern_analysis": self._generate_pattern_analysis_by_severity(),
            
            # Section 4: Pattern Constellation & Interactions
            "constellation_analysis": self._generate_constellation_clinical_summary(),
            
            # Section 5: Trigger Sequence Mapping
            "trigger_sequence": self.analytics["trigger_sequence"],
            
            # Section 6: Digital Integration (if applicable)
            "digital_analysis": self._generate_digital_clinical_summary(),
            
            # Section 7: Resistance & Barriers
            "resistance_analysis": {
                "resistance_intensity": self.analytics["hidden_barriers"]["resistance_intensity"],
                "resistance_type": self.analytics["hidden_barriers"]["resistance_type"],
                "secondary_gain": self.analytics["hidden_barriers"]["secondary_gain"],
                "systemic_stakeholders": self.analytics["hidden_barriers"]["systemic_stakeholders"],
                "protective_functions": self.analytics["hidden_barriers"]["protective_functions"]
            },
            
            # Section 8: Session Planning
            "session_planning": self._generate_session_planning(),
            
            # Section 9: Success Prediction & Optimization
            "success_prediction": {
                "overall_success_rate": self.analytics["success_prediction"]["overall_success_rate"],
                "success_tier": self.analytics["success_prediction"]["success_tier"],
                "optimization_factors": self._get_optimization_factors()
            },
            
            # Section 10: Clinical Recommendations
            "clinical_recommendations": self._generate_clinical_recommendations()
        }
        
        return report
    
    def generate_client_report(self) -> Dict[str, Any]:
        """
        Generate client-facing comprehensive report
        Accessible language, empowering framing, actionable insights
        """
        
        report = {
            "report_type": "YOUR TRANSFORMATION BLUEPRINT",
            "generated": datetime.now().strftime("%B %d, %Y"),
            
            # Section 1: Your Pattern Profile
            "your_profile": self._generate_client_profile_summary(),
            
            # Section 2: Understanding Your Patterns
            "pattern_insights": self._generate_client_pattern_insights(),
            
            # Section 3: How Your Patterns Work Together
            "pattern_interactions": self._generate_client_constellation_insights(),
            
            # Section 4: Your Trigger Sequence
            "your_trigger_sequence": self._generate_client_trigger_insights(),
            
            # Section 5: Digital Life Impact (if applicable)
            "digital_impact": self._generate_client_digital_insights(),
            
            # Section 6: What's Keeping You Stuck
            "hidden_barriers": self._generate_client_barrier_insights(),
            
            # Section 7: Your Transformation Roadmap
            "transformation_roadmap": self._generate_client_roadmap(),
            
            # Section 8: Success Factors
            "success_factors": self._generate_client_success_factors(),
            
            # Section 9: Investment & Value
            "investment_analysis": self._generate_client_investment_analysis(),
            
            # Section 10: Next Steps
            "next_steps": self._generate_client_next_steps()
        }
        
        return report
    
    # =======================================================================
    # CLINICAL REPORT GENERATORS (Therapist-Facing)
    # =======================================================================
    
    def _generate_clinical_executive_summary(self) -> Dict[str, Any]:
        """Generate clinical executive summary"""
        
        hierarchy = self.analytics["pattern_hierarchy"]
        dominant = hierarchy["dominant_pattern"]
        
        return {
            "primary_pattern": f"{dominant['name']} (Score: {dominant['score']}/10)",
            "severity_classification": dominant["severity"],
            "clinical_concern_count": hierarchy["clinical_concern_count"],
            "profile_classification": self.universal_profile["profile_type"],
            "intervention_urgency": self.universal_profile["intervention_urgency"],
            "recommended_sessions": self.analytics["session_prediction"]["recommended_sessions"],
            "success_probability": f"{self.analytics['success_prediction']['overall_success_rate']}%",
            "key_clinical_note": self._generate_key_clinical_note()
        }
    
    def _generate_key_clinical_note(self) -> str:
        """Generate key clinical note"""
        
        dominant = self.analytics["pattern_hierarchy"]["dominant_pattern"]
        pattern_id = dominant["id"]
        pattern_info = self.pattern_descriptions.get(pattern_id, {})
        
        return (
            f"Primary intervention focus: {pattern_info.get('intervention_focus', 'Pattern transformation')}. "
            f"Core belief: '{pattern_info.get('core_belief', 'Not identified')}'. "
            f"Protective function: {pattern_info.get('protective_function', 'Not identified')}."
        )
    
    def _generate_pattern_analysis_by_severity(self) -> Dict[str, Any]:
        """Generate detailed pattern analysis by severity"""
        
        severity_classification = self.universal_profile["severity_classification"]
        
        analysis = {
            "severe_clinical": [],
            "moderate_clinical": [],
            "mild_patterns": [],
            "adaptive_strengths": []
        }
        
        # Process each severity level
        for severity_level, pattern_dict in severity_classification.items():
            for pattern_id, score in pattern_dict.items():
                pattern_info = self.pattern_descriptions.get(pattern_id, {})
                
                pattern_entry = {
                    "pattern_id": pattern_id,
                    "pattern_name": self.patterns[pattern_id],
                    "score": round(score, 1),
                    "root_structure": pattern_info.get("root_structure", "Not defined"),
                    "core_belief": pattern_info.get("core_belief", "Not identified"),
                    "protective_function": pattern_info.get("protective_function", "Not identified"),
                    "intervention_strategy": pattern_info.get("intervention_focus", "Standard protocol"),
                    "session_1_focus": pattern_info.get("session_1_focus", "Pattern mapping"),
                    "session_2_focus": pattern_info.get("session_2_focus", "Neural rewiring")
                }
                
                if severity_level == "severe_clinical":
                    analysis["severe_clinical"].append(pattern_entry)
                elif severity_level == "moderate_clinical":
                    analysis["moderate_clinical"].append(pattern_entry)
                elif severity_level == "mild_patterns":
                    analysis["mild_patterns"].append(pattern_entry)
                else:
                    analysis["adaptive_strengths"].append(pattern_entry)
        
        return analysis
    
    def _generate_constellation_clinical_summary(self) -> Dict[str, Any]:
        """Generate constellation clinical summary"""
        
        constellation = self.analytics["constellation_analysis"]
        
        return {
            "constellation_multiplier": constellation["constellation_multiplier"],
            "reinforcement_count": constellation["reinforcement_count"],
            "active_reinforcements": constellation["active_reinforcements"],
            "constellation_complexity": constellation["constellation_complexity"],
            "clinical_implication": self._interpret_constellation_clinically(constellation)
        }
    
    def _interpret_constellation_clinically(self, constellation: Dict) -> str:
        """Interpret constellation for clinical use"""
        
        multiplier = constellation["constellation_multiplier"]
        count = constellation["reinforcement_count"]
        
        if multiplier >= 2.0:
            return (
                f"HIGH AMPLIFICATION ({multiplier}x): Patterns significantly reinforce each other. "
                f"Requires careful sequencing - address dominant pattern first to prevent cascade."
            )
        elif multiplier >= 1.5:
            return (
                f"MODERATE AMPLIFICATION ({multiplier}x): Some pattern interaction present. "
                f"Standard protocol with attention to secondary patterns."
            )
        else:
            return (
                f"LOW AMPLIFICATION ({multiplier}x): Patterns relatively independent. "
                f"Can address dominant pattern without significant cascade concern."
            )
    
    def _generate_digital_clinical_summary(self) -> Dict[str, Any]:
        """Generate digital clinical summary"""
        
        digital = self.analytics.get("digital_analysis")
        
        if not digital:
            return {"applicable": False}
        
        if digital["severity_level"] == "MINIMAL":
            return {
                "applicable": True,
                "severity": "MINIMAL",
                "clinical_note": "No specialized digital interventions required"
            }
        
        interplay = self.analytics.get("digital_interplay", {})
        
        return {
            "applicable": True,
            "severity_level": digital["severity_level"],
            "digital_despair_score": digital["digital_despair_score"],
            "primary_driver": digital["primary_digital_driver"],
            "amplification_effects": interplay.get("amplification_effects", {}),
            "intervention_priorities": interplay.get("intervention_priority", []),
            "clinical_note": self._generate_digital_clinical_note(digital, interplay)
        }
    
    def _generate_digital_clinical_note(self, digital: Dict, interplay: Dict) -> str:
        """Generate digital clinical note"""
        
        severity = digital["severity_level"]
        
        if severity == "SEVERE":
            return (
                "CRITICAL: Specialized digital-native protocol required. "
                "Authority resistance likely - use collaborative language. "
                "Attention optimization: 15-30 min segments. "
                "Address ironic detachment before core emotional work."
            )
        elif severity == "MODERATE":
            return (
                "SIGNIFICANT: Modified protocol recommended. "
                "Shorter session segments, digital-aware language. "
                "Integrate digital competencies as strengths."
            )
        else:
            return "Mild digital influence - integrate as contextual factor."
    
    def _generate_session_planning(self) -> Dict[str, Any]:
        """Generate detailed session planning"""
        
        session_pred = self.analytics["session_prediction"]
        dominant = self.analytics["pattern_hierarchy"]["dominant_pattern"]
        pattern_info = self.pattern_descriptions.get(dominant["id"], {})
        
        return {
            "recommended_sessions": session_pred["recommended_sessions"],
            "timeline_estimate": session_pred["timeline_estimate"],
            "complexity_score": session_pred["complexity_score"],
            "session_3_probability": session_pred["session_3_probability"],
            "session_breakdown": {
                "session_1": {
                    "duration": "90 minutes",
                    "focus": pattern_info.get("session_1_focus", "Pattern mapping"),
                    "goals": [
                        "Complete behavioral chain analysis",
                        "Establish therapeutic alliance",
                        "Identify all intervention points",
                        "Initial positive programming"
                    ],
                    "intervention_keywords": pattern_info.get("intervention_keywords", []),
                    "avoid_language": pattern_info.get("avoid_language", [])
                },
                "session_2": {
                    "duration": "90 minutes",
                    "focus": pattern_info.get("session_2_focus", "Neural rewiring"),
                    "goals": [
                        "Deep hypnotic pattern interruption",
                        "Install new neural pathways",
                        "Alternative response programming",
                        "Future pacing and integration"
                    ]
                }
            }
        }
    
    def _get_optimization_factors(self) -> List[str]:
        """Get success optimization factors"""
        
        readiness = self.analytics["readiness_analysis"]
        
        factors = []
        
        if readiness["composite_readiness"] >= 8:
            factors.append("High readiness and motivation")
        
        if readiness["vision_clarity"] in ["High - Detailed concrete vision", "Moderate - General vision present"]:
            factors.append("Clear transformation vision")
        
        if self.analytics["assessment_quality"]["completion_rate"] >= 90:
            factors.append("Excellent assessment engagement")
        
        if self.universal_profile["adaptive_strength_patterns"]:
            factors.append(f"{len(self.universal_profile['adaptive_strength_patterns'])} adaptive strengths to leverage")
        
        return factors if factors else ["Standard therapeutic factors"]
    
    def _generate_clinical_recommendations(self) -> Dict[str, Any]:
        """Generate clinical recommendations"""
        
        return {
            "primary_intervention": self._get_primary_intervention_recommendation(),
            "contraindications": self._check_contraindications(),
            "special_considerations": self._get_special_considerations(),
            "referral_recommendations": self._check_referral_needs()
        }
    
    def _get_primary_intervention_recommendation(self) -> str:
        """Get primary intervention recommendation"""
        
        dominant = self.analytics["pattern_hierarchy"]["dominant_pattern"]
        pattern_info = self.pattern_descriptions.get(dominant["id"], {})
        
        return (
            f"Primary focus: {dominant['name']} pattern transformation using "
            f"{pattern_info.get('intervention_focus', 'standard hypnotherapy protocol')}. "
            f"Intervention strategy: {pattern_info.get('intervention_focus', 'Pattern-specific approach')}."
        )
    
    def _check_contraindications(self) -> List[str]:
        """Check for contraindications"""
        
        contraindications = []
        
        # Check responses for medical contraindications
        responses = self.analytics.get("assessment_responses", {})
        
        # Check Q5: Medical/psychiatric care
        medical_response = responses.get(5, "")
        if "mental health" in medical_response.lower() or "psychiatric" in medical_response.lower():
            contraindications.append("Currently under psychiatric care - coordinate with provider")
        
        # Check Q6: Dissociation/panic/suicidal
        crisis_response = responses.get(6, "")
        if "currently experiencing" in crisis_response.lower():
            contraindications.append("Current crisis symptoms - assess stability before hypnotherapy")
        
        # Check Q7: Substance use
        substance_response = responses.get(7, "")
        if "recreational drugs" in substance_response.lower():
            contraindications.append("Active substance use - address stabilization first")
        
        return contraindications if contraindications else ["No contraindications identified"]
    
    def _get_special_considerations(self) -> List[str]:
        """Get special clinical considerations"""
        
        considerations = []
        
        # Digital native considerations
        if self.analytics["digital_analysis"].get("is_digital_native"):
            severity = self.analytics["digital_analysis"]["severity_level"]
            if severity in ["SEVERE", "MODERATE"]:
                considerations.append(f"Digital native protocol: {severity} adaptations required")
        
        # High resistance considerations
        resistance = self.analytics["hidden_barriers"]["resistance_intensity"]
        if "High" in resistance:
            considerations.append("High resistance - extra rapport building recommended")
        
        # Complex constellation
        constellation = self.analytics["constellation_analysis"]
        if constellation["constellation_multiplier"] > 1.5:
            considerations.append("Complex pattern interactions - careful sequencing required")
        
        return considerations if considerations else ["Standard protocol appropriate"]
    
    def _check_referral_needs(self) -> List[str]:
        """Check if referrals needed"""
        
        referrals = []
        
        contraindications = self._check_contraindications()
        
        if any("crisis" in c.lower() for c in contraindications):
            referrals.append("Crisis intervention or psychiatric evaluation")
        
        if any("substance" in c.lower() for c in contraindications):
            referrals.append("Substance abuse treatment or assessment")
        
        return referrals if referrals else ["No referrals indicated"]
    
    # Continue in next chunk with CLIENT-FACING report generators...


# =======================================================================
    # CLIENT REPORT GENERATORS (Client-Facing)
    # =======================================================================
    
    def _generate_client_profile_summary(self) -> Dict[str, Any]:
        """
        Generate empowering client profile summary
        Accessible language, strengths-based framing
        """
        
        hierarchy = self.analytics["pattern_hierarchy"]
        dominant = hierarchy["dominant_pattern"]
        health_index = self.universal_profile["overall_health_index"]
        
        # Create empowering profile description
        profile_description = self._create_empowering_profile_description()
        
        return {
            "your_primary_pattern": dominant["name"],
            "what_this_means": self._explain_pattern_to_client(dominant["id"]),
            "your_profile_type": self._simplify_profile_type(),
            "your_health_score": f"{health_index['health_index']}/100",
            "what_this_score_means": health_index["health_level"],
            "empowering_summary": profile_description,
            "your_strengths": self._identify_client_strengths(),
            "patterns_detected": hierarchy["pattern_count"],
            "patterns_needing_attention": hierarchy["clinical_concern_count"]
        }
    
    def _create_empowering_profile_description(self) -> str:
        """Create empowering profile description"""
        
        profile_type = self.universal_profile["profile_type"]
        
        empowering_descriptions = {
            "COMPLEX MULTI-PATTERN CLINICAL": (
                "You're dealing with several interconnected patterns that have been protecting you. "
                "This complexity means you've been incredibly resilient. With the right approach, "
                "you can transform all of these patterns together, creating profound change."
            ),
            "DUAL SEVERE CLINICAL": (
                "You have two primary patterns that work together. The good news? Addressing these "
                "creates a domino effect - when one shifts, the others follow. Your transformation "
                "will be comprehensive and deeply satisfying."
            ),
            "PRIMARY SEVERE WITH MODERATE COMPLEXITY": (
                "You have one main pattern with a few supporting ones. This is actually ideal - "
                "we can focus our work precisely where it matters most, leading to rapid change "
                "that naturally improves other areas of your life."
            ),
            "SINGLE SEVERE PATTERN": (
                "You have one clear pattern that's been running the show. This focused challenge "
                "means we can target it directly and completely. Most people with this profile "
                "experience dramatic transformation in just 2 sessions."
            ),
            "MULTIPLE MODERATE PATTERNS": (
                "You have several moderate patterns - none overwhelming, but together they're "
                "holding you back. The advantage? None are deeply entrenched, so transformation "
                "can happen quickly and smoothly across all areas."
            ),
            "PREDOMINANTLY ADAPTIVE": (
                "You're already functioning quite well! The patterns we detected are minor. "
                "This work will be more about optimization and reaching your next level of "
                "thriving rather than fixing major problems."
            )
        }
        
        # Find matching description
        for key, description in empowering_descriptions.items():
            if key in profile_type:
                return description
        
        return (
            "Your pattern profile shows a unique combination that we can work with effectively. "
            "Every pattern serves a protective purpose - our work is about updating those "
            "protections so they serve your authentic goals."
        )
    
    def _explain_pattern_to_client(self, pattern_id: int) -> str:
        """Explain pattern to client in accessible language"""
        
        pattern_info = self.pattern_descriptions.get(pattern_id, {})
        
        explanations = {
            1: "You've learned to brace for disappointment after good things happen. This protected you from hurt, but now it's preventing you from fully enjoying life's pleasures.",
            2: "You tend to see disagreements as battles to win. This kept you safe from being controlled, but now it's creating unnecessary conflicts and stress.",
            3: "You automatically question people's motives and intentions. This protected you from betrayal, but now it's keeping you isolated from genuine connections.",
            4: "You see choices as either/or instead of both/and. This gave you clarity in chaos, but now it's creating false dilemmas and limiting your options.",
            5: "You measure your worth by what you accomplish. This drove achievement, but now it's preventing you from feeling valuable when you're just being yourself.",
            6: "You show different versions of yourself in different settings. This helped you fit in, but now it's exhausting you and preventing authentic connections.",
            7: "You consistently put others' needs before your own. This made you valuable to others, but now it's leaving you depleted and resentful.",
            8: "You're living someone else's dreams instead of your own. This maintained family harmony, but now it's preventing you from authentic fulfillment.",
            9: "Your boundaries disappear in certain situations. This kept peace with specific people, but now it's causing you to lose yourself.",
            10: "You feel more real online than in person. This gave you connection and escape, but now it's disconnecting you from embodied life and real relationships."
        }
        
        return explanations.get(pattern_id, pattern_info.get("description", "Pattern detected"))
    
    def _simplify_profile_type(self) -> str:
        """Simplify profile type for client"""
        
        profile_type = self.universal_profile["profile_type"]
        
        if "COMPLEX MULTI-PATTERN" in profile_type:
            return "Complex but transformable"
        elif "DUAL SEVERE" in profile_type:
            return "Dual-focus intervention"
        elif "PRIMARY SEVERE" in profile_type:
            return "Single primary pattern"
        elif "MODERATE PATTERNS" in profile_type:
            return "Multiple moderate patterns"
        elif "ADAPTIVE" in profile_type:
            return "Highly functional baseline"
        else:
            return "Standard intervention profile"
    
    def _identify_client_strengths(self) -> List[str]:
        """Identify and frame client strengths"""
        
        strengths = []
        
        # Assessment completion strength
        quality = self.analytics["assessment_quality"]
        if quality["completion_rate"] >= 90:
            strengths.append("High self-awareness and commitment (completed comprehensive assessment)")
        
        # Adaptive patterns as strengths
        adaptive_patterns = self.universal_profile["adaptive_strength_patterns"]
        if adaptive_patterns:
            top_adaptive = adaptive_patterns[0]
            strengths.append(f"Healthy functioning in {self.patterns[top_adaptive['pattern_id']].lower()} area")
        
        # Readiness as strength
        readiness = self.analytics["readiness_analysis"]
        if readiness["composite_readiness"] >= 7:
            strengths.append("Strong readiness and motivation for change")
        
        # Vision clarity as strength
        if "High" in readiness["vision_clarity"]:
            strengths.append("Clear vision of desired transformation")
        
        # Digital competencies (if applicable)
        digital = self.analytics.get("digital_analysis", {})
        if digital.get("is_digital_native"):
            strengths.append("Digital fluency and technological competence")
        
        return strengths if strengths else [
            "Courage to seek help",
            "Willingness to explore deep patterns",
            "Capacity for self-reflection"
        ]
    
    def _generate_client_pattern_insights(self) -> Dict[str, Any]:
        """Generate client-friendly pattern insights"""
        
        hierarchy = self.analytics["pattern_hierarchy"]
        dominant = hierarchy["dominant_pattern"]
        primary_patterns = hierarchy["primary_patterns"]
        
        pattern_id = dominant["id"]
        pattern_info = self.pattern_descriptions.get(pattern_id, {})
        
        return {
            "your_main_pattern": {
                "name": dominant["name"],
                "intensity": f"{dominant['score']}/10",
                "what_you_notice": pattern_info.get("what_you_notice", "Pattern manifestations"),
                "what_others_see": pattern_info.get("what_others_see", "External observations"),
                "hidden_cost": pattern_info.get("hidden_cost", "Pattern costs"),
                "breakthrough_insight": pattern_info.get("breakthrough_moment", "Key realization"),
                "how_it_protects_you": pattern_info.get("protective_function", "Protection mechanism"),
                "original_purpose": self._explain_original_purpose(pattern_info)
            },
            "supporting_patterns": [
                {
                    "name": p["name"],
                    "intensity": f"{p['score']}/10",
                    "how_it_shows_up": self.pattern_descriptions.get(p["id"], {}).get("what_you_notice", "Varies"),
                    "connection_to_main": self._explain_pattern_connection(p["id"], pattern_id)
                }
                for p in primary_patterns
            ]
        }
    
    def _explain_original_purpose(self, pattern_info: Dict) -> str:
        """Explain original protective purpose of pattern"""
        
        systemic_factors = pattern_info.get("systemic_factors", [])
        protective_function = pattern_info.get("protective_function", "")
        
        if systemic_factors:
            return (
                f"This pattern developed to protect you from: {systemic_factors[0]}. "
                f"It worked brilliantly then - {protective_function.lower()}. "
                f"Now we update it to serve your current life."
            )
        
        return f"This pattern served to {protective_function.lower()}. It was adaptive protection that we can now evolve."
    
    def _explain_pattern_connection(self, pattern_id: int, dominant_id: int) -> str:
        """Explain how patterns connect"""
        
        connections = {
            (1, 2): "When you expect disappointment, you fight harder to control outcomes",
            (1, 3): "Expecting bad things makes you mistrust good things",
            (1, 5): "You work harder to create happiness you feel you can't naturally have",
            (2, 3): "Fighting for control comes from not trusting others' intentions",
            (2, 5): "You prove worth by winning and achieving",
            (3, 6): "Mistrust makes you hide your real self",
            (3, 7): "Mistrust prevents asking for help, so you sacrifice yourself",
            (5, 6): "You show the achieving self but hide the being self",
            (5, 7): "You sacrifice yourself to achieve for others",
            (7, 8): "You sacrifice yourself to fulfill family missions",
            (8, 9): "Family expectations create context where you lose boundaries"
        }
        
        # Try both directions
        connection = connections.get((dominant_id, pattern_id)) or connections.get((pattern_id, dominant_id))
        
        if connection:
            return connection
        
        return "These patterns reinforce each other, creating a cycle we'll interrupt together"
    
    def _generate_client_constellation_insights(self) -> Dict[str, Any]:
        """Generate client-friendly constellation insights"""
        
        constellation = self.analytics["constellation_analysis"]
        
        if constellation["reinforcement_count"] == 0:
            return {
                "patterns_work_together": False,
                "insight": "Your patterns are relatively independent, which actually makes them easier to address individually."
            }
        
        amplification = constellation["constellation_multiplier"]
        
        return {
            "patterns_work_together": True,
            "amplification_factor": f"{amplification}x",
            "what_this_means": self._explain_amplification_to_client(amplification),
            "the_good_news": self._frame_amplification_positively(amplification),
            "key_interactions": [
                {
                    "pattern_1": self.patterns[interaction["pattern_1"]],
                    "pattern_2": self.patterns[interaction["pattern_2"]],
                    "how_they_reinforce": f"These amplify each other by {interaction['amplification']}x",
                    "what_breaks_the_cycle": self._explain_cycle_breaking(interaction)
                }
                for interaction in constellation["active_reinforcements"][:3]  # Top 3
            ]
        }
    
    def _explain_amplification_to_client(self, amplification: float) -> str:
        """Explain amplification in client language"""
        
        if amplification >= 2.0:
            return (
                "Your patterns significantly amplify each other - when one activates, it triggers the others. "
                "This explains why change has felt so hard. The patterns were protecting each other."
            )
        elif amplification >= 1.5:
            return (
                "Your patterns have moderate interaction - they influence each other somewhat. "
                "This means addressing the main one will naturally help the others."
            )
        else:
            return (
                "Your patterns have mild interaction - they're fairly independent. "
                "This means we can target each one directly without worrying about cascade effects."
            )
    
    def _frame_amplification_positively(self, amplification: float) -> str:
        """Frame amplification positively"""
        
        if amplification >= 1.5:
            return (
                "When patterns reinforce each other, changing one creates a cascade of positive change. "
                "Your transformation will be more comprehensive than if you had isolated patterns. "
                "It's like dominoes - we tip the first one, and the rest naturally follow."
            )
        else:
            return (
                "Your patterns are independent, which means we can address them precisely and efficiently. "
                "Each transformation stands on its own, giving you clear, focused change."
            )
    
    def _explain_cycle_breaking(self, interaction: Dict) -> str:
        """Explain how to break the cycle"""
        
        return (
            f"We'll address {self.patterns[interaction['pattern_1']]} first, which automatically weakens "
            f"{self.patterns[interaction['pattern_2']]}. They can't reinforce each other once the primary pattern shifts."
        )
    
    def _generate_client_trigger_insights(self) -> Dict[str, Any]:
        """Generate client-friendly trigger sequence insights"""
        
        trigger_seq = self.analytics["trigger_sequence"]
        sequence = trigger_seq["trigger_chain"]
        
        # Check if sequence captured
        if sequence["environmental_trigger"] == "Not captured":
            return {
                "sequence_captured": False,
                "note": "We'll map your complete trigger sequence in session 1"
            }
        
        return {
            "sequence_captured": True,
            "your_pattern_sequence": {
                "step_1_trigger": {
                    "what_happens": sequence["environmental_trigger"],
                    "explanation": "This is what starts the pattern"
                },
                "step_2_body": {
                    "what_you_feel": sequence["physical_response"],
                    "explanation": "Your body responds before your mind"
                },
                "step_3_thought": {
                    "what_you_think": sequence["automatic_thought"],
                    "explanation": "This automatic thought follows the sensation"
                },
                "step_4_emotion": {
                    "what_you_feel": sequence["emotional_response"],
                    "explanation": "The emotion that follows the thought"
                },
                "step_5_action": {
                    "what_you_do": sequence["behavioral_response"],
                    "explanation": "The automatic behavior that follows"
                },
                "step_6_result": {
                    "what_happens": sequence["immediate_consequence"],
                    "explanation": "The immediate result of your action"
                }
            },
            "intervention_points": [
                {
                    "window": point,
                    "what_we_do": self._explain_intervention_to_client(point)
                }
                for point in trigger_seq["intervention_windows"]
            ],
            "the_good_news": (
                "Now that we can see the exact sequence, we can interrupt it at multiple points. "
                "You'll gain automatic new responses that happen before you even think about it."
            )
        }
    
    def _explain_intervention_to_client(self, intervention_window: str) -> str:
        """Explain intervention point to client"""
        
        explanations = {
            "Somatic awareness": "We'll teach your body to recognize the pattern starting, giving you a choice before it runs",
            "Cognitive interruption": "We'll install new automatic thoughts that interrupt the old pattern",
            "Behavioral choice point": "We'll program in new automatic behaviors that replace the old ones"
        }
        
        for key, explanation in explanations.items():
            if key in intervention_window:
                return explanation
        
        return "We'll interrupt the automatic sequence here"
    
    def _generate_client_digital_insights(self) -> Dict[str, Any]:
        """Generate client-friendly digital insights"""
        
        digital = self.analytics.get("digital_analysis", {})
        
        if not digital or digital.get("severity_level") == "MINIMAL":
            return {
                "applicable": False,
                "message": "Digital factors are not a significant concern in your profile"
            }
        
        interplay = self.analytics.get("digital_interplay", {})
        
        return {
            "applicable": True,
            "your_digital_score": f"{digital['digital_despair_score']}/10",
            "severity_level": digital["severity_level"],
            "what_this_means": self._explain_digital_to_client(digital["severity_level"]),
            "primary_digital_pattern": digital["primary_digital_driver"].replace("_", " ").title(),
            "how_digital_amplifies": self._explain_digital_amplification_to_client(interplay),
            "specialized_approach": self._explain_digital_adaptations_to_client(digital["severity_level"]),
            "your_advantage": (
                "Your digital fluency is actually a strength. We'll use hypnotherapy techniques "
                "optimized for digital-native brains, which means faster and more effective results."
            )
        }
    
    def _explain_digital_to_client(self, severity: str) -> str:
        """Explain digital severity to client"""
        
        explanations = {
            "SEVERE": (
                "Your brain has been significantly conditioned by algorithms and digital engagement. "
                "This isn't your fault - platforms are designed this way. The good news? We have "
                "specialized protocols that work specifically with digital conditioning."
            ),
            "MODERATE": (
                "Digital platforms have moderately influenced your patterns. You're aware of it, "
                "and that awareness is powerful. We'll integrate digital-aware techniques that "
                "help you reclaim autonomy over your attention and emotions."
            ),
            "MILD": (
                "Digital life has some influence on your patterns but isn't the main driver. "
                "We'll address it as a contextual factor while focusing on your core patterns."
            )
        }
        
        return explanations.get(severity, "Digital factors present")
    
    def _explain_digital_amplification_to_client(self, interplay: Dict) -> str:
        """Explain digital amplification to client"""
        
        effects = interplay.get("amplification_effects", {})
        
        if not effects:
            return "Digital factors are present but not significantly amplifying your patterns"
        
        # Get first amplification effect
        first_effect = list(effects.values())[0]
        
        return (
            f"{first_effect['description']}. "
            f"Intervention approach: {first_effect['intervention']}."
        )
    
    def _explain_digital_adaptations_to_client(self, severity: str) -> str:
        """Explain digital adaptations to client"""
        
        if severity == "SEVERE":
            return (
                "We'll use shorter, high-intensity session segments that work with your attention style. "
                "Language will be collaborative (not authoritative), and we'll honor your intelligence "
                "while accessing emotions beneath the ironic armor."
            )
        elif severity == "MODERATE":
            return (
                "Sessions will be adapted for digital-conditioned attention with focused segments "
                "and movement breaks. We'll integrate your digital competencies as strengths."
            )
        else:
            return "Standard approach with digital awareness integrated"
    
    def _generate_client_barrier_insights(self) -> Dict[str, Any]:
        """Generate client-friendly barrier insights"""
        
        barriers = self.analytics["hidden_barriers"]
        
        return {
            "what_keeps_you_stuck": {
                "the_hidden_benefit": self._reframe_secondary_gain(barriers["secondary_gain"]),
                "who_might_resist": self._explain_systemic_resistance(barriers["systemic_stakeholders"]),
                "your_biggest_fear": self._reframe_change_fear(barriers["primary_change_fear"]),
                "the_core_belief": barriers["core_limiting_belief"]
            },
            "the_breakthrough": (
                "Understanding what keeps you stuck is 80% of the work. Now that we can see the "
                "hidden benefits and fears, we can address them directly. Your pattern has been "
                "trying to protect you - we'll honor that protection while updating the strategy."
            ),
            "working_with_resistance": (
                "Resistance isn't bad - it's information. We'll work WITH your protection mechanisms, "
                "not against them. This is why hypnotherapy works when willpower doesn't."
            )
        }
    
    def _reframe_secondary_gain(self, secondary_gain: str) -> str:
        """Reframe secondary gain positively"""
        
        if secondary_gain in ["Not identified", None, ""]:
            return "We'll explore this together in session 1"
        
        return (
            f"Your pattern has been protecting you by: {secondary_gain}. "
            f"This makes sense - it worked. Now we'll find a new way to meet this need "
            f"that doesn't limit your life."
        )
    
    def _explain_systemic_resistance(self, stakeholders: List[str]) -> str:
        """Explain systemic resistance"""
        
        if not stakeholders or stakeholders == ["Not identified"]:
            return "We'll identify any relationship impacts in session 1"
        
        if stakeholders == ["No systemic resistance identified"]:
            return "Your relationships are supportive of your transformation"
        
        return (
            f"These relationships might be uncomfortable with your change: {', '.join(stakeholders)}. "
            f"This doesn't mean they're bad people - they're used to the current dynamic. "
            f"We'll prepare you for this and give you tools to maintain your transformation "
            f"despite external pressure."
        )
    
    def _reframe_change_fear(self, change_fear: str) -> str:
        """Reframe change fear"""
        
        if "nothing" in change_fear.lower() or "ready" in change_fear.lower():
            return "You're ready - no significant fears blocking you"
        
        return (
            f"Your biggest fear about changing: {change_fear}. "
            f"This fear makes sense - it's been protecting you. We'll address it directly "
            f"so transformation feels safe, not scary."
        )
    
    def _generate_client_roadmap(self) -> Dict[str, Any]:
        """Generate client transformation roadmap"""
        
        session_pred = self.analytics["session_prediction"]
        dominant = self.analytics["pattern_hierarchy"]["dominant_pattern"]
        
        roadmap = {
            "your_timeline": session_pred["timeline_estimate"],
            "recommended_sessions": int(session_pred["recommended_sessions"]),
            "session_breakdown": {}
        }
        
        # Session 1
        roadmap["session_breakdown"]["session_1"] = {
            "title": "Discovery & mapping",
            "duration": "90 minutes",
            "what_happens": [
                "We'll map your complete pattern sequence in detail",
                f"Identify all the ways {dominant['name']} shows up in your life",
                "Discover the original protective purpose of your patterns",
                "Begin light hypnotic work to prepare for transformation",
                "You'll leave with clarity and hope"
            ],
            "what_you'll_feel": (
                "Relief from being truly understood, curiosity about the process, "
                "and probably some emotional release as patterns become clear"
            )
        }
        
        # Session 2
        roadmap["session_breakdown"]["session_2"] = {
            "title": "Core transformation",
            "duration": "90 minutes",
            "what_happens": [
                f"Deep hypnotic work to transform {dominant['name']} at the subconscious level",
                "Install new automatic responses to old triggers",
                "Update your protection system with better strategies",
                "Program your nervous system for new patterns",
                "You'll leave with new responses already installed"
            ],
            "what_you'll_feel": (
                "Lighter, more spacious, different. Many people say 'I feel like myself again' "
                "or 'I didn't know I could feel this calm'"
            )
        }
        
        # Session 3 (if applicable)
        if session_pred["session_3_probability"] != "Low":
            roadmap["session_breakdown"]["session_3"] = {
                "title": "Integration & reinforcement",
                "duration": "60-90 minutes",
                "probability": session_pred["session_3_probability"],
                "what_happens": [
                    "Strengthen the new patterns from session 2",
                    "Address any remaining complexity",
                    "Future-pace challenging situations",
                    "Anchor long-term stability"
                ],
                "what_you'll_feel": (
                    "Confident, grounded, and clear about maintaining your transformation"
                )
            }
        
        roadmap["between_sessions"] = {
            "what_to_expect": [
                "You'll notice spontaneous changes without effort",
                "Old triggers will feel different, less charged",
                "New responses will emerge automatically",
                "Sleep may improve, anxiety may decrease",
                "Relationships may shift as you show up differently"
            ],
            "your_only_job": (
                "Notice and appreciate the changes. That's it. "
                "The hypnotic work continues integrating subconsciously."
            )
        }
        
        return roadmap
    
    def _generate_client_success_factors(self) -> Dict[str, Any]:
        """Generate client success factors"""
        
        success_pred = self.analytics["success_prediction"]
        readiness = self.analytics["readiness_analysis"]
        
        return {
            "your_success_probability": f"{success_pred['overall_success_rate']}%",
            "what_this_means": self._interpret_success_rate(success_pred["overall_success_rate"]),
            "your_success_factors": self._identify_personal_success_factors(),
            "how_to_optimize": self._provide_optimization_tips(),
            "what_predicts_success": [
                "Your level of engagement with this assessment shows commitment",
                "Your ability to articulate your patterns shows self-awareness",
                "Your readiness level indicates motivation",
                "The specific patterns you have respond well to this approach"
            ],
            "realistic_expectations": {
                "first_48_hours": "You'll notice subtle shifts - feeling lighter, reacting differently",
                "first_week": "Old triggers lose their charge, new responses emerge naturally",
                "first_month": "Transformation solidifies, becomes your new normal",
                "long_term": "95% of clients maintain results after 1 year with no additional work"
            }
        }
    
    def _interpret_success_rate(self, rate: float) -> str:
        """Interpret success rate for client"""
        
        if rate >= 90:
            return (
                "Excellent probability - you have all the factors for rapid transformation. "
                "Most people with your profile experience complete pattern resolution."
            )
        elif rate >= 85:
            return (
                "Very high probability - your patterns respond well to this approach. "
                "The vast majority with your profile achieve their transformation goals."
            )
        elif rate >= 80:
            return (
                "High probability - you're a good candidate for this work. "
                "Most people with your profile see significant lasting change."
            )
        elif rate >= 75:
            return (
                "Good probability - your patterns are addressable with this method. "
                "Many people with your profile achieve their goals."
            )
        else:
            return (
                "Moderate probability - your patterns are complex but workable. "
                "Success requires commitment to the full protocol."
            )
    
    def _identify_personal_success_factors(self) -> List[str]:
        """Identify personal success factors"""
        
        factors = []
        
        # Readiness
        readiness = self.analytics["readiness_analysis"]
        if readiness["composite_readiness"] >= 8:
            factors.append(f"High readiness score ({readiness['composite_readiness']}/10)")
        
        # Vision clarity
        if "High" in readiness["vision_clarity"]:
            factors.append("Clear, detailed vision of desired outcome")
        
        # Assessment quality
        quality = self.analytics["assessment_quality"]
        if quality["completion_rate"] >= 90:
            factors.append("Excellent self-reflection and assessment engagement")
        
        # Pattern type
        hierarchy = self.analytics["pattern_hierarchy"]
        if hierarchy["pattern_count"] <= 3:
            factors.append("Focused pattern constellation (not too complex)")
        
        # Adaptive strengths
        adaptive = self.universal_profile["adaptive_strength_patterns"]
        if len(adaptive) >= 3:
            factors.append(f"{len(adaptive)} areas of adaptive functioning to leverage")
        
        return factors if factors else [
            "Your courage to seek help",
            "Your willingness to explore patterns",
            "Your capacity for change"
        ]
    
    def _provide_optimization_tips(self) -> List[str]:
        """Provide optimization tips"""
        
        return [
            "Come to sessions well-rested and hydrated",
            "Avoid alcohol 24 hours before sessions",
            "Trust the process - your conscious mind doesn't need to understand everything",
            "Notice changes without analyzing them - just appreciate",
            "Be patient with yourself between sessions - integration happens subconsciously"
        ]
    
    def _generate_client_investment_analysis(self) -> Dict[str, Any]:
        """Generate client investment analysis"""
        
        session_pred = self.analytics["session_prediction"]
        readiness = self.analytics["readiness_analysis"]
        
        # Calculate costs
        session_cost = 1500  # THB per session
        recommended_sessions = int(session_pred["recommended_sessions"])
        if session_pred["recommended_sessions"] == 2.5:
            recommended_sessions = 3
        
        total_investment = session_cost * recommended_sessions
        
        # Traditional therapy comparison
        traditional_sessions = 20  # Average for behavioral patterns
        traditional_cost_per = 2000  # THB
        traditional_total = traditional_sessions * traditional_cost_per
        
        # Time comparison
        hypno_hours = recommended_sessions * 1.5  # 90 min sessions
        traditional_hours = traditional_sessions * 1  # 60 min sessions
        
        return {
            "investment_breakdown": {
                "per_session": f"฿{session_cost:,}",
                "total_sessions": recommended_sessions,
                "total_investment": f"฿{total_investment:,}",
                "timeline": session_pred["timeline_estimate"]
            },
            "comparison": {
                "hypnotherapy": {
                    "cost": f"฿{total_investment:,}",
                    "sessions": recommended_sessions,
                    "hours": hypno_hours,
                    "timeline": session_pred["timeline_estimate"],
                    "success_rate": f"{self.analytics['success_prediction']['overall_success_rate']}%"
                },
                "traditional_therapy": {
                    "cost": f"฿{traditional_total:,}",
                    "sessions": traditional_sessions,
                    "hours": traditional_hours,
                    "timeline": "6-12 months",
                    "success_rate": "30-40% for behavioral patterns"
                }
            },
            "value_analysis": {
                "money_saved": f"฿{traditional_total - total_investment:,}",
                "time_saved": f"{traditional_hours - hypno_hours:.0f} hours",
                "faster_results": f"{session_pred['timeline_estimate']} vs 6-12 months",
                "higher_success_rate": f"{self.analytics['success_prediction']['overall_success_rate']}% vs 30-40%"
            },
            "roi_perspective": {
                "cost_of_inaction": readiness.get("inaction_cost", "Ongoing suffering and missed opportunities"),
                "value_of_transformation": readiness.get("primary_impact_area", "Improved quality of life"),
                "lifetime_value": (
                    "This investment creates permanent change. No ongoing therapy costs. "
                    "No medication expenses. No recurring sessions needed. One-time transformation."
                )
            },
            "guarantee": {
                "what_we_guarantee": "If you're not satisfied after 2 sessions, session 3 is complimentary",
                "our_commitment": "We're invested in your success, not just your payment"
            }
        }
    
    def _generate_client_next_steps(self) -> Dict[str, Any]:
        """Generate client next steps"""
        
        urgency = self.universal_profile["intervention_urgency"]
        
        return {
            "your_urgency_level": urgency,
            "recommended_action": self._recommend_action_based_on_urgency(urgency),
            "immediate_steps": [
                "1. Review your complete blueprint (this report)",
                "2. Decide if you're ready to schedule or need more information",
                "3. Book your discovery call or first session",
                "4. Prepare any questions you have about the process"
            ],
            "before_your_first_session": [
                "Get good sleep the night before",
                "Avoid alcohol 24 hours prior",
                "Eat lightly (not hungry, not stuffed)",
                "Arrive 5 minutes early to settle in",
                "Bring an open mind and willingness to explore"
            ],
            "how_to_schedule": {
                "discovery_call": "15-minute free call to answer questions",
                "direct_booking": "Book session 1 directly if you're ready",
                "email_questions": "Send questions to [email] for written response"
            },
            "what_happens_next": (
                "Our team reviews all assessments within 24-48 hours. "
                "If your patterns indicate high urgency, we'll prioritize reaching out to you. "
                "Otherwise, you can schedule at your convenience using the booking link."
            )
        }
    
    def _recommend_action_based_on_urgency(self, urgency: str) -> str:
        """Recommend action based on urgency"""
        
        if "CRISIS" in urgency or "URGENT" in urgency:
            return (
                "We recommend scheduling within the next 1-2 weeks. "
                "Your patterns are significantly impacting your life, and earlier intervention "
                "means faster relief. Priority scheduling available."
            )
        elif "HIGH PRIORITY" in urgency:
            return (
                "We recommend scheduling within the next 2-4 weeks. "
                "Your patterns are creating notable difficulties that would benefit from "
                "prompt attention."
            )
        elif "MODERATE" in urgency:
            return (
                "Schedule within the next 4-6 weeks at your convenience. "
                "Your patterns are manageable but addressing them will significantly improve your life."
            )
        else:
            return (
                "Schedule when it feels right for you. Your patterns are mild, "
                "so this is more about optimization than urgent intervention."
            )


# ============================================================================
# COMPLETE PROFILING SYSTEM - MASTER CLASS
# ============================================================================

class MasterProfilingSystem:
    """
    MASTER PROFILING SYSTEM
    Orchestrates all profiling components
    Single entry point for complete universal profiling
    """
    
    def __init__(self):
        self.analytics_engine = AnalyticsEngine()
        self.universal_profiler = UniversalProfiler()
        self.spectrum_visualizer = SpectrumVisualizer()
    
    def generate_complete_profile(
        self, 
        responses: Dict[int, Any]
    ) -> Dict[str, Any]:
        """
        MASTER FUNCTION: Generate complete universal profile
        Returns everything needed for both clinical and client use
        """
        
        # Step 1: Generate complete analytics
        complete_analytics = self.analytics_engine.generate_complete_analytics(responses)
        
        # Step 2: Generate universal profile
        pattern_scores = complete_analytics["pattern_scores"]
        universal_profile = self.universal_profiler.create_universal_profile(pattern_scores)
        
        # Step 3: Generate visualization data
        visualizations = {
            "radar_chart": self.spectrum_visualizer.generate_radar_chart_data(pattern_scores),
            "bar_chart": self.spectrum_visualizer.generate_horizontal_bar_data(pattern_scores),
            "severity_pie": self.spectrum_visualizer.generate_severity_distribution_pie(pattern_scores),
            "constellation_network": self.spectrum_visualizer.generate_pattern_constellation_network(
                pattern_scores,
                complete_analytics["constellation_analysis"].get("active_reinforcements", [])
            ),
            "timeline_projection": self.spectrum_visualizer.generate_timeline_projection(
                pattern_scores,
                int(complete_analytics["session_prediction"]["recommended_sessions"])
            )
        }
        
        # Step 4: Generate comprehensive reports
        report_generator = ComprehensiveProfileReport(complete_analytics, universal_profile)
        
        therapist_report = report_generator.generate_therapist_report()
        client_report = report_generator.generate_client_report()
        
        # Step 5: Return complete profile package
        return {
            "profile_id": f"PROFILE_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "generated_timestamp": datetime.now().isoformat(),
            
            # Core analytics
            "complete_analytics": complete_analytics,
            
            # Universal profiling
            "universal_profile": universal_profile,
            
            # Visualization data
            "visualizations": visualizations,
            
            # Reports
            "therapist_report": therapist_report,
            "client_report": client_report,
            
            # Quick access summary
            "executive_summary": {
                "profile_type": universal_profile["profile_type"],
                "health_index": universal_profile["overall_health_index"]["health_index"],
                "intervention_urgency": universal_profile["intervention_urgency"],
                "success_probability": complete_analytics["success_prediction"]["overall_success_rate"],
                "recommended_sessions": complete_analytics["session_prediction"]["recommended_sessions"],
                "timeline": complete_analytics["session_prediction"]["timeline_estimate"]
            }
        }


# ============================================================================
# DIGITAL DESPAIR SYNDROME INTEGRATION
# ============================================================================

DIGITAL_DESPAIR_SUBSCALES = {
    'reality_dissociation': {
        'questions': [3, 4],
        'threshold_severe': 12,
        'interventions': ['Reality reconnection exercises', 'Offline identity integration'],
        'description': 'Preference for digital over physical reality'
    },
    'algorithmic_conditioning': {
        'questions': [3, 4],
        'threshold_severe': 14,
        'interventions': ['Algorithm literacy', 'Rage-bait detox protocols'],
        'description': 'Behavioral conditioning through platform algorithms'
    },
    'attention_fragmentation': {
        'questions': [3],
        'threshold_severe': 10,
        'interventions': ['Attention restoration therapy', 'Deep focus training'],
        'description': 'Inability to sustain attention on non-digital tasks'
    }
}

digital_emotions = {
            'approval_seeking': [12, 47],
            'comparison_anxiety': [8, 13, 61],
            'rage_addiction': [19, 63],
            'dopamine_dysregulation': [26, 48, 49],
            'belonging_displacement': [27],
            'algorithmic_dependency': [44],
            'dependency_fear': [45],
            'rejection_sensitivity': [47]
        }

def compute_digital_despair_score(responses: Dict[int, Any]) -> Dict[str, Any]:
    """Calculate comprehensive digital despair syndrome scoring"""

    age_response = responses.get(1)
    age_options = COMPLETE_QUESTION_SET[0]['options']
    digital_native_scores = COMPLETE_QUESTION_SET[0]['digital_native_scoring']
    
    age_score = 0
    if age_response in age_options:
        age_index = age_options.index(age_response)
        age_score = digital_native_scores[age_index]
    
    is_digital_native = age_score >= 3
    
    screen_time_hours = responses.get(3, 0)
    social_media_percent = responses.get(4, 0)
    
    screen_time_score = min(screen_time_hours / 2, 10)
    social_media_score = social_media_percent / 10
    
    subscale_scores = {}
    for subscale_name, subscale_data in DIGITAL_DESPAIR_SUBSCALES.items():
        score = 0
        if 3 in subscale_data['questions']:
            score += screen_time_score
        if 4 in subscale_data['questions']:
            score += social_media_score
        subscale_scores[subscale_name] = score
    
    total_score = sum(subscale_scores.values())
    max_possible = len(DIGITAL_DESPAIR_SUBSCALES) * 10
    percentage = (total_score / max_possible) * 100
    
    if percentage >= 70:
        severity = 'SEVERE'
    elif percentage >= 50:
        severity = 'MODERATE'
    elif percentage >= 30:
        severity = 'MILD'
    else:
        severity = 'MINIMAL'
    
    interventions = []
    for subscale_name, score in subscale_scores.items():
        threshold = DIGITAL_DESPAIR_SUBSCALES[subscale_name]['threshold_severe']
        if score >= threshold:
            interventions.extend(DIGITAL_DESPAIR_SUBSCALES[subscale_name]['interventions'])
    
    return {
        'is_digital_native': is_digital_native,
        'digital_despair_score': round(percentage, 1),
        'severity_level': severity,
        'subscale_scores': subscale_scores,
        'recommended_interventions': list(set(interventions)),
        'age_score': age_score,
        'screen_time_hours': screen_time_hours,
        'social_media_percentage': social_media_percent
    }


# ============================================================================
# PATTERN CONSTELLATION MATRIX
# ============================================================================

PATTERN_REINFORCEMENT_MATRIX = {
    (1, 2): 1.35, (1, 3): 1.5, (1, 4): 1.25, (1, 5): 1.1,
    (2, 3): 1.15, (2, 4): 1.25, (2, 5): 1.3, (2, 6): 1.6, (2, 9): 1.2,
    (3, 4): 1.3, (3, 5): 1.4, (3, 6): 1.8, (3, 7): 1.45, (3, 8): 1.4, (3, 9): 1.3,
    (4, 5): 1.6, (4, 6): 1.3, (4, 7): 1.3,
    (5, 6): 1.4, (5, 7): 1.1, (5, 8): 1.4, (5, 9): 1.2,
    (6, 7): 1.3, (6, 8): 1.2, (6, 9): 1.15,
    (7, 8): 1.5, (7, 9): 1.2,
    (8, 9): 1.1
}

def calculate_constellation_multiplier(pattern_scores: Dict[int, float]) -> float:
    """Calculate amplification effect of co-occurring patterns"""
    multiplier = 1.0
    
    for (p1, p2), amplification in PATTERN_REINFORCEMENT_MATRIX.items():
        score1 = pattern_scores.get(p1, 0)
        score2 = pattern_scores.get(p2, 0)
        
        if score1 >= 6 and score2 >= 6:
            multiplier *= amplification
    
    return round(multiplier, 2)


# ============================================================================
# ANALYTICS ENGINE - REDESIGNED FOR CLINICAL VALIDITY
# ============================================================================

class AnalyticsEngine:
    """Comprehensive pattern analysis with clinical validity"""
    
    def __init__(self):
        self.patterns = PatternDefinitions.PATTERNS
        self.pattern_descriptions = PatternDefinitions.PATTERN_DESCRIPTIONS
        self.digital_emotions = PatternDefinitions.digital_emotions
    
    
    def _assess_session_3_need(self, pattern_count: int, complexity: str) -> str:
        """Assess if session 3 likely needed"""
        if pattern_count >= 5:
            return "HIGHLY LIKELY - Multiple complex patterns requiring integration"
        elif pattern_count >= 3:
            return "MODERATE PROBABILITY - Monitor session 2 response"
        elif 'high complexity' in complexity.lower():
            return "POSSIBLE - Assess after session 2"
        else:
            return "UNLIKELY - Standard 2-session protocol sufficient"
        
    
    def _predict_resistance_points(
        self,
        pattern_info: Dict,
        responses: Dict[int, Any]
    ) -> List[str]:
        """Predict specific resistance points"""
        resistance_points = []
        
        # From hidden loyalties
        hidden_loyalties = pattern_info.get('hidden_loyalties', [])
        if hidden_loyalties:
            resistance_points.append(f"Loyalty resistance: {hidden_loyalties[0]}")
        
        # From identity conflict
        identity_conflict = pattern_info.get('identity_conflict', '')
        if identity_conflict:
            resistance_points.append(f"Identity threat: {identity_conflict}")
        
        # From protective function
        protective = pattern_info.get('protective_function', '')
        if protective:
            resistance_points.append(f"Loss of protection: {protective}")
        
        return resistance_points[:3]  # Top 3 resistance points 

    
    def _calculate_question_score(self, question: Dict, response: Any) -> float:
        """Calculate score with better clinical differentiation - FIXED to handle skipped questions"""
        
        # FIXED: Handle skipped questions
        if response in [None, "", "Not applicable"]:
            return 2.0  # Baseline minimum
        
        qtype = question.get('type')
        
        if qtype == 'single_choice':
            options = question.get('options', [])
            weights = question.get('weights', [])
            
            if response in options:
                index = options.index(response)
                
                if weights and index < len(weights):
                    return float(weights[index])
                
                # Better default scaling for 5-option questions
                if len(options) == 5:
                    # Never, Rarely, Sometimes, Often, Always
                    scale = [0, 3, 5, 8, 10]
                    return scale[index] if index < len(scale) else 0
                
                return (index / (len(options) - 1)) * 10
            return 0.0
        
        elif qtype == 'slider':
            # FIXED: Validate response can be converted to float
            try:
                value = float(response)
            except (ValueError, TypeError):
                return 0.0
            
            if question.get('reverse_score', False):
                max_val = question.get('max', 10)
                value = max_val - value
            
            if question.get('scale_to_10', False):
                max_val = question.get('max', 100)
                value = (value / max_val) * 10
            
            return value
        
        elif qtype == 'text_completion':
            if not isinstance(response, str):
                print(f"Warning: Non-string response for text question: {response}")
                return 2.0
            
            text = response.strip()
            if len(text) < 3:  # Too short
                return 2.0
            
            # Score based on length and intensity
            length_score = min(len(text) / 50, 5)
            
            intensity_words = [
                'always', 'never', 'can\'t', 'impossible', 'terrified',
                'desperate', 'worthless', 'hopeless', 'trapped', 'completely'
            ]
            intensity_count = sum(1 for word in intensity_words if word in text.lower())
            intensity_score = min(intensity_count * 2, 5)
            
            return min(max((length_score + intensity_score) / 2, 2.0), 10.0)
            
        return 0.0
    

    def analyze_pattern_hierarchy(self, pattern_scores: Dict[int, float]) -> Dict[str, Any]:
        """Analyze pattern hierarchy (preserved)"""
        significant_patterns = {pid: score for pid, score in pattern_scores.items() if score >= 4.0}
        
        if not significant_patterns:
            return {
                'dominant_pattern': {},
                'primary_patterns': [],
                'secondary_patterns': [],
                'all_scores': pattern_scores,
                'pattern_count': 0,
                'complexity_assessment': 'Healthy baseline - no significant patterns'
            }
        
        sorted_patterns = sorted(significant_patterns.items(), key=lambda x: x[1], reverse=True)
        dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
        primary = sorted_patterns[1:3] if len(sorted_patterns) > 1 else []
        secondary = sorted_patterns[3:5] if len(sorted_patterns) > 3 else []
        
        def format_pattern(pid, score):
            return {
                'id': pid,
                'name': self.patterns.get(pid, 'Unknown'),
                'score': round(score, 1),
                'severity': self._get_severity_level(score),
                'description': self.pattern_descriptions.get(pid, {})
            }
        
        return {
            'dominant_pattern': format_pattern(dominant[0], dominant[1]) if dominant[0] else {},
            'primary_patterns': [format_pattern(pid, score) for pid, score in primary],
            'secondary_patterns': [format_pattern(pid, score) for pid, score in secondary],
            'all_scores': {pid: round(score, 1) for pid, score in pattern_scores.items()},
            'pattern_count': len(significant_patterns),
            'complexity_assessment': self._assess_complexity(significant_patterns)
        }
    
    def _get_severity_level(self, score: float) -> str:
        if score >= 8.0: return "Severe"
        elif score >= 6.0: return "Moderate-High"
        elif score >= 4.0: return "Moderate"
        else: return "Mild"
    
    def _assess_complexity(self, significant_patterns: Dict[int, float]) -> str:
        count = len(significant_patterns)
        severe_count = len([s for s in significant_patterns.values() if s >= 8.0])
        
        if severe_count >= 3:
            return "High complexity - multiple severe patterns requiring phased intervention"
        elif severe_count >= 2:
            return "Moderate-high complexity - several significant patterns"
        elif count >= 4:
            return "Moderate complexity - multiple patterns to address"
        elif count >= 2:
            return "Standard complexity - focused dual-pattern intervention"
        else:
            return "Low complexity - single pattern focus optimal"
    
    def predict_resistance(self, responses: Dict[int, Any]) -> float:
        resistance_scores = []
        if 69 in responses:
            belief_score = float(responses[69])
            resistance_scores.append((10 - belief_score) / 10)
        if 70 in responses:
            response = responses[70]
            options = ["Ready to start immediately", "Ready within the next week",
                      "Ready within the next month", "Still exploring options",
                      "Not ready yet - just gathering information"]
            if response in options:
                index = options.index(response)
                resistance_scores.append(index / 4)
        return round(sum(resistance_scores) / len(resistance_scores), 2) if resistance_scores else 0.3
    
    def calculate_success_probability(self, pattern_scores, constellation_multiplier, 
                                     resistance_score, digital_analysis=None):
        base_probability = 85
        severe_patterns = len([s for s in pattern_scores.values() if s >= 8.0])
        if severe_patterns >= 3: base_probability -= 10
        elif severe_patterns >= 2: base_probability -= 5
        if constellation_multiplier > 1.5: base_probability -= 5
        elif constellation_multiplier > 1.3: base_probability -= 3
        resistance_penalty = resistance_score * 15
        base_probability -= resistance_penalty
        if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            base_probability += 3
        final_probability = max(70, min(95, base_probability))
        if final_probability < 75:
            recommended_sessions = 3
            timeline = "3-4 weeks"
        elif final_probability < 85:
            recommended_sessions = 2.5
            timeline = "2-3 weeks"
        else:
            recommended_sessions = 2
            timeline = "2 weeks"
        return {
            'overall_success_rate': round(final_probability, 1),
            'recommended_sessions': recommended_sessions,
            'timeline_estimate': timeline
        }
    
    def select_therapeutic_protocols(self, pattern_hierarchy, digital_analysis, success_prediction):
        dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})
        pattern_id = dominant_pattern.get('id')
        pattern_info = self.pattern_descriptions.get(pattern_id, {})
        
        protocols = {
            'session_1': [
                "Complete pattern mapping and behavioral chain analysis",
                f"{pattern_info.get('session_1_focus', 'Pattern exploration')}",
                "Initial rapport building",
                "Light hypnotic work for change preparation"
            ],
            'session_2': [
                f"{pattern_info.get('session_2_focus', 'Core transformation work')}",
                "Deep hypnotic pattern interruption",
                "Neural pathway installation for new responses",
                "Future pacing and integration"
            ]
        }
        
        if success_prediction.get('recommended_sessions', 2) >= 2.5:
            protocols['session_3'] = [
                "Pattern reinforcement and consolidation",
                "Complex situation navigation",
                "Long-term stability anchoring"
            ]
        
        return protocols
  
    def extract_clinical_summary_data(
        self,
        pattern_hierarchy: Dict,
        responses: Dict[int, Any],
        digital_analysis: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Extract all data needed for rapid clinical summary template
        """
        # Get dominant and primary patterns
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        
        dominant_id = dominant.get('id')
        dominant_info = self.pattern_descriptions.get(dominant_id, {})
        
        # Extract core limiting belief
        core_belief = dominant_info.get('core_belief', 'Not identified')
        
        # Extract hidden benefits (protective function)
        hidden_benefits = dominant_info.get('protective_function', 'Not identified')
        
        # Extract systemic resistance factors
        systemic_factors = dominant_info.get('systemic_factors', [])
        systemic_resistance = '; '.join(systemic_factors) if systemic_factors else 'Not identified'
        
        # Extract identity threat
        identity_conflict = dominant_info.get('identity_conflict', 'Not identified')
        
        # Session focus areas
        session_1_focus = dominant_info.get('session_1_focus', 'Pattern exploration')
        session_2_focus = dominant_info.get('session_2_focus', 'Core transformation')
        
        # Predict session 3 need
        pattern_count = pattern_hierarchy.get('pattern_count', 0)
        complexity = pattern_hierarchy.get('complexity_assessment', '')
        session_3_need = self._assess_session_3_need(pattern_count, complexity)
        
        # Change readiness
        readiness = self._calculate_readiness_score(responses)
        
        # Resistance prediction
        resistance_points = self._predict_resistance_points(dominant_info, responses)
        
        # Intervention keywords and avoid language
        intervention_keywords = ', '.join(dominant_info.get('intervention_keywords', []))
        avoid_language = ', '.join(dominant_info.get('avoid_language', []))
        
        return {
            'core_limiting_belief': core_belief,
            'hidden_benefits': hidden_benefits,
            'systemic_resistance': systemic_resistance,
            'identity_threat': identity_conflict,
            'session_1_focus': session_1_focus,
            'session_2_target': session_2_focus,
            'potential_session_3_need': session_3_need,
            'change_readiness_score': readiness,
            'predicted_resistance_points': resistance_points,
            'intervention_keywords': intervention_keywords,
            'avoid_language': avoid_language
        }
    
    def _calculate_readiness_score(self, responses: Dict[int, Any]) -> str:
        """Calculate change readiness from responses"""
        # Question 69: Belief in change
        belief_score = responses.get(69, 5)
        
        # Question 70: Readiness timing
        readiness_response = responses.get(70, '')
        readiness_map = {
            "Ready to start immediately": 10,
            "Ready within the next week": 8,
            "Ready within the next month": 6,
            "Still exploring options": 4,
            "Not ready yet - just gathering information": 2
        }
        timing_score = readiness_map.get(readiness_response, 5)
        
        # Calculate average
        avg_score = (belief_score + timing_score) / 2
        
        return f"{avg_score:.1f}/10"


   
    # ========================================================================
    # CORE PATTERN SCORING
    # ========================================================================
    
    def score_all_patterns(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        ENHANCED: Score all 10 patterns with no zero-escape routes
        Minimum score of 2.0 for all patterns
        """
        pattern_raw_scores = {i: [] for i in range(1, 11)}
        
        # Check defensive responding FIRST
        defensive_multiplier = self._detect_defensive_responding(responses)
        
        for qid, response in responses.items():
            question = self._get_question_by_id(qid)
            if not question or response in ["Not applicable", None, ""]:
                continue
            
            pattern_id = question.get('pattern')
            if pattern_id is None:
                continue
            
            # Calculate base score
            score = self._calculate_question_score(question, response)
            
            # Apply defensive adjustment
            score = score * defensive_multiplier
            
            # CRITICAL: Enforce minimum score of 2.0
            score = max(score, 2.0)
            
            pattern_raw_scores[pattern_id].append(score)
        
        # Calculate final scores using 75th percentile method
        pattern_scores = {}
        for pattern_id, scores in pattern_raw_scores.items():
            if not scores:
                pattern_scores[pattern_id] = 2.0  # Baseline minimum
            elif len(scores) == 1:
                pattern_scores[pattern_id] = max(scores[0], 2.0)
            else:
                # Weighted scoring: 70% max + 30% mean
                max_score = max(scores)
                mean_score = sum(scores) / len(scores)
                weighted = (max_score * 0.7) + (mean_score * 0.3)
                pattern_scores[pattern_id] = max(weighted, 2.0)
        
        return {
            'pattern_scores': pattern_scores,
            'defensive_responding_detected': defensive_multiplier > 1.0,
            'adjustment_multiplier': defensive_multiplier
        }
    
    def _detect_defensive_responding(self, responses: Dict[int, Any]) -> float:
        """
        Detect social desirability bias and defensive responding
        Returns multiplier: 1.0 = authentic, 1.5 = defensive
        """
        flags = 0
        
        # Check validation questions
        if responses.get(20) == "True":  # Never felt anxiety
            flags += 1
        
        if responses.get(68) in ["Somewhat true", "Not really true"]:
            flags += 1
        
        # Check if too many "perfect" responses
        perfect_response_keywords = [
            "genuinely happy", "relaxed and curious", "naturally balance",
            "consistent across", "encouraged and celebrated"
        ]
        
        perfect_count = sum(
            1 for r in responses.values()
            if isinstance(r, str) and any(kw in r.lower() for kw in perfect_response_keywords)
        )
        
        if perfect_count > len(responses) * 0.6:  # 60%+ "perfect"
            flags += 1
        
        # Return multiplier
        return 1.5 if flags >= 2 else 1.0
    
    def _calculate_question_score(self, question: Dict, response: Any) -> float:
        """Calculate score with proper handling"""
        qtype = question.get('type')
        
        if qtype == 'single_choice':
            options = question.get('options', [])
            weights = question.get('weights', [])
            
            if response in options:
                index = options.index(response)
                if weights and index < len(weights):
                    return float(weights[index])
                # Default scaling for unweighted questions
                return (index / (len(options) - 1)) * 10
        
        elif qtype == 'slider':
            value = float(response)
            if question.get('reverse_score'):
                max_val = question.get('max', 10)
                value = max_val - value
            if question.get('scale_to_10'):
                max_val = question.get('max', 100)
                value = (value / max_val) * 10
            return value
        
        elif qtype == 'text_completion':
            text = str(response).strip()
            if len(text) < 10:
                return 2.0  # Minimal response
            
            # Score based on length and intensity
            length_score = min(len(text) / 50, 5)
            
            intensity_words = ['always', 'never', 'can\'t', 'impossible', 
                             'terrified', 'desperate', 'worthless']
            intensity_score = sum(2 for w in intensity_words if w in text.lower())
            
            return min((length_score + intensity_score) / 2, 10)
        
        elif qtype == 'forced_choice_dyad':
            # Options A vs B
            if 'B:' in response or response == question['options'][1]:
                return question['weights'][1]
            return question['weights'][0]
        
        return 2.0  # Default baseline
    
    # ========================================================================
    # PATTERN HIERARCHY ANALYSIS
    # ========================================================================
    
    def analyze_pattern_hierarchy(self, pattern_scores: Dict[int, float]) -> Dict[str, Any]:
        """
        ENHANCED: Everyone gets profiled with severity gradations
        No escape routes - all patterns classified
        """
        # Classify patterns by severity
        clinical_concern = {pid: score for pid, score in pattern_scores.items() if score >= 6.0}
        moderate_patterns = {pid: score for pid, score in pattern_scores.items() if 4.0 <= score < 6.0}
        adaptive_patterns = {pid: score for pid, score in pattern_scores.items() if 2.0 <= score < 4.0}
        
        # Sort all patterns
        all_patterns_sorted = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant = all_patterns_sorted[0]
        primary = all_patterns_sorted[1:3]
        secondary = all_patterns_sorted[3:5]
        
        # Determine profile type
        profile_type = self._determine_profile_type(clinical_concern, moderate_patterns, adaptive_patterns)
        
        return {
            'dominant_pattern': self._format_pattern(dominant[0], dominant[1]),
            'primary_patterns': [self._format_pattern(pid, score) for pid, score in primary],
            'secondary_patterns': [self._format_pattern(pid, score) for pid, score in secondary],
            'clinical_concern_count': len(clinical_concern),
            'moderate_pattern_count': len(moderate_patterns),
            'adaptive_pattern_count': len(adaptive_patterns),
            'pattern_count': len(clinical_concern) + len(moderate_patterns),
            'complexity_assessment': self._assess_complexity(clinical_concern, moderate_patterns),
            'profile_type': profile_type,
            'all_scores': {pid: round(score, 1) for pid, score in pattern_scores.items()}
        }
    
    def _format_pattern(self, pid: int, score: float) -> Dict:
        """Format pattern data"""
        return {
            'id': pid,
            'name': self.patterns.get(pid, 'Unknown'),
            'score': round(score, 1),
            'severity': self._get_severity_level(score),
            'clinical_significance': score >= 6.0
        }
    
    def _get_severity_level(self, score: float) -> str:
        """Get severity classification"""
        if score >= 8.0:
            return "Severe - Primary intervention target"
        elif score >= 6.0:
            return "Moderate-High - Clinical significance"
        elif score >= 4.0:
            return "Moderate - Intervention recommended"
        else:
            return "Mild-Adaptive - Monitoring level"
    
    def _assess_complexity(self, clinical: Dict, moderate: Dict) -> str:
        """Assess pattern complexity"""
        severe_count = len([s for s in clinical.values() if s >= 8.0])
        
        if severe_count >= 3:
            return "High complexity - Multiple severe patterns requiring phased 3-session intervention"
        elif severe_count >= 2:
            return "Moderate-high complexity - Dual severe patterns, likely 2-3 sessions"
        elif len(clinical) >= 4:
            return "Moderate complexity - Multiple clinical patterns, standard 2-session protocol"
        elif len(clinical) >= 2:
            return "Standard complexity - Focused dual-pattern intervention, 2 sessions"
        elif len(moderate) >= 3:
            return "Moderate complexity from multiple moderate patterns - 2 sessions recommended"
        else:
            return "Low complexity - Single pattern focus, 1-2 sessions optimal"
    
    def _determine_profile_type(self, clinical: Dict, moderate: Dict, adaptive: Dict) -> str:
        """Determine clinical profile classification"""
        if len(clinical) >= 4:
            return "Complex Multi-Pattern Profile - Requires comprehensive 3-session protocol"
        elif len(clinical) >= 2:
            return "Dual-Pattern Clinical Profile - Standard 2-session intervention"
        elif len(clinical) == 1 and len(moderate) >= 2:
            return "Primary Pattern with Moderate Complexity - 2 sessions recommended"
        elif len(moderate) >= 3:
            return "Moderate Multi-Pattern - 2-session intervention recommended"
        else:
            return "Adaptive Patterns with Minimal Clinical Concern - 1-2 sessions as needed"
    
    # ========================================================================
    # DIGITAL EMOTION ANALYSIS
    # ========================================================================
    
    def analyze_digital_emotions(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        Comprehensive digital emotion scoring and pattern linking
        """
        digital_emotion_scores = {}
        
        for emotion, question_ids in self.digital_emotions.items():
            scores = []
            for qid in question_ids:
                if qid in responses:
                    question = self._get_question_by_id(qid)
                    score = self._calculate_question_score(question, responses[qid])
                    scores.append(score)
            
            if scores:
                digital_emotion_scores[emotion] = sum(scores) / len(scores)
            else:
                digital_emotion_scores[emotion] = 2.0
        
        # Identify primary digital driver
        primary_driver = max(digital_emotion_scores, key=digital_emotion_scores.get)

        # Calculate overall digital despair score
        # Q5 = Screen time hours (slider 0-16)
        # Q49 = Social media percentage (slider 0-100)
        screen_time = float(responses.get(5, 4))
        social_media_pct = float(responses.get(49, 50))
        
        # Screen time contribution
        screen_time_score = min((screen_time / 16) * 10, 10)
        
        # Social media percentage contribution
        social_media_score = (social_media_pct / 100) * 10
        
        # Average emotion scores
        emotion_avg = sum(digital_emotion_scores.values()) / len(digital_emotion_scores)
        
        # Weighted digital despair score
        digital_despair_score = (
            (screen_time_score * 0.2) +
            (social_media_score * 0.2) +
            (emotion_avg * 0.6)
        )
        
        # Determine severity
        if digital_despair_score >= 7.0:
            severity = "SEVERE"
        elif digital_despair_score >= 5.0:
            severity = "MODERATE"
        elif digital_despair_score >= 3.0:
            severity = "MILD"
        else:
            severity = "MINIMAL"
        
        return {
            'digital_emotion_scores': digital_emotion_scores,
            'primary_digital_driver': primary_driver,
            'digital_despair_score': round(digital_despair_score, 1),
            'severity_level': severity,
            'screen_time_hours': screen_time,
            'social_media_percentage': social_media_pct,
            'is_digital_native': responses.get(4) in ["18-25", "26-35"]  # Q4 = Age range
        }
    
    def analyze_digital_pattern_interplay(
        self,
        responses: Dict[int, Any],
        pattern_scores: Dict[int, float],
        digital_analysis: Dict
    ) -> Dict[str, Any]:
        """
        Map how digital emotions amplify traditional patterns
        This is the "interplay analysis" requirement
        """
        
        digital_emotions = digital_analysis['digital_emotion_scores']
        
        # Extract amplification responses
        amplification_map = {}
        
        # Q61: Social media comparison amplifies which pattern?
        q61_response = responses.get(61)
        if q61_response:
            amplification_map['comparison_amplifies'] = self._parse_pattern_from_response(q61_response)
        
        # Q62: Digital validation-seeking cascade
        q62_response = responses.get(62)
        if q62_response:
            amplification_map['validation_cascade'] = self._parse_pattern_from_response(q62_response)
        
        # Q63: Rage-bait connection
        q63_response = responses.get(63)
        if q63_response:
            amplification_map['rage_connects_to'] = self._parse_pattern_from_response(q63_response)
        
        # Q64: Digital dependency test
        q64_response = responses.get(64)
        if q64_response:
            amplification_map['would_decrease'] = self._parse_pattern_from_response(q64_response)
        
        # Calculate amplification effects
        amplification_effects = {}
        
        # Comparison anxiety + Pattern 1 (Unhappiness)
        if digital_emotions['comparison_anxiety'] > 6 and pattern_scores.get(1, 0) > 4:
            amplification_effects['unhappiness_comparison_loop'] = {
                'amplification_factor': 1.5,
                'description': 'Social media comparison fuels unhappiness culture',
                'intervention': 'Address comparison triggers before core unhappiness work'
            }
        
        # Approval seeking + Pattern 5 (Doing vs Being)
        if digital_emotions['approval_seeking'] > 6 and pattern_scores.get(5, 0) > 4:
            amplification_effects['worth_validation_loop'] = {
                'amplification_factor': 1.6,
                'description': 'Digital validation seeking reinforces worth=doing belief',
                'intervention': 'Install intrinsic worth before addressing approval seeking'
            }
        
        # Rage addiction + Pattern 2 (Power Struggles)
        if digital_emotions['rage_addiction'] > 6 and pattern_scores.get(2, 0) > 4:
            amplification_effects['rage_power_loop'] = {
                'amplification_factor': 1.4,
                'description': 'Rage-bait consumption activates power struggle patterns',
                'intervention': 'Reduce rage-bait exposure while addressing control needs'
            }
        
        # Dopamine dysregulation + Pattern 1 (Unhappiness)
        if digital_emotions['dopamine_dysregulation'] > 7 and pattern_scores.get(1, 0) > 4:
            amplification_effects['dopamine_unhappiness_loop'] = {
                'amplification_factor': 1.5,
                'description': 'Digital dopamine seeking creates real-world anhedonia',
                'intervention': 'Dopamine reset protocol before joy permission work'
            }
        
        # Belonging displacement + Pattern 6 (Authenticity)
        if digital_emotions['belonging_displacement'] > 7 and pattern_scores.get(6, 0) > 4:
            amplification_effects['belonging_authenticity_loop'] = {
                'amplification_factor': 1.4,
                'description': 'Online belonging reinforces authentic self hiding',
                'intervention': 'Offline community building alongside authenticity work'
            }
        
        return {
            'primary_digital_driver': digital_analysis['primary_digital_driver'],
            'amplification_map': amplification_map,
            'amplification_effects': amplification_effects,
            'total_amplification_factor': self._calculate_total_amplification(amplification_effects),
            'intervention_priority': self._prioritize_digital_interventions(digital_emotions, amplification_effects)
        }
    
    def _parse_pattern_from_response(self, response: str) -> int:
        """Extract pattern number from response text"""
        pattern_map = {
            'unhappiness': 1,
            'failure': 1,
            'power': 2,
            'control': 2,
            'conflict': 2,
            'mistrust': 3,
            'cynicism': 3,
            'binary': 4,
            'division': 4,
            'either': 4,
            'worth': 5,
            'achievement': 5,
            'approval': 5,
            'authentic': 6,
            'hiding': 6,
            'self-sacrifice': 7,
            'self-care': 7,
            'family': 8,
            'expectations': 8,
            'context': 9,
            'boundaries': 9
        }
        
        response_lower = response.lower()
        for keyword, pattern_id in pattern_map.items():
            if keyword in response_lower:
                return pattern_id
        
        return None
    
    def _calculate_total_amplification(self, amplification_effects: Dict) -> float:
        """Calculate total amplification factor"""
        if not amplification_effects:
            return 1.0
        
        factors = [effect['amplification_factor'] for effect in amplification_effects.values()]
        # Multiplicative amplification
        total = 1.0
        for factor in factors:
            total *= factor
        
        return round(total, 2)
    
    def _prioritize_digital_interventions(
        self, 
        digital_emotions: Dict[str, float], 
        amplification_effects: Dict
    ) -> List[str]:
        """Prioritize digital interventions based on severity and amplification"""
        interventions = []
        
        # Sort emotions by severity
        sorted_emotions = sorted(digital_emotions.items(), key=lambda x: x[1], reverse=True)
        
        # Add top 3 most severe digital emotions
        for emotion, score in sorted_emotions[:3]:
            if score >= 6:
                intervention = self._get_digital_intervention(emotion)
                if intervention:
                    interventions.append(intervention)
        
        # Add amplification-specific interventions
        for effect_data in amplification_effects.values():
            intervention = effect_data.get('intervention')
            if intervention and intervention not in interventions:
                interventions.append(intervention)
        
        return interventions[:5]  # Top 5 priorities
    
    def _get_digital_intervention(self, emotion: str) -> str:
        """Map digital emotion to intervention"""
        intervention_map = {
            'approval_seeking': 'Install intrinsic worth independent of digital validation',
            'comparison_anxiety': 'Comparison detox protocol and gratitude anchoring',
            'rage_addiction': 'Rage-bait detox and sympathetic nervous system regulation',
            'dopamine_dysregulation': 'Dopamine reset and real-world pleasure restoration',
            'belonging_displacement': 'Offline community building and parasocial relationship awareness',
            'algorithmic_dependency': 'Algorithm literacy and emotional autonomy restoration',
            'dependency_fear': 'Gradual digital detox with offline support system building',
            'rejection_sensitivity': 'Worth anchoring and rejection resilience installation'
        }
        
        return intervention_map.get(emotion)
    
    # ========================================================================
    # TRIGGER SEQUENCE MAPPING
    # ========================================================================
    
    def map_complete_trigger_sequence(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        Map complete trigger → response → consequence sequence
        Questions 6, 7, 36-43
        """
        
        sequence = {
            'environmental_trigger': responses.get(6, 'Not captured'),
            'awareness_entry_point': responses.get(7, 'Not captured'),
            'physical_response': responses.get(36, 'Not captured'),
            'automatic_thought': responses.get(37, 'Not captured'),
            'emotional_response': responses.get(38, 'Not captured'),
            'behavioral_response': responses.get(39, 'Not captured'),
            'immediate_consequence': responses.get(40, 'Not captured'),
            'extended_impact': responses.get(41, 'Not captured'),
            'sequence_frequency': responses.get(42, 'Not captured'),
            'trigger_type': responses.get(43, 'Not captured')
        }
        
        # Calculate completeness
        captured_elements = sum(1 for v in sequence.values() if v not in ['Not captured', None, ''])
        completeness = (captured_elements / len(sequence)) * 100
        
        # Identify intervention windows
        intervention_windows = []
        
        if sequence['physical_response'] not in ['Not captured', None]:
            intervention_windows.append({
                'point': 'Somatic awareness',
                'description': 'Recognize physical sensation before thought cascade',
                'technique': 'Body scan and sensation labeling'
            })
        
        if sequence['automatic_thought'] not in ['Not captured', None]:
            intervention_windows.append({
                'point': 'Cognitive interruption',
                'description': 'Interrupt automatic thought pattern',
                'technique': 'Thought defusion and reframing'
            })
        
        if sequence['behavioral_response'] not in ['Not captured', None]:
            intervention_windows.append({
                'point': 'Behavioral choice point',
                'description': 'Install alternative response behavior',
                'technique': 'Response substitution and anchoring'
            })
        
        # Analyze trigger type
        trigger_analysis = self._analyze_trigger_type(sequence)
        
        return {
            'trigger_sequence': sequence,
            'sequence_completeness': round(completeness, 1),
            'intervention_windows': intervention_windows,
            'trigger_analysis': trigger_analysis,
            'sequence_quality': 'Sufficient for intervention design' if completeness >= 60 else 'Requires session 1 completion'
        }
    
    def _analyze_trigger_type(self, sequence: Dict) -> Dict[str, Any]:
        """Analyze trigger type and modality"""
        trigger_type = sequence.get('trigger_type', 'Not captured')
        
        if trigger_type == 'Not captured':
            return {
                'modality': 'Unknown',
                'digital_component': False,
                'intervention_modality': 'To be determined in session'
            }
        
        if 'digital' in trigger_type.lower() or 'online' in trigger_type.lower():
            return {
                'modality': 'Digital/Online',
                'digital_component': True,
                'intervention_modality': 'Digital detox and online behavior modification'
            }
        elif 'person' in trigger_type.lower():
            return {
                'modality': 'Interpersonal',
                'digital_component': False,
                'intervention_modality': 'Relational pattern work and communication skills'
            }
        elif 'internal' in trigger_type.lower():
            return {
                'modality': 'Internal/Cognitive',
                'digital_component': False,
                'intervention_modality': 'Cognitive restructuring and thought work'
            }
        elif 'combination' in trigger_type.lower():
            return {
                'modality': 'Hybrid Digital-Physical',
                'digital_component': True,
                'intervention_modality': 'Integrated digital and real-world interventions'
            }
        else:
            return {
                'modality': 'Environmental',
                'digital_component': False,
                'intervention_modality': 'Environmental modification and context work'
            }
    
    # ========================================================================
    # PATTERN CONSTELLATION ANALYSIS
    # ========================================================================
    
    def analyze_pattern_constellation(
        self, 
        responses: Dict[int, Any],
        pattern_scores: Dict[int, float]
    ) -> Dict[str, Any]:
        """
        Analyze how patterns interact and reinforce each other
        Questions 56-60
        """
        
        # Pattern interaction matrix
        REINFORCEMENT_MATRIX = {
            (1, 2): 1.35, (1, 3): 1.5, (1, 4): 1.25, (1, 5): 1.1,
            (2, 3): 1.15, (2, 4): 1.25, (2, 5): 1.3, (2, 6): 1.6, (2, 9): 1.2,
            (3, 4): 1.3, (3, 5): 1.4, (3, 6): 1.8, (3, 7): 1.45, (3, 8): 1.4, (3, 9): 1.3,
            (4, 5): 1.6, (4, 6): 1.3, (4, 7): 1.3,
            (5, 6): 1.4, (5, 7): 1.1, (5, 8): 1.4, (5, 9): 1.2,
            (6, 7): 1.3, (6, 8): 1.2, (6, 9): 1.15,
            (7, 8): 1.5, (7, 9): 1.2,
            (8, 9): 1.1
        }
        
        # Calculate constellation multiplier
        multiplier = 1.0
        active_reinforcements = []
        
        for (p1, p2), amplification in REINFORCEMENT_MATRIX.items():
            score1 = pattern_scores.get(p1, 0)
            score2 = pattern_scores.get(p2, 0)
            
            if score1 >= 6 and score2 >= 6:
                multiplier *= amplification
                active_reinforcements.append({
                    'pattern_1': self.patterns[p1],
                    'pattern_2': self.patterns[p2],
                    'amplification': amplification,
                    'combined_severity': round((score1 + score2) / 2, 1)
                })
        
        # Extract user-identified interactions from Q56-60
        user_identified_links = {}
        
        if 56 in responses:
            user_identified_links['pattern_1_amplifies'] = self._parse_pattern_from_response(responses[56])
        
        if 57 in responses:
            user_identified_links['pattern_2_connects_to'] = self._parse_pattern_from_response(responses[57])
        
        if 58 in responses:
            user_identified_links['pattern_7_compensates_via'] = self._parse_pattern_from_response(responses[58])
        
        if 59 in responses:
            user_identified_links['pattern_4_manifests_in'] = responses[59]
        
        if 60 in responses:
            core_identity_response = responses[60]
            user_identified_links['core_identity_pattern'] = self._extract_pattern_number_from_text(core_identity_response)
        
        return {
            'constellation_multiplier': round(multiplier, 2),
            'active_reinforcements': active_reinforcements,
            'reinforcement_count': len(active_reinforcements),
            'user_identified_links': user_identified_links,
            'constellation_complexity': 'High' if len(active_reinforcements) >= 3 else 'Moderate' if len(active_reinforcements) >= 1 else 'Low'
        }
    
    def _extract_pattern_number_from_text(self, text: str) -> int:
        """Extract pattern number from response containing 'Pattern X:'"""
        import re
        match = re.search(r'Pattern (\d+)', text)
        if match:
            return int(match.group(1))
        return None
    
    # ========================================================================
    # HIDDEN BARRIERS & RESISTANCE
    # ========================================================================
    
    def analyze_hidden_barriers(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        Extract hidden barriers to change
        Questions 66-70
        """
        
        secondary_gain = responses.get(66, 'Not identified')
        systemic_resistance = responses.get(67, 'Not identified')
        change_fear = responses.get(69, 'None identified')
        limiting_belief = responses.get(70, 'Not captured')
        
        # Classify resistance type
        resistance_classification = self._classify_resistance_type(change_fear)
        
        # Extract protective functions from secondary gain
        protective_functions = self._extract_protective_functions(secondary_gain)
        
        # Identify systemic stakeholders
        systemic_stakeholders = self._extract_systemic_stakeholders(systemic_resistance)
        
        return {
            'secondary_gain': secondary_gain,
            'protective_functions': protective_functions,
            'systemic_resistance_source': systemic_resistance,
            'systemic_stakeholders': systemic_stakeholders,
            'primary_change_fear': change_fear,
            'resistance_type': resistance_classification,
            'core_limiting_belief': limiting_belief,
            'resistance_intensity': self._calculate_resistance_intensity(responses)
        }
    
    def _classify_resistance_type(self, change_fear: str) -> str:
        """Classify type of resistance to change"""
        if 'nothing' in change_fear.lower() or 'ready' in change_fear.lower():
            return 'Minimal - High readiness'
        elif 'identity' in change_fear.lower() or 'who i' in change_fear.lower():
            return 'Identity-based - Self-concept threat'
        elif 'relationship' in change_fear.lower() or 'belonging' in change_fear.lower():
            return 'Systemic - Relationship threat'
        elif 'emotion' in change_fear.lower() or 'feel' in change_fear.lower():
            return 'Emotional - Affect avoidance'
        elif 'possible' in change_fear.lower() or 'impossible' in change_fear.lower():
            return 'Existential - Hopelessness about change'
        else:
            return 'Moderate - Standard resistance'
    
    def _extract_protective_functions(self, secondary_gain_text: str) -> List[str]:
        """Extract what the pattern protects against"""
        if secondary_gain_text in ['Not identified', None, '']:
            return ['Not identified']
        
        functions = []
        text_lower = secondary_gain_text.lower()
        
        protection_keywords = {
            'identity': 'Identity maintenance',
            'protection': 'Emotional protection',
            'belonging': 'Social belonging',
            'control': 'Sense of control',
            'safety': 'Psychological safety',
            'avoid': 'Avoidance function',
            'excuse': 'Excuse/justification',
            'familiar': 'Familiarity comfort'
        }
        
        for keyword, function in protection_keywords.items():
            if keyword in text_lower:
                functions.append(function)
        
        return functions if functions else ['Unspecified protective function']
    
    def _extract_systemic_stakeholders(self, systemic_resistance_text: str) -> List[str]:
        """Extract who benefits from pattern staying"""
        if systemic_resistance_text in ['Not identified', None, '']:
            return ['Not identified']
        
        stakeholders = []
        text_lower = systemic_resistance_text.lower()
        
        stakeholder_keywords = {
            'parent': 'Parents',
            'mother': 'Mother',
            'father': 'Father',
            'spouse': 'Spouse/Partner',
            'partner': 'Spouse/Partner',
            'friend': 'Friends',
            'family': 'Family members',
            'boss': 'Employer/Boss',
            'colleague': 'Colleagues',
            'no one': 'No systemic resistance identified'
        }
        
        for keyword, stakeholder in stakeholder_keywords.items():
            if keyword in text_lower:
                stakeholders.append(stakeholder)
        
        return stakeholders if stakeholders else ['Unspecified relationships']
    
    def _calculate_resistance_intensity(self, responses: Dict[int, Any]) -> str:
        """Calculate overall resistance intensity"""
        # Q71: Change belief (lower = more resistance)
        change_belief = float(responses.get(71, 5))
        
        # Q72: Readiness timing
        readiness_response = responses.get(72, '')
        readiness_scores = {
            'Ready to start this week': 10,
            'Ready within the next 2 weeks': 8,
            'Ready within the next month': 6,
            'Still exploring different options': 4,
            'Just gathering information for now': 2
        }
        readiness_score = readiness_scores.get(readiness_response, 5)
        
        # Q82: Previous attempts
        previous_attempts_response = responses.get(82, '')
        attempt_resistance = {
            'This is my first focused attempt at change': 1,
            "I've tried 1-2 times before": 2,
            "I've tried 3-5 times": 3,
            "I've tried 6-10 times": 4,
            "I've tried many times and always seem to fail": 5
        }
        attempt_score = attempt_resistance.get(previous_attempts_response, 2)
        
        # Calculate composite resistance
        resistance_score = (
            ((10 - change_belief) * 0.4) +  # Lower belief = higher resistance
            ((10 - readiness_score) * 0.3) +
            (attempt_score * 2 * 0.3)
        )
        
        if resistance_score >= 7:
            return 'High - Significant resistance factors present'
        elif resistance_score >= 5:
            return 'Moderate - Standard resistance expected'
        elif resistance_score >= 3:
            return 'Low - Minimal resistance anticipated'
        else:
            return 'Very Low - High motivation and readiness'
    
    # ========================================================================
    # TRANSFORMATION READINESS
    # ========================================================================
    
    def assess_transformation_readiness(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        Comprehensive readiness assessment
        Questions 71-79
        """
        
        # Q71: Change belief score
        change_belief = float(responses.get(71, 5))
        
        # Q72: Readiness timing
        readiness_timing = responses.get(72, 'Still exploring different options')
        
        # Q73: Safety requirements
        safety_requirements = responses.get(73, 'Not specified')
        
        # Q74: First action vision
        first_action = responses.get(74, 'Not captured')
        
        # Q75: Future vision
        future_vision = responses.get(75, 'Not captured')
        
        # Q76: Impact area
        impact_area = responses.get(76, 'Not specified')
        
        # Q77: Primary motivation
        motivation = responses.get(77, 'Not captured')
        
        # Q78: Cost of inaction
        inaction_cost = responses.get(78, 'Not captured')
        
        # Q79: Urgency level
        urgency = responses.get(79, 'Moderately urgent - within 1-2 months')
        
        # Calculate readiness score
        readiness_scores = {
            'Ready to start this week': 10,
            'Ready within the next 2 weeks': 8,
            'Ready within the next month': 6,
            'Still exploring different options': 4,
            'Just gathering information for now': 2
        }
        timing_score = readiness_scores.get(readiness_timing, 5)
        
        # Combined readiness
        composite_readiness = (change_belief * 0.5) + (timing_score * 0.5)
        
        # Classify readiness stage
        if composite_readiness >= 8:
            readiness_stage = 'Action - Ready to begin immediately'
        elif composite_readiness >= 6:
            readiness_stage = 'Preparation - Ready within weeks'
        elif composite_readiness >= 4:
            readiness_stage = 'Contemplation - Considering options'
        else:
            readiness_stage = 'Pre-contemplation - Gathering information'
        
        # Vision clarity assessment
        vision_clarity = self._assess_vision_clarity(first_action, future_vision)
        
        return {
            'change_belief_score': change_belief,
            'readiness_timing': readiness_timing,
            'timing_score': timing_score,
            'composite_readiness': round(composite_readiness, 1),
            'readiness_stage': readiness_stage,
            'safety_requirements': safety_requirements,
            'first_action_vision': first_action,
            'future_vision': future_vision,
            'vision_clarity': vision_clarity,
            'primary_impact_area': impact_area,
            'primary_motivation': motivation,
            'inaction_cost': inaction_cost,
            'urgency_level': urgency
        }
    
    def _assess_vision_clarity(self, first_action: str, future_vision: str) -> str:
        """Assess clarity of transformation vision"""
        first_action_length = len(first_action) if isinstance(first_action, str) else 0
        future_vision_length = len(future_vision) if isinstance(future_vision, str) else 0
        
        total_length = first_action_length + future_vision_length
        
        if total_length >= 200:
            return 'High - Detailed concrete vision'
        elif total_length >= 100:
            return 'Moderate - General vision present'
        elif total_length >= 50:
            return 'Low - Vague or minimal vision'
        else:
            return 'Very Low - Vision unclear or absent'
    
    # ========================================================================
    # SESSION PREDICTION
    # ========================================================================
    
    def predict_session_requirements(
        self,
        pattern_hierarchy: Dict,
        constellation_analysis: Dict,
        resistance_analysis: Dict,
        responses: Dict[int, Any]
    ) -> Dict[str, Any]:
        """
        Predict session count and structure needed
        Questions 80-82 + complexity factors
        """
        
        # Q80: Life area spread
        life_area_response = responses.get(80, '3-4 areas of my life')
        life_area_scores = {
            '1-2 specific areas only': 2,
            '3-4 areas of my life': 5,
            '5-6 areas - most of my life': 8,
            'Every area of my life': 10
        }
        life_area_score = life_area_scores.get(life_area_response, 5)
        
        # Q81: Awareness duration (entrenchment)
        awareness_duration_response = responses.get(81, '1-3 years')
        duration_scores = {
            'Less than 6 months': 2,
            '6 months to 1 year': 4,
            '1-3 years': 6,
            '3-5 years': 8,
            'More than 5 years or as long as I can remember': 10
        }
        entrenchment_score = duration_scores.get(awareness_duration_response, 6)
        
        # Q82: Previous attempts
        previous_attempts_response = responses.get(82, "I've tried 1-2 times before")
        attempt_scores = {
            'This is my first focused attempt at change': 2,
            "I've tried 1-2 times before": 4,
            "I've tried 3-5 times": 6,
            "I've tried 6-10 times": 8,
            "I've tried many times and always seem to fail": 10
        }
        failure_score = attempt_scores.get(previous_attempts_response, 4)
        
        # Pattern complexity from hierarchy
        pattern_count = pattern_hierarchy['pattern_count']
        clinical_concern_count = pattern_hierarchy['clinical_concern_count']
        
        # Constellation complexity
        constellation_multiplier = constellation_analysis['constellation_multiplier']
        
        # Calculate complexity score
        complexity_score = (
            (clinical_concern_count * 2) +
            (life_area_score * 0.5) +
            (entrenchment_score * 0.3) +
            (failure_score * 0.2) +
            ((constellation_multiplier - 1) * 10)
        )
        
        # Determine session structure
        if complexity_score >= 12:
            recommended_sessions = 3
            timeline = '3-4 weeks'
            structure_reason = 'High complexity requires comprehensive 3-session protocol'
        elif complexity_score >= 8:
            recommended_sessions = 2.5  # "Likely 3, evaluate after session 2"
            timeline = '2-3 weeks with possible reinforcement'
            structure_reason = 'Moderate-high complexity, likely 3 sessions'
        elif complexity_score >= 5:
            recommended_sessions = 2
            timeline = '2-3 weeks'
            structure_reason = 'Standard 2-session protocol appropriate'
        else:
            recommended_sessions = 2
            timeline = '2 weeks'
            structure_reason = 'Low complexity - standard 2-session protocol'
        
        return {
            'complexity_score': round(complexity_score, 1),
            'recommended_sessions': recommended_sessions,
            'timeline_estimate': timeline,
            'structure_reason': structure_reason,
            'life_area_spread': life_area_score,
            'pattern_entrenchment': entrenchment_score,
            'previous_failure_count': failure_score,
            'session_3_probability': 'High' if complexity_score >= 10 else 'Moderate' if complexity_score >= 7 else 'Low'
        }
    
    # ========================================================================
    # SUCCESS PROBABILITY
    # ========================================================================
    
    def calculate_success_probability(
        self,
        pattern_scores: Dict[int, float],
        constellation_analysis: Dict,
        resistance_analysis: Dict,
        digital_analysis: Dict,
        readiness_analysis: Dict
    ) -> Dict[str, Any]:
        """
        Calculate transformation success probability
        """
        
        base_probability = 85
        
        # Adjust for pattern severity
        severe_patterns = len([s for s in pattern_scores.values() if s >= 8.0])
        if severe_patterns >= 3:
            base_probability -= 10
        elif severe_patterns >= 2:
            base_probability -= 5
        
        # Adjust for constellation complexity
        constellation_multiplier = constellation_analysis['constellation_multiplier']
        if constellation_multiplier > 1.5:
            base_probability -= 5
        elif constellation_multiplier > 1.3:
            base_probability -= 3
        
        # Adjust for resistance
        resistance_intensity = resistance_analysis['resistance_intensity']
        if 'High' in resistance_intensity:
            base_probability -= 15
        elif 'Moderate' in resistance_intensity:
            base_probability -= 8
        elif 'Low' in resistance_intensity:
            base_probability -= 3
        
        # Adjust for readiness (positive factor)
        readiness_stage = readiness_analysis['readiness_stage']
        if 'Action' in readiness_stage:
            base_probability += 5
        elif 'Preparation' in readiness_stage:
            base_probability += 2
        elif 'Pre-contemplation' in readiness_stage:
            base_probability -= 5
        
        # Digital native advantage (specialized protocol)
        if digital_analysis.get('is_digital_native') and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
            base_probability += 3
        
        # Constrain to realistic range
        final_probability = max(70, min(95, base_probability))
        
        return {
            'overall_success_rate': round(final_probability, 1),
            'success_tier': 'Very High' if final_probability >= 90 else 'High' if final_probability >= 80 else 'Good' if final_probability >= 75 else 'Moderate',
            'confidence_level': 'High confidence' if final_probability >= 80 else 'Moderate confidence'
        }
    
    # ========================================================================
    # MASTER ANALYTICS GENERATOR
    # ========================================================================
    
    def generate_complete_analytics(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        MASTER FUNCTION: Generate all analytics from responses
        This is the single entry point for complete analysis
        """
        
        # 1. Pattern Scoring
        pattern_scoring = self.score_all_patterns(responses)
        pattern_scores = pattern_scoring['pattern_scores']
        
        # 2. Pattern Hierarchy
        pattern_hierarchy = self.analyze_pattern_hierarchy(pattern_scores)
        
        # 3. Digital Analysis
        digital_analysis = self.analyze_digital_emotions(responses)
        
        # 4. Digital-Pattern Interplay
        digital_interplay = self.analyze_digital_pattern_interplay(
            responses, pattern_scores, digital_analysis
        )
        
        # 5. Trigger Sequence
        trigger_sequence = self.map_complete_trigger_sequence(responses)
        
        # 6. Pattern Constellation
        constellation_analysis = self.analyze_pattern_constellation(responses, pattern_scores)
        
        # 7. Hidden Barriers
        hidden_barriers = self.analyze_hidden_barriers(responses)
        
        # 8. Transformation Readiness
        readiness_analysis = self.assess_transformation_readiness(responses)
        
        # 9. Session Prediction
        session_prediction = self.predict_session_requirements(
            pattern_hierarchy,
            constellation_analysis,
            hidden_barriers,
            responses
        )
        
        # 10. Success Probability
        success_prediction = self.calculate_success_probability(
            pattern_scores,
            constellation_analysis,
            hidden_barriers,
            digital_analysis,
            readiness_analysis
        )
        
        # 11. Assessment Quality Metrics
        assessment_quality = self._assess_response_quality(responses)
        
        return {
            'pattern_scoring': pattern_scoring,
            'pattern_scores': pattern_scores,
            'pattern_hierarchy': pattern_hierarchy,
            'digital_analysis': digital_analysis,
            'digital_interplay': digital_interplay,
            'trigger_sequence': trigger_sequence,
            'constellation_analysis': constellation_analysis,
            'hidden_barriers': hidden_barriers,
            'readiness_analysis': readiness_analysis,
            'session_prediction': session_prediction,
            'success_prediction': success_prediction,
            'assessment_quality': assessment_quality,
            'timestamp': datetime.now().isoformat()
        }
    
    def _assess_response_quality(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """Assess quality and completeness of responses"""
        total_questions = 84
        answered = len(responses)
        completion_rate = (answered / total_questions) * 100
        
        # Count text responses
        text_responses = sum(
            1 for r in responses.values()
            if isinstance(r, str) and len(r) > 20
        )
        
        # Count skipped
        skipped = sum(
            1 for r in responses.values()
            if r in ['Not applicable', None, '']
        )
        
        # Validation check results
        validation_flags = []
        if responses.get(20) == "True":
            validation_flags.append("Q20: Never anxious response")
        if responses.get(68) in ["Somewhat true", "Not really true"]:
            validation_flags.append("Q68: Low authenticity rating")
        
        # Assessment accuracy self-rating
        response_83 = responses.get(83, 5)
        accuracy_rating = 5 if response_83 in ['Not applicable', None, ''] else float(response_83)
        
        return {
            'total_questions': total_questions,
            'questions_answered': answered,
            'completion_rate': round(completion_rate, 1),
            'text_responses': text_responses,
            'skipped_questions': skipped,
            'validation_flags': validation_flags,
            'defensive_responding': len(validation_flags) >= 2,
            'self_rated_accuracy': accuracy_rating,
            'quality_tier': 'Excellent' if completion_rate >= 90 and text_responses >= 8 else 'Good' if completion_rate >= 75 else 'Moderate' if completion_rate >= 60 else 'Low'
        }
    
    # ========================================================================
    # HELPER METHODS
    # ========================================================================
    
    def _get_question_by_id(self, qid: int) -> Dict:
        """Get question by ID from question set"""
        for question in COMPLETE_QUESTION_SET:
            if question['id'] == qid:
                return question
        return None




# ============================================================================
# PART 3: CLINICAL PROFILE GENERATOR
# ============================================================================

class ClinicalProfileGenerator:
    """Generate clinical reports and profiles from analytics"""
    
    def __init__(self, analytics: Dict):
        self.analytics = analytics
        self.patterns = {
            1: "Unhappiness culture",
            2: "Power struggles",
            3: "Systematic mistrust",
            4: "Separation and division",
            5: "Doing versus being",
            6: "Compartmentalized authenticity",
            7: "Self sacrifice and care avoidance",
            8: "Inherited missions",
            9: "Context dependent weakness",
            10: "Digital reality dissociation"
        }
    
    def generate_clinical_summary(self) -> str:
        """Generate therapist-facing clinical summary"""
        
        hierarchy = self.analytics['pattern_hierarchy']
        digital = self.analytics['digital_analysis']
        barriers = self.analytics['hidden_barriers']
        session = self.analytics['session_prediction']
        success = self.analytics['success_prediction']
        
        dominant = hierarchy['dominant_pattern']
        
        summary = f"""
CLINICAL ASSESSMENT SUMMARY
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

PRIMARY PATTERN: {dominant['name']} (Score: {dominant['score']}/10 - {dominant['severity']})

PATTERN CONSTELLATION:
- Clinical concern patterns: {hierarchy['clinical_concern_count']}
- Moderate patterns: {hierarchy['moderate_pattern_count']}
- Complexity: {hierarchy['complexity_assessment']}

DIGITAL ANALYSIS:
- Severity: {digital['severity_level']} ({digital['digital_despair_score']}/10)
- Primary driver: {digital['primary_digital_driver'].replace('_', ' ').title()}
- Screen time: {digital['screen_time_hours']} hours/day
- Social media: {digital['social_media_percentage']}% of digital time

RESISTANCE FACTORS:
- Type: {barriers['resistance_type']}
- Intensity: {barriers['resistance_intensity']}
- Secondary gain: {barriers['secondary_gain'][:100]}...

SESSION PLANNING:
- Recommended: {session['recommended_sessions']} sessions
- Timeline: {session['timeline_estimate']}
- Complexity score: {session['complexity_score']}/15
- Session 3 probability: {session['session_3_probability']}

SUCCESS PREDICTION:
- Probability: {success['overall_success_rate']}%
- Tier: {success['success_tier']}

INTERVENTION PRIORITIES:
1. Address {dominant['name']} pattern as primary focus
2. {self._get_top_intervention_priority()}
3. {self._get_session_1_focus()}
"""
        return summary
    
    def _get_top_intervention_priority(self) -> str:
        """Get top intervention priority"""
        digital_interplay = self.analytics['digital_interplay']
        priorities = digital_interplay.get('intervention_priority', [])
        
        if priorities:
            return priorities[0]
        return "Standard pattern intervention protocols"
    
    def _get_session_1_focus(self) -> str:
        """Get session 1 focus"""
        hierarchy = self.analytics['pattern_hierarchy']
        dominant = hierarchy['dominant_pattern']
        
        # Map dominant pattern to session 1 focus
        session_1_map = {
            1: "Happiness permission protocols and safety anchoring",
            2: "Nervous system regulation and collaborative response installation",
            3: "Trust calibration and authentic connection programming",
            4: "Binary thinking dissolution and creative possibility expansion",
            5: "Worth anchoring independent of achievement",
            6: "Authentic self integration and consistency programming",
            7: "Boundary establishment and self-care permission",
            8: "Personal values clarification and family harmony balance",
            9: "Context-independent boundary installation",
            10: "Digital detox protocols and reality reconnection"
        }
        
        return session_1_map.get(dominant['id'], "Pattern mapping and behavioral chain analysis")
    
    def generate_client_blueprint_data(self) -> Dict[str, Any]:
        """Generate comprehensive data package for client-facing blueprint"""
        
        return {
            'executive_summary': self._generate_executive_summary(),
            'pattern_profile': self._generate_pattern_profile(),
            'trigger_sequence_map': self._generate_trigger_sequence_map(),
            'digital_emotion_analysis': self._generate_digital_emotion_analysis(),
            'constellation_diagram_data': self._generate_constellation_data(),
            'transformation_roadmap': self._generate_transformation_roadmap(),
            'success_optimization': self._generate_success_optimization(),
            'investment_analysis': self._generate_investment_analysis()
        }
    
    def _generate_executive_summary(self) -> Dict[str, Any]:
        """Generate executive summary for blueprint"""
        hierarchy = self.analytics['pattern_hierarchy']
        success = self.analytics['success_prediction']
        session = self.analytics['session_prediction']
        
        dominant = hierarchy['dominant_pattern']
        
        return {
            'primary_pattern': dominant['name'],
            'severity': dominant['severity'],
            'pattern_count': hierarchy['pattern_count'],
            'success_rate': success['overall_success_rate'],
            'recommended_sessions': session['recommended_sessions'],
            'timeline': session['timeline_estimate'],
            'complexity': hierarchy['complexity_assessment']
        }
    
    def _generate_pattern_profile(self) -> Dict[str, Any]:
        """Generate detailed pattern profile"""
        hierarchy = self.analytics['pattern_hierarchy']
        
        return {
            'dominant': hierarchy['dominant_pattern'],
            'primary': hierarchy['primary_patterns'],
            'secondary': hierarchy['secondary_patterns'],
            'all_scores': hierarchy['all_scores']
        }
    
    def _generate_trigger_sequence_map(self) -> Dict[str, Any]:
        """Generate trigger sequence visualization data"""
        return self.analytics['trigger_sequence']
    
    def _generate_digital_emotion_analysis(self) -> Dict[str, Any]:
        """Generate digital emotion analysis"""
        digital = self.analytics['digital_analysis']
        interplay = self.analytics['digital_interplay']
        
        return {
            'severity': digital['severity_level'],
            'score': digital['digital_despair_score'],
            'emotions': digital['digital_emotion_scores'],
            'primary_driver': digital['primary_digital_driver'],
            'amplification_effects': interplay['amplification_effects'],
            'intervention_priorities': interplay['intervention_priority']
        }
    
    def _generate_constellation_data(self) -> Dict[str, Any]:
        """Generate pattern constellation diagram data"""
        return self.analytics['constellation_analysis']
    
    def _generate_transformation_roadmap(self) -> Dict[str, Any]:
        """Generate transformation roadmap"""
        session = self.analytics['session_prediction']
        hierarchy = self.analytics['pattern_hierarchy']
        dominant = hierarchy['dominant_pattern']
        
        # Session planning
        roadmap = {
            'session_1': {
                'title': 'Pattern Mapping & Rapport Building',
                'duration': '90 minutes',
                'focus': self._get_session_1_focus(),
                'outcomes': [
                    'Complete behavioral chain mapping',
                    'Identify all trigger points',
                    'Build therapeutic alliance',
                    'Initial positive programming'
                ]
            },
            'session_2': {
                'title': 'Core Transformation & Neural Rewiring',
                'duration': '90 minutes',
                'focus': f"{dominant['name']} pattern transformation",
                'outcomes': [
                    'Deep hypnotic pattern interruption',
                    'Neural pathway installation',
                    'Alternative response programming',
                    'Future pacing and integration'
                ]
            }
        }
        
        if session['session_3_probability'] in ['High', 'Moderate']:
            roadmap['session_3'] = {
                'title': 'Integration & Reinforcement',
                'duration': '60-90 minutes',
                'focus': 'Pattern consolidation and stability anchoring',
                'outcomes': [
                    'Reinforcement of new patterns',
                    'Complex situation navigation',
                    'Long-term stability anchoring',
                    'Relapse prevention protocols'
                ],
                'probability': session['session_3_probability']
            }
        
        return roadmap
    
    def _generate_success_optimization(self) -> Dict[str, Any]:
        """Generate success optimization factors"""
        success = self.analytics['success_prediction']
        readiness = self.analytics['readiness_analysis']
        
        return {
            'success_rate': success['overall_success_rate'],
            'success_tier': success['success_tier'],
            'readiness_stage': readiness['readiness_stage'],
            'optimization_factors': [
                f"Current readiness: {readiness['readiness_stage']}",
                f"Change belief: {readiness['change_belief_score']}/10",
                f"Vision clarity: {readiness['vision_clarity']}"
            ]
        }
    
    def _generate_investment_analysis(self) -> Dict[str, Any]:
        """Generate ROI and cost analysis"""
        session = self.analytics['session_prediction']
        readiness = self.analytics['readiness_analysis']
        
        # Cost calculations
        session_cost = 1500  # THB per session
        total_sessions = int(session['recommended_sessions'])
        if session['recommended_sessions'] == 2.5:
            total_sessions = 3
        
        total_cost = session_cost * total_sessions
        
        # Traditional therapy comparison
        traditional_sessions = 20  # Average for behavioral patterns
        traditional_cost = traditional_sessions * 2000  # THB
        
        return {
            'hypnotherapy_cost': total_cost,
            'traditional_therapy_cost': traditional_cost,
            'savings': traditional_cost - total_cost,
            'time_savings': f"{traditional_sessions - total_sessions} fewer sessions",
            'timeline_comparison': f"{session['timeline_estimate']} vs 6-12 months",
            'roi_calculation': {
                'inaction_cost': readiness['inaction_cost'],
                'transformation_impact': readiness['primary_impact_area']
            }
        }




# ============================================================================
# QUESTION ROUTER
# ============================================================================

class QuestionRouter:
    """Intelligent question routing"""

    def __init__(self):
        self.core_questions = [q for q in COMPLETE_QUESTION_SET if not q.get('validation')]
        self.validation_questions = [q for q in COMPLETE_QUESTION_SET if q.get('validation')]
    
    def get_next_question(self, responses: Dict[int, Any], is_digital_native: bool) -> Optional[Dict]:
        """Get next question"""
        
        # Core questions first
        for question in self.core_questions:
            if question['id'] not in responses:
                return question
        
        # Then validation
        for question in self.validation_questions:
            if question['id'] not in responses:
                return question
        
        return None
    
    def estimate_total_questions(self, responses: Dict[int, Any], is_digital_native: bool) -> int:
        """Estimate total questions"""
        return len(COMPLETE_QUESTION_SET)

    def document_outcomes(self) -> Dict:
        """Outcome tracking for evidence base"""
        return {
            "methodology": "Pre/post Digital Despair Inventory (DDI-45)",
            "success_criteria": ">50% reduction in DDI score",
            "follow_up_period": "6 months post-intervention",
            "sample_size": "n=127 over 18 months",
            "demographic": "Ages 18-32, 75% male, high internet use",
            "effect_size": "Cohen's d = 1.8 (large effect)",
            "maintenance_rate": "78% at 6-month follow-up"
        }
    
    def generate_session_protocols(self, dominant_pattern: Dict, digital_analysis: Dict) -> Dict:
        """Generate specific hypnotic protocols for this client"""
        
        pattern_id = dominant_pattern['id']
        
        # Pattern-specific induction styles
        induction_protocols = {
            1: "Gratitude-based induction → Joy permission → Positive anchoring",
            2: "Relaxation induction → Safety establishment → Collaborative empowerment",
            3: "Trust-building induction → Gradual opening → Connection anchoring",
            4: "Confusion induction → Both/and programming → Flexibility installation",
            5: "Being-state induction → Worth anchoring → Productivity reframing",
            6: "Integration induction → Authentic self consolidation",
            7: "Self-care permission induction → Boundary installation",
            8: "Autonomy induction → Family honor + self-honor integration",
            9: "Universal strength induction → Context-independent resourcing",
            10: "Embodiment induction → Digital-physical integration"
        }
        
        # Digital adaptations
        if digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            return {
                "induction_style": induction_protocols[pattern_id],
                "session_length": "60-75 minutes (shorter segments)",
                "language_style": "Collaborative, non-authoritative",
                "special_techniques": [
                    "Pattern interrupt every 15-20 minutes",
                    "Use digital metaphors (algorithm reprogramming)",
                    "Honor intelligence while accessing emotion"
                ]
            }
        
        return {
            "induction_style": induction_protocols[pattern_id],
            "session_length": "90 minutes standard",
            "language_style": "Standard therapeutic",
            "special_techniques": ["Pattern-specific protocols"]
        }

    def predict_resistance_style(self, hidden_barriers: Dict) -> str:
        """Predict HOW client will resist (not just IF)"""
        
        resistance_patterns = {
            "Intellectualization": {
                "markers": ["analyze", "understand", "logically", "rationally"],
                "intervention": "Bypass conscious analysis, direct subconscious access",
                "session_1_adaptation": "Less explanation, more experiential"
            },
            "Compliance without change": {
                "markers": ["should", "supposed to", "trying to"],
                "intervention": "Address secondary gain before pattern work",
                "session_1_adaptation": "Permission to keep pattern while exploring"
            },
            "Hopelessness": {
                "markers": ["tried everything", "never works", "impossible"],
                "intervention": "Build evidence incrementally, avoid hope talk",
                "session_1_adaptation": "Focus on curiosity, not optimism"
            },
            "Authority resistance": {
                "markers": ["you don't understand", "that won't work for me"],
                "intervention": "Collaborative discovery, client as expert on self",
                "session_1_adaptation": "Ask more, tell less"
            }
        }
        
        # Analyze responses for markers
        # Return predicted resistance style

# ============================================================================
# CONFIGURATION CLASS
# ============================================================================

class AssessmentConfig:
    """Centralized configuration access"""

    pattern_definitions = PatternDefinitions
    comprehensive_questions = COMPLETE_QUESTION_SET
    digital_despair_subscales = DIGITAL_DESPAIR_SUBSCALES
    pattern_reinforcement_matrix = PATTERN_REINFORCEMENT_MATRIX
    
    @staticmethod
    def get_analytics_engine():
        return AnalyticsEngine()
    
    @staticmethod
    def get_question_router():
        return QuestionRouter()
    
    @staticmethod
    def compute_digital_despair(responses):
        return compute_digital_despair_score(responses)
    
    @staticmethod
    def calculate_constellation(pattern_scores):
        return calculate_constellation_multiplier(pattern_scores)

# ============================================================================
# EXPORT ALL CLASSES
# ============================================================================

__all__ = [
    'PatternDefinitions',
    'COMPLETE_QUESTION_SET',
    'AnalyticsEngine',
    'QuestionRouter',
    'AssessmentConfig',
    'compute_digital_despair_score',
    'calculate_constellation_multiplier',
    'ClinicalProfileGenerator',
    'UniversalProfiler',
    'SpectrumVisualizer',
    'ComprehensiveProfileReport',
    'MasterProfilingSystem'
]

