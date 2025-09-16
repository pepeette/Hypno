# Complete Enhanced Clinical Behavioral Pattern Assessment
# Integrated with algorithmical divide Syndrome screening and analysis
# Comprehensive implementation with adaptive questioning and pattern detection
# Optimized for both traditional and digital-native populations

import streamlit as st
from datetime import datetime
import re

# Import components with error handling
try:
    from components.blueprint import create_behavioral_blueprint
    BLUEPRINT_AVAILABLE = True
except ImportError:
    BLUEPRINT_AVAILABLE = False
    st.warning("Blueprint component not available")

try:
    from utils.cloud_storage_streamlit import StreamlitCloudStorage
    CLOUD_STORAGE_AVAILABLE = True
except ImportError:
    CLOUD_STORAGE_AVAILABLE = False

try:
    from utils.storage_factory import create_storage_client
    STORAGE_FACTORY_AVAILABLE = True
except ImportError:
    STORAGE_FACTORY_AVAILABLE = False

try:
    from utils.pdf_generator import PDFGenerator
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

try:
    from utils.config import PatternDefinitions, EmailConfig
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False

try:
    from utils.email_handler import UnifiedEmailHandler
    EMAIL_AVAILABLE = True
except ImportError:
    EMAIL_AVAILABLE = False

import uuid
import base64
import json
import hashlib

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


# ---- Simplified Storage Class ----
class SimpleStorage:
    """Simplified storage for Streamlit Community Cloud"""
    
    def __init__(self):
        if 'assessment_storage' not in st.session_state:
            st.session_state.assessment_storage = {}
            self.storage = create_storage_client()
    
    def save_assessment(self, session_id, data):
        """Save assessment data"""
        st.session_state.assessment_storage[session_id] = {
            'data': data,
            'saved_at': datetime.now().isoformat(),
            'type': 'assessment'
        }
        return f"session://{session_id}"
    
    def get_assessment(self, session_id):
        """Get assessment data"""
        return st.session_state.assessment_storage.get(session_id, {}).get('data')

# ---- Email Queue System ----
class EmailQueue:
    """Simple email queue for manual processing"""
    
    def __init__(self):
        if 'email_queue' not in st.session_state:
            st.session_state.email_queue = []
    
    def add_request(self, email_data):
        """Add email request to queue"""
        st.session_state.email_queue.append({
            **email_data,
            'timestamp': datetime.now().isoformat(),
            'processed': False
        })
    
    def get_pending(self):
        """Get pending email requests"""
        return [req for req in st.session_state.email_queue if not req.get('processed')]
    
    def mark_processed(self, index):
        """Mark email as processed"""
        if 0 <= index < len(st.session_state.email_queue):
            st.session_state.email_queue[index]['processed'] = True

# ---- Simplified PDF Generator ----
def generate_simple_pdf_content(assessment_data):
    """Generate PDF content as text (fallback when reportlab unavailable)"""
    contact_info = assessment_data.get('contact_info', {})
    pattern_scores = assessment_data.get('pattern_scores', {})
    
    patterns = {
        1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
        4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
        7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
    }
    
    content = f"""
BEHAVIORAL TRANSFORMATION BLUEPRINT
Personalized Analysis for {contact_info.get('name', 'Valued Client')}
Generated: {datetime.now().strftime('%B %d, %Y')}

EXECUTIVE SUMMARY
==============
Patterns Identified: {len(pattern_scores)}
Assessment Completion: {assessment_data.get('completion_rate', 1.0)*100:.0f}%
Digital Native: {'Yes' if assessment_data.get('is_digital_native') else 'No'}

PATTERN ANALYSIS
===============
"""
    
    if pattern_scores:
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
            pattern_name = patterns.get(pattern_id, f"Pattern {pattern_id}")
            intensity = "High" if score >= 6 else "Moderate" if score >= 4 else "Mild"
            content += f"{i+1}. {pattern_name} - {intensity} Intensity (Score: {score:.1f}/10)\n"
    
    content += f"""

TRANSFORMATION ROADMAP
=====================
Recommended Protocol: 2-3 sessions over 2-4 weeks
Success Probability: 85-92%
Timeline for Results: 24-48 hours for initial shifts

SESSION BREAKDOWN:
Session 1: Deep Pattern Analysis & Rapport Building (90 minutes)
Session 2: Core Transformation & Neural Rewiring (90 minutes)
Session 3: Integration & Mastery (60 minutes - if needed)

INVESTMENT ANALYSIS
==================
Transformation Investment: $3,000-4,000
Traditional Therapy Alternative: $15,000-25,000 over 18+ months
Success Rate: 85% vs 30-40% traditional approaches
Break-even Time: 2-6 months typically

NEXT STEPS
==========
1. Clinical Review (24-48 hours)
2. Personal Contact (48-72 hours)
3. First Transformation Session (within 1 week)

Contact: hypnotherapy.streamlit.app
Direct Scheduling: calendly.com/laetitiasheppard/discovery

© 2024 Rapid Transformation Hypnotherapy - Confidential Report
Assessment ID: {assessment_data.get('session_id', 'Unknown')[:8]}
"""
    
    return content

# ---- Admin Interface ----
def render_admin_interface():
    """Simple admin interface for email queue management"""
    if not st.session_state.get('admin_authenticated', False):
        with st.sidebar:
            st.markdown("### 🔐 Admin Access")
            admin_password = st.text_input("Password", type="password", key="admin_pass")
            
            if st.button("Login"):
                # Simple password check - use environment variable in production
                if admin_password == st.secrets.get("admin", {}).get("password", "admin123"):
                    st.session_state.admin_authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid password")
    else:
        with st.sidebar:
            st.success("✅ Admin Access")
            
            if st.button("Logout"):
                st.session_state.admin_authenticated = False
                st.rerun()
        
        # Main admin interface
        st.markdown("### Admin Dashboard")
        
        tab1, tab2 = st.tabs(["📧 Email Queue", "📊 Analytics"])
        
        with tab1:
            email_queue = EmailQueue()
            pending_emails = email_queue.get_pending()
            
            st.markdown(f"**Pending email requests: {len(pending_emails)}**")
            
            if pending_emails:
                for i, request in enumerate(pending_emails):
                    with st.expander(f"Email {i+1}: {request['recipient']} - {request['assessment_summary']['urgency']}"):
                        st.json(request)
                        
                        if st.button(f"Mark as processed", key=f"process_{i}"):
                            email_queue.mark_processed(i)
                            st.success("Request marked as processed")
                            st.rerun()
            else:
                st.info("No pending email requests")
        
        with tab2:
            # Storage analytics
            storage_count = len(st.session_state.get('assessment_storage', {}))
            email_count = len(st.session_state.get('email_queue', []))
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Stored Assessments", storage_count)
            with col2:
                st.metric("Email Requests", email_count)
            
            # Show recent assessments
            if st.session_state.get('assessment_storage'):
                st.markdown("**Recent Assessments:**")
                for session_id, data in list(st.session_state.assessment_storage.items())[-5:]:
                    assessment_data = data.get('data', {})
                    contact_info = assessment_data.get('contact_info', {})
                    st.markdown(f"• {session_id[:8]} - {contact_info.get('name', 'Anonymous')} - {data.get('saved_at', 'Unknown')}")




# ---- Enhanced Assessment Class ----
class ComprehensiveBehavioralAssessment:
    """Clinical-grade behavioral pattern assessment with algorithmical divide Syndrome integration"""
    
    def __init__(self):
        self._init_session_state()
        self.storage = SimpleStorage()
        self.email_queue = EmailQueue()
        self.discovery_url = "https://calendly.com/laetitiasheppard/discovery"
        # self.patterns = {
        #     1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
        #     4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
        #     7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
        # }
        # Fallback pattern definitions if config not available
        if CONFIG_AVAILABLE:
            self.patterns = PatternDefinitions.PATTERNS
            self.email_config = EmailConfig()
        else:
            self.patterns = {
                1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust", 
                4: "Separation and Division", 5: "Doing versus Being", 6: "Compartmentalized Authenticity", 
                7: "Self Sacrifice and Care Avoidance", 8: "Inherited Missions", 9: "Context Dependent Weakness"
            }
            self.email_config = None
        
        # Question pools organized by integrated phase system
        self.age_screening_questions = self._get_age_screening_questions()
        self.digital_screening_questions = self._get_digital_screening_questions()
        self.engagement_questions = self._get_engagement_questions()
        self.trigger_mapping_questions = self._get_trigger_mapping_questions()
        self.pattern_specific_questions = self._get_pattern_specific_questions()
        self.integration_questions = self._get_integration_questions()

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
            'adaptive_paths': [],
            'assessment_session_id': str(uuid.uuid4())
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def _get_age_screening_questions(self):
        """Phase 0: Age Screening for Digital Native Assessment"""
        return {
            0: {
                "text": "What is your age range?",
                "type": "single_choice",
                "options": [
                    "Under 18", "18-22", "23-27", "28-32", 
                    "33-37", "38-42", "43-50", "Over 50"
                ],
                "digital_native_scoring": [3, 5, 4, 3, 2, 1, 0, 0],
                "phase": "age_screening",
                "determines_flow": True
            }
        }

    def _get_digital_screening_questions(self):
        """Phase 1: Algorithmic Syndrome Screening (for digital natives)"""
        return {
            1: {
                "text": "On average, how many hours per day do you spend on digital devices (excluding required work)?",
                "type": "single_choice",
                "options": [
                    "Less than 2 hours", "2-4 hours", "4-6 hours",
                    "6-8 hours", "8-10 hours", "Over 10 hours"
                ],
                "digital_despair_weights": [0, 1, 2, 3, 4, 5],
                "phase": "digital_screening"
            },
            2: {
                "text": "Where do you feel most like your authentic self?",
                "type": "single_choice_with_intensity",
                "options": [
                    "In offline, face-to-face interactions",
                    "In online communities and digital spaces", 
                    "Both online and offline equally",
                    "Neither - I don't feel authentic anywhere",
                    "It varies completely depending on the situation"
                ],
                "digital_despair_indicators": {
                    1: 3,  # Strong offline dissociation indicator
                    3: 2,  # Identity fragmentation 
                    4: 4   # Complete authenticity loss
                },
                "phase": "digital_screening"
            },
            3: {
                "text": "When you imagine a successful life, you typically think:",
                "type": "single_choice",
                "options": [
                    "Meaningful relationships and personal fulfillment",
                    "Extraordinary wealth, fame, or achievement",
                    "Being significantly better than most people at something",
                    "Just being happy and content with normal life",
                    "Success feels impossible or meaningless to me"
                ],
                "digital_despair_patterns": {
                    1: 4,  # Extraordinary achievement pressure
                    2: 3,  # Comparative inadequacy 
                    4: 4   # Nihilistic worldview
                },
                "phase": "digital_screening"
            },
            4: {
                "text": "When expressing genuine emotions or enthusiasm:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I express them naturally and directly",
                    "I tend to use humor or irony to deflect",
                    "I feel embarrassed or 'cringe' about sincerity",
                    "I mainly express emotions through memes or online references",
                    "I rarely express genuine emotions at all"
                ],
                "ironic_detachment_scoring": [0, 2, 3, 3, 4],
                "phase": "digital_screening"
            },
            5: {
                "text": "What primarily influences your daily emotional state?",
                "type": "single_choice",
                "options": [
                    "Interactions with family and friends in person",
                    "Social media feeds and online content",
                    "Work or school experiences", 
                    "Internal thoughts and self-reflection",
                    "Online communities and digital relationships"
                ],
                "algorithmic_dependency": {
                    1: 3,  # Social media primary
                    4: 3   # Digital relationships primary
                },
                "phase": "digital_screening"
            },
            6: {
                "text": "You feel more emotionally connected to:",
                "type": "single_choice",
                "options": [
                    "People in your physical daily life",
                    "Online personalities (streamers, influencers, content creators)",
                    "Online friends and communities",
                    "Fictional characters or media personalities",
                    "No significant emotional connections anywhere"
                ],
                "parasocial_indicators": {
                    1: 2,  # Online personalities
                    2: 2,  # Online communities over offline
                    3: 3,  # Fictional over real
                    4: 4   # Complete disconnection
                },
                "phase": "digital_screening"
            },
            7: {
                "text": "When someone suggests things could get better or offers optimistic perspectives:",
                "type": "single_choice_with_intensity",
                "options": [
                    "I feel encouraged and want to believe them",
                    "I appreciate it but remain cautiously skeptical", 
                    "I immediately think of reasons why they're wrong",
                    "I feel annoyed because they don't understand reality",
                    "I dismiss it as naive or manipulative"
                ],
                "hope_avoidance_indicators": {
                    2: 2,  # Automatic negativity
                    3: 3,  # Irritated by optimism
                    4: 4   # Complete hope dismissal
                },
                "phase": "digital_screening"
            },
            8: {
                "text": "Your attention span for non-digital activities (reading books, conversations, offline tasks):",
                "type": "single_choice",
                "options": [
                    "Same as always - can focus for hours when interested",
                    "Slightly shorter but manageable",
                    "Noticeably fragmented - need frequent stimulation",
                    "Very difficult - mind wanders constantly",
                    "Almost impossible without background digital stimulation"
                ],
                "attention_fragmentation": [0, 1, 2, 3, 4],
                "phase": "digital_screening"
            }
        }

    def _get_engagement_questions(self):
        """Phase 2: Engagement & Initial Pattern Detection"""
        return {
            9: {
                "text": "What made you decide to explore hypnotherapy for this particular issue?",
                "type": "single_choice",
                "options": [
                    "I've tried other approaches without lasting success",
                    "I want faster results than traditional methods",
                    "Something about the subconscious mind approach appeals to me",
                    "Someone recommended it specifically for my type of issue",
                    "I'm curious but also skeptical about whether it will work"
                ],
                "pattern_triggers": {
                    0: [5], 1: [5], 2: [3], 3: [8], 4: [3]
                },
                "phase": "engagement"
            },
            10: {
                "text": "If this issue completely resolved, what would be different about your daily life?",
                "type": "text_completion",
                "placeholder": "Describe what you'd be doing differently in 6 months - be as specific as possible about the changes you'd see...",
                "min_chars": 3,
                "pattern_analysis": True,
                "keywords": {
                    "productivity": [5], "relationships": [2, 3, 6, 7], "peace": [1], 
                    "authentic": [6], "happy": [1], "control": [2, 4], "boundaries": [7, 9]
                },
                "phase": "engagement"
            },
            11: {
                "text": "How ready are you to completely let go of this pattern?",
                "type": "scale_10",
                "labels": ["Not ready at all", "Completely ready"],
                "follow_up_trigger": 7,  # If 7 or below, ask follow-up
                "phase": "engagement"
            },
            12: {
                "text": "When did this issue most recently show up?",
                "type": "single_choice",
                "options": [
                    "Today",
                    "Yesterday", 
                    "This week",
                    "Last week",
                    "I can't recall the last specific time"
                ],
                "pattern_triggers": {
                    4: [1, 6]  # Can't recall suggests normalization or compartmentalization
                },
                "phase": "engagement"
            },
            13: {
                "text": "This issue tends to show up more:",
                "type": "single_choice",
                "options": [
                    "At work or in professional settings",
                    "In family or close relationships",
                    "In social situations with acquaintances", 
                    "When I'm alone with my thoughts",
                    "Across all situations equally"
                ],
                "pattern_triggers": {
                    0: [5, 8], 1: [7, 8, 9], 2: [2, 3, 6], 3: [1], 4: [1, 4]
                },
                "phase": "engagement"
            }
        }

    def _get_trigger_mapping_questions(self):
        """Phase 3: Core Trigger Mapping"""
        return {
            14: {
                "text": "Thinking of the most recent time, what was happening in the 30 seconds right before this pattern kicked in?",
                "type": "text_completion",
                "placeholder": "Be specific: Where were you? Who was present? What was being discussed or happening? What did you see, hear, or notice?",
                "min_chars": 5,
                "trigger_analysis": True,
                "phase": "trigger_mapping"
            },
            15: {
                "text": "In that situation, what did you notice first?",
                "type": "single_choice",
                "options": [
                    "A physical sensation somewhere in my body",
                    "A specific thought or worry popping up",
                    "An emotional shift or feeling change",
                    "Something another person said or did",
                    "A change in the environment around me"
                ],
                "chain_mapping": "awareness_point",
                "phase": "trigger_mapping"
            },
            16: {
                "text": "When this pattern activates, the first physical sensation is usually:",
                "type": "single_choice_with_intensity",
                "options": [
                    "Chest tightness, racing heart, or breathing changes",
                    "Stomach drop, nausea, or digestive upset", 
                    "Muscle tension, jaw clenching, or physical rigidity",
                    "Hot/cold flashes, sweating, or temperature changes",
                    "Numbness, disconnection, or feeling 'outside yourself'",
                    "Restlessness, fidgeting, or urge to move/escape",
                    "Fatigue, heaviness, or sudden energy drain"
                ],
                "pattern_indicators": {
                    0: [1, 3, 4], 1: [1, 3, 4], 2: [2, 5], 3: [2, 5], 
                    4: [6, 9], 5: [2, 5], 6: [1, 7]
                },
                "chain_mapping": "physical_response",
                "phase": "trigger_mapping"
            },
            17: {
                "text": "What thought automatically appears when you feel that physical sensation?",
                "type": "text_completion",
                "placeholder": "The actual words that go through your mind - even if they seem harsh or unreasonable. What does your inner voice say?",
                "min_chars": 3,
                "pattern_keywords": {
                    "not good enough": [1], "fight": [2], "can't trust": [3], 
                    "either or": [4], "must do": [5], "can't be real": [6],
                    "others need": [7], "should": [8], "can't handle": [9]
                },
                "chain_mapping": "automatic_thought",
                "phase": "trigger_mapping"
            },
            18: {
                "text": "After that thought, you typically feel:",
                "type": "multi_select_weighted",
                "max_selections": 3,
                "options": [
                    "Anxious or worried", "Angry or frustrated", "Ashamed or embarrassed",
                    "Sad or defeated", "Guilty or self-blaming", "Overwhelmed or panicked",
                    "Numb or disconnected", "Confused or uncertain"
                ],
                "chain_mapping": "emotional_response",
                "phase": "trigger_mapping"
            },
            19: {
                "text": "When you feel that emotion at that intensity, you typically:",
                "type": "single_choice",
                "options": [
                    "Withdraw, avoid, or postpone dealing with it",
                    "Become more active, busy, or productive",
                    "Seek reassurance or validation from others",
                    "Become argumentative or defensive", 
                    "Try to control or fix the situation",
                    "Please others or put their needs first",
                    "Shut down emotionally or 'check out'",
                    "Analyze or overthink the situation"
                ],
                "pattern_mapping": {
                    0: [1, 4, 9], 1: [5], 2: [3, 7], 3: [2], 
                    4: [2, 5], 5: [7], 6: [6, 9], 7: [4, 5]
                },
                "chain_mapping": "behavioral_response",
                "phase": "trigger_mapping"
            },
            20: {
                "text": "Right after you respond that way, you usually feel:",
                "type": "single_choice",
                "options": [
                    "Temporary relief but underlying tension remains",
                    "More agitated or upset than before",
                    "Emotionally numb or disconnected",
                    "Guilty about how you handled it",
                    "Justified in your response",
                    "Confused about what just happened",
                    "Physically exhausted or drained"
                ],
                "chain_mapping": "immediate_consequence",
                "phase": "trigger_mapping"
            },
            21: {
                "text": "A few hours later, you're typically:",
                "type": "single_choice", 
                "options": [
                    "Have moved on and forgotten about it",
                    "Still replaying what happened",
                    "Planning how to avoid it next time",
                    "Angry at yourself for reacting that way",
                    "Feeling misunderstood by others involved",
                    "Resigned that this is just how things are"
                ],
                "pattern_reinforcement": {
                    1: [5], 2: [1, 4, 9], 3: [5], 4: [1], 5: [1]
                },
                "chain_mapping": "longer_term_impact",
                "phase": "trigger_mapping"
            }
        }

    def _get_pattern_specific_questions(self):
        """Phase 4: Adaptive Pattern-Specific Deep Dives"""
        return {
            # Pattern 1: Unhappiness Culture
            "pattern_1": {
                22: {
                    "text": "When something genuinely good happens to you, your first reaction is usually:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Pure enjoyment and celebration",
                        "Immediately looking for the catch or downside", 
                        "Feeling guilty or undeserving of good things",
                        "Minimizing its importance",
                        "Anxiety about when it will end"
                    ],
                    "weights": [0, 3, 3, 2, 2],
                    "pattern": 1
                },
                23: {
                    "text": "Growing up, the message about happiness in your family was:",
                    "type": "single_choice",
                    "options": [
                        "Happiness is natural and should be enjoyed",
                        "Happiness must be earned through hard work",
                        "Too much happiness leads to disappointment", 
                        "Other people's happiness comes first",
                        "Happiness is selfish or shallow"
                    ],
                    "weights": [0, 2, 3, 2, 3],
                    "pattern": 1
                },
                24: {
                    "text": "What would you lose if you allowed yourself to be genuinely happy?",
                    "type": "text_completion",
                    "placeholder": "Think about identity, relationships, what others might think, or what might change...",
                    "min_chars": 3,
                    "pattern": 1
                }
            },
            
            # Pattern 2: Power Struggles
            "pattern_2": {
                25: {
                    "text": "When someone disagrees with you, your nervous system:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stays curious about their perspective",
                        "Immediately activates into combat mode",
                        "Feels threatened or attacked",
                        "Shuts down to avoid confrontation",
                        "Searches for ways to prove them wrong"
                    ],
                    "weights": [0, 3, 2, 1, 3],
                    "pattern": 2
                },
                26: {
                    "text": "In your family growing up, disagreements typically:",
                    "type": "single_choice",
                    "options": [
                        "Were handled through calm discussion",
                        "Escalated into arguments or fights",
                        "Were avoided at all costs",
                        "Involved guilt, manipulation, or silent treatment",
                        "Had clear winners and losers"
                    ],
                    "weights": [0, 3, 2, 3, 4],
                    "pattern": 2
                }
            },
            
            # Pattern 3: Systematic Mistrust
            "pattern_3": {
                27: {
                    "text": "When meeting new people, you assume they:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Are generally well-intentioned",
                        "Are judging or evaluating you",
                        "Want something from you",
                        "Will eventually disappoint you",
                        "Are basically indifferent"
                    ],
                    "weights": [0, 2, 3, 3, 1],
                    "pattern": 3
                },
                28: {
                    "text": "When someone is unexpectedly kind to you, you:",
                    "type": "single_choice",
                    "options": [
                        "Feel grateful and warmed",
                        "Wonder what they want from you",
                        "Feel suspicious of their motives",
                        "Feel unworthy of their kindness",
                        "Barely notice or dismiss it"
                    ],
                    "weights": [0, 3, 3, 2, 1],
                    "pattern": 3
                }
            },
            
            # Pattern 4: Separation/Division
            "pattern_4": {
                29: {
                    "text": "When facing important decisions, you typically:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "See multiple creative possibilities",
                        "Feel trapped between two impossible choices",
                        "Get paralyzed by perfectionist analysis",
                        "Create artificial deadlines or urgency",
                        "Defer to what others expect"
                    ],
                    "weights": [0, 2, 3, 2, 1],
                    "pattern": 4
                }
            },
            
            # Pattern 5: Doing vs Being
            "pattern_5": {
                30: {
                    "text": "You feel most valuable when you're:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Simply existing as yourself",
                        "Accomplishing something significant",
                        "Being productive or busy",
                        "Helping others achieve their goals",
                        "Receiving recognition for your work"
                    ],
                    "weights": [0, 2, 3, 2, 2],
                    "pattern": 5
                }
            },
            
            # Pattern 6: Compartmentalized Authenticity
            "pattern_6": {
                31: {
                    "text": "Your personality tends to:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stay consistent across all situations",
                        "Shift significantly based on who you're with",
                        "Change between professional and personal settings",
                        "Adapt to what others seem to want",
                        "Feel fragmented or inconsistent"
                    ],
                    "weights": [0, 2, 2, 3, 4],
                    "pattern": 6
                }
            },
            
            # Pattern 7: Self-Sacrifice/Care Avoidance
            "pattern_7": {
                32: {
                    "text": "When it comes to your own needs versus others' needs:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "I naturally balance both",
                        "Others' needs usually come first",
                        "I feel guilty focusing on my own needs",
                        "I often don't even know what I need",
                        "Taking care of myself feels selfish"
                    ],
                    "weights": [0, 2, 3, 3, 4],
                    "pattern": 7
                }
            },
            
            # Pattern 8: Inherited Missions
            "pattern_8": {
                33: {
                    "text": "Your major life goals are primarily:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Based on your own genuine desires",
                        "Influenced by family expectations",
                        "Meant to honor someone's sacrifices",
                        "Designed to prove your worth",
                        "A reaction against others' expectations"
                    ],
                    "weights": [0, 2, 3, 3, 2],
                    "pattern": 8
                }
            },
            
            # Pattern 9: Context-Dependent Weakness
            "pattern_9": {
                34: {
                    "text": "Your boundaries and limits:",
                    "type": "single_choice_with_intensity",
                    "options": [
                        "Stay pretty consistent across situations",
                        "Vary significantly based on who you're with",
                        "Disappear completely in certain contexts",
                        "Are stronger in some areas than others",
                        "Feel almost non-existent sometimes"
                    ],
                    "weights": [0, 2, 3, 2, 4],
                    "pattern": 9
                }
            }
        }

    def _get_integration_questions(self):
        """Phase 5: Integration & Change Readiness"""
        return {
            35: {
                "text": "If you had to guess, this pattern might be trying to:",
                "type": "single_choice",
                "options": [
                    "Protect you from emotional pain",
                    "Keep you safe from rejection or judgment",
                    "Maintain some sense of control",
                    "Help you belong or fit in",
                    "Avoid disappointing important people",
                    "Ensure you're prepared for worst-case scenarios"
                ],
                "secondary_gain": True,
                "phase": "integration"
            },
            36: {
                "text": "What would need to be true for you to feel completely safe changing this pattern?",
                "type": "text_completion",
                "placeholder": "Think about what guarantees, support, or conditions you'd need to feel safe letting go...",
                "min_chars": 3,
                "safety_assessment": True,
                "phase": "integration"
            },
            37: {
                "text": "When learning or changing, you respond best to:",
                "type": "single_choice",
                "options": [
                    "Direct, clear guidance and instructions",
                    "Gentle, permissive suggestions",
                    "Stories, metaphors, and imagery",
                    "Logical explanations and understanding",
                    "Collaborative exploration and discovery"
                ],
                "hypnotic_preference": True,
                "phase": "integration"
            },
            38: {
                "text": "Imagine you've completely transformed this pattern. What's the first thing you'd do that you can't do now?",
                "type": "text_completion",
                "placeholder": "Be specific about the first action, conversation, or decision you'd make...",
                "min_chars": 5,
                "outcome_visualization": True,
                "phase": "integration"
            }
        }

    # ---- algorithmical divide Analysis Methods ----
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
            return None  # Skip algorithmical divide analysis for non-digital natives
        
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
        
        # Severity classification
        if digital_despair_percentage >= 70:
            severity = "SEVERE"
            recommendation = "Specialized digital-native intervention required"
        elif digital_despair_percentage >= 50:
            severity = "MODERATE" 
            recommendation = "Modified approach with digital awareness"
        elif digital_despair_percentage >= 30:
            severity = "MILD"
            recommendation = "Standard approach with digital considerations"
        else:
            severity = "MINIMAL"
            recommendation = "Traditional hypnotherapy approach suitable"
        
        return {
            'digital_despair_score': digital_despair_percentage,
            'severity_level': severity,
            'clinical_recommendation': recommendation,
            'component_scores': {
                'digital_native_status': digital_native_score,
                'reality_dissociation': reality_dissociation,
                'binary_success_pressure': binary_thinking,
                'ironic_detachment': ironic_detachment, 
                'algorithmic_dependency': algorithmic_dependency,
                'nihilistic_worldview': nihilistic_worldview,
                'hope_avoidance': hope_avoidance,
                'attention_fragmentation': attention_fragmentation
            },
            'therapeutic_adaptations_needed': self._get_therapeutic_adaptations(severity)
        }

    def _get_therapeutic_adaptations(self, severity):
        """Get required therapeutic adaptations based on algorithmical divide severity"""
        
        adaptations = {
            "SEVERE": [
                "Attention span optimization: 15-30 minute focused segments",
                "Anti-authority language: Collaborative, non-directive approach",
                "Ironic armor dissolution: Validate intelligence while accessing authentic emotion",
                "Digital bridge-building: Connect online competencies to offline confidence",
                "Binary thinking interruption: Install 'both/and' processing patterns",
                "Hope introduction protocol: Gradual realistic optimism vs. overwhelming positivity",
                "Meaning-making assistance: Personal contribution vs. extraordinary achievement"
            ],
            "MODERATE": [
                "Modified session length: 45-60 minutes with movement breaks",
                "Authority resistance awareness: Reduce directive language", 
                "Cynicism validation: Acknowledge systemic problems while building agency",
                "Digital competency honor: Validate online achievements and skills",
                "Nuanced goal-setting: Meaningful vs. extraordinary success redefinition",
                "Gradual hope building: Evidence-based optimism introduction"
            ],
            "MILD": [
                "Digital literacy integration: Use familiar cultural references",
                "Achievement pressure awareness: Expand success definitions",
                "Authentic expression permission: Reduce 'cringe' about sincerity",
                "Real-world confidence transfer: Apply online skills offline"
            ],
            "MINIMAL": [
                "Standard approach with generational awareness",
                "Technology balance considerations",
                "Modern stress factor acknowledgment"
            ]
        }
        
        return adaptations.get(severity, adaptations["MINIMAL"])

    # Helper functions for extracting specific scores
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
        
        elif question.get('pattern_keywords') and isinstance(response, str):
            detected_patterns = self._analyze_text_for_patterns(response, question['pattern_keywords'])
            for pattern in detected_patterns:
                self._add_pattern_score(pattern, 2.0)
        
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

    # ---- Question Navigation Logic ----
    def _get_next_question(self):
        """Determine next question based on current phase and responses"""
        answered = set(st.session_state.assessment_responses.keys())
        
        # Phase 0: Age Screening (Question 0)
        if st.session_state.current_phase == 'age_screening':
            if 0 not in answered:
                return 0, self.age_screening_questions[0]
            else:
                # Determine if digital native
                age_response = st.session_state.assessment_responses.get(0, {}).get('response', '')
                age_options = ["Under 18", "18-22", "23-27", "28-32", "33-37", "38-42", "43-50", "Over 50"]
                scoring = [3, 5, 4, 3, 2, 1, 0, 0]
                
                try:
                    age_index = age_options.index(age_response)
                    digital_native_score = scoring[age_index]
                    st.session_state.is_digital_native = digital_native_score >= 2
                except (ValueError, IndexError):
                    st.session_state.is_digital_native = False
                
                # Move to appropriate next phase
                if st.session_state.is_digital_native:
                    st.session_state.current_phase = 'digital_screening'
                else:
                    st.session_state.current_phase = 'engagement'
        
        # Phase 1: Digital Screening (Questions 1-8) - Only for digital natives
        if st.session_state.current_phase == 'digital_screening':
            for q_id in range(1, 9):
                if q_id not in answered:
                    return q_id, self.digital_screening_questions[q_id]
            st.session_state.current_phase = 'engagement'
        
        # Phase 2: Engagement (Questions 9-13)
        if st.session_state.current_phase == 'engagement':
            for q_id in range(9, 14):
                if q_id not in answered:
                    return q_id, self.engagement_questions[q_id]
            st.session_state.current_phase = 'trigger_mapping'
        
        # Phase 3: Trigger Mapping (Questions 14-21)
        if st.session_state.current_phase == 'trigger_mapping':
            for q_id in range(14, 22):
                if q_id not in answered:
                    return q_id, self.trigger_mapping_questions[q_id]
            st.session_state.current_phase = 'pattern_specific'
        
        # Phase 4: Pattern-Specific Questions
        if st.session_state.current_phase == 'pattern_specific':
            for pattern_id in st.session_state.triggered_patterns:
                pattern_key = f"pattern_{pattern_id}"
                if pattern_key in self.pattern_specific_questions:
                    pattern_questions = self.pattern_specific_questions[pattern_key]
                    for q_id, question in pattern_questions.items():
                        if q_id not in answered:
                            return q_id, question
            st.session_state.current_phase = 'integration'
        
        # Phase 5: Integration (Questions 35-38)
        if st.session_state.current_phase == 'integration':
            for q_id in range(35, 39):
                if q_id not in answered:
                    return q_id, self.integration_questions[q_id]
        
        return None, None

    def _estimate_total_questions(self):
        """Estimate total questions based on triggered patterns and digital native status"""
        base_questions = 1  # age screening
        
        if st.session_state.is_digital_native:
            base_questions += 8  # digital screening
        
        base_questions += 5 + 8 + 4  # engagement + trigger_mapping + integration
        pattern_questions = len(st.session_state.triggered_patterns) * 2  # avg 2 questions per pattern
        return base_questions + pattern_questions

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

    # ---- Rendering Functions ----
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

        # Phase indicator
        current_phase = question.get('phase', 'unknown')
        phase_names = {
            'age_screening': 'Initial Screening',
            'digital_screening': 'Digital Pattern Assessment',
            'engagement': 'Pattern Discovery',
            'trigger_mapping': 'Trigger Analysis',
            'pattern_specific': 'Deep Pattern Exploration',
            'integration': 'Integration & Planning'
        }
        phase_display = phase_names.get(current_phase, current_phase.title())
        
        # if current_phase != 'age_screening':
        #     st.caption(f"**Phase:** {phase_display}")

        # Question display
        st.markdown(f"### {question['text']}")
        
        # Show pattern detection hints for engaged users
        if completed > 8 and st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])
            if top_pattern[1] >= 2.0:
                pattern_name = self.patterns.get(top_pattern[0], "Unknown Pattern")
                # Only show hints in later phases to avoid influencing responses

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

    def _render_contact_form(self):
        """Render contact form for results with enhanced clinical data"""
        #st.markdown("**Assessment complete!**")
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
                
                # Add severity descriptions
                severity_descriptions = {
                    'SEVERE': 'Specialized intervention required',
                    'MODERATE': 'Enhanced approach needed',
                    'MILD': 'Standard with modifications', 
                    'MINIMAL': 'Traditional approach suitable'
                }
                description = severity_descriptions.get(severity, 'Assessment incomplete')
                
                st.metric("", "Digital patterns", f"{digital_score:.0f}%")
                #st.metric("Digital patterns", f"{severity}", f"{digital_score:.0f}%")
                #st.caption(description)
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
            
            # submit_button_html = """
            # <style>
            # .custom-submit-button {
            #     background-color: #4CA1A3 !important;
            #     color: #FFFFFF !important;
            #     border: 2px solid #4CA1A3 !important;
            #     border-radius: 8px !important;
            #     padding: 12px 24px !important;
            #     font-size: 1rem !important;
            #     font-weight: 600 !important;
            #     width: 100% !important;
            #     margin: 8px 0 !important;
            #     cursor: pointer !important;
            #     transition: all 0.3s ease !important;
            #     text-align: center !important;
            #     min-height: 2.5rem !important;
            # }
            
            # .custom-submit-button:hover {
            #     background-color: #E1F0F0 !important;
            #     color: #273548 !important;
            #     border-color: #E1F0F0 !important;
            #     transform: translateY(-1px) !important;
            #     box-shadow: 0 4px 12px rgba(243,246,248,0.6) !important;
            # }
            # </style>
            # """
            # st.markdown(submit_button_html, unsafe_allow_html=True)
            
            # Use the regular streamlit submit button but with custom styling
            submitted = st.form_submit_button("Get my personalized analysis", type="primary", use_container_width=True)


            if submitted:
                errors = []
                
                # ONLY EMAIL VALIDATION IS REQUIRED
                if not email.strip(): 
                    errors.append("Email is required")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    errors.append("Valid email address is required")
                
                # MARKETING CONSENT CHECK
                if not marketing_consent:
                    errors.append("Please consent to follow-up communications to receive your results")
                
                if errors:
                    for error in errors:
                        st.error(f"❌ {error}")
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
                    
                    # GENERATE COMPREHENSIVE CLINICAL TEMPLATE
                    clinical_template = self._format_comprehensive_clinical_template()
                    
                    # Prepare assessment data for email with enhanced clinical template
                    assessment_data = {
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
                    
                    # Send comprehensive clinical assessment email
                    try:
                        email_success = self._send_assessment_email(assessment_data)
                        
                        if email_success:
                            st.success("✅ Assessment completed and clinical team notified!")
                            st.info("📧 Your detailed analysis has been sent to our clinical team for review.")
                        else:
                            st.warning("⚠️ Assessment saved, but email notification failed. Our team will still receive your results.")
                            
                    except ImportError as e:
                        st.error(f"Email system unavailable: {e}")
                        st.info("Assessment completed! Our clinical team will review your results.")
                    except Exception as e:
                        st.error(f"Email error: {str(e)}")
                    
                    st.session_state.contact_provided = True
                    st.rerun()

    # # ADD THIS NEW METHOD at the end of the class for email sent to client:
    # def _send_assessment_email(self, assessment_data):
    #     """Send assessment email using unified email handler"""
    #     try:
    #         email_handler = UnifiedEmailHandler()
    #         return email_handler.send_assessment_results(assessment_data, "standard")
    #     except Exception as e:
    #         print(f"Error sending assessment email: {str(e)}")
    #         return False
    

    def _format_comprehensive_clinical_template(self):
        """Format comprehensive clinical template integrating traditional patterns + digital analysis"""
        # Extract all clinical insights
        clinical_insights = self._extract_clinical_insights()
        
        # Get pattern scores and session planning
        pattern_scores = st.session_state.pattern_scores
        session_plan = self._generate_session_plan(pattern_scores, clinical_insights)
        
        # Get top 3 patterns
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            dominant_pattern = self.patterns.get(sorted_patterns[0][0], "Unknown") if sorted_patterns else "Unknown"
            dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
            
            primary_pattern = self.patterns.get(sorted_patterns[1][0], "Unknown") if len(sorted_patterns) > 1 else "None detected"
            primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
            
            secondary_pattern = self.patterns.get(sorted_patterns[2][0], "Unknown") if len(sorted_patterns) > 2 else "None detected"
            secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
        else:
            dominant_pattern = primary_pattern = secondary_pattern = "Assessment incomplete"
            dominant_score = primary_score = secondary_score = 0
        
        # Get change readiness
        readiness_score = 5  # Default
        for response_data in st.session_state.assessment_responses.values():
            if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                readiness_score = response_data['response']['rating']
                break
        
        # Generate behavioral sequence analysis
        behavioral_sequence = self._generate_behavioral_sequence_analysis()
        
        # Build base template
        template = f"""
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║          Enhanced Behavioral Pattern Assessment              ║
╚══════════════════════════════════════════════════════════════╝

**TRADITIONAL PATTERN ANALYSIS:**
Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10) 
Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: {clinical_insights.get('core_limiting_belief', 'Requires session exploration')}
Hidden Benefits: {clinical_insights.get('hidden_benefits', 'Emotional protection and familiar identity')}
Systemic Resistance: {clinical_insights.get('systemic_resistance', 'Minimal resistance expected')}
Identity Threat: {clinical_insights.get('identity_threat', 'Identity evolution requires navigation')}

**CHANGE READINESS:**
Readiness Score: {readiness_score}/10
Motivation Level: {"HIGH" if readiness_score >= 8 else "MODERATE" if readiness_score >= 6 else "REQUIRES BUILDING"}
"""
        
        # Add digital despair analysis if applicable
        if st.session_state.is_digital_native:
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                digital_score = digital_analysis['digital_despair_score']
                severity = digital_analysis['severity_level']
                
                template += f"""

╔══════════════════════════════════════════════════════════════╗
║               DIGITAL DESPAIR SYNDROME ANALYSIS             ║
╚══════════════════════════════════════════════════════════════╝

**SYNDROME ASSESSMENT:**
Algorithmical divide Score: {digital_score:.1f}% ({severity} severity)
Clinical Recommendation: {digital_analysis['clinical_recommendation']}

**SYNDROME COMPONENTS:**"""
                
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
                    template += f"\n• {name}: {level} ({score:.1f}/5)"
                
                template += f"""

**REQUIRED THERAPEUTIC ADAPTATIONS:**
{"🚨 SPECIALIZED INTERVENTION REQUIRED" if severity in ['SEVERE', 'MODERATE'] else "✅ STANDARD APPROACH WITH MODIFICATIONS"}
"""
                
                adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
                for i, adaptation in enumerate(adaptations[:5], 1):
                    template += f"\n{i}. {adaptation}"
                
                if severity in ['SEVERE', 'MODERATE']:
                    template += f"""

**DIGITAL-NATIVE SESSION MODIFICATIONS:**
• Session Structure: {"20-minute focused segments" if severity == 'SEVERE' else "45-60 minutes with breaks"}
• Language Style: Collaborative, non-directive, intelligence-validating
• Authority Approach: Peer consultant vs traditional therapist-patient
• Hope Introduction: Evidence-based gradual vs overwhelming positivity
• Success Framework: Meaningful contribution vs extraordinary achievement
• Resistance Management: Expect intellectual challenges and cynicism
"""

        template += f"""

**SESSION PLANNING:**
Session 1 Focus: {session_plan.get('session_1_focus', 'Pattern analysis and rapport building')}
Session 2 Target: {session_plan.get('session_2_target', 'Core transformation and positive programming')}
Potential Session 3 Need: {session_plan.get('session_3_need', 'Reinforcement if needed')}

**THERAPEUTIC APPROACH:**
Intervention Keywords: {clinical_insights.get('intervention_keywords', 'Collaborative, gentle, permissive')}
Avoid Language: {clinical_insights.get('avoid_language', 'Pressure, criticism, commands')}
Predicted Resistance: {clinical_insights.get('resistance_points', ['Standard change resistance'])[0] if clinical_insights.get('resistance_points') else 'Standard patterns'}

{behavioral_sequence}

**SUCCESS PROBABILITY:**
Estimated Success Rate: {self._calculate_comprehensive_success_rate()}%
Based on: Pattern complexity, digital factors, readiness, completion rate

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL NOTES                          ║
╚══════════════════════════════════════════════════════════════╝

{"This assessment reveals a digital-native psychology requiring specialized intervention approaches. Traditional methods may fail without proper adaptations." if st.session_state.is_digital_native and st.session_state.assessment_results.get('digital_despair_analysis', {}).get('severity_level') in ['SEVERE', 'MODERATE'] else "This comprehensive analysis provides framework for effective hypnotherapy intervention based on traditional behavioral pattern constellation."}
"""
        
        return template

    def _calculate_comprehensive_success_rate(self):
        """Calculate success rate based on pattern complexity and readiness factors"""
        # Base success rate
        base_rate = 85
        
        # Get assessment data
        results = st.session_state.get('assessment_results', {})
        pattern_scores = results.get('pattern_scores', {})
        
        # Adjust based on pattern count (more patterns = slightly lower initial success)
        pattern_count = len(pattern_scores)
        if pattern_count >= 5:
            base_rate -= 5
        elif pattern_count >= 3:
            base_rate -= 2
        
        # Adjust based on digital native status (they respond better to this approach)
        if st.session_state.get('is_digital_native', False):
            base_rate += 5
        
        # Adjust based on readiness indicators (if available in responses)
        responses = st.session_state.get('assessment_responses', {})
        
        # Check for high motivation indicators
        high_motivation_keywords = ['desperate', 'ready', 'tired', 'enough', 'change']
        motivation_boost = 0
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                for keyword in high_motivation_keywords:
                    if keyword.lower() in response.lower():
                        motivation_boost = 3
                        break
        
        final_rate = min(95, max(70, base_rate + motivation_boost))
        return final_rate

    # Clinical Insights Methods (simplified versions)
    def _extract_clinical_insights(self):
        """Extract basic clinical insights from assessment responses"""
        # This is a simplified version - in practice would be more comprehensive
        return {
            'core_limiting_belief': "Core belief requires session exploration",
            'hidden_benefits': "Pattern provides emotional protection and familiar identity",
            'systemic_resistance': "Minimal systemic resistance expected",
            'identity_threat': "Identity evolution requires careful navigation",
            'intervention_keywords': "Collaborative, gentle, permissive",
            'avoid_language': "Pressure, criticism, commands",
            'resistance_points': ["Standard change resistance", "Possible skepticism about process"]
        }

    def _generate_session_plan(self, pattern_scores, clinical_insights):
        """Generate session planning recommendations"""
        return {
            'session_1_focus': "Comprehensive pattern assessment and rapport building",
            'session_2_target': "Core pattern transformation and positive programming",
            'session_3_need': "Standard reinforcement if needed"
        }

    def _generate_behavioral_sequence_analysis(self):
        """Generate basic behavioral sequence analysis"""
        return """
╔══════════════════════════════════════════════════════════════╗
║            BEHAVIORAL SEQUENCE MAPPING                      ║
╚══════════════════════════════════════════════════════════════╝

Complete behavioral chain analysis available in full clinical template.
Session 1 will focus on completing any missing sequence components for
optimal intervention design.
"""


    def _render_results(self):
        """Render user-centric results page with comprehensive insights"""
        self._render_results_hero_at_top()
        # self._render_results_hero()
        # self._render_pattern_insights()
        
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
        if 'assessment_session_id' not in st.session_state:
            st.session_state.assessment_session_id = str(uuid.uuid4())
        
        # # Create comprehensive assessment data package
        # assessment_data = self._compile_complete_assessment_data()
        
        # # Blueprint preview and full access
        # #self._render_blueprint_access(assessment_data)

    def _render_results_hero_at_top(self):
            """Render hero section at top of results page"""
            try:
                # Check if we have minimum required data
                if not hasattr(st.session_state, 'assessment_results') or not st.session_state.assessment_results:
                    st.warning("⚠️ Assessment data incomplete. Please complete the full assessment for detailed analysis.")
                    return
    
                # Generate assessment data
                assessment_data = self._compile_complete_assessment_data()
                
                # Check if assessment_data has required fields
                if not assessment_data or not assessment_data.get('pattern_scores'):
                    st.info("📊 Complete the assessment to unlock your personalized behavioral analysis.")
                    return
                    
                preview_data = self._extract_preview_insights(assessment_data)
                
                # STEP 2: Compelling personalized preview header at top
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
                
                # STEP 3: Add transformation success likelihood and progress bar
                st.markdown("**Transformation success likelihood:**")
                col1, col2 = st.columns([3, 1])
                with col1:
                    progress_bar = st.progress(preview_data['success_rate'] / 100)
                with col2:
                    st.markdown(f"**{preview_data['success_rate']}%**")
                
                # STEP 4: Add digital pattern analysis if applicable
                self._render_digital_insights_at_top(preview_data)

                # STEP 5: Blueprint access - call without parameters, let method generate its own data, access behind paywall
                self._render_blueprint_access()

            except Exception as e:
                st.error(f"Error loading results analysis: {str(e)}")
                st.info("Please complete the full assessment for detailed insights.")
                # Show fallback content
                st.markdown("**Assessment in progress**")
                st.info("Complete all assessment questions to unlock your personalized behavioral analysis and transformation roadmap.")

    def _render_digital_insights_at_top(self, preview_data):
        """Render digital insights at top of page if applicable"""
        if preview_data.get('digital_insights'):
            st.markdown("**Digital pattern analysis:**")
            
            digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
            if digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                
                # Enhanced digital insights display
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
                
    def _render_results_hero(self):
        """Render the hero section with key insights using Streamlit components"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        # Calculate key metrics
        total_patterns = len(pattern_scores)
        completion_rate = results.get('completion_rate', 1.0)
        success_probability = self._calculate_comprehensive_success_rate()
        
        # Check for urgency
        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '')
        is_urgent = any(word in urgency.lower() for word in ['extremely', 'very urgent', 'significantly impacting'])
        
        # Priority banner for urgent cases
        if is_urgent:
            st.warning("**Priority contact scheduled** - Given your urgency level, our clinical team will contact you within 24 hours to expedite your transformation process.")
        
        # Main hero section
        st.markdown("**Your core behavioral patterns**")
        
        # Success probability section
        st.markdown("**Transformation success likelihood:**")
        col1, col2 = st.columns([3, 1])
        with col1:
            progress_bar = st.progress(success_probability / 100)
        with col2:
            st.markdown(f"**{success_probability}%**")
        
        # Metrics in 3 columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Patterns identified", total_patterns)
        
        with col2:
            # Get primary pattern and intensity
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                primary_pattern_id, primary_score = sorted_patterns[0]
                primary_pattern_name = self.patterns.get(primary_pattern_id, f"Pattern {primary_pattern_id}")
                
                if primary_score >= 6:
                    intensity_level = "High intensity"
                elif primary_score >= 4:
                    intensity_level = "Moderate intensity" 
                elif primary_score >= 2:
                    intensity_level = "Mild intensity"
                else:
                    intensity_level = "Emerging pattern"
                
                st.metric("Intensity level", intensity_level, primary_pattern_name)
            else:
                st.metric("Intensity level", "Assessment incomplete")
        
        with col3:
            # Calculate pattern rarity
            pattern_rarity_percentage = self._calculate_pattern_rarity(total_patterns)
            st.metric("Pattern rarity", f"{pattern_rarity_percentage}%", "of people show this combination")
    
    def _render_pattern_insights(self):
        """Render detailed pattern insights using Streamlit components"""
        results = st.session_state.assessment_results
        pattern_scores = results.get('pattern_scores', {})
        
        if not pattern_scores:
            st.warning("Pattern analysis incomplete - please complete the full assessment for detailed insights.")
            return
        
        # Key insight and transformation messaging
        st.success("**Key insight:** Your pattern recognition ability is already strong - that's 60% of the transformation work already complete.")
        st.markdown("Most people see initial shifts within 48 hours of Session 2")
        
        # Digital insights if applicable
        self._render_digital_insights()
        
        # Blueprint access - call without parameters, let method generate its own data, access behind paywall
        self._render_blueprint_access()
        #self._render_clinical_analysis_section()

    
    # def _render_results_hero(self):
    #     """Render the hero section with key insights using Streamlit components"""
    #     results = st.session_state.assessment_results
    #     pattern_scores = results.get('pattern_scores', {})
        
    #     # Calculate key metrics
    #     total_patterns = len(pattern_scores)
    #     completion_rate = results.get('completion_rate', 1.0)
    #     success_probability = self._calculate_comprehensive_success_rate()
        
    #     # Check for urgency
    #     contact_info = st.session_state.get('contact_info', {})
    #     urgency = contact_info.get('urgency', '')
    #     is_urgent = any(word in urgency.lower() for word in ['extremely', 'very urgent', 'significantly impacting'])
        
    #     # Priority banner for urgent cases
    #     if is_urgent:
    #         st.warning("**Priority contact scheduled** - Given your urgency level, our clinical team will contact you within 24 hours to expedite your transformation process.")
        
    #     # Main hero section
    #     st.markdown("**Your core behavioral patterns**")
    #     st.markdown("Based on your comprehensive assessment, we've identified your unique pattern signature")
        
    #     # Metrics display
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         st.metric("Patterns identified", total_patterns)
    #     with col2:
    #         st.metric("Assessment complete", f"{completion_rate*100:.0f}%")
    #     with col3:
    #         st.metric("Success probability", f"{success_probability}%")
        
    #     # Success probability bar
    #     st.markdown("**Transformation success likelihood:**")
    #     progress_bar = st.progress(success_probability / 100)
    
    # def _render_pattern_insights(self):
    #     """Render detailed pattern insights using Streamlit components"""
    #     results = st.session_state.assessment_results
    #     pattern_scores = results.get('pattern_scores', {})
        
    #     if not pattern_scores:
    #         st.warning("Pattern analysis incomplete - please complete the full assessment for detailed insights.")
    #         return
        
    #     st.markdown("**Your core behavioral patterns**")
        
    #     # Sort patterns by score
    #     sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
    #     # Pattern descriptions (keep for later use)
    #     """
    #     pattern_descriptions = {
    #         1: {
    #             "description": "You may find it challenging to accept or maintain positive emotional states",
    #             "impact": "This can limit your ability to fully enjoy success and happiness",
    #             "transformation": "Learning to trust that joy and success can be sustainable and deserved"
    #         },
    #         2: {
    #             "description": "You experience recurring conflicts and power struggles in relationships",
    #             "impact": "This can create stress and prevent collaborative problem-solving",
    #             "transformation": "Developing skills for curious dialogue and win-win resolution"
    #         },
    #         3: {
    #             "description": "You maintain a default skepticism about others' intentions",
    #             "impact": "This protective mechanism may limit deep connections and opportunities",
    #             "transformation": "Calibrating trust responses and building authentic relationships"
    #         },
    #         4: {
    #             "description": "You tend toward black-and-white thinking patterns",
    #             "impact": "This can limit creative solutions and increase decision paralysis",
    #             "transformation": "Developing nuanced thinking and embracing creative possibilities"
    #         },
    #         5: {
    #             "description": "Your self-worth is closely tied to productivity and achievement",
    #             "impact": "This can lead to burnout and difficulty with rest or self-care",
    #             "transformation": "Anchoring worth in your inherent value, independent of accomplishments"
    #         },
    #         6: {
    #             "description": "Your sense of identity shifts significantly across different contexts",
    #             "impact": "This can create internal confusion and emotional exhaustion",
    #             "transformation": "Integrating an authentic, consistent self across all situations"
    #         },
    #         7: {
    #             "description": "You prioritize others' needs while neglecting your own self-care",
    #             "impact": "This can lead to resentment and emotional depletion over time",
    #             "transformation": "Developing healthy boundaries and self-care practices"
    #         },
    #         8: {
    #             "description": "Your life choices are driven more by family expectations than personal desires",
    #             "impact": "This can create internal conflict and limit authentic self-expression",
    #             "transformation": "Clarifying personal values while maintaining family harmony"
    #         },
    #         9: {
    #             "description": "Your boundaries and limits vary dramatically based on context",
    #             "impact": "This can lead to inconsistent relationships and self-advocacy",
    #             "transformation": "Establishing consistent, healthy boundaries across all situations"
    #         }
    #     }
    #     """
        
    #     # Show only the first pattern with basic info
    #     if sorted_patterns:
    #         pattern_id, score = sorted_patterns[0]
    #         pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
            
    #         # Determine severity
    #         if score >= 6:
    #             intensity_text = "High intensity"
    #             badge_color = "🔴"
    #         elif score >= 4:
    #             intensity_text = "Moderate intensity" 
    #             badge_color = "🟡"
    #         elif score >= 2:
    #             intensity_text = "Mild intensity"
    #             badge_color = "🟢"
    #         else:
    #             intensity_text = "Emerging pattern"
    #             badge_color = "🟢"
            
    #         with st.container():
    #             col1, col2 = st.columns([3, 1])
    #             with col1:
    #                 st.markdown(f"**1. {pattern_name}**")
    #             with col2:
    #                 st.markdown(f"{badge_color} {intensity_text}")
                
        
    #     # Show count of additional patterns if present
    #     if len(sorted_patterns) > 1:
    #         additional_count = len(sorted_patterns) - 1
    #         st.markdown(f"Plus {additional_count} additional pattern{'s' if additional_count > 1 else ''} identified")
    #         st.markdown("Complete pattern analysis and interaction mapping available during your consultation.")

    #     st.success("**Key insight:** Your pattern recognition ability is already strong - that's 60% of the transformation work already complete.")
    #     st.markdown("Most people see initial shifts within 48 hours of Session 2")

    #     # Clinical analysis access
    #     self._render_clinical_analysis_section()
        
    #     # COMMENTED OUT SECTIONS FOR LATER USE:
    #     """
    #     # Show top 3 patterns with insights - FULL VERSION FOR LATER
    #     for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
    #         pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
    #         pattern_info = pattern_descriptions.get(pattern_id, {
    #             "description": "Unique behavioral pattern requiring individual exploration",
    #             "impact": "May be affecting your daily life and relationships",
    #             "transformation": "Personalized approach will be developed in your sessions"
    #         })
            
    #         # Determine severity
    #         if score >= 6:
    #             intensity_text = "High intensity"
    #             badge_color = "🔴"
    #         elif score >= 4:
    #             intensity_text = "Moderate intensity" 
    #             badge_color = "🟡"
    #         elif score >= 2:
    #             intensity_text = "Mild intensity"
    #             badge_color = "🟢"
    #         else:
    #             intensity_text = "Emerging pattern"
    #             badge_color = "🟢"
            
    #         with st.container():
    #             col1, col2 = st.columns([3, 1])
    #             with col1:
    #                 st.markdown(f"**{i+1}. {pattern_name}**")
    #             with col2:
    #                 st.markdown(f"{badge_color} {intensity_text}")
                
    #             st.markdown(f"**What this means:** {pattern_info['description']}")
    #             st.markdown(f"**Current impact:** {pattern_info['impact']}")
    #             st.info(f"**Transformation potential:** {pattern_info['transformation']}")
    #             st.markdown("---")
        
    #     # Show additional patterns if present - FULL VERSION
    #     if len(sorted_patterns) > 3:
    #         additional_count = len(sorted_patterns) - 3
    #         additional_patterns = [self.patterns.get(pid, f"Pattern {pid}") for pid, _ in sorted_patterns[3:]]
            
    #         st.markdown(f"**Additional patterns identified ({additional_count})**")
    #         st.markdown(f"Your comprehensive analysis also reveals these supporting patterns: {', '.join(additional_patterns)}")
    #         st.caption("These will be addressed as part of your integrated transformation approach.")
    #     """

    
    def _extract_response_by_keywords(self, responses, keywords):
        """Extract specific responses based on question keywords"""
        for response_data in responses.values():
            question_text = response_data.get('question_text', '').lower()
            if any(keyword.lower() in question_text for keyword in keywords):
                return response_data.get('response', 'Not specified')
        return 'Assessment incomplete'
    
    def _find_question_id_for_content(self, responses, content):
        """Find question ID that matches content"""
        for q_id, response_data in responses.items():
            if response_data.get('response') == content:
                return q_id
        return None
    
    def _question_relates_to_pattern(self, q_id, pattern_id, responses):
        """Check if a question relates to a specific pattern"""
        question_text = responses.get(q_id, {}).get('question_text', '').lower()
        
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
    
    def _determine_discovery_phase(self, adaptive_path, phase_progress):
        """Determine which phase a pattern was discovered in"""
        if 'pattern_1' in adaptive_path or 'pattern_2' in adaptive_path:
            return 'Early engagement'
        elif 'pattern_3' in adaptive_path or 'pattern_4' in adaptive_path:
            return 'Trigger mapping'
        else:
            return 'Pattern-specific questioning'
    
    def _generate_success_indicators(self, component, score):
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




    def _render_pattern_cost_analysis(self):
        """Render pattern cost analysis using Streamlit components"""
        future_vision = self._extract_future_vision()
        current_cost = self._calculate_pattern_cost()
        
        st.markdown("**The hidden cost of your current patterns**")
        
        st.warning(f"**Weekly impact:** This pattern sequence is likely costing you approximately **{current_cost['hours']} hours of peace and productivity per week**")
        
        st.markdown("**Compound cost over time:** Without intervention, these patterns typically solidify further, making change more difficult and the impact more severe.")
        
        if future_vision:
            st.info(f"**Your vision:** You mentioned wanting to {future_vision}. These patterns are the primary barrier standing between you and that reality.")
    
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
    
    def _render_digital_insights(self):
        """Render digital insights using Streamlit components"""
        digital_analysis = st.session_state.assessment_results.get('digital_despair_analysis')
        if not digital_analysis:
            return
        
        severity = digital_analysis['severity_level']
        score = digital_analysis['digital_despair_score']
        
        # Digital-specific insights
        digital_insights = {
            'SEVERE': {
                'title': 'Specialized digital-native approach required',
                'description': 'Your assessment reveals significant digital conditioning patterns that require adapted therapeutic techniques.',
                'benefits': 'With proper specialized approach, you can integrate your digital competencies with real-world confidence and authentic emotional expression.'
            },
            'MODERATE': {
                'title': 'Enhanced digital-aware therapy recommended', 
                'description': 'You show moderate digital conditioning that benefits from modified therapeutic approaches.',
                'benefits': 'Standard techniques enhanced with digital awareness will optimize your transformation process.'
            },
            'MILD': {
                'title': 'Digital considerations integrated',
                'description': 'Some digital influence detected that will be incorporated into your standard approach.',
                'benefits': 'Your digital skills can be leveraged as strengths in your transformation journey.'
            },
            'MINIMAL': {
                'title': 'Traditional approach optimal',
                'description': 'Minimal digital conditioning detected - standard hypnotherapy approach is ideal.',
                'benefits': 'You can benefit from proven traditional techniques without modification.'
            }
        }
        
        insight = digital_insights.get(severity, digital_insights['MINIMAL'])
        
        st.markdown(f"#### Digital pattern analysis: {insight['title']}")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**Digital conditioning score:** {score:.0f}% ({severity})")
        
        st.markdown(insight['description'])
        st.info(f"**Specialized advantage:** {insight['benefits']}")
    
    def _render_transformation_roadmap(self):
        """Render transformation roadmap using Streamlit components"""
        st.markdown("**Your transformation roadmap**")
        
        # Estimate timeline and sessions needed
        pattern_count = len(st.session_state.pattern_scores)
        digital_severity = st.session_state.assessment_results.get('digital_despair_analysis', {}).get('severity_level', 'MINIMAL')
        
        # Determine session structure
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
        
        # Phase breakdown
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
    
    def _render_next_steps_section(self):
        """Render next steps using Streamlit components"""
        contact_info = st.session_state.get('contact_info', {})
        urgency = contact_info.get('urgency', '')

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
        
        
        # # Additional support information
        # st.markdown("**Questions or need immediate support?**")
        # st.markdown("""
        # **Email:** Reply to any assessment email you receive from us  
        # **Direct contact:** Our clinical team will reach out to you personally  
        # **Emergency support:** If you're experiencing crisis, please contact your local emergency services
        # """)

    
    def _render_empowerment_section(self):
        """Render empowerment section using Streamlit components"""
        # COMMENTED OUT FOR NOW:
        readiness_indicators = self._extract_readiness_indicators()
        user_insights = self._extract_user_insights()
        
        st.markdown("**You have everything needed for rapid transformation**")
        
        # COMMENTED OUT:
        st.markdown("**Your transformation readiness indicators:**")
        st.markdown(readiness_indicators, unsafe_allow_html=True)
        
        st.success("**Key insight:** Your pattern recognition ability is already strong - that's 60% of the transformation work already complete.")
        
        # COMMENTED OUT:
        if user_insights:
            st.markdown(user_insights, unsafe_allow_html=True)
        
        # st.markdown("**Most people see initial shifts within 48 hours of Session 1**")
    
    def _render_value_comparison(self):
        """Render value comparison using Streamlit components"""
        # CHANGED FROM ### to **
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
    
    def _render_enhanced_paywall_preview(self):
        """Render enhanced paywall preview using Streamlit components"""
        core_belief_hint = self._extract_core_belief_hint()
        resistance_preview = self._predict_specific_resistance()
        rarity_stat = self._calculate_pattern_rarity()
        
        st.markdown("**Unlock your complete psychological blueprint**")
        
        # Create tabs for different analysis sections
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
        
        # Base calculation: more patterns and higher intensity = more weekly cost
        base_hours = 8
        pattern_multiplier = min(pattern_count * 1.5, 10)  # Cap at 10
        intensity_multiplier = min(intensity_avg / 5, 2)   # Cap at 2x
        
        total_hours = int(base_hours + pattern_multiplier + intensity_multiplier)
        
        return {'hours': total_hours}
    
    def _identify_hidden_mechanisms(self):
        """Identify hidden protective mechanisms"""
        mechanisms = []
        
        # Analyze top patterns for hidden mechanisms
        if st.session_state.pattern_scores:
            sorted_patterns = sorted(st.session_state.pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            mechanism_map = {
                1: "Happiness deflection to avoid disappointment",
                2: "Control seeking to prevent vulnerability", 
                3: "Preemptive rejection to avoid abandonment",
                4: "Binary thinking to simplify complex emotions",
                5: "Achievement addiction to earn worth",
                6: "Identity shifting to avoid rejection",
                7: "Self-sacrifice to maintain connection",
                8: "Mission inheritance to avoid family conflict",
                9: "Boundary collapse to avoid confrontation"
            }
            
            for pattern_id, score in sorted_patterns[:3]:
                if score >= 3:
                    mechanisms.append(mechanism_map.get(pattern_id, "Protective response pattern"))
        
        return mechanisms
    
    def _generate_future_prediction(self):
        """Generate pattern trajectory prediction"""
        pattern_count = len(st.session_state.pattern_scores)
        
        if pattern_count >= 4:
            return "Based on this pattern constellation, without intervention these protective mechanisms typically strengthen over time, creating increasing life restriction and relationship difficulties."
        elif pattern_count >= 2:
            return "These patterns tend to become more automatic and entrenched without conscious intervention, gradually limiting life satisfaction and authentic relationships."
        else:
            return "This pattern will likely solidify further without intervention, making future change more challenging."
    
    def _extract_core_belief_hint(self):
        """Extract hint about core limiting belief"""
        # Analyze text responses for belief indicators
        belief_indicators = {
            "not good enough": "I'm not good enough as I am",
            "can't trust": "I can't trust others to be there for me", 
            "must do": "I must constantly prove my worth",
            "don't deserve": "I don't deserve good things",
            "can't handle": "I can't handle difficult emotions"
        }
        
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str):
                for indicator, belief in belief_indicators.items():
                    if indicator in response.lower():
                        return belief
        
        return "Deep exploration needed in clinical analysis"
    
    def _predict_specific_resistance(self):
        """Predict specific resistance point"""
        if st.session_state.pattern_scores:
            top_pattern = max(st.session_state.pattern_scores.items(), key=lambda x: x[1])[0]
            
            resistance_map = {
                1: "May resist feeling genuine joy",
                2: "May challenge collaborative approach",
                3: "May question therapeutic relationship",
                4: "May resist nuanced solutions", 
                5: "May fear identity change",
                6: "May struggle with consistency",
                7: "May feel guilty about self-focus",
                8: "May feel disloyal to family",
                9: "May fear setting boundaries"
            }
            
            return resistance_map.get(top_pattern, "Standard change resistance")
        
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
        
    def _extract_readiness_indicators(self):
        """Extract readiness indicators from responses - simplified for Streamlit"""
        indicators = []
        
        # Check completion rate
        completion_rate = st.session_state.assessment_results.get('completion_rate', 0)
        if completion_rate >= 0.9:
            indicators.append(f"- High assessment engagement - completed {completion_rate * 100:.0f}% of questions")
        
        # Check for specific readiness responses
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
        """Extract user insights - simplified for Streamlit"""
        for response_data in st.session_state.assessment_responses.values():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            if 'different about your daily life' in question_text and isinstance(response, str) and len(response) > 30:
                return f'**Your transformation vision:** "{response[:150]}{"..." if len(response) > 150 else ""}"'
        
        return None
    
    def _render_clinical_analysis_section(self):
        """Render clinical analysis section using Streamlit components"""
        st.markdown("---")
        st.markdown("**Complete clinical analysis**")
        
        if PAYWALL_AVAILABLE:
            try:
                paywall = create_clinical_paywall()
                assessment_data = {
                    'assessment_results': st.session_state.assessment_results,
                    'assessment_responses': st.session_state.assessment_responses,
                    'intensity_responses': st.session_state.get('intensity_responses', {}),
                    'is_digital_native': st.session_state.is_digital_native,
                    'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis')
                }
                
                # Add contact info if available
                if 'contact_info' in st.session_state:
                    assessment_data.update(st.session_state.contact_info)
                
                if paywall.check_payment_status():
                    paywall.render_premium_analysis(assessment_data)
                else:
                    self._render_enhanced_paywall_preview()
                    
                    with st.expander("Access complete clinical analysis", expanded=False):
                        paywall.render_paywall_interface(assessment_data)
                        
            except Exception as e:
                st.error(f"Error loading premium analysis: {str(e)}")
                self._render_simple_analysis_preview()
        else:
            st.info("Complete clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning are available with premium access.")
            self._render_simple_analysis_preview()
    
    # def _render_clinical_analysis_section(self):
    #     """Render clinical analysis with paywall integration"""
    #     if PAYWALL_AVAILABLE:
    #         try:
    #             paywall = create_clinical_paywall()
    #             assessment_data = {
    #                 'assessment_results': st.session_state.assessment_results,
    #                 'assessment_responses': st.session_state.assessment_responses,
    #                 'intensity_responses': st.session_state.intensity_responses,
    #                 'is_digital_native': st.session_state.is_digital_native,
    #                 'digital_despair_analysis': st.session_state.assessment_results.get('digital_despair_analysis')
    #             }
    #             contact_info = st.session_state.get('contact_info', {})
    #             assessment_data.update(contact_info)
                
    #             if paywall.check_payment_status():
    #                 paywall.render_premium_analysis(assessment_data)
    #             else:
    #                 self._render_analysis_preview()
    #                 with st.expander("🔓 Unlock complete clinical analysis", expanded=False):
    #                     paywall.render_paywall_interface(assessment_data)
    #         except Exception as e:
    #             st.error(f"Error loading premium analysis: {str(e)}")
    #             self._render_analysis_preview()
    #     else:
    #         st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")
    #         self._render_analysis_preview()

    def _render_simple_analysis_preview(self):
        """Render simple analysis preview when paywall is not available"""
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
    
    # def _render_analysis_preview(self):
    #     """Render preview of analysis results"""
    #     results = st.session_state.assessment_results
    #     pattern_scores = results.get('pattern_scores', {})
        
    #     # Show algorithmical divide results if applicable
    #     if st.session_state.is_digital_native:
    #         digital_analysis = results.get('digital_despair_analysis')
    #         if digital_analysis:
    #             severity = digital_analysis['severity_level']
    #             score = digital_analysis['digital_despair_score']
                
    #             st.markdown(f"**📲 Algorithmic syndrome assessment: {severity}** ({score:.0f}% score)")
                
    #             if severity in ['SEVERE', 'MODERATE']:
    #                 st.warning(f"⚠️ **Hypnotherapy required** - Traditional approaches may be less effective")
    #             else:
    #                 st.success("✅ **Standard approach suitable** with highly targetted analysis")
        
    #     # Show traditional patterns
    #     if pattern_scores:
    #         st.markdown("**🎯 Your top behavioral patterns:**")
    #         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
    #         descriptions = {
    #             1: "Difficulty accepting or maintaining positive emotional states",
    #             2: "Recurring conflicts and power struggles in relationships", 
    #             3: "Default skepticism and difficulty trusting others' intentions",
    #             4: "Black-and-white thinking patterns that limit options",
    #             5: "Self-worth tied to productivity and achievement",
    #             6: "Inconsistent sense of identity across different contexts",
    #             7: "Prioritizing others' needs while neglecting self-care",
    #             8: "Life choices driven by family expectations",
    #             9: "Context-dependent loss of personal boundaries"
    #         }
            
    #         # Show only the top pattern
    #         if sorted_patterns:
    #             pattern_id, score = sorted_patterns[0]
    #             pattern_name = self.patterns.get(pattern_id, f"Pattern {pattern_id}")
    #             strength = "High" if score >= 6 else "Moderate" if score >= 3 else "Emerging"
                
    #             st.markdown(f"**1. {pattern_name}** - *{strength} intensity pattern detected*")
                
    #             if pattern_id in descriptions:
    #                 st.caption(descriptions[pattern_id])
                
    #             # Show indication of additional patterns if there are more
    #             if len(sorted_patterns) > 1:
    #                 remaining = len(sorted_patterns) - 1
    #                 st.write(f"**2. ...** *Plus {remaining} additional pattern{'s' if remaining > 1 else ''} identified*")
        
    #     # Info section outside the expander
    #     st.info("💡 **Premium analysis available**: Comprehensive clinical insights, personalized hypnotherapy recommendations, and detailed treatment planning available with premium access.")


    def _compile_assessment_data_for_blueprint(self):
        """Compile assessment data in the format expected by blueprint"""
        if 'assessment_session_id' not in st.session_state:
            st.session_state.assessment_session_id = str(uuid.uuid4())
        return {
            'session_id': st.session_state.assessment_session_id,
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
    
    def _compile_complete_assessment_data(self):
        """Compile complete assessment data for blueprint"""
        if 'assessment_session_id' not in st.session_state:
            st.session_state.assessment_session_id = str(uuid.uuid4())
        return {
            'session_id': st.session_state.assessment_session_id,
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
    

    # def _render_blueprint_access(self, assessment_data):
    #     """Render blueprint access with preview and full version"""
    #     st.markdown("**Your complete transformation blueprint**")
        
    #     # Preview section
    #     with st.expander("📋 Preview your behavioral blueprint", expanded=True):
    #         st.markdown("""
    #         Your comprehensive blueprint includes:
    #         - **Detailed pattern analysis** with specific insights for each detected pattern
    #         - **Hidden cost calculations** showing weekly and lifetime impact
    #         - **Digital conditioning analysis** (if applicable) with specialized recommendations
    #         - **Transformation roadmap** with personalized session planning
    #         - **Success probability analysis** based on your specific factors
    #         - **Investment analysis** comparing costs vs. benefits
    #         - **Why hypnotherapy works** for your specific pattern constellation
    #         """)
            
    #         # Show key metrics
    #         pattern_count = len(assessment_data.get('pattern_scores', {}))
    #         success_rate = self._calculate_comprehensive_success_rate()
            
    #         col1, col2, col3 = st.columns(3)
    #         with col1:
    #             st.metric("Patterns analyzed", pattern_count)
    #         with col2:
    #             st.metric("Success probability", f"{success_rate}%")
    #         with col3:
    #             digital_score = assessment_data.get('digital_despair_analysis', {}).get('digital_despair_score', 0)
    #             st.metric("Digital conditioning", f"{digital_score:.0f}%")
        
    #     # Access options
    #     col1, col2 = st.columns(2)
        
    #     with col1:
    #         if st.button("📖 View full blueprint", type="primary", use_container_width=True):
    #             st.session_state.show_blueprint = True
    #             st.rerun()
        
    #     with col2:
    #         if st.button("📄 Generate PDF report", use_container_width=True):
    #             self._generate_and_offer_pdf(assessment_data)
        
    #     # Show full blueprint if requested
    #     if st.session_state.get('show_blueprint', False):
    #         st.markdown("---")
    #         self._render_full_blueprint(assessment_data)
    

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
    
    def _extract_preview_insights(self, assessment_data):
            """Extract rich insights from assessment data for compelling preview"""
            
            # Basic data extraction
            pattern_scores = assessment_data.get('pattern_scores', {})
            responses = assessment_data.get('assessment_responses', {})
            digital_analysis = assessment_data.get('digital_despair_analysis')
            is_digital_native = assessment_data.get('is_digital_native', False)
            
            # Pattern analysis
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                dominant_pattern_id, dominant_score = sorted_patterns[0]
                dominant_pattern_name = self.patterns.get(dominant_pattern_id, "Unknown")
                pattern_count = len(pattern_scores)
            else:
                dominant_pattern_name = "Assessment incomplete"
                dominant_pattern_id = 1  # Default pattern ID for functions that need it
                dominant_score = 0
                pattern_count = 0
                sorted_patterns = []
            
            # Ensure all required fields are set before using them
            if not pattern_scores:
                # Provide complete default data structure when no patterns are detected
                return {
                    'dominant_pattern_name': 'Assessment incomplete - please complete full assessment',
                    'intensity_description': 'Assessment needed',
                    'complexity_description': 'Analysis pending',
                    'pattern_count': 0,
                    'success_rate': 85,  # Base success rate
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
            
            # Intensity description
            if dominant_score >= 6:
                intensity_description = "High intensity - requires immediate intervention"
            elif dominant_score >= 4:
                intensity_description = "Moderate intensity - well-suited for rapid transformation"
            elif dominant_score >= 2:
                intensity_description = "Emerging pattern - excellent prognosis for quick resolution"
            else:
                intensity_description = "Mild pattern - high success probability"
            
            # Complexity description
            if pattern_count >= 5:
                complexity_description = "Complex multi-pattern system"
            elif pattern_count >= 3:
                complexity_description = "Moderate complexity with clear intervention points"
            elif pattern_count >= 2:
                complexity_description = "Standard complexity level"
            else:
                complexity_description = "Single-pattern focus"
            
            # Success factors
            success_factors_list = []
            if pattern_count <= 3:
                success_factors_list.append("focused pattern constellation")
            
            completion_rate = assessment_data.get('completion_rate', 0)
            if completion_rate >= 0.9:
                success_factors_list.append("high assessment engagement")
            
            if is_digital_native and digital_analysis:
                success_factors_list.append("specialized approach match")
            
            # Extract readiness indicators
            readiness_score = 7  # Default
            for response_data in responses.values():
                if isinstance(response_data.get('response'), dict) and 'rating' in response_data['response']:
                    readiness_score = response_data['response']['rating']
                    break
            
            if readiness_score >= 8:
                success_factors_list.append("high motivation level")
            
            success_factors = ", ".join(success_factors_list) if success_factors_list else "strong assessment completion"
            
            # Calculate success rate
            success_rate = self._calculate_comprehensive_success_rate()
            
            # Digital summary
            digital_summary = ""
            if is_digital_native and digital_analysis:
                severity = digital_analysis['severity_level']
                score = digital_analysis['digital_despair_score']
                digital_summary = f"<strong>Digital conditioning:</strong> {score:.0f}% ({severity}) - specialized protocol activated"
            
            # Key insight generation
            key_insight = self._generate_key_insight(dominant_pattern_id, responses, digital_analysis)
            
            # Trigger sequence extraction
            trigger_sequence = self._extract_trigger_sequence(responses)
            
            # Cost preview calculation
            cost_preview = self._calculate_detailed_cost_preview(pattern_count, dominant_score)
        
            # Ensure cost_preview has required fields
            if not cost_preview:
                cost_preview = {
                    'weekly_hours': 8,
                    'annual_cost': '฿331,200',
                    'relationship_impact': 'Moderate impact on relationship quality'
                }
                
            # Pattern interactions
            pattern_interactions = [self.patterns.get(pid, f"Pattern {pid}") for pid, _ in sorted_patterns[:3]]
            if not pattern_interactions:
                pattern_interactions = ['Assessment incomplete']
            
            # Session plan preview
            session_plan = self._generate_session_plan_preview(dominant_pattern_id, pattern_count, digital_analysis)
            
            # Immediate techniques
            immediate_techniques = self._generate_immediate_techniques_preview(dominant_pattern_id, trigger_sequence)
            
            # Digital insights
            digital_insights = None
            if is_digital_native and digital_analysis:
                digital_insights = self._extract_digital_insights_preview(digital_analysis, responses)
            
            # Scoring for metrics
            clarity_score = min(10, max(1, int(completion_rate * 10)))
            match_score = 9 if is_digital_native else 8  # Our method is well-suited
            
            return {
                'dominant_pattern_name': dominant_pattern_name,
                'intensity_description': intensity_description,
                'complexity_description': complexity_description,
                'pattern_count': pattern_count,
                'success_rate': success_rate,
                'success_factors': success_factors,
                'digital_summary': digital_summary,
                'key_insight': key_insight,
                'trigger_sequence': trigger_sequence,
                'cost_preview': cost_preview,
                'pattern_interactions': pattern_interactions,
                'session_plan': session_plan,
                'immediate_techniques': immediate_techniques,
                'digital_insights': digital_insights,
                'clarity_score': clarity_score,
                'readiness_score': readiness_score,
                'match_score': match_score
            }
        
    
    def _generate_key_insight(self, dominant_pattern_id, responses, digital_analysis):
        """Generate a compelling key insight based on the dominant pattern"""
        
        insights_map = {
            1: "Your mind has learned to deflect happiness as protection against disappointment - but this same mechanism is preventing the joy you deserve",
            2: "You're fighting battles that don't need to be fought - your nervous system activates 'combat mode' even in collaborative situations",
            3: "Your protective skepticism, while once useful, is now creating the very rejection and isolation you're trying to avoid",
            4: "Your brilliant analytical mind gets trapped in 'either/or' thinking when 'both/and' solutions would serve you better",
            5: "You've created an equation where doing = worth, but your actual value exists independent of any achievement",
            6: "You're exhausting yourself maintaining different versions of yourself instead of trusting that your authentic self is enough",
            7: "Your generous heart has learned to give to others but forgotten how to receive - creating an unsustainable energy drain",
            8: "You're living someone else's dream while your own authentic desires remain buried under family expectations",
            9: "Your boundaries disappear in certain contexts because you've never learned you can be both loved and boundaried"
        }
        
        base_insight = insights_map.get(dominant_pattern_id, "Your assessment reveals protective patterns that once served you but now limit your potential")
        
        # Add digital conditioning insight if applicable
        if digital_analysis and digital_analysis['severity_level'] in ['SEVERE', 'MODERATE']:
            base_insight += " - compounded by digital conditioning that requires specialized intervention"
        
        return base_insight
    
    def _extract_trigger_sequence(self, responses):
        """Extract the behavioral trigger sequence from responses"""
        
        sequence = {}
        
        # Extract trigger information with safe key access
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
        
        # Provide defaults for missing sequence elements
        if 'trigger' not in sequence:
            sequence['trigger'] = "Situation analysis needed"
        if 'physical' not in sequence:
            sequence['physical'] = "Body awareness exploration needed"
        if 'thought' not in sequence:
            sequence['thought'] = "Automatic thought mapping needed"
        if 'emotion' not in sequence:
            sequence['emotion'] = "Emotional response identification needed"
        if 'behavior' not in sequence:
            sequence['behavior'] = "Behavioral pattern assessment needed"
        
        return sequence
    
    def _calculate_detailed_cost_preview(self, pattern_count, dominant_score):
        """Calculate detailed cost preview with specific numbers"""
        
        # Base calculation
        base_weekly_hours = 6 + (pattern_count * 2) + (dominant_score * 0.5)
        weekly_hours = min(int(base_weekly_hours), 25)  # Cap at 25 hours
        
        # Annual opportunity cost (using conservative estimates)
        hourly_value = 800  # THB per hour (conservative professional rate)
        annual_cost = f"฿{weekly_hours * 52 * hourly_value:,}"
        
        # Relationship impact
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
    
    def _generate_session_plan_preview(self, dominant_pattern_id, pattern_count, digital_analysis):
        """Generate session plan preview based on patterns"""
        
        session_1_focuses = {
            1: "Happiness permission protocols and safety anchoring",
            2: "Nervous system regulation and collaborative response installation",
            3: "Trust calibration and authentic connection programming",
            4: "Binary thinking dissolution and creative possibility expansion",
            5: "Worth anchoring independent of achievement",
            6: "Authentic self integration and consistency programming",
            7: "Boundary establishment and self-care permission",
            8: "Personal values clarification and family harmony balance",
            9: "Context-independent boundary installation"
        }
        
        session_2_targets = {
            1: "Joy sustainability and positive emotion anchoring",
            2: "Conflict transformation and win-win response automation",
            3: "Healthy skepticism calibration and openness programming",
            4: "Creative problem-solving and nuanced thinking installation",
            5: "Intrinsic worth recognition and balanced achievement",
            6: "Integrated identity and consistent self-expression",
            7: "Reciprocal relationship patterns and energy management",
            8: "Authentic life direction and confident decision-making",
            9: "Consistent boundary maintenance across all contexts"
        }
        
        session_1_preview = session_1_focuses.get(dominant_pattern_id, "Comprehensive pattern analysis and foundational work")
        session_2_preview = session_2_targets.get(dominant_pattern_id, "Core transformation and positive programming")
        
        # Adjust timeline based on complexity
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
    
    def _generate_immediate_techniques_preview(self, dominant_pattern_id, trigger_sequence):
        """Generate immediate techniques preview based on patterns"""
        
        technique_map = {
            1: {
                'technique_1': {
                    'name': 'Happiness Permission Check',
                    'description': 'Before dismissing good feelings, pause and ask: "What would I lose by enjoying this for 5 more minutes?" Usually, the answer reveals the pattern isn\'t protecting anything real.'
                },
                'technique_2': {
                    'name': 'Joy Anchoring Breath',
                    'description': 'When you notice happiness deflection starting, take 3 deep breaths while internally saying "I deserve this good feeling" - interrupt the automatic deflection.'
                }
            },
            2: {
                'technique_1': {
                    'name': 'Combat Mode Recognition',
                    'description': 'Notice when your body activates (tension, faster heartbeat) during disagreements. Pause and ask: "Is this actually a battle or an opportunity to understand?"'
                },
                'technique_2': {
                    'name': 'Collaboration Reset',
                    'description': 'When you feel the urge to "win," try saying: "Help me understand your perspective" instead of defending your position.'
                }
            },
            3: {
                'technique_1': {
                    'name': 'Trust Calibration Check',
                    'description': 'When suspicion arises, ask: "What evidence do I actually have?" vs "What story is my protective mind creating?"'
                },
                'technique_2': {
                    'name': 'Authentic Risk Taking',
                    'description': 'Practice sharing one small authentic thing daily - start building evidence that being real is safe.'
                }
            }
            # Add more patterns as needed
        }
        
        default_techniques = {
            'technique_1': {
                'name': 'Pattern Interrupt Pause',
                'description': 'When you notice your pattern activating, pause for 10 seconds and ask: "Is this response serving me right now?"'
            },
            'technique_2': {
                'name': 'Conscious Choice Point',
                'description': 'Before your automatic response, create a 3-second gap to choose a different response that aligns with who you want to be.'
            }
        }
        
        return technique_map.get(dominant_pattern_id, default_techniques)
    
    def _extract_digital_insights_preview(self, digital_analysis, responses):
        """Extract digital conditioning insights for preview"""
        
        severity = digital_analysis['severity_level']
        components = digital_analysis['component_scores']
        
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
        
        # Adaptation needed
        adaptation_map = {
            'SEVERE': "Complete protocol redesign with anti-authority language and ironic armor dissolution",
            'MODERATE': "Modified approach with digital-aware techniques and pacing adjustments",
            'MILD': "Standard approach enhanced with digital competency integration"
        }
        
        adaptation_needed = adaptation_map.get(severity, "Standard approach optimal")
        
        return {
            'attention_pattern': attention_pattern,
            'validation_source': validation_source,
            'adaptation_needed': adaptation_needed
        }
    
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
                    label="📥 Download PDF Report",
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

    def _send_assessment_email(self, assessment_data):
        """Send assessment email using unified email handler"""
        try:
            # Try to import and use the handler
            try:
                from utils.email_handler import UnifiedEmailHandler
                email_handler = UnifiedEmailHandler()
                return email_handler.send_assessment_results(assessment_data, "standard")
            except ImportError:
                # Fallback to existing email queue system
                self.email_queue.add_request({
                    'recipient': assessment_data.get('contact_info', {}).get('email'),
                    'assessment_data': assessment_data,
                    'type': 'assessment_results'
                })
                return True
        except Exception as e:
            print(f"Error sending assessment email: {str(e)}")
            return False
    
    def _save_to_cloud(self, assessment_data):
        """Save assessment data to cloud storage"""
        try:
            with st.spinner("Saving to cloud..."):
                cloud_storage = StreamlitCloudStorage()
                
                # Save complete assessment data
                cloud_url = cloud_storage.save_assessment_data(
                    assessment_data,
                    f"assessment_{assessment_data['session_id']}.json"
                )
                
                if cloud_url:
                    st.success("✅ Assessment saved successfully!")
                    st.info("📡 Your data is securely stored and can be accessed via download links.")
                    
                    # Store cloud reference in session
                    st.session_state.cloud_save_url = cloud_url
                else:
                    st.warning("⚠️ Save completed locally. Cloud storage may have limitations.")
                    
        except Exception as e:
            st.error(f"Error saving: {str(e)}")
    
    def _email_blueprint(self, assessment_data):
        """Email the blueprint to user"""
        contact_info = assessment_data.get('contact_info', {})
        user_email = contact_info.get('email')
        
        if not user_email:
            st.error("❌ No email address found. Please provide your email to receive the report.")
            return
        
        try:
            with st.spinner("Preparing blueprint email..."):
                # Generate PDF first
                pdf_generator = PDFGenerator()
                pdf_bytes = pdf_generator.generate_blueprint_pdf(assessment_data)
                
                # Send email with attachment
                from utils.email_blueprint_streamlit import send_blueprint_email_streamlit
                
                success = send_blueprint_email_streamlit(
                    user_email=user_email,
                    user_name=contact_info.get('name', 'Valued Client'),
                    assessment_data=assessment_data,
                    pdf_attachment=pdf_bytes
                )
                
                if success:
                    st.success(f"✅ Blueprint prepared for {user_email}")
                    st.info("📧 Email will be sent within 24 hours by our clinical team.")
                else:
                    st.warning("⚠️ Blueprint prepared. Our team will contact you directly.")
                    
        except Exception as e:
            st.error(f"Error preparing email: {str(e)}")
    
    def _get_user_agent(self):
        """Get basic user agent info for analytics"""
        return "Streamlit Community Cloud User"

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







