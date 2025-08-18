"""
Professional Suitability Quiz Component
With progress tracking, visual feedback, and personalized results
"""
from utils import config, styling
import streamlit as st

QUESTIONS = [
    {
        "question": "How long have you been dealing with this issue?",
        "options": [
            "Less than 6 months",
            "6 months to 2 years", 
            "More than 2 years"
        ],
        "weights": [1, 2, 3]
    },
    {
        "question": "How does this affect your daily life?",
        "options": [
            "Minimal impact",
            "Noticeable but manageable",
            "Severely disruptive"
        ],
        "weights": [1, 2, 3]
    },
    {
        "question": "What's your belief about change?",
        "options": [
            "I can change easily",
            "Change is possible with help",
            "I doubt change is possible"
        ],
        "weights": [3, 2, 1]  # Reverse scored
    }
]

def show_quiz():
    """Main quiz component with all features"""
    _init_quiz_state()
    _render_progress_bar()
    
    if st.session_state.quiz_step < len(QUESTIONS):
        _render_current_question()
    else:
        _render_results()
        st.session_state.quiz_completed = True

def _init_quiz_state():
    """Initialize quiz session state"""
    if 'quiz_step' not in st.session_state:
        st.session_state.quiz_step = 0
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = []

def _render_progress_bar():
    """Visual progress indicator"""
    progress = st.progress((st.session_state.quiz_step) / len(QUESTIONS))
    st.caption(f"Question {st.session_state.quiz_step + 1} of {len(QUESTIONS)}")

def _render_current_question():
    """Render current question with options"""
    question = QUESTIONS[st.session_state.quiz_step]
    
    st.markdown(f"### {question['question']}")
    
    # Visual options with hover effects
    cols = st.columns(2)
    for idx, option in enumerate(question['options']):
        with cols[idx % 2]:
            if st.button(
                option,
                key=f"q{st.session_state.quiz_step}_o{idx}",
                use_container_width=True
            ):
                _handle_answer(question['weights'][idx])
                st.rerun()

def _handle_answer(weight):
    """Store answer and advance quiz"""
    st.session_state.quiz_answers.append(weight)
    st.session_state.quiz_step += 1

def _render_results():
    """Show personalized results based on score"""
    total_score = sum(st.session_state.quiz_answers)
    
    st.markdown("## Your Assessment Results")
    st.markdown("---")
    
    if total_score <= 4:
        _render_result_card(
            "Excellent Candidate",
            "Our methods are likely very effective for your situation",
            "😊",
            f"""
            - High likelihood of success (85%+)
            - Typically see results in 1-2 sessions
            - Book your initial session below
            """
        )
    elif total_score <= 7:
        _render_result_card(
            "Good Candidate",
            "We can help, though may require additional sessions",
            "🤔", 
            f"""
            - Good potential for change (65-85%)
            - May benefit from 2-3 sessions  
            - Recommend discovery call
            """
        )
    else:
        _render_result_card(
            "Challenging Case",
            "We recommend a consultation to assess suitability",
            "🧐",
            f"""
            - Complex/long-standing issue
            - Requires detailed evaluation
            - 50-65% success likelihood
            """
        )
    
    st.markdown("---")
    st.button("Book Discovery Call", type="primary")

def _render_result_card(title, subtitle, emoji, content):
    """Styled result card"""
    st.markdown(f"""
    <div style='
        background: {config.card_bg};
        padding: 1.5rem;
        border-radius: {config.radius_md};
        border-left: 4px solid {config.accent_color};
        margin: 1rem 0;
    '>
        <div style='display: flex; align-items: center; gap: 1rem;'>
            <span style='font-size: 2rem;'>{emoji}</span>
            <div>
                <h3>{title}</h3>
                <p>{subtitle}</p>
            </div>
        </div>
        <div style='margin-top: 1rem;'>
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)
