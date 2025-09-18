"""
Behavioral Pattern Assessment Page
A comprehensive, mobile-optimized assessment tool for behavioral pattern analysis
with dynamic analytics, email integration, and personalized results.
"""

import streamlit as st
import re
import smtplib
import json
from datetime import datetime
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
from email.mime.base import MimeBase
from email import encoders
import traceback

# ================================
# 1. CORE CONFIGURATION & PATTERNS
# ================================

class PatternDefinitions:
    """Core behavioral pattern definitions and descriptions"""
    
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
            "description": "You may find it challenging to accept or maintain positive emotional states",
            "impact": "This can limit your ability to fully enjoy success and happiness",
            "transformation": "Learning to trust that joy and success can be sustainable and deserved",
            "insights_map": "Your mind has learned to deflect happiness as protection against disappointment - but this same mechanism is preventing the joy you deserve",
            "what_you_notice": "Feeling guilty when things go well, waiting for the other shoe to drop, minimizing achievements",
            "what_others_see": "Someone who deflects compliments, seems uncomfortable with praise, or finds problems in good situations",
            "hidden_cost": "Missing out on life's genuine pleasures and the motivation that comes from celebrating wins",
            "breakthrough_moment": "Realizing that happiness doesn't make you vulnerable - it makes you stronger and more resilient"
        },
        2: {
            "name": "Power struggles",
            "description": "You experience recurring conflicts and power struggles in relationships", 
            "impact": "This can create stress and prevent collaborative problem-solving",
            "transformation": "Developing skills for curious dialogue and win-win resolution",
            "insights_map": "You're fighting battles that don't need to be fought - your nervous system activates 'combat mode' even in collaborative situations",
            "what_you_notice": "Feeling defensive quickly, needing to be right, seeing disagreements as threats",
            "what_others_see": "Someone who argues their point intensely, seems confrontational, or withdraws when challenged",
            "hidden_cost": "Exhausting mental energy on conflicts instead of creative collaboration and genuine connection",
            "breakthrough_moment": "Discovering that being curious about others' perspectives actually strengthens your position"
        },
        3: {
            "name": "Systematic mistrust",
            "description": "You maintain a default skepticism about others' intentions",
            "impact": "This protective mechanism may limit deep connections and opportunities", 
            "transformation": "Calibrating trust responses and building authentic relationships",
            "insights_map": "Your protective skepticism, while once useful, is now creating the very rejection and isolation you're trying to avoid",
            "what_you_notice": "Analyzing people's motives, feeling suspicious of kindness, expecting hidden agendas",
            "what_others_see": "Someone who seems guarded, asks probing questions, or appears cynical about human nature",
            "hidden_cost": "Living in emotional isolation and missing genuine opportunities for support and connection",
            "breakthrough_moment": "Understanding that discernment and openness can coexist - you can be wise AND trusting"
        },
        4: {
            "name": "Separation and division",
            "description": "You tend toward black-and-white thinking patterns",
            "impact": "This can limit creative solutions and increase decision paralysis",
            "transformation": "Developing nuanced thinking and embracing creative possibilities",
            "insights_map": "Your brilliant analytical mind gets trapped in 'either/or' thinking when 'both/and' solutions would serve you better",
            "what_you_notice": "Feeling stuck between two options, seeing things as all good or all bad, struggling with grey areas",
            "what_others_see": "Someone who wants clear answers, seems frustrated by ambiguity, or makes quick either/or judgments",
            "hidden_cost": "Missing innovative solutions that require holding multiple perspectives simultaneously",
            "breakthrough_moment": "Realizing that complexity isn't confusion - it's where the most elegant solutions hide"
        },
        5: {
            "name": "Doing versus being",
            "description": "Your self-worth is closely tied to productivity and achievement",
            "impact": "This can lead to burnout and difficulty with rest or self-care",
            "transformation": "Anchoring worth in your inherent value, independent of accomplishments",
            "insights_map": "You've created an equation where doing = worth, but your actual value exists independent of any achievement",
            "what_you_notice": "Feeling anxious when not productive, equating rest with laziness, measuring yourself by output",
            "what_others_see": "Someone who's always busy, seems uncomfortable with downtime, or talks about achievements frequently",
            "hidden_cost": "Chronic stress, missed opportunities for reflection and creativity that come from mental space",
            "breakthrough_moment": "Discovering that your value exists completely separate from what you do or achieve"
        },
        6: {
            "name": "Compartmentalized authenticity",
            "description": "Your sense of identity shifts significantly across different contexts",
            "impact": "This can create internal confusion and emotional exhaustion",
            "transformation": "Integrating an authentic, consistent self across all situations",
            "insights_map": "You're exhausting yourself maintaining different versions of yourself instead of trusting that your authentic self is enough",
            "what_you_notice": "Feeling like different people in different settings, adapting personality to fit in, losing sense of 'real self'",
            "what_others_see": "Someone who seems different depending on the group, appears to chameleon, or seems inconsistent",
            "hidden_cost": "Emotional exhaustion from performance, loss of authentic self-expression and genuine connections",
            "breakthrough_moment": "Realizing that your authentic self is actually more likeable and magnetic than any persona"
        },
        7: {
            "name": "Self sacrifice and care avoidance",
            "description": "You prioritize others' needs while neglecting your own self-care",
            "impact": "This can lead to resentment and emotional depletion over time",
            "transformation": "Developing healthy boundaries and self-care practices",
            "insights_map": "Your generous heart has learned to give to others but forgotten how to receive - creating an unsustainable energy drain",
            "what_you_notice": "Feeling guilty when focusing on yourself, automatically saying yes to requests, feeling responsible for others' emotions",
            "what_others_see": "Someone who's always helpful, never seems to have needs, or appears stressed but won't ask for help",
            "hidden_cost": "Resentment buildup, burnout, and becoming less effective at helping others when you're depleted",
            "breakthrough_moment": "Understanding that taking care of yourself is actually the most loving thing you can do for others"
        },
        8: {
            "name": "Inherited missions",
            "description": "Your life choices are driven more by family expectations than personal desires",
            "impact": "This can create internal conflict and limit authentic self-expression",
            "transformation": "Clarifying personal values while maintaining family harmony",
            "insights_map": "You're living someone else's dream while your own authentic desires remain buried under family expectations",
            "what_you_notice": "Feeling torn between what you want and what's expected, guilt about disappointing family, unclear about your own desires",
            "what_others_see": "Someone who references family expectations often, seems conflicted about decisions, or appears to live for others",
            "hidden_cost": "Living someone else's life instead of your own, missing your unique contribution to the world",
            "breakthrough_moment": "Realizing you can honor your family AND live authentically - they're not mutually exclusive"
        },
        9: {
            "name": "Context dependent weakness",
            "description": "Your boundaries and limits vary dramatically based on context",
            "impact": "This can lead to inconsistent relationships and self-advocacy",
            "transformation": "Establishing consistent, healthy boundaries across all situations",
            "insights_map": "Your boundaries disappear in certain contexts because you've never learned you can be both loved and boundaried",
            "what_you_notice": "Being strong in some situations but passive in others, feeling like you lose yourself in certain contexts",
            "what_others_see": "Someone who seems confident sometimes but submissive other times, appears unpredictable in their responses",
            "hidden_cost": "Confusion about your own limits, relationships built on false premises, accumulated resentment",
            "breakthrough_moment": "Discovering that consistent boundaries actually make you more trustworthy and respected"
        }
    }

# ================================
# 2. QUESTION SETS & LOGIC
# ================================

class QuestionSets:
    """Complete question sets for dynamic assessment"""
    
    @staticmethod
    def get_core_questions():
        """Core 25 questions that all users answer"""
        return {
            1: {
                "text": "What specific behavior or pattern would you most like to transform?",
                "type": "text_area",
                "placeholder": "Describe the exact behavior, feeling, or situation you want to change...",
                "min_chars": 10,
                "patterns": ["presenting_problem"],
                "category": "initial_assessment"
            },
            2: {
                "text": "When something genuinely good happens to you, your first reaction is usually:",
                "type": "single_choice",
                "options": [
                    "Pure enjoyment and celebration",
                    "Immediately looking for the catch or downside", 
                    "Feeling guilty or undeserving of good things",
                    "Minimizing its importance",
                    "Anxiety about when it will end"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 3, 3, 2, 2],
                "category": "pattern_detection"
            },
            3: {
                "text": "During conflicts or disagreements, your nervous system typically:",
                "type": "single_choice",
                "options": [
                    "Stays curious about their perspective",
                    "Immediately activates into combat mode",
                    "Feels threatened or attacked",
                    "Shuts down to avoid confrontation",
                    "Searches for ways to prove them wrong"
                ],
                "patterns": [None, 2, 2, 2, 2],
                "weights": [0, 3, 2, 1, 3],
                "category": "pattern_detection"
            },
            4: {
                "text": "When meeting new people, you typically assume they:",
                "type": "single_choice",
                "options": [
                    "Are generally well-intentioned",
                    "Are judging or evaluating you",
                    "Want something from you",
                    "Will eventually disappoint you",
                    "Are basically indifferent"
                ],
                "patterns": [None, 3, 3, 3, 3],
                "weights": [0, 2, 3, 3, 1],
                "category": "pattern_detection"
            },
            5: {
                "text": "When facing important decisions, you typically:",
                "type": "single_choice",
                "options": [
                    "See multiple creative possibilities",
                    "Feel trapped between two impossible choices",
                    "Get paralyzed by perfectionist analysis",
                    "Create artificial deadlines or urgency",
                    "Defer to what others expect"
                ],
                "patterns": [None, 4, 4, 4, 4],
                "weights": [0, 2, 3, 2, 1],
                "category": "pattern_detection"
            },
            6: {
                "text": "You feel most valuable when you're:",
                "type": "single_choice",
                "options": [
                    "Simply existing as yourself",
                    "Accomplishing something significant",
                    "Being productive or busy",
                    "Helping others achieve their goals",
                    "Receiving recognition for your work"
                ],
                "patterns": [None, 5, 5, 5, 5],
                "weights": [0, 2, 3, 2, 2],
                "category": "pattern_detection"
            },
            7: {
                "text": "Your personality tends to:",
                "type": "single_choice",
                "options": [
                    "Stay consistent across all situations",
                    "Shift significantly based on who you're with",
                    "Change between professional and personal settings",
                    "Adapt to what others seem to want",
                    "Feel fragmented or inconsistent"
                ],
                "patterns": [None, 6, 6, 6, 6],
                "weights": [0, 2, 2, 3, 4],
                "category": "pattern_detection"
            },
            8: {
                "text": "When it comes to your own needs versus others' needs:",
                "type": "single_choice",
                "options": [
                    "I naturally balance both",
                    "Others' needs usually come first",
                    "I feel guilty focusing on my own needs",
                    "I often don't even know what I need",
                    "Taking care of myself feels selfish"
                ],
                "patterns": [None, 7, 7, 7, 7],
                "weights": [0, 2, 3, 3, 4],
                "category": "pattern_detection"
            },
            9: {
                "text": "Your major life goals are primarily:",
                "type": "single_choice",
                "options": [
                    "Based on your own genuine desires",
                    "Influenced by family expectations",
                    "Meant to honor someone's sacrifices",
                    "Designed to prove your worth",
                    "A reaction against others' expectations"
                ],
                "patterns": [None, 8, 8, 8, 8],
                "weights": [0, 2, 3, 3, 2],
                "category": "pattern_detection"
            },
            10: {
                "text": "Your boundaries and limits:",
                "type": "single_choice",
                "options": [
                    "Stay pretty consistent across situations",
                    "Vary significantly based on who you're with",
                    "Disappear completely in certain contexts",
                    "Are stronger in some areas than others",
                    "Feel almost non-existent sometimes"
                ],
                "patterns": [None, 9, 9, 9, 9],
                "weights": [0, 2, 3, 2, 4],
                "category": "pattern_detection"
            },
            11: {
                "text": "When this pattern gets triggered, what's the first physical sensation you notice?",
                "type": "text_area",
                "placeholder": "e.g., chest tightness, stomach drop, heat flush, numbness...",
                "min_chars": 5,
                "patterns": ["somatic_response"],
                "category": "trigger_mapping"
            },
            12: {
                "text": "What automatic thoughts accompany these physical sensations?",
                "type": "text_area",
                "placeholder": "What does your inner voice say in these moments?",
                "min_chars": 5,
                "patterns": ["automatic_thoughts"],
                "category": "trigger_mapping"
            },
            13: {
                "text": "After those thoughts, you typically feel:",
                "type": "multi_select",
                "options": [
                    "Anxious or worried", "Angry or frustrated", "Ashamed or embarrassed",
                    "Sad or defeated", "Guilty or self-blaming", "Overwhelmed or panicked",
                    "Numb or disconnected", "Confused or uncertain"
                ],
                "max_selections": 3,
                "patterns": ["emotional_response"],
                "category": "trigger_mapping"
            },
            14: {
                "text": "When you feel that emotion, you typically:",
                "type": "single_choice",
                "options": [
                    "Withdraw, avoid, or postpone dealing with it",
                    "Become more active, busy, or productive",
                    "Seek reassurance or validation from others",
                    "Become argumentative or defensive", 
                    "Try to control or fix the situation",
                    "Please others or put their needs first",
                    "Shut down emotionally or 'check out'"
                ],
                "patterns": [1, 5, 3, 2, 2, 7, 6],
                "weights": [2, 3, 2, 3, 2, 3, 3],
                "category": "behavioral_response"
            },
            15: {
                "text": "What would you lose if this pattern disappeared completely?",
                "type": "text_area",
                "placeholder": "Consider protection, identity, relationships, expectations...",
                "min_chars": 10,
                "patterns": ["secondary_gain"],
                "category": "resistance_mapping"
            },
            16: {
                "text": "How ready are you to completely let go of this pattern?",
                "type": "scale",
                "min_value": 1,
                "max_value": 10,
                "labels": ["Not ready at all", "Completely ready"],
                "patterns": ["readiness_level"],
                "category": "change_readiness"
            },
            17: {
                "text": "If this issue completely resolved, what would be different about your daily life?",
                "type": "text_area",
                "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible...",
                "min_chars": 15,
                "patterns": ["outcome_vision"],
                "category": "outcome_mapping"
            },
            18: {
                "text": "What fears come up about actually changing this pattern?",
                "type": "multi_select",
                "options": [
                    "Fear of unknown", "Fear of failure", "Fear of success",
                    "Fear of rejection", "Fear of overwhelming emotions",
                    "Fear of losing identity", "Fear of disappointing others"
                ],
                "max_selections": 4,
                "patterns": ["change_fears"],
                "category": "resistance_mapping"
            },
            19: {
                "text": "How easily can you become absorbed in daydreams or movies?",
                "type": "single_choice",
                "options": [
                    "Very easily - completely lose track of time",
                    "Moderately easily - can get quite absorbed",
                    "Sometimes - depends on my interest level",
                    "Rarely - usually remain aware of surroundings",
                    "Almost never - always maintain full awareness"
                ],
                "patterns": ["hypnotic_susceptibility"],
                "weights": [4, 3, 2, 1, 0],
                "category": "therapeutic_assessment"
            },
            20: {
                "text": "What type of guidance feels most comfortable to you?",
                "type": "single_choice",
                "options": [
                    "Direct and authoritative guidance",
                    "Gentle and permissive suggestions",
                    "Metaphorical and storytelling approach",
                    "Collaborative and exploratory style",
                    "Scientific and logical explanation"
                ],
                "patterns": ["therapeutic_preference"],
                "category": "therapeutic_assessment"
            },
            21: {
                "text": "Growing up, the message about happiness in your family was:",
                "type": "single_choice",
                "options": [
                    "Happiness is natural and should be enjoyed",
                    "Happiness must be earned through hard work",
                    "Too much happiness leads to disappointment", 
                    "Other people's happiness comes first",
                    "Happiness is selfish or shallow"
                ],
                "patterns": [None, 1, 1, 1, 1],
                "weights": [0, 2, 3, 2, 3],
                "category": "family_patterns"
            },
            22: {
                "text": "In your family growing up, disagreements typically:",
                "type": "single_choice",
                "options": [
                    "Were handled through calm discussion",
                    "Escalated into arguments or fights",
                    "Were avoided at all costs",
                    "Involved guilt, manipulation, or silent treatment",
                    "Had clear winners and losers"
                ],
                "patterns": [None, 2, 2, 2, 2],
                "weights": [0, 3, 2, 3, 4],
                "category": "family_patterns"
            },
            23: {
                "text": "How urgently do you need to resolve your main concern?",
                "type": "single_choice",
                "options": [
                    "Extremely urgent - affecting daily life significantly",
                    "Very urgent - need change within few months",
                    "Moderately urgent - within 6 months",
                    "Somewhat urgent - exploring gradual options",
                    "Not urgent - just curious"
                ],
                "patterns": ["urgency_level"],
                "weights": [5, 4, 3, 2, 1],
                "category": "readiness_assessment"
            },
            24: {
                "text": "Have you tried other approaches to address this issue?",
                "type": "multi_select",
                "options": [
                    "Traditional talk therapy", "Self-help books/courses", "Meditation/mindfulness",
                    "Medication", "Life coaching", "Hypnotherapy before",
                    "Support groups", "Nothing specific yet"
                ],
                "patterns": ["previous_attempts"],
                "category": "treatment_history"
            },
            25: {
                "text": "What made you decide to explore hypnotherapy for this particular issue?",
                "type": "text_area",
                "placeholder": "What drew you to this approach specifically?",
                "min_chars": 10,
                "patterns": ["hypnotherapy_motivation"],
                "category": "therapeutic_assessment"
            }
        }

    @staticmethod
    def get_adaptive_questions():
        """Additional questions triggered by specific responses"""
        return {
            "pattern_1_deep": {
                26: {
                    "text": "When good things happen to others, you typically:",
                    "type": "single_choice",
                    "options": [
                        "Feel genuinely happy for them",
                        "Wonder why good things don't happen to me",
                        "Feel it proves I'm not worthy of good things",
                        "Get suspicious about what will balance it"
                    ],
                    "patterns": [None, 1, 1, 1],
                    "weights": [0, 2, 3, 2],
                    "trigger_condition": "pattern_1_score >= 4"
                }
            },
            "pattern_2_deep": {
                27: {
                    "text": "What happens in your body when someone challenges your viewpoint?",
                    "type": "text_area",
                    "placeholder": "Describe the physical sensations - tension, heat, breathing changes...",
                    "min_chars": 10,
                    "patterns": ["conflict_somatic"],
                    "trigger_condition": "pattern_2_score >= 4"
                }
            }
        }

# ================================
# 3. STYLING AND UI COMPONENTS
# ================================

def apply_assessment_styles():
    """Apply professional, mobile-optimized styling"""
    st.markdown("""
    <style>
    /* Reset and base styles */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    @media (min-width: 768px) {
        .main .block-container {
            max-width: 600px !important;
            margin: 0 auto;
        }
    }
    
    /* Button styling for mobile optimization */
    .stButton > button {
        width: 100% !important;
        margin-bottom: 0.5rem !important;
        padding: 0.75rem 1rem !important;
        text-align: left !important;
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        color: #273548 !important;
        font-size: 1rem !important;
        transition: all 0.2s ease !important;
        line-height: 1.4 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
    }
    
    .stButton > button:hover {
        background-color: #F3F6F8 !important;
        border-color: #4CA1A3 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15) !important;
    }
    
    .stButton > button:focus {
        background-color: #F3F6F8 !important;
        border-color: #4CA1A3 !important;
        outline: none !important;
    }
    
    /* Primary button styling */
    .stButton > button[kind="primary"] {
        background-color: #4CA1A3 !important;
        color: white !important;
        border-color: #4CA1A3 !important;
        font-weight: 600 !important;
    }
    
    .stButton > button[kind="primary"]:hover {
        background-color: #3B7A7A !important;
        border-color: #3B7A7A !important;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 1rem !important;
        background-color: #FFFFFF !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #4CA1A3 !important;
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.2) !important;
    }
    
    /* Progress bar styling */
    .progress-container {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        padding: 0.75rem;
        background-color: #FFFFFF;
        border-radius: 8px;
        border: 1px solid #CBD5E1;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .progress-bar {
        flex: 1;
        height: 6px;
        background: #F3F6F8;
        border-radius: 3px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #4CA1A3 0%, #22c55e 100%);
        transition: width 0.3s ease;
        border-radius: 3px;
    }
    
    /* Question styling */
    .question-header {
        background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #4CA1A3;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    
    .question-text {
        color: #273548;
        font-size: 1.1rem;
        line-height: 1.5;
        margin: 0;
        font-weight: 500;
    }
    
    /* Results styling */
    .results-hero {
        background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .pattern-card {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        border-left: 4px solid #4CA1A3;
    }
    
    .insight-box {
        background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
        border: 1px solid #CBD5E1;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 3px solid #4CA1A3;
    }
    
    /* Hide Streamlit elements */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    .stDeployButton {
        display: none !important;
    }
    
    /* Mobile responsive adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .question-header {
            padding: 1rem;
        }
        
        .question-text {
            font-size: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ================================
# 4. ANALYTICS ENGINE
# ================================

class AssessmentAnalytics:
    """Comprehensive analytics engine for behavioral pattern analysis"""
    
    def __init__(self):
        self.patterns = PatternDefinitions.PATTERNS
        self.descriptions = PatternDefinitions.PATTERN_DESCRIPTIONS
    
    def calculate_pattern_scores(self, responses):
        """Calculate scores for each behavioral pattern"""
        pattern_scores = {i: 0 for i in range(1, 10)}
        
        # Process responses for pattern scoring
        for q_id, response_data in responses.items():
            question = QuestionSets.get_core_questions().get(q_id, {})
            response = response_data.get('response', '')
            
            if question.get('type') == 'single_choice':
                self._score_single_choice(question, response, pattern_scores)
            elif question.get('type') == 'multi_select':
                self._score_multi_select(question, response, pattern_scores)
            elif question.get('type') == 'text_area':
                self._score_text_response(question, response, pattern_scores)
            elif question.get('type') == 'scale':
                self._score_scale_response(question, response, pattern_scores)
        
        return pattern_scores
    
    def _score_single_choice(self, question, response, pattern_scores):
        """Score single choice questions"""
        options = question.get('options', [])
        patterns = question.get('patterns', [])
        weights = question.get('weights', [])
        
        try:
            option_index = options.index(response)
            if option_index < len(patterns) and patterns[option_index] is not None:
                pattern_id = patterns[option_index]
                weight = weights[option_index] if option_index < len(weights) else 1
                pattern_scores[pattern_id] += weight
        except (ValueError, IndexError):
            pass  # Response not found in options
    
    def _score_multi_select(self, question, response, pattern_scores):
        """Score multi-select questions"""
        if isinstance(response, list):
            # Each selection adds base weight to relevant patterns
            for selection in response:
                if any(keyword in selection.lower() for keyword in ['anxious', 'worried']):
                    pattern_scores[1] += 1  # Unhappiness culture
                elif any(keyword in selection.lower() for keyword in ['angry', 'frustrated']):
                    pattern_scores[2] += 1  # Power struggles
                elif any(keyword in selection.lower() for keyword in ['ashamed', 'guilty']):
                    pattern_scores[1] += 1  # Unhappiness culture
                elif any(keyword in selection.lower() for keyword in ['numb', 'disconnected']):
                    pattern_scores[6] += 1  # Compartmentalized authenticity
    
    def _score_text_response(self, question, response, pattern_scores):
        """Score text area responses using keyword analysis"""
        if not response or len(response) < 3:
            return
        
        response_lower = response.lower()
        
        # Pattern-specific keyword scoring
        pattern_keywords = {
            1: ['unhappy', 'sad', 'depressed', 'guilty', 'undeserving', 'doom', 'worry'],
            2: ['angry', 'fight', 'argue', 'defensive', 'conflict', 'control', 'right'],
            3: ['trust', 'suspicious', 'doubt', 'betrayal', 'disappointed', 'guard'],
            4: ['either', 'or', 'black', 'white', 'all', 'nothing', 'stuck', 'trapped'],
            5: ['busy', 'productive', 'achieve', 'work', 'accomplish', 'do', 'rest'],
            6: ['different', 'fake', 'real', 'authentic', 'mask', 'persona', 'pretend'],
            7: ['others', 'help', 'selfish', 'guilty', 'needs', 'sacrifice', 'care'],
            8: ['family', 'parents', 'expect', 'should', 'duty', 'obligation', 'loyal'],
            9: ['boundaries', 'weak', 'strong', 'context', 'situation', 'people', 'lose']
        }
        
        for pattern_id, keywords in pattern_keywords.items():
            keyword_matches = sum(1 for keyword in keywords if keyword in response_lower)
            if keyword_matches > 0:
                pattern_scores[pattern_id] += min(keyword_matches, 3)  # Cap at 3 points per text
    
    def _score_scale_response(self, question, response, pattern_scores):
        """Score scale responses"""
        try:
            if isinstance(response, (int, float)):
                scale_value = int(response)
                pattern_type = question.get('patterns', [''])[0]
                
                if pattern_type == 'readiness_level':
                    # High readiness is positive for all patterns
                    if scale_value >= 8:
                        # Add readiness bonus to all detected patterns
                        for pattern_id in pattern_scores:
                            if pattern_scores[pattern_id] > 0:
                                pattern_scores[pattern_id] += 0.5
                elif pattern_type == 'hypnotic_susceptibility':
                    # Higher susceptibility helps with intervention
                    weights = question.get('weights', [4, 3, 2, 1, 0])
                    if scale_value <= len(weights):
                        # This affects therapeutic approach, not pattern detection
                        pass
        except (ValueError, TypeError):
            pass
    
    def identify_dominant_patterns(self, pattern_scores):
        """Identify top 3 dominant patterns"""
        # Filter out patterns with zero scores
        active_patterns = {pid: score for pid, score in pattern_scores.items() if score > 0}
        
        # Sort by score, descending
        sorted_patterns = sorted(active_patterns.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_patterns[:3]  # Top 3 patterns
    
    def calculate_complexity_score(self, pattern_scores):
        """Calculate overall complexity of the pattern constellation"""
        active_patterns = sum(1 for score in pattern_scores.values() if score > 0)
        total_intensity = sum(pattern_scores.values())
        max_individual_score = max(pattern_scores.values()) if pattern_scores.values() else 0
        
        # Complexity factors:
        # 1. Number of active patterns (more = complex)
        # 2. Total intensity (higher = complex)
        # 3. Distribution (more evenly distributed = complex)
        
        complexity = 0
        complexity += active_patterns * 2  # 2 points per active pattern
        complexity += min(total_intensity / 2, 10)  # Cap intensity contribution
        
        # Distribution factor - more even distribution = higher complexity
        if active_patterns > 1 and max_individual_score > 0:
            distribution_factor = total_intensity / (max_individual_score * active_patterns)
            complexity += distribution_factor * 3
        
        return min(complexity, 10)  # Cap at 10
    
    def generate_clinical_insights(self, responses, pattern_scores):
        """Generate comprehensive clinical insights"""
        dominant_patterns = self.identify_dominant_patterns(pattern_scores)
        
        if not dominant_patterns:
            return {
                'primary_pattern': None,
                'clinical_summary': 'Assessment incomplete - additional data needed',
                'intervention_strategy': 'Complete comprehensive assessment',
                'session_plan': 'Standard 2-session protocol with full assessment'
            }
        
        primary_pattern_id, primary_score = dominant_patterns[0]
        primary_pattern = self.descriptions.get(primary_pattern_id, {})
        
        # Extract specific insights from responses
        trigger_analysis = self._analyze_trigger_sequence(responses)
        therapeutic_preferences = self._analyze_therapeutic_preferences(responses)
        readiness_assessment = self._assess_change_readiness(responses)
        
        return {
            'primary_pattern': {
                'id': primary_pattern_id,
                'name': primary_pattern.get('name', 'Unknown'),
                'score': primary_score,
                'description': primary_pattern.get('description', ''),
                'insights_map': primary_pattern.get('insights_map', ''),
                'what_you_notice': primary_pattern.get('what_you_notice', ''),
                'what_others_see': primary_pattern.get('what_others_see', ''),
                'hidden_cost': primary_pattern.get('hidden_cost', ''),
                'breakthrough_moment': primary_pattern.get('breakthrough_moment', '')
            },
            'secondary_patterns': [
                {
                    'id': pid,
                    'name': self.patterns.get(pid, 'Unknown'),
                    'score': score
                } for pid, score in dominant_patterns[1:]
            ],
            'trigger_analysis': trigger_analysis,
            'therapeutic_preferences': therapeutic_preferences,
            'readiness_assessment': readiness_assessment,
            'complexity_score': self.calculate_complexity_score(pattern_scores),
            'clinical_summary': self._generate_clinical_summary(primary_pattern, dominant_patterns),
            'intervention_strategy': self._determine_intervention_strategy(primary_pattern_id, pattern_scores),
            'session_plan': self._create_session_plan(primary_pattern_id, self.calculate_complexity_score(pattern_scores))
        }
    
    def _analyze_trigger_sequence(self, responses):
        """Analyze the complete trigger sequence from responses"""
        trigger_data = {}
        
        for q_id, response_data in responses.items():
            response = response_data.get('response', '')
            question = QuestionSets.get_core_questions().get(q_id, {})
            patterns = question.get('patterns', [])
            
            if 'somatic_response' in patterns:
                trigger_data['physical_trigger'] = response
            elif 'automatic_thoughts' in patterns:
                trigger_data['thought_pattern'] = response
            elif 'emotional_response' in patterns:
                trigger_data['emotional_pattern'] = response
            elif 'behavioral_response' in patterns:
                trigger_data['behavioral_pattern'] = response
        
        return trigger_data
    
    def _analyze_therapeutic_preferences(self, responses):
        """Analyze therapeutic approach preferences"""
        preferences = {}
        
        for q_id, response_data in responses.items():
            response = response_data.get('response', '')
            question = QuestionSets.get_core_questions().get(q_id, {})
            patterns = question.get('patterns', [])
            
            if 'therapeutic_preference' in patterns:
                preferences['guidance_style'] = response
            elif 'hypnotic_susceptibility' in patterns:
                preferences['trance_capacity'] = response
        
        return preferences
    
    def _assess_change_readiness(self, responses):
        """Assess readiness for change"""
        readiness_data = {}
        
        for q_id, response_data in responses.items():
            response = response_data.get('response', '')
            question = QuestionSets.get_core_questions().get(q_id, {})
            patterns = question.get('patterns', [])
            
            if 'readiness_level' in patterns:
                readiness_data['readiness_score'] = response
            elif 'urgency_level' in patterns:
                readiness_data['urgency'] = response
            elif 'change_fears' in patterns:
                readiness_data['resistance_factors'] = response
        
        return readiness_data
    
    def _generate_clinical_summary(self, primary_pattern, dominant_patterns):
        """Generate clinical summary"""
        if not primary_pattern:
            return "Assessment requires completion for clinical analysis"
        
        pattern_count = len(dominant_patterns)
        primary_name = primary_pattern.get('name', 'Unknown')
        
        if pattern_count == 1:
            return f"Clear {primary_name} pattern presentation requiring focused intervention"
        elif pattern_count == 2:
            secondary_name = self.patterns.get(dominant_patterns[1][0], 'Unknown')
            return f"Primary {primary_name} pattern with {secondary_name} components requiring integrated approach"
        else:
            return f"Complex multi-pattern presentation with {primary_name} dominance requiring comprehensive intervention"
    
    def _determine_intervention_strategy(self, primary_pattern_id, pattern_scores):
        """Determine optimal intervention strategy"""
        strategies = {
            1: "Happiness permission installation with safety anchoring",
            2: "Collaborative empowerment with maintained autonomy", 
            3: "Gradual trust building with transparent safety protocols",
            4: "Both/and integration with safety in uncertainty",
            5: "Inherent worth installation with productivity reframing",
            6: "Authentic self integration with safety across contexts",
            7: "Self-care as service reframing with boundary installation",
            8: "Honor family while claiming personal path integration",
            9: "Universal strength anchoring with context-independent resources"
        }
        
        return strategies.get(primary_pattern_id, "Personalized assessment-based approach")
    
    def _create_session_plan(self, primary_pattern_id, complexity_score):
        """Create detailed session plan"""
        pattern_name = self.patterns.get(primary_pattern_id, 'Unknown')
        
        if complexity_score >= 7:
            sessions = "3 sessions recommended"
            timeline = "3-4 weeks"
        elif complexity_score >= 5:
            sessions = "2-3 sessions"
            timeline = "2-3 weeks" 
        else:
            sessions = "2 sessions"
            timeline = "2 weeks"
        
        return {
            'total_sessions': sessions,
            'timeline': timeline,
            'session_1': f"Deep {pattern_name} pattern analysis, rapport building, and initial positive programming",
            'session_2': f"Core {pattern_name} transformation, neural pathway rewiring, and positive response installation",
            'session_3': "Integration reinforcement and pattern consolidation (if needed)",
            'success_probability': min(85 + (10 - complexity_score), 95)
        }
    
    def calculate_transformation_costs(self, responses, pattern_scores):
        """Calculate the costs of maintaining current patterns"""
        dominant_patterns = self.identify_dominant_patterns(pattern_scores)
        
        if not dominant_patterns:
            return {
                'weekly_cost': 'Assessment incomplete',
                'monthly_cost': 'Data insufficient',
                'annual_cost': 'Analysis pending'
            }
        
        # Base weekly time cost calculation
        primary_score = dominant_patterns[0][1]
        pattern_count = len(dominant_patterns)
        
        # Time costs (hours per week of mental energy/stress)
        weekly_time_cost = min(primary_score * 2 + pattern_count * 1.5, 20)
        
        # Opportunity costs (estimated lost productivity/happiness)
        weekly_opportunity_cost = weekly_time_cost * 50  # $50/hour equivalent
        monthly_cost = weekly_opportunity_cost * 4.3
        annual_cost = monthly_cost * 12
        
        return {
            'weekly_time': f"{weekly_time_cost:.1f} hours of mental energy",
            'weekly_opportunity': f"${weekly_opportunity_cost:.0f} in lost productivity/wellbeing",
            'monthly_cost': f"${monthly_cost:.0f}",
            'annual_cost': f"${annual_cost:.0f}",
            'five_year_projection': f"${annual_cost * 5:.0f}"
        }

# ================================
# 5. EMAIL INTEGRATION
# ================================

class EmailHandler:
    """Handle email notifications and report generation"""
    
    def __init__(self):
        # Get email credentials from Streamlit secrets
        self.smtp_server = st.secrets.get("email", {}).get("smtp_server", "smtp.gmail.com")
        self.smtp_port = st.secrets.get("email", {}).get("smtp_port", 587)
        self.sender_email = st.secrets.get("email", {}).get("sender_email", "")
        self.sender_password = st.secrets.get("email", {}).get("sender_password", "")
        self.recipient_email = st.secrets.get("email", {}).get("recipient_email", "")
    
    def send_assessment_results(self, contact_info, assessment_data, analytics_results):
        """Send comprehensive assessment results via email"""
        try:
            # Create message
            msg = MimeMultipart('alternative')
            msg['Subject'] = f"Behavioral Pattern Assessment - {contact_info['name']}"
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            
            # Generate email content
            html_content = self._generate_email_content(contact_info, assessment_data, analytics_results)
            
            # Attach HTML content
            html_part = MimeText(html_content, 'html')
            msg.attach(html_part)
            
            # Generate and attach JSON data
            json_data = self._generate_json_report(contact_info, assessment_data, analytics_results)
            json_attachment = MimeBase('application', 'json')
            json_attachment.set_payload(json_data.encode())
            encoders.encode_base64(json_attachment)
            json_attachment.add_header(
                'Content-Disposition',
                f'attachment; filename=assessment_{contact_info["name"].replace(" ", "_")}.json'
            )
            msg.attach(json_attachment)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            st.error(f"Email sending failed: {str(e)}")
            print(f"Email error details: {traceback.format_exc()}")
            return False
    
    def _generate_email_content(self, contact_info, assessment_data, analytics_results):
        """Generate comprehensive HTML email content"""
        clinical_insights = analytics_results.get('clinical_insights', {})
        primary_pattern = clinical_insights.get('primary_pattern', {})
        cost_analysis = analytics_results.get('cost_analysis', {})
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #273548; }}
                .header {{ background: #4CA1A3; color: white; padding: 20px; text-align: center; }}
                .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #4CA1A3; }}
                .pattern-box {{ background: #F3F6F8; padding: 15px; margin: 10px 0; border-radius: 8px; }}
                .cost-highlight {{ background: #fff3cd; padding: 10px; border-radius: 5px; }}
                .urgent {{ background: #f8d7da; padding: 10px; border-radius: 5px; color: #721c24; }}
                table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
                th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #CBD5E1; }}
                th {{ background: #F3F6F8; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Behavioral Pattern Assessment Results</h1>
                <p>Comprehensive Clinical Analysis</p>
            </div>
            
            <div class="section">
                <h2>Client Information</h2>
                <table>
                    <tr><td><strong>Name:</strong></td><td>{contact_info.get('name', 'N/A')}</td></tr>
                    <tr><td><strong>Email:</strong></td><td>{contact_info.get('email', 'N/A')}</td></tr>
                    <tr><td><strong>Phone:</strong></td><td>{contact_info.get('phone', 'Not provided')}</td></tr>
                    <tr><td><strong>Urgency:</strong></td><td>{contact_info.get('urgency', 'Not specified')}</td></tr>
                    <tr><td><strong>Preferred next step:</strong></td><td>{contact_info.get('next_step', 'Not specified')}</td></tr>
                    <tr><td><strong>Assessment completed:</strong></td><td>{datetime.now().strftime('%Y-%m-%d %H:%M')}</td></tr>
                </table>
            </div>
            
            <div class="section">
                <h2>Primary Concern</h2>
                <div class="pattern-box">
                    {contact_info.get('primary_concern', 'Not specified')}
                </div>
            </div>
            
            <div class="section">
                <h2>Clinical Analysis Summary</h2>
                <div class="pattern-box">
                    <h3>Primary Pattern: {primary_pattern.get('name', 'Analysis pending')}</h3>
                    <p><strong>Intensity Score:</strong> {primary_pattern.get('score', 0):.1f}/10</p>
                    <p><strong>Clinical Summary:</strong> {clinical_insights.get('clinical_summary', 'Assessment incomplete')}</p>
                    <p><strong>Intervention Strategy:</strong> {clinical_insights.get('intervention_strategy', 'To be determined')}</p>
                </div>
            </div>
            
            <div class="section">
                <h2>Pattern Cost Analysis</h2>
                <div class="cost-highlight">
                    <p><strong>Weekly Impact:</strong> {cost_analysis.get('weekly_time', 'Analysis pending')}</p>
                    <p><strong>Monthly Cost:</strong> {cost_analysis.get('monthly_cost', 'TBD')}</p>
                    <p><strong>Annual Projection:</strong> {cost_analysis.get('annual_cost', 'TBD')}</p>
                </div>
            </div>
            
            <div class="section">
                <h2>Recommended Session Plan</h2>
                <div class="pattern-box">
                    {self._format_session_plan(clinical_insights.get('session_plan', {}))}
                </div>
            </div>
            
            <div class="section">
                <h2>Next Steps Recommendation</h2>
                {self._generate_next_steps_recommendation(contact_info, clinical_insights)}
            </div>
            
            <div class="section">
                <h2>Complete Assessment Data</h2>
                <p>Detailed assessment responses and analytics are attached as JSON file for clinical review.</p>
                <p><strong>Total questions answered:</strong> {len(assessment_data.get('responses', {}))}</p>
                <p><strong>Assessment completion rate:</strong> {self._calculate_completion_rate(assessment_data)}%</p>
            </div>
        </body>
        </html>
        """
        
        return html_content
    
    def _format_session_plan(self, session_plan):
        """Format session plan for email"""
        if not session_plan:
            return "<p>Session plan to be determined after clinical review</p>"
        
        plan_html = f"""
        <p><strong>Recommended Structure:</strong> {session_plan.get('total_sessions', 'TBD')}</p>
        <p><strong>Timeline:</strong> {session_plan.get('timeline', 'TBD')}</p>
        <p><strong>Success Probability:</strong> {session_plan.get('success_probability', 85)}%</p>
        <br>
        <p><strong>Session 1:</strong> {session_plan.get('session_1', 'Pattern analysis and rapport building')}</p>
        <p><strong>Session 2:</strong> {session_plan.get('session_2', 'Core transformation work')}</p>
        """
        
        if 'session_3' in session_plan:
            plan_html += f"<p><strong>Session 3:</strong> {session_plan.get('session_3', 'Integration reinforcement')}</p>"
        
        return plan_html
    
    def _generate_next_steps_recommendation(self, contact_info, clinical_insights):
        """Generate next steps recommendation"""
        urgency = contact_info.get('urgency', '').lower()
        next_step = contact_info.get('next_step', '').lower()
        
        if 'extremely urgent' in urgency:
            priority_class = 'urgent'
            recommendation = "PRIORITY CLIENT - Contact within 24 hours. High urgency indicates significant daily life impact."
        elif 'very urgent' in urgency:
            priority_class = 'cost-highlight'
            recommendation = "Contact within 48 hours. Client reports significant concern requiring prompt attention."
        else:
            priority_class = 'pattern-box'
            recommendation = "Standard contact within 72 hours. Follow normal scheduling protocol."
        
        if 'schedule' in next_step:
            recommendation += " Client specifically requested scheduling consultation."
        elif 'book' in next_step:
            recommendation += " Client interested in booking transformation package directly."
        
        return f'<div class="{priority_class}"><p>{recommendation}</p></div>'
    
    def _calculate_completion_rate(self, assessment_data):
        """Calculate assessment completion rate"""
        total_questions = len(QuestionSets.get_core_questions())
        answered_questions = len(assessment_data.get('responses', {}))
        return round((answered_questions / total_questions) * 100, 1)
    
    def _generate_json_report(self, contact_info, assessment_data, analytics_results):
        """Generate comprehensive JSON report"""
        report_data = {
            'assessment_metadata': {
                'completion_timestamp': datetime.now().isoformat(),
                'total_questions': len(QuestionSets.get_core_questions()),
                'questions_answered': len(assessment_data.get('responses', {})),
                'completion_rate': self._calculate_completion_rate(assessment_data)
            },
            'client_information': contact_info,
            'assessment_responses': assessment_data.get('responses', {}),
            'pattern_scores': assessment_data.get('pattern_scores', {}),
            'clinical_analytics': analytics_results,
            'session_notes': {
                'created_by': 'Automated Assessment System',
                'requires_clinical_review': True,
                'priority_level': self._determine_priority_level(contact_info)
            }
        }
        
        return json.dumps(report_data, indent=2, default=str)
    
    def _determine_priority_level(self, contact_info):
        """Determine client priority level"""
        urgency = contact_info.get('urgency', '').lower()
        
        if 'extremely urgent' in urgency:
            return 'HIGH'
        elif 'very urgent' in urgency:
            return 'MEDIUM'
        else:
            return 'STANDARD'

# ================================
# 6. MAIN ASSESSMENT CLASS
# ================================

class BehavioralPatternAssessment:
    """Main assessment class orchestrating the entire process"""
    
    def __init__(self):
        self.questions = QuestionSets.get_core_questions()
        self.analytics = AssessmentAnalytics()
        self.email_handler = EmailHandler()
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """Initialize session state variables"""
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'assessment_completed': False,
            'contact_submitted': False,
            'contact_info': {},
            'pattern_scores': {},
            'analytics_results': {},
            'show_results': False
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
    
    def render(self):
        """Main render method"""
        apply_assessment_styles()
        self._render_header()
        
        if not st.session_state.assessment_completed:
            self._render_assessment()
        elif not st.session_state.contact_submitted:
            self._render_contact_form()
        else:
            self._render_results()
    
    def _render_header(self):
        """Render assessment header"""
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #273548; font-size: 2.2rem; margin-bottom: 0.5rem;">
                Behavioral pattern assessment
            </h1>
            <p style="color: #556D7A; font-size: 1rem; margin: 0;">
                Personalized analysis for rapid transformation planning
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_assessment(self):
        """Render the assessment questionnaire"""
        current_q_id = self._get_current_question_id()
        
        if current_q_id is None:
            # Assessment complete
            st.session_state.assessment_completed = True
            self._calculate_results()
            st.rerun()
            return
        
        question = self.questions.get(current_q_id)
        if not question:
            st.error("Question not found")
            return
        
        # Progress indicator
        self._render_progress()
        
        # Question content
        self._render_question(current_q_id, question)
        
        # Navigation
        self._render_navigation()
    
    def _get_current_question_id(self):
        """Get the next unanswered question ID"""
        answered = set(st.session_state.assessment_responses.keys())
        
        for q_id in sorted(self.questions.keys()):
            if q_id not in answered:
                return q_id
        
        return None  # All questions answered
    
    def _render_progress(self):
        """Render progress indicator"""
        total_questions = len(self.questions)
        completed = len(st.session_state.assessment_responses)
        progress = completed / total_questions if total_questions > 0 else 0
        
        st.markdown(f"""
        <div class="progress-container">
            <span style="color: #273548; font-weight: 600;">
                Question {completed + 1} of {total_questions}
            </span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span style="color: #556D7A; font-weight: 500;">
                {int(progress * 100)}%
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_question(self, q_id, question):
        """Render individual question"""
        # Question header
        st.markdown(f"""
        <div class="question-header">
            <p class="question-text">{question['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Question input based on type
        question_type = question.get('type', 'single_choice')
        
        if question_type == 'single_choice':
            self._render_single_choice(q_id, question)
        elif question_type == 'multi_select':
            self._render_multi_select(q_id, question)
        elif question_type == 'text_area':
            self._render_text_area(q_id, question)
        elif question_type == 'scale':
            self._render_scale(q_id, question)
    
    def _render_single_choice(self, q_id, question):
        """Render single choice question"""
        options = question.get('options', [])
        
        for i, option in enumerate(options):
            if st.button(
                option,
                key=f"q_{q_id}_opt_{i}",
                use_container_width=True
            ):
                self._save_response(q_id, option, question)
                self._advance_question()
                st.rerun()
    
    def _render_multi_select(self, q_id, question):
        """Render multi-select question"""
        options = question.get('options', [])
        max_selections = question.get('max_selections', len(options))
        
        selected = st.multiselect(
            "",
            options,
            key=f"q_{q_id}_multi",
            max_selections=max_selections,
            label_visibility="collapsed"
        )
        
        if st.button(
            "Continue",
            key=f"q_{q_id}_continue",
            type="primary",
            use_container_width=True,
            disabled=len(selected) == 0
        ):
            self._save_response(q_id, selected, question)
            self._advance_question()
            st.rerun()
    
    def _render_text_area(self, q_id, question):
        """Render text area question"""
        placeholder = question.get('placeholder', 'Your response...')
        min_chars = question.get('min_chars', 3)
        
        response = st.text_area(
            "",
            placeholder=placeholder,
            key=f"q_{q_id}_text",
            height=100,
            label_visibility="collapsed"
        )
        
        if st.button(
            "Continue",
            key=f"q_{q_id}_continue",
            type="primary",
            use_container_width=True,
            disabled=len(response.strip()) < min_chars
        ):
            self._save_response(q_id, response.strip(), question)
            self._advance_question()
            st.rerun()
        
        if len(response.strip()) < min_chars and len(response.strip()) > 0:
            st.info(f"Please provide at least {min_chars} characters")
    
    def _render_scale(self, q_id, question):
        """Render scale question"""
        min_val = question.get('min_value', 1)
        max_val = question.get('max_value', 10)
        labels = question.get('labels', ['Min', 'Max'])
        
        # Custom scale with labels
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            st.markdown(f"<small>{labels[0]}</small>", unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"<small>{labels[1]}</small>", unsafe_allow_html=True)
        
        value = st.slider(
            "",
            min_value=min_val,
            max_value=max_val,
            value=(min_val + max_val) // 2,
            key=f"q_{q_id}_scale",
            label_visibility="collapsed"
        )
        
        if st.button(
            "Continue",
            key=f"q_{q_id}_continue",
            type="primary",
            use_container_width=True
        ):
            self._save_response(q_id, value, question)
            self._advance_question()
            st.rerun()
    
    def _save_response(self, q_id, response, question):
        """Save question response"""
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat(),
            'patterns': question.get('patterns', []),
            'category': question.get('category', 'general')
        }
    
    def _advance_question(self):
        """Advance to next question"""
        st.session_state.current_question += 1
    
    def _render_navigation(self):
        """Render navigation controls"""
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Back button (if not first question)
            if len(st.session_state.assessment_responses) > 0:
                if st.button("← Previous", key="nav_back", use_container_width=True):
                    self._go_back()
                    st.rerun()
        
        with col2:
            # Skip button for optional questions
            answered_count = len(st.session_state.assessment_responses)
            st.markdown(f"""
            <div style="text-align: center; padding: 0.5rem; color: #556D7A;">
                <small>{answered_count} answered</small>
            </div>
            """, unsafe_allow_html=True)
    
    def _go_back(self):
        """Go back to previous question"""
        if st.session_state.assessment_responses:
            # Remove last response
            last_q_id = max(st.session_state.assessment_responses.keys())
            del st.session_state.assessment_responses[last_q_id]
            st.session_state.current_question = max(1, st.session_state.current_question - 1)
    
    def _calculate_results(self):
        """Calculate assessment results using analytics engine"""
        try:
            # Calculate pattern scores
            pattern_scores = self.analytics.calculate_pattern_scores(
                st.session_state.assessment_responses
            )
            st.session_state.pattern_scores = pattern_scores
            
            # Generate clinical insights
            clinical_insights = self.analytics.generate_clinical_insights(
                st.session_state.assessment_responses,
                pattern_scores
            )
            
            # Calculate transformation costs
            cost_analysis = self.analytics.calculate_transformation_costs(
                st.session_state.assessment_responses,
                pattern_scores
            )
            
            # Store complete analytics
            st.session_state.analytics_results = {
                'clinical_insights': clinical_insights,
                'cost_analysis': cost_analysis,
                'pattern_scores': pattern_scores,
                'completion_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            st.error(f"Error calculating results: {str(e)}")
            print(f"Analytics error: {traceback.format_exc()}")
    
    def _render_contact_form(self):
        """Render contact information form"""
        st.markdown("### Assessment complete! 🎉")
        st.markdown("Get your personalized behavioral pattern analysis by providing your contact information.")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full name*", placeholder="Your full name")
                email = st.text_input("Email address*", placeholder="your@email.com")
            
            with col2:
                phone = st.text_input("Phone number", placeholder="+66 xxx xxx xxx")
                urgency = st.selectbox(
                    "How urgent is your concern?*",
                    ["Select urgency level...", "Extremely urgent - affecting daily life", 
                     "Very urgent - need change soon", "Moderately urgent - within 6 months", 
                     "Not urgent - exploring options"]
                )
            
            primary_concern = st.text_area(
                "What brought you to this assessment?*",
                placeholder="Describe your main concern or what you hope to change...",
                height=100
            )
            
            next_step = st.selectbox(
                "What would you like as next step?*",
                ["Select preference...", "Schedule discovery call first", 
                 "Book transformation sessions directly", "Send me detailed analysis first"]
            )
            
            submitted = st.form_submit_button(
                "Get my transformation analysis →",
                type="primary",
                use_container_width=True
            )
            
            if submitted:
                if self._validate_contact_form(name, email, primary_concern, urgency, next_step):
                    # Save contact info
                    contact_info = {
                        'name': name,
                        'email': email,
                        'phone': phone,
                        'urgency': urgency,
                        'primary_concern': primary_concern,
                        'next_step': next_step,
                        'timestamp': datetime.now().isoformat()
                    }
                    st.session_state.contact_info = contact_info
                    
                    # Send email notification
                    self._send_assessment_email(contact_info)
                    
                    # Mark as submitted
                    st.session_state.contact_submitted = True
                    st.rerun()
    
    def _validate_contact_form(self, name, email, concern, urgency, next_step):
        """Validate contact form inputs"""
        errors = []
        
        if not name.strip():
            errors.append("Name is required")
        
        if not email.strip():
            errors.append("Email is required")
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
            errors.append("Please enter a valid email address")
        
        if not concern.strip():
            errors.append("Please describe your main concern")
        
        if urgency == "Select urgency level...":
            errors.append("Please select urgency level")
        
        if next_step == "Select preference...":
            errors.append("Please select your preferred next step")
        
        for error in errors:
            st.error(f"❌ {error}")
        
        return len(errors) == 0
    
    def _send_assessment_email(self, contact_info):
        """Send assessment results via email"""
        with st.spinner("Sending your analysis..."):
            try:
                # Prepare assessment data
                assessment_data = {
                    'responses': st.session_state.assessment_responses,
                    'pattern_scores': st.session_state.pattern_scores,
                    'completion_timestamp': datetime.now().isoformat()
                }
                
                # Send email
                success = self.email_handler.send_assessment_results(
                    contact_info,
                    assessment_data,
                    st.session_state.analytics_results
                )
                
                if success:
                    st.success("✅ Analysis sent successfully!")
                else:
                    st.warning("⚠️ Assessment completed but email notification failed. We'll contact you directly.")
                
            except Exception as e:
                st.error(f"Error sending analysis: {str(e)}")
                print(f"Email sending error: {traceback.format_exc()}")
    
    def _render_results(self):
        """Render comprehensive results page"""
        self._render_results_header()
        self._render_pattern_analysis()
        self._render_insights_section()
        self._render_transformation_preview()
        self._render_next_steps()
    
    def _render_results_header(self):
        """Render results header with key metrics"""
        analytics = st.session_state.analytics_results
        clinical_insights = analytics.get('clinical_insights', {})
        primary_pattern = clinical_insights.get('primary_pattern', {})
        
        st.markdown(f"""
        <div class="results-hero">
            <h2>Your behavioral pattern analysis</h2>
            <h3>Primary pattern: {primary_pattern.get('name', 'Analysis complete')}</h3>
            <p>Personalized transformation roadmap generated</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Key metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            pattern_count = len([score for score in st.session_state.pattern_scores.values() if score > 0])
            st.metric("Patterns identified", pattern_count)
        
        with col2:
            complexity = clinical_insights.get('complexity_score', 0)
            st.metric("Complexity level", f"{complexity:.1f}/10")
        
        with col3:
            session_plan = clinical_insights.get('session_plan', {})
            success_rate = session_plan.get('success_probability', 85)
            st.metric("Success probability", f"{success_rate}%")
    
    def _render_pattern_analysis(self):
        """Render detailed pattern analysis"""
        analytics = st.session_state.analytics_results
        clinical_insights = analytics.get('clinical_insights', {})
        primary_pattern = clinical_insights.get('primary_pattern', {})
        secondary_patterns = clinical_insights.get('secondary_patterns', [])
        
        st.markdown("## Your unique pattern constellation")
        
        if primary_pattern:
            # Primary pattern card
            st.markdown(f"""
            <div class="pattern-card">
                <h3 style="color: #4CA1A3; margin-top: 0;">
                    🎯 Primary pattern: {primary_pattern.get('name', 'Unknown')}
                </h3>
                <p><strong>Intensity:</strong> {primary_pattern.get('score', 0):.1f}/10</p>
                <p><strong>What this means:</strong> {primary_pattern.get('description', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Pattern insights
            with st.expander("🔍 Deep pattern insights", expanded=True):
                insights_map = primary_pattern.get('insights_map', '')
                if insights_map:
                    st.markdown(f"""
                    <div class="insight-box">
                        <h4>The hidden mechanism:</h4>
                        <p>{insights_map}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    what_you_notice = primary_pattern.get('what_you_notice', '')
                    if what_you_notice:
                        st.markdown(f"""
                        **What you experience internally:**
                        {what_you_notice}
                        """)
                
                with col2:
                    what_others_see = primary_pattern.get('what_others_see', '')
                    if what_others_see:
                        st.markdown(f"""
                        **What others observe:**
                        {what_others_see}
                        """)
                
                hidden_cost = primary_pattern.get('hidden_cost', '')
                if hidden_cost:
                    st.markdown(f"""
                    <div style="background: #fff3cd; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                        <strong>Hidden cost:</strong> {hidden_cost}
                    </div>
                    """, unsafe_allow_html=True)
                
                breakthrough_moment = primary_pattern.get('breakthrough_moment', '')
                if breakthrough_moment:
                    st.markdown(f"""
                    <div style="background: #d1ecf1; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                        <strong>Your breakthrough insight:</strong> {breakthrough_moment}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Secondary patterns
        if secondary_patterns:
            st.markdown("### Supporting patterns")
            for pattern in secondary_patterns:
                st.markdown(f"""
                <div style="background: #F3F6F8; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                    <strong>{pattern.get('name', 'Unknown')}</strong> 
                    (Intensity: {pattern.get('score', 0):.1f}/10)
                </div>
                """, unsafe_allow_html=True)
    
    def _render_insights_section(self):
        """Render clinical insights and costs"""
        analytics = st.session_state.analytics_results
        cost_analysis = analytics.get('cost_analysis', {})
        
        st.markdown("## The real cost of these patterns")
        
        if cost_analysis:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Current weekly impact")
                weekly_time = cost_analysis.get('weekly_time', 'Calculating...')
                weekly_cost = cost_analysis.get('weekly_opportunity', 'Calculating...')
                
                st.markdown(f"""
                - **Mental energy drain:** {weekly_time}
                - **Opportunity cost:** {weekly_cost}
                """)
            
            with col2:
                st.markdown("### Long-term projection")
                annual_cost = cost_analysis.get('annual_cost', 'Calculating...')
                five_year_cost = cost_analysis.get('five_year_projection', 'Calculating...')
                
                st.markdown(f"""
                - **Annual impact:** {annual_cost}
                - **5-year projection:** {five_year_cost}
                """)
        
        # Trigger sequence analysis
        clinical_insights = analytics.get('clinical_insights', {})
        trigger_analysis = clinical_insights.get('trigger_analysis', {})
        
        if trigger_analysis:
            with st.expander("🔄 Your pattern trigger sequence"):
                physical_trigger = trigger_analysis.get('physical_trigger', '')
                thought_pattern = trigger_analysis.get('thought_pattern', '')
                emotional_pattern = trigger_analysis.get('emotional_pattern', '')
                
                if physical_trigger:
                    st.markdown(f"**Physical trigger:** {physical_trigger}")
                if thought_pattern:
                    st.markdown(f"**Automatic thoughts:** {thought_pattern}")
                if emotional_pattern:
                    st.markdown(f"**Emotional response:** {emotional_pattern}")
    
    def _render_transformation_preview(self):
        """Render transformation preview and session plan"""
        analytics = st.session_state.analytics_results
        clinical_insights = analytics.get('clinical_insights', {})
        session_plan = clinical_insights.get('session_plan', {})
        
        st.markdown("## Your transformation roadmap")
        
        if session_plan:
            st.markdown(f"""
            <div class="pattern-card">
                <h3 style="color: #22c55e; margin-top: 0;">Recommended approach</h3>
                <p><strong>Sessions needed:</strong> {session_plan.get('total_sessions', 'TBD')}</p>
                <p><strong>Timeline:</strong> {session_plan.get('timeline', 'TBD')}</p>
                <p><strong>Success probability:</strong> {session_plan.get('success_probability', 85)}%</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("📋 Detailed session breakdown"):
                session_1 = session_plan.get('session_1', '')
                session_2 = session_plan.get('session_2', '')
                session_3 = session_plan.get('session_3', '')
                
                if session_1:
                    st.markdown(f"**Session 1:** {session_1}")
                if session_2:
                    st.markdown(f"**Session 2:** {session_2}")
                if session_3:
                    st.markdown(f"**Session 3:** {session_3}")
        
        # Intervention strategy
        intervention_strategy = clinical_insights.get('intervention_strategy', '')
        if intervention_strategy:
            st.markdown(f"""
            <div class="insight-box">
                <h4>Your personalized intervention strategy:</h4>
                <p>{intervention_strategy}</p>
            </div>
            """, unsafe_allow_html=True)
    
    def _render_next_steps(self):
        """Render next steps and contact information"""
        contact_info = st.session_state.contact_info
        urgency = contact_info.get('urgency', '').lower()
        
        st.markdown("## What happens next")
        
        # Timeline based on urgency
        if 'extremely urgent' in urgency:
            timeline = "within 24 hours"
            priority_note = "🚨 Priority case - expedited review"
        elif 'very urgent' in urgency:
            timeline = "within 48 hours"
            priority_note = "⚡ Fast-track review"
        else:
            timeline = "within 72 hours"
            priority_note = "📋 Standard review process"
        
        st.markdown(f"""
        <div class="insight-box">
            <p>{priority_note}</p>
            <p><strong>Expected contact:</strong> {timeline}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### Your transformation journey starts here:
        
        1. **Clinical review** (24-48 hours): Licensed therapist analyzes your complete assessment
        2. **Personal consultation** (within 72 hours): We discuss your specific needs and answer questions
        3. **Transformation sessions**: Begin your personalized rapid-change program
        
        ### Why this approach works:
        
        - **85% success rate** with our specialized method vs. 30% with traditional approaches
        - **2-3 sessions** instead of months or years of weekly therapy
        - **Direct subconscious intervention** rather than just talking about problems
        - **Personalized protocols** based on your unique pattern constellation
        """)
        
        # Contact buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗓️ Schedule consultation now", type="primary", use_container_width=True):
                st.markdown("**Contact us directly:**")
                st.markdown("📞 +66 (0) 123-456-789")
                st.markdown("📧 info@rapidtransformation.com")
        
        with col2:
            if st.button("💬 Have questions first?", use_container_width=True):
                st.markdown("**We're here to help:**")
                st.markdown("Feel free to reply to the email we sent you, or call us directly for immediate assistance.")
        
        # Value proposition reminder
        st.markdown("""
        ---
        ### Investment comparison:
        
        **Traditional therapy approach:** 18+ months, ฿60,000+, uncertain outcomes
        
        **Our specialized method:** 2-3 sessions, ฿3,000-4,000, 85% success rate
        
        **Time to results:** 48-72 hours vs. 3-6 months
        """)

# ================================
# 7. MAIN PAGE FUNCTION
# ================================

def create_assess_page():
    """Main function to create and render the assessment page"""
    assessment = BehavioralPatternAssessment()
    assessment.render()

# Export the main function for use in other modules
if __name__ == "__main__":
    create_assess_page()
