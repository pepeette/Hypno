# # """
# # Clinical Assessment Email Handler
# # Specialized email handler for comprehensive behavioral pattern assessments
# # To be placed in utils/email_assess.py
# # """
# # import smtplib
# # import os
# # import json
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart
# # from datetime import datetime

# # class ClinicalAssessmentEmailHandler:
# #     """Specialized email handler for clinical assessment results"""
    
# #     def __init__(self):
# #         # Gmail SMTP configuration
# #         self.smtp_server = "smtp.gmail.com"
# #         self.smtp_port = 587
# #         self.sender_email = "laetitiasheppard@gmail.com"
# #         self.recipient_email = "laetitiasheppard@gmail.com"
        
# #         # Pattern name mappings
# #         self.pattern_names = {
# #             1: "Unhappiness Culture",
# #             2: "Power Struggles", 
# #             3: "Systematic Mistrust",
# #             4: "Separation/Division",
# #             5: "Doing vs Being",
# #             6: "Compartmentalized Authenticity",
# #             7: "Self-Sacrifice/Care Avoidance",
# #             8: "Inherited Missions",
# #             9: "Context-Dependent Weakness"
# #         }
        
# #         # Try to get password from environment variables or Streamlit secrets
# #         try:
# #             import streamlit as st
# #             self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
# #         except:
# #             self.password = os.environ.get("GMAIL_APP_PASSWORD", "")
    
# #     def send_clinical_assessment_results(self, assessment_data):
# #         """Send comprehensive clinical assessment results with full analysis"""
# #         try:
# #             # Extract key information safely
# #             contact_info = assessment_data.get('contact_info', {})
# #             assessment_results = assessment_data.get('assessment_results', {})
            
# #             email = contact_info.get('email', 'unknown@email.com')
# #             name = contact_info.get('name', 'Assessment Participant')
# #             urgency = contact_info.get('urgency', 'Not specified')
# #             concern = contact_info.get('primary_concern', 'Not specified')
# #             next_step = contact_info.get('next_step', 'Not specified')
            
# #             # Create enhanced email message
# #             msg = MIMEMultipart()
# #             msg['From'] = self.sender_email
# #             msg['To'] = self.recipient_email
# #             msg['Subject'] = self._generate_email_subject(name, urgency, assessment_results)
            
# #             # Build comprehensive email body
# #             body = self._build_comprehensive_email_body(assessment_data)
            
# #             msg.attach(MIMEText(body, 'plain'))
            
# #             # Send email if password is available
# #             if self.password:
# #                 return self._send_email(msg)
# #             else:
# #                 # Log the assessment data for debugging
# #                 print(f"Clinical Assessment: {name} ({email})")
# #                 print(f"Urgency: {urgency}")
# #                 print(f"Patterns detected: {len(assessment_results.get('pattern_scores', {}))}")
# #                 print(f"Completion rate: {assessment_results.get('completion_rate', 0)*100:.0f}%")
# #                 return True  # Simulate success when no password is configured
                
# #         except Exception as e:
# #             print(f"Error sending clinical assessment: {str(e)}")
# #             import traceback
# #             print(f"Full traceback: {traceback.format_exc()}")
# #             return False
    
# #     def _generate_email_subject(self, name, urgency, assessment_results):
# #         """Generate contextual email subject based on assessment data"""
# #         # Priority indicator
# #         if 'extremely urgent' in urgency.lower():
# #             priority = "🚨 PRIORITY"
# #         elif 'very urgent' in urgency.lower():
# #             priority = "⚡ HIGH PRIORITY"
# #         elif 'urgent' in urgency.lower():
# #             priority = "📋 URGENT"
# #         else:
# #             priority = "🧠 CLINICAL"
        
# #         # Pattern complexity indicator
# #         pattern_count = len(assessment_results.get('pattern_scores', {}))
# #         if pattern_count >= 5:
# #             complexity = "COMPLEX"
# #         elif pattern_count >= 3:
# #             complexity = "MULTI-PATTERN"
# #         else:
# #             complexity = "FOCUSED"
        
# #         # Completion indicator
# #         completion_rate = assessment_results.get('completion_rate', 0)
# #         if completion_rate >= 0.9:
# #             completion = "COMPLETE"
# #         elif completion_rate >= 0.7:
# #             completion = "SUBSTANTIAL"
# #         else:
# #             completion = "PARTIAL"
        
# #         return f"{priority} ASSESSMENT: {name} - {complexity} {completion} ANALYSIS"
    
# #     def _build_comprehensive_email_body(self, assessment_data):
# #         """Build comprehensive email body with all clinical data"""
# #         contact_info = assessment_data.get('contact_info', {})
# #         assessment_results = assessment_data.get('assessment_results', {})
        
# #         # Header section
# #         body = self._build_header_section(contact_info, assessment_results)
        
# #         # Clinical template section
# #         clinical_template = assessment_data.get('clinical_template', '')
# #         if clinical_template:
# #             body += f"\n{clinical_template}\n"
# #         else:
# #             body += "\n" + self._generate_clinical_template_fallback(assessment_data) + "\n"
        
# #         # Detailed analysis section
# #         body += self._build_detailed_analysis_section(assessment_data)
        
# #         # Assessment transcript section
# #         body += self._build_assessment_transcript_section(assessment_data)
        
# #         # Raw data section
# #         body += self._build_raw_data_section(assessment_data)
        
# #         # Action items section
# #         body += self._build_action_items_section(contact_info, assessment_results)
        
# #         # Footer
# #         body += self._build_footer_section()
        
# #         return body
    
# #     def _build_header_section(self, contact_info, assessment_results):
# #         """Build email header with client information"""
# #         name = contact_info.get('name', 'Not provided')
# #         email = contact_info.get('email', 'Not provided')
# #         phone = contact_info.get('phone', 'Not provided')
# #         urgency = contact_info.get('urgency', 'Not specified')
# #         concern = contact_info.get('primary_concern', 'Not specified')
# #         next_step = contact_info.get('next_step', 'Not specified')
# #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
# #         questions_answered = assessment_results.get('total_questions_answered', 0)
# #         completion_rate = assessment_results.get('completion_rate', 0) * 100
# #         patterns_detected = len(assessment_results.get('pattern_scores', {}))
        
# #         return f"""
# # 🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
# # ══════════════════════════════════════════════════════════════════

# # 📋 CLIENT INFORMATION:
# # Name: {name}
# # Email: {email}
# # Phone: {phone}
# # Primary Concern: {concern}
# # Urgency Level: {urgency}
# # Preferred Next Step: {next_step}
# # Assessment Completed: {timestamp}

# # 📊 ASSESSMENT METRICS:
# # Questions Answered: {questions_answered}
# # Completion Rate: {completion_rate:.0f}%
# # Patterns Detected: {patterns_detected}
# # Assessment Quality: {'EXCELLENT' if completion_rate >= 90 else 'GOOD' if completion_rate >= 70 else 'PARTIAL'}

# # ══════════════════════════════════════════════════════════════════
# # """
    
# #     def _generate_clinical_template_fallback(self, assessment_data):
# #         """Generate clinical template if not provided"""
# #         pattern_scores = assessment_data.get('pattern_scores', {})
        
# #         if not pattern_scores:
# #             return """
# # ╔══════════════════════════════════════════════════════════════╗
# # ║                    CLINICAL ANALYSIS TEMPLATE                ║
# # ║                   (Assessment Incomplete)                    ║
# # ╚══════════════════════════════════════════════════════════════╝

# # **PATTERN ANALYSIS:**
# # Dominant Pattern: Assessment requires completion for accurate analysis
# # Primary Pattern: Insufficient data for pattern ranking
# # Secondary Pattern: Additional questions needed

# # **PSYCHOLOGICAL PROFILE:**
# # Core Limiting Belief: Requires session exploration
# # Hidden Benefits: Cannot determine without complete assessment
# # Systemic Resistance: Assessment incomplete - manual evaluation needed
# # Identity Threat: Requires completed assessment for accurate profiling

# # **SESSION PLANNING:**
# # Session 1 Focus: Comprehensive pattern assessment and rapport building
# # Session 2 Target: Pattern-specific intervention based on session 1 findings
# # Potential Session 3 Need: Standard reinforcement protocol

# # **THERAPEUTIC APPROACH:**
# # Change Readiness Score: Not assessed
# # Predicted Resistance Points:
# # 1. Standard change resistance - unknown specific patterns
# # 2. Possible assessment completion resistance

# # Intervention Keywords: Adaptive approach based on session 1 findings
# # Avoid Language: Generic restrictions until pattern identification

# # ╔══════════════════════════════════════════════════════════════╗
# # ║         RECOMMENDATION: DISCOVERY CALL REQUIRED             ║
# # ╚══════════════════════════════════════════════════════════════╝
# # """
        
# #         # Get top patterns
# #         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
# #         dominant_pattern = self.pattern_names.get(int(sorted_patterns[0][0]), "Unknown") if sorted_patterns else "Unknown"
# #         dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
        
# #         primary_pattern = self.pattern_names.get(int(sorted_patterns[1][0]), "Unknown") if len(sorted_patterns) > 1 else "None detected"
# #         primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
        
# #         secondary_pattern = self.pattern_names.get(int(sorted_patterns[2][0]), "Unknown") if len(sorted_patterns) > 2 else "None detected"
# #         secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
        
# #         # Generate session recommendations based on dominant pattern
# #         session_plans = self._get_session_recommendations(int(sorted_patterns[0][0]) if sorted_patterns else 1)
        
# #         return f"""
# # ╔══════════════════════════════════════════════════════════════╗
# # ║                    CLINICAL ANALYSIS TEMPLATE                ║
# # ║                   Behavioral Pattern Assessment              ║
# # ╚══════════════════════════════════════════════════════════════╝

# # **PATTERN ANALYSIS:**
# # Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
# # Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10)
# # Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)

# # **PSYCHOLOGICAL PROFILE:**
# # Core Limiting Belief: {self._extract_core_belief(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
# # Hidden Benefits: {self._extract_hidden_benefits(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
# # Systemic Resistance: {self._extract_systemic_resistance(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
# # Identity Threat: {self._extract_identity_threat(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

# # **SESSION PLANNING:**
# # Session 1 Focus: {session_plans['session_1']}
# # Session 2 Target: {session_plans['session_2']}
# # Potential Session 3 Need: {session_plans['session_3']}

# # **THERAPEUTIC APPROACH:**
# # Change Readiness Score: {self._extract_readiness_score(assessment_data)}/10
# # Predicted Resistance Points:
# # {self._extract_resistance_points(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

# # Intervention Keywords: {self._extract_intervention_keywords(int(sorted_patterns[0][0]) if sorted_patterns else 1)}
# # Avoid Language: {self._extract_avoid_language(int(sorted_patterns[0][0]) if sorted_patterns else 1)}

# # ╔══════════════════════════════════════════════════════════════╗
# # ║                     CLINICAL NOTES                          ║
# # ╚══════════════════════════════════════════════════════════════╝

# # Pattern constellation indicates {self._get_therapeutic_complexity(sorted_patterns)} therapeutic approach required.
# # Estimated session success probability: {self._calculate_success_probability(sorted_patterns, assessment_data)}%
# # """
    
# #     def _build_detailed_analysis_section(self, assessment_data):
# #         """Build detailed pattern analysis section with behavioral sequence"""
# #         pattern_scores = assessment_data.get('pattern_scores', {})
# #         trigger_chain = assessment_data.get('trigger_chain', {})
        
# #         if not pattern_scores:
# #             return "\n🔍 DETAILED PATTERN ANALYSIS:\nInsufficient data for detailed analysis. Discovery call recommended.\n"
        
# #         section = "\n🔍 DETAILED PATTERN ANALYSIS:\n"
# #         section += "═" * 50 + "\n"
        
# #         # Pattern breakdown
# #         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
# #         for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
# #             pattern_name = self.pattern_names.get(int(pattern_id), f"Pattern {pattern_id}")
# #             activation_level = "HIGH" if score >= 6 else "MEDIUM" if score >= 3 else "LOW"
            
# #             section += f"\n{i}. {pattern_name}:\n"
# #             section += f"   Activation Level: {activation_level} (Score: {score:.1f})\n"
# #             section += f"   Therapeutic Priority: {self._get_therapeutic_priority(score)}\n"
# #             section += f"   Clinical Significance: {self._get_clinical_significance(int(pattern_id), score)}\n"
        
# #         # Enhanced trigger chain analysis
# #         if trigger_chain:
# #             section += f"\n🔗 COMPLETE BEHAVIORAL SEQUENCE ANALYSIS:\n"
# #             section += "Trigger → Physical → Thought → Emotion → Behavior → Consequence\n\n"
            
# #             sequence_components = {
# #                 'awareness_point': '🎯 TRIGGER',
# #                 'physical_response': '💓 PHYSICAL RESPONSE', 
# #                 'automatic_thought': '💭 AUTOMATIC THOUGHT',
# #                 'emotional_response': '❤️ EMOTIONAL RESPONSE',
# #                 'behavioral_response': '🏃 BEHAVIORAL RESPONSE',
# #                 'immediate_consequence': '⚡ IMMEDIATE CONSEQUENCE',
# #                 'longer_term_impact': '📈 LONGER-TERM IMPACT'
# #             }
            
# #             captured_count = 0
# #             total_count = len(sequence_components)
            
# #             for component_key, component_name in sequence_components.items():
# #                 response = trigger_chain.get(component_key, 'Not captured')
                
# #                 section += f"{component_name}:\n"
                
# #                 if response and response != 'Not captured' and response != 'Skipped':
# #                     captured_count += 1
# #                     section += f"   ✅ CAPTURED: \"{response}\"\n"
                    
# #                     # Add analysis based on component type
# #                     if component_key == 'physical_response':
# #                         section += f"   Clinical Notes: Somatic response indicates {self._analyze_somatic_response(response)}\n"
# #                     elif component_key == 'automatic_thought':
# #                         section += f"   Clinical Notes: Thought pattern shows {self._analyze_thought_pattern(response)}\n"
# #                     elif component_key == 'behavioral_response':
# #                         section += f"   Clinical Notes: Behavioral pattern indicates {self._analyze_behavioral_pattern_clinical(response)}\n"
# #                     elif component_key == 'immediate_consequence':
# #                         section += f"   Clinical Notes: Consequence pattern shows {self._analyze_consequence_pattern(response)}\n"
# #                 else:
# #                     section += f"   ❌ NOT CAPTURED - Session 1 priority\n"
# #                     section += f"   Clinical Impact: {self._get_missing_component_impact(component_key)}\n"
                
# #                 section += "\n"
            
# #             # Chain completeness assessment
# #             completeness_percentage = int((captured_count / total_count) * 100)
# #             section += f"BEHAVIORAL CHAIN COMPLETENESS: {completeness_percentage}% ({captured_count}/{total_count} components)\n"
            
# #             if completeness_percentage >= 70:
# #                 section += "✅ SUFFICIENT for targeted intervention design\n"
# #             elif completeness_percentage >= 50:
# #                 section += "⚠️ PARTIAL - Can proceed with Session 1 gap-filling focus\n"
# #             else:
# #                 section += "❌ INSUFFICIENT - Discovery call essential for intervention design\n"
            
# #             section += "\n"
        
# #         return section
    
# #     def _build_assessment_transcript_section(self, assessment_data):
# #         """Build complete assessment transcript section"""
# #         responses = assessment_data.get('assessment_responses', {})
        
# #         if not responses:
# #             return "\n📝 ASSESSMENT TRANSCRIPT:\nNo response data available\n"
        
# #         section = f"\n📝 COMPLETE ASSESSMENT TRANSCRIPT:\n"
# #         section += "═" * 60 + "\n"
# #         section += "Full client responses for clinical review and session preparation\n\n"
        
# #         # Sort responses by question ID
# #         sorted_responses = sorted(responses.items(), key=lambda x: int(str(x[0])))
        
# #         for q_id, response_data in sorted_responses:
# #             question_text = response_data.get('question_text', 'Unknown question')
# #             response = response_data.get('response', 'No response')
# #             intensity = response_data.get('intensity', None)
# #             timestamp = response_data.get('timestamp', 'Unknown time')
# #             question_type = response_data.get('question_type', 'Unknown type')
# #             phase = response_data.get('phase', 'Unknown phase')
            
# #             section += f"Question {q_id} [{phase.upper()}] - {question_type}:\n"
# #             section += f"   Q: {question_text}\n"
            
# #             # Format response based on type
# #             if isinstance(response, dict):
# #                 if 'rating' in response:
# #                     # Scale response
# #                     section += f"   A: Rating: {response['rating']}/10\n"
# #                     if response.get('follow_up'):
# #                         section += f"      Follow-up: {response['follow_up']}\n"
# #                 else:
# #                     # Multi-select weighted response
# #                     section += f"   A: Multiple selections with intensities:\n"
# #                     for item, item_intensity in response.items():
# #                         section += f"      - {item}: {item_intensity}/7\n"
# #             elif isinstance(response, list):
# #                 # Multi-select response
# #                 section += f"   A: {', '.join(response)}\n"
# #             else:
# #                 # Text or single choice response
# #                 section += f"   A: {response}\n"
            
# #             # Add intensity if available
# #             if intensity:
# #                 section += f"   Intensity: {intensity}/7\n"
            
# #             # Add timestamp
# #             try:
# #                 from datetime import datetime
# #                 dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
# #                 formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
# #                 section += f"   Completed: {formatted_time}\n"
# #             except:
# #                 section += f"   Completed: {timestamp}\n"
            
# #             section += "\n"
        
# #         # Add summary statistics
# #         section += f"TRANSCRIPT SUMMARY:\n"
# #         section += f"Total Questions: {len(responses)}\n"
        
# #         # Count by phase
# #         phase_counts = {}
# #         for response_data in responses.values():
# #             phase = response_data.get('phase', 'unknown')
# #             phase_counts[phase] = phase_counts.get(phase, 0) + 1
        
# #         section += f"Responses by Phase: {phase_counts}\n"
        
# #         # Count text vs choice responses
# #         text_responses = sum(1 for r in responses.values() if isinstance(r.get('response'), str) and len(r.get('response', '')) > 50)
# #         choice_responses = len(responses) - text_responses
        
# #         section += f"Text Responses: {text_responses}\n"
# #         section += f"Choice Responses: {choice_responses}\n"
        
# #         # Intensity data summary
# #         intensity_responses = assessment_data.get('intensity_responses', {})
# #         if intensity_responses:
# #             avg_intensity = sum(intensity_responses.values()) / len(intensity_responses)
# #             section += f"Average Response Intensity: {avg_intensity:.1f}/7\n"
        
# #         section += "\n"
        
# #         return section

# #     def _build_raw_data_section(self, assessment_data):
# #         """Build raw data section for clinical review"""
# #         section = f"\n📊 RAW ASSESSMENT DATA:\n"
# #         section += "═" * 50 + "\n"
        
# #         # Pattern scores
# #         pattern_scores = assessment_data.get('pattern_scores', {})
# #         section += f"Pattern Scores: {pattern_scores}\n"
        
# #         # Assessment metadata
# #         assessment_results = assessment_data.get('assessment_results', {})
# #         section += f"Triggered Patterns: {assessment_results.get('triggered_patterns', [])}\n"
# #         section += f"Risk Flags: {assessment_results.get('risk_flags', [])}\n"
# #         section += f"Adaptive Paths: {assessment_results.get('adaptive_paths_triggered', [])}\n"
# #         section += f"Phase Completion: {assessment_results.get('phase_completion', {})}\n"
        
# #         # Response sampling (first 3 responses for privacy)
# #         responses = assessment_data.get('assessment_responses', {})
# #         if responses:
# #             section += f"\nSample Responses (first 3):\n"
# #             for i, (q_id, response_data) in enumerate(list(responses.items())[:3], 1):
# #                 question_text = response_data.get('question_text', 'Unknown question')
# #                 response = response_data.get('response', 'No response')
# #                 section += f"   Q{q_id}: {question_text[:50]}...\n"
# #                 section += f"   Response: {str(response)[:100]}...\n"
        
# #         # Intensity data
# #         intensity_responses = assessment_data.get('intensity_responses', {})
# #         if intensity_responses:
# #             section += f"\nIntensity Mappings: {intensity_responses}\n"
        
# #         return section
    
# #     def _build_action_items_section(self, contact_info, assessment_results):
# #         """Build action items section"""
# #         urgency = contact_info.get('urgency', 'Not specified')
# #         email = contact_info.get('email', 'Not provided')
# #         next_step = contact_info.get('next_step', 'Not specified')
# #         patterns_count = len(assessment_results.get('pattern_scores', {}))
# #         completion_rate = assessment_results.get('completion_rate', 0)
        
# #         section = f"\n⚡ IMMEDIATE ACTION ITEMS:\n"
# #         section += "═" * 50 + "\n"
        
# #         # Contact timeline
# #         if 'extremely urgent' in urgency.lower():
# #             contact_window = "4-6 hours"
# #             priority = "EMERGENCY"
# #         elif 'very urgent' in urgency.lower():
# #             contact_window = "12-24 hours"
# #             priority = "HIGH"
# #         elif 'urgent' in urgency.lower():
# #             contact_window = "24-48 hours"
# #             priority = "ELEVATED"
# #         else:
# #             contact_window = "48-72 hours"
# #             priority = "STANDARD"
        
# #         section += f"1. PRIORITY CONTACT: {email} within {contact_window}\n"
# #         section += f"   Contact Priority Level: {priority}\n"
# #         section += f"   Client Requested: {next_step}\n\n"
        
# #         # Clinical preparation
# #         if completion_rate >= 0.8 and patterns_count >= 3:
# #             section += "2. CLINICAL PREPARATION:\n"
# #             section += "   ✓ Comprehensive assessment complete\n"
# #             section += "   ✓ Pattern-specific approach ready\n"
# #             section += "   ✓ Session planning template above\n"
# #             section += "   → Proceed with targeted intervention\n\n"
# #         elif completion_rate >= 0.6:
# #             section += "2. CLINICAL PREPARATION:\n"
# #             section += "   ⚠ Substantial data available\n"
# #             section += "   → Brief discovery call to fill gaps\n"
# #             section += "   → Proceed with hybrid approach\n\n"
# #         else:
# #             section += "2. CLINICAL PREPARATION:\n"
# #             section += "   ❌ Insufficient assessment data\n"
# #             section += "   → Full discovery call required\n"
# #             section += "   → Standard 2-session approach\n\n"
        
# #         # Follow-up actions
# #         section += "3. FOLLOW-UP PROTOCOL:\n"
# #         section += "   □ Send confirmation email to client\n"
# #         section += "   □ Schedule appropriate session type\n"
# #         section += "   □ Prepare session materials based on patterns\n"
# #         section += "   □ Set up progress tracking system\n"
        
# #         return section
    
# #     def _build_footer_section(self):
# #         """Build email footer"""
# #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
# #         return f"""
# # ══════════════════════════════════════════════════════════════════
# # Bangkok Hypnotherapy Clinic - Clinical Assessment System
# # Comprehensive Behavioral Pattern Analysis Generated: {timestamp}
# # System Status: Operational | Data Quality: Verified | Action Required: Review Above
# # ══════════════════════════════════════════════════════════════════
# # """
    
# #     # Helper methods for clinical template generation
# #     def _get_session_recommendations(self, pattern_id):
# #         """Get session recommendations for specific pattern"""
# #         recommendations = {
# #             1: {
# #                 'session_1': "Unhappiness Culture mapping + permission for joy + gentle positive anchoring",
# #                 'session_2': "Deep joy permission installation + reframe happiness beliefs + positive emotion anchors",
# #                 'session_3': "Joy maintenance if relapse into pessimism or guilt about happiness"
# #             },
# #             2: {
# #                 'session_1': "Power struggle pattern analysis + collaboration establishment + shared control",
# #                 'session_2': "Transform win/lose to win/win mindset + install collaboration reflexes + peace anchors",
# #                 'session_3': "Conflict de-escalation if old fighting patterns resurface"
# #             },
# #             3: {
# #                 'session_1': "Trust violation history + safety establishment + graduated vulnerability",
# #                 'session_2': "Install healthy discernment vs. systematic mistrust + trust capacity building",
# #                 'session_3': "Trust maintenance if cynicism returns or trust betrayal occurs"
# #             },
# #             4: {
# #                 'session_1': "Binary thinking identification + both/and introduction + cognitive flexibility",
# #                 'session_2': "Install nuanced thinking + creative option generation + decision confidence",
# #                 'session_3': "Flexibility maintenance if black/white thinking resurfaces under stress"
# #             },
# #             5: {
# #                 'session_1': "Achievement addiction mapping + inherent worth establishment + being practice",
# #                 'session_2': "Install worth independence from productivity + being/doing balance + rest permission",
# #                 'session_3': "Worth maintenance if productivity pressure returns"
# #             },
# #             6: {
# #                 'session_1': "Authentic self identification + consistency across contexts + integration work",
# #                 'session_2': "Install unified authentic self + consistent expression + context independence",
# #                 'session_3': "Authenticity maintenance if compartmentalization returns under pressure"
# #             },
# #             7: {
# #                 'session_1': "Self-sacrifice pattern mapping + self-care as strength reframe + boundary establishment",
# #                 'session_2': "Install healthy balance + self-care habits + boundary maintenance reflexes",
# #                 'session_3': "Balance maintenance if caretaking patterns resurface"
# #             },
# #             8: {
# #                 'session_1': "Family mission identification + personal desire differentiation + loyalty vs. autonomy",
# #                 'session_2': "Install personal path confidence + family respect integration + autonomous choice",
# #                 'session_3': "Autonomy maintenance if family pressure increases"
# #             },
# #             9: {
# #                 'session_1': "Context-dependent weakness mapping + universal strength identification + boundary work",
# #                 'session_2': "Install consistent boundaries + context-independent strength + situational confidence",
# #                 'session_3': "Strength maintenance if old contexts trigger boundary collapse"
# #             }
# #         }
        
# #         return recommendations.get(pattern_id, {
# #             'session_1': "Comprehensive pattern assessment and initial rapport building",
# #             'session_2': "Core pattern transformation and positive programming",
# #             'session_3': "Standard reinforcement if needed"
# #         })
    
# #     def _extract_core_belief(self, pattern_id):
# #         """Extract core limiting belief for pattern"""
# #         beliefs = {
# #             1: "Happiness and positive emotions are dangerous or undeserved",
# #             2: "I must fight to maintain control or I'll be powerless",
# #             3: "Others cannot be trusted with my vulnerability or truth",
# #             4: "Life is black and white - there are no good compromises",
# #             5: "I am only valuable when I'm being productive or achieving",
# #             6: "Showing my real self will result in rejection or judgment",
# #             7: "Others' needs matter more than my own wellbeing",
# #             8: "I must fulfill family expectations to maintain love/belonging",
# #             9: "I am powerless in certain situations or with certain people"
# #         }
# #         return beliefs.get(pattern_id, "Core belief requires session exploration")
    
# #     def _extract_hidden_benefits(self, pattern_id):
# #         """Extract hidden benefits for pattern"""
# #         benefits = {
# #             1: "Maintains emotional safety through familiar pessimism + avoids disappointment",
# #             2: "Provides sense of control and power + maintains competitive edge",
# #             3: "Protects from emotional pain and betrayal + maintains independence",
# #             4: "Simplifies complex decisions + maintains moral clarity",
# #             5: "Ensures external validation + maintains sense of purpose",
# #             6: "Maintains acceptance in different groups + avoids authentic vulnerability",
# #             7: "Ensures others' love and appreciation + maintains moral superiority",
# #             8: "Preserves family harmony and belonging + avoids guilt and conflict",
# #             9: "Receives special care and understanding + avoids full responsibility"
# #         }
# #         return benefits.get(pattern_id, "Pattern provides emotional protection and familiar identity")
    
# #     def _extract_systemic_resistance(self, pattern_id):
# #         """Extract systemic resistance for pattern"""
# #         resistance = {
# #             1: "Family may resist optimism as 'unrealistic' or threatening to shared pessimism",
# #             2: "Others may escalate conflicts when client stops engaging in power struggles",
# #             3: "Trusted people may feel hurt by increased discernment and boundary-setting",
# #             4: "Binary thinkers around client may resist nuanced perspectives",
# #             5: "Productivity-focused environment may resist 'being' over 'doing' approach",
# #             6: "Different social groups may resist authentic consistency across contexts",
# #             7: "Family system may resist when client stops over-giving and care-taking",
# #             8: "Strong family pressure to maintain traditional expectations and roles",
# #             9: "Certain people may resist client's newfound boundaries and consistent strength"
# #         }
# #         return resistance.get(pattern_id, "Minimal systemic resistance expected")
    
# #     def _extract_identity_threat(self, pattern_id):
# #         """Extract identity threat for pattern"""
# #         threats = {
# #             1: "Fear: 'If I'm happy, I won't be the deep/thoughtful person I am'",
# #             2: "Fear: 'If I stop fighting, I'll become weak and people will walk all over me'",
# #             3: "Fear: 'If I trust, I'll become naive and people will take advantage of me'",
# #             4: "Fear: 'If I see nuance, I'll lose my moral clarity and convictions'",
# #             5: "Fear: 'If I stop doing, I'll become lazy and worthless'",
# #             6: "Fear: 'If I'm consistent, I'll be boring and people will lose interest'",
# #             7: "Fear: 'If I prioritize myself, I'll become selfish and people will leave'",
# #             8: "Fear: 'If I follow my path, I'll lose my family's love and belonging'",
# #             9: "Fear: 'If I'm strong everywhere, I'll lose special care and understanding'"
# #         }
# #         return threats.get(pattern_id, "Identity evolution requires careful therapeutic navigation")
    
# #     def _extract_intervention_keywords(self, pattern_id):
# #         """Extract intervention keywords for pattern"""
# #         keywords = {
# #             1: "Permission, gentle, allowing, natural, ease, comfort, safe joy",
# #             2: "Collaboration, choice, partnership, respect, empowerment, mutual",
# #             3: "Transparency, evidence, clear, step-by-step, gradual, your pace",
# #             4: "Integration, both/and, possibilities, options, flexibility, nuance",
# #             5: "Being, presence, inherent worth, natural value, simply existing",
# #             6: "Authentic, genuine, consistent, true self, unified, wholeness",
# #             7: "Balance, strength through self-care, energy, sustainable, healthy boundaries",
# #             8: "Personal truth, individual path, respectful autonomy, honoring both",
# #             9: "Consistent strength, reliable self, universal power, steady boundaries"
# #         }
# #         return keywords.get(pattern_id, "Collaborative, gentle, adaptive, respectful")
    
# #     def _extract_avoid_language(self, pattern_id):
# #         """Extract language to avoid for pattern"""
# #         avoid = {
# #             1: "Forced positivity, 'just be happy', minimizing pain, overwhelming enthusiasm",
# #             2: "Commands, authority, 'you must', domination, control, surrender completely",
# #             3: "Hidden agendas, unclear processes, 'trust me', unexplained techniques",
# #             4: "Either/or choices, black/white thinking, 'you have to choose', extremes",
# #             5: "Performance pressure, achievement focus, productivity language, 'earn it'",
# #             6: "Role expectations, 'be consistent', contextual shoulds, fitting in",
# #             7: "Guilt about self-focus, 'be selfish', minimizing others' needs",
# #             8: "Family rejection themes, 'disappointing others', complete rebellion",
# #             9: "Universal weakness, 'you're always', situational helplessness"
# #         }
# #         return avoid.get(pattern_id, "Pressure, criticism, commands, one-size-fits-all approaches")
    
# #     def _extract_resistance_points(self, pattern_id):
# #         """Extract resistance points for pattern"""
# #         points = {
# #             1: "1. May resist positive suggestions as 'fake' or temporary\n2. Possible guilt about feeling good\n3. Fear of losing depth or authenticity",
# #             2: "1. May challenge therapist authority or process\n2. Resistance to collaborative vs. dominant approach\n3. Fear of losing power or control",
# #             3: "1. May question therapist motives excessively\n2. Need for complete transparency and explanation\n3. Testing trustworthiness repeatedly",
# #             4: "1. May get paralyzed by perfectionist analysis\n2. Difficulty accepting 'good enough' solutions\n3. Fear of making wrong choice",
# #             5: "1. May resist 'being' focused work as unproductive\n2. Guilt about not accomplishing during sessions\n3. Fear of losing sense of purpose",
# #             6: "1. May present differently than in assessment\n2. Confusion about 'real' vs. adaptive self\n3. Fear of consistency leading to rejection",
# #             7: "1. May prioritize therapist's needs over own growth\n2. Guilt about focusing on self\n3. Fear of becoming selfish",
# #             8: "1. Guilt about changing family dynamics\n2. Fear of disappointing family members\n3. Conflicted loyalty between growth and family",
# #             9: "1. May lose boundaries when triggered in session\n2. Context-dependent strength variations\n3. Fear of being strong everywhere"
# #         }
# #         return points.get(pattern_id, "1. Standard change resistance\n2. Possible skepticism about process\n3. Fear of unknown outcomes")
    
# #     def _extract_readiness_score(self, assessment_data):
# #         """Extract change readiness score from assessment"""
# #         responses = assessment_data.get('assessment_responses', {})
# #         for response_data in responses.values():
# #             response = response_data.get('response', {})
# #             if isinstance(response, dict) and 'rating' in response:
# #                 return response['rating']
# #         return 5  # Default moderate readiness
    
# #     def _get_therapeutic_priority(self, score):
# #         """Get therapeutic priority based on score"""
# #         if score >= 7:
# #             return "IMMEDIATE - Session 1 primary focus"
# #         elif score >= 4:
# #             return "HIGH - Address in session 2"
# #         elif score >= 2:
# #             return "MODERATE - Monitor and reinforce"
# #         else:
# #             return "LOW - Background awareness"
    
# #     def _get_clinical_significance(self, pattern_id, score):
# #         """Get clinical significance description"""
# #         if score >= 7:
# #             return "Dominant pattern requiring immediate therapeutic attention"
# #         elif score >= 4:
# #             return "Significant pattern contributing to presenting concerns"
# #         elif score >= 2:
# #             return "Moderate pattern influencing behavior and responses"
# #         else:
# #             return "Emerging pattern requiring monitoring"
    
# #     def _get_therapeutic_complexity(self, sorted_patterns):
# #         """Determine therapeutic complexity"""
# #         if not sorted_patterns:
# #             return "STANDARD"
        
# #         high_patterns = [p for p in sorted_patterns if p[1] >= 7]
# #         medium_patterns = [p for p in sorted_patterns if 4 <= p[1] < 7]
        
# #         if len(high_patterns) >= 3:
# #             return "COMPLEX MULTI-PATTERN"
# #         elif len(high_patterns) >= 2:
# #             return "MODERATE COMPLEXITY"
# #         elif len(high_patterns) == 1 and len(medium_patterns) >= 2:
# #             return "FOCUSED WITH SECONDARY PATTERNS"
# #         else:
# #             return "FOCUSED SINGLE-PATTERN"
    
# #     def _calculate_success_probability(self, sorted_patterns, assessment_data):
# #         """Calculate estimated success probability"""
# #         if not sorted_patterns:
# #             return 75  # Default probability
        
# #         # Base probability
# #         probability = 85
        
# #         # Adjust for pattern complexity
# #         high_patterns = [p for p in sorted_patterns if p[1] >= 7]
# #         medium_patterns = [p for p in sorted_patterns if 4 <= p[1] < 7]
        
# #         # Complexity adjustments
# #         if len(high_patterns) >= 3:
# #             probability -= 15  # Complex cases need more work
# #         elif len(high_patterns) >= 2:
# #             probability -= 8   # Moderate complexity
        
# #         # Readiness adjustment
# #         readiness = self._extract_readiness_score(assessment_data)
# #         if readiness >= 8:
# #             probability += 10  # High readiness boosts success
# #         elif readiness <= 5:
# #             probability -= 10  # Low readiness reduces success
        
# #         # Completion rate adjustment
# #         completion_rate = assessment_data.get('assessment_results', {}).get('completion_rate', 0)
# #         if completion_rate >= 0.9:
# #             probability += 5   # Complete assessment helps
# #         elif completion_rate <= 0.6:
# #             probability -= 8   # Incomplete assessment reduces confidence
        
# #         # Risk factors adjustment
# #         risk_flags = assessment_data.get('risk_flags', [])
# #         if len(risk_flags) >= 3:
# #             probability -= 12  # Multiple risk factors
# #         elif len(risk_flags) >= 1:
# #             probability -= 5   # Some risk factors
        
# #         # Ensure reasonable bounds
# #         return max(40, min(95, probability))
    
# #     def _analyze_somatic_response(self, response):
# #         """Analyze somatic response for clinical notes"""
# #         response_lower = response.lower()
# #         if any(word in response_lower for word in ['chest', 'heart', 'breathing']):
# #             return "anxiety/stress activation in cardiac/respiratory system"
# #         elif any(word in response_lower for word in ['stomach', 'nausea', 'digestive']):
# #             return "gut-brain connection activation - deep emotional processing"
# #         elif any(word in response_lower for word in ['muscle', 'tension', 'jaw']):
# #             return "muscular system activation - fight/flight preparation"
# #         elif any(word in response_lower for word in ['numb', 'disconnect', 'freeze']):
# #             return "dorsal vagal shutdown - dissociative protection response"
# #         else:
# #             return "complex somatic activation requiring exploration"
    
# #     def _analyze_thought_pattern(self, thought):
# #         """Analyze thought pattern for clinical notes"""
# #         thought_lower = thought.lower()
# #         if any(phrase in thought_lower for phrase in ['not good enough', 'inadequate', 'failure']):
# #             return "core inadequacy belief system activation"
# #         elif any(phrase in thought_lower for phrase in ['must', 'should', 'have to']):
# #             return "perfectionist/demanding cognitive schema"
# #         elif any(phrase in thought_lower for phrase in ['danger', 'threat', 'bad']):
# #             return "threat detection and safety-seeking cognitive pattern"
# #         elif any(phrase in thought_lower for phrase in ['always', 'never', 'everyone']):
# #             return "all-or-nothing thinking with cognitive rigidity"
# #         else:
# #             return "complex cognitive pattern requiring deeper analysis"
    
# #     def _analyze_behavioral_pattern_clinical(self, behavior):
# #         """Analyze behavioral pattern for clinical notes"""
# #         behavior_lower = behavior.lower()
# #         if any(word in behavior_lower for word in ['avoid', 'withdraw', 'escape']):
# #             return "avoidance/withdrawal pattern - flight response activation"
# #         elif any(word in behavior_lower for word in ['busy', 'active', 'productive']):
# #             return "hyperactivity/doing addiction - emotional regulation through action"
# #         elif any(word in behavior_lower for word in ['argue', 'fight', 'defend']):
# #             return "confrontation/defense pattern - fight response activation"
# #         elif any(word in behavior_lower for word in ['help', 'others', 'care']):
# #             return "caretaking/self-sacrifice pattern - fawn response"
# #         elif any(word in behavior_lower for word in ['shut down', 'numb', 'disconnect']):
# #             return "emotional shutdown pattern - freeze response"
# #         else:
# #             return "complex behavioral response requiring pattern analysis"
    
# #     def _analyze_consequence_pattern(self, consequence):
# #         """Analyze consequence pattern for clinical notes"""
# #         consequence_lower = consequence.lower()
# #         if any(word in consequence_lower for word in ['worse', 'agitated', 'escalate']):
# #             return "escalating pattern - behavior increases distress (paradoxical reinforcement)"
# #         elif any(word in consequence_lower for word in ['relief', 'better', 'calm']):
# #             return "reinforcing pattern - behavior provides temporary relief (maintains cycle)"
# #         elif any(word in consequence_lower for word in ['numb', 'empty', 'nothing']):
# #             return "numbing pattern - behavior creates emotional disconnection"
# #         elif any(word in consequence_lower for word in ['guilt', 'shame', 'regret']):
# #             return "self-punishment pattern - behavior triggers self-criticism cycle"
# #         else:
# #             return "complex consequence pattern requiring cycle analysis"
    
# #     def _get_missing_component_impact(self, component_key):
# #         """Get clinical impact of missing component"""
# #         impacts = {
# #             'awareness_point': "Cannot design trigger-specific interventions",
# #             'physical_response': "Cannot implement somatic regulation techniques",
# #             'automatic_thought': "Cannot target cognitive restructuring effectively",
# #             'emotional_response': "Cannot design emotional regulation strategies",
# #             'behavioral_response': "Cannot create alternative response patterns",
# #             'immediate_consequence': "Cannot address reinforcement mechanisms",
# #             'longer_term_impact': "Limits intervention precision and effectiveness"
# #         }
# #         return impacts.get(component_key, "Limits intervention precision and effectiveness")
    
# #     def _send_email(self, msg):
# #         """Send email via Gmail SMTP"""
# #         try:
# #             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
# #             server.starttls()
# #             server.login(self.sender_email, self.password)
            
# #             text = msg.as_string()
# #             server.sendmail(self.sender_email, self.recipient_email, text)
# #             server.quit()
            
# #             print("✅ Clinical assessment email sent successfully")
# #             return True
            
# #         except Exception as e:
# #             print(f"❌ SMTP error: {e}")
# #             return False


# # # Global instance and convenience function
# # clinical_email_handler = ClinicalAssessmentEmailHandler()

# # def send_clinical_assessment_results(assessment_data):
# #     """Send clinical assessment results email"""
# #     return clinical_email_handler.send_clinical_assessment_results(assessment_data)


# # # Additional utility functions for assessment integration
# # def format_pattern_summary(pattern_scores):
# #     """Format pattern scores for quick reference"""
# #     if not pattern_scores:
# #         return "No patterns detected"
    
# #     pattern_names = {
# #         1: "Unhappiness Culture", 2: "Power Struggles", 3: "Systematic Mistrust",
# #         4: "Separation/Division", 5: "Doing vs Being", 6: "Compartmentalized Authenticity",
# #         7: "Self-Sacrifice/Care Avoidance", 8: "Inherited Missions", 9: "Context-Dependent Weakness"
# #     }
    
# #     sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
# #     summary = []
    
# #     for pattern_id, score in sorted_patterns[:3]:
# #         pattern_name = pattern_names.get(int(pattern_id), f"Pattern {pattern_id}")
# #         level = "HIGH" if score >= 6 else "MEDIUM" if score >= 3 else "LOW"
# #         summary.append(f"{pattern_name}: {level} ({score:.1f})")
    
# #     return " | ".join(summary)


# # def validate_assessment_data(assessment_data):
# #     """Validate assessment data structure before sending email"""
# #     required_fields = ['contact_info', 'assessment_results']
# #     missing_fields = []
    
# #     for field in required_fields:
# #         if field not in assessment_data:
# #             missing_fields.append(field)
    
# #     # Check contact info completeness
# #     contact_info = assessment_data.get('contact_info', {})
# #     if not contact_info.get('email'):
# #         missing_fields.append('contact_info.email')
    
# #     # Check assessment results
# #     assessment_results = assessment_data.get('assessment_results', {})
# #     if not assessment_results.get('pattern_scores'):
# #         missing_fields.append('assessment_results.pattern_scores')
    
# #     if missing_fields:
# #         print(f"⚠️ Assessment data validation warnings: {missing_fields}")
# #         return False, missing_fields
    
# #     return True, []


# # def generate_assessment_report_id(assessment_data):
# #     """Generate unique ID for assessment report tracking"""
# #     import hashlib
    
# #     contact_info = assessment_data.get('contact_info', {})
# #     email = contact_info.get('email', 'unknown')
# #     timestamp = contact_info.get('timestamp', '')
    
# #     combined = f"ASSESS_{email}_{timestamp}"
# #     return hashlib.md5(combined.encode()).hexdigest()[:12].upper()


# # def log_assessment_completion(assessment_data):
# #     """Log assessment completion for tracking"""
# #     try:
# #         contact_info = assessment_data.get('contact_info', {})
# #         assessment_results = assessment_data.get('assessment_results', {})
        
# #         log_entry = {
# #             'timestamp': datetime.now().isoformat(),
# #             'email': contact_info.get('email', 'unknown'),
# #             'name': contact_info.get('name', 'unknown'),
# #             'completion_rate': assessment_results.get('completion_rate', 0),
# #             'patterns_detected': len(assessment_results.get('pattern_scores', {})),
# #             'urgency': contact_info.get('urgency', 'not specified'),
# #             'report_id': generate_assessment_report_id(assessment_data)
# #         }
        
# #         print(f"📊 Assessment completed: {log_entry}")
# #         return log_entry
        
# #     except Exception as e:
# #         print(f"❌ Logging error: {e}")
# #         return None


# # # Testing and debugging functions
# # def test_email_handler():
# #     """Test the email handler with sample data"""
# #     sample_data = {
# #         'contact_info': {
# #             'name': 'Test Client',
# #             'email': 'test@example.com',
# #             'urgency': 'Very urgent - causing daily distress',
# #             'primary_concern': 'Anxiety and perfectionism affecting work performance',
# #             'next_step': 'Schedule free consultation call',
# #             'timestamp': datetime.now().isoformat()
# #         },
# #         'assessment_results': {
# #             'pattern_scores': {1: 7.2, 5: 6.1, 7: 4.3},
# #             'total_questions_answered': 35,
# #             'completion_rate': 0.92,
# #             'triggered_patterns': [1, 5, 7],
# #             'risk_flags': [],
# #             'completion_timestamp': datetime.now().isoformat()
# #         },
# #         'pattern_scores': {1: 7.2, 5: 6.1, 7: 4.3},
# #         'trigger_chain': {
# #             'physical_response': 'Chest tightness and racing heart',
# #             'automatic_thought': 'I must be perfect or I will fail',
# #             'emotional_response': 'Anxiety and overwhelm',
# #             'behavioral_response': 'Procrastination and avoidance'
# #         },
# #         'assessment_responses': {},
# #         'intensity_responses': {},
# #         'clinical_template': """
# # ╔══════════════════════════════════════════════════════════════╗
# # ║                    TEST CLINICAL TEMPLATE                    ║
# # ╚══════════════════════════════════════════════════════════════╝

# # **PATTERN ANALYSIS:**
# # Dominant Pattern: Unhappiness Culture (Score: 7.2/10)
# # Primary Pattern: Doing vs Being (Score: 6.1/10)
# # Secondary Pattern: Self-Sacrifice/Care Avoidance (Score: 4.3/10)

# # **PSYCHOLOGICAL PROFILE:**
# # Core Limiting Belief: Happiness is dangerous and must be earned through achievement
# # Hidden Benefits: Maintains emotional safety and familiar identity structure
# # Systemic Resistance: Family may resist optimism as unrealistic
# # Identity Threat: Fear of losing depth and thoughtfulness

# # **SESSION PLANNING:**
# # Session 1 Focus: Unhappiness Culture mapping + permission for joy
# # Session 2 Target: Deep joy permission installation + achievement worth separation
# # Potential Session 3 Need: Joy maintenance if guilt resurfaces

# # **THERAPEUTIC APPROACH:**
# # Change Readiness Score: 8/10
# # Predicted Resistance Points:
# # 1. May resist positive suggestions as fake
# # 2. Guilt about feeling good
# # 3. Fear of losing depth

# # Intervention Keywords: Permission, gentle, allowing, natural ease
# # Avoid Language: Forced positivity, overwhelming enthusiasm
# #         """
# #     }
    
# #     print("🧪 Testing clinical assessment email handler...")
# #     result = send_clinical_assessment_results(sample_data)
    
# #     if result:
# #         print("✅ Test successful - email handler working")
# #     else:
# #         print("❌ Test failed - check email handler configuration")
    
# #     return result


# # def debug_assessment_data(assessment_data):
# #     """Debug function to examine assessment data structure"""
# #     print("🔍 DEBUGGING ASSESSMENT DATA STRUCTURE:")
# #     print("=" * 50)
    
# #     # Check main sections
# #     main_sections = ['contact_info', 'assessment_results', 'pattern_scores', 'trigger_chain']
# #     for section in main_sections:
# #         if section in assessment_data:
# #             print(f"✅ {section}: Present")
# #             if isinstance(assessment_data[section], dict):
# #                 print(f"   Keys: {list(assessment_data[section].keys())}")
# #             else:
# #                 print(f"   Type: {type(assessment_data[section])}")
# #         else:
# #             print(f"❌ {section}: Missing")
    
# #     # Check assessment responses
# #     responses = assessment_data.get('assessment_responses', {})
# #     print(f"\n📝 Assessment Responses: {len(responses)} questions")
    
# #     # Check pattern scores
# #     pattern_scores = assessment_data.get('pattern_scores', {})
# #     if pattern_scores:
# #         print(f"\n🎯 Pattern Scores:")
# #         for pattern_id, score in sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True):
# #             pattern_name = clinical_email_handler.pattern_names.get(int(pattern_id), f"Pattern {pattern_id}")
# #             print(f"   {pattern_name}: {score:.1f}")
# #     else:
# #         print(f"\n🎯 Pattern Scores: None detected")
    
# #     # Check trigger chain
# #     trigger_chain = assessment_data.get('trigger_chain', {})
# #     if trigger_chain:
# #         print(f"\n🔗 Trigger Chain Components:")
# #         components = ['awareness_point', 'physical_response', 'automatic_thought', 
# #                      'emotional_response', 'behavioral_response', 'immediate_consequence']
# #         for component in components:
# #             status = "✅" if trigger_chain.get(component) and trigger_chain[component] != 'Not captured' else "❌"
# #             print(f"   {status} {component}: {trigger_chain.get(component, 'Missing')}")
    
# #     print("\n" + "=" * 50)


# # def extract_assessment_insights(assessment_data):
# #     """Extract key insights from assessment data for quick review"""
# #     insights = {
# #         'completion_rate': 0,
# #         'dominant_pattern': 'None',
# #         'urgency_level': 'Not specified',
# #         'readiness_score': 'Not assessed',
# #         'chain_completeness': 0,
# #         'recommended_action': 'Standard approach'
# #     }
    
# #     try:
# #         # Extract completion rate
# #         assessment_results = assessment_data.get('assessment_results', {})
# #         insights['completion_rate'] = int(assessment_results.get('completion_rate', 0) * 100)
        
# #         # Extract dominant pattern
# #         pattern_scores = assessment_data.get('pattern_scores', {})
# #         if pattern_scores:
# #             dominant_id = max(pattern_scores.items(), key=lambda x: x[1])[0]
# #             insights['dominant_pattern'] = clinical_email_handler.pattern_names.get(int(dominant_id), f"Pattern {dominant_id}")
        
# #         # Extract urgency
# #         contact_info = assessment_data.get('contact_info', {})
# #         insights['urgency_level'] = contact_info.get('urgency', 'Not specified')
        
# #         # Extract readiness score
# #         responses = assessment_data.get('assessment_responses', {})
# #         for response_data in responses.values():
# #             response = response_data.get('response', {})
# #             if isinstance(response, dict) and 'rating' in response:
# #                 insights['readiness_score'] = f"{response['rating']}/10"
# #                 break
        
# #         # Calculate chain completeness
# #         trigger_chain = assessment_data.get('trigger_chain', {})
# #         if trigger_chain:
# #             total_components = 6
# #             completed = sum(1 for comp in ['awareness_point', 'physical_response', 'automatic_thought', 
# #                                          'emotional_response', 'behavioral_response', 'immediate_consequence']
# #                            if trigger_chain.get(comp) and trigger_chain[comp] != 'Not captured')
# #             insights['chain_completeness'] = int((completed / total_components) * 100)
        
# #         # Determine recommended action
# #         if insights['completion_rate'] >= 80 and len(pattern_scores) >= 3:
# #             insights['recommended_action'] = "Proceed with targeted intervention"
# #         elif insights['completion_rate'] >= 60:
# #             insights['recommended_action'] = "Brief discovery call + targeted approach"
# #         else:
# #             insights['recommended_action'] = "Full discovery call required"
            
# #     except Exception as e:
# #         print(f"❌ Error extracting insights: {e}")
    
# #     return insights


# # def format_clinical_summary(assessment_data):
# #     """Format a concise clinical summary for quick review"""
# #     insights = extract_assessment_insights(assessment_data)
# #     contact_info = assessment_data.get('contact_info', {})
    
# #     summary = f"""
# # 📋 CLINICAL SUMMARY - {contact_info.get('name', 'Unknown Client')}
# # {'=' * 60}

# # 👤 Client: {contact_info.get('email', 'Unknown')}
# # ⏰ Urgency: {insights['urgency_level']}
# # 📊 Completion: {insights['completion_rate']}%
# # 🎯 Dominant Pattern: {insights['dominant_pattern']}
# # 🔗 Chain Completeness: {insights['chain_completeness']}%
# # 📈 Readiness: {insights['readiness_score']}
# # 💡 Recommendation: {insights['recommended_action']}

# # {'=' * 60}
# #     """
    
# #     return summary


# # # Export main functions for use by assessment system
# # __all__ = [
# #     'send_clinical_assessment_results',
# #     'ClinicalAssessmentEmailHandler',
# #     'format_pattern_summary',
# #     'validate_assessment_data',
# #     'generate_assessment_report_id',
# #     'log_assessment_completion',
# #     'test_email_handler',
# #     'debug_assessment_data',
# #     'extract_assessment_insights',
# #     'format_clinical_summary'
# # ]


# # if __name__ == "__main__":
# #     # Run test when script is executed directly
# #     print("🧠 Clinical Assessment Email Handler")
# #     print("=" * 40)
# #     test_email_handler()











# """
# Enhanced Clinical Assessment Email Handler
# Comprehensive email handler for behavioral pattern assessments with Digital Despair Syndrome integration
# Complete implementation for utils/email_assess.py
# """
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime

# class EnhancedClinicalAssessmentEmailHandler:
#     """Enhanced email handler for comprehensive clinical assessment results"""
    
#     def __init__(self):
#         # Gmail SMTP configuration
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587
#         self.sender_email = "laetitiasheppard@gmail.com"
#         self.recipient_email = "laetitiasheppard@gmail.com"
        
#         # Pattern name mappings
#         self.pattern_names = {
#             1: "Unhappiness Culture",
#             2: "Power Struggles", 
#             3: "Systematic Mistrust",
#             4: "Separation/Division",
#             5: "Doing vs Being",
#             6: "Compartmentalized Authenticity",
#             7: "Self-Sacrifice/Care Avoidance",
#             8: "Inherited Missions",
#             9: "Context-Dependent Weakness"
#         }
        
#         # Try to get password from environment variables or Streamlit secrets
#         try:
#             import streamlit as st
#             self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
#         except:
#             self.password = os.environ.get("GMAIL_APP_PASSWORD", "")

#     def send_clinical_assessment_results(self, assessment_data):
#         """Send comprehensive clinical assessment results with full analysis"""
#         try:
#             # Extract key information safely
#             contact_info = assessment_data.get('contact_info', {})
#             assessment_results = assessment_data.get('assessment_results', {})
#             is_digital_native = assessment_data.get('is_digital_native', False)
#             digital_analysis = assessment_data.get('digital_despair_analysis')
            
#             email = contact_info.get('email', 'unknown@email.com')
#             name = contact_info.get('name', 'Assessment Participant')
#             urgency = contact_info.get('urgency', 'Not specified')
            
#             # Create enhanced email message
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = self._generate_email_subject(name, urgency, assessment_results, is_digital_native, digital_analysis)
            
#             # Build comprehensive email body
#             body = self._build_email_body(assessment_data)
            
#             msg.attach(MIMEText(body, 'plain'))
            
#             # Send email if password is available
#             if self.password:
#                 return self._send_email(msg)
#             else:
#                 # Log the assessment data for debugging
#                 print(f"Enhanced Clinical Assessment: {name} ({email})")
#                 if is_digital_native:
#                     severity = digital_analysis.get('severity_level', 'UNKNOWN') if digital_analysis else 'UNKNOWN'
#                     score = digital_analysis.get('digital_despair_score', 0) if digital_analysis else 0
#                     print(f"Digital Native: YES - {severity} ({score:.1f}%)")
#                 else:
#                     print(f"Digital Native: NO - Traditional approach")
#                 print(f"Urgency: {urgency}")
#                 print(f"Traditional patterns: {len(assessment_results.get('pattern_scores', {}))}")
#                 return True
                
#         except Exception as e:
#             print(f"Error sending enhanced clinical assessment: {str(e)}")
#             return False

#     def _send_email(self, msg):
#         """Send the email message"""
#         try:
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
#             server.starttls()
#             server.login(self.sender_email, self.password)
#             server.send_message(msg)
#             server.quit()
#             return True
#         except Exception as e:
#             print(f"Error sending email: {str(e)}")
#             return False

#     def _generate_email_subject(self, name, urgency, assessment_results, is_digital_native, digital_analysis):
#         """Generate contextual email subject"""
#         # Priority indicator
#         if 'extremely urgent' in urgency.lower():
#             priority = "🚨 EMERGENCY"
#         elif 'very urgent' in urgency.lower():
#             priority = "⚡ HIGH PRIORITY"
#         elif 'urgent' in urgency.lower():
#             priority = "📋 URGENT"
#         else:
#             priority = "🧠 CLINICAL"
        
#         # Assessment type indicator
#         if is_digital_native and digital_analysis:
#             severity = digital_analysis.get('severity_level', 'MINIMAL')
#             if severity in ['SEVERE', 'MODERATE']:
#                 assessment_type = f"DIGITAL-NATIVE {severity}"
#             else:
#                 assessment_type = "DIGITAL-AWARE"
#         else:
#             assessment_type = "TRADITIONAL"
        
#         return f"{priority} ASSESSMENT: {name} - {assessment_type}"

#     def _build_email_body(self, assessment_data):
#         """Build comprehensive email body"""
#         contact_info = assessment_data.get('contact_info', {})
#         assessment_results = assessment_data.get('assessment_results', {})
#         is_digital_native = assessment_data.get('is_digital_native', False)
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         # Header section
#         body = self._build_header_section(contact_info, assessment_results, is_digital_native, digital_analysis)
        
#         # Digital despair syndrome analysis (if applicable)
#         if is_digital_native:
#             body += self._build_digital_analysis_section(digital_analysis)
        
#         # Traditional behavioral pattern analysis
#         body += self._build_pattern_analysis_section(assessment_data)
        
#         # Clinical template
#         clinical_template = assessment_data.get('clinical_template', '')
#         if clinical_template:
#             body += f"\n{clinical_template}\n"
        
#         # Footer
#         body += self._build_footer_section()
        
#         return body

#     def _build_header_section(self, contact_info, assessment_results, is_digital_native, digital_analysis):
#         """Build email header with client information"""
#         name = contact_info.get('name', 'Not provided')
#         email = contact_info.get('email', 'Not provided')
#         phone = contact_info.get('phone', 'Not provided')
#         urgency = contact_info.get('urgency', 'Not specified')
#         concern = contact_info.get('primary_concern', 'Not specified')
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         questions_answered = assessment_results.get('total_questions_answered', 0)
#         patterns_detected = len(assessment_results.get('pattern_scores', {}))
        
#         header = f"""
# 🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
# {"WITH DIGITAL DESPAIR SYNDROME ANALYSIS" if is_digital_native else "TRADITIONAL BEHAVIORAL ANALYSIS"}
# ══════════════════════════════════════════════════════════════════

# 📋 CLIENT INFORMATION:
# Name: {name}
# Email: {email}
# Phone: {phone}
# Primary Concern: {concern}
# Urgency Level: {urgency}
# Assessment Completed: {timestamp}

# 📊 ASSESSMENT METRICS:
# Assessment Type: {"Digital-Native Enhanced" if is_digital_native else "Traditional Behavioral"}
# Questions Answered: {questions_answered}
# Traditional Patterns Detected: {patterns_detected}
# """
        
#         # Add digital metrics if applicable
#         if is_digital_native and digital_analysis:
#             digital_score = digital_analysis.get('digital_despair_score', 0)
#             severity = digital_analysis.get('severity_level', 'UNKNOWN')
            
#             header += f"""
# Digital Despair Score: {digital_score:.1f}% ({severity} severity)
# Clinical Adaptation Required: {"YES - Specialized approach" if severity in ['SEVERE', 'MODERATE'] else "MINIMAL - Standard with modifications"}
# """
        
#         header += "\n══════════════════════════════════════════════════════════════════\n"
        
#         return header

#     def _build_digital_analysis_section(self, digital_analysis):
#         """Build Digital Despair Syndrome analysis section"""
#         if not digital_analysis:
#             return """
# 🖥️ DIGITAL NATIVE ASSESSMENT:
# ══════════════════════════════════════════════════════════════════
# Status: Digital native identified but syndrome analysis incomplete
# Recommendation: Brief digital assessment completion recommended

# """
        
#         section = f"""
# 🖥️ DIGITAL DESPAIR SYNDROME ANALYSIS:
# ══════════════════════════════════════════════════════════════════

# 📈 OVERALL SYNDROME ASSESSMENT:
# Digital Despair Score: {digital_analysis.get('digital_despair_score', 0):.1f}%
# Severity Classification: {digital_analysis.get('severity_level', 'UNKNOWN')}
# Clinical Recommendation: {digital_analysis.get('clinical_recommendation', 'Assessment incomplete')}

# 🔍 SYNDROME COMPONENT BREAKDOWN:
# """
        
#         components = digital_analysis.get('component_scores', {})
#         for component, score in components.items():
#             component_name = component.replace('_', ' ').title()
#             section += f"• {component_name}: {score:.1f}/5\n"
        
#         # Therapeutic adaptations
#         adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
#         if adaptations:
#             section += f"""
# 🎯 REQUIRED THERAPEUTIC ADAPTATIONS:
# """
#             for i, adaptation in enumerate(adaptations[:3], 1):
#                 section += f"{i}. {adaptation}\n"
        
#         return section + "\n"

#     def _build_pattern_analysis_section(self, assessment_data):
#         """Build traditional behavioral pattern analysis section"""
#         pattern_scores = assessment_data.get('pattern_scores', {})
        
#         if not pattern_scores:
#             return """
# 🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
# ══════════════════════════════════════════════════════════════════
# Status: Insufficient pattern data - discovery session recommended

# """
        
#         section = f"""
# 🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
# ══════════════════════════════════════════════════════════════════

# 📊 PATTERN HIERARCHY (Ranked by Activation Strength):
# """
        
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
#         for i, (pattern_id, score) in enumerate(sorted_patterns[:3], 1):
#             pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#             activation_level = self._get_pattern_activation_level(score)
            
#             section += f"""
# {i}. {pattern_name}:
#    Activation Score: {score:.1f}/10 ({activation_level})
# """
        
#         return section

#     def _build_footer_section(self):
#         """Build footer section"""
#         return f"""
# ╔══════════════════════════════════════════════════════════════╗
# ║                        SYSTEM INFORMATION                    ║
# ╚══════════════════════════════════════════════════════════════╝

# Assessment System: Enhanced Clinical Assessment Platform
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Protocol: Rapid Transformation Hypnotherapy

# ══════════════════════════════════════════════════════════════════
# """

#     def _get_pattern_activation_level(self, score):
#         """Get activation level for behavioral pattern"""
#         if score >= 7.0:
#             return "VERY HIGH"
#         elif score >= 5.0:
#             return "HIGH"
#         elif score >= 3.0:
#             return "MODERATE"
#         elif score >= 1.0:
#             return "MILD"
#         else:
#             return "MINIMAL"


# # Main function to be called from assess.py
# def send_clinical_assessment_results(assessment_data):
#     """Main function to send clinical assessment results - called from assess.py"""
#     handler = EnhancedClinicalAssessmentEmailHandler()
#     return handler.send_clinical_assessment_results(assessment_data)


# # Legacy function for backward compatibility
# def send_assessment_results(client_info, assessment_data):
#     """Legacy function wrapper for sending assessment results"""
#     if 'contact_info' not in assessment_data:
#         assessment_data['contact_info'] = client_info
    
#     handler = EnhancedClinicalAssessmentEmailHandler()
#     return handler.send_clinical_assessment_results(assessment_data)


# # Initialize global handler instance
# email_handler = EnhancedClinicalAssessmentEmailHandler()








"""
Enhanced Clinical Assessment Email Handler
Comprehensive email handler for behavioral pattern assessments with Digital Despair Syndrome integration
Complete rewrite for utils/email_assess.py with full functionality
"""
import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

class EnhancedClinicalAssessmentEmailHandler:
    """Enhanced email handler for comprehensive clinical assessment results"""
    
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
        
        # Digital despair component names
        self.digital_component_names = {
            'digital_native_status': 'Digital Native Conditioning',
            'reality_dissociation': 'Online vs Offline Authenticity Gap',
            'binary_success_pressure': 'Extraordinary Achievement Pressure',
            'ironic_detachment': 'Emotional Protection Through Cynicism',
            'algorithmic_dependency': 'Social Media Emotional Regulation',
            'nihilistic_worldview': 'Hopelessness and Meaning Crisis',
            'hope_avoidance': 'Resistance to Optimism',
            'attention_fragmentation': 'Digital Attention Conditioning',
            'future_hopelessness': 'Economic and Existential Anxiety',
            'social_anxiety_escalation': 'Offline Interaction Avoidance'
        }
        
        # Clinical significance thresholds
        self.clinical_thresholds = {
            'high': 6.0,
            'moderate': 4.0,
            'mild': 2.5,
            'minimal': 1.0
        }
        
        # Digital despair severity levels
        self.dds_severity_levels = {
            'SEVERE': {'threshold': 7.0, 'description': 'Severe Digital Despair Syndrome - Immediate intervention recommended'},
            'MODERATE': {'threshold': 5.5, 'description': 'Moderate Digital Despair Syndrome - Enhanced protocol required'},
            'MILD': {'threshold': 4.0, 'description': 'Mild DDS patterns - Digital-aware approach recommended'},
            'MINIMAL': {'threshold': 2.5, 'description': 'Minimal DDS indicators - Standard protocol with digital awareness'},
            'NONE': {'threshold': 0.0, 'description': 'No significant digital despair patterns detected'}
        }
        
        # Try to get password from environment variables or Streamlit secrets
        try:
            import streamlit as st
            self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        except:
            self.password = os.environ.get("GMAIL_APP_PASSWORD", "")

    def calculate_digital_despair_score(self, assessment_data):
        """Calculate comprehensive Digital Despair Syndrome score"""
        if 'digital_despair_assessment' not in assessment_data:
            return {'score': 0, 'severity': 'not_assessed', 'components': {}}
        
        dds_data = assessment_data['digital_despair_assessment']
        component_scores = {}
        total_score = 0
        component_count = 0
        
        # Calculate individual component scores
        for component, questions in dds_data.items():
            if isinstance(questions, dict) and questions:
                component_score = 0
                question_count = 0
                
                for q_id, response_data in questions.items():
                    if isinstance(response_data, dict):
                        # Handle different response types
                        if 'rating' in response_data:
                            # Scale responses (1-10 to 1-7 for consistency)
                            rating = response_data['rating']
                            normalized_rating = min(7, (rating * 7) / 10)
                            component_score += normalized_rating
                            question_count += 1
                        elif 'response' in response_data:
                            response = response_data['response']
                            if isinstance(response, dict) and 'rating' in response:
                                rating = response['rating']
                                normalized_rating = min(7, (rating * 7) / 10)
                                component_score += normalized_rating
                                question_count += 1
                            elif isinstance(response, (int, float)):
                                component_score += min(7, response)
                                question_count += 1
                
                if question_count > 0:
                    avg_component_score = component_score / question_count
                    component_scores[component] = {
                        'score': round(avg_component_score, 1),
                        'raw_total': component_score,
                        'question_count': question_count
                    }
                    total_score += avg_component_score
                    component_count += 1
        
        # Calculate overall DDS score
        overall_score = total_score / component_count if component_count > 0 else 0
        
        # Determine severity level
        severity = 'NONE'
        severity_description = self.dds_severity_levels['NONE']['description']
        
        for level, data in sorted(self.dds_severity_levels.items(), 
                                key=lambda x: x[1]['threshold'], reverse=True):
            if overall_score >= data['threshold']:
                severity = level
                severity_description = data['description']
                break
        
        return {
            'overall_score': round(overall_score, 1),
            'severity': severity,
            'severity_description': severity_description,
            'component_scores': component_scores,
            'component_count': component_count,
            'assessment_completeness': f"{component_count}/10 components assessed"
        }

    def calculate_pattern_scores(self, assessment_data):
        """Calculate scores for the 9 core behavioral patterns"""
        pattern_scores = {}
        
        # Process responses by pattern
        responses_data = assessment_data.get('responses', {})
        
        for response_id, response_data in responses_data.items():
            patterns = response_data.get('patterns', [])
            intensity = response_data.get('intensity', 0)
            
            # Handle response data format
            response = response_data.get('response', '')
            if isinstance(response, dict) and 'rating' in response:
                intensity = response['rating']
            
            # Add to pattern scores
            for pattern in patterns:
                if isinstance(pattern, str):
                    # Convert pattern name to number if needed
                    pattern_num = None
                    for num, name in self.pattern_names.items():
                        if pattern.lower() in name.lower() or name.lower() in pattern.lower():
                            pattern_num = num
                            break
                    
                    if pattern_num:
                        if pattern_num not in pattern_scores:
                            pattern_scores[pattern_num] = {
                                'total_score': 0,
                                'response_count': 0,
                                'responses': []
                            }
                        
                        pattern_scores[pattern_num]['total_score'] += intensity
                        pattern_scores[pattern_num]['response_count'] += 1
                        pattern_scores[pattern_num]['responses'].append({
                            'question_id': response_id,
                            'intensity': intensity,
                            'response': response
                        })
                elif isinstance(pattern, int) and pattern in self.pattern_names:
                    if pattern not in pattern_scores:
                        pattern_scores[pattern] = {
                            'total_score': 0,
                            'response_count': 0,
                            'responses': []
                        }
                    
                    pattern_scores[pattern]['total_score'] += intensity
                    pattern_scores[pattern]['response_count'] += 1
                    pattern_scores[pattern]['responses'].append({
                        'question_id': response_id,
                        'intensity': intensity,
                        'response': response
                    })
        
        # Calculate average scores and severity levels
        final_pattern_scores = {}
        for pattern_num, data in pattern_scores.items():
            if data['response_count'] > 0:
                avg_score = data['total_score'] / data['response_count']
                
                # Determine severity level
                if avg_score >= self.clinical_thresholds['high']:
                    severity = 'High'
                elif avg_score >= self.clinical_thresholds['moderate']:
                    severity = 'Moderate'
                elif avg_score >= self.clinical_thresholds['mild']:
                    severity = 'Mild'
                else:
                    severity = 'Minimal'
                
                final_pattern_scores[pattern_num] = {
                    'name': self.pattern_names[pattern_num],
                    'average_score': round(avg_score, 1),
                    'severity': severity,
                    'response_count': data['response_count'],
                    'total_score': data['total_score'],
                    'responses': data['responses']
                }
        
        return final_pattern_scores

    def generate_clinical_insights(self, pattern_scores, dds_results):
        """Generate comprehensive clinical insights based on assessment results"""
        insights = []
        
        # Primary pattern analysis
        high_patterns = [p for p in pattern_scores.values() if p['severity'] == 'High']
        moderate_patterns = [p for p in pattern_scores.values() if p['severity'] == 'Moderate']
        
        if high_patterns:
            insight = f"**Primary Clinical Patterns** (High intensity): {', '.join([p['name'] for p in high_patterns])}"
            insights.append(insight)
        
        if moderate_patterns:
            insight = f"**Secondary Patterns** (Moderate intensity): {', '.join([p['name'] for p in moderate_patterns])}"
            insights.append(insight)
        
        # Digital Despair Syndrome analysis
        if dds_results['severity'] != 'not_assessed':
            if dds_results['severity'] in ['SEVERE', 'MODERATE']:
                insights.append(f"**🚨 Digital Despair Syndrome Alert**: {dds_results['severity_description']}")
                insights.append("**Recommended Protocol**: 2-Session Neuroplasticity Method with digital-native adaptations")
            elif dds_results['severity'] == 'MILD':
                insights.append(f"**📊 Digital Patterns Detected**: {dds_results['severity_description']}")
                insights.append("**Recommended Protocol**: Standard method with digital awareness components")
        
        # Specific component insights for high-scoring DDS areas
        if dds_results['component_scores']:
            high_dds_components = [
                (comp, data) for comp, data in dds_results['component_scores'].items() 
                if data['score'] >= 6.0
            ]
            
            if high_dds_components:
                comp_names = [self.digital_component_names.get(comp, comp) for comp, _ in high_dds_components]
                insights.append(f"**High-Priority Digital Components**: {', '.join(comp_names)}")
        
        # Treatment timeline recommendations
        total_high_patterns = len(high_patterns)
        if dds_results['severity'] in ['SEVERE', 'MODERATE']:
            total_high_patterns += 2  # DDS adds complexity
        
        if total_high_patterns >= 4:
            insights.append("**Treatment Recommendation**: 2+1 Session Protocol (high complexity)")
            insights.append("**Estimated Timeline**: 3-4 weeks for complete integration")
        elif total_high_patterns >= 2:
            insights.append("**Treatment Recommendation**: Standard 2-Session Protocol")
            insights.append("**Estimated Timeline**: 2-3 weeks for transformation")
        else:
            insights.append("**Treatment Recommendation**: Focused 2-Session Protocol")
            insights.append("**Estimated Timeline**: 1-2 weeks for results")
        
        return insights

    def send_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment results with full digital analysis"""
        try:
            # Extract key information safely
            contact_info = assessment_data.get('contact_info', {})
            assessment_results = assessment_data.get('assessment_results', {})
            is_digital_native = assessment_data.get('is_digital_native', False)
            digital_analysis = assessment_data.get('digital_despair_analysis')
            
            email = contact_info.get('email', 'unknown@email.com')
            name = contact_info.get('name', 'Assessment Participant')
            urgency = contact_info.get('urgency', 'Not specified')
            
            # Create enhanced email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = self._generate_enhanced_email_subject(name, urgency, assessment_results, is_digital_native, digital_analysis)
            
            # Build comprehensive email body
            body = self._build_comprehensive_email_body(assessment_data)
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email if password is available
            if self.password:
                return self._send_email(msg)
            else:
                # Log the assessment data for debugging
                print(f"Enhanced Clinical Assessment: {name} ({email})")
                if is_digital_native:
                    severity = digital_analysis.get('severity_level', 'UNKNOWN') if digital_analysis else 'UNKNOWN'
                    score = digital_analysis.get('digital_despair_score', 0) if digital_analysis else 0
                    print(f"Digital Native: YES - {severity} ({score:.1f}%)")
                else:
                    print(f"Digital Native: NO - Traditional approach")
                print(f"Urgency: {urgency}")
                print(f"Traditional patterns: {len(assessment_results.get('pattern_scores', {}))}")
                print(f"Completion rate: {assessment_results.get('completion_rate', 0)*100:.0f}%")
                return True
                
        except Exception as e:
            print(f"Error sending enhanced clinical assessment: {str(e)}")
            import traceback
            print(f"Full traceback: {traceback.format_exc()}")
            return False

    def _send_email(self, msg):
        """Send the email message"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False

    def _generate_enhanced_email_subject(self, name, urgency, assessment_results, is_digital_native, digital_analysis):
        """Generate contextual email subject based on comprehensive assessment data"""
        # Priority indicator
        if 'extremely urgent' in urgency.lower():
            priority = "🚨 EMERGENCY"
        elif 'very urgent' in urgency.lower():
            priority = "⚡ HIGH PRIORITY"
        elif 'urgent' in urgency.lower():
            priority = "📋 URGENT"
        else:
            priority = "🧠 CLINICAL"
        
        # Assessment type indicator
        if is_digital_native and digital_analysis:
            severity = digital_analysis.get('severity_level', 'MINIMAL')
            if severity in ['SEVERE', 'MODERATE']:
                assessment_type = f"DIGITAL-NATIVE {severity}"
            else:
                assessment_type = "DIGITAL-AWARE"
        else:
            assessment_type = "TRADITIONAL"
        
        # Complexity indicator
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
        
        return f"{priority} ASSESSMENT: {name} - {assessment_type} {complexity} {completion}"

    def _build_comprehensive_email_body(self, assessment_data):
        """Build comprehensive email body with integrated digital and traditional analysis"""
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        # Header section
        body = self._build_enhanced_header_section(contact_info, assessment_results, is_digital_native, digital_analysis)
        
        # Digital despair syndrome analysis (if applicable)
        if is_digital_native:
            body += self._build_digital_despair_analysis_section(digital_analysis, assessment_data)
        
        # Traditional behavioral pattern analysis
        body += self._build_traditional_pattern_analysis_section(assessment_data)
        
        # Integrated clinical template
        body += self._build_integrated_clinical_template(assessment_data)
        
        # Complete behavioral sequence analysis
        body += self._build_behavioral_sequence_analysis_section(assessment_data)
        
        # Assessment transcript
        body += self._build_enhanced_assessment_transcript_section(assessment_data)
        
        # Action items and recommendations
        body += self._build_enhanced_action_items_section(assessment_data)
        
        # Footer
        body += self._build_enhanced_footer_section()
        
        return body

    def _build_enhanced_header_section(self, contact_info, assessment_results, is_digital_native, digital_analysis):
        """Build enhanced email header with comprehensive client information"""
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
        
        header = f"""
🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
{"WITH DIGITAL DESPAIR SYNDROME ANALYSIS" if is_digital_native else "TRADITIONAL BEHAVIORAL ANALYSIS"}
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
Assessment Type: {"Digital-Native Enhanced" if is_digital_native else "Traditional Behavioral"}
Questions Answered: {questions_answered}
Completion Rate: {completion_rate:.0f}%
Traditional Patterns Detected: {patterns_detected}
Assessment Quality: {'EXCELLENT' if completion_rate >= 90 else 'GOOD' if completion_rate >= 70 else 'PARTIAL'}
"""
        
        # Add digital metrics if applicable
        if is_digital_native and digital_analysis:
            digital_score = digital_analysis.get('digital_despair_score', 0)
            severity = digital_analysis.get('severity_level', 'UNKNOWN')
            
            header += f"""
Digital Despair Score: {digital_score:.1f}% ({severity} severity)
Clinical Adaptation Required: {"YES - Specialized approach" if severity in ['SEVERE', 'MODERATE'] else "MINIMAL - Standard with modifications"}
"""
        
        header += "\n══════════════════════════════════════════════════════════════════\n"
        
        return header

    def _build_digital_despair_analysis_section(self, digital_analysis, assessment_data):
        """Build comprehensive Digital Despair Syndrome analysis section"""
        
        if not digital_analysis:
            return f"""
🖥️ DIGITAL NATIVE ASSESSMENT:
══════════════════════════════════════════════════════════════════
Status: Digital native identified but syndrome analysis incomplete
Recommendation: Brief digital assessment completion recommended
Approach: Standard with digital awareness modifications

"""
        
        section = f"""
🖥️ DIGITAL DESPAIR SYNDROME COMPREHENSIVE ANALYSIS:
══════════════════════════════════════════════════════════════════

📈 OVERALL SYNDROME ASSESSMENT:
Digital Despair Score: {digital_analysis.get('digital_despair_score', 0):.1f}%
Severity Classification: {digital_analysis.get('severity_level', 'UNKNOWN')}
Clinical Recommendation: {digital_analysis.get('clinical_recommendation', 'Assessment incomplete')}

🔍 SYNDROME COMPONENT BREAKDOWN:
"""
        
        components = digital_analysis.get('component_scores', {})
        for component, score in components.items():
            component_name = self.digital_component_names.get(component, component.replace('_', ' ').title())
            severity_level = self._get_component_severity(score)
            clinical_significance = self._get_component_clinical_significance(component, score)
            
            section += f"""
• {component_name}:
  Score: {score:.1f}/5 ({severity_level})
  Clinical Impact: {clinical_significance}
"""
        
        # Therapeutic adaptations
        adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
        if adaptations:
            section += f"""
🎯 REQUIRED THERAPEUTIC ADAPTATIONS:
"""
            for i, adaptation in enumerate(adaptations, 1):
                section += f"{i}. {adaptation}\n"
        
        # Digital-specific intervention protocols
        section += self._build_digital_intervention_protocols(digital_analysis)
        
        return section + "\n"

    def _build_digital_intervention_protocols(self, digital_analysis):
        """Generate specific intervention protocols for digital despair patterns"""
        severity = digital_analysis.get('severity_level', 'MINIMAL')
        components = digital_analysis.get('component_scores', {})
        
        protocols = f"""
🛠️ DIGITAL-NATIVE INTERVENTION PROTOCOLS:

**SESSION STRUCTURE MODIFICATIONS:**
"""
        
        if severity == 'SEVERE':
            protocols += """• Session Length: 60-75 minutes MAX (attention span limits)
• Segment Structure: 15-20 minute focused blocks with 5-minute breaks
• Total Sessions: 3 sessions highly recommended (digital patterns reassert quickly)
"""
        elif severity == 'MODERATE':
            protocols += """• Session Length: 75-90 minutes with brief breaks
• Segment Structure: 25-30 minute focused blocks  
• Total Sessions: 2-3 sessions based on progress
"""
        else:
            protocols += """• Session Length: Standard 90 minutes
• Segment Structure: Standard with digital awareness
• Total Sessions: 2 sessions typically sufficient
"""
        
        protocols += f"""
**LANGUAGE PATTERN ADAPTATIONS:**
✅ Use: "What if you discovered..." vs "You will..."
✅ Use: "I'm curious about..." vs "You need to..."
✅ Use: "Based on what we're finding..." vs "Trust me..."
✅ Use: "You might notice..." vs "You must..."

❌ Avoid: Authoritarian commands, overwhelming positivity, dismissing online achievements
❌ Avoid: Binary choice frameworks, traditional success metrics
❌ Avoid: "Just relax" or "Don't think about it" (triggers resistance)

**SPECIFIC PROTOCOL IMPLEMENTATIONS:**
"""
        
        # Component-specific protocols
        if components.get('attention_fragmentation', 0) >= 3:
            protocols += "• ATTENTION PROTOCOL: Match digital flow state familiarity in induction\n"
        
        if components.get('ironic_detachment', 0) >= 3:
            protocols += "• IRONIC ARMOR DISSOLUTION: 'Your intelligence includes wisdom beyond the clever mind'\n"
        
        if components.get('binary_success_pressure', 0) >= 3:
            protocols += "• BINARY INTERRUPTION: 'What if success included...' rather than extraordinary vs ordinary\n"
        
        if components.get('hope_avoidance', 0) >= 3:
            protocols += "• HOPE INTRODUCTION: 'Possibilities you haven't yet considered' vs overwhelming optimism\n"
        
        if components.get('reality_dissociation', 0) >= 3:
            protocols += "• REALITY BRIDGING: Honor online competencies, transfer to offline confidence\n"
        
        if components.get('algorithmic_dependency', 0) >= 3:
            protocols += "• VALIDATION SHIFT: Install internal vs external digital validation systems\n"
        
        return protocols + "\n"

    def _build_traditional_pattern_analysis_section(self, assessment_data):
        """Build traditional behavioral pattern analysis section"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return """
🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
══════════════════════════════════════════════════════════════════
Status: Insufficient pattern data - discovery session recommended
Patterns Detected: None with sufficient confidence
Recommendation: Complete pattern mapping in Session 1

"""
        
        section = f"""
🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
══════════════════════════════════════════════════════════════════

📊 PATTERN HIERARCHY (Ranked by Activation Strength):
"""
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Pattern descriptions and clinical significance
        pattern_descriptions = {
            1: "Difficulty accepting or maintaining positive emotional states - blocks natural joy",
            2: "Recurring conflicts and power struggles in relationships - fight/flight activation", 
            3: "Default skepticism and difficulty trusting others' intentions - protective isolation",
            4: "Black-and-white thinking patterns that limit options - decision paralysis",
            5: "Self-worth tied to productivity and achievement - being vs doing imbalance",
            6: "Inconsistent sense of identity across different contexts - authenticity fragmentation",
            7: "Prioritizing others' needs while neglecting self-care - boundary dissolution",
            8: "Life choices driven by family expectations - autonomy vs loyalty conflict",
            9: "Context-dependent loss of personal boundaries - situational powerlessness"
        }
        
        pattern_interventions = {
            1: "Joy permission installation + positive emotion anchoring + happiness safety protocols",
            2: "Collaboration installation + win-win mindset + conflict de-escalation reflexes",
            3: "Healthy discernment vs mistrust + graduated vulnerability + trust capacity building",
            4: "Both/and thinking installation + creative option generation + nuanced decision making",
            5: "Inherent worth recognition + being/doing balance + rest permission protocols",
            6: "Authentic self integration + consistent expression + context-independent identity",
            7: "Self-care as strength + healthy boundaries + sustainable balance installation",
            8: "Personal path confidence + family respect integration + autonomous choice empowerment",
            9: "Universal boundary strength + context-independent power + consistent self-advocacy"
        }
        
        for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
            pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
            activation_level = self._get_pattern_activation_level(score)
            therapeutic_priority = self._get_therapeutic_priority(score)
            
            section += f"""
{i}. {pattern_name}:
   Activation Score: {score:.1f}/10 ({activation_level})
   Therapeutic Priority: {therapeutic_priority}
   Clinical Description: {pattern_descriptions.get(pattern_id, 'Requires individual assessment')}
   Intervention Approach: {pattern_interventions.get(pattern_id, 'Customized based on presentation')}
   
"""
        
        # Pattern interaction analysis
        if len(sorted_patterns) > 1:
            section += self._analyze_pattern_interactions(sorted_patterns)
        
        return section

    def _analyze_pattern_interactions(self, sorted_patterns):
        """Analyze how multiple patterns interact and reinforce each other"""
        top_patterns = [p[0] for p in sorted_patterns[:3]]
        
        interaction_analysis = """
🔗 PATTERN INTERACTION ANALYSIS:
"""
        
        # Common pattern combinations and their clinical significance
        pattern_synergies = {
            (1, 5): "Unhappiness + Achievement Pressure: 'I don't deserve joy unless I earn it through work'",
            (1, 7): "Unhappiness + Self-Sacrifice: 'Taking care of others justifies my misery'",
            (2, 3): "Power Struggles + Mistrust: 'I must fight because others can't be trusted'",
            (2, 4): "Power Struggles + Binary Thinking: 'Either I win or I lose - no middle ground'",
            (3, 6): "Mistrust + Compartmentalized Authenticity: 'I can't be real because others will hurt me'",
            (4, 5): "Binary Thinking + Achievement Pressure: 'Either extraordinary success or complete failure'",
            (5, 7): "Achievement + Self-Sacrifice: 'My worth depends on what I produce for others'",
            (6, 9): "Compartmentalized Authenticity + Context Weakness: 'I lose myself in certain situations'",
            (7, 8): "Self-Sacrifice + Inherited Missions: 'I must sacrifice myself for family expectations'"
        }
        
        # Check for known synergistic combinations
        found_synergies = []
        for combination, description in pattern_synergies.items():
            if combination[0] in top_patterns and combination[1] in top_patterns:
                found_synergies.append(description)
        
        if found_synergies:
            interaction_analysis += """
**Identified Pattern Synergies:**
"""
            for synergy in found_synergies:
                interaction_analysis += f"• {synergy}\n"
        
        # Overall complexity assessment
        complexity_level = "HIGH" if len(top_patterns) >= 4 else "MODERATE" if len(top_patterns) >= 3 else "FOCUSED"
        
        interaction_analysis += f"""
**Pattern Complexity Level:** {complexity_level}
**Clinical Implication:** {"Multi-session approach recommended with careful sequencing" if complexity_level == "HIGH" else "Standard 2-session approach suitable" if complexity_level == "MODERATE" else "Focused intervention possible"}

"""
        
        return interaction_analysis

    def _build_integrated_clinical_template(self, assessment_data):
        """Build integrated clinical template combining traditional and digital analysis"""
        
        # Use the clinical template from assessment_data if available
        clinical_template = assessment_data.get('clinical_template', '')
        
        if clinical_template:
            return f"""
{clinical_template}
"""
        
        # Generate fallback template if not provided
        return self._generate_fallback_clinical_template(assessment_data)

    def _generate_fallback_clinical_template(self, assessment_data):
        """Generate fallback clinical template when not provided by assessment"""
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        pattern_scores = assessment_data.get('pattern_scores', {})
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        template = f"""
╔══════════════════════════════════════════════════════════════╗
║                    INTEGRATED CLINICAL TEMPLATE              ║
║              Traditional + Digital Analysis                  ║
╚══════════════════════════════════════════════════════════════╝

**CLIENT PROFILE:**
Assessment Type: {"Digital-Native Enhanced" if is_digital_native else "Traditional Behavioral"}
Primary Concerns: {contact_info.get('primary_concern', 'Not specified')}
Urgency Level: {contact_info.get('urgency', 'Not specified')}

**BEHAVIORAL PATTERN ANALYSIS:**
"""
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            dominant_pattern = self.pattern_names.get(sorted_patterns[0][0], "Unknown") if sorted_patterns else "Unknown"
            dominant_score = sorted_patterns[0][1] if sorted_patterns else 0
            
            primary_pattern = self.pattern_names.get(sorted_patterns[1][0], "Unknown") if len(sorted_patterns) > 1 else "None detected"
            primary_score = sorted_patterns[1][1] if len(sorted_patterns) > 1 else 0
            
            secondary_pattern = self.pattern_names.get(sorted_patterns[2][0], "Unknown") if len(sorted_patterns) > 2 else "None detected"
            secondary_score = sorted_patterns[2][1] if len(sorted_patterns) > 2 else 0
            
            template += f"""
Dominant Pattern: {dominant_pattern} (Score: {dominant_score:.1f}/10)
Primary Pattern: {primary_pattern} (Score: {primary_score:.1f}/10)
Secondary Pattern: {secondary_pattern} (Score: {secondary_score:.1f}/10)
"""
        else:
            template += """
Dominant Pattern: Assessment incomplete - requires session completion
Primary Pattern: Insufficient data for ranking
Secondary Pattern: Additional assessment needed
"""
        
        # Add digital analysis if applicable
        if is_digital_native and digital_analysis:
            digital_score = digital_analysis.get('digital_despair_score', 0)
            severity = digital_analysis.get('severity_level', 'UNKNOWN')
            
            template += f"""

**DIGITAL DESPAIR SYNDROME OVERLAY:**
Syndrome Severity: {severity} ({digital_score:.1f}% Digital Despair Score)
Therapeutic Adaptation Required: {"ESSENTIAL" if severity in ['SEVERE', 'MODERATE'] else "RECOMMENDED"}

**INTEGRATED TREATMENT APPROACH:**
• Traditional pattern work + Digital-native adaptations
• {"Collaborative peer-consultant model" if severity in ['SEVERE', 'MODERATE'] else "Standard therapeutic relationship"}
• {"Modified session structure (60-75 min)" if severity == 'SEVERE' else "Standard 90-minute sessions"}
• {"Evidence-based hope introduction" if digital_analysis.get('component_scores', {}).get('hope_avoidance', 0) >= 3 else "Standard optimism building"}
"""
        else:
            template += f"""

**TREATMENT APPROACH:**
• Traditional behavioral pattern transformation
• Standard hypnotherapy protocols
• 90-minute session structure
• Classical therapeutic relationship model
"""
        
        # Session planning recommendations
        template += f"""

**SESSION PLANNING RECOMMENDATIONS:**
Session 1 Focus: {"Digital-aware pattern mapping + trust building" if is_digital_native else "Comprehensive pattern assessment + rapport"}
Session 2 Target: {"Adapted hypnotherapy with digital considerations" if is_digital_native else "Core pattern transformation"}
Session 3 Need: {"Higher probability due to digital pattern reassertion" if is_digital_native and digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE'] else "Standard - as needed"}

**SUCCESS PROBABILITY:**
Estimated Rate: {self._calculate_integrated_success_probability(assessment_data)}%
Key Success Factors: {"Digital adaptation compliance, intellectual engagement, gradual hope building" if is_digital_native else "Pattern recognition, change readiness, therapeutic alliance"}

╔══════════════════════════════════════════════════════════════╗
║                     CLINICAL RECOMMENDATIONS                ║
╚══════════════════════════════════════════════════════════════╝

This assessment reveals {"a digital-native psychology requiring specialized intervention adaptations alongside traditional pattern work" if is_digital_native else "traditional behavioral patterns suitable for standard hypnotherapy approaches"}.

Priority Actions:
1. {"Review digital-native protocols before contact" if is_digital_native else "Standard contact and session preparation"}
2. {"Use collaborative language patterns from first contact" if is_digital_native and digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE'] else "Standard therapeutic communication"}
3. {"Prepare for intellectual resistance and cynicism" if is_digital_native and digital_analysis and digital_analysis.get('component_scores', {}).get('ironic_detachment', 0) >= 3 else "Standard resistance management"}
"""
        
        return template

    def _build_behavioral_sequence_analysis_section(self, assessment_data):
        """Build comprehensive behavioral sequence mapping analysis"""
        trigger_chain = assessment_data.get('trigger_chain', {})
        
        section = f"""
╔══════════════════════════════════════════════════════════════╗
║            COMPLETE BEHAVIORAL SEQUENCE MAPPING             ║
╚══════════════════════════════════════════════════════════════╝

🔗 TRIGGER → PHYSICAL → THOUGHT → EMOTION → BEHAVIOR → CONSEQUENCE CHAIN:

"""
        
        sequence_components = {
            'awareness_point': '🎯 TRIGGER IDENTIFICATION',
            'physical_response': '💓 PHYSICAL RESPONSE', 
            'automatic_thought': '💭 AUTOMATIC THOUGHT',
            'emotional_response': '❤️ EMOTIONAL RESPONSE',
            'behavioral_response': '🏃 BEHAVIORAL RESPONSE',
            'immediate_consequence': '⚡ IMMEDIATE CONSEQUENCE',
            'longer_term_impact': '📈 LONGER-TERM IMPACT'
        }
        
        captured_count = 0
        total_count = len(sequence_components)
        
        for component_key, component_name in sequence_components.items():
            response = trigger_chain.get(component_key, 'Not captured')
            
            section += f"{component_name}:\n"
            
            if response and response != 'Not captured' and response != 'Skipped':
                captured_count += 1
                section += f"   ✅ CAPTURED: \"{response}\"\n"
                
                # Add clinical analysis based on component type
                if component_key == 'physical_response':
                    section += f"   Clinical Analysis: {self._analyze_somatic_response(response)}\n"
                elif component_key == 'automatic_thought':
                    section += f"   Clinical Analysis: {self._analyze_thought_pattern(response)}\n"
                elif component_key == 'behavioral_response':
                    section += f"   Clinical Analysis: {self._analyze_behavioral_pattern_clinical(response)}\n"
                elif component_key == 'immediate_consequence':
                    section += f"   Clinical Analysis: {self._analyze_consequence_pattern(response)}\n"
            else:
                section += f"   ❌ NOT CAPTURED - Session 1 priority for intervention design\n"
                section += f"   Clinical Impact: {self._get_missing_component_impact(component_key)}\n"
            
            section += "\n"
        
        # Chain completeness assessment
        completeness_percentage = int((captured_count / total_count) * 100)
        section += f"""
📊 BEHAVIORAL CHAIN COMPLETENESS ANALYSIS:
Overall Completeness: {completeness_percentage}% ({captured_count}/{total_count} components captured)

{"✅ SUFFICIENT for targeted intervention design - proceed with hypnotherapy" if completeness_percentage >= 60 else "⚠️ PARTIAL - Session 1 must prioritize chain completion" if completeness_percentage >= 40 else "❌ INSUFFICIENT - Discovery call essential for intervention design"}

🎯 SESSION 1 CHAIN COMPLETION PROTOCOL:
Missing components require exploration using these therapeutic questions:
"""
        
        # Generate session 1 questions for missing components
        missing_components = [comp for comp in sequence_components.keys() 
                            if not trigger_chain.get(comp) or trigger_chain.get(comp) in ['Not captured', 'Skipped']]
        
        component_questions = {
            'awareness_point': "What specific situations tend to set this whole pattern in motion?",
            'physical_response': "When this pattern starts, what's the first thing you notice in your body?",
            'automatic_thought': "What thought pops into your mind the moment you feel that physical sensation?",
            'emotional_response': "What emotions show up right after that thought?",
            'behavioral_response': "When you feel that emotion, what do you typically do?",
            'immediate_consequence': "Right after you do that, how do you feel?",
            'longer_term_impact': "Hours or days later, what's the lasting effect?"
        }
        
        for component in missing_components[:5]:  # Show up to 5 missing components
            question = component_questions.get(component, "Explore this component in session")
            section += f"• {component.replace('_', ' ').title()}: \"{question}\"\n"
        
        section += "\n"
        
        return section

    def _build_enhanced_assessment_transcript_section(self, assessment_data):
        """Build enhanced assessment transcript section with phase organization"""
        responses = assessment_data.get('responses', {})
        
        if not responses:
            return """
╔══════════════════════════════════════════════════════════════╗
║                    ASSESSMENT TRANSCRIPT                     ║
╚══════════════════════════════════════════════════════════════╝

Status: No detailed responses recorded
Recommendation: Complete assessment for full clinical analysis

"""
        
        section = """
╔══════════════════════════════════════════════════════════════╗
║                    ASSESSMENT TRANSCRIPT                     ║
║                  Phase-Organized Responses                   ║
╚══════════════════════════════════════════════════════════════╝

"""
        
        # Organize responses by phase
        phases = {
            'age_assessment': '🎂 AGE & DEMOGRAPHIC ASSESSMENT',
            'digital_assessment': '💻 DIGITAL NATIVE EVALUATION', 
            'engagement_assessment': '📞 ENGAGEMENT & URGENCY ASSESSMENT',
            'trigger_mapping': '🔗 BEHAVIORAL TRIGGER MAPPING',
            'pattern_assessment': '🧠 BEHAVIORAL PATTERN ANALYSIS',
            'integration_assessment': '🎯 INTEGRATION & COMPLETION'
        }
        
        # Sort responses by phase and question ID
        phase_responses = {}
        for response_id, response_data in responses.items():
            phase = response_data.get('phase', 'unknown_phase')
            if phase not in phase_responses:
                phase_responses[phase] = []
            phase_responses[phase].append((response_id, response_data))
        
        # Sort within each phase
        for phase in phase_responses:
            phase_responses[phase].sort(key=lambda x: int(x[0]) if x[0].isdigit() else float('inf'))
        
        total_responses = 0
        high_intensity_responses = 0
        
        for phase_key in phases.keys():
            if phase_key in phase_responses:
                section += f"\n{phases[phase_key]}:\n"
                section += "─" * 60 + "\n"
                
                for response_id, response_data in phase_responses[phase_key]:
                    total_responses += 1
                    
                    question_text = response_data.get('question_text', 'Unknown question')
                    response = response_data.get('response', 'No response')
                    intensity = response_data.get('intensity', 0)
                    timestamp = response_data.get('timestamp', 'Unknown time')
                    question_type = response_data.get('question_type', 'Unknown type')
                    patterns = response_data.get('patterns', [])
                    
                    if intensity >= 6:
                        high_intensity_responses += 1
                    
                    section += f"\nQ{response_id} [{question_type.upper()}]:\n"
                    section += f"Question: {question_text}\n"
                    
                    # Format response based on type
                    if isinstance(response, dict):
                        if 'rating' in response:
                            section += f"Response: Rating {response['rating']}/10"
                            if response.get('follow_up'):
                                section += f" - {response['follow_up']}"
                            section += "\n"
                        else:
                            section += f"Response: Multiple selections:\n"
                            for item, item_intensity in response.items():
                                section += f"  • {item}: {item_intensity}/7\n"
                    elif isinstance(response, list):
                        section += f"Response: {', '.join(response)}\n"
                    else:
                        section += f"Response: {response}\n"
                    
                    if intensity and intensity != response:
                        section += f"Intensity: {intensity}/7 {'(HIGH CLINICAL SIGNIFICANCE)' if intensity >= 6 else '(MODERATE)' if intensity >= 4 else ''}\n"
                    
                    if patterns:
                        pattern_names = []
                        for pattern in patterns:
                            if isinstance(pattern, int) and pattern in self.pattern_names:
                                pattern_names.append(f"{pattern}. {self.pattern_names[pattern]}")
                            elif isinstance(pattern, str):
                                pattern_names.append(pattern)
                        
                        if pattern_names:
                            section += f"Associated Patterns: {', '.join(pattern_names)}\n"
                    
                    if timestamp != 'Unknown time':
                        try:
                            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                            formatted_time = dt.strftime("%H:%M:%S")
                            section += f"Time: {formatted_time}\n"
                        except:
                            section += f"Time: {timestamp}\n"
                    
                    section += "─" * 30 + "\n"
        
        # Transcript quality metrics
        high_intensity_percentage = (high_intensity_responses / total_responses * 100) if total_responses > 0 else 0
        
        section += f"""

📊 TRANSCRIPT QUALITY METRICS:
Total Responses Recorded: {total_responses}
High-Intensity Responses (≥6): {high_intensity_responses} ({high_intensity_percentage:.0f}%)
Assessment Depth: {'COMPREHENSIVE' if total_responses >= 20 else 'SUBSTANTIAL' if total_responses >= 15 else 'BASIC' if total_responses >= 10 else 'LIMITED'}
Clinical Data Quality: {'EXCELLENT' if high_intensity_percentage >= 30 else 'GOOD' if high_intensity_percentage >= 20 else 'ADEQUATE' if high_intensity_percentage >= 10 else 'LIMITED'}

"""
        
        return section

    def _build_enhanced_action_items_section(self, assessment_data):
        """Build enhanced action items and recommendations section"""
        contact_info = assessment_data.get('contact_info', {})
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        urgency = contact_info.get('urgency', 'not specified').lower()
        
        section = """
╔══════════════════════════════════════════════════════════════╗
║                    ENHANCED ACTION ITEMS                     ║
║              Prioritized Clinical Recommendations           ║
╚══════════════════════════════════════════════════════════════╝

"""
        
        # Priority contact timeline
        if 'extremely urgent' in urgency or 'emergency' in urgency:
            contact_priority = "🚨 IMMEDIATE CONTACT (within 4-6 hours)"
        elif 'very urgent' in urgency:
            contact_priority = "⚡ PRIORITY CONTACT (within 12-24 hours)" 
        elif 'urgent' in urgency:
            contact_priority = "📋 URGENT CONTACT (within 24-48 hours)"
        elif is_digital_native and digital_analysis and digital_analysis.get('severity_level') == 'SEVERE':
            contact_priority = "⚡ DIGITAL SEVERITY CONTACT (within 12-24 hours)"
        else:
            contact_priority = "📞 STANDARD CONTACT (within 2-3 days)"
        
        section += f"**CONTACT PRIORITY:** {contact_priority}\n\n"
        
        # Digital-native preparation protocols
        if is_digital_native:
            section += "**DIGITAL-NATIVE PREPARATION PROTOCOLS:**\n"
            
            if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
                section += """✅ Review digital-native intervention protocols before contact
✅ Prepare collaborative language patterns (avoid authoritarian approaches)
✅ Plan modified session structure (shorter focused blocks)
✅ Anticipate intellectual resistance and cynicism as protective mechanisms
✅ Prepare reality-bridging techniques (online competence → offline confidence)
✅ Ready hope introduction protocols (gradual, evidence-based)

"""
            else:
                section += """✅ Review basic digital awareness protocols
✅ Prepare standard approach with digital sensitivity
✅ Plan standard session structure with brief breaks
✅ Be aware of potential online/offline authenticity gaps

"""
        
        # Traditional preparation
        else:
            section += """**TRADITIONAL APPROACH PREPARATION:**
✅ Standard hypnotherapy protocols applicable
✅ Classical therapeutic relationship approach
✅ 90-minute session structure recommended
✅ Focus on traditional pattern transformation techniques

"""
        
        # Intervention readiness assessment
        pattern_scores = assessment_data.get('pattern_scores', {})
        trigger_chain = assessment_data.get('trigger_chain', {})
        
        trigger_completeness = len([k for k, v in trigger_chain.items() if v and v not in ['Not captured', 'Skipped']]) / 7
        pattern_clarity = len(pattern_scores)
        
        section += f"""**INTERVENTION READINESS ASSESSMENT:**
Trigger Chain Completeness: {trigger_completeness*100:.0f}% {'✅ READY' if trigger_completeness >= 0.6 else '⚠️ NEEDS COMPLETION' if trigger_completeness >= 0.4 else '❌ INSUFFICIENT'}
Pattern Clarity: {pattern_clarity} patterns identified {'✅ SUFFICIENT' if pattern_clarity >= 3 else '⚠️ BASIC' if pattern_clarity >= 2 else '❌ INSUFFICIENT'}

Intervention Readiness: {'✅ PROCEED WITH HYPNOTHERAPY' if trigger_completeness >= 0.6 and pattern_clarity >= 2 else '⚠️ BRIEF DISCOVERY SESSION RECOMMENDED' if trigger_completeness >= 0.4 or pattern_clarity >= 1 else '❌ COMPREHENSIVE DISCOVERY CALL ESSENTIAL'}

"""
        
        # Success optimization strategies
        section += "**SUCCESS OPTIMIZATION STRATEGIES:**\n"
        
        estimated_success = self._calculate_integrated_success_probability(assessment_data)
        
        if estimated_success >= 85:
            section += f"""✅ HIGH SUCCESS PROBABILITY ({estimated_success}%)
• Standard protocols with confidence
• Expect rapid response to interventions
• Plan for maintenance and integration phase
"""
        elif estimated_success >= 70:
            section += f"""📊 GOOD SUCCESS PROBABILITY ({estimated_success}%)
• Enhanced preparation recommended
• Allow extra time for trust building
• Consider 2+1 session protocol for complex patterns
"""
        else:
            section += f"""⚠️ MODERATE SUCCESS PROBABILITY ({estimated_success}%)
• Comprehensive preparation essential
• Extended rapport building required
• 2+1 session protocol highly recommended
• Consider addressing barriers to change first
"""
        
        # Follow-up checklist
        section += """
**FOLLOW-UP CHECKLIST:**
□ Review complete assessment data before contact
□ Prepare session environment (digital-aware if applicable)
□ Ready specific intervention protocols based on pattern analysis
□ Plan session structure based on attention capacity
□ Prepare integration and homework assignments
□ Schedule appropriate follow-up timing based on complexity

"""
        
        return section

    def _build_enhanced_footer_section(self):
        """Build enhanced footer section"""
        return f"""
╔══════════════════════════════════════════════════════════════╗
║                        SYSTEM INFORMATION                    ║
╚══════════════════════════════════════════════════════════════╝

Assessment System: Enhanced Clinical Assessment Platform v2.1
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Protocol: Rapid Transformation Hypnotherapy with Digital Despair Syndrome Integration
Clinical Framework: 9 Behavioral Patterns + 10 Digital Components Analysis

This comprehensive assessment integrates traditional behavioral pattern analysis 
with cutting-edge Digital Despair Syndrome evaluation to provide clinically-
appropriate therapeutic approaches for both traditional and digital-native clients.

For questions about this assessment system or clinical protocols, contact:
Enhanced Clinical Assessment Support

══════════════════════════════════════════════════════════════════
"""

    # Helper methods for clinical analysis
    
    def _get_component_severity(self, score):
        """Get severity level for digital component score"""
        if score >= 4.0:
            return "SEVERE"
        elif score >= 3.0:
            return "MODERATE"
        elif score >= 2.0:
            return "MILD"
        else:
            return "MINIMAL"

    def _get_component_clinical_significance(self, component, score):
        """Get clinical significance for specific component"""
        significance_map = {
            'attention_fragmentation': {
                'high': 'Requires modified session structure with frequent breaks',
                'medium': 'May benefit from varied therapeutic techniques',
                'low': 'Standard attention approaches suitable'
            },
            'ironic_detachment': {
                'high': 'Essential to work with rather than against intellectual defenses',
                'medium': 'Some resistance to traditional optimistic approaches expected',
                'low': 'Standard hope-building techniques appropriate'
            },
            'binary_success_pressure': {
                'high': 'Critical to reframe success definitions before goal setting',
                'medium': 'Address achievement pressure during intervention',
                'low': 'Standard goal-setting approaches suitable'
            }
        }
        
        level = 'high' if score >= 3.5 else 'medium' if score >= 2.5 else 'low'
        return significance_map.get(component, {}).get(level, 'Requires individual clinical assessment')

    def _get_pattern_activation_level(self, score):
        """Get activation level for behavioral pattern"""
        if score >= 7.0:
            return "VERY HIGH"
        elif score >= 5.0:
            return "HIGH"
        elif score >= 3.0:
            return "MODERATE"
        elif score >= 1.0:
            return "MILD"
        else:
            return "MINIMAL"

    def _get_therapeutic_priority(self, score):
        """Get therapeutic priority for pattern"""
        if score >= 6.0:
            return "PRIMARY TARGET"
        elif score >= 4.0:
            return "SECONDARY TARGET"
        elif score >= 2.0:
            return "MONITOR & ADDRESS"
        else:
            return "BACKGROUND AWARENESS"

    def _calculate_integrated_success_probability(self, assessment_data):
        """Calculate integrated success probability considering all factors"""
        base_probability = 85  # Base success rate
        
        # Adjust for digital factors
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        if is_digital_native and digital_analysis:
            severity = digital_analysis.get('severity_level', 'MINIMAL')
            if severity == 'SEVERE':
                base_probability -= 15
            elif severity == 'MODERATE':
                base_probability -= 10
            elif severity == 'MILD':
                base_probability -= 5
        
        # Adjust for pattern complexity
        pattern_scores = assessment_data.get('pattern_scores', {})
        high_patterns = len([p for p in pattern_scores.values() if p >= 6.0])
        
        if high_patterns >= 4:
            base_probability -= 10
        elif high_patterns >= 2:
            base_probability -= 5
        
        # Adjust for assessment completeness
        assessment_results = assessment_data.get('assessment_results', {})
        completion_rate = assessment_results.get('completion_rate', 0)
        
        if completion_rate < 0.7:
            base_probability -= 10
        elif completion_rate < 0.8:
            base_probability -= 5
        
        # Adjust for trigger chain completeness
        trigger_chain = assessment_data.get('trigger_chain', {})
        trigger_completeness = len([k for k, v in trigger_chain.items() if v and v not in ['Not captured', 'Skipped']]) / 7
        
        if trigger_completeness < 0.6:
            base_probability -= 10
        elif trigger_completeness < 0.8:
            base_probability -= 5
        
        return max(50, min(95, base_probability))  # Keep between 50-95%

    def _analyze_somatic_response(self, response):
        """Analyze somatic response for clinical insights"""
        response_lower = response.lower()
        
        if any(word in response_lower for word in ['chest', 'tight', 'pressure', 'heart']):
            return "Cardiovascular activation - indicates high stress response, suitable for breathing techniques"
        elif any(word in response_lower for word in ['stomach', 'gut', 'nausea', 'sick']):
            return "Digestive system activation - suggests anxiety pattern, benefits from grounding techniques"
        elif any(word in response_lower for word in ['muscle', 'tense', 'jaw', 'shoulder']):
            return "Muscular tension pattern - indicates fight/flight, responds well to progressive relaxation"
        else:
            return "Individual somatic pattern - requires personalized approach"

    def _analyze_thought_pattern(self, response):
        """Analyze automatic thought pattern for clinical insights"""
        response_lower = response.lower()
        
        if any(phrase in response_lower for phrase in ['should', 'must', 'have to', 'supposed to']):
            return "Perfectionist/obligation thinking - address 'shoulds' and install permission for imperfection"
        elif any(phrase in response_lower for phrase in ['always', 'never', 'everyone', 'nobody']):
            return "All-or-nothing thinking - teach nuanced perspective and exception finding"
        elif any(phrase in response_lower for phrase in ['what if', 'going to happen', 'worry']):
            return "Catastrophic thinking - future-focused anxiety requiring present-moment anchoring"
        else:
            return "Individual thought pattern - requires specific cognitive restructuring"

    def _analyze_behavioral_pattern_clinical(self, response):
        """Analyze behavioral response pattern for clinical insights"""
        response_lower = response.lower()
        
        if any(word in response_lower for word in ['avoid', 'hide', 'withdraw', 'isolate']):
            return "Avoidance pattern - gradual exposure with safety building required"
        elif any(word in response_lower for word in ['fight', 'argue', 'angry', 'attack']):
            return "Fight response - conflict de-escalation and collaboration skills needed"
        elif any(word in response_lower for word in ['please', 'agree', 'go along', 'accommodate']):
            return "People-pleasing pattern - boundary setting and authentic expression work"
        else:
            return "Individual behavioral pattern - requires customized intervention approach"

    def _analyze_consequence_pattern(self, response):
        """Analyze consequence pattern for clinical insights"""
        response_lower = response.lower()
        
        if any(word in response_lower for word in ['guilty', 'shame', 'bad', 'wrong']):
            return "Self-blame pattern - self-compassion and worth-building interventions needed"
        elif any(word in response_lower for word in ['angry', 'frustrated', 'mad', 'annoyed']):
            return "Anger consequence - emotional regulation and expression skills required"
        elif any(word in response_lower for word in ['tired', 'exhausted', 'drained', 'empty']):
            return "Energy depletion - sustainable coping strategies and energy management needed"
        else:
            return "Individual consequence pattern - monitor for intervention effectiveness"

    def _get_missing_component_impact(self, component_key):
        """Get clinical impact of missing behavioral sequence component"""
        impact_map = {
            'awareness_point': 'Cannot identify intervention entry points - limits prevention strategies',
            'physical_response': 'Missing early warning system - reduces intervention timing effectiveness',
            'automatic_thought': 'Cannot address cognitive component - limits cognitive restructuring',
            'emotional_response': 'Missing emotional processing needs - reduces emotional regulation work',
            'behavioral_response': 'Cannot target specific behaviors - limits behavioral modification',
            'immediate_consequence': 'Missing reinforcement understanding - reduces pattern interruption effectiveness',
            'longer_term_impact': 'Cannot assess full pattern cost - reduces motivation for change'
        }
        
        return impact_map.get(component_key, 'Reduces comprehensive intervention design')


# Convenience functions for backward compatibility
def send_clinical_assessment_results(client_info, assessment_data):
    """Legacy function wrapper for sending assessment results"""
    # Convert old format to new format if necessary
    if 'contact_info' not in assessment_data:
        assessment_data['contact_info'] = client_info
    
    handler = EnhancedClinicalAssessmentEmailHandler()
    return handler.send_assessment_results(assessment_data)


# Initialize global handler instance
email_handler = EnhancedClinicalAssessmentEmailHandler()


# Testing and debugging functions
def validate_enhanced_assessment_data(assessment_data):
    """Validate assessment data structure for enhanced email handler"""
    required_fields = ['contact_info', 'assessment_results']
    missing_fields = []
    
    for field in required_fields:
        if field not in assessment_data:
            missing_fields.append(field)
    
    is_valid = len(missing_fields) == 0
    
    return is_valid, missing_fields


def debug_enhanced_assessment_data(assessment_data):
    """Debug assessment data for enhanced email handler"""
    print("=== ENHANCED ASSESSMENT DATA DEBUG ===")
    
    # Basic structure
    print(f"Keys present: {list(assessment_data.keys())}")
    
    # Contact info
    contact_info = assessment_data.get('contact_info', {})
    print(f"Contact info keys: {list(contact_info.keys())}")
    print(f"Name: {contact_info.get('name', 'Not provided')}")
    print(f"Email: {contact_info.get('email', 'Not provided')}")
    print(f"Urgency: {contact_info.get('urgency', 'Not provided')}")
    
    # Digital native status
    is_digital_native = assessment_data.get('is_digital_native', False)
    print(f"Digital native: {is_digital_native}")
    
    # Digital analysis
    digital_analysis = assessment_data.get('digital_despair_analysis')
    if digital_analysis:
        print(f"Digital severity: {digital_analysis.get('severity_level', 'Unknown')}")
        print(f"Digital score: {digital_analysis.get('digital_despair_score', 0):.1f}%")
        print(f"Digital components: {len(digital_analysis.get('component_scores', {}))}")
    else:
        print("Digital analysis: Not present")
    
    # Traditional patterns
    pattern_scores = assessment_data.get('pattern_scores', {})
    print(f"Traditional patterns detected: {len(pattern_scores)}")
    
    # Assessment results
    assessment_results = assessment_data.get('assessment_results', {})
    print(f"Total questions: {assessment_results.get('total_questions_answered', 0)}")
    print(f"Completion rate: {assessment_results.get('completion_rate', 0)*100:.0f}%")
    
    # Trigger chain
    trigger_chain = assessment_data.get('trigger_chain', {})
    captured_components = len([k for k, v in trigger_chain.items() if v and v not in ['Not captured', 'Skipped']])
    print(f"Trigger chain components captured: {captured_components}/7")
    
    print("=== DEBUG COMPLETE ===")


def test_enhanced_email_handler():
    """Test enhanced email handler with digital native assessment"""
    print("Testing enhanced email handler with digital native assessment...")
    
    # Create test data for digital native with severe syndrome
    test_data = {
        'contact_info': {
            'name': 'Alex Chen',
            'email': 'alex.chen.test@gmail.com',
            'phone': '+66-98-765-4321',
            'urgency': 'Very urgent - struggling with motivation and future direction',
            'primary_concern': 'Lost sense of purpose, everything feels pointless, can\'t get motivated',
            'next_step': 'I want to try hypnotherapy - heard it might help'
        },
        'assessment_results': {
            'total_questions_answered': 45,
            'completion_rate': 0.89,
            'pattern_scores': {
                1: 7.2,  # Unhappiness Culture
                4: 6.8,  # Separation/Division
                5: 8.1   # Doing vs Being
            }
        },
        'is_digital_native': True,
        'digital_despair_analysis': {
            'digital_despair_score': 73.5,
            'severity_level': 'SEVERE',
            'clinical_recommendation': 'Immediate specialized intervention with digital-native protocols',
            'component_scores': {
                'nihilistic_worldview': 4.2,
                'binary_success_pressure': 4.8,
                'hope_avoidance': 4.5,
                'ironic_detachment': 3.9,
                'attention_fragmentation': 3.7,
                'algorithmic_dependency': 4.1
            },
            'therapeutic_adaptations_needed': [
                'Modified session structure (60-75 minutes)',
                'Collaborative peer-consultant approach',
                'Evidence-based hope introduction protocols',
                'Reality bridging techniques'
            ]
        },
        'pattern_scores': {
            1: 7.2,
            4: 6.8,
            5: 8.1
        },
        'trigger_chain': {
            'awareness_point': 'Seeing success stories on social media',
            'physical_response': 'Heavy feeling in chest, like being crushed',
            'automatic_thought': 'I\'ll never achieve anything meaningful',
            'emotional_response': 'Deep despair and hopelessness',
            'behavioral_response': 'Scroll more social media or play games to numb out',
            'immediate_consequence': 'Feel worse about wasting time',
            'longer_term_impact': 'Reinforces belief that I\'m a failure'
        },
        'responses': {
            '1': {
                'question_text': 'How old are you?',
                'response': '23',
                'phase': 'age_assessment',
                'question_type': 'demographic',
                'timestamp': '2024-01-15T10:30:00Z'
            },
            '15': {
                'question_text': 'How often do you feel like nothing really matters?',
                'response': {'rating': 8, 'follow_up': 'Most days, especially when I see what others are accomplishing'},
                'intensity': 8,
                'phase': 'digital_assessment',
                'question_type': 'scale_with_followup',
                'patterns': [1, 4],
                'timestamp': '2024-01-15T10:45:00Z'
            }
        }
    }
    
    # Test the email handler
    handler = EnhancedClinicalAssessmentEmailHandler()
    success = handler.send_clinical_assessment_results(test_data)
    
    if success:
        print("✅ Digital native test passed - comprehensive email generated")
    else:
        print("❌ Digital native test failed")
    
    return success


def test_traditional_assessment():
    """Test enhanced email handler with traditional assessment"""
    print("Testing enhanced email handler with traditional assessment...")
    
    # Create test data for traditional client
    test_data = {
        'contact_info': {
            'name': 'Sarah Johnson',
            'email': 'sarah.johnson.test@gmail.com',
            'phone': '+66-87-654-3210',
            'urgency': 'Moderate - want to address anxiety patterns',
            'primary_concern': 'Anxiety in social situations and perfectionism',
            'next_step': 'Book a session to work on confidence'
        },
        'assessment_results': {
            'total_questions_answered': 32,
            'completion_rate': 0.94,
            'pattern_scores': {
                2: 6.5,  # Power Struggles
                3: 5.8,  # Systematic Mistrust
                7: 7.1   # Self-Sacrifice
            }
        },
        'is_digital_native': False,
        'pattern_scores': {
            2: 6.5,
            3: 5.8,
            7: 7.1
        },
        'trigger_chain': {
            'awareness_point': 'Social gatherings or work meetings',
            'physical_response': 'Tight shoulders and shallow breathing',
            'automatic_thought': 'They\'re judging me',
            'emotional_response': 'Anxiety and self-consciousness',
            'behavioral_response': 'Stay quiet or leave early',
            'immediate_consequence': 'Relief but also regret',
            'longer_term_impact': 'Avoid similar situations more'
        },
        'responses': {
            '1': {
                'question_text': 'How old are you?',
                'response': '45',
                'phase': 'age_assessment',
                'question_type': 'demographic',
                'timestamp': '2024-01-15T14:30:00Z'
            },
            '12': {
                'question_text': 'How often do you put others\' needs before your own?',
                'response': {'rating': 9, 'follow_up': 'Almost always - I feel guilty when I say no'},
                'intensity': 7,
                'phase': 'pattern_assessment',
                'question_type': 'scale_with_followup',
                'patterns': [7],
                'timestamp': '2024-01-15T14:45:00Z'
            }
        }
    }
    
    # Test the email handler
    handler = EnhancedClinicalAssessmentEmailHandler()
    success = handler.send_clinical_assessment_results(test_data)
    
    if success:
        print("✅ Traditional assessment test passed - standard email generated")
    else:
        print("❌ Traditional assessment test failed")
    
    return success


def run_comprehensive_tests():
    """Run comprehensive tests for enhanced email handler"""
    print("🧪 RUNNING COMPREHENSIVE EMAIL HANDLER TESTS")
    print("=" * 60)
    
    # Test 1: Digital native with severe DDS
    test1_result = test_enhanced_email_handler()
    
    print()
    
    # Test 2: Traditional assessment
    test2_result = test_traditional_assessment()
    
    print()
    print("=" * 60)
    
    if test1_result and test2_result:
        print("✅ ALL TESTS PASSED - Enhanced email handler fully functional")
        return True
    else:
        print("❌ SOME TESTS FAILED - Review implementation")
        return False


# Export main functions
__all__ = [
    'EnhancedClinicalAssessmentEmailHandler',
    'send_clinical_assessment_results',
    'email_handler',
    'validate_enhanced_assessment_data',
    'debug_enhanced_assessment_data',
    'test_enhanced_email_handler',
    'test_traditional_assessment',
    'run_comprehensive_tests'
]
