"""
Clean configuration module for the Hypnotherapy website
Centralizes all settings and constants
"""

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


# Add to utils/config.py
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

    STRUCTURES = {
        1: {
                "name": "Unhappiness Culture",
                "root_structure": "Positive states = danger/loss/punishment",
                "core_belief": "Happiness leads to disappointment or makes me a target",
                "systemic_factors": ["Family depression patterns", "Cultural suffering valorization", "Positive suppression rewards"],
                "identity_conflict": "Happy self vs. Familiar/safe suffering self",
                "hidden_loyalties": ["Family unhappiness solidarity", "Suffering = virtue beliefs", "Protection from envy/attacks"],
                "intervention_strategy": "Permission installation for positive states with safety anchoring"
        },
        2: {
                "name": "Power Struggles", 
                "root_structure": "Submission = death/annihilation of self",
                "core_belief": "I must fight to exist/maintain my identity",
                "systemic_factors": ["Authoritarian family dynamics", "Competition-based relationships", "Win-lose paradigms"],
                "identity_conflict": "Collaborative self vs. Fighter/survivor self",
                "hidden_loyalties": ["Family fight patterns", "Strength = resistance beliefs", "Protection from domination"],
                "intervention_strategy": "Collaborative empowerment with maintained autonomy"
        },
        3: {
                "name": "Systematic Mistrust",
                "root_structure": "Others = eventual betrayal/harm",
                "core_belief": "Trust leads to being hurt, used, or abandoned",
                "systemic_factors": ["Early betrayal experiences", "Inconsistent caregiving", "Trust violation patterns"],
                "identity_conflict": "Trusting self vs. Protected/vigilant self", 
                "hidden_loyalties": ["Loyalty to hurt parts", "Vigilance = safety beliefs", "Protection from re-injury"],
                "intervention_strategy": "Gradual trust building with transparent safety protocols"
        },
        4: {
                "name": "Separation and Division",
                "root_structure": "Gray areas = chaos/uncertainty/danger",
                "core_belief": "Things must be clearly defined or everything falls apart",
                "systemic_factors": ["Rigid family rules", "Religious absolutism", "Chaotic early environment"],
                "identity_conflict": "Flexible self vs. Clear/defined self",
                "hidden_loyalties": ["Family certainty patterns", "Order = safety beliefs", "Protection from confusion"],
                "intervention_strategy": "Both/and integration with safety in uncertainty"
        },
        5: {
                "name": "Doing versus Being",
                "root_structure": "Worth = productivity/achievement only",
                "core_belief": "I am only valuable when I'm producing/achieving",
                "systemic_factors": ["Achievement-focused family", "Work/school performance pressure", "Productivity culture"],
                "identity_conflict": "Being self vs. Achieving self",
                "hidden_loyalties": ["Family achievement patterns", "Worth = doing beliefs", "Protection from worthlessness"],
                "intervention_strategy": "Inherent worth installation with productivity reframing"
        },
        6: {
                "name": "Compartmentalized Authenticity",
                "root_structure": "Real self = rejection/abandonment",
                "core_belief": "I must be different selves to be accepted",
                "systemic_factors": ["Conditional family acceptance", "Social role expectations", "Authenticity punishment"],
                "identity_conflict": "Authentic self vs. Acceptable/safe selves",
                "hidden_loyalties": ["Family role patterns", "Adaptation = survival beliefs", "Protection from rejection"],
                "intervention_strategy": "Authentic self integration with safety across contexts"
        },
        7: {
                "name": "Self Sacrifice and Care Avoidance",
                "root_structure": "My needs = selfish/wrong/dangerous",
                "core_belief": "I am only good/loveable when serving others",
                "systemic_factors": ["Caretaker family roles", "Self-sacrifice modeling", "Need-shaming patterns"],
                "identity_conflict": "Self-caring self vs. Service/giving self",
                "hidden_loyalties": ["Family service patterns", "Sacrifice = love beliefs", "Protection from selfishness"],
                "intervention_strategy": "Self-care as service reframing with boundary installation"
        },
        8: {
                "name": "Inherited Missions",
                "root_structure": "My path = betrayal of family/ancestors",
                "core_belief": "I must fulfill family dreams/expectations to be loyal",
                "systemic_factors": ["Family sacrifice stories", "Generational expectations", "Dream inheritance patterns"],
                "identity_conflict": "Personal desire self vs. Family loyal self",
                "hidden_loyalties": ["Ancestral sacrifice honor", "Family dream continuation", "Protection from guilt/betrayal"],
                "intervention_strategy": "Honor family while claiming personal path integration"
        },
        9: {
                "name": "Context Dependent Weakness",
                "root_structure": "Certain contexts = powerlessness/helplessness",
                "core_belief": "I lose myself in specific situations/with certain people",
                "systemic_factors": ["Trauma context associations", "Power dynamic patterns", "Learned helplessness"],
                "identity_conflict": "Strong self vs. Overwhelmed/powerless self",
                "hidden_loyalties": ["Trauma bond maintenance", "Powerlessness = safety beliefs", "Protection from responsibility"],
                "intervention_strategy": "Universal strength anchoring with context-independent resources"
        }
    }

    DIGITAL_THRESHOLDS = {
        'SEVERE': 70,
        'MODERATE': 50, 
        'MILD': 30,
        'MINIMAL': 0
    }

class EmailConfig:
    """Email system configuration"""
    SMTP_SERVER = st.secrets["email"]["SMTP_SERVER"]
    SMTP_PORT = st.secrets["email"]["SMTP_PORT"]
    SENDER_EMAIL = st.secrets["email"]["SENDER_EMAIL"]
    RECIPIENT_EMAIL = st.secrets["email"]["RECIPIENT_EMAIL"]
    MAIL_APP_PASSWORD = st.secrets["email"]["GMAIL_APP_PASSWORD"]
