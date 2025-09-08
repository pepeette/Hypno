"""
Session state management for the Hypnotherapy website
Clean session state handling using Streamlit's built-in system
"""
import streamlit as st

def initialize_session_state():
    """Initialize all session state variables with default values"""
    
    # Enhanced quiz-related state
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    
    if 'quiz_step' not in st.session_state:
        st.session_state.quiz_step = 1
    
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    
    # New quiz tracking variables
    if 'unwanted_pattern' not in st.session_state:
        st.session_state.unwanted_pattern = ""
    
    if 'pattern_duration' not in st.session_state:
        st.session_state.pattern_duration = ""
    
    if 'blocking_mechanism' not in st.session_state:
        st.session_state.blocking_mechanism = ""
    
    if 'readiness_level' not in st.session_state:
        st.session_state.readiness_level = ""
    
    # Existing form and navigation state...
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    
    if 'form_success' not in st.session_state:
        st.session_state.form_success = False
    
    if 'form_error' not in st.session_state:
        st.session_state.form_error = None
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    
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
    st.session_state.unwanted_pattern = ""
    st.session_state.pattern_duration = ""
    st.session_state.blocking_mechanism = ""
    st.session_state.readiness_level = ""

def update_quiz_answer(question_id, answer):
    """Update quiz answer and manage progression"""
    st.session_state.quiz_answers[question_id] = answer
    
    # Store pattern-specific data
    if question_id == 1:
        st.session_state.unwanted_pattern = answer.split('\n')[0]  # Extract main pattern
    elif question_id == 2:
        st.session_state.pattern_duration = answer.split('\n')[0]
    elif question_id == 3:
        st.session_state.blocking_mechanism = answer.split('\n')[0]
    elif question_id == 4:
        st.session_state.readiness_level = answer.split('\n')[0]
    
    # Advance to next step or complete quiz
    if question_id < 4:
        st.session_state.quiz_step = question_id + 1
    else:
        st.session_state.quiz_completed = True
        st.session_state.quiz_score = calculate_quiz_score()

def calculate_quiz_score():
    """Calculate quiz score based on 4-question answers"""
    from utils.config import QuizConfig
    
    total_score = 0
    scoring = QuizConfig.SCORING
    
    for q_id, answer in st.session_state.quiz_answers.items():
        # Extract the main answer (before newline)
        main_answer = answer.split('\n')[0]
        
        if q_id in scoring and main_answer in scoring[q_id]:
            total_score += scoring[q_id][main_answer]
    
    score = min(total_score, 100)
    st.session_state.quiz_score = score
    return score

def get_quiz_recommendation(score):
    """Get recommendation based on quiz score"""
    if score >= 75:
        return {
            "title": "High Suitability",
            "level": "excellent",
            "message": "You show strong indicators for success with our 2-session method.",
            "action": "Book your transformation package or start with a discovery call."
        }
    elif score >= 55:
        return {
            "title": "Good Potential", 
            "level": "good",
            "message": "You have solid foundations for change with proper support.",
            "action": "A discovery call will help us tailor the approach to your situation."
        }
    elif score >= 35:
        return {
            "title": "Assessment Recommended",
            "level": "moderate", 
            "message": "Your situation would benefit from personalized evaluation.",
            "action": "A free discovery call will determine the best path forward."
        }
    else:
        return {
            "title": "Preparation Phase",
            "level": "low",
            "message": "Building readiness first may optimize your success.",
            "action": "Let's discuss your situation and explore when you might be ready."
        }

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
    total_questions = 4  # Updated for 4 questions
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
