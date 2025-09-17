# Complete Enhanced Clinical Behavioral Pattern Assessment
# Integrated with algorithmical divide Syndrome screening and analysis
# Comprehensive implementation with adaptive questioning and pattern detection
# Optimized for both traditional and digital-native populations

import streamlit as st
from datetime import datetime
import re
import uuid
import base64
import json
import hashlib

# Import components with error handling
try:
    from components.blueprint import create_behavioral_blueprint
    BLUEPRINT_AVAILABLE = True
except ImportError:
    BLUEPRINT_AVAILABLE = False
    st.warning("Blueprint component not available")

try:
    from utils.pdf_generator import PDFGenerator
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

try:
    from utils.email_assess import send_clinical_assessment_results

    SEND_CLINICAL_AVAILABLE = True
except Exception:
    SEND_CLINICAL_AVAILABLE = False

try:
    from utils.email_handler import UnifiedEmailHandler
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False

# Try to import centralized config; if unavailable, create minimal fallbacks
try:
    from utils.config import (
        PatternDefinitions,
        QuestionSets,
        DIGITAL_SCORING_RULES,
        PATTERN_SCORING_RULES,
        BELIEF_HINTS,
        DISCOVERY_PHASE_RULES,
        DIGITAL_SUCCESS_INDICATORS,
        DIGITAL_THRESHOLDS
        EmailConfig,
    )
    CONFIG_AVAILABLE = True
except Exception:
    CONFIG_AVAILABLE = False

    # Minimal fallback (keeps app from crashing if config import fails)
    class PatternDefinitions:
        PATTERNS = {
            1: "Unhappiness Culture",
            2: "Power Struggles",
            3: "Systematic Mistrust",
            4: "Separation and Division",
            5: "Doing versus Being",
            6: "Compartmentalized Authenticity",
            7: "Self Sacrifice and Care Avoidance",
            8: "Inherited Missions",
            9: "Context Dependent Weakness",
        }
        PATTERN_DESCRIPTIONS = {}
        DIGITAL_THRESHOLDS = {}

    class QuestionSets:
        AGE_SCREENING = {}
        DIGITAL_SCREENING = {}
        ENGAGEMENT = {}
        TRIGGER_MAPPING = {}
        PATTERN_SPECIFIC = {}
        INTEGRATION = {}

    DIGITAL_SCORING_RULES = {}
    PATTERN_SCORING_RULES = {}
    EmailConfig = None



# ---- Paywall Integration ----
try:
    from components.paywall import create_clinical_paywall
    PAYWALL_AVAILABLE = True
except ImportError:
    PAYWALL_AVAILABLE = False

# ---- Styling Functions ----
def apply_clinical_styles():
    """Apply expert clinical-grade styling with enhanced UX elements"""
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 0.75rem !important;
        padding-bottom: 0.75rem !important;
        max-width: 100% !important;
    }
    @media (min-width: 768px) {
        .main .block-container {
            max-width: 650px !important;
            margin: 0 auto;
        }
    }
    .stButton > button {
        width: 100% !important;
        margin-bottom: 0.25rem !important;
        padding: 0.6rem 1rem !important;
        text-align: left !important;
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 6px !important;
        color: #374151 !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        line-height: 1.3 !important;
    }
    .stButton > button:hover {
        background-color: #F1F5F9 !important;
        border-color: #4CA1A3 !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:focus {
        background-color: #E1F0F0 !important;
        border-color: #4CA1A3 !important;
        outline: none !important;
    }
    .progress-container {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        font-size: 0.75rem;
        font-weight: normal; 
        color: #556D7A;
        padding: 0.5rem;
    }
    .progress-bar {
        flex: 1;
        height: 4px;
        background: #E2E8F0;
        border-radius: 2px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        background: #4CA1A3;
        transition: width 0.3s ease;
    }
    .time-estimate {
        font-size: 0.8rem;
        color: #64748b;
        text-align: center;
        margin-top: 0.5rem;
    }
    .char-counter {
        font-size: 0.8rem;
        margin-top: 0.5rem;
        text-align: right;
    }
    .char-counter.sufficient {
        color: #059669;
    }
    .char-counter.insufficient {
        color: #dc2626;
    }
    .digital-indicator {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        font-size: 0.85rem;
        text-align: center;
    }
    .pattern-hint {
        background: #f0f9ff;
        border-left: 3px solid #0ea5e9;
        padding: 0.5rem;
        margin: 0.5rem 0;
        font-size: 0.85rem;
        font-style: italic;
    }
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #4CA1A3 0%, #357a7c 100%);
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        margin: 20px auto;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .cta-button:hover {
        transform: translateY(-2px);
        text-decoration: none;
        color: white !important;
    }
    .text-center {
        text-align: center;
    }
    /* Enhanced Results Page Styles */
    .results-hero {
        background: linear-gradient(135deg, #F3F6F8 0%, #e1f0f0 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid #CBD5E1;
    }
    .insight-card {
        background: #FFFFFF;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .pattern-badge {
        display: inline-block;
        background: #4CA1A3;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    .severity-high { background: #ef4444; }
    .severity-moderate { background: #eab308; }
    .severity-mild { background: #4CA1A3; }
    .severity-minimal { background: #22c55e; }
    .next-step-card {
        background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .timeline-item {
        display: flex;
        align-items: center;
        margin: 0.8rem 0;
        padding: 0.5rem;
        background: #F3F6F8;
        border-radius: 6px;
        border-left: 3px solid #4CA1A3;
    }
    .timeline-number {
        background: #4CA1A3;
        color: white;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 1rem;
        flex-shrink: 0;
    }
    .priority-banner {
        background: #fef3c7;
        border: 1px solid #eab308;
        color: #92400e;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 500;
    }
    .success-indicator {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-bar {
        flex: 1;
        height: 8px;
        background: #E2E8F0;
        border-radius: 4px;
        overflow: hidden;
    }
    .success-fill {
        height: 100%;
        background: linear-gradient(90deg, #4CA1A3 0%, #22c55e 100%);
        transition: width 0.5s ease;
    }
    .transformation-preview {
        background: #f0f9ff;
        border: 1px solid #0ea5e9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# -------------------------
# Simple Storage & Email Queue
# -------------------------

class SimpleStorage:
    def __init__(self):
        if 'assessment_storage' not in st.session_state:
            st.session_state.assessment_storage = {}
        if STORAGE_FACTORY_AVAILABLE:
            self.storage = create_storage_client()
        else:
            self.storage = None
    
    def save_assessment(self, session_id, data):
        st.session_state.assessment_storage[session_id] = {
            'data': data,
            'saved_at': datetime.now().isoformat(),
            'type': 'assessment'
        }
        return f"session://{session_id}"
    
    def get_assessment(self, session_id):
        return st.session_state.assessment_storage.get(session_id, {}).get('data')


# # ---- Email Queue System ----
# class EmailQueue:
#     def __init__(self):
#         if 'email_queue' not in st.session_state:
#             st.session_state.email_queue = []
    
#     def add_request(self, email_data):
#         st.session_state.email_queue.append({
#             **email_data,
#             'timestamp': datetime.now().isoformat(),
#             'processed': False
#         })
    
#     def get_pending(self):
#         return [req for req in st.session_state.email_queue if not req.get('processed')]
    
#     def mark_processed(self, index):
#         if 0 <= index < len(st.session_state.email_queue):
#             st.session_state.email_queue[index]['processed'] = True

# # ---- Simplified PDF Generator ----
# def generate_simple_pdf_content(assessment_data):
#     """Generate PDF content as text (fallback when reportlab unavailable)"""
#     contact_info = assessment_data.get('contact_info', {})
#     pattern_scores = assessment_data.get('pattern_scores', {})
    
#     patterns = {
#         1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
#         4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
#         7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
#     }
    
#     content = f"""
# BEHAVIORAL TRANSFORMATION BLUEPRINT
# Personalized Analysis for {contact_info.get('name', 'Valued Client')}
# Generated: {datetime.now().strftime('%B %d, %Y')}

# EXECUTIVE SUMMARY
# ==============
# Patterns Identified: {len(pattern_scores)}
# Assessment Completion: {assessment_data.get('completion_rate', 1.0)*100:.0f}%
# Digital Native: {'Yes' if assessment_data.get('is_digital_native') else 'No'}

# PATTERN ANALYSIS
# ===============
# """
    
#     if pattern_scores:
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
#         for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
#             pattern_name = patterns.get(pattern_id, f"Pattern {pattern_id}")
#             intensity = "High" if score >= 6 else "Moderate" if score >= 4 else "Mild"
#             content += f"{i+1}. {pattern_name} - {intensity} Intensity (Score: {score:.1f}/10)\n"
    
#     content += f"""

# TRANSFORMATION ROADMAP
# =====================
# Recommended Protocol: 2-3 sessions over 2-4 weeks
# Success Probability: 85-92%
# Timeline for Results: 24-48 hours for initial shifts

# SESSION BREAKDOWN:
# Session 1: Deep Pattern Analysis & Rapport Building (90 minutes)
# Session 2: Core Transformation & Neural Rewiring (90 minutes)
# Session 3: Integration & Mastery (60 minutes - if needed)

# INVESTMENT ANALYSIS
# ==================
# Transformation Investment: $3,000-4,000
# Traditional Therapy Alternative: $15,000-25,000 over 18+ months
# Success Rate: 85% vs 30-40% traditional approaches
# Break-even Time: 2-6 months typically

# NEXT STEPS
# ==========
# 1. Clinical Review (24-48 hours)
# 2. Personal Contact (48-72 hours)
# 3. First Transformation Session (within 1 week)

# Contact: hypnotherapy.streamlit.app
# Direct Scheduling: calendly.com/laetitiasheppard/discovery

# © 2024 Rapid Transformation Hypnotherapy - Confidential Report
# Assessment ID: {assessment_data.get('session_id', 'Unknown')[:8]}
# """
    
#     return content

# # ---- Admin Interface ----
# def render_admin_interface():
#     """Simple admin interface for email queue management"""
#     if not st.session_state.get('admin_authenticated', False):
#         with st.sidebar:
#             st.markdown("### 🔐 Admin Access")
#             admin_password = st.text_input("Password", type="password", key="admin_pass")
            
#             if st.button("Login"):
#                 # Simple password check - use environment variable in production
#                 if admin_password == st.secrets.get("admin", {}).get("password", "admin123"):
#                     st.session_state.admin_authenticated = True
#                     st.rerun()
#                 else:
#                     st.error("Invalid password")
#     else:
#         with st.sidebar:
#             st.success("✅ Admin Access")
            
#             if st.button("Logout"):
#                 st.session_state.admin_authenticated = False
#                 st.rerun()
        
#         # Main admin interface
#         st.markdown("### Admin Dashboard")
        
#         tab1, tab2 = st.tabs(["📧 Email Queue", "📊 Analytics"])
        
#         with tab1:
#             email_queue = EmailQueue()
#             pending_emails = email_queue.get_pending()
            
#             st.markdown(f"**Pending email requests: {len(pending_emails)}**")
            
#             if pending_emails:
#                 for i, request in enumerate(pending_emails):
#                     with st.expander(f"Email {i+1}: {request['recipient']} - {request['assessment_summary']['urgency']}"):
#                         st.json(request)
                        
#                         if st.button(f"Mark as processed", key=f"process_{i}"):
#                             email_queue.mark_processed(i)
#                             st.success("Request marked as processed")
#                             st.rerun()
#             else:
#                 st.info("No pending email requests")
        
#         with tab2:
#             # Storage analytics
#             storage_count = len(st.session_state.get('assessment_storage', {}))
#             email_count = len(st.session_state.get('email_queue', []))
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.metric("Stored Assessments", storage_count)
#             with col2:
#                 st.metric("Email Requests", email_count)
            
#             # Show recent assessments
#             if st.session_state.get('assessment_storage'):
#                 st.markdown("**Recent Assessments:**")
#                 for session_id, data in list(st.session_state.assessment_storage.items())[-5:]:
#                     assessment_data = data.get('data', {})
#                     contact_info = assessment_data.get('contact_info', {})
#                     st.markdown(f"• {session_id[:8]} - {contact_info.get('name', 'Anonymous')} - {data.get('saved_at', 'Unknown')}")




# -------------------------
# Core Assessment Class
# -------------------------

class ComprehensiveBehavioralAssessment:
    """Clinical-grade behavioral pattern assessment with algorithmical divide Syndrome integration"""
    
    def __init__(self):
        self._init_session_state()
        self.storage = SimpleStorage()
        self.email_queue = EmailQueue()
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        
        # patterns & email config imported from config
        self.patterns = PatternDefinitions.PATTERNS if CONFIG_AVAILABLE else PatternDefinitions.PATTERNS
        self.pattern_descriptions = (
            PatternDefinitions.PATTERN_DESCRIPTIONS if CONFIG_AVAILABLE else PatternDefinitions.PATTERN_DESCRIPTIONS
        )
        self.digital_thresholds = (
            PatternDefinitions.DIGITAL_THRESHOLDS if CONFIG_AVAILABLE else getattr(PatternDefinitions, "DIGITAL_THRESHOLDS", {})
        )
        self.email_config = EmailConfig if CONFIG_AVAILABLE else None

        # load question pools from config (or fallback empty dicts)
        self.age_screening_questions = getattr(QuestionSets, "AGE_SCREENING", {})
        self.digital_screening_questions = getattr(QuestionSets, "DIGITAL_SCREENING", {})
        self.engagement_questions = getattr(QuestionSets, "ENGAGEMENT", {})
        self.trigger_mapping_questions = getattr(QuestionSets, "TRIGGER_MAPPING", {})
        self.pattern_specific_questions = getattr(QuestionSets, "PATTERN_SPECIFIC", {})
        self.integration_questions = getattr(QuestionSets, "INTEGRATION", {})


    def _init_session_state(self):
        defaults = {
            'assessment_responses': {},
            'current_question': 1,
            'current_phase': 'age_screening',
            'phase_progress': {
                'age_screening': 0, 'digital_screening': 0, 'engagement': 0, 
                'trigger_mapping': 0, 'pattern_specific': 0, 'integration': 0
            },
            'is_digital_native': False,
            'digital_despair_score': 0,
            'digital_severity': 'MINIMAL',
            'triggered_patterns': set(),
            'pattern_scores': {},
            'risk_flags': [],
            'assessment_completed': False,
            'contact_provided': False,
            'assessment_results': {},
            'start_time': datetime.now().isoformat(),
            'intensity_responses': {},
            'trigger_chain': {},
            'digital_responses': {},
            'adaptive_paths': []
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    # ---- Response analysis & digital calculations ----
    
    def _analyze_digital_despair_indicators(self, responses):
        """Analyze responses for algorithmical divide Syndrome indicators"""
        
        # Age factor (digital native status)
        age_response = responses.get(0, {}).get('response', '')
        digital_native_score = 0
        
        age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
        scoring = [3, 5, 4, 3, 2, 1, 0, 0]
        
        try:
            age_index = age_options.index(age_response)
            digital_native_score = scoring[age_index]
        except (ValueError, IndexError):
            digital_native_score = 0
        
        # Determine if digital native assessment was triggered
        if digital_native_score < 2:
            return None  # Skip digital despair analysis for non-digital natives
        
        # Extract component scores
        reality_dissociation = self._extract_reality_dissociation_score(responses)
        binary_thinking = self._extract_binary_success_score(responses) 
        ironic_detachment = self._extract_ironic_detachment_score(responses)
        algorithmic_dependency = self._extract_algorithmic_dependency_score(responses)
        nihilistic_worldview = self._extract_nihilistic_worldview_score(responses)
        hope_avoidance = self._extract_hope_avoidance_score(responses)
        attention_fragmentation = self._extract_attention_fragmentation_score(responses)
        
        # Calculate composite algorithmical divide Score
        total_possible = 35  # Maximum possible score across all indicators
        raw_score = (digital_native_score + reality_dissociation + binary_thinking + 
                     ironic_detachment + algorithmic_dependency + nihilistic_worldview + 
                     hope_avoidance + attention_fragmentation)
        
        digital_despair_percentage = (raw_score / total_possible) * 100
        
        # severity lookup using thresholds in config when available
        severity = "MINIMAL"
        recommendation = "Traditional hypnotherapy approach suitable"
        if self.digital_thresholds:
            for level, data in sorted(
                self.digital_thresholds.items(),
                key=lambda x: x[1]["threshold"],
                reverse=True
            ):
                if digital_despair_percentage >= data["threshold"]:
                    severity = level
                    recommendation = data.get("title", "")
                    break
    
        return {
            "digital_despair_score": digital_despair_percentage,
            "severity_level": severity,
            "clinical_recommendation": recommendation,
            "component_scores": {
                'digital_native_status': digital_native_score,
                'reality_dissociation': reality_dissociation,
                'binary_success_pressure': binary_thinking,
                'ironic_detachment': ironic_detachment, 
                'algorithmic_dependency': algorithmic_dependency,
                'nihilistic_worldview': nihilistic_worldview,
                'hope_avoidance': hope_avoidance,
                'attention_fragmentation': attention_fragmentation
            },
            "therapeutic_adaptations_needed": self.digital_thresholds[severity].get("adaptations", []),
        }

    
    # ---Helper functions for extracting specific scores
    def _extract_reality_dissociation_score(self, responses):
        """Extract reality dissociation indicators from responses"""
        score = 0
        
        # Digital vs offline authenticity (question 2)
        digital_auth_data = responses.get(2, {})
        digital_auth = digital_auth_data.get('response', '')
        
        if 'online communities and digital spaces' in digital_auth:
            score += 3
        elif 'don\'t feel authentic anywhere' in digital_auth:
            score += 4
        elif 'varies completely depending' in digital_auth:
            score += 2
            
        # Add intensity multiplier if available
        intensity = digital_auth_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)  # Scale intensity 1-7 to multiplier
        
        return min(5, score)  # Cap at 5 points for this component

    def _extract_binary_success_score(self, responses):
        """Extract binary success framework indicators"""
        score = 0
        
        success_def = responses.get(3, {}).get('response', '')
        if 'Extraordinary wealth, fame, or achievement' in success_def:
            score += 4
        elif 'Success feels impossible or meaningless' in success_def:
            score += 4
        elif 'significantly better than most people' in success_def:
            score += 3
            
        return min(5, score)

    def _extract_ironic_detachment_score(self, responses):
        """Extract ironic detachment indicators"""
        score = 0
        
        emotion_expr_data = responses.get(4, {})
        emotion_expr = emotion_expr_data.get('response', '')
        
        if 'embarrassed or \'cringe\' about sincerity' in emotion_expr:
            score += 3
        elif 'through memes or online references' in emotion_expr:
            score += 3
        elif 'rarely express genuine emotions' in emotion_expr:
            score += 4
        elif 'humor or irony to deflect' in emotion_expr:
            score += 2
        
        # Apply intensity multiplier
        intensity = emotion_expr_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)
        
        return min(5, score)

    def _extract_algorithmic_dependency_score(self, responses):
        """Extract algorithmic emotional regulation indicators"""
        score = 0
        
        emotion_source = responses.get(5, {}).get('response', '')
        if 'Social media feeds and online content' in emotion_source:
            score += 3
        elif 'Online communities and digital relationships' in emotion_source:
            score += 3
            
        relationship_invest = responses.get(6, {}).get('response', '')
        if 'Online personalities' in relationship_invest:
            score += 2
        elif 'Online friends and communities' in relationship_invest:
            score += 2
        elif 'Fictional characters' in relationship_invest:
            score += 3
            
        return min(5, score)

    def _extract_nihilistic_worldview_score(self, responses):
        """Extract nihilistic worldview indicators"""  
        score = 0
        
        # Check success definition for nihilism
        success_def = responses.get(3, {}).get('response', '')
        if 'Success feels impossible or meaningless' in success_def:
            score += 4
            
        return min(5, score)

    def _extract_hope_avoidance_score(self, responses):
        """Extract hope avoidance indicators"""
        score = 0
        
        hope_relation_data = responses.get(7, {})
        hope_relation = hope_relation_data.get('response', '')
        
        if 'dismiss it as naive or manipulative' in hope_relation:
            score += 4
        elif 'annoyed because they don\'t understand reality' in hope_relation:
            score += 3  
        elif 'think of reasons why they\'re wrong' in hope_relation:
            score += 2
        
        # Apply intensity multiplier
        intensity = hope_relation_data.get('intensity', 1)
        if intensity:
            score *= (intensity / 4)
        
        return min(5, score)

    def _extract_attention_fragmentation_score(self, responses):
        """Extract attention fragmentation indicators"""
        score = 0
        
        focus_capacity = responses.get(8, {}).get('response', '')
        focus_options = [
            "Same as always - can focus for hours when interested",
            "Slightly shorter but manageable", 
            "Noticeably fragmented - need frequent stimulation",
            "Very difficult - mind wanders constantly",
            "Almost impossible without background digital stimulation"
        ]
        scoring = [0, 1, 2, 3, 4]
        
        try:
            focus_index = focus_options.index(focus_capacity)
            score = scoring[focus_index]
        except (ValueError, IndexError):
            score = 0
        
        return min(5, score)

    # ---- Pattern Detection and Scoring ----
    
    def _analyze_text_for_patterns(self, text, keywords_dict):
        """Analyze text response for pattern indicators"""
        text_lower = text.lower()
        detected_patterns = set()
        
        for keyword, patterns in keywords_dict.items():
            if keyword in text_lower:
                detected_patterns.update(patterns)
        
        return detected_patterns

    def _update_pattern_scores(self, question_id, response, question):
        """Update pattern scores based on response"""
        # Handle different question types
        if question.get('pattern_triggers') and isinstance(response, str):
            if 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_triggers']:
                        patterns = question['pattern_triggers'][option_index]
                        for pattern in patterns:
                            self._add_pattern_score(pattern, 1.0)
                except (ValueError, IndexError):
                    pass
        # pattern_mapping
        elif question.get('pattern_mapping') and isinstance(response, str):
            if 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index in question['pattern_mapping']:
                        patterns = question['pattern_mapping'][option_index]
                        for pattern in patterns:
                            self._add_pattern_score(pattern, 1.5)
                except (ValueError, IndexError):
                    pass
        # pattern_keywords (analysis of free-text)
        elif question.get('pattern_keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['pattern_keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 2.0)
        # keywords (less strong)
        elif question.get('keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 1.0)
        
        # Handle pattern-specific questions with weights
        if question.get('pattern') and question.get('weights'):
            pattern_id = question['pattern']
            if isinstance(response, str) and 'options' in question:
                try:
                    option_index = question['options'].index(response)
                    if option_index < len(question['weights']):
                        weight = question['weights'][option_index]
                        if weight > 0:
                            self._add_pattern_score(pattern_id, weight)
                except (ValueError, IndexError):
                    pass

    def _add_pattern_score(self, pattern_id, score):
        """Add score to pattern with intensity multiplier if available"""
        if pattern_id in st.session_state.pattern_scores:
            st.session_state.pattern_scores[pattern_id] += score
        else:
            st.session_state.pattern_scores[pattern_id] = score

    def _check_adaptive_triggers(self, question_id, response, question):
        """Check if response triggers adaptive questioning"""
        # Trigger pattern-specific questions when scores reach threshold
        for pattern_id, score in st.session_state.pattern_scores.items():
            if score >= 3.0 and pattern_id not in st.session_state.triggered_patterns:
                st.session_state.triggered_patterns.add(pattern_id)
                st.session_state.adaptive_paths.append(f"pattern_{pattern_id}")


    # ---- Response persistence ----
    
    def _save_response(self, q_id, response, question, intensity=None):
        """Save response and update scoring"""
        st.session_state.assessment_responses[q_id] = {
            'response': response,
            'intensity': intensity,
            'question_text': question['text'],
            'question_type': question['type'],
            'timestamp': datetime.now().isoformat(),
            'phase': question.get('phase', 'unknown')
        }
        
        if intensity:
            st.session_state.intensity_responses[q_id] = intensity
        
        # Update chain mapping for trigger sequence
        if question.get('chain_mapping'):
            st.session_state.trigger_chain[question['chain_mapping']] = response
        
        # Store digital responses separately
        if question.get('phase') == 'digital_screening':
            st.session_state.digital_responses[q_id] = response
        
        # Update pattern scores
        self._update_pattern_scores(q_id, response, question)
        # Check for adaptive triggers
        self._check_adaptive_triggers(q_id, response, question)
        
        # Update phase progress
        phase = question.get('phase', 'unknown')
        if phase in st.session_state.phase_progress:
            st.session_state.phase_progress[phase] += 1

    # ---- Question Navigation Logic based on config question pools ----
    
    def _get_next_question(self):
        """Determine next question based on current phase and responses"""
        answered = set(st.session_state.assessment_responses.keys())

        # Phase 0: age screening (single question expected)
        if st.session_state.current_phase == "age_screening":
            # If question 0 not answered, return it
            if 0 in self.age_screening_questions and 0 not in answered:
                return 0, self.age_screening_questions[0]
            # determine digital native flag
            age_response = st.session_state.assessment_responses.get(0, {}).get("response", "")
            age_options = self.age_screening_questions.get(0, {}).get("options", [])
            scoring = self.age_screening_questions.get(0, {}).get("digital_native_scoring", [])
            try:
                idx = age_options.index(age_response)
                st.session_state.is_digital_native = scoring[idx] >= 2
            except Exception:
                st.session_state.is_digital_native = False
            # advance
            st.session_state.current_phase = "digital_screening" if st.session_state.is_digital_native else "engagement"

        # Phase 1: digital screening (1..8)
        if st.session_state.current_phase == "digital_screening":
            for q_id in sorted(self.digital_screening_questions.keys()):
                if q_id not in answered:
                    return q_id, self.digital_screening_questions[q_id]
            st.session_state.current_phase = "engagement"

        # Phase 2: engagement (9..13)
        if st.session_state.current_phase == "engagement":
            for q_id in sorted(self.engagement_questions.keys()):
                if q_id not in answered:
                    return q_id, self.engagement_questions[q_id]
            st.session_state.current_phase = "trigger_mapping"

        # Phase 3: trigger mapping (14..21)
        if st.session_state.current_phase == "trigger_mapping":
            for q_id in sorted(self.trigger_mapping_questions.keys()):
                if q_id not in answered:
                    return q_id, self.trigger_mapping_questions[q_id]
            st.session_state.current_phase = "pattern_specific"

        # Phase 4: pattern-specific (adaptive)
        if st.session_state.current_phase == "pattern_specific":
            # iterate triggered patterns first
            for pattern_id in list(st.session_state.triggered_patterns):
                pattern_key = f"pattern_{pattern_id}"
                if pattern_key in self.pattern_specific_questions:
                    for q_id, question in self.pattern_specific_questions[pattern_key].items():
                        if q_id not in answered:
                            return q_id, question
            # if none left, move to integration
            st.session_state.current_phase = "integration"

        # Phase 5: integration (last set)
        if st.session_state.current_phase == "integration":
            for q_id in sorted(self.integration_questions.keys()):
                if q_id not in answered:
                    return q_id, self.integration_questions[q_id]

        return None, None

    def _estimate_total_questions(self):
        base = 1  # age question
        if st.session_state.is_digital_native:
            base += len(self.digital_screening_questions)
        base += len(self.engagement_questions) + len(self.trigger_mapping_questions) + len(self.integration_questions)
        # pattern questions depending on triggered
        pattern_qs = 0
        for pid in st.session_state.triggered_patterns:
            pk = f"pattern_{pid}"
            pattern_qs += len(self.pattern_specific_questions.get(pk, {}))
        return base + pattern_qs

    def _estimate_time_remaining(self):
        """Estimate remaining time"""
        total_q = self._estimate_total_questions()
        answered = len(st.session_state.assessment_responses)
        remaining = max(0, total_q - answered)
        # Adjust time estimate based on digital native status
        if st.session_state.is_digital_native and st.session_state.digital_severity == 'SEVERE':
            return remaining * 0.8  # Faster pacing for digital natives
        else:
            return remaining * 1.0

    # ---- Response Type Handlers ----
    
    def _handle_single_choice(self, q_id, question):
        """Handle single choice questions"""
        for i, option in enumerate(question['options']):
            if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                self._save_response(q_id, option, question)
                self._advance_question()
                st.rerun()

    def _handle_single_choice_with_intensity(self, q_id, question):
        """Handle single choice with intensity rating"""
        selection_key = f"selected_option_{q_id}"
        
        for i, option in enumerate(question['options']):
            if st.button(option, key=f"q_{q_id}_opt_{i}", use_container_width=True):
                st.session_state[selection_key] = option
                st.rerun()
        
        if selection_key in st.session_state:
            selected_option = st.session_state[selection_key]
            st.success(f"Selected: {selected_option}")
            
            st.markdown("**How intense is this experience for you?**")
            intensity = st.select_slider(
                "Intensity level:",
                options=[1, 2, 3, 4, 5, 6, 7],
                format_func=lambda x: f"{x}/7",
                value=4,
                key=f"q_{q_id}_intensity"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                st.caption("1 = Very mild")
            with col2:
                st.caption("7 = Extremely intense")
            
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, selected_option, question, intensity)
                if selection_key in st.session_state:
                    del st.session_state[selection_key]
                self._advance_question()
                st.rerun()

    def _handle_multi_select_weighted(self, q_id, question):
        """Handle multi-select with intensity weighting"""
        max_sel = question.get('max_selections', len(question['options']))
        selected = st.multiselect(
            "Select all that apply:",
            question['options'],
            key=f"q_{q_id}_multi",
            max_selections=max_sel
        )
        
        if selected:
            st.markdown("**Rate the intensity of each selected emotion:**")
            intensities = {}
            for emotion in selected:
                safe_key = emotion.replace('/', '_').replace(' ', '_')
                intensities[emotion] = st.select_slider(
                    f"{emotion}:",
                    options=[1, 2, 3, 4, 5, 6, 7],
                    format_func=lambda x: f"{x}/7",
                    value=4,
                    key=f"q_{q_id}_{safe_key}_intensity"
                )
            
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                weighted_response = {emotion: intensities[emotion] for emotion in selected}
                self._save_response(q_id, weighted_response, question)
                self._advance_question()
                st.rerun()

    def _handle_text_completion(self, q_id, question):
        """Handle text completion questions"""
        min_chars = question.get('min_chars', 3)
        response = st.text_area(
            "Your response:",
            placeholder=question.get('placeholder', 'Please share your thoughts...'),
            key=f"q_{q_id}_text",
            height=120
        )
        
        char_count = len(response.strip())
        if char_count > 0:
            sufficient = char_count >= min_chars
            color_class = "sufficient" if sufficient else "insufficient"
        
        if char_count >= min_chars:
            if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
                self._save_response(q_id, response.strip(), question)
                self._advance_question()
                st.rerun()
        elif char_count > 0:
            st.info(f"Please provide at least {min_chars - char_count} more characters for a complete response.")

    def _handle_scale_10(self, q_id, question):
        """Handle 1-10 scale questions"""
        labels = question.get('labels', ['Low', 'High'])
        value = st.select_slider(
            "Rate your readiness:",
            options=list(range(1, 11)),
            format_func=lambda x: f"{x}/10",
            value=5,
            key=f"q_{q_id}_scale"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.caption(f"1 = {labels[0]}")
        with col2:
            st.caption(f"10 = {labels[1]}")
        
        # Show follow-up if score is low
        follow_up = ""
        if value <= question.get('follow_up_trigger', 5):
            follow_up = st.text_input(
                "What would need to happen to make it a 10?",
                key=f"q_{q_id}_followup",
                placeholder="What would increase your readiness?"
            )
        
        if st.button("Continue", key=f"q_{q_id}_continue", type="primary", use_container_width=True):
            response_data = {'rating': value, 'follow_up': follow_up}
            self._save_response(q_id, response_data, question)
            self._advance_question()
            st.rerun()

    def _advance_question(self):
        """Move to next question"""
        st.session_state.current_question += 1

    def _go_back(self):
        """Go back one question"""
        if st.session_state.current_question > 1:
            st.session_state.current_question -= 1
            if st.session_state.assessment_responses:
                last_key = max(st.session_state.assessment_responses.keys())
                del st.session_state.assessment_responses[last_key]
                if last_key in st.session_state.intensity_responses:
                    del st.session_state.intensity_responses[last_key]

    # ---- Completion & Results ----
    def _complete_assessment(self):
        """Complete the assessment and prepare results"""
        st.session_state.assessment_completed = True
        
        # Analyze algorithmical divide if digital native
        digital_analysis = None
        if st.session_state.is_digital_native:
            digital_analysis = self._analyze_digital_despair_indicators(st.session_state.assessment_responses)
            if digital_analysis:
                st.session_state.digital_despair_score = digital_analysis['digital_despair_score']
                st.session_state.digital_severity = digital_analysis['severity_level']
        
        # Determine dominant pattern
        dominant_pattern = None
        if st.session_state.pattern_scores:
            dominant_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
        
        # Compile results
        st.session_state.assessment_results = {
            'pattern_scores': dict(st.session_state.pattern_scores),
            'dominant_pattern': dominant_pattern,
            'triggered_patterns': list(st.session_state.triggered_patterns),
            'risk_flags': st.session_state.risk_flags,
            'completion_timestamp': datetime.now().isoformat(),
            'total_questions_answered': len(st.session_state.assessment_responses),
            'adaptive_paths_triggered': st.session_state.adaptive_paths,
            'intensity_data': dict(st.session_state.intensity_responses),
            'trigger_chain': dict(st.session_state.trigger_chain),
            'phase_completion': dict(st.session_state.phase_progress),
            'is_digital_native': st.session_state.is_digital_native,
            'digital_despair_analysis': digital_analysis,
            'completion_rate': len(st.session_state.assessment_responses) / self._estimate_total_questions() if self._estimate_total_questions() > 0 else 1.0
        }
        st.rerun()

    # ---- Rendering Questionnaire Functions ----
    def render(self):
        apply_clinical_styles()
        self._render_header()
        
        if not st.session_state.contact_provided:
            if not st.session_state.assessment_completed:
                self._render_current_question()
            else:
                self._render_contact_form()
        else:
            self._render_results()

    def _render_header(self):
        if not st.session_state.assessment_completed:
            time_remaining = self._estimate_time_remaining()           
            st.info(f"Understanding **your unique behavioral patterns** is the key to **targeted, effective hypnotherapy** that brings rapid, lasting change. This assessment takes about {time_remaining:.0f} minutes to complete.")
            st.markdown("<h2 style='text-align: center;'>Behavioral pattern assessment</h1>", unsafe_allow_html=True)

    def _render_current_question(self):
        """Render the current question with progress tracking"""
        q_id, question = self._get_next_question()
        
        if q_id is None:
            self._complete_assessment()
            return
        
        if not question:
            st.error("Question configuration error")
            return

        # Progress tracking
        total_questions = self._estimate_total_questions()
        completed = len(st.session_state.assessment_responses)
        progress = completed / total_questions if total_questions > 0 else 0
        time_remaining = self._estimate_time_remaining()

        st.markdown(f"""
        <div class="progress-container">
            <span><strong>Question {completed + 1} of {total_questions}</strong></span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            <span><strong>{int(progress * 100)}%</strong></span>
        </div>
        <div class="time-estimate"> ~ {time_remaining:.0f} minutes remaining</div>
        """, unsafe_allow_html=True)

        # Question display
        st.markdown(f"### {question['text']}")

        # Handle different question types
        q_type = question['type']
        if q_type == 'single_choice':
            self._handle_single_choice(q_id, question)
        elif q_type == 'single_choice_with_intensity':
            self._handle_single_choice_with_intensity(q_id, question)
        elif q_type == 'multi_select_weighted':
            self._handle_multi_select_weighted(q_id, question)
        elif q_type == 'text_completion':
            self._handle_text_completion(q_id, question)
        elif q_type == 'scale_10':
            self._handle_scale_10(q_id, question)

        self._render_navigation(q_id)

    def _render_navigation(self, current_q_id):
        """Render navigation controls"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if len(st.session_state.assessment_responses) > 0:
                if st.button("← Back", key="nav_back", use_container_width=True):
                    self._go_back()
                    st.rerun()        
        with col2:
            answered_count = len(st.session_state.assessment_responses)
            total_count = self._estimate_total_questions()
            st.markdown(f"""
            <div style="text-align: center; padding: 0.25rem; color: #556D7A; font-size: 0.8rem;">
                <strong>{answered_count}/{total_count}</strong> completed
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Only allow skipping after age screening
            if current_q_id > 0:
                if st.button("Skip", key="nav_skip", use_container_width=True):
                    skip_question = {"text": "Skipped", "type": "skip", "phase": "skip"}
                    self._save_response(current_q_id, "Skipped", skip_question)
                    self._advance_question()
                    st.rerun()

    

    # ---- Build calculation and mapping  ----
# ---- Build calculation and mapping  ----

    def _analyze_digital_despair_indicators(self, responses):
        """Analyze responses for digital despair syndrome indicators using config rules"""
        
        # Extract age-based digital native scoring from config
        age_response = responses.get(0, {}).get('response', '')
        age_data = self.age_screening_questions.get(0, {})
        age_options = age_data.get('options', [])
        digital_scoring = age_data.get('digital_native_scoring', [0] * len(age_options))
        
        try:
            age_index = age_options.index(age_response)
            digital_native_score = digital_scoring[age_index]
        except (ValueError, IndexError):
            digital_native_score = 0
        
        # Skip digital analysis for non-digital natives
        if digital_native_score < 2:
            return None
            
        # Calculate component scores using centralized scoring rules
        component_scores = self._calculate_digital_components(responses)
        
        # Calculate composite score
        total_possible = 35  # Maximum across all components
        raw_score = digital_native_score + sum(component_scores.values())
        digital_despair_percentage = (raw_score / total_possible) * 100
        
        # Determine severity using thresholds from config
        severity_data = self._determine_digital_severity(digital_despair_percentage)
        
        return {
            "digital_despair_score": digital_despair_percentage,
            "severity_level": severity_data['level'],
            "clinical_recommendation": severity_data['title'],
            "component_scores": {
                'digital_native_status': digital_native_score,
                **component_scores
            },
            "therapeutic_adaptations_needed": severity_data.get('adaptations', []),
        }

    def _calculate_digital_components(self, responses):
        """Calculate digital component scores using centralized rules"""
        components = {}
        
        # Use DIGITAL_SCORING_RULES from config for each component
        for component, rules in DIGITAL_SCORING_RULES.items():
            if component == 'attention_fragmentation':
                # Handle special case with direct scoring array
                score = self._score_attention_fragmentation(responses, rules)
            else:
                # Handle condition-based scoring
                score = self._score_digital_component(responses, rules)
            
            components[component] = min(rules.get('max_score', 5), score)
        
        return components

    def _score_digital_component(self, responses, rules):
        """Score individual digital component using condition matching"""
        score = 0
        question_ids = rules['question_id'] if isinstance(rules['question_id'], list) else [rules['question_id']]
        
        for q_id in question_ids:
            response_data = responses.get(q_id, {})
            response = response_data.get('response', '')
            intensity = response_data.get('intensity', 1)
            
            # Check conditions for this component
            for condition, condition_score in rules.get('conditions', {}).items():
                if condition.lower() in response.lower():
                    score += condition_score
                    # Apply intensity multiplier if available
                    if intensity > 1:
                        score *= (intensity / 4)
                    break
        
        return score

    def _score_attention_fragmentation(self, responses, rules):
        """Score attention fragmentation using direct option mapping"""
        response = responses.get(rules['question_id'], {}).get('response', '')
        try:
            option_index = rules['options'].index(response)
            return rules['scores'][option_index]
        except (ValueError, IndexError):
            return 0

    def _determine_digital_severity(self, percentage):
        """Determine severity level using thresholds from config"""
        for level, data in sorted(
            self.digital_thresholds.items(),
            key=lambda x: x[1]["threshold"],
            reverse=True
        ):
            if percentage >= data["threshold"]:
                return {'level': level, **data}
        
        return {
            'level': 'MINIMAL',
            'title': 'Traditional approach optimal',
            'adaptations': []
        }

    # ---- Pattern Detection and Scoring ----
    
    def _update_pattern_scores(self, question_id, response, question):
        """Update pattern scores using centralized scoring rules"""
        
        # Handle different scoring types from config
        scoring_handlers = {
            'pattern_triggers': self._handle_pattern_triggers,
            'pattern_mapping': self._handle_pattern_mapping,
            'pattern_keywords': self._handle_pattern_keywords,
            'keywords': self._handle_keywords,
            'weights': self._handle_weighted_patterns
        }
        
        for score_type, handler in scoring_handlers.items():
            if score_type in question:
                handler(question_id, response, question, score_type)

    def _handle_pattern_triggers(self, question_id, response, question, score_type):
        """Handle pattern trigger scoring"""
        if not isinstance(response, str) or 'options' not in question:
            return
            
        try:
            option_index = question['options'].index(response)
            if option_index in question[score_type]:
                patterns = question[score_type][option_index]
                for pattern in patterns:
                    self._add_pattern_score(pattern, 1.0)
        except (ValueError, IndexError):
            pass

    def _handle_pattern_mapping(self, question_id, response, question, score_type):
        """Handle pattern mapping scoring with higher weight"""
        if not isinstance(response, str) or 'options' not in question:
            return
            
        try:
            option_index = question['options'].index(response)
            if option_index in question[score_type]:
                patterns = question[score_type][option_index]
                for pattern in patterns:
                    self._add_pattern_score(pattern, 1.5)
        except (ValueError, IndexError):
            pass

    def _handle_pattern_keywords(self, question_id, response, question, score_type):
        """Handle keyword analysis for text responses"""
        if not isinstance(response, str):
            return
            
        detected_patterns = self._analyze_text_for_patterns(response, question[score_type])
        for pattern in detected_patterns:
            self._add_pattern_score(pattern, 2.0)

    def _handle_keywords(self, question_id, response, question, score_type):
        """Handle general keyword scoring"""
        if not isinstance(response, str):
            return
            
        detected_patterns = self._analyze_text_for_patterns(response, question[score_type])
        for pattern in detected_patterns:
            self._add_pattern_score(pattern, 1.0)

    def _handle_weighted_patterns(self, question_id, response, question, score_type):
        """Handle pattern-specific weighted scoring"""
        pattern_id = question.get('pattern')
        weights = question.get('weights', [])
        
        if not pattern_id or not weights or not isinstance(response, str):
            return
            
        if 'options' in question:
            try:
                option_index = question['options'].index(response)
                if option_index < len(weights):
                    weight = weights[option_index]
                    if weight > 0:
                        self._add_pattern_score(pattern_id, weight)
            except (ValueError, IndexError):
                pass

    def _analyze_text_for_patterns(self, text, keywords_dict):
        """Analyze text response for pattern indicators using config keywords"""
        text_lower = text.lower()
        detected_patterns = set()
        
        for keyword, patterns in keywords_dict.items():
            if keyword in text_lower:
                detected_patterns.update(patterns)
        
        return detected_patterns

    def _add_pattern_score(self, pattern_id, score):
        """Add score to pattern with intensity consideration"""
        current_score = st.session_state.pattern_scores.get(pattern_id, 0)
        st.session_state.pattern_scores[pattern_id] = current_score + score
        
        # Check for adaptive triggers
        self._check_adaptive_triggers(pattern_id, current_score + score)

    def _check_adaptive_triggers(self, pattern_id, score):
        """Check if pattern score triggers adaptive questioning"""
        if score >= 3.0 and pattern_id not in st.session_state.triggered_patterns:
            st.session_state.triggered_patterns.add(pattern_id)
            st.session_state.adaptive_paths.append(f"pattern_{pattern_id}")

    # ---- Clinical Analysis Methods (using config data) ----
    
    def _extract_clinical_insights(self):
        """Extract clinical insights using pattern descriptions from config"""
        pattern_scores = st.session_state.pattern_scores
        if not pattern_scores:
            return self._get_default_clinical_insights()
            
        # Get dominant pattern insights from config
        dominant_pattern_id = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_descriptions.get(dominant_pattern_id, {})
        
        return {
            'core_limiting_belief': pattern_info.get('core_belief', 'Requires session exploration'),
            'hidden_benefits': self._extract_hidden_loyalties(pattern_info),
            'systemic_resistance': pattern_info.get('pattern_resistance', 'Standard resistance expected'),
            'identity_conflict': pattern_info.get('identity_conflict', 'Identity evolution requires navigation'),
            'intervention_strategy': pattern_info.get('intervention_strategy', 'Collaborative approach'),
            'intervention_keywords': self._extract_intervention_keywords(pattern_info),
            'avoid_language': ['Pressure', 'criticism', 'commands'],
            'resistance_points': [pattern_info.get('pattern_resistance', 'Standard change resistance')]
        }

    def _extract_hidden_loyalties(self, pattern_info):
        """Extract hidden loyalties from pattern configuration"""
        loyalties = pattern_info.get('hidden_loyalties', [])
        if loyalties:
            return '; '.join(loyalties[:2])  # First two loyalties
        return 'Emotional protection and familiar identity'

    def _extract_intervention_keywords(self, pattern_info):
        """Extract intervention approach from pattern configuration"""
        strategy = pattern_info.get('intervention_strategy', '')
        if 'collaborative' in strategy.lower():
            return 'Collaborative, gentle, permissive'
        elif 'permission' in strategy.lower():
            return 'Permission-based, safety-focused'
        elif 'gradual' in strategy.lower():
            return 'Gradual, trust-building, transparent'
        else:
            return 'Adaptive, person-centered'

    def _get_default_clinical_insights(self):
        """Provide default insights when pattern analysis is incomplete"""
        return {
            'core_limiting_belief': 'Assessment incomplete - requires full evaluation',
            'hidden_benefits': 'Pattern provides emotional protection and familiar identity',
            'systemic_resistance': 'To be determined in clinical analysis',
            'identity_conflict': 'Identity evolution assessment needed',
            'intervention_strategy': 'Collaborative exploration required',
            'intervention_keywords': 'Gentle, curious, supportive',
            'avoid_language': ['Pressure', 'urgency', 'criticism'],
            'resistance_points': ['Assessment completion needed']
        }

    def _generate_session_plan(self, pattern_scores, clinical_insights):
        """Generate session planning using pattern-specific focuses from config"""
        if not pattern_scores:
            return self._get_default_session_plan()
            
        dominant_pattern_id = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_descriptions.get(dominant_pattern_id, {})
        
        return {
            'session_1_focus': pattern_info.get('session_1_focuses', 'Comprehensive pattern analysis and rapport building'),
            'session_2_target': pattern_info.get('session_2_focuses', 'Core transformation and positive programming'),
            'session_3_need': self._determine_session_3_need(pattern_scores)
        }

    def _determine_session_3_need(self, pattern_scores):
        """Determine if third session is needed based on complexity"""
        pattern_count = len(pattern_scores)
        max_score = max(pattern_scores.values()) if pattern_scores else 0
        
        if pattern_count >= 4 or max_score >= 7:
            return "Recommended for complex pattern integration"
        elif pattern_count >= 2 or max_score >= 5:
            return "Optional reinforcement session"
        else:
            return "Unlikely to be needed"

    def _get_default_session_plan(self):
        """Default session plan when pattern analysis incomplete"""
        return {
            'session_1_focus': 'Complete assessment and initial rapport building',
            'session_2_target': 'Pattern exploration and foundational work',
            'session_3_need': 'To be determined based on response'
        }

    # ---- Success Rate Calculation (using config factors) ----
    
    def _calculate_comprehensive_success_rate(self):
        """Calculate success rate using factors from assessment and config"""
        base_rate = 85
        
        # Pattern complexity factor
        pattern_count = len(st.session_state.pattern_scores)
        if pattern_count >= 5:
            base_rate -= 5
        elif pattern_count >= 3:
            base_rate -= 2
        
        # Digital native advantage (they respond well to this approach)
        if st.session_state.get('is_digital_native', False):
            base_rate += 5
        
        # Readiness factor from responses
        readiness_boost = self._calculate_readiness_boost()
        
        # Digital severity adjustment
        digital_analysis = st.session_state.get('assessment_results', {}).get('digital_despair_analysis')
        if digital_analysis:
            severity = digital_analysis.get('severity_level', 'MINIMAL')
            if severity in ['SEVERE', 'MODERATE']:
                base_rate += 3  # Specialized approach advantage
        
        final_rate = min(95, max(70, base_rate + readiness_boost))
        return final_rate

    def _calculate_readiness_boost(self):
        """Calculate motivation boost from response analysis"""
        responses = st.session_state.get('assessment_responses', {})
        
        # Check for high motivation keywords using config
        motivation_keywords = PatternDefinitions.BELIEF_HINTS.keys()  # Use config keywords
        motivation_boost = 0
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                response_lower = response.lower()
                if any(keyword in response_lower for keyword in ['ready', 'desperate', 'tired', 'enough']):
                    motivation_boost = 3
                    break
                elif any(keyword in response_lower for keyword in motivation_keywords):
                    motivation_boost = 2
                    break
        
        # Check readiness scale responses
        for response_data in responses.values():
            if isinstance(response_data.get('response'), dict):
                rating = response_data['response'].get('rating', 0)
                if rating >= 8:
                    motivation_boost = max(motivation_boost, 3)
                elif rating >= 6:
                    motivation_boost = max(motivation_boost, 2)
        
        return motivation_boost

    # ---- Comprehensive Clinical Template (enhanced with config) ----
    
    def _format_comprehensive_clinical_template(self):
        """Format clinical template using config data and centralized analysis"""
        # Get analyzed data
        clinical_insights = self._extract_clinical_insights()
        pattern_scores = st.session_state.pattern_scores
        session_plan = self._generate_session_plan(pattern_scores, clinical_insights)
        
        # Build pattern analysis section using config
        pattern_analysis = self._build_pattern_analysis_section(pattern_scores)
        
        # Build base template
        template = f"""
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║          Enhanced Behavioral Pattern Assessment              ║
╚══════════════════════════════════════════════════════════════╝

{pattern_analysis}

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: {clinical_insights.get('core_limiting_belief')}
Hidden Benefits: {clinical_insights.get('hidden_benefits')}
Systemic Resistance: {clinical_insights.get('systemic_resistance')}
Identity Conflict: {clinical_insights.get('identity_conflict')}
Intervention Strategy: {clinical_insights.get('intervention_strategy')}

**CHANGE READINESS:**
Readiness Score: {self._extract_readiness_score()}/10
Motivation Level: {self._determine_motivation_level()}
Success Probability: {self._calculate_comprehensive_success_rate()}%

**SESSION PLANNING:**
Session 1 Focus: {session_plan.get('session_1_focus')}
Session 2 Target: {session_plan.get('session_2_target')}
Session 3 Need: {session_plan.get('session_3_need')}

**THERAPEUTIC APPROACH:**
Intervention Keywords: {clinical_insights.get('intervention_keywords')}
Avoid Language: {', '.join(clinical_insights.get('avoid_language', []))}
Predicted Resistance: {clinical_insights.get('resistance_points', ['Standard patterns'])[0]}
"""

        # Add digital analysis if applicable
        if st.session_state.is_digital_native:
            digital_section = self._build_digital_analysis_section()
            template += digital_section
        
        # Add clinical notes
        template += self._build_clinical_notes_section()
        
        return template

    def _build_pattern_analysis_section(self, pattern_scores):
        """Build pattern analysis using config pattern descriptions"""
        if not pattern_scores:
            return "**PATTERN ANALYSIS:** Assessment incomplete - full evaluation needed"
            
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        section = "**TRADITIONAL PATTERN ANALYSIS:**\n"
        
        for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
            pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
            role = ["Dominant", "Primary", "Secondary"][i]
            section += f"{role} Pattern: {pattern_name} (Score: {score:.1f}/10)\n"
            
            # Add pattern details from config if available
            pattern_info = self.pattern_descriptions.get(pattern_id, {})
            if pattern_info:
                section += f"  • Mechanism: {pattern_info.get('pattern_mechanism', 'Analysis needed')}\n"
                section += f"  • Core Impact: {pattern_info.get('impact', 'Assessment needed')}\n"
        
        return section

    def _build_digital_analysis_section(self):
        """Build digital analysis section using config thresholds"""
        digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
        if not digital_analysis:
            return ""
            
        severity = digital_analysis['severity_level']
        score = digital_analysis['digital_despair_score']
        adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
        
        section = f"""

╔══════════════════════════════════════════════════════════════╗
║               DIGITAL DESPAIR SYNDROME ANALYSIS             ║
╚══════════════════════════════════════════════════════════════╝

**SYNDROME ASSESSMENT:**
Digital Conditioning Score: {score:.1f}% ({severity} severity)
Clinical Recommendation: {digital_analysis['clinical_recommendation']}

**SYNDROME COMPONENTS:**"""

        # Add component breakdown
        components = digital_analysis['component_scores']
        component_names = {
            'digital_native_status': 'Digital Native Conditioning',
            'reality_dissociation': 'Online vs Offline Authenticity Gap',
            'binary_success_pressure': 'Extraordinary Achievement Pressure',
            'ironic_detachment': 'Emotional Protection Through Cynicism',
            'algorithmic_dependency': 'Social Media Emotional Regulation',
            'nihilistic_worldview': 'Hopelessness and Meaning Crisis',
            'hope_avoidance': 'Resistance to Optimism',
            'attention_fragmentation': 'Digital Attention Conditioning'
        }
        
        for comp, score in components.items():
            name = component_names.get(comp, comp)
            level = "HIGH" if score >= 4 else "MEDIUM" if score >= 2 else "LOW"
            section += f"\n• {name}: {level} ({score:.1f}/5)"
        
        # Add adaptations from config
        section += f"\n\n**REQUIRED THERAPEUTIC ADAPTATIONS:**\n"
        severity_flag = "🚨 SPECIALIZED INTERVENTION REQUIRED" if severity in ['SEVERE', 'MODERATE'] else "✅ STANDARD APPROACH WITH MODIFICATIONS"
        section += severity_flag
        
        for i, adaptation in enumerate(adaptations[:5], 1):
            section += f"\n{i}. {adaptation}"
        
        return section

    def _build_clinical_notes_section(self):
        """Build clinical notes section"""
        digital_note = ""
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                digital_note = "This assessment reveals a digital-native psychology requiring specialized intervention approaches. Traditional methods may fail without proper adaptations."
            else:
                digital_note = "Digital-native adaptations recommended but standard framework applicable."
        else:
            digital_note = "Traditional hypnotherapy approach optimal for this client profile."
        
        return f"""

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL NOTES                          ║
╚══════════════════════════════════════════════════════════════╝

{digital_note}

Pattern constellation suggests {self._get_complexity_assessment()} intervention approach.
Success probability enhanced by specialized assessment completion and clear motivation indicators.
"""

    def _get_complexity_assessment(self):
        """Assess complexity based on pattern count and scores"""
        pattern_count = len(st.session_state.pattern_scores)
        if pattern_count >= 4:
            return "complex multi-pattern"
        elif pattern_count >= 2:
            return "standard multi-pattern"
        else:
            return "focused single-pattern"

    def _extract_readiness_score(self):
        """Extract readiness score from responses"""
        for response_data in st.session_state.assessment_responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                return response_data['response']['rating']
        return 7  # Default moderate readiness

    def _determine_motivation_level(self):
        """Determine motivation level based on readiness and responses"""
        readiness_score = self._extract_readiness_score()
        if readiness_score >= 8:
            return "HIGH"
        elif readiness_score >= 6:
            return "MODERATE" 
        else:
            return "REQUIRES BUILDING"

    # ---- Helper Methods for User Agent and Utilities ----
    
    def _get_user_agent(self):
        """Get user agent information for assessment data"""
        try:
            return st.context.headers.get("User-Agent", "Unknown")
        except:
            return "Unknown"

    # ---- Preview and Results Generation (using config) ----
    
    def _extract_preview_insights(self, assessment_data):
        """Extract rich insights from assessment data for compelling preview using config"""
        
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        digital_analysis = assessment_data.get('digital_despair_analysis')
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        # Provide defaults if no pattern data
        if not pattern_scores:
            return self._get_default_preview_insights()
        
        # Pattern analysis using config
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        dominant_pattern_id, dominant_score = sorted_patterns[0]
        dominant_pattern_name = self.patterns.get(dominant_pattern_id, "Unknown")
        pattern_count = len(pattern_scores)
        
        # Get pattern description from config
        pattern_info = self.pattern_descriptions.get(dominant_pattern_id, {})
        
        # Build insights using config data
        intensity_description = self._get_intensity_description(dominant_score)
        complexity_description = self._get_complexity_description(pattern_count)
        success_factors = self._calculate_success_factors(pattern_count, assessment_data)
        success_rate = self._calculate_comprehensive_success_rate()
        
        # Digital summary from config
        digital_summary = self._build_digital_summary(is_digital_native, digital_analysis)
        
        # Key insight from config pattern descriptions
        key_insight = pattern_info.get('insights_map', 'Pattern analysis reveals protective mechanisms that need updating')
        if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
            key_insight += " - compounded by digital conditioning requiring specialized intervention"
        
        return {
            'dominant_pattern_name': dominant_pattern_name,
            'intensity_description': intensity_description,
            'complexity_description': complexity_description,
            'pattern_count': pattern_count,
            'success_rate': success_rate,
            'success_factors': success_factors,
            'digital_summary': digital_summary,
            'key_insight': key_insight,
            'trigger_sequence': self._extract_trigger_sequence_from_config(responses, pattern_info),
            'cost_preview': self._calculate_cost_preview_from_config(pattern_count, dominant_score),
            'pattern_interactions': [self.patterns.get(pid, f"Pattern {pid}") for pid, _ in sorted_patterns[:3]],
            'session_plan': self._generate_session_preview_from_config(dominant_pattern_id, pattern_count, digital_analysis),
            'immediate_techniques': self._get_immediate_techniques_from_config(dominant_pattern_id),
            'digital_insights': self._extract_digital_insights_from_config(digital_analysis, responses) if digital_analysis else None,
            'clarity_score': min(10, max(1, int(assessment_data.get('completion_rate', 0) * 10))),
            'readiness_score': self._extract_readiness_score(),
            'match_score': 9 if is_digital_native else 8
        }

    def _get_default_preview_insights(self):
        """Provide default preview insights when assessment incomplete"""
        return {
            'dominant_pattern_name': 'Assessment incomplete - complete full assessment for analysis',
            'intensity_description': 'Assessment needed',
            'complexity_description': 'Analysis pending',
            'pattern_count': 0,
            'success_rate': 85,
            'success_factors': 'assessment completion needed',
            'digital_summary': '',
            'key_insight': 'Complete assessment needed for personalized insights',
            'trigger_sequence': None,
            'cost_preview': {
                'weekly_hours': 8,
                'annual_cost': '฿331,200',
                'relationship_impact': 'Assessment needed for analysis'
            },
            'pattern_interactions': ['Assessment incomplete'],
            'session_plan': {
                'session_1_preview': 'Comprehensive assessment and rapport building',
                'session_2_preview': 'Core transformation and programming',
                'results_timeline': '2-4 weeks',
                'optimization_factor': 'Assessment completion needed'
            },
            'immediate_techniques': {
                'technique_1': {'name': 'Mindful Pause', 'description': 'Take 3 deep breaths before reacting'},
                'technique_2': {'name': 'Choice Point', 'description': 'Ask: Is this serving me?'}
            },
            'digital_insights': None,
            'clarity_score': 1,
            'readiness_score': 5,
            'match_score': 8
        }

    def _get_intensity_description(self, score):
        """Get intensity description based on score"""
        if score >= 6:
            return "High intensity - requires immediate intervention"
        elif score >= 4:
            return "Moderate intensity - well-suited for rapid transformation"
        elif score >= 2:
            return "Emerging pattern - excellent prognosis for quick resolution"
        else:
            return "Mild pattern - high success probability"

    def _get_complexity_description(self, pattern_count):
        """Get complexity description based on pattern count"""
        if pattern_count >= 5:
            return "Complex multi-pattern system"
        elif pattern_count >= 3:
            return "Moderate complexity with clear intervention points"
        elif pattern_count >= 2:
            return "Standard complexity level"
        else:
            return "Single-pattern focus"

    def _calculate_success_factors(self, pattern_count, assessment_data):
        """Calculate success factors string"""
        factors = []
        
        if pattern_count <= 3:
            factors.append("focused pattern constellation")
        
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.9:
            factors.append("high assessment engagement")
        
        if assessment_data.get('is_digital_native') and assessment_data.get('digital_despair_analysis'):
            factors.append("specialized approach match")
        
        readiness_score = self._extract_readiness_score()
        if readiness_score >= 8:
            factors.append("high motivation level")
        
        return ", ".join(factors) if factors else "strong assessment completion"

    def _build_digital_summary(self, is_digital_native, digital_analysis):
        """Build digital summary using config thresholds"""
        if not is_digital_native or not digital_analysis:
            return ""
        
        severity = digital_analysis['severity_level']
        score = digital_analysis['digital_despair_score']
        return f"<strong>Digital conditioning:</strong> {score:.0f}% ({severity}) - specialized protocol activated"

    def _extract_trigger_sequence_from_config(self, responses, pattern_info):
        """Extract trigger sequence using pattern-specific insights from config"""
        sequence = {}
        
        # Use standard extraction method but enhance with pattern-specific insights
        basic_sequence = self._extract_trigger_sequence_basic(responses)
        
        # Add pattern-specific mechanism from config
        if pattern_info:
            sequence = {
                **basic_sequence,
                'pattern_mechanism': pattern_info.get('pattern_mechanism', 'Protective response pattern')
            }
        else:
            sequence = basic_sequence
        
        return sequence if any(sequence.values()) else None

    def _extract_trigger_sequence_basic(self, responses):
        """Basic trigger sequence extraction"""
        sequence = {}
        
        for response_data in responses.values():
            question_text = response_data.get('question_text', '').lower()
            response = response_data.get('response', '')
            
            if 'happening in the 30 seconds' in question_text and isinstance(response, str):
                sequence['trigger'] = response[:80] + "..." if len(response) > 80 else response
            elif 'physical sensation' in question_text and isinstance(response, str):
                sequence['physical'] = response
            elif 'thought automatically appears' in question_text and isinstance(response, str):
                sequence['thought'] = response[:60] + "..." if len(response) > 60 else response
            elif 'typically feel' in question_text and isinstance(response, (str, dict)):
                if isinstance(response, dict):
                    sequence['emotion'] = "Multiple emotions detected"
                else:
                    sequence['emotion'] = response
            elif 'you typically:' in question_text and isinstance(response, str):
                sequence['behavior'] = response
        
        return sequence

    def _calculate_cost_preview_from_config(self, pattern_count, dominant_score):
        """Calculate cost preview with config-based factors"""
        base_weekly_hours = 6 + (pattern_count * 2) + (dominant_score * 0.5)
        weekly_hours = min(int(base_weekly_hours), 25)
        
        hourly_value = 800  # THB per hour
        annual_cost = f"฿{weekly_hours * 52 * hourly_value:,}"
        
        if pattern_count >= 4:
            relationship_impact = "Significant strain on close relationships due to pattern complexity"
        elif pattern_count >= 2:
            relationship_impact = "Moderate impact on relationship depth and authenticity"
        else:
            relationship_impact = "Manageable impact with clear improvement potential"
        
        return {
            'weekly_hours': weekly_hours,
            'annual_cost': annual_cost,
            'relationship_impact': relationship_impact
        }

    def _generate_session_preview_from_config(self, dominant_pattern_id, pattern_count, digital_analysis):
        """Generate session preview using config pattern data"""
        pattern_info = self.pattern_descriptions.get(dominant_pattern_id, {})
        
        session_1_preview = pattern_info.get('session_1_focuses', 'Comprehensive pattern analysis and foundational work')
        session_2_preview = pattern_info.get('session_2_focuses', 'Core transformation and positive programming')
        
        # Timeline based on complexity
        if pattern_count >= 4 or (digital_analysis and digital_analysis['severity_level'] == 'SEVERE'):
            results_timeline = "48-72 hours for initial shifts, 2-3 weeks for full integration"
            optimization_factor = "Session 3 recommended for optimal reinforcement"
        elif pattern_count >= 2:
            results_timeline = "24-48 hours for noticeable changes, 1-2 weeks for stabilization"
            optimization_factor = "Standard 2-session protocol optimal"
        else:
            results_timeline = "24-48 hours for significant shifts, 1 week for complete integration"
            optimization_factor = "Accelerated results likely due to single-pattern focus"
        
        return {
            'session_1_preview': session_1_preview,
            'session_2_preview': session_2_preview,
            'results_timeline': results_timeline,
            'optimization_factor': optimization_factor
        }

    def _get_immediate_techniques_from_config(self, dominant_pattern_id):
        """Get immediate techniques based on pattern using config insights"""
        # Use pattern-specific what_you_notice from config for technique development
        pattern_info = self.pattern_descriptions.get(dominant_pattern_id, {})
        pattern_name = self.patterns.get(dominant_pattern_id, f"Pattern {dominant_pattern_id}")
        
        technique_map = {
            1: {  # Unhappiness Culture
                'technique_1': {
                    'name': 'Happiness Permission Check',
                    'description': 'Before dismissing good feelings, pause and ask: "What would I lose by enjoying this for 5 more minutes?" Usually, the answer reveals the pattern isn\'t protecting anything real.'
                },
                'technique_2': {
                    'name': 'Joy Anchoring Breath',
                    'description': 'When happiness deflection starts, take 3 deep breaths while saying "I deserve this good feeling" - interrupt the automatic deflection.'
                }
            },
            2: {  # Power Struggles
                'technique_1': {
                    'name': 'Combat Mode Recognition',
                    'description': 'Notice when your body activates during disagreements. Pause and ask: "Is this actually a battle or an opportunity to understand?"'
                },
                'technique_2': {
                    'name': 'Collaboration Reset',
                    'description': 'When you feel the urge to "win," try saying: "Help me understand your perspective" instead of defending your position.'
                }
            },
            3: {  # Systematic Mistrust
                'technique_1': {
                    'name': 'Trust Calibration Check',
                    'description': 'When suspicion arises, ask: "What evidence do I actually have?" vs "What story is my protective mind creating?"'
                },
                'technique_2': {
                    'name': 'Authentic Risk Taking',
                    'description': 'Practice sharing one small authentic thing daily - start building evidence that being real is safe.'
                }
            }
        }
        
        default_techniques = {
            'technique_1': {
                'name': f'{pattern_name} Pattern Interrupt',
                'description': 'When you notice your pattern activating, pause for 10 seconds and ask: "Is this response serving me right now?"'
            },
            'technique_2': {
                'name': 'Conscious Choice Point',
                'description': 'Before your automatic response, create a 3-second gap to choose a different response that aligns with who you want to be.'
            }
        }
        
        return technique_map.get(dominant_pattern_id, default_techniques)

    def _extract_digital_insights_from_config(self, digital_analysis, responses):
        """Extract digital insights using config component analysis"""
        if not digital_analysis:
            return None
            
        severity = digital_analysis['severity_level']
        components = digital_analysis['component_scores']
        adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
        
        # Attention pattern analysis
        attention_score = components.get('attention_fragmentation', 0)
        if attention_score >= 4:
            attention_pattern = "Severely fragmented - requires 15-minute session segments"
        elif attention_score >= 2:
            attention_pattern = "Moderately fragmented - benefits from varied pacing"
        else:
            attention_pattern = "Standard attention capacity with minor digital impact"
        
        # Validation source analysis
        algorithmic_score = components.get('algorithmic_dependency', 0)
        if algorithmic_score >= 3:
            validation_source = "Primarily digital/online validation - real-world confidence needs rebuilding"
        elif algorithmic_score >= 2:
            validation_source = "Mixed digital/offline validation - balance needs optimization"
        else:
            validation_source = "Healthy validation sources with minor digital influence"
        
        # Adaptation needed from config
        adaptation_map = {
            'SEVERE': "Complete protocol redesign with anti-authority language and ironic armor dissolution",
            'MODERATE': "Modified approach with digital-aware techniques and pacing adjustments",
            'MILD': "Standard approach enhanced with digital competency integration"
        }
        
        return {
            'attention_pattern': attention_pattern,
            'validation_source': validation_source,
            'adaptation_needed': adaptation_map.get(severity, "Standard approach optimal"),
            'severity_level': severity,
            'component_breakdown': components,
            'required_adaptations': adaptations[:3]  # Top 3 adaptations
        }

    # ---- Additional Rendering Support Methods ----
    
    def _render_aha_moment_bridge(self):
        """Render aha moment bridge using Streamlit components"""
        hidden_mechanisms = self._identify_hidden_mechanisms()
        future_prediction = self._generate_future_prediction()
        
        st.markdown("**The hidden layer**")
        
        with st.container():
            st.markdown("**Protective mechanisms detected:**")
            st.markdown(f"Your assessment reveals {len(hidden_mechanisms)} protective mechanisms your mind uses that we haven't fully explored yet. These unconscious strategies are actually trying to help you, but they're creating the very problems you want to solve.")
            
            st.markdown("**The paradox:**")
            st.markdown("Why your logical mind keeps you stuck (and it's not what you think): Your conscious efforts to change are actually reinforcing the pattern at a deeper level.")
            
            st.warning(f"**Pattern trajectory:** {future_prediction}")
            
            st.caption("This free analysis covers your behavioral patterns. Your complete clinical profile reveals the deeper psychological architecture driving these patterns.")

    def _identify_hidden_mechanisms(self):
        """Identify hidden protective mechanisms using config data"""
        mechanisms = []
        
        if st.session_state.pattern_scores:
            sorted_patterns = sorted(st.session_state.pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            for pattern_id, score in sorted_patterns[:3]:
                if score >= 3:
                    pattern_info = self.pattern_descriptions.get(pattern_id, {})
                    mechanism = pattern_info.get('pattern_mechanism', 'Protective response pattern')
                    mechanisms.append(mechanism)
        
        return mechanisms

    def _generate_future_prediction(self):
        """Generate pattern trajectory prediction using config insights"""
        pattern_count = len(st.session_state.pattern_scores)
        
        if pattern_count >= 4:
            return "Based on this pattern constellation, without intervention these protective mechanisms typically strengthen over time, creating increasing life restriction and relationship difficulties."
        elif pattern_count >= 2:
            return "These patterns tend to become more automatic and entrenched without conscious intervention, gradually limiting life satisfaction and authentic relationships."
        else:
            return "This pattern will likely solidify further without intervention, making future change more challenging."

    def _render_pattern_cost_analysis(self):
        """Render pattern cost analysis using Streamlit components"""
        future_vision = self._extract_future_vision()
        current_cost = self._calculate_pattern_cost()
        
        st.markdown("**The hidden cost of your current patterns**")
        
        st.warning(f"**Weekly impact:** This pattern sequence is likely costing you approximately **{current_cost['hours']} hours of peace and productivity per week**")
        
        st.markdown("**Compound cost over time:** Without intervention, these patterns typically solidify further, making change more difficult and the impact more severe.")
        
        if future_vision:
            st.info(f"**Your vision:** You mentioned wanting to {future_vision}. These patterns are the primary barrier standing between you and that reality.")

    def _extract_future_vision(self):
        """Extract user's future vision from their responses"""
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and any(keyword in response_data.get('question_text', '').lower() 
                                               for keyword in ['completely resolved', 'different about your daily life', 'first thing you\'d do']):
                return response[:100] + "..." if len(response) > 100 else response
        return None

    def _calculate_pattern_cost(self):
        """Calculate estimated weekly cost of patterns"""
        pattern_count = len(st.session_state.pattern_scores)
        intensity_avg = sum(st.session_state.pattern_scores.values()) / len(st.session_state.pattern_scores) if st.session_state.pattern_scores else 0
        
        base_hours = 8
        pattern_multiplier = min(pattern_count * 1.5, 10)
        intensity_multiplier = min(intensity_avg / 5, 2)
        
        total_hours = int(base_hours + pattern_multiplier + intensity_multiplier)
        
        return {'hours': total_hours}

    def _extract_core_belief_hint(self):
        """Extract hint about core limiting belief using config"""
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                for indicator, belief in PatternDefinitions.BELIEF_HINTS.items():
                    if indicator in response.lower():
                        return belief
        
        return "Deep exploration needed in clinical analysis"

    def _predict_specific_resistance(self):
        """Predict specific resistance point using config"""
        if st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
            pattern_info = self.pattern_descriptions.get(top_pattern, {})
            return pattern_info.get('pattern_resistance', 'Standard change resistance')
        
        return "To be determined in clinical analysis"

    def _calculate_pattern_rarity(self, total_patterns=None):
        """Calculate pattern combination rarity percentage"""
        if total_patterns is None:
            total_patterns = len(st.session_state.pattern_scores)
        
        if total_patterns >= 5:
            return 8
        elif total_patterns >= 4:
            return 12
        elif total_patterns >= 3:
            return 18
        elif total_patterns >= 2:
            return 25
        else:
            return 35

    def _render_empowerment_section(self):
        """Render empowerment section using Streamlit components"""
        readiness_indicators = self._extract_readiness_indicators()
        user_insights = self._extract_user_insights()
        
        st.markdown("**You have everything needed for rapid transformation**")
        
        st.markdown("**Your transformation readiness indicators:**")
        st.markdown(readiness_indicators, unsafe_allow_html=True)
        
        st.success("**Key insight:** Your pattern recognition ability is already strong - that's 60% of the transformation work already complete.")
        
        if user_insights:
            st.markdown(user_insights, unsafe_allow_html=True)

    def _extract_readiness_indicators(self):
        """Extract readiness indicators from responses for Streamlit display"""
        indicators = []
        
        completion_rate = st.session_state.assessment_results.get('completion_rate', 0)
        if completion_rate >= 0.9:
            indicators.append(f"- High assessment engagement - completed {completion_rate * 100:.0f}% of questions")
        
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            if 'ready' in question_text.lower() and isinstance(response, dict) and response.get('rating', 0) >= 7:
                indicators.append(f"- High readiness score: {response['rating']}/10")
            
            if isinstance(response, str):
                if any(phrase in response.lower() for phrase in ['want to change', 'ready for', 'tired of']):
                    indicators.append("- Clear motivation expressed in responses")
                
                if len(response) > 50:
                    indicators.append("- Thoughtful, detailed responses showing self-reflection")
        
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
                indicators.append("- Pattern recognition despite digital conditioning shows strong awareness")
        
        return "\n".join(indicators) if indicators else "- Completion of comprehensive assessment shows readiness to explore change"

    def _extract_user_insights(self):
        """Extract user insights for display"""
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            if 'different about your daily life' in question_text and isinstance(response, str) and len(response) > 30:
                return f'**Your transformation vision:** "{response[:150]}{"..." if len(response) > 150 else ""}"'
        
        return None

    def _render_transformation_roadmap(self):
        """Render transformation roadmap using Streamlit components"""
        st.markdown("**Your transformation roadmap**")
        
        pattern_count = len(st.session_state.pattern_scores)
        digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
        digital_severity = digital_analysis.get('severity_level', 'MINIMAL') if digital_analysis else 'MINIMAL'
        
        if pattern_count >= 5 or digital_severity in ['SEVERE', 'MODERATE']:
            sessions = "2-3 sessions"
            timeline = "3-4 weeks"
            session_3_prob = "40-60%"
        elif pattern_count >= 3:
            sessions = "2 sessions"
            timeline = "2-3 weeks" 
            session_3_prob = "20-30%"
        else:
            sessions = "2 sessions"
            timeline = "2 weeks"
            session_3_prob = "10-15%"
        
        st.markdown(f"**Estimated transformation timeline:** {timeline}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total sessions", sessions)
        with col2:
            st.metric("Timeline", f"{timeline} for complete transformation")
        
        phases = [
            {
                "title": "Pattern analysis & rapport building",
                "duration": "Session 1 (90 minutes)",
                "description": "Complete behavioral sequence mapping, core belief identification, and initial positive programming",
                "outcome": "Clear understanding of your unique patterns and therapeutic alliance established"
            },
            {
                "title": "Core transformation & programming",
                "duration": "Session 2 (90 minutes)", 
                "description": "Direct pattern interruption, new empowering response installation, and future scenario testing",
                "outcome": "Fundamental shifts in automatic responses and new positive patterns anchored"
            },
            {
                "title": "Integration & mastery",
                "duration": f"Session 3 if needed ({session_3_prob} probability)",
                "description": "Pattern reinforcement, fine-tuning, and long-term stability anchoring",
                "outcome": "Complete integration and sustained transformation confidence"
            }
        ]
        
        for i, phase in enumerate(phases):
            with st.container():
                st.markdown(f"**{i+1}. {phase['title']}**")
                st.markdown(f"*{phase['duration']}*")
                st.markdown(phase['description'])
                st.success(f"**Expected outcome:** {phase['outcome']}")
                if i < len(phases) - 1:
                    st.markdown("---")

    def _render_simple_analysis_preview(self):
        """Render simple analysis preview when paywall not available"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            dominant_pattern = self.patterns.get(sorted_patterns[0][0], "Unknown")
            
            st.markdown(f"""
            <div class="insight-card">
                <h4 style="color: #273548;">Clinical analysis preview</h4>
                <p style="color: #556D7A;">
                    <strong>Primary focus:</strong> {dominant_pattern} pattern transformation<br>
                    <strong>Complexity level:</strong> {"High" if len(sorted_patterns) >= 4 else "Moderate" if len(sorted_patterns) >= 2 else "Standard"}<br>
                    <strong>Approach:</strong> {"Specialized digital-native protocol" if st.session_state.is_digital_native else "Standard clinical hypnotherapy"}
                </p>
            </div>
            """, unsafe_allow_html=True)

    def _render_enhanced_paywall_preview(self):
        """Render enhanced paywall preview using Streamlit components"""
        core_belief_hint = self._extract_core_belief_hint()
        resistance_preview = self._predict_specific_resistance()
        rarity_stat = self._calculate_pattern_rarity()
        
        st.markdown("**Unlock your complete psychological blueprint**")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Deep psychology", "Intervention design", "Sequence interruption", "Success optimization"])
        
        with tab1:
            st.markdown("**Deep psychology profile**")
            st.markdown("Core limiting beliefs, secondary gains, identity threats, and systemic resistance mapping")
            st.info(f'**Preview:** Your assessment suggests the core belief "{core_belief_hint}"')
        
        with tab2:
            st.markdown("**Neuroplasticity intervention design**")
            st.markdown("Session-by-session blueprints with exact hypnotic language patterns for your brain type")
            st.info(f"**Preview:** Likely resistance point - {resistance_preview}")
        
        with tab3:
            st.markdown("**Behavioral sequence interruption**")
            st.markdown("Early warning system and circuit breakers specific to your trigger patterns")
        
        with tab4:
            st.markdown("**Success optimization plan**")
            st.markdown("Personalized timeline and probability enhancers to increase success from 85% to 95%+")
        
        st.warning(f"**Pattern rarity:** Only {rarity_stat}% of people show this specific pattern combination")
        
        st.caption("This detailed analysis is based on 500+ successful transformations with similar patterns")

    # ---- Contact Form and Email Integration ----
    
    def _render_contact_form(self):
        """
        Render the contact form after completion. Gathers email and optional data.
        Sends results via email if system available.
        """
        st.success("Your comprehensive behavioral pattern analysis is ready!")
        
        results = st.session_state.assessment_results
        
        # Show different metrics based on assessment type
        if st.session_state.is_digital_native:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("", "Questions answered", results['total_questions_answered'])
            with col2:
                st.metric("", "Patterns detected", len(results.get('pattern_scores', {})))
            with col3:
                digital_score = st.session_state.get('digital_despair_score', 0)
                severity = st.session_state.get('digital_severity', 'MINIMAL')
                st.metric("", "Digital patterns", f"{digital_score:.0f}%")
            with col4:
                completion_rate = results.get('completion_rate', 1.0)
                st.metric("", "Completion rate", f"{completion_rate*100:.0f}%")
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("", "Questions answered", results['total_questions_answered'])
            with col2:
                st.metric("", "Patterns detected", len(results.get('pattern_scores', {})))
            with col3:
                completion_rate = results.get('completion_rate', 1.0)
                st.metric("", "Completion rate", f"{completion_rate*100:.0f}%")
        
        st.markdown("**Enter your email to receive your personalized analysis and next steps:**")
        
        with st.form("contact_form"):
            # ONLY EMAIL IS MANDATORY
            email = st.text_input("Email*", placeholder="your@email.com")
            
            # ALL OTHER FIELDS ARE OPTIONAL
            name = st.text_input("Full name (optional)", placeholder="Your full name")
            phone = st.text_input("Phone (optional)", placeholder="+1 xxx xxx xxxx")

            concern = st.text_area(
                "What brought you to this assessment? (optional)",
                placeholder="Brief description of what motivated you to take this assessment...",
                height=100
            )
            
            urgency = st.selectbox(
                "How urgent is addressing this pattern? (optional)",
                ["Not specified", "Extremely urgent - significantly impacting life", 
                 "Very urgent - causing daily distress", "Moderately urgent - noticeable impact", 
                 "Somewhat urgent - want to address soon", "Not urgent - exploring options"]
            )
            
            next_step = st.selectbox(
                "Preferred next step (optional)",
                ["Not specified", "Schedule free consultation call", 
                 "Information about transformation packages", "Receive analysis and recommendations first", 
                 "Connect with clinical team directly"]
            )
            
            marketing_consent = st.checkbox(
                "I consent to receiving follow-up communications about my assessment results and relevant therapeutic services."
            )
            
            submitted = st.form_submit_button("Get my personalized analysis", type="primary", use_container_width=True)

            if submitted:
                errors = []
                
                # ONLY EMAIL VALIDATION IS REQUIRED
                if not email.strip(): 
                    errors.append("Email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}, email):
                    errors.append("Valid email address is required")
                
                # MARKETING CONSENT CHECK
                if not marketing_consent:
                    errors.append("Please consent to follow-up communications to receive your results")
                
                if errors:
                    for error in errors:
                        st.error(f"⚠ {error}")
                else:
                    # Save contact info with optional fields defaulting to empty/not specified
                    st.session_state.contact_info = {
                        'name': name.strip() if name.strip() else 'Not provided',
                        'email': email.strip(),
                        'phone': phone.strip() if phone.strip() else 'Not provided',
                        'urgency': urgency if urgency != 'Not specified' else 'Not specified',
                        'primary_concern': concern.strip() if concern.strip() else 'Not provided',
                        'next_step': next_step if next_step != 'Not specified' else 'Not specified',
                        'marketing_consent': marketing_consent,
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    # GENERATE COMPREHENSIVE CLINICAL TEMPLATE using refactored method
                    clinical_template = self._format_comprehensive_clinical_template()
                    
                    # Prepare assessment data for email with enhanced clinical template
                    email_data = {
                        'contact_info': st.session_state.contact_info,
                        'assessment_results': st.session_state.assessment_results,
                        'responses': st.session_state.assessment_responses,
                        'assessment_responses': st.session_state.assessment_responses,
                        'intensity_responses': st.session_state.intensity_responses,
                        'adaptive_triggered': st.session_state.adaptive_paths,
                        'risk_flags': st.session_state.risk_flags,
                        'pattern_scores': st.session_state.pattern_scores,
                        'trigger_chain': st.session_state.trigger_chain,
                        'digital_responses': st.session_state.digital_responses,
                        'is_digital_native': st.session_state.is_digital_native,
                        'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis'),
                        'clinical_template': clinical_template,
                        'start_time': st.session_state.start_time,
                        'completion_timestamp': datetime.now().isoformat()
                    }
                    
                    # Send comprehensive clinical assessment email using utils.email_assess
                    self._send_assessment_email(email_data)
                    
                    st.session_state.contact_provided = True
                    st.rerun()

    def _send_assessment_email(self, email_data):
        """Send assessment email using utils.email_assess with error handling"""
        try:
            if SEND_CLINICAL_AVAILABLE:
                from utils.email_assess import send_clinical_assessment_results      
                email_success = send_clinical_assessment_results(email_data)
                
                if email_success:
                    st.success("✅ Assessment completed and clinical team notified!")
                    st.info("📧 Your detailed analysis has been sent to our clinical team for review.")
                else:
                    st.warning("⚠️ Assessment saved, but email notification failed. Our team will still receive your results.")
            else:
                st.warning("Email system temporarily unavailable. Assessment data has been saved.")
                st.info("Our clinical team will receive your results through backup systems.")
                
        except ImportError as e:
            st.error(f"Email system unavailable: {e}")
            st.info("Assessment completed! Our clinical team will review your results.")
        except Exception as e:
            st.error(f"Email error: {str(e)}")
            st.info("Assessment saved locally. Please contact support if this persists.")

    def _render_results(self):
        """Render user-centric results page with comprehensive insights"""
        self._render_results_hero_at_top()
        
        # COMMENTED OUT FOR NOW - WILL BE ENABLED IN COMPLETE BLUEPRINT:
        # self._render_pattern_cost_analysis()
        # self._render_aha_moment_bridge()
        # if st.session_state.is_digital_native:
        #     self._render_digital_insights()
        # self._render_transformation_roadmap()
        # self._render_empowerment_section()
        
        # Jump directly to empowerment and next steps
        self._render_next_steps_section()
       
        # Generate unique session ID for this assessment
        # if 'assessment_session_id' not in st.session_state:
        #     st.session_state.assessment_session_id = str(uuid.uuid4())
        
        # Create comprehensive assessment data package
        # assessment_data = self._compile_complete_assessment_data()
        
        # Blueprint preview and full access
        #self._render_blueprint_access(assessment_data)

    def _render_blueprint_access(self):
        """Render blueprint access with preview and full version"""
        try:
            # Generate assessment data
            assessment_data = self._compile_complete_assessment_data()

            try:
                preview_data = self._extract_preview_insights(assessment_data)
            except KeyError as e:
                st.warning(f"Preview data incomplete - some assessment responses may be missing")
                # Provide minimal preview data
                preview_data = {
                    'dominant_pattern_name': 'Assessment incomplete',
                    'trigger_sequence': None,
                    'cost_preview': {'weekly_hours': 8, 'annual_cost': '฿331,200', 'relationship_impact': 'Assessment needed'},
                    'pattern_interactions': ['Pattern analysis needed'],
                    'session_plan': {
                        'session_1_preview': 'Comprehensive assessment and rapport building',
                        'session_2_preview': 'Core transformation and programming',
                        'results_timeline': '2-4 weeks',
                        'optimization_factor': 'Assessment completion needed'
                    },
                    'immediate_techniques': {
                        'technique_1': {'name': 'Mindful Pause', 'description': 'Take 3 breaths before reacting'},
                        'technique_2': {'name': 'Choice Point', 'description': 'Ask: Is this serving me?'}
                    },
                    'digital_insights': None,
                    'pattern_count': 0
                }
            
            # STEP 5: Expander with only blueprint content
            with st.expander("**Your complete transformation blueprint**", expanded=False):

                # STEP 7: Paywall and buttons section
                self._render_paywall_and_buttons(assessment_data)
                
                # Only show "What your complete blueprint reveals" section
                st.markdown("*What your complete blueprint reveals:*")
                
                # Behavioral sequence preview
                if preview_data['trigger_sequence']:
                    st.markdown(f"""
                    **🔍 Your behavioral sequence decoded:**
                    - **Trigger pattern:** {preview_data['trigger_sequence']['trigger']}
                    - **Physical response:** {preview_data['trigger_sequence']['physical']}
                    - **Automatic thought:** "{preview_data['trigger_sequence']['thought']}"
                    - **Emotional cascade:** {preview_data['trigger_sequence']['emotion']}
                    - **Protective behavior:** {preview_data['trigger_sequence']['behavior']}
                    
                    *Complete blueprint shows exact intervention points to interrupt this sequence*
                    """)
                
                # Cost calculation preview
                if preview_data['cost_preview']:
                    st.markdown(f"""
                    **💰 Hidden cost analysis preview:**
                    - **Weekly time cost:** ~{preview_data['cost_preview']['weekly_hours']} hours of mental energy
                    - **Annual impact:** Approximately {preview_data['cost_preview']['annual_cost']} in opportunity costs
                    - **Relationship cost:** {preview_data['cost_preview']['relationship_impact']}
                    
                    *Full analysis includes lifetime projections and specific dollar amounts*
                    """)
                
                # Pattern interaction preview
                if len(preview_data['pattern_interactions']) > 1:
                    st.markdown(f"""
                    **🔗 Pattern interaction analysis:**
                    Your {preview_data['dominant_pattern_name']} pattern triggers your {preview_data['pattern_interactions'][1]} pattern, 
                    creating a reinforcing cycle that explains why this has been so persistent.
                    
                    *Complete blueprint maps all {preview_data['pattern_count']} pattern interactions*
                    """)
                
                # Transformation roadmap preview
                st.markdown(f"""
                **🎯 Your precision transformation roadmap:**
                - **Session 1 focus:** {preview_data['session_plan']['session_1_preview']}
                - **Session 2 target:** {preview_data['session_plan']['session_2_preview']}
                - **Timeline to results:** {preview_data['session_plan']['results_timeline']}
                - **Success optimization:** {preview_data['session_plan']['optimization_factor']}
                
                *Detailed session scripts and hypnotic language patterns included*
                """)
                
                # Self-help preview section
                if preview_data['immediate_techniques']:
                    st.markdown(f"""
                    **⚡ Immediate pattern interruption techniques you can use today:**
                    
                    **Technique 1 - The {preview_data['immediate_techniques']['technique_1']['name']}:**
                    {preview_data['immediate_techniques']['technique_1']['description']}
                    
                    **Technique 2 - {preview_data['immediate_techniques']['technique_2']['name']}:**
                    {preview_data['immediate_techniques']['technique_2']['description']}
                    
                    *Complete blueprint includes 5-7 personalized techniques with step-by-step instructions*
                    """)
                
                st.markdown("---")
                
                # Action buttons
                col1, col2 = st.columns(2)
                
                with col1:
                    button_text = "📖 Access your complete blueprint" if st.session_state.get('blueprint_access_granted', False) else "📖 View full blueprint (payment required)"
                    if st.button(button_text, 
                                type="primary", 
                                use_container_width=True,
                                disabled=not st.session_state.get('blueprint_access_granted', False)):
                        st.session_state.show_blueprint = True
                        st.rerun()
                
                with col2:
                    pdf_text = "📄 Download PDF report" if st.session_state.get('blueprint_access_granted', False) else "📄 Generate PDF (payment required)"
                    if st.button(pdf_text, 
                                use_container_width=True,
                                disabled=not st.session_state.get('blueprint_access_granted', False)):
                        self._generate_and_offer_pdf(assessment_data)
                
                # Show full blueprint if payment verified and requested
                if (st.session_state.get('show_blueprint', False) and 
                    st.session_state.get('blueprint_access_granted', False)):
                    st.markdown("---")
                    st.markdown("**Your complete transformation blueprint**")
                    self._render_full_blueprint(assessment_data)
                    
                
        except Exception as e:
            st.error(f"Error loading blueprint: {str(e)}")
            st.info("Please refresh the page")

    def _render_paywall_and_buttons(self, assessment_data):
        """Render paywall integration and action buttons"""
        try:
            # Complete analysis report
            
            st.markdown(f"""
            <div style="background: #FFFFFF; padding: 24px; border-radius: 12px; 
                        border: 2px solid #4CA1A3; margin: 16px 0;">
                <div style="text-align: center;">
                    <div style="color: #273548; font-size: 1.8rem; font-weight: 600; margin-bottom: 8px;">
                        <strong>Your personalized transformation blueprint</strong>
                    </div>
                    <p style="color: #556D7A; font-size: 1rem; margin-bottom: 16px;">
                        Complete 15-20 page analysis • Immediate access • Lifetime download
                    </p>
                    <div style="background: #F3F6F8; padding: 16px; border-radius: 8px; margin-bottom: 16px;">
                        <span style="color: #4CA1A3; font-weight: bold; font-size: 1.6rem;">฿1000</span>
                        <span style="color: #556D7A; font-size: 1rem;"> (Clinical value ฿2,500)</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Paywall integration
            if PAYWALL_AVAILABLE:
                try:
                    paywall = create_clinical_paywall()
                    
                    if paywall.check_payment_status():
                        st.success("✅ Payment verified - Full blueprint access granted")
                        st.session_state.blueprint_access_granted = True
                    else:
                        with st.container():
                            paywall.render_paywall_interface(assessment_data)
                            
                except Exception as e:
                    st.error(f"Payment system temporarily unavailable: {str(e)}")
                    st.info("Contact support for manual access: info@rapidtransformation.com")
            else:
                st.info("💳 Secure payment processing available - Contact for access")
            
        except Exception as e:
            st.error(f"Error with paywall integration: {str(e)}")

    def _render_full_blueprint(self, assessment_data=None):
        """Render the full behavioral blueprint"""
        try:
            if assessment_data is None:
                assessment_data = self._compile_assessment_data_for_blueprint()
                
            blueprint = create_behavioral_blueprint()
            blueprint.render_complete_blueprint(assessment_data)
            
            # Add download and save options at the bottom
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("💾 Save to cloud", use_container_width=True):
                    self._save_to_cloud(assessment_data)
            
            with col2:
                if st.button("📧 Email report", use_container_width=True):
                    self._email_blueprint(assessment_data)
            
            with col3:
                if st.button("🔄 Update blueprint", use_container_width=True):
                    # Force refresh of blueprint
                    st.rerun()
                    
        except Exception as e:
            st.error(f"Error loading blueprint: {str(e)}")
            st.info("Please contact our technical support team.")

    def _generate_and_offer_pdf(self, assessment_data):
        """Generate PDF and offer download"""
        try:
            with st.spinner("Generating your personalized report..."):
                pdf_generator = PDFGenerator()
                pdf_bytes = pdf_generator.generate_blueprint_pdf(assessment_data)
                
                # Save to Streamlit Community Cloud storage
                cloud_storage = StreamlitCloudStorage()
                pdf_url = cloud_storage.save_pdf(
                    pdf_bytes, 
                    f"blueprint_{assessment_data['session_id']}.pdf"
                )
                
                st.success("✅ Your personalized blueprint report has been generated!")
                
                # Offer download
                st.download_button(
                    label="🔥 Download PDF Report",
                    data=pdf_bytes,
                    file_name=f"behavioral_blueprint_{assessment_data['session_id'][:8]}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
                # Show cloud access info
                if pdf_url:
                    st.info("📡 Your report is saved and can be accessed through the download link above.")
                    
        except Exception as e:
            st.error(f"Error generating PDF: {str(e)}")
            st.info("Please try again or contact support if the issue persists.")

    def _compile_assessment_data_for_blueprint(self):
        """Compile assessment data in the format expected by blueprint"""
        return {
            'assessment_responses': st.session_state.get('assessment_responses', {}),
            'pattern_scores': st.session_state.get('pattern_scores', {}),
            'intensity_responses': st.session_state.get('intensity_responses', {}),
            'trigger_chain': st.session_state.get('trigger_chain', {}),
            'digital_responses': st.session_state.get('digital_responses', {}),
            'is_digital_native': st.session_state.get('is_digital_native', False),
            'digital_despair_analysis': st.session_state.get('assessment_results', {}).get('digital_despair_analysis'),
            'contact_info': st.session_state.get('contact_info', {}),
            'completion_rate': st.session_state.get('assessment_results', {}).get('completion_rate', 1.0),
            'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
            'adaptive_paths': st.session_state.get('adaptive_paths', []),
            'risk_flags': st.session_state.get('risk_flags', []),
            'start_time': st.session_state.get('start_time'),
            'completion_timestamp': datetime.now().isoformat(),
            'phase_completion': st.session_state.get('phase_progress', {}),
            'assessment_version': '2.0'
        }

    def _render_digital_insights(self):
        """Render digital insights using Streamlit components"""
        digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
        if not digital_analysis:
            return
        
        severity = digital_analysis['severity_level']
        score = digital_analysis['digital_despair_score']
        
        # Digital-specific insights using config thresholds
        insight_data = self.digital_thresholds.get(severity, self.digital_thresholds.get('MINIMAL', {}))
        
        st.markdown(f"#### Digital pattern analysis: {insight_data.get('title', 'Analysis needed')}")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**Digital conditioning score:** {score:.0f}% ({severity})")
        
        st.markdown(insight_data.get('description', 'Digital pattern analysis in progress'))
        st.info(f"**Specialized advantage:** {insight_data.get('benefits', 'Approach optimized for your profile')}")

    # ---- Additional utility methods that may be called ----
    
    def _save_to_cloud(self, assessment_data):
        """Save assessment to cloud storage"""
        try:
            storage = SimpleStorage()
            session_id = str(uuid.uuid4())
            storage_url = storage.save_assessment(session_id, assessment_data)
            st.success(f"Assessment saved to cloud: {session_id[:8]}")
        except Exception as e:
            st.error(f"Cloud save error: {str(e)}")

    def _email_blueprint(self, assessment_data):
        """Email blueprint to user"""
        try:
            if 'contact_info' in st.session_state:
                email = st.session_state.contact_info.get('email')
                if email:
                    # Use existing email system
                    self._send_assessment_email(assessment_data)
                    st.success(f"Blueprint emailed to {email}")
                else:
                    st.error("No email address available")
            else:
                st.error("Contact information not provided")
        except Exception as e:
            st.error(f"Email error: {str(e)}")

    # ---- Advanced Analytics Methods for Blueprint Support ----
    
    def _extract_complete_trigger_analysis(self, assessment_data):
        """Extract and analyze complete trigger sequence with intensity weighting"""
        responses = assessment_data.get('assessment_responses', {})
        intensity_data = assessment_data.get('intensity_responses', {})
        
        # Extract complete 8-step sequence with client's exact words
        trigger_sequence = {
            'environmental_trigger': self._extract_response_by_keywords(responses, ['30 seconds', 'happening']),
            'first_awareness': self._extract_response_by_keywords(responses, ['notice first']),
            'physical_sensation': self._extract_response_by_keywords(responses, ['physical sensation']),
            'automatic_thought': self._extract_response_by_keywords(responses, ['thought automatically']),
            'emotional_cascade': self._extract_response_by_keywords(responses, ['typically feel']),
            'behavioral_response': self._extract_response_by_keywords(responses, ['you typically:']),
            'immediate_consequence': self._extract_response_by_keywords(responses, ['right after']),
            'long_term_impact': self._extract_response_by_keywords(responses, ['few hours later'])
        }
        
        # Calculate intensity per step
        intensity_mapping = {}
        for step, content in trigger_sequence.items():
            related_q_id = self._find_question_id_for_content(responses, content)
            if related_q_id and related_q_id in intensity_data:
                intensity_mapping[step] = intensity_data[related_q_id]
            else:
                intensity_mapping[step] = 5  # Default
        
        return {
            'sequence': trigger_sequence,
            'intensity_map': intensity_mapping,
            'highest_intensity_step': max(intensity_mapping.items(), key=lambda x: x[1]),
            'intervention_windows': self._calculate_intervention_windows(trigger_sequence, intensity_mapping)
        }

    def _calculate_intervention_windows(self, trigger_sequence, intensity_mapping):
        """Calculate optimal intervention windows"""
        windows = []
        
        # Physical sensation window
        physical_intensity = intensity_mapping.get('physical_sensation', 5)
        if physical_intensity >= 5:
            windows.append({
                'name': 'Somatic Awareness Intervention',
                'timing': 'At first physical sensation',
                'success_rate': min(95, 70 + physical_intensity * 5),
                'technique': 'Body scan interruption with breathing reset'
            })
        
        # Thought interruption window  
        thought_intensity = intensity_mapping.get('automatic_thought', 5)
        if thought_intensity >= 4:
            windows.append({
                'name': 'Cognitive Pattern Interrupt',
                'timing': 'At automatic thought emergence',
                'success_rate': min(90, 60 + thought_intensity * 6),
                'technique': 'Thought stopping with positive reframe installation'
            })
        
        # Behavioral choice window
        behavior_intensity = intensity_mapping.get('behavioral_response', 5)
        windows.append({
            'name': 'Behavioral Choice Point',
            'timing': 'Before automatic behavior',
            'success_rate': min(85, 50 + behavior_intensity * 7),
            'technique': 'Pause and alternative response selection'
        })
        
        return sorted(windows, key=lambda x: x['success_rate'], reverse=True)

    def _extract_digital_component_analysis(self, assessment_data):
        """Detailed analysis of each digital conditioning component"""
        digital_analysis = assessment_data.get('digital_despair_analysis', {})
        if not digital_analysis:
            return None
        
        components = digital_analysis.get('component_scores', {})
        responses = assessment_data.get('digital_responses', {})
        
        component_details = {}
        
        # Map each component to specific responses and interventions
        component_map = {
            'reality_dissociation': {
                'questions': [2],  # Authenticity question
                'intervention': 'Offline confidence transfer protocols',
                'timeline': '2-3 sessions for integration'
            },
            'ironic_detachment': {
                'questions': [4],  # Emotional expression question
                'intervention': 'Authentic emotion permission installation',
                'timeline': '1-2 sessions for breakthrough'
            },
            'attention_fragmentation': {
                'questions': [8],  # Attention span question
                'intervention': 'Focused attention restoration therapy',
                'timeline': '2-4 weeks for stabilization'
            }
        }
        
        for component, score in components.items():
            if component in component_map and score >= 2:
                details = component_map[component]
                related_responses = [responses.get(q_id, '') for q_id in details['questions']]
                
                component_details[component] = {
                    'score': score,
                    'severity': 'High' if score >= 4 else 'Moderate',
                    'client_responses': related_responses,
                    'intervention': details['intervention'],
                    'timeline': details['timeline'],
                    'success_indicators': self._generate_digital_success_indicators(component, score)
                }
        
        return component_details

    def _generate_digital_success_indicators(self, component, score):
        """Generate specific success indicators for digital components"""
        indicators_map = {
            'reality_dissociation': [
                'Feeling equally authentic online and offline',
                'Preferring face-to-face conversations over digital',
                'Natural eye contact during conversations'
            ],
            'ironic_detachment': [
                'Expressing genuine emotions without self-mockery',
                'Sincere enthusiasm without embarrassment',
                'Connecting emotionally with others naturally'
            ],
            'attention_fragmentation': [
                'Reading for 30+ minutes without distraction',
                'Having complete conversations without phone checking',
                'Deep focus on single tasks for extended periods'
            ]
        }
        
        return indicators_map.get(component, ['Improved well-being in this area'])

    def _extract_pattern_emergence_data(self, assessment_data):
        """Analyze how patterns emerged during assessment"""
        triggered_patterns = assessment_data.get('triggered_patterns', set())
        adaptive_paths = assessment_data.get('adaptive_paths', [])
        pattern_scores = assessment_data.get('pattern_scores', {})
        phase_progress = assessment_data.get('phase_completion', {})
        
        emergence_analysis = {
            'pattern_discovery_order': [],
            'resistance_indicators': [],
            'engagement_patterns': [],
            'therapeutic_readiness': {}
        }
        
        # Analyze pattern discovery order
        for path in adaptive_paths:
            if 'pattern_' in path:
                pattern_id = int(path.split('_')[1])
                if pattern_id in pattern_scores:
                    emergence_analysis['pattern_discovery_order'].append({
                        'pattern_id': pattern_id,
                        'pattern_name': self.patterns[pattern_id],
                        'final_score': pattern_scores[pattern_id],
                        'discovery_phase': self._determine_discovery_phase_detailed(path, phase_progress)
                    })
        
        # Analyze engagement patterns
        total_questions = sum(phase_progress.values())
        if total_questions >= 20:
            engagement_level = 'High'
        elif total_questions >= 15:
            engagement_level = 'Moderate'
        else:
            engagement_level = 'Low'
        
        emergence_analysis['engagement_patterns'] = {
            'level': engagement_level,
            'total_questions': total_questions,
            'completion_rate': assessment_data.get('completion_rate', 0),
            'phase_distribution': phase_progress
        }
        
        return emergence_analysis

    def _determine_discovery_phase_detailed(self, adaptive_path, phase_progress):
        """Determine which phase a pattern was discovered in"""
        if 'pattern_1' in adaptive_path or 'pattern_2' in adaptive_path:
            return 'Early engagement'
        elif 'pattern_3' in adaptive_path or 'pattern_4' in adaptive_path:
            return 'Trigger mapping'
        else:
            return 'Pattern-specific questioning'

    def _extract_emotional_intensity_profile(self, assessment_data):
        """Create detailed emotional intensity analysis"""
        intensity_responses = assessment_data.get('intensity_responses', {})
        pattern_scores = assessment_data.get('pattern_scores', {})
        responses = assessment_data.get('assessment_responses', {})
        
        intensity_profile = {
            'emotional_volatility': 0,
            'pattern_intensity_map': {},
            'intervention_priority': [],
            'emotional_regulation_needs': []
        }
        
        if not intensity_responses:
            return intensity_profile
        
        # Calculate emotional volatility (variance in intensity responses)
        intensities = list(intensity_responses.values())
        avg_intensity = sum(intensities) / len(intensities)
        variance = sum((x - avg_intensity) ** 2 for x in intensities) / len(intensities)
        intensity_profile['emotional_volatility'] = variance
        
        # Map patterns to their intensity levels
        for pattern_id, score in pattern_scores.items():
            pattern_intensities = []
            for q_id, intensity in intensity_responses.items():
                # Find questions related to this pattern
                if self._question_relates_to_pattern_detailed(q_id, pattern_id, responses):
                    pattern_intensities.append(intensity)
            
            if pattern_intensities:
                avg_pattern_intensity = sum(pattern_intensities) / len(pattern_intensities)
                intensity_profile['pattern_intensity_map'][pattern_id] = {
                    'average_intensity': avg_pattern_intensity,
                    'pattern_name': self.patterns[pattern_id],
                    'regulation_need': 'High' if avg_pattern_intensity >= 6 else 'Moderate' if avg_pattern_intensity >= 4 else 'Low'
                }
        
        # Create intervention priority based on intensity + pattern score
        priority_list = []
        for pattern_id in pattern_scores:
            if pattern_id in intensity_profile['pattern_intensity_map']:
                combined_score = (pattern_scores[pattern_id] * 
                                intensity_profile['pattern_intensity_map'][pattern_id]['average_intensity'])
                priority_list.append((pattern_id, combined_score))
        
        intensity_profile['intervention_priority'] = sorted(priority_list, key=lambda x: x[1], reverse=True)
        
        return intensity_profile

    def _question_relates_to_pattern_detailed(self, q_id, pattern_id, responses):
        """Check if a question relates to a specific pattern using config keywords"""
        question_text = responses.get(q_id, {}).get('question_text', '').lower()
        
        # Use pattern keywords from config if available
        pattern_info = self.pattern_descriptions.get(pattern_id, {})
        keywords = pattern_info.get('keywords_matching', [])
        
        # Fallback keyword mapping
        if not keywords:
            pattern_keywords = {
                1: ['happy', 'joy', 'success', 'good things'],
                2: ['conflict', 'argument', 'disagree', 'defensive'],
                3: ['trust', 'suspicious', 'motives', 'skeptical'],
                4: ['choice', 'decision', 'either', 'both'],
                5: ['productive', 'busy', 'achievement', 'worth'],
                6: ['different', 'personality', 'authentic', 'real'],
                7: ['others', 'help', 'needs', 'care'],
                8: ['family', 'expectations', 'should', 'duty'],
                9: ['boundaries', 'limits', 'context', 'situation']
            }
            keywords = pattern_keywords.get(pattern_id, [])
        
        return any(keyword in question_text for keyword in keywords)

    def _extract_personal_language(self, assessment_data):
        """Extract client's actual words and metaphors from responses"""
        responses = assessment_data.get('assessment_responses', {})
        personal_phrases = []
        emotional_language = []
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and len(response.strip()) > 20:
                # Extract meaningful phrases (first-person language)
                if any(word in response.lower() for word in ['i feel', 'i think', 'i notice', 'i want']):
                    personal_phrases.append(response.strip())
                
                # Extract emotional language
                emotion_words = ['anxious', 'frustrated', 'stuck', 'overwhelmed', 'tired', 'afraid']
                for word in emotion_words:
                    if word in response.lower():
                        emotional_language.append(word)
        
        return {
            'personal_phrases': personal_phrases[:3],
            'emotional_language': list(set(emotional_language))
        }

    def _create_personalized_trigger_analysis(self, assessment_data):
        """Create detailed trigger sequence using client's actual responses"""
        trigger_chain = assessment_data.get('trigger_chain', {})
        intensity_data = assessment_data.get('intensity_responses', {})
        
        # Build complete sequence with client's words
        sequence = {
            'trigger': trigger_chain.get('trigger', 'Situation needs exploration'),
            'awareness_point': trigger_chain.get('awareness_point', 'Body or thought awareness'),
            'physical': trigger_chain.get('physical_response', 'Physical sensation'),
            'thought': trigger_chain.get('automatic_thought', 'Automatic thought pattern'),
            'emotion': trigger_chain.get('emotional_response', 'Emotional response'),
            'behavior': trigger_chain.get('behavioral_response', 'Behavioral pattern'),
            'consequence': trigger_chain.get('immediate_consequence', 'Immediate outcome'),
            'reinforcement': trigger_chain.get('longer_term_impact', 'Pattern reinforcement')
        }
        
        # Add intensity weighting
        avg_intensity = sum(intensity_data.values()) / len(intensity_data) if intensity_data else 5
        
        return {
            'sequence': sequence,
            'intensity_level': avg_intensity,
            'intervention_points': self._identify_intervention_points_detailed(sequence)
        }

    def _identify_intervention_points_detailed(self, sequence):
        """Identify key intervention points in the trigger sequence"""
        intervention_points = []
        
        # Physical awareness point
        if sequence.get('physical') and sequence['physical'] != 'Physical sensation':
            intervention_points.append("Physical sensation awareness")
        
        # Thought interruption point  
        if sequence.get('thought') and sequence['thought'] != 'Automatic thought pattern':
            intervention_points.append("Automatic thought interruption")
        
        # Behavioral choice point
        if sequence.get('behavior') and sequence['behavior'] != 'Behavioral pattern':
            intervention_points.append("Behavioral response choice")
        
        # Always include these standard points
        if len(intervention_points) < 3:
            intervention_points.extend(["Pattern recognition point", "Response choice point", "Future outcome consideration"])
        
        return intervention_points[:4]  # Return max 4 points

    def _generate_speaking_to_you_insights(self, assessment_data):
        """Generate insights using client's actual language and responses"""
        personal_lang = self._extract_personal_language(assessment_data)
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return {}
        
        dominant_pattern_id = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        # Use client's emotional language in insights
        emotional_context = personal_lang['emotional_language']
        personal_phrases = personal_lang['personal_phrases']
        
        speaking_insights = {
            'recognition': f"When you mentioned feeling {', '.join(emotional_context[:2]) if emotional_context else 'stuck'}, this perfectly describes the {self.patterns[dominant_pattern_id]} pattern in action.",
            'validation': f"Your awareness that {personal_phrases[0][:100] if personal_phrases else 'these patterns affect your daily life'} shows remarkable self-insight.",
            'breakthrough': f"The fact that you can articulate {personal_phrases[1][:100] if len(personal_phrases) > 1 else 'your experience so clearly'} means you're already 60% of the way to transformation."
        }
        
        return speaking_insights

    def _calculate_comprehensive_costs(self, pattern_scores, assessment_data):
        """Calculate comprehensive weekly and annual costs"""
        if not pattern_scores:
            return {'time_hours': 0, 'opportunities': 0, 'relationship_strain': 0, 'energy_drain': 0}
        
        pattern_count = len(pattern_scores)
        intensity_avg = sum(pattern_scores.values()) / len(pattern_scores)
        
        # Base calculations with realistic estimates
        base_time = 8  # hours per week
        pattern_multiplier = min(pattern_count * 1.5, 12)
        intensity_multiplier = min(intensity_avg / 3, 3)
        
        time_hours = int(base_time + pattern_multiplier + intensity_multiplier)
        opportunities = max(1, int(pattern_count / 2))
        relationship_strain = min(pattern_count, 5)
        energy_drain = min(int(30 + (intensity_avg * 10) + (pattern_count * 5)), 80)
        
        return {
            'time_hours': time_hours,
            'opportunities': opportunities, 
            'relationship_strain': relationship_strain,
            'energy_drain': energy_drain
        }

    def _calculate_lifetime_costs(self, pattern_scores, assessment_data):
        """Calculate estimated lifetime costs of patterns"""
        if not pattern_scores:
            return {'total_5_year': 0, 'lost_opportunities': 0, 'stress_costs': 0, 
                   'relationship_costs': 0, 'happiness_hours': 0, 'relationship_quality': 0,
                   'career_impact': 0, 'health_impact': 0}
        
        pattern_count = len(pattern_scores)
        intensity_avg = sum(pattern_scores.values()) / len(pattern_scores)
        
        # Financial calculations (conservative estimates)
        lost_opportunities = pattern_count * intensity_avg * 2000  # Career/business opportunities
        stress_costs = pattern_count * 1500  # Health, therapy, stress management
        relationship_costs = min(pattern_count * 800, 5000)  # Relationship counseling, social costs
        
        total_5_year = int((lost_opportunities + stress_costs + relationship_costs) * 5)
        
        # Life satisfaction calculations
        happiness_hours = int(pattern_count * intensity_avg * 50)  # Hours per year
        relationship_quality = min(int(pattern_count * 8), 40)  # Percentage reduction
        career_impact = min(int(pattern_count * 6), 30)  # Percentage limitation
        health_impact = min(int(pattern_count * 0.5), 3)  # Years of stress impact
        
        return {
            'total_5_year': total_5_year,
            'lost_opportunities': int(lost_opportunities * 5),
            'stress_costs': int(stress_costs * 5),
            'relationship_costs': int(relationship_costs * 5),
            'happiness_hours': happiness_hours,
            'relationship_quality': relationship_quality,
            'career_impact': career_impact,
            'health_impact': health_impact
        }

    def _identify_transformation_assets(self, assessment_data):
        """Identify visitor's existing assets for transformation"""
        assets = []
        
        # Intelligence and insight
        pattern_scores = assessment_data.get('pattern_scores', {})
        if len(pattern_scores) >= 3:
            assets.append("High emotional intelligence and pattern recognition ability")
        
        # Completion demonstrates persistence
        completion_rate = assessment_data.get('completion_rate', 0)
        if completion_rate >= 0.8:
            assets.append("Demonstrated persistence and commitment to understanding yourself")
        
        # Self-awareness
        responses = assessment_data.get('assessment_responses', {})
        self_aware_responses = 0
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and any(word in response.lower() for word in ['realize', 'notice', 'aware', 'recognize']):
                self_aware_responses += 1
        
        if self_aware_responses >= 2:
            assets.append("Strong self-awareness and ability to observe your own patterns")
        
        # Communication skills
        detailed_responses = sum(1 for response_data in responses.values() 
                               if isinstance(response_data.get('response'), str) and len(response_data.get('response', '').strip()) > 30)
        
        if detailed_responses >= 4:
            assets.append("Excellent communication and self-expression abilities")
        
        # Analytical thinking
        if pattern_scores:
            assets.append("Strong analytical thinking that can be redirected from self-criticism to self-development")
        
        # Digital competencies
        if assessment_data.get('is_digital_native'):
            assets.append("Digital competencies that can transfer to real-world confidence")
        
        # Courage to seek help
        assets.append("Courage to seek help and willingness to explore new approaches")
        
        # Default assets
        if len(assets) < 3:
            assets.extend([
                "Natural problem-solving abilities",
                "Capacity for insight and self-reflection",
                "Existing coping strategies that show resilience"
            ])
        
        return assets[:6]  # Return top 6 assets

    def _compile_complete_assessment_data(self):
        """Compile complete assessment data for blueprint"""
        return {
            'assessment_results': st.session_state.assessment_results,
            'assessment_responses': st.session_state.assessment_responses,
            'pattern_scores': st.session_state.pattern_scores,
            'intensity_responses': st.session_state.get('intensity_responses', {}),
            'trigger_chain': st.session_state.get('trigger_chain', {}),
            'digital_responses': st.session_state.get('digital_responses', {}),
            'is_digital_native': st.session_state.is_digital_native,
            'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis'),
            'contact_info': st.session_state.get('contact_info', {}),
            'completion_rate': st.session_state.assessment_results.get('completion_rate', 1.0),
            'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
            'adaptive_paths': st.session_state.get('adaptive_paths', []),
            'risk_flags': st.session_state.get('risk_flags', []),
            'start_time': st.session_state.get('start_time'),
            'completion_timestamp': datetime.now().isoformat(),
            'user_agent': self._get_user_agent(),
            'assessment_version': '2.0'
        }

    def _render_results_hero_at_top(self):
        """Render hero section at top of results page"""
        try:
            assessment_data = self._compile_complete_assessment_data()
            preview_data = self._extract_preview_insights(assessment_data)
            
            # Compelling personalized preview header
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #F3F6F8 0%, #FFFFFF 100%); 
                        padding: 24px; border-radius: 12px; border-left: 4px solid #4CA1A3; margin: 16px 0;">
                <div style="color: #273548; font-size: 1.1rem; line-height: 1.6; margin-bottom: 16px;">
                    <strong style="color: #4CA1A3; font-size: 1.3rem;">🎯 Your unique pattern signature revealed</strong><br><br>
                    <strong>Primary pattern:</strong> {preview_data['dominant_pattern_name']} - {preview_data['intensity_description']}<br>
                    <strong>Complexity level:</strong> {preview_data['complexity_description']} ({preview_data['pattern_count']} interconnected patterns)<br>
                    <strong>Success probability:</strong> {preview_data['success_rate']}% (above average due to {preview_data['success_factors']})<br>
                    {preview_data['digital_summary']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Transformation success likelihood
            st.markdown("**Transformation success likelihood:**")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.progress(preview_data['success_rate'] / 100)
            with col2:
                st.markdown(f"**{preview_data['success_rate']}%**")
            
            # Digital insights if applicable
            self._render_digital_insights_at_top(preview_data)
            
            # Blueprint access
            self._render_blueprint_access()

        except Exception as e:
            st.error(f"Error loading results analysis: {str(e)}")
            st.info("Please complete the full assessment for detailed insights.")

    def _render_digital_insights_at_top(self, preview_data):
        """Render digital insights at top of page if applicable"""
        if preview_data.get('digital_insights'):
            st.markdown("**Digital pattern analysis:**")
            
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                insight_colors = {
                    'SEVERE': '#ef4444',
                    'MODERATE': '#eab308', 
                    'MILD': '#4CA1A3',
                    'MINIMAL': '#22c55e'
                }
                
                color = insight_colors.get(severity, '#4CA1A3')
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}20 0%, #FFFFFF 100%); 
                            border-left: 4px solid {color}; 
                            padding: 16px; border-radius: 8px; margin: 16px 0;">
                    <strong style="color: {color};">📱 Digital conditioning: {score:.0f}% ({severity})</strong><br>
                    <span style="color: #273548;">
                        {preview_data['digital_insights']['attention_pattern']}<br>
                        <strong>Specialized approach:</strong> {preview_data['digital_insights']['adaptation_needed']}
                    </span>
                </div>
                """, unsafe_allow_html=True)

    def _render_next_steps_section(self):
        """Render next steps using Streamlit components"""
        contact_info = st.session_state.get('contact_info', {})

        st.markdown("""
        **What happens next:**
    
        1. **Clinical review** (24-48 hours): Licensed therapist analyzes your comprehensive assessment
        2. **Personal contact** (48-72 hours): We reach out via your preferred method  
        3. **Custom protocol** (within 72 hours): Personalized hypnotherapy approach designed for your specific patterns
        
        """)
        
        # Call to action section
        st.markdown("**Ready to start your transformation?**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Schedule direct consultation", "https://calendly.com/laetitiasheppard/discovery")
        with col2:
            st.link_button("Learn about our method", "https://hypnotherapy.streamlit.app")
            
        self._render_value_comparison()

    def _render_value_comparison(self):
        """Render value comparison using Streamlit components"""
        st.markdown("**Price comparison**")
        
        col1, col2, col3 = st.columns([4, 1, 4])
        
        with col1:
            st.markdown("**Traditional therapy** with gradual talk and uncertain outcomes for pattern-based issues")
            st.markdown("**18+ months, ฿15,000+**")
        
        with col2:
            st.markdown("🆚")
        
        with col3:
            st.markdown("**Specialized hypnotherapy** for direct subconscious intervention with 85% success rate")
            st.markdown("**2 to 3 sessions, ~฿3,000-4,000**")
        
        st.info("**Time to initial results: 48-72 hours vs 3-6 months**")

# ---- Main Application Classes ----
class AssessPage:
    """Main application wrapper maintaining compatibility with original interface"""
    
    def __init__(self):
        self.assessment = ComprehensiveBehavioralAssessment()
    
    def render(self):
        # Show admin interface if admin is authenticated
        if st.session_state.get('admin_authenticated', False):
            render_admin_interface()
        self.assessment.render()


# ---- Page Factory Function ----
def create_assess_page():
    """Factory function to create the assessment page"""
    return AssessPage()


# ---- Helper Functions ----
def get_assessment_summary():
    """Get current assessment summary"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results
    return None

def get_pattern_scores():
    """Get current pattern scores"""
    if 'pattern_scores' in st.session_state:
        return st.session_state.pattern_scores
    return {}

def get_digital_analysis():
    """Get algorithmical divide analysis if available"""
    if 'assessment_results' in st.session_state:
        return st.session_state.assessment_results.get('digital_despair_analysis')
    return None

def is_digital_native():
    """Check if current user is assessed as digital native"""
    return st.session_state.get('is_digital_native', False)

def reset_assessment():
    """Reset assessment state"""
    keys_to_reset = [
        'assessment_responses', 'current_question', 'current_phase', 'phase_progress',
        'is_digital_native', 'digital_despair_score', 'digital_severity',
        'triggered_patterns', 'pattern_scores', 'risk_flags', 'assessment_completed', 
        'contact_provided', 'assessment_results', 'intensity_responses', 
        'trigger_chain', 'digital_responses', 'adaptive_paths'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]

def export_assessment_data():
    """Export complete assessment data including digital analysis"""
    if 'assessment_responses' not in st.session_state:
        return None
    
    return {
        'responses': st.session_state.assessment_responses,
        'pattern_scores': st.session_state.get('pattern_scores', {}),
        'intensity_data': st.session_state.get('intensity_responses', {}),
        'triggered_patterns': list(st.session_state.get('triggered_patterns', set())),
        'adaptive_paths': st.session_state.get('adaptive_paths', []),
        'risk_flags': st.session_state.get('risk_flags', []),
        'trigger_chain': st.session_state.get('trigger_chain', {}),
        'digital_responses': st.session_state.get('digital_responses', {}),
        'is_digital_native': st.session_state.get('is_digital_native', False),
        'digital_analysis': st.session_state.get('assessment_results', {}).get('digital_despair_analysis'),
        'phase_progress': st.session_state.get('phase_progress', {}),
        'results': st.session_state.get('assessment_results', {}),
        'contact_info': st.session_state.get('contact_info', {}),
        'completion_timestamp': datetime.now().isoformat()
    }

def create_blueprint_link(session_id):
    """Create shareable link to blueprint"""
    return f"https://yourapp.com/blueprint/{session_id}"

def save_assessment_summary(assessment_data):
    """Save assessment summary for analytics"""
    try:
        summary = {
            'session_id': assessment_data['session_id'],
            'pattern_count': len(assessment_data.get('pattern_scores', {})),
            'completion_rate': assessment_data.get('completion_rate', 0),
            'is_digital_native': assessment_data.get('is_digital_native', False),
            'timestamp': datetime.now().isoformat(),
            'user_email_hash': hashlib.sha256(
                assessment_data.get('contact_info', {}).get('email', '').encode()
            ).hexdigest()[:8]  # Privacy-safe identifier
        }
        
        # Save to analytics database or file
        # Implementation depends on your analytics setup
        
        return True
    except Exception as e:
        print(f"Analytics save failed: {str(e)}")
        return False

def load_blueprint_from_session(session_id):
    """Load existing blueprint by session ID"""
    try:
        cloud_storage = CloudStorage()
        assessment_data = cloud_storage.retrieve_assessment_data(session_id)
        
        if assessment_data:
            return assessment_data
        else:
            return None
            
    except Exception as e:
        print(f"Blueprint loading failed: {str(e)}")
        return None


if __name__ == "__main__":
    st.set_page_config(
        page_title="Enhanced Behavioral Pattern Assessment",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    assessment_page = create_assess_page()
    assessment_page.render()







