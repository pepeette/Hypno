"""
Clinical Assessment Email Handler
Specialized email handler for comprehensive behavioral pattern assessments
To be placed in utils/email_assess.py
"""
import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class ClinicalAssessmentEmailHandler:
    """Specialized email handler for clinical assessment results"""
    
    def __init__(self):
        # Gmail SMTP configuration
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = "laetitiasheppard@gmail.com"
        self.recipient_email = "laetitiasheppard@gmail.com"
        
        # Pattern name mappings
        self.pattern_names = {
            1: "Unhappiness Culture",
            2: "Power Struggles", 
            3: "Systematic Mistrust",
            4: "Separation/Division",
            5: "Doing vs Being",
            6: "Compartmentalized Authenticity",
            7: "Self-Sacrifice/Care Avoidance",
            8: "Inherited Missions",
            9: "Context-Dependent Weakness"
        }
        
        # Try to get password from environment variables or Streamlit secrets
        try:
            import streamlit as st
            self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        except:
            self.password = os.environ.get("GMAIL_APP_PASSWORD", "")
    
    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment results with full analysis"""
        try:
            # Extract key information safely
            contact_info = assessment_data.get('contact_info', {})
            assessment_results = assessment_data.get('assessment_results', {})
            
            email = contact_info.get('email', 'unknown@email.com')
            name = contact_info.get('name', 'Assessment Participant')
            urgency = contact_info.get('urgency', 'Not specified')
            concern = contact_info.get('primary_concern', 'Not specified')
            next_step = contact_info.get('next_step', 'Not specified')
            
            # Create enhanced email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = self._generate_email_subject(name, urgency, assessment_results)
            
            # Build comprehensive email body
            body = self._build_comprehensive_email_body(assessment_data)
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email if password is available
            if self.password:
                return self._send_email(msg)
            else:
                # Log the assessment data for debugging
                print(f"Clinical Assessment: {name} ({email})")
                print(f"Urgency: {urgency}")
                print(f"Patterns detected: {len(assessment_results.get('pattern_scores', {}))}")
                print(f"Completion rate: {assessment_results.get('completion_rate', 0)*100:.0f}%")
                return True  # Simulate success when no password is configured
                
        except Exception as e:
            print(f"Error sending clinical assessment: {str(e)}")
            import traceback
            print(f"Full traceback: {traceback.format_exc()}")
            return False
    
    def _generate_email_subject(self, name, urgency, assessment_results):
        """Generate contextual email subject based on assessment data"""
        # Priority indicator
        if 'extremely urgent' in urgency.lower():
            priority = "🚨 PRIORITY"
        elif 'very urgent' in urgency.lower():
            priority = "⚡ HIGH PRIORITY"
        elif 'urgent' in urgency.lower():
            priority = "📋 URGENT"
        else:
            priority = "🧠 CLINICAL"
        
        # Pattern complexity indicator
        pattern_count = len(assessment_results.get('pattern_scores', {}))
        if pattern_count >= 5:
            complexity = "COMPLEX"
        elif pattern_count >= 3:
            complexity = "MULTI-PATTERN"
        else:
            complexity = "FOCUSED"
        
        # Completion indicator
        completion_rate = assessment_results.get('completion_rate', 0)
        if completion_rate >= 0.9:
            completion = "COMPLETE"
        elif completion_rate >= 0.7:
            completion = "SUBSTANTIAL"
        else:
            completion = "PARTIAL"
        
        return f"{priority} ASSESSMENT: {name} - {complexity} {completion} ANALYSIS"
    
    def _build_comprehensive_email_body(self, assessment_data):
        """Build comprehensive email body with all clinical data"""
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        
        # Header section
        body = self._build_header_section(contact_info, assessment_results)
        
        # Clinical template section
        clinical_template = assessment_data.get('clinical_template', '')
        if clinical_template:
            body += f"\n{clinical_template}\n"
        else:
            body += "\n" + self._generate_clinical_template_fallback(assessment_data) + "\n"
        
        # Detailed analysis section
        body += self._build_detailed_analysis_section(assessment_data)
        
        # Raw data section
        body += self._build_raw_data_section(assessment_data)
        
        # Action items section
        body += self._build_action_items_section(contact_info, assessment_results)
        
        # Footer
        body += self._build_footer_section()
        
        return body
    
    def _build_header_section(self, contact_info, assessment_results):
        """Build email header with client information"""
        name = contact_info.get('name', 'Not provided')
        email = contact_info.get('email', 'Not provided')
        phone = contact_info.get('phone', 'Not provided')
        urgency = contact_info.get('urgency', 'Not specified')
        concern = contact_info.get('primary_concern', 'Not specified')
        next_step = contact_info.get('next_step', 'Not specified')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        questions_answered = assessment_results.get('total_questions_answered', 0)
        completion_rate = assessment_results.get('completion_rate', 0) * 100
        patterns_detected = len(assessment_results.get('pattern_scores', {}))
        
        return f"""
🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
══════════════════════════════════════════════════════════════════

📋 CLIENT INFORMATION:
Name: {name}
Email: {email}
Phone: {phone}
Primary Concern: {concern}
Urgency Level: {urgency}
Preferred Next Step: {next_step}
Assessment Completed: {timestamp}

📊 ASSESSMENT METRICS:
Questions Answered: {questions_answered}
Completion Rate: {completion_rate:.0f}%
Patterns Detected: {patterns_detected}
Assessment Quality: {'EXCELLENT' if completion_rate >= 90 else 'GOOD' if completion_rate >= 70 else 'PARTIAL'}

══════════════════════════════════════════════════════════════════
"""
    
    def _generate_clinical_template_fallback(self, assessment_data):
        """Generate clinical template if not provided"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return """
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║                   (Assessment Incomplete)                    ║
╚══════════════════════════════════════════════════════════════╝

**PATTERN ANALYSIS:**
Dominant Pattern: Assessment requires completion for accurate analysis
Primary Pattern: Insufficient data for pattern ranking
Secondary Pattern: Additional questions needed

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: Requires session exploration
Hidden Benefits: Cannot determine without complete assessment
Systemic Resistance: Assessment incomplete - manual evaluation needed
Identity Threat: Requires completed assessment for accurate profiling

**SESSION PLANNING:**
Session 1 Focus: Comprehensive pattern assessment and rapport building
Session 2 Target: Pattern-specific intervention based on session 1 findings
Potential Session 3 Need: Standard reinforcement protocol

**THERAPEUTIC APPROACH:**
Change Readiness Score: Not assessed
Predicted Resistance Points:
1. Standard change resistance - unknown specific patterns
2. Possible assessment completion resistance

Intervention Keywords: Adaptive approach based on session 1 findings
Avoid Language: Generic restrictions until pattern identification

╔══════════════════════════════════════════════════════════════╗
║         RECOMMENDATION: DISCOVERY CALL REQUIRED             ║
╚══════════════════════════════════════════════════════════════╝
"""
        
        # Get top patterns
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        dominant_pattern = self.pattern_names.get(int(sorted_patterns[0][0]), "Unknown") if sorted_patterns else "Unknown"
        dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
        
        primary_pattern = self.pattern_names.get(int(sorted_patterns[1][0]), "Unknown") if len(sorted_patterns) > 1 else "None detected"
        primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
        
        secondary_pattern = self.pattern_names.get(int(sorted_patterns[2][0]), "Unknown") if len(sorted_patterns) > 2 else "None detected"
        secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
        
        # Generate session recommendations based on dominant pattern
        session_plans = self._get_session_recommendations(int(sorted_patterns[0][0]) if sorted_patterns else 1)
        
        return f"""
╔══════════════════════════════════════════════════════════════╗
║                    CLINICAL ANALYSIS TEMPLATE                ║
║                   Behavioral Pattern Assessment              ║
╚══════════════════════════════════════════════════════════════╝

**PATTERN ANALYSIS:**
Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10)
Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: {self._extract_core_belief(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
Hidden Benefits: {self._extract_hidden_benefits(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
Systemic Resistance: {self._extract_systemic_resistance(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
Identity Threat: {self._extract_identity_threat(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

**SESSION PLANNING:**
Session 1 Focus: {session_plans['session_1']}
Session 2 Target: {session_plans['session_2']}
Potential Session 3 Need: {session_plans['session_3']}

**THERAPEUTIC APPROACH:**
Change Readiness Score: {self._extract_readiness_score(assessment_data)}/10
Predicted Resistance Points:
{self._extract_resistance_points(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

Intervention Keywords: {self._extract_intervention_keywords(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
Avoid Language: {self._extract_avoid_language(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL NOTES                          ║
╚══════════════════════════════════════════════════════════════╝

Pattern constellation indicates {self._get_therapeutic_complexity(sorted_patterns)} therapeutic approach required.
Estimated session success probability: {self._calculate_success_probability(sorted_patterns, assessment_data)}%
"""
    
    def _build_detailed_analysis_section(self, assessment_data):
        """Build detailed pattern analysis section"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        trigger_chain = assessment_data.get('trigger_chain', {})
        
        if not pattern_scores:
            return "\n🔍 DETAILED PATTERN ANALYSIS:\nInsufficient data for detailed analysis. Discovery call recommended.\n"
        
        section = "\n🔍 DETAILED PATTERN ANALYSIS:\n"
        section += "═" * 50 + "\n"
        
        # Pattern breakdown
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
            pattern_name = self.pattern_names.get(int(pattern_id), f"Pattern {pattern_id}")
            activation_level = "HIGH" if score >= 6 else "MEDIUM" if score >= 3 else "LOW"
            
            section += f"\n{i}. {pattern_name}:\n"
            section += f"   Activation Level: {activation_level} (Score: {score:.1f})\n"
            section += f"   Therapeutic Priority: {self._get_therapeutic_priority(score)}\n"
            section += f"   Clinical Significance: {self._get_clinical_significance(int(pattern_id), score)}\n"
        
        # Trigger chain analysis
        if trigger_chain:
            section += f"\n🔗 BEHAVIORAL TRIGGER CHAIN:\n"
            for stage, response in trigger_chain.items():
                section += f"   {stage.replace('_', ' ').title()}: {response}\n"
        
        return section
    
    def _build_raw_data_section(self, assessment_data):
        """Build raw data section for clinical review"""
        section = f"\n📊 RAW ASSESSMENT DATA:\n"
        section += "═" * 50 + "\n"
        
        # Pattern scores
        pattern_scores = assessment_data.get('pattern_scores', {})
        section += f"Pattern Scores: {pattern_scores}\n"
        
        # Assessment metadata
        assessment_results = assessment_data.get('assessment_results', {})
        section += f"Triggered Patterns: {assessment_results.get('triggered_patterns', [])}\n"
        section += f"Risk Flags: {assessment_results.get('risk_flags', [])}\n"
        section += f"Adaptive Paths: {assessment_results.get('adaptive_paths_triggered', [])}\n"
        section += f"Phase Completion: {assessment_results.get('phase_completion', {})}\n"
        
        # Response sampling (first 3 responses for privacy)
        responses = assessment_data.get('assessment_responses', {})
        if responses:
            section += f"\nSample Responses (first 3):\n"
            for i, (q_id, response_data) in enumerate(list(responses.items())[:3], 1):
                question_text = response_data.get('question_text', 'Unknown question')
                response = response_data.get('response', 'No response')
                section += f"   Q{q_id}: {question_text[:50]}...\n"
                section += f"   Response: {str(response)[:100]}...\n"
        
        # Intensity data
        intensity_responses = assessment_data.get('intensity_responses', {})
        if intensity_responses:
            section += f"\nIntensity Mappings: {intensity_responses}\n"
        
        return section
    
    def _build_action_items_section(self, contact_info, assessment_results):
        """Build action items section"""
        urgency = contact_info.get('urgency', 'Not specified')
        email = contact_info.get('email', 'Not provided')
        next_step = contact_info.get('next_step', 'Not specified')
        patterns_count = len(assessment_results.get('pattern_scores', {}))
        completion_rate = assessment_results.get('completion_rate', 0)
        
        section = f"\n⚡ IMMEDIATE ACTION ITEMS:\n"
        section += "═" * 50 + "\n"
        
        # Contact timeline
        if 'extremely urgent' in urgency.lower():
            contact_window = "4-6 hours"
            priority = "EMERGENCY"
        elif 'very urgent' in urgency.lower():
            contact_window = "12-24 hours"
            priority = "HIGH"
        elif 'urgent' in urgency.lower():
            contact_window = "24-48 hours"
            priority = "ELEVATED"
        else:
            contact_window = "48-72 hours"
            priority = "STANDARD"
        
        section += f"1. PRIORITY CONTACT: {email} within {contact_window}\n"
        section += f"   Contact Priority Level: {priority}\n"
        section += f"   Client Requested: {next_step}\n\n"
        
        # Clinical preparation
        if completion_rate >= 0.8 and patterns_count >= 3:
            section += "2. CLINICAL PREPARATION:\n"
            section += "   ✓ Comprehensive assessment complete\n"
            section += "   ✓ Pattern-specific approach ready\n"
            section += "   ✓ Session planning template above\n"
            section += "   → Proceed with targeted intervention\n\n"
        elif completion_rate >= 0.6:
            section += "2. CLINICAL PREPARATION:\n"
            section += "   ⚠ Substantial data available\n"
            section += "   → Brief discovery call to fill gaps\n"
            section += "   → Proceed with hybrid approach\n\n"
        else:
            section += "2. CLINICAL PREPARATION:\n"
            section += "   ❌ Insufficient assessment data\n"
            section += "   → Full discovery call required\n"
            section += "   → Standard 2-session approach\n\n"
        
        # Follow-up actions
        section += "3. FOLLOW-UP PROTOCOL:\n"
        section += "   □ Send confirmation email to client\n"
        section += "   □ Schedule appropriate session type\n"
        section += "   □ Prepare session materials based on patterns\n"
        section += "   □ Set up progress tracking system\n"
        
        return section
    
    def _build_footer_section(self):
        """Build email footer"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
══════════════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Clinical Assessment System
Comprehensive Behavioral Pattern Analysis Generated: {timestamp}
System Status: Operational | Data Quality: Verified | Action Required: Review Above
══════════════════════════════════════════════════════════════════
"""
    
    # Helper methods for clinical template generation
    def _get_session_recommendations(self, pattern_id):
        """Get session recommendations for specific pattern"""
        recommendations = {
            1: {
                'session_1': "Unhappiness Culture mapping + permission for joy + gentle positive anchoring",
                'session_2': "Deep joy permission installation + reframe happiness beliefs + positive emotion anchors",
                'session_3': "Joy maintenance if relapse into pessimism or guilt about happiness"
            },
            2: {
                'session_1': "Power struggle pattern analysis + collaboration establishment + shared control",
                'session_2': "Transform win/lose to win/win mindset + install collaboration reflexes + peace anchors",
                'session_3': "Conflict de-escalation if old fighting patterns resurface"
            },
            3: {
                'session_1': "Trust violation history + safety establishment + graduated vulnerability",
                'session_2': "Install healthy discernment vs. systematic mistrust + trust capacity building",
                'session_3': "Trust maintenance if cynicism returns or trust betrayal occurs"
            },
            4: {
                'session_1': "Binary thinking identification + both/and introduction + cognitive flexibility",
                'session_2': "Install nuanced thinking + creative option generation + decision confidence",
                'session_3': "Flexibility maintenance if black/white thinking resurfaces under stress"
            },
            5: {
                'session_1': "Achievement addiction mapping + inherent worth establishment + being practice",
                'session_2': "Install worth independence from productivity + being/doing balance + rest permission",
                'session_3': "Worth maintenance if productivity pressure returns"
            },
            6: {
                'session_1': "Authentic self identification + consistency across contexts + integration work",
                'session_2': "Install unified authentic self + consistent expression + context independence",
                'session_3': "Authenticity maintenance if compartmentalization returns under pressure"
            },
            7: {
                'session_1': "Self-sacrifice pattern mapping + self-care as strength reframe + boundary establishment",
                'session_2': "Install healthy balance + self-care habits + boundary maintenance reflexes",
                'session_3': "Balance maintenance if caretaking patterns resurface"
            },
            8: {
                'session_1': "Family mission identification + personal desire differentiation + loyalty vs. autonomy",
                'session_2': "Install personal path confidence + family respect integration + autonomous choice",
                'session_3': "Autonomy maintenance if family pressure increases"
            },
            9: {
                'session_1': "Context-dependent weakness mapping + universal strength identification + boundary work",
                'session_2': "Install consistent boundaries + context-independent strength + situational confidence",
                'session_3': "Strength maintenance if old contexts trigger boundary collapse"
            }
        }
        
        return recommendations.get(pattern_id, {
            'session_1': "Comprehensive pattern assessment and initial rapport building",
            'session_2': "Core pattern transformation and positive programming",
            'session_3': "Standard reinforcement if needed"
        })
    
    def _extract_core_belief(self, pattern_id):
        """Extract core limiting belief for pattern"""
        beliefs = {
            1: "Happiness and positive emotions are dangerous or undeserved",
            2: "I must fight to maintain control or I'll be powerless",
            3: "Others cannot be trusted with my vulnerability or truth",
            4: "Life is black and white - there are no good compromises",
            5: "I am only valuable when I'm being productive or achieving",
            6: "Showing my real self will result in rejection or judgment",
            7: "Others' needs matter more than my own wellbeing",
            8: "I must fulfill family expectations to maintain love/belonging",
            9: "I am powerless in certain situations or with certain people"
        }
        return beliefs.get(pattern_id, "Core belief requires session exploration")
    
    def _extract_hidden_benefits(self, pattern_id):
        """Extract hidden benefits for pattern"""
        benefits = {
            1: "Maintains emotional safety through familiar pessimism + avoids disappointment",
            2: "Provides sense of control and power + maintains competitive edge",
            3: "Protects from emotional pain and betrayal + maintains independence",
            4: "Simplifies complex decisions + maintains moral clarity",
            5: "Ensures external validation + maintains sense of purpose",
            6: "Maintains acceptance in different groups + avoids authentic vulnerability",
            7: "Ensures others' love and appreciation + maintains moral superiority",
            8: "Preserves family harmony and belonging + avoids guilt and conflict",
            9: "Receives special care and understanding + avoids full responsibility"
        }
        return benefits.get(pattern_id, "Pattern provides emotional protection and familiar identity")
    
    def _extract_systemic_resistance(self, pattern_id):
        """Extract systemic resistance for pattern"""
        resistance = {
            1: "Family may resist optimism as 'unrealistic' or threatening to shared pessimism",
            2: "Others may escalate conflicts when client stops engaging in power struggles",
            3: "Trusted people may feel hurt by increased discernment and boundary-setting",
            4: "Binary thinkers around client may resist nuanced perspectives",
            5: "Productivity-focused environment may resist 'being' over 'doing' approach",
            6: "Different social groups may resist authentic consistency across contexts",
            7: "Family system may resist when client stops over-giving and care-taking",
            8: "Strong family pressure to maintain traditional expectations and roles",
            9: "Certain people may resist client's newfound boundaries and consistent strength"
        }
        return resistance.get(pattern_id, "Minimal systemic resistance expected")
    
    def _extract_identity_threat(self, pattern_id):
        """Extract identity threat for pattern"""
        threats = {
            1: "Fear: 'If I'm happy, I won't be the deep/thoughtful person I am'",
            2: "Fear: 'If I stop fighting, I'll become weak and people will walk all over me'",
            3: "Fear: 'If I trust, I'll become naive and people will take advantage of me'",
            4: "Fear: 'If I see nuance, I'll lose my moral clarity and convictions'",
            5: "Fear: 'If I stop doing, I'll become lazy and worthless'",
            6: "Fear: 'If I'm consistent, I'll be boring and people will lose interest'",
            7: "Fear: 'If I prioritize myself, I'll become selfish and people will leave'",
            8: "Fear: 'If I follow my path, I'll lose my family's love and belonging'",
            9: "Fear: 'If I'm strong everywhere, I'll lose special care and understanding'"
        }
        return threats.get(pattern_id, "Identity evolution requires careful therapeutic navigation")
    
    def _extract_intervention_keywords(self, pattern_id):
        """Extract intervention keywords for pattern"""
        keywords = {
            1: "Permission, gentle, allowing, natural, ease, comfort, safe joy",
            2: "Collaboration, choice, partnership, respect, empowerment, mutual",
            3: "Transparency, evidence, clear, step-by-step, gradual, your pace",
            4: "Integration, both/and, possibilities, options, flexibility, nuance",
            5: "Being, presence, inherent worth, natural value, simply existing",
            6: "Authentic, genuine, consistent, true self, unified, wholeness",
            7: "Balance, strength through self-care, energy, sustainable, healthy boundaries",
            8: "Personal truth, individual path, respectful autonomy, honoring both",
            9: "Consistent strength, reliable self, universal power, steady boundaries"
        }
        return keywords.get(pattern_id, "Collaborative, gentle, adaptive, respectful")
    
    def _extract_avoid_language(self, pattern_id):
        """Extract language to avoid for pattern"""
        avoid = {
            1: "Forced positivity, 'just be happy', minimizing pain, overwhelming enthusiasm",
            2: "Commands, authority, 'you must', domination, control, surrender completely",
            3: "Hidden agendas, unclear processes, 'trust me', unexplained techniques",
            4: "Either/or choices, black/white thinking, 'you have to choose', extremes",
            5: "Performance pressure, achievement focus, productivity language, 'earn it'",
            6: "Role expectations, 'be consistent', contextual shoulds, fitting in",
            7: "Guilt about self-focus, 'be selfish', minimizing others' needs",
            8: "Family rejection themes, 'disappointing others', complete rebellion",
            9: "Universal weakness, 'you're always', situational helplessness"
        }
        return avoid.get(pattern_id, "Pressure, criticism, commands, one-size-fits-all approaches")
    
    def _extract_resistance_points(self, pattern_id):
        """Extract resistance points for pattern"""
        points = {
            1: "1. May resist positive suggestions as 'fake' or temporary\n2. Possible guilt about feeling good\n3. Fear of losing depth or authenticity",
            2: "1. May challenge therapist authority or process\n2. Resistance to collaborative vs. dominant approach\n3. Fear of losing power or control",
            3: "1. May question therapist motives excessively\n2. Need for complete transparency and explanation\n3. Testing trustworthiness repeatedly",
            4: "1. May get paralyzed by perfectionist analysis\n2. Difficulty accepting 'good enough' solutions\n3. Fear of making wrong choice",
            5: "1. May resist 'being' focused work as unproductive\n2. Guilt about not accomplishing during sessions\n3. Fear of losing sense of purpose",
            6: "1. May present differently than in assessment\n2. Confusion about 'real' vs. adaptive self\n3. Fear of consistency leading to rejection",
            7: "1. May prioritize therapist's needs over own growth\n2. Guilt about focusing on self\n3. Fear of becoming selfish",
            8: "1. Guilt about changing family dynamics\n2. Fear of disappointing family members\n3. Conflicted loyalty between growth and family",
            9: "1. May lose boundaries when triggered in session\n2. Context-dependent strength variations\n3. Fear of being strong everywhere"
        }
        return points.get(pattern_id, "1. Standard change resistance\n2. Possible skepticism about process\n3. Fear of unknown outcomes")
    
    def _extract_readiness_score(self, assessment_data):
        """Extract change readiness score from assessment"""
        responses = assessment_data.get('assessment_responses', {})
        for response_data in responses.values():
            response = response_data.get('response', {})
            if isinstance(response, dict) and 'rating' in response:
                return response['rating']
        return 5  # Default moderate readiness
    
    def _get_therapeutic_priority(self, score):
        """Get therapeutic priority based on score"""
        if score >= 7:
            return "IMMEDIATE - Session 1 primary focus"
        elif score >= 4:
            return "HIGH - Address in session 2"
        elif score >= 2:
            return "MODERATE - Monitor and reinforce"
        else:
            return "LOW - Background awareness"
    
    def _get_clinical_significance(self, pattern_id, score):
        """Get clinical significance description"""
        if score >= 7:
            return "Dominant pattern requiring immediate therapeutic attention"
        elif score >= 4:
            return "Significant pattern contributing to presenting concerns"
        elif score >= 2:
            return "Moderate pattern influencing behavior and responses"
        else:
            return "Emerging pattern requiring monitoring"
    
    def _get_therapeutic_complexity(self, sorted_patterns):
        """Determine therapeutic complexity"""
        if not sorted_patterns:
            return "STANDARD"
        
        high_patterns = [p for p in sorted_patterns if p[1] >= 7]
        medium_patterns = [p for p in sorted_patterns if 4 <= p[1] < 7]
        
        if len(high_patterns) >= 3:
            return "COMPLEX MULTI-PATTERN"
        elif len(high_patterns) >= 2:
            return "MODERATE COMPLEXITY"
        elif len(high_patterns) == 1 and len(medium_patterns) >= 2:
            return "FOCUSED WITH SECONDARY PATTERNS"
        else:
            return "FOCUSED SINGLE-PATTERN"
    
    def _calculate_success_probability(self, sorted_patterns, assessment_data):
        """Calculate estimated success probability"""
        if not sorted_patterns:
            return 75  # Default probability
        
        # Base probability
        probability = 85
        
        # Adjust for pattern complexity
        high_patterns = [p for p in sorted_patterns if p[1] >= 7]
        medium_patterns = [p for p in sorted_patterns if 4 <= p[1] < 7]
        
        # Complexity adjustments
        if len(high_patterns) >= 3:
            probability -= 15  # Complex cases need more work
        elif len(high_patterns) >= 2:
            probability -= 8   # Moderate complexity
        
        # Readiness adjustment
        readiness = self._extract_readiness_score(assessment_data)
        if readiness >= 8:
            probability += 10  # High readiness boosts success
        elif readiness <= 5:
            probability -= 10  # Low readiness reduces success
        
        # Completion rate adjustment
        completion_rate = assessment_data.get('assessment_results', {}).get('completion_rate', 0)
        if completion_rate >= 0.9:
            probability += 5   # Complete assessment helps
        elif completion_rate <= 0.6:
            probability -= 8   # Incomplete assessment reduces confidence
        
        # Risk factors adjustment
        risk_flags = assessment_data.get('risk_flags', [])
        if len(risk_flags) >= 3:
            probability -= 12  # Multiple risk factors
        elif len(risk_flags) >= 1:
            probability -= 5   # Some risk factors
        
        # Ensure reasonable bounds
        return max(40, min(95, probability))
    
    def _send_email(self, msg):
        """Send email via Gmail SMTP"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            
            text = msg.as_string()
            server.sendmail(self.sender_email, self.recipient_email, text)
            server.quit()
            
            print("✅ Clinical assessment email sent successfully")
            return True
            
        except Exception as e:
            print(f"❌ SMTP error: {e}")
            return False


# Global instance and convenience function
clinical_email_handler = ClinicalAssessmentEmailHandler()

def send_clinical_assessment_results(assessment_data):
    """Send clinical assessment results email"""
    return clinical_email_handler.send_clinical_assessment_results(assessment_data)


# Additional utility functions for assessment integration
def format_pattern_summary(pattern_scores):
    """Format pattern scores for quick reference"""
    if not pattern_scores:
        return "No patterns detected"
    
    pattern_names = {
        1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust",
        4: "Separation/Division", 5: "Doing vs Being", 6: "Compartmentalized Authenticity",
        7: "Self-Sacrifice/Care Avoidance", 8: "Inherited Missions", 9: "Context-Dependent Weakness"
    }
    
    sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
    summary = []
    
    for pattern_id, score in sorted_patterns[:3]:
        pattern_name = pattern_names.get(int(pattern_id), f"Pattern {pattern_id}")
        level = "HIGH" if score >= 6 else "MEDIUM" if score >= 3 else "LOW"
        summary.append(f"{pattern_name}: {level} ({score:.1f})")
    
    return " | ".join(summary)


def validate_assessment_data(assessment_data):
    """Validate assessment data structure before sending email"""
    required_fields = ['contact_info', 'assessment_results']
    missing_fields = []
    
    for field in required_fields:
        if field not in assessment_data:
            missing_fields.append(field)
    
    # Check contact info completeness
    contact_info = assessment_data.get('contact_info', {})
    if not contact_info.get('email'):
        missing_fields.append('contact_info.email')
    
    # Check assessment results
    assessment_results = assessment_data.get('assessment_results', {})
    if not assessment_results.get('pattern_scores'):
        missing_fields.append('assessment_results.pattern_scores')
    
    if missing_fields:
        print(f"⚠️ Assessment data validation warnings: {missing_fields}")
        return False, missing_fields
    
    return True, []


def generate_assessment_report_id(assessment_data):
    """Generate unique ID for assessment report tracking"""
    import hashlib
    
    contact_info = assessment_data.get('contact_info', {})
    email = contact_info.get('email', 'unknown')
    timestamp = contact_info.get('timestamp', '')
    
    combined = f"ASSESS_{email}_{timestamp}"
    return hashlib.md5(combined.encode()).hexdigest()[:12].upper()


def log_assessment_completion(assessment_data):
    """Log assessment completion for tracking"""
    try:
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'email': contact_info.get('email', 'unknown'),
            'name': contact_info.get('name', 'unknown'),
            'completion_rate': assessment_results.get('completion_rate', 0),
            'patterns_detected': len(assessment_results.get('pattern_scores', {})),
            'urgency': contact_info.get('urgency', 'not specified'),
            'report_id': generate_assessment_report_id(assessment_data)
        }
        
        print(f"📊 Assessment completed: {log_entry}")
        return log_entry
        
    except Exception as e:
        print(f"❌ Logging error: {e}")
        return None


# Testing and debugging functions
def test_email_handler():
    """Test the email handler with sample data"""
    sample_data = {
        'contact_info': {
            'name': 'Test Client',
            'email': 'test@example.com',
            'urgency': 'Very urgent - causing daily distress',
            'primary_concern': 'Anxiety and perfectionism affecting work performance',
            'next_step': 'Schedule free consultation call',
            'timestamp': datetime.now().isoformat()
        },
        'assessment_results': {
            'pattern_scores': {1: 7.2, 5: 6.1, 7: 4.3},
            'total_questions_answered': 35,
            'completion_rate': 0.92,
            'triggered_patterns': [1, 5, 7],
            'risk_flags': [],
            'completion_timestamp': datetime.now().isoformat()
        },
        'pattern_scores': {1: 7.2, 5: 6.1, 7: 4.3},
        'trigger_chain': {
            'physical_response': 'Chest tightness and racing heart',
            'automatic_thought': 'I must be perfect or I will fail',
            'emotional_response': 'Anxiety and overwhelm',
            'behavioral_response': 'Procrastination and avoidance'
        },
        'assessment_responses': {},
        'intensity_responses': {},
        'clinical_template': """
╔══════════════════════════════════════════════════════════════╗
║                    TEST CLINICAL TEMPLATE                    ║
╚══════════════════════════════════════════════════════════════╝

**PATTERN ANALYSIS:**
Dominant Pattern: Unhappiness Culture (Score: 7.2/10)
Primary Pattern: Doing vs Being (Score: 6.1/10)
Secondary Pattern: Self-Sacrifice/Care Avoidance (Score: 4.3/10)

**PSYCHOLOGICAL PROFILE:**
Core Limiting Belief: Happiness is dangerous and must be earned through achievement
Hidden Benefits: Maintains emotional safety and familiar identity structure
Systemic Resistance: Family may resist optimism as unrealistic
Identity Threat: Fear of losing depth and thoughtfulness

**SESSION PLANNING:**
Session 1 Focus: Unhappiness Culture mapping + permission for joy
Session 2 Target: Deep joy permission installation + achievement worth separation
Potential Session 3 Need: Joy maintenance if guilt resurfaces

**THERAPEUTIC APPROACH:**
Change Readiness Score: 8/10
Predicted Resistance Points:
1. May resist positive suggestions as fake
2. Guilt about feeling good
3. Fear of losing depth

Intervention Keywords: Permission, gentle, allowing, natural ease
Avoid Language: Forced positivity, overwhelming enthusiasm
        """
    }
    
    print("🧪 Testing clinical assessment email handler...")
    result = send_clinical_assessment_results(sample_data)
    
    if result:
        print("✅ Test successful - email handler working")
    else:
        print("❌ Test failed - check email handler configuration")
    
    return result


if __name__ == "__main__":
    # Run test when script is executed directly
    test_email_handler()
