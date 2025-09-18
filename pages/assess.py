import streamlit as st
from datetime import datetime
import re
import json
from utils.config import (
    PatternDefinitions, 
    QuestionSets, 
    PATTERN_SCORING_RULES, 
    DIGITAL_SCORING_RULES,
    AnalyticsMethods
)

class ProductionAssessment:
    def __init__(self):
        # Config integration
        self.patterns = PatternDefinitions.PATTERNS
        self.pattern_details = PatternDefinitions.PATTERN_DESCRIPTIONS
        self.questions = {
            **QuestionSets.AGE_SCREENING,
            **QuestionSets.DIGITAL_SCREENING,
            **QuestionSets.ENGAGEMENT,
            **QuestionSets.TRIGGER_MAPPING,
            **QuestionSets.PATTERN_SPECIFIC,
            **QuestionSets.INTEGRATION
        }
        
        # State initialization with all tracking variables
        self._init_production_state()

    def _init_production_state(self):
        """Enhanced State Management"""
        defaults = {
            # Core assessment flow
            'assessment_responses': {},
            'current_question': 1,
            'current_phase': 'age_screening',
            'question_history': [],
            
            # Pattern detection system
            'pattern_scores': {},
            'pattern_intensities': {},
            'pattern_interactions': {},
            'triggered_patterns': set(),
            'pattern_development_timeline': {},
            
            # Digital native analysis
            'is_digital_native': False,
            'digital_component_scores': {},
            'digital_severity': 'MINIMAL',
            'digital_adaptations_needed': [],
            
            # # Behavioral sequence mapping
            # 'trigger_chain': {},
            # 'behavioral_sequence_completeness': 0,
            # 'intervention_windows': [],
            
            # # Clinical insights extraction
            # 'core_limiting_beliefs': {},
            # 'secondary_gains': {},
            # 'systemic_resistance_factors': {},
            # 'identity_conflicts': {},
            # 'hidden_loyalties': {},
            
            # # Success prediction system
            # 'readiness_score': 0,
            # 'engagement_metrics': {},
            # 'success_probability': 85,
            # 'risk_mitigation_strategies': [],
            
            # # Session planning
            # 'session_complexity_score': 0,
            # 'recommended_approach': 'standard',
            # 'session_structure': {},
            # 'timeline_predictions': {},
            
            # Results and completion
            'assessment_completed': False,
            'contact_provided': False,
            # 'comprehensive_analysis': {},
            
            # Analytics tracking
            'start_time': datetime.now().isoformat(),
            'completion_timestamps': {},
            'user_journey_tracking': []
        }

    #Question Flow Logic
    def _get_next_question_enhanced(self):
        """Enhanced question flow with adaptive branching"""
        answered = set(st.session_state.assessment_responses.keys())
        current_phase = st.session_state.current_phase
        
        # Phase progression with intelligent branching
        if current_phase == 'age_screening':
            return self._handle_age_screening(answered)
        elif current_phase == 'digital_screening':
            return self._handle_digital_screening(answered)
        elif current_phase == 'engagement':
            return self._handle_engagement_phase(answered)
        elif current_phase == 'trigger_mapping':
            return self._handle_trigger_mapping(answered)
        elif current_phase == 'pattern_specific':
            return self._handle_adaptive_pattern_questions(answered)
        elif current_phase == 'integration':
            return self._handle_integration_phase(answered)
        
        return None, None

   
    def _handle_adaptive_pattern_questions(self, answered):
        """Smart pattern-specific question selection"""
        triggered_patterns = list(st.session_state.triggered_patterns)
        
        # Prioritize highest-scoring patterns
        pattern_priority = sorted(
            triggered_patterns, 
            key=lambda p: st.session_state.pattern_scores.get(p, 0), 
            reverse=True
        )[:3]  # Focus on top 3 patterns
        
        # Dynamic question selection based on pattern scores
        for pattern_id in pattern_priority:
            pattern_questions = QuestionSets.PATTERN_SPECIFIC.get(f"pattern_{pattern_id}", {})
            for q_id, question in pattern_questions.items():
                if q_id not in answered:
                    return q_id, question
        
        # Move to integration if all pattern questions answered
        st.session_state.current_phase = 'integration'
        return self._handle_integration_phase(answered)

    #Advanced Scoring Engine 
    def _update_comprehensive_scores(self, q_id, response, question):
        """Production scoring system using config rules"""
        
        # Pattern scoring using config rules
        self._apply_pattern_scoring(q_id, response, question)
        
        # Digital scoring for digital natives
        if st.session_state.is_digital_native:
            self._apply_digital_scoring(q_id, response, question)
        
        # Behavioral sequence mapping
        self._map_behavioral_sequence(q_id, response, question)
        
        # Real-time pattern interaction analysis
        self._analyze_pattern_interactions()
        
        # Adaptive triggering for follow-up questions
        self._check_adaptive_triggers(q_id, response, question)
    
    def _apply_pattern_scoring(self, q_id, response, question):
        """Apply pattern scoring using config rules"""
        scoring_rules = PATTERN_SCORING_RULES
        
        # Handle different scoring mechanisms
        if q_id in scoring_rules.get('pattern_triggers', {}):
            self._process_pattern_triggers(q_id, response)
        
        if q_id in scoring_rules.get('pattern_mapping', {}):
            self._process_pattern_mapping(q_id, response)
        
        if q_id in scoring_rules.get('pattern_keywords', {}):
            self._process_keyword_analysis(q_id, response)
        
        if question.get('weights') and question.get('pattern'):
            self._process_weighted_scoring(q_id, response, question)

    #Responsive Styling System
    def apply_production_mobile_styles():
        """Production-grade mobile-first styling"""
        st.markdown("""
        <style>
        /* Mobile-first base styles */
        .main .block-container {
            padding: 0.75rem !important;
            max-width: 100% !important;
            font-size: 16px; /* Prevent mobile zoom */
        }
        
        /* Progressive enhancement for tablets and desktop */
        @media (min-width: 768px) {
            .main .block-container {
                max-width: 650px !important;
                margin: 0 auto;
                padding: 1.5rem !important;
            }
        }
        
        /* Touch-optimized buttons */
        .stButton > button {
            min-height: 48px !important; /* WCAG touch target */
            width: 100% !important;
            margin-bottom: 0.75rem !important;
            padding: 1rem !important;
            text-align: left !important;
            font-size: 0.95rem !important;
            line-height: 1.4 !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
            
            /* Visual hierarchy */
            background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%) !important;
            border: 1px solid #E2E8F0 !important;
            color: #374151 !important;
        }
        
        /* Interactive states */
        .stButton > button:hover, .stButton > button:focus {
            background: linear-gradient(135deg, #E1F0F0 0%, #D1E7DD 100%) !important;
            border-color: #4CA1A3 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(76, 161, 163, 0.15) !important;
        }
        
        /* Progress system */
        .progress-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            background: #F8FAFC;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            border-left: 4px solid #4CA1A3;
        }
        
        .progress-bar {
            flex: 1;
            height: 8px;
            background: #E2E8F0;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4CA1A3 0%, #22c55e 100%);
            transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Enhanced form elements */
        .stTextArea textarea, .stTextInput input {
            min-height: 48px !important;
            font-size: 16px !important; /* Prevent mobile zoom */
            border-radius: 8px !important;
            border: 2px solid #E2E8F0 !important;
            padding: 0.75rem !important;
            transition: border-color 0.2s ease !important;
        }
        
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #4CA1A3 !important;
            box-shadow: 0 0 0 3px rgba(76, 161, 163, 0.1) !important;
            outline: none !important;
        }
        
        /* Accessibility improvements */
        .stRadio label, .stCheckbox label {
            font-size: 0.95rem !important;
            line-height: 1.4 !important;
            cursor: pointer !important;
        }
        
        /* High contrast mode support */
        @media (prefers-contrast: high) {
            .stButton > button {
                border: 2px solid #000 !important;
                color: #000 !important;
            }
        }
        
        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)

#Question Rendering System
class QuestionRenderer:
    """Production question rendering with accessibility"""
    
    def render_question_with_progress(self, q_id, question):
        """Render question with enhanced progress tracking"""
        self._render_progress_system()
        self._render_phase_indicator(question)
        self._render_question_content(q_id, question)
        self._render_pattern_hints_if_appropriate(q_id)
        self._render_navigation_system(q_id)
    
    def _render_progress_system(self):
        """Enhanced progress visualization"""
        total_questions = 35  # Fixed for consistency
        answered = len(st.session_state.assessment_responses)
        progress = answered / total_questions
        
        # Time estimation with learning algorithm
        time_remaining = self._calculate_smart_time_estimate(answered)
        
        st.markdown(f"""
        <div class="progress-container">
            <div>
                <strong>Question {answered + 1} of {total_questions}</strong>
                <br>
                <span style="color: #6B7280; font-size: 0.85rem;">
                    About {time_remaining:.0f} minutes remaining
                </span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <div style="text-align: center;">
                <strong>{int(progress * 100)}%</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _handle_single_choice_enhanced(self, q_id, question):
        """Enhanced single choice with keyboard navigation"""
        options = question['options']
        
        # Keyboard shortcuts for power users
        if len(options) <= 9:
            st.caption("💡 Tip: Use number keys 1-9 for quick selection")
        
        for i, option in enumerate(options):
            col1, col2 = st.columns([1, 10])
            with col1:
                st.markdown(f"**{i+1}**")
            with col2:
                if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                    self._save_response_with_analytics(q_id, option, question)
                    self._advance_with_transition(q_id)
                    st.rerun()
    
    def _handle_intensity_rating_enhanced(self, q_id, question, selected_option):
        """Enhanced intensity rating with visual feedback"""
        st.success(f"✅ Selected: {selected_option}")
        
        st.markdown("**How intense is this experience for you?**")
        
        # Visual intensity scale
        intensity_labels = [
            "1 - Very mild", "2 - Mild", "3 - Noticeable", 
            "4 - Moderate", "5 - Significant", 
            "6 - Strong", "7 - Very intense"
        ]
        
        # Use radio buttons for mobile accessibility
        intensity_choice = st.radio(
            "Select intensity level:",
            intensity_labels,
            key=f"q_{q_id}_intensity_radio",
            index=3,  # Default to moderate
            help="Consider how much this impacts your daily life"
        )
        
        intensity = int(intensity_choice.split(' - ')[0])
        
        # Visual feedback
        self._render_intensity_visualization(intensity)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Change selection", key=f"q_{q_id}_change"):
                self._clear_selection(q_id)
                st.rerun()
        with col2:
            if st.button("Continue →", key=f"q_{q_id}_continue", type="primary"):
                self._save_response_with_analytics(q_id, selected_option, question, intensity)
                self._advance_with_transition(q_id)
                st.rerun()

    #Advance input system
    def _handle_text_completion_enhanced(self, q_id, question):
        """Production text input with smart validation"""
        min_chars = question.get('min_chars', 5)
        placeholder = question.get('placeholder', 'Share your thoughts...')
        
        # Smart placeholder based on question context
        enhanced_placeholder = self._generate_smart_placeholder(question)
        
        response = st.text_area(
            "Your response:",
            placeholder=enhanced_placeholder,
            key=f"q_{q_id}_text",
            height=120,
            help="Take your time - detailed responses lead to better insights"
        )
        
        # Real-time character count with encouraging feedback
        char_count = len(response.strip())
        self._render_character_feedback(char_count, min_chars)
        
        # Smart suggestions based on question type
        if char_count < min_chars and char_count > 0:
            self._render_smart_suggestions(question, response)
        
        # Continue button with validation
        if char_count >= min_chars:
            if st.button("Continue →", key=f"q_{q_id}_continue", type="primary"):
                # Extract insights before saving
                insights = self._extract_text_insights(response, question)
                self._save_response_with_analytics(q_id, response.strip(), question, insights=insights)
                self._advance_with_transition(q_id)
                st.rerun()
        else:
            remaining = min_chars - char_count
            st.button(
                f"Continue → ({remaining} more characters needed)", 
                disabled=True, 
                key=f"q_{q_id}_disabled"
            )
    
    def _extract_text_insights(self, response, question):
        """Extract insights from text responses using config patterns"""
        insights = {}
        response_lower = response.lower()
        
        # Pattern keyword detection from config
        if question.get('pattern_keywords'):
            detected_patterns = []
            for keyword, patterns in question['pattern_keywords'].items():
                if keyword in response_lower:
                    detected_patterns.extend(patterns)
            insights['detected_patterns'] = detected_patterns
        
        # Emotional tone analysis
        emotion_words = {
            'anxiety': ['anxious', 'worried', 'scared', 'nervous', 'panic'],
            'depression': ['sad', 'hopeless', 'empty', 'worthless', 'defeated'],
            'anger': ['angry', 'frustrated', 'irritated', 'furious', 'rage'],
            'hope': ['hope', 'optimistic', 'positive', 'better', 'improve']
        }
        
        detected_emotions = []
        for emotion, words in emotion_words.items():
            if any(word in response_lower for word in words):
                detected_emotions.append(emotion)
        
        insights['emotional_tone'] = detected_emotions
        insights['response_depth'] = 'detailed' if len(response) > 100 else 'brief'
        insights['authenticity_markers'] = self._detect_authenticity_markers(response)
        
        return insights

    #Navigation and Flow Control
    def _render_navigation_system(self, current_q_id):
        """Production navigation with smart controls"""
        answered_count = len(st.session_state.assessment_responses)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            # Smart back button
            if answered_count > 0:
                if st.button("← Back", key="nav_back"):
                    self._go_back_with_validation()
                    st.rerun()
            else:
                st.button("← Back", disabled=True, help="First question")
        
        with col2:
            # Progress summary with phase info
            current_phase = st.session_state.current_phase
            phase_names = {
                'age_screening': 'Initial Setup',
                'digital_screening': 'Digital Assessment',
                'engagement': 'Pattern Discovery',
                'trigger_mapping': 'Trigger Analysis',
                'pattern_specific': 'Deep Exploration',
                'integration': 'Integration Planning'
            }
            
            phase_display = phase_names.get(current_phase, 'Assessment')
            
            st.markdown(f"""
            <div style="text-align: center; padding: 0.5rem;">
                <strong>{answered_count}/35 completed</strong><br>
                <span style="color: #6B7280; font-size: 0.8rem;">{phase_display}</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Smart skip with consequences
            if current_q_id > 0:  # Allow skipping after first question
                skip_help = "Skipping reduces analysis accuracy"
                if st.button("Skip", key="nav_skip", help=skip_help):
                    self._handle_skip_with_impact_warning(current_q_id)
            else:
                st.button("Skip", disabled=True, help="Required question")
    
    def _advance_with_transition(self, q_id):
        """Advance with smooth transition and analytics"""
        # Record progression analytics
        st.session_state.completion_timestamps[q_id] = datetime.now().isoformat()
        
        # Update user journey tracking
        st.session_state.user_journey_tracking.append({
            'question_id': q_id,
            'phase': st.session_state.current_phase,
            'timestamp': datetime.now().isoformat(),
            'action': 'completed'
        })
        
        st.session_state.current_question += 1
        
        # Smooth progress indication
        st.success("✅ Response saved")
        time.sleep(0.3)  # Brief feedback moment

#Comprehensive Pattern Detection 
class AdvancedPatternAnalyzer:
    """Production pattern analysis using config definitions"""
    
    def __init__(self):
        self.pattern_details = PatternDefinitions.PATTERN_DESCRIPTIONS
        self.scoring_rules = PATTERN_SCORING_RULES
        
    def analyze_complete_pattern_constellation(self, assessment_data):
        """Comprehensive pattern analysis with interactions"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        
        if not pattern_scores:
            return self._generate_minimal_pattern_analysis()
        
        # Sort patterns by strength
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Analyze dominant pattern with full detail
        dominant_pattern = self._analyze_dominant_pattern(sorted_patterns[0], responses)
        
        # Analyze supporting patterns
        supporting_patterns = []
        for pattern_id, score in sorted_patterns[1:4]:  # Top 3 supporting
            supporting_patterns.append(
                self._analyze_supporting_pattern(pattern_id, score, responses)
            )
        
        # Analyze pattern interactions using config data
        pattern_interactions = self._analyze_pattern_interactions_comprehensive(sorted_patterns)
        
        # Calculate complexity score
        complexity_analysis = self._calculate_pattern_complexity(sorted_patterns, pattern_interactions)
        
        return {
            'dominant_pattern': dominant_pattern,
            'supporting_patterns': supporting_patterns,
            'pattern_interactions': pattern_interactions,
            'complexity_analysis': complexity_analysis,
            'total_patterns_detected': len(sorted_patterns),
            'clinical_significance': self._assess_clinical_significance(sorted_patterns),
            'intervention_priorities': self._rank_intervention_priorities(sorted_patterns),
            'pattern_development_timeline': self._analyze_pattern_development(responses)
        }
    
    def _analyze_dominant_pattern(self, pattern_data, responses):
        """Detailed analysis of dominant pattern using config"""
        pattern_id, score = pattern_data
        pattern_config = self.pattern_details.get(pattern_id, {})
        
        # Extract pattern-specific insights
        pattern_insights = {
            'id': pattern_id,
            'name': pattern_config.get('name', f'Pattern {pattern_id}'),
            'score': score,
            'intensity': self._classify_intensity(score),
            'root_structure': pattern_config.get('root_structure', 'Unknown'),
            'core_belief': pattern_config.get('core_belief', 'Requires exploration'),
            'systemic_factors': pattern_config.get('systemic_factors', []),
            'identity_conflict': pattern_config.get('identity_conflict', 'Unknown'),
            'hidden_loyalties': pattern_config.get('hidden_loyalties', []),
            'pattern_mechanism': pattern_config.get('pattern_mechanism', 'Unknown'),
            'what_you_notice': pattern_config.get('what_you_notice', 'Requires assessment'),
            'what_others_see': pattern_config.get('what_others_see', 'Requires assessment'),
            'hidden_cost': pattern_config.get('hidden_cost', 'Analysis needed'),
            'breakthrough_moment': pattern_config.get('breakthrough_moment', 'Discovery pending'),
            'transformation_strategy': pattern_config.get('intervention_strategy', 'To be determined')
        }
        
        # Extract evidence from responses
        pattern_insights['evidence_from_responses'] = self._extract_pattern_evidence(
            pattern_id, responses
        )
        
        # Calculate pattern strength indicators
        pattern_insights['strength_indicators'] = self._calculate_strength_indicators(
            pattern_id, score, responses
        )
        
        return pattern_insights
    
    def _analyze_pattern_interactions_comprehensive(self, sorted_patterns):
        """Analyze how patterns interact and reinforce each other"""
        interactions = []
        
        # Common pattern reinforcement cycles from research
        reinforcement_cycles = {
            (1, 5): {
                'description': 'Unhappiness culture drives achievement addiction - joy feels dangerous so productivity becomes the only acceptable state',
                'reinforcement_mechanism': 'Each pattern validates the other',
                'intervention_complexity': 'High - requires simultaneous approach',
                'breaking_point': 'Install joy permission while maintaining productivity satisfaction'
            },
            (2, 4): {
                'description': 'Power struggles combined with binary thinking create win-lose mentality in all interactions',
                'reinforcement_mechanism': 'Either/or thinking fuels conflict escalation',
                'intervention_complexity': 'Moderate - sequential intervention possible',
                'breaking_point': 'Both/and thinking installation breaks the cycle'
            },
            (3, 6): {
                'description': 'Systematic mistrust leads to compartmentalized authenticity - different masks for different people to stay safe',
                'reinforcement_mechanism': 'Trust fears create identity fragmentation',
                'intervention_complexity': 'High - authenticity feels like vulnerability',
                'breaking_point': 'Graduated authenticity practice with safety anchoring'
            },
            (7, 9): {
                'description': 'Self-sacrifice pattern weakens boundaries in relationship contexts - overgiving becomes context-dependent',
                'reinforcement_mechanism': 'Boundary collapse reinforces caretaking identity',
                'intervention_complexity': 'Moderate - boundary installation with permission work',
                'breaking_point': 'Self-care reframed as service to others'
            }
        }
        
        # Check for known interaction patterns
        for i, (pattern1_id, score1) in enumerate(sorted_patterns[:3]):
            for pattern2_id, score2 in sorted_patterns[i+1:4]:
                combination = tuple(sorted([pattern1_id, pattern2_id]))
                
                if combination in reinforcement_cycles:
                    cycle_data = reinforcement_cycles[combination]
                    interactions.append({
                        'patterns': [pattern1_id, pattern2_id],
                        'pattern_names': [
                            self.pattern_details[pattern1_id]['name'],
                            self.pattern_details[pattern2_id]['name']
                        ],
                        'combined_strength': (score1 + score2) / 2,
                        'interaction_type': 'Reinforcing Cycle',
                        **cycle_data
                    })
        
        # Analyze novel interaction patterns
        if len(sorted_patterns) >= 3 and not interactions:
            interactions.append(self._analyze_novel_pattern_interaction(sorted_patterns[:3]))
        
        return interactions

#Digital Despair Analysis System 
class DigitalDespairAnalyzer:
    """Production digital conditioning analysis"""
    
    def __init__(self):
        self.digital_rules = DIGITAL_SCORING_RULES
        self.thresholds = PatternDefinitions.DIGITAL_THRESHOLDS
    
    def analyze_comprehensive_digital_conditioning(self, responses, is_digital_native):
        """Complete digital despair syndrome analysis"""
        if not is_digital_native:
            return None
        
        # Calculate all component scores using config rules
        component_scores = {}
        for component, rules in self.digital_rules.items():
            component_scores[component] = self._calculate_component_score(component, rules, responses)
        
        # Calculate composite digital despair score
        total_score = sum(component_scores.values())
        max_possible = len(component_scores) * 5  # Each component max 5
        percentage = (total_score / max_possible) * 100
        
        # Determine severity using config thresholds
        severity = self._determine_severity(percentage)
        threshold_config = self.thresholds[severity]
        
        # Generate therapeutic adaptations
        adaptations = self._generate_digital_adaptations(severity, component_scores)
        
        # Session modifications for digital natives
        session_modifications = self._generate_session_modifications(severity, component_scores)
        
        # Success rate adjustments
        success_adjustments = self._calculate_digital_success_adjustments(severity, component_scores)
        
        return {
            'digital_despair_score': percentage,
            'severity_level': severity,
            'clinical_recommendation': threshold_config['description'],
            'therapeutic_benefits': threshold_config['benefits'],
            'component_breakdown': component_scores,
            'component_analysis': self._analyze_each_component(component_scores, responses),
            'therapeutic_adaptations': adaptations,
            'session_modifications': session_modifications,
            'success_rate_impact': success_adjustments,
            'specialized_interventions': self._recommend_specialized_interventions(severity, component_scores),
            'digital_native_advantages': self._identify_digital_advantages(component_scores)
        }
    
    def _calculate_component_score(self, component, rules, responses):
        """Calculate individual component scores using config rules"""
        if component == 'reality_dissociation':
            return self._calculate_reality_dissociation(responses)
        elif component == 'ironic_detachment':
            return self._calculate_ironic_detachment(responses)
        elif component == 'attention_fragmentation':
            return self._calculate_attention_fragmentation(responses)
        elif component == 'algorithmic_dependency':
            return self._calculate_algorithmic_dependency(responses)
        elif component == 'nihilistic_worldview':
            return self._calculate_nihilistic_worldview(responses)
        elif component == 'hope_avoidance':
            return self._calculate_hope_avoidance(responses)
        elif component == 'binary_success':
            return self._calculate_binary_success(responses)
        else:
            return 0
    
    def _analyze_each_component(self, component_scores, responses):
        """Detailed analysis of each digital component"""
        analysis = {}
        
        for component, score in component_scores.items():
            analysis[component] = {
                'score': score,
                'severity': 'High' if score >= 4 else 'Moderate' if score >= 2 else 'Low',
                'clinical_impact': self._assess_component_impact(component, score),
                'intervention_target': self._get_component_intervention(component, score),
                'success_indicators': PatternDefinitions.DIGITAL_SUCCESS_INDICATORS.get(component, []),
                'evidence_from_responses': self._extract_component_evidence(component, responses)
            }
        
        return analysis
    
    def _recommend_specialized_interventions(self, severity, component_scores):
        """Recommend specialized interventions for digital natives"""
        interventions = []
        
        if severity in ['SEVERE', 'MODERATE']:
            # High-priority interventions
            if component_scores.get('ironic_detachment', 0) >= 3:
                interventions.append({
                        'target': 'Ironic Detachment Dissolution',
                        'method': 'Intelligence validation while accessing authentic emotion beneath protective cynicism',
                        'timeline': 'Session 1 focus',
                        'success_marker': 'Client expresses genuine emotion without self-mockery'
                    })
                
            if component_scores.get('attention_fragmentation', 0) >= 3:
                    interventions.append({
                        'target': 'Attention Reconditioning',
                        'method': '15-20 minute focused segments with movement breaks, building to longer periods',
                        'timeline': 'Throughout all sessions',
                        'success_marker': 'Can maintain focus for 45+ minutes without digital stimulation'
                    })
                
            if component_scores.get('hope_avoidance', 0) >= 3:
                    interventions.append({
                        'target': 'Evidence-Based Hope Building',
                        'method': 'Gradual realistic optimism vs overwhelming positivity, systemic awareness maintained',
                        'timeline': 'Session 2 integration',
                        'success_marker': 'Can accept positive possibilities without automatic dismissal'
                    })
            
        return interventions
        
    def _generate_session_modifications(self, severity, component_scores):
        """Generate session structure modifications for digital natives"""
        modifications = {
                'session_length': '90 minutes',
                'break_structure': 'Standard',
                'language_approach': 'Professional',
                'authority_style': 'Traditional therapeutic',
                'resistance_expectations': 'Standard change resistance'
            }
            
        if severity == 'SEVERE':
                modifications.update({
                    'session_length': '90 minutes (3x30 minute segments)',
                    'break_structure': 'Mandatory 5-minute breaks between segments',
                    'language_approach': 'Collaborative, anti-directive, intelligence-validating',
                    'authority_style': 'Peer consultant model',
                    'resistance_expectations': 'High intellectual challenges, cynical testing, authority resistance'
                })
        elif severity == 'MODERATE':
                modifications.update({
                    'session_length': '90 minutes with optional mid-session break',
                    'break_structure': '10-minute movement break if needed',
                    'language_approach': 'Respectful collaboration with reduced directive language',
                    'authority_style': 'Gentle expert guidance',
                    'resistance_expectations': 'Moderate skepticism about traditional approaches'
                })
            
        return modifications

#Comprehensive Results Engine 
class ProductionResultsEngine:
    """Advanced results generation using config insights"""
    
    def __init__(self):
        self.patterns = PatternDefinitions.PATTERNS
        self.pattern_details = PatternDefinitions.PATTERN_DESCRIPTIONS
        self.analytics = AnalyticsMethods()
    
    def generate_comprehensive_results(self, assessment_data):
        """Generate complete results analysis"""
        
        # Core analysis components
        pattern_analysis = self._analyze_pattern_constellation_complete(assessment_data)
        digital_analysis = self._analyze_digital_conditioning_complete(assessment_data)
        behavioral_sequence = self._analyze_behavioral_sequence_complete(assessment_data)
        clinical_insights = self._extract_clinical_insights_complete(assessment_data)
        transformation_roadmap = self._generate_transformation_roadmap_complete(assessment_data)
        
        return {
            'assessment_summary': self._generate_assessment_summary(assessment_data),
            'pattern_analysis': pattern_analysis,
            'digital_analysis': digital_analysis,
            'behavioral_sequence_analysis': behavioral_sequence,
            'clinical_insights': clinical_insights,
            'transformation_roadmap': transformation_roadmap,
            'success_prediction': self._calculate_success_prediction_complete(assessment_data),
            'personalized_techniques': self._generate_personalized_techniques(assessment_data),
            'cost_benefit_analysis': self._calculate_comprehensive_costs(assessment_data),
            'empowerment_profile': self._generate_empowerment_profile(assessment_data)
        }
    
    def _generate_assessment_summary(self, assessment_data):
        """Generate executive summary of assessment"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        
        if not pattern_scores:
            return {
                'primary_finding': 'Assessment incomplete - detailed analysis pending',
                'complexity_level': 'Unknown',
                'intervention_approach': 'To be determined',
                'timeline_estimate': 'Pending complete assessment'
            }
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        dominant_pattern = self.pattern_details.get(sorted_patterns[0][0], {})
        
        return {
            'primary_finding': dominant_pattern.get('insights_map', 'Pattern analysis complete'),
            'complexity_level': self._assess_complexity_level(sorted_patterns),
            'intervention_approach': self._recommend_intervention_approach(assessment_data),
            'timeline_estimate': self._estimate_transformation_timeline(assessment_data),
            'success_probability': self._calculate_base_success_probability(assessment_data),
            'key_breakthrough_prediction': dominant_pattern.get('breakthrough_moment', 'Breakthrough insights pending')
        }
    
    def _generate_transformation_roadmap_complete(self, assessment_data):
        """Generate detailed transformation roadmap using config and analytics"""
        
        # Use analytics methods from config
        pattern_analysis = assessment_data.get('pattern_analysis', {})
        digital_analysis = assessment_data.get('digital_analysis', {})
        
        # Calculate session complexity
        complexity_score = self.analytics.calculate_session_complexity_score(
            len(assessment_data.get('pattern_scores', {})),
            digital_analysis.get('severity_level', 'MINIMAL') if digital_analysis else 'MINIMAL'
        )
        
        # Generate session structure
        session_structure = self.analytics.determine_session_structure(complexity_score)
        
        # Plan individual sessions
        session_1_plan = self.analytics.plan_session_1(pattern_analysis, digital_analysis)
        session_2_plan = self.analytics.plan_session_2(pattern_analysis, digital_analysis)
        session_3_plan = self.analytics.plan_session_3_if_needed(complexity_score, pattern_analysis)
        
        return {
            'session_structure': session_structure,
            'detailed_session_plans': {
                'session_1': {
                    'focus': session_1_plan,
                    'duration': '90 minutes',
                    'objectives': self._generate_session_1_objectives(assessment_data),
                    'techniques': self._select_session_1_techniques(assessment_data),
                    'success_markers': self._define_session_1_success_markers(assessment_data)
                },
                'session_2': {
                    'focus': session_2_plan,
                    'duration': '90 minutes', 
                    'objectives': self._generate_session_2_objectives(assessment_data),
                    'techniques': self._select_session_2_techniques(assessment_data),
                    'success_markers': self._define_session_2_success_markers(assessment_data)
                },
                'session_3': {
                    'probability': f"{self._calculate_session_3_probability(complexity_score)}%",
                    'focus': session_3_plan,
                    'conditions': 'If reinforcement needed for complex pattern integration'
                }
            },
            'timeline_predictions': {
                'total_duration': self.analytics.predict_total_duration(complexity_score),
                'initial_results': '24-48 hours post Session 1',
                'significant_shifts': '48-72 hours post Session 2',
                'full_integration': self.analytics.predict_total_duration(complexity_score)
            },
            'between_session_work': self.analytics.determine_integration_work(pattern_analysis),
            'follow_up_schedule': self.analytics.determine_follow_up_schedule(complexity_score),
            'success_optimization': {
                'probability': self.analytics.calculate_session_success_probability(pattern_analysis, digital_analysis),
                'optimization_factors': self.analytics.identify_optimization_factors(assessment_data),
                'risk_mitigation': self.analytics.generate_risk_mitigation_strategies(assessment_data)
            }
        }

    def render_results_hero_mobile_optimized(self):
        """Mobile-optimized results hero section"""
        
        # Generate comprehensive results
        assessment_data = self._compile_complete_assessment_data()
        results = self.results_engine.generate_comprehensive_results(assessment_data)
        
        # Hero banner with key insights
        summary = results['assessment_summary']
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%); 
            padding: 1.5rem; 
            border-radius: 12px; 
            border-left: 4px solid #4CA1A3; 
            margin: 1rem 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        ">
            <div style="color: #273548; font-size: 1rem; line-height: 1.6;">
                <div style="color: #4CA1A3; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem;">
                    🎯 Your Transformation Blueprint Ready
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <strong>Key Insight:</strong><br>
                    {summary['primary_finding']}
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                    <div>
                        <strong>Complexity:</strong><br>
                        <span style="color: #4CA1A3;">{summary['complexity_level']}</span>
                    </div>
                    <div>
                        <strong>Success Rate:</strong><br>
                        <span style="color: #4CA1A3;">{summary['success_probability']}%</span>
                    </div>
                </div>
                
                <div style="margin-top: 1rem; padding: 0.75rem; background: #E1F0F0; border-radius: 6px;">
                    <strong>Timeline:</strong> {summary['timeline_estimate']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Success probability visualization
        self._render_success_probability_mobile(summary['success_probability'])
        
        # Pattern insights preview
        self._render_pattern_insights_mobile(results['pattern_analysis'])
        
        # Digital insights if applicable
        if results.get('digital_analysis'):
            self._render_digital_insights_mobile(results['digital_analysis'])
        
        # Transformation roadmap preview
        self._render_roadmap_preview_mobile(results['transformation_roadmap'])
        
        # Immediate techniques
        self._render_immediate_techniques_mobile(results['personalized_techniques'])
    
    def _render_success_probability_mobile(self, success_rate):
        """Mobile-optimized success probability display"""
        st.markdown("**Transformation Success Likelihood:**")
        
        # Progress bar with animation
        col1, col2 = st.columns([4, 1])
        with col1:
            progress_bar = st.progress(success_rate / 100)
        with col2:
            st.markdown(f"**{success_rate}%**")
        
        # Success factors
        if success_rate >= 90:
            st.success("🔥 Exceptional success indicators - optimal conditions for rapid transformation")
        elif success_rate >= 85:
            st.success("⭐ Strong success indicators - excellent prognosis for transformation")
        elif success_rate >= 80:
            st.info("✅ Good success indicators - standard excellent outcomes expected")
        else:
            st.warning("⚠️ Moderate success indicators - specialized approach may be needed")
    
    def _render_pattern_insights_mobile(self, pattern_analysis):
        """Mobile-optimized pattern insights"""
        if not pattern_analysis or not pattern_analysis.get('dominant_pattern'):
            st.info("🔍 Complete assessment needed for detailed pattern analysis")
            return
        
        dominant = pattern_analysis['dominant_pattern']
        
        st.markdown("**🎯 Your Primary Pattern:**")
        
        # Expandable pattern card
        with st.expander(f"**{dominant['name']}** - {dominant['intensity']} Intensity", expanded=True):
            
            # What you notice
            st.markdown(f"**What you might notice:**\n{dominant.get('what_you_notice', 'Pattern exploration needed')}")
            
            # Hidden cost preview
            st.markdown(f"**Hidden cost:**\n{dominant.get('hidden_cost', 'Analysis pending')}")
            
            # Breakthrough moment
            st.info(f"**Your breakthrough moment:**\n{dominant.get('breakthrough_moment', 'Discovery awaiting')}")
            
            # Evidence from responses
            if dominant.get('evidence_from_responses'):
                st.markdown("**Evidence from your responses:**")
                for evidence in dominant['evidence_from_responses'][:2]:
                    st.markdown(f"• {evidence}")
        
        # Supporting patterns summary
        supporting = pattern_analysis.get('supporting_patterns', [])
        if supporting:
            st.markdown(f"**Plus {len(supporting)} supporting pattern{'s' if len(supporting) > 1 else ''} identified**")
            pattern_names = [p['name'] for p in supporting[:3]]
            st.caption(f"Including: {', '.join(pattern_names)}")

    #Personalized Techniques Generator
    def _render_immediate_techniques_mobile(self, techniques):
        """Mobile-optimized immediate techniques section"""
        if not techniques:
            return
        
        st.markdown("**⚡ Techniques You Can Use Today:**")
        
        # Get top 3 most relevant techniques
        top_techniques = techniques.get('immediate_techniques', [])[:3]
        
        for i, technique in enumerate(top_techniques, 1):
            with st.expander(f"**Technique {i}: {technique['name']}**", expanded=i==1):
                
                # Technique description
                st.markdown(f"**How to use it:**\n{technique['description']}")
                
                # When to use
                if technique.get('timing'):
                    st.markdown(f"**When to use:**\n{technique['timing']}")
                
                # Expected result
                if technique.get('expected_result'):
                    st.success(f"**Expected result:** {technique['expected_result']}")
                
                # Practice reminder
                st.info("💡 **Practice tip:** Try this technique 3 times today in low-stakes situations to build familiarity")
    
    def _generate_personalized_techniques(self, assessment_data):
        """Generate personalized techniques based on assessment"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        trigger_chain = assessment_data.get('trigger_chain', {})
        
        if not pattern_scores:
            return {'immediate_techniques': self._get_default_techniques()}
        
        # Get dominant pattern
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        dominant_pattern_id = sorted_patterns[0][0]
        
        # Pattern-specific techniques from config
        pattern_config = self.pattern_details.get(dominant_pattern_id, {})
        
        # Generate techniques based on pattern and triggers
        techniques = []
        
        # Pattern-specific technique 1
        techniques.append(self._generate_pattern_technique_1(dominant_pattern_id, pattern_config, trigger_chain))
        
        # Pattern-specific technique 2
        techniques.append(self._generate_pattern_technique_2(dominant_pattern_id, pattern_config, trigger_chain))
        
        # Universal grounding technique
        techniques.append(self._generate_grounding_technique(trigger_chain))
        
        # Digital-specific technique if applicable
        if assessment_data.get('is_digital_native'):
            digital_analysis = assessment_data.get('digital_analysis')
            if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
                techniques.append(self._generate_digital_technique(digital_analysis))
        
        return {
            'immediate_techniques': techniques,
            'practice_schedule': self._generate_practice_schedule(techniques),
            'progress_tracking': self._generate_progress_tracking_system(techniques)
        }
    
    def _generate_pattern_technique_1(self, pattern_id, pattern_config, trigger_chain):
        """Generate first pattern-specific technique"""
        
        technique_map = {
            1: {  # Unhappiness Culture
                'name': 'Happiness Permission Check',
                'description': 'Before dismissing good feelings, pause and ask: "What would I lose by enjoying this for 5 more minutes?" Usually, the answer reveals the pattern isn\'t protecting anything real.',
                'timing': 'When you notice yourself deflecting compliments, minimizing achievements, or waiting for bad news',
                'expected_result': 'Permission to experience positive emotions without fear'
            },
            2: {  # Power Struggles
                'name': 'Combat Mode Recognition',
                'description': 'Notice when your body activates (tension, faster heartbeat) during disagreements. Pause and ask: "Is this actually a battle or an opportunity to understand?"',
                'timing': 'When you feel defensive or the urge to prove you\'re right',
                'expected_result': 'Shift from combat to collaboration mindset'
            },
            3: {  # Systematic Mistrust
                'name': 'Trust Calibration Check',
                'description': 'When suspicion arises, ask: "What evidence do I actually have?" vs "What story is my protective mind creating?"',
                'timing': 'When meeting new people or receiving unexpected kindness',
                'expected_result': 'More accurate assessment of actual vs imagined threats'
            }
            # Add remaining patterns...
        }
        
        return technique_map.get(pattern_id, {
            'name': 'Pattern Interrupt Pause',
            'description': 'When you notice your pattern activating, pause for 10 seconds and ask: "Is this response serving me right now?"',
            'timing': 'Any time you recognize your pattern starting',
            'expected_result': 'Increased awareness and conscious choice'
        })

#Clinical Template Generator
class ClinicalIntegrationSystem:
    """Production clinical integration using config data"""
    
    def generate_comprehensive_clinical_template(self, assessment_data):
        """Generate complete clinical template for practitioners"""
        
        results = self.results_engine.generate_comprehensive_results(assessment_data)
        
        # Header section
        template = self._generate_clinical_header(assessment_data, results)
        
        # Pattern constellation analysis
        template += self._generate_pattern_constellation_section(results['pattern_analysis'])
        
        # Digital conditioning analysis (if applicable)
        if results.get('digital_analysis'):
            template += self._generate_digital_conditioning_section(results['digital_analysis'])
        
        # Behavioral sequence mapping
        template += self._generate_behavioral_sequence_section(results['behavioral_sequence_analysis'])
        
        # Clinical insights section
        template += self._generate_clinical_insights_section(results['clinical_insights'])
        
        # Session design section
        template += self._generate_session_design_section(results['transformation_roadmap'])
        
        # Success prediction section
        template += self._generate_success_prediction_section(results['success_prediction'])
        
        # Risk assessment and mitigation
        template += self._generate_risk_assessment_section(results)
        
        # Footer with recommendations
        template += self._generate_clinical_footer(results)
        
        return template
    
    def _generate_clinical_header(self, assessment_data, results):
        """Generate clinical template header"""
        summary = results['assessment_summary']
        contact_info = assessment_data.get('contact_info', {})
        
        return f"""
╔═══════════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                    ║
║              Production Behavioral Pattern Assessment             ║
╚═══════════════════════════════════════════════════════════════════╝

**CLIENT INFORMATION:**
Assessment Date: {datetime.now().strftime('%B %d, %Y')}
Completion Rate: {assessment_data.get('completion_rate', 0)*100:.0f}%
Digital Native Status: {'Yes' if assessment_data.get('is_digital_native') else 'No'}
Urgency Level: {contact_info.get('urgency', 'Not specified')}

**EXECUTIVE SUMMARY:**
Primary Finding: {summary['primary_finding']}
Complexity Level: {summary['complexity_level']}
Success Probability: {summary['success_probability']}%
Recommended Timeline: {summary['timeline_estimate']}

"""
    
    def _generate_pattern_constellation_section(self, pattern_analysis):
        """Generate detailed pattern analysis section"""
        if not pattern_analysis or not pattern_analysis.get('dominant_pattern'):
            return """
**PATTERN ANALYSIS:**
Assessment incomplete - detailed pattern analysis pending session completion.
Recommend completing full assessment for comprehensive clinical insights.

"""
        
        dominant = pattern_analysis['dominant_pattern']
        supporting = pattern_analysis.get('supporting_patterns', [])
        interactions = pattern_analysis.get('pattern_interactions', [])
        
        section = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                     PATTERN CONSTELLATION ANALYSIS               ║
╚═══════════════════════════════════════════════════════════════════╝

**DOMINANT PATTERN ANALYSIS:**
Pattern: {dominant['name']} (Score: {dominant['score']:.1f}/10 - {dominant['intensity']})
Root Structure: {dominant.get('root_structure', 'Analysis pending')}
Core Limiting Belief: {dominant.get('core_belief', 'Requires exploration')}
Identity Conflict: {dominant.get('identity_conflict', 'To be determined')}

**SYSTEMIC FACTORS:**"""
        
        for factor in dominant.get('systemic_factors', []):
            section += f"\n• {factor}"
        
        section += f"""

**HIDDEN LOYALTIES & SECONDARY GAINS:**"""
        
        for loyalty in dominant.get('hidden_loyalties', []):
            section += f"\n• {loyalty}"
        
        if supporting:
            section += f"""

**SUPPORTING PATTERNS:**"""
            for pattern in supporting[:3]:
                section += f"""
{pattern['name']} (Score: {pattern['score']:.1f}/10 - {pattern['intensity']})
└─ Root Structure: {pattern.get('root_structure', 'Standard analysis')}"""
        
        if interactions:
            section += f"""

**PATTERN INTERACTIONS & REINFORCEMENT CYCLES:**"""
            for interaction in interactions:
                section += f"""
{' + '.join(interaction['pattern_names'])} Interaction:
└─ {interaction['description']}
└─ Intervention Complexity: {interaction.get('intervention_complexity', 'Standard')}
└─ Breaking Point: {interaction.get('breaking_point', 'To be determined in session')}"""
        
        return section + "\n\n"

#Data Analytics & Export System
class ProductionDataManager:
    """Advanced data management and analytics"""
    
    def __init__(self):
        self.analytics = AnalyticsMethods()
    
    def export_complete_assessment_data(self):
        """Export comprehensive assessment data"""
        if 'assessment_responses' not in st.session_state:
            return None
        
        # Compile all assessment data
        export_data = {
            'metadata': {
                'export_timestamp': datetime.now().isoformat(),
                'assessment_version': '3.0',
                'total_questions': len(st.session_state.assessment_responses),
                'completion_rate': len(st.session_state.assessment_responses) / 35,
                'session_duration': self._calculate_session_duration(),
                'user_agent': 'Streamlit Production'
            },
            
            'raw_responses': {
                'assessment_responses': dict(st.session_state.assessment_responses),
                'intensity_responses': dict(st.session_state.get('intensity_responses', {})),
                'trigger_chain': dict(st.session_state.get('trigger_chain', {})),
                'user_journey_tracking': st.session_state.get('user_journey_tracking', [])
            },
            
            'pattern_analysis': {
                'pattern_scores': dict(st.session_state.get('pattern_scores', {})),
                'pattern_intensities': dict(st.session_state.get('pattern_intensities', {})),
                'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
                'pattern_interactions': dict(st.session_state.get('pattern_interactions', {}))
            },
            
            'digital_analysis': {
                'is_digital_native': st.session_state.get('is_digital_native', False),
                'digital_component_scores': dict(st.session_state.get('digital_component_scores', {})),
                'digital_severity': st.session_state.get('digital_severity', 'MINIMAL'),
                'digital_adaptations_needed': st.session_state.get('digital_adaptations_needed', [])
            },
            
            'clinical_insights': {
                'core_limiting_beliefs': dict(st.session_state.get('core_limiting_beliefs', {})),
                'secondary_gains': dict(st.session_state.get('secondary_gains', {})),
                'systemic_resistance_factors': dict(st.session_state.get('systemic_resistance_factors', {})),
                'intervention_windows': st.session_state.get('intervention_windows', [])
            },
            
            'success_prediction': {
                'readiness_score': st.session_state.get('readiness_score', 0),
                'success_probability': st.session_state.get('success_probability', 85),
                'engagement_metrics': dict(st.session_state.get('engagement_metrics', {})),
                'risk_mitigation_strategies': st.session_state.get('risk_mitigation_strategies', [])
            },
            
            'session_planning': {
                'session_complexity_score': st.session_state.get('session_complexity_score', 0),
                'recommended_approach': st.session_state.get('recommended_approach', 'standard'),
                'session_structure': dict(st.session_state.get('session_structure', {})),
                'timeline_predictions': dict(st.session_state.get('timeline_predictions', {}))
            },
            
            'contact_information': st.session_state.get('contact_info', {}),
            
            'comprehensive_analysis': st.session_state.get('comprehensive_analysis', {})
        }
        
        return export_data
    
    def generate_analytics_insights(self, assessment_data):
        """Generate analytics insights for continuous improvement"""
        
        insights = {
            'completion_analysis': self._analyze_completion_patterns(assessment_data),
            'response_quality_analysis': self._analyze_response_quality(assessment_data),
            'pattern_detection_efficiency': self._analyze_pattern_detection(assessment_data),
            'user_experience_metrics': self._analyze_user_experience(assessment_data),
            'clinical_accuracy_indicators': self._analyze_clinical_accuracy(assessment_data)
        }
        
        return insights
    
    def _analyze_completion_patterns(self, assessment_data):
        """Analyze completion patterns for optimization"""
        responses = assessment_data.get('raw_responses', {}).get('assessment_responses', {})
        journey = assessment_data.get('raw_responses', {}).get('user_journey_tracking', [])
        
        completion_insights = {
            'total_questions_answered': len(responses),
            'completion_rate': len(responses) / 35,
            'average_response_time': self._calculate_avg_response_time(journey),
            'drop_off_points': self._identify_drop_off_points(journey),
            'phase_completion_rates': self._analyze_phase_completion(responses)
        }
        
        return completion_insights

#Email & Communication System
class CommunicationManager:
    """Production communication system"""
    
    def prepare_comprehensive_assessment_email(self, assessment_data):
        """Prepare comprehensive email with all results"""
        
        # Generate all components
        clinical_template = self.clinical_system.generate_comprehensive_clinical_template(assessment_data)
        results = self.results_engine.generate_comprehensive_results(assessment_data)
        
        email_data = {
            'recipient_info': assessment_data.get('contact_information', {}),
            'assessment_summary': results['assessment_summary'],
            'clinical_template': clinical_template,
            'pattern_insights': results['pattern_analysis'],
            'transformation_roadmap': results['transformation_roadmap'],
            'personalized_techniques': results['personalized_techniques'],
            'urgency_level': assessment_data.get('contact_information', {}).get('urgency', 'Standard'),
            'follow_up_recommendations': self._generate_follow_up_recommendations(results),
            'export_data': self.data_manager.export_complete_assessment_data()
        }
        
        return email_data
    
    def _generate_follow_up_recommendations(self, results):
        """Generate follow-up recommendations based on results"""
        recommendations = []
        
        success_probability = results['success_prediction'].get('overall_probability', 85)
        
        if success_probability >= 90:
            recommendations.append("Priority scheduling recommended - excellent transformation candidate")
        elif success_probability >= 85:
            recommendations.append("Standard scheduling within 48-72 hours")
        else:
            recommendations.append("Consider preliminary consultation to optimize success factors")
        
        # Urgency-based recommendations
        urgency = results.get('urgency_level', 'Standard')
        if 'extremely urgent' in urgency.lower():
            recommendations.append("URGENT: Contact within 24 hours - high distress indicators")
        elif 'very urgent' in urgency.lower():
            recommendations.append("High priority: Contact within 48 hours")
        
        # Digital native recommendations
        if results.get('digital_analysis'):
            severity = results['digital_analysis'].get('severity_level', 'MINIMAL')
            if severity in ['SEVERE', 'MODERATE']:
                recommendations.append("Digital-native specialized approach required - brief clinical team on adaptations")
        
        return recommendations

#Smart Question Branching
class SmartQuestionFlow:
    """Advanced question flow with ML-like adaptation"""
    
    def __init__(self):
        self.questions = QuestionSets()
        self.patterns = PatternDefinitions.PATTERNS
        
    def get_next_optimized_question(self):
        """Get next question with intelligent branching"""
        answered = set(st.session_state.assessment_responses.keys())
        current_phase = st.session_state.current_phase
        
        # Analyze current response patterns for smart branching
        pattern_emergence = self._analyze_emerging_patterns()
        engagement_level = self._assess_current_engagement()
        
        # Adaptive question selection based on emerging insights
        if current_phase == 'pattern_specific':
            return self._select_adaptive_pattern_question(pattern_emergence, answered)
        
        # Standard flow with optimizations
        return self._get_standard_next_question(answered, current_phase)
    
    def _analyze_emerging_patterns(self):
        """Analyze which patterns are emerging strongest"""
        pattern_scores = st.session_state.get('pattern_scores', {})
        
        if not pattern_scores:
            return []
        
        # Sort by strength and recency of detection
        sorted_patterns = sorted(
            pattern_scores.items(), 
            key=lambda x: (x[1], self._get_pattern_recency(x[0])), 
            reverse=True
        )
        
        # Focus on patterns above threshold
        strong_patterns = [p_id for p_id, score in sorted_patterns if score >= 3.0]
        
        return strong_patterns[:3]  # Top 3 emerging patterns
    
    def _select_adaptive_pattern_question(self, strong_patterns, answered):
        """Select most relevant pattern-specific question"""
        
        # Prioritize unexplored high-scoring patterns
        for pattern_id in strong_patterns:
            pattern_questions = QuestionSets.PATTERN_SPECIFIC.get(f"pattern_{pattern_id}", {})
            
            for q_id, question in pattern_questions.items():
                if q_id not in answered:
                    # Mark this as an adaptive selection for analytics
                    self._track_adaptive_selection(q_id, pattern_id)
                    return q_id, question
        
        # Fall back to standard progression
        return self._get_next_integration_question(answered)
    
    def _assess_current_engagement(self):
        """Assess user engagement for flow optimization"""
        responses = st.session_state.get('assessment_responses', {})
        
        if not responses:
            return 'initial'
        
        # Analyze response quality indicators
        recent_responses = list(responses.values())[-3:]  # Last 3 responses
        
        engagement_indicators = {
            'text_quality': self._assess_text_response_quality(recent_responses),
            'completion_speed': self._assess_completion_speed(),
            'intensity_ratings': self._assess_intensity_engagement(recent_responses),
            'skip_rate': self._calculate_recent_skip_rate()
        }
        
        # Calculate overall engagement
        if all(indicator > 0.7 for indicator in engagement_indicators.values()):
            return 'high'
        elif any(indicator < 0.3 for indicator in engagement_indicators.values()):
            return 'low'
        else:
            return 'moderate'

    def _handle_low_engagement_optimization(self):
        """Optimize experience for low engagement users"""
        # Shorter questions, more encouragement, simplified language
        optimizations = {
            'question_style': 'simplified',
            'progress_encouragement': True,
            'shorter_options': True,
            'more_visual_feedback': True
        }
        
        return optimizations
    
    def _handle_high_engagement_optimization(self):
        """Optimize for highly engaged users"""
        # More detailed questions, faster pace, advanced insights
        optimizations = {
            'question_style': 'detailed',
            'show_pattern_hints': True,
            'advanced_insights': True,
            'faster_progression': True
        }
        
        return optimizations

#Advanced Error Handling & Recovery 
class ProductionErrorHandling:
    """Comprehensive error handling and recovery system"""
    
    def handle_assessment_error(self, error_type, context=None):
        """Handle various assessment errors gracefully"""
        
        error_handlers = {
            'question_load_error': self._handle_question_load_error,
            'response_save_error': self._handle_response_save_error,
            'scoring_calculation_error': self._handle_scoring_error,
            'pattern_analysis_error': self._handle_pattern_analysis_error,
            'results_generation_error': self._handle_results_error,
            'state_corruption_error': self._handle_state_corruption,
            'config_integration_error': self._handle_config_error
        }
        
        handler = error_handlers.get(error_type, self._handle_generic_error)
        return handler(context)
    
    def _handle_question_load_error(self, context):
        """Handle question loading failures"""
        st.error("Question loading issue detected. Attempting recovery...")
        
        # Try to load fallback question
        fallback_question = {
            "text": "Please describe your main concern that brought you to this assessment:",
            "type": "text_completion",
            "placeholder": "Share what you'd like to work on...",
            "min_chars": 10,
            "phase": "recovery"
        }
        
        # Save recovery state
        st.session_state.error_recovery_mode = True
        st.session_state.error_recovery_timestamp = datetime.now().isoformat()
        
        st.info("Using backup question system. Your progress is saved.")
        
        return fallback_question
    
    def _handle_response_save_error(self, context):
        """Handle response saving failures"""
        response = context.get('response')
        question_id = context.get('question_id')
        
        # Attempt alternative save methods
        try:
            # Try simplified save
            st.session_state.assessment_responses[question_id] = {
                'response': response,
                'timestamp': datetime.now().isoformat(),
                'recovery_save': True
            }
            st.success("Response saved successfully (backup method)")
            return True
            
        except Exception as e:
            # Emergency local storage fallback
            self._emergency_local_save(question_id, response)
            st.warning("Response saved locally. Assessment can continue.")
            return True
    
    def _handle_state_corruption(self, context):
        """Handle session state corruption"""
        st.error("Session state issue detected. Initializing recovery mode...")
        
        # Preserve critical data
        preserved_data = self._preserve_critical_assessment_data()
        
        # Reset corrupted state
        self._reset_corrupted_state()
        
        # Restore preserved data
        self._restore_preserved_data(preserved_data)
        
        st.success("Assessment state recovered. You can continue from where you left off.")
        
        return True
    
    def _preserve_critical_assessment_data(self):
        """Preserve critical data before state reset"""
        preserved = {}
        
        critical_keys = [
            'assessment_responses',
            'pattern_scores',
            'contact_info',
            'current_question',
            'current_phase'
        ]
        
        for key in critical_keys:
            if key in st.session_state:
                try:
                    preserved[key] = st.session_state[key]
                except:
                    pass  # Skip corrupted data
        
        return preserved
    
    def validate_assessment_integrity(self):
        """Validate assessment integrity and fix issues"""
        issues_found = []
        fixes_applied = []
        
        # Check response consistency
        if hasattr(st.session_state, 'assessment_responses'):
            responses = st.session_state.assessment_responses
            
            # Validate response format
            for q_id, response_data in responses.items():
                if not isinstance(response_data, dict):
                    issues_found.append(f"Question {q_id}: Invalid response format")
                    # Fix: Convert to proper format
                    st.session_state.assessment_responses[q_id] = {
                        'response': response_data,
                        'timestamp': datetime.now().isoformat(),
                        'auto_fixed': True
                    }
                    fixes_applied.append(f"Fixed response format for question {q_id}")
        
        # Check pattern scores validity
        if hasattr(st.session_state, 'pattern_scores'):
            pattern_scores = st.session_state.pattern_scores
            
            for pattern_id, score in pattern_scores.items():
                if not isinstance(score, (int, float)) or score < 0:
                    issues_found.append(f"Pattern {pattern_id}: Invalid score")
                    # Fix: Reset to 0
                    st.session_state.pattern_scores[pattern_id] = 0
                    fixes_applied.append(f"Reset invalid score for pattern {pattern_id}")
        
        # Check phase consistency
        current_question = st.session_state.get('current_question', 1)
        current_phase = st.session_state.get('current_phase', 'age_screening')
        
        expected_phase = self._determine_expected_phase(current_question)
        
        if current_phase != expected_phase:
            issues_found.append(f"Phase inconsistency: {current_phase} vs expected {expected_phase}")
            st.session_state.current_phase = expected_phase
            fixes_applied.append(f"Corrected phase to {expected_phase}")
        
        return {
            'issues_found': issues_found,
            'fixes_applied': fixes_applied,
            'integrity_score': len(fixes_applied) / max(len(issues_found), 1)
        }

#Accessibility & Performance Optimization
class AccessibilityManager:
    """Comprehensive accessibility and performance optimization"""
    
    def apply_accessibility_enhancements(self):
        """Apply comprehensive accessibility enhancements"""
        
        # WCAG 2.1 AA compliance
        accessibility_css = """
        <style>
        /* High contrast support */
        @media (prefers-contrast: high) {
            .stButton > button {
                border: 2px solid #000 !important;
                background: #fff !important;
                color: #000 !important;
            }
            .stButton > button:hover {
                background: #000 !important;
                color: #fff !important;
            }
        }
        
        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }
        
        /* Focus management */
        .stButton > button:focus,
        .stTextInput input:focus,
        .stTextArea textarea:focus {
            outline: 3px solid #4CA1A3 !important;
            outline-offset: 2px !important;
        }
        
        /* Touch target size compliance (WCAG 2.5.5) */
        .stButton > button,
        .stRadio label,
        .stCheckbox label {
            min-height: 44px !important;
            min-width: 44px !important;
        }
        
        /* Screen reader support */
        .sr-only {
            position: absolute !important;
            width: 1px !important;
            height: 1px !important;
            padding: 0 !important;
            margin: -1px !important;
            overflow: hidden !important;
            clip: rect(0,0,0,0) !important;
            white-space: nowrap !important;
            border: 0 !important;
        }
        
        /* Color contrast compliance */
        .progress-fill {
            background: #2D5D3F !important; /* Higher contrast green */
        }
        
        /* Typography accessibility */
        body, .stMarkdown, .stButton {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif !important;
            line-height: 1.5 !important;
        }
        
        /* Spacing for readability */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            margin-top: 1.5em !important;
            margin-bottom: 0.5em !important;
        }
        
        .stMarkdown p {
            margin-bottom: 1em !important;
        }
        </style>
        """
        
        st.markdown(accessibility_css, unsafe_allow_html=True)
    
    def add_screen_reader_support(self, question_context):
        """Add screen reader specific enhancements"""
        
        # Progress announcement
        answered = len(st.session_state.get('assessment_responses', {}))
        total = 35
        
        # Hidden announcement for screen readers
        st.markdown(f"""
        <div class="sr-only" aria-live="polite" aria-atomic="true">
            Question {answered + 1} of {total}. Assessment {int((answered/total)*100)}% complete.
        </div>
        """, unsafe_allow_html=True)
        
        # Add ARIA labels to form elements
        if question_context.get('type') == 'single_choice':
            st.markdown("""
            <div role="radiogroup" aria-labelledby="question-text">
            """, unsafe_allow_html=True)
    
    def optimize_performance(self):
        """Apply performance optimizations"""
        
        # Lazy loading for non-critical components
        if 'performance_optimized' not in st.session_state:
            st.session_state.performance_optimized = True
            
            # Minimize rerun triggers
            if 'last_interaction' not in st.session_state:
                st.session_state.last_interaction = datetime.now()
            
            # Cache heavy computations
            self._setup_computation_caching()
    
    def _setup_computation_caching(self):
        """Setup caching for expensive operations"""
        
        # Cache pattern analysis results
        if 'pattern_analysis_cache' not in st.session_state:
            st.session_state.pattern_analysis_cache = {}
        
        # Cache digital analysis results
        if 'digital_analysis_cache' not in st.session_state:
            st.session_state.digital_analysis_cache = {}
        
        # Cache clinical template generation
        if 'template_cache' not in st.session_state:
            st.session_state.template_cache = {}

    def check_mobile_optimization(self):
        """Check and apply mobile-specific optimizations"""
        
        # Detect mobile viewport
        mobile_script = """
        <script>
        function isMobile() {
            return window.innerWidth <= 768 || /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        }
        
        if (isMobile()) {
            document.body.classList.add('mobile-optimized');
            
            // Prevent zoom on form inputs
            var inputs = document.querySelectorAll('input, textarea, select');
            inputs.forEach(function(input) {
                input.style.fontSize = '16px';
            });
        }
        </script>
        """
        
        st.markdown(mobile_script, unsafe_allow_html=True)
        
        # Mobile-specific CSS
        mobile_css = """
        <style>
        @media (max-width: 768px) {
            .mobile-optimized .stButton > button {
                font-size: 1rem !important;
                padding: 1rem !important;
                margin-bottom: 0.75rem !important;
            }
            
            .mobile-optimized .stTextArea textarea,
            .mobile-optimized .stTextInput input {
                font-size: 16px !important; /* Prevents iOS zoom */
            }
            
            .mobile-optimized .progress-container {
                flex-direction: column;
                gap: 0.5rem;
            }
            
            .mobile-optimized .progress-bar {
                width: 100%;
            }
        }
        </style>
        """
        
        st.markdown(mobile_css, unsafe_allow_html=True)

#Final Integration & Main Application
class ProductionAssessment:
    """Main production assessment class integrating all components"""
    
    def __init__(self):
        # Initialize all systems
        self.pattern_analyzer = AdvancedPatternAnalyzer()
        self.digital_analyzer = DigitalDespairAnalyzer()
        self.results_engine = ProductionResultsEngine()
        self.clinical_system = ClinicalIntegrationSystem()
        self.data_manager = ProductionDataManager()
        self.communication_manager = CommunicationManager()
        self.question_flow = SmartQuestionFlow()
        self.error_handler = ProductionErrorHandling()
        self.accessibility_manager = AccessibilityManager()
        self.ui_renderer = QuestionRenderer()
        
        # Initialize state
        self._init_production_state()
        
        # Apply optimizations
        self.accessibility_manager.apply_accessibility_enhancements()
        self.accessibility_manager.optimize_performance()
        self.accessibility_manager.check_mobile_optimization()
    
    def render(self):
        """Main render method with comprehensive error handling"""
        try:
            # Apply production styling
            apply_production_mobile_styles()
            
            # Validate assessment integrity
            integrity_check = self.error_handler.validate_assessment_integrity()
            
            if integrity_check['fixes_applied']:
                st.info(f"Applied {len(integrity_check['fixes_applied'])} automatic fixes to ensure data integrity")
            
            # Main assessment flow
            if not st.session_state.get('contact_provided', False):
                if not st.session_state.get('assessment_completed', False):
                    self._render_assessment_flow()
                else:
                    self._render_contact_form()
            else:
                self._render_comprehensive_results()
                
        except Exception as e:
            self.error_handler.handle_assessment_error('generic_error', {'exception': e})
    
    def _render_assessment_flow(self):
        """Render main assessment flow with smart question selection"""
        try:
            # Get next optimized question
            q_id, question = self.question_flow.get_next_optimized_question()
            
            if q_id is None:
                self._complete_comprehensive_assessment()
                return
            
            if not question:
                # Handle missing question
                question = self.error_handler.handle_assessment_error('question_load_error')
            
            # Add accessibility support
            self.accessibility_manager.add_screen_reader_support(question)
            
            # Render question with full UI system
            self.ui_renderer.render_question_with_progress(q_id, question)
            
        except Exception as e:
            self.error_handler.handle_assessment_error('assessment_flow_error', {'exception': e})
    
    def _complete_comprehensive_assessment(self):
        """Complete assessment with full analysis generation"""
        try:
            st.session_state.assessment_completed = True
            
            # Generate complete analysis
            assessment_data = self._compile_complete_assessment_data()
            comprehensive_results = self.results_engine.generate_comprehensive_results(assessment_data)
            
            # Store results
            st.session_state.comprehensive_analysis = comprehensive_results
            
            # Generate clinical insights
            clinical_template = self.clinical_system.generate_comprehensive_clinical_template(assessment_data)
            st.session_state.clinical_template = clinical_template
            
            # Calculate final success predictions
            success_prediction = comprehensive_results.get('success_prediction', {})
            st.session_state.success_probability = success_prediction.get('overall_probability', 85)
            
            st.rerun()
            
        except Exception as e:
            self.error_handler.handle_assessment_error('completion_error', {'exception': e})
    
    def _render_comprehensive_results(self):
        """Render comprehensive results with all insights"""
        try:
            # Mobile-optimized hero section
            self.render_results_hero_mobile_optimized()
            
            # Full analysis sections
            self._render_pattern_analysis_section()
            self._render_transformation_roadmap_section()
            self._render_personalized_techniques_section()
            self._render_next_steps_section()
            
        except Exception as e:
            self.error_handler.handle_assessment_error('results_rendering_error', {'exception': e})


# ---- Factory Functions ----
def create_production_assessment():
    """Factory function to create production assessment"""
    return ProductionAssessment()

def get_assessment_analytics():
    """Get comprehensive assessment analytics"""
    if 'comprehensive_analysis' in st.session_state:
        return st.session_state.comprehensive_analysis
    return None

def reset_assessment_with_backup():
    """Reset assessment with data backup"""
    # Create backup
    backup_data = ProductionDataManager().export_complete_assessment_data()
    
    # Store backup
    if backup_data:
        st.session_state.assessment_backup = backup_data
    
    # Reset assessment state
    assessment_keys = [k for k in st.session_state.keys() if 'assessment' in k.lower() or 'pattern' in k.lower()]
    for key in assessment_keys:
        if key != 'assessment_backup':
            del st.session_state[key]

def create_assess_page():
    """Factory function to create assessment page instance"""
    return ProductionAssessment()

# Alternative class wrapper if needed
class AssessPage:
    def __init__(self):
        self.assessment = ProductionAssessment()
    
    def render(self):
        self.assessment.render()

# ---- Main Application Entry Point ----
if __name__ == "__main__":
    st.set_page_config(
        page_title="Advanced Behavioral Pattern Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize and render production assessment
    assessment = create_production_assessment()
    assessment.render()


        



# import streamlit as st

# def create_assess_page():
#     """Ultra minimal test version with debug"""
    
#     st.write("🔍 **Debug: create_assess_page() function called**")
    
#     try:
#         st.write("✅ Inside create_assess_page function")
        
#         class UltraSimpleAssessment:
#             def __init__(self):
#                 st.write("✅ UltraSimpleAssessment.__init__ called")
            
#             def render(self):
#                 st.write("✅ UltraSimpleAssessment.render() called")
#                 st.markdown("# 🧠 Ultra Simple Assessment")
#                 st.success("✅ Basic assessment page loading works!")
                
#                 st.markdown("## Test Form")
#                 name = st.text_input("Name:")
#                 if name:
#                     st.success(f"Hello, {name}!")
        
#         st.write("✅ About to create UltraSimpleAssessment instance")
#         assessment = UltraSimpleAssessment()
#         st.write("✅ UltraSimpleAssessment instance created successfully")
        
#         return assessment
        
#     except Exception as e:
#         st.error(f"❌ Error in create_assess_page: {str(e)}")
#         st.exception(e)
#         return None
