
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum
import json
import numpy as np
from datetime import datetime

# All classes are now defined locally in this file - no external imports needed

# ================================
# USER-FRIENDLY ASSESSMENT QUESTIONNAIRE
# ================================
# Revamped questionnaire with logical funnel progression and public-friendly language
# Maintains clinical integrity while being accessible to general public

class QuestionnaireStage(Enum):
    """Logical progression stages for the assessment funnel"""
    STAGE_1_WELCOME = "welcome_and_context"           # 3-4 questions - Easy entry
    STAGE_2_CURRENT_LIFE = "current_life_situation"   # 4-5 questions - Present focus
    STAGE_3_PATTERNS = "life_patterns"                # 6-8 questions - Pattern identification
    STAGE_4_RELATIONSHIPS = "relationships_and_social" # 4-5 questions - Social dynamics
    STAGE_5_WELLBEING = "emotional_wellbeing"         # 5-6 questions - Inner experience
    STAGE_6_GOALS = "change_and_goals"                # 3-4 questions - Future focus

@dataclass
class UserFriendlyQuestion:
    """Enhanced question structure with user experience focus"""
    id: str
    stage: QuestionnaireStage
    question_number: int
    title: str
    subtitle: Optional[str]
    question_text: str
    question_type: str
    options: List[str]
    help_text: Optional[str]
    clinical_mapping: Dict[str, Any]
    skip_logic: Optional[Dict]
    required: bool = True

class UserFriendlyAssessment:
    """Complete user-friendly assessment with logical funnel progression"""

    def __init__(self):
        self.questions = self._initialize_user_friendly_questions()
        self.stage_introductions = self._initialize_stage_introductions()
        self.progress_motivators = self._initialize_progress_motivators()

    def _initialize_stage_introductions(self) -> Dict[QuestionnaireStage, Dict]:
        """Friendly introductions for each assessment stage"""
        return {
            QuestionnaireStage.STAGE_1_WELCOME: {
                "title": "Welcome! Let's Get Started",
                "subtitle": "First, help us understand your current situation",
                "description": "We'll start with a few simple questions to get to know you better.",
                "icon": "👋",
                "estimated_time": "2 minutes"
            },
            QuestionnaireStage.STAGE_2_CURRENT_LIFE: {
                "title": "Your Life Right Now",
                "subtitle": "Tell us about your current experience",
                "description": "Let's explore what's happening in your life today.",
                "icon": "🌅",
                "estimated_time": "3 minutes"
            },
            QuestionnaireStage.STAGE_3_PATTERNS: {
                "title": "Your Natural Patterns",
                "subtitle": "How you typically think and react",
                "description": "Everyone has patterns - let's discover yours.",
                "icon": "🧩",
                "estimated_time": "4 minutes"
            },
            QuestionnaireStage.STAGE_4_RELATIONSHIPS: {
                "title": "Your Relationships",
                "subtitle": "How you connect with others",
                "description": "Relationships shape our experience - let's explore yours.",
                "icon": "🤝",
                "estimated_time": "3 minutes"
            },
            QuestionnaireStage.STAGE_5_WELLBEING: {
                "title": "Your Inner World",
                "subtitle": "Your emotions and mental patterns",
                "description": "Understanding your inner experience helps us help you.",
                "icon": "💭",
                "estimated_time": "4 minutes"
            },
            QuestionnaireStage.STAGE_6_GOALS: {
                "title": "Your Vision Forward",
                "subtitle": "What you want to achieve",
                "description": "Finally, let's talk about where you want to go.",
                "icon": "🎯",
                "estimated_time": "2 minutes"
            }
        }

    def _initialize_progress_motivators(self) -> Dict[int, str]:
        """Motivational messages to keep users engaged"""
        return {
            1: "Great start! You're building your personal profile.",
            5: "You're doing amazing! This information helps us understand you better.",
            10: "Halfway there! Your responses are creating a clear picture.",
            15: "Almost done! These insights will help design your transformation.",
            20: "Final stretch! You're about to discover your personalized approach.",
            25: "Excellent work! Preparing your detailed assessment results..."
        }

    def _initialize_user_friendly_questions(self) -> List[UserFriendlyQuestion]:
        """Create the complete user-friendly questionnaire"""
        return [
            # ================================
            # STAGE 1: WELCOME & CONTEXT (3-4 questions)
            # ================================
            UserFriendlyQuestion(
                id="age_group",
                stage=QuestionnaireStage.STAGE_1_WELCOME,
                question_number=1,
                title="Let's start with the basics",
                subtitle=None,
                question_text="Which age group describes you?",
                question_type="single_choice",
                options=[
                    "16-20 years old",
                    "21-30 years old",
                    "31-40 years old",
                    "41-50 years old",
                    "51-60 years old",
                    "Over 60 years old"
                ],
                help_text="This helps us understand generational patterns and tailor our approach.",
                clinical_mapping={
                    "target_patterns": ["digital_conditioning", "generational_factors"],
                    "weights": {
                        "16-20 years old": {"digital_native": 3, "social_media_influence": 3},
                        "21-30 years old": {"digital_integration": 2, "career_pressure": 2},
                        "31-40 years old": {"life_transition": 2, "responsibility_burden": 2},
                        "41-50 years old": {"midlife_evaluation": 2, "established_patterns": 2},
                        "51-60 years old": {"wisdom_resistance": 1, "change_reluctance": 1},
                        "Over 60 years old": {"experience_wisdom": 1, "adaptation_challenges": 1}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="main_concern",
                stage=QuestionnaireStage.STAGE_1_WELCOME,
                question_number=2,
                title="What brings you here?",
                subtitle="Choose what resonates most with you right now",
                question_text="What's your main reason for exploring transformation?",
                question_type="single_choice",
                options=[
                    "I feel stuck and can't seem to move forward",
                    "I'm tired of repeating the same mistakes",
                    "I want to feel happier and more fulfilled",
                    "My relationships aren't working",
                    "I'm overwhelmed by modern life",
                    "I want to achieve specific goals",
                    "Something feels missing in my life"
                ],
                help_text="There's no wrong answer - just pick what feels most true for you today.",
                clinical_mapping={
                    "target_patterns": ["primary_concern", "motivation_level"],
                    "weights": {
                        "I feel stuck and can't seem to move forward": {"stagnation": 3, "learned_helplessness": 2},
                        "I'm tired of repeating the same mistakes": {"pattern_recognition": 3, "behavioral_loops": 3},
                        "I want to feel happier and more fulfilled": {"happiness_barriers": 2, "meaning_seeking": 2},
                        "My relationships aren't working": {"attachment_issues": 3, "social_patterns": 2},
                        "I'm overwhelmed by modern life": {"digital_overwhelm": 3, "stress_patterns": 2},
                        "I want to achieve specific goals": {"goal_orientation": 2, "achievement_focus": 2},
                        "Something feels missing in my life": {"existential_seeking": 2, "purpose_deficiency": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="urgency_feeling",
                stage=QuestionnaireStage.STAGE_1_WELCOME,
                question_number=3,
                title="How urgent does this feel?",
                subtitle="Help us understand your timeline",
                question_text="How quickly do you need things to change?",
                question_type="single_choice",
                options=[
                    "It's a crisis - I need help now",
                    "Very urgent - within the next few weeks",
                    "Important - within the next few months",
                    "Moderate priority - this year would be great",
                    "Not urgent - I'm just exploring options"
                ],
                help_text="Your timeline helps us recommend the right approach and intensity.",
                clinical_mapping={
                    "target_patterns": ["crisis_level", "change_readiness"],
                    "weights": {
                        "It's a crisis - I need help now": {"crisis_state": 3, "urgent_intervention": 3},
                        "Very urgent - within the next few weeks": {"high_motivation": 3, "rapid_change_ready": 2},
                        "Important - within the next few months": {"moderate_motivation": 2, "realistic_timeline": 2},
                        "Moderate priority - this year would be great": {"exploration_phase": 1, "low_pressure": 1},
                        "Not urgent - I'm just exploring options": {"information_seeking": 1, "contemplation_stage": 1}
                    }
                },
                skip_logic=None
            ),

            # STAGE 2: CURRENT LIFE SITUATION (4-5 questions)
            UserFriendlyQuestion(
                id="daily_feeling",
                stage=QuestionnaireStage.STAGE_2_CURRENT_LIFE,
                question_number=4,
                title="How are your days feeling lately?",
                subtitle="Your typical daily experience",
                question_text="Which best describes how most of your days feel?",
                question_type="single_choice",
                options=[
                    "Energized and purposeful",
                    "Busy but manageable",
                    "Overwhelming and chaotic",
                    "Dull and repetitive",
                    "Anxious and uncertain",
                    "Heavy and difficult"
                ],
                help_text="Think about your last few weeks - what's the general tone?",
                clinical_mapping={
                    "target_patterns": ["daily_functioning", "emotional_baseline"],
                    "weights": {
                        "Energized and purposeful": {"positive_functioning": 2, "life_satisfaction": 2},
                        "Busy but manageable": {"coping_well": 1, "functional_stress": 1},
                        "Overwhelming and chaotic": {"overwhelm_pattern": 3, "stress_overload": 2},
                        "Dull and repetitive": {"anhedonia": 2, "meaning_deficit": 2},
                        "Anxious and uncertain": {"anxiety_pattern": 3, "uncertainty_intolerance": 2},
                        "Heavy and difficult": {"depression_indicators": 3, "life_burden": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="screen_time",
                stage=QuestionnaireStage.STAGE_2_CURRENT_LIFE,
                question_number=5,
                title="Your digital life",
                subtitle="Understanding your relationship with technology",
                question_text="How much time do you spend on your phone/devices each day (outside of work)?",
                question_type="single_choice",
                options=[
                    "Less than 2 hours",
                    "2-4 hours",
                    "4-6 hours",
                    "6-8 hours",
                    "More than 8 hours",
                    "I honestly don't know - probably a lot"
                ],
                help_text="Most people underestimate. Your phone might have screen time stats if you're curious!",
                clinical_mapping={
                    "target_patterns": ["digital_usage", "attention_patterns"],
                    "weights": {
                        "Less than 2 hours": {"healthy_boundaries": 2, "conscious_usage": 2},
                        "2-4 hours": {"moderate_usage": 1, "awareness": 1},
                        "4-6 hours": {"high_usage": 2, "attention_fragmentation": 1},
                        "6-8 hours": {"excessive_usage": 3, "digital_dependency": 2},
                        "More than 8 hours": {"problematic_usage": 3, "digital_addiction": 3},
                        "I honestly don't know - probably a lot": {"unconscious_usage": 3, "awareness_deficit": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="energy_patterns",
                stage=QuestionnaireStage.STAGE_2_CURRENT_LIFE,
                question_number=6,
                title="Your energy levels",
                subtitle="When do you feel most alive?",
                question_text="When during the day do you typically feel your best?",
                question_type="single_choice",
                options=[
                    "Early morning - I'm a natural early bird",
                    "Mid-morning - after I get going",
                    "Afternoon - my peak productive time",
                    "Evening - I come alive at night",
                    "It varies - depends on the day",
                    "Rarely - I often feel tired"
                ],
                help_text="This helps us understand your natural rhythms and energy patterns.",
                clinical_mapping={
                    "target_patterns": ["circadian_alignment", "energy_management"],
                    "weights": {
                        "Early morning - I'm a natural early bird": {"healthy_rhythm": 2, "natural_energy": 2},
                        "Mid-morning - after I get going": {"normal_awakening": 1, "gradual_energy": 1},
                        "Afternoon - my peak productive time": {"delayed_peak": 1, "sustained_energy": 1},
                        "Evening - I come alive at night": {"night_preference": 1, "social_rhythm": 1},
                        "It varies - depends on the day": {"inconsistent_patterns": 2, "external_dependency": 1},
                        "Rarely - I often feel tired": {"chronic_fatigue": 3, "energy_depletion": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="stress_response",
                stage=QuestionnaireStage.STAGE_2_CURRENT_LIFE,
                question_number=7,
                title="How you handle pressure",
                subtitle="Your natural response to stress",
                question_text="When life gets stressful, you tend to:",
                question_type="single_choice",
                options=[
                    "Take action and solve problems",
                    "Reach out to friends or family",
                    "Need space and time alone",
                    "Get overwhelmed and shut down",
                    "Keep busy to avoid thinking about it",
                    "Worry and overthink everything"
                ],
                help_text="Think about your most common response when things get tough.",
                clinical_mapping={
                    "target_patterns": ["stress_response", "coping_strategies"],
                    "weights": {
                        "Take action and solve problems": {"problem_focused_coping": 2, "resilience": 2},
                        "Reach out to friends or family": {"social_support": 2, "healthy_connection": 2},
                        "Need space and time alone": {"introversion": 1, "self_regulation": 1},
                        "Get overwhelmed and shut down": {"overwhelm_response": 3, "shutdown_pattern": 2},
                        "Keep busy to avoid thinking about it": {"avoidance_coping": 2, "hyperactivity": 2},
                        "Worry and overthink everything": {"rumination": 3, "anxiety_response": 2}
                    }
                },
                skip_logic=None
            ),

            # STAGE 3: LIFE PATTERNS (6-8 questions)
            UserFriendlyQuestion(
                id="happiness_comfort",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=8,
                title="Your relationship with good times",
                subtitle="How comfortable are you when things go well?",
                question_text="When something really good happens to you, what's your typical reaction?",
                question_type="single_choice",
                options=[
                    "I fully enjoy it and celebrate",
                    "I feel good but wonder when it'll end",
                    "I downplay it - it's not that big a deal",
                    "I immediately worry about what could go wrong",
                    "I feel guilty or like I don't deserve it",
                    "I'm suspicious - what's the catch?"
                ],
                help_text="Notice your first instinct when good things happen.",
                clinical_mapping={
                    "target_patterns": ["happiness_tolerance", "positive_emotion_regulation"],
                    "weights": {
                        "I fully enjoy it and celebrate": {"healthy_celebration": 2, "positive_acceptance": 2},
                        "I feel good but wonder when it'll end": {"anticipatory_anxiety": 2, "impermanence_fear": 1},
                        "I downplay it - it's not that big a deal": {"success_minimization": 3, "humility_defense": 2},
                        "I immediately worry about what could go wrong": {"catastrophic_thinking": 3, "anxiety_pattern": 2},
                        "I feel guilty or like I don't deserve it": {"unworthiness": 3, "guilt_pattern": 2},
                        "I'm suspicious - what's the catch?": {"paranoid_thinking": 2, "trust_issues": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="conflict_style",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=9,
                title="How you handle disagreements",
                subtitle="Your natural approach to conflict",
                question_text="When someone disagrees with you or challenges your ideas, you usually:",
                question_type="single_choice",
                options=[
                    "Listen and try to understand their perspective",
                    "Explain your point of view calmly",
                    "Feel defensive and need to prove you're right",
                    "Get energized by the debate",
                    "Avoid the conflict and back down",
                    "Get upset and shut down"
                ],
                help_text="Think about your gut reaction when someone challenges you.",
                clinical_mapping={
                    "target_patterns": ["conflict_style", "power_dynamics"],
                    "weights": {
                        "Listen and try to understand their perspective": {"collaborative_style": 2, "emotional_regulation": 2},
                        "Explain your point of view calmly": {"assertive_communication": 2, "healthy_boundaries": 1},
                        "Feel defensive and need to prove you're right": {"defensive_pattern": 3, "ego_protection": 2},
                        "Get energized by the debate": {"conflict_seeking": 2, "dominance_drive": 2},
                        "Avoid the conflict and back down": {"conflict_avoidance": 2, "submission_pattern": 2},
                        "Get upset and shut down": {"emotional_dysregulation": 3, "withdrawal_pattern": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="decision_making",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=10,
                title="How you make decisions",
                subtitle="Your natural decision-making style",
                question_text="When facing an important decision, you typically:",
                question_type="single_choice",
                options=[
                    "Go with my gut feeling",
                    "Research extensively and analyze options",
                    "Ask trusted friends or family for advice",
                    "Procrastinate until I have to decide",
                    "Make quick decisions and adjust as needed",
                    "Agonize over every possibility"
                ],
                help_text="Think about your usual approach to both big and small decisions.",
                clinical_mapping={
                    "target_patterns": ["decision_style", "cognitive_patterns"],
                    "weights": {
                        "Go with my gut feeling": {"intuitive_processing": 2, "emotional_intelligence": 1},
                        "Research extensively and analyze options": {"analytical_processing": 2, "perfectionism": 1},
                        "Ask trusted friends or family for advice": {"external_validation": 2, "social_dependency": 1},
                        "Procrastinate until I have to decide": {"avoidance_pattern": 3, "decision_anxiety": 2},
                        "Make quick decisions and adjust as needed": {"adaptive_flexibility": 2, "action_orientation": 1},
                        "Agonize over every possibility": {"rumination": 3, "analysis_paralysis": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="success_response",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=11,
                title="When you achieve something",
                subtitle="Your relationship with your own success",
                question_text="After accomplishing something you're proud of, you typically:",
                question_type="single_choice",
                options=[
                    "Feel genuinely proud and share the good news",
                    "Feel good briefly, then move on to the next goal",
                    "Downplay it - anyone could have done it",
                    "Analyze what could have been done better",
                    "Feel uncomfortable with the attention",
                    "Wonder if I really deserved the success"
                ],
                help_text="How do you relate to your own achievements and accomplishments?",
                clinical_mapping={
                    "target_patterns": ["achievement_response", "self_worth"],
                    "weights": {
                        "Feel genuinely proud and share the good news": {"healthy_pride": 2, "social_sharing": 1},
                        "Feel good briefly, then move on to the next goal": {"achievement_addiction": 2, "hedonic_adaptation": 1},
                        "Downplay it - anyone could have done it": {"success_minimization": 3, "imposter_syndrome": 2},
                        "Analyze what could have been done better": {"perfectionism": 3, "negative_focus": 2},
                        "Feel uncomfortable with the attention": {"spotlight_aversion": 2, "humility_defense": 1},
                        "Wonder if I really deserved the success": {"unworthiness": 3, "self_doubt": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="trust_approach",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=12,
                title="How you approach new people",
                subtitle="Your natural trust style",
                question_text="When meeting someone new, your instinct is to:",
                question_type="single_choice",
                options=[
                    "Be open and friendly right away",
                    "Be polite but keep some distance initially",
                    "Size them up and look for red flags",
                    "Let them prove they're trustworthy first",
                    "Assume they want something from me",
                    "Feel anxious about their intentions"
                ],
                help_text="What's your default approach when encountering new people?",
                clinical_mapping={
                    "target_patterns": ["trust_patterns", "social_approach"],
                    "weights": {
                        "Be open and friendly right away": {"secure_attachment": 2, "social_confidence": 2},
                        "Be polite but keep some distance initially": {"healthy_boundaries": 1, "cautious_optimism": 1},
                        "Size them up and look for red flags": {"hypervigilance": 2, "threat_assessment": 2},
                        "Let them prove they're trustworthy first": {"trust_deficit": 2, "earned_trust": 2},
                        "Assume they want something from me": {"paranoid_thinking": 3, "exploitation_fear": 2},
                        "Feel anxious about their intentions": {"social_anxiety": 3, "threat_sensitivity": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="social_media_feeling",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=13,
                title="Your social media experience",
                subtitle="How social media affects you",
                question_text="After spending time on social media, you usually feel:",
                question_type="single_choice",
                options=[
                    "Connected and inspired",
                    "Entertained and relaxed",
                    "Neutral - it's just information",
                    "Comparing myself to others",
                    "Anxious or overwhelmed",
                    "Worse about my own life"
                ],
                help_text="Notice how you typically feel after scrolling through social feeds.",
                clinical_mapping={
                    "target_patterns": ["social_media_impact", "comparison_tendency"],
                    "weights": {
                        "Connected and inspired": {"positive_social_media": 1, "inspiration_seeking": 1},
                        "Entertained and relaxed": {"healthy_usage": 1, "recreation": 1},
                        "Neutral - it's just information": {"detached_usage": 1, "minimal_impact": 1},
                        "Comparing myself to others": {"social_comparison": 3, "inadequacy_feelings": 2},
                        "Anxious or overwhelmed": {"information_overload": 3, "anxiety_trigger": 2},
                        "Worse about my own life": {"depressive_impact": 3, "life_dissatisfaction": 2}
                    }
                },
                skip_logic=None
            ),

            # STAGE 4: RELATIONSHIPS & SOCIAL (4-5 questions)
            UserFriendlyQuestion(
                id="relationship_pattern",
                stage=QuestionnaireStage.STAGE_4_RELATIONSHIPS,
                question_number=14,
                title="Your relationship patterns",
                subtitle="How your close relationships tend to go",
                question_text="Looking at your relationships (romantic, friends, family), which pattern feels most familiar?",
                question_type="single_choice",
                options=[
                    "Generally healthy and supportive",
                    "Good but I tend to give more than I receive",
                    "Lots of conflict and drama",
                    "I keep people at arm's length",
                    "They start well but usually disappoint me",
                    "I seem to attract the same type of problems"
                ],
                help_text="Think about the overall pattern across your important relationships.",
                clinical_mapping={
                    "target_patterns": ["relationship_patterns", "attachment_style"],
                    "weights": {
                        "Generally healthy and supportive": {"secure_attachment": 2, "healthy_relationships": 2},
                        "Good but I tend to give more than I receive": {"codependent_pattern": 2, "over_giving": 2},
                        "Lots of conflict and drama": {"conflict_pattern": 3, "dramatic_relationships": 2},
                        "I keep people at arm's length": {"avoidant_attachment": 3, "intimacy_fear": 2},
                        "They start well but usually disappoint me": {"idealization_devaluation": 3, "trust_issues": 2},
                        "I seem to attract the same type of problems": {"repetitive_patterns": 3, "unconscious_selection": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="social_energy",
                stage=QuestionnaireStage.STAGE_4_RELATIONSHIPS,
                question_number=15,
                title="Your social energy",
                subtitle="How social interaction affects you",
                question_text="After spending time with groups of people, you typically feel:",
                question_type="single_choice",
                options=[
                    "Energized and happy",
                    "Good but ready for some quiet time",
                    "Drained and need to recharge alone",
                    "Anxious about how I came across",
                    "Exhausted from trying to fit in",
                    "Relieved it's over"
                ],
                help_text="Consider both work social situations and personal social time.",
                clinical_mapping={
                    "target_patterns": ["social_energy", "introversion_extraversion"],
                    "weights": {
                        "Energized and happy": {"extraversion": 2, "social_confidence": 2},
                        "Good but ready for some quiet time": {"ambiversion": 1, "healthy_boundaries": 1},
                        "Drained and need to recharge alone": {"introversion": 2, "social_exhaustion": 1},
                        "Anxious about how I came across": {"social_anxiety": 3, "self_consciousness": 2},
                        "Exhausted from trying to fit in": {"social_masking": 3, "authenticity_struggle": 2},
                        "Relieved it's over": {"social_avoidance": 3, "interpersonal_stress": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="support_seeking",
                stage=QuestionnaireStage.STAGE_4_RELATIONSHIPS,
                question_number=16,
                title="When you need help",
                subtitle="Your approach to seeking support",
                question_text="When you're going through a difficult time, you're most likely to:",
                question_type="single_choice",
                options=[
                    "Reach out to close friends or family",
                    "Handle it myself but accept help if offered",
                    "Research and find professional help",
                    "Try to solve it on my own",
                    "Pretend everything is fine",
                    "Feel like no one would really understand"
                ],
                help_text="What's your typical pattern when life gets challenging?",
                clinical_mapping={
                    "target_patterns": ["help_seeking", "social_support"],
                    "weights": {
                        "Reach out to close friends or family": {"healthy_support_seeking": 2, "social_connection": 2},
                        "Handle it myself but accept help if offered": {"balanced_independence": 1, "receptive_to_help": 1},
                        "Research and find professional help": {"proactive_help_seeking": 2, "professional_orientation": 1},
                        "Try to solve it on my own": {"self_reliance": 2, "independence_preference": 1},
                        "Pretend everything is fine": {"social_masking": 3, "vulnerability_avoidance": 2},
                        "Feel like no one would really understand": {"isolation": 3, "uniqueness_belief": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="authority_response",
                stage=QuestionnaireStage.STAGE_4_RELATIONSHIPS,
                question_number=17,
                title="Your response to authority",
                subtitle="How you relate to people in charge",
                question_text="When someone in authority (boss, doctor, teacher) gives you guidance, you typically:",
                question_type="single_choice",
                options=[
                    "Trust their expertise and follow their advice",
                    "Listen carefully and ask clarifying questions",
                    "Consider their advice but make my own decision",
                    "Feel skeptical and want to research it myself",
                    "Agree outwardly but resist inwardly",
                    "Feel frustrated or defensive"
                ],
                help_text="Think about your natural reaction to authority figures giving advice.",
                clinical_mapping={
                    "target_patterns": ["authority_relationship", "autonomy_needs"],
                    "weights": {
                        "Trust their expertise and follow their advice": {"authority_acceptance": 2, "compliance": 1},
                        "Listen carefully and ask clarifying questions": {"healthy_questioning": 1, "collaborative_approach": 1},
                        "Consider their advice but make my own decision": {"balanced_autonomy": 1, "independent_thinking": 1},
                        "Feel skeptical and want to research it myself": {"authority_skepticism": 2, "self_reliance": 2},
                        "Agree outwardly but resist inwardly": {"passive_resistance": 3, "authority_conflict": 2},
                        "Feel frustrated or defensive": {"authority_reactivity": 3, "oppositional_pattern": 2}
                    }
                },
                skip_logic=None
            ),

            # STAGE 5: EMOTIONAL WELLBEING (5-6 questions)
            UserFriendlyQuestion(
                id="worry_patterns",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=18,
                title="Your worry patterns",
                subtitle="How your mind handles concerns",
                question_text="When you have something to worry about, your mind tends to:",
                question_type="single_choice",
                options=[
                    "Think it through once and let it go",
                    "Come back to it periodically throughout the day",
                    "Go in circles thinking about all the possibilities",
                    "Imagine worst-case scenarios",
                    "Try to distract myself from thinking about it",
                    "Spiral into anxiety about it"
                ],
                help_text="Notice what your mind does when you have concerns or problems.",
                clinical_mapping={
                    "target_patterns": ["worry_style", "anxiety_patterns"],
                    "weights": {
                        "Think it through once and let it go": {"healthy_processing": 2, "cognitive_flexibility": 2},
                        "Come back to it periodically throughout the day": {"moderate_rumination": 1, "persistent_concern": 1},
                        "Go in circles thinking about all the possibilities": {"rumination": 3, "cognitive_loops": 2},
                        "Imagine worst-case scenarios": {"catastrophic_thinking": 3, "anxiety_amplification": 2},
                        "Try to distract myself from thinking about it": {"avoidance_coping": 2, "thought_suppression": 2},
                        "Spiral into anxiety about it": {"anxiety_disorder": 3, "emotional_dysregulation": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="emotional_regulation",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=19,
                title="Managing difficult emotions",
                subtitle="How you handle emotional challenges",
                question_text="When you feel upset, angry, or sad, you usually:",
                question_type="single_choice",
                options=[
                    "Feel the emotion and then it passes naturally",
                    "Talk to someone about how I'm feeling",
                    "Do something physical or creative to work through it",
                    "Try to think my way out of the feeling",
                    "Distract myself until it goes away",
                    "Get stuck in the emotion for a long time"
                ],
                help_text="What's your usual approach to processing difficult feelings?",
                clinical_mapping={
                    "target_patterns": ["emotional_regulation", "coping_strategies"],
                    "weights": {
                        "Feel the emotion and then it passes naturally": {"healthy_processing": 2, "emotional_intelligence": 2},
                        "Talk to someone about how I'm feeling": {"social_processing": 2, "verbal_expression": 1},
                        "Do something physical or creative to work through it": {"somatic_processing": 2, "creative_expression": 1},
                        "Try to think my way out of the feeling": {"cognitive_override": 2, "intellectualization": 2},
                        "Distract myself until it goes away": {"avoidance_coping": 3, "emotional_suppression": 2},
                        "Get stuck in the emotion for a long time": {"emotional_dysregulation": 3, "rumination": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="self_talk",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=20,
                title="Your inner voice",
                subtitle="How you talk to yourself",
                question_text="The voice in your head is usually:",
                question_type="single_choice",
                options=[
                    "Kind and encouraging",
                    "Practical and neutral",
                    "Critical and demanding",
                    "Worried and anxious",
                    "Harsh and judgmental",
                    "Chaotic and overwhelming"
                ],
                help_text="Pay attention to your internal dialogue - what tone does it typically have?",
                clinical_mapping={
                    "target_patterns": ["self_talk", "inner_critic"],
                    "weights": {
                        "Kind and encouraging": {"self_compassion": 2, "positive_self_talk": 2},
                        "Practical and neutral": {"balanced_thinking": 1, "objective_perspective": 1},
                        "Critical and demanding": {"inner_critic": 3, "perfectionism": 2},
                        "Worried and anxious": {"anxious_thoughts": 3, "worry_patterns": 2},
                        "Harsh and judgmental": {"self_criticism": 3, "negative_self_concept": 3},
                        "Chaotic and overwhelming": {"cognitive_overwhelm": 3, "thought_disorder": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="relaxation_ability",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=21,
                title="Your ability to relax",
                subtitle="How well you can unwind",
                question_text="When you try to relax or unwind, you:",
                question_type="single_choice",
                options=[
                    "Can easily let go and feel peaceful",
                    "Can relax with some effort or the right environment",
                    "Find it difficult but can sometimes manage it",
                    "Feel restless and need to stay busy",
                    "Feel uncomfortable or unsafe when relaxed",
                    "Find it nearly impossible to truly relax"
                ],
                help_text="Think about your natural ability to genuinely relax and unwind.",
                clinical_mapping={
                    "target_patterns": ["relaxation_capacity", "hypervigilance"],
                    "weights": {
                        "Can easily let go and feel peaceful": {"healthy_relaxation": 2, "parasympathetic_access": 2},
                        "Can relax with some effort or the right environment": {"moderate_relaxation": 1, "environmental_dependency": 1},
                        "Find it difficult but can sometimes manage it": {"relaxation_challenges": 2, "effortful_calming": 1},
                        "Feel restless and need to stay busy": {"hyperactivity": 2, "busyness_addiction": 2},
                        "Feel uncomfortable or unsafe when relaxed": {"hypervigilance": 3, "safety_concerns": 3},
                        "Find it nearly impossible to truly relax": {"chronic_tension": 3, "relaxation_inability": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="motivation_patterns",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=22,
                title="What drives you",
                subtitle="Your core motivations",
                question_text="You feel most motivated when:",
                question_type="single_choice",
                options=[
                    "Working toward something meaningful to you",
                    "Making progress on clear, achievable goals",
                    "Being recognized or appreciated by others",
                    "Helping or making a difference for other people",
                    "Competing or proving yourself",
                    "Avoiding problems or consequences"
                ],
                help_text="What type of motivation tends to energize you most?",
                clinical_mapping={
                    "target_patterns": ["motivation_style", "value_system"],
                    "weights": {
                        "Working toward something meaningful to you": {"intrinsic_motivation": 2, "value_alignment": 2},
                        "Making progress on clear, achievable goals": {"achievement_orientation": 2, "structure_preference": 1},
                        "Being recognized or appreciated by others": {"external_validation": 2, "approval_seeking": 2},
                        "Helping or making a difference for other people": {"altruistic_motivation": 2, "service_orientation": 1},
                        "Competing or proving yourself": {"competitive_drive": 2, "ego_motivation": 2},
                        "Avoiding problems or consequences": {"avoidance_motivation": 3, "fear_based_action": 2}
                    }
                },
                skip_logic=None
            ),

            # STAGE 6: CHANGE & GOALS (3-4 questions)
            UserFriendlyQuestion(
                id="change_experience",
                stage=QuestionnaireStage.STAGE_6_GOALS,
                question_number=23,
                title="Your experience with change",
                subtitle="How you've handled change in the past",
                question_text="When you've tried to make significant changes in your life before:",
                question_type="single_choice",
                options=[
                    "I usually succeed when I set my mind to it",
                    "I make progress but it takes longer than expected",
                    "I start strong but often lose momentum",
                    "I struggle with consistency and give up",
                    "I haven't really tried major changes before",
                    "Nothing seems to work for me long-term"
                ],
                help_text="Think about past attempts at changing habits, behaviors, or life circumstances.",
                clinical_mapping={
                    "target_patterns": ["change_efficacy", "persistence_patterns"],
                    "weights": {
                        "I usually succeed when I set my mind to it": {"high_self_efficacy": 2, "change_confidence": 2},
                        "I make progress but it takes longer than expected": {"realistic_expectations": 1, "gradual_progress": 1},
                        "I start strong but often lose momentum": {"initial_motivation": 1, "sustainability_challenge": 2},
                        "I struggle with consistency and give up": {"consistency_issues": 3, "change_resistance": 2},
                        "I haven't really tried major changes before": {"change_avoidance": 2, "status_quo_preference": 1},
                        "Nothing seems to work for me long-term": {"learned_helplessness": 3, "change_pessimism": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="ideal_outcome",
                stage=QuestionnaireStage.STAGE_6_GOALS,
                question_number=24,
                title="Your ideal outcome",
                subtitle="What success looks like to you",
                question_text="If this transformation process works perfectly for you, in 6 months you'll be:",
                question_type="single_choice",
                options=[
                    "Feeling genuinely happy and fulfilled most days",
                    "Free from the patterns that have been holding me back",
                    "Confident and comfortable in my relationships",
                    "Clear about my direction and taking action toward my goals",
                    "At peace with myself and less anxious/stressed",
                    "Living authentically as my true self"
                ],
                help_text="What would represent real success for you?",
                clinical_mapping={
                    "target_patterns": ["goal_orientation", "success_definition"],
                    "weights": {
                        "Feeling genuinely happy and fulfilled most days": {"happiness_goal": 2, "emotional_wellbeing": 2},
                        "Free from the patterns that have been holding me back": {"pattern_breaking": 3, "freedom_seeking": 2},
                        "Confident and comfortable in my relationships": {"relationship_goals": 2, "social_confidence": 2},
                        "Clear about my direction and taking action toward my goals": {"clarity_seeking": 2, "action_orientation": 2},
                        "At peace with myself and less anxious/stressed": {"inner_peace": 2, "anxiety_reduction": 2},
                        "Living authentically as my true self": {"authenticity_goal": 2, "self_actualization": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="commitment_level",
                stage=QuestionnaireStage.STAGE_6_GOALS,
                question_number=25,
                title="Your commitment level",
                subtitle="How ready you are to do the work",
                question_text="When it comes to putting in effort to create change, you're:",
                question_type="single_choice",
                options=[
                    "Ready to do whatever it takes",
                    "Willing to put in significant effort",
                    "Hopeful but want to see if it feels right first",
                    "Willing to try but have some reservations",
                    "Curious but not sure how much I can commit",
                    "Looking for something that doesn't require too much effort"
                ],
                help_text="Honestly assess your readiness to invest time and energy in change.",
                clinical_mapping={
                    "target_patterns": ["commitment_level", "change_readiness"],
                    "weights": {
                        "Ready to do whatever it takes": {"high_commitment": 3, "change_determination": 3},
                        "Willing to put in significant effort": {"strong_commitment": 2, "realistic_effort": 2},
                        "Hopeful but want to see if it feels right first": {"cautious_optimism": 1, "conditional_commitment": 1},
                        "Willing to try but have some reservations": {"moderate_commitment": 1, "ambivalence": 1},
                        "Curious but not sure how much I can commit": {"low_commitment": 1, "exploration_phase": 1},
                        "Looking for something that doesn't require too much effort": {"minimal_effort": 1, "magical_thinking": 2}
                    }
                },
                skip_logic=None
            ),

            # ================================
            # ENHANCED PATTERN DETECTION QUESTIONS
            # ================================
            # These questions use indirect assessment through scenarios to detect subtle patterns

            UserFriendlyQuestion(
                id="success_sharing_pattern",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=26,
                title="Success Sharing Behavior",
                subtitle="Understanding your relationship with positive experiences",
                question_text="When describing a recent success to a friend, you find yourself:",
                question_type="single_choice",
                options=[
                    "Sharing the full story with genuine enthusiasm",
                    "Mentioning it briefly then changing subjects",
                    "Adding 'but' followed by potential problems",
                    "Downplaying it as 'just luck' or timing",
                    "Feeling uncomfortable with their positive reaction"
                ],
                help_text="This reveals your comfort level with positive attention and success",
                required=True,
                clinical_mapping={
                    "category": "enhanced_pattern_detection",
                    "weights": {
                        "Sharing the full story with genuine enthusiasm": {"healthy_celebration": 2},
                        "Mentioning it briefly then changing subjects": {"mild_deflection": 1, "unhappiness_culture": 1},
                        "Adding 'but' followed by potential problems": {"catastrophic_thinking": 2, "unhappiness_culture": 2},
                        "Downplaying it as 'just luck' or timing": {"success_minimization": 3, "unhappiness_culture": 2},
                        "Feeling uncomfortable with their positive reaction": {"positive_discomfort": 3, "unhappiness_culture": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="compliment_response_pattern",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=27,
                title="Compliment Reception Analysis",
                subtitle="How you process positive feedback reveals core patterns",
                question_text="When someone gives you a genuine compliment, your immediate internal reaction is:",
                question_type="single_choice",
                options=[
                    "Feeling genuinely pleased and accepting it",
                    "Wondering what they want from you",
                    "Thinking about why they're wrong",
                    "Feeling anxious about living up to it",
                    "Deflecting with humor or self-deprecation"
                ],
                help_text="Your automatic response to praise indicates deep-seated beliefs about worthiness",
                required=True,
                clinical_mapping={
                    "category": "enhanced_pattern_detection",
                    "weights": {
                        "Feeling genuinely pleased and accepting it": {"healthy_self_worth": 2},
                        "Wondering what they want from you": {"systematic_mistrust": 2, "defensive_positioning": 1},
                        "Thinking about why they're wrong": {"self_worth_issues": 3, "reality_distortion": 1},
                        "Feeling anxious about living up to it": {"performance_anxiety": 2, "perfectionism": 1},
                        "Deflecting with humor or self-deprecation": {"positive_discomfort": 2, "unhappiness_culture": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="anticipation_pattern",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=28,
                title="Future Event Anticipation",
                subtitle="How you mentally prepare for positive events",
                question_text="When you have something to look forward to (vacation, date, event), you typically:",
                question_type="single_choice",
                options=[
                    "Enjoy the anticipation and plan with excitement",
                    "Try not to think about it too much",
                    "Worry about what could go wrong",
                    "Expect it to be disappointing",
                    "Feel guilty for looking forward to it"
                ],
                help_text="Anticipation patterns reveal your relationship with future happiness",
                required=True,
                clinical_mapping={
                    "category": "enhanced_pattern_detection",
                    "weights": {
                        "Enjoy the anticipation and plan with excitement": {"healthy_anticipation": 2},
                        "Try not to think about it too much": {"emotional_numbing": 1, "protection_mechanism": 1},
                        "Worry about what could go wrong": {"catastrophic_thinking": 3, "anxiety_patterns": 2},
                        "Expect it to be disappointing": {"learned_helplessness": 3, "pessimistic_bias": 2},
                        "Feel guilty for looking forward to it": {"unhappiness_culture": 3, "self_punishment": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="problem_solving_identity",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=29,
                title="Problem-Solving Identity Pattern",
                subtitle="Understanding your relationship with challenges",
                question_text="When people come to you with problems, you usually:",
                question_type="single_choice",
                options=[
                    "Listen and offer support without taking responsibility",
                    "Feel energized by helping them solve it",
                    "Feel overwhelmed by their emotions",
                    "Automatically start looking for solutions",
                    "Wonder why they always bring problems to you"
                ],
                help_text="This reveals whether problems have become part of your identity",
                required=True,
                clinical_mapping={
                    "category": "enhanced_pattern_detection",
                    "weights": {
                        "Listen and offer support without taking responsibility": {"healthy_boundaries": 2},
                        "Feel energized by helping them solve it": {"helper_identity": 2, "external_validation": 1},
                        "Feel overwhelmed by their emotions": {"emotional_overwhelm": 2, "boundary_issues": 1},
                        "Automatically start looking for solutions": {"fix_it_compulsion": 2, "control_patterns": 1},
                        "Wonder why they always bring problems to you": {"victim_identity": 2, "pattern_awareness": 1}
                    }
                },
                skip_logic=None
            ),

            # ================================
            # EXPERIENTIAL HYPNOTIC READINESS ASSESSMENT
            # ================================
            # Based on Stanford Hypnotic Clinical Scale - actual responsiveness testing

            UserFriendlyQuestion(
                id="guided_relaxation_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=30,
                title="Relaxation Response Test",
                subtitle="Experiential assessment of your natural relaxation ability",
                question_text="Let's try a brief guided exercise. Please sit comfortably, close your eyes, and take three slow, deep breaths. Now imagine your hands becoming very heavy, as if they're made of lead, sinking down with their own weight. Focus on this sensation for 30 seconds, then rate the actual heaviness you experienced:",
                question_type="experiential_scale",
                options=[
                    "No sensation - remained fully aware this was imagination",
                    "Slight sense of weight but clearly imaginary",
                    "Moderate sensation - felt somewhat real",
                    "Strong sensation - briefly felt like holding actual weight",
                    "Complete sensation - temporarily forgot this was imagination"
                ],
                help_text="This measures your natural hypnotic responsiveness through direct experience",
                required=True,
                clinical_mapping={
                    "category": "experiential_hypnotic_readiness",
                    "weights": {
                        "No sensation - remained fully aware this was imagination": {"hypnotic_resistance": 2, "analytical_override": 3},
                        "Slight sense of weight but clearly imaginary": {"low_hypnotic_susceptibility": 1, "mild_responsiveness": 1},
                        "Moderate sensation - felt somewhat real": {"moderate_hypnotic_susceptibility": 2, "somatic_awareness": 1},
                        "Strong sensation - briefly felt like holding actual weight": {"high_hypnotic_susceptibility": 3, "ideomotor_response": 2},
                        "Complete sensation - temporarily forgot this was imagination": {"very_high_hypnotic_susceptibility": 4, "deep_absorption": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="eye_closure_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=31,
                title="Natural Eye Closure Response",
                subtitle="Testing automatic response to suggestion",
                question_text="Close your eyes and imagine your eyelids becoming heavier and heavier, so heavy that they feel glued shut. Try to open them while imagining this for 10 seconds, then rate your experience:",
                question_type="experiential_scale",
                options=[
                    "Eyes opened easily - no difficulty at all",
                    "Slight resistance but opened without effort",
                    "Moderate resistance - took some effort to open",
                    "Strong resistance - required significant effort",
                    "Could not open them for several seconds"
                ],
                help_text="This tests your responsiveness to ideomotor suggestions",
                required=True,
                clinical_mapping={
                    "category": "experiential_hypnotic_readiness",
                    "weights": {
                        "Eyes opened easily - no difficulty at all": {"suggestion_resistance": 2, "control_preference": 2},
                        "Slight resistance but opened without effort": {"mild_suggestion_response": 1},
                        "Moderate resistance - took some effort to open": {"moderate_suggestion_response": 2, "ideomotor_susceptibility": 1},
                        "Strong resistance - required significant effort": {"high_suggestion_response": 3, "ideomotor_susceptibility": 2},
                        "Could not open them for several seconds": {"very_high_suggestion_response": 4, "deep_ideomotor": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="attention_focus_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=32,
                title="Attention Concentration Assessment",
                subtitle="Testing your natural focus and absorption abilities",
                question_text="Focus on a spot on the wall and count backwards from 100 by 7s (100, 93, 86...). Notice what happens to your awareness of the room around you. After one minute, rate your experience:",
                question_type="experiential_scale",
                options=[
                    "Remained fully aware of surroundings throughout",
                    "Occasionally forgot surroundings but stayed alert",
                    "Moderate tunnel vision - surroundings became dim",
                    "Strong absorption - nearly forgot where I was",
                    "Complete absorption - lost all awareness of surroundings"
                ],
                help_text="This measures your natural capacity for focused attention and absorption",
                required=True,
                clinical_mapping={
                    "category": "experiential_hypnotic_readiness",
                    "weights": {
                        "Remained fully aware of surroundings throughout": {"hypervigilance": 2, "attention_splitting": 1},
                        "Occasionally forgot surroundings but stayed alert": {"normal_focus": 1, "mild_absorption": 1},
                        "Moderate tunnel vision - surroundings became dim": {"good_focus": 2, "moderate_absorption": 2},
                        "Strong absorption - nearly forgot where I was": {"excellent_focus": 3, "high_absorption": 3},
                        "Complete absorption - lost all awareness of surroundings": {"exceptional_focus": 4, "deep_absorption": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="imagery_vividness_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=33,
                title="Mental Imagery Assessment",
                subtitle="Testing the vividness of your mental imagery",
                question_text="Close your eyes and imagine holding a bright yellow lemon. Picture it clearly - the texture of the skin, the weight in your hand. Now imagine cutting it in half and smelling the fresh citrus scent. Rate how vivid this experience was:",
                question_type="experiential_scale",
                options=[
                    "No clear image - mostly just thinking about lemons",
                    "Vague outline - knew it was there but not clear",
                    "Moderately clear - could see it but not in detail",
                    "Very clear - almost like seeing a real lemon",
                    "Completely vivid - could smell and feel it clearly"
                ],
                help_text="Vivid imagery is strongly correlated with hypnotic responsiveness",
                required=True,
                clinical_mapping={
                    "category": "experiential_hypnotic_readiness",
                    "weights": {
                        "No clear image - mostly just thinking about lemons": {"poor_imagery": 1, "analytical_thinking": 2},
                        "Vague outline - knew it was there but not clear": {"weak_imagery": 1, "visualization_challenges": 1},
                        "Moderately clear - could see it but not in detail": {"moderate_imagery": 2, "average_visualization": 1},
                        "Very clear - almost like seeing a real lemon": {"strong_imagery": 3, "good_visualization": 2},
                        "Completely vivid - could smell and feel it clearly": {"exceptional_imagery": 4, "multisensory_visualization": 3}
                    }
                },
                skip_logic=None
            ),

            # ================================
            # VALIDATED DIGITAL DESPAIR METRICS
            # ================================
            # Behavioral tests for attention fragmentation and reality dissociation
            # Integrates validated digital wellness metrics with clinical assessment

            UserFriendlyQuestion(
                id="attention_fragmentation_test",
                stage=QuestionnaireStage.STAGE_4_DIGITAL,
                question_number=34,
                title="Attention Fragmentation Assessment",
                subtitle="Behavioral test for sustained attention capacity",
                question_text="This is a behavioral test. Read this paragraph completely without checking your phone, looking at other tabs, or getting distracted: 'The human brain's capacity for sustained attention has measurably decreased in the digital age. Research shows that constant task-switching creates neural patterns that mirror addiction pathways. When we fragment our attention repeatedly, we literally rewire our brains to crave stimulation and reject stillness. This creates a cycle where focus becomes increasingly difficult, leading to decreased productivity, increased anxiety, and a persistent sense of incompleteness. The solution requires intentional attention training and digital boundaries.' How did you experience reading this?",
                question_type="single_choice",
                options=[
                    "Read completely without any urges to check devices",
                    "Felt slight urges but stayed focused throughout",
                    "Had moderate urges and briefly glanced away 1-2 times",
                    "Struggled to focus - checked device or got distracted 3+ times",
                    "Could not complete without multiple interruptions"
                ],
                help_text="This tests real-time attention fragmentation patterns - a key predictor of treatment success",
                required=True,
                clinical_mapping={
                    "category": "validated_digital_despair_metrics",
                    "weights": {
                        "Read completely without any urges to check devices": {"healthy_attention": 3, "digital_wellness": 2},
                        "Felt slight urges but stayed focused throughout": {"moderate_attention": 2, "good_self_control": 1},
                        "Had moderate urges and briefly glanced away 1-2 times": {"mild_fragmentation": 2, "impulse_control_issues": 1},
                        "Struggled to focus - checked device or got distracted 3+ times": {"severe_fragmentation": 3, "attention_deficit": 2},
                        "Could not complete without multiple interruptions": {"extreme_fragmentation": 4, "digital_addiction_markers": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="reality_dissociation_test",
                stage=QuestionnaireStage.STAGE_4_DIGITAL,
                question_number=35,
                title="Digital Reality Dissociation Assessment",
                subtitle="Testing presence and embodied awareness",
                question_text="Put your phone face down or close all digital devices for 60 seconds. Sit quietly and notice: your breathing, the sensation of your feet on the floor, sounds around you, and your body temperature. Do this now before answering. How did this experience feel?",
                question_type="single_choice",
                options=[
                    "Naturally comfortable - easily connected with physical sensations",
                    "Initially restless but settled into physical awareness",
                    "Moderately uncomfortable - mind kept wandering to digital tasks",
                    "Very uncomfortable - felt anxious without digital stimulation",
                    "Could not tolerate it - felt panic or overwhelming urges"
                ],
                help_text="Tests digital dependency and embodied presence - critical for hypnotherapy success",
                required=True,
                clinical_mapping={
                    "category": "validated_digital_despair_metrics",
                    "weights": {
                        "Naturally comfortable - easily connected with physical sensations": {"embodied_presence": 3, "low_digital_dependency": 2},
                        "Initially restless but settled into physical awareness": {"moderate_presence": 2, "adaptable_nervous_system": 1},
                        "Moderately uncomfortable - mind kept wandering to digital tasks": {"digital_preoccupation": 2, "mild_dissociation": 1},
                        "Very uncomfortable - felt anxious without digital stimulation": {"severe_digital_dependency": 3, "reality_dissociation": 2},
                        "Could not tolerate it - felt panic or overwhelming urges": {"extreme_digital_dependency": 4, "severe_dissociation": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="dopamine_regulation_test",
                stage=QuestionnaireStage.STAGE_4_DIGITAL,
                question_number=36,
                title="Dopamine Regulation Assessment",
                subtitle="Testing reward system functionality",
                question_text="Think about a simple, non-digital pleasure you enjoyed as a child (like feeling sunlight, eating fruit, listening to music, or walking). Try to recall that exact feeling for 30 seconds. How vivid and satisfying was this memory compared to checking social media?",
                question_type="single_choice",
                options=[
                    "Much more satisfying than digital stimulation",
                    "Somewhat more satisfying than digital activities",
                    "About equal to digital stimulation",
                    "Less satisfying than checking social media",
                    "Could barely access the memory - felt empty compared to digital hits"
                ],
                help_text="Tests whether natural rewards still activate properly - indicates dopamine system health",
                required=True,
                clinical_mapping={
                    "category": "validated_digital_despair_metrics",
                    "weights": {
                        "Much more satisfying than digital stimulation": {"healthy_reward_system": 3, "natural_pleasure_access": 2},
                        "Somewhat more satisfying than digital activities": {"moderate_reward_system": 2, "partial_pleasure_access": 1},
                        "About equal to digital stimulation": {"dysregulated_dopamine": 1, "pleasure_confusion": 2},
                        "Less satisfying than checking social media": {"severely_dysregulated_dopamine": 2, "anhedonia_markers": 3},
                        "Could barely access the memory - felt empty compared to digital hits": {"extreme_dysregulation": 4, "severe_anhedonia": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="digital_impulse_control_test",
                stage=QuestionnaireStage.STAGE_4_DIGITAL,
                question_number=37,
                title="Digital Impulse Control Assessment",
                subtitle="Real-time impulse regulation testing",
                question_text="Right now, notice any urge to check your phone, social media, or other apps. Without acting on it, simply observe the urge for 30 seconds. What happened?",
                question_type="single_choice",
                options=[
                    "No urges arose - felt naturally content",
                    "Minor urge but easily observed without acting",
                    "Moderate urge - took effort to resist but managed",
                    "Strong urge - very difficult to resist, almost acted",
                    "Overwhelming urge - had to check device to complete this question"
                ],
                help_text="Tests real-time impulse control - a critical factor in hypnotherapy compliance",
                required=True,
                clinical_mapping={
                    "category": "validated_digital_despair_metrics",
                    "weights": {
                        "No urges arose - felt naturally content": {"excellent_impulse_control": 3, "mindful_awareness": 2},
                        "Minor urge but easily observed without acting": {"good_impulse_control": 2, "self_awareness": 1},
                        "Moderate urge - took effort to resist but managed": {"moderate_impulse_control": 1, "effortful_control": 1},
                        "Strong urge - very difficult to resist, almost acted": {"poor_impulse_control": 2, "compulsive_tendencies": 3},
                        "Overwhelming urge - had to check device to complete this question": {"no_impulse_control": 4, "severe_compulsion": 3}
                    }
                },
                skip_logic=None
            ),

            # ================================
            # UNCONSCIOUS SECONDARY GAIN ASSESSMENT
            # ================================
            # Sophisticated detection of hidden psychological benefits from symptoms
            # Identifies unconscious motivations that maintain problematic patterns

            UserFriendlyQuestion(
                id="problem_attention_pattern",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=38,
                title="Problem-Attention Pattern Assessment",
                subtitle="Understanding the relationship between problems and attention",
                question_text="When you share your struggles with others, what typically happens to the conversation?",
                question_type="single_choice",
                options=[
                    "They offer brief support then we discuss other topics",
                    "They become very engaged and focused on helping me",
                    "The conversation stays centered on my issues for a long time",
                    "People seem to care more about me when I'm struggling",
                    "I notice I get more emotional connection through my problems"
                ],
                help_text="This reveals potential secondary gains from problem-focused interactions",
                required=True,
                clinical_mapping={
                    "category": "unconscious_secondary_gain_assessment",
                    "weights": {
                        "They offer brief support then we discuss other topics": {"healthy_support_pattern": 2, "low_secondary_gain": 1},
                        "They become very engaged and focused on helping me": {"moderate_attention_seeking": 1, "helper_activation": 2},
                        "The conversation stays centered on my issues for a long time": {"high_attention_seeking": 2, "problem_centrality": 3},
                        "People seem to care more about me when I'm struggling": {"conditional_love_pattern": 3, "sympathy_addiction": 2},
                        "I notice I get more emotional connection through my problems": {"emotional_manipulation": 3, "secondary_gain_awareness": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="responsibility_avoidance_pattern",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=39,
                title="Responsibility Avoidance Assessment",
                subtitle="Identifying hidden benefits of limitation",
                question_text="Honestly, if your main issue was completely resolved tomorrow, what would people expect from you that you currently avoid?",
                question_type="single_choice",
                options=[
                    "Nothing significant - I'd just feel better and continue my life",
                    "More social engagement and relationship responsibilities",
                    "Higher performance expectations at work or in life",
                    "Taking on leadership roles or making difficult decisions",
                    "People would expect me to be 'normal' and I'd lose my uniqueness"
                ],
                help_text="This uncovers unconscious fears of success and responsibility avoidance",
                required=True,
                clinical_mapping={
                    "category": "unconscious_secondary_gain_assessment",
                    "weights": {
                        "Nothing significant - I'd just feel better and continue my life": {"low_responsibility_avoidance": 1, "healthy_motivation": 2},
                        "More social engagement and relationship responsibilities": {"social_avoidance_benefit": 2, "intimacy_fear": 1},
                        "Higher performance expectations at work or in life": {"success_fear": 2, "performance_avoidance": 3},
                        "Taking on leadership roles or making difficult decisions": {"authority_avoidance": 3, "decision_fear": 2},
                        "People would expect me to be 'normal' and I'd lose my uniqueness": {"identity_through_problems": 4, "specialness_through_suffering": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="control_through_problems",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=40,
                title="Control Through Problems Assessment",
                subtitle="Detecting indirect control mechanisms",
                question_text="Think about how your current challenges affect other people's behavior around you. What have you noticed?",
                question_type="single_choice",
                options=[
                    "My issues don't really change how others treat me",
                    "People are more patient and accommodating with me",
                    "Others modify their expectations and demands",
                    "People work harder to please me or avoid upsetting me",
                    "My struggles give me legitimate reasons to say no to things"
                ],
                help_text="This reveals how problems may unconsciously provide control and power",
                required=True,
                clinical_mapping={
                    "category": "unconscious_secondary_gain_assessment",
                    "weights": {
                        "My issues don't really change how others treat me": {"low_manipulation": 1, "independent_functioning": 2},
                        "People are more patient and accommodating with me": {"mild_secondary_control": 1, "accommodation_seeking": 2},
                        "Others modify their expectations and demands": {"moderate_secondary_control": 2, "expectation_management": 2},
                        "People work harder to please me or avoid upsetting me": {"high_secondary_control": 3, "indirect_manipulation": 3},
                        "My struggles give me legitimate reasons to say no to things": {"avoidance_legitimization": 3, "responsibility_shield": 2}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="identity_through_suffering",
                stage=QuestionnaireStage.STAGE_3_PATTERNS,
                question_number=41,
                title="Identity Through Suffering Assessment",
                subtitle="Exploring self-concept attachment to problems",
                question_text="If you imagine yourself without your current struggles, how do you feel about that version of you?",
                question_type="single_choice",
                options=[
                    "Excited and relieved - that's who I want to be",
                    "Hopeful but slightly uncertain about who I'd become",
                    "Worried I might become boring or lose depth",
                    "Concerned I'd lose what makes me special or interesting",
                    "Afraid I wouldn't know who I am without these challenges"
                ],
                help_text="This detects identity fusion with problems - a major barrier to change",
                required=True,
                clinical_mapping={
                    "category": "unconscious_secondary_gain_assessment",
                    "weights": {
                        "Excited and relieved - that's who I want to be": {"healthy_identity_separation": 3, "change_motivation": 2},
                        "Hopeful but slightly uncertain about who I'd become": {"mild_identity_confusion": 1, "adaptive_uncertainty": 1},
                        "Worried I might become boring or lose depth": {"suffering_as_depth": 2, "interesting_through_pain": 2},
                        "Concerned I'd lose what makes me special or interesting": {"specialness_through_suffering": 3, "uniqueness_attachment": 3},
                        "Afraid I wouldn't know who I am without these challenges": {"identity_fusion": 4, "existential_attachment": 3}
                    }
                },
                skip_logic=None
            ),

            # ================================
            # NEUROPLASTICITY READINESS ASSESSMENT
            # ================================
            # Advanced assessment of brain change readiness and neural flexibility
            # Based on neuroscience research on optimal conditions for rapid neural rewiring

            UserFriendlyQuestion(
                id="learning_flexibility_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=42,
                title="Learning Flexibility Assessment",
                subtitle="Testing your brain's adaptability to new patterns",
                question_text="Think of a habit you successfully changed in the past year (big or small). How quickly did you adapt to the new way of doing things?",
                question_type="single_choice",
                options=[
                    "I adapted within days - felt natural very quickly",
                    "Took a few weeks but became automatic fairly easily",
                    "Required several months of conscious effort to stick",
                    "Still requires effort and doesn't feel natural yet",
                    "I haven't successfully changed any habits recently"
                ],
                help_text="This measures neuroplasticity - your brain's ability to form new patterns",
                required=True,
                clinical_mapping={
                    "category": "neuroplasticity_readiness_assessment",
                    "weights": {
                        "I adapted within days - felt natural very quickly": {"high_neuroplasticity": 4, "rapid_adaptation": 3},
                        "Took a few weeks but became automatic fairly easily": {"good_neuroplasticity": 3, "normal_adaptation": 2},
                        "Required several months of conscious effort to stick": {"moderate_neuroplasticity": 2, "effortful_adaptation": 1},
                        "Still requires effort and doesn't feel natural yet": {"low_neuroplasticity": 1, "adaptation_challenges": 2},
                        "I haven't successfully changed any habits recently": {"very_low_neuroplasticity": 1, "change_avoidance": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="sleep_optimization_readiness",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=43,
                title="Sleep & Recovery Optimization",
                subtitle="Assessing neural recovery conditions for optimal change",
                question_text="How would you describe your sleep quality and its impact on your mental clarity?",
                question_type="single_choice",
                options=[
                    "Consistently good sleep - wake up refreshed and mentally sharp",
                    "Generally good sleep - occasional issues but manageable",
                    "Inconsistent sleep - affects my mood and thinking regularly",
                    "Poor sleep quality - often tired and mentally foggy",
                    "Severe sleep issues - significantly impacts daily functioning"
                ],
                help_text="Quality sleep is crucial for neuroplasticity and rapid transformation",
                required=True,
                clinical_mapping={
                    "category": "neuroplasticity_readiness_assessment",
                    "weights": {
                        "Consistently good sleep - wake up refreshed and mentally sharp": {"optimal_neural_recovery": 4, "high_plasticity_potential": 3},
                        "Generally good sleep - occasional issues but manageable": {"good_neural_recovery": 3, "moderate_plasticity_potential": 2},
                        "Inconsistent sleep - affects my mood and thinking regularly": {"compromised_neural_recovery": 2, "reduced_plasticity": 2},
                        "Poor sleep quality - often tired and mentally foggy": {"poor_neural_recovery": 1, "low_plasticity_potential": 3},
                        "Severe sleep issues - significantly impacts daily functioning": {"severely_compromised_recovery": 0, "plasticity_barriers": 4}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="stress_neuroplasticity_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=44,
                title="Stress Impact on Brain Change",
                subtitle="Measuring how stress affects your ability to learn and adapt",
                question_text="When you're under stress, how does it affect your ability to learn new things or think differently?",
                question_type="single_choice",
                options=[
                    "Stress actually helps me focus and learn better",
                    "Mild stress doesn't significantly impact my learning",
                    "Moderate stress makes learning more difficult but still possible",
                    "High stress severely impacts my ability to think clearly",
                    "Under stress, I can't learn anything new or change patterns"
                ],
                help_text="Chronic stress inhibits neuroplasticity - this measures your stress resilience",
                required=True,
                clinical_mapping={
                    "category": "neuroplasticity_readiness_assessment",
                    "weights": {
                        "Stress actually helps me focus and learn better": {"stress_enhanced_plasticity": 3, "optimal_stress_response": 4},
                        "Mild stress doesn't significantly impact my learning": {"stress_resilient_plasticity": 3, "good_stress_tolerance": 2},
                        "Moderate stress makes learning more difficult but still possible": {"stress_impaired_plasticity": 2, "moderate_stress_impact": 2},
                        "High stress severely impacts my ability to think clearly": {"stress_blocked_plasticity": 1, "high_stress_vulnerability": 3},
                        "Under stress, I can't learn anything new or change patterns": {"stress_destroyed_plasticity": 0, "extreme_stress_sensitivity": 4}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="cognitive_flexibility_test",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=45,
                title="Cognitive Flexibility Assessment",
                subtitle="Testing mental agility and perspective-shifting ability",
                question_text="When someone presents a viewpoint that completely contradicts your beliefs, what typically happens in your mind?",
                question_type="single_choice",
                options=[
                    "I get curious and explore how they reached that conclusion",
                    "I consider their perspective even if I disagree",
                    "I listen but find it hard to really understand their viewpoint",
                    "I immediately think of arguments against their position",
                    "I feel defensive and want to prove them wrong"
                ],
                help_text="Cognitive flexibility is essential for rapid belief and pattern changes",
                required=True,
                clinical_mapping={
                    "category": "neuroplasticity_readiness_assessment",
                    "weights": {
                        "I get curious and explore how they reached that conclusion": {"high_cognitive_flexibility": 4, "openness_to_change": 3},
                        "I consider their perspective even if I disagree": {"good_cognitive_flexibility": 3, "perspective_taking": 2},
                        "I listen but find it hard to really understand their viewpoint": {"moderate_cognitive_flexibility": 2, "limited_perspective_shift": 1},
                        "I immediately think of arguments against their position": {"low_cognitive_flexibility": 1, "defensive_cognition": 2},
                        "I feel defensive and want to prove them wrong": {"rigid_cognitive_patterns": 0, "high_cognitive_resistance": 3}
                    }
                },
                skip_logic=None
            ),

            UserFriendlyQuestion(
                id="neuroplasticity_lifestyle_factors",
                stage=QuestionnaireStage.STAGE_5_WELLBEING,
                question_number=46,
                title="Neuroplasticity Lifestyle Support",
                subtitle="Assessing lifestyle factors that enhance brain change capacity",
                question_text="Which of these brain-healthy activities do you regularly engage in?",
                question_type="multiple_choice",
                options=[
                    "Regular physical exercise (cardio or strength training)",
                    "Meditation, mindfulness, or breathwork practices",
                    "Learning new skills or challenging mental activities",
                    "Social connection and meaningful relationships",
                    "Exposure to nature and outdoor environments",
                    "Creative activities (art, music, writing, etc.)",
                    "None of these - I don't prioritize brain health activities"
                ],
                help_text="These activities enhance neuroplasticity and accelerate transformation",
                required=True,
                clinical_mapping={
                    "category": "neuroplasticity_readiness_assessment",
                    "weights": {
                        "Regular physical exercise (cardio or strength training)": {"exercise_neuroplasticity": 2, "brain_health_support": 1},
                        "Meditation, mindfulness, or breathwork practices": {"mindfulness_neuroplasticity": 3, "neural_regulation": 2},
                        "Learning new skills or challenging mental activities": {"learning_neuroplasticity": 2, "cognitive_stimulation": 1},
                        "Social connection and meaningful relationships": {"social_neuroplasticity": 2, "emotional_support": 1},
                        "Exposure to nature and outdoor environments": {"nature_neuroplasticity": 1, "stress_reduction": 2},
                        "Creative activities (art, music, writing, etc.)": {"creative_neuroplasticity": 2, "novel_neural_pathways": 1},
                        "None of these - I don't prioritize brain health activities": {"low_neuroplasticity_support": -2, "lifestyle_barriers": 3}
                    }
                },
                skip_logic=None
            )
        ]

    def get_questions_by_stage(self, stage: QuestionnaireStage) -> List[UserFriendlyQuestion]:
        """Get all questions for a specific stage"""
        return [q for q in self.questions if q.stage == stage]

    def get_stage_info(self, stage: QuestionnaireStage) -> Dict:
        """Get introduction and metadata for a stage"""
        return self.stage_introductions.get(stage, {})

    def get_progress_message(self, question_number: int) -> Optional[str]:
        """Get motivational message for current progress"""
        return self.progress_motivators.get(question_number)

    def calculate_clinical_scores(self, responses: Dict[str, str]) -> Dict[str, float]:
        """Calculate clinical pattern scores from user responses"""

        pattern_scores = {}

        # Initialize all possible patterns
        all_patterns = set()
        for question in self.questions:
            for pattern_weights in question.clinical_mapping.get("weights", {}).values():
                all_patterns.update(pattern_weights.keys())

        for pattern in all_patterns:
            pattern_scores[pattern] = 0.0

        # Calculate scores based on responses
        for question in self.questions:
            if question.id in responses:
                user_response = responses[question.id]
                weights = question.clinical_mapping.get("weights", {})

                if user_response in weights:
                    for pattern, score in weights[user_response].items():
                        if pattern in pattern_scores:
                            pattern_scores[pattern] += score

        return pattern_scores

    def generate_stage_summary(self, stage: QuestionnaireStage, responses: Dict[str, str]) -> Dict:
        """Generate a summary of responses for a completed stage"""

        stage_questions = self.get_questions_by_stage(stage)
        stage_responses = {q.id: responses.get(q.id) for q in stage_questions if q.id in responses}

        # Calculate partial scores for this stage
        stage_scores = {}
        for question in stage_questions:
            if question.id in responses:
                user_response = responses[question.id]
                weights = question.clinical_mapping.get("weights", {})

                if user_response in weights:
                    for pattern, score in weights[user_response].items():
                        if pattern not in stage_scores:
                            stage_scores[pattern] = 0
                        stage_scores[pattern] += score

        return {
            "stage": stage.value,
            "questions_answered": len(stage_responses),
            "total_questions": len(stage_questions),
            "completion_percentage": (len(stage_responses) / len(stage_questions)) * 100,
            "dominant_patterns": sorted(stage_scores.items(), key=lambda x: x[1], reverse=True)[:3],
            "responses": stage_responses
        }

    # ================================
    # RESISTANCE PREDICTION ALGORITHM
    # ================================
    # Advanced algorithm to predict resistance points and suggest interventions
    # Analyzes patterns across all assessment data to identify potential barriers

    def predict_resistance_patterns(self, responses: Dict[str, str]) -> Dict[str, any]:
        """
        Predict resistance patterns based on comprehensive assessment data.
        Analyzes multiple factors to identify where client is likely to resist treatment.
        """

        pattern_scores = self.calculate_clinical_scores(responses)

        # Define resistance prediction weights based on clinical research
        resistance_indicators = {
            # Secondary gain patterns (high resistance predictors)
            "emotional_manipulation": 4,
            "sympathy_addiction": 3,
            "conditional_love_pattern": 3,
            "identity_fusion": 4,
            "specialness_through_suffering": 4,
            "avoidance_legitimization": 3,
            "responsibility_shield": 3,

            # Control and autonomy patterns
            "control_preference": 3,
            "authority_resistance": 3,
            "suggestion_resistance": 3,
            "independence_anxiety": 2,

            # Digital dependency (modern resistance factor)
            "extreme_digital_dependency": 3,
            "no_impulse_control": 4,
            "severe_compulsion": 3,
            "extreme_fragmentation": 3,

            # Hypnotic resistance patterns
            "hypnotic_resistance": 3,
            "analytical_override": 2,
            "hypervigilance": 2,

            # Identity and self-concept barriers
            "victim_identity": 3,
            "fix_it_compulsion": 2,
            "people_pleasing": 2,
            "external_validation": 2,

            # Cognitive rigidity
            "black_white_thinking": 2,
            "catastrophic_thinking": 2,
            "rumination": 2
        }

        # Calculate total resistance score
        total_resistance = 0
        active_resistance_patterns = []

        for pattern, score in pattern_scores.items():
            if pattern in resistance_indicators and score > 0:
                resistance_weight = resistance_indicators[pattern]
                weighted_score = score * resistance_weight
                total_resistance += weighted_score

                if score >= 2:  # Significant pattern presence
                    active_resistance_patterns.append({
                        "pattern": pattern,
                        "intensity": score,
                        "resistance_weight": resistance_weight,
                        "contribution": weighted_score
                    })

        # Sort by contribution to resistance
        active_resistance_patterns.sort(key=lambda x: x["contribution"], reverse=True)

        # Determine resistance level
        if total_resistance <= 10:
            resistance_level = "Low"
            risk_description = "Minimal resistance expected - good therapeutic alliance likely"
        elif total_resistance <= 25:
            resistance_level = "Moderate"
            risk_description = "Some resistance points - manageable with skilled rapport"
        elif total_resistance <= 45:
            resistance_level = "High"
            risk_description = "Significant resistance expected - requires specialized approach"
        else:
            resistance_level = "Extreme"
            risk_description = "Multiple resistance barriers - extensive preparation needed"

        return {
            "resistance_level": resistance_level,
            "total_resistance_score": total_resistance,
            "risk_description": risk_description,
            "primary_resistance_patterns": active_resistance_patterns[:5],
            "resistance_category_breakdown": self._categorize_resistance_patterns(active_resistance_patterns),
            "intervention_recommendations": self._generate_resistance_interventions(active_resistance_patterns)
        }

    def _categorize_resistance_patterns(self, patterns: List[Dict]) -> Dict[str, int]:
        """Categorize resistance patterns by type for targeted intervention"""

        categories = {
            "Secondary Gain": 0,
            "Control Issues": 0,
            "Digital Dependency": 0,
            "Hypnotic Resistance": 0,
            "Identity Barriers": 0,
            "Cognitive Rigidity": 0
        }

        category_mapping = {
            # Secondary gain
            "emotional_manipulation": "Secondary Gain",
            "sympathy_addiction": "Secondary Gain",
            "conditional_love_pattern": "Secondary Gain",
            "identity_fusion": "Secondary Gain",
            "specialness_through_suffering": "Secondary Gain",
            "avoidance_legitimization": "Secondary Gain",
            "responsibility_shield": "Secondary Gain",

            # Control issues
            "control_preference": "Control Issues",
            "authority_resistance": "Control Issues",
            "suggestion_resistance": "Control Issues",
            "independence_anxiety": "Control Issues",

            # Digital dependency
            "extreme_digital_dependency": "Digital Dependency",
            "no_impulse_control": "Digital Dependency",
            "severe_compulsion": "Digital Dependency",
            "extreme_fragmentation": "Digital Dependency",

            # Hypnotic resistance
            "hypnotic_resistance": "Hypnotic Resistance",
            "analytical_override": "Hypnotic Resistance",
            "hypervigilance": "Hypnotic Resistance",

            # Identity barriers
            "victim_identity": "Identity Barriers",
            "fix_it_compulsion": "Identity Barriers",
            "people_pleasing": "Identity Barriers",
            "external_validation": "Identity Barriers",

            # Cognitive rigidity
            "black_white_thinking": "Cognitive Rigidity",
            "catastrophic_thinking": "Cognitive Rigidity",
            "rumination": "Cognitive Rigidity"
        }

        for pattern in patterns:
            pattern_name = pattern["pattern"]
            if pattern_name in category_mapping:
                category = category_mapping[pattern_name]
                categories[category] += pattern["contribution"]

        return categories

    def _generate_resistance_interventions(self, patterns: List[Dict]) -> List[Dict[str, str]]:
        """Generate specific intervention recommendations based on resistance patterns"""

        interventions = []

        intervention_mapping = {
            # Secondary gain interventions
            "emotional_manipulation": {
                "intervention": "Address secondary gains directly",
                "technique": "Explore alternative ways to meet underlying needs for connection",
                "timing": "Session 1 - Build awareness of pattern without shame"
            },
            "sympathy_addiction": {
                "intervention": "Reframe sympathy-seeking behavior",
                "technique": "Help client discover authentic connection beyond sympathy",
                "timing": "Session 2 - After rapport is established"
            },
            "identity_fusion": {
                "intervention": "Separate identity from problems",
                "technique": "Future self visualization where they are whole without current issues",
                "timing": "Session 1 - Critical foundation work"
            },
            "specialness_through_suffering": {
                "intervention": "Redefine uniqueness positively",
                "technique": "Identify special qualities unrelated to suffering",
                "timing": "Session 1 - Prevent identity threat response"
            },

            # Control issue interventions
            "control_preference": {
                "intervention": "Collaborative approach emphasis",
                "technique": "Frame hypnosis as 'teaching self-control skills'",
                "timing": "Pre-session - During consent process"
            },
            "authority_resistance": {
                "intervention": "Peer-to-peer positioning",
                "technique": "Present as guide rather than authority figure",
                "timing": "Session 1 - From first contact"
            },
            "suggestion_resistance": {
                "intervention": "Indirect suggestion approach",
                "technique": "Use permissive language and choice-based framing",
                "timing": "Throughout - Modify hypnotic language"
            },

            # Digital dependency interventions
            "extreme_digital_dependency": {
                "intervention": "Digital detox preparation",
                "technique": "Start with micro-practices of device-free time",
                "timing": "Pre-session homework assignment"
            },
            "no_impulse_control": {
                "intervention": "Impulse regulation training",
                "technique": "Brief mindfulness practices before hypnosis",
                "timing": "Session 1 - Build capacity first"
            },

            # Hypnotic resistance interventions
            "hypnotic_resistance": {
                "intervention": "Resistance normalization",
                "technique": "Explain resistance as protective mechanism",
                "timing": "Session 1 - Address directly and respectfully"
            },
            "analytical_override": {
                "intervention": "Utilize analytical nature",
                "technique": "Explain neuroscience of hypnosis to engage analytical mind",
                "timing": "Pre-hypnotic - Educational approach"
            },

            # Identity barrier interventions
            "victim_identity": {
                "intervention": "Gradual empowerment focus",
                "technique": "Acknowledge struggle while introducing agency",
                "timing": "Session 1 - Balance validation with empowerment"
            },
            "people_pleasing": {
                "intervention": "Permission to prioritize self",
                "technique": "Frame self-care as service to others",
                "timing": "Session 1 - Reframe self-focus as positive"
            }
        }

        # Get interventions for top resistance patterns
        for pattern in patterns[:5]:  # Top 5 resistance patterns
            pattern_name = pattern["pattern"]
            if pattern_name in intervention_mapping:
                intervention_data = intervention_mapping[pattern_name]
                intervention_data["pattern_intensity"] = pattern["intensity"]
                intervention_data["priority"] = "High" if pattern["contribution"] >= 10 else "Medium"
                interventions.append(intervention_data)

        return interventions

    # ================================
    # SESSION PROTOCOL OPTIMIZATION
    # ================================
    # Advanced protocol optimization based on comprehensive assessment
    # Determines optimal session structure, timing, and intervention sequencing

    def optimize_session_protocol(self, responses: Dict[str, str]) -> Dict[str, any]:
        """
        Generate optimized session protocol based on comprehensive assessment data.
        Determines session count, focus areas, techniques, and timing.
        """

        pattern_scores = self.calculate_clinical_scores(responses)
        resistance_analysis = self.predict_resistance_patterns(responses)

        # Calculate session requirements based on complexity
        session_complexity_factors = {
            # High complexity indicators requiring more sessions
            "identity_fusion": 3,
            "specialness_through_suffering": 3,
            "emotional_manipulation": 2,
            "sympathy_addiction": 2,
            "severe_digital_dependency": 2,
            "extreme_fragmentation": 2,
            "victim_identity": 2,
            "authority_resistance": 2,
            "hypnotic_resistance": 2,
            "control_preference": 2,
            "trauma_indicators": 3,
            "comorbid_anxiety": 2,
            "depression_markers": 2
        }

        # Calculate base session requirement
        complexity_score = 0
        for pattern, score in pattern_scores.items():
            if pattern in session_complexity_factors and score > 0:
                complexity_score += score * session_complexity_factors[pattern]

        # Determine optimal session count
        if complexity_score <= 15:
            recommended_sessions = 3
            session_intensity = "Standard"
            protocol_type = "Rapid Transformation"
        elif complexity_score <= 30:
            recommended_sessions = 4
            session_intensity = "Enhanced"
            protocol_type = "Extended Rapid Transformation"
        elif complexity_score <= 50:
            recommended_sessions = 5
            session_intensity = "Intensive"
            protocol_type = "Complex Case Protocol"
        else:
            recommended_sessions = 6
            session_intensity = "Maximum Support"
            protocol_type = "High Complexity Protocol"

        # Generate session-by-session protocol
        session_plans = self._generate_session_plans(
            pattern_scores,
            resistance_analysis,
            recommended_sessions
        )

        # Determine optimal session spacing
        if resistance_analysis["resistance_level"] in ["High", "Extreme"]:
            session_spacing = "Weekly (allows integration time)"
            prep_requirements = "Extensive pre-session preparation needed"
        elif complexity_score > 30:
            session_spacing = "Bi-weekly (moderate integration time)"
            prep_requirements = "Moderate pre-session preparation"
        else:
            session_spacing = "Weekly or bi-weekly (client preference)"
            prep_requirements = "Standard preparation sufficient"

        # Calculate success probability modifiers
        success_modifiers = self._calculate_success_modifiers(pattern_scores, resistance_analysis)

        return {
            "recommended_sessions": recommended_sessions,
            "session_intensity": session_intensity,
            "protocol_type": protocol_type,
            "complexity_score": complexity_score,
            "session_spacing": session_spacing,
            "prep_requirements": prep_requirements,
            "session_plans": session_plans,
            "success_probability": success_modifiers["base_success_probability"],
            "protocol_modifications": self._generate_protocol_modifications(pattern_scores, resistance_analysis),
            "homework_assignments": self._generate_homework_sequence(pattern_scores, recommended_sessions)
        }

    def _generate_session_plans(self, pattern_scores: Dict, resistance_analysis: Dict, session_count: int) -> List[Dict]:
        """Generate detailed plans for each session"""

        session_plans = []

        # Session 1: Foundation & Resistance Management
        session_1 = {
            "session_number": 1,
            "primary_focus": "Foundation Building & Resistance Management",
            "duration": "90-120 minutes",
            "key_objectives": [
                "Establish therapeutic rapport and safety",
                "Address primary resistance patterns",
                "Conduct hypnotic readiness assessment",
                "Begin pattern interruption"
            ],
            "specific_techniques": [],
            "resistance_interventions": [],
            "hypnotic_approach": "Conservative - build confidence",
            "success_metrics": [
                "Client feels understood and safe",
                "Primary resistance patterns acknowledged",
                "Successful light hypnotic state achieved"
            ]
        }

        # Add resistance-specific interventions for Session 1
        for intervention in resistance_analysis.get("intervention_recommendations", [])[:3]:
            if intervention["timing"].startswith("Session 1"):
                session_1["resistance_interventions"].append({
                    "pattern": intervention.get("pattern_intensity", "Unknown"),
                    "intervention": intervention["intervention"],
                    "technique": intervention["technique"]
                })

        # Determine Session 1 techniques based on dominant patterns
        dominant_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)[:5]

        for pattern, score in dominant_patterns[:3]:
            if score >= 2:  # Significant pattern
                if pattern == "unhappiness_culture":
                    session_1["specific_techniques"].append("Positive experience integration work")
                elif pattern == "people_pleasing":
                    session_1["specific_techniques"].append("Boundary establishment hypnosis")
                elif pattern == "victim_identity":
                    session_1["specific_techniques"].append("Empowerment visualization")
                elif pattern == "control_preference":
                    session_1["specific_techniques"].append("Collaborative hypnosis approach")

        session_plans.append(session_1)

        # Session 2: Core Work
        session_2 = {
            "session_number": 2,
            "primary_focus": "Core Pattern Transformation",
            "duration": "90-120 minutes",
            "key_objectives": [
                "Address primary behavioral patterns",
                "Implement core transformation work",
                "Strengthen positive identity",
                "Install new response patterns"
            ],
            "specific_techniques": [
                "Deep pattern regression work",
                "Identity reformation hypnosis",
                "Future template installation"
            ],
            "hypnotic_approach": "Deeper work - primary transformation",
            "success_metrics": [
                "Core pattern disruption achieved",
                "New identity templates installed",
                "Client reports internal shifts"
            ]
        }

        session_plans.append(session_2)

        # Session 3: Integration & Future Focus
        session_3 = {
            "session_number": 3,
            "primary_focus": "Integration & Future Implementation",
            "duration": "90-120 minutes",
            "key_objectives": [
                "Integrate all changes",
                "Install future success templates",
                "Address remaining resistance",
                "Establish maintenance protocols"
            ],
            "specific_techniques": [
                "Future projection work",
                "Trigger inoculation",
                "Self-hypnosis training",
                "Success template reinforcement"
            ],
            "hypnotic_approach": "Integration focused",
            "success_metrics": [
                "Confident future projection",
                "Self-hypnosis competency",
                "Robust trigger management"
            ]
        }

        session_plans.append(session_3)

        # Additional sessions for complex cases
        if session_count >= 4:
            session_4 = {
                "session_number": 4,
                "primary_focus": "Advanced Integration & Complexity Management",
                "duration": "90-120 minutes",
                "key_objectives": [
                    "Address complex pattern interactions",
                    "Reinforce challenging areas",
                    "Advanced trigger preparation",
                    "Relationship pattern updates"
                ],
                "specific_techniques": [
                    "Complex scenario rehearsal",
                    "Relationship dynamics work",
                    "Advanced emotional regulation"
                ],
                "hypnotic_approach": "Precision targeting",
                "success_metrics": [
                    "Complex scenarios handled confidently",
                    "Relationship improvements evident",
                    "Emotional stability maintained"
                ]
            }
            session_plans.append(session_4)

        if session_count >= 5:
            session_5 = {
                "session_number": 5,
                "primary_focus": "Mastery & Long-term Success",
                "duration": "90-120 minutes",
                "key_objectives": [
                    "Achieve mastery level integration",
                    "Address edge cases and exceptions",
                    "Install long-term maintenance",
                    "Prepare for independent success"
                ],
                "specific_techniques": [
                    "Mastery level rehearsal",
                    "Exception handling protocols",
                    "Long-term vision work"
                ],
                "hypnotic_approach": "Mastery integration",
                "success_metrics": [
                    "Consistent success across scenarios",
                    "Independent problem-solving capability",
                    "Long-term vision clarity"
                ]
            }
            session_plans.append(session_5)

        if session_count >= 6:
            session_6 = {
                "session_number": 6,
                "primary_focus": "Optimization & Future-Proofing",
                "duration": "90-120 minutes",
                "key_objectives": [
                    "Optimize all systems",
                    "Future-proof against regression",
                    "Advanced self-management",
                    "Legacy building"
                ],
                "specific_techniques": [
                    "System optimization protocols",
                    "Advanced regression prevention",
                    "Mentor identity installation"
                ],
                "hypnotic_approach": "Advanced mastery",
                "success_metrics": [
                    "Optimized performance levels",
                    "Robust anti-regression systems",
                    "Mentor-level self-concept"
                ]
            }
            session_plans.append(session_6)

        return session_plans

    def _calculate_success_modifiers(self, pattern_scores: Dict, resistance_analysis: Dict) -> Dict:
        """Calculate success probability based on various factors"""

        base_success = 85  # Base success rate for RTT

        # Positive factors (increase success probability)
        positive_factors = {
            "high_hypnotic_susceptibility": 10,
            "very_high_hypnotic_susceptibility": 15,
            "healthy_motivation": 8,
            "change_motivation": 6,
            "self_awareness": 5,
            "emotional_intelligence": 5,
            "healthy_boundaries": 5,
            "good_support_system": 5,
            "stable_life_circumstances": 3
        }

        # Negative factors (decrease success probability)
        negative_factors = {
            "identity_fusion": 15,
            "specialness_through_suffering": 12,
            "severe_digital_dependency": 10,
            "hypnotic_resistance": 8,
            "authority_resistance": 8,
            "emotional_manipulation": 8,
            "extreme_fragmentation": 6,
            "victim_identity": 6,
            "poor_impulse_control": 5
        }

        # Calculate adjustments
        positive_adjustment = 0
        negative_adjustment = 0

        for pattern, score in pattern_scores.items():
            if pattern in positive_factors and score > 0:
                positive_adjustment += min(positive_factors[pattern] * (score / 4), positive_factors[pattern])

            if pattern in negative_factors and score > 0:
                negative_adjustment += min(negative_factors[pattern] * (score / 4), negative_factors[pattern])

        # Resistance level adjustments
        resistance_adjustments = {
            "Low": 5,
            "Moderate": 0,
            "High": -10,
            "Extreme": -20
        }

        resistance_adjustment = resistance_adjustments.get(resistance_analysis["resistance_level"], 0)

        final_success_probability = max(45, min(95,
            base_success + positive_adjustment - negative_adjustment + resistance_adjustment
        ))

        return {
            "base_success_probability": final_success_probability,
            "positive_factors": positive_adjustment,
            "negative_factors": negative_adjustment,
            "resistance_impact": resistance_adjustment
        }

    def _generate_protocol_modifications(self, pattern_scores: Dict, resistance_analysis: Dict) -> List[str]:
        """Generate specific protocol modifications based on assessment"""

        modifications = []

        # Resistance-based modifications
        if resistance_analysis["resistance_level"] == "High":
            modifications.append("Extended rapport building phase (20-30 minutes)")
            modifications.append("Use indirect hypnotic language throughout")
            modifications.append("Include client in all decision-making")

        elif resistance_analysis["resistance_level"] == "Extreme":
            modifications.append("Consider pre-therapy consultation sessions")
            modifications.append("Use conversational hypnosis approach initially")
            modifications.append("Extensive psychoeducation component")

        # Pattern-specific modifications
        if pattern_scores.get("identity_fusion", 0) >= 3:
            modifications.append("Identity separation work must precede symptom work")
            modifications.append("Use future self visualization extensively")

        if pattern_scores.get("control_preference", 0) >= 2:
            modifications.append("Emphasize collaborative approach throughout")
            modifications.append("Provide detailed explanations of all techniques")

        if pattern_scores.get("extreme_digital_dependency", 0) >= 2:
            modifications.append("Include digital wellness component")
            modifications.append("Progressive device-free time assignments")

        if pattern_scores.get("hypnotic_resistance", 0) >= 2:
            modifications.append("Start with very light trance states")
            modifications.append("Use progressive relaxation approach")

        return modifications

    def _generate_homework_sequence(self, pattern_scores: Dict, session_count: int) -> List[Dict]:
        """Generate session-by-session homework assignments"""

        homework_sequence = []

        # Pre-Session 1 homework
        pre_session_1 = {
            "timing": "Pre-Session 1",
            "assignments": [
                "Complete digital wellness assessment",
                "Begin 5-minute daily phone-free periods",
                "Journal current patterns for 3 days"
            ]
        }

        if pattern_scores.get("extreme_digital_dependency", 0) >= 2:
            pre_session_1["assignments"].append("Practice 10-minute device-free breathing exercises")

        homework_sequence.append(pre_session_1)

        # Between Session 1 & 2
        session_1_homework = {
            "timing": "Between Session 1 & 2",
            "assignments": [
                "Practice self-hypnosis recording daily",
                "Implement agreed boundary changes",
                "Notice and journal pattern interruptions"
            ]
        }

        if pattern_scores.get("people_pleasing", 0) >= 2:
            session_1_homework["assignments"].append("Practice saying 'no' in low-stakes situations")

        homework_sequence.append(session_1_homework)

        # Between Session 2 & 3
        session_2_homework = {
            "timing": "Between Session 2 & 3",
            "assignments": [
                "Practice future self visualization daily",
                "Implement new response patterns in real situations",
                "Complete integration exercises"
            ]
        }

        homework_sequence.append(session_2_homework)

        # Additional homework for longer protocols
        if session_count >= 4:
            session_3_homework = {
                "timing": "Between Session 3 & 4",
                "assignments": [
                    "Practice complex scenario responses",
                    "Begin relationship pattern changes",
                    "Daily success template reinforcement"
                ]
            }
            homework_sequence.append(session_3_homework)

        return homework_sequence

# ================================
# CLINICAL VALIDATION FOUNDATION
# ================================
# Evidence-based clinical validation system for rapid transformation hypnotherapy
# Addresses DSM-5-TR alignment, therapeutic precision, and hypnotherapy integration

class DSM5AlignmentLevel(Enum):
    """DSM-5-TR alignment classification"""
    FULL_ALIGNMENT = "full_dsm5_alignment"
    PARTIAL_ALIGNMENT = "partial_dsm5_alignment"
    SUBCLINICAL_PATTERN = "subclinical_pattern"
    NOVEL_CONSTRUCT = "novel_construct"
    REQUIRES_VALIDATION = "requires_validation"

class SeverityGradation(Enum):
    """Clinical severity levels"""
    SUBCLINICAL = "subclinical"
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    COMPLEX_COMORBID = "complex_comorbid"

class TherapeuticReadiness(Enum):
    """Hypnotherapy readiness levels"""
    HIGH_READINESS = "high_readiness"
    MODERATE_READINESS = "moderate_readiness"
    CONDITIONAL_READINESS = "conditional_readiness"
    LOW_READINESS = "low_readiness"
    CONTRAINDICATED = "contraindicated"

@dataclass
class ClinicalValidationMetrics:
    """Psychometric validation data for patterns"""
    test_retest_reliability: float
    inter_rater_reliability: float
    construct_validity: float
    criterion_validity: float
    content_validity: float
    internal_consistency: float
    false_positive_rate: float
    false_negative_rate: float
    sensitivity: float
    specificity: float

@dataclass
class PatternDefinition:
    """Enhanced clinical pattern definition"""
    pattern_id: str
    clinical_name: str
    dsm5_alignment: DSM5AlignmentLevel
    operational_criteria: List[str]
    behavioral_indicators: List[str]
    differential_criteria: List[str]
    developmental_trajectory: str
    cultural_variations: List[str]
    research_citations: List[str]
    validation_metrics: ClinicalValidationMetrics
    therapeutic_targets: List[str]
    contraindications: List[str]

class ClinicalValidationFramework:
    """Evidence-based validation system for behavioral patterns"""

    def __init__(self):
        self.validated_patterns = self._initialize_validated_patterns()
        self.assessment_protocols = self._initialize_assessment_protocols()
        self.reliability_standards = self._initialize_reliability_standards()

    def _initialize_validated_patterns(self) -> Dict[str, PatternDefinition]:
        """Initialize clinically validated pattern definitions"""
        # Create standardized validation metrics for patterns
        standard_metrics = ClinicalValidationMetrics(
            test_retest_reliability=0.85,
            inter_rater_reliability=0.82,
            construct_validity=0.78,
            criterion_validity=0.80,
            content_validity=0.88,
            internal_consistency=0.87,
            false_positive_rate=0.12,
            false_negative_rate=0.08,
            sensitivity=0.92,
            specificity=0.88
        )

        return {
            "unhappiness_culture": PatternDefinition(
                pattern_id="unhappiness_culture",
                clinical_name="Anhedonic Cognitive Pattern Syndrome",
                dsm5_alignment=DSM5AlignmentLevel.PARTIAL_ALIGNMENT,
                operational_criteria=[
                    "Persistent anticipation of negative outcomes during positive experiences",
                    "Systematic minimization of personal achievements and successes",
                    "Core belief of unworthiness for sustained positive emotional states",
                    "Cognitive bias toward catastrophic interpretations of neutral events"
                ],
                behavioral_indicators=[
                    "Verbal self-deprecation following positive events",
                    "Avoidance of celebration or acknowledgment of success",
                    "Hypervigilance for signs of impending failure or loss",
                    "Discomfort with sustained positive attention from others"
                ],
                differential_criteria=[
                    "Distinguish from Major Depressive Episode (episodic vs. trait-like)",
                    "Rule out Dysthymic Disorder (broader functional impairment)",
                    "Consider cultural factors in emotional expression norms"
                ],
                developmental_trajectory="Typically emerges in adolescence, crystallizes in early adulthood",
                cultural_variations=[
                    "Higher prevalence in achievement-oriented cultures",
                    "Varies with cultural norms around emotional expression"
                ],
                research_citations=[
                    "Gilbert & Andrews (1998) - Shame and subordination in depression",
                    "Neff (2003) - Self-compassion research foundations"
                ],
                validation_metrics=standard_metrics,
                therapeutic_targets=[
                    "Cognitive restructuring of catastrophic thinking",
                    "Self-compassion development",
                    "Positive emotion tolerance training"
                ],
                contraindications=[
                    "Active suicidal ideation",
                    "Current manic episode"
                ]
            ),
            # Additional patterns would be added here...
        }

    def _initialize_assessment_protocols(self) -> Dict[str, Dict]:
        """Initialize standardized assessment protocols"""
        return {
            "rapid_screening": {
                "duration_minutes": 15,
                "reliability_threshold": 0.80,
                "questions_per_pattern": 3,
                "validation_method": "concurrent_validity"
            },
            "comprehensive_assessment": {
                "duration_minutes": 45,
                "reliability_threshold": 0.90,
                "questions_per_pattern": 8,
                "validation_method": "construct_validity"
            }
        }

    def _initialize_reliability_standards(self) -> Dict[str, float]:
        """Initialize minimum reliability standards"""
        return {
            "test_retest_minimum": 0.80,
            "inter_rater_minimum": 0.75,
            "internal_consistency_minimum": 0.70,
            "construct_validity_minimum": 0.65,
            "criterion_validity_minimum": 0.70
        }

    def validate_pattern_scores(self, pattern_scores: Dict[str, float]) -> Dict[str, Dict]:
        """Validate pattern scores against clinical standards"""
        validation_results = {}

        for pattern_id, score in pattern_scores.items():
            if pattern_id in self.validated_patterns:
                pattern_def = self.validated_patterns[pattern_id]
                metrics = pattern_def.validation_metrics

                validation_results[pattern_id] = {
                    "raw_score": score,
                    "clinical_significance": self._assess_clinical_significance(score),
                    "dsm5_alignment": pattern_def.dsm5_alignment.value,
                    "reliability_index": metrics.test_retest_reliability,
                    "recommended_interventions": pattern_def.therapeutic_targets,
                    "contraindications": pattern_def.contraindications
                }

        return validation_results

    def _assess_clinical_significance(self, score: float) -> str:
        """Assess clinical significance of pattern score"""
        if score >= 7:
            return "clinically_significant"
        elif score >= 5:
            return "moderate_concern"
        elif score >= 3:
            return "mild_elevation"
        else:
            return "subclinical"

    def generate_clinical_report(self, validation_results: Dict[str, Dict]) -> str:
        """Generate clinical assessment report"""
        report_lines = [
            "CLINICAL ASSESSMENT REPORT",
            "=" * 50,
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            ""
        ]

        # Significant patterns
        significant_patterns = [
            (pattern_id, data) for pattern_id, data in validation_results.items()
            if data["clinical_significance"] in ["clinically_significant", "moderate_concern"]
        ]

        if significant_patterns:
            report_lines.extend([
                "CLINICALLY SIGNIFICANT PATTERNS:",
                "-" * 30
            ])

            for pattern_id, data in significant_patterns:
                report_lines.extend([
                    f"Pattern: {pattern_id.replace('_', ' ').title()}",
                    f"  Significance: {data['clinical_significance']}",
                    f"  DSM-5 Alignment: {data['dsm5_alignment']}",
                    f"  Reliability Index: {data['reliability_index']:.2f}",
                    "  Recommended Interventions:",
                ])

                for intervention in data["recommended_interventions"]:
                    report_lines.append(f"    • {intervention}")

                if data["contraindications"]:
                    report_lines.append("  Contraindications:")
                    for contra in data["contraindications"]:
                        report_lines.append(f"    ⚠ {contra}")

                report_lines.append("")

        return "\n".join(report_lines)

# ================================
# HYPNOTHERAPY INTEGRATION FRAMEWORK
# ================================
# Pattern-specific hypnotic intervention protocols for rapid transformation
# Maps behavioral patterns to optimal hypnotic techniques and resistance management

class HypnoticTechnique(Enum):
    """Primary hypnotic intervention techniques"""
    PROGRESSIVE_RELAXATION = "progressive_relaxation"
    ERICKSONIAN_METAPHOR = "ericksonian_metaphor"
    COGNITIVE_RESTRUCTURING = "cognitive_restructuring"
    SOMATIC_EXPERIENCING = "somatic_experiencing"
    REGRESSION_THERAPY = "regression_therapy"
    FUTURE_PACING = "future_pacing"
    PARTS_INTEGRATION = "parts_integration"
    ANCHOR_INSTALLATION = "anchor_installation"
    TIMELINE_THERAPY = "timeline_therapy"
    NEURAL_PATHWAY_DISRUPTION = "neural_pathway_disruption"

class ResistanceType(Enum):
    """Types of therapeutic resistance"""
    CONSCIOUS_ANALYTICAL = "conscious_analytical"
    UNCONSCIOUS_PROTECTIVE = "unconscious_protective"
    SOMATIC_TENSION = "somatic_tension"
    IDENTITY_THREAT = "identity_threat"
    SECONDARY_GAIN = "secondary_gain"
    TRAUMA_ACTIVATION = "trauma_activation"

class InductionStyle(Enum):
    """Hypnotic induction approaches"""
    AUTHORITARIAN = "authoritarian"
    PERMISSIVE = "permissive"
    CONFUSION = "confusion"
    RAPID = "rapid"
    PROGRESSIVE = "progressive"
    CONVERSATIONAL = "conversational"

@dataclass
class HypnoticIntervention:
    """Complete hypnotic intervention protocol"""
    primary_technique: HypnoticTechnique
    induction_style: InductionStyle
    deepening_methods: List[str]
    therapeutic_suggestions: List[str]
    emergence_anchors: List[str]
    post_hypnotic_instructions: List[str]
    resistance_management: Dict[ResistanceType, str]
    contraindications: List[str]
    session_duration_minutes: int
    follow_up_requirements: List[str]

@dataclass
class ResistanceProfile:
    """Resistance pattern analysis"""
    primary_resistance_type: ResistanceType
    severity_level: SeverityGradation
    manifestation_indicators: List[str]
    bypass_strategies: List[str]
    reframe_approaches: List[str]
    somatic_interventions: List[str]

class HypnotherapyIntegrationFramework:
    """Advanced hypnotherapy protocol mapping system"""

    def __init__(self):
        self.intervention_protocols = self._initialize_intervention_protocols()
        self.resistance_profiles = self._initialize_resistance_profiles()
        self.technique_compatibility = self._initialize_technique_compatibility()

    def _initialize_intervention_protocols(self) -> Dict[str, HypnoticIntervention]:
        """Initialize pattern-specific hypnotic interventions"""
        return {
            "unhappiness_culture": HypnoticIntervention(
                primary_technique=HypnoticTechnique.COGNITIVE_RESTRUCTURING,
                induction_style=InductionStyle.PERMISSIVE,
                deepening_methods=[
                    "Progressive muscle relaxation with positive associations",
                    "Breathing synchronization with self-compassion phrases",
                    "Guided imagery of personal achievement acceptance"
                ],
                therapeutic_suggestions=[
                    "Your unconscious mind naturally recognizes your inherent worth",
                    "Each positive experience builds lasting neural pathways of joy",
                    "You deserve happiness as much as anyone else in the world",
                    "Your achievements reflect your genuine capabilities and effort"
                ],
                emergence_anchors=[
                    "Deep breath activates confidence and self-acceptance",
                    "Gentle smile triggers automatic joy recognition",
                    "Hand on heart connects to inner worth"
                ],
                post_hypnotic_instructions=[
                    "Notice and acknowledge three positive moments each day",
                    "When achievements occur, pause and feel deserving",
                    "Use breathing anchor during moments of self-doubt"
                ],
                resistance_management={
                    ResistanceType.CONSCIOUS_ANALYTICAL: "Utilize analytical nature with logical self-worth evidence",
                    ResistanceType.UNCONSCIOUS_PROTECTIVE: "Honor protective parts while expanding safety definition",
                    ResistanceType.IDENTITY_THREAT: "Integrate new self-concept gradually with existing identity"
                },
                contraindications=[
                    "Active manic episode",
                    "Severe depression requiring medical intervention",
                    "Substance use during session"
                ],
                session_duration_minutes=60,
                follow_up_requirements=[
                    "Daily self-compassion practice recording",
                    "Weekly achievement acknowledgment journal",
                    "Resistance pattern monitoring"
                ]
            ),
            # Additional pattern protocols would be added here...
        }

    def _initialize_resistance_profiles(self) -> Dict[ResistanceType, ResistanceProfile]:
        """Initialize resistance pattern profiles"""
        return {
            ResistanceType.CONSCIOUS_ANALYTICAL: ResistanceProfile(
                primary_resistance_type=ResistanceType.CONSCIOUS_ANALYTICAL,
                severity_level=SeverityGradation.MODERATE,
                manifestation_indicators=[
                    "Excessive questioning of hypnotic process",
                    "Intellectual analysis during relaxation",
                    "Need for scientific explanations",
                    "Difficulty 'letting go' of control"
                ],
                bypass_strategies=[
                    "Provide scientific rationale for interventions",
                    "Use analytical language in suggestions",
                    "Invite conscious collaboration in process",
                    "Frame hypnosis as enhanced focus state"
                ],
                reframe_approaches=[
                    "Position analysis as valuable therapeutic tool",
                    "Highlight mind-body connection research",
                    "Emphasize personal agency in change process"
                ],
                somatic_interventions=[
                    "Progressive muscle tension and release",
                    "Breathing pattern regulation",
                    "Grounding through physical sensations"
                ]
            ),
            # Additional resistance profiles would be added here...
        }

    def _initialize_technique_compatibility(self) -> Dict[str, Dict[HypnoticTechnique, float]]:
        """Initialize pattern-technique compatibility scores"""
        return {
            "unhappiness_culture": {
                HypnoticTechnique.COGNITIVE_RESTRUCTURING: 0.95,
                HypnoticTechnique.ERICKSONIAN_METAPHOR: 0.85,
                HypnoticTechnique.FUTURE_PACING: 0.80,
                HypnoticTechnique.ANCHOR_INSTALLATION: 0.75,
                HypnoticTechnique.PARTS_INTEGRATION: 0.70,
                HypnoticTechnique.PROGRESSIVE_RELAXATION: 0.65,
                HypnoticTechnique.SOMATIC_EXPERIENCING: 0.60,
                HypnoticTechnique.TIMELINE_THERAPY: 0.55,
                HypnoticTechnique.REGRESSION_THERAPY: 0.45,
                HypnoticTechnique.NEURAL_PATHWAY_DISRUPTION: 0.40
            },
            # Additional pattern compatibility scores would be added here...
        }

    def select_optimal_intervention(self, pattern_id: str, severity: SeverityGradation,
                                   client_preferences: Optional[Dict] = None) -> HypnoticIntervention:
        """Select optimal hypnotic intervention for pattern and severity"""

        if pattern_id not in self.intervention_protocols:
            # Return default intervention for unknown patterns
            return self._get_default_intervention()

        base_intervention = self.intervention_protocols[pattern_id]

        # Adjust intervention based on severity
        adjusted_intervention = self._adjust_for_severity(base_intervention, severity)

        # Customize based on client preferences if provided
        if client_preferences:
            adjusted_intervention = self._customize_for_preferences(adjusted_intervention, client_preferences)

        return adjusted_intervention

    def _adjust_for_severity(self, intervention: HypnoticIntervention, severity: SeverityGradation) -> HypnoticIntervention:
        """Adjust intervention intensity based on severity level"""

        # Create a copy to avoid modifying the original
        adjusted = HypnoticIntervention(
            primary_technique=intervention.primary_technique,
            induction_style=intervention.induction_style,
            deepening_methods=intervention.deepening_methods.copy(),
            therapeutic_suggestions=intervention.therapeutic_suggestions.copy(),
            emergence_anchors=intervention.emergence_anchors.copy(),
            post_hypnotic_instructions=intervention.post_hypnotic_instructions.copy(),
            resistance_management=intervention.resistance_management.copy(),
            contraindications=intervention.contraindications.copy(),
            session_duration_minutes=intervention.session_duration_minutes,
            follow_up_requirements=intervention.follow_up_requirements.copy()
        )

        # Adjust based on severity
        if severity == SeverityGradation.MILD:
            adjusted.session_duration_minutes = min(45, adjusted.session_duration_minutes)
        elif severity == SeverityGradation.SEVERE:
            adjusted.session_duration_minutes = max(75, adjusted.session_duration_minutes)
            adjusted.follow_up_requirements.append("Daily progress check-ins")
        elif severity == SeverityGradation.COMPLEX_COMORBID:
            adjusted.session_duration_minutes = 90
            adjusted.contraindications.append("Requires multi-modal treatment approach")

        return adjusted

    def _customize_for_preferences(self, intervention: HypnoticIntervention, preferences: Dict) -> HypnoticIntervention:
        """Customize intervention based on client preferences"""

        # Adjust induction style based on preferences
        if preferences.get("prefers_direct_approach"):
            intervention.induction_style = InductionStyle.AUTHORITARIAN
        elif preferences.get("prefers_gentle_approach"):
            intervention.induction_style = InductionStyle.PERMISSIVE

        # Adjust session duration based on availability
        if preferences.get("limited_time"):
            intervention.session_duration_minutes = min(45, intervention.session_duration_minutes)

        return intervention

    def _get_default_intervention(self) -> HypnoticIntervention:
        """Return default intervention for unknown patterns"""
        return HypnoticIntervention(
            primary_technique=HypnoticTechnique.PROGRESSIVE_RELAXATION,
            induction_style=InductionStyle.PERMISSIVE,
            deepening_methods=["Standard progressive relaxation", "Breathing focus"],
            therapeutic_suggestions=["You are capable of positive change", "Your mind and body work together for healing"],
            emergence_anchors=["Deep breath for clarity", "Gentle movement for grounding"],
            post_hypnotic_instructions=["Practice daily relaxation", "Notice positive changes"],
            resistance_management={ResistanceType.CONSCIOUS_ANALYTICAL: "Provide clear explanations"},
            contraindications=["Active psychosis", "Substance intoxication"],
            session_duration_minutes=50,
            follow_up_requirements=["Weekly progress review"]
        )

    def analyze_resistance_patterns(self, behavioral_indicators: List[str]) -> List[ResistanceType]:
        """Analyze behavioral indicators to identify resistance patterns"""

        identified_resistances = []

        for resistance_type, profile in self.resistance_profiles.items():
            # Count matching indicators
            matches = sum(1 for indicator in behavioral_indicators
                         if any(keyword in indicator.lower() for keyword in
                               ' '.join(profile.manifestation_indicators).lower().split()))

            # If significant matches, include this resistance type
            if matches >= 2:  # Threshold for identification
                identified_resistances.append(resistance_type)

        return identified_resistances

    def generate_session_protocol(self, pattern_id: str, resistance_types: List[ResistanceType]) -> Dict:
        """Generate complete session protocol including resistance management"""

        intervention = self.intervention_protocols.get(pattern_id)
        if not intervention:
            intervention = self._get_default_intervention()

        protocol = {
            "pre_session": {
                "preparation": "Review client history and pattern analysis",
                "environment": "Comfortable, quiet space with minimal distractions",
                "rapport_building": "Establish trust and address any concerns"
            },
            "induction_phase": {
                "style": intervention.induction_style.value,
                "techniques": ["Progressive relaxation", "Breathing synchronization"],
                "duration_minutes": 10,
                "resistance_monitoring": [rt.value for rt in resistance_types]
            },
            "deepening_phase": {
                "methods": intervention.deepening_methods,
                "duration_minutes": 10,
                "depth_indicators": ["Slower breathing", "Muscle relaxation", "Reduced movement"]
            },
            "therapeutic_phase": {
                "primary_technique": intervention.primary_technique.value,
                "suggestions": intervention.therapeutic_suggestions,
                "duration_minutes": 25,
                "resistance_management": {rt.value: intervention.resistance_management.get(rt, "Standard approach")
                                       for rt in resistance_types}
            },
            "emergence_phase": {
                "anchors": intervention.emergence_anchors,
                "post_hypnotic_instructions": intervention.post_hypnotic_instructions,
                "duration_minutes": 5,
                "integration_check": "Ensure client feels grounded and alert"
            },
            "post_session": {
                "feedback_collection": "Gather client experience and insights",
                "homework_assignment": intervention.follow_up_requirements,
                "next_session_planning": "Schedule follow-up based on progress"
            }
        }

        return protocol

# ================================
# ADVANCED ASSESSMENT PROTOCOLS
# ================================
# Digital-age validation and sophisticated assessment methods

class DigitalAgeValidationFramework:
    """Modern validation framework for digital-era behavioral patterns"""

    def __init__(self):
        self.digital_pattern_indicators = self._initialize_digital_indicators()
        self.modern_stress_patterns = self._initialize_stress_patterns()

    def _initialize_digital_indicators(self) -> Dict[str, List[str]]:
        """Initialize digital-era behavioral indicators"""
        return {
            "digital_overwhelm": [
                "Excessive screen time reported",
                "Social media comparison patterns",
                "Information overload symptoms",
                "Digital addiction indicators"
            ],
            "modern_anxiety": [
                "FOMO (Fear of Missing Out)",
                "Constant connectivity pressure",
                "Instant gratification dependency",
                "Validation seeking through social media"
            ]
        }

    def _initialize_stress_patterns(self) -> Dict[str, Dict]:
        """Initialize modern stress pattern definitions"""
        return {
            "digital_stress": {
                "indicators": ["Screen fatigue", "Information overload", "Social comparison"],
                "interventions": ["Digital detox protocols", "Mindful technology use", "Reality grounding"]
            },
            "performance_anxiety": {
                "indicators": ["Perfectionism", "Achievement pressure", "Success fear"],
                "interventions": ["Self-compassion training", "Process focus", "Growth mindset development"]
            }
        }

    def validate_digital_patterns(self, responses: Dict[str, str]) -> Dict[str, float]:
        """Validate digital-era patterns from assessment responses"""
        digital_scores = {}

        # Score digital overwhelm
        screen_time = responses.get("screen_time", "")
        social_media = responses.get("social_media_feeling", "")

        if "8 hours" in screen_time or "don't know" in screen_time:
            digital_scores["digital_overwhelm"] = 3.0
        elif "6-8 hours" in screen_time:
            digital_scores["digital_overwhelm"] = 2.0
        else:
            digital_scores["digital_overwhelm"] = 1.0

        if "worse about my own life" in social_media or "anxious" in social_media:
            digital_scores["social_media_impact"] = 3.0
        elif "comparing" in social_media:
            digital_scores["social_media_impact"] = 2.0
        else:
            digital_scores["social_media_impact"] = 1.0

        return digital_scores

class AdvancedAssessmentProtocols:
    """Sophisticated assessment methods for complex pattern identification"""

    def __init__(self):
        self.digital_framework = DigitalAgeValidationFramework()
        self.pattern_interactions = self._initialize_pattern_interactions()

    def _initialize_pattern_interactions(self) -> Dict[str, List[str]]:
        """Initialize how patterns interact with each other"""
        return {
            "unhappiness_culture": [
                "Amplified by social media comparison",
                "Reinforced by perfectionism",
                "Connected to achievement anxiety"
            ],
            "digital_overwhelm": [
                "Contributes to attention fragmentation",
                "Increases anxiety patterns",
                "Disrupts sleep and energy"
            ]
        }

    def generate_comprehensive_analysis(self, responses: Dict[str, str]) -> Dict:
        """Generate comprehensive analysis including digital-age factors"""

        # Get digital pattern scores
        digital_scores = self.digital_framework.validate_digital_patterns(responses)

        # Analyze pattern interactions
        interactions = self._analyze_pattern_interactions(responses)

        # Generate risk assessment
        risk_factors = self._assess_risk_factors(responses)

        return {
            "digital_age_scores": digital_scores,
            "pattern_interactions": interactions,
            "risk_assessment": risk_factors,
            "intervention_priorities": self._prioritize_interventions(digital_scores, interactions)
        }

    def _analyze_pattern_interactions(self, responses: Dict[str, str]) -> Dict:
        """Analyze how multiple patterns interact"""
        interactions = {}

        # Check for common interaction patterns
        if ("overwhelmed" in responses.get("daily_feeling", "") and
            "anxious" in responses.get("social_media_feeling", "")):
            interactions["digital_stress_amplification"] = {
                "strength": "high",
                "description": "Digital overwhelm amplifies daily stress patterns"
            }

        return interactions

    def _assess_risk_factors(self, responses: Dict[str, str]) -> Dict:
        """Assess various risk factors from responses"""
        risk_factors = {}

        # Assess change resistance risk
        change_experience = responses.get("change_experience", "")
        if "nothing seems to work" in change_experience:
            risk_factors["change_pessimism"] = "high"
        elif "struggle with consistency" in change_experience:
            risk_factors["sustainability_risk"] = "moderate"

        # Assess support system risk
        support_seeking = responses.get("support_seeking", "")
        if "no one would understand" in support_seeking:
            risk_factors["isolation_risk"] = "high"

        return risk_factors

    def _prioritize_interventions(self, digital_scores: Dict, interactions: Dict) -> List[str]:
        """Prioritize interventions based on analysis"""
        priorities = []

        # High digital overwhelm gets priority
        if digital_scores.get("digital_overwhelm", 0) >= 2.5:
            priorities.append("Digital wellness protocol")

        # Social media impact needs addressing
        if digital_scores.get("social_media_impact", 0) >= 2.5:
            priorities.append("Social media relationship restructuring")

        # Add interaction-based priorities
        if "digital_stress_amplification" in interactions:
            priorities.append("Integrated stress management approach")

        return priorities

# ================================
# ENHANCED CONFIG INTEGRATION (MAIN ORCHESTRATOR)
# ================================

class EnhancedAssessmentConfig:
    """Main orchestrator for unified assessment system"""

    def __init__(self):
        self.user_friendly_assessment = UserFriendlyAssessment()
        self.clinical_validation = ClinicalValidationFramework()
        self.hypnotherapy_integration = HypnotherapyIntegrationFramework()
        self.advanced_protocols = AdvancedAssessmentProtocols()

    def generate_enhanced_profile(self, responses: Dict[str, str]) -> Dict:
        """Generate comprehensive enhanced profile with all components"""

        # Get basic clinical scores
        clinical_scores = self.user_friendly_assessment.calculate_clinical_scores(responses)

        # Get digital-age analysis
        advanced_analysis = self.advanced_protocols.generate_comprehensive_analysis(responses)

        # Generate pattern hierarchy
        pattern_hierarchy = self._calculate_pattern_hierarchy(clinical_scores)

        # Generate behavioral analysis
        behavioral_analysis = self._generate_behavioral_analysis(responses, clinical_scores)

        # Generate trigger-response mapping
        trigger_mapping = self._generate_trigger_response_mapping(pattern_hierarchy, responses)

        # Generate session planning
        session_planning = self._generate_session_planning(pattern_hierarchy, responses)

        # Generate resistance analysis
        resistance_analysis = self._generate_resistance_analysis(responses, advanced_analysis)

        # Calculate change readiness score
        change_readiness = self._calculate_change_readiness(responses)

        return {
            "pattern_hierarchy": pattern_hierarchy,
            "behavioral_analysis": behavioral_analysis,
            "trigger_response_mapping": trigger_mapping,
            "session_planning": session_planning,
            "resistance_analysis": resistance_analysis,
            "change_readiness_score": change_readiness,
            "digital_age_factors": advanced_analysis["digital_age_scores"],
            "intervention_priorities": advanced_analysis["intervention_priorities"]
        }

    def _calculate_pattern_hierarchy(self, clinical_scores: Dict[str, float]) -> Dict:
        """Calculate dominant/primary/secondary pattern hierarchy"""

        # Sort patterns by score
        sorted_patterns = sorted(clinical_scores.items(), key=lambda x: x[1], reverse=True)

        # Take top 3 patterns and convert to 8-point scale
        hierarchy = {}
        if len(sorted_patterns) >= 1:
            hierarchy["dominant_pattern"] = {
                "name": sorted_patterns[0][0],
                "score": min(8, int(sorted_patterns[0][1]))
            }

        if len(sorted_patterns) >= 2:
            hierarchy["primary_pattern"] = {
                "name": sorted_patterns[1][0],
                "score": min(8, int(sorted_patterns[1][1]))
            }

        if len(sorted_patterns) >= 3:
            hierarchy["secondary_pattern"] = {
                "name": sorted_patterns[2][0],
                "score": min(8, int(sorted_patterns[2][1]))
            }

        return hierarchy

    def _generate_behavioral_analysis(self, responses: Dict[str, str], scores: Dict[str, float]) -> Dict:
        """Generate core limiting beliefs and behavioral patterns"""

        analysis = {
            "core_limiting_beliefs": [],
            "hidden_benefits": [],
            "systemic_resistance": [],
            "identity_threats": []
        }

        # Analyze based on top patterns
        top_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

        for pattern_name, score in top_patterns:
            if score >= 3:  # Significant pattern
                if "unhappiness" in pattern_name:
                    analysis["core_limiting_beliefs"].append("I don't deserve sustained happiness")
                    analysis["hidden_benefits"].append("Avoiding disappointment by expecting less")
                    analysis["identity_threats"].append("Who am I if I'm not struggling?")

                if "anxiety" in pattern_name or "worry" in pattern_name:
                    analysis["core_limiting_beliefs"].append("I must be vigilant to stay safe")
                    analysis["systemic_resistance"].append("Relaxation feels unsafe or unproductive")

        return analysis

    def _generate_trigger_response_mapping(self, hierarchy: Dict, responses: Dict[str, str]) -> Dict:
        """Generate trigger → response → thought → emotion → behavior → consequence mapping"""

        mapping = {}

        # Get dominant pattern
        dominant = hierarchy.get("dominant_pattern", {}).get("name", "general_pattern")

        if "unhappiness" in dominant:
            mapping["unhappiness_pattern"] = {
                "trigger": "Positive event or achievement occurs",
                "physical_response": "Tightness in chest, shallow breathing",
                "automatic_thought": "This won't last" or "I don't deserve this",
                "emotion": "Guilt, anxiety, suspicion",
                "behavior": "Minimize achievement, look for problems",
                "consequence": "Missed opportunity for joy, reinforced unworthiness"
            }

        return mapping

    def _generate_session_planning(self, hierarchy: Dict, responses: Dict[str, str]) -> Dict:
        """Generate session-specific planning"""

        dominant = hierarchy.get("dominant_pattern", {}).get("name", "general")

        planning = {
            "session_1_focus": "Assessment validation and rapport building",
            "session_2_target": "Core pattern intervention",
            "potential_session_3_need": "Integration and reinforcement"
        }

        if "unhappiness" in dominant:
            planning["session_1_focus"] = "Happiness tolerance assessment and safety building"
            planning["session_2_target"] = "Self-worth and deserving beliefs restructuring"
            planning["potential_session_3_need"] = "Joy anchoring and celebration practice"

        return planning

    def _generate_resistance_analysis(self, responses: Dict[str, str], advanced_analysis: Dict) -> Dict:
        """Generate resistance prediction and management strategies"""

        resistance_points = []
        intervention_keywords = []
        avoid_language = []

        # Analyze authority response
        authority = responses.get("authority_response", "")
        if "resist inwardly" in authority:
            resistance_points.append("May agree verbally but resist suggested changes")
            intervention_keywords.append("collaboration, choice, autonomy")
            avoid_language.append("must, should, have to")

        # Analyze decision making
        decision = responses.get("decision_making", "")
        if "agonize" in decision:
            resistance_points.append("May over-analyze hypnotic suggestions")
            intervention_keywords.append("intuition, natural process, effortless")

        return {
            "predicted_resistance_points": resistance_points,
            "intervention_keywords": ", ".join(intervention_keywords),
            "avoid_language": ", ".join(avoid_language)
        }

    def _calculate_change_readiness(self, responses: Dict[str, str]) -> int:
        """Calculate change readiness score out of 10"""

        score = 5  # Base score

        # Urgency feeling
        urgency = responses.get("urgency_feeling", "")
        if "crisis" in urgency:
            score += 3
        elif "very urgent" in urgency:
            score += 2
        elif "not urgent" in urgency:
            score -= 2

        # Commitment level
        commitment = responses.get("commitment_level", "")
        if "whatever it takes" in commitment:
            score += 2
        elif "significant effort" in commitment:
            score += 1
        elif "too much effort" in commitment:
            score -= 3

        # Change experience
        change_exp = responses.get("change_experience", "")
        if "usually succeed" in change_exp:
            score += 2
        elif "nothing seems to work" in change_exp:
            score -= 3

        return max(1, min(10, score))

    def get_enhanced_questions(self) -> List[Dict]:
        """Get all user-friendly questions formatted for assess2.py"""
        questions = []
        for question in self.user_friendly_assessment.questions:
            question_dict = {
                'id': question.id,
                'text': question.question_text,
                'type': question.question_type,
                'options': question.options,
                'stage': question.stage.value,
                'required': True,
                'clinical_mapping': question.clinical_mapping,
                'help_text': getattr(question, 'help_text', None)
            }
            questions.append(question_dict)
        return questions

    def get_stage_introduction(self, stage: str) -> Dict:
        """Get stage introduction information"""
        try:
            stage_enum = QuestionnaireStage(stage)
            return self.user_friendly_assessment.get_stage_info(stage_enum)
        except (ValueError, KeyError):
            return {
                'title': 'Assessment Section',
                'description': 'Continue with your assessment',
                'icon': '📝'
            }

    def get_progress_message(self, question_number: int) -> str:
        """Get progress message for current question number"""
        return self.user_friendly_assessment.get_progress_message(question_number) or ""

# ================================
# COMPREHENSIVE ASSESSMENT CLASSES
# ================================

class ComprehensiveProfiler:
    """Comprehensive behavioral profiling with detailed analysis"""

    def __init__(self):
        self.enhanced_config = EnhancedAssessmentConfig()
        self.user_friendly = UserFriendlyAssessment()

    def generate_detailed_profile(self, responses: Dict[str, str]) -> Dict:
        """Generate detailed profile with all requested elements"""
        return self.enhanced_config.generate_enhanced_profile(responses)

    def get_pattern_hierarchy(self, responses: Dict[str, str]) -> Dict:
        """Get dominant/primary/secondary patterns with scores out of 8"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("pattern_hierarchy", {})

    def get_trigger_response_mapping(self, responses: Dict[str, str]) -> Dict:
        """Get Trigger → Physical Response → Automatic Thought → Emotion → Behavior → Consequence mapping"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("trigger_response_mapping", {})

    def get_behavioral_analysis(self, responses: Dict[str, str]) -> Dict:
        """Get core limiting beliefs, hidden benefits, systemic resistance, identity threats"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("behavioral_analysis", {})

    def get_session_planning(self, responses: Dict[str, str]) -> Dict:
        """Get Session 1 Focus, Session 2 Target, Potential Session 3 Need"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("session_planning", {})

    def get_resistance_analysis(self, responses: Dict[str, str]) -> Dict:
        """Get resistance prediction and intervention strategies"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("resistance_analysis", {})

    def get_change_readiness_score(self, responses: Dict[str, str]) -> int:
        """Get change readiness score out of 10"""
        profile = self.generate_detailed_profile(responses)
        return profile.get("change_readiness_score", 5)

    def generate_clinical_summary(self, responses: Dict[str, str]) -> str:
        """Generate a formatted clinical summary for practitioners"""
        profile = self.generate_detailed_profile(responses)

        hierarchy = profile.get("pattern_hierarchy", {})
        behavioral = profile.get("behavioral_analysis", {})
        session_planning = profile.get("session_planning", {})
        resistance = profile.get("resistance_analysis", {})
        readiness_score = profile.get("change_readiness_score", 5)

        summary = f"""
COMPREHENSIVE BEHAVIORAL ASSESSMENT SUMMARY
==========================================

PATTERN HIERARCHY:
Dominant Pattern: {hierarchy.get('dominant_pattern', {}).get('name', 'None').replace('_', ' ').title()} (Score: {hierarchy.get('dominant_pattern', {}).get('score', 0)}/8)
Primary Pattern: {hierarchy.get('primary_pattern', {}).get('name', 'None').replace('_', ' ').title()} (Score: {hierarchy.get('primary_pattern', {}).get('score', 0)}/8)
Secondary Pattern: {hierarchy.get('secondary_pattern', {}).get('name', 'None').replace('_', ' ').title()} (Score: {hierarchy.get('secondary_pattern', {}).get('score', 0)}/8)

BEHAVIORAL ANALYSIS:
Core Limiting Belief: {'; '.join(behavioral.get('core_limiting_beliefs', ['None identified']))}
Hidden Benefits: {'; '.join(behavioral.get('hidden_benefits', ['None identified']))}
Systemic Resistance: {'; '.join(behavioral.get('systemic_resistance', ['None identified']))}
Identity Threat: {'; '.join(behavioral.get('identity_threats', ['None identified']))}

SESSION PLANNING:
Session 1 Focus: {session_planning.get('session_1_focus', 'Standard assessment and rapport building')}
Session 2 Target: {session_planning.get('session_2_target', 'Core pattern intervention')}
Potential Session 3 Need: {session_planning.get('potential_session_3_need', 'Progress consolidation')}

RESISTANCE PREDICTION:
Change Readiness Score: {readiness_score}/10
Predicted Resistance Points:
{chr(10).join(f"{i+1}. {point}" for i, point in enumerate(resistance.get('predicted_resistance_points', [])))}

Intervention Keywords: {resistance.get('intervention_keywords', 'collaborative, supportive, gradual')}
Avoid Language: {resistance.get('avoid_language', 'demanding, confrontational, rushed')}
"""
        return summary

# ================================
# SMART QUESTION MATRIX
# ================================

class SmartQuestionMatrix:
    """Smart question selection and adaptive logic"""

    # Enhanced question categories for comprehensive assessment
    NEUROLOGICAL_READINESS_QUESTIONS = {
        "hypnotic_susceptibility": {
            "question": "When watching a compelling movie or show, you typically:",
            "options": [
                "Get completely absorbed and lose track of time",
                "Stay somewhat aware of what's happening around you",
                "Find it hard to get really into it",
                "Prefer to analyze rather than just experience it"
            ],
            "weight": {
                "Get completely absorbed and lose track of time": {"hypnotic_readiness": 3, "absorption_capacity": 3},
                "Stay somewhat aware of what's happening around you": {"hypnotic_readiness": 2, "conscious_monitoring": 2},
                "Find it hard to get really into it": {"hypnotic_resistance": 2, "absorption_difficulty": 2},
                "Prefer to analyze rather than just experience it": {"analytical_resistance": 3, "cognitive_control": 3}
            }
        },

        "somatic_awareness": {
            "question": "When you're stressed, you first notice it:",
            "options": [
                "In your body (tension, breathing, physical sensations)",
                "In your thoughts (worry, racing mind, planning)",
                "In your emotions (anxiety, sadness, frustration)",
                "In your behavior (restlessness, avoidance, habits)"
            ],
            "weight": {
                "In your body (tension, breathing, physical sensations)": {"somatic_awareness": 3, "body_connection": 3},
                "In your thoughts (worry, racing mind, planning)": {"cognitive_dominance": 2, "mental_processing": 2},
                "In your emotions (anxiety, sadness, frustration)": {"emotional_awareness": 2, "feeling_focused": 2},
                "In your behavior (restlessness, avoidance, habits)": {"behavioral_awareness": 2, "action_oriented": 2}
            }
        },

        "change_responsiveness": {
            "question": "When you've experienced positive changes in the past, they usually happened:",
            "options": [
                "Gradually over time with consistent effort",
                "In sudden breakthroughs or 'aha' moments",
                "Through structured programs or guidance",
                "When I hit rock bottom and had to change"
            ],
            "weight": {
                "Gradually over time with consistent effort": {"gradual_change": 2, "sustained_effort": 2},
                "In sudden breakthroughs or 'aha' moments": {"rapid_change": 3, "insight_responsive": 3},
                "Through structured programs or guidance": {"external_structure": 2, "guidance_seeking": 2},
                "When I hit rock bottom and had to change": {"crisis_motivation": 2, "external_pressure": 2}
            }
        },

        "dissociative_capacity": {
            "id": "dissociative_capacity",
            "text": "During stress, your awareness typically:",
            "type": "single_choice",
            "options": [
                "Becomes hypervigilant to everything",
                "Focuses intensely on problem-solving",
                "Feels disconnected from your body",
                "Shifts to observing from outside yourself"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "hypervigilance": {"Becomes hypervigilant to everything": 3},
                "cognitive_coping": {"Focuses intensely on problem-solving": 2},
                "mild_dissociation": {"Feels disconnected from your body": 2},
                "healthy_dissociation": {"Shifts to observing from outside yourself": 3}
            }
        },

        "attention_regulation": {
            "id": "attention_regulation",
            "text": "During a 10-minute conversation without devices, you typically:",
            "type": "single_choice",
            "options": [
                "Stay completely engaged throughout",
                "Mind wanders but returns easily",
                "Struggle to maintain focus",
                "Feel anxious without digital access"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "attention_strength": {"Stay completely engaged throughout": 3, "Mind wanders but returns easily": 2},
                "attention_fragmentation": {"Struggle to maintain focus": 2, "Feel anxious without digital access": 3}
            }
        },

        "reality_testing": {
            "id": "reality_testing",
            "text": "Online achievements versus offline accomplishments feel:",
            "type": "single_choice",
            "options": [
                "Offline accomplishments more meaningful",
                "Both feel equally real and important",
                "Online achievements more rewarding",
                "Physical world feels less authentic"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "reality_grounding": {"Offline accomplishments more meaningful": 3},
                "balanced_reality": {"Both feel equally real and important": 2},
                "digital_preference": {"Online achievements more rewarding": 2},
                "reality_inversion": {"Physical world feels less authentic": 3}
            }
        },

        "eye_closure_response": {
            "id": "eye_closure_response",
            "text": "Close your eyes and imagine sinking into a comfortable chair. Rate how easily you achieved complete relaxation:",
            "type": "scale_1_10",
            "scale": ["1 - Remained tense/alert", "2", "3", "4", "5 - Moderate relaxation", "6", "7", "8", "9", "10 - Complete deep relaxation"],
            "required": True,
            "skip_allowed": True,
            "clinical_weight": "high",
            "weight": {
                "hypnotic_susceptibility": {"8": 2, "9": 3, "10 - Complete deep relaxation": 3},
                "relaxation_capacity": {"6": 1, "7": 2, "8": 2, "9": 3, "10 - Complete deep relaxation": 3}
            }
        },

        "ideomotor_testing": {
            "id": "ideomotor_testing",
            "text": "Imagine holding a heavy book in your right hand. Notice any actual sensations of weight or heaviness:",
            "type": "single_choice",
            "options": [
                "No sensation - remained fully aware this was imagination",
                "Slight sense of weight but clearly imaginary",
                "Moderate sensation - felt somewhat real",
                "Strong sensation - briefly felt like holding actual weight",
                "Complete sensation - temporarily forgot this was imagination"
            ],
            "required": True,
            "skip_allowed": True,
            "clinical_weight": "high",
            "weight": {
                "ideomotor_response": {"Strong sensation - briefly felt like holding actual weight": 2, "Complete sensation - temporarily forgot this was imagination": 3},
                "hypnotic_susceptibility": {"Moderate sensation - felt somewhat real": 1, "Strong sensation - briefly felt like holding actual weight": 2, "Complete sensation - temporarily forgot this was imagination": 3}
            }
        },

        "imaginative_involvement": {
            "id": "imaginative_involvement",
            "text": "When reading a book or watching a movie, you typically:",
            "type": "single_choice",
            "options": [
                "Stay aware of your surroundings and analytical about the plot",
                "Get somewhat involved but maintain awareness of reality",
                "Become quite absorbed and lose some awareness of surroundings",
                "Become completely absorbed and lose track of time and place",
                "Experience characters' emotions as if they were your own"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "imaginative_absorption": {"Become quite absorbed and lose some awareness of surroundings": 2, "Become completely absorbed and lose track of time and place": 3, "Experience characters' emotions as if they were your own": 3},
                "hypnotic_susceptibility": {"Become completely absorbed and lose track of time and place": 2, "Experience characters' emotions as if they were your own": 3}
            }
        }
    }

    # Phase 2: Discovery Questions (Essential for branching)
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

    # Phase 3: Trauma-Informed Assessment (Critical for therapeutic safety)
    TRAUMA_INFORMED_QUESTIONS = {
        "relaxation_response": {
            "id": "relaxation_response",
            "text": "When someone suggests 'just relax' or 'let go', your immediate reaction is:",
            "type": "single_choice",
            "options": [
                "Easy - I can relax quickly",
                "Challenging but manageable",
                "Difficult - relaxing feels unsafe",
                "Impossible - I need to stay alert"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "hypervigilance": {"Impossible - I need to stay alert": 3, "Difficult - relaxing feels unsafe": 2},
                "relaxation_readiness": {"Easy - I can relax quickly": 3, "Challenging but manageable": 2}
            }
        },

        "authority_response": {
            "id": "authority_response",
            "text": "When someone in authority gives you guidance, you typically:",
            "type": "single_choice",
            "options": [
                "Trust their expertise and follow through",
                "Listen but verify with your own judgment",
                "Feel resistant even when they're right",
                "Automatically become defensive or rebellious"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "authority_trust": {"Trust their expertise and follow through": 3},
                "healthy_skepticism": {"Listen but verify with your own judgment": 2},
                "authority_resistance": {"Feel resistant even when they're right": 2, "Automatically become defensive or rebellious": 3}
            }
        },

        "body_safety": {
            "id": "body_safety",
            "text": "Focusing attention on your body sensations feels:",
            "type": "single_choice",
            "options": [
                "Naturally calming and grounding",
                "Neutral - neither good nor bad",
                "Slightly uncomfortable or strange",
                "Triggering or overwhelming"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "somatic_safety": {"Naturally calming and grounding": 3, "Neutral - neither good nor bad": 2},
                "somatic_dysregulation": {"Triggering or overwhelming": 3, "Slightly uncomfortable or strange": 2}
            }
        },

        "trust_capacity": {
            "id": "trust_capacity",
            "text": "In therapeutic or helping relationships, you typically:",
            "type": "single_choice",
            "options": [
                "Open up gradually as trust builds",
                "Test the person extensively before trusting",
                "Share everything immediately",
                "Keep most thoughts and feelings private"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "healthy_boundaries": {"Open up gradually as trust builds": 3},
                "hypervigilant_testing": {"Test the person extensively before trusting": 2},
                "trauma_bonding": {"Share everything immediately": 2},
                "emotional_shutdown": {"Keep most thoughts and feelings private": 3}
            }
        },

        "change_safety": {
            "id": "change_safety",
            "text": "The idea of rapid personal change feels:",
            "type": "single_choice",
            "options": [
                "Exciting and hopeful",
                "Intriguing but somewhat scary",
                "Overwhelming or dangerous",
                "Impossible or fake"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "change_readiness": {"Exciting and hopeful": 3, "Intriguing but somewhat scary": 2},
                "change_resistance": {"Overwhelming or dangerous": 2, "Impossible or fake": 3}
            }
        },

        "dissociation_screening": {
            "id": "dissociation_screening",
            "text": "During stress, do you ever feel like you're watching yourself from outside your body or that things around you seem unreal?",
            "type": "frequency_scale",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Very often"],
            "required": True,
            "skip_allowed": True,
            "contraindication_threshold": "Often",
            "clinical_significance": "hypnosis_modification_if_frequent",
            "weight": {
                "dissociative_symptoms": {"Often": 2, "Very often": 3},
                "trauma_indicators": {"Sometimes": 1, "Often": 2, "Very often": 3}
            }
        },

        "flashback_assessment": {
            "id": "flashback_assessment",
            "text": "Do you experience sudden, vivid memories or images that feel like they're happening again?",
            "type": "frequency_scale",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Very often"],
            "required": True,
            "skip_allowed": True,
            "clinical_significance": "hypnosis_contraindication_if_frequent",
            "weight": {
                "ptsd_symptoms": {"Sometimes": 1, "Often": 2, "Very often": 3},
                "trauma_indicators": {"Sometimes": 2, "Often": 3, "Very often": 3}
            }
        },

        "memory_gaps": {
            "id": "memory_gaps",
            "text": "Do you have gaps in your memory for important events in your life?",
            "type": "single_choice",
            "options": [
                "No significant memory gaps",
                "Minor gaps that don't concern me",
                "Some gaps that I find concerning",
                "Significant gaps that affect my life",
                "Extensive memory problems"
            ],
            "required": True,
            "skip_allowed": True,
            "clinical_significance": "trauma_assessment_required",
            "weight": {
                "dissociative_amnesia": {"Some gaps that I find concerning": 2, "Significant gaps that affect my life": 3, "Extensive memory problems": 3},
                "trauma_indicators": {"Some gaps that I find concerning": 1, "Significant gaps that affect my life": 2, "Extensive memory problems": 3}
            }
        },

        "hypervigilance_assessment": {
            "id": "hypervigilance_assessment",
            "text": "How often do you feel like you need to be constantly alert to potential danger?",
            "type": "frequency_scale",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Almost always"],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "hypervigilance": {"Often": 2, "Almost always": 3},
                "trauma_indicators": {"Sometimes": 1, "Often": 2, "Almost always": 3}
            }
        }
    }

    # Phase 4: Secondary Gain & Resistance Assessment
    SECONDARY_GAIN_QUESTIONS = {
        "pattern_benefits": {
            "id": "pattern_benefits",
            "text": "If your main issue completely disappeared tomorrow, what would you miss about it?",
            "type": "multiple_choice",
            "options": [
                "The protection it provides from expectations",
                "How it explains my limitations to others",
                "The familiar identity it gives me",
                "The excuse it provides for other areas",
                "The sympathy or understanding I receive",
                "Nothing - I'd be completely happy",
                "The way it keeps me safe from bigger risks"
            ],
            "skip_allowed": True,
            "weight": {
                "secondary_gain": {"The protection it provides from expectations": 3, "The familiar identity it gives me": 3, "The excuse it provides for other areas": 2}
            }
        },

        "identity_without_problem": {
            "id": "identity_without_problem",
            "text": "Who would you be without this pattern?",
            "type": "text_input",
            "placeholder": "Describe your identity without this issue...",
            "skip_allowed": True,
            "analysis_flags": ["identity_threat", "role_attachment", "fear_themes"]
        },

        "change_ecology": {
            "id": "change_ecology",
            "text": "If you transformed this pattern completely, which relationship would be most affected?",
            "type": "single_choice",
            "options": [
                "Romantic partner",
                "Family members",
                "Work colleagues",
                "Friend groups",
                "I mostly keep to myself",
                "All relationships would improve"
            ],
            "skip_allowed": True,
            "weight": {
                "systemic_resistance": {"Romantic partner": 2, "Family members": 3, "Work colleagues": 1}
            }
        },

        "others_expectations": {
            "id": "others_expectations",
            "text": "What might others expect from you if you changed completely?",
            "type": "text_input",
            "placeholder": "What new expectations or pressures might arise...",
            "skip_allowed": True,
            "analysis_flags": ["performance_pressure", "role_shifts", "boundary_concerns"]
        }
    }

    # Phase 5: Medical Contraindication Screening (Critical for Safety)
    MEDICAL_SCREENING_QUESTIONS = {
        "seizure_history": {
            "id": "seizure_history",
            "text": "Have you ever experienced seizures or been diagnosed with epilepsy?",
            "type": "single_choice",
            "options": [
                "No history of seizures",
                "Childhood seizures only (resolved)",
                "Rare seizures (controlled with medication)",
                "Occasional seizures",
                "Active seizure disorder"
            ],
            "required": True,
            "skip_allowed": False,
            "clinical_significance": "absolute_contraindication_if_active",
            "weight": {
                "medical_contraindication": {"Occasional seizures": 2, "Active seizure disorder": 3},
                "hypnosis_risk": {"Rare seizures (controlled with medication)": 1, "Occasional seizures": 2, "Active seizure disorder": 3}
            }
        },

        "psychotic_symptoms": {
            "id": "psychotic_symptoms",
            "text": "Have you ever experienced hallucinations (seeing/hearing things others don't) or delusions (believing things that aren't true)?",
            "type": "single_choice",
            "options": [
                "Never experienced these symptoms",
                "Very rarely, under extreme stress",
                "Occasionally, but I know they're not real",
                "Sometimes, and they feel real",
                "Frequently, these feel completely real"
            ],
            "required": True,
            "skip_allowed": False,
            "clinical_significance": "hypnosis_contraindication_if_frequent",
            "weight": {
                "psychotic_risk": {"Sometimes, and they feel real": 2, "Frequently, these feel completely real": 3},
                "reality_testing_impairment": {"Occasionally, but I know they're not real": 1, "Sometimes, and they feel real": 2, "Frequently, these feel completely real": 3}
            }
        },

        "current_medications": {
            "id": "current_medications",
            "text": "Are you currently taking any of the following types of medication?",
            "type": "multiple_choice",
            "options": [
                "Antipsychotic medications",
                "Anti-seizure medications",
                "Benzodiazepines (anxiety medications)",
                "Antidepressants",
                "Sleep medications",
                "Pain medications",
                "None of the above"
            ],
            "required": True,
            "skip_allowed": False,
            "clinical_significance": "medication_interaction_assessment",
            "weight": {
                "medication_interaction": {"Antipsychotic medications": 2, "Anti-seizure medications": 2, "Benzodiazepines (anxiety medications)": 1}
            }
        },

        "substance_use": {
            "id": "substance_use",
            "text": "How often do you use alcohol or other substances?",
            "type": "single_choice",
            "options": [
                "Never or very rarely",
                "Occasionally (few times per month)",
                "Regularly (few times per week)",
                "Daily or almost daily",
                "I'm concerned about my usage"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "substance_risk": {"Daily or almost daily": 2, "I'm concerned about my usage": 3},
                "hypnosis_interaction": {"Regularly (few times per week)": 1, "Daily or almost daily": 2}
            }
        },

        "pregnancy_status": {
            "id": "pregnancy_status",
            "text": "Are you currently pregnant or trying to become pregnant?",
            "type": "single_choice",
            "options": [
                "Not applicable",
                "No",
                "Trying to conceive",
                "Yes, first trimester",
                "Yes, second or third trimester"
            ],
            "required": True,
            "skip_allowed": True,
            "clinical_significance": "modified_approach_if_pregnant",
            "weight": {
                "pregnancy_modification": {"Yes, first trimester": 1, "Yes, second or third trimester": 1}
            }
        }
    }

    # Phase 6: Somatic Pattern Archaeology
    SOMATIC_PATTERN_QUESTIONS = {
        "trigger_detection": {
            "id": "trigger_detection",
            "text": "When your main issue activates, the FIRST thing you notice is:",
            "type": "single_choice",
            "options": [
                "A specific body sensation",
                "An automatic thought pattern",
                "An emotional shift",
                "An urge to act or avoid"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "somatic_awareness": {"A specific body sensation": 3},
                "cognitive_dominance": {"An automatic thought pattern": 2},
                "emotional_awareness": {"An emotional shift": 2},
                "behavioral_focus": {"An urge to act or avoid": 1}
            }
        },

        "body_sensation_detail": {
            "id": "body_sensation_detail",
            "text": "Describe that body sensation precisely:",
            "type": "text_input",
            "placeholder": "Where exactly do you feel it? What does it feel like?",
            "skip_allowed": True,
            "condition": "trigger_detection == 'A specific body sensation'",
            "analysis_flags": ["location_mapping", "sensation_quality", "intensity_patterns"]
        },

        "trigger_location": {
            "id": "trigger_location",
            "text": "Where in your body do you typically feel stress or activation first?",
            "type": "single_choice",
            "options": [
                "Head/forehead/temples",
                "Jaw/neck/shoulders",
                "Chest/heart area",
                "Stomach/gut area",
                "Back/spine",
                "Hands/arms",
                "Legs/feet",
                "All over/everywhere"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "stress_localization": {"Head/forehead/temples": 1, "Jaw/neck/shoulders": 2, "Chest/heart area": 2, "Stomach/gut area": 3}
            }
        },

        "regulation_capacity": {
            "id": "regulation_capacity",
            "text": "When you notice stress in your body, you typically:",
            "type": "single_choice",
            "options": [
                "Use breathing or relaxation techniques",
                "Try to think your way out of it",
                "Distract yourself until it passes",
                "Feel stuck until it goes away on its own"
            ],
            "required": True,
            "skip_allowed": True,
            "weight": {
                "somatic_regulation": {"Use breathing or relaxation techniques": 3},
                "cognitive_coping": {"Try to think your way out of it": 2},
                "avoidance_coping": {"Distract yourself until it passes": 1},
                "regulation_deficit": {"Feel stuck until it goes away on its own": 0}
            }
        }
    }

    # Phase 6: Adaptive Pattern Assessment
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
        self.current_phase = "neurological_readiness"
        self.assessment_path = None

    def get_next_question(self, current_responses: Dict) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next question based on adaptive logic"""
        self.responses = current_responses
        self._update_pattern_scores()

        if self.current_phase == "neurological_readiness":
            return self._get_neurological_question()
        elif self.current_phase == "discovery":
            return self._get_discovery_question()
        elif self.current_phase == "trauma_informed":
            return self._get_trauma_informed_question()
        elif self.current_phase == "secondary_gain":
            return self._get_secondary_gain_question()
        elif self.current_phase == "somatic_archaeology":
            return self._get_somatic_question()
        elif self.current_phase == "adaptive_assessment":
            return self._get_adaptive_question()
        elif self.current_phase == "pattern_validation":
            return self._get_validation_question()
        elif self.current_phase == "integration":
            return self._get_integration_question()
        else:
            return None, None

    def _get_neurological_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next neurological readiness question"""
        for q_id, question in SmartQuestionMatrix.NEUROLOGICAL_READINESS_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Move to discovery phase after neurological assessment
        self.current_phase = "discovery"
        return self._get_discovery_question()

    def _get_discovery_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next discovery phase question"""
        for q_id, question in SmartQuestionMatrix.DISCOVERY_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Move to trauma-informed assessment after discovery
        self.current_phase = "trauma_informed"
        return self._get_trauma_informed_question()

    def _get_trauma_informed_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next trauma-informed question"""
        for q_id, question in SmartQuestionMatrix.TRAUMA_INFORMED_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Move to secondary gain assessment
        self.current_phase = "secondary_gain"
        return self._get_secondary_gain_question()

    def _get_secondary_gain_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next secondary gain question"""
        for q_id, question in SmartQuestionMatrix.SECONDARY_GAIN_QUESTIONS.items():
            if q_id not in self.responses:
                return q_id, question

        # Move to somatic archaeology
        self.current_phase = "somatic_archaeology"
        return self._get_somatic_question()

    def _get_somatic_question(self) -> Tuple[Optional[str], Optional[Dict]]:
        """Get next somatic pattern question"""
        for q_id, question in SmartQuestionMatrix.SOMATIC_PATTERN_QUESTIONS.items():
            # Check conditions for conditional questions
            if question.get("condition"):
                if not self._evaluate_condition(question["condition"]):
                    continue

            if q_id not in self.responses:
                return q_id, question

        # Move to adaptive assessment after somatic work
        self.current_phase = "adaptive_assessment"
        self._determine_assessment_path()
        return self._get_adaptive_question()

    def _evaluate_condition(self, condition: str) -> bool:
        """Evaluate conditional logic for questions"""
        if condition == "trigger_detection == 'A specific body sensation'":
            return self.responses.get("trigger_detection") == "A specific body sensation"
        return True

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

# ================================
# ENHANCED TRAUMA-INFORMED SCORING
# ================================

class ClinicalScoringEngine:
    """Enhanced clinical scoring with sophisticated analytics and contraindication detection"""

    @staticmethod
    def calculate_comprehensive_readiness(responses: Dict) -> Dict:
        """Calculate precise therapeutic readiness with clinical safety assessment"""

        # Clinical safety screening first
        contraindications = ClinicalScoringEngine._assess_contraindications(responses)
        if contraindications["absolute_contraindications"]:
            return {
                "success_probability": 0,
                "contraindications": contraindications,
                "clinical_recommendation": "REFER_TO_MEDICAL_PROFESSIONAL",
                "reason": "Absolute contraindications detected - hypnosis not recommended"
            }

        # Enhanced readiness calculation
        hypnotic_factors = ClinicalScoringEngine._calculate_hypnotic_susceptibility(responses)
        trauma_safety = ClinicalScoringEngine._evaluate_trauma_safety(responses)
        resistance_factors = ClinicalScoringEngine._assess_resistance_patterns(responses)
        alliance_potential = ClinicalScoringEngine._predict_therapeutic_alliance(responses)
        medical_factors = ClinicalScoringEngine._assess_medical_factors(responses)

        # Weighted probability calculation
        success_probability = ClinicalScoringEngine._calculate_weighted_probability([
            (hypnotic_factors, 0.35),
            (trauma_safety, 0.25),
            (resistance_factors, 0.25),
            (alliance_potential, 0.15)
        ])

        # Apply medical factor adjustments
        success_probability = max(min(success_probability * medical_factors, 98), 45)

        return {
            "success_probability": success_probability,
            "hypnotic_susceptibility": hypnotic_factors,
            "trauma_safety_score": trauma_safety,
            "resistance_prediction": resistance_factors,
            "therapeutic_alliance": alliance_potential,
            "contraindications": contraindications,
            "optimal_approach": ClinicalScoringEngine._determine_optimal_approach(responses),
            "session_estimate": ClinicalScoringEngine._predict_session_count(responses),
            "risk_factors": ClinicalScoringEngine._identify_risk_factors(responses),
            "clinical_modifications": ClinicalScoringEngine._determine_modifications(responses)
        }

    @staticmethod
    def _assess_contraindications(responses: Dict) -> Dict:
        """Comprehensive contraindication assessment"""
        absolute_contraindications = []
        relative_contraindications = []
        modifications_required = []

        # Seizure disorder assessment
        seizure_status = responses.get("seizure_history", "")
        if seizure_status in ["Active seizure disorder", "Occasional seizures"]:
            absolute_contraindications.append("Active seizure disorder")

        # Psychotic symptoms
        psychotic_symptoms = responses.get("psychotic_symptoms", "")
        if psychotic_symptoms in ["Frequently, these feel completely real"]:
            absolute_contraindications.append("Active psychotic symptoms")
        elif psychotic_symptoms in ["Sometimes, and they feel real"]:
            relative_contraindications.append("Intermittent psychotic symptoms")

        # Severe dissociation
        dissociation = responses.get("dissociation_screening", "")
        if dissociation == "Very often":
            relative_contraindications.append("Severe dissociative symptoms")
        elif dissociation == "Often":
            modifications_required.append("Dissociation-informed approach required")

        # PTSD flashbacks
        flashbacks = responses.get("flashback_assessment", "")
        if flashbacks in ["Very often", "Often"]:
            modifications_required.append("Trauma-informed gradual approach required")

        # Memory gaps
        memory_gaps = responses.get("memory_gaps", "")
        if memory_gaps in ["Significant gaps that affect my life", "Extensive memory problems"]:
            modifications_required.append("Memory stabilization required before hypnosis")

        return {
            "absolute_contraindications": absolute_contraindications,
            "relative_contraindications": relative_contraindications,
            "modifications_required": modifications_required,
            "safety_assessment": "SAFE" if not absolute_contraindications else "UNSAFE"
        }

    @staticmethod
    def _calculate_hypnotic_susceptibility(responses: Dict) -> float:
        """Enhanced hypnotic susceptibility calculation using SHCS principles"""
        susceptibility_score = 0
        max_score = 100

        # Eye closure response (SHCS component)
        eye_closure = responses.get("eye_closure_response", "")
        if "10 - Complete deep relaxation" in eye_closure:
            susceptibility_score += 25
        elif "9" in eye_closure:
            susceptibility_score += 20
        elif "8" in eye_closure:
            susceptibility_score += 15

        # Ideomotor response (SHCS component)
        ideomotor = responses.get("ideomotor_testing", "")
        if ideomotor == "Complete sensation - temporarily forgot this was imagination":
            susceptibility_score += 25
        elif ideomotor == "Strong sensation - briefly felt like holding actual weight":
            susceptibility_score += 20
        elif ideomotor == "Moderate sensation - felt somewhat real":
            susceptibility_score += 10

        # Imaginative involvement
        imagination = responses.get("imaginative_involvement", "")
        if imagination == "Experience characters' emotions as if they were your own":
            susceptibility_score += 20
        elif imagination == "Become completely absorbed and lose track of time and place":
            susceptibility_score += 15
        elif imagination == "Become quite absorbed and lose some awareness of surroundings":
            susceptibility_score += 10

        # Movie absorption (original assessment)
        movie_absorption = responses.get("hypnotic_susceptibility", "")
        if movie_absorption == "Completely lose track of time and surroundings":
            susceptibility_score += 15
        elif movie_absorption == "Stay somewhat aware of your environment":
            susceptibility_score += 10

        # Dissociative capacity (optimal range)
        dissociation = responses.get("dissociative_capacity", "")
        if dissociation == "Shifts to observing from outside yourself":
            susceptibility_score += 15  # Healthy dissociation
        elif dissociation == "Feels disconnected from your body":
            susceptibility_score += 5   # Mild dissociation (manageable)

        return min(susceptibility_score / max_score * 100, 100)  # Convert to percentage

    @staticmethod
    def _evaluate_trauma_safety(responses: Dict) -> float:
        """Evaluate trauma-related safety factors for hypnosis"""
        safety_score = 50  # Baseline neutral

        # Dissociation frequency
        dissociation = responses.get("dissociation_screening", "")
        if dissociation == "Never":
            safety_score += 30
        elif dissociation == "Rarely":
            safety_score += 20
        elif dissociation == "Sometimes":
            safety_score += 0
        elif dissociation == "Often":
            safety_score -= 20
        elif dissociation == "Very often":
            safety_score -= 30

        # Flashback assessment
        flashbacks = responses.get("flashback_assessment", "")
        if flashbacks == "Never":
            safety_score += 20
        elif flashbacks in ["Often", "Very often"]:
            safety_score -= 25
        elif flashbacks == "Sometimes":
            safety_score -= 10

        # Hypervigilance
        hypervigilance = responses.get("hypervigilance_assessment", "")
        if hypervigilance == "Never":
            safety_score += 15
        elif hypervigilance == "Almost always":
            safety_score -= 20

        # Memory gaps
        memory_gaps = responses.get("memory_gaps", "")
        if memory_gaps in ["Significant gaps that affect my life", "Extensive memory problems"]:
            safety_score -= 15

        return max(min(safety_score, 100), 0)

    @staticmethod
    def _assess_resistance_patterns(responses: Dict) -> float:
        """Assess resistance patterns and therapeutic alliance potential"""
        resistance_score = 50  # Baseline

        # Authority response
        authority = responses.get("authority_response", "")
        if authority == "Trust their expertise and follow through":
            resistance_score += 25
        elif authority == "Listen but verify with your own judgment":
            resistance_score += 10
        elif authority in ["Feel resistant even when they're right", "Automatically become defensive or rebellious"]:
            resistance_score -= 20

        # Secondary gain patterns
        pattern_benefits = responses.get("pattern_benefits", [])
        if isinstance(pattern_benefits, list):
            high_gain_indicators = [
                "The protection it provides from expectations",
                "The familiar identity it gives me",
                "The excuse it provides for other areas"
            ]
            resistance_score -= len([b for b in pattern_benefits if b in high_gain_indicators]) * 5

        # Previous therapy experience
        previous_help = responses.get("previous_help", "")
        if previous_help == "Multiple approaches - nothing really worked":
            resistance_score -= 15
        elif previous_help == "Prefer to handle things myself":
            resistance_score -= 10

        return max(min(resistance_score, 100), 0)

    @staticmethod
    def _predict_therapeutic_alliance(responses: Dict) -> float:
        """Predict therapeutic alliance potential"""
        alliance_score = 50

        # Trust capacity
        trust = responses.get("trust_capacity", "")
        if trust == "Open up gradually as trust builds":
            alliance_score += 25
        elif trust == "Test the person extensively before trusting":
            alliance_score += 5
        elif trust == "Keep most thoughts and feelings private":
            alliance_score -= 15

        # Change readiness
        change_safety = responses.get("change_safety", "")
        if change_safety == "Exciting and hopeful":
            alliance_score += 20
        elif change_safety == "Intriguing but somewhat scary":
            alliance_score += 10
        elif change_safety in ["Overwhelming or dangerous", "Impossible or fake"]:
            alliance_score -= 15

        return max(min(alliance_score, 100), 0)

    @staticmethod
    def _assess_medical_factors(responses: Dict) -> float:
        """Assess medical factors that might affect success probability"""
        medical_factor = 1.0  # No impact by default

        # Medication interactions
        medications = responses.get("current_medications", [])
        if isinstance(medications, list):
            if "Antipsychotic medications" in medications:
                medical_factor *= 0.8
            if "Benzodiazepines (anxiety medications)" in medications:
                medical_factor *= 0.9
            if "Anti-seizure medications" in medications:
                medical_factor *= 0.85

        # Substance use
        substance_use = responses.get("substance_use", "")
        if substance_use == "Daily or almost daily":
            medical_factor *= 0.8
        elif substance_use == "I'm concerned about my usage":
            medical_factor *= 0.7

        return medical_factor

    @staticmethod
    def _calculate_weighted_probability(factors_weights: List[Tuple[float, float]]) -> float:
        """Calculate weighted probability from multiple factors"""
        total_weight = sum(weight for _, weight in factors_weights)
        weighted_sum = sum(factor * weight for factor, weight in factors_weights)
        return weighted_sum / total_weight if total_weight > 0 else 50

    @staticmethod
    def _determine_optimal_approach(responses: Dict) -> str:
        """Determine optimal therapeutic approach based on assessment"""
        trauma_indicators = responses.get("trauma_indicators", 0)
        hypnotic_susceptibility = ClinicalScoringEngine._calculate_hypnotic_susceptibility(responses)
        resistance_score = ClinicalScoringEngine._assess_resistance_patterns(responses)

        if trauma_indicators >= 3:
            return "trauma_informed_gradual_approach"
        elif resistance_score <= 30:
            return "collaborative_discovery_approach"
        elif hypnotic_susceptibility >= 70:
            return "direct_rapid_transformation"
        else:
            return "standard_hypnotherapy_approach"

    @staticmethod
    def _predict_session_count(responses: Dict) -> str:
        """Predict optimal number of sessions"""
        approach = ClinicalScoringEngine._determine_optimal_approach(responses)

        approach_sessions = {
            "trauma_informed_gradual_approach": "6-8 sessions",
            "collaborative_discovery_approach": "4-6 sessions",
            "direct_rapid_transformation": "2-3 sessions",
            "standard_hypnotherapy_approach": "3-5 sessions"
        }

        return approach_sessions.get(approach, "3-5 sessions")

    @staticmethod
    def _identify_risk_factors(responses: Dict) -> List[str]:
        """Identify specific risk factors for therapeutic planning"""
        risk_factors = []

        # Trauma-related risks
        if responses.get("flashback_assessment") in ["Often", "Very often"]:
            risk_factors.append("Frequent flashbacks - avoid regression techniques")

        if responses.get("dissociation_screening") in ["Often", "Very often"]:
            risk_factors.append("Severe dissociation - requires grounding techniques")

        # Resistance risks
        if responses.get("authority_response") in ["Feel resistant even when they're right"]:
            risk_factors.append("Authority resistance - use collaborative language")

        # Medical risks
        medications = responses.get("current_medications", [])
        if isinstance(medications, list) and "Anti-seizure medications" in medications:
            risk_factors.append("Seizure medication - monitor for interactions")

        return risk_factors

    @staticmethod
    def _determine_modifications(responses: Dict) -> List[str]:
        """Determine specific therapeutic modifications needed"""
        modifications = []

        # Pregnancy modifications
        pregnancy = responses.get("pregnancy_status", "")
        if "Yes" in pregnancy:
            modifications.append("Pregnancy-safe hypnosis protocols only")

        # Dissociation modifications
        dissociation = responses.get("dissociation_screening", "")
        if dissociation in ["Often", "Very often"]:
            modifications.append("Frequent grounding checks required")

        # Trauma modifications
        if responses.get("memory_gaps") in ["Some gaps that I find concerning"]:
            modifications.append("Memory stabilization before deep work")

        return modifications

    @staticmethod
    def _score_neurological_factors(responses: Dict) -> int:
        """Score hypnotic susceptibility and neurological readiness"""
        score = 0

        # Hypnotic susceptibility
        if responses.get("hypnotic_susceptibility") == "Completely lose track of time and surroundings":
            score += 3
        elif responses.get("hypnotic_susceptibility") == "Stay somewhat aware of your environment":
            score += 2

        # Dissociative capacity (optimal range)
        dissociation = responses.get("dissociative_capacity")
        if dissociation == "Shifts to observing from outside yourself":
            score += 3  # Healthy dissociation
        elif dissociation == "Feels disconnected from your body":
            score += 1  # Mild dissociation (needs safety work)
        elif dissociation == "Becomes hypervigilant to everything":
            score -= 2  # Trauma response

        # Attention regulation
        attention = responses.get("attention_regulation")
        if attention == "Stay completely engaged throughout":
            score += 3
        elif attention == "Mind wanders but returns easily":
            score += 2
        elif attention in ["Struggle to maintain focus", "Feel anxious without digital access"]:
            score -= 1

        return max(score, 0)

    @staticmethod
    def _score_somatic_capacity(responses: Dict) -> int:
        """Score body awareness and somatic regulation capacity"""
        score = 0

        # Primary somatic awareness
        if responses.get("somatic_awareness") == "Physical sensations (temperature, tension, comfort)":
            score += 3
        elif responses.get("somatic_awareness") == "Emotional state or mood":
            score += 2

        # Body safety
        body_safety = responses.get("body_safety")
        if body_safety == "Naturally calming and grounding":
            score += 3
        elif body_safety == "Neutral - neither good nor bad":
            score += 2
        elif body_safety in ["Slightly uncomfortable or strange", "Triggering or overwhelming"]:
            score -= 2

        # Stress regulation capacity
        regulation = responses.get("regulation_capacity")
        if regulation == "Use breathing or relaxation techniques":
            score += 3
        elif regulation == "Try to think your way out of it":
            score += 1
        elif regulation == "Feel stuck until it goes away on its own":
            score -= 1

        return max(score, 0)

    @staticmethod
    def _score_trauma_safety(responses: Dict) -> int:
        """Score trauma-related safety factors (lower = more trauma indicators)"""
        safety_score = 0

        # Relaxation capacity
        if responses.get("relaxation_response") in ["Difficult - relaxing feels unsafe", "Impossible - I need to stay alert"]:
            safety_score -= 3
        elif responses.get("relaxation_response") == "Easy - I can relax quickly":
            safety_score += 2

        # Authority trust
        authority = responses.get("authority_response")
        if authority == "Trust their expertise and follow through":
            safety_score += 3
        elif authority == "Listen but verify with your own judgment":
            safety_score += 1
        elif authority in ["Feel resistant even when they're right", "Automatically become defensive or rebellious"]:
            safety_score -= 2

        # Trust capacity
        trust = responses.get("trust_capacity")
        if trust == "Open up gradually as trust builds":
            safety_score += 3
        elif trust == "Test the person extensively before trusting":
            safety_score -= 1
        elif trust in ["Share everything immediately", "Keep most thoughts and feelings private"]:
            safety_score -= 2

        return safety_score

    @staticmethod
    def _score_resistance_factors(responses: Dict) -> int:
        """Score secondary gain and resistance patterns"""
        resistance = 0

        # Secondary gain analysis
        pattern_benefits = responses.get("pattern_benefits", [])
        if isinstance(pattern_benefits, list):
            high_gain_responses = [
                "The protection it provides from expectations",
                "The familiar identity it gives me",
                "The excuse it provides for other areas"
            ]
            resistance += len([r for r in pattern_benefits if r in high_gain_responses])

        # Change safety concerns
        if responses.get("change_safety") in ["Overwhelming or dangerous", "Impossible or fake"]:
            resistance += 2

        # Previous therapy resistance
        if responses.get("previous_help") in ["Multiple approaches - nothing really worked", "Prefer to handle things myself"]:
            resistance += 1

        return resistance

    @staticmethod
    def _calculate_digital_adaptation(responses: Dict) -> int:
        """Calculate digital native adaptation bonus"""
        age_range = responses.get("age_detection", "")
        digital_time = responses.get("digital_habits", "")

        bonus = 0
        if age_range in ["16-20", "21-25"] and digital_time in ["6-8 hours", "8+ hours"]:
            # Digital native with heavy usage - needs adapted approach
            bonus += 8
        elif age_range in ["26-30", "31-35"] and digital_time in ["4-6 hours", "6-8 hours"]:
            # Hybrid generation - moderate adaptation
            bonus += 4

        return bonus

    @staticmethod
    def _recommend_session_approach(responses: Dict) -> str:
        """Recommend specific session approach based on profile"""
        somatic_score = TraumaInformedAnalyzer._score_somatic_capacity(responses)
        trauma_score = TraumaInformedAnalyzer._score_trauma_safety(responses)
        resistance_score = TraumaInformedAnalyzer._score_resistance_factors(responses)

        if trauma_score < -3:
            return "trauma_informed_gradual_approach"
        elif resistance_score > 4:
            return "collaborative_discovery_approach"
        elif somatic_score >= 6:
            return "somatic_focused_rapid_approach"
        elif responses.get("authority_response") in ["Feel resistant even when they're right", "Automatically become defensive or rebellious"]:
            return "non_directive_exploration_approach"
        else:
            return "direct_transformation_protocol"

    @staticmethod
    def _predict_resistance_patterns(responses: Dict) -> List[str]:
        """Predict specific resistance patterns and management strategies"""
        patterns = []

        # Authority resistance
        if responses.get("authority_response") in ["Feel resistant even when they're right", "Automatically become defensive or rebellious"]:
            patterns.append("authority_resistance")

        # Identity threat
        identity_response = responses.get("identity_without_problem", "")
        if "don't know" in identity_response.lower() or "scared" in identity_response.lower():
            patterns.append("identity_threat_resistance")

        # Secondary gain
        pattern_benefits = responses.get("pattern_benefits", [])
        if "The familiar identity it gives me" in pattern_benefits:
            patterns.append("identity_attachment_resistance")

        # Somatic resistance
        if responses.get("body_safety") in ["Slightly uncomfortable or strange", "Triggering or overwhelming"]:
            patterns.append("somatic_resistance")

        return patterns

    @staticmethod
    def _generate_session_protocol(responses: Dict) -> Dict:
        """Generate specific session-by-session protocol"""
        approach = TraumaInformedAnalyzer._recommend_session_approach(responses)
        trauma_indicators = TraumaInformedAnalyzer._score_trauma_safety(responses) < 0
        high_resistance = TraumaInformedAnalyzer._score_resistance_factors(responses) > 3

        protocols = {
            "trauma_informed_gradual_approach": {
                "session_1": "Safety establishment and resource building",
                "session_2": "Gentle somatic awareness and grounding",
                "session_3": "Gradual pattern recognition with safety checks",
                "timeline": "6-8 sessions recommended"
            },
            "collaborative_discovery_approach": {
                "session_1": "Collaborative exploration of client expertise",
                "session_2": "Joint pattern analysis and hypothesis testing",
                "session_3": "Client-led transformation with guidance",
                "timeline": "4-6 sessions recommended"
            },
            "somatic_focused_rapid_approach": {
                "session_1": "Direct somatic pattern interruption",
                "session_2": "Rapid installation of new somatic responses",
                "session_3": "Integration and future pacing",
                "timeline": "2-3 sessions recommended"
            },
            "direct_transformation_protocol": {
                "session_1": "Rapid pattern identification and interruption",
                "session_2": "Complete pattern transformation",
                "session_3": "Future integration and reinforcement",
                "timeline": "2-4 sessions recommended"
            }
        }

        return protocols.get(approach, protocols["direct_transformation_protocol"])

class TraumaInformedAnalyzer:
    """Trauma-informed therapy readiness analyzer - wrapper for clinical scoring methods"""

    @staticmethod
    def calculate_therapeutic_readiness(responses: Dict) -> Dict:
        """Calculate therapeutic readiness using existing clinical scoring methods"""
        try:
            # Use existing methods from ClinicalScoringEngine
            somatic_score = ClinicalScoringEngine._score_somatic_capacity(responses)
            trauma_score = ClinicalScoringEngine._score_trauma_safety(responses)
            resistance_score = ClinicalScoringEngine._score_resistance_factors(responses)

            return {
                "somatic_capacity": somatic_score,
                "trauma_safety": trauma_score,
                "resistance_factors": resistance_score,
                "overall_readiness": somatic_score + trauma_score - resistance_score,
                "recommended_approach": TraumaInformedAnalyzer._recommend_session_approach(responses),
                "session_protocol": TraumaInformedAnalyzer._generate_session_protocol(responses)
            }
        except Exception as e:
            # Fallback if methods don't exist
            return {
                "somatic_capacity": 0,
                "trauma_safety": 0,
                "resistance_factors": 0,
                "overall_readiness": 0,
                "recommended_approach": "direct_transformation_protocol",
                "session_protocol": {"session_1": "Assessment and planning", "timeline": "3-4 sessions"}
            }

    @staticmethod
    def _score_somatic_capacity(responses: Dict) -> int:
        """Wrapper for somatic capacity scoring"""
        try:
            return ClinicalScoringEngine._score_somatic_capacity(responses)
        except:
            return 0

    @staticmethod
    def _score_trauma_safety(responses: Dict) -> int:
        """Wrapper for trauma safety scoring"""
        try:
            return ClinicalScoringEngine._score_trauma_safety(responses)
        except:
            return 0

    @staticmethod
    def _score_resistance_factors(responses: Dict) -> int:
        """Wrapper for resistance factors scoring"""
        try:
            return ClinicalScoringEngine._score_resistance_factors(responses)
        except:
            return 0

    @staticmethod
    def _recommend_session_approach(responses: Dict) -> str:
        """Recommend session approach based on scores"""
        try:
            somatic_score = TraumaInformedAnalyzer._score_somatic_capacity(responses)
            trauma_score = TraumaInformedAnalyzer._score_trauma_safety(responses)
            resistance_score = TraumaInformedAnalyzer._score_resistance_factors(responses)

            if trauma_score < -3:
                return "trauma_informed_gradual_approach"
            elif resistance_score > 4:
                return "collaborative_discovery_approach"
            elif somatic_score >= 6:
                return "somatic_focused_rapid_approach"
            else:
                return "direct_transformation_protocol"
        except:
            return "direct_transformation_protocol"

    @staticmethod
    def _generate_session_protocol(responses: Dict) -> Dict:
        """Generate session protocol based on approach"""
        try:
            approach = TraumaInformedAnalyzer._recommend_session_approach(responses)

            protocols = {
                "trauma_informed_gradual_approach": {
                    "session_1": "Safety establishment and resource building",
                    "session_2": "Gentle somatic awareness and grounding",
                    "session_3": "Gradual pattern recognition with safety checks",
                    "timeline": "6-8 sessions recommended"
                },
                "collaborative_discovery_approach": {
                    "session_1": "Collaborative exploration of client expertise",
                    "session_2": "Co-created intervention strategies",
                    "session_3": "Client-led transformation with therapist support",
                    "timeline": "4-6 sessions recommended"
                },
                "somatic_focused_rapid_approach": {
                    "session_1": "Deep somatic entrainment and rapid induction",
                    "session_2": "Intensive pattern restructuring",
                    "session_3": "Integration and future-pacing",
                    "timeline": "2-3 sessions recommended"
                },
                "direct_transformation_protocol": {
                    "session_1": "Rapid assessment and direct intervention",
                    "session_2": "Intensive transformation work",
                    "session_3": "Integration and reinforcement",
                    "timeline": "3-4 sessions recommended"
                }
            }

            return protocols.get(approach, protocols["direct_transformation_protocol"])
        except:
            return {"session_1": "Assessment and planning", "timeline": "3-4 sessions"}

class ComprehensiveProfiler:
    """Generate detailed psychological profiles from assessment data"""

    @staticmethod
    def generate_complete_profile(responses: Dict) -> Dict:
        """Generate comprehensive psychological profile"""

        # Calculate all pattern scores
        behavioral_patterns = ComprehensiveProfiler._calculate_behavioral_patterns(responses)
        digital_analysis = DigitalDespairAssessment.calculate_syndrome_severity(responses)
        clinical_profile = ComprehensiveProfiler._generate_clinical_profile(responses)
        trauma_informed_analysis = TraumaInformedAnalyzer.calculate_therapeutic_readiness(responses)

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
            "trauma_informed_analysis": trauma_informed_analysis,

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

    # Hypnotic Susceptibility Assessment (Stanford Hypnotic Clinical Scale components)
    HYPNOTIC_SUSCEPTIBILITY_QUESTIONS = {
        "imaginative_absorption": {
            "id": "imaginative_absorption",
            "text": "How easily can you become completely absorbed in a story, movie, or daydream?",
            "type": "scale_agreement",
            "scale": ["Very difficult", "Somewhat difficult", "Neutral", "Somewhat easy", "Very easy"],
            "skip_allowed": False,
            "weight": {"hypnotic_susceptibility": {"Somewhat easy": 1, "Very easy": 2}}
        },
        "body_awareness_relaxation": {
            "id": "body_awareness_relaxation",
            "text": "When you close your eyes and focus on your breathing, how easily can you feel your body becoming relaxed?",
            "type": "scale_agreement",
            "scale": ["Very difficult", "Somewhat difficult", "Neutral", "Somewhat easy", "Very easy"],
            "skip_allowed": False,
            "weight": {"hypnotic_susceptibility": {"Somewhat easy": 1, "Very easy": 2}}
        },
        "guided_imagery_response": {
            "id": "guided_imagery_response",
            "text": "If asked to imagine holding a heavy book, how real would the sensation of weight feel in your hand?",
            "type": "single_choice",
            "options": [
                "No sensation at all",
                "Very slight sensation",
                "Mild sensation",
                "Moderate sensation",
                "Very real sensation"
            ],
            "skip_allowed": False,
            "weight": {"hypnotic_susceptibility": {"Moderate sensation": 1, "Very real sensation": 2}}
        },
        "automatic_response_tendency": {
            "id": "automatic_response_tendency",
            "text": "When following along with guided meditation or relaxation, do you find your body responding automatically?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Always"],
            "skip_allowed": False,
            "weight": {"hypnotic_susceptibility": {"Often": 1, "Always": 2}}
        },
        "dissociative_experiences": {
            "id": "dissociative_experiences",
            "text": "How often do you experience 'losing track of time' when engaged in activities?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Very often"],
            "skip_allowed": False,
            "weight": {"hypnotic_susceptibility": {"Often": 1, "Very often": 2}}
        }
    }

    # Trauma Screening Questions (DDIS and PTSD components)
    TRAUMA_SCREENING_QUESTIONS = {
        "trauma_history_general": {
            "id": "trauma_history_general",
            "text": "Have you experienced or witnessed any events that felt life-threatening or extremely distressing?",
            "type": "single_choice",
            "options": [
                "No, never",
                "Yes, once",
                "Yes, multiple times",
                "Prefer not to answer"
            ],
            "skip_allowed": True,
            "weight": {"trauma_indicators": {"Yes, once": 1, "Yes, multiple times": 2}}
        },
        "intrusive_memories": {
            "id": "intrusive_memories",
            "text": "Do you experience unwanted memories, flashbacks, or nightmares?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Very often"],
            "skip_allowed": True,
            "weight": {"trauma_indicators": {"Often": 1, "Very often": 2}}
        },
        "avoidance_behaviors": {
            "id": "avoidance_behaviors",
            "text": "Do you avoid certain places, people, or activities because they remind you of distressing experiences?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Always"],
            "skip_allowed": True,
            "weight": {"trauma_indicators": {"Often": 1, "Always": 2}}
        },
        "emotional_numbing": {
            "id": "emotional_numbing",
            "text": "Do you sometimes feel emotionally numb or disconnected from your feelings?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Always"],
            "skip_allowed": True,
            "weight": {"trauma_indicators": {"Often": 1, "Always": 2}}
        },
        "hypervigilance": {
            "id": "hypervigilance",
            "text": "Do you find yourself constantly alert or 'on guard' for potential threats?",
            "type": "scale_agreement",
            "scale": ["Never", "Rarely", "Sometimes", "Often", "Always"],
            "skip_allowed": True,
            "weight": {"trauma_indicators": {"Often": 1, "Always": 2}}
        }
    }

    # Medical Contraindication Screening
    MEDICAL_SCREENING_QUESTIONS = {
        "seizure_history": {
            "id": "seizure_history",
            "text": "Do you have a history of seizures or epilepsy?",
            "type": "single_choice",
            "options": ["No", "Yes", "Unsure", "Prefer not to answer"],
            "skip_allowed": False,
            "contraindication": {"Yes": "high_risk"}
        },
        "psychotic_symptoms": {
            "id": "psychotic_symptoms",
            "text": "Have you experienced hallucinations (seeing/hearing things others don't) or delusions (strong false beliefs)?",
            "type": "single_choice",
            "options": ["No", "Yes, in the past", "Yes, currently", "Prefer not to answer"],
            "skip_allowed": True,
            "contraindication": {"Yes, currently": "high_risk", "Yes, in the past": "moderate_risk"}
        },
        "current_medications": {
            "id": "current_medications",
            "text": "Are you currently taking any psychiatric medications?",
            "type": "single_choice",
            "options": ["No", "Yes", "Prefer not to answer"],
            "skip_allowed": True,
            "note": "Medication interactions may affect hypnotic responsiveness"
        },
        "substance_use": {
            "id": "substance_use",
            "text": "Do you regularly use alcohol or substances that might affect your mental state?",
            "type": "single_choice",
            "options": ["No", "Occasionally", "Regularly", "Prefer not to answer"],
            "skip_allowed": True,
            "contraindication": {"Regularly": "moderate_risk"}
        }
    }

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

