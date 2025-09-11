"""
Clinical Assessment Email Handler for Hypnotherapy Website
Specialized email handler for comprehensive behavioral pattern assessments
Provides detailed clinical analysis and intervention protocols for therapists
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

class ClinicalAssessmentEmailHandler:
    """Specialized handler for clinical assessment emails with comprehensive intervention mapping"""
    
    def __init__(self):
        # Gmail SMTP configuration
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "laetitiasheppard@gmail.com"
        self.recipient_email = "laetitiasheppard@gmail.com"
        
        # Try to get password from environment variables or Streamlit secrets
        try:
            import streamlit as st
            self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        except:
            self.password = os.environ.get("GMAIL_APP_PASSWORD", "")
        
        # Clinical pattern analysis database
        self.pattern_structures = {
            1: {
                "name": "Unhappiness Culture",
                "root_structure": "Positive states = danger/loss/punishment",
                "core_belief": "Happiness leads to disappointment or makes me a target",
                "systemic_factors": ["Family depression patterns", "Cultural suffering valorization", "Positive suppression rewards"],
                "identity_conflict": "Happy self vs. Familiar/safe suffering self",
                "hidden_loyalties": ["Family unhappiness solidarity", "Suffering = virtue beliefs", "Protection from envy/attacks"],
                "intervention_strategy": "Permission installation for positive states with safety anchoring"
            },
            2: {
                "name": "Power Struggles", 
                "root_structure": "Submission = death/annihilation of self",
                "core_belief": "I must fight to exist/maintain my identity",
                "systemic_factors": ["Authoritarian family dynamics", "Competition-based relationships", "Win-lose paradigms"],
                "identity_conflict": "Collaborative self vs. Fighter/survivor self",
                "hidden_loyalties": ["Family fight patterns", "Strength = resistance beliefs", "Protection from domination"],
                "intervention_strategy": "Collaborative empowerment with maintained autonomy"
            },
            3: {
                "name": "Systematic Mistrust",
                "root_structure": "Others = eventual betrayal/harm",
                "core_belief": "Trust leads to being hurt, used, or abandoned",
                "systemic_factors": ["Early betrayal experiences", "Inconsistent caregiving", "Trust violation patterns"],
                "identity_conflict": "Trusting self vs. Protected/vigilant self", 
                "hidden_loyalties": ["Loyalty to hurt parts", "Vigilance = safety beliefs", "Protection from re-injury"],
                "intervention_strategy": "Gradual trust building with transparent safety protocols"
            },
            4: {
                "name": "Separation and Division",
                "root_structure": "Gray areas = chaos/uncertainty/danger",
                "core_belief": "Things must be clearly defined or everything falls apart",
                "systemic_factors": ["Rigid family rules", "Religious absolutism", "Chaotic early environment"],
                "identity_conflict": "Flexible self vs. Clear/defined self",
                "hidden_loyalties": ["Family certainty patterns", "Order = safety beliefs", "Protection from confusion"],
                "intervention_strategy": "Both/and integration with safety in uncertainty"
            },
            5: {
                "name": "Doing versus Being",
                "root_structure": "Worth = productivity/achievement only",
                "core_belief": "I am only valuable when I'm producing/achieving",
                "systemic_factors": ["Achievement-focused family", "Work/school performance pressure", "Productivity culture"],
                "identity_conflict": "Being self vs. Achieving self",
                "hidden_loyalties": ["Family achievement patterns", "Worth = doing beliefs", "Protection from worthlessness"],
                "intervention_strategy": "Inherent worth installation with productivity reframing"
            },
            6: {
                "name": "Compartmentalized Authenticity",
                "root_structure": "Real self = rejection/abandonment",
                "core_belief": "I must be different selves to be accepted",
                "systemic_factors": ["Conditional family acceptance", "Social role expectations", "Authenticity punishment"],
                "identity_conflict": "Authentic self vs. Acceptable/safe selves",
                "hidden_loyalties": ["Family role patterns", "Adaptation = survival beliefs", "Protection from rejection"],
                "intervention_strategy": "Authentic self integration with safety across contexts"
            },
            7: {
                "name": "Self Sacrifice and Care Avoidance",
                "root_structure": "My needs = selfish/wrong/dangerous",
                "core_belief": "I am only good/loveable when serving others",
                "systemic_factors": ["Caretaker family roles", "Self-sacrifice modeling", "Need-shaming patterns"],
                "identity_conflict": "Self-caring self vs. Service/giving self",
                "hidden_loyalties": ["Family service patterns", "Sacrifice = love beliefs", "Protection from selfishness"],
                "intervention_strategy": "Self-care as service reframing with boundary installation"
            },
            8: {
                "name": "Inherited Missions",
                "root_structure": "My path = betrayal of family/ancestors",
                "core_belief": "I must fulfill family dreams/expectations to be loyal",
                "systemic_factors": ["Family sacrifice stories", "Generational expectations", "Dream inheritance patterns"],
                "identity_conflict": "Personal desire self vs. Family loyal self",
                "hidden_loyalties": ["Ancestral sacrifice honor", "Family dream continuation", "Protection from guilt/betrayal"],
                "intervention_strategy": "Honor family while claiming personal path integration"
            },
            9: {
                "name": "Context Dependent Weakness",
                "root_structure": "Certain contexts = powerlessness/helplessness",
                "core_belief": "I lose myself in specific situations/with certain people",
                "systemic_factors": ["Trauma context associations", "Power dynamic patterns", "Learned helplessness"],
                "identity_conflict": "Strong self vs. Overwhelmed/powerless self",
                "hidden_loyalties": ["Trauma bond maintenance", "Powerlessness = safety beliefs", "Protection from responsibility"],
                "intervention_strategy": "Universal strength anchoring with context-independent resources"
            }
        }
        
        # Hypnotic language mapping for each pattern
        self.hypnotic_language_map = {
            1: {
                "key_phrases": ["permission to enjoy", "safe to feel good", "happiness belongs to you"],
                "avoid_phrases": ["you should be happy", "force positivity", "get over it"],
                "somatic_anchors": "Heart warmth, gentle smile, relaxed shoulders",
                "metaphors": "Garden growing, sunrise emerging, door opening to light"
            },
            2: {
                "key_phrases": ["choose your response", "powerful in cooperation", "strength in partnership"],
                "avoid_phrases": ["you must", "submit to", "follow directions"],
                "somatic_anchors": "Grounded feet, centered core, relaxed jaw",
                "metaphors": "Dance partnership, river flowing, mountain standing"
            },
            3: {
                "key_phrases": ["when you're ready", "at your own pace", "trust yourself first"],
                "avoid_phrases": ["trust me", "let go completely", "surrender"],
                "somatic_anchors": "Steady breathing, firm boundaries, protected heart",
                "metaphors": "Fortress with opening gates, bridge building, seed planting"
            },
            4: {
                "key_phrases": ["both are possible", "many pathways", "flexible strength"],
                "avoid_phrases": ["either or", "must choose", "black and white"],
                "somatic_anchors": "Flexible spine, open hands, flowing breath",
                "metaphors": "River around rocks, rainbow colors, flexible tree"
            },
            5: {
                "key_phrases": ["you are enough", "being is valuable", "presence matters"],
                "avoid_phrases": ["must achieve", "prove yourself", "earn worth"],
                "somatic_anchors": "Still center, peaceful heart, grounded being",
                "metaphors": "Mountain being, still lake, rooted tree"
            },
            6: {
                "key_phrases": ["authentic in all places", "consistent truth", "real you everywhere"],
                "avoid_phrases": ["put on mask", "different faces", "hide yourself"],
                "somatic_anchors": "Centered spine, open heart, clear voice",
                "metaphors": "Diamond clarity, consistent light, authentic song"
            },
            7: {
                "key_phrases": ["balanced care", "serve from fullness", "include yourself"],
                "avoid_phrases": ["selfish", "only others matter", "sacrifice yourself"],
                "somatic_anchors": "Full heart, strong boundaries, balanced giving",
                "metaphors": "Full cup overflowing, airplane oxygen mask, strong foundation"
            },
            8: {
                "key_phrases": ["honor family and self", "personal truth", "unique expression"],
                "avoid_phrases": ["betray family", "abandon heritage", "reject traditions"],
                "somatic_anchors": "Rooted yet reaching, connected independence, honored truth",
                "metaphors": "Tree with deep roots growing toward light, river honoring source while flowing to sea"
            },
            9: {
                "key_phrases": ["consistent strength", "power in all contexts", "unchanging core"],
                "avoid_phrases": ["weak in situations", "powerless there", "different person"],
                "somatic_anchors": "Unshakeable core, portable strength, consistent power",
                "metaphors": "Portable lighthouse, diamond unchanged by setting, consistent star"
            }
        }

    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment with complete intervention mapping"""
        try:
            print("[DEBUG] Sending comprehensive clinical assessment results email")
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "🧠 CLINICAL ASSESSMENT - Complete Intervention Protocol"
            
            # Format the comprehensive clinical email body
            body = self._format_comprehensive_clinical_assessment(assessment_data)
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email if password is available
            if self.password:
                result = self._send_email(msg)
                print(f"[DEBUG] Clinical assessment email sent: {result}")
                return result
            else:
                print(f"Clinical Assessment Results: {assessment_data}")
                return True
                
        except Exception as e:
            print(f"[ERROR] Exception in send_clinical_assessment_results: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _format_comprehensive_clinical_assessment(self, data):
        """Format complete clinical assessment with intervention mapping"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract data components
            contact_info = data.get('contact_info', {})
            assessment_results = data.get('assessment_results', {})
            assessment_responses = data.get('assessment_responses', {})
            pattern_scores = data.get('pattern_scores', {})
            intensity_responses = data.get('intensity_responses', {})
            risk_flags = data.get('risk_flags', [])
            trigger_chain = data.get('trigger_chain', {})
            adaptive_triggered = data.get('adaptive_triggered', [])
            
            # Build comprehensive email
            email_body = f"""
🧠 COMPREHENSIVE CLINICAL BEHAVIORAL PATTERN ASSESSMENT
Advanced Intervention Protocol Generation System
Generated: {timestamp}

════════════════════════════════════════════════════════════════════════════════
CLIENT PROFILE & URGENCY ASSESSMENT
════════════════════════════════════════════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {contact_info.get('name', 'Not provided')}
Email: {contact_info.get('email', 'Not provided')}
Phone: {contact_info.get('phone', 'Not provided')}
Primary Concern: {contact_info.get('primary_concern', 'Not provided')}
Urgency Level: {contact_info.get('urgency', 'Not specified')}
Preferred Next Step: {contact_info.get('next_step', 'Not specified')}

📊 ASSESSMENT QUALITY METRICS:
Total Questions Answered: {assessment_results.get('total_questions_answered', 0)}
Completion Rate: {assessment_results.get('completion_rate', 1.0)*100:.1f}%
Adaptive Paths Triggered: {len(adaptive_triggered)}
Clinical Confidence Level: {self._assess_clinical_confidence(assessment_results, pattern_scores)}

⚡ CONTACT PROTOCOL:
{self._generate_contact_protocol(contact_info.get('urgency', ''), risk_flags)}

════════════════════════════════════════════════════════════════════════════════
🎯 ROOT PATTERN STRUCTURE ANALYSIS
════════════════════════════════════════════════════════════════════════════════

{self._analyze_root_pattern_structures(pattern_scores, assessment_responses)}

════════════════════════════════════════════════════════════════════════════════
🔄 COMPLETE BEHAVIORAL CHAIN MAPPING
════════════════════════════════════════════════════════════════════════════════

{self._generate_behavioral_chain_analysis(trigger_chain, assessment_responses)}

════════════════════════════════════════════════════════════════════════════════
🧬 SYSTEMIC FACTORS ANALYSIS
════════════════════════════════════════════════════════════════════════════════

{self._analyze_systemic_factors(pattern_scores, assessment_responses)}

════════════════════════════════════════════════════════════════════════════════
🆔 IDENTITY CONFLICTS & HIDDEN LOYALTIES
════════════════════════════════════════════════════════════════════════════════

{self._analyze_identity_conflicts_and_loyalties(pattern_scores, assessment_responses)}

════════════════════════════════════════════════════════════════════════════════
⚠️ CLINICAL RISK ASSESSMENT & SAFETY PROTOCOLS
════════════════════════════════════════════════════════════════════════════════

{self._generate_risk_assessment(risk_flags, intensity_responses, assessment_responses)}

════════════════════════════════════════════════════════════════════════════════
🎭 SESSION 1 PROTOCOL - ANALYSIS & RAPPORT
════════════════════════════════════════════════════════════════════════════════

{self._generate_session_1_protocol(pattern_scores, trigger_chain, contact_info)}

════════════════════════════════════════════════════════════════════════════════
⚡ SESSION 2 PROTOCOL - TRANSFORMATION & INTEGRATION
════════════════════════════════════════════════════════════════════════════════

{self._generate_session_2_protocol(pattern_scores, trigger_chain, contact_info)}

════════════════════════════════════════════════════════════════════════════════
📊 INTERVENTION MAPPING TABLE
════════════════════════════════════════════════════════════════════════════════

{self._generate_intervention_mapping_table(pattern_scores, assessment_responses, trigger_chain)}

════════════════════════════════════════════════════════════════════════════════
🎨 HYPNOTIC LANGUAGE PREPARATION
════════════════════════════════════════════════════════════════════════════════

{self._generate_hypnotic_language_preparation(pattern_scores, assessment_responses, trigger_chain)}

════════════════════════════════════════════════════════════════════════════════
📋 COMPLETE RESPONSE TRANSCRIPT (Clinical Reference)
════════════════════════════════════════════════════════════════════════════════

{self._format_complete_response_transcript(assessment_responses, intensity_responses)}

════════════════════════════════════════════════════════════════════════════════
📈 SUCCESS TRACKING & FOLLOW-UP PROTOCOL
════════════════════════════════════════════════════════════════════════════════

{self._generate_success_tracking_protocol(pattern_scores, contact_info)}

════════════════════════════════════════════════════════════════════════════════
CONFIDENTIAL CLINICAL DOCUMENT - LICENSED THERAPIST REVIEW REQUIRED
Bangkok Hypnotherapy Clinic - Advanced Assessment Protocol System
Client Reference: {contact_info.get('name', 'Unknown').replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}
════════════════════════════════════════════════════════════════════════════════
"""
            
            return email_body
            
        except Exception as e:
            print(f"[ERROR] Error in comprehensive clinical assessment formatting: {e}")
            return self._format_fallback_clinical_email(data, e)

    # ================== CLINICAL ANALYSIS METHODS ==================
    
    def _analyze_root_pattern_structures(self, pattern_scores, responses):
        """Analyze root psychological structures causing surface symptoms"""
        if not pattern_scores:
            return "No significant patterns identified - exploratory approach recommended"
        
        analysis = "🔍 IDENTIFIED ROOT PSYCHOLOGICAL STRUCTURES:\n\n"
        
        # Sort patterns by intensity
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns[:3], 1):
            if score >= 2.0:  # Significant patterns only
                pattern_info = self.pattern_structures.get(int(pattern_id), {})
                
                analysis += f"""
🎯 ROOT PATTERN {i}: {pattern_info.get('name', f'Pattern {pattern_id}')}
├─ Intensity Score: {score:.1f}/12 ({self._get_intensity_description(score)})
├─ Root Structure: {pattern_info.get('root_structure', 'Unknown structure')}
├─ Core Belief: {pattern_info.get('core_belief', 'Core belief analysis needed')}
├─ Identity Conflict: {pattern_info.get('identity_conflict', 'Identity conflict analysis needed')}
├─ Hidden Loyalties: {', '.join(pattern_info.get('hidden_loyalties', ['Analysis needed']))}
└─ Intervention Strategy: {pattern_info.get('intervention_strategy', 'Strategy development needed')}

"""
        
        # Add systemic pattern interactions
        if len(sorted_patterns) > 1:
            analysis += f"""
🔄 SYSTEMIC PATTERN INTERACTIONS:
• Patterns {' + '.join([str(p[0]) for p in sorted_patterns[:3]])} create mutually reinforcing system
• Primary intervention target: Pattern {sorted_patterns[0][0]} (highest intensity)
• Secondary stabilization: Patterns {' + '.join([str(p[0]) for p in sorted_patterns[1:3]])}
• System disruption approach: Address dominant pattern to destabilize entire system
"""
        
        return analysis
    
    def _generate_behavioral_chain_analysis(self, trigger_chain, responses):
        """Generate complete behavioral chain mapping with intervention points"""
        if not trigger_chain:
            return """
BEHAVIORAL CHAIN MAPPING: Requires Session 1 exploration

🔍 SESSION 1 PRIORITY: Complete behavioral chain mapping
• Identify specific trigger contexts and cues
• Map physiological response patterns
• Capture automatic thought sequences
• Track emotional progression patterns
• Document behavioral response choices
• Analyze consequence reinforcement cycles

📍 INTERVENTION POINT PREPARATION:
• Trigger interruption strategies ready for installation
• Somatic intervention protocols prepared
• Cognitive reframing techniques selected
• Emotional regulation tools prepared
• Behavioral anchoring methods ready
"""
        
        chain_analysis = """
🔗 COMPLETE BEHAVIORAL SEQUENCE MAPPED:

"""
        
        # Map each component of the behavioral chain
        chain_components = {
            'awareness_point': ('🎯 TRIGGER AWARENESS', 'Initial recognition point'),
            'physical_response': ('💓 SOMATIC RESPONSE', 'Body sensations and reactions'),
            'automatic_thought': ('💭 AUTOMATIC COGNITION', 'Immediate thought patterns'),
            'emotional_response': ('❤️ EMOTIONAL STATE', 'Feeling responses and intensity'),
            'behavioral_response': ('🏃 BEHAVIORAL ACTION', 'Actual behavior choices'),
            'immediate_consequence': ('⚡ IMMEDIATE RESULT', 'Short-term outcomes'),
            'longer_term_impact': ('📈 SYSTEMIC IMPACT', 'Long-term pattern reinforcement')
        }
        
        for key, (title, description) in chain_components.items():
            if key in trigger_chain:
                value = trigger_chain[key]
                if isinstance(value, dict):
                    # Handle emotional response with intensities
                    emotions = []
                    for emotion, intensity in value.items():
                        emotions.append(f"{emotion} ({intensity}/7)")
                    chain_analysis += f"{title}: {', '.join(emotions)}\n"
                else:
                    chain_analysis += f"{title}: {value}\n"
                
                # Add intervention points
                intervention_point = self._get_intervention_point(key, value)
                chain_analysis += f"   └─ INTERVENTION: {intervention_point}\n\n"
            else:
                chain_analysis += f"{title}: [SESSION 1 EXPLORATION NEEDED]\n"
                chain_analysis += f"   └─ INTERVENTION: Prepare {description.lower()} mapping\n\n"
        
        # Add chain disruption strategies
        chain_analysis += f"""
🎯 CHAIN DISRUPTION STRATEGY:
• PRIMARY INTERRUPTION POINT: {self._identify_primary_interruption_point(trigger_chain)}
• SECONDARY ANCHOR POINTS: {self._identify_secondary_anchor_points(trigger_chain)}
• INTERVENTION SEQUENCE: {self._generate_intervention_sequence(trigger_chain)}

📊 CHAIN PATTERN ANALYSIS:
• Chain complexity: {self._assess_chain_complexity(trigger_chain)}
• Intervention readiness: {self._assess_intervention_readiness(trigger_chain)}
• Success probability: {self._estimate_chain_success_probability(trigger_chain)}
"""
        
        return chain_analysis
    
    def _analyze_systemic_factors(self, pattern_scores, responses):
        """Analyze systemic factors maintaining problems"""
        systemic_analysis = """
🌍 ENVIRONMENTAL & SYSTEMIC FACTORS MAINTAINING PATTERNS:

"""
        
        # Analyze family system factors
        family_factors = self._extract_family_system_factors(responses)
        if family_factors:
            systemic_analysis += f"""
👨‍👩‍👧‍👦 FAMILY SYSTEM FACTORS:
{family_factors}

"""
        
        # Analyze cultural/social factors
        cultural_factors = self._extract_cultural_factors(responses, pattern_scores)
        if cultural_factors:
            systemic_analysis += f"""
🌏 CULTURAL/SOCIAL FACTORS:
{cultural_factors}

"""
        
        # Secondary gains analysis
        secondary_gains = self._analyze_secondary_gains(responses, pattern_scores)
        if secondary_gains:
            systemic_analysis += f"""
🎁 SECONDARY GAINS ANALYSIS:
{secondary_gains}

"""
        
        return systemic_analysis
    
    def _analyze_identity_conflicts_and_loyalties(self, pattern_scores, responses):
        """Analyze identity conflicts and hidden loyalties blocking change"""
        if not pattern_scores:
            return "Identity analysis requires pattern identification - conduct Session 1 exploration"
        
        identity_analysis = """
🆔 CORE IDENTITY CONFLICTS BLOCKING TRANSFORMATION:

"""
        
        # Analyze identity conflicts for each significant pattern
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for pattern_id, score in sorted_patterns[:3]:
            if score >= 2.0:
                pattern_info = self.pattern_structures.get(int(pattern_id), {})
                identity_analysis += f"""
⚔️ PATTERN {pattern_id} IDENTITY CONFLICT:
├─ Core Conflict: {pattern_info.get('identity_conflict', 'Analysis needed')}
├─ Hidden Loyalties: {', '.join(pattern_info.get('hidden_loyalties', ['Unknown']))}
├─ Loyalty Function: {self._analyze_loyalty_function(pattern_id, responses)}
└─ Integration Strategy: {self._generate_integration_strategy(pattern_id)}

"""
        
        # Generate loyalty honoring strategies
        loyalty_strategies = self._generate_loyalty_honoring_strategies(pattern_scores)
        identity_analysis += f"""
🤝 LOYALTY HONORING STRATEGIES:
{loyalty_strategies}
"""
        
        return identity_analysis
    
    def _generate_session_1_protocol(self, pattern_scores, trigger_chain, contact_info):
        """Generate specific Session 1 protocol based on assessment"""
        if not pattern_scores:
            return """
SESSION 1: EXPLORATORY ANALYSIS PROTOCOL

🎯 PRIMARY OBJECTIVES:
• Complete behavioral pattern identification
• Map complete trigger → response → consequence chain
• Identify pattern origins and protective functions
• Build therapeutic rapport and safety
• Assess transformation readiness

📋 SESSION STRUCTURE (90 minutes):
• Opening & rapport building (15 min)
• Pattern exploration & validation (30 min)
• Behavioral chain mapping (30 min)
• Initial positive programming (10 min)
• Session 2 planning & preparation (5 min)
"""
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_structures.get(int(dominant_pattern), {})
        
        protocol = f"""
SESSION 1: PATTERN-SPECIFIC ANALYSIS PROTOCOL

🎯 PRIMARY PATTERN TARGET: {pattern_info.get('name', f'Pattern {dominant_pattern}')}
Root Structure: {pattern_info.get('root_structure', 'Unknown')}
Core Belief: {pattern_info.get('core_belief', 'Unknown')}

📋 SESSION STRUCTURE (90 minutes):

🔍 OPENING & VALIDATION (15 minutes):
• Validate assessment findings: "{pattern_info.get('name', 'pattern')} pattern detected"
• Normalize pattern as protective mechanism
• Build therapeutic alliance using collaborative language
• Address any pattern-specific resistance

🗺️ PATTERN EXPLORATION (30 minutes):
• Origins exploration: "When did this pattern first serve you?"
• Protective function identification: "How has this pattern protected you?"
• Current context mapping: "Where does this show up most?"
• Pattern interaction analysis: "How do these patterns work together?"

🔗 BEHAVIORAL CHAIN COMPLETION (30 minutes):
{self._generate_chain_mapping_protocol(trigger_chain)}

🌱 INITIAL PROGRAMMING (10 minutes):
• Install permission for change
• Safety anchoring for transformation process
• Pattern-specific positive suggestions
• Future pacing for Session 2 readiness

📝 SESSION 2 PREPARATION (5 minutes):
• Review change readiness
• Address any remaining resistance
• Set expectations for transformation session
• Schedule follow-up within optimal window

⚠️ PATTERN-SPECIFIC CONSIDERATIONS:
{self._generate_pattern_specific_considerations(dominant_pattern)}

🎯 SUCCESS INDICATORS:
• Client reports feeling understood and hopeful
• Behavioral chain is completely mapped
• Pattern origins and functions are clear
• Client expresses readiness for transformation
• Therapeutic alliance is strong and collaborative
"""
        
        return protocol
    
    def _generate_session_2_protocol(self, pattern_scores, trigger_chain, contact_info):
        """Generate specific Session 2 transformation protocol"""
        if not pattern_scores:
            return """
SESSION 2: INDIVIDUALIZED TRANSFORMATION PROTOCOL

Session 2 protocol will be determined based on Session 1 findings.
Prepare general transformation tools and adapt based on discovered patterns.
"""
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_structures.get(int(dominant_pattern), {})
        
        protocol = f"""
SESSION 2: PATTERN-SPECIFIC TRANSFORMATION PROTOCOL

🎯 TRANSFORMATION TARGET: {pattern_info.get('name', f'Pattern {dominant_pattern}')}
Core Intervention: {pattern_info.get('intervention_strategy', 'Pattern-specific approach')}

📋 SESSION STRUCTURE (90 minutes):

🔄 OPENING & REINFORCEMENT (15 minutes):
• Review Session 1 changes and insights
• Reinforce positive shifts already occurring
• Address any resistance or concerns
• Prepare for deep transformation work

⚡ PATTERN INTERRUPTION (25 minutes):
• Access pattern-maintaining trance state
• Interrupt pattern at neurological level
• Install alternative neural pathways
• Use pattern-specific intervention language

🧬 CORE TRANSFORMATION (35 minutes):
{self._generate_core_transformation_protocol(dominant_pattern, trigger_chain)}

🔗 INTEGRATION & ANCHORING (10 minutes):
• Integrate new patterns across life contexts
• Install behavioral and identity anchors
• Test new responses in imagined scenarios
• Strengthen neural pathway connections

🎯 FUTURE PACING & CLOSING (5 minutes):
• Future pace successful behavior in trigger situations
• Install confidence and capability anchors
• Plan for continued transformation beyond sessions
• Schedule follow-up check and optional Session 3

🎨 HYPNOTIC TECHNIQUES:
{self._generate_hypnotic_techniques_for_pattern(dominant_pattern)}

🔧 INTERVENTION TOOLS:
{self._generate_intervention_tools(dominant_pattern, trigger_chain)}

⚠️ TRANSFORMATION CONSIDERATIONS:
{self._generate_transformation_considerations(dominant_pattern, contact_info)}
"""
        
        return protocol
    
    def _generate_intervention_mapping_table(self, pattern_scores, responses, trigger_chain):
        """Generate direct intervention mapping table"""
        if not pattern_scores:
            return "Intervention mapping will be created after Session 1 pattern identification"
        
        mapping_table = """
📊 DIRECT RESPONSE → INTERVENTION MAPPING TABLE:

"""
        
        # Map each significant pattern to specific interventions
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for pattern_id, score in sorted_patterns[:3]:
            if score >= 2.0:
                pattern_info = self.pattern_structures.get(int(pattern_id), {})
                hypnotic_info = self.hypnotic_language_map.get(int(pattern_id), {})
                
                mapping_table += f"""
🎯 PATTERN {pattern_id}: {pattern_info.get('name', f'Pattern {pattern_id}')}
┌─────────────────────────────────────────────────────────────────┐
│ INTERVENTION MAPPING                                            │
├─────────────────────────────────────────────────────────────────┤
│ Root Belief: {pattern_info.get('core_belief', 'Unknown')[:50]}...
│ Target Structure: {pattern_info.get('root_structure', 'Unknown')[:45]}...
│ Intervention Strategy: {pattern_info.get('intervention_strategy', 'Unknown')[:40]}...
├─────────────────────────────────────────────────────────────────┤
│ HYPNOTIC LANGUAGE:                                             │
│ ✓ Use: {', '.join(hypnotic_info.get('key_phrases', ['Pattern-specific phrases']))}
│ ✗ Avoid: {', '.join(hypnotic_info.get('avoid_phrases', ['Resistance-triggering phrases']))}
│ 🎯 Anchors: {hypnotic_info.get('somatic_anchors', 'Pattern-specific somatic work')}
│ 🌟 Metaphors: {hypnotic_info.get('metaphors', 'Pattern-specific metaphors')}
├─────────────────────────────────────────────────────────────────┤
│ SUCCESS MARKERS:                                               │
│ • Reduced pattern activation intensity                         │
│ • Natural alternative responses in trigger situations          │
│ • Identity integration across contexts                         │
│ • Sustained change without conscious effort                    │
└─────────────────────────────────────────────────────────────────┘

"""
        
        # Add behavioral chain intervention points
        if trigger_chain:
            mapping_table += """
🔗 BEHAVIORAL CHAIN INTERVENTION POINTS:

"""
            chain_interventions = {
                'awareness_point': 'Trigger Recognition Training',
                'physical_response': 'Somatic Interruption Techniques',
                'automatic_thought': 'Cognitive Reframing Installation',
                'emotional_response': 'Emotional Regulation Anchoring',
                'behavioral_response': 'Alternative Behavior Programming',
                'immediate_consequence': 'Consequence Reframing',
                'longer_term_impact': 'Pattern Interruption Reinforcement'
            }
            
            for key, intervention in chain_interventions.items():
                if key in trigger_chain:
                    mapping_table += f"• {intervention}: {trigger_chain[key]}\n"
                else:
                    mapping_table += f"• {intervention}: [SESSION 1 MAPPING NEEDED]\n"
        
        return mapping_table
    
    def _generate_hypnotic_language_preparation(self, pattern_scores, responses, trigger_chain):
        """Generate hypnotic language preparation based on client's exact language"""
        if not pattern_scores:
            return "Hypnotic language preparation requires pattern identification"
        
        language_prep = """
🎨 CLIENT-SPECIFIC HYPNOTIC LANGUAGE PREPARATION:

"""
        
        # Extract client's exact language from responses
        client_language = self._extract_client_language_patterns(responses)
        
        language_prep += f"""
🗣️ CLIENT'S EXACT LANGUAGE TO MIRROR:
{client_language}

"""
        
        # Generate pattern-specific language
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        hypnotic_info = self.hypnotic_language_map.get(int(dominant_pattern), {})
        
        language_prep += f"""
🎯 PATTERN-SPECIFIC THERAPEUTIC LANGUAGE:

✅ PERMISSION-BASED PHRASES:
{chr(10).join(f"• {phrase}" for phrase in hypnotic_info.get('key_phrases', ['Pattern-specific permission phrases']))}

❌ AVOID THESE PHRASES (Trigger Resistance):
{chr(10).join(f"• {phrase}" for phrase in hypnotic_info.get('avoid_phrases', ['Resistance-triggering language']))}

🌊 SOMATIC ANCHORING LANGUAGE:
"{hypnotic_info.get('somatic_anchors', 'Pattern-specific body awareness')}"

🌟 METAPHORICAL FRAMEWORKS:
{chr(10).join(f"• {metaphor}" for metaphor in hypnotic_info.get('metaphors', 'Pattern-specific metaphors').split(', '))}

"""
        
        # Add therapeutic reframes based on client responses
        therapeutic_reframes = self._generate_therapeutic_reframes(responses, dominant_pattern)
        language_prep += f"""
🔄 THERAPEUTIC REFRAMES FOR CLIENT'S LANGUAGE:
{therapeutic_reframes}

"""
        
        # Add induction style recommendations
        induction_style = self._recommend_induction_style(pattern_scores, responses)
        language_prep += f"""
🎭 RECOMMENDED INDUCTION STYLE:
{induction_style}

"""
        
        return language_prep

    # ================== HELPER METHODS ==================
    
    def _send_email(self, msg):
        """Send email via Gmail SMTP"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            
            text = msg.as_string()
            server.sendmail(self.sender_email, self.recipient_email, text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"SMTP error: {e}")
            return False
    
    def _assess_clinical_confidence(self, assessment_results, pattern_scores):
        """Assess clinical confidence level"""
        completion_rate = assessment_results.get('completion_rate', 0)
        pattern_count = len(pattern_scores) if pattern_scores else 0
        
        if completion_rate >= 0.9 and pattern_count >= 2:
            return "HIGH - Comprehensive data for targeted intervention"
        elif completion_rate >= 0.75:
            return "GOOD - Adequate data for effective treatment"
        else:
            return "MODERATE - May benefit from supplemental Session 1 exploration"
    
    def _generate_contact_protocol(self, urgency, risk_flags):
        """Generate urgency-based contact protocol"""
        urgency_lower = urgency.lower() if urgency else ''
        
        if len(risk_flags) >= 3:
            return "🚨 IMMEDIATE CONTACT - Crisis safety assessment within 6 hours"
        elif 'extremely urgent' in urgency_lower:
            return "🔥 PRIORITY CONTACT - Within 12 hours for urgent scheduling"
        elif 'very urgent' in urgency_lower:
            return "🟡 ELEVATED CONTACT - Within 24 hours for prompt response"
        else:
            return "📋 STANDARD CONTACT - Within 48-72 hours for routine follow-up"
    
    def _get_intensity_description(self, score):
        """Get intensity description for pattern scores"""
        if score >= 8:
            return "CRITICAL INTENSITY"
        elif score >= 6:
            return "HIGH INTENSITY"
        elif score >= 4:
            return "MODERATE INTENSITY"
        elif score >= 2:
            return "EMERGING PATTERN"
        else:
            return "MINIMAL PRESENCE"
    
    def _get_intervention_point(self, chain_key, value):
        """Get specific intervention point for behavioral chain component"""
        interventions = {
            'awareness_point': f"Install trigger recognition training for: {str(value)[:50]}",
            'physical_response': f"Somatic interruption techniques for: {str(value)[:50]}",
            'automatic_thought': f"Cognitive reframing installation for: {str(value)[:50]}",
            'emotional_response': f"Emotional regulation anchoring for: {str(value)[:50]}",
            'behavioral_response': f"Alternative behavior programming for: {str(value)[:50]}",
            'immediate_consequence': f"Consequence reframing for: {str(value)[:50]}",
            'longer_term_impact': f"Pattern interruption reinforcement for: {str(value)[:50]}"
        }
        return interventions.get(chain_key, f"Intervention point identification for {chain_key}")
    
    def _identify_primary_interruption_point(self, trigger_chain):
        """Identify the primary interruption point in the behavioral chain"""
        if 'physical_response' in trigger_chain:
            return "Somatic interruption (body awareness before thought cascade)"
        elif 'automatic_thought' in trigger_chain:
            return "Cognitive interruption (thought pattern intervention)"
        elif 'awareness_point' in trigger_chain:
            return "Trigger recognition (environmental awareness training)"
        else:
            return "Session 1 mapping required for optimal interruption point"
    
    def _identify_secondary_anchor_points(self, trigger_chain):
        """Identify secondary anchor points for intervention"""
        anchor_points = []
        if 'emotional_response' in trigger_chain:
            anchor_points.append("Emotional regulation")
        if 'behavioral_response' in trigger_chain:
            anchor_points.append("Behavioral choice point")
        if 'immediate_consequence' in trigger_chain:
            anchor_points.append("Consequence reframing")
        
        return ", ".join(anchor_points) if anchor_points else "Session 1 identification needed"
    
    def _generate_intervention_sequence(self, trigger_chain):
        """Generate optimal intervention sequence"""
        if len(trigger_chain) >= 4:
            return "Multi-point intervention: Trigger → Somatic → Cognitive → Behavioral"
        elif len(trigger_chain) >= 2:
            return "Dual-point intervention: Primary interruption + behavioral anchoring"
        else:
            return "Single-point intervention: Focus on strongest mapped component"
    
    def _assess_chain_complexity(self, trigger_chain):
        """Assess behavioral chain complexity"""
        complexity_levels = {
            0: "Unmapped - requires Session 1 exploration",
            1: "Simple - single intervention point",
            2: "Moderate - dual intervention approach",
            3: "Complex - multi-point intervention",
            4: "Comprehensive - complete chain mapped"
        }
        return complexity_levels.get(min(len(trigger_chain), 4), "Unknown complexity")
    
    def _assess_intervention_readiness(self, trigger_chain):
        """Assess readiness for intervention"""
        if len(trigger_chain) >= 3:
            return "HIGH - Multiple intervention points mapped"
        elif len(trigger_chain) >= 1:
            return "MODERATE - Some intervention points available"
        else:
            return "LOW - Requires Session 1 mapping for readiness"
    
    def _estimate_chain_success_probability(self, trigger_chain):
        """Estimate success probability based on chain mapping"""
        if len(trigger_chain) >= 4:
            return "EXCELLENT (85%+) - Complete chain enables precise targeting"
        elif len(trigger_chain) >= 2:
            return "GOOD (70-85%) - Adequate mapping for effective intervention"
        else:
            return "VARIABLE - Success depends on Session 1 mapping quality"
    
    def _extract_family_system_factors(self, responses):
        """Extract family system factors from responses"""
        family_factors = []
        
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            question_text = str(response_data.get('question_text', '')).lower()
            
            if any(keyword in question_text for keyword in ['family', 'growing up', 'childhood', 'parents']):
                if any(indicator in response_text for indicator in ['family', 'mother', 'father', 'parents', 'siblings']):
                    family_factors.append(f"• {response_data.get('response', '')[:100]}...")
        
        return "\n".join(family_factors[:3]) if family_factors else "• Family system analysis requires Session 1 exploration"
    
    def _extract_cultural_factors(self, responses, pattern_scores):
        """Extract cultural/social factors"""
        cultural_factors = []
        
        # Infer cultural factors from pattern combinations
        if 7 in pattern_scores and 8 in pattern_scores:  # Self-sacrifice + Inherited missions
            cultural_factors.append("• Cultural self-sacrifice values reinforcing family loyalty patterns")
        
        if 5 in pattern_scores:  # Doing vs Being
            cultural_factors.append("• Achievement-oriented cultural programming affecting self-worth")
        
        if 3 in pattern_scores:  # Systematic mistrust
            cultural_factors.append("• Cultural or social trust-erosion experiences")
        
        return "\n".join(cultural_factors) if cultural_factors else "• Cultural factor analysis requires deeper exploration"
    
    def _analyze_secondary_gains(self, responses, pattern_scores):
        """Analyze secondary gains keeping patterns in place"""
        gains = []
        
        # Pattern-specific secondary gains
        gain_patterns = {
            1: "Unhappiness may provide protection from envy, maintain family loyalty, or avoid disappointment",
            2: "Power struggles may maintain sense of identity, control, or prevent submission/vulnerability",
            3: "Mistrust may provide protection from betrayal and maintain emotional safety",
            7: "Self-sacrifice may maintain relationships, avoid guilt, and preserve caretaker identity",
            8: "Family loyalty may maintain belonging, honor sacrifices, and avoid guilt/shame"
        }
        
        for pattern_id, score in pattern_scores.items():
            if score >= 3.0 and int(pattern_id) in gain_patterns:
                gains.append(f"• {gain_patterns[int(pattern_id)]}")
        
        # Look for secondary gain responses
        for response_data in responses.values():
            question_text = str(response_data.get('question_text', '')).lower()
            if 'lose' in question_text or 'benefit' in question_text or 'protect' in question_text:
                response_text = response_data.get('response', '')
                if response_text and len(response_text) > 10:
                    gains.append(f"• Client identified: {response_text[:80]}...")
        
        return "\n".join(gains[:4]) if gains else "• Secondary gain analysis requires deeper exploration"
    
    def _analyze_loyalty_function(self, pattern_id, responses):
        """Analyze the function of hidden loyalties"""
        loyalty_functions = {
            1: "Loyalty to family suffering patterns - maintains connection through shared unhappiness",
            2: "Loyalty to family strength/fighter identity - maintains family warrior tradition",
            3: "Loyalty to protective vigilance - honors past hurt by maintaining guard",
            7: "Loyalty to family service role - maintains love through self-sacrifice",
            8: "Loyalty to family dreams/sacrifices - honors ancestors through mission fulfillment"
        }
        return loyalty_functions.get(int(pattern_id), "Loyalty function requires deeper exploration")
    
    def _generate_integration_strategy(self, pattern_id):
        """Generate identity integration strategy for pattern"""
        integration_strategies = {
            1: "Honor family while claiming right to joy - 'I can be happy AND stay connected'",
            2: "Honor strength while embracing collaboration - 'I can be strong AND cooperative'", 
            3: "Honor wisdom while opening gradually - 'I can be wise AND trusting when appropriate'",
            7: "Honor service while including self - 'I can serve others AND care for myself'",
            8: "Honor family while pursuing personal path - 'I can love family AND follow my own dreams'"
        }
        return integration_strategies.get(int(pattern_id), "Integration strategy development needed")
    
    def _generate_loyalty_honoring_strategies(self, pattern_scores):
        """Generate strategies for honoring loyalties while enabling change"""
        strategies = []
        
        for pattern_id, score in pattern_scores.items():
            if score >= 3.0:
                pattern_strategies = {
                    1: "Frame happiness as honoring family by showing their love created a capable person",
                    2: "Frame cooperation as ultimate strength - strong enough to include others",
                    3: "Frame trust as honoring own wisdom - trusting selectively shows good judgment",
                    7: "Frame self-care as increasing capacity to serve others more effectively",
                    8: "Frame personal path as honoring family values while expressing them uniquely"
                }
                if int(pattern_id) in pattern_strategies:
                    strategies.append(f"• Pattern {pattern_id}: {pattern_strategies[int(pattern_id)]}")
        
        return "\n".join(strategies) if strategies else "• Loyalty honoring strategies require pattern identification"
    
    def _generate_risk_assessment(self, risk_flags, intensity_responses, responses):
        """Generate comprehensive risk assessment"""
        if not risk_flags and not any(intensity >= 6 for intensity in intensity_responses.values()):
            return """
RISK ASSESSMENT: LOW RISK - Standard hypnotherapy approach suitable

✅ NO SIGNIFICANT RISK FACTORS IDENTIFIED
• Standard 2-session approach recommended
• No special safety protocols required
• High success probability with standard methods
"""
        
        risk_assessment = f"""
RISK LEVEL: {self._calculate_overall_risk_level(risk_flags, intensity_responses)}
Risk Factors Identified: {len(risk_flags)}
High Intensity Responses: {sum(1 for i in intensity_responses.values() if i >= 6)}

"""
        
        if risk_flags:
            risk_assessment += "🚨 SPECIFIC RISK FACTORS:\n"
            for i, flag in enumerate(risk_flags, 1):
                risk_description = self._get_risk_description(flag)
                management_strategy = self._get_risk_management_strategy(flag)
                risk_assessment += f"{i}. {risk_description}\n   Management: {management_strategy}\n\n"
        
        if any(intensity >= 6 for intensity in intensity_responses.values()):
            high_intensity_count = sum(1 for i in intensity_responses.values() if i >= 6)
            risk_assessment += f"⚡ HIGH INTENSITY RESPONSES: {high_intensity_count} items rated 6-7/7\n"
            risk_assessment += "   Management: Use gentle pacing, frequent check-ins, grounding techniques\n\n"
        
        # Add safety protocols
        risk_assessment += self._generate_safety_protocols(risk_flags, intensity_responses)
        
        return risk_assessment
    
    def _calculate_overall_risk_level(self, risk_flags, intensity_responses):
        """Calculate overall risk level"""
        risk_score = len(risk_flags) * 2 + sum(1 for i in intensity_responses.values() if i >= 6)
        
        if risk_score >= 6:
            return "HIGH RISK - Specialized approach required"
        elif risk_score >= 3:
            return "MODERATE RISK - Modified approach with safety protocols"
        elif risk_score >= 1:
            return "LOW-MODERATE RISK - Standard approach with precautions"
        else:
            return "LOW RISK - Standard approach suitable"
    
    def _get_risk_description(self, flag):
        """Get description for risk flag"""
        descriptions = {
            'risk_q_10': "Current medical/mental health care - coordination required",
            'risk_q_11': "Intense emotional states - emotional regulation concerns", 
            'risk_q_12': "Dissociation/panic/self-harm history - safety protocols needed",
            'risk_q_13': "Substance use patterns - sobriety considerations"
        }
        return descriptions.get(flag, f"Risk factor identified: {flag}")
    
    def _get_risk_management_strategy(self, flag):
        """Get management strategy for risk flag"""
        strategies = {
            'risk_q_10': "Coordinate with existing providers, obtain clearance if needed",
            'risk_q_11': "Use grounding techniques, shorter sessions, frequent check-ins",
            'risk_q_12': "Safety assessment, crisis resources, gentle modified approach",
            'risk_q_13': "Address substance use, consider timing of intervention"
        }
        return strategies.get(flag, "Standard clinical precautions and monitoring")
    
    def _generate_safety_protocols(self, risk_flags, intensity_responses):
        """Generate specific safety protocols"""
        protocols = """
🛡️ SAFETY PROTOCOLS:

"""
        
        if len(risk_flags) >= 2:
            protocols += """
HIGH RISK PROTOCOLS:
• Obtain written consent with risk acknowledgment
• Have crisis resources immediately available
• Consider shorter initial sessions (60 minutes)
• Maintain frequent verbal check-ins during hypnosis
• Use permissive rather than directive language
• Have emergency contact information readily available

"""
        
        if any(intensity >= 6 for intensity in intensity_responses.values()):
            protocols += """
HIGH INTENSITY PROTOCOLS:
• Use extra grounding and stabilization techniques
• Gentle emergence from hypnosis with extra time
• Provide post-session integration support
• Check emotional state before client departure
• Offer additional between-session support if needed

"""
        
        protocols += """
STANDARD SAFETY MEASURES:
• Maintain professional therapeutic boundaries
• Document all sessions thoroughly
• Provide clear emergency contact information
• Ensure client has transportation home if needed
• Schedule appropriate follow-up timing
"""
        
        return protocols
    
    def _generate_chain_mapping_protocol(self, trigger_chain):
        """Generate chain mapping protocol for Session 1"""
        if len(trigger_chain) >= 4:
            return """
CHAIN VALIDATION & COMPLETION:
• Validate mapped sequence with client experience
• Fill in any missing components or details
• Identify optimal intervention points
• Test chain accuracy with
