# Enhanced clinical behavioral pattern assessment - complete final version
# Comprehensive implementation with all optimizations and full functionality

import streamlit as st
from datetime import datetime
import re

# ---- paywall integration ----
try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False

# ---- styling functions ----
def apply_clinical_styles():
    """Apply expert clinical-grade styling with enhanced ux elements"""
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 0.75rem !important;
        padding-bottom: 0.75rem !important;
        max-width: 100% !important;
    }
    @media (min-width: 768px) {
        .main .block-container {
            max-width: 600px !important;
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
    .clinical-question {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .safety-notice {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    .clinical-insight {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 0.75rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
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
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
        .clinical-question {
            padding: 1rem;
            margin-bottom: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ---- enhanced assessment class ----
class ComprehensiveBehavioralAssessment:
    """Clinical-grade behavioral pattern assessment optimized for completion and accuracy"""
    
    def __init__(self):
        self._init_session_state()
        self.patterns = {
            1: "unhappiness culture", 2: "power struggles", 3: "systematic mistrust", 4: "separation and division",
            5: "doing versus being", 6: "compartmentalized authenticity", 7: "self sacrifice and care avoidance",
            8: "inherited missions", 9: "context dependent weakness"
        }
        self.core_questions = self._get_core_questions()
        self.adaptive_pools = self._get_adaptive_question_pools()
        self.safety_questions = self._get_safety_questions()
        self.hypnotic_questions = self._get_hypnotic_responsiveness_questions()

    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'question_sequence': [],
            'adaptive_triggered': [],
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'pattern_scores': {},
            'risk_flags': [],
            'start_time': datetime.now().isoformat(),
            'intensity_responses': {}
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _get_core_questions(self):
        """Optimized core questions balancing clinical depth with user experience"""
        return {
            1: {
                "text": "what specific behavior or pattern would you most like to transform?",
                "type": "text_completion",
                "placeholder": "describe the exact behavior, feeling, or situation you want to change (e.g., 'procrastination on important tasks', 'anxiety in social situations', 'perfectionism that prevents me from finishing projects')...",
                "patterns": "presenting_problem",
                "min_chars": 40,
                "adaptive_triggers": ["behavioral_specificity"]
            },
            2: {
                "text": "how long has this pattern been affecting your life?",
                "type": "single_choice",
                "options": [
                    "less than 6 months",
                    "6 months to 2 years", 
                    "2-5 years",
                    "5-10 years",
                    "over 10 years or as long as i can remember"
                ],
                "patterns": "chronicity",
                "weights": [1, 2, 3, 4, 5],
                "adaptive_triggers": ["pattern_entrenchment"]
            },
            3: {
                "text": "rate how much this pattern interferes with your daily life:",
                "type": "scale_7",
                "labels": ["minimal disruption", "completely overwhelming"],
                "patterns": "interference_level"
            },
            4: {
                "text": "describe a typical situation that triggers this pattern:",
                "type": "text_completion",
                "placeholder": "what happens right before the pattern occurs? who is involved? where are you? what time of day? be specific about the context...",
                "patterns": "trigger_mapping",
                "min_chars": 50,
                "adaptive_triggers": ["trigger_specificity"]
            },
            5: {
                "text": "when this pattern gets triggered, your first physical sensation is:",
                "type": "single_choice_with_intensity",
                "options": [
                    "chest tightness, heart racing, or breathing changes",
                    "stomach drop, nausea, or digestive discomfort",
                    "muscle tension, clenching, or physical rigidity",
                    "hot flash, sweating, or temperature changes",
                    "numbness, disconnection, or dissociative feelings",
                    "restlessness, agitation, or urge to move/escape",
                    "no noticeable physical response"
                ],
                "patterns": "somatic_response",
                "weights": [3, 3, 2, 2, 4, 3, 0],
                "adaptive_triggers": ["somatic_awareness"]
            },
            6: {
                "text": "what emotions surface immediately after the physical sensation?",
                "type": "multi_select_weighted",
                "max_selections": 4,
                "options": [
                    "anxiety/fear", "anger/rage", "shame/embarrassment", 
                    "sadness/grief", "guilt/self-blame", "frustration/irritation", 
                    "overwhelm/panic", "numbness/emptiness", "confusion/disorientation"
                ],
                "patterns": "emotional_chain"
            },
            7: {
                "text": "your inner voice typically says:",
                "type": "single_choice_with_intensity",
                "options": [
                    "\"i'm not good enough / i'm inadequate\"",
                    "\"something bad will happen / danger is coming\"",
                    "\"i can't handle this / i'm powerless\"",
                    "\"they'll reject, judge, or abandon me\"",
                    "\"i should be doing more / i'm lazy\"",
                    "\"this is hopeless / nothing will change\"",
                    "\"i need to control this situation\""
                ],
                "patterns": [1, 3, 7, 3, 5, 1, 2],
                "weights": [3, 2, 3, 2, 2, 3, 3],
                "adaptive_triggers": ["core_beliefs"]
            },
            8: {
                "text": "your typical behavioral response is:",
                "type": "single_choice",
                "options": [
                    "avoidance, withdrawal, or procrastination",
                    "compulsive action, repetition, or checking behaviors",
                    "seeking reassurance or approval from others",
                    "self-critical internal dialogue or self-punishment",
                    "overcompensation, perfectionism, or over-preparation",
                    "aggressive behavior, arguing, or attempts to control"
                ],
                "patterns": [7, 5, 3, 1, 5, 2],
                "weights": [2, 3, 2, 3, 2, 3],
                "adaptive_triggers": ["behavioral_pattern"]
            },
            9: {
                "text": "what happens after this behavioral response?",
                "type": "single_choice",
                "options": [
                    "temporary relief followed by guilt or shame",
                    "the pattern escalates or gets worse over time",
                    "emotional exhaustion and numbness",
                    "conflict or problems in relationships", 
                    "the pattern reinforces itself for next time",
                    "i feel more anxious and out of control"
                ],
                "patterns": "consequence_chain",
                "weights": [2, 3, 2, 2, 3, 2]
            },
            10: {
                "text": "are you currently receiving any medical or mental health care?",
                "type": "single_choice",
                "options": [
                    "no medical or mental health care currently",
                    "physical health care only",
                    "mental health counseling or therapy only",
                    "both physical and mental health care",
                    "psychiatric medication management only",
                    "prefer not to disclose"
                ],
                "risk_assessment": True
            },
            11: {
                "text": "rate your experience with intense emotional states:",
                "type": "single_choice",
                "options": [
                    "rarely experience intense emotions",
                    "occasional intense emotions, easily managed",
                    "regular intense emotions, usually manageable",
                    "frequent overwhelming emotions, hard to manage",
                    "constant emotional intensity, feels uncontrollable"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 3, 4]
            },
            12: {
                "text": "have you experienced dissociation, panic attacks, or thoughts of self-harm?",
                "type": "single_choice",
                "options": [
                    "never experienced any of these",
                    "very rarely and easily manageable",
                    "occasionally but i have coping strategies",
                    "frequently and they significantly impact my life",
                    "currently experiencing these regularly"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 3, 4]
            },
            13: {
                "text": "do you use any substances to cope with this pattern?",
                "type": "single_choice",
                "options": [
                    "never use substances for coping",
                    "occasional alcohol (1-2 drinks socially)",
                    "regular alcohol use to manage emotions",
                    "prescription medication as prescribed", 
                    "recreational drugs or misused prescriptions"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 1, 3]
            },
            14: {
                "text": "when something wonderful happens in your life, your immediate reaction is:",
                "type": "single_choice",
                "options": [
                    "genuine enjoyment and celebration",
                    "immediately searching for potential problems",
                    "feeling undeserving or guilty",
                    "minimizing its importance or downplaying it",
                    "emotional numbness or disconnection from joy"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 3, 3, 2, 4],
                "adaptive_triggers": ["unhappiness_deep"]
            },
            15: {
                "text": "during interpersonal conflict, your nervous system response is:",
                "type": "single_choice",
                "options": [
                    "generally calm and able to think clearly",
                    "fight response - tension, anger, need to argue",
                    "flight response - strong urge to escape",
                    "freeze response - numbness, shutdown, unable to speak",
                    "fawn response - immediate people-pleasing and apologizing"
                ],
                "patterns": [None, 2, 2, 2, 7],
                "weights": [0, 3, 2, 3, 2],
                "adaptive_triggers": ["conflict_trauma"]
            },
            16: {
                "text": "your default assumption about new people's intentions toward you is:",
                "type": "single_choice",
                "options": [
                    "generally well-meaning until proven otherwise",
                    "probably judging or critically evaluating me",
                    "wanting something from me or likely to use me",
                    "will reject me once they discover my flaws",
                    "indifferent or uninterested in connecting"
                ],
                "patterns": [None, 3, 3, 3, 3],
                "weights": [0, 2, 3, 3, 1],
                "adaptive_triggers": ["trust_trauma"]
            },
            17: {
                "text": "when facing important life decisions, you typically feel:",
                "type": "single_choice",
                "options": [
                    "multiple creative options and possibilities exist",
                    "trapped between two impossible either/or choices",
                    "only extreme alternatives with no middle ground",
                    "paralyzed by black and white thinking",
                    "overwhelmed by too many complex options"
                ],
                "patterns": [None, 4, 4, 4, 4],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["binary_thinking"]
            },
            18: {
                "text": "complete this sentence: 'i feel most valuable when i...'",
                "type": "single_choice",
                "options": [
                    "simply exist as i am, without proving anything",
                    "accomplish something important or significant",
                    "help other people or make them happy", 
                    "prove my worth through performance",
                    "receive external validation or recognition"
                ],
                "patterns": [None, 5, 7, 5, 5],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["performance_anxiety"]
            },
            19: {
                "text": "your personality and behavior change significantly based on:",
                "type": "single_choice",
                "options": [
                    "they stay consistent across all situations",
                    "which group of people i'm with",
                    "professional versus personal settings",
                    "whether i'm in control or following others",
                    "my current emotional state or stress level"
                ],
                "patterns": [None, 6, 6, 6, 6],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["identity_fragmentation"]
            },
            20: {
                "text": "when it comes to your own health, self-care, and wellbeing:",
                "type": "single_choice",
                "options": [
                    "i naturally prioritize it alongside caring for others",
                    "i know what i should do but struggle to follow through",
                    "i care for everyone else first, no energy left for me",
                    "i feel selfish or guilty focusing on my own needs",
                    "i completely neglect my own needs"
                ],
                "patterns": [None, 7, 7, 7, 7],
                "weights": [0, 2, 3, 3, 4],
                "adaptive_triggers": ["self_neglect"]
            },
            21: {
                "text": "your major life goals are primarily influenced by:",
                "type": "single_choice",
                "options": [
                    "what i genuinely desire for my own fulfillment",
                    "what my family expected or dreamed for me",
                    "honoring someone who died or sacrificed",
                    "proving i'm worthy of someone's love",
                    "rebelling against others' expectations"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["family_loyalty"]
            },
            22: {
                "text": "with certain people or situations, you tend to:",
                "type": "single_choice",
                "options": [
                    "stay true to your values and boundaries",
                    "become someone you don't recognize",
                    "lose all your usual boundaries",
                    "can't say no even when you want to",
                    "completely lose sense of self"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 3, 3, 4],
                "adaptive_triggers": ["boundary_collapse"]
            },
            23: {
                "text": "what would you lose if this pattern completely disappeared tomorrow?",
                "type": "text_completion",
                "placeholder": "consider: what protection does it provide? what identity might change? how might relationships shift?",
                "patterns": "secondary_gain",
                "min_chars": 40,
                "adaptive_triggers": ["resistance_mapping"]
            },
            24: {
                "text": "how easily can you become completely absorbed in movies, books, or daydreams?",
                "type": "single_choice",
                "options": [
                    "very easily - completely lose track of time",
                    "moderately easily - can get quite absorbed",
                    "sometimes - depends on my mood",
                    "rarely - usually remain aware of surroundings",
                    "almost never - always maintain awareness"
                ],
                "patterns": "absorption_capacity",
                "weights": [5, 4, 3, 2, 1]
            },
            25: {
                "text": "what type of therapeutic guidance appeals most to you?",
                "type": "single_choice",
                "options": [
                    "direct, clear instructions and guidance",
                    "gentle, permissive suggestions",
                    "metaphorical stories and symbolic approaches",
                    "collaborative exploration together",
                    "scientific explanations and logical understanding"
                ],
                "patterns": "therapeutic_preference"
            }
        }

    def _get_adaptive_question_pools(self):
        """Targeted follow-up questions triggered by specific responses"""
        return {
            "unhappiness_deep": {
                26: {
                    "text": "what messages did you receive in your family about happiness and success?",
                    "type": "single_choice",
                    "options": [
                        "happiness is natural and should be celebrated",
                        "happiness must be earned through achievement",
                        "too much happiness leads to disappointment",
                        "others' happiness is more important than your own",
                        "happiness is selfish or frivolous"
                    ],
                    "patterns": [None, 5, 1, 7, 1],
                    "weights": [0, 2, 3, 2, 3]
                }
            },
            "conflict_trauma": {
                27: {
                    "text": "during childhood conflicts, the adults around you typically:",
                    "type": "single_choice",
                    "options": [
                        "modeled healthy conflict resolution",
                        "escalated conflicts with yelling or aggression",
                        "completely avoided conflict",
                        "used guilt or manipulation",
                        "were unpredictable in responses"
                    ],
                    "patterns": [None, 2, 2, 2, 2],
                    "weights": [0, 3, 2, 3, 4]
                }
            },
            "trust_trauma": {
                28: {
                    "text": "your earliest trust violation involved:",
                    "type": "single_choice",
                    "options": [
                        "no significant early violations",
                        "broken promises from caregivers",
                        "betrayal by close friends",
                        "emotional unavailability",
                        "abuse or severe neglect"
                    ],
                    "patterns": [None, 3, 3, 3, 3],
                    "weights": [0, 2, 2, 3, 4]
                }
            },
            "binary_thinking": {
                29: {
                    "text": "where did you learn that choices had to be either/or?",
                    "type": "text_completion",
                    "placeholder": "consider family rules, religious teachings, school experiences...",
                    "patterns": "cognitive_conditioning",
                    "min_chars": 30
                }
            },
            "performance_anxiety": {
                30: {
                    "text": "what childhood experiences linked your worth to performance?",
                    "type": "text_completion",
                    "placeholder": "think about school, activities, family expectations...",
                    "patterns": "worth_conditioning",
                    "min_chars": 30
                }
            },
            "identity_fragmentation": {
                31: {
                    "text": "when did you learn to show different selves to different people?",
                    "type": "text_completion",
                    "placeholder": "consider family dynamics, social groups, safety concerns...",
                    "patterns": "identity_development",
                    "min_chars": 30
                }
            },
            "self_neglect": {
                32: {
                    "text": "who modeled self-sacrifice as virtue in your upbringing?",
                    "type": "single_choice",
                    "options": [
                        "no one specifically modeled self-sacrifice",
                        "primary caregiver",
                        "extended family member",
                        "religious or cultural community",
                        "multiple people - it was the norm"
                    ],
                    "patterns": [None, 7, 7, 7, 7],
                    "weights": [0, 2, 2, 2, 3]
                }
            },
            "family_loyalty": {
                33: {
                    "text": "what unspoken family rules still govern your choices?",
                    "type": "text_completion",
                    "placeholder": "consider career expectations, relationship choices, values...",
                    "patterns": "family_rules",
                    "min_chars": 30
                }
            },
            "boundary_collapse": {
                34: {
                    "text": "when did you learn that others' needs come before your own?",
                    "type": "text_completion",
                    "placeholder": "think about early caretaking roles, family dynamics...",
                    "patterns": "boundary_development",
                    "min_chars": 30
                }
            }
        }

    def _get_safety_questions(self):
        """Safety assessment triggered by risk indicators"""
        return {
            "support_system": {
                35: {
                    "text": "if you were in emotional crisis right now, you would:",
                    "type": "single_choice",
                    "options": [
                        "have multiple trusted people to reach out to",
                        "have one reliable person to contact",
                        "try to handle it alone first",
                        "not feel comfortable reaching out",
                        "have no one available"
                    ],
                    "risk_assessment": True,
                    "weights": [0, 0, 1, 2, 3]
                }
            },
            "safety_planning": {
                36: {
                    "text": "do you have strategies for managing overwhelming emotions?",
                    "type": "single_choice",
                    "options": [
                        "yes, multiple effective strategies",
                        "some strategies that work",
                        "basic strategies but don't always help",
                        "few strategies, rarely effective",
                        "no strategies - feel helpless"
                    ],
                    "risk_assessment": True,
                    "weights": [0, 0, 1, 2, 3]
                }
            }
        }

    def _get_hypnotic_responsiveness_questions(self):
        """Hypnotic susceptibility assessment"""
        return {
            "hypnotic_profile": {
                37: {
                    "text": "how do you typically process information most effectively?",
                    "type": "single_choice",
                    "options": [
                        "through visual imagery and pictures",
                        "through physical sensations and feelings",
                        "through auditory guidance and words",
                        "through logical understanding",
                        "through metaphorical and symbolic meaning"
                    ],
                    "patterns": "processing_style"
                }
            },
            "trance_experience": {
                38: {
                    "text": "have you experienced hypnotic or trance-like states before?",
                    "type": "single_choice",
                    "options": [
                        "frequently in meditation or relaxation",
                        "occasionally in daydreaming or flow states",
                        "rarely but open to experiencing it",
                        "never but curious to try",
                        "skeptical or apprehensive about it"
                    ],
                    "patterns": "trance_familiarity",
                    "weights": [4, 3, 2, 1, 0]
                }
            }
        }

    # ---- navigation and response logic ----
    def _get_current_question_id(self):
        answered = set(st.session_state.assessment_responses.keys())
        
        # core questions first
        for qid in sorted(self.core_questions.keys()):
            if qid not in answered:
                return qid
        
        # adaptive questions
        for pool_name in st.session_state.adaptive_triggered:
            pool = self.adaptive_pools.get(pool_name, {})
            for qid in sorted(pool.keys()):
                if qid not in answered:
                    return qid
        
        # safety questions
        if st.session_state.risk_flags:
            for pool in self.safety_questions.values():
                for qid in sorted(pool.keys()):
                    if qid not in answered:
                        return qid
        
        # hypnotic questions
        for pool in self.hypnotic_questions.values():
            for qid in sorted(pool.keys()):
                if qid not in answered:
                    return qid
        
        return None

    def _estimate_total_questions(self):
        base = len(self.core_questions)
        adaptive = len(st.session_state.adaptive_triggered)
        safety = len(st.session_state.risk_flags)
        hypnotic = sum(len(pool) for pool in self.hypnotic_questions.values())
        return base + adaptive + safety + hypnotic

    def _estimate_time_remaining(self):
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        return remaining * 1.25

    def _get_question_by_id(self, q_id):
        if q_id in self.core_questions:
            return self.core_questions[q_id]
        for pool in self.adaptive_pools.values():
            if q_id in pool:
                return pool[q_id]
        for pool in self.safety_questions.values():
            if q_id in pool:
                return pool[q_id]
        for pool in self.hypnotic_questions.values():
            if q_id in pool:
                return pool[q_id]
        return None

    def _save_response(self, q_id, response, question, intensity=None):
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'intensity': intensity,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat()
        }
        
        if intensity:
            st.session_state.intensity_responses[q_id] = intensity
        
        # process adaptive triggers
        if 'adaptive_triggers' in question:
            for trigger in question['adaptive_triggers']:
                if trigger not in st.session_state.adaptive_triggered:
                    st.session_state.adaptive_triggered.append(trigger)
        
        # process risk assessment
        if question.get('risk_assessment'):
            weights = question.get('weights', [0])
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(weights) and weights[option_index] >= 2:
                        risk_flag = f"risk_q_{q_id}"
                        if risk_flag not in st.session_state.risk_flags:
                            st.session_state.risk_flags.append(risk_flag)
                except (ValueError, IndexError):
                    pass
        
        # process pattern scoring
        if 'patterns' in question and question['patterns'] is not None:
            patterns = question['patterns']
            weights = question.get('weights', [1])
            
            if isinstance(patterns, list) and isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(patterns) and patterns[option_index] is not None:
                        pattern_id = patterns[option_index]
                        weight = weights[option_index] if option_index < len(weights) else 1
                        if intensity:
                            weight *= (intensity / 5.0)
                        
                        if pattern_id in st.session_state.pattern_scores:
                            st.session_state.pattern_scores[pattern_id] += weight
                        else:
                            st.session_state.pattern_scores[pattern_id] = weight
                except (ValueError, IndexError):
                    pass
            elif isinstance(patterns, (int, str)):
                weight = weights[0] if weights else 1
                if intensity:
                    # Enhanced Clinical Behavioral Pattern Assessment - Complete Final Version
# Comprehensive implementation with all optimizations and full functionality

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
            max-width: 600px !important;
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
    .clinical-question {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .safety-notice {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    .clinical-insight {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 0.75rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
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
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
        .clinical-question {
            padding: 1rem;
            margin-bottom: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ---- Enhanced Assessment Class ----
class ComprehensiveBehavioralAssessment:
    """Clinical-grade behavioral pattern assessment optimized for completion and accuracy"""
    
    def __init__(self):
        self._init_session_state()
        self.patterns = {
            1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 4: "Separation and Division",
            5: "Doing versus Being", 6: "Compartmentalized Authenticity", 7: "Self Sacrifice and Care Avoidance",
            8: "Inherited Missions", 9: "Context Dependent Weakness"
        }
        self.core_questions = self._get_core_questions()
        self.adaptive_pools = self._get_adaptive_question_pools()
        self.safety_questions = self._get_safety_questions()
        self.hypnotic_questions = self._get_hypnotic_responsiveness_questions()

    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'question_sequence': [],
            'adaptive_triggered': [],
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'pattern_scores': {},
            'risk_flags': [],
            'start_time': datetime.now().isoformat(),
            'intensity_responses': {}
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _get_core_questions(self):
        """Optimized core questions balancing clinical depth with user experience"""
        return {
            1: {
                "text": "What specific behavior or pattern would you most like to transform?",
                "type": "text_completion",
                "placeholder": "Describe the exact behavior, feeling, or situation you want to change (e.g., 'procrastination on important tasks', 'anxiety in social situations', 'perfectionism that prevents me from finishing projects')...",
                "patterns": "presenting_problem",
                "min_chars": 40,
                "adaptive_triggers": ["behavioral_specificity"],
                "clinical_insight": "Primary therapeutic target identification"
            },
            2: {
                "text": "How long has this pattern been affecting your life?",
                "type": "single_choice",
                "options": [
                    "Less than 6 months",
                    "6 months to 2 years", 
                    "2-5 years",
                    "5-10 years",
                    "Over 10 years or as long as I can remember"
                ],
                "patterns": "chronicity",
                "weights": [1, 2, 3, 4, 5],
                "adaptive_triggers": ["pattern_entrenchment"],
                "clinical_insight": "Pattern entrenchment assessment"
            },
            3: {
                "text": "Rate how much this pattern interferes with your daily life:",
                "type": "scale_7",
                "labels": ["Minimal disruption", "Completely overwhelming"],
                "patterns": "interference_level",
                "clinical_insight": "Functional impact measurement"
            },
            4: {
                "text": "Describe a typical situation that triggers this pattern:",
                "type": "text_completion",
                "placeholder": "What happens right before the pattern occurs? Who is involved? Where are you? What time of day? Be specific about the context...",
                "patterns": "trigger_mapping",
                "min_chars": 50,
                "adaptive_triggers": ["trigger_specificity"],
                "clinical_insight": "Environmental trigger identification"
            },
            5: {
                "text": "When this pattern gets triggered, your first physical sensation is:",
                "type": "single_choice_with_intensity",
                "options": [
                    "Chest tightness, heart racing, or breathing changes",
                    "Stomach drop, nausea, or digestive discomfort",
                    "Muscle tension, clenching, or physical rigidity",
                    "Hot flash, sweating, or temperature changes",
                    "Numbness, disconnection, or dissociative feelings",
                    "Restlessness, agitation, or urge to move/escape",
                    "No noticeable physical response"
                ],
                "patterns": "somatic_response",
                "weights": [3, 3, 2, 2, 4, 3, 0],
                "adaptive_triggers": ["somatic_awareness"],
                "clinical_insight": "Somatic awareness mapping"
            },
            6: {
                "text": "What emotions surface immediately after the physical sensation?",
                "type": "multi_select_weighted",
                "max_selections": 4,
                "options": [
                    "Anxiety/Fear", "Anger/Rage", "Shame/Embarrassment", 
                    "Sadness/Grief", "Guilt/Self-blame", "Frustration/Irritation", 
                    "Overwhelm/Panic", "Numbness/Emptiness", "Confusion/Disorientation"
                ],
                "patterns": "emotional_chain",
                "clinical_insight": "Emotional sequence mapping"
            },
            7: {
                "text": "Your inner voice typically says:",
                "type": "single_choice_with_intensity",
                "options": [
                    "\"I'm not good enough / I'm inadequate\"",
                    "\"Something bad will happen / Danger is coming\"",
                    "\"I can't handle this / I'm powerless\"",
                    "\"They'll reject, judge, or abandon me\"",
                    "\"I should be doing more / I'm lazy\"",
                    "\"This is hopeless / Nothing will change\"",
                    "\"I need to control this situation\""
                ],
                "patterns": [1, 3, 7, 3, 5, 1, 2],
                "weights": [3, 2, 3, 2, 2, 3, 3],
                "adaptive_triggers": ["core_beliefs"],
                "clinical_insight": "Core cognitive distortion identification"
            },
            8: {
                "text": "Your typical behavioral response is:",
                "type": "single_choice",
                "options": [
                    "Avoidance, withdrawal, or procrastination",
                    "Compulsive action, repetition, or checking behaviors",
                    "Seeking reassurance or approval from others",
                    "Self-critical internal dialogue or self-punishment",
                    "Overcompensation, perfectionism, or over-preparation",
                    "Aggressive behavior, arguing, or attempts to control"
                ],
                "patterns": [7, 5, 3, 1, 5, 2],
                "weights": [2, 3, 2, 3, 2, 3],
                "adaptive_triggers": ["behavioral_pattern"],
                "clinical_insight": "Behavioral response identification"
            },
            9: {
                "text": "What happens after this behavioral response?",
                "type": "single_choice",
                "options": [
                    "Temporary relief followed by guilt or shame",
                    "The pattern escalates or gets worse over time",
                    "Emotional exhaustion and numbness",
                    "Conflict or problems in relationships", 
                    "The pattern reinforces itself for next time",
                    "I feel more anxious and out of control"
                ],
                "patterns": "consequence_chain",
                "weights": [2, 3, 2, 2, 3, 2],
                "clinical_insight": "Pattern reinforcement cycle analysis"
            },
            10: {
                "text": "Are you currently receiving any medical or mental health care?",
                "type": "single_choice",
                "options": [
                    "No medical or mental health care currently",
                    "Physical health care only",
                    "Mental health counseling or therapy only",
                    "Both physical and mental health care",
                    "Psychiatric medication management only",
                    "Prefer not to disclose"
                ],
                "risk_assessment": True,
                "clinical_insight": "Medical contraindication screening"
            },
            11: {
                "text": "Rate your experience with intense emotional states:",
                "type": "single_choice",
                "options": [
                    "Rarely experience intense emotions",
                    "Occasional intense emotions, easily managed",
                    "Regular intense emotions, usually manageable",
                    "Frequent overwhelming emotions, hard to manage",
                    "Constant emotional intensity, feels uncontrollable"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 3, 4],
                "clinical_insight": "Emotional regulation capacity assessment"
            },
            12: {
                "text": "Have you experienced dissociation, panic attacks, or thoughts of self-harm?",
                "type": "single_choice",
                "options": [
                    "Never experienced any of these",
                    "Very rarely and easily manageable",
                    "Occasionally but I have coping strategies",
                    "Frequently and they significantly impact my life",
                    "Currently experiencing these regularly"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 3, 4],
                "clinical_insight": "Crisis risk assessment"
            },
            13: {
                "text": "Do you use any substances to cope with this pattern?",
                "type": "single_choice",
                "options": [
                    "Never use substances for coping",
                    "Occasional alcohol (1-2 drinks socially)",
                    "Regular alcohol use to manage emotions",
                    "Prescription medication as prescribed", 
                    "Recreational drugs or misused prescriptions"
                ],
                "risk_assessment": True,
                "weights": [0, 1, 2, 1, 3],
                "clinical_insight": "Substance use patterns assessment"
            },
            14: {
                "text": "When something wonderful happens in your life, your immediate reaction is:",
                "type": "single_choice",
                "options": [
                    "Genuine enjoyment and celebration",
                    "Immediately searching for potential problems",
                    "Feeling undeserving or guilty",
                    "Minimizing its importance or downplaying it",
                    "Emotional numbness or disconnection from joy"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 3, 3, 2, 4],
                "adaptive_triggers": ["unhappiness_deep"],
                "clinical_insight": "Pleasure reception capacity"
            },
            15: {
                "text": "During interpersonal conflict, your nervous system response is:",
                "type": "single_choice",
                "options": [
                    "Generally calm and able to think clearly",
                    "Fight response - tension, anger, need to argue",
                    "Flight response - strong urge to escape",
                    "Freeze response - numbness, shutdown, unable to speak",
                    "Fawn response - immediate people-pleasing and apologizing"
                ],
                "patterns": [None, 2, 2, 2, 7],
                "weights": [0, 3, 2, 3, 2],
                "adaptive_triggers": ["conflict_trauma"],
                "clinical_insight": "Autonomic nervous system patterns"
            },
            16: {
                "text": "Your default assumption about new people's intentions toward you is:",
                "type": "single_choice",
                "options": [
                    "Generally well-meaning until proven otherwise",
                    "Probably judging or critically evaluating me",
                    "Wanting something from me or likely to use me",
                    "Will reject me once they discover my flaws",
                    "Indifferent or uninterested in connecting"
                ],
                "patterns": [None, 3, 3, 3, 3],
                "weights": [0, 2, 3, 3, 1],
                "adaptive_triggers": ["trust_trauma"],
                "clinical_insight": "Relational expectation patterns"
            },
            17: {
                "text": "When facing important life decisions, you typically feel:",
                "type": "single_choice",
                "options": [
                    "Multiple creative options and possibilities exist",
                    "Trapped between two impossible either/or choices",
                    "Only extreme alternatives with no middle ground",
                    "Paralyzed by black and white thinking",
                    "Overwhelmed by too many complex options"
                ],
                "patterns": [None, 4, 4, 4, 4],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["binary_thinking"],
                "clinical_insight": "Cognitive flexibility assessment"
            },
            18: {
                "text": "Complete this sentence: 'I feel most valuable when I...'",
                "type": "single_choice",
                "options": [
                    "Simply exist as I am, without proving anything",
                    "Accomplish something important or significant",
                    "Help other people or make them happy", 
                    "Prove my worth through performance",
                    "Receive external validation or recognition"
                ],
                "patterns": [None, 5, 7, 5, 5],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["performance_anxiety"],
                "clinical_insight": "Self-worth conditioning analysis"
            },
            19: {
                "text": "Your personality and behavior change significantly based on:",
                "type": "single_choice",
                "options": [
                    "They stay consistent across all situations",
                    "Which group of people I'm with",
                    "Professional versus personal settings",
                    "Whether I'm in control or following others",
                    "My current emotional state or stress level"
                ],
                "patterns": [None, 6, 6, 6, 6],
                "weights": [0, 2, 2, 3, 2],
                "adaptive_triggers": ["identity_fragmentation"],
                "clinical_insight": "Identity consistency patterns"
            },
            20: {
                "text": "When it comes to your own health, self-care, and wellbeing:",
                "type": "single_choice",
                "options": [
                    "I naturally prioritize it alongside caring for others",
                    "I know what I should do but struggle to follow through",
                    "I care for everyone else first, no energy left for me",
                    "I feel selfish or guilty focusing on my own needs",
                    "I completely neglect my own needs"
                ],
                "patterns": [None, 7, 7, 7, 7],
                "weights": [0, 2, 3, 3, 4],
                "adaptive_triggers": ["self_neglect"],
                "clinical_insight": "Self-care capacity patterns"
            },
            21: {
                "text": "Your major life goals are primarily influenced by:",
                "type": "single_choice",
                "options": [
                    "What I genuinely desire for my own fulfillment",
                    "What my family expected or dreamed for me",
                    "Honoring someone who died or sacrificed",
                    "Proving I'm worthy of someone's love",
                    "Rebelling against others' expectations"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 3, 3, 2],
                "adaptive_triggers": ["family_loyalty"],
                "clinical_insight": "Autonomy versus loyalty conflicts"
            },
            22: {
                "text": "With certain people or situations, you tend to:",
                "type": "single_choice",
                "options": [
                    "Stay true to your values and boundaries",
                    "Become someone you don't recognize",
                    "Lose all your usual boundaries",
                    "Can't say no even when you want to",
                    "Completely lose sense of self"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 3, 3, 4],
                "adaptive_triggers": ["boundary_collapse"],
                "clinical_insight": "Context-dependent self-regulation"
            },
            23: {
                "text": "What would you lose if this pattern completely disappeared tomorrow?",
                "type": "text_completion",
                "placeholder": "Consider: What protection does it provide? What identity might change? How might relationships shift?",
                "patterns": "secondary_gain",
                "min_chars": 40,
                "adaptive_triggers": ["resistance_mapping"],
                "clinical_insight": "Secondary gain identification"
            },
            24: {
                "text": "How easily can you become completely absorbed in movies, books, or daydreams?",
                "type": "single_choice",
                "options": [
                    "Very easily - completely lose track of time",
                    "Moderately easily - can get quite absorbed",
                    "Sometimes - depends on my mood",
                    "Rarely - usually remain aware of surroundings",
                    "Almost never - always maintain awareness"
                ],
                "patterns": "absorption_capacity",
                "weights": [5, 4, 3, 2, 1],
                "clinical_insight": "Natural trance capacity assessment"
            },
            25: {
                "text": "What type of therapeutic guidance appeals most to you?",
                "type": "single_choice",
                "options": [
                    "Direct, clear instructions and guidance",
                    "Gentle, permissive suggestions",
                    "Metaphorical stories and symbolic approaches",
                    "Collaborative exploration together",
                    "Scientific explanations and logical understanding"
                ],
                "patterns": "therapeutic_preference",
                "clinical_insight": "Therapeutic modality optimization"
            }
        }

    def _get_adaptive_question_pools(self):
        """Targeted follow-up questions triggered by specific responses"""
        return {
            "unhappiness_deep": {
                26: {
                    "text": "What messages did you receive in your family about happiness and success?",
                    "type": "single_choice",
                    "options": [
                        "Happiness is natural and should be celebrated",
                        "Happiness must be earned through achievement",
                        "Too much happiness leads to disappointment",
                        "Others' happiness is more important than your own",
                        "Happiness is selfish or frivolous"
                    ],
                    "patterns": [None, 5, 1, 7, 1],
                    "weights": [0, 2, 3, 2, 3],
                    "clinical_insight": "Intergenerational happiness patterns"
                }
            },
            "conflict_trauma": {
                27: {
                    "text": "During childhood conflicts, the adults around you typically:",
                    "type": "single_choice",
                    "options": [
                        "Modeled healthy conflict resolution",
                        "Escalated conflicts with yelling or aggression",
                        "Completely avoided conflict",
                        "Used guilt or manipulation",
                        "Were unpredictable in responses"
                    ],
                    "patterns": [None, 2, 2, 2, 2],
                    "weights": [0, 3, 2, 3, 4],
                    "clinical_insight": "Early conflict modeling"
                }
            },
            "trust_trauma": {
                28: {
                    "text": "Your earliest trust violation involved:",
                    "type": "single_choice",
                    "options": [
                        "No significant early violations",
                        "Broken promises from caregivers",
                        "Betrayal by close friends",
                        "Emotional unavailability",
                        "Abuse or severe neglect"
                    ],
                    "patterns": [None, 3, 3, 3, 3],
                    "weights": [0, 2, 2, 3, 4],
                    "clinical_insight": "Trust development history"
                }
            },
            "binary_thinking": {
                29: {
                    "text": "Where did you learn that choices had to be either/or?",
                    "type": "text_completion",
                    "placeholder": "Consider family rules, religious teachings, school experiences...",
                    "patterns": "cognitive_conditioning",
                    "min_chars": 30,
                    "clinical_insight": "Rigid thinking pattern origins"
                }
            },
            "performance_anxiety": {
                30: {
                    "text": "What childhood experiences linked your worth to performance?",
                    "type": "text_completion",
                    "placeholder": "Think about school, activities, family expectations...",
                    "patterns": "worth_conditioning",
                    "min_chars": 30,
                    "clinical_insight": "Performance-based worth conditioning"
                }
            },
            "identity_fragmentation": {
                31: {
                    "text": "When did you learn to show different selves to different people?",
                    "type": "text_completion",
                    "placeholder": "Consider family dynamics, social groups, safety concerns...",
                    "patterns": "identity_development",
                    "min_chars": 30,
                    "clinical_insight": "Authentic self-expression patterns"
                }
            },
            "self_neglect": {
                32: {
                    "text": "Who modeled self-sacrifice as virtue in your upbringing?",
                    "type": "single_choice",
                    "options": [
                        "No one specifically modeled self-sacrifice",
                        "Primary caregiver",
                        "Extended family member",
                        "Religious or cultural community",
                        "Multiple people - it was the norm"
                    ],
                    "patterns": [None, 7, 7, 7, 7],
                    "weights": [0, 2, 2, 2, 3],
                    "clinical_insight": "Self-sacrifice modeling"
                }
            },
            "family_loyalty": {
                33: {
                    "text": "What unspoken family rules still govern your choices?",
                    "type": "text_completion",
                    "placeholder": "Consider career expectations, relationship choices, values...",
                    "patterns": "family_rules",
                    "min_chars": 30,
                    "clinical_insight": "Family system dynamics"
                }
            },
            "boundary_collapse": {
                34: {
                    "text": "When did you learn that others' needs come before your own?",
                    "type": "text_completion",
                    "placeholder": "Think about early caretaking roles, family dynamics...",
                    "patterns": "boundary_development",
                    "min_chars": 30,
                    "clinical_insight": "Boundary formation history"
                }
            }
        }

    def _get_safety_questions(self):
        """Safety assessment triggered by risk indicators"""
        return {
            "support_system": {
                35: {
                    "text": "If you were in emotional crisis right now, you would:",
                    "type": "single_choice",
                    "options": [
                        "Have multiple trusted people to reach out to",
                        "Have one reliable person to contact",
                        "Try to handle it alone first",
                        "Not feel comfortable reaching out",
                        "Have no one available"
                    ],
                    "risk_assessment": True,
                    "weights": [0, 0, 1, 2, 3],
                    "clinical_insight": "Crisis support system"
                }
            },
            "safety_planning": {
                36: {
                    "text": "Do you have strategies for managing overwhelming emotions?",
                    "type": "single_choice",
                    "options": [
                        "Yes, multiple effective strategies",
                        "Some strategies that work",
                        "Basic strategies but don't always help",
                        "Few strategies, rarely effective",
                        "No strategies - feel helpless"
                    ],
                    "risk_assessment": True,
                    "weights": [0, 0, 1, 2, 3],
                    "clinical_insight": "Emotional regulation capacity"
                }
            }
        }

    def _get_hypnotic_responsiveness_questions(self):
        """Hypnotic susceptibility assessment"""
        return {
            "hypnotic_profile": {
                37: {
                    "text": "How do you typically process information most effectively?",
                    "type": "single_choice",
                    "options": [
                        "Through visual imagery and pictures",
                        "Through physical sensations and feelings",
                        "Through auditory guidance and words",
                        "Through logical understanding",
                        "Through metaphorical and symbolic meaning"
                    ],
                    "patterns": "processing_style",
                    "clinical_insight": "Representational system preference"
                }
            },
            "trance_experience": {
                38: {
                    "text": "Have you experienced hypnotic or trance-like states before?",
                    "type": "single_choice",
                    "options": [
                        "Frequently in meditation or relaxation",
                        "Occasionally in daydreaming or flow states",
                        "Rarely but open to experiencing it",
                        "Never but curious to try",
                        "Skeptical or apprehensive about it"
                    ],
                    "patterns": "trance_familiarity",
                    "weights": [4, 3, 2, 1, 0],
                    "clinical_insight": "Hypnotic experience level"
                }
            }
        }

    # ---- Navigation and Response Logic ----
    def _get_current_question_id(self):
        answered = set(st.session_state.assessment_responses.keys())
        
        # Core questions first
        for qid in sorted(self.core_questions.keys()):
            if qid not in answered:
                return qid
        
        # Adaptive questions
        for pool_name in st.session_state.adaptive_triggered:
            pool = self.adaptive_pools.get(pool_name, {})
            for qid in sorted(pool.keys()):
                if qid not in answered:
                    return qid
        
        # Safety questions
        if st.session_state.risk_flags:
            for pool in self.safety_questions.values():
                for qid in sorted(pool.keys()):
                    if qid not in answered:
                        return qid
        
        # Hypnotic questions
        for pool in self.hypnotic_questions.values():
            for qid in sorted(pool.keys()):
                if qid not in answered:
                    return qid
        
        return None

    def _estimate_total_questions(self):
        base = len(self.core_questions)
        adaptive = len(st.session_state.adaptive_triggered)
        safety = len(st.session_state.risk_flags)
        hypnotic = sum(len(pool) for pool in self.hypnotic_questions.values())
        return base + adaptive + safety + hypnotic

    def _estimate_time_remaining(self):
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        return remaining * 1.25

    def _get_question_by_id(self, q_id):
        if q_id in self.core_questions:
            return self.core_questions[q_id]
        for pool in self.adaptive_pools.values():
            if q_id in pool:
                return pool[q_id]
        for pool in self.safety_questions.values():
            if q_id in pool:
                return pool[q_id]
        for pool in self.hypnotic_questions.values():
            if q_id in pool:
                return pool[q_id]
        return None

    def _save_response(self, q_id, response, question, intensity=None):
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'intensity': intensity,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat()
        }
        
        if intensity:
            st.session_state.intensity_responses[q_id] = intensity
        
        # Process adaptive triggers
        if 'adaptive_triggers' in question:
            for trigger in question['adaptive_triggers']:
                if trigger not in st.session_state.adaptive_triggered:
                    st.session_state.adaptive_triggered.append(trigger)
        
        # Process risk assessment
        if question.get('risk_assessment'):
            weights = question.get('weights', [0])
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(weights) and weights[option_index] >= 2:
                        risk_flag = f"risk_q_{q_id}"
                        if risk_flag not in st.session_state.risk_flags:
                            st.session_state.risk_flags.append(risk_flag)
                except (ValueError, IndexError):
                    pass
        
        # Process pattern scoring
        if 'patterns' in question and question['patterns'] is not None:
            patterns = question['patterns']
            weights = question.get('weights', [1])
            
            if isinstance(patterns, list) and isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(patterns) and patterns[option_index] is not None:
                        pattern_id = patterns[option_index]
                        weight = weights[option_index] if option_index < len(weights) else 1
                        if intensity:
                            weight *= (intensity / 5.0)
                        
                        if pattern_id in st.session_state.pattern_scores:
                            st.session_state.pattern_scores[pattern_id] += weight
                        else:
                            st.session_state.pattern_scores[pattern_id] = weight
                except (ValueError, IndexError):
                    pass
            elif isinstance(patterns, (int, str)):
                weight = weights[0] if weights else 1
                if intensity:
                    weight *= (intensity / 5.0)
                
                if patterns in st.session_state.pattern_scores:
                    st.session_state.pattern_scores[patterns] += weight
                else:
                    st.session_state.pattern_scores[patterns] = weight

    def _advance_question(self):
        st.session_state.current_question += 1

    def _go_back(self):
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
                if last_key in st.session_state.intensity_responses:
                    del st.session_state.intensity_responses[last_key]

    def _complete_assessment(self):
        st.session_state.assessment_completed = True
        
        dominant_pattern = None
        if st.session_state.pattern_scores:
            dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': dominant_pattern,
            'risk_flags': st.session_state.risk_flags,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'adaptive_paths_triggered': st.session_state.adaptive_triggered,
            'intensity_data': dict(st.session_state.intensity_responses),
            'completion_rate': len(st.session_state.assessment_responses) / self._estimate_total_questions() if self._estimate_total_questions() > 0 else 1.0
        }
        st.rerun()

    # ---- rendering functions ----
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
        st.markdown("<h1 style='text-align: center;'>Behavioral pattern assessment</h1>", unsafe_allow_html=True)
        
        if not st.session_state.assessment_completed:
            total_q = self._estimate_total_questions()
            time_remaining = self._estimate_time_remaining()
            st.info(f"**Personalized hypnotherapy starts with understanding your unique patterns.** This assessment identifies your specific behavioral patterns to create the most effective transformation approach. Estimated time: {time_remaining:.0f} minutes.")

    def _render_current_question(self):
        current_q_id = self._get_current_question_id()
        if current_q_id is None:
            self._complete_assessment()
            return
            
        question = self._get_question_by_id(current_q_id)
        if not question:
            st.error("Question configuration error")
            return

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
        <div class="time-estimate">About {time_remaining:.0f} minutes remaining</div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {question['text']}")

        self._handle_response_types(current_q_id, question)
        self._render_navigation(current_q_id)

    def _handle_response_types(self, q_id, question):
        q_type = question['type']
        
        if q_type == 'single_choice':
            for i, option in enumerate(question['options']):
                if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                    self._save_response(q_id, option, question)
                    self._advance_question()
                    st.rerun()
        
        elif q_type == 'single_choice_with_intensity':
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
                    st.caption("1 = very mild")
                with col2:
                    st.caption("7 = extremely intense")
                
                if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                    self._save_response(q_id, selected_option, question, intensity)
                    if selection_key in st.session_state:
                        del st.session_state[selection_key]
                    self._advance_question()
                    st.rerun()
                    
        elif q_type == 'multi_select_weighted':
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
                    intensities[emotion] = st.select_slider(
                        f"{emotion}:",
                        options=[1, 2, 3, 4, 5, 6, 7],
                        format_func=lambda x: f"{x}/7",
                        value=4,
                        key=f"q_{q_id}_{emotion.replace('/', '_')}_intensity"
                    )
                
                if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                    weighted_response = {emotion: intensities[emotion] for emotion in selected}
                    self._save_response(q_id, weighted_response, question)
                    self._advance_question()
                    st.rerun()
                    
        elif q_type == 'text_completion':
            min_chars = question.get('min_chars', 20)
            response = st.text_area(
                "Your response:",
                placeholder=question.get('placeholder', 'Please provide your response...'),
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
                    
        elif q_type == 'scale_7':
            labels = question.get('labels', ['low', 'high'])
            value = st.select_slider(
                "Rate your experience:",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: f"{x}/7",
                value=4,
                key=f"q_{q_id}_scale"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"1 = {labels[0]}")
            with col2:
                st.caption(f"7 = {labels[1]}")
                
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, value, question)
                self._advance_question()
                st.rerun()

    def _render_navigation(self, current_q_id):
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if len(st.session_state.assessment_responses) > 0:
                if st.button("← back", key="nav_back", use_container_width=True):
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
                skip_question = {"patterns": None, "weights": [0], "text": "skipped", "type": "skip"}
                self._save_response(current_q_id, "skipped", skip_question)
                self._advance_question()
                st.rerun()

    def _render_contact_form(self):
        st.markdown("### Assessment complete")
        st.success("Your personalized behavioral analysis is ready!")
        
        results = st.session_state.assessment_results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "completed")
        with col2:
            st.metric("Patterns", len(results.get('pattern_scores', {})), "identified")
        with col3:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completion", f"{completion_rate*100:.0f}%", "rate")

        st.markdown("**Provide your details to receive your comprehensive behavioral pattern analysis:**")
        
        with st.form("contact_form"):
            name = st.text_input("Full name*", placeholder="your full name")
            email = st.text_input("Email*", placeholder="your@email.com")
            phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")
            
            urgency = st.selectbox(
                "How urgent is addressing this pattern?*",
                ["select urgency level...", "extremely urgent - significantly impacting life", 
                 "very urgent - causing daily distress", "moderately urgent - noticeable impact", 
                 "somewhat urgent - want to address soon", "not urgent - exploring options"]
            )
            
            concern = st.text_area(
                "What brought you to this assessment?*",
                placeholder="brief description of what motivated you to take this assessment...",
                height=100
            )
            
            next_step = st.selectbox(
                "Preferred next step:*",
                ["select your preference...", "schedule free consultation call", 
                 "information about transformation packages", "receive analysis and recommendations first", 
                 "connect with clinical team directly"]
            )
            
            marketing_consent = st.checkbox(
                "i consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
            )
            
            submitted = st.form_submit_button("Get my personalized analysis", type="primary", use_container_width=True)
            
            if submitted:
                errors = []
                if not name.strip(): 
                    errors.append("name is required")
                if not email.strip(): 
                    errors.append("email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

    def _advance_question(self):
        st.session_state.current_question += 1

    def _go_back(self):
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
                if last_key in st.session_state.intensity_responses:
                    del st.session_state.intensity_responses[last_key]

    def _complete_assessment(self):
        st.session_state.assessment_completed = True
        
        dominant_pattern = None
        if st.session_state.pattern_scores:
            dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': dominant_pattern,
            'risk_flags': st.session_state.risk_flags,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'adaptive_paths_triggered': st.session_state.adaptive_triggered,
            'intensity_data': dict(st.session_state.intensity_responses),
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
            total_q = self._estimate_total_questions()
            time_remaining = self._estimate_time_remaining()
            st.info(f"**Personalized hypnotherapy starts with understanding your unique patterns.** This clinical assessment identifies your specific behavioral patterns to create the most effective transformation approach. Estimated time: {time_remaining:.0f} minutes.")

    def _render_current_question(self):
        current_q_id = self._get_current_question_id()
        if current_q_id is None:
            self._complete_assessment()
            return
            
        question = self._get_question_by_id(current_q_id)
        if not question:
            st.error("Question configuration error")
            return

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
        <div class="time-estimate">About {time_remaining:.0f} minutes remaining</div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {question['text']}")
        
        if 'clinical_insight' in question:
            with st.expander("Clinical Context", expanded=False):
                st.markdown(f"**Purpose:** {question['clinical_insight']}")

        self._handle_response_types(current_q_id, question)
        self._render_navigation(current_q_id)

    def _handle_response_types(self, q_id, question):
        q_type = question['type']
        
        if q_type == 'single_choice':
            for i, option in enumerate(question['options']):
                if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                    self._save_response(q_id, option, question)
                    self._advance_question()
                    st.rerun()
        
        elif q_type == 'single_choice_with_intensity':
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
                    
        elif q_type == 'multi_select_weighted':
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
                    intensities[emotion] = st.select_slider(
                        f"{emotion}:",
                        options=[1, 2, 3, 4, 5, 6, 7],
                        format_func=lambda x: f"{x}/7",
                        value=4,
                        key=f"q_{q_id}_{emotion.replace('/', '_')}_intensity"
                    )
                
                if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                    weighted_response = {emotion: intensities[emotion] for emotion in selected}
                    self._save_response(q_id, weighted_response, question)
                    self._advance_question()
                    st.rerun()
                    
        elif q_type == 'text_completion':
            min_chars = question.get('min_chars', 20)
            response = st.text_area(
                "Your response:",
                placeholder=question.get('placeholder', 'Please provide your response...'),
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
                    
        elif q_type == 'scale_7':
            labels = question.get('labels', ['Low', 'High'])
            value = st.select_slider(
                "Rate your experience:",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: f"{x}/7",
                value=4,
                key=f"q_{q_id}_scale"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"1 = {labels[0]}")
            with col2:
                st.caption(f"7 = {labels[1]}")
                
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, value, question)
                self._advance_question()
                st.rerun()

    def _render_navigation(self, current_q_id):
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
                skip_question = {"patterns": None, "weights": [0], "text": "Skipped", "type": "skip"}
                self._save_response(current_q_id, "Skipped", skip_question)
                self._advance_question()
                st.rerun()

    def _render_contact_form(self):
        st.markdown("### Assessment Complete")
        st.success("Your personalized behavioral analysis is ready!")
        
        results = st.session_state.assessment_results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "Completed")
        with col2:
            st.metric("Patterns", len(results.get('pattern_scores', {})), "Identified")
        with col3:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")

        st.markdown("**Provide your details to receive your comprehensive behavioral pattern analysis:**")
        
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
                    st.session_state.contact_provided = True
                    st.success("Contact information saved! Generating your analysis...")
                    st.rerun()

    def _render_results(self):
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
                strength = "High" if score >= 5 else "Moderate" if score >= 3 else "Mild"
                
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


# ---- Main Application Class ----
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
        'assessment_responses', 'current_question', 'question_sequence',
        'adaptive_triggered', 'assessment_completed', 'contact_provided',
        'assessment_results', 'pattern_scores', 'risk_flags', 'intensity_responses'
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
        'adaptive_triggered': st.session_state.get('adaptive_triggered', []),
        'risk_flags': st.session_state.get('risk_flags', []),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }


# ---- Main Execution ----
if __name__ == "__main__":
    st.set_page_config(
        page_title="Behavioral Pattern Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render(), email):
                    errors.append("valid email address is required")
                if not concern.strip(): 
                    errors.append("please describe what brought you here")
                if urgency == "select urgency level...": 
                    errors.append("please select urgency level")
                if next_step == "select your preference...": 
                    errors.append("please select your preferred next step")
                if not marketing_consent:
                    errors.append("please consent to follow-up communications to receive your results")
                
                if errors:
                    for error in errors:
                        st.error(f"❌ {error}")
                else:
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
                    st.session_state.contact_provided = True
                    st.success("Contact information saved! Generating your analysis...")
                    st.rerun()

    def _render_results(self):
        st.markdown("## Your behavioral pattern analysis")
        
        contact_info = st.session_state.get('contact_info', {})
        st.success(f"Thank you, {contact_info.get('name', 'there')}! Your comprehensive analysis has been generated.")
        
        results = st.session_state.assessment_results
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "answered")
        with col2:
            patterns_count = len(results.get('pattern_scores', {}))
            st.metric("Patterns", patterns_count, "detected")
        with col3:
            risk_count = len(results.get('risk_flags', []))
            st.metric("Risk factors", risk_count, "identified")
        with col4:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completeness", f"{completion_rate*100:.0f}%", "assessment")

        self._render_clinical_analysis_section()

        st.markdown("### Your next steps")
        
        next_step = contact_info.get('next_step', '')
        urgency = contact_info.get('urgency', '')
        
        if 'extremely urgent' in urgency.lower() or 'very urgent' in urgency.lower():
            st.warning("⚠️ **Priority contact**: given your urgency level, our clinical team will contact you within 24 hours.")
        
        if 'consultation' in next_step.lower():
            st.info("📅 **Consultation scheduling**: we'll contact you within 48 hours to schedule your free consultation call.")
        elif 'package' in next_step.lower():
            st.success("📋 **Transformation packages**: we'll send you detailed information about our personalized programs.")
        elif 'analysis' in next_step.lower():
            st.info("📊 **Analysis first**: we'll email your detailed analysis and specific recommendations.")
        else:
            st.info("🤝 **Clinical team contact**: our team will reach out with personalized next steps.")
        
        st.markdown("""
        **What happens next:**

        1. **Clinical review** (24-48 hours): licensed therapist analyzes your responses
        2. **Personalized protocol** (48-72 hours): custom hypnotherapy approach designed for your patterns  
        3. **Initial contact** (48-72 hours): we'll reach out via your preferred method
        4. **Transformation planning** (1 week): develop your individualized program
        
        **Questions?** Reply to any email from us or contact our clinical team directly.
        """)

    def _render_clinical_analysis_section(self):
        st.markdown("### Clinical pattern analysis")
        
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
                    with st.expander("🔓 unlock complete clinical analysis", expanded=True):
                        paywall.render_paywall_interface(assessment_data)
            except Exception as e:
                st.error(f"Error loading premium analysis: {str(e)}")
                self._render_analysis_preview()
        else:
            st.info("💡 **Premium analysis available**: comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
            self._render_analysis_preview()

    def _render_analysis_preview(self):
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            st.markdown("**🎯 Your top behavioral patterns:**")
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            descriptions = {
                1: "difficulty accepting or maintaining positive emotional states",
                2: "recurring conflicts and power struggles in relationships", 
                3: "default skepticism and difficulty trusting others' intentions",
                4: "black-and-white thinking patterns that limit options",
                5: "self-worth tied to productivity and achievement",
                6: "inconsistent sense of identity across different contexts",
                7: "prioritizing others' needs while neglecting self-care",
                8: "life choices driven by family expectations",
                9: "context-dependent loss of personal boundaries"
            }
            
            for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
                pattern_name = self.patterns.get(pattern_id, f"pattern {pattern_id}")
                strength = "high" if score >= 5 else "moderate" if score >= 3 else "mild"
                
                st.markdown(f"**{i+1}. {pattern_name}** - *{strength} intensity pattern detected*")
                
                if pattern_id in descriptions:
                    st.caption(descriptions[pattern_id])
            
            if len(sorted_patterns) > 3:
                remaining = len(sorted_patterns) - 3
                st.write(f"*plus {remaining} additional patterns identified...*")
        
        risk_count = len(results.get('risk_flags', []))
        if risk_count > 0:
            st.markdown(f"**⚠️ Clinical considerations:** {risk_count} factors requiring specialized approach")
        
        st.info("**Complete analysis includes:** detailed pattern breakdowns, root cause analysis, personalized hypnotherapy protocol, session planning, and progress tracking recommendations.")


# ---- main application class ----
class AssessPage:
    """Main application wrapper maintaining compatibility with original interface"""
    
    def __init__(self):
        self.assessment = ComprehensiveBehavioralAssessment()
    
    def render(self):
        self.assessment.render()


# ---- page factory function ----
def create_assess_page():
    """Factory function to create the assessment page"""
    return AssessPage()


# ---- helper functions ----
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
        'assessment_responses', 'current_question', 'question_sequence',
        'adaptive_triggered', 'assessment_completed', 'contact_provided',
        'assessment_results', 'pattern_scores', 'risk_flags', 'intensity_responses'
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
        'adaptive_triggered': st.session_state.get('adaptive_triggered', []),
        'risk_flags': st.session_state.get('risk_flags', []),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }


# ---- main execution ----
if __name__ == "__main__":
    st.set_page_config(
        page_title="Behavioral pattern assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render()

    def _advance_question(self):
        st.session_state.current_question += 1

    def _go_back(self):
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
                if last_key in st.session_state.intensity_responses:
                    del st.session_state.intensity_responses[last_key]

    def _complete_assessment(self):
        st.session_state.assessment_completed = True
        
        dominant_pattern = None
        if st.session_state.pattern_scores:
            dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': dominant_pattern,
            'risk_flags': st.session_state.risk_flags,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'adaptive_paths_triggered': st.session_state.adaptive_triggered,
            'intensity_data': dict(st.session_state.intensity_responses),
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
            total_q = self._estimate_total_questions()
            time_remaining = self._estimate_time_remaining()
            st.info(f"**Personalized hypnotherapy starts with understanding your unique patterns.** This clinical assessment identifies your specific behavioral patterns to create the most effective transformation approach. Estimated time: {time_remaining:.0f} minutes.")

    def _render_current_question(self):
        current_q_id = self._get_current_question_id()
        if current_q_id is None:
            self._complete_assessment()
            return
            
        question = self._get_question_by_id(current_q_id)
        if not question:
            st.error("Question configuration error")
            return

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
        <div class="time-estimate">About {time_remaining:.0f} minutes remaining</div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {question['text']}")
        
        if 'clinical_insight' in question:
            with st.expander("Clinical Context", expanded=False):
                st.markdown(f"**Purpose:** {question['clinical_insight']}")

        self._handle_response_types(current_q_id, question)
        self._render_navigation(current_q_id)

    def _handle_response_types(self, q_id, question):
        q_type = question['type']
        
        if q_type == 'single_choice':
            for i, option in enumerate(question['options']):
                if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                    self._save_response(q_id, option, question)
                    self._advance_question()
                    st.rerun()
        
        elif q_type == 'single_choice_with_intensity':
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
                    
        elif q_type == 'multi_select_weighted':
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
                    intensities[emotion] = st.select_slider(
                        f"{emotion}:",
                        options=[1, 2, 3, 4, 5, 6, 7],
                        format_func=lambda x: f"{x}/7",
                        value=4,
                        key=f"q_{q_id}_{emotion.replace('/', '_')}_intensity"
                    )
                
                if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                    weighted_response = {emotion: intensities[emotion] for emotion in selected}
                    self._save_response(q_id, weighted_response, question)
                    self._advance_question()
                    st.rerun()
                    
        elif q_type == 'text_completion':
            min_chars = question.get('min_chars', 20)
            response = st.text_area(
                "Your response:",
                placeholder=question.get('placeholder', 'Please provide your response...'),
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
                    
        elif q_type == 'scale_7':
            labels = question.get('labels', ['Low', 'High'])
            value = st.select_slider(
                "Rate your experience:",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: f"{x}/7",
                value=4,
                key=f"q_{q_id}_scale"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"1 = {labels[0]}")
            with col2:
                st.caption(f"7 = {labels[1]}")
                
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, value, question)
                self._advance_question()
                st.rerun()

    def _render_navigation(self, current_q_id):
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
                skip_question = {"patterns": None, "weights": [0], "text": "Skipped", "type": "skip"}
                self._save_response(current_q_id, "Skipped", skip_question)
                self._advance_question()
                st.rerun()

    def _render_contact_form(self):
        st.markdown("### Assessment Complete")
        st.success("Your personalized behavioral analysis is ready!")
        
        results = st.session_state.assessment_results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions", results['total_questions_answered'], "Completed")
        with col2:
            st.metric("Patterns", len(results.get('pattern_scores', {})), "Identified")
        with col3:
            completion_rate = results.get('completion_rate', 1.0)
            st.metric("Completion", f"{completion_rate*100:.0f}%", "Rate")

        st.markdown("**Provide your details to receive your comprehensive behavioral pattern analysis:**")
        
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
                    st.session_state.contact_provided = True
                    st.success("Contact information saved! Generating your analysis...")
                    st.rerun()

    def _render_results(self):
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
                strength = "High" if score >= 5 else "Moderate" if score >= 3 else "Mild"
                
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


# ---- Main Application Class ----
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
        'assessment_responses', 'current_question', 'question_sequence',
        'adaptive_triggered', 'assessment_completed', 'contact_provided',
        'assessment_results', 'pattern_scores', 'risk_flags', 'intensity_responses'
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
        'adaptive_triggered': st.session_state.get('adaptive_triggered', []),
        'risk_flags': st.session_state.get('risk_flags', []),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }


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
