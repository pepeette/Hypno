"""
Configuration module for the Hypnotherapy website
Centralizes all configuration settings and constants
"""
import streamlit as st
import os
from typing import Dict, Any

class PageConfig:
    """Page configuration settings"""
    
    @staticmethod
    def setup():
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="2-Step Hypnotherapy | Laetitia Sheppard",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://laetitiasheppard.com/help',
                'Report a bug': 'https://laetitiasheppard.com/bug-report',
                'About': "Transform your life with science-backed hypnotherapy"
            }
        )

class SMTPConfig:
    """SMTP email configuration"""
    
    @property
    def config(self) -> Dict[str, Any]:
        """Get SMTP configuration from environment variables"""
        return {
            "server": os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
            "port": int(os.environ.get("SMTP_PORT", 587)),
            "from_email": os.environ.get("EMAIL_FROM", "website@laetitiasheppard.com"),
            "to_email": os.environ.get("EMAIL_TO", "laetitiasheppard@gmail.com"),
            "username": os.environ.get("SMTP_USERNAME"),
            "password": os.environ.get("SMTP_PASSWORD")
        }
    
    def validate_config(self) -> bool:
        """Validate SMTP configuration completeness"""
        config = self.config
        required_fields = ["username", "password", "from_email", "to_email"]
        return all(config.get(field) for field in required_fields)

class AppConstants:
    """Application-wide constants"""
    
    # Navigation menu options
    NAVIGATION_OPTIONS = ["Home", "Method", "Success", "Blog", "Book Now"]
    NAVIGATION_ICONS = ["house", "magic", "stars", "book", "calendar"]
    
    # Quiz configuration
    QUIZ_TOTAL_QUESTIONS = 3
    
    # Concern options for forms
    CONCERN_OPTIONS = [
        "Select one...", 
        "Quit Smoking", 
        "Reduce Anxiety", 
        "Improve Sleep", 
        "Break Bad Habits",
        "Other"
    ]
    
    # Success rates and statistics
    SUCCESS_RATES = {
        "two_sessions": 85,
        "third_session_needed": 15,
        "ongoing_therapy_needed": 0
    }
    
    # Pricing
    PRICING = {
        "complete_package": 3000,
        "premium_package": 4000,
        "currency": "THB"
    }
    
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
    
    # Image URLs
    IMAGES = {
        "founder_photo": "https://github.com/pepeette/Hypno/blob/main/img/ID.jpg?raw=true",
        "behavior_map": "https://github.com/pepeette/Hypno/blob/main/img%2FBehaviourMap.png?raw=true",
        "transformation": "https://github.com/pepeette/Hypno/blob/main/img%2Femo.jpg?raw=true"
    }

class QuizConfig:
    """Quiz-specific configuration and scoring"""
    
    QUESTIONS = {
        1: {
            "title": "🎯 What would you most like to change or improve?",
            "options": [
                ("🚭", "Quit smoking", "Break free from tobacco addiction"),
                ("😌", "Reduce anxiety", "Find calm and peace of mind"), 
                ("😴", "Improve sleep", "Get better, deeper rest"),
                ("🔄", "Break bad habits", "Change unwanted behaviors"),
                ("❓", "Other", "Something else I'd like to change")
            ]
        },
        2: {
            "title": "⏰ How long have you been dealing with this challenge?",
            "options": [
                ("🆕", "Less than 6 months", "Relatively new challenge"),
                ("📅", "6 months to 2 years", "Moderate duration"),
                ("⏳", "More than 2 years", "Long-standing issue"),
                ("🔄", "Many years", "Deeply ingrained pattern")
            ]
        },
        3: {
            "title": "🚀 How ready are you to make this change happen?",
            "options": [
                ("🤔", "Just exploring options", "Learning about possibilities"),
                ("👍", "Somewhat ready", "Interested and considering"),
                ("💪", "Very ready - I'm committed", "Fully motivated to change"),
                ("🔥", "Desperate for change", "Need transformation now")
            ]
        }
    }
    
    SCORING = {
        1: {  # Question 1: What are you looking to change? (0-40 points)
            "Quit smoking": 40,
            "Reduce anxiety": 35,
            "Improve sleep": 30,
            "Break bad habits": 35,
            "Other": 25
        },
        2: {  # Question 2: How long have you struggled? (0-30 points)
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30,
            "Many years": 25
        },
        3: {  # Question 3: How ready are you? (0-30 points)
            "Just exploring options": 10,
            "Somewhat ready": 20,
            "Very ready - I'm committed": 30,
            "Desperate for change": 25
        }
    }
    
    SUITABILITY_MESSAGES = {
        "excellent": (85, "Excellent candidate for hypnotherapy!", "#22c55e", "🌟"),
        "very_good": (70, "Very good fit for our 2-session method", "#65a30d", "✅"),
        "good": (55, "Good potential with hypnotherapy", "#eab308", "🎯"),
        "moderate": (40, "May benefit with additional preparation", "#f97316", "⚡"),
        "low": (0, "Consider a discovery call first", "#ef4444", "💬")
    }

class TestimonialConfig:
    """Testimonial data configuration"""
    
    TESTIMONIALS = [
        {
            "icon": "🌟",
            "quote": "Finally broke free from old patterns – 2 sessions changed everything.",
            "author": "Director, Banking, Singapore",
            "concern": "Anxiety",
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
