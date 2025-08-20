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
