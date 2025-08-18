"""
Session State Management
Centralized state management for the hypnotherapy website
"""
import streamlit as st
from typing import Dict, Any

def initialize_session_state():
    """Initialize all session state variables with defaults"""
    defaults = {
        # Quiz state
        'quiz_answers': {},
        'quiz_step': 1,
        'quiz_completed': False,
        'quiz_score': 0,
        'quiz_started': False,
        
        # Form state
        'form_submitted': False,
        'form_success': False,
        'form_errors': [],
        
        # User data
        'user_name': '',
        'user_email': '',
        'user_concern': '',
        'user_phone': '',
        
        # Navigation and analytics
        'current_page': 'Home',
        'page_views': [],
        
        # UI state
        'show_success_modal': False,
        'loading_state': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_quiz():
    """Reset all quiz-related state"""
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1
    st.session_state.quiz_completed = False
    st.session_state.quiz_score = 0
    st.session_state.quiz_started = False

def update_quiz_answer(question_id: int, answer: str):
    """Update quiz answer and progress"""
    st.session_state.quiz_answers[question_id] = answer
    st.session_state.quiz_step += 1
    st.session_state.quiz_started = True
    
    # Check if quiz is completed (3 questions)
    if len(st.session_state.quiz_answers) >= 3:
        st.session_state.quiz_completed = True
        calculate_quiz_score()

def calculate_quiz_score() -> int:
    """Calculate final quiz score based on answers"""
    scoring = {
        1: {  # What transformation are you seeking?
            "Quit Smoking": 40,
            "Reduce Anxiety": 35,
            "Improve Sleep": 30,
            "Break Habits": 35,
            "Other": 25
        },
        2: {  # How long have you been dealing with this?
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30,
            "Many years": 25
        },
        3: {  # How ready are you for transformation?
            "Just exploring": 10,
            "Somewhat ready": 20,
            "Very ready": 30,
            "Absolutely determined": 30
        }
    }
    
    total_score = 0
    for question_id, answer in st.session_state.quiz_answers.items():
        if question_id in scoring and answer in scoring[question_id]:
            total_score += scoring[question_id][answer]
    
    st.session_state.quiz_score = min(total_score, 100)
    return st.session_state.quiz_score

def get_quiz_recommendation(score: int) -> Dict[str, str]:
    """Get personalized recommendation based on quiz score"""
    if score >= 80:
        return {
            "level": "excellent",
            "title": "Excellent Candidate",
            "message": "You're perfectly suited for our 2-session method!",
            "action": "Book Transformation Package"
        }
    elif score >= 65:
        return {
            "level": "very_good",
            "title": "Very Good Fit",
            "message": "Great potential for success with our method.",
            "action": "Free Discovery Call Recommended"
        }
    elif score >= 50:
        return {
            "level": "good",
            "title": "Good Potential",
            "message": "You have good potential for transformation.",
            "action": "Discovery Call Recommended"
        }
    else:
        return {
            "level": "consultation",
            "title": "Let's Talk",
            "message": "A consultation will help us understand your situation.",
            "action": "Free Consultation Recommended"
        }

def update_user_data(name: str = None, email: str = None, concern: str = None, phone: str = None):
    """Update user information"""
    if name is not None:
        st.session_state.user_name = name
    if email is not None:
        st.session_state.user_email = email
    if concern is not None:
        st.session_state.user_concern = concern
    if phone is not None:
        st.session_state.user_phone = phone

def set_form_success(success: bool = True):
    """Set form submission success state"""
    st.session_state.form_success = success
    st.session_state.form_submitted = True
    if success:
        st.session_state.show_success_modal = True

def set_form_errors(errors: list):
    """Set form validation errors"""
    st.session_state.form_errors = errors
    st.session_state.form_success = False

def clear_form_state():
    """Clear all form-related state"""
    st.session_state.form_submitted = False
    st.session_state.form_success = False
    st.session_state.form_errors = []
    st.session_state.show_success_modal = False

def track_page_view(page_name: str):
    """Track page views for analytics"""
    st.session_state.current_page = page_name
    if 'page_views' not in st.session_state:
        st.session_state.page_views = []
    st.session_state.page_views.append(page_name)

def get_user_progress() -> Dict[str, Any]:
    """Get user's progress through the website"""
    return {
        'quiz_completed': st.session_state.get('quiz_completed', False),
        'quiz_score': st.session_state.get('quiz_score', 0),
        'form_submitted': st.session_state.get('form_submitted', False),
        'pages_visited': len(set(st.session_state.get('page_views', []))),
        'current_page': st.session_state.get('current_page', 'Home')
    }
