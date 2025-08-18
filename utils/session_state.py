"""
Session state management for the Hypnotherapy website
Clean session state handling using Streamlit's built-in system
"""
import streamlit as st

def initialize_session_state():
    """Initialize all session state variables with default values"""
    
    # Quiz-related state
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    
    if 'quiz_step' not in st.session_state:
        st.session_state.quiz_step = 1
    
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    
    # Form-related state
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    
    if 'form_success' not in st.session_state:
        st.session_state.form_success = False
    
    if 'form_error' not in st.session_state:
        st.session_state.form_error = None
    
    # Navigation state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    
    # User data
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
    
    if 'user_email' not in st.session_state:
        st.session_state.user_email = ""
    
    if 'user_concern' not in st.session_state:
        st.session_state.user_concern = ""

def reset_quiz():
    """Reset all quiz-related session state"""
    st.session_state.quiz_answers = {}
    st.session_state.quiz_step = 1
    st.session_state.quiz_completed = False
    st.session_state.quiz_score = 0

def update_quiz_answer(question_id, answer):
    """Update quiz answer and manage progression"""
    st.session_state.quiz_answers[question_id] = answer
    
    # Advance to next step or complete quiz
    if question_id < 3:
        st.session_state.quiz_step = question_id + 1
    else:
        st.session_state.quiz_completed = True

def calculate_quiz_score():
    """Calculate quiz score based on answers"""
    scoring = {
        1: {
            "Quit Smoking": 40,
            "Reduce Anxiety": 35,
            "Improve Sleep": 30,
            "Break Bad Habits": 35,
            "Other": 25
        },
        2: {
            "Less than 6 months": 20,
            "6 months to 2 years": 25,
            "More than 2 years": 30
        },
        3: {
            "Just exploring options": 10,
            "Very ready - I'm committed": 30,
            "Desperate for change": 25
        }
    }
    
    total_score = 0
    for q_id, answer in st.session_state.quiz_answers.items():
        if q_id in scoring and answer in scoring[q_id]:
            total_score += scoring[q_id][answer]
    
    score = min(total_score, 100)
    st.session_state.quiz_score = score
    return score

def reset_form_state():
    """Reset form-related session state"""
    st.session_state.form_submitted = False
    st.session_state.form_success = False
    st.session_state.form_error = None

def set_form_success(success=True):
    """Set form success state"""
    st.session_state.form_success = success
    st.session_state.form_submitted = True

def set_form_error(error_message):
    """Set form error state"""
    st.session_state.form_error = error_message
    st.session_state.form_success = False
    st.session_state.form_submitted = True

def update_user_data(name=None, email=None, concern=None):
    """Update user data in session state"""
    if name is not None:
        st.session_state.user_name = name
    if email is not None:
        st.session_state.user_email = email
    if concern is not None:
        st.session_state.user_concern = concern

def get_quiz_progress():
    """Get quiz completion progress as percentage"""
    total_questions = 3
    answered_questions = len(st.session_state.quiz_answers)
    return (answered_questions / total_questions) * 100

def has_completed_quiz():
    """Check if user has completed the quiz"""
    return st.session_state.quiz_completed

def get_quiz_answers():
    """Get all quiz answers"""
    return st.session_state.quiz_answers

def get_quiz_score():
    """Get the calculated quiz score"""
    return st.session_state.quiz_score

def is_form_submitted():
    """Check if any form has been submitted"""
    return st.session_state.form_submitted

def get_user_data():
    """Get all user data"""
    return {
        'name': st.session_state.user_name,
        'email': st.session_state.user_email,
        'concern': st.session_state.user_concern
    }

def track_page_visit(page_name):
    """Track current page for analytics"""
    st.session_state.current_page = page_name
