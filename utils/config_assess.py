"""
Assessment Configuration Module
Contains all question sets, scoring rules, pattern definitions, and analytics
Centralized data structure for clinical behavioral pattern assessment
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
import re


# ========================================================================================
# PATTERN DEFINITIONS
# ========================================================================================

class PatternDefinitions:
    """Core behavioral pattern definitions and clinical information"""
    
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
            "core_belief": "Happiness leads to disappointment or makes me a target",
            "protective_function": "Protection from disappointment, envy, or loss",
            "intervention_focus": "Permission installation for positive states with safety anchoring"
        },
        2: {
            "name": "Power struggles",
            "core_belief": "I must fight to exist and maintain my identity",
            "protective_function": "Protection from domination or loss of self",
            "intervention_focus": "Collaborative empowerment with maintained autonomy"
        },
        3: {
            "name": "Systematic mistrust",
            "core_belief": "Trust leads to being hurt, used, or abandoned",
            "protective_function": "Protection from betrayal and emotional injury",
            "intervention_focus": "Gradual trust building with transparent safety protocols"
        },
        4: {
            "name": "Separation and division",
            "core_belief": "Things must be clearly defined or everything falls apart",
            "protective_function": "Protection from chaos and uncertainty",
            "intervention_focus": "Both/and integration with safety in uncertainty"
        },
        5: {
            "name": "Doing versus being",
            "core_belief": "I am only valuable when producing or achieving",
            "protective_function": "Protection from worthlessness and rejection",
            "intervention_focus": "Inherent worth installation with productivity reframing"
        },
        6: {
            "name": "Compartmentalized authenticity",
            "core_belief": "I must be different selves to be accepted",
            "protective_function": "Protection from rejection and abandonment",
            "intervention_focus": "Authentic self integration with safety across contexts"
        },
        7: {
            "name": "Self sacrifice and care avoidance",
            "core_belief": "I am only good/loveable when serving others",
            "protective_function": "Protection from selfishness guilt and rejection",
            "intervention_focus": "Self-care as service reframing with boundary installation"
        },
        8: {
            "name": "Inherited missions",
            "core_belief": "I must fulfill family dreams/expectations to be loyal",
            "protective_function": "Protection from guilt, betrayal, and family disconnection",
            "intervention_focus": "Honor family while claiming personal path integration"
        },
        9: {
            "name": "Context dependent weakness",
            "core_belief": "I lose myself in specific situations/with certain people",
            "protective_function": "Protection from confrontation and responsibility",
            "intervention_focus": "Universal strength anchoring with context-independent resources"
        }
    }


# ========================================================================================
# QUESTION SETS
# ========================================================================================

class QuestionSets:
    """All assessment questions organized by phase"""
    
    # --------------------------------------------------------------------------------
    # Phase 0: Age screening (determines digital native status)
    # --------------------------------------------------------------------------------
    AGE_SCREENING = {
        0: {
            "text": "What is your age range?",
            "type": "single_choice",
            "options": [
                "Under 18",
                "18-22",
                "23-27",
                "28-32",
                "33-37",
                "38-42",
                "43-50",
                "Over 50"
            ],
            "digital_native_scoring": [3, 5, 4, 3, 2, 1, 0, 0],
            "phase": "age_screening",
            "determines_flow": True
        }
    }
    
    # --------------------------------------------------------------------------------
    # Phase 1: Digital despair screening (for digital natives only)
    # --------------------------------------------------------------------------------
    DIGITAL_SCREENING = {
        1: {
            "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
            "type": "single_choice",
            "options": [
                "Less than 2 hours",
                "2-4 hours",
                "4-6 hours",
                "6-8 hours",
                "8-10 hours",
                "Over 10 hours"
            ],
            "digital_despair_weights": [0, 1, 2, 3, 4, 5],
            "phase": "digital_screening"
        },
        2: {
            "text": "Where do you feel most like your authentic self?",
            "type": "single_choice",
            "options": [
                "In offline, face-to-face interactions",
                "In online communities and digital spaces",
                "Both online and offline equally",
                "Neither - I don't feel authentic anywhere",
                "It varies completely depending on the situation"
            ],
            "pattern_triggers": {
                1: [6],  # Options that trigger pattern 6
                3: [3, 6]
            },
            "digital_despair_weights": [0, 3, 1, 4, 2],
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
            "pattern_triggers": {
                1: [4],
                4: [2, 4]
            },
            "digital_despair_weights": [0, 4, 3, 0, 4],
            "phase": "digital_screening"
        },
        4: {
            "text": "When expressing genuine emotions or enthusiasm:",
            "type": "single_choice",
            "options": [
                "I express them naturally and directly",
                "I tend to use humor or irony to deflect",
                "I feel embarrassed or 'cringe' about sincerity",
                "I mainly express emotions through memes or online references",
                "I rarely express genuine emotions at all"
            ],
            "pattern_triggers": {
                1: [2, 3, 4],
                6: [1, 2, 3]
            },
            "digital_despair_weights": [0, 2, 3, 3, 4],
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
            "digital_despair_weights": [0, 3, 1, 0, 3],
            "phase": "digital_screening"
        },
        6: {
            "text": "When someone suggests things could get better or offers optimistic perspectives:",
            "type": "single_choice",
            "options": [
                "I feel encouraged and want to believe them",
                "I appreciate it but remain cautiously skeptical",
                "I immediately think of reasons why they're wrong",
                "I feel annoyed because they don't understand reality",
                "I dismiss it as naive or manipulative"
            ],
            "pattern_triggers": {
                3: [2, 3, 4]
            },
            "digital_despair_weights": [0, 1, 2, 3, 4],
            "phase": "digital_screening"
        },
        7: {
            "text": "Your attention span for non-digital activities (reading books, conversations, offline tasks):",
            "type": "single_choice",
            "options": [
                "Same as always - can focus for hours when interested",
                "Slightly shorter but manageable",
                "Noticeably fragmented - need frequent stimulation",
                "Very difficult - mind wanders constantly",
                "Almost impossible without background digital stimulation"
            ],
            "digital_despair_weights": [0, 1, 2, 3, 4],
            "phase": "digital_screening"
        }
    }
    
    # --------------------------------------------------------------------------------
    # Phase 2: Core engagement questions (everyone)
    # --------------------------------------------------------------------------------
    ENGAGEMENT = {
        8: {
            "text": "What specific behavior or pattern would you most like to transform?",
            "type": "text_completion",
            "placeholder": "Describe the exact behavior, feeling, or situation you want to change...",
            "min_chars": 10,
            "patterns": "presenting_problem",
            "phase": "engagement"
        },
        9: {
            "text": "How long has this pattern been affecting your life?",
            "type": "single_choice",
            "options": [
                "Less than 6 months",
                "6 months to 2 years",
                "2-5 years",
                "5-10 years",
                "Over 10 years or as long as I can remember"
            ],
            "chronicity_weights": [1, 2, 3, 4, 5],
            "phase": "engagement"
        },
        10: {
            "text": "If this issue completely resolved, what would be different about your daily life?",
            "type": "text_completion",
            "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible...",
            "min_chars": 10,
            "keywords": {
                "productivity": [5],
                "relationships": [2, 3, 6, 7],
                "peace": [1],
                "authentic": [6],
                "happy": [1],
                "control": [2, 4],
                "boundaries": [7, 9]
            },
            "phase": "engagement"
        },
        11: {
            "text": "On a scale of 1-10, how much does this interfere with your daily life?",
            "type": "slider",
            "min": 1,
            "max": 10,
            "default": 5,
            "patterns": "interference_level",
            "phase": "engagement"
        }
    }
    
    # --------------------------------------------------------------------------------
    # Phase 3: Behavioral chain mapping (everyone)
    # --------------------------------------------------------------------------------
    TRIGGER_MAPPING = {
        12: {
            "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
            "type": "text_completion",
            "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening?",
            "min_chars": 10,
            "chain_mapping": "trigger",
            "phase": "trigger_mapping"
        },
        13: {
            "text": "When this pattern activates, the first physical sensation is usually:",
            "type": "single_choice",
            "options": [
                "Chest tightness, racing heart, or breathing changes",
                "Stomach drop, nausea, or digestive upset",
                "Muscle tension, jaw clenching, or physical rigidity",
                "Hot/cold flashes, sweating, or temperature changes",
                "Numbness, disconnection, or feeling 'outside yourself'",
                "Restlessness, fidgeting, or urge to move/escape",
                "Fatigue, heaviness, or sudden energy drain"
            ],
            "pattern_triggers": {
                0: [1, 3, 4],
                1: [1, 3, 4],
                2: [2, 5],
                3: [2, 5],
                4: [6, 9],
                5: [2, 5],
                6: [1, 7]
            },
            "chain_mapping": "physical_response",
            "phase": "trigger_mapping"
        },
        14: {
            "text": "What automatic thoughts appear when you feel that physical sensation?",
            "type": "text_completion",
            "placeholder": "The actual words that go through your mind - even if they seem harsh or unreasonable...",
            "min_chars": 5,
            "pattern_keywords": {
                "not good enough": [1, 5],
                "fight": [2],
                "can't trust": [3],
                "either or": [4],
                "must do": [5],
                "can't be real": [6],
                "others need": [7],
                "should": [8],
                "can't handle": [9]
            },
            "chain_mapping": "automatic_thought",
            "phase": "trigger_mapping"
        },
        15: {
            "text": "After that thought, you typically feel:",
            "type": "multi_select",
            "max_selections": 3,
            "options": [
                "Anxious or worried",
                "Angry or frustrated",
                "Ashamed or embarrassed",
                "Sad or defeated",
                "Guilty or self-blaming",
                "Overwhelmed or panicked",
                "Numb or disconnected",
                "Confused or uncertain"
            ],
            "chain_mapping": "emotional_response",
            "phase": "trigger_mapping"
        },
        16: {
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
                0: [1, 4, 9],
                1: [5],
                2: [3, 7],
                3: [2],
                4: [2, 5],
                5: [7],
                6: [6, 9],
                7: [4, 5]
            },
            "chain_mapping": "behavioral_response",
            "phase": "trigger_mapping"
        }
    }
    
    # --------------------------------------------------------------------------------
    # Phase 4: Pattern-specific deep dive questions
    # --------------------------------------------------------------------------------
    PATTERN_SPECIFIC = {
        # Pattern 1: Unhappiness culture
        "pattern_1": {
            17: {
                "text": "When something genuinely good happens to you, your first reaction is usually:",
                "type": "single_choice",
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
            18: {
                "text": "Growing up, what messages did you receive about happiness in your family?",
                "type": "text_completion",
                "placeholder": "What was said explicitly or shown through behavior...",
                "min_chars": 10,
                "pattern": 1
            }
        },
        
        # Pattern 2: Power struggles
        "pattern_2": {
            19: {
                "text": "When someone disagrees with you, your nervous system:",
                "type": "single_choice",
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
            20: {
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
        
        # Pattern 3: Systematic mistrust
        "pattern_3": {
            21: {
                "text": "When meeting new people, you assume they:",
                "type": "single_choice",
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
            22: {
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
        
        # Pattern 4: Separation and division
        "pattern_4": {
            23: {
                "text": "When facing important decisions, you typically:",
                "type": "single_choice",
                "options": [
                    "See multiple creative possibilities",
                    "Feel trapped between two impossible choices",
                    "Get paralyzed by perfectionist analysis",
                    "Create artificial deadlines or urgency",
                    "Defer to what others expect"
                ],
                "weights": [0, 3, 3, 2, 1],
                "pattern": 4
            },
            24: {
                "text": "Complete this: 'In life, I have to choose between security _____ freedom'",
                "type": "single_choice",
                "options": [
                    "AND (I can have both)",
                    "OR (I must choose one)",
                    "This doesn't resonate with me",
                    "Both seem impossible to achieve"
                ],
                "weights": [0, 3, 0, 2],
                "pattern": 4
            }
        },
        
        # Pattern 5: Doing versus being
        "pattern_5": {
            25: {
                "text": "You feel most valuable when you're:",
                "type": "single_choice",
                "options": [
                    "Simply existing as yourself",
                    "Accomplishing something important",
                    "Being productive or busy",
                    "Helping others achieve their goals",
                    "Receiving recognition for your work"
                ],
                "weights": [0, 2, 3, 2, 2],
                "pattern": 5
            },
            26: {
                "text": "When efforts go unnoticed or unappreciated:",
                "type": "single_choice",
                "options": [
                    "My worth isn't dependent on external recognition",
                    "I feel invisible and unimportant",
                    "I work even harder to get attention",
                    "I question whether what I did mattered"
                ],
                "weights": [0, 2, 2, 2],
                "pattern": 5
            }
        },
        
        # Pattern 6: Compartmentalized authenticity
        "pattern_6": {
            27: {
                "text": "Your personality tends to:",
                "type": "single_choice",
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
            28: {
                "text": "Different life areas where you feel capable versus powerless:",
                "type": "single_choice",
                "options": [
                    "I feel consistently myself everywhere",
                    "I'm like two completely different people",
                    "Strong professionally but weak personally",
                    "Confident socially but insecure privately"
                ],
                "weights": [0, 3, 2, 2],
                "pattern": 6
            }
        },
        
        # Pattern 7: Self sacrifice and care avoidance
        "pattern_7": {
            29: {
                "text": "When it comes to your own needs versus others' needs:",
                "type": "single_choice",
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
            30: {
                "text": "You consistently have energy and motivation for:",
                "type": "single_choice",
                "options": [
                    "Both personal and external responsibilities",
                    "Other people's goals but not my own",
                    "Work projects but not personal care",
                    "Helping others but not helping myself"
                ],
                "weights": [0, 2, 2, 3],
                "pattern": 7
            }
        },
        
        # Pattern 8: Inherited missions
        "pattern_8": {
            31: {
                "text": "Your major life goals are primarily:",
                "type": "single_choice",
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
            32: {
                "text": "When thinking about what YOU actually want:",
                "type": "single_choice",
                "options": [
                    "I can access it clearly and confidently",
                    "I honestly don't know anymore",
                    "I feel guilty for wanting something different",
                    "I'd be betraying someone important"
                ],
                "weights": [0, 2, 2, 3],
                "pattern": 8
            }
        },
        
        # Pattern 9: Context dependent weakness
        "pattern_9": {
            33: {
                "text": "Your boundaries and limits:",
                "type": "single_choice",
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
            34: {
                "text": "With certain people or situations, you tend to:",
                "type": "single_choice",
                "options": [
                    "Stay true to my values and boundaries",
                    "Become someone I don't respect",
                    "Lose all my usual boundaries",
                    "Can't say no even when I want to",
                    "Completely lose sense of self"
                ],
                "weights": [0, 2, 3, 3, 4],
                "pattern": 9
            }
        }
    }
    
    # --------------------------------------------------------------------------------
    # Phase 5: Integration and readiness
    # --------------------------------------------------------------------------------
    INTEGRATION = {
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
            "placeholder": "Think about what guarantees, support, or conditions you'd need...",
            "min_chars": 10,
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
            "text": "How urgently do you need to resolve your main concern?",
            "type": "single_choice",
            "options": [
                "Extremely urgent - affecting daily life significantly",
                "Very urgent - need change within few months",
                "Moderately urgent - within 6 months",
                "Somewhat urgent - exploring gradual options",
                "Not urgent - just curious"
            ],
            "urgency_weights": [5, 4, 3, 2, 1],
            "phase": "integration"
        }
    }


# ========================================================================================
# SCORING ENGINE
# ========================================================================================

class ScoringEngine:
    """Calculates pattern scores and intensity from responses"""
    
    def __init__(self):
        self.patterns = PatternDefinitions.PATTERNS
        
    def calculate_pattern_scores(self, responses: Dict) -> Dict[int, float]:
        """
        Calculate intensity scores for all 9 patterns
        Returns: {pattern_id: score} dictionary
        """
        pattern_scores = {i: 0.0 for i in range(1, 10)}
        
        # Process each response
        for q_id, response_data in responses.items():
            response = response_data.get('response', '')
            question = self._get_question_by_id(q_id)
            
            if not question:
                continue
            
            # Single choice questions with pattern mapping
            if question.get('type') == 'single_choice':
                self._score_single_choice(question, response, pattern_scores)
            
            # Text completion with keyword analysis
            elif question.get('type') == 'text_completion':
                self._score_text_completion(question, response, pattern_scores)
            
            # Multi-select questions
            elif question.get('type') == 'multi_select':
                self._score_multi_select(question, response, pattern_scores)
        
        # Normalize scores to 0-10 scale
        return self._normalize_scores(pattern_scores)
    
    def _score_single_choice(self, question: Dict, response: str, pattern_scores: Dict):
        """Score single choice questions"""
        options = question.get('options', [])
        
        # Find option index
        try:
            option_index = options.index(response)
        except ValueError:
            return
        
        # Pattern mapping scoring
        pattern_mapping = question.get('pattern_mapping', {})
        if option_index in pattern_mapping:
            for pattern_id in pattern_mapping[option_index]:
                pattern_scores[pattern_id] += 2
        
        # Pattern triggers scoring
        pattern_triggers = question.get('pattern_triggers', {})
        if option_index in pattern_triggers:
            for pattern_id in pattern_triggers[option_index]:
                pattern_scores[pattern_id] += 2
        
        # Direct pattern with weights
        if 'pattern' in question and 'weights' in question:
            pattern_id = question['pattern']
            weights = question['weights']
            if option_index < len(weights):
                pattern_scores[pattern_id] += weights[option_index]
    
    def _score_text_completion(self, question: Dict, response: str, pattern_scores: Dict):
        """Score text completion questions with keyword analysis"""
        if not response or len(response) < 3:
            return
        
        response_lower = response.lower()
        
        # Keyword matching
        keywords = question.get('keywords', {})
        for keyword, pattern_ids in keywords.items():
            if keyword in response_lower:
                for pattern_id in pattern_ids:
                    pattern_scores[pattern_id] += 1
        
        # Pattern keywords
        pattern_keywords = question.get('pattern_keywords', {})
        for keyword, pattern_ids in pattern_keywords.items():
            if keyword in response_lower:
                for pattern_id in pattern_ids:
                    pattern_scores[pattern_id] += 2
        
        # Direct pattern assignment
        if 'pattern' in question:
            pattern_id = question['pattern']
            # Award points for detailed responses
            if len(response) > 50:
                pattern_scores[pattern_id] += 1
    
    def _score_multi_select(self, question: Dict, response: str, pattern_scores: Dict):
        """Score multi-select questions"""
        # Response format: "option1, option2, option3"
        selected = [opt.strip() for opt in response.split(',')]
        
        # Each selection adds base points to emotional complexity
        for pattern_id in range(1, 10):
            if len(selected) > 2:
                pattern_scores[pattern_id] += 0.5
    
    def _normalize_scores(self, pattern_scores: Dict[int, float]) -> Dict[int, float]:
        """Normalize scores to 0-10 scale"""
        if not pattern_scores:
            return pattern_scores
        
        max_score = max(pattern_scores.values())
        if max_score == 0:
            return pattern_scores
        
        # Normalize to 10-point scale
        normalized = {}
        for pattern_id, score in pattern_scores.items():
            normalized[pattern_id] = min(10.0, (score / max_score) * 10)
        
        return normalized
    
    def _get_question_by_id(self, q_id: int) -> Optional[Dict]:
        """Retrieve question by ID from all question sets"""
        # Check all question sets
        all_sets = [
            QuestionSets.AGE_SCREENING,
            QuestionSets.DIGITAL_SCREENING,
            QuestionSets.ENGAGEMENT,
            QuestionSets.TRIGGER_MAPPING,
            QuestionSets.INTEGRATION
        ]
        
        for question_set in all_sets:
            if q_id in question_set:
                return question_set[q_id]
        
        # Check pattern-specific questions
        for pattern_questions in QuestionSets.PATTERN_SPECIFIC.values():
            if q_id in pattern_questions:
                return pattern_questions[q_id]
        
        return None
    
    def calculate_digital_despair_score(self, responses: Dict) -> float:
        """Calculate digital despair syndrome score for digital natives"""
        total_score = 0
        question_count = 0
        
        # Check digital screening questions (1-7)
        for q_id in range(1, 8):
            if q_id in responses:
                question = self._get_question_by_id(q_id)
                if question and 'digital_despair_weights' in question:
                    response = responses[q_id].get('response', '')
                    options = question.get('options', [])
                    
                    try:
                        option_index = options.index(response)
                        weights = question['digital_despair_weights']
                        if option_index < len(weights):
                            total_score += weights[option_index]
                            question_count += 1
                    except (ValueError, IndexError):
                        continue
        
        # Return normalized percentage score
        if question_count == 0:
            return 0.0
        
        max_possible = question_count * 5  # Max weight per question is 5
        return (total_score / max_possible) * 100
    

# ========================================================================================
# ANALYTICS ENGINE
# ========================================================================================

class AnalyticsEngine:
    """Generates comprehensive clinical analytics from assessment data"""
    
    def __init__(self):
        self.scoring_engine = ScoringEngine()
        self.patterns = PatternDefinitions.PATTERNS
        self.pattern_descriptions = PatternDefinitions.PATTERN_DESCRIPTIONS
    
    def generate_complete_analysis(self, assessment_data: Dict) -> Dict:
        """
        Generate comprehensive clinical analysis
        Returns complete analytics structure
        """
        responses = assessment_data.get('responses', {})
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        # Calculate pattern scores
        pattern_scores = self.scoring_engine.calculate_pattern_scores(responses)
        
        # Generate all analysis components
        analysis = {
            'pattern_analysis': self._analyze_patterns(pattern_scores),
            'behavioral_chains': self._map_behavioral_chains(responses),
            'digital_analysis': self._analyze_digital_trauma(responses, is_digital_native),
            'hidden_dynamics': self._uncover_hidden_dynamics(responses, pattern_scores),
            'readiness_profile': self._evaluate_readiness(responses),
            'therapeutic_recommendations': self._generate_recommendations(pattern_scores, is_digital_native),
            'session_planning': self._plan_sessions(pattern_scores, is_digital_native),
            'clinical_insights': self._extract_clinical_insights(responses, pattern_scores)
        }
        
        return analysis
    
    def _analyze_patterns(self, pattern_scores: Dict[int, float]) -> Dict:
        """Analyze pattern intensity and rankings"""
        # Sort patterns by score
        sorted_patterns = sorted(
            pattern_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Identify dominant pattern
        dominant = sorted_patterns[0] if sorted_patterns else (None, 0)
        dominant_id, dominant_score = dominant
        
        # Count clinically significant patterns (score >= 5)
        significant_patterns = [p for p, s in pattern_scores.items() if s >= 5]
        
        # Determine complexity
        complexity = self._assess_complexity(len(significant_patterns), dominant_score)
        
        return {
            'pattern_scores': pattern_scores,
            'dominant_pattern': {
                'id': dominant_id,
                'name': self.patterns.get(dominant_id, 'Unknown'),
                'score': dominant_score,
                'description': self.pattern_descriptions.get(dominant_id, {})
            },
            'secondary_patterns': [
                {
                    'id': p_id,
                    'name': self.patterns.get(p_id),
                    'score': score
                }
                for p_id, score in sorted_patterns[1:4]
                if score >= 5
            ],
            'pattern_count': len(significant_patterns),
            'complexity_assessment': complexity,
            'pattern_ranking': sorted_patterns
        }
    
    def _assess_complexity(self, pattern_count: int, dominant_score: float) -> str:
        """Assess overall pattern complexity"""
        if pattern_count >= 5:
            return "highly complex - multiple interconnected patterns"
        elif pattern_count >= 3:
            return "complex - several significant patterns"
        elif pattern_count == 2:
            return "moderate - dual pattern interaction"
        elif pattern_count == 1 and dominant_score >= 8:
            return "focused - single intense pattern"
        else:
            return "simple - clear focal point"
    
    def _map_behavioral_chains(self, responses: Dict) -> Dict:
        """Map complete behavioral sequences"""
        chain = {
            'trigger': self._extract_chain_element(responses, 'trigger'),
            'physical_response': self._extract_chain_element(responses, 'physical_response'),
            'automatic_thought': self._extract_chain_element(responses, 'automatic_thought'),
            'emotional_response': self._extract_chain_element(responses, 'emotional_response'),
            'behavioral_response': self._extract_chain_element(responses, 'behavioral_response')
        }
        
        # Calculate chain completeness
        completeness = sum(1 for v in chain.values() if v) / len(chain) * 100
        
        return {
            'chain_sequence': chain,
            'completeness_percentage': completeness,
            'intervention_points': self._identify_intervention_points(chain)
        }
    
    def _extract_chain_element(self, responses: Dict, element_type: str) -> Optional[str]:
        """Extract specific chain element from responses"""
        for response_data in responses.values():
            question_data = response_data.get('question_data', {})
            if question_data.get('chain_mapping') == element_type:
                return response_data.get('response', '')
        return None
    
    def _identify_intervention_points(self, chain: Dict) -> List[str]:
        """Identify key intervention windows in behavioral chain"""
        points = []
        
        if chain.get('physical_response'):
            points.append("Physical awareness - early somatic intervention")
        
        if chain.get('automatic_thought'):
            points.append("Thought pattern interruption - cognitive reframe")
        
        if chain.get('behavioral_response'):
            points.append("Behavioral choice point - alternative response installation")
        
        return points
    
    def _analyze_digital_trauma(self, responses: Dict, is_digital_native: bool) -> Optional[Dict]:
        """Analyze digital despair syndrome if applicable"""
        if not is_digital_native:
            return None
        
        digital_score = self.scoring_engine.calculate_digital_despair_score(responses)
        
        # Determine severity
        if digital_score >= 70:
            severity = "SEVERE"
        elif digital_score >= 50:
            severity = "MODERATE"
        elif digital_score >= 30:
            severity = "MILD"
        else:
            severity = "MINIMAL"
        
        return {
            'digital_despair_score': digital_score,
            'severity_level': severity,
            'requires_adaptation': severity in ['SEVERE', 'MODERATE'],
            'specialized_protocol': self._get_digital_protocol(severity),
            'attention_modifications': self._get_attention_modifications(severity)
        }
    
    def _get_digital_protocol(self, severity: str) -> str:
        """Get specialized protocol for digital natives"""
        protocols = {
            'SEVERE': "Full digital-native protocol with attention optimization, anti-authority language, ironic armor dissolution",
            'MODERATE': "Enhanced digital-aware therapy with modified session length and authority resistance awareness",
            'MILD': "Standard approach with digital considerations integrated",
            'MINIMAL': "Traditional approach optimal"
        }
        return protocols.get(severity, "Standard approach")
    
    def _get_attention_modifications(self, severity: str) -> List[str]:
        """Get attention span modifications needed"""
        modifications = {
            'SEVERE': [
                "15-30 minute focused segments",
                "Movement breaks between phases",
                "High-intensity engagement techniques"
            ],
            'MODERATE': [
                "45-60 minute sessions with breaks",
                "Varied engagement methods"
            ],
            'MILD': [
                "Standard 90-minute sessions",
                "Minor pacing adjustments"
            ],
            'MINIMAL': []
        }
        return modifications.get(severity, [])
    
    def _uncover_hidden_dynamics(self, responses: Dict, pattern_scores: Dict) -> Dict:
        """Uncover secondary gains and hidden beliefs"""
        # Extract secondary gain response (question 35)
        secondary_gain = responses.get(35, {}).get('response', 'Not captured')
        
        # Extract safety needs (question 36)
        safety_needs = responses.get(36, {}).get('response', 'Not captured')
        
        # Analyze dominant pattern's protective function
        dominant_id = max(pattern_scores, key=pattern_scores.get)
        protective_function = self.pattern_descriptions.get(dominant_id, {}).get('protective_function', 'Unknown')
        
        return {
            'secondary_gain': secondary_gain,
            'protective_function': protective_function,
            'safety_requirements': safety_needs,
            'resistance_prediction': self._predict_resistance(pattern_scores)
        }
    
    def _predict_resistance(self, pattern_scores: Dict) -> str:
        """Predict likely resistance patterns"""
        high_scores = [p for p, s in pattern_scores.items() if s >= 7]
        
        resistances = []
        if 1 in high_scores:
            resistances.append("May resist positive suggestions as temporary")
        if 3 in high_scores:
            resistances.append("May be skeptical of therapist intentions")
        if 8 in high_scores:
            resistances.append("Change may feel like betraying family")
        
        return "; ".join(resistances) if resistances else "Standard therapeutic resistance expected"
    
    def _evaluate_readiness(self, responses: Dict) -> Dict:
        """Evaluate change readiness and motivation"""
        # Extract urgency (question 38)
        urgency_response = responses.get(38, {}).get('response', '')
        
        urgency_levels = {
            "Extremely urgent": 10,
            "Very urgent": 8,
            "Moderately urgent": 6,
            "Somewhat urgent": 4,
            "Not urgent": 2
        }
        
        readiness_score = urgency_levels.get(urgency_response, 5)
        
        # Extract hypnotic preference (question 37)
        hypnotic_pref = responses.get(37, {}).get('response', 'Collaborative exploration')
        
        return {
            'urgency_level': readiness_score,
            'motivation': self._categorize_motivation(readiness_score),
            'hypnotic_preference': hypnotic_pref,
            'readiness_stage': self._determine_readiness_stage(readiness_score)
        }
    
    def _categorize_motivation(self, score: int) -> str:
        """Categorize motivation level"""
        if score >= 8:
            return "High - immediate action readiness"
        elif score >= 6:
            return "Moderate - exploring solutions actively"
        else:
            return "Low - early contemplation stage"
    
    def _determine_readiness_stage(self, score: int) -> str:
        """Determine stage of change readiness"""
        if score >= 8:
            return "Action - ready for immediate intervention"
        elif score >= 6:
            return "Preparation - planning for change"
        elif score >= 4:
            return "Contemplation - considering change"
        else:
            return "Precontemplation - exploring possibilities"
    
    def _generate_recommendations(self, pattern_scores: Dict, is_digital_native: bool) -> Dict:
        """Generate therapeutic recommendations"""
        dominant_id = max(pattern_scores, key=pattern_scores.get)
        dominant_pattern = self.pattern_descriptions.get(dominant_id, {})
        
        # Count significant patterns
        significant_count = sum(1 for s in pattern_scores.values() if s >= 5)
        
        # Expected session count
        if significant_count >= 4:
            sessions = "2-3 sessions"
            timeline = "3-4 weeks"
        else:
            sessions = "2 sessions"
            timeline = "2-3 weeks"
        
        return {
            'primary_approach': dominant_pattern.get('intervention_focus', 'Personalized hypnotherapy'),
            'session_count': sessions,
            'timeline_estimate': timeline,
            'success_probability': self._calculate_success_probability(pattern_scores, is_digital_native),
            'key_interventions': self._list_key_interventions(dominant_id)
        }
    
    def _calculate_success_probability(self, pattern_scores: Dict, is_digital_native: bool) -> int:
        """Calculate success probability percentage"""
        base_rate = 85
        
        # Adjust for complexity
        significant_count = sum(1 for s in pattern_scores.values() if s >= 5)
        if significant_count >= 5:
            base_rate -= 5
        elif significant_count >= 3:
            base_rate -= 2
        
        # Digital native bonus (specialized protocol)
        if is_digital_native:
            base_rate += 3
        
        return max(70, min(95, base_rate))
    
    def _list_key_interventions(self, dominant_pattern_id: int) -> List[str]:
        """List key therapeutic interventions for pattern"""
        interventions = {
            1: ["Permission installation for positive states", "Safety anchoring with joy", "Expectation reframing"],
            2: ["Collaborative empowerment", "Nervous system regulation", "Win-win response installation"],
            3: ["Gradual trust building", "Transparent safety protocols", "Healthy skepticism calibration"],
            4: ["Both/and integration", "Nuanced thinking installation", "Creative solution generation"],
            5: ["Inherent worth anchoring", "Productivity reframing", "Being permission protocols"],
            6: ["Authentic self integration", "Consistent identity anchoring", "Cross-context confidence"],
            7: ["Self-care permission", "Boundary installation", "Reciprocal relationship patterns"],
            8: ["Personal path claiming", "Family honor integration", "Autonomous decision-making"],
            9: ["Universal strength anchoring", "Context-independent resources", "Consistent boundary maintenance"]
        }
        return interventions.get(dominant_pattern_id, ["Personalized protocol development"])
    
    def _plan_sessions(self, pattern_scores: Dict, is_digital_native: bool) -> Dict:
        """Plan session structure and content"""
        dominant_id = max(pattern_scores, key=pattern_scores.get)
        dominant_name = self.patterns.get(dominant_id)
        significant_count = sum(1 for s in pattern_scores.values() if s >= 5)
        
        # Session 1 planning
        session_1 = f"Deep pattern mapping of {dominant_name}, behavioral chain analysis, therapeutic alliance building"
        if is_digital_native:
            session_1 += ", digital-native rapport establishment"
        
        # Session 2 planning
        session_2 = f"Core {dominant_name} pattern transformation through deep hypnotherapy, neural pathway rewiring"
        
        # Session 3 planning (if needed)
        session_3_needed = significant_count >= 4
        session_3 = "Integration reinforcement and pattern consolidation" if session_3_needed else "Unlikely to be needed"
        
        return {
            'session_1': {
                'duration': '90 minutes',
                'focus': session_1,
                'objectives': [
                    'Complete pattern validation',
                    'Map behavioral chains',
                    'Build therapeutic alliance',
                    'Initial hypnotic preparation'
                ]
            },
            'session_2': {
                'duration': '90 minutes',
                'focus': session_2,
                'objectives': [
                    'Deep hypnotic intervention',
                    'Pattern interruption and rewiring',
                    'New response installation',
                    'Integration and future pacing'
                ]
            },
            'session_3': {
                'duration': '60 minutes',
                'needed': session_3_needed,
                'focus': session_3,
                'note': 'Complimentary if needed based on session 2 results'
            },
            'total_timeline': '2-4 weeks',
            'between_sessions': 'Pattern awareness exercises and integration practice'
        }
    
    def _extract_clinical_insights(self, responses: Dict, pattern_scores: Dict) -> Dict:
        """Extract key clinical insights for therapist"""
        # Extract presenting problem
        presenting_problem = responses.get(8, {}).get('response', 'Not specified')
        
        # Extract chronicity
        chronicity = responses.get(9, {}).get('response', 'Unknown')
        
        # Extract interference level
        interference = responses.get(11, {}).get('response', 5)
        
        # Extract desired outcome
        desired_outcome = responses.get(10, {}).get('response', 'Not specified')
        
        return {
            'presenting_problem': presenting_problem,
            'chronicity': chronicity,
            'interference_level': interference,
            'desired_outcome': desired_outcome,
            'dominant_pattern_focus': self._get_pattern_focus(pattern_scores),
            'clinical_priority': self._determine_clinical_priority(interference, pattern_scores)
        }
    
    def _get_pattern_focus(self, pattern_scores: Dict) -> str:
        """Get clinical focus for dominant pattern"""
        dominant_id = max(pattern_scores, key=pattern_scores.get)
        return self.pattern_descriptions.get(dominant_id, {}).get('intervention_focus', 'Personalized approach')
    
    def _determine_clinical_priority(self, interference: int, pattern_scores: Dict) -> str:
        """Determine clinical priority level"""
        if interference >= 8 or max(pattern_scores.values()) >= 9:
            return "High priority - significant functional impact"
        elif interference >= 6 or max(pattern_scores.values()) >= 7:
            return "Moderate priority - notable interference"
        else:
            return "Standard priority - manageable impact"


# ========================================================================================
# ADAPTIVE QUESTION ROUTER
# ========================================================================================

class QuestionRouter:
    """Routes questions adaptively based on responses"""
    
    def __init__(self):
        self.question_sets = QuestionSets
    
    def get_next_question(self, current_responses: Dict, is_digital_native: bool) -> Optional[Dict]:
        """
        Determine next question based on current responses
        Returns: question dict with ID, or None if complete
        """
        answered_ids = set(current_responses.keys())
        
        # Phase 0: Age screening (always first)
        if 0 not in answered_ids:
            return self._format_question(0, self.question_sets.AGE_SCREENING[0])
        
        # Phase 1: Digital screening (only for digital natives)
        if is_digital_native:
            for q_id in range(1, 8):
                if q_id not in answered_ids:
                    return self._format_question(q_id, self.question_sets.DIGITAL_SCREENING[q_id])
        
        # Phase 2: Core engagement questions
        for q_id in range(8, 12):
            if q_id not in answered_ids:
                return self._format_question(q_id, self.question_sets.ENGAGEMENT[q_id])
        
        # Phase 3: Trigger mapping
        for q_id in range(12, 17):
            if q_id not in answered_ids:
                return self._format_question(q_id, self.question_sets.TRIGGER_MAPPING[q_id])
        
        # Phase 4: Pattern-specific questions (adaptive based on detected patterns)
        pattern_questions = self._get_pattern_specific_questions(current_responses, answered_ids)
        if pattern_questions:
            return pattern_questions
        
        # Phase 5: Integration questions
        for q_id in range(35, 39):
            if q_id not in answered_ids:
                return self._format_question(q_id, self.question_sets.INTEGRATION[q_id])
        
        # Assessment complete
        return None
    
    def _format_question(self, q_id: int, question_data: Dict) -> Dict:
        """Format question with ID for rendering"""
        return {
            'id': q_id,
            **question_data
        }
    
    def _get_pattern_specific_questions(self, responses: Dict, answered_ids: set) -> Optional[Dict]:
        """Get pattern-specific questions based on detected patterns"""
        # Quick pattern detection from responses so far
        scoring_engine = ScoringEngine()
        pattern_scores = scoring_engine.calculate_pattern_scores(responses)
        
        # Get top 3 patterns
        top_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Check pattern-specific questions for top patterns
        for pattern_id, score in top_patterns:
            if score >= 3:  # Threshold for pattern-specific questions
                pattern_key = f"pattern_{pattern_id}"
                if pattern_key in self.question_sets.PATTERN_SPECIFIC:
                    pattern_questions = self.question_sets.PATTERN_SPECIFIC[pattern_key]
                    for q_id, question in pattern_questions.items():
                        if q_id not in answered_ids:
                            return self._format_question(q_id, question)
        
        return None
    
    def estimate_total_questions(self, current_responses: Dict, is_digital_native: bool) -> int:
        """Estimate total number of questions for progress tracking"""
        base = 1  # Age screening
        
        if is_digital_native:
            base += 7  # Digital screening
        
        base += 4  # Engagement
        base += 5  # Trigger mapping
        base += 4  # Integration
        
        # Pattern-specific (estimate 2 per detected pattern)
        scoring_engine = ScoringEngine()
        pattern_scores = scoring_engine.calculate_pattern_scores(current_responses)
        significant_patterns = sum(1 for s in pattern_scores.values() if s >= 3)
        base += significant_patterns * 2
        
        return base


# ========================================================================================
# EXPORT CLASSES
# ========================================================================================

__all__ = [
    'PatternDefinitions',
    'QuestionSets',
    'ScoringEngine',
    'AnalyticsEngine',
    'QuestionRouter'
]