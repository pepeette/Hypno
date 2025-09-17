"""
Clean configuration module for the Hypnotherapy website
Centralizes all settings and constants
"""

from datetime import datetime
import re

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
                "insights_map":"Your mind has learned to deflect happiness as protection against disappointment - but this same mechanism is preventing the joy you deserve",
                "what_you_notice": "Feeling guilty when things go well, waiting for the other shoe to drop, minimizing achievements",
                "what_others_see": "Someone who deflects compliments, seems uncomfortable with praise, or finds problems in good situations",
                "hidden_cost": "Missing out on life's genuine pleasures and the motivation that comes from celebrating wins",
                "breakthrough_moment": "Realizing that happiness doesn't make you vulnerable - it makes you stronger and more resilient",
                "session_1_focuses":"Happiness permission protocols and safety anchoring",
                "session_2_focuses":"Joy sustainability and positive emotion anchoring"
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
                "insights_map":"You're fighting battles that don't need to be fought - your nervous system activates 'combat mode' even in collaborative situations",
                "what_you_notice": "Feeling defensive quickly, needing to be right, seeing disagreements as threats",
                "what_others_see": "Someone who argues their point intensely, seems confrontational, or withdraws when challenged",
                "hidden_cost": "Exhausting mental energy on conflicts instead of creative collaboration and genuine connection",
                "breakthrough_moment": "Discovering that being curious about others' perspectives actually strengthens your position",
                "session_1_focuses":"Nervous system regulation and collaborative response installation",
                "session_2_focuses":"Conflict transformation and win-win response automation"
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
                "insights_map":"Your protective skepticism, while once useful, is now creating the very rejection and isolation you're trying to avoid",
                "what_you_notice": "Analyzing people's motives, feeling suspicious of kindness, expecting hidden agendas",
                "what_others_see": "Someone who seems guarded, asks probing questions, or appears cynical about human nature",
                "hidden_cost": "Living in emotional isolation and missing genuine opportunities for support and connection",
                "breakthrough_moment": "Understanding that discernment and openness can coexist - you can be wise AND trusting",
                "session_1_focuses":"Trust calibration and authentic connection programming",
                "session_2_focuses":"Healthy skepticism calibration and openness programming"
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
                "insights_map":"Your brilliant analytical mind gets trapped in 'either/or' thinking when 'both/and' solutions would serve you better",
                "what_you_notice": "Feeling stuck between two options, seeing things as all good or all bad, struggling with grey areas",
                "what_others_see": "Someone who wants clear answers, seems frustrated by ambiguity, or makes quick either/or judgments",
                "hidden_cost": "Missing innovative solutions that require holding multiple perspectives simultaneously",
                "breakthrough_moment": "Realizing that complexity isn't confusion - it's where the most elegant solutions hide",
                "session_1_focuses":"Binary thinking dissolution and creative possibility expansion",
                "session_2_focuses":"Creative problem-solving and nuanced thinking installation"
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
                "insights_map":"You've created an equation where doing = worth, but your actual value exists independent of any achievement",
                "what_you_notice": "Feeling anxious when not productive, equating rest with laziness, measuring yourself by output",
                "what_others_see": "Someone who's always busy, seems uncomfortable with downtime, or talks about achievements frequently",
                "hidden_cost": "Chronic stress, missed opportunities for reflection and creativity that come from mental space",
                "breakthrough_moment": "Discovering that your value exists completely separate from what you do or achieve",
                "session_1_focuses":"Worth anchoring independent of achievement",
                "session_2_focuses":"Intrinsic worth recognition and balanced achievement"
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
                "insights_map":"You're exhausting yourself maintaining different versions of yourself instead of trusting that your authentic self is enough",
                "what_you_notice": "Feeling like different people in different settings, adapting personality to fit in, losing sense of 'real self'",
                "what_others_see": "Someone who seems different depending on the group, appears to chameleon, or seems inconsistent",
                "hidden_cost": "Emotional exhaustion from performance, loss of authentic self-expression and genuine connections",
                "breakthrough_moment": "Realizing that your authentic self is actually more likeable and magnetic than any persona",
                "session_1_focuses": "Authentic self integration and consistency programming",
                "session_2_focuses":"Integrated identity and consistent self-expression"
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
                "insights_map":"Your generous heart has learned to give to others but forgotten how to receive - creating an unsustainable energy drain",
                "what_you_notice": "Feeling guilty when focusing on yourself, automatically saying yes to requests, feeling responsible for others' emotions",
                "what_others_see": "Someone who's always helpful, never seems to have needs, or appears stressed but won't ask for help",
                "hidden_cost": "Resentment buildup, burnout, and becoming less effective at helping others when you're depleted",
                "breakthrough_moment": "Understanding that taking care of yourself is actually the most loving thing you can do for others",
                "session_1_focuses": "Boundary establishment and self-care permission",
                "session_2_focuses":"Reciprocal relationship patterns and energy management"
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
                "insights_map":"You're living someone else's dream while your own authentic desires remain buried under family expectations",
                "what_you_notice": "Feeling torn between what you want and what's expected, guilt about disappointing family, unclear about your own desires",
                "what_others_see": "Someone who references family expectations often, seems conflicted about decisions, or appears to live for others",
                "hidden_cost": "Living someone else's life instead of your own, missing your unique contribution to the world",
                "breakthrough_moment": "Realizing you can honor your family AND live authentically - they're not mutually exclusive",
                "session_1_focuses":"Personal values clarification and family harmony balance",
                "session_2_focuses":"Authentic life direction and confident decision-making"
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
                "insights_map":"Your boundaries disappear in certain contexts because you've never learned you can be both loved and boundaried",
                "what_you_notice": "Being strong in some situations but passive in others, feeling like you lose yourself in certain contexts",
                "what_others_see": "Someone who seems confident sometimes but submissive other times, appears unpredictable in their responses",
                "hidden_cost": "Confusion about your own limits, relationships built on false premises, accumulated resentment",
                "breakthrough_moment": "Discovering that consistent boundaries actually make you more trustworthy and respected",
                "session_1_focuses": "Context-independent boundary installation",
                "session_2_focuses":"Consistent boundary maintenance across all contexts"
        }
    }

    DIGITAL_THRESHOLDS = {
            'SEVERE': {
                'threshold':70,
                'title': 'Specialized digital-native approach required',
                'description': 'Your assessment reveals significant digital conditioning patterns that require adapted therapeutic techniques.',
                'what_you_notice': 'Feeling more authentic online than offline, struggling with attention span for real-world activities, emotional states tied to digital feeds',
                'what_others_see': 'Someone who seems more engaged with their phone than present conversations, appears cynical about traditional approaches',
                'hidden_cost': 'Living in digital reality while real life passes by, missing genuine human connections and embodied experiences',
                'benefits': 'With proper specialized approach, you can integrate your digital competencies with real-world confidence and authentic emotional expression.',
                'why_traditional_fails': 'Traditional therapy expects attention spans and emotional patterns that digital conditioning has fundamentally altered',
                'hypnotherapy_advantage': 'Bypasses conscious resistance and works directly with the neural patterns that digital conditioning has created'
            },
            'MODERATE': {
                'threshold':50,
                'title': 'Enhanced digital-aware therapy recommended', 
                'description': 'You show moderate digital conditioning that benefits from modified therapeutic approaches.',
                'what_you_notice': 'Some difficulty with extended focus, occasional preference for online interactions, influence of social media on mood',
                'what_others_see': 'Someone who checks their phone regularly, seems more comfortable texting than calling, references online culture',
                'hidden_cost': 'Fragmented attention reducing deep thinking capacity, some authentic emotions filtered through digital expression',
                'benefits': 'Standard techniques enhanced with digital awareness will optimize your transformation process.',
                'why_traditional_fails': 'Traditional approaches don\'t account for how digital environments have shaped your neural pathways',
                'hypnotherapy_advantage': 'Can work with both traditional patterns and digital conditioning simultaneously'
            },
            'MILD': {
                'threshold':30,
                'title': 'Digital considerations integrated',
                'description': 'Some digital influence detected that will be incorporated into your standard approach.',
                'what_you_notice': 'Balanced online and offline life with occasional digital overwhelm, mostly traditional attention patterns',
                'what_others_see': 'Someone who uses technology normally without it dominating their personality or relationships',
                'hidden_cost': 'Minor attention fragmentation and occasional comparison triggered by social media',
                'benefits': 'Your digital skills can be leveraged as strengths in your transformation journey.',
                'why_traditional_fails': 'Standard approaches work well but miss opportunities to leverage your digital competencies',
                'hypnotherapy_advantage': 'Can enhance traditional patterns while optimizing your relationship with technology'
            },
            'MINIMAL': {
                'threshold':0,
                'title': 'Traditional approach optimal',
                'description': 'Minimal digital conditioning detected - standard hypnotherapy approach is ideal.',
                'what_you_notice': 'Technology serves you rather than controlling you, strong attention span for offline activities',
                'what_others_see': 'Someone who uses technology as a tool without being dominated by it, present in conversations',
                'hidden_cost': 'Minimal digital interference with authentic living and relationships',
                'benefits': 'You can benefit from proven traditional techniques without modification.',
                'why_traditional_fails': 'Traditional approaches work well for you - this is about optimizing what already works',
                'hypnotherapy_advantage': 'Direct access to your subconscious without digital conditioning interference'
            }
    }


class EmailConfig:
    """Email system configuration"""
    SMTP_SERVER = st.secrets["email"]["SMTP_SERVER"]
    SMTP_PORT = st.secrets["email"]["SMTP_PORT"]
    SENDER_EMAIL = st.secrets["email"]["SENDER_EMAIL"]
    RECIPIENT_EMAIL = st.secrets["email"]["RECIPIENT_EMAIL"]
    MAIL_APP_PASSWORD = st.secrets["email"]["GMAIL_APP_PASSWORD"]
