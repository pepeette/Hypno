"""
Clean configuration module for the Hypnotherapy website
Centralizes all settings and constants
"""

import streamlit as st
from datetime import datetime
import re

#for HOME.py
class AppConstants:
    """Application-wide constants"""
    
    # Navigation
    NAVIGATION_OPTIONS = ["Home", "Method", "Blog", "Testimonials", "Book Now"]
    NAVIGATION_ICONS = ["house", "gear", "book", "star", "calendar"]
    
    # Contact information
    CONTACT_INFO = {
        "clinic_name": "NEW Bangkok ADDRESS",
        "address": "27 Soi Sukhumvit 10 (Asoke)",
        "city": "Bangkok, Thailand",
        "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
        "calendly_url": "https://calendly.com/laetitiasheppard/session",
        "discovery_call_url": "https://calendly.com/laetitiasheppard/discovery",
        "package_booking_url": "https://calendly.com/laetitiasheppard/package"
    }
    
    # Images
    IMAGES = {
        "founder_photo": "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true",
        "behavior_map": "https://github.com/pepeette/Hypno/blob/main/img%2FBehaviourMap.png?raw=true",
        "transformation": "https://github.com/pepeette/Hypno/blob/main/img%2Femo.jpg?raw=true"
    }
    
    # Pricing
    PRICING = {
        "complete_package": 3000,
        "premium_package": 4000,
        "currency": "THB"
    }
    
    # Form options
    CONCERN_OPTIONS = [
        "Select one...", 
        "Quit Smoking", 
        "Reduce Anxiety", 
        "Improve Sleep", 
        "Break Bad Habits",
        "Other"
    ]
    
    # Success statistics
    SUCCESS_RATES = {
        "two_sessions": 85,
        "third_session_needed": 15,
        "years_experience": 10
    }

# Add to utils/config.py

class QuizConfig:
    """Enhanced 4-question quiz configuration"""
    
    QUESTIONS = {
        1: {
            "title": "What unwanted pattern would you most like to eliminate?",
            "options": [
                ("🚭", "Quit smoking\nBreak nicotine addiction permanently"),
                ("😰", "Reduce anxiety\nStop panic attacks and overthinking"), 
                ("😴", "Improve sleep\nEnd insomnia and sleep anxiety"),
                ("🍷", "Control drinking\nHealthy relationship with alcohol"),
                ("🍕", "Stop overeating\nBreak emotional eating patterns"),
                ("📱", "Break bad habits\nEliminate destructive behaviors")
            ]
        },
        2: {
            "title": "How long have you been dealing with this pattern?",
            "options": [
                ("🆕", "Less than 6 months\nRecent development"),
                ("📅", "6 months to 2 years\nEstablished pattern"),
                ("⏳", "More than 2 years\nDeep-rooted habit")
            ]
        },
        3: {
            "title": "Which internal pattern most blocks your progress?",
            "options": [
                ("⚔️", "Force and control\n'I must push through resistance'"),
                ("🔒", "Mistrust and defensiveness\n'I can't let my guard down'"),
                ("⚖️", "All-or-nothing thinking\n'It's either perfect or failure'"),
                ("🏃", "Doing addiction\n'My worth depends on productivity'")
            ]
        },
        4: {
            "title": "How ready are you to transform this pattern?",
            "options": [
                ("🤔", "Curious but cautious\nWant to understand the approach first"),
                ("🎯", "Ready to commit\nPrepared to do the inner work"),
                ("🔥", "Desperate for change\nThis pattern must end now"),
                ("🛡️", "Prefer gradual approach\nWant to try other methods first")
            ]
        }
    }


class QuizConfig:
    """Quiz configuration and scoring"""
    SCORING = {
        1: {  # Unwanted patterns
            "Quit smoking": 30,
            "Reduce anxiety": 25,
            "Improve sleep": 20,
            "Control drinking": 25,
            "Stop overeating": 20,
            "Break bad habits": 25
        },
        2: {  # Duration
            "Less than 6 months": 15,
            "6 months to 2 years": 20,
            "More than 2 years": 25
        },
        3: {  # Blocking mechanisms
            "Force and control": 20,
            "Mistrust and defensiveness": 15,
            "All-or-nothing thinking": 25,
            "Doing addiction": 30
        },
        4: {  # Readiness levels
            "Curious but cautious": 15,
            "Ready to commit": 30,
            "Desperate for change": 25,
            "Prefer gradual approach": 5
        }
    }



class TestimonialConfig:
    """Testimonial data"""
    
    TESTIMONIALS = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Director, Banking, Singapore",
            "concern": "Anxiety patterns",
            "duration": "2 sessions"
        },
        {
            "icon": "🎓", 
            "quote": "I was struggling with my studies abroad... now doing my specialization internship.",
            "author": "Medical Student, Morocco",
            "concern": "Study anxiety",
            "duration": "2 sessions"
        },
        {
            "icon": "🚭",
            "quote": "My husband was a heavy smoker... No more addiction.",
            "author": "Wife, Bangkok",
            "concern": "Smoking cessation",
            "duration": "2 sessions"
        }
    ]


# for ASSESS.PY

# -------------------------
# Pattern Definitions
# -------------------------

class PatternDefinitions:
    """Centralized pattern definitions"""
    PATTERNS = {
        1: "Unhappiness Culture", 
        2: "Power Struggles", 
        3: "Systematic Mistrust",
        4: "Separation and Division", 
        5: "Doing versus Being", 
        6: "Compartmentalized Authenticity",
        7: "Self Sacrifice and Care Avoidance", 
        8: "Inherited Missions", 
        9: "Context Dependent Weakness"
    }

    PATTERN_DESCRIPTIONS = {
        1: {
            "name": "Unhappiness Culture",
            "root_structure": "Positive states = danger/loss/punishment",
            "core_belief": "Happiness leads to disappointment or makes me a target",
            "systemic_factors": ["Family depression patterns", "Cultural suffering valorization", "Positive suppression rewards"],
            "identity_conflict": "Happy self vs. Familiar/safe suffering self",
            "hidden_loyalties": ["Family unhappiness solidarity", "Suffering = virtue beliefs", "Protection from envy/attacks"],
            "intervention_strategy": "Permission installation for positive states with safety anchoring",
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
            "session_1_focuses": "Happiness permission protocols and safety anchoring",
            "session_2_focuses": "Joy sustainability and positive emotion anchoring"
        },
        2: {
            "name": "Power Struggles", 
            "root_structure": "Submission = death/annihilation of self",
            "core_belief": "I must fight to exist/maintain my identity",
            "systemic_factors": ["Authoritarian family dynamics", "Competition-based relationships", "Win-lose paradigms"],
            "identity_conflict": "Collaborative self vs. Fighter/survivor self",
            "hidden_loyalties": ["Family fight patterns", "Strength = resistance beliefs", "Protection from domination"],
            "intervention_strategy": "Collaborative empowerment with maintained autonomy",
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
            "session_1_focuses": "Nervous system regulation and collaborative response installation",
            "session_2_focuses": "Conflict transformation and win-win response automation"
        },
        3: {
            "name": "Systematic Mistrust",
            "root_structure": "Others = eventual betrayal/harm",
            "core_belief": "Trust leads to being hurt, used, or abandoned",
            "systemic_factors": ["Early betrayal experiences", "Inconsistent caregiving", "Trust violation patterns"],
            "identity_conflict": "Trusting self vs. Protected/vigilant self", 
            "hidden_loyalties": ["Loyalty to hurt parts", "Vigilance = safety beliefs", "Protection from re-injury"],
            "intervention_strategy": "Gradual trust building with transparent safety protocols",
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
            "session_1_focuses": "Trust calibration and authentic connection programming",
            "session_2_focuses": "Healthy skepticism calibration and openness programming"
        },
        4: {
            "name": "Separation and Division",
            "root_structure": "Gray areas = chaos/uncertainty/danger",
            "core_belief": "Things must be clearly defined or everything falls apart",
            "systemic_factors": ["Rigid family rules", "Religious absolutism", "Chaotic early environment"],
            "identity_conflict": "Flexible self vs. Clear/defined self",
            "hidden_loyalties": ["Family certainty patterns", "Order = safety beliefs", "Protection from confusion"],
            "intervention_strategy": "Both/and integration with safety in uncertainty",
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
            "session_1_focuses": "Binary thinking dissolution and creative possibility expansion",
            "session_2_focuses": "Creative problem-solving and nuanced thinking installation"
        },
        5: {
            "name": "Doing versus Being",
            "root_structure": "Worth = productivity/achievement only",
            "core_belief": "I am only valuable when I'm producing/achieving",
            "systemic_factors": ["Achievement-focused family", "Work/school performance pressure", "Productivity culture"],
            "identity_conflict": "Being self vs. Achieving self",
            "hidden_loyalties": ["Family achievement patterns", "Worth = doing beliefs", "Protection from worthlessness"],
            "intervention_strategy": "Inherent worth installation with productivity reframing",
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
            "session_1_focuses": "Worth anchoring independent of achievement",
            "session_2_focuses": "Intrinsic worth recognition and balanced achievement"
        },
        6: {
            "name": "Compartmentalized Authenticity",
            "root_structure": "Real self = rejection/abandonment",
            "core_belief": "I must be different selves to be accepted",
            "systemic_factors": ["Conditional family acceptance", "Social role expectations", "Authenticity punishment"],
            "identity_conflict": "Authentic self vs. Acceptable/safe selves",
            "hidden_loyalties": ["Family role patterns", "Adaptation = survival beliefs", "Protection from rejection"],
            "intervention_strategy": "Authentic self integration with safety across contexts",
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
            "session_1_focuses": "Authentic self integration and consistency programming",
            "session_2_focuses": "Integrated identity and consistent self-expression"
        },
        7: {
            "name": "Self Sacrifice and Care Avoidance",
            "root_structure": "My needs = selfish/wrong/dangerous",
            "core_belief": "I am only good/loveable when serving others",
            "systemic_factors": ["Caretaker family roles", "Self-sacrifice modeling", "Need-shaming patterns"],
            "identity_conflict": "Self-caring self vs. Service/giving self",
            "hidden_loyalties": ["Family service patterns", "Sacrifice = love beliefs", "Protection from selfishness"],
            "intervention_strategy": "Self-care as service reframing with boundary installation",
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
            "session_1_focuses": "Boundary establishment and self-care permission",
            "session_2_focuses": "Reciprocal relationship patterns and energy management"
        },
        8: {
            "name": "Inherited Missions",
            "root_structure": "My path = betrayal of family/ancestors",
            "core_belief": "I must fulfill family dreams/expectations to be loyal",
            "systemic_factors": ["Family sacrifice stories", "Generational expectations", "Dream inheritance patterns"],
            "identity_conflict": "Personal desire self vs. Family loyal self",
            "hidden_loyalties": ["Ancestral sacrifice honor", "Family dream continuation", "Protection from guilt/betrayal"],
            "intervention_strategy": "Honor family while claiming personal path integration",
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
            "session_1_focuses": "Personal values clarification and family harmony balance",
            "session_2_focuses": "Authentic life direction and confident decision-making"
        },
        9: {
            "name": "Context Dependent Weakness",
            "root_structure": "Certain contexts = powerlessness/helplessness",
            "core_belief": "I lose myself in specific situations/with certain people",
            "systemic_factors": ["Trauma context associations", "Power dynamic patterns", "Learned helplessness"],
            "identity_conflict": "Strong self vs. Overwhelmed/powerless self",
            "hidden_loyalties": ["Trauma bond maintenance", "Powerlessness = safety beliefs", "Protection from responsibility"],
            "intervention_strategy": "Universal strength anchoring with context-independent resources",
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
            "session_1_focuses": "Context-independent boundary installation",
            "session_2_focuses": "Consistent boundary maintenance across all contexts"
        }
    }


    # -------------------------
    # Core belief hint keywords
    # -------------------------
    BELIEF_HINTS = {
        "not good enough": "I'm not good enough as I am",
        "can't trust": "I can't trust others to be there for me", 
        "must do": "I must constantly prove my worth",
        "don't deserve": "I don't deserve good things",
        "can't handle": "I can't handle difficult emotions"
    }
    
    # -------------------------
    # Discovery phase rules
    # -------------------------
    DISCOVERY_PHASE_RULES = {
        "early": ["pattern_1", "pattern_2"],
        "trigger_mapping": ["pattern_3", "pattern_4"],
        "default": "Pattern-specific questioning"
    }
    
    # -------------------------
    # Success indicators for digital components
    # -------------------------
    DIGITAL_SUCCESS_INDICATORS = {
        'reality_dissociation': [
            'Feeling equally authentic online and offline',
            'Preferring face-to-face conversations over digital',
            'Natural eye contact during conversations'
        ],
        'ironic_detachment': [
            'Expressing genuine emotions without self-mockery',
            'Sincere enthusiasm without embarrassment',
            'Connecting emotionally with others naturally'
        ],
        'attention_fragmentation': [
            'Reading for 30+ minutes without distraction',
            'Having complete conversations without phone checking',
            'Deep focus on single tasks for extended periods'
        ]
    }
    # -------------------------
    # Expand DIGITAL_THRESHOLDS with adaptations & benefits
    # -------------------------
    DIGITAL_THRESHOLDS = {
        'SEVERE': {
            'threshold': 70,
            'title': 'Specialized digital-native approach required',
            'description': 'Your assessment reveals significant digital conditioning patterns that require adapted therapeutic techniques.',
            'benefits': 'With proper specialized approach, you can integrate your digital competencies with real-world confidence and authentic emotional expression.',
            'adaptations': [
                "Attention span optimization: 15-30 minute focused segments",
                "Anti-authority language: Collaborative, non-directive approach",
                "Ironic armor dissolution: Validate intelligence while accessing authentic emotion",
                "Digital bridge-building: Connect online competencies to offline confidence",
                "Binary thinking interruption: Install 'both/and' processing patterns",
                "Hope introduction protocol: Gradual realistic optimism vs. overwhelming positivity",
                "Meaning-making assistance: Personal contribution vs. extraordinary achievement",
            ]
        },
        'MODERATE': {
            'threshold': 50,
            'title': 'Enhanced digital-aware therapy recommended',
            'description': 'You show moderate digital conditioning that benefits from modified therapeutic approaches.',
            'benefits': 'Standard techniques enhanced with digital awareness will optimize your transformation process.',
            'adaptations': [
                "Modified session length: 45-60 minutes with movement breaks",
                "Authority resistance awareness: Reduce directive language",
                "Cynicism validation: Acknowledge systemic problems while building agency",
                "Digital competency honor: Validate online achievements and skills",
                "Nuanced goal-setting: Meaningful vs. extraordinary success redefinition",
                "Gradual hope building: Evidence-based optimism introduction",
            ]
        },
        'MILD': {
            'threshold': 30,
            'title': 'Digital considerations integrated',
            'description': 'Some digital influence detected that will be incorporated into your standard approach.',
            'benefits': 'Your digital skills can be leveraged as strengths in your transformation journey.',
            'adaptations': [
                "Digital literacy integration: Use familiar cultural references",
                "Achievement pressure awareness: Expand success definitions",
                "Authentic expression permission: Reduce 'cringe' about sincerity",
                "Real-world confidence transfer: Apply online skills offline",
            ]
        },
        'MINIMAL': {
            'threshold': 0,
            'title': 'Traditional approach optimal',
            'description': 'Minimal digital conditioning detected - standard hypnotherapy approach is ideal.',
            'benefits': 'You can benefit from proven traditional techniques without modification.',
            'adaptations': [
                "Standard approach with generational awareness",
                "Technology balance considerations",
                "Modern stress factor acknowledgment",
            ]
        }
    }




# -------------------------
# Question Sets
# -------------------------
"""All question pools for each assessment phase"""
"""Phase 1: Algorithmic Syndrome Screening (for digital natives)"""
"""Phase 2: Engagement & Initial Pattern Detection"""
"""Phase 3: Core Trigger Mapping"""
"""Phase 4: Adaptive Pattern-Specific Deep Dives"""
"""Phase 5: Integration & Change Readiness"""

class QuestionSets:
    AGE_SCREENING = {
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

    DIGITAL_SCREENING = {   
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
                "pattern_triggers": {  # Changed from digital_despair_indicators
                    1: [6], 3: [3, 6], 4: [6]
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
                "pattern_triggers": {  # Changed from digital_despair_patterns
                    1: [5], 2: [2, 5], 4: [3]
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
                "pattern_triggers": {  # Added pattern triggers
                    1: [1], 2: [1, 3], 3: [1, 3, 6], 4: [6]
                },
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
                "pattern_triggers": {  # Changed from hope_avoidance_indicators
                    2: [3], 3: [3, 2], 4: [3, 2]
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

    ENGAGEMENT = {
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
                "min_chars": 3,
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

    TRIGGER_MAPPING = {
            14: {
                "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
                "type": "text_completion",
                "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
                "min_chars": 5,
                "chain_mapping": "trigger",
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
                "pattern_triggers": {
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
                "min_chars": 3,
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

    PATTERN_SPECIFIC = {
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
                    "min_chars": 3,
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
                "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
                "min_chars": 3,
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
                "min_chars": 5,
                "outcome_visualization": True,
                "phase": "integration"
            }
        }

# -------------------------
# Digital Scoring Rules
# -------------------------

DIGITAL_SCORING_RULES = {
    "reality_dissociation": {
        "question_id": 2,
        "conditions": {
            "online communities and digital spaces": 3,
            "don't feel authentic anywhere": 4,
            "varies completely depending": 2
        },
        "max_score": 5
    },
    "binary_success": {
        "question_id": 3,
        "conditions": {
            "Extraordinary wealth": 4,
            "Success feels impossible": 4,
            "significantly better than most people": 3
        },
        "max_score": 5
    },
    "ironic_detachment": {
        "question_id": 4,
        "conditions": {
            "embarrassed or 'cringe'": 3,
            "through memes or online references": 3,
            "rarely express genuine emotions": 4,
            "humor or irony to deflect": 2
        },
        "max_score": 5
    },
    "algorithmic_dependency": {
        "question_id": [5, 6],
        "conditions": {
            "Social media feeds": 3,
            "Online communities and digital relationships": 3,
            "Online personalities": 2,
            "Fictional characters": 3
        },
        "max_score": 5
    },
    "nihilistic_worldview": {
        "question_id": 3,
        "conditions": {"Success feels impossible": 4},
        "max_score": 5
    },
    "hope_avoidance": {
        "question_id": 7,
        "conditions": {
            "dismiss it as naive": 4,
            "annoyed because": 3,
            "reasons why they're wrong": 2
        },
        "max_score": 5
    },
    "attention_fragmentation": {
        "question_id": 8,
        "options": [
            "Same as always - can focus for hours when interested",
            "Slightly shorter but manageable",
            "Noticeably fragmented - need frequent stimulation",
            "Very difficult - mind wanders constantly",
            "Almost impossible without background digital stimulation"
        ],
        "scores": [0, 1, 2, 3, 4],
        "max_score": 5
    }
}

# -------------------------
# Pattern Scoring Rules
# -------------------------

PATTERN_SCORING_RULES = {
    "pattern_triggers": {
        # Example from engagement Qs
        9: {0: [5], 1: [5], 2: [3], 3: [8], 4: [3]},
        13: {0: [5, 8], 1: [7, 8, 9], 2: [2, 3, 6], 3: [1], 4: [1, 4]}
    },
    "pattern_mapping": {
        19: {0: [1, 4, 9], 1: [5], 2: [3, 7], 3: [2], 4: [2, 5], 5: [7], 6: [6, 9], 7: [4, 5]}
    },
    "pattern_keywords": {
        17: {
            "not good enough": [1],
            "fight": [2],
            "can't trust": [3],
            "either or": [4],
            "must do": [5],
            "can't be real": [6],
            "others need": [7],
            "should": [8],
            "can't handle": [9]
        }
    },
    "keywords": {
        10: {
            "productivity": [5],
            "relationships": [2, 3, 6, 7],
            "peace": [1],
            "authentic": [6],
            "happy": [1],
            "control": [2, 4],
            "boundaries": [7, 9]
        }
    },
    "weights": {
        # Example for pattern-specific questions
        22: {"pattern": 1, "weights": [0, 3, 3, 2, 2]},
        25: {"pattern": 2, "weights": [0, 3, 2, 1, 3]}
    }
}


class AnalyticsMethods:
    """Analytics methods that MasterAnalytics can import to stay clean"""
    
    @staticmethod
    def get_default_session_plan():
        """Default session plan when pattern analysis incomplete"""
        return {
            'session_structure': {
                'total_sessions': '2-3 sessions',
                'session_length': '90 minutes each',
                'timeline': '2-4 weeks'
            },
            'detailed_planning': {
                'session_1': 'Complete assessment and initial rapport building',
                'session_2': 'Pattern exploration and foundational work',
                'session_3': 'Integration and reinforcement if needed'
            },
            'timeline_predictions': {
                'total_duration': '2-4 weeks',
                'between_session_work': 'Minimal homework assignments',
                'follow_up_schedule': 'Check-in after 2 weeks'
            },
            'success_optimization': {
                'success_probability': 85,
                'optimization_factors': ['Complete assessment needed'],
                'potential_challenges': ['Assessment completion required']
            }
        }
    
    @staticmethod
    def plan_session_1(pattern_analysis, digital_analysis):
        """Plan session 1 based on analysis"""
        if not pattern_analysis:
            return "Complete assessment and initial rapport building"
        
        dominant_pattern = pattern_analysis.get('dominant_pattern', {})
        pattern_name = dominant_pattern.get('name', 'Unknown')
        
        digital_adaptations = ""
        if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            digital_adaptations = " with digital-native adaptations"
        
        return f"Deep pattern analysis focusing on {pattern_name} pattern{digital_adaptations}, rapport building, and initial positive programming"
    
    @staticmethod
    def plan_session_2(pattern_analysis, digital_analysis):
        """Plan session 2 based on analysis"""
        if not pattern_analysis:
            return "Pattern exploration and foundational transformation work"
        
        dominant_pattern = pattern_analysis.get('dominant_pattern', {})
        pattern_name = dominant_pattern.get('name', 'Unknown')
        
        return f"Core {pattern_name} pattern transformation, neural pathway rewiring, and positive response installation"
    
    @staticmethod
    def plan_session_3_if_needed(complexity_score, pattern_analysis):
        """Plan session 3 if needed based on complexity"""
        if complexity_score >= 7:
            return "Integration reinforcement, pattern consolidation, and long-term stability anchoring"
        elif complexity_score >= 5:
            return "Optional reinforcement session for complex pattern integration"
        else:
            return "Unlikely to be needed - standard 2-session protocol sufficient"
    
    @staticmethod
    def calculate_session_complexity_score(pattern_count, digital_severity):
        """Calculate session complexity score"""
        base_score = 3
        
        # Pattern complexity
        if pattern_count >= 5:
            base_score += 4
        elif pattern_count >= 3:
            base_score += 2
        elif pattern_count >= 2:
            base_score += 1
        
        # Digital complexity
        if digital_severity == 'SEVERE':
            base_score += 3
        elif digital_severity == 'MODERATE':
            base_score += 2
        elif digital_severity == 'MILD':
            base_score += 1
        
        return min(base_score, 10)
    
    @staticmethod
    def determine_session_structure(complexity_score):
        """Determine session structure based on complexity"""
        if complexity_score >= 8:
            return {
                'total_sessions': '3 sessions',
                'session_length': '90 minutes each',
                'timeline': '3-4 weeks',
                'structure_reason': 'High complexity requires comprehensive approach'
            }
        elif complexity_score >= 5:
            return {
                'total_sessions': '2-3 sessions', 
                'session_length': '90 minutes each',
                'timeline': '2-3 weeks',
                'structure_reason': 'Moderate complexity with optional reinforcement'
            }
        else:
            return {
                'total_sessions': '2 sessions',
                'session_length': '90 minutes each', 
                'timeline': '2 weeks',
                'structure_reason': 'Standard protocol optimal'
            }
    
    @staticmethod
    def predict_total_duration(complexity_score):
        """Predict total duration based on complexity"""
        if complexity_score >= 8:
            return "3-4 weeks for complete transformation"
        elif complexity_score >= 5:
            return "2-3 weeks with possible reinforcement"
        else:
            return "2 weeks for standard transformation"
    
    @staticmethod
    def determine_integration_work(pattern_analysis):
        """Determine between-session integration work"""
        if not pattern_analysis:
            return "Standard integration exercises"
        
        pattern_count = pattern_analysis.get('pattern_count', 0)
        
        if pattern_count >= 4:
            return "Daily pattern awareness exercises and response practice"
        elif pattern_count >= 2:
            return "Pattern recognition practice and mindful response exercises"
        else:
            return "Simple awareness exercises and positive anchoring"
    
    @staticmethod
    def determine_follow_up_schedule(complexity_score):
        """Determine follow-up schedule"""
        if complexity_score >= 7:
            return "1 week, 2 weeks, and 1 month check-ins"
        elif complexity_score >= 5:
            return "2 weeks and 1 month check-ins"
        else:
            return "1 month check-in"
    
    @staticmethod
    def calculate_session_success_probability(pattern_analysis, digital_analysis):
        """Calculate session success probability"""
        base_rate = 85
        
        if not pattern_analysis:
            return base_rate
        
        pattern_count = pattern_analysis.get('pattern_count', 0)
        
        # Pattern complexity adjustment
        if pattern_count >= 5:
            base_rate -= 5
        elif pattern_count >= 3:
            base_rate -= 2
        
        # Digital native advantage
        if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            base_rate += 3  # Specialized approach advantage
        
        return max(70, min(95, base_rate))
    
    @staticmethod
    def identify_optimization_factors(assessment_data):
        """Identify factors that optimize success"""
        factors = []
        
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.9:
            factors.append("High assessment engagement")
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) <= 3:
            factors.append("Focused pattern constellation")
        
        is_digital_native = assessment_data.get('is_digital_native', False)
        if is_digital_native:
            factors.append("Digital-native protocol match")
        
        if not factors:
            factors.append("Standard optimization protocols")
        
        return factors
    
    @staticmethod
    def predict_session_challenges(pattern_analysis, digital_analysis):
        """Predict potential session challenges"""
        challenges = []
        
        if not pattern_analysis:
            return ["Assessment completion needed"]
        
        pattern_count = pattern_analysis.get('pattern_count', 0)
        
        if pattern_count >= 4:
            challenges.append("Complex pattern interactions requiring careful sequencing")
        
        if digital_analysis and digital_analysis.get('severity_level') == 'SEVERE':
            challenges.append("Authority resistance and ironic detachment requiring specialized approach")
        
        if not challenges:
            challenges.append("Standard therapeutic resistance patterns")
        
        return challenges
    
    @staticmethod
    def calculate_engagement_adjustment(assessment_data):
        """Calculate engagement adjustment factor"""
        completion_rate = assessment_data.get('completion_rate', 0)
        
        if completion_rate >= 0.9:
            return 3  # High engagement bonus
        elif completion_rate >= 0.7:
            return 1  # Moderate engagement
        elif completion_rate >= 0.5:
            return -1  # Low engagement penalty
        else:
            return -3  # Very low engagement
    
    @staticmethod
    def calculate_readiness_adjustment(responses):
        """Calculate readiness adjustment from responses"""
        if not responses:
            return 0
        
        readiness_indicators = 0
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, dict) and 'rating' in response:
                rating = response.get('rating', 0)
                if rating >= 8:
                    readiness_indicators = 3
                elif rating >= 6:
                    readiness_indicators = max(readiness_indicators, 1)
            elif isinstance(response, str):
                if any(word in response.lower() for word in ['ready', 'desperate', 'tired of', 'need to change']):
                    readiness_indicators = max(readiness_indicators, 2)
        
        return readiness_indicators
    
    @staticmethod
    def generate_success_factors_list(assessment_data):
        """Generate list of success factors"""
        factors = []
        
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.9:
            factors.append("High assessment completion rate shows commitment")
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) <= 3:
            factors.append("Focused pattern constellation allows targeted intervention")
        
        if assessment_data.get('is_digital_native'):
            factors.append("Digital-native adaptations provide specialized advantage")
        
        if not factors:
            factors.append("Standard therapeutic factors support transformation")
        
        return factors
    
    @staticmethod
    def generate_risk_mitigation_strategies(assessment_data):
        """Generate risk mitigation strategies"""
        strategies = []
        
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        if pattern_count >= 4:
            strategies.append("Careful session pacing to prevent overwhelm")
        
        digital_analysis = assessment_data.get('digital_despair_analysis')
        if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            strategies.append("Anti-authority language and collaborative approach")
        
        if not strategies:
            strategies.append("Standard risk management protocols")
        
        return strategies

   
    @staticmethod
    def analyze_complete_trigger_sequence(assessment_data):
        """Analyze trigger sequence from assessment data"""
        trigger_chain = assessment_data.get('trigger_chain', {})
        responses = assessment_data.get('assessment_responses', {})
        
        if not trigger_chain and not responses:
            return {
                'sequence_completeness': 0,
                'trigger_points': [],
                'intervention_windows': [],
                'sequence_analysis': 'Trigger sequence data not captured - assessment incomplete'
            }
        
        # Extract basic sequence
        sequence = {
            'environmental_trigger': trigger_chain.get('trigger', 'Not captured'),
            'awareness_point': trigger_chain.get('awareness_point', 'Not captured'),
            'physical_response': trigger_chain.get('physical_response', 'Not captured'),
            'automatic_thought': trigger_chain.get('automatic_thought', 'Not captured'),
            'emotional_response': trigger_chain.get('emotional_response', 'Not captured'),
            'behavioral_response': trigger_chain.get('behavioral_response', 'Not captured'),
            'immediate_consequence': trigger_chain.get('immediate_consequence', 'Not captured')
        }
        
        # Calculate completeness
        captured_elements = sum(1 for v in sequence.values() if v != 'Not captured')
        completeness = int((captured_elements / len(sequence)) * 100)
        
        # Identify intervention points
        intervention_points = []
        if sequence['physical_response'] != 'Not captured':
            intervention_points.append('Physical awareness intervention')
        if sequence['automatic_thought'] != 'Not captured':
            intervention_points.append('Thought pattern interruption')
        if sequence['behavioral_response'] != 'Not captured':
            intervention_points.append('Behavioral choice point')
        
        return {
            'sequence_completeness': completeness,
            'trigger_sequence': sequence,
            'intervention_windows': intervention_points,
            'sequence_analysis': f"Sequence {completeness}% complete - {'sufficient for intervention design' if completeness >= 60 else 'requires completion in session 1'}"
        }
    
    @staticmethod
    def identify_all_transformation_assets(assessment_data):
        """Identify transformation assets from assessment"""
        assets = []
        
        # Assessment completion as asset
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.8:
            assets.append("High assessment engagement demonstrates commitment to change")
        
        # Pattern recognition ability
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) >= 2:
            assets.append("Strong pattern recognition and self-awareness abilities")
        
        # Communication skills from text responses
        responses = assessment_data.get('assessment_responses', {})
        detailed_responses = sum(1 for r in responses.values() 
                               if isinstance(r.get('response'), str) and len(r.get('response', '')) > 30)
        if detailed_responses >= 3:
            assets.append("Excellent self-expression and communication skills")
        
        # Digital competencies
        if assessment_data.get('is_digital_native'):
            assets.append("Digital competencies that can transfer to real-world confidence")
        
        # Motivation indicators
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and any(word in response.lower() for word in ['ready', 'want to change', 'tired of']):
                assets.append("Clear motivation and readiness for transformation")
                break
        
        # Default assets if none identified
        if len(assets) < 3:
            assets.extend([
                "Natural problem-solving abilities",
                "Capacity for insight and self-reflection",
                "Courage to seek help and explore new approaches"
            ])
        
        return assets[:5]  # Return top 5 assets
    
    @staticmethod
    def extract_complete_empowerment_profile(assessment_data):
        """Extract empowerment profile from assessment"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        
        # Strengths identification
        strengths = []
        if len(pattern_scores) >= 3:
            strengths.append("Pattern recognition ability")
        if assessment_data.get('completion_rate', 0) >= 0.8:
            strengths.append("Commitment and follow-through")
        
        # Readiness indicators
        readiness_indicators = []
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, dict) and 'rating' in response:
                rating = response.get('rating', 0)
                if rating >= 7:
                    readiness_indicators.append(f"High readiness rating: {rating}/10")
        
        # Change motivation
        motivation_level = "Moderate"
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                if any(word in response.lower() for word in ['desperate', 'must change', 'can\'t continue']):
                    motivation_level = "High"
                    break
                elif any(word in response.lower() for word in ['ready', 'want to', 'need to']):
                    motivation_level = "High"
                    break
        
        return {
            'identified_strengths': strengths,
            'readiness_indicators': readiness_indicators,
            'motivation_level': motivation_level,
            'empowerment_summary': f"{motivation_level} motivation with strong assessment engagement"
        }
    
    @staticmethod
    def extract_communication_preferences(assessment_data):
        """Extract communication preferences from responses"""
        responses = assessment_data.get('assessment_responses', {})
        
        # Analyze response style
        response_style = "Concise"
        avg_response_length = 0
        text_responses = 0
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                text_responses += 1
                avg_response_length += len(response)
        
        if text_responses > 0:
            avg_response_length = avg_response_length / text_responses
            if avg_response_length > 100:
                response_style = "Detailed and expressive"
            elif avg_response_length > 50:
                response_style = "Moderate detail"
        
        # Digital communication preference
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        return {
            'response_style': response_style,
            'communication_preference': 'Digital-friendly approach' if is_digital_native else 'Traditional approach',
            'detail_level': 'High' if avg_response_length > 80 else 'Moderate',
            'engagement_style': 'Interactive and collaborative'
        }

# -------------------------
# Emails 
# -------------------------

class EmailConfig:
    """Email system configuration"""
    SMTP_SERVER = st.secrets["email"]["SMTP_SERVER"]
    SMTP_PORT = st.secrets["email"]["SMTP_PORT"]
    SENDER_EMAIL = st.secrets["email"]["SENDER_EMAIL"]
    RECIPIENT_EMAIL = st.secrets["email"]["RECIPIENT_EMAIL"]
    MAIL_APP_PASSWORD = st.secrets["email"]["GMAIL_APP_PASSWORD"]
