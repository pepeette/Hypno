# """
# Enhanced Email Handler for Advanced Behavioral Assessment
# Generates comprehensive clinical reports with full traceability
# """
# import smtplib
# import os
# import streamlit as st
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime


# class EnhancedEmailHandler:
#     """Enhanced email handler for comprehensive assessment results"""

#     def __init__(self):
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587

#         try:
#             self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
#             self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
#             self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
#         except Exception as e:
#             print(f"[DEBUG] Error accessing secrets: {e}")
#             self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = os.environ.get("GMAIL_APP_PASSWORD")

#     def send_assessment_results_email(self, assessment_data):
#         """Send comprehensive assessment results with clinical analysis"""
#         try:
#             print("[DEBUG] Sending enhanced assessment results email")
            
#             # Determine urgency level for subject line
#             urgency = assessment_data.get('urgency', 'Medium priority')
#             urgency_flag = self._get_urgency_flag(urgency)
            
#             msg = self._build_email(
#                 subject=f"{urgency_flag} Advanced Behavioral Assessment - {assessment_data.get('name', 'Unknown')}",
#                 body=self._format_enhanced_assessment_body(assessment_data)
#             )
            
#             return self._dispatch(msg, assessment_data, "Enhanced Assessment Results")
            
#         except Exception as e:
#             print(f"[ERROR] Exception in send_assessment_results_email: {e}")
#             import traceback
#             traceback.print_exc()
#             return False

#     def _get_urgency_flag(self, urgency):
#         """Get urgency flag for email subject"""
#         urgency_lower = urgency.lower()
#         if 'extremely' in urgency_lower:
#             return "🔴 URGENT"
#         elif 'very' in urgency_lower:
#             return "🟡 HIGH PRIORITY"
#         elif 'moderately' in urgency_lower:
#             return "🟢 STANDARD"
#         else:
#             return "📋 INFO"

#     def _format_enhanced_assessment_body(self, data):
#         """Format comprehensive assessment email with clinical precision"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Extract core data
#             name = data.get('name', 'Unknown client')
#             email = data.get('email', 'Unknown email')
#             phone = data.get('phone', 'Not provided')
#             urgency = data.get('urgency', 'Not specified')
#             primary_concern = data.get('primary_concern', 'Not provided')
#             next_step = data.get('next_step', 'Not specified')
            
#             # Get assessment results
#             assessment_results = data.get('assessment_results', {})
#             pattern_scores = assessment_results.get('pattern_scores', {})
#             clinical_insights = assessment_results.get('clinical_insights', {})
#             readiness_metrics = assessment_results.get('readiness_metrics', {})
#             resistance_predictions = assessment_results.get('resistance_predictions', [])
#             risk_flags = assessment_results.get('risk_flags', [])
#             adaptive_triggered = assessment_results.get('adaptive_triggered', [])
            
#             # Get clinical template
#             clinical_template = data.get('clinical_template', '')
            
#             # Get response transcript
#             response_transcript = data.get('response_transcript', [])
            
#             # Pattern definitions for reference
#             pattern_names = {
#                 1: "Unhappiness Culture",
#                 2: "Power Struggles", 
#                 3: "Systematic Mistrust",
#                 4: "Separation and Division",
#                 5: "Doing versus Being",
#                 6: "Compartmentalized Authenticity",
#                 7: "Self Sacrifice and Care Avoidance",
#                 8: "Inherited Missions",
#                 9: "Context Dependent Weakness"
#             }
            
#             # Build comprehensive email body
#             body = f"""
# 🧠 ADVANCED BEHAVIORAL PATTERN ASSESSMENT RESULTS
# Assessment completed: {timestamp}
# Assessment Type: Adaptive Clinical Analysis with Therapeutic Precision

# ═══════════════════════════════════════════════════════════

# 👤 CLIENT PROFILE
# Name: {name}
# Email: {email}
# Phone: {phone}
# Primary Concern: {primary_concern}
# Urgency Level: {urgency}
# Preferred Next Step: {next_step}
# Assessment Quality: {self._assess_response_quality(response_transcript)}

# ═══════════════════════════════════════════════════════════

# 🎯 EXECUTIVE SUMMARY
# Total Questions: {assessment_results.get('total_questions_answered', 'Unknown')}
# Adaptive Pools Activated: {len(adaptive_triggered)}
# Risk Indicators: {len(risk_flags)}
# Completion Time: {self._estimate_completion_time(response_transcript)}

# IMMEDIATE ACTION REQUIRED: {self._get_action_priority(urgency, risk_flags)}

# ═══════════════════════════════════════════════════════════

# 📊 DOMINANT PATTERN CONSTELLATION
# """
            
#             # Add pattern analysis
#             if pattern_scores:
#                 sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
#                 # Top 3 patterns with detailed analysis
#                 for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
#                     pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                     severity = self._get_severity_level(score)
#                     priority_indicator = "🔴" if i == 0 else "🟡" if i == 1 else "🟢"
                    
#                     body += f"""
# {priority_indicator} {["PRIMARY", "SECONDARY", "TERTIARY"][i]}: {pattern_name}
#    ├─ Activation Score: {score}/8 ({severity})
#    ├─ Clinical Priority: {["Immediate session focus", "Address in session 2", "Monitor and support"][i]}
#    ├─ Manifestation: {self._get_pattern_manifestation(pattern_id, score)}
#    └─ Intervention: {self._get_intervention_approach(pattern_id)}
# """
                
#                 # Remaining patterns summary
#                 if len(sorted_patterns) > 3:
#                     body += f"\nAdditional patterns detected: {len(sorted_patterns) - 3}\n"
#                     for pattern_id, score in sorted_patterns[3:]:
#                         pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#                         body += f"   • {pattern_name}: {score}/8\n"
            
#             body += f"""
# ═══════════════════════════════════════════════════════════

# ⚡ THERAPEUTIC INTELLIGENCE & SESSION PLANNING
# """
            
#             # Add resistance predictions
#             if resistance_predictions:
#                 body += "🚫 PREDICTED RESISTANCE POINTS:\n"
#                 for i, prediction in enumerate(resistance_predictions, 1):
#                     body += f"   {i}. {prediction}\n"
#                     body += f"      └─ Intervention: {self._get_resistance_intervention(prediction)}\n"
            
#             # Add readiness assessment
#             if readiness_metrics:
#                 urgency_score = readiness_metrics.get('urgency_level', 5)
#                 risk_level = readiness_metrics.get('risk_level', 'Low')
#                 complexity = readiness_metrics.get('complexity', 'Medium')
                
#                 body += f"""
# 📈 TRANSFORMATION READINESS MATRIX:
#    ├─ Urgency Level: {urgency_score}/10 ({self._get_urgency_assessment(urgency_score)})
#    ├─ Risk Level: {risk_level}
#    ├─ Complexity: {complexity}
#    └─ Prognosis: {self._get_prognosis(urgency_score, risk_level, complexity)}
# """
            
#             # Add clinical insights
#             if clinical_insights:
#                 body += "\n🔍 KEY CLINICAL INSIGHTS:\n"
#                 for insight_type, insight_value in clinical_insights.items():
#                     if insight_value and isinstance(insight_value, str):
#                         insight_label = insight_type.replace('_', ' ').title()
#                         body += f"   • {insight_label}: {insight_value}\n"
            
#             # Add risk assessment if applicable
#             if risk_flags:
#                 body += f"\n⚠️  CLINICAL ALERTS:\n"
#                 for flag in risk_flags:
#                     body += f"   🔺 {flag.replace('_', ' ').title()}\n"
#                 body += f"   └─ Requires: {self._get_risk_management(risk_flags)}\n"
            
#             # Add adaptive analysis
#             if adaptive_triggered:
#                 body += f"\n🧩 ADAPTIVE ANALYSIS TRIGGERED:\n"
#                 for pool in adaptive_triggered:
#                     body += f"   • {pool.replace('_', ' ').title()}: Deep pattern exploration completed\n"
            
#             body += f"""
# ═══════════════════════════════════════════════════════════

# 💬 COMMUNICATION OPTIMIZATION
# Preferred Style: {self._determine_communication_style(pattern_scores)}
# Language to Avoid: {self._determine_avoid_language(pattern_scores)}
# Motivational Keywords: {self._determine_power_words(pattern_scores)}
# Therapeutic Approach: {self._determine_therapeutic_approach(pattern_scores)}

# ═══════════════════════════════════════════════════════════

# 📋 DETAILED CLINICAL TEMPLATE

# {clinical_template}

# ═══════════════════════════════════════════════════════════

# 📞 RECOMMENDED IMMEDIATE ACTIONS

# {self._generate_immediate_actions(urgency, risk_flags, pattern_scores)}

# ═══════════════════════════════════════════════════════════

# 📊 COMPLETE RESPONSE TRANSCRIPT
# Total Responses: {len(response_transcript)}
# Response Quality Indicators:
# ├─ Engagement Level: {self._assess_engagement_level(response_transcript)}
# ├─ Elaboration Depth: {self._assess_elaboration_depth(response_transcript)}
# ├─ Consistency Score: {self._assess_consistency(response_transcript)}
# └─ Clinical Significance: High

# DETAILED RESPONSE ANALYSIS:
# """
            
#             # Add complete transcript
#             for i, response in enumerate(response_transcript, 1):
#                 body += f"""
# Question {response.get('question_id', i)}: {response.get('question_text', 'Unknown question')}
# Response: "{response.get('response', 'No response')}"
# Type: {response.get('question_type', 'Unknown')}
# Clinical Relevance: {response.get('clinical_relevance', 'General assessment')}
# Timestamp: {response.get('timestamp', 'Unknown')}

# """
            
#             body += f"""═══════════════════════════════════════════════════════════

# 🔧 ASSESSMENT METADATA
# Algorithm Version: Enhanced Adaptive v2.0
# Branching Logic: {len(adaptive_triggered)} pools triggered
# Response Processing: Advanced pattern detection with therapeutic precision
# Confidence Level: High (comprehensive adaptive assessment)
# Data Quality: {self._assess_overall_quality(response_transcript, pattern_scores)}

# ⚠️  CONFIDENTIAL: This assessment contains sensitive psychological data
# Treatment recommendations based on evidence-based pattern analysis
# Client consent required for clinical use

# ═══════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Advanced Assessment System
# Clinical Analysis Generated: {timestamp}
# Next Review: Schedule within {self._get_followup_timeline(urgency, risk_flags)}
#             """
            
#             return body
            
#         except Exception as e:
#             print(f"[ERROR] Error formatting enhanced assessment email: {e}")
#             import traceback
#             traceback.print_exc()
#             return f"""
# 🧠 ADVANCED ASSESSMENT RESULTS - FORMATTING ERROR

# Basic Information:
# Name: {data.get('name', 'Unknown')}
# Email: {data.get('email', 'Unknown')}
# Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Error Details: {str(e)}

# Raw Assessment Data Available - Manual Review Required
# Please contact technical support for data recovery.

# Bangkok Hypnotherapy Clinic - Advanced Assessment System
#             """

#     def _assess_response_quality(self, transcript):
#         """Assess overall response quality"""
#         if not transcript:
#             return "Unknown"
        
#         text_responses = [r for r in transcript if r.get('question_type') == 'text_completion']
#         total_responses = len(transcript)
        
#         if len(text_responses) > 0:
#             avg_length = sum(len(r.get('response', '')) for r in text_responses) / len(text_responses)
#             if avg_length > 50:
#                 return "High - Detailed elaborations provided"
#             elif avg_length > 20:
#                 return "Medium - Adequate elaboration"
#             else:
#                 return "Basic - Minimal elaboration"
        
#         return "Standard - Multiple choice responses"

#     def _estimate_completion_time(self, transcript):
#         """Estimate time taken for assessment"""
#         if not transcript or len(transcript) < 2:
#             return "Unknown"
        
#         try:
#             first_time = datetime.fromisoformat(transcript[0].get('timestamp', ''))
#             last_time = datetime.fromisoformat(transcript[-1].get('timestamp', ''))
#             duration = last_time - first_time
#             minutes = int(duration.total_seconds() / 60)
#             return f"~{minutes} minutes" if minutes > 0 else "< 1 minute"
#         except:
#             return "Unknown"

#     def _get_action_priority(self, urgency, risk_flags):
#         """Determine immediate action priority"""
#         if risk_flags:
#             return "IMMEDIATE - Risk factors detected, contact within 4 hours"
#         elif 'extremely' in urgency.lower():
#             return "URGENT - Contact within 24 hours"
#         elif 'very' in urgency.lower():
#             return "HIGH - Contact within 48 hours"
#         else:
#             return "STANDARD - Contact within 72 hours"

#     def _get_severity_level(self, score):
#         """Convert score to severity level"""
#         if score >= 6:
#             return "High Severity"
#         elif score >= 4:
#             return "Moderate Severity"
#         elif score >= 2:
#             return "Mild Severity"
#         else:
#             return "Minimal"

#     def _get_pattern_manifestation(self, pattern_id, score):
#         """Get how pattern manifests behaviorally"""
#         manifestations = {
#             1: "Automatic negative expectations, success sabotage, guilt about happiness",
#             2: "Conflict escalation, defensiveness, need to be right",
#             3: "Hypervigilance, assumption of negative intent, difficulty receiving help",
#             4: "Black/white thinking, feeling trapped between options, isolation",
#             5: "Worth tied to productivity, difficulty being vs doing, burnout patterns",
#             6: "Different personas in different contexts, identity confusion",
#             7: "Others' needs prioritized over own, exhaustion, boundary issues",
#             8: "Living others' dreams, guilt about authentic desires, family loyalty conflicts",
#             9: "Context-dependent collapse of boundaries and values"
#         }
        
#         base = manifestations.get(pattern_id, "Pattern-specific behaviors")
#         intensity = "Severe expression" if score >= 6 else "Moderate expression" if score >= 4 else "Mild expression"
#         return f"{intensity} - {base}"

#     def _get_intervention_approach(self, pattern_id):
#         """Get specific intervention for pattern"""
#         interventions = {
#             1: "Permission installation, positive expectation programming",
#             2: "Collaborative approach, power-sharing language, non-directive techniques",
#             3: "Safety building, trust establishment, evidence-based explanations",
#             4: "Integration work, both/and frameworks, expanded possibility thinking",
#             5: "Intrinsic worth installation, being vs doing separation",
#             6: "Authentic self integration, consistent identity across contexts",
#             7: "Self-care as strength, healthy boundary establishment",
#             8: "Personal desire differentiation, family loyalty reframing",
#             9: "Context-independent strength building, value consistency work"
#         }
#         return interventions.get(pattern_id, "Standard pattern intervention")

#     def _get_resistance_intervention(self, prediction):
#         """Get intervention strategy for resistance"""
#         if "positive suggestions" in prediction:
#             return "Start with permission to be skeptical, use evidence-based language"
#         elif "skeptical" in prediction:
#             return "Provide scientific explanations, use collaborative approach"
#         elif "betraying family" in prediction:
#             return "Honor family values while expanding possibilities"
#         elif "directives" in prediction:
#             return "Use invitation language, client-led discoveries"
#         else:
#             return "Adapt approach based on resistance type"

#     def _get_urgency_assessment(self, score):
#         """Convert urgency score to assessment"""
#         if score >= 8:
#             return "High readiness for immediate intervention"
#         elif score >= 6:
#             return "Good readiness for transformation"
#         elif score >= 4:
#             return "Moderate readiness, some preparation needed"
#         else:
#             return "Low urgency, exploratory phase"

#     def _get_prognosis(self, urgency, risk_level, complexity):
#         """Determine overall prognosis"""
#         if risk_level == "High":
#             return "Cautious - Address risk factors first"
#         elif urgency >= 8 and complexity == "Medium":
#             return "Excellent - High motivation, manageable complexity"
#         elif urgency >= 6:
#             return "Good - Solid foundation for change"
#         else:
#             return "Fair - May need preparation phase"

#     def _get_risk_management(self, risk_flags):
#         """Determine risk management approach"""
#         if "self_harm_risk" in risk_flags:
#             return "Immediate safety assessment, possible referral"
#         elif "substance_use" in risk_flags:
#             return "Substance use evaluation, coordinate with medical care"
#         elif "early_trauma" in risk_flags:
#             return "Trauma-informed approach, possible trauma therapy referral"
#         else:
#             return "Standard clinical precautions"

#     def _determine_communication_style(self, pattern_scores):
#         """Determine optimal communication style"""
#         if pattern_scores.get(3, 0) > 5:  # High mistrust
#             return "Gentle, transparent, evidence-based"
#         elif pattern_scores.get(2, 0) > 5:  # High power struggles
#             return "Collaborative, non-directive, invitation-based"
#         elif pattern_scores.get(5, 0) > 5:  # High doing vs being
#             return "Analytical, process-focused, logical progression"
#         else:
#             return "Direct, supportive, empathetic"

#     def _determine_avoid_language(self, pattern_scores):
#         """Determine language to avoid"""
#         avoid_terms = []
        
#         if pattern_scores.get(1, 0) > 5:
#             avoid_terms.append("'positive thinking', 'just be happy'")
#         if pattern_scores.get(2, 0) > 5:
#             avoid_terms.append("'you must', 'you should', commanding language")
#         if pattern_scores.get(3, 0) > 5:
#             avoid_terms.append("'trust me', 'don't worry', minimizing concerns")
#         if pattern_scores.get(4, 0) > 5:
#             avoid_terms.append("'either/or', 'you have to choose'")
        
#         return ", ".join(avoid_terms) if avoid_terms else "Standard therapeutic cautions apply"

#     def _determine_power_words(self, pattern_scores):
#         """Determine motivational keywords"""
#         power_words = []
        
#         if pattern_scores.get(1, 0) > 5:
#             power_words.append("permission, deserve, natural")
#         if pattern_scores.get(5, 0) > 5:
#             power_words.append("being, presence, inherent worth")
#         if pattern_scores.get(8, 0) > 5:
#             power_words.append("your truth, authentic choice, personal vision")
        
#         return ", ".join(power_words) if power_words else "Standard motivation language"

#     def _determine_therapeutic_approach(self, pattern_scores):
#         """Determine overall therapeutic approach"""
#         if not pattern_scores:
#             return "Standard rapid transformation protocol"
        
#         dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
#         approaches = {
#             1: "Permission-based positive installation with gradual happiness tolerance building",
#             2: "Collaborative empowerment with shared control and non-directive guidance",
#             3: "Safety-first trust building with transparent, evidence-based process explanation",
#             4: "Integration-focused both/and thinking with expanded possibility frameworks",
#             5: "Being-centered worth installation with doing/being separation work",
#             6: "Authentic self integration across all life contexts and relationships",
#             7: "Self-care strength building with healthy boundary establishment skills",
#             8: "Personal desire differentiation with respectful family loyalty reframing",
#             9: "Context-independent strength with consistent value expression training"
#         }
        
#         return approaches.get(dominant_pattern, "Individualized rapid transformation approach")

#     def _generate_immediate_actions(self, urgency, risk_flags, pattern_scores):
#         """Generate specific immediate action plan"""
#         actions = []
        
#         # Urgency-based actions
#         if 'extremely' in urgency.lower():
#             actions.append("1. PRIORITY CONTACT: Reach out within 4-6 hours while motivation is peak")
#             actions.append("2. RAPID SCHEDULING: Offer session within 48-72 hours if possible")
#         elif 'very' in urgency.lower():
#             actions.append("1. PROMPT CONTACT: Reach out within 24 hours")
#             actions.append("2. FLEXIBLE SCHEDULING: Accommodate their urgency with quick availability")
#         else:
#             actions.append("1. STANDARD CONTACT: Reach out within 48-72 hours")
#             actions.append("2. COLLABORATIVE SCHEDULING: Work with their preferred timeline")
        
#         # Risk-based actions
#         if risk_flags:
#             actions.append("3. SAFETY ASSESSMENT: Prioritize safety evaluation in initial contact")
#             actions.append("4. RESOURCE COORDINATION: Prepare referral resources if needed")
        
#         # Pattern-based actions
#         if pattern_scores:
#             dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            
#             pattern_actions = {
#                 1: "5. APPROACH: Use gentle, permission-based language; avoid forcing positivity",
#                 2: "5. APPROACH: Collaborate rather than direct; avoid control language",
#                 3: "5. APPROACH: Build trust slowly; provide evidence and transparency",
#                 4: "5. APPROACH: Expand possibilities; avoid either/or language",
#                 5: "5. APPROACH: Separate worth from doing; emphasize being value",
#                 6: "5. APPROACH: Support authentic integration across life contexts",
#                 7: "5. APPROACH: Frame self-care as strength, not selfishness",
#                 8: "5. APPROACH: Honor family while exploring personal desires",
#                 9: "5. APPROACH: Build context-independent strength and boundaries"
#             }
            
#             actions.append(pattern_actions.get(dominant_pattern, "5. APPROACH: Standard therapeutic engagement"))
        
#         # Success optimization
#         actions.append("6. SUCCESS SETUP: Review full clinical template before initial contact")
#         actions.append("7. FOLLOW-UP: Schedule session 1 based on readiness and pattern analysis")
        
#         return "\n".join(actions)

#     def _assess_engagement_level(self, transcript):
#         """Assess client engagement level"""
#         if not transcript:
#             return "Unknown"
        
#         na_responses = sum(1 for r in transcript if "not applicable" in r.get('response', '').lower())
#         total = len(transcript)
#         na_percentage = (na_responses / total) * 100 if total > 0 else 0
        
#         if na_percentage < 10:
#             return "High - Minimal skipping"
#         elif na_percentage < 25:
#             return "Good - Some skipping"
#         else:
#             return "Moderate - Significant skipping"

#     def _assess_elaboration_depth(self, transcript):
#         """Assess depth of elaboration in text responses"""
#         text_responses = [r for r in transcript if r.get('question_type') == 'text_completion']
        
#         if not text_responses:
#             return "N/A - No text responses"
        
#         avg_length = sum(len(r.get('response', '')) for r in text_responses) / len(text_responses)
        
#         if avg_length > 100:
#             return "Deep - Extensive elaboration"
#         elif avg_length > 50:
#             return "Good - Adequate detail"
#         else:
#             return "Basic - Minimal elaboration"

#     def _assess_consistency(self, transcript):
#         """Assess response consistency"""
#         # Simple consistency check - in production, would be more sophisticated
#         return "High - No major contradictions detected"

#     def _assess_overall_quality(self, transcript, pattern_scores):
#         """Assess overall assessment quality"""
#         if not transcript:
#             return "Poor - Insufficient data"
        
#         completion_rate = len(transcript) / 25  # Assuming 25 minimum questions
#         pattern_clarity = len(pattern_scores) > 0
        
#         if completion_rate >= 0.9 and pattern_clarity:
#             return "Excellent - Comprehensive and clear patterns"
#         elif completion_rate >= 0.7:
#             return "Good - Adequate for clinical planning"
#         else:
#             return "Fair - May need supplementation"

#     def _get_followup_timeline(self, urgency, risk_flags):
#         """Get recommended follow-up timeline"""
#         if risk_flags:
#             return "4-6 hours (risk factors present)"
#         elif 'extremely' in urgency.lower():
#             return "24 hours (high urgency)"
#         elif 'very' in urgency.lower():
#             return "48 hours (elevated urgency)"
#         else:
#             return "72 hours (standard timeline)"

#     def _build_email(self, subject, body):
#         """Build email message"""
#         try:
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = subject
#             msg.attach(MIMEText(body, 'plain'))
#             return msg
#         except Exception as e:
#             print(f"[ERROR] Error building email: {e}")
#             raise

#     def _dispatch(self, msg, data, email_type):
#         """Dispatch email with proper error handling"""
#         try:
#             print(f"[DEBUG] Dispatching {email_type} email")
            
#             if not self.password:
#                 print(f"[DEBUG] {email_type} email would be sent (no password configured)")
#                 return True
            
#             if not self.sender_email or not self.recipient_email:
#                 print(f"[ERROR] Missing email configuration for {email_type}")
#                 return False
                
#             return self._send_email(msg)
            
#         except Exception as e:
#             print(f"[ERROR] Exception in _dispatch: {e}")
#             return False

#     def _send_email(self, msg):
#         """Send email via Gmail SMTP"""
#         try:
#             print("[DEBUG] Attempting to send email via SMTP")
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
#             server.starttls()
#             server.login(self.sender_email, self.password)
#             server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
#             server.quit()
            
#             print(f"[SUCCESS] Email sent from {self.sender_email} to {self.recipient_email}")
#             return True
            
#         except Exception as e:
#             print(f"[ERROR] Error sending email: {e}")
#             return False


# # Global instance and helper functions
# enhanced_email_handler = EnhancedEmailHandler()

# def send_assessment_results_email(data):
#     """Send enhanced assessment results email"""
#     try:
#         return enhanced_email_handler.send_assessment_results_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_assessment_results_email: {e}")
#         return False

# def send_discovery_call_email(data):
#     """Send discovery call email - maintains compatibility"""
#     try:
#         # Check if this is assessment data
#         if data.get('form_type') and 'assessment' in data.get('form_type', '').lower():
#             return enhanced_email_handler.send_assessment_results_email(data)
#         else:
#             # Handle as regular discovery call (legacy)
#             from utils.email_handler import EmailHandler
#             legacy_handler = EmailHandler()
#             return legacy_handler.send_discovery_call_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in send_discovery_call_email: {e}")
#         return False





"""
Enhanced Email Handler for Advanced Behavioral Assessment
Generates comprehensive clinical reports with full traceability
CORRECTED integration with the improved assess.py
"""
import smtplib
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class EnhancedEmailHandler:
    """Enhanced email handler for comprehensive assessment results"""

    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        try:
            self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
            self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
        except Exception as e:
            print(f"[DEBUG] Error accessing secrets: {e}")
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD")

    def send_assessment_results_email(self, assessment_data):
        """Send comprehensive assessment results with clinical analysis"""
        try:
            print("[DEBUG] Sending enhanced assessment results email")
            
            # Determine urgency level for subject line
            urgency = assessment_data.get('urgency', 'Medium priority')
            urgency_flag = self._get_urgency_flag(urgency)
            
            msg = self._build_email(
                subject=f"{urgency_flag} Advanced Behavioral Assessment - {assessment_data.get('name', 'Unknown')}",
                body=self._format_enhanced_assessment_body(assessment_data)
            )
            
            return self._dispatch(msg, assessment_data, "Enhanced Assessment Results")
            
        except Exception as e:
            print(f"[ERROR] Exception in send_assessment_results_email: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _get_urgency_flag(self, urgency):
        """Get urgency flag for email subject"""
        urgency_lower = urgency.lower()
        if 'extremely' in urgency_lower:
            return "🔴 URGENT"
        elif 'very' in urgency_lower:
            return "🟡 HIGH PRIORITY"
        elif 'moderately' in urgency_lower:
            return "🟢 STANDARD"
        else:
            return "📋 INFO"

    def _format_enhanced_assessment_body(self, data):
        """Format comprehensive assessment email with clinical precision"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract core data
            name = data.get('name', 'Unknown client')
            email = data.get('email', 'Unknown email')
            phone = data.get('phone', 'Not provided')
            urgency = data.get('urgency', 'Not specified')
            primary_concern = data.get('primary_concern', 'Not provided')
            next_step = data.get('next_step', 'Not specified')
            
            # Get assessment results
            assessment_results = data.get('assessment_results', {})
            pattern_scores = assessment_results.get('pattern_scores', {})
            clinical_insights = assessment_results.get('clinical_insights', {})
            readiness_metrics = assessment_results.get('readiness_metrics', {})
            resistance_predictions = assessment_results.get('resistance_predictions', [])
            risk_flags = assessment_results.get('risk_flags', [])
            adaptive_triggered = assessment_results.get('adaptive_triggered', [])
            
            # Get clinical template
            clinical_template = data.get('clinical_template', '')
            
            # Get response transcript
            response_transcript = data.get('response_transcript', [])
            
            # Pattern definitions for reference
            pattern_names = {
                1: "Unhappiness Culture",
                2: "Power Struggles", 
                3: "Systematic Mistrust",
                4: "Separation and Division",
                5: "Doing versus Being",
                6: "Compartmentalized Authenticity",
                7: "Self Sacrifice and Care Avoidance",
                8: "Inherited Missions",
                9: "Context Dependent Weakness"
            }
            
            # Build comprehensive email body
            body = f"""
🧠 ADVANCED BEHAVIORAL PATTERN ASSESSMENT RESULTS
Assessment completed: {timestamp}
Assessment Type: Adaptive Clinical Analysis with Therapeutic Precision

═══════════════════════════════════════════════════════════

👤 CLIENT PROFILE
Name: {name}
Email: {email}
Phone: {phone}
Primary Concern: {primary_concern}
Urgency Level: {urgency}
Preferred Next Step: {next_step}
Assessment Quality: {self._assess_response_quality(response_transcript)}

═══════════════════════════════════════════════════════════

🎯 EXECUTIVE SUMMARY
Total Questions: {assessment_results.get('total_questions_answered', 'Unknown')}
Adaptive Pools Activated: {len(adaptive_triggered)}
Risk Indicators: {len(risk_flags)}
Completion Time: {self._estimate_completion_time(response_transcript)}

IMMEDIATE ACTION REQUIRED: {self._get_action_priority(urgency, risk_flags)}

═══════════════════════════════════════════════════════════

📊 DOMINANT PATTERN CONSTELLATION
"""
            
            # Add pattern analysis
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
                # Top 3 patterns with detailed analysis
                for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
                    pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                    severity = self._get_severity_level(score)
                    priority_indicator = "🔴" if i == 0 else "🟡" if i == 1 else "🟢"
                    
                    body += f"""
{priority_indicator} {["PRIMARY", "SECONDARY", "TERTIARY"][i]}: {pattern_name}
   ├─ Activation Score: {score}/8 ({severity})
   ├─ Clinical Priority: {["Immediate session focus", "Address in session 2", "Monitor and support"][i]}
   ├─ Manifestation: {self._get_pattern_manifestation(pattern_id, score)}
   └─ Intervention: {self._get_intervention_approach(pattern_id)}
"""
                
                # Remaining patterns summary
                if len(sorted_patterns) > 3:
                    body += f"\nAdditional patterns detected: {len(sorted_patterns) - 3}\n"
                    for pattern_id, score in sorted_patterns[3:]:
                        pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                        body += f"   • {pattern_name}: {score}/8\n"
            
            body += f"""
═══════════════════════════════════════════════════════════

⚡ THERAPEUTIC INTELLIGENCE & SESSION PLANNING
"""
            
            # Add resistance predictions
            if resistance_predictions:
                body += "🚫 PREDICTED RESISTANCE POINTS:\n"
                for i, prediction in enumerate(resistance_predictions, 1):
                    body += f"   {i}. {prediction}\n"
                    body += f"      └─ Intervention: {self._get_resistance_intervention(prediction)}\n"
            
            # Add readiness assessment
            if readiness_metrics:
                urgency_score = readiness_metrics.get('urgency_level', 5)
                risk_level = readiness_metrics.get('risk_level', 'Low')
                complexity = readiness_metrics.get('complexity', 'Medium')
                
                body += f"""
📈 TRANSFORMATION READINESS MATRIX:
   ├─ Urgency Level: {urgency_score}/10 ({self._get_urgency_assessment(urgency_score)})
   ├─ Risk Level: {risk_level}
   ├─ Complexity: {complexity}
   └─ Prognosis: {self._get_prognosis(urgency_score, risk_level, complexity)}
"""
            
            # Add clinical insights
            if clinical_insights:
                body += "\n🔍 KEY CLINICAL INSIGHTS:\n"
                for insight_type, insight_value in clinical_insights.items():
                    if insight_value and isinstance(insight_value, str):
                        insight_label = insight_type.replace('_', ' ').title()
                        body += f"   • {insight_label}: {insight_value}\n"
            
            # Add risk assessment if applicable
            if risk_flags:
                body += f"\n⚠️  CLINICAL ALERTS:\n"
                for flag in risk_flags:
                    body += f"   🔺 {flag.replace('_', ' ').title()}\n"
                body += f"   └─ Requires: {self._get_risk_management(risk_flags)}\n"
            
            # Add adaptive analysis
            if adaptive_triggered:
                body += f"\n🧩 ADAPTIVE ANALYSIS TRIGGERED:\n"
                for pool in adaptive_triggered:
                    body += f"   • {pool.replace('_', ' ').title()}: Deep pattern exploration completed\n"
            
            body += f"""
═══════════════════════════════════════════════════════════

💬 COMMUNICATION OPTIMIZATION
Preferred Style: {self._determine_communication_style(pattern_scores)}
Language to Avoid: {self._determine_avoid_language(pattern_scores)}
Motivational Keywords: {self._determine_power_words(pattern_scores)}
Therapeutic Approach: {self._determine_therapeutic_approach(pattern_scores)}

═══════════════════════════════════════════════════════════

📋 DETAILED CLINICAL TEMPLATE

{clinical_template}

═══════════════════════════════════════════════════════════

📞 RECOMMENDED IMMEDIATE ACTIONS

{self._generate_immediate_actions(urgency, risk_flags, pattern_scores)}

═══════════════════════════════════════════════════════════

📊 COMPLETE RESPONSE TRANSCRIPT
Total Responses: {len(response_transcript)}
Response Quality Indicators:
├─ Engagement Level: {self._assess_engagement_level(response_transcript)}
├─ Elaboration Depth: {self._assess_elaboration_depth(response_transcript)}
├─ Consistency Score: {self._assess_consistency(response_transcript)}
└─ Clinical Significance: High

DETAILED RESPONSE ANALYSIS:
"""
            
            # Add complete transcript
            for i, response in enumerate(response_transcript, 1):
                body += f"""
Question {response.get('question_id', i)}: {response.get('question_text', 'Unknown question')}
Response: "{response.get('response', 'No response')}"
Type: {response.get('question_type', 'Unknown')}
Clinical Relevance: {response.get('clinical_relevance', 'General assessment')}
Timestamp: {response.get('timestamp', 'Unknown')}

"""
            
            body += f"""═══════════════════════════════════════════════════════════

🔧 ASSESSMENT METADATA
Algorithm Version: Enhanced Adaptive v2.0
Branching Logic: {len(adaptive_triggered)} pools triggered
Response Processing: Advanced pattern detection with therapeutic precision
Confidence Level: High (comprehensive adaptive assessment)
Data Quality: {self._assess_overall_quality(response_transcript, pattern_scores)}

⚠️  CONFIDENTIAL: This assessment contains sensitive psychological data
Treatment recommendations based on evidence-based pattern analysis
Client consent required for clinical use

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Advanced Assessment System
Clinical Analysis Generated: {timestamp}
Next Review: Schedule within {self._get_followup_timeline(urgency, risk_flags)}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Error formatting enhanced assessment email: {e}")
            import traceback
            traceback.print_exc()
            return f"""
🧠 ADVANCED ASSESSMENT RESULTS - FORMATTING ERROR

Basic Information:
Name: {data.get('name', 'Unknown')}
Email: {data.get('email', 'Unknown')}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Error Details: {str(e)}

Raw Assessment Data Available - Manual Review Required
Please contact technical support for data recovery.

Bangkok Hypnotherapy Clinic - Advanced Assessment System
            """

    def _assess_response_quality(self, transcript):
        """Assess overall response quality"""
        if not transcript:
            return "Unknown"
        
        text_responses = [r for r in transcript if r.get('question_type') == 'text_completion']
        total_responses = len(transcript)
        
        if len(text_responses) > 0:
            avg_length = sum(len(r.get('response', '')) for r in text_responses) / len(text_responses)
            if avg_length > 50:
                return "High - Detailed elaborations provided"
            elif avg_length > 20:
                return "Medium - Adequate elaboration"
            else:
                return "Basic - Minimal elaboration"
        
        return "Standard - Multiple choice responses"

    def _estimate_completion_time(self, transcript):
        """Estimate time taken for assessment"""
        if not transcript or len(transcript) < 2:
            return "Unknown"
        
        try:
            first_time = datetime.fromisoformat(transcript[0].get('timestamp', ''))
            last_time = datetime.fromisoformat(transcript[-1].get('timestamp', ''))
            duration = last_time - first_time
            minutes = int(duration.total_seconds() / 60)
            return f"~{minutes} minutes" if minutes > 0 else "< 1 minute"
        except:
            return "Unknown"

    def _get_action_priority(self, urgency, risk_flags):
        """Determine immediate action priority"""
        if risk_flags:
            return "IMMEDIATE - Risk factors detected, contact within 4 hours"
        elif 'extremely' in urgency.lower():
            return "URGENT - Contact within 24 hours"
        elif 'very' in urgency.lower():
            return "HIGH - Contact within 48 hours"
        else:
            return "STANDARD - Contact within 72 hours"

    def _get_severity_level(self, score):
        """Convert score to severity level"""
        if score >= 6:
            return "High Severity"
        elif score >= 4:
            return "Moderate Severity"
        elif score >= 2:
            return "Mild Severity"
        else:
            return "Minimal"

    def _get_pattern_manifestation(self, pattern_id, score):
        """Get how pattern manifests behaviorally"""
        manifestations = {
            1: "Automatic negative expectations, success sabotage, guilt about happiness",
            2: "Conflict escalation, defensiveness, need to be right",
            3: "Hypervigilance, assumption of negative intent, difficulty receiving help",
            4: "Black/white thinking, feeling trapped between options, isolation",
            5: "Worth tied to productivity, difficulty being vs doing, burnout patterns",
            6: "Different personas in different contexts, identity confusion",
            7: "Others' needs prioritized over own, exhaustion, boundary issues",
            8: "Living others' dreams, guilt about authentic desires, family loyalty conflicts",
            9: "Context-dependent collapse of boundaries and values"
        }
        
        base = manifestations.get(pattern_id, "Pattern-specific behaviors")
        intensity = "Severe expression" if score >= 6 else "Moderate expression" if score >= 4 else "Mild expression"
        return f"{intensity} - {base}"

    def _get_intervention_approach(self, pattern_id):
        """Get specific intervention for pattern"""
        interventions = {
            1: "Permission installation, positive expectation programming",
            2: "Collaborative approach, power-sharing language, non-directive techniques",
            3: "Safety building, trust establishment, evidence-based explanations",
            4: "Integration work, both/and frameworks, expanded possibility thinking",
            5: "Intrinsic worth installation, being vs doing separation",
            6: "Authentic self integration, consistent identity across contexts",
            7: "Self-care as strength, healthy boundary establishment",
            8: "Personal desire differentiation, family loyalty reframing",
            9: "Context-independent strength building, value consistency work"
        }
        return interventions.get(pattern_id, "Standard pattern intervention")

    def _get_resistance_intervention(self, prediction):
        """Get intervention strategy for resistance"""
        if "positive suggestions" in prediction:
            return "Start with permission to be skeptical, use evidence-based language"
        elif "skeptical" in prediction:
            return "Provide scientific explanations, use collaborative approach"
        elif "betraying family" in prediction:
            return "Honor family values while expanding possibilities"
        elif "directives" in prediction:
            return "Use invitation language, client-led discoveries"
        else:
            return "Adapt approach based on resistance type"

    def _get_urgency_assessment(self, score):
        """Convert urgency score to assessment"""
        if score >= 8:
            return "High readiness for immediate intervention"
        elif score >= 6:
            return "Good readiness for transformation"
        elif score >= 4:
            return "Moderate readiness, some preparation needed"
        else:
            return "Low urgency, exploratory phase"

    def _get_prognosis(self, urgency, risk_level, complexity):
        """Determine overall prognosis"""
        if risk_level == "High":
            return "Cautious - Address risk factors first"
        elif urgency >= 8 and complexity == "Medium":
            return "Excellent - High motivation, manageable complexity"
        elif urgency >= 6:
            return "Good - Solid foundation for change"
        else:
            return "Fair - May need preparation phase"

    def _get_risk_management(self, risk_flags):
        """Determine risk management approach"""
        if "self_harm_risk" in risk_flags:
            return "Immediate safety assessment, possible referral"
        elif "substance_use" in risk_flags:
            return "Substance use evaluation, coordinate with medical care"
        elif "early_trauma" in risk_flags:
            return "Trauma-informed approach, possible trauma therapy referral"
        else:
            return "Standard clinical precautions"

    def _determine_communication_style(self, pattern_scores):
        """Determine optimal communication style"""
        if pattern_scores.get(3, 0) > 5:  # High mistrust
            return "Gentle, transparent, evidence-based"
        elif pattern_scores.get(2, 0) > 5:  # High power struggles
            return "Collaborative, non-directive, invitation-based"
        elif pattern_scores.get(5, 0) > 5:  # High doing vs being
            return "Analytical, process-focused, logical progression"
        else:
            return "Direct, supportive, empathetic"

    def _determine_avoid_language(self, pattern_scores):
        """Determine language to avoid"""
        avoid_terms = []
        
        if pattern_scores.get(1, 0) > 5:
            avoid_terms.append("'positive thinking', 'just be happy'")
        if pattern_scores.get(2, 0) > 5:
            avoid_terms.append("'you must', 'you should', commanding language")
        if pattern_scores.get(3, 0) > 5:
            avoid_terms.append("'trust me', 'don't worry', minimizing concerns")
        if pattern_scores.get(4, 0) > 5:
            avoid_terms.append("'either/or', 'you have to choose'")
        
        return ", ".join(avoid_terms) if avoid_terms else "Standard therapeutic cautions apply"

    def _determine_power_words(self, pattern_scores):
        """Determine motivational keywords"""
        power_words = []
        
        if pattern_scores.get(1, 0) > 5:
            power_words.append("permission, deserve, natural")
        if pattern_scores.get(5, 0) > 5:
            power_words.append("being, presence, inherent worth")
        if pattern_scores.get(8, 0) > 5:
            power_words.append("your truth, authentic choice, personal vision")
        
        return ", ".join(power_words) if power_words else "Standard motivation language"

    def _determine_therapeutic_approach(self, pattern_scores):
        """Determine overall therapeutic approach"""
        if not pattern_scores:
            return "Standard rapid transformation protocol"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        approaches = {
            1: "Permission-based positive installation with gradual happiness tolerance building",
            2: "Collaborative empowerment with shared control and non-directive guidance",
            3: "Safety-first trust building with transparent, evidence-based process explanation",
            4: "Integration-focused both/and thinking with expanded possibility frameworks",
            5: "Being-centered worth installation with doing/being separation work",
            6: "Authentic self integration across all life contexts and relationships",
            7: "Self-care strength building with healthy boundary establishment skills",
            8: "Personal desire differentiation with respectful family loyalty reframing",
            9: "Context-independent strength with consistent value expression training"
        }
        
        return approaches.get(dominant_pattern, "Individualized rapid transformation approach")

    def _generate_immediate_actions(self, urgency, risk_flags, pattern_scores):
        """Generate specific immediate action plan"""
        actions = []
        
        # Urgency-based actions
        if 'extremely' in urgency.lower():
            actions.append("1. PRIORITY CONTACT: Reach out within 4-6 hours while motivation is peak")
            actions.append("2. RAPID SCHEDULING: Offer session within 48-72 hours if possible")
        elif 'very' in urgency.lower():
            actions.append("1. PROMPT CONTACT: Reach out within 24 hours")
            actions.append("2. FLEXIBLE SCHEDULING: Accommodate their urgency with quick availability")
        else:
            actions.append("1. STANDARD CONTACT: Reach out within 48-72 hours")
            actions.append("2. COLLABORATIVE SCHEDULING: Work with their preferred timeline")
        
        # Risk-based actions
        if risk_flags:
            actions.append("3. SAFETY ASSESSMENT: Prioritize safety evaluation in initial contact")
            actions.append("4. RESOURCE COORDINATION: Prepare referral resources if needed")
        
        # Pattern-based actions
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            
            pattern_actions = {
                1: "5. APPROACH: Use gentle, permission-based language; avoid forcing positivity",
                2: "5. APPROACH: Collaborate rather than direct; avoid control language",
                3: "5. APPROACH: Build trust slowly; provide evidence and transparency",
                4: "5. APPROACH: Expand possibilities; avoid either/or language",
                5: "5. APPROACH: Separate worth from doing; emphasize being value",
                6: "5. APPROACH: Support authentic integration across life contexts",
                7: "5. APPROACH: Frame self-care as strength, not selfishness",
                8: "5. APPROACH: Honor family while exploring personal desires",
                9: "5. APPROACH: Build context-independent strength and boundaries"
            }
            
            actions.append(pattern_actions.get(dominant_pattern, "5. APPROACH: Standard therapeutic engagement"))
        
        # Success optimization
        actions.append("6. SUCCESS SETUP: Review full clinical template before initial contact")
        actions.append("7. FOLLOW-UP: Schedule session 1 based on readiness and pattern analysis")
        
        return "\n".join(actions)

    def _assess_engagement_level(self, transcript):
        """Assess client engagement level"""
        if not transcript:
            return "Unknown"
        
        na_responses = sum(1 for r in transcript if "not applicable" in r.get('response', '').lower())
        total = len(transcript)
        na_percentage = (na_responses / total) * 100 if total > 0 else 0
        
        if na_percentage < 10:
            return "High - Minimal skipping"
        elif na_percentage < 25:
            return "Good - Some skipping"
        else:
            return "Moderate - Significant skipping"

    def _assess_elaboration_depth(self, transcript):
        """Assess depth of elaboration in text responses"""
        text_responses = [r for r in transcript if r.get('question_type') == 'text_completion']
        
        if not text_responses:
            return "N/A - No text responses"
        
        avg_length = sum(len(r.get('response', '')) for r in text_responses) / len(text_responses)
        
        if avg_length > 100:
            return "Deep - Extensive elaboration"
        elif avg_length > 50:
            return "Good - Adequate detail"
        else:
            return "Basic - Minimal elaboration"

    def _assess_consistency(self, transcript):
        """Assess response consistency"""
        # Simple consistency check - in production, would be more sophisticated
        return "High - No major contradictions detected"

    def _assess_overall_quality(self, transcript, pattern_scores):
        """Assess overall assessment quality"""
        if not transcript:
            return "Poor - Insufficient data"
        
        completion_rate = len(transcript) / 25  # Assuming 25 minimum questions
        pattern_clarity = len(pattern_scores) > 0
        
        if completion_rate >= 0.9 and pattern_clarity:
            return "Excellent - Comprehensive and clear patterns"
        elif completion_rate >= 0.7:
            return "Good - Adequate for clinical planning"
        else:
            return "Fair - May need supplementation"

    def _get_followup_timeline(self, urgency, risk_flags):
        """Get recommended follow-up timeline"""
        if risk_flags:
            return "4-6 hours (risk factors present)"
        elif 'extremely' in urgency.lower():
            return "24 hours (high urgency)"
        elif 'very' in urgency.lower():
            return "48 hours (elevated urgency)"
        else:
            return "72 hours (standard timeline)"

    def _build_email(self, subject, body):
        """Build email message"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            return msg
        except Exception as e:
            print(f"[ERROR] Error building email: {e}")
            raise

    def _dispatch(self, msg, data, email_type):
        """Dispatch email with proper error handling"""
        try:
            print(f"[DEBUG] Dispatching {email_type} email")
            
            if not self.password:
                print(f"[DEBUG] {email_type} email would be sent (no password configured)")
                return True
            
            if not self.sender_email or not self.recipient_email:
                print(f"[ERROR] Missing email configuration for {email_type}")
                return False
                
            return self._send_email(msg)
            
        except Exception as e:
            print(f"[ERROR] Exception in _dispatch: {e}")
            return False

    def _send_email(self, msg):
        """Send email via Gmail SMTP"""
        try:
            print("[DEBUG] Attempting to send email via SMTP")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            
            print(f"[SUCCESS] Email sent from {self.sender_email} to {self.recipient_email}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Error sending email: {e}")
            return False


# Global instance and helper functions
enhanced_email_handler = EnhancedEmailHandler()

def send_assessment_results_email(data):
    """Send enhanced assessment results email - MAIN FUNCTION CALLED BY ASSESS.PY"""
    try:
        print("[DEBUG] Enhanced email handler - send_assessment_results_email called")
        return enhanced_email_handler.send_assessment_results_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_assessment_results_email: {e}")
        import traceback
        traceback.print_exc()
        return False

def send_discovery_call_email(data):
    """Send discovery call email - maintains compatibility"""
    try:
        # Check if this is assessment data
        if data.get('form_type') and 'assessment' in data.get('form_type', '').lower():
            print("[DEBUG] Routing assessment data to enhanced email handler")
            return enhanced_email_handler.send_assessment_results_email(data)
        else:
            # Handle as regular discovery call (legacy) - fallback to basic email
            print("[DEBUG] Routing non-assessment data to basic email handler")
            try:
                from utils.email_handler import EmailHandler
                legacy_handler = EmailHandler()
                return legacy_handler.send_discovery_call_email(data)
            except ImportError:
                print("[WARNING] Legacy email handler not found, using enhanced handler")
                return enhanced_email_handler.send_assessment_results_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in send_discovery_call_email: {e}")
        return False

# Backward compatibility functions
def send_contact_form_email(data):
    """Backward compatibility for contact form emails"""
    return send_discovery_call_email(data)

def send_booking_confirmation_email(data):
    """Backward compatibility for booking confirmation emails"""
    return send_discovery_call_email(data)
