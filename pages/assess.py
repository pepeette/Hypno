"""
COMPREHENSIVE ASSESSMENT - PRODUCTION VERSION
===========================================
Enhanced Behavioral Pattern Assessment v2 with comprehensive clinical profiling
User-friendly assessment with beautiful styling and detailed behavioral analysis

Author: Assessment Enhancement Team
Version: 3.0.0 - Production Ready
Date: 2025-01-25
"""

import streamlit as st
import sys
import os

# Add the utils directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    from utils.config import EnhancedAssessmentConfig, QuestionnaireStage
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Make sure all enhancement modules are available")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Comprehensive Assessment - Production Version",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add comprehensive CSS styling
st.markdown("""
    <style>
    /* Enhanced Assessment Styling with Consistent Layout */
    .assessment-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0.5rem;
        display: flex;
        flex-direction: column;
        min-height: calc(100vh - 120px);
    }

    /* Fixed Header Area */
    .assessment-header {
        background: white;
        padding: 1rem 0 0.5rem 0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }

    .assessment-header h1 {
        font-size: 1.5rem !important;
        margin-bottom: 0.5rem !important;
        line-height: 1.3 !important;
    }

    .assessment-header p {
        margin-bottom: 0 !important;
        color: #64748B;
        font-size: 1rem;
    }

    /* Fixed Question Area */
    .question-area {
        min-height: 160px;
        max-height: 200px;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
        overflow: hidden;
    }

    /* Fixed Answer Area */
    .answer-area {
        min-height: 280px;
        max-height: 380px;
        overflow-y: auto;
        padding: 0.5rem 0;
        margin-bottom: 100px; /* Space for fixed navigation */
    }

    /* Fixed Navigation Area */
    .navigation-area {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px);
        padding: 1rem !important;
        border-top: 1px solid #E2E8F0;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
        z-index: 9999 !important;
    }

    /* Target the Streamlit container that holds navigation */
    .navigation-area .stContainer {
        position: static !important;
    }

    /* Target columns within navigation */
    .navigation-area .stColumns {
        margin: 0 !important;
    }

    .navigation-buttons {
        max-width: 800px;
        margin: 0 auto;
    }

    /* Button consistent sizing */
    .stButton > button {
        height: 48px !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    /* Mobile Responsive Adjustments */
    @media (max-width: 768px) {
        .assessment-container {
            padding: 0.25rem;
            min-height: calc(100vh - 100px);
        }

        .assessment-header h1 {
            font-size: 1.3rem !important;
        }

        .question-area {
            min-height: 140px;
            max-height: 180px;
        }

        .answer-area {
            min-height: 250px;
            max-height: 320px;
            margin-bottom: 90px;
        }

        .navigation-area {
            padding: 0.75rem 0.5rem;
        }

        .stButton > button {
            height: 44px !important;
            font-size: 0.9rem !important;
        }
    }

    /* Hide Streamlit elements that interfere */
    .stApp > header {
        display: none;
    }

    .stApp > .main > .block-container {
        padding-top: 1rem !important;
        padding-bottom: 100px !important;
        max-width: 100% !important;
    }

    /* Ensure content doesn't scroll behind navigation */
    .main .block-container {
        padding-bottom: 120px !important;
    }

    .question-header {
        background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%) !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border-left: 4px solid #4CA1A3 !important;
        margin-bottom: 1.5rem !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1) !important;
        display: block !important;
    }

    .question-text {
        color: #273548 !important;
        font-size: 1.1rem !important;
        line-height: 1.5 !important;
        margin: 0 !important;
        font-weight: 500 !important;
        padding: 0 !important;
    }

    .question-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        box-shadow: 0 4px 20px rgba(39, 53, 72, 0.08);
        border: 1px solid #CBD5E1;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }

    .stage-header {
        background: linear-gradient(135deg, #4CA1A3 0%, #5fb3b5 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }

    /* Button Styling */
    .stButton > button {
        background-color: #4CA1A3;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #3A8A8C;
        box-shadow: 0 4px 12px rgba(76, 161, 163, 0.3);
    }

    .stButton > button:focus {
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.5);
    }

    /* Primary Button (Next) */
    .stButton > button[kind="primary"] {
        background-color: #4CA1A3;
        border: 2px solid #4CA1A3;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #3A8A8C;
        border-color: #3A8A8C;
    }

    /* Radio Button Styling - Fixed for Streamlit */
    .stRadio > div {
        gap: 0.5rem;
    }

    /* Radio button circle styling */
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] {
        padding-left: 0.75rem;
        color: #273548;
        font-weight: 400;
    }

    /* Target the actual radio input */
    .stRadio input[type="radio"] {
        width: 18px;
        height: 18px;
        border: 2px solid #CBD5E1;
        border-radius: 50%;
        background-color: white;
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        cursor: pointer;
        transition: all 0.2s ease;
        position: relative;
        margin-right: 0.5rem;
    }

    /* Hover state */
    .stRadio input[type="radio"]:hover {
        border-color: #4CA1A3;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.1);
    }

    /* Selected state */
    .stRadio input[type="radio"]:checked {
        border-color: #4CA1A3;
        background-color: #4CA1A3;
    }

    /* Inner dot for selected state */
    .stRadio input[type="radio"]:checked::before {
        content: '';
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: white;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    /* Focus state for accessibility */
    .stRadio input[type="radio"]:focus {
        outline: none;
        box-shadow: 0 0 0 2px rgba(76, 161, 163, 0.3);
    }

    /* Label styling */
    .stRadio > div > label {
        display: flex;
        align-items: center;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 6px;
        transition: background-color 0.2s ease;
    }

    .stRadio > div > label:hover {
        background-color: rgba(76, 161, 163, 0.05);
    }

    /* Success Message Styling */
    .stSuccess {
        background-color: rgba(76, 161, 163, 0.1);
        border-left: 4px solid #4CA1A3;
        color: #273548;
    }

    /* Progress Bar Styling - Grey background, teal fill */
    .stProgress > div {
        background-color: #E5E7EB;
    }

    .stProgress > div > div > div {
        background-color: #4CA1A3;
    }

    /* Results styling */
    .results-container {
        background: linear-gradient(135deg, #F8FFFE 0%, #F3F6F8 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid #CBD5E1;
    }

    .pattern-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CA1A3;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .session-planning {
        background: linear-gradient(135deg, #E6F7F7 0%, #F0FFFE 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #4CA1A3;
    }

    .resistance-analysis {
        background: linear-gradient(135deg, #FFF7E6 0%, #FFFAF0 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #D69E2E;
    }

    .trigger-mapping {
        background: linear-gradient(135deg, #F0F4FF 0%, #F7FAFC 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #4C6EF5;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize enhanced assessment
@st.cache_resource
def initialize_assessment():
    return EnhancedAssessmentConfig()

def render_stage_introduction(stage_info, current_stage):
    """Render friendly stage introduction"""
    stage_title = stage_info.get('title', 'ASSESSMENT STAGE').upper()
    return stage_title

def render_question_card(question_data, question_number, total_questions):
    """Render individual question in an appealing card format"""

    progress_percentage = (question_number / total_questions) * 100

    # Use a container to prevent duplication
    with st.container():
        # Progress information
        col1, col2 = st.columns([1, 1])
        with col1:
            st.caption(f"Question {question_number} of {total_questions}")
        with col2:
            st.caption(f"{progress_percentage:.0f}% Complete")

        # Progress bar with unique key
        st.progress(progress_percentage / 100, text=None)

        # Question content with CSS styling - only the question gets the card styling
        question_html = f"""
        <div class="question-header">
            <p class="question-text">{question_data['text']}</p>
        </div>
        """
        st.markdown(question_html, unsafe_allow_html=True)

def render_enhanced_options(options, question_id, key_suffix=""):
    """Render options with enhanced styling"""

    # Create a unique key that includes session state to avoid duplicates
    unique_key = f"radio_{question_id}_{key_suffix}_{st.session_state.current_question}"

    return st.radio(
        "Choose the option that best describes you:",
        options=options,
        key=unique_key,
        label_visibility="collapsed"
    )

def show_preliminary_results(enhanced_assessment, responses):
    """Show preliminary insights and gather contact information"""

    # Generate the profile for preliminary insights
    profile = enhanced_assessment.generate_enhanced_profile(responses)

    st.markdown("# ASSESSMENT COMPLETE")
    st.success("Congratulations! You've completed the comprehensive assessment. Here are some key insights from your responses:")

    # Show 3-4 key statistics
    col1, col2 = st.columns(2)

    with col1:
        # Dominant pattern
        patterns = profile.get('enhanced_pattern_scores', {})
        if patterns:
            dominant_pattern = max(patterns.keys(), key=lambda k: patterns[k] if isinstance(patterns[k], (int, float)) else 0)
            dominant_score = patterns.get(dominant_pattern, 0)
            pattern_names = {
                'unhappiness_culture': 'Unhappiness Culture',
                'power_struggles': 'Power Struggles',
                'systematic_mistrust': 'Systematic Mistrust',
                'separation_division': 'Binary Thinking',
                'doing_vs_being': 'Achievement Focus',
                'digital_despair': 'Digital-Age Patterns'
            }

            st.markdown("""
            <div style="background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
                        padding: 1.5rem; border-radius: 10px; color: white; text-align: center;">
                <h4 style="margin: 0; color: white;">Dominant Pattern</h4>
                <h3 style="margin: 0.5rem 0; color: white;">{}</h3>
                <p style="margin: 0; opacity: 0.9;">Your primary behavioral focus area</p>
            </div>
            """.format(pattern_names.get(dominant_pattern, dominant_pattern.replace('_', ' ').title())),
            unsafe_allow_html=True)

        # Hypnotic readiness
        hypnotic_score = patterns.get('hypnotic_responsiveness', 0) * 100
        if hypnotic_score > 70:
            readiness_text = "High"
            readiness_color = "#22c55e"
        elif hypnotic_score > 40:
            readiness_text = "Moderate"
            readiness_color = "#eab308"
        else:
            readiness_text = "Developing"
            readiness_color = "#ef4444"

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {readiness_color} 0%, {readiness_color}CC 100%);
                    padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin-top: 1rem;">
            <h4 style="margin: 0; color: white;">Hypnotic Readiness</h4>
            <h3 style="margin: 0.5rem 0; color: white;">{readiness_text}</h3>
            <p style="margin: 0; opacity: 0.9;">{hypnotic_score:.0f}% responsive capacity</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Success probability
        success_prob = profile.get('success_probability', {})
        probability = success_prob.get('probability', 85)

        if probability >= 90:
            prob_color = "#22c55e"
            prob_text = "Excellent"
        elif probability >= 75:
            prob_color = "#4CA1A3"
            prob_text = "Very Good"
        elif probability >= 60:
            prob_color = "#eab308"
            prob_text = "Good"
        else:
            prob_color = "#ef4444"
            prob_text = "Challenging"

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {prob_color} 0%, {prob_color}CC 100%);
                    padding: 1.5rem; border-radius: 10px; color: white; text-align: center;">
            <h4 style="margin: 0; color: white;">📈 Success Probability</h4>
            <h3 style="margin: 0.5rem 0; color: white;">{probability}%</h3>
            <p style="margin: 0; opacity: 0.9;">Predicted transformation success</p>
        </div>
        """, unsafe_allow_html=True)

        # Resistance level
        resistance = profile.get('resistance_prediction', {})
        resistance_level = resistance.get('resistance_level', 'Moderate')

        resistance_colors = {
            'Low': '#22c55e',
            'Moderate': '#eab308',
            'High': '#ef4444',
            'Extreme': '#dc2626'
        }

        resistance_level_clean = resistance_level.replace('_resistance', '').replace('_', ' ').title()
        resistance_color = resistance_colors.get(resistance_level_clean, '#eab308')

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {resistance_color} 0%, {resistance_color}CC 100%);
                    padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin-top: 1rem;">
            <h4 style="margin: 0; color: white;">Resistance Level</h4>
            <h3 style="margin: 0.5rem 0; color: white;">{resistance_level_clean}</h3>
            <p style="margin: 0; opacity: 0.9;">Therapeutic challenge level</p>
        </div>
        """, unsafe_allow_html=True)

def render_contact_form():
    """Render contact information form"""
    from datetime import datetime

    st.markdown("---")
    st.markdown("**Get your complete analysis**")
    st.info("To receive your detailed assessment report and personalized therapeutic recommendations, please provide your contact information below.")

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name*", key="contact_first_name")
            email = st.text_input("Email Address*", key="contact_email")
        with col2:
            last_name = st.text_input("Last Name*", key="contact_last_name")
            phone = st.text_input("Phone Number", key="contact_phone")

        urgency = st.selectbox(
            "How urgent is your need for support?*",
            ["Standard - within a week", "High priority - within 2-3 days", "Very urgent - within 24 hours", "Extremely urgent - same day if possible"]
        )

        additional_info = st.text_area(
            "Additional information or specific concerns:",
            placeholder="Any additional details that might help us better understand your situation..."
        )

        submitted = st.form_submit_button("Get My Complete Analysis", type="primary")

        if submitted:
            if first_name and last_name and email:
                # Save contact info
                st.session_state.contact_info = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'urgency': urgency,
                    'additional_info': additional_info,
                    'submission_time': datetime.now().isoformat()
                }
                st.session_state.contact_provided = True
                st.rerun()
            else:
                st.error("Please fill in all required fields (marked with *)")

def show_comprehensive_results(enhanced_assessment, responses):
    """Show comprehensive assessment results with beautiful styling"""

    st.markdown("# YOUR COMPREHENSIVE ASSESSMENT IS COMPLETE")
    st.markdown("Here's your detailed transformation profile")
    st.divider()

    # Generate comprehensive profile
    profile = enhanced_assessment.generate_enhanced_profile(responses)

    # Main results container
    st.markdown('<div class="results-container">', unsafe_allow_html=True)

    # Pattern Hierarchy - Most Important Section
    st.markdown("**Your behavioral pattern profile**")
    hierarchy = profile["pattern_hierarchy"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Dominant Pattern",
            hierarchy["dominant_pattern"]["name"].replace("_", " ").title(),
            f"{hierarchy['dominant_pattern']['score']}/8"
        )
    with col2:
        st.metric(
            "Primary Pattern",
            hierarchy["primary_pattern"]["name"].replace("_", " ").title(),
            f"{hierarchy['primary_pattern']['score']}/8"
        )
    with col3:
        st.metric(
            "Secondary Pattern",
            hierarchy["secondary_pattern"]["name"].replace("_", " ").title(),
            f"{hierarchy['secondary_pattern']['score']}/8"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Session Planning
    st.markdown('<div class="session-planning">', unsafe_allow_html=True)
    st.markdown("**Your transformation plan**")
    session_planning = profile["session_planning"]

    st.markdown(f"Session 1 focus: {session_planning['session_1_focus']}")
    st.markdown(f"Session 2 target: {session_planning['session_2_target']}")
    st.markdown(f"Potential session 3 need: {session_planning['potential_session_3_need']}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Change Readiness
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Change Readiness Score", f"{profile['change_readiness_score']}/10")

    # Behavioral Analysis
    st.markdown("**Understanding your patterns**")
    behavioral = profile["behavioral_analysis"]

    col1, col2 = st.columns(2)
    with col1:
        if behavioral["core_limiting_beliefs"]:
            st.markdown("**Core limiting beliefs**")
            for belief in behavioral["core_limiting_beliefs"]:
                st.markdown(f"• {belief}")

        if behavioral["hidden_benefits"]:
            st.markdown("**Hidden benefits**")
            for benefit in behavioral["hidden_benefits"]:
                st.markdown(f"• {benefit}")

    with col2:
        if behavioral["systemic_resistance"]:
            st.markdown("**Potential challenges**")
            for resistance in behavioral["systemic_resistance"]:
                st.markdown(f"• {resistance}")

        if behavioral["identity_threats"]:
            st.markdown("**Identity considerations**")
            for threat in behavioral["identity_threats"]:
                st.markdown(f"• {threat}")

    # Trigger-Response Patterns
    if profile["trigger_response_mapping"]:
        st.markdown("**Your trigger-response patterns**")
        for pattern_name, pattern_data in profile["trigger_response_mapping"].items():
            with st.expander(f"{pattern_name.replace('_', ' ').title()}"):
                st.markdown('<div class="trigger-mapping">', unsafe_allow_html=True)
                st.write(f"Trigger: {pattern_data['trigger']}")
                st.write(f"Physical response: {pattern_data['physical_response']}")
                st.write(f"Automatic thought: {pattern_data['automatic_thought']}")
                st.write(f"Emotion: {pattern_data['emotion']}")
                st.write(f"Behavior: {pattern_data['behavior']}")
                st.write(f"Consequence: {pattern_data['consequence']}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Resistance Analysis
    st.markdown('<div class="resistance-analysis">', unsafe_allow_html=True)
    st.markdown("**Therapeutic approach recommendations**")
    resistance = profile["resistance_analysis"]

    st.markdown("**Predicted resistance points:**")
    for i, point in enumerate(resistance["predicted_resistance_points"], 1):
        st.write(f"{i}. {point}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"Effective language: {resistance['intervention_keywords']}")
    with col2:
        st.markdown(f"Avoid using: {resistance['avoid_language']}")
    st.markdown('</div>', unsafe_allow_html=True)

    # User Journey Summary
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**Your journey summary**")
        user_journey = profile.get('user_journey', {})

        key_insights = user_journey.get('key_insights', [])
        for insight in key_insights:
            st.markdown(f"• {insight}")

        st.markdown("**Your strongest patterns**")
        strongest_patterns = user_journey.get('strongest_patterns_identified', [])
        for pattern in strongest_patterns:
            st.markdown(f"• {pattern}")

        st.markdown("**Recommended focus areas**")
        focus_areas = user_journey.get('recommended_focus_areas', [])
        for area in focus_areas:
            st.markdown(f"• {area}")

        st.markdown("**Your next steps**")
        next_steps = user_journey.get('next_steps', [])
        for step in next_steps:
            st.markdown(f"• {step}")

    with col2:
        st.markdown("**Assessment summary**")
        st.metric("Questions Answered", profile.get('total_questions_answered', 0))
        st.metric("Completion Rate", f"{profile.get('assessment_completion', 0):.0f}%")

    # Success Probability Analysis (NEW)
    success_prob = profile.get('success_probability', {})
    if success_prob:
        st.markdown('<div class="session-planning">', unsafe_allow_html=True)
        st.markdown("**Success probability analysis**")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Success Probability", f"{success_prob.get('probability', 85)}%")
        with col2:
            st.metric("Confidence Interval", success_prob.get('confidence_interval', '±12%'))
        with col3:
            success_category = success_prob.get('success_category', 'moderate_likelihood')
            st.metric("Success Category", success_category.replace('_', ' ').title())

        # Key recommendations
        key_recs = success_prob.get('key_recommendations', [])
        if key_recs:
            st.markdown("**Key recommendations for success:**")
            for rec in key_recs[:3]:
                st.markdown(f"• {rec}")

        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Pattern Analysis (NEW)
    enhanced_patterns = profile.get('enhanced_pattern_scores', {})
    if enhanced_patterns:
        with st.expander("Enhanced Pattern Analysis"):
            st.markdown("**Advanced pattern detection results:**")
            for pattern, score in enhanced_patterns.items():
                if score > 0:
                    st.write(f"**{pattern.replace('_', ' ').title()}**: {score:.1f}/8")

    # Pattern Interaction Analysis (NEW)
    pattern_interactions = profile.get('pattern_interaction_analysis', {})
    if pattern_interactions:
        with st.expander("🔗 Pattern Interaction Analysis"):
            st.markdown(f"Complexity score: {pattern_interactions.get('complexity_score', 0):.1f}")

            detected_interactions = pattern_interactions.get('detected_interactions', [])
            if detected_interactions:
                st.markdown("**Pattern interactions detected:**")
                for interaction in detected_interactions:
                    patterns = " ↔ ".join([p.replace('_', ' ').title() for p in interaction['patterns']])
                    st.write(f"• **{patterns}**: {interaction['mechanism']}")

    # Neuroplasticity Assessment (NEW)
    neuroplasticity = profile.get('neuroplasticity_assessment', {})
    if neuroplasticity:
        with st.expander("🧘 Neuroplasticity Readiness"):
            readiness_level = neuroplasticity.get('readiness_level', 'moderate_readiness')
            st.markdown(f"Readiness level: {readiness_level.replace('_', ' ').title()}")

            total_score = neuroplasticity.get('total_score', 0)
            st.metric("Neuroplasticity Score", f"{total_score:.1f}/18")

            recommendations = neuroplasticity.get('enhancement_recommendations', [])
            if recommendations:
                st.markdown("**Enhancement recommendations:**")
                for rec in recommendations:
                    st.write(f"• {rec}")

    # Session Protocol Details (NEW)
    session_protocol = profile.get('session_protocol', {})
    if session_protocol:
        with st.expander("Personalized Session Protocol"):
            session_1 = session_protocol.get('session_1', {})
            st.markdown(f"Hypnotic approach: {session_1.get('hypnotic_approach', 'standard').replace('_', ' ').title()}")
            st.markdown(f"Session duration: {session_1.get('duration', 90)} minutes")

            special_considerations = session_1.get('special_considerations', [])
            if special_considerations:
                st.markdown("**Special considerations:**")
                for consideration in special_considerations:
                    st.write(f"• {consideration.replace('_', ' ').title()}")

    # Clinical Details (for practitioners)
    with st.expander("🔬 Clinical Assessment Details (For Practitioners)"):
        st.markdown("**Clinical pattern scores**")
        clinical_scores = profile.get('clinical_scores', {})

        for pattern, score in clinical_scores.items():
            if score > 0:
                st.write(f"**{pattern.replace('_', ' ').title()}**: {score:.1f}")

        st.markdown("**Severity assessment**")
        severity = profile.get('severity_assessment', {})
        for pattern, level in severity.items():
            if level != 'subclinical':
                st.write(f"**{pattern.replace('_', ' ').title()}**: {level.title()}")

        st.markdown("**Clinical recommendations**")
        recommendations = profile.get('clinical_recommendations', [])
        for rec in recommendations:
            st.write(f"• {rec}")

        # Secondary Gain Analysis (NEW)
        secondary_gains = profile.get('secondary_gain_analysis', {})
        if secondary_gains:
            st.markdown("**Secondary gain analysis**")
            total_gain = secondary_gains.get('total_secondary_gain', 0)
            st.write(f"Total secondary gain score: {total_gain}")

            if secondary_gains.get('identity_protection_level', 0) >= 2:
                st.write("High identity protection: Change may feel threatening to sense of self")

        # Resistance Prediction Details (NEW)
        resistance_prediction = profile.get('resistance_prediction', {})
        if resistance_prediction:
            st.markdown("**Resistance prediction analysis**")
            st.write(f"Resistance level: {resistance_prediction.get('resistance_level', 'unknown').replace('_', ' ').title()}")
            st.write(f"Primary type: {resistance_prediction.get('primary_resistance_type', 'unknown').replace('_', ' ').title()}")
            st.write(f"Intervention approach: {resistance_prediction.get('intervention_approach', 'standard').replace('_', ' ').title()}")

        # Cultural Adaptation (NEW)
        cultural_factors = profile.get('cultural_adaptation', {})
        if cultural_factors:
            st.markdown("**Cultural adaptation requirements**")
            adaptations = cultural_factors.get('adaptation_requirements', [])
            for adaptation in adaptations:
                st.write(f"• {adaptation.replace('_', ' ').title()}")

def main():
    """Main application function"""

    # Initialize assessment
    enhanced_assessment = initialize_assessment()

    # Initialize session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    if 'current_stage' not in st.session_state:
        st.session_state.current_stage = QuestionnaireStage.STAGE_1_WELCOME

    # Get all questions
    all_questions = enhanced_assessment.get_enhanced_questions()
    total_questions = len(all_questions)

    # Check if assessment is complete
    if st.session_state.current_question >= total_questions:
        # Initialize contact_provided state if not present
        if 'contact_provided' not in st.session_state:
            st.session_state.contact_provided = False

        # Show preliminary results and contact form if contact not provided yet
        if not st.session_state.contact_provided:
            show_preliminary_results(enhanced_assessment, st.session_state.responses)
            render_contact_form()
            return

        # Show full results after contact is provided
        st.markdown("**COMPREHENSIVE TRANSFORMATION ASSESSMENT**")
        st.markdown("Your detailed behavioral analysis and therapeutic roadmap")
        st.divider()
        show_comprehensive_results(enhanced_assessment, st.session_state.responses)

        # Reset button
        if st.button("Take Assessment Again", type="primary"):
            # Clear session state
            for key in list(st.session_state.keys()):
                if key.startswith(('current_question', 'responses', 'current_stage', 'contact_')):
                    del st.session_state[key]
            st.rerun()
        return

    # Get current question
    current_q = all_questions[st.session_state.current_question]
    current_question_number = st.session_state.current_question + 1

    # Check if we need to show stage introduction and update header
    current_stage = QuestionnaireStage(current_q['stage'])
    stage_title = ""
    if current_stage != st.session_state.current_stage:
        st.session_state.current_stage = current_stage
        stage_info = enhanced_assessment.get_stage_introduction(current_q['stage'])
        stage_title = f" : {render_stage_introduction(stage_info, current_stage)}"

    # Create main assessment container
    st.markdown('<div class="assessment-container">', unsafe_allow_html=True)

    # Fixed Header Area
    st.markdown('<div class="assessment-header">', unsafe_allow_html=True)
    header_text = f"**COMPREHENSIVE TRANSFORMATION ASSESSMENT{stage_title}**"
    st.markdown(header_text)
    st.markdown('</div>', unsafe_allow_html=True)

    # Fixed Question Area
    st.markdown('<div class="question-area">', unsafe_allow_html=True)
    render_question_card(current_q, current_question_number, total_questions)
    st.markdown('</div>', unsafe_allow_html=True)

    # Fixed Answer Area
    st.markdown('<div class="answer-area">', unsafe_allow_html=True)
    response = render_enhanced_options(
        current_q['options'],
        current_q['id'],
        key_suffix=str(current_question_number)
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close assessment-container

    # Fixed Navigation Area using container
    with st.container():
        st.markdown('<div class="navigation-area">', unsafe_allow_html=True)
        st.markdown('<div class="navigation-buttons">', unsafe_allow_html=True)

        # Navigation buttons using columns within the fixed navigation
        col_prev, col_next, col_skip = st.columns([1, 1, 1])

        with col_prev:
            if st.session_state.current_question > 0:
                if st.button("← Previous", use_container_width=True, key="nav_prev"):
                    st.session_state.current_question -= 1
                    st.rerun()

        with col_next:
            if response:
                if st.button("Next →", use_container_width=True, type="primary", key="nav_next"):
                    # Save response
                    st.session_state.responses[current_q['id']] = response
                    st.session_state.current_question += 1
                    st.rerun()

        with col_skip:
            if current_q.get('required', True) == False:
                if st.button("Skip", use_container_width=True, key="nav_skip"):
                    st.session_state.current_question += 1
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)  # Close navigation-buttons
        st.markdown('</div>', unsafe_allow_html=True)  # Close navigation-area

class create_assess_page:
    """Compatibility wrapper for app.py integration"""

    def render(self):
        """Render the assessment page"""
        main()

if __name__ == "__main__":
    main()
