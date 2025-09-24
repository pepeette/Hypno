"""
Enhanced Behavioral Pattern Assessment v2
Sophisticated content-driven assessment with adaptive questioning
Digital despair integration and comprehensive profiling
"""

import streamlit as st
import json
import smtplib
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple

# Email imports with error handling
try:
    from email.mime.text import MimeText
    from email.mime.multipart import MimeMultipart
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False

# Import enhanced configuration
try:
    from utils.config import (
        SmartQuestionMatrix,
        DigitalDespairAssessment,
        AdaptiveQuestionFlow,
        ComprehensiveProfiler,
        EnhancedEmailConfig,
        SkipLogic
    )
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    st.error("Enhanced configuration not available. Please ensure utils/config2.py exists.")

# ================================
# ENHANCED ASSESSMENT ORCHESTRATOR
# ================================

class EnhancedAssessmentOrchestrator:
    """Sophisticated assessment flow with content-driven engagement"""

    def __init__(self):
        self.initialize_session_state()
        self.question_flow = AdaptiveQuestionFlow() if CONFIG_AVAILABLE else None

    def initialize_session_state(self):
        """Initialize enhanced session state management"""
        if 'assessment_v2_responses' not in st.session_state:
            st.session_state.assessment_v2_responses = {}

        if 'assessment_v2_phase' not in st.session_state:
            st.session_state.assessment_v2_phase = "discovery"

        if 'assessment_v2_path' not in st.session_state:
            st.session_state.assessment_v2_path = None

        if 'skip_counts' not in st.session_state:
            st.session_state.skip_counts = {}

        if 'current_question_id' not in st.session_state:
            st.session_state.current_question_id = None

        # Initialize question history tracking for previous button
        if 'question_history' not in st.session_state:
            st.session_state.question_history = []

        if 'assessment_v2_completed' not in st.session_state:
            st.session_state.assessment_v2_completed = False

        if 'comprehensive_profile' not in st.session_state:
            st.session_state.comprehensive_profile = None

    def render(self):
        """Main assessment rendering with elegant visual design"""

        # Apply sophisticated CSS styling
        self._apply_assessment_styling()

        # Render assessment header with progress
        self._render_elegant_header()

        # Main assessment flow
        if not st.session_state.assessment_v2_completed:
            self._render_question_flow()
        else:
            self._render_comprehensive_results()

    def _apply_assessment_styling(self):
        """Apply sophisticated visual styling"""
        st.markdown("""
        <style>
        /* Enhanced Assessment Styling */
        .assessment-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }

        .question-header {
            background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #4CA1A3;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .question-text {
            color: #273548;
            font-size: 1.1rem;
            line-height: 1.5;
            margin: 0;
            font-weight: 500;
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

        .option-button {
            background: #F3F6F8;
            border: 2px solid #CBD5E1;
            border-radius: 8px;
            padding: 0.8rem 1.2rem;
            margin: 0.05rem;
            color: #273548;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            text-align: center;
            font-size: 1rem;
            min-height: 2.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .options-grid {
            display: grid;
            gap: 0.3rem;
            margin-bottom: 1rem;
        }

        .options-grid-2 {
            grid-template-columns: 1fr 1fr;
        }

        .options-grid-1 {
            grid-template-columns: 1fr;
        }

        .option-button:hover {
            background: #4CA1A3;
            color: white;
            border-color: #4CA1A3;
            transform: translateX(5px);
        }

        .progress-indicator {
            background: linear-gradient(90deg, #4CA1A3 0%, #3B7A7A 100%);
            height: 6px;
            border-radius: 3px;
            margin-bottom: 1.5rem;
            transition: width 0.5s ease;
            box-shadow: 0 1px 3px rgba(76, 161, 163, 0.3);
        }

        .progress-container {
            background: white;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            margin-bottom: 1.5rem;
            border: 1px solid #E8E8E8;
        }

        .progress-stats {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.8rem;
            font-size: 0.9rem;
        }

        .progress-left {
            color: #4CA1A3;
            font-weight: 500;
        }

        .progress-right {
            color: #556D7A;
        }

        .phase-label {
            color: #556D7A;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .skip-option {
            color: #556D7A;
            font-size: 0.9rem;
            text-align: center;
            padding: 1rem;
            cursor: pointer;
            transition: color 0.3s ease;
        }

        .skip-option:hover {
            color: #4CA1A3;
        }

        .insights-preview {
            background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
            border-left: 4px solid #4CA1A3;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
        }

        .pattern-detection {
            background: rgba(76, 161, 163, 0.1);
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            border: 1px solid rgba(76, 161, 163, 0.2);
        }

        /* Results styling */
        .results-hero {
            background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
        }

        .pattern-card {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            border-left: 4px solid #4CA1A3;
        }

        .insight-box {
            background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%);
            border: 1px solid #CBD5E1;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            border-left: 3px solid #4CA1A3;
        }

        /* Hide Streamlit elements */
        header[data-testid="stHeader"] {
            display: none !important;
        }

        .stDeployButton {
            display: none !important;
        }

        /* Mobile optimization */
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .question-header {
                padding: 1rem;
            }

            .question-card {
                padding: 2rem 1.5rem;
                margin-bottom: 1.5rem;
            }

            .question-text {
                font-size: 1rem;
            }

            .option-button {
                padding: 1rem;
                font-size: 0.95rem;
            }

            .options-grid-2 {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """, unsafe_allow_html=True)

    def _render_elegant_header(self):
        """Render sophisticated header with detailed progress indication"""

        # Calculate progress with better estimation
        current_progress = len(st.session_state.assessment_v2_responses)

        # Get more accurate total based on assessment progress and phase
        if hasattr(self.question_flow, 'assessment_path') and hasattr(self.question_flow, 'current_phase'):
            total_expected = self._get_accurate_total_questions()
        else:
            # For initial questions (before path determination), show conservative estimate
            if current_progress == 0:
                total_expected = 25  # Show a realistic middle-ground estimate initially
            else:
                total_expected = self._estimate_total_questions()

        # Ensure we never show less than current progress + 1
        total_expected = max(total_expected, current_progress + 1)

        progress_percentage = min(100, (current_progress / total_expected) * 100) if total_expected > 0 else 0

        # Smart time estimation based on question complexity and user patterns
        # If current question is the last question (current_progress >= total_expected), show 0 time
        if current_progress >= total_expected:
            questions_remaining = 0
            time_remaining = 0
        else:
            questions_remaining = max(0, total_expected - current_progress)
            time_remaining = self._calculate_smart_time_estimate(questions_remaining, current_progress)

        # Format time display
        if time_remaining >= 60:
            minutes = int(time_remaining // 60)
            seconds = int(time_remaining % 60)
            if seconds > 0:
                time_display = f"{minutes}:{seconds:02d} min"
            else:
                time_display = f"{minutes} min"
        elif time_remaining > 0:
            time_display = f"{int(time_remaining)} sec"
        else:
            time_display = "Almost done!"

        # Phase descriptions
        phase_descriptions = {
            "discovery": "DISCOVERY",
            "adaptive_assessment": "PATTERN EXPLORATION",
            "pattern_validation": "DEEP ANALYSIS",
            "integration": "TRANSFORMATION PLANNING"
        }

        current_phase = st.session_state.assessment_v2_phase
        phase_title = phase_descriptions.get(current_phase, "ASSESSMENT")

        # Compact header without main title
        st.markdown(f"""
        <div class="assessment-container" style="margin-top: 0; padding-top: 0.2rem;">
            <div class="phase-label" style="margin-bottom: 0.3rem;">Behavioral Assessment: {phase_title}</div>
            <div class="progress-stats">
                <div class="progress-left">
                    Question {current_progress + 1} of {total_expected}
                </div>
                <div class="progress-right">
                    ⏱️ {time_display} remaining
                </div>
            </div>
            <div class="progress-container" style="margin-bottom: 0.8rem;">
                <div class="progress-indicator" style="width: {max(progress_percentage, 1)}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    def _render_question_flow(self):
        """Render adaptive question flow with elegant interactions"""

        if not CONFIG_AVAILABLE:
            st.error("Configuration not available. Cannot proceed with assessment.")
            return

        try:
            # Safety check - prevent infinite loops
            current_question_count = len(st.session_state.assessment_v2_responses)
            if current_question_count > 35:  # Safety limit
                st.warning("Assessment limit reached. Proceeding to results.")
                self._complete_assessment()
                return

            # Get next question
            question_id, question_data = self.question_flow.get_next_question(
                st.session_state.assessment_v2_responses
            )

            # Update session state phase
            st.session_state.assessment_v2_phase = self.question_flow.current_phase

            if question_id is None:
                # Assessment complete, generate profile
                self._complete_assessment()
                return

            # Validate question data
            if not question_data or 'text' not in question_data:
                st.error(f"Invalid question data for question: {question_id}")
                # Skip to next question
                st.session_state.assessment_v2_responses[question_id] = "INVALID_QUESTION"
                st.rerun()
                return

            # Additional validation for question structure
            question_type = question_data.get('type', 'single_choice')
            if question_type == 'single_choice' and 'options' not in question_data:
                st.error(f"Single choice question missing options: {question_id}")
                st.session_state.assessment_v2_responses[question_id] = "MISSING_OPTIONS"
                st.rerun()
                return
            elif question_type == 'multiple_choice' and 'options' not in question_data:
                st.error(f"Multiple choice question missing options: {question_id}")
                st.session_state.assessment_v2_responses[question_id] = "MISSING_OPTIONS"
                st.rerun()
                return
            elif question_type == 'scale_agreement' and 'scale' not in question_data:
                st.error(f"Scale question missing scale: {question_id}")
                st.session_state.assessment_v2_responses[question_id] = "MISSING_SCALE"
                st.rerun()
                return

            # Update current question
            st.session_state.current_question_id = question_id

            # Track question history for previous button
            if question_id not in st.session_state.question_history:
                st.session_state.question_history.append(question_id)

            # Render question with sophisticated styling
            self._render_sophisticated_question(question_id, question_data)

            # Use pattern components for question enhancement (without explicit insights)
            self._enhance_question_with_patterns()

        except Exception as e:
            st.error(f"Critical error in question flow: {str(e)}")
            st.error("Please refresh the page to continue your assessment.")

            # Debug information
            if st.checkbox("Show debug information"):
                st.code(f"Current phase: {getattr(self.question_flow, 'current_phase', 'Unknown')}")
                st.code(f"Responses count: {len(st.session_state.assessment_v2_responses)}")
                st.code(f"Last question ID: {st.session_state.get('current_question_id', 'Unknown')}")

            # Emergency reset option
            if st.button("🚨 Reset Assessment (This will clear all progress)"):
                for key in list(st.session_state.keys()):
                    if key.startswith('assessment_v2'):
                        del st.session_state[key]
                st.rerun()

    def _render_sophisticated_question(self, question_id: str, question_data: Dict):
        """Render individual question with high-quality visual design"""

        try:
            # Question text with beautiful header styling
            st.markdown(f"""
            <div class="question-header">
                <div class="question-text">
                    {question_data['text']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Render response options based on question type with error handling
            question_type = question_data.get('type', 'single_choice')

            if question_type == 'single_choice':
                self._render_single_choice_options(question_id, question_data)
            elif question_type == 'multiple_choice':
                self._render_multiple_choice_options(question_id, question_data)
            elif question_type == 'scale_agreement':
                self._render_scale_agreement(question_id, question_data)
            else:
                st.error(f"Unknown question type: {question_type}")
                return

        except Exception as e:
            st.error(f"Error rendering question {question_id}: {str(e)}")
            # Add fallback to skip the problematic question
            if st.button(f"Skip question due to error", key=f"{question_id}_error_skip"):
                st.session_state.assessment_v2_responses[question_id] = "ERROR_SKIPPED"
                st.rerun()

    def _render_single_choice_options(self, question_id: str, question_data: Dict):
        """Render single choice options with responsive Streamlit columns"""

        options = question_data['options']
        num_options = len(options)

        # Determine layout based on number of options and option length
        # Use 2 columns for 2-6 options if text is short, otherwise single column
        use_two_columns = (
            2 <= num_options <= 6 and
            all(len(option) <= 40 for option in options)  # Short text options
        )

        if use_two_columns:
            # Two-column layout
            col1, col2 = st.columns(2)
            for i, option in enumerate(options):
                with col1 if i % 2 == 0 else col2:
                    if st.button(
                        option,
                        key=f"{question_id}_option_{i}",
                        help="Click to select this option",
                        use_container_width=True
                    ):
                        st.session_state.assessment_v2_responses[question_id] = option
                        st.rerun()
        else:
            # Single-column layout
            for i, option in enumerate(options):
                if st.button(
                    option,
                    key=f"{question_id}_option_{i}",
                    help="Click to select this option",
                    use_container_width=True
                ):
                    st.session_state.assessment_v2_responses[question_id] = option
                    st.rerun()

        # Add skip option if allowed with column layout
        if question_data.get('skip_allowed', False):
            st.markdown("<br>", unsafe_allow_html=True)  # Small spacing
            col1, col2 = st.columns(2)
            # Split col2 into two half-width buttons for Previous and Skip
            col2a, col2b = st.columns(2)

            with col2a:
                if st.button("Previous", key=f"{question_id}_single_previous", help="Go to previous question", use_container_width=True):
                    self._handle_previous_question()

            with col2b:
                if st.button("Skip", key=f"{question_id}_single_skip", help="Skip to next question", use_container_width=True):
                    st.session_state.assessment_v2_responses[question_id] = "SKIPPED"
                    st.rerun()

    def _render_multiple_choice_options(self, question_id: str, question_data: Dict):
        """Render multiple choice with checkboxes"""

        try:
            st.markdown("**Select all that apply:**")

            # Initialize session state for this question if not exists
            checkbox_key = f"{question_id}_multiselect"
            if checkbox_key not in st.session_state:
                st.session_state[checkbox_key] = []

            selected_options = []
            options = question_data.get('options', [])

            if not options:
                st.error("No options available for this question")
                return

            for i, option in enumerate(options):
                checkbox_key_individual = f"{question_id}_check_{i}"
                if st.checkbox(option, key=checkbox_key_individual):
                    selected_options.append(option)

            # Buttons in two columns
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Continue", key=f"{question_id}_continue", use_container_width=True):
                    if selected_options:
                        st.session_state.assessment_v2_responses[question_id] = selected_options
                        st.rerun()
                    else:
                        st.warning("Please select at least one option to continue.")

            # Split col2 into two half-width buttons for Previous and Skip
            col2a, col2b = st.columns(2)

            with col2a:
                if st.button("Previous", key=f"{question_id}_mc_previous", help="Go to previous question", use_container_width=True):
                    self._handle_previous_question()

            with col2b:
                if st.button("Skip", key=f"{question_id}_mc_skip", help="Skip to next question", use_container_width=True):
                    st.session_state.assessment_v2_responses[question_id] = "SKIPPED"
                    st.rerun()

        except Exception as e:
            st.error(f"Error rendering multiple choice options: {str(e)}")
            # Fallback to skip
            if st.button("Skip due to error", key=f"{question_id}_mc_error"):
                st.session_state.assessment_v2_responses[question_id] = "ERROR_SKIPPED"
                st.rerun()

    def _render_scale_agreement(self, question_id: str, question_data: Dict):
        """Render agreement scale with visual slider"""

        try:
            scale_options = question_data.get('scale', [])

            if not scale_options:
                st.error("No scale options available for this question")
                # Fallback to skip
                if st.button("Skip due to missing scale", key=f"{question_id}_no_scale"):
                    st.session_state.assessment_v2_responses[question_id] = "NO_SCALE"
                    st.rerun()
                return

            # Ensure scale_options is a list
            if not isinstance(scale_options, list):
                st.error("Invalid scale format")
                if st.button("Skip due to invalid scale", key=f"{question_id}_invalid_scale"):
                    st.session_state.assessment_v2_responses[question_id] = "INVALID_SCALE"
                    st.rerun()
                return

            # Find neutral option
            neutral_index = len(scale_options) // 2  # Find middle option

            # Ensure we have a neutral option
            if len(scale_options) % 2 == 1:  # Odd number of options
                default_value = scale_options[neutral_index]
            else:  # Even number, pick the lower middle
                default_value = scale_options[neutral_index - 1] if neutral_index > 0 else scale_options[0]

            # Create elegant scale selection with guaranteed neutral default
            selected_value = st.select_slider(
                "Your response:",
                options=scale_options,
                value=default_value,  # Always neutral
                key=f"{question_id}_scale"
            )

            # Visual feedback for neutral position
            st.markdown("""
            <div style="text-align: center; color: #556D7A; font-size: 0.8rem; margin-top: 0.5rem;">
                💡 Take your time - there are no right or wrong answers
            </div>
            """, unsafe_allow_html=True)

            # Buttons in two columns
            if question_data.get('skip_allowed', False):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Continue", key=f"{question_id}_scale_continue", use_container_width=True):
                        st.session_state.assessment_v2_responses[question_id] = selected_value
                        st.rerun()

                # Split col2 into two half-width buttons for Previous and Skip
                col2a, col2b = st.columns(2)

                with col2a:
                    if st.button("Previous", key=f"{question_id}_scale_previous", help="Go to previous question", use_container_width=True):
                        self._handle_previous_question()

                with col2b:
                    if st.button("Skip", key=f"{question_id}_scale_skip", help="Skip to next question", use_container_width=True):
                        st.session_state.assessment_v2_responses[question_id] = "SKIPPED"
                        st.rerun()
            else:
                # Only continue button if skip not allowed
                if st.button("Continue", key=f"{question_id}_scale_continue"):
                    st.session_state.assessment_v2_responses[question_id] = selected_value
                    st.rerun()

        except Exception as e:
            st.error(f"Error rendering scale question: {str(e)}")
            # Fallback to skip
            if st.button("Skip due to error", key=f"{question_id}_scale_error"):
                st.session_state.assessment_v2_responses[question_id] = "ERROR_SKIPPED"
                st.rerun()

    def _render_skip_option(self, question_id: str, question_data: Dict):
        """Render skip option with appropriate warnings"""

        if not question_data.get('skip_allowed', True):
            return

        current_phase = st.session_state.assessment_v2_phase
        can_skip, message = SkipLogic.can_skip_question(
            question_id,
            current_phase,
            st.session_state.skip_counts
        )

        if can_skip:
            st.markdown('<div class="skip-option">', unsafe_allow_html=True)

            if message:
                st.markdown(f"*{message}*")

            col1, col2 = st.columns(2)
            # Split col2 into two half-width buttons for Previous and Skip
            col2a, col2b = st.columns(2)

            with col2a:
                if st.button("Previous", key=f"{question_id}_text_previous", help="Go to previous question", use_container_width=True):
                    self._handle_previous_question()

            with col2b:
                if st.button("Skip", key=f"{question_id}_skip", help="Skip to next question", use_container_width=True):
                    # Update skip count
                    if current_phase not in st.session_state.skip_counts:
                        st.session_state.skip_counts[current_phase] = 0
                    st.session_state.skip_counts[current_phase] += 1

                    # Mark as skipped and continue
                    st.session_state.assessment_v2_responses[question_id] = "SKIPPED"
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    def _enhance_question_with_patterns(self):
        """Enhance question rendering with subtle pattern-based elements"""

        # Only enhance if we have some responses to work with
        if len(st.session_state.assessment_v2_responses) < 2:
            return

        # Detect which patterns are emerging subtly
        patterns_detected = self._detect_preliminary_patterns()

        # Pattern detection is performed but no visual nudge is shown
        # This maintains the backend analysis without UI clutter

    def _detect_preliminary_patterns(self) -> List[str]:
        """Detect preliminary patterns without revealing analysis"""

        patterns = []
        responses = st.session_state.assessment_v2_responses

        # Check for digital-related responses (including neutral patterns)
        digital_indicators = ["8+ hours", "I've lost track", "Strongly agree", "Agree"]
        neutral_indicators = ["Neutral", "Somewhat ready", "Ready"]

        if any(indicator in str(responses.values()) for indicator in digital_indicators):
            patterns.append("digital_focus")

        # Even neutral responses indicate engagement and pattern formation
        if any(indicator in str(responses.values()) for indicator in neutral_indicators):
            patterns.append("balanced_assessment")

        return patterns

    def _complete_assessment(self):
        """Complete assessment and generate comprehensive profile"""

        if not CONFIG_AVAILABLE:
            st.error("Cannot generate profile - configuration not available")
            return

        # Generate comprehensive profile
        profile = ComprehensiveProfiler.generate_complete_profile(
            st.session_state.assessment_v2_responses
        )

        st.session_state.comprehensive_profile = profile
        st.session_state.assessment_v2_completed = True
        st.rerun()

    def _render_comprehensive_results(self):
        """Render sophisticated results presentation"""

        if not st.session_state.comprehensive_profile:
            st.error("Profile not available")
            return

        profile = st.session_state.comprehensive_profile

        # Main header
        st.markdown("**YOUR PERSONAL ASSESSMENT**")

        st.markdown("""
        <div class="assessment-container">
            <div style="text-align: center; margin-bottom: 3rem;">
                <div style="color: #556D7A; font-size: 1.1rem;">
                    A comprehensive analysis of your unique patterns and transformation pathway
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Render results sections
        self._render_pattern_constellation(profile)
        self._render_digital_analysis_section(profile)
        self._render_transformation_roadmap(profile)
        self._render_contact_form()

    def _render_pattern_constellation(self, profile: Dict):
        """Render pattern analysis in elegant format"""

        behavioral_patterns = profile.get('behavioral_patterns', {})
        primary_pattern = behavioral_patterns.get('primary_pattern', 'Unknown')

        # Enhanced pattern descriptions
        pattern_descriptions = {
            "balanced_assessment": "Balanced cognitive approach with multiple adaptive strategies",
            "digital_despair": "Digital environment conditioning with reality dissociation patterns",
            "unhappiness_culture": "Joy deflection mechanisms with success minimization",
            "systematic_mistrust": "Protective cynicism with vulnerability avoidance",
            "power_struggles": "Conflict engagement patterns with binary thinking",
            "inherited_missions": "Family loyalty patterns with achievement pressure",
            "context_dependent_weakness": "Situational confidence variations",
            "doing_vs_being": "Achievement-based worth validation patterns",
            "compartmentalized_authenticity": "Context-dependent identity management"
        }

        pattern_display = primary_pattern.replace('_', ' ').title()
        pattern_description = pattern_descriptions.get(primary_pattern,
            "This represents your mind's primary protective strategy, developed to keep you safe but now limiting your growth potential.")

        # Pattern Constellation header
        st.markdown("**YOUR PATTERN CONSTELLATION**")

        st.markdown(f"""
        <div class="assessment-container">
            <div class="question-card">
                <div class="pattern-detection">
                    <div style="font-weight: 500; color: #4CA1A3; margin-bottom: 0.5rem;">
                        **Primary: {pattern_display}**
                    </div>
                    <div style="color: #556D7A;">
                        {pattern_description}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    def _render_digital_analysis_section(self, profile: Dict):
        """Render digital despair analysis if relevant"""

        digital_analysis = profile.get('digital_analysis', {})
        severity = digital_analysis.get('severity_level', 'Minimal')

        if severity != 'Minimal':
            # Digital analysis header
            st.markdown("**DIGITAL CONDITIONING ANALYSIS**")

            st.markdown(f"""
            <div class="assessment-container">
                <div class="question-card">
                    <div style="color: #556D7A; line-height: 1.6;">
                        **Assessment: reveals specific patterns related to digital environment conditioning.**
                        Understanding these patterns is crucial for creating an effective transformation approach
                        that works with your unique neural wiring.
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    def _render_transformation_roadmap(self, profile: Dict):
        """Render transformation recommendations"""

        clinical_profile = profile.get('clinical_profile', {})
        estimated_sessions = clinical_profile.get('estimated_sessions', 'Unknown')

        # Transformation roadmap header
        st.markdown("**YOUR TRANSFORMATION ROADMAP**")

        st.markdown(f"""
        <div class="assessment-container">
            <div class="question-card">
                <div style="color: #556D7A; line-height: 1.6; margin-bottom: 1.5rem;">
                    **Based: on your unique pattern constellation, we've identified the most effective
                    approach for your transformation journey.**
                </div>
                <div class="insights-preview">
                    <div style="font-weight: 500; color: #4CA1A3; margin-bottom: 0.5rem;">
                        **Recommended: {estimated_sessions} session intensive**
                    </div>
                    <div style="color: #556D7A; font-size: 0.9rem;">
                        Your pattern combination responds optimally to rapid transformation techniques
                        that work directly with your subconscious programming.
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    def _render_contact_form(self):
        """Render sophisticated contact form"""

        st.success("🎉 Your comprehensive behavioral pattern analysis is ready!")

        st.markdown("**To: receive your complete analysis and discuss your personalized transformation approach, please provide your contact information below.**")

        with st.form("contact_form_v2"):
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name", placeholder="Your full name")
                email = st.text_input("Email Address", placeholder="your.email@example.com")

            with col2:
                phone = st.text_input("Phone Number (Optional)", placeholder="+1 (555) 123-4567")
                preferred_contact = st.selectbox(
                    "Preferred Contact Method",
                    ["Email", "Phone", "WhatsApp", "No preference"]
                )

            goals = st.text_area(
                "What would success look like for you?",
                placeholder="Describe your ideal outcome...",
                height=100
            )

            urgency = st.select_slider(
                "How urgent is change for you?",
                options=["Exploring options", "This year", "Next few months", "Very soon", "Urgent"]
            )

            # Submit button
            submitted = st.form_submit_button("Send My Complete Analysis")

            if submitted:
                if name and email:
                    self._process_contact_submission({
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "preferred_contact": preferred_contact,
                        "goals": goals,
                        "urgency": urgency
                    })
                else:
                    st.error("Please provide at least your name and email address.")

    def _process_contact_submission(self, contact_info: Dict):
        """Process contact form submission and send notifications"""

        # Store contact info in session
        st.session_state.contact_info_v2 = contact_info

        # Send email notification
        self._send_comprehensive_notification(contact_info)

        # Show success message
        st.success("""
        ✅ **Assessment Complete!**

        Your comprehensive analysis has been sent to our clinical team. You'll receive:

        1. **Complete Pattern Analysis** - Detailed breakdown of your unique psychological patterns
        2. **Personalized Transformation Plan** - Specific approach designed for your pattern combination
        3. **Session Scheduling** - Direct booking link for your initial consultation

        *Expect contact within 24 hours.*
        """)

    def _send_comprehensive_notification(self, contact_info: Dict):
        """Send enhanced email notification with comprehensive report"""

        if not EMAIL_AVAILABLE or not st.session_state.comprehensive_profile:
            return

        try:
            # Generate comprehensive report
            report = EnhancedEmailConfig.generate_therapist_report(
                st.session_state.comprehensive_profile,
                contact_info
            )

            # Email configuration (simplified for demo)
            # In production, this would use proper email configuration
            print("Email notification sent (simulated)")
            print(f"Report generated for: {contact_info['name']}")

        except Exception as e:
            st.error(f"Email notification failed: {str(e)}")

    def _estimate_total_questions(self) -> int:
        """Estimate total questions for progress calculation"""

        if not CONFIG_AVAILABLE:
            return 25  # Fallback estimate

        base_discovery = len(SmartQuestionMatrix.DISCOVERY_QUESTIONS)
        digital_questions = len(SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS)

        # Count behavioral pattern questions
        behavioral_count = 0
        for pattern_category, questions in SmartQuestionMatrix.BEHAVIORAL_PATTERN_QUESTIONS.items():
            behavioral_count += len(questions)

        validation_questions = len(SmartQuestionMatrix.PATTERN_VALIDATION_QUESTIONS)
        integration_questions = 4  # Updated to match the 4 integration questions we now have

        # Estimate based on assessment path if available
        if hasattr(self.question_flow, 'assessment_path'):
            if self.question_flow.assessment_path == "digital_focus":
                return base_discovery + digital_questions + validation_questions + integration_questions
            elif self.question_flow.assessment_path == "traditional_focus":
                return base_discovery + behavioral_count + validation_questions + integration_questions
            else:  # hybrid_focus
                return base_discovery + (digital_questions // 2) + (behavioral_count // 2) + validation_questions + integration_questions

        # Default estimate
        return base_discovery + digital_questions + behavioral_count + validation_questions + integration_questions

    def _get_accurate_total_questions(self) -> int:
        """Get more accurate total question count based on current assessment progress"""

        if not CONFIG_AVAILABLE:
            # If no config available, return current progress + estimated remaining
            current_count = len(st.session_state.assessment_v2_responses)
            return max(current_count + 1, 25)  # At least show current + 1

        # Get current progress
        current_responses = st.session_state.assessment_v2_responses
        current_count = len(current_responses)
        current_phase = getattr(self.question_flow, 'current_phase', 'discovery')
        assessment_path = getattr(self.question_flow, 'assessment_path', 'digital_focus')

        # Define phase counts
        discovery_total = len(SmartQuestionMatrix.DISCOVERY_QUESTIONS)
        digital_total = len(SmartQuestionMatrix.DIGITAL_DESPAIR_QUESTIONS)

        # Count behavioral pattern questions
        behavioral_total = 0
        for pattern_category, questions in SmartQuestionMatrix.BEHAVIORAL_PATTERN_QUESTIONS.items():
            behavioral_total += len(questions)

        validation_total = len(SmartQuestionMatrix.PATTERN_VALIDATION_QUESTIONS)
        integration_total = 4  # 4 integration questions

        # Calculate expected total based on current phase and assessment path
        if current_phase == 'discovery':
            # Still in discovery phase - use full estimation
            if assessment_path == "digital_focus":
                return discovery_total + digital_total + validation_total + integration_total
            elif assessment_path == "traditional_focus":
                return discovery_total + behavioral_total + validation_total + integration_total
            else:  # hybrid_focus
                return discovery_total + (digital_total // 2) + (behavioral_total // 2) + validation_total + integration_total

        elif current_phase == 'digital_despair':
            # In digital phase - calculate remaining accurately
            if assessment_path == "digital_focus":
                # Full digital path
                return discovery_total + digital_total + validation_total + integration_total
            else:  # hybrid_focus
                # Partial digital path
                return discovery_total + (digital_total // 2) + (behavioral_total // 2) + validation_total + integration_total

        elif current_phase == 'behavioral_patterns':
            # In behavioral phase
            if assessment_path == "traditional_focus":
                # Full behavioral path
                return discovery_total + behavioral_total + validation_total + integration_total
            else:  # hybrid_focus
                # Partial behavioral path
                return discovery_total + (digital_total // 2) + (behavioral_total // 2) + validation_total + integration_total

        elif current_phase == 'pattern_validation':
            # In validation phase - almost done
            return current_count + validation_total + integration_total

        elif current_phase == 'integration':
            # In final phase
            return current_count + integration_total

        else:
            # Unknown phase - conservative estimate
            return max(current_count + 1, self._estimate_total_questions())

    def _calculate_smart_time_estimate(self, questions_remaining: int, current_progress: int) -> float:
        """Calculate smart time estimate based on question types and user patterns"""

        if questions_remaining <= 0:
            return 0

        # Base times per question type (in seconds)
        base_times = {
            'discovery': 25,        # Discovery questions tend to be longer
            'digital_despair': 20,  # Standard rating questions
            'behavioral_patterns': 22,  # Slightly longer due to complexity
            'pattern_validation': 18,   # Shorter validation questions
            'integration': 30          # Final integration questions are longest
        }

        # Determine current phase
        current_phase = getattr(self.question_flow, 'current_phase', 'discovery')

        # Calculate time based on phase and remaining questions
        if current_phase == 'discovery':
            # Early phase - mix of discovery and upcoming phase questions
            base_time = base_times['discovery']
        elif current_phase == 'digital_despair':
            base_time = base_times['digital_despair']
        elif current_phase == 'behavioral_patterns':
            base_time = base_times['behavioral_patterns']
        elif current_phase == 'pattern_validation':
            base_time = base_times['pattern_validation']
        elif current_phase == 'integration':
            base_time = base_times['integration']
        else:
            base_time = 22  # Default average

        # Adjust based on user speed patterns
        if current_progress > 5:
            # Calculate average time based on progress (simplified simulation)
            if current_progress > 10:
                # User is experienced with the flow, slightly faster
                speed_multiplier = 0.9
            elif current_progress > 15:
                # User is very experienced, faster
                speed_multiplier = 0.8
            else:
                # Normal speed
                speed_multiplier = 1.0
        else:
            # Early questions, users typically slower
            speed_multiplier = 1.1

        # Calculate total time
        estimated_time = questions_remaining * base_time * speed_multiplier

        # Add small buffer for final questions (integration phase)
        if current_phase == 'integration':
            estimated_time *= 1.2

        return estimated_time

    def _handle_previous_question(self):
        """Navigate to the previous question"""
        if len(st.session_state.question_history) > 1:
            # Remove current question from history
            st.session_state.question_history.pop()
            # Get previous question
            previous_question_id = st.session_state.question_history[-1]

            # Remove the response for current question if it exists
            current_question_id = st.session_state.get('current_question_id')
            if current_question_id and current_question_id in st.session_state.assessment_v2_responses:
                del st.session_state.assessment_v2_responses[current_question_id]

            # Set current question to previous
            st.session_state.current_question_id = previous_question_id
            st.rerun()
        else:
            st.warning("This is the first question. Cannot go back further.")

# ================================
# ASSESSMENT PAGE FACTORY
# ================================

class EnhancedAssessmentPage:
    """Enhanced assessment page wrapper"""

    def __init__(self):
        self.orchestrator = EnhancedAssessmentOrchestrator()

    def render(self):
        """Render the enhanced assessment page"""
        self.orchestrator.render()

def create_assess_page():
    """Factory function for enhanced assessment page"""
    return EnhancedAssessmentPage()

# Export for module usage
if __name__ == "__main__":
    page = create_assess_page()
    page.render()
