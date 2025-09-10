# """
# Enhanced Email Handler for Advanced Behavioral Assessment
# Generates comprehensive clinical reports with full traceability
# CORRECTED integration with the improved assess.py
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
#     """Send enhanced assessment results email - MAIN FUNCTION CALLED BY ASSESS.PY"""
#     try:
#         print("[DEBUG] Enhanced email handler - send_assessment_results_email called")
#         return enhanced_email_handler.send_assessment_results_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_assessment_results_email: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# def send_discovery_call_email(data):
#     """Send discovery call email - maintains compatibility"""
#     try:
#         # Check if this is assessment data
#         if data.get('form_type') and 'assessment' in data.get('form_type', '').lower():
#             print("[DEBUG] Routing assessment data to enhanced email handler")
#             return enhanced_email_handler.send_assessment_results_email(data)
#         else:
#             # Handle as regular discovery call (legacy) - fallback to basic email
#             print("[DEBUG] Routing non-assessment data to basic email handler")
#             try:
#                 from utils.email_handler import EmailHandler
#                 legacy_handler = EmailHandler()
#                 return legacy_handler.send_discovery_call_email(data)
#             except ImportError:
#                 print("[WARNING] Legacy email handler not found, using enhanced handler")
#                 return enhanced_email_handler.send_assessment_results_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in send_discovery_call_email: {e}")
#         return False

# # Backward compatibility functions
# def send_contact_form_email(data):
#     """Backward compatibility for contact form emails"""
#     return send_discovery_call_email(data)

# def send_booking_confirmation_email(data):
#     """Backward compatibility for booking confirmation emails"""
#     return send_discovery_call_email(data)









"""
Enhanced Clinical Email Handler for Hypnotherapy Assessment
Comprehensive therapeutic analysis with actionable treatment recommendations
"""
import smtplib
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class ClinicalEmailHandler:
    """Enhanced email handler for comprehensive clinical assessment results"""

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

    def send_clinical_assessment_results(self, clinical_data):
        """Send comprehensive clinical assessment with therapeutic analysis"""
        try:
            print("[DEBUG] Sending clinical assessment results email")
            
            # Determine clinical priority for subject line
            urgency = clinical_data.get('urgency', 'Medium priority')
            safety_flags = clinical_data.get('assessment_results', {}).get('clinical_flags', [])
            priority_flag = self._get_clinical_priority_flag(urgency, safety_flags)
            
            msg = self._build_email(
                subject=f"{priority_flag} Clinical Behavioral Assessment - {clinical_data.get('name', 'Unknown Client')}",
                body=self._format_clinical_assessment_body(clinical_data)
            )
            
            return self._dispatch(msg, clinical_data, "Clinical Assessment Results")
            
        except Exception as e:
            print(f"[ERROR] Exception in send_clinical_assessment_results: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _get_clinical_priority_flag(self, urgency, safety_flags):
        """Get clinical priority flag for email subject"""
        if 'suicide_risk' in safety_flags:
            return "🔴 CRISIS"
        elif 'high_risk_client' in safety_flags:
            return "🟠 HIGH RISK"
        elif 'extremely urgent' in urgency.lower():
            return "🔴 URGENT"
        elif 'very urgent' in urgency.lower():
            return "🟡 HIGH PRIORITY"
        elif 'moderately urgent' in urgency.lower():
            return "🟢 PRIORITY"
        else:
            return "📋 STANDARD"

    def _format_clinical_assessment_body(self, data):
        """Format comprehensive clinical email with therapeutic precision"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract core data
            name = data.get('name', 'Unknown client')
            email = data.get('email', 'Unknown email')
            phone = data.get('phone', 'Not provided')
            urgency = data.get('urgency', 'Not specified')
            availability = ', '.join(data.get('availability', [])) or 'Not specified'
            previous_therapy = data.get('previous_therapy', 'Not specified')
            additional_info = data.get('additional_info', 'None provided')
            
            # Get assessment results
            assessment_results = data.get('assessment_results', {})
            presenting_problem = assessment_results.get('presenting_problem', {})
            pattern_constellation = assessment_results.get('pattern_constellation', {})
            behavioral_chain = assessment_results.get('behavioral_chain', {})
            resistance_analysis = assessment_results.get('resistance_analysis', {})
            hypnotic_profile = assessment_results.get('hypnotic_profile', {})
            safety_assessment = assessment_results.get('safety_assessment', {})
            treatment_recommendations = assessment_results.get('treatment_recommendations', {})
            outcome_predictions = assessment_results.get('outcome_predictions', {})
            
            # Get clinical flags
            clinical_flags = assessment_results.get('clinical_flags', [])
            
            # Get script guidance
            script_guide = data.get('hypnotherapy_script_guide', {})
            
            # Build comprehensive clinical email
            body = f"""
🧠 CLINICAL BEHAVIORAL ASSESSMENT - THERAPEUTIC ANALYSIS
Assessment Completed: {timestamp}
Assessment Type: Comprehensive Clinical Analysis for Hypnotherapy Intervention

═══════════════════════════════════════════════════════════

👤 CLIENT PROFILE & INTAKE
Name: {name}
Email: {email}
Phone: {phone}
Urgency Level: {urgency}
Preferred Availability: {availability}
Previous Therapy: {previous_therapy}
Additional Context: {additional_info}

Clinical Priority: {presenting_problem.get('clinical_priority', 'Standard')}
Assessment Completion: {data.get('completion_rate', '100%')}
Total Questions Answered: {data.get('total_questions', 'Unknown')}

═══════════════════════════════════════════════════════════

🎯 PRESENTING PROBLEM ANALYSIS

TARGET BEHAVIOR FOR ELIMINATION:
Primary Complaint: {presenting_problem.get('presenting_problem', 'Not specified')}
Specific Unwanted Behavior: {presenting_problem.get('target_behavior', 'Not specified')}
Duration: {presenting_problem.get('duration', 'Not specified')}
Life Interference Level: {presenting_problem.get('impact_level', 'Not specified')}

IMMEDIATE ACTION REQUIRED: {self._get_action_timeline(urgency, clinical_flags)}

═══════════════════════════════════════════════════════════

🔗 BEHAVIORAL CHAIN MAPPING (Situation-Emotion-Reaction)

TRIGGERING SITUATION:
{behavioral_chain.get('triggering_situation', 'Not provided')}

PRE-BEHAVIOR THOUGHTS:
{behavioral_chain.get('pre_behavior_thoughts', 'Not provided')}

PHYSICAL SENSATIONS:
{behavioral_chain.get('physical_sensations', 'Not provided')}

PRIMARY EMOTION:
{behavioral_chain.get('primary_emotion', 'Not provided')}

BEHAVIORAL RESPONSE:
{behavioral_chain.get('behavioral_response', 'Not provided')}

INTERVENTION POINT: {self._identify_intervention_point(behavioral_chain)}

═══════════════════════════════════════════════════════════

📊 DOMINANT PATTERN CONSTELLATION
"""
            
            # Add pattern analysis
            dominant = pattern_constellation.get('dominant')
            secondary = pattern_constellation.get('secondary', [])
            tertiary = pattern_constellation.get('tertiary', [])
            
            if dominant:
                body += f"""
🔴 PRIMARY PATTERN: {dominant['pattern_name']}
   ├─ Activation Score: {dominant['score']}/12 ({dominant['severity']} intensity)
   ├─ Clinical Manifestation: {self._get_clinical_manifestation(dominant['pattern_id'], dominant['score'])}
   ├─ Therapeutic Approach: {self._get_therapeutic_approach(dominant['pattern_id'])}
   └─ Session 1 Priority: {treatment_recommendations.get('session_1_focus', 'Assessment and rapport building')}
"""
            
            if secondary:
                for i, pattern in enumerate(secondary[:2]):
                    indicator = "🟡" if i == 0 else "🟢"
                    level = ["SECONDARY", "TERTIARY"][i]
                    body += f"""
{indicator} {level} PATTERN: {pattern['pattern_name']}
   ├─ Activation Score: {pattern['score']}/12 ({pattern['severity']} intensity)
   ├─ Interaction Effect: {self._get_pattern_interaction(dominant['pattern_id'] if dominant else 0, pattern['pattern_id'])}
   └─ Treatment Integration: {self._get_integration_strategy(pattern['pattern_id'])}
"""
            
            # Additional patterns summary
            if tertiary:
                body += f"\nADDITIONAL PATTERNS DETECTED: {len(tertiary)}\n"
                for pattern in tertiary:
                    body += f"   • {pattern['pattern_name']}: {pattern['score']}/12\n"

            body += f"""
═══════════════════════════════════════════════════════════

⚡ HYPNOTHERAPY SCRIPT DEVELOPMENT GUIDE

INDUCTION STRATEGY:
Recommended Approach: {hypnotic_profile.get('hypnotic_approach', 'Standard approach')}
Therapeutic Style: {hypnotic_profile.get('therapeutic_style', 'Collaborative')}
Trance Capacity: {hypnotic_profile.get('trance_capacity', 'Unknown')}

SUGGESTION FRAMEWORK:
Primary Suggestions: {self._format_primary_suggestions(dominant, behavioral_chain)}
Secondary Suggestions: {self._format_secondary_suggestions(secondary)}
Language Style: {script_guide.get('suggestion_style', 'Direct positive suggestions')}

THERAPEUTIC LANGUAGE OPTIMIZATION:
✅ POWER WORDS TO USE: {', '.join(script_guide.get('therapeutic_language', {}).get('power_words', ['strength', 'natural', 'capable']))}
❌ LANGUAGE TO AVOID: {', '.join(script_guide.get('therapeutic_language', {}).get('avoid_language', ['Standard cautions apply']))}
🎯 CLIENT'S OWN LANGUAGE: {self._extract_client_language(script_guide)}

SPECIFIC HYPNOTIC COMMANDS:
• "When {behavioral_chain.get('triggering_situation', '[trigger]')} occurs, you naturally {self._get_desired_response(behavioral_chain)}"
• "The old pattern of {presenting_problem.get('target_behavior', '[behavior]')} simply dissolves"  
• "You find yourself responding with {self._get_new_response_pattern(dominant)}"

═══════════════════════════════════════════════════════════

🚫 RESISTANCE ANALYSIS & MANAGEMENT

SECONDARY GAIN IDENTIFICATION:
{resistance_analysis.get('secondary_gains', 'Not identified')}

CHANGE FEARS:
{resistance_analysis.get('change_fears', 'Not identified')}

RELATIONSHIP IMPACT CONCERNS:
{resistance_analysis.get('relationship_impact', 'Not identified')}

PREDICTED RESISTANCE POINTS:
"""
            
            # Add resistance predictions
            resistance_predictions = resistance_analysis.get('predictions', [])
            if resistance_predictions:
                for i, prediction in enumerate(resistance_predictions, 1):
                    body += f"   {i}. {prediction}\n"
                    body += f"      └─ Management Strategy: {self._get_resistance_management_strategy(prediction)}\n"
            else:
                body += "   • Low resistance predicted based on assessment responses\n"

            body += f"""
RESISTANCE MANAGEMENT PROTOCOL:
{self._generate_resistance_protocol(resistance_analysis, dominant)}

═══════════════════════════════════════════════════════════

⚠️  CLINICAL SAFETY ASSESSMENT

RISK LEVEL: {safety_assessment.get('risk_level', 'Low')}
"""
            
            # Safety considerations
            if clinical_flags:
                body += "CLINICAL FLAGS DETECTED:\n"
                for flag in clinical_flags:
                    body += f"   🔺 {flag.replace('_', ' ').title()}\n"
                    body += f"      └─ Protocol: {self._get_safety_protocol(flag)}\n"
            
            contraindications = safety_assessment.get('contraindications', [])
            if contraindications:
                body += "\nCONTRAINDICATIONS:\n"
                for contraindication in contraindications:
                    body += f"   ❌ {contraindication}\n"
            
            special_considerations = safety_assessment.get('special_considerations', [])
            if special_considerations:
                body += "\nSPECIAL CONSIDERATIONS:\n"
                for consideration in special_considerations:
                    body += f"   ⚠️  {consideration}\n"
            
            referral_needed = safety_assessment.get('referral_needed', False)
            if referral_needed:
                body += "\n🏥 REFERRAL REQUIRED: Coordinate with medical/psychiatric care before hypnotherapy\n"

            body += f"""
═══════════════════════════════════════════════════════════

📋 SESSION-BY-SESSION TREATMENT PROTOCOL

SESSION 1 - ASSESSMENT & PATTERN INTERRUPTION:
Focus: {treatment_recommendations.get('session_1_focus', 'Rapport building and initial intervention')}
Techniques: {', '.join(treatment_recommendations.get('technique_recommendations', [])[:3])}
Goals: 
├─ Establish therapeutic rapport using {hypnotic_profile.get('therapeutic_style', 'collaborative approach')}
├─ Map client's internal experience of the problem
├─ Install initial pattern interruption at: {self._identify_intervention_point(behavioral_chain)}
└─ Test hypnotic responsiveness and adjust approach

SESSION 2 - ROOT TRANSFORMATION:
Focus: {self._get_session_2_focus(dominant, resistance_analysis)}
Techniques: {self._get_session_2_techniques(dominant, clinical_flags)}
Goals:
├─ Address root cause: {self._get_root_cause_focus(dominant)}
├─ Transform core limiting belief: {self._extract_core_belief(behavioral_chain)}
├─ Install new identity: {self._get_new_identity_installation(dominant)}
└─ Strengthen new response pattern

SESSION 3 - INTEGRATION & FUTURE-PACING:
Focus: Consolidation and real-world application
Techniques: Future pacing, anchor strengthening, relapse prevention
Goals:
├─ Test integration across life contexts
├─ Strengthen new automatic responses
├─ Address any remaining resistance
└─ Establish maintenance protocol

HOMEWORK & INTEGRATION:
{self._generate_homework_protocol(dominant, hypnotic_profile)}

═══════════════════════════════════════════════════════════

📈 THERAPEUTIC OUTCOME PREDICTIONS

RAPID CHANGE PROBABILITY: {outcome_predictions.get('rapid_change_probability', 'Unknown')}
ESTIMATED TREATMENT DURATION: {outcome_predictions.get('estimated_sessions', 'Unknown')}
OVERALL PROGNOSIS: {outcome_predictions.get('prognosis', 'Fair')}

SUCCESS PREDICTORS:
"""
            
            # Success factors
            success_factors = outcome_predictions.get('success_factors', [])
            if success_factors:
                for factor in success_factors:
                    body += f"   ✅ {factor}\n"
            else:
                body += "   ✅ Assessment completed thoroughly\n"
                body += f"   ✅ {urgency} indicates motivation\n"
                if not clinical_flags:
                    body += "   ✅ No significant safety concerns\n"
            
            # Challenge factors
            challenge_factors = outcome_predictions.get('challenge_factors', [])
            if challenge_factors:
                body += "\nCHALLENGE FACTORS:\n"
                for factor in challenge_factors:
                    body += f"   ⚠️  {factor}\n"
            
            if clinical_flags:
                body += "\nCLINICAL COMPLEXITY:\n"
                for flag in clinical_flags:
                    body += f"   ⚠️  {flag.replace('_', ' ').title()} requires specialized approach\n"

            body += f"""
EXPECTED TIMELINE:
Week 1: {self._get_week_1_prediction(outcome_predictions)}
Week 2-4: {self._get_month_1_prediction(outcome_predictions)}
3 Months: {self._get_3month_prediction(outcome_predictions)}

═══════════════════════════════════════════════════════════

💬 THERAPEUTIC RELATIONSHIP OPTIMIZATION

RAPPORT BUILDING STRATEGY:
{self._get_rapport_strategy(dominant, hypnotic_profile)}

COMMUNICATION STYLE:
Preferred Approach: {hypnotic_profile.get('therapeutic_style', 'Collaborative')}
Client Guidance Preference: {hypnotic_profile.get('guidance_preference', 'Not specified')}
Therapeutic Pace: {self._determine_therapeutic_pace(urgency, clinical_flags)}

EXPECTED CLIENT BEHAVIOR IN SESSION:
Authority Response: {self._predict_authority_response(pattern_constellation)}
Emotional Regulation: {self._predict_emotional_regulation(pattern_constellation, clinical_flags)}
Change Pace Tolerance: {self._predict_change_tolerance(resistance_analysis)}
Feedback Style Needed: {self._recommend_feedback_style(pattern_constellation)}

═══════════════════════════════════════════════════════════

📞 IMMEDIATE ACTION PROTOCOL

CONTACT TIMELINE: {self._get_contact_timeline(urgency, clinical_flags)}
PRIORITY LEVEL: {presenting_problem.get('clinical_priority', 'Standard')}

RECOMMENDED IMMEDIATE ACTIONS:
{self._generate_immediate_action_plan(urgency, clinical_flags, pattern_constellation)}

PRE-SESSION PREPARATION:
1. Review complete clinical template (attached data)
2. Prepare induction style: {script_guide.get('induction_recommendations', 'Standard relaxation')}
3. Plan resistance management for: {self._get_primary_resistance_focus(resistance_analysis)}
4. Set up safety protocols if needed: {self._get_safety_prep(clinical_flags)}

═══════════════════════════════════════════════════════════

📊 COMPLETE CLINICAL DATA SUMMARY

ASSESSMENT QUALITY: {self._assess_data_quality(data)}
THERAPEUTIC CONFIDENCE: {self._assess_therapeutic_confidence(assessment_results)}
INTERVENTION READINESS: {self._assess_intervention_readiness(clinical_flags, resistance_analysis)}

KEY SUCCESS FACTORS:
1. Strong assessment completion indicating client engagement
2. Clear behavioral target identified for intervention
3. Specific triggering situation mapped for pattern interruption
4. {len(pattern_constellation.get('secondary', []))} supporting patterns identified for comprehensive treatment

CLINICAL TEMPLATE SUMMARY:
{data.get('clinical_template', 'Template generation error - see raw data below')}

═══════════════════════════════════════════════════════════

🔧 ASSESSMENT TECHNICAL METADATA
Algorithm Version: Clinical Assessment v2.0
Adaptive Logic: {len(assessment_results.get('adaptive_triggered', []))} specialized modules activated
Pattern Detection: Advanced constellation mapping with therapeutic precision
Data Quality: {self._assess_overall_data_quality(data)}
Clinical Confidence: {self._assess_clinical_confidence(assessment_results)}

⚠️  CONFIDENTIAL: Contains sensitive psychological assessment data
Clinical use only - Licensed therapist review required
Client consent obtained for therapeutic purposes

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Clinical Assessment System
Therapeutic Analysis Generated: {timestamp}
Next Clinical Review: {self._get_next_review_timeline(urgency, clinical_flags)}
Therapist Assignment: {self._recommend_therapist_type(assessment_results)}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Error formatting clinical assessment email: {e}")
            import traceback
            traceback.print_exc()
            return f"""
🧠 CLINICAL ASSESSMENT RESULTS - FORMATTING ERROR

Basic Information:
Name: {data.get('name', 'Unknown')}
Email: {data.get('email', 'Unknown')}
Phone: {data.get('phone', 'Unknown')}
Urgency: {data.get('urgency', 'Unknown')}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Error Details: {str(e)}

Raw Clinical Data Available - Manual Review Required
Complete assessment responses and analysis data preserved
Please contact technical support for data recovery and manual clinical review.

Bangkok Hypnotherapy Clinic - Clinical Assessment System
            """

    def _get_action_timeline(self, urgency, clinical_flags):
        """Get immediate action timeline based on risk and urgency"""
        if 'suicide_risk' in clinical_flags:
            return "IMMEDIATE - Crisis intervention within 4 hours"
        elif 'high_risk_client' in clinical_flags:
            return "URGENT - Contact within 12 hours for safety assessment"
        elif 'extremely urgent' in urgency.lower():
            return "HIGH PRIORITY - Contact within 24 hours"
        elif 'very urgent' in urgency.lower():
            return "PRIORITY - Contact within 48 hours"
        else:
            return "STANDARD - Contact within 72 hours"

    def _identify_intervention_point(self, behavioral_chain):
        """Identify optimal intervention point in behavioral chain"""
        if behavioral_chain.get('pre_behavior_thoughts'):
            return "Thought pattern interruption before behavioral activation"
        elif behavioral_chain.get('physical_sensations'):
            return "Somatic awareness and response modification"
        elif behavioral_chain.get('triggering_situation'):
            return "Environmental trigger response retraining"
        else:
            return "General pattern interruption and response modification"

    def _get_clinical_manifestation(self, pattern_id, score):
        """Get clinical manifestation description"""
        manifestations = {
            1: f"Automatic rejection of positive experiences, success sabotage behaviors, guilt about happiness (Score: {score}/12)",
            2: f"Conflict escalation patterns, need to control or win, defensive responses (Score: {score}/12)",
            3: f"Hypervigilance in relationships, assumption of negative intent, difficulty receiving help (Score: {score}/12)",
            4: f"Binary thinking patterns, feeling trapped between extremes, isolation tendencies (Score: {score}/12)",
            5: f"Self-worth tied to productivity, difficulty with being vs doing, burnout patterns (Score: {score}/12)",
            6: f"Context-dependent identity shifts, authenticity struggles, compartmentalization (Score: {score}/12)",
            7: f"Chronic self-neglect, others-first orientation, boundary difficulties (Score: {score}/12)",
            8: f"Living inherited dreams/expectations, guilt about personal desires, family loyalty conflicts (Score: {score}/12)",
            9: f"Context-dependent boundary collapse, inconsistent values expression (Score: {score}/12)"
        }
        return manifestations.get(pattern_id, f"Pattern-specific behavioral manifestations (Score: {score}/12)")

    def _get_therapeutic_approach(self, pattern_id):
        """Get specific therapeutic approach for pattern"""
        approaches = {
            1: "Permission installation therapy, positive expectation programming, success tolerance building",
            2: "Collaborative empowerment approach, shared control frameworks, non-directive techniques",
            3: "Safety-first trust building, transparent process explanation, evidence-based interventions",
            4: "Integration-focused therapy, both/and thinking expansion, possibility framework development",
            5: "Being-centered identity work, intrinsic worth installation, doing/being separation",
            6: "Authentic self integration, consistent identity development across contexts",
            7: "Self-care strength reframing, healthy boundary establishment, self-worth building",
            8: "Personal desire differentiation, respectful family loyalty reframing, authentic vision development",
            9: "Context-independent strength building, consistent value expression training"
        }
        return approaches.get(pattern_id, "Individualized pattern-specific intervention")

    def _get_pattern_interaction(self, primary_pattern, secondary_pattern):
        """Analyze interaction between patterns"""
        interactions = {
            (1, 3): "Unhappiness culture reinforced by mistrust - expect resistance to positive suggestions",
            (2, 3): "Power struggles amplified by mistrust - use extra collaborative approach",
            (1, 7): "Unhappiness culture with self-sacrifice - address guilt about self-care",
            (5, 7): "Doing/being confusion with self-neglect - focus on inherent worth",
            (8, 7): "Inherited missions with self-sacrifice - explore family loyalty vs. self-care"
        }
        
        key = (primary_pattern, secondary_pattern)
        return interactions.get(key, f"Monitor interaction between Pattern {primary_pattern} and Pattern {secondary_pattern}")

    def _get_integration_strategy(self, pattern_id):
        """Get integration strategy for secondary patterns"""
        strategies = {
            1: "Address alongside primary pattern - unhappiness patterns often co-occur",
            2: "Monitor for power struggles during therapy - use invitation language",
            3: "Build trust gradually - explain each intervention rationally",
            4: "Expand either/or thinking - show multiple possibilities",
            5: "Separate worth from achievement - reinforce being value",
            6: "Support authentic expression - consistency across contexts",
            7: "Reframe self-care as strength - necessary for helping others",
            8: "Honor family while expanding personal choice",
            9: "Strengthen boundaries across all contexts"
        }
        return strategies.get(pattern_id, "Standard integration approach")

    def _format_primary_suggestions(self, dominant, behavioral_chain):
        """Format primary hypnotic suggestions"""
        if not dominant:
            return "Standard positive programming based on target behavior"
        
        pattern_id = dominant['pattern_id']
        target_behavior = behavioral_chain.get('behavioral_response', 'unwanted behavior')
        
        suggestions = {
            1: f"You give yourself full permission to experience happiness and success naturally",
            2: f"You find collaboration more satisfying than control, naturally choosing cooperation",
            3: f"You trust your ability to assess situations accurately while remaining open to others",
            4: f"You see multiple possibilities in every situation, finding creative both/and solutions",
            5: f"Your worth exists independent of what you do, allowing you to simply be",
            6: f"You express your authentic self consistently across all areas of life",
            7: f"You care for yourself with the same love you show others, naturally and easily",
            8: f"You honor your family while following your own authentic path with confidence",
            9: f"You maintain your strength and boundaries in every context, naturally and consistently"
        }
        
        return suggestions.get(pattern_id, f"You naturally respond differently when {behavioral_chain.get('triggering_situation', 'the situation')} occurs")

    def _format_secondary_suggestions(self, secondary_patterns):
        """Format secondary supporting suggestions"""
        if not secondary_patterns:
            return "Supporting suggestions based on assessment responses"
        
        suggestions = []
        for pattern in secondary_patterns[:2]:
            pattern_id = pattern['pattern_id']
            secondary_suggestions = {
                1: "Positive experiences feel natural and deserved",
                2: "Collaboration brings deeper satisfaction than control",
                3: "You trust your inner wisdom while staying open to others",
                4: "Multiple possibilities exist in every situation",
                5: "Your value exists simply because you are",
                6: "Authenticity flows naturally in every context",
                7: "Self-care strengthens your ability to help others",
                8: "Personal dreams honor your family in new ways",
                9: "Your strength remains consistent everywhere"
            }
            suggestion = secondary_suggestions.get(pattern_id, f"Pattern {pattern_id} positive programming")
            suggestions.append(suggestion)
        
        return "; ".join(suggestions)

    def _extract_client_language(self, script_guide):
        """Extract client's own language for suggestions"""
        client_language = script_guide.get('therapeutic_language', {}).get('client_language', [])
        if client_language:
            return f"Use client's own words: {', '.join(client_language[:3])}"
        else:
            return "Use client's emotional vocabulary from text responses"

    def _get_desired_response(self, behavioral_chain):
        """Get desired response pattern"""
        unwanted = behavioral_chain.get('behavioral_response', '')
        if 'angry' in unwanted.lower() or 'yell' in unwanted.lower():
            return "remain calm and respond thoughtfully"
        elif 'avoid' in unwanted.lower() or 'withdraw' in unwanted.lower():
            return "stay present and engage constructively"
        elif 'worry' in unwanted.lower() or 'anxious' in unwanted.lower():
            return "feel calm and confident"
        else:
            return "respond with your natural strength and wisdom"

    def _get_new_response_pattern(self, dominant):
        """Get new response pattern based on dominant pattern"""
        if not dominant:
            return "strength and confidence"
        
        pattern_id = dominant['pattern_id']
        responses = {
            1: "natural happiness and confidence",
            2: "collaborative strength and mutual respect",
            3: "grounded trust and open communication",
            4: "creative flexibility and integrated solutions",
            5: "peaceful presence and inherent worth",
            6: "authentic consistency and genuine expression",
            7: "balanced self-care and loving boundaries",
            8: "personal authenticity while honoring family",
            9: "consistent strength and clear boundaries"
        }
        return responses.get(pattern_id, "natural strength and wisdom")

    def _get_resistance_management_strategy(self, prediction):
        """Get specific resistance management strategy"""
        if "unconsciously resist" in prediction:
            return "Address secondary gains directly - 'Part of you might miss...' exploration"
        elif "skepticism" in prediction:
            return "Provide evidence-based explanations, use client's own logic system"
        elif "directive approaches" in prediction:
            return "Use invitation language: 'You might find...' rather than 'You will...'"
        elif "positive suggestions" in prediction:
            return "Start with permission to be skeptical, validate current feelings first"
        else:
            return "Monitor closely and adapt approach based on client response"

    def _generate_resistance_protocol(self, resistance_analysis, dominant):
        """Generate comprehensive resistance management protocol"""
        if not dominant:
            return "Standard resistance management - collaborative approach with ongoing calibration"
        
        pattern_id = dominant['pattern_id']
        
        protocols = {
            1: "Unhappiness Culture Protocol: Start with permission to be unhappy, validate struggles, gradually introduce possibility of happiness",
            2: "Power Struggle Protocol: Avoid all directive language, use collaborative discovery, let client lead insights",
            3: "Mistrust Protocol: Transparent explanation of every technique, evidence-based rationale, client choice at each step",
            4: "Binary Thinking Protocol: Introduce both/and language, explore nuance, expand possibility thinking",
            5: "Achievement Pressure Protocol: Separate worth from performance, emphasize being over doing",
            6: "Authenticity Protocol: Support real self expression, consistency across contexts",
            7: "Self-Sacrifice Protocol: Reframe self-care as strength that enables helping others",
            8: "Family Loyalty Protocol: Honor family values while expanding personal choice",
            9: "Boundary Protocol: Strengthen consistent values expression across all contexts"
        }
        
        base_protocol = protocols.get(pattern_id, "Standard resistance management")
        
        # Add secondary gain considerations
        secondary_gains = resistance_analysis.get('secondary_gains', '')
        if secondary_gains and 'not' not in secondary_gains.lower():
            base_protocol += f"\nSecondary Gain Management: Address benefits client receives from current pattern - explore in session 1"
        
        return base_protocol

    def _get_safety_protocol(self, flag):
        """Get specific safety protocol for clinical flag"""
        protocols = {
            'suicide_risk': "IMMEDIATE crisis intervention, safety plan, emergency contacts, do not proceed with hypnotherapy until stabilized",
            'high_risk_client': "Specialized assessment, possible referral, modified hypnotherapy approach with safety monitoring",
            'dissociation_risk': "Grounding techniques, avoid regression, maintain present-moment awareness, shorter sessions",
            'medication_considerations': "Coordinate with prescribing physician, understand medication effects on hypnotic response",
            'substance_considerations': "Address substance use patterns, possible delay of hypnotherapy until stabilized"
        }
        return protocols.get(flag, "Standard clinical precautions apply")

    def _get_session_2_focus(self, dominant, resistance_analysis):
        """Get session 2 focus based on patterns and resistance"""
        if not dominant:
            return "Core belief transformation and new identity installation"
        
        pattern_id = dominant['pattern_id']
        
        # Check for secondary gains that need addressing
        secondary_gains = resistance_analysis.get('secondary_gains', '')
        if secondary_gains and 'not' not in secondary_gains.lower():
            return f"Address secondary gains first, then {self._get_core_transformation(pattern_id)}"
        else:
            return self._get_core_transformation(pattern_id)

    def _get_core_transformation(self, pattern_id):
        """Get core transformation focus for pattern"""
        transformations = {
            1: "Transform core belief about deserving happiness, install positive expectation as natural state",
            2: "Transform need for control into preference for collaboration, install shared power as strength",
            3: "Transform hypervigilance into grounded discernment, install basic trust with wisdom",
            4: "Transform binary thinking into integration, install both/and possibility consciousness",
            5: "Transform worth-achievement connection, install intrinsic value and being consciousness",
            6: "Transform fragmented identity into integrated authenticity across all contexts",
            7: "Transform self-sacrifice into balanced care, install self-care as strength for service",
            8: "Transform inherited dreams into personal authentic vision while honoring family",
            9: "Transform context-dependent weakness into consistent strength and boundary integrity"
        }
        return transformations.get(pattern_id, "Core limiting belief transformation and new identity installation")

    def _get_session_2_techniques(self, dominant, clinical_flags):
        """Get specific techniques for session 2"""
        if not dominant:
            return "Standard regression and reframe techniques"
        
        pattern_id = dominant['pattern_id']
        
        # Modify techniques based on safety flags
        if 'dissociation_risk' in clinical_flags:
            base_techniques = "Present-moment techniques, cognitive reframing, avoid regression"
        else:
            base_techniques = {
                1: "Age regression to install early permission for happiness, positive memory installation",
                2: "Parts therapy for control vs. collaboration, inner negotiation techniques",
                3: "Trust-building visualization, evidence installation, safety anchor strengthening",
                4: "Integration imagery, both/and visualization, possibility expansion techniques",
                5: "Identity regression, inherent worth installation, being state anchoring",
                6: "Identity integration work, authentic self visualization across contexts",
                7: "Self-care strength installation, boundary visualization, balanced care modeling",
                8: "Family honor visualization while following personal path, loyalty reframe",
                9: "Strength consistency installation, boundary integrity across all contexts"
            }.get(pattern_id, "Standard transformation techniques")
        
        return base_techniques

    def _get_root_cause_focus(self, dominant):
        """Get root cause focus for session 2"""
        if not dominant:
            return "Core limiting belief system"
        
        pattern_id = dominant['pattern_id']
        focuses = {
            1: "Early messages about happiness being dangerous or temporary",
            2: "Early powerlessness leading to need for control",
            3: "Early trust violations or betrayals",
            4: "Early forced either/or choices, black/white family dynamics",
            5: "Early conditional love based on performance/achievement",
            6: "Early need to be different people for safety or acceptance",
            7: "Early role as family caretaker or emotional support",
            8: "Early pressure to fulfill family dreams or honor sacrifices",
            9: "Early contexts where strength led to harm or rejection"
        }
        return focuses.get(pattern_id, "Core belief formation and early conditioning")

    def _extract_core_belief(self, behavioral_chain):
        """Extract core limiting belief from behavioral chain"""
        thoughts = behavioral_chain.get('pre_behavior_thoughts', '')
        if thoughts:
            # Extract potential limiting belief from thoughts
            if 'not' in thoughts.lower() and ('good' in thoughts.lower() or 'enough' in thoughts.lower()):
                return f"Core belief: '{thoughts[:50]}...'"
            else:
                return f"Explore belief behind: '{thoughts[:50]}...'"
        else:
            return "Identify core limiting belief driving the behavioral pattern"

    def _get_new_identity_installation(self, dominant):
        """Get new identity to install"""
        if not dominant:
            return "Confident, capable person who handles challenges naturally"
        
        pattern_id = dominant['pattern_id']
        identities = {
            1: "Someone who naturally deserves and enjoys happiness",
            2: "Someone who finds strength in collaboration and mutual respect",
            3: "Someone who trusts wisely while remaining open and connected",
            4: "Someone who sees multiple possibilities and finds creative solutions",
            5: "Someone whose worth exists independent of achievements",
            6: "Someone who expresses authenticity consistently across all contexts",
            7: "Someone who cares for self and others with balanced love",
            8: "Someone who honors family while living their authentic truth",
            9: "Someone who maintains strength and boundaries in every situation"
        }
        return identities.get(pattern_id, "Someone who responds to challenges with natural strength and wisdom")

    def _generate_homework_protocol(self, dominant, hypnotic_profile):
        """Generate homework and integration protocol"""
        if not dominant:
            return "Standard self-hypnosis practice and pattern awareness exercises"
        
        pattern_id = dominant['pattern_id']
        trance_capacity = hypnotic_profile.get('trance_capacity', '')
        
        # Base homework by pattern
        homework = {
            1: "Daily happiness permission practice: Notice and allow positive moments without guilt",
            2: "Collaboration practice: One daily situation where you choose cooperation over control",
            3: "Trust calibration: Daily practice of appropriate trust with evidence-based assessment",
            4: "Both/and thinking: Daily identification of either/or thoughts and expansion to possibilities",
            5: "Being practice: Daily moments of worth not tied to doing or achieving",
            6: "Authenticity practice: Consistent self-expression across different contexts daily",
            7: "Self-care strength: Daily practice of caring for yourself as you would a loved one",
            8: "Personal truth: Daily check-in with your authentic desires separate from family expectations",
            9: "Boundary consistency: Daily practice of maintaining values and boundaries across contexts"
        }.get(pattern_id, "Pattern-specific daily awareness and practice")
        
        # Add self-hypnosis based on trance capacity
        if 'very easily' in trance_capacity.lower():
            homework += "\nSelf-hypnosis: 15-20 minute daily practice with recorded session"
        elif 'never' in trance_capacity.lower():
            homework += "\nMindful awareness: 5-10 minute daily mindfulness practice"
        else:
            homework += "\nSelf-hypnosis: 10-15 minute daily practice with simple relaxation"
        
        return homework

    def _get_week_1_prediction(self, outcome_predictions):
        """Predict week 1 outcomes"""
        probability = outcome_predictions.get('rapid_change_probability', '')
        if 'High' in probability:
            return "Noticeable shift in automatic responses, reduced pattern frequency"
        elif 'Good' in probability:
            return "Initial changes in awareness, some pattern interruption"
        else:
            return "Increased awareness of patterns, beginning of change process"

    def _get_month_1_prediction(self, outcome_predictions):
        """Predict month 1 outcomes"""
        probability = outcome_predictions.get('rapid_change_probability', '')
        if 'High' in probability:
            return "Significant pattern transformation, new responses becoming automatic"
        elif 'Good' in probability:
            return "Consistent pattern interruption, new responses developing"
        else:
            return "Gradual pattern modification, increased conscious choice"

    def _get_3month_prediction(self, outcome_predictions):
        """Predict 3 month outcomes"""
        probability = outcome_predictions.get('rapid_change_probability', '')
        if 'High' in probability:
            return "Full integration of new patterns, unconscious competence achieved"
        elif 'Good' in probability:
            return "Strong integration, occasional conscious reinforcement needed"
        else:
            return "Solid progress, continued practice for full integration"

    def _get_rapport_strategy(self, dominant, hypnotic_profile):
        """Get rapport building strategy"""
        if not dominant:
            return "Standard rapport building with client's preferred communication style"
        
        pattern_id = dominant['pattern_id']
        therapeutic_style = hypnotic_profile.get('therapeutic_style', '')
        
        strategies = {
            1: "Validate their struggles genuinely, avoid premature positivity",
            2: "Collaborative approach, ask permission, share control of session",
            3: "Transparent explanation of all techniques, evidence-based rationale",
            4: "Explore options together, avoid either/or language",
            5: "Appreciate them for who they are, not what they do",
            6: "Consistent authentic presence, no therapeutic 'persona'",
            7: "Model balanced care - caring for them while maintaining boundaries",
            8: "Honor their family values while supporting their individual path",
            9: "Consistent therapeutic boundaries and reliability"
        }
        
        base_strategy = strategies.get(pattern_id, "Standard rapport building")
        
        if 'analytical' in therapeutic_style.lower():
            base_strategy += " - Provide clear explanations and logical frameworks"
        elif 'receptive' in therapeutic_style.lower():
            base_strategy += " - Can be more directive while maintaining warmth"
        
        return base_strategy

    def _predict_authority_response(self, pattern_constellation):
        """Predict how client will respond to therapist authority"""
        dominant = pattern_constellation.get('dominant')
        if not dominant:
            return "Standard therapeutic relationship dynamics"
        
        pattern_id = dominant['pattern_id']
        responses = {
            1: "May be suspicious of therapist's positive regard or suggestions",
            2: "Likely to challenge or test therapist authority, need collaborative approach",
            3: "Will be evaluating therapist trustworthiness, need transparency",
            4: "May feel trapped if given only limited options, need multiple choices",
            5: "May try to 'perform' as good client, remind them they're valuable as-is",
            6: "May present differently than in real life, encourage authenticity",
            7: "May focus on therapist needs over own, redirect to self-care",
            8: "May worry about disappointing therapist like family, address directly",
            9: "May become compliant in session but not outside, check for consistency"
        }
        return responses.get(pattern_id, "Standard authority response patterns")

    def _predict_emotional_regulation(self, pattern_constellation, clinical_flags):
        """Predict emotional regulation during sessions"""
        if 'dissociation_risk' in clinical_flags:
            return "High risk of dissociation - use grounding techniques, shorter sessions"
        
        dominant = pattern_constellation.get('dominant')
        if not dominant:
            return "Standard emotional processing capacity"
        
        pattern_id = dominant['pattern_id']
        regulations = {
            1: "May resist positive emotions, allow gradual happiness tolerance building",
            2: "May become activated during authority topics, use de-escalation",
            3: "May become hypervigilant, provide safety and predictability",
            4: "May become overwhelmed by possibilities, provide structure",
            5: "May become anxious about being vs doing, provide reassurance",
            6: "May struggle with authentic emotional expression, encourage genuineness",
            7: "May minimize own emotions while focusing on others, redirect attention",
            8: "May become guilty about personal emotions, validate feelings",
            9: "May shut down emotions in vulnerable contexts, create safety"
        }
        return regulations.get(pattern_id, "Standard emotional regulation patterns")

    def _predict_change_tolerance(self, resistance_analysis):
        """Predict how fast client can tolerate change"""
        secondary_gains = resistance_analysis.get('secondary_gains', '')
        change_fears = resistance_analysis.get('change_fears', '')
        
        if secondary_gains and 'not' not in secondary_gains.lower():
            return "Slower pace needed - secondary gains present"
        elif change_fears and len(change_fears) > 50:
            return "Moderate pace - address fears first"
        else:
            return "Can likely tolerate rapid change"

    def _recommend_feedback_style(self, pattern_constellation):
        """Recommend feedback style for client"""
        dominant = pattern_constellation.get('dominant')
        if not dominant:
            return "Direct, supportive feedback with specific examples"
        
        pattern_id = dominant['pattern_id']
        styles = {
            1: "Gentle feedback, validate progress, avoid overwhelming positivity",
            2: "Collaborative feedback, ask their opinion first",
            3: "Clear, evidence-based feedback with transparent reasoning",
            4: "Offer multiple perspectives, avoid absolute statements",
            5: "Separate feedback from worth, focus on being not doing",
            6: "Authentic, consistent feedback across all topics",
            7: "Balanced feedback, encourage receiving as well as giving",
            8: "Honor their values while supporting personal growth",
            9: "Consistent feedback regardless of context or their presentation"
        }
        return styles.get(pattern_id, "Supportive, direct feedback with empathy")

    def _get_contact_timeline(self, urgency, clinical_flags):
        """Get contact timeline"""
        if 'suicide_risk' in clinical_flags:
            return "IMMEDIATE - Within 4 hours for crisis intervention"
        elif 'high_risk_client' in clinical_flags:
            return "Within 12 hours for safety assessment"
        elif 'extremely urgent' in urgency.lower():
            return "Within 24 hours for priority scheduling"
        elif 'very urgent' in urgency.lower():
            return "Within 48 hours for expedited response"
        else:
            return "Within 72 hours for standard response"

    def _generate_immediate_action_plan(self, urgency, clinical_flags, pattern_constellation):
        """Generate immediate action plan"""
        actions = []
        
        # Safety first
        if 'suicide_risk' in clinical_flags:
            actions.append("1. CRISIS RESPONSE: Immediate safety assessment required")
            actions.append("2. EMERGENCY PROTOCOL: Have crisis resources ready")
        elif 'high_risk_client' in clinical_flags:
            actions.append("1. PRIORITY CONTACT: Safety-focused initial call")
            actions.append("2. SPECIALIZED APPROACH: Review contraindications")
        
        # Urgency-based actions
        if 'extremely urgent' in urgency.lower():
            actions.append("3. RAPID SCHEDULING: Offer session within 48-72 hours")
            actions.append("4. MOTIVATION OPTIMIZATION: Contact while motivation is peak")
        elif 'very urgent' in urgency.lower():
            actions.append("3. PRIORITY SCHEDULING: Accommodate urgent timeline")
            actions.append("4. EXPEDITED RESPONSE: Show responsiveness to their urgency")
        
        # Pattern-based approach
        dominant = pattern_constellation.get('dominant')
        if dominant:
            pattern_id = dominant['pattern_id']
            approach_actions = {
                1: "5. APPROACH: Validate struggles, avoid premature optimism",
                2: "5. APPROACH: Use collaborative language, avoid directive commands",
                3: "5. APPROACH: Provide clear explanations, build trust gradually",
                4: "5. APPROACH: Offer multiple options, avoid either/or language",
                5: "5. APPROACH: Value them for who they are, not achievements",
                6: "5. APPROACH: Be authentic and consistent",
                7: "5. APPROACH: Model balanced care and boundaries",
                8: "5. APPROACH: Honor family while supporting personal growth",
                9: "5. APPROACH: Maintain consistent boundaries and reliability"
            }
            actions.append(approach_actions.get(pattern_id, "5. APPROACH: Use pattern-specific therapeutic style"))
        
        # Preparation actions
        actions.append("6. PREPARATION: Review complete clinical analysis before contact")
        actions.append("7. SESSION SETUP: Prepare pattern-specific intervention strategy")
        
        return "\n".join(actions)

    def _get_safety_prep(self, clinical_flags):
        """Get safety preparation requirements"""
        if not clinical_flags:
            return "Standard safety protocols"
        
        prep_items = []
        for flag in clinical_flags:
            if flag == 'suicide_risk':
                prep_items.append("Crisis intervention resources")
            elif flag == 'dissociation_risk':
                prep_items.append("Grounding techniques ready")
            elif flag == 'medication_considerations':
                prep_items.append("Medication interaction review")
        
        return ", ".join(prep_items) if prep_items else "Standard safety protocols"

    def _get_primary_resistance_focus(self, resistance_analysis):
        """Get primary resistance focus for preparation"""
        secondary_gains = resistance_analysis.get('secondary_gains', '')
        predictions = resistance_analysis.get('predictions', [])
        
        if secondary_gains and 'not' not in secondary_gains.lower():
            return "Secondary gains from current problem"
        elif predictions:
            return predictions[0]
        else:
            return "General resistance to change"

    def _assess_data_quality(self, data):
        """Assess overall data quality"""
        total_questions = data.get('total_questions', 0)
        completion_rate = data.get('completion_rate', '0%')
        
        if total_questions >= 25 and '100%' in completion_rate:
            return "Excellent - Complete assessment with comprehensive data"
        elif total_questions >= 20:
            return "Good - Adequate data for clinical planning"
        else:
            return "Fair - May need supplemental assessment"

    def _assess_therapeutic_confidence(self, assessment_results):
        """Assess confidence in therapeutic recommendations"""
        pattern_constellation = assessment_results.get('pattern_constellation', {})
        behavioral_chain = assessment_results.get('behavioral_chain', {})
        
        dominant = pattern_constellation.get('dominant')
        chain_complete = len([v for v in behavioral_chain.values() if v and v != 'Not provided']) >= 3
        
        if dominant and chain_complete:
            return "High - Clear patterns and behavioral chain identified"
        elif dominant or chain_complete:
            return "Moderate - Some key data points identified"
        else:
            return "Lower - May need additional assessment"

    def _assess_intervention_readiness(self, clinical_flags, resistance_analysis):
        """Assess readiness for intervention"""
        if 'suicide_risk' in clinical_flags:
            return "Crisis intervention required first"
        elif clinical_flags:
            return "Modified approach needed due to clinical considerations"
        elif resistance_analysis.get('secondary_gains'):
            return "Address resistance factors in session 1"
        else:
            return "Ready for standard hypnotherapy intervention"

    def _assess_overall_data_quality(self, data):
        """Assess overall data quality for clinical use"""
        assessment_results = data.get('assessment_results', {})
        
        # Check data completeness
        presenting_problem = assessment_results.get('presenting_problem', {})
        pattern_constellation = assessment_results.get('pattern_constellation', {})
        behavioral_chain = assessment_results.get('behavioral_chain', {})
        
        quality_score = 0
        
        if presenting_problem.get('target_behavior') and presenting_problem.get('target_behavior') != 'Not specified':
            quality_score += 2
        
        if pattern_constellation.get('dominant'):
            quality_score += 2
        
        chain_completeness = len([v for v in behavioral_chain.values() if v and v != 'Not provided'])
        if chain_completeness >= 3:
            quality_score += 2
        
        if quality_score >= 5:
            return "High quality - Complete data for therapeutic planning"
        elif quality_score >= 3:
            return "Good quality - Adequate for clinical intervention"
        else:
            return "Moderate quality - May need supplemental data"

    def _assess_clinical_confidence(self, assessment_results):
        """Assess clinical confidence in recommendations"""
        # Multiple factors contribute to confidence
        confidence_factors = 0
        
        if assessment_results.get('presenting_problem', {}).get('target_behavior') != 'Not specified':
            confidence_factors += 1
        
        if assessment_results.get('pattern_constellation', {}).get('dominant'):
            confidence_factors += 1
        
        if len(assessment_results.get('behavioral_chain', {})) >= 3:
            confidence_factors += 1
        
        if not assessment_results.get('clinical_flags'):
            confidence_factors += 1
        
        if confidence_factors >= 3:
            return "High confidence in therapeutic recommendations"
        elif confidence_factors >= 2:
            return "Moderate confidence with ongoing calibration needed"
        else:
            return "Lower confidence - recommend additional assessment"

    def _get_next_review_timeline(self, urgency, clinical_flags):
        """Get next review timeline"""
        if 'suicide_risk' in clinical_flags:
            return "Immediate review after crisis intervention"
        elif 'extremely urgent' in urgency.lower():
            return "24-48 hours post initial contact"
        else:
            return "1 week post initial session"

    def _recommend_therapist_type(self, assessment_results):
        """Recommend type of therapist needed"""
        clinical_flags = assessment_results.get('clinical_flags', [])
        safety_assessment = assessment_results.get('safety_assessment', {})
        
        if 'suicide_risk' in clinical_flags:
            return "Crisis intervention specialist, then licensed clinical hypnotherapist"
        elif safety_assessment.get('referral_needed'):
            return "Licensed clinical psychologist with hypnotherapy specialization"
        elif clinical_flags:
            return "Licensed clinical hypnotherapist with trauma experience"
        else:
            return "Certified hypnotherapist with rapid transformation specialization"

    def _determine_therapeutic_pace(self, urgency, clinical_flags):
        """Determine appropriate therapeutic pace"""
        if clinical_flags:
            return "Cautious pace with safety monitoring"
        elif 'extremely urgent' in urgency.lower():
            return "Accelerated pace matching client urgency"
        elif 'very urgent' in urgency.lower():
            return "Moderately accelerated pace"
        else:
            return "Standard therapeutic pace"

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
clinical_email_handler = ClinicalEmailHandler()

def send_clinical_assessment_results(data):
    """Send clinical assessment results email - MAIN FUNCTION CALLED BY ASSESS.PY"""
    try:
        print("[DEBUG] Clinical email handler - send_clinical_assessment_results called")
        return clinical_email_handler.send_clinical_assessment_results(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_clinical_assessment_results: {e}")
        import traceback
        traceback.print_exc()
        return False

# Backward compatibility functions
def send_assessment_results_email(data):
    """Backward compatibility for assessment results"""
    return send_clinical_assessment_results(data)

def send_discovery_call_email(data):
    """Backward compatibility for discovery calls"""
    return send_clinical_assessment_results(data)

def send_contact_form_email(data):
    """Backward compatibility for contact forms"""
    return send_clinical_assessment_results(data)

def send_booking_confirmation_email(data):
    """Backward compatibility for booking confirmations"""
    return send_clinical_assessment_results(data)
