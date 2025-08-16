"""
Session state management for the Hypnotherapy website
Handles all session state initialization and management
"""
import streamlit as st
from typing import Dict, Any

class SessionStateKeys:
    """Constants for session state keys to avoid typos"""
    
    # Quiz-related keys
    QUIZ_ANSWERS = "quiz_answers"
    QUIZ_STEP = "quiz_step"
    QUIZ_COMPLETED = "quiz_completed"
    QUIZ_SCORE = "quiz_score"
    QUIZ_STARTED = "quiz_started"
    
    # Form-related keys
    FORM_SUBMITTED = "form_submitted"
    FORM_SUCCESS = "form_success"
    FORM_ERROR = "form_error"
    
    # Navigation-related keys
    LAST_PAGE = "last_page"
    PAGE_VISITED = "page_visited"
    
    # User data keys
    USER_EMAIL = "user_email"
    USER_NAME = "user_name"
    USER_CONCERN = "user_concern"
    
    # UI state keys
    SHOW_SUCCESS_MESSAGE = "show_success_message"
    LOADING_STATE = "loading_state"

class SessionStateManager:
    """Manages session state initialization and updates"""
    
    @staticmethod
    def initialize_session_state():
        """Initialize all session state variables with default values"""
        default_values = {
            # Quiz state
            SessionStateKeys.QUIZ_ANSWERS: {},
            SessionStateKeys.QUIZ_STEP: 1,
            SessionStateKeys.QUIZ_COMPLETED: False,
            SessionStateKeys.QUIZ_SCORE: 0,
            SessionStateKeys.QUIZ_STARTED: False,
            
            # Form state
            SessionStateKeys.FORM_SUBMITTED: False,
            SessionStateKeys.FORM_SUCCESS: False,
            SessionStateKeys.FORM_ERROR: None,
            
            # Navigation state
            SessionStateKeys.LAST_PAGE: "Home",
            SessionStateKeys.PAGE_VISITED: set(),
            
            # User data
            SessionStateKeys.USER_EMAIL: "",
            SessionStateKeys.USER_NAME: "",
            SessionStateKeys.USER_CONCERN: "",
            
            # UI state
            SessionStateKeys.SHOW_SUCCESS_MESSAGE: False,
            SessionStateKeys.LOADING_STATE: False,
        }
        
        for key, default_value in default_values.items():
            if key not in st.session_state:
                st.session_state[key] = default_value
    
    @staticmethod
    def reset_quiz():
        """Reset all quiz-related session state"""
        st.session_state[SessionStateKeys.QUIZ_ANSWERS] = {}
        st.session_state[SessionStateKeys.QUIZ_STEP] = 1
        st.session_state[SessionStateKeys.QUIZ_COMPLETED] = False
        st.session_state[SessionStateKeys.QUIZ_SCORE] = 0
        st.session_state[SessionStateKeys.QUIZ_STARTED] = False
    
    @staticmethod
    def update_quiz_answer(question_id: int, answer: str):
        """Update quiz answer and advance to next step"""
        st.session_state[SessionStateKeys.QUIZ_ANSWERS][question_id] = answer
        st.session_state[SessionStateKeys.QUIZ_STEP] += 1
        st.session_state[SessionStateKeys.QUIZ_STARTED] = True
        
        # Check if quiz is completed
        if len(st.session_state[SessionStateKeys.QUIZ_ANSWERS]) >= 3:
            st.session_state[SessionStateKeys.QUIZ_COMPLETED] = True
    
    @staticmethod
    def go_to_previous_question():
        """Go back to the previous quiz question"""
        current_step = st.session_state[SessionStateKeys.QUIZ_STEP]
        if current_step > 1:
            st.session_state[SessionStateKeys.QUIZ_STEP] -= 1
            # Remove the answer for the question we're going back from
            if current_step - 1 in st.session_state[SessionStateKeys.QUIZ_ANSWERS]:
                del st.session_state[SessionStateKeys.QUIZ_ANSWERS][current_step - 1]
            
            # Update completed status
            if len(st.session_state[SessionStateKeys.QUIZ_ANSWERS]) < 3:
                st.session_state[SessionStateKeys.QUIZ_COMPLETED] = False
    
    @staticmethod
    def set_quiz_score(score: int):
        """Set the calculated quiz score"""
        st.session_state[SessionStateKeys.QUIZ_SCORE] = score
    
    @staticmethod
    def reset_form_state():
        """Reset form-related session state"""
        st.session_state[SessionStateKeys.FORM_SUBMITTED] = False
        st.session_state[SessionStateKeys.FORM_SUCCESS] = False
        st.session_state[SessionStateKeys.FORM_ERROR] = None
    
    @staticmethod
    def set_form_success(success: bool = True):
        """Set form success state"""
        st.session_state[SessionStateKeys.FORM_SUCCESS] = success
        st.session_state[SessionStateKeys.FORM_SUBMITTED] = True
        st.session_state[SessionStateKeys.SHOW_SUCCESS_MESSAGE] = success
    
    @staticmethod
    def set_form_error(error_message: str):
        """Set form error state"""
        st.session_state[SessionStateKeys.FORM_ERROR] = error_message
        st.session_state[SessionStateKeys.FORM_SUCCESS] = False
        st.session_state[SessionStateKeys.FORM_SUBMITTED] = True
    
    @staticmethod
    def clear_messages():
        """Clear all success and error messages"""
        st.session_state[SessionStateKeys.SHOW_SUCCESS_MESSAGE] = False
        st.session_state[SessionStateKeys.FORM_ERROR] = None
    
    @staticmethod
    def set_loading(loading: bool = True):
        """Set loading state"""
        st.session_state[SessionStateKeys.LOADING_STATE] = loading
    
    @staticmethod
    def update_user_data(name: str = None, email: str = None, concern: str = None):
        """Update user data in session state"""
        if name is not None:
            st.session_state[SessionStateKeys.USER_NAME] = name
        if email is not None:
            st.session_state[SessionStateKeys.USER_EMAIL] = email
        if concern is not None:
            st.session_state[SessionStateKeys.USER_CONCERN] = concern
    
    @staticmethod
    def track_page_visit(page_name: str):
        """Track which pages the user has visited"""
        if SessionStateKeys.PAGE_VISITED not in st.session_state:
            st.session_state[SessionStateKeys.PAGE_VISITED] = set()
        
        st.session_state[SessionStateKeys.PAGE_VISITED].add(page_name)
        st.session_state[SessionStateKeys.LAST_PAGE] = page_name
    
    @staticmethod
    def get_quiz_progress() -> float:
        """Get quiz completion progress as percentage"""
        total_questions = 3
        answered_questions = len(st.session_state.get(SessionStateKeys.QUIZ_ANSWERS, {}))
        return (answered_questions / total_questions) * 100
    
    @staticmethod
    def has_completed_quiz() -> bool:
        """Check if user has completed the quiz"""
        return st.session_state.get(SessionStateKeys.QUIZ_COMPLETED, False)
    
    @staticmethod
    def get_quiz_answers() -> Dict[int, str]:
        """Get all quiz answers"""
        return st.session_state.get(SessionStateKeys.QUIZ_ANSWERS, {})
    
    @staticmethod
    def get_quiz_score() -> int:
        """Get the calculated quiz score"""
        return st.session_state.get(SessionStateKeys.QUIZ_SCORE, 0)
    
    @staticmethod
    def is_form_submitted() -> bool:
        """Check if any form has been submitted"""
        return st.session_state.get(SessionStateKeys.FORM_SUBMITTED, False)
    
    @staticmethod
    def get_user_data() -> Dict[str, str]:
        """Get all user data"""
        return {
            'name': st.session_state.get(SessionStateKeys.USER_NAME, ''),
            'email': st.session_state.get(SessionStateKeys.USER_EMAIL, ''),
            'concern': st.session_state.get(SessionStateKeys.USER_CONCERN, '')
        }

def initialize_session_state():
    """Initialize session state - to be called from app.py"""
    SessionStateManager.initialize_session_state()

# Convenience functions for easier imports
def reset_quiz():
    """Reset quiz state"""
    SessionStateManager.reset_quiz()

def update_quiz_answer(question_id: int, answer: str):
    """Update quiz answer"""
    SessionStateManager.update_quiz_answer(question_id, answer)

def set_quiz_score(score: int):
    """Set quiz score"""
    SessionStateManager.set_quiz_score(score)

def set_form_success(success: bool = True):
    """Set form success state"""
    SessionStateManager.set_form_success(success)

def set_form_error(error_message: str):
    """Set form error state"""
    SessionStateManager.set_form_error(error_message)

def track_page_visit(page_name: str):
    """Track page visit"""
    SessionStateManager.track_page_visit(page_name)
