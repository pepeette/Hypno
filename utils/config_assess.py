
"""
Clinical Behavioral Pattern Assessment - Enhanced Configuration & Analytics
Version 3.5 - Complete Clinical Data Extraction

Extracts:
- Root pattern structures
- Systemic factors maintaining problems
- Identity conflicts blocking change
- Hidden loyalties creating resistance
- Complete trigger sequences
- Intervention keywords and avoid language
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import re
import math

# ============================================================================
# ENHANCED PATTERN DEFINITIONS WITH COMPLETE CLINICAL DATA
# ============================================================================
class PatternDefinitions:
    """9 fundamental behavioral patterns with complete clinical extraction data"""
    
    PATTERNS = {
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
            "avoid_language": ["just be happy", "think positive", "you're being negative"]
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
            "avoid_language": ["just compromise", "stop being defensive", "you're too aggressive"]
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
            "avoid_language": ["just trust people", "you're too paranoid", "not everyone is bad"]
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
            "avoid_language": ["it's not black and white", "stop being so rigid"]
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
            "avoid_language": ["just relax", "stop working so much", "you don't need to prove yourself"]
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
            "avoid_language": ["just be yourself", "stop being fake", "pick one identity"]
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
            "avoid_language": ["just say no", "stop being a doormat", "be selfish for once"]
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
            "avoid_language": ["forget your family", "it's your life", "they're holding you back"]
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
            "avoid_language": ["just stand up for yourself", "why can't you be strong there too"]
        }
    }


# ============================================================================
# COMPREHENSIVE QUESTION BANK - REDESIGNED FOR CLINICAL VALIDITY
# 81 Questions: 5-7 per pattern + screening + validation
# ============================================================================

COMPREHENSIVE_QUESTIONS = [
    # -------------------------------------------------------------------------
    # DEMOGRAPHICS & SCREENING (Questions 1-5)
    # -------------------------------------------------------------------------
    {
        "id": 1,
        "text": "What is your age range?",
        "type": "single_choice",
        "options": ["Under 18", "18-25", "26-35", "36-45", "46-55", "56+"],
        "pattern": None,
        "digital_native_scoring": [3, 5, 4, 3, 2, 1],
        "phase": "screening"
    },
    {
        "id": 2,
        "text": "What is your gender?",
        "type": "single_choice",
        "options": ["Male", "Female", "Non-binary/Other", "Prefer not to say"],
        "pattern": None,
        "phase": "demographics"
    },
    {
        "id": 3,
        "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
        "type": "slider",
        "min": 0,
        "max": 16,
        "default": 4,
        "pattern": None,
        "digital_despair_component": "screen_time",
        "phase": "digital_screening"
    },
    {
        "id": 4,
        "text": "What percentage of your digital time is spent on social media?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "pattern": None,
        "digital_despair_component": "social_media_usage",
        "phase": "digital_screening"
    },
    {
        "id": 5,
        "text": "How would you rate your overall stress level in the past month?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": None,
        "phase": "context"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 1: UNHAPPINESS CULTURE (Questions 6-12) - 7 questions
    # -------------------------------------------------------------------------
    {
        "id": 6,
        "text": "When something genuinely good happens to you, your first automatic thought is:",
        "type": "single_choice",
        "options": [
            "I feel genuinely happy and want to celebrate",
            "I enjoy it but wonder how long it will last",
            "This won't last or something bad will balance it out",
            "I feel uncomfortable, like I don't deserve it",
            "I immediately look for what's wrong or what will go wrong"
        ],
        "pattern": 1,
        "weights": [0, 3, 7, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 7,
        "text": "How often do you downplay your accomplishments or good news when sharing with others?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 1,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 8,
        "text": "When you're feeling happy, you experience:",
        "type": "single_choice",
        "options": [
            "Pure enjoyment without worry",
            "Happiness mixed with mild anxiety",
            "A sense that I need to 'prepare for the worst'",
            "Guilt or feeling I should be more serious",
            "The need to hide or suppress it"
        ],
        "pattern": 1,
        "weights": [0, 4, 7, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 9,
        "text": "Growing up, expressing joy or excitement was:",
        "type": "single_choice",
        "options": [
            "Encouraged and celebrated",
            "Tolerated but not really acknowledged",
            "Met with warnings about 'getting hopes up'",
            "Seen as naive or immature",
            "Actively discouraged or punished"
        ],
        "pattern": 1,
        "weights": [0, 3, 7, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 10,
        "text": "Complete this thought: 'If I allow myself to be truly happy...'",
        "type": "single_choice",
        "options": [
            "Good things will continue",
            "I might get disappointed later",
            "Something bad will definitely happen",
            "People will judge me or bring me down",
            "I'll lose my edge or motivation"
        ],
        "pattern": 1,
        "weights": [0, 5, 9, 8, 7],
        "phase": "core_patterns"
    },
    {
        "id": 11,
        "text": "When others around you are celebrating success, you typically:",
        "type": "single_choice",
        "options": [
            "Join in their joy genuinely",
            "Feel happy for them but uncomfortable",
            "Wonder why good things don't happen to me",
            "Feel suspicious or look for downsides",
            "Feel resentful or withdraw"
        ],
        "pattern": 1,
        "weights": [0, 3, 6, 8, 9],
        "phase": "core_patterns"
    },
    {
        "id": 12,
        "text": "On a scale of 1-10, how comfortable are you maintaining a positive mood for an entire day?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 1,
        "reverse_score": True,
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 2: POWER STRUGGLES (Questions 13-19) - 7 questions
    # -------------------------------------------------------------------------
    {
        "id": 13,
        "text": "When someone disagrees with you, your immediate physical response is:",
        "type": "single_choice",
        "options": [
            "I stay relaxed and curious",
            "Mild tension but manageable",
            "My body tenses up, ready to defend",
            "Adrenaline rush, heart races",
            "Intense physical activation, fight-or-flight"
        ],
        "pattern": 2,
        "weights": [0, 3, 7, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 14,
        "text": "In disagreements, how often do you find yourself needing to 'win' or prove your point?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 2,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 15,
        "text": "Someone challenges your decision in front of others. You feel:",
        "type": "single_choice",
        "options": [
            "Open to hearing their perspective",
            "Slightly defensive but willing to discuss",
            "Threatened and need to reassert authority",
            "Angry and want to shut them down",
            "Attacked and must fight back immediately"
        ],
        "pattern": 2,
        "weights": [0, 3, 7, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 16,
        "text": "Growing up, conflicts in your family typically ended with:",
        "type": "single_choice",
        "options": [
            "Calm resolution and mutual understanding",
            "Someone compromising to keep peace",
            "The loudest/strongest person winning",
            "Anger, tears, or silent treatment",
            "Threats, intimidation, or physical conflict"
        ],
        "pattern": 2,
        "weights": [0, 3, 7, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 17,
        "text": "When you lose an argument or are proven wrong, you:",
        "type": "single_choice",
        "options": [
            "Acknowledge it and learn from it",
            "Accept it but feel uncomfortable",
            "Feel diminished or humiliated",
            "Internally plan how to 'win' next time",
            "Feel rage or a sense of defeat"
        ],
        "pattern": 2,
        "weights": [0, 2, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 18,
        "text": "How often do small disagreements escalate into major conflicts for you?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 2,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 19,
        "text": "In relationships, how much do you need to feel 'in control' to feel safe?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 2,
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 3: SYSTEMATIC MISTRUST (Questions 20-26) - 7 questions
    # -------------------------------------------------------------------------
    {
        "id": 20,
        "text": "When meeting someone new, your default assumption about their intentions is:",
        "type": "single_choice",
        "options": [
            "They're probably friendly and genuine",
            "Neutral until I know them better",
            "Cautious - they might have hidden motives",
            "Suspicious - they probably want something",
            "Highly guarded - they'll likely betray me"
        ],
        "pattern": 3,
        "weights": [0, 2, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 21,
        "text": "Someone you just met is unexpectedly kind or helpful. You think:",
        "type": "single_choice",
        "options": [
            "That's nice, they seem genuine",
            "I appreciate it but wonder why",
            "What do they want from me?",
            "This is manipulation - what's their angle?",
            "This is definitely a trap or scheme"
        ],
        "pattern": 3,
        "weights": [0, 3, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 22,
        "text": "How long does it typically take before you trust someone enough to be vulnerable with them?",
        "type": "single_choice",
        "options": [
            "A few weeks to months",
            "Several months to a year",
            "1-2 years of consistent behavior",
            "Many years, and even then not fully",
            "I never fully trust anyone"
        ],
        "pattern": 3,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 23,
        "text": "When people share personal information about themselves, you:",
        "type": "single_choice",
        "options": [
            "Feel honored and reciprocate naturally",
            "Listen but remain somewhat guarded",
            "Wonder if they're testing me or setting a trap",
            "Assume they're manipulating me into sharing",
            "Become more suspicious of their motives"
        ],
        "pattern": 3,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 24,
        "text": "In past relationships, how many times have you been significantly betrayed or let down?",
        "type": "single_choice",
        "options": [
            "Never or once",
            "2-3 times",
            "4-5 times",
            "6-10 times",
            "Too many to count"
        ],
        "pattern": 3,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 25,
        "text": "How often do you 'test' people to see if they're trustworthy?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 3,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 26,
        "text": "On a scale of 1-10, how much do you believe 'trust no one' is a wise life philosophy?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 3,
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 4: SEPARATION/DIVISION (Questions 27-32) - 6 questions
    # -------------------------------------------------------------------------
    {
        "id": 27,
        "text": "When facing a difficult decision, you typically:",
        "type": "single_choice",
        "options": [
            "See multiple options and creative solutions",
            "See a few main options with pros and cons",
            "Feel stuck between two opposing choices",
            "See only two extreme options (all or nothing)",
            "Feel paralyzed by either/or thinking"
        ],
        "pattern": 4,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 28,
        "text": "How comfortable are you with ambiguity or 'gray areas' in life?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 4,
        "reverse_score": True,
        "phase": "core_patterns"
    },
    {
        "id": 29,
        "text": "When evaluating people, you tend to see them as:",
        "type": "single_choice",
        "options": [
            "Complex humans with strengths and flaws",
            "Mostly good or mostly bad",
            "Either completely good or completely bad",
            "Good until proven bad, then irredeemable",
            "Categories that are absolute and unchangeable"
        ],
        "pattern": 4,
        "weights": [0, 3, 7, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 30,
        "text": "Complete this: 'In life, you must choose between...'",
        "type": "single_choice",
        "options": [
            "Nothing - you can integrate multiple values",
            "Occasionally making hard choices",
            "Security OR freedom (can't have both)",
            "Success OR relationships (can't have both)",
            "Everything is either/or - no middle ground"
        ],
        "pattern": 4,
        "weights": [0, 2, 7, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 31,
        "text": "How often do you find yourself thinking in 'all or nothing' terms?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 4,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 32,
        "text": "When someone changes their mind or shows complexity, you feel:",
        "type": "single_choice",
        "options": [
            "That's normal human growth",
            "Slightly confused but accepting",
            "Uncomfortable with the inconsistency",
            "Betrayed or that they're unreliable",
            "They're a hypocrite - can't trust them"
        ],
        "pattern": 4,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 5: DOING VS BEING (Questions 33-39) - 7 questions
    # -------------------------------------------------------------------------
    {
        "id": 33,
        "text": "Complete this: 'I feel valuable when I...'",
        "type": "single_choice",
        "options": [
            "Simply exist as I am",
            "Am doing something meaningful",
            "Accomplish something important",
            "Prove my worth through achievements",
            "Am constantly productive/achieving"
        ],
        "pattern": 5,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 34,
        "text": "When you have free time with nothing scheduled, you feel:",
        "type": "single_choice",
        "options": [
            "Peaceful and content",
            "Relaxed but slightly restless",
            "Guilty like I should be doing something",
            "Anxious and need to find something productive",
            "Worthless or like I'm wasting my life"
        ],
        "pattern": 5,
        "weights": [0, 3, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 35,
        "text": "How many hours per week do you work (including work you bring home)?",
        "type": "single_choice",
        "options": [
            "35-40 hours",
            "41-50 hours",
            "51-60 hours",
            "61-70 hours",
            "70+ hours or constantly"
        ],
        "pattern": 5,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 36,
        "text": "When not being productive, how intense is your guilt or anxiety?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 5,
        "phase": "core_patterns"
    },
    {
        "id": 37,
        "text": "If all your achievements were taken away, you would feel:",
        "type": "single_choice",
        "options": [
            "Still confident in who I am",
            "Uncertain but still have worth",
            "Lost without my accomplishments",
            "Like I have no identity or value",
            "Completely worthless"
        ],
        "pattern": 5,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 38,
        "text": "How often do you sacrifice sleep, health, or relationships for productivity?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 5,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 39,
        "text": "Growing up, love and approval were conditional on:",
        "type": "single_choice",
        "options": [
            "Nothing - I was loved unconditionally",
            "Being good/not causing trouble",
            "Getting good grades/performing well",
            "Achieving specific goals or standards",
            "Constant exceptional achievement"
        ],
        "pattern": 5,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 6: COMPARTMENTALIZED AUTHENTICITY (Questions 40-45) - 6 questions
    # -------------------------------------------------------------------------
    {
        "id": 40,
        "text": "Your personality and behavior across different settings (work, family, friends):",
        "type": "single_choice",
        "options": [
            "Stay very consistent - I'm the same person",
            "Vary slightly based on context",
            "Vary significantly - different personas",
            "Completely different - like different people",
            "So fragmented I don't know who I really am"
        ],
        "pattern": 6,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 41,
        "text": "How much of your 'real self' do you hide from most people?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "pattern": 6,
        "scale_to_10": True,
        "phase": "core_patterns"
    },
    {
        "id": 42,
        "text": "When you imagine being completely authentic in all areas of life, you feel:",
        "type": "single_choice",
        "options": [
            "That's how I already live",
            "Hopeful and excited",
            "Scared but curious",
            "Terrified of rejection or consequences",
            "Impossible - I'd lose everything"
        ],
        "pattern": 6,
        "weights": [0, 1, 4, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 43,
        "text": "How exhausting is it to maintain your different personas?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 6,
        "phase": "core_patterns"
    },
    {
        "id": 44,
        "text": "In how many areas of your life do you feel you can be completely yourself?",
        "type": "single_choice",
        "options": [
            "All or most areas",
            "About half of areas",
            "A few specific safe spaces",
            "One or two people only",
            "Nowhere - not even alone"
        ],
        "pattern": 6,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 45,
        "text": "Growing up, being your authentic self resulted in:",
        "type": "single_choice",
        "options": [
            "Acceptance and love",
            "Mostly acceptance with some criticism",
            "Criticism, ridicule, or rejection",
            "Punishment, shame, or abandonment",
            "Severe consequences or danger"
        ],
        "pattern": 6,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 7: SELF-SACRIFICE (Questions 46-52) - 7 questions
    # -------------------------------------------------------------------------
    {
        "id": 46,
        "text": "When it comes to your needs versus others' needs:",
        "type": "single_choice",
        "options": [
            "I naturally balance both",
            "I usually prioritize mine but consider theirs",
            "Others' needs usually come first",
            "I almost always put others first",
            "I completely ignore my own needs"
        ],
        "pattern": 7,
        "weights": [0, 1, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 47,
        "text": "How often do you say 'yes' when you really want to say 'no'?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 7,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 48,
        "text": "When you think about taking time for self-care, you feel:",
        "type": "single_choice",
        "options": [
            "That's normal and necessary",
            "Slightly guilty but know I should",
            "Guilty - others need me more",
            "Selfish and undeserving",
            "It's impossible - I have no time for myself"
        ],
        "pattern": 7,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 49,
        "text": "How much energy do you have left for yourself after taking care of others?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "pattern": 7,
        "reverse_score": True,
        "scale_to_10": True,
        "phase": "core_patterns"
    },
    {
        "id": 50,
        "text": "In relationships, you tend to be the one who:",
        "type": "single_choice",
        "options": [
            "Gives and receives in balance",
            "Gives slightly more than you receive",
            "Gives much more than you receive",
            "Gives almost everything, receives little",
            "Gives everything, receives nothing"
        ],
        "pattern": 7,
        "weights": [0, 3, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 51,
        "text": "Growing up, putting your own needs first was seen as:",
        "type": "single_choice",
        "options": [
            "Healthy and encouraged",
            "Acceptable when appropriate",
            "Selfish but tolerated",
            "Selfish and discouraged",
            "Shameful, wrong, or punishable"
        ],
        "pattern": 7,
        "weights": [0, 1, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 52,
        "text": "How often do you feel resentful while helping others?",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 7,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 8: INHERITED MISSIONS (Questions 53-58) - 6 questions
    # -------------------------------------------------------------------------
    {
        "id": 53,
        "text": "Your major life goals are primarily:",
        "type": "single_choice",
        "options": [
            "Based on my own genuine desires",
            "Mostly mine with some family influence",
            "A mix of mine and family expectations",
            "Primarily family expectations",
            "Entirely family dreams, not mine"
        ],
        "pattern": 8,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 54,
        "text": "When thinking about pursuing your own path separate from family expectations:",
        "type": "single_choice",
        "options": [
            "I feel free and excited",
            "I feel supportive curiosity from family",
            "I feel some guilt but mostly okay",
            "I feel guilty like I'm betraying them",
            "I feel I would destroy family relationships"
        ],
        "pattern": 8,
        "weights": [0, 1, 4, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 55,
        "text": "How much do you feel you 'owe' your family for their sacrifices?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 8,
        "phase": "core_patterns"
    },
    {
        "id": 56,
        "text": "If you disappointed your family's expectations, you would feel:",
        "type": "single_choice",
        "options": [
            "Sad but accepting of my choice",
            "Uncomfortable but able to live with it",
            "Deeply guilty and conflicted",
            "Like I betrayed or destroyed them",
            "Unbearable shame and unworthiness"
        ],
        "pattern": 8,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 57,
        "text": "Your current life path feels:",
        "type": "single_choice",
        "options": [
            "Authentically mine",
            "Mostly mine with some compromises",
            "A duty or obligation",
            "Like living someone else's dream",
            "Like a script I have no choice but to follow"
        ],
        "pattern": 8,
        "weights": [0, 2, 5, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 58,
        "text": "How clearly can you identify what YOU actually want, separate from others' expectations?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 8,
        "reverse_score": True,
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # PATTERN 9: CONTEXT-DEPENDENT WEAKNESS (Questions 59-64) - 6 questions
    # -------------------------------------------------------------------------
    {
        "id": 59,
        "text": "Your boundaries and limits:",
        "type": "single_choice",
        "options": [
            "Stay consistent across all situations",
            "Vary slightly based on context",
            "Vary significantly - strong some places, weak others",
            "Disappear completely in certain contexts",
            "Don't exist in most contexts"
        ],
        "pattern": 9,
        "weights": [0, 2, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 60,
        "text": "With certain people or in certain situations, you become someone you don't respect. This happens:",
        "type": "single_choice",
        "options": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
        "pattern": 9,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 61,
        "text": "How many specific people or situations make you lose your normal sense of self?",
        "type": "single_choice",
        "options": [
            "None",
            "1-2 specific people/situations",
            "3-5 people/situations",
            "6-10 people/situations",
            "Many - most contexts weaken me"
        ],
        "pattern": 9,
        "weights": [0, 3, 6, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 62,
        "text": "In certain contexts where you lose power, you:",
        "type": "single_choice",
        "options": [
            "Can still maintain boundaries",
            "Find it difficult but possible",
            "Can't say no even when I want to",
            "Completely lose all agency",
            "Become a different person with no self"
        ],
        "pattern": 9,
        "weights": [0, 3, 6, 9, 10],
        "phase": "core_patterns"
    },
    {
        "id": 63,
        "text": "After being in a situation where you lost yourself, you feel:",
        "type": "single_choice",
        "options": [
            "Fine - I maintained myself",
            "Slightly disappointed but okay",
            "Frustrated and ashamed",
            "Deeply ashamed and angry at myself",
            "Disgusted with myself and hopeless"
        ],
        "pattern": 9,
        "weights": [0, 2, 5, 8, 10],
        "phase": "core_patterns"
    },
    {
        "id": 64,
        "text": "How much does your confidence vary depending on context?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": 9,
        "phase": "core_patterns"
    },
    
    # -------------------------------------------------------------------------
    # VALIDATION & CROSS-CHECK QUESTIONS (65-71)
    # -------------------------------------------------------------------------
    {
        "id": 65,
        "text": "Overall, how much does past emotional pain still control your current decisions?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": None,
        "validation": True,
        "phase": "validation"
    },
    {
        "id": 66,
        "text": "How much of your life energy goes into protecting yourself from being hurt again?",
        "type": "slider",
        "min": 0,
        "max": 100,
        "default": 50,
        "pattern": None,
        "validation": True,
        "phase": "validation"
    },
    {
        "id": 67,
        "text": "If you could push a button and completely resolve one behavioral pattern, which would it be?",
        "type": "text_completion",
        "placeholder": "Describe the one pattern you most want to change...",
        "min_chars": 20,
        "pattern": None,
        "validation": True,
        "phase": "validation"
    },
    {
        "id": 68,
        "text": "What would your life look like if all these patterns were resolved?",
        "type": "text_completion",
        "placeholder": "Describe your life without these limitations...",
        "min_chars": 30,
        "pattern": None,
        "validation": True,
        "phase": "validation"
    },
    {
        "id": 69,
        "text": "On a scale of 1-10, how much do you believe change is truly possible for you?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "pattern": None,
        "readiness_assessment": True,
        "phase": "readiness"
    },
    {
        "id": 70,
        "text": "How ready are you to begin transformation work right now?",
        "type": "single_choice",
        "options": [
            "Ready to start immediately",
            "Ready within the next week",
            "Ready within the next month",
            "Still exploring options",
            "Not ready yet - just gathering information"
        ],
        "pattern": None,
        "readiness_assessment": True,
        "weights": [10, 8, 6, 4, 2],
        "phase": "readiness"
    },
    {
        "id": 71,
        "text": "What motivates you most to change right now?",
        "type": "text_completion",
        "placeholder": "Be specific about what's driving your desire for transformation...",
        "min_chars": 20,
        "pattern": None,
        "readiness_assessment": True,
        "phase": "readiness"
    }
]


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

def compute_digital_despair_score(responses: Dict[int, Any]) -> Dict[str, Any]:
    """Calculate comprehensive digital despair syndrome scoring"""
    
    age_response = responses.get(1)
    age_options = COMPREHENSIVE_QUESTIONS[0]['options']
    digital_native_scores = COMPREHENSIVE_QUESTIONS[0]['digital_native_scoring']
    
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

    def score_patterns(self, responses: Dict[int, Any]) -> Dict[int, float]:
        """
        REDESIGNED: Score with proper statistical validity
        FIXED: Skip "Not applicable" responses
        Returns scores that actually differentiate patterns
        """
        pattern_raw_scores = {i: [] for i in range(1, 10)}  # Store all scores
        
        for question in COMPREHENSIVE_QUESTIONS:
            qid = question['id']
            pattern_id = question.get('pattern')
            
            if pattern_id is None or qid not in responses:
                continue
            
            response = responses[qid]
            
            # FIXED: Skip "Not applicable" responses
            if response == "Not applicable" or response is None or response == "":
                continue
            
            score = self._calculate_question_score(question, response)
            
            # Only add non-zero scores
            if score > 0:
                pattern_raw_scores[pattern_id].append(score)
        
        # CRITICAL: Use 75th percentile instead of mean for better differentiation
        pattern_scores = {}
        for pattern_id, scores in pattern_raw_scores.items():
            if not scores:
                pattern_scores[pattern_id] = 0.0
            elif len(scores) == 1:
                pattern_scores[pattern_id] = scores[0]
            else:
                # Use weighted scoring: 70% max + 30% mean
                # This makes significant patterns stand out
                max_score = max(scores)
                mean_score = sum(scores) / len(scores)
                pattern_scores[pattern_id] = (max_score * 0.7) + (mean_score * 0.3)
        
        return pattern_scores
    
    def _calculate_question_score(self, question: Dict, response: Any) -> float:
        """Calculate score with better clinical differentiation - FIXED to handle skipped questions"""
        
        # FIXED: Handle skipped questions
        if response == "Not applicable" or response is None or response == "":
            return 0.0
        
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
            # FIXED: Handle empty or skipped text responses
            if not response or response == "Not applicable":
                return 0.0
            
            text = str(response).strip()
            if len(text) < 10:
                return 0
            
            # Score based on length and intensity words
            length_score = min(len(text) / 50, 5)
            
            intensity_words = ['always', 'never', 'can\'t', 'impossible', 'terrified', 
                            'desperate', 'worthless', 'hopeless', 'trapped']
            intensity_score = sum(1 for word in intensity_words if word in text.lower())
            intensity_score = min(intensity_score * 2, 5)
            
            return min((length_score + intensity_score) / 2, 10)
        
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


    def extract_trigger_chain(self, responses: Dict[int, Any]) -> Dict[str, Any]:
        """
        Extract complete trigger → response sequence
        Maps exact intervention points for hypnotherapy
        """
        chain = {
            'environmental_trigger': responses.get(14, 'Not captured'),  # Q14: Trigger situation
            'awareness_point': responses.get(15, 'Not captured'),        # Q15: First notice
            'physical_response': responses.get(16, 'Not captured'),      # Q16: Physical sensation
            'automatic_thought': responses.get(17, 'Not captured'),      # Q17: Automatic thought
            'emotional_response': responses.get(18, 'Not captured'),     # Q18: Emotions
            'behavioral_response': responses.get(19, 'Not captured'),    # Q19: Behavior
            'immediate_consequence': responses.get(20, 'Not captured'),  # Q20: After response
            'longer_term_impact': responses.get(21, 'Not captured')      # Q21: Hours later
        }
        
        # Calculate sequence completeness
        captured_elements = sum(1 for v in chain.values() if v != 'Not captured')
        completeness = (captured_elements / len(chain)) * 100
        
        # Identify intervention windows
        intervention_points = []
        if chain['physical_response'] != 'Not captured':
            intervention_points.append('Somatic awareness intervention (physical sensation recognition)')
        if chain['automatic_thought'] != 'Not captured':
            intervention_points.append('Cognitive interruption (thought pattern disruption)')
        if chain['behavioral_response'] != 'Not captured':
            intervention_points.append('Behavioral choice point (alternative response installation)')
        
        return {
            'trigger_chain': chain,
            'sequence_completeness': round(completeness, 1),
            'intervention_windows': intervention_points,
            'chain_analysis': f"Sequence {completeness:.0f}% complete - {'sufficient for intervention design' if completeness >= 60 else 'requires session 1 completion'}"
        }
     
     
    def generate_complete_analysis(self, assessment_data: Dict) -> Dict[str, Any]:
        """Generate comprehensive assessment analysis with all clinical data"""
        responses = assessment_data.get('responses', {})
        
        # Score patterns
        pattern_scores = self.score_patterns(responses)
        
        # Analyze hierarchy
        from utils.config_assess import calculate_constellation_multiplier
        pattern_hierarchy = self.analyze_pattern_hierarchy(pattern_scores)
        constellation_multiplier = calculate_constellation_multiplier(pattern_scores)
        
        # Digital analysis
        from utils.config_assess import compute_digital_despair_score
        digital_analysis = compute_digital_despair_score(responses)
        is_digital_native = digital_analysis['is_digital_native']
        
        # Resistance and success
        resistance_score = self.predict_resistance(responses)
        success_prediction = self.calculate_success_probability(
            pattern_scores, constellation_multiplier, resistance_score,
            digital_analysis if is_digital_native else None
        )
        
        # Therapeutic protocols
        therapeutic_protocols = self.select_therapeutic_protocols(
            pattern_hierarchy,
            digital_analysis if is_digital_native else None,
            success_prediction
        )

        # ENHANCED: Extract trigger chain
        trigger_chain_data = self.extract_trigger_chain(responses)
        
        # ENHANCED: Extract clinical summary data
        clinical_summary = self.extract_clinical_summary_data(
            pattern_hierarchy, responses, digital_analysis
        )
        
        return {
            'pattern_scores': pattern_scores,
            'pattern_analysis': pattern_hierarchy,
            'pattern_hierarchy': pattern_hierarchy,
            'constellation_multiplier': constellation_multiplier,
            'resistance_score': resistance_score,
            'digital_analysis': digital_analysis,
            'is_digital_native': is_digital_native,
            'success_prediction': success_prediction,
            'therapeutic_recommendations': {
                'success_probability': success_prediction['overall_success_rate'],
                'recommended_sessions': success_prediction['recommended_sessions'],
                'timeline': success_prediction['timeline_estimate'],
                'protocols': therapeutic_protocols
            },
            'therapeutic_protocols': therapeutic_protocols,
            'trigger_chain_analysis': trigger_chain_data,
            'clinical_summary': clinical_summary,
            'timestamp': datetime.now().isoformat(),
            'assessment_quality': {
                'total_questions_answered': len(responses),
                'completion_rate': (len(responses) / len(COMPREHENSIVE_QUESTIONS)) * 100,
                'text_responses': len([r for r in responses.values() if isinstance(r, str) and len(str(r)) > 20])
            }
        }
    
  
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



# ============================================================================
# QUESTION ROUTER
# ============================================================================

class QuestionRouter:
    """Intelligent question routing"""
    
    def __init__(self):
        self.core_questions = [q for q in COMPREHENSIVE_QUESTIONS if not q.get('validation')]
        self.validation_questions = [q for q in COMPREHENSIVE_QUESTIONS if q.get('validation')]
    
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
        return len(COMPREHENSIVE_QUESTIONS)


# ============================================================================
# CONFIGURATION CLASS
# ============================================================================

class AssessmentConfig:
    """Centralized configuration access"""
    
    pattern_definitions = PatternDefinitions
    comprehensive_questions = COMPREHENSIVE_QUESTIONS
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


__all__ = [
    'PatternDefinitions',
    'COMPREHENSIVE_QUESTIONS',
    'AnalyticsEngine',
    'QuestionRouter',
    'AssessmentConfig',
    'compute_digital_despair_score',
    'calculate_constellation_multiplier'
]
