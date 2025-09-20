"""
Enhanced Assessment Configuration
Advanced behavioral pattern analysis with digital despair integration
Sophisticated question matrix with adaptive branching logic
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

# ================================
# SMART QUESTION MATRIX ARCHITECTURE
# ================================

class SmartQuestionMatrix:
    """Intelligent question selection and adaptive assessment flow"""

    # Phase 1: Discovery Questions (Essential for branching)
    DISCOVERY_QUESTIONS = {
        "age_detection": {
            "id": "age_detection",
            "text": "What age range best describes you?",
            "type": "single_choice",
            "options": [
                "16-20", "21-25", "26-30", "31-35",
                "36-45", "46-55", "56+"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {"digital_native": {"16-20": 3, "21-25": 3, "26-30": 2, "31-35": 1}},
            "branching_logic": {
                "16-30": "digital_focus",
                "31-45": "hybrid_focus",
                "46+": "traditional_focus"
            }
        },

        "primary_concern": {
            "id": "primary_concern",
            "text": "What brings you here today?",
            "type": "single_choice",
            "options": [
                "Nothing feels meaningful anymore",
                "Constant anxiety about the future",
                "Stuck in destructive patterns",
                "Relationships keep failing",
                "Can't achieve what I want",
                "Everything feels overwhelming",
                "Lost sense of who I am",
                "Something specific I need to change"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "digital_despair": {"Nothing feels meaningful anymore": 3, "Lost sense of who I am": 2},
                "systematic_mistrust": {"Constant anxiety about the future": 2, "Everything feels overwhelming": 1},
                "power_struggles": {"Relationships keep failing": 2},
                "unhappiness_culture": {"Can't achieve what I want": 2},
                "doing_vs_being": {"Stuck in destructive patterns": 2}
            }
        },

        "digital_habits": {
            "id": "digital_habits",
            "text": "How much time do you spend on screens daily (outside work)?",
            "type": "single_choice",
            "options": [
                "Less than 2 hours",
                "2-4 hours",
                "4-6 hours",
                "6-8 hours",
                "8+ hours",
                "I've lost track"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "digital_conditioning": {"6-8 hours": 2, "8+ hours": 3, "I've lost track": 3},
                "context_dependent_weakness": {"8+ hours": 2, "I've lost track": 2}
            }
        },

        "urgency_level": {
            "id": "urgency_level",
            "text": "How urgent does change feel for you right now?",
            "type": "single_choice",
            "options": [
                "Extremely urgent - things are falling apart",
                "Very urgent - I need help soon",
                "Moderately urgent - within the next few months",
                "Somewhat urgent - this year would be good",
                "Not urgent - just exploring options"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "crisis_indicators": {"Extremely urgent - things are falling apart": 3, "Very urgent - I need help soon": 2}
            }
        },

        "previous_help": {
            "id": "previous_help",
            "text": "Have you tried therapy or coaching before?",
            "type": "single_choice",
            "options": [
                "Never tried anything",
                "Traditional therapy - didn't help much",
                "Multiple approaches - nothing really worked",
                "Had some success but relapsed",
                "Currently in therapy",
                "Prefer to handle things myself"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "therapeutic_resistance": {"Multiple approaches - nothing really worked": 3, "Prefer to handle things myself": 2},
                "systematic_mistrust": {"Traditional therapy - didn't help much": 2}
            }
        }
    }

    # Phase 2: Adaptive Pattern Assessment
    DIGITAL_DESPAIR_QUESTIONS = {
        "reality_dissociation": {
            "id": "reality_dissociation",
            "text": "Online interactions often feel more authentic than face-to-face conversations",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        },

        "ironic_detachment": {
            "id": "ironic_detachment",
            "text": "Genuine emotions feel 'cringe' - irony and sarcasm feel safer",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        },

        "binary_success": {
            "id": "binary_success",
            "text": "Either I achieve something extraordinary or I'm basically a failure",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}, "inherited_missions": {"Agree": 1, "Strongly agree": 2}}
        },

        "algorithmic_conditioning": {
            "id": "algorithmic_conditioning",
            "text": "My mood is significantly influenced by what I see on social media",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        },

        "future_hopelessness": {
            "id": "future_hopelessness",
            "text": "Unless something extraordinary happens (like winning the lottery), life won't get much better",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}, "unhappiness_culture": {"Agree": 1}}
        },

        "attention_fragmentation": {
            "id": "attention_fragmentation",
            "text": "I struggle to focus on one thing for more than a few minutes without checking my phone",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        },

        "parasocial_preference": {
            "id": "parasocial_preference",
            "text": "Online personalities (streamers, influencers) feel more relatable than people in my real life",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        },

        "nihilistic_sophistication": {
            "id": "nihilistic_sophistication",
            "text": "Believing that 'nothing really matters' feels intellectually honest rather than depressing",
            "type": "scale_agreement",
            "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
            "skip_allowed": True,
            "weight": {"digital_despair": {"Agree": 2, "Strongly agree": 3}}
        }
    }

    # Traditional Behavioral Patterns (Enhanced)
    BEHAVIORAL_PATTERN_QUESTIONS = {
        "unhappiness_culture": {
            "happiness_guilt": {
                "id": "happiness_guilt",
                "text": "When good things happen, I automatically start looking for what could go wrong",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"unhappiness_culture": {"Agree": 2, "Strongly agree": 3}}
            },
            "success_minimization": {
                "id": "success_minimization",
                "text": "I tend to downplay my achievements or find reasons they 'don't count'",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"unhappiness_culture": {"Agree": 2, "Strongly agree": 3}}
            },
            "joy_permission": {
                "id": "joy_permission",
                "text": "Deep down, I believe I don't deserve to be genuinely happy",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"unhappiness_culture": {"Agree": 2, "Strongly agree": 3}}
            }
        },

        "power_struggles": {
            "conflict_adrenaline": {
                "id": "conflict_adrenaline",
                "text": "I feel energized by arguments and debates, even when they're not productive",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"power_struggles": {"Agree": 2, "Strongly agree": 3}}
            },
            "win_lose_thinking": {
                "id": "win_lose_thinking",
                "text": "In disagreements, someone has to be right and someone has to be wrong",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"power_struggles": {"Agree": 2, "Strongly agree": 3}, "separation_division": {"Agree": 1}}
            },
            "submission_resentment": {
                "id": "submission_resentment",
                "text": "When I have to go along with others, I often feel resentful afterwards",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"power_struggles": {"Agree": 2, "Strongly agree": 3}}
            }
        },

        "systematic_mistrust": {
            "default_suspicion": {
                "id": "default_suspicion",
                "text": "My first instinct is to question people's motives rather than trust them",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"systematic_mistrust": {"Agree": 2, "Strongly agree": 3}}
            },
            "vulnerability_danger": {
                "id": "vulnerability_danger",
                "text": "Being vulnerable feels dangerous - like giving others ammunition against me",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"systematic_mistrust": {"Agree": 2, "Strongly agree": 3}}
            },
            "worst_case_preparation": {
                "id": "worst_case_preparation",
                "text": "I often prepare for the worst-case scenario in relationships and situations",
                "type": "scale_agreement",
                "scale": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
                "skip_allowed": True,
                "weight": {"systematic_mistrust": {"Agree": 2, "Strongly agree": 3}}
            }
        }
    }

    # Deep Validation Questions (Triggered only if patterns detected)
    PATTERN_VALIDATION_QUESTIONS = {
        "digital_despair_triggers": {
            "id": "digital_despair_triggers",
            "text": "What typically triggers your strongest feelings of hopelessness?",
            "type": "multiple_choice",
            "options": [
                "Seeing others' success on social media",
                "Thinking about job/career prospects",
                "Being asked about future plans",
                "Comparing my life to expectations",
                "Economic news or housing costs",
                "Family questions about achievements",
                "Dating app experiences"
            ],
            "skip_allowed": True,
            "condition": "digital_despair_score > 8"
        },

        "pattern_origin_exploration": {
            "id": "pattern_origin_exploration",
            "text": "When did you first remember feeling like you had to be extraordinary to matter?",
            "type": "single_choice",
            "options": [
                "Elementary school",
                "Middle school",
                "High school",
                "College/University",
                "After graduation",
                "Can't remember - feels like always"
            ],
            "skip_allowed": True,
            "condition": "inherited_missions_score > 6"
        }
    }

# ================================
# DIGITAL DESPAIR SYNDROME FRAMEWORK
# ================================

class DigitalDespairAssessment:
    """Comprehensive assessment for digital despair syndrome"""

    SYNDROME_COMPONENTS = {
        "reality_dissociation": {
            "name": "Reality Dissociation",
            "description": "Online engagement feels more authentic than offline relationships",
            "indicators": ["parasocial_preference", "digital_authenticity", "offline_anxiety"],
            "intervention_priority": "high"
        },

        "ironic_detachment": {
            "name": "Ironic Armor",
            "description": "Cynical defense against vulnerability and disappointment",
            "indicators": ["emotional_cringe", "sincerity_fear", "hope_resistance"],
            "intervention_priority": "critical"
        },

        "binary_success_framework": {
            "name": "Binary Success Trap",
            "description": "Extraordinary achievement vs complete failure thinking",
            "indicators": ["normal_inadequacy", "extraordinary_requirement", "incremental_dismissal"],
            "intervention_priority": "high"
        },

        "algorithmic_conditioning": {
            "name": "Algorithm Dependency",
            "description": "Emotional regulation dependent on digital feeds",
            "indicators": ["mood_algorithm_link", "rage_consumption", "validation_seeking"],
            "intervention_priority": "medium"
        },

        "attention_fragmentation": {
            "name": "Attention Collapse",
            "description": "Inability to sustain focus without digital stimulation",
            "indicators": ["focus_struggle", "stimulation_seeking", "boredom_intolerance"],
            "intervention_priority": "medium"
        },

        "future_hopelessness": {
            "name": "Existential Despair",
            "description": "No realistic path to meaningful life improvement",
            "indicators": ["lottery_mentality", "systemic_hopelessness", "agency_loss"],
            "intervention_priority": "critical"
        },

        "nihilistic_sophistication": {
            "name": "Intellectual Nihilism",
            "description": "'Nothing matters' philosophy as protection against caring",
            "indicators": ["meaning_dismissal", "caring_cringe", "detachment_pride"],
            "intervention_priority": "high"
        }
    }

    @staticmethod
    def calculate_syndrome_severity(responses: Dict) -> Dict:
        """Calculate digital despair syndrome severity across all components"""
        component_scores = {}

        for component, config in DigitalDespairAssessment.SYNDROME_COMPONENTS.items():
            score = 0
            # Complex scoring algorithm based on responses
            # Would implement sophisticated pattern matching here
            component_scores[component] = score

        return {
            "total_score": sum(component_scores.values()),
            "component_scores": component_scores,
            "severity_level": DigitalDespairAssessment._determine_severity_level(sum(component_scores.values())),
            "intervention_recommendations": DigitalDespairAssessment._get_intervention_recommendations(component_scores)
        }

    @staticmethod
    def _determine_severity_level(total_score: int) -> str:
        """Determine severity level based on total score"""
        if total_score >= 20: return "Severe"
        elif total_score >= 15: return "Moderate-Severe"
        elif total_score >= 10: return "Moderate"
        elif total_score >= 5: return "Mild-Moderate"
        else: return "Minimal"

    @staticmethod
    def _get_intervention_recommendations(component_scores: Dict) -> List[str]:
        """Generate intervention recommendations based on component scores"""
        recommendations = []

        # Digital overwhelm interventions
        if component_scores.get("digital_overwhelm", 0) >= 3:
            recommendations.extend([
                "Digital detox protocols",
                "Attention restoration techniques",
                "Mindfulness-based stress reduction"
            ])

        # Social comparison interventions
        if component_scores.get("social_comparison", 0) >= 3:
            recommendations.extend([
                "Self-worth reconstruction therapy",
                "Cognitive restructuring for comparison",
                "Authentic self-expression training"
            ])

        # Instant gratification dependency
        if component_scores.get("instant_gratification", 0) >= 3:
            recommendations.extend([
                "Delayed gratification training",
                "Dopamine regulation strategies",
                "Goal-setting and achievement frameworks"
            ])

        # FOMO and connection anxiety
        if component_scores.get("connection_anxiety", 0) >= 3:
            recommendations.extend([
                "Social anxiety management",
                "Real-world connection building",
                "Present-moment awareness training"
            ])

        # Identity fragmentation
        if component_scores.get("identity_fragmentation", 0) >= 3:
            recommendations.extend([
                "Identity integration therapy",
                "Authentic self-discovery work",
                "Values clarification exercises"
            ])

        # Reality disconnection
        if component_scores.get("reality_disconnection", 0) >= 3:
            recommendations.extend([
                "Grounding and embodiment practices",
                "Physical world re-engagement",
                "Sensory awareness enhancement"
            ])

        # Validation dependency
        if component_scores.get("validation_dependency", 0) >= 3:
            recommendations.extend([
                "Self-validation development",
                "Internal confidence building",
                "Independence from external approval"
            ])

        # Default recommendations if none specified
        if not recommendations:
            recommendations = [
                "Digital wellness assessment",
                "Mindfulness-based interventions",
                "Lifestyle balance optimization"
            ]

        return recommendations

# ================================
# ADAPTIVE QUESTION FLOW LOGIC
# ================================

class AdaptiveQuestionFlow:
    """Intelligent question selection and flow management"""

    def __init__(self):
        self.responses = {}
        self.pattern_scores = {}
        self.current_phase = "discovery"
        self.assessment_path = None

    def get_next_question(self, current_responses: Dict) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next question based on adaptive logic"""
        self.responses = current_responses
        self._update_pattern_scores()

        if self.current_phase == "discovery":
            return self._get_discovery_question()
        elif self.current_phase == "adaptive_assessment":
            return self._get_adaptive_question()
        elif self.current_phase == "pattern_validation":
            return self._get_validation_question()
        elif self.current_phase == "integration":
            return self._get_integration_question()
        else:
            return None, None

    def _get_discovery_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next discovery phase question"""
        for q_id, question in SmartQuestionMatrix.DISCOVERY_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Discovery complete, determine assessment path
        self._determine_assessment_path()
        self.current_phase = "adaptive_assessment"
        return self._get_adaptive_question()

    def _determine_assessment_path(self):
        """Determine which assessment path to follow based on discovery responses"""
        age_response = self.responses.get("age_detection", "")
        digital_response = self.responses.get("digital_habits", "")

        # Age-based path selection
        if any(age in age_response for age in ["16-20", "21-25", "26-30"]):
            if any(usage in digital_response for usage in ["6-8 hours", "8+ hours", "I've lost track"]):
                self.assessment_path = "digital_focus"
            else:
                self.assessment_path = "hybrid_focus"
        else:
            self.assessment_path = "traditional_focus"

    def _get_adaptive_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next adaptive assessment question based on path"""

        # Digital focus path
        if self.assessment_path == "digital_focus":
            return self._get_digital_despair_question()

        # Traditional focus path
        elif self.assessment_path == "traditional_focus":
            return self._get_behavioral_pattern_question()

        # Hybrid path - mix both
        else:
            # Alternate between digital and behavioral questions
            digital_answered = len([q for q in self.responses.keys()
                                   if q in SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS])
            behavioral_answered = len([q for q in self.responses.keys()
                                      if any(q in category for category in SmartQuestionMatrix.BEHAVIORAL_PATTERN_QUESTIONS.values())])

            if digital_answered <= behavioral_answered:
                return self._get_digital_despair_question()
            else:
                return self._get_behavioral_pattern_question()

    def _get_digital_despair_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next digital despair question"""
        for q_id, question in SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Digital questions complete, move to validation
        self.current_phase = "pattern_validation"
        return self._get_validation_question()

    def _get_behavioral_pattern_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next behavioral pattern question"""
        for pattern_category, questions in SmartQuestionMatrix.BEHAVIORAL_PATTERN_QUESTIONS.items():
            for q_id, question in questions.items():
                if q_id not in self.responses:
                    return q_id, question

        # Behavioral questions complete, move to validation
        self.current_phase = "pattern_validation"
        return self._get_validation_question()

    def _get_validation_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next pattern validation question"""
        # Check which patterns need validation based on scores
        self._update_pattern_scores()

        for q_id, question in SmartQuestionMatrix.PATTERN_VALIDATION_QUESTIONS.items():
            if q_id not in self.responses:
                # Check if condition is met for this validation question
                condition = question.get("condition", "")
                if self._evaluate_condition(condition):
                    return q_id, question

        # Validation complete, move to integration
        self.current_phase = "integration"
        return self._get_integration_question()

    def _get_integration_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get integration phase questions"""
        # Expanded integration questions for better assessment completion
        integration_questions = {
            "change_readiness": {
                "id": "change_readiness",
                "text": "How ready are you to make significant changes in your life?",
                "type": "scale_agreement",
                "scale": ["Not ready", "Somewhat ready", "Ready", "Very ready", "Completely ready"],
                "skip_allowed": True
            },
            "preferred_approach": {
                "id": "preferred_approach",
                "text": "What type of therapeutic approach appeals to you most?",
                "type": "single_choice",
                "options": [
                    "Fast, intensive transformation",
                    "Gradual, step-by-step change",
                    "Combination of both approaches",
                    "Whatever the expert recommends"
                ],
                "skip_allowed": True
            },
            "commitment_level": {
                "id": "commitment_level",
                "text": "How committed are you to following through with a transformation process?",
                "type": "scale_agreement",
                "scale": ["Not committed", "Somewhat committed", "Committed", "Very committed", "Fully committed"],
                "skip_allowed": True
            },
            "timeline_preference": {
                "id": "timeline_preference",
                "text": "What timeline would work best for your transformation journey?",
                "type": "single_choice",
                "options": [
                    "Within the next month",
                    "Within 2-3 months",
                    "Within 6 months",
                    "No specific timeline",
                    "I need to think about timing"
                ],
                "skip_allowed": True
            }
        }

        for q_id, question in integration_questions.items():
            if q_id not in self.responses:
                return q_id, question

        # Assessment complete
        return None, None

    def _evaluate_condition(self, condition: str) -> bool:
        """Evaluate if a validation question condition is met"""
        if not condition:
            return True

        # Simple condition evaluation
        if "digital_despair_score > 8" in condition:
            digital_score = sum(1 for q_id in self.responses.keys()
                               if q_id in SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS
                               and "Agree" in str(self.responses[q_id]))
            return digital_score > 8

        if "inherited_missions_score > 6" in condition:
            # Simplified scoring for demo
            return self.responses.get("age_detection", "") in ["16-20", "21-25"]

        return True

    def _update_pattern_scores(self):
        """Update pattern scores based on current responses"""
        # Calculate preliminary scores for validation logic
        for pattern in ["digital_despair", "inherited_missions", "systematic_mistrust"]:
            score = 0
            for q_id, response in self.responses.items():
                if "Agree" in str(response) or "Strongly agree" in str(response):
                    score += 1
            self.pattern_scores[pattern] = score

# ================================
# COMPREHENSIVE PROFILING ENGINE
# ================================

class ComprehensiveProfiler:
    """Generate detailed psychological profiles from assessment data"""

    @staticmethod
    def generate_complete_profile(responses: Dict) -> Dict:
        """Generate comprehensive psychological profile"""

        # Calculate all pattern scores
        behavioral_patterns = ComprehensiveProfiler._calculate_behavioral_patterns(responses)
        digital_analysis = DigitalDespairAssessment.calculate_syndrome_severity(responses)
        clinical_profile = ComprehensiveProfiler._generate_clinical_profile(responses)

        return {
            "assessment_metadata": {
                "completion_time": datetime.now().isoformat(),
                "total_questions_answered": len(responses),
                "assessment_path": ComprehensiveProfiler._determine_path(responses),
                "completion_percentage": ComprehensiveProfiler._calculate_completion(responses)
            },

            "behavioral_patterns": behavioral_patterns,
            "digital_analysis": digital_analysis,
            "clinical_profile": clinical_profile,

            "intervention_recommendations": ComprehensiveProfiler._generate_interventions(
                behavioral_patterns, digital_analysis, clinical_profile
            ),

            "therapeutic_approach": ComprehensiveProfiler._recommend_therapeutic_approach(
                behavioral_patterns, digital_analysis
            )
        }

    @staticmethod
    def _calculate_behavioral_patterns(responses: Dict) -> Dict:
        """Calculate comprehensive behavioral pattern scores"""
        pattern_scores = {
            "unhappiness_culture": 0,
            "power_struggles": 0,
            "systematic_mistrust": 0,
            "separation_division": 0,
            "doing_vs_being": 0,
            "compartmentalized_authenticity": 0,
            "self_sacrifice": 0,
            "inherited_missions": 0,
            "context_dependent_weakness": 0,
            "digital_despair": 0
        }

        # Calculate scores based on weighted responses (including neutral handling)
        for question_id, response in responses.items():
            if response == "SKIPPED":
                continue

            # Digital despair indicators (enhanced neutral handling)
            if question_id in ["reality_dissociation", "ironic_detachment", "binary_success",
                              "algorithmic_conditioning", "future_hopelessness", "attention_fragmentation"]:
                if "Strongly agree" in str(response):
                    pattern_scores["digital_despair"] += 3
                elif "Agree" in str(response):
                    pattern_scores["digital_despair"] += 2
                elif "Neutral" in str(response):
                    pattern_scores["digital_despair"] += 1  # Neutral still indicates some pattern presence

            # Traditional pattern detection (enhanced)
            if "automatically start looking for what could go wrong" in str(response):
                if "Strongly agree" in str(response):
                    pattern_scores["unhappiness_culture"] += 3
                elif "Agree" in str(response):
                    pattern_scores["unhappiness_culture"] += 2
                elif "Neutral" in str(response):
                    pattern_scores["unhappiness_culture"] += 1

            if "energized by arguments" in str(response):
                if "Strongly agree" in str(response):
                    pattern_scores["power_struggles"] += 3
                elif "Agree" in str(response):
                    pattern_scores["power_struggles"] += 2
                elif "Neutral" in str(response):
                    pattern_scores["power_struggles"] += 1

            if "question people's motives" in str(response):
                if "Strongly agree" in str(response):
                    pattern_scores["systematic_mistrust"] += 3
                elif "Agree" in str(response):
                    pattern_scores["systematic_mistrust"] += 2
                elif "Neutral" in str(response):
                    pattern_scores["systematic_mistrust"] += 1

            # Age-based inherited missions scoring
            if question_id == "age_detection" and any(age in str(response) for age in ["16-20", "21-25", "26-30"]):
                pattern_scores["inherited_missions"] += 2

            # Digital conditioning context dependency
            if question_id == "digital_habits":
                if any(usage in str(response) for usage in ["8+ hours", "I've lost track"]):
                    pattern_scores["context_dependent_weakness"] += 3
                elif any(usage in str(response) for usage in ["6-8 hours", "4-6 hours"]):
                    pattern_scores["context_dependent_weakness"] += 2
                elif any(usage in str(response) for usage in ["2-4 hours"]):
                    pattern_scores["context_dependent_weakness"] += 1

            # Baseline pattern scoring for engagement (even neutral responses indicate patterns)
            if "Neutral" in str(response) or any(word in str(response) for word in ["Ready", "Somewhat", "Moderately"]):
                # Distribute neutral engagement across multiple potential patterns
                pattern_scores["doing_vs_being"] += 1
                pattern_scores["compartmentalized_authenticity"] += 1

        # Determine primary and secondary patterns (enhanced for neutral responses)
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)

        # If no clear patterns emerge, create a balanced profile
        if sorted_patterns[0][1] == 0:
            primary_pattern = "balanced_assessment"
            secondary_patterns = ["doing_vs_being", "compartmentalized_authenticity"]
        else:
            primary_pattern = sorted_patterns[0][0]
            # Lower threshold for secondary patterns to ensure profiling
            secondary_patterns = [p[0] for p in sorted_patterns[1:4] if p[1] > 0]

        # Pattern interactions
        interactions = ComprehensiveProfiler._detect_pattern_interactions(pattern_scores)

        # Severity levels
        severity_levels = {}
        for pattern, score in pattern_scores.items():
            if score >= 8: severity_levels[pattern] = "severe"
            elif score >= 6: severity_levels[pattern] = "moderate"
            elif score >= 3: severity_levels[pattern] = "mild"

        return {
            "primary_pattern": primary_pattern,
            "secondary_patterns": secondary_patterns,
            "pattern_interactions": interactions,
            "severity_levels": severity_levels,
            "raw_scores": pattern_scores
        }

    @staticmethod
    def _generate_clinical_profile(responses: Dict) -> Dict:
        """Generate comprehensive clinical assessment profile"""

        # Calculate readiness score
        readiness_score = 50  # Base score

        urgency = responses.get("urgency_level", "")
        if "Extremely urgent" in urgency:
            readiness_score += 30
        elif "Very urgent" in urgency:
            readiness_score += 20
        elif "Moderately urgent" in urgency:
            readiness_score += 10

        # Previous help experience
        previous_help = responses.get("previous_help", "")
        resistance_factors = []
        if "Multiple approaches - nothing really worked" in previous_help:
            resistance_factors.append("therapy_skepticism")
            readiness_score -= 10
        elif "Prefer to handle things myself" in previous_help:
            resistance_factors.append("independence_preference")
            readiness_score -= 5

        # Age-based success predictors
        age_response = responses.get("age_detection", "")
        success_predictors = []
        if any(age in age_response for age in ["16-20", "21-25", "26-30"]):
            success_predictors.extend(["neuroplasticity_advantage", "digital_native_adaptability"])

        # Digital conditioning assessment
        digital_hours = responses.get("digital_habits", "")
        session_complexity = "standard"
        estimated_sessions = 2

        if "8+ hours" in digital_hours or "I've lost track" in digital_hours:
            session_complexity = "complex"
            estimated_sessions = 3
            success_predictors.append("digital_fluency")

        # Intelligence indicators
        sophisticated_responses = 0
        for response in responses.values():
            if isinstance(response, str) and len(response) > 50:
                sophisticated_responses += 1

        if sophisticated_responses >= 2:
            success_predictors.append("high_analytical_capacity")
            readiness_score += 10

        return {
            "readiness_score": min(100, max(0, readiness_score)),
            "resistance_factors": resistance_factors,
            "success_predictors": success_predictors,
            "session_complexity": session_complexity,
            "estimated_sessions": estimated_sessions,
            "therapeutic_approach_recommendations": ComprehensiveProfiler._recommend_approach(responses)
        }

    @staticmethod
    def _detect_pattern_interactions(pattern_scores: Dict) -> List[str]:
        """Detect pattern interactions and reinforcement cycles"""
        interactions = []

        # Digital despair + inherited missions = extraordinary pressure
        if pattern_scores.get("digital_despair", 0) >= 4 and pattern_scores.get("inherited_missions", 0) >= 3:
            interactions.append("digital_amplified_achievement_pressure")

        # Systematic mistrust + power struggles = defensive isolation
        if pattern_scores.get("systematic_mistrust", 0) >= 3 and pattern_scores.get("power_struggles", 0) >= 3:
            interactions.append("defensive_isolation_cycle")

        # Context dependent weakness + digital despair = reality avoidance
        if pattern_scores.get("context_dependent_weakness", 0) >= 3 and pattern_scores.get("digital_despair", 0) >= 4:
            interactions.append("reality_avoidance_amplification")

        return interactions

    @staticmethod
    def _recommend_approach(responses: Dict) -> List[str]:
        """Recommend therapeutic approach based on profile"""
        recommendations = []

        age = responses.get("age_detection", "")
        digital_usage = responses.get("digital_habits", "")

        # Digital native recommendations
        if any(young_age in age for young_age in ["16-20", "21-25", "26-30"]):
            recommendations.append("digital_native_adapted_hypnotherapy")

        # High digital usage adaptations
        if "8+ hours" in digital_usage or "I've lost track" in digital_usage:
            recommendations.extend([
                "attention_span_adapted_sessions",
                "gamification_elements",
                "digital_detox_preparation"
            ])

        # Authority resistance handling
        previous_help = responses.get("previous_help", "")
        if "Multiple approaches - nothing really worked" in previous_help:
            recommendations.append("collaborative_non_authoritarian_approach")

        return recommendations

    @staticmethod
    def _determine_path(responses: Dict) -> str:
        """Determine assessment path based on responses"""

        # Check age to determine digital native status
        age_response = responses.get("age_detection", "")
        digital_native = any(age in age_response for age in ["16-20", "21-25", "26-30"])

        # Check digital usage patterns
        digital_hours = responses.get("digital_habits", "")
        high_digital_usage = "8+ hours" in digital_hours or "I've lost track" in digital_hours

        # Check digital-focused responses
        digital_focus_indicators = 0
        for question_id, response in responses.items():
            if question_id.startswith(("social_", "instant_", "fomo_", "validation_", "identity_")):
                if isinstance(response, str) and any(keyword in response.lower() for keyword in ["strongly agree", "agree", "very", "extremely"]):
                    digital_focus_indicators += 1

        # Check traditional pattern focus
        traditional_focus_indicators = 0
        for question_id, response in responses.items():
            if question_id.startswith(("inherited_", "systematic_", "power_", "compartment_", "context_")):
                if isinstance(response, str) and any(keyword in response.lower() for keyword in ["strongly agree", "agree", "very", "extremely"]):
                    traditional_focus_indicators += 1

        # Determine path based on indicators
        if digital_native and high_digital_usage and digital_focus_indicators >= 3:
            return "digital_focus"
        elif not digital_native and traditional_focus_indicators >= 3:
            return "traditional_focus"
        else:
            return "hybrid_focus"

    @staticmethod
    def _calculate_completion(responses: Dict) -> float:
        """Calculate assessment completion percentage"""

        if not responses:
            return 0.0

        # Count total questions in the assessment matrix
        total_discovery = len(SmartQuestionMatrix.DISCOVERY_QUESTIONS)
        total_digital = len(SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS)
        total_behavioral = 0
        for pattern_category, questions in SmartQuestionMatrix.BEHAVIORAL_PATTERN_QUESTIONS.items():
            total_behavioral += len(questions)
        total_validation = len(SmartQuestionMatrix.PATTERN_VALIDATION_QUESTIONS)
        total_integration = 4  # Integration questions are dynamic

        # Determine expected total based on assessment path
        assessment_path = ComprehensiveProfiler._determine_path(responses)
        if assessment_path == "digital_focus":
            expected_total = total_discovery + total_digital + total_validation + total_integration
        elif assessment_path == "traditional_focus":
            expected_total = total_discovery + total_behavioral + total_validation + total_integration
        else:  # hybrid_focus
            expected_total = total_discovery + (total_digital // 2) + (total_behavioral // 2) + total_validation + total_integration

        # Calculate completion percentage
        completed_questions = len(responses)
        completion_percentage = min(100.0, (completed_questions / expected_total) * 100)

        return round(completion_percentage, 1)

    @staticmethod
    def _generate_interventions(behavioral_patterns: Dict, digital_analysis: Dict, clinical_profile: Dict) -> List[str]:
        """Generate intervention recommendations based on assessment data"""

        interventions = []

        # Behavioral pattern interventions
        if behavioral_patterns:
            for pattern, score in behavioral_patterns.items():
                # Convert score to float for comparison, default to 0 if conversion fails
                try:
                    score_value = float(score) if score is not None else 0.0
                except (ValueError, TypeError):
                    score_value = 0.0

                if score_value >= 3:  # High score threshold
                    if pattern == "unhappiness_culture":
                        interventions.extend([
                            "Cognitive restructuring for happiness patterns",
                            "Values clarification exercises",
                            "Gratitude and positive psychology interventions"
                        ])
                    elif pattern == "power_struggles":
                        interventions.extend([
                            "Assertiveness training",
                            "Boundary setting techniques",
                            "Collaborative problem-solving skills"
                        ])
                    elif pattern == "systematic_mistrust":
                        interventions.extend([
                            "Trust-building exercises",
                            "Social anxiety intervention",
                            "Attachment style work"
                        ])
                    elif pattern == "separation_division":
                        interventions.extend([
                            "Integration therapy techniques",
                            "Holistic thinking patterns",
                            "Connection and unity practices"
                        ])
                    elif pattern == "doing_vs_being":
                        interventions.extend([
                            "Mindfulness and presence training",
                            "Work-life balance coaching",
                            "Being-oriented meditation practices"
                        ])

        # Digital despair interventions
        if digital_analysis and digital_analysis.get("overall_severity_level") in ["Moderate", "Moderate-Severe", "Severe"]:
            interventions.extend([
                "Digital detox protocols",
                "Attention restoration training",
                "Technology mindfulness practices",
                "Real-world engagement activities"
            ])

        # Clinical profile based interventions
        if clinical_profile:
            readiness_raw = clinical_profile.get("therapeutic_readiness", {}).get("overall_readiness", 0)
            # Convert readiness to float for comparison
            try:
                readiness = float(readiness_raw) if readiness_raw is not None else 0.0
            except (ValueError, TypeError):
                readiness = 0.0

            if readiness >= 7:  # High readiness
                interventions.append("Intensive transformation program")
            elif readiness >= 4:  # Moderate readiness
                interventions.append("Gradual change approach with support")
            else:  # Low readiness
                interventions.extend([
                    "Motivation enhancement techniques",
                    "Readiness building exercises"
                ])

        # Remove duplicates and return
        return list(set(interventions))

    @staticmethod
    def _recommend_therapeutic_approach(behavioral_patterns: Dict, digital_analysis: Dict) -> Dict:
        """Recommend therapeutic approach based on assessment data"""

        approach = {
            "primary_modality": "Rapid Transformation Therapy (RTT)",
            "session_length": "90-120 minutes",
            "estimated_sessions": 3,
            "focus_areas": [],
            "modifications": []
        }

        # Determine focus areas based on behavioral patterns
        if behavioral_patterns:
            high_scoring_patterns = []
            for pattern, score in behavioral_patterns.items():
                # Convert score to float for comparison
                try:
                    score_value = float(score) if score is not None else 0.0
                except (ValueError, TypeError):
                    score_value = 0.0

                if score_value >= 3:
                    high_scoring_patterns.append(pattern)

            if "digital_despair" in high_scoring_patterns:
                approach["focus_areas"].append("Digital detox and attention restoration")
                approach["modifications"].append("Technology-adapted hypnosis techniques")

            if "unhappiness_culture" in high_scoring_patterns:
                approach["focus_areas"].append("Happiness pattern restructuring")
                approach["session_length"] = "120 minutes"  # Longer for deeper work

            if "power_struggles" in high_scoring_patterns:
                approach["focus_areas"].append("Authority and control issues")
                approach["modifications"].append("Collaborative, non-authoritarian approach")

            if "systematic_mistrust" in high_scoring_patterns:
                approach["focus_areas"].append("Trust and safety building")
                approach["estimated_sessions"] = 4  # May need extra session for trust building

        # Digital analysis modifications
        if digital_analysis:
            severity = digital_analysis.get("overall_severity_level", "Mild")
            if severity in ["Severe", "Moderate-Severe"]:
                approach["modifications"].extend([
                    "Shortened attention span accommodations",
                    "Multi-sensory hypnosis approach",
                    "Digital preparation protocols"
                ])
                approach["estimated_sessions"] = 4  # May need extra session

        # Default focus if none identified
        if not approach["focus_areas"]:
            approach["focus_areas"] = ["General transformation and goal achievement"]

        return approach

# ================================
# ENHANCED EMAIL AND NOTIFICATIONS
# ================================

class EnhancedEmailConfig:
    """Enhanced email configuration for comprehensive reports"""

    @staticmethod
    def generate_therapist_report(profile: Dict, contact_info: Dict) -> str:
        """Generate comprehensive therapist report"""

        return f"""
COMPREHENSIVE ASSESSMENT REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

CLIENT INFORMATION:
Name: {contact_info.get('name', 'Not provided')}
Email: {contact_info.get('email', 'Not provided')}
Urgency: {profile.get('urgency_level', 'Unknown')}

DIGITAL DESPAIR ANALYSIS:
Severity: {profile.get('digital_analysis', {}).get('severity_level', 'Unknown')}
Primary Components: {', '.join(profile.get('digital_analysis', {}).get('component_scores', {}).keys())}

BEHAVIORAL PATTERNS:
Primary: {profile.get('behavioral_patterns', {}).get('primary_pattern', 'Unknown')}
Secondary: {', '.join(profile.get('behavioral_patterns', {}).get('secondary_patterns', []))}

THERAPEUTIC RECOMMENDATIONS:
Approach: {profile.get('therapeutic_approach', 'Unknown')}
Estimated Sessions: {profile.get('clinical_profile', {}).get('estimated_sessions', 'Unknown')}
Success Predictors: {', '.join(profile.get('clinical_profile', {}).get('success_predictors', []))}

INTERVENTION PRIORITIES:
{profile.get('intervention_recommendations', 'Not generated')}
        """

# ================================
# SKIP FUNCTIONALITY RULES
# ================================

class SkipLogic:
    """Manage skip functionality and completion requirements"""

    SKIP_RULES = {
        "discovery_phase": {
            "skip_allowed": True,
            "reason": "Essential for adaptive branching"
        },
        "adaptive_assessment": {
            "skip_allowed": True,
            "max_skips_per_pattern": 3,
            "warning_message": "Skipping reduces assessment accuracy"
        },
        "pattern_validation": {
            "skip_allowed": True,
            "warning_message": "Deep insights help optimize your sessions"
        },
        "integration_phase": {
            "skip_allowed": True,
            "reason": "Required for therapeutic planning"
        }
    }

    @staticmethod
    def can_skip_question(question_id: str, current_phase: str, skip_count: Dict) -> Tuple[bool, str]:
        """Determine if question can be skipped and return reason if not"""
        rules = SkipLogic.SKIP_RULES.get(current_phase, {})

        if not rules.get("skip_allowed", False):
            return False, rules.get("reason", "Required question")

        # Check pattern-specific skip limits
        max_skips = rules.get("max_skips_per_pattern", float('inf'))
        if skip_count.get(current_phase, 0) >= max_skips:
            return False, f"Maximum skips reached for this section"

        return True, rules.get("warning_message", "")
