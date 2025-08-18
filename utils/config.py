# """
# Configuration Management
# Centralized configuration for the hypnotherapy website
# """

# class AppConfig:
#     """Application configuration constants"""
    
#     # Practice Information
#     PRACTICE_NAME = "Hypnotherapy Clinic >> NEW ADDRESS"
#     PRACTITIONER_NAME = "Laetitia Sheppard"
#     PRACTICE_ESTABLISHED = 2017
    
#     # Qualifications
#     LCCH_CERTIFICATION = "2017"  # London College of Clinical Hypnotherapy
#     DBT_CERTIFICATION = "2023"   # Dialectical Behavioral Therapy
    
#     # Contact Information
#     CLINIC_ADDRESS = "27 Soi Sukhumvit 10 (Asoke)"
#     CLINIC_CITY = "Bangkok, Thailand"
#     MAPS_URL = "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw"
#     CALENDLY_URL = "https://calendly.com/laetitiasheppard/new-meeting"
#     DISCOVERY_CALL_URL = "https://calendly.com/laetitiasheppard/30min"
    
#     # Images
#     FOUNDER_IMAGE = "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true"
    
#     # Success Statistics (Honest, Verifiable)
#     SUCCESS_RATE_2_SESSIONS = 85
#     NEED_3RD_SESSION_RATE = 15
    
#     # Pricing (Thai Baht)
#     COMPLETE_PACKAGE_PRICE = 3000
#     PREMIUM_PACKAGE_PRICE = 4000
#     CURRENCY = "THB"

# class QuizConfig:
#     """Quiz configuration and questions"""
    
#     QUESTIONS = {
#         1: {
#             "title": "What would you like to change?",
#             "options": [
#                 ("🚭", "Quit Smoking"),
#                 ("😌", "Reduce Anxiety"),
#                 ("😴", "Improve Sleep"),
#                 ("🔄", "Break Habits")
#             ]
#         },
#         2: {
#             "title": "How long have you dealt with this?",
#             "options": [
#                 ("🆕", "Less than 6 months"),
#                 ("📅", "6 months to 2 years"),
#                 ("⏳", "More than 2 years"),
#                 ("🔄", "Many years")
#             ]
#         },
#         3: {
#             "title": "How ready are you for change?",
#             "options": [
#                 ("🤔", "Just exploring"),
#                 ("👍", "Somewhat ready"),
#                 ("💪", "Very ready"),
#                 ("🔥", "Absolutely determined")
#             ]
#         }
#     }

# class FormConfig:
#     """Form configuration options"""
    
#     CONCERN_OPTIONS = [
#         "Select one...",
#         "Quit Smoking",
#         "Reduce Anxiety",
#         "Improve Sleep",
#         "Break Bad Habits",
#         "Weight Management",
#         "Overcome Phobias",
#         "Boost Confidence",
#         "Other"
#     ]
    
#     URGENCY_OPTIONS = [
#         "How urgent is this?",
#         "Very urgent - need help now",
#         "Somewhat urgent - within a month",
#         "Not urgent - just exploring",
#         "Flexible timing"
#     ]
    
#     EXPERIENCE_OPTIONS = [
#         "Previous hypnotherapy experience?",
#         "No previous experience",
#         "Some experience",
#         "Experienced",
#         "Prefer not to say"
#     ]

# class ContentConfig:
#     """Content and messaging configuration"""
    
#     # Method Session Details
#     SESSION_1 = {
#         "name": "Analysis",
#         "duration": "90 minutes",
#         "description": "Deep dive into subconscious patterns and triggers",
#         "features": [
#             "Uncover subconscious triggers",
#             "Map behavior patterns",
#             "Identify root causes",
#             "Begin positive programming"
#         ]
#     }
    
#     SESSION_2 = {
#         "name": "Hypnosis", 
#         "duration": "90 minutes",
#         "description": "Deep hypnotic state for neural rewiring",
#         "features": [
#             "Deep hypnotic state",
#             "Rewire neural pathways", 
#             "Install new patterns",
#             "Lock in transformation"
#         ]
#     }
    
#     SESSION_3 = {
#         "name": "Reinforcement (Optional)",
#         "duration": "60 minutes",
#         "description": "Optional reinforcement, not needed for 85% of cases",
#         "features": [
#             "Fine-tune remaining patterns",
#             "Address unexpected triggers",
#             "Strengthen new behaviors",
#             "Complete peace of mind"
#         ]
#     }
    
#     # Testimonials (Anonymous for Privacy)
#     TESTIMONIALS = [
#         {
#             "icon": "🌟",
#             "quote": "After years of anxiety controlling my life, I found freedom in just 2 sessions. The change was so profound that my colleagues noticed immediately.",
#             "author": "Banking Director, Singapore",
#             "challenge": "Performance anxiety",
#             "result": "Promoted within 3 months",
#             "sessions": "2 sessions"
#         },
#         {
#             "icon": "🚭",
#             "quote": "My husband smoked 2 packs a day for 20 years. I was smelling his heavy breathe smell Nothing worked until hypnotherapy. He hasn't touched a cigarette since session 2.",
#             "author": "Client's Wife, Bangkok",
#             "challenge": "Heavy smoking (40 cigarettes/day)",
#             "result": "Completely smoke-free",
#             "sessions": "2 sessions"
#         },
#         {
#             "icon": "🎓",
#             "quote": "I was failing my second year of medical school abroad due to overwhelming stress and lack of family support. Now I'm excelling in my specialization and being a doctor has become a conscious vocational career.",
#             "author": "Medical Student, Morocco",
#             "challenge": "Study anxiety and focus",
#             "result": "Improved academic performance",
#             "sessions": "2 sessions"
#         }
#     ]
    
#     # FAQ Content
#     FAQ_ITEMS = [
#         {
#             "question": "Is hypnotherapy safe?",
#             "answer": "Yes, clinical hypnotherapy is completely safe. You remain fully aware and in control throughout the session."
#         },
#         {
#             "question": "How many sessions will I need?",
#             "answer": "85% of clients achieve their goals in just 2 sessions. About 15% opt for an optional 3rd session for reinforcement."
#         },
#         {
#             "question": "What if I can't be hypnotized?",
#             "answer": "This is a myth. Everyone can be hypnotized because hypnosis is a natural state we enter daily (like when absorbed in a book or movie)."
#         },
#         {
#             "question": "Will I lose control during hypnosis?",
#             "answer": "Absolutely not. You remain fully aware and can open your eyes or speak at any time. Hypnosis is not mind control."
#         },
#         {
#             "question": "How much does it cost?",
#             "answer": "Our complete 2-session package is 3,000 THB. Compare this to years of traditional therapy which can cost 60,000+ THB."
#         },
#         {
#             "question": "What are your qualifications?",
#             "answer": "Certified by London College of Clinical Hypnotherapy (2017) and Dialectical Behavioral Therapy certified (2023). Practice established in 2017."
#         }
#     ]

# def get_years_of_experience():
#     """Calculate years of experience since practice establishment"""
#     from datetime import datetime
#     current_year = datetime.now().year
#     return current_year - AppConfig.PRACTICE_ESTABLISHED


"""
Clean configuration module for the Hypnotherapy website
Centralizes all settings and constants
"""

class AppConstants:
    """Application-wide constants"""
    
    # Navigation
    NAVIGATION_OPTIONS = ["Home", "Method", "Success", "Blog", "Book Now"]
    NAVIGATION_ICONS = ["house", "gear", "star", "book", "calendar"]
    
    # Contact information
    CONTACT_INFO = {
        "clinic_name": "Bangkok Hypnotherapy Clinic",
        "address": "27 Soi Sukhumvit 10 (Asoke)",
        "city": "Bangkok, Thailand",
        "maps_url": "https://maps.app.goo.gl/RmobTn5B6JLZ2Lmk8?g_st=aw",
        "calendly_url": "https://calendly.com/laetitiasheppard/new-meeting",
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

class QuizConfig:
    """Quiz configuration and scoring"""
    
    SCORING = {
        1: {  # What to change
            "Quit Smoking": 40,
            "Reduce Anxiety": 35,
            "Improve Sleep": 30,
            "Break Bad Habits": 35,
            "Other": 25
        },
        2: {  # Duration
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30
        },
        3: {  # Readiness
            "Just exploring": 10,
            "Very ready": 30,
            "Desperate for change": 25
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
