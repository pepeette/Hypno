# """
# Complete Email Handler for Hypnotherapy Website
# Supports both clinical assessment analysis and standard booking workflows
# Integrates with all website pages and maintains backward compatibility
# """
# import smtplib
# import os
# import re
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime

# class ComprehensiveEmailHandler:
#     """Complete email handler for all website email needs"""
    
#     def __init__(self):
#         # Gmail SMTP configuration
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587
        
#         # Try to get credentials from Streamlit secrets, then environment
#         try:
#             import streamlit as st
#             self.sender_email = st.secrets.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = st.secrets.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
#         except:
#             self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = os.environ.get("GMAIL_APP_PASSWORD", "")
        
#         # Pattern descriptions for clinical analysis
#         self.pattern_descriptions = {
#             1: "Unhappiness Culture - Difficulty accepting or maintaining positive states",
#             2: "Power Struggles - Recurring conflicts and control issues",
#             3: "Systematic Mistrust - Default skepticism and trust difficulties",
#             4: "Separation/Division - Black-and-white thinking patterns",
#             5: "Doing vs Being - Self-worth tied to achievement",
#             6: "Compartmentalized Authenticity - Inconsistent identity",
#             7: "Self-Sacrifice - Prioritizing others while neglecting self",
#             8: "Inherited Missions - Life choices driven by family expectations",
#             9: "Context Dependent Weakness - Situational boundary loss"
#         }
    
#     # ================== CLINICAL ASSESSMENT EMAILS ==================
    
#     def send_clinical_assessment_results(self, assessment_data):
#         """Send comprehensive clinical assessment with therapeutic analysis"""
#         try:
#             print("[DEBUG] Starting clinical assessment email process")
#             print(f"[DEBUG] Assessment data keys: {list(assessment_data.keys())}")
            
#             # Extract key information
#             contact_info = assessment_data.get('contact_info', {})
#             results = assessment_data.get('assessment_results', {})
            
#             if not contact_info:
#                 print("[ERROR] No contact_info found in assessment_data")
#                 return False
            
#             if not results and not assessment_data.get('pattern_scores'):
#                 print("[ERROR] No assessment_results or pattern_scores found")
#                 return False
            
#             urgency = contact_info.get('urgency', 'Standard priority')
#             risk_flags = results.get('risk_flags', []) or assessment_data.get('risk_flags', [])
            
#             print(f"[DEBUG] Found {len(risk_flags)} risk flags")
#             print(f"[DEBUG] Urgency level: {urgency}")
            
#             # Determine priority flag
#             priority_flag = self._get_priority_flag(urgency, risk_flags)
            
#             subject = f"{priority_flag} Clinical Assessment - {contact_info.get('name', 'Client')}"
#             print(f"[DEBUG] Email subject: {subject}")
            
#             body = self._format_clinical_email_body(assessment_data)
            
#             if not body or len(body) < 100:
#                 print("[ERROR] Email body generation failed or too short")
#                 return False
            
#             print(f"[DEBUG] Email body length: {len(body)} characters")
#             return self._send_email(subject, body, "Clinical Assessment")
            
#         except Exception as e:
#             print(f"[ERROR] Clinical assessment email error: {e}")
#             import traceback
#             print(f"[ERROR] Traceback: {traceback.format_exc()}")
#             return False
    
#     def _format_clinical_email_body(self, data):
#         """Format comprehensive clinical assessment email"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Extract data components
#             contact_info = data.get('contact_info', {})
#             results = data.get('assessment_results', {})
#             responses = data.get('assessment_responses', {})
#             intensity_data = data.get('intensity_responses', {})
            
#             # Basic info
#             name = contact_info.get('name', 'Unknown')
#             email = contact_info.get('email', 'Unknown')
#             phone = contact_info.get('phone', 'Not provided')
#             urgency = contact_info.get('urgency', 'Not specified')
#             primary_concern = contact_info.get('primary_concern', 'Not provided')
#             next_step = contact_info.get('next_step', 'Not specified')
            
#             # Clinical data
#             pattern_scores = results.get('pattern_scores', {})
#             risk_flags = results.get('risk_flags', [])
#             dominant_pattern = results.get('dominant_pattern')
#             completion_rate = results.get('completion_rate', 0) * 100
#             total_questions = results.get('total_questions_answered', 0)
#             adaptive_paths = results.get('adaptive_paths_triggered', [])
            
#             body = f"""
# 🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT
# Assessment Completed: {timestamp}
# Clinical Priority: {self._get_clinical_priority(urgency, risk_flags)}

# ═══════════════════════════════════════════════════════════

# 👤 CLIENT PROFILE & CONTACT INFORMATION

# Name: {name}
# Email: {email}
# Phone: {phone}
# Urgency Level: {urgency}
# Primary Concern: {primary_concern}
# Preferred Next Step: {next_step}

# Assessment Quality: {completion_rate:.0f}% completion rate
# Total Questions Answered: {total_questions}
# Adaptive Pathways Triggered: {len(adaptive_paths)}

# ═══════════════════════════════════════════════════════════

# 🎯 BEHAVIORAL PATTERN ANALYSIS

# PRIMARY PATTERNS IDENTIFIED:
# """
            
#             # Add pattern analysis
#             if pattern_scores:
#                 sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                
#                 for i, (pattern_id, score) in enumerate(sorted_patterns[:5]):
#                     pattern_name = self.pattern_descriptions.get(pattern_id, f"Pattern {pattern_id}")
#                     intensity = self._get_intensity_level(score)
#                     rank = "🔴 DOMINANT" if i == 0 else f"{i+1}. SECONDARY"
                    
#                     body += f"""
# {rank} PATTERN: {pattern_name}
# ├─ Activation Score: {score:.1f}/12 ({intensity} intensity)
# ├─ Clinical Significance: {self._get_clinical_significance(pattern_id, score)}
# ├─ Therapeutic Approach: {self._get_therapeutic_approach(pattern_id)}
# └─ Session Priority: {self._get_session_priority(pattern_id, i == 0)}
# """
                
#                 if len(sorted_patterns) > 5:
#                     body += f"\nADDITIONAL PATTERNS: {len(sorted_patterns) - 5} lower-intensity patterns detected\n"
#             else:
#                 body += "\nNo significant patterns above threshold - exploratory approach recommended\n"
            
#             body += f"""
# ═══════════════════════════════════════════════════════════

# ⚠️ CLINICAL RISK ASSESSMENT

# Risk Level: {self._assess_overall_risk_level(risk_flags)}
# Risk Factors Identified: {len(risk_flags)}
# """
            
#             # Risk factor details
#             if risk_flags:
#                 body += "\nSPECIFIC RISK CONSIDERATIONS:\n"
#                 for i, flag in enumerate(risk_flags, 1):
#                     risk_description = self._get_risk_description(flag)
#                     management = self._get_risk_management(flag)
#                     body += f"{i}. {risk_description}\n   └─ Management: {management}\n"
#             else:
#                 body += "\n✅ No significant risk factors identified - standard approach suitable\n"
            
#             body += f"""
# ═══════════════════════════════════════════════════════════

# 🎯 THERAPEUTIC RECOMMENDATIONS

# RECOMMENDED APPROACH: {self._get_recommended_approach(dominant_pattern, risk_flags)}
# ESTIMATED SESSIONS: {self._estimate_session_count(pattern_scores, risk_flags)}
# SUCCESS PROBABILITY: {self._estimate_success_probability(completion_rate, len(risk_flags))}

# SESSION 1 FOCUS:
# {self._get_session_1_focus(dominant_pattern, primary_concern)}

# SESSION 2 FOCUS:
# {self._get_session_2_focus(dominant_pattern, pattern_scores)}

# POTENTIAL RESISTANCE POINTS:
# {self._identify_resistance_points(pattern_scores, responses)}

# HYPNOTHERAPY PROTOCOL:
# {self._generate_hypnotherapy_protocol(dominant_pattern, intensity_data)}

# ═══════════════════════════════════════════════════════════

# 📊 DETAILED RESPONSE ANALYSIS

# ASSESSMENT COMPLETION DATA:
# """
            
#             # Add key responses analysis
#             key_responses = self._extract_key_responses(responses)
#             if key_responses:
#                 body += "\nKEY CLIENT RESPONSES:\n"
#                 for question, response in key_responses.items():
#                     body += f"• {question}: {response}\n"
            
#             # Intensity data
#             if intensity_data:
#                 body += f"\nINTENSITY RATINGS PROVIDED: {len(intensity_data)} questions\n"
#                 high_intensity = {k: v for k, v in intensity_data.items() if v >= 6}
#                 if high_intensity:
#                     body += f"HIGH INTENSITY RESPONSES: {len(high_intensity)} items rated 6-7/7\n"
            
#             body += f"""
# ADAPTIVE QUESTIONING TRIGGERED: {', '.join(adaptive_paths) if adaptive_paths else 'None'}

# ═══════════════════════════════════════════════════════════

# 📞 IMMEDIATE ACTION PROTOCOL

# CONTACT TIMELINE: {self._get_contact_timeline(urgency, risk_flags)}
# RECOMMENDED RESPONSE: {self._get_recommended_response(next_step)}

# PREPARATION CHECKLIST:
# 1. Review complete client responses (attached below)
# 2. Prepare pattern-specific approach for {self.pattern_descriptions.get(dominant_pattern, 'identified patterns')}
# 3. {self._get_specific_preparation(dominant_pattern, risk_flags)}
# 4. Set up appropriate session environment and materials

# ═══════════════════════════════════════════════════════════

# 💬 COMPLETE CLIENT RESPONSES TRANSCRIPT

# FULL ASSESSMENT RESPONSES:
# """
            
#             # Add complete response transcript
#             if responses:
#                 for q_id in sorted(responses.keys()):
#                     response_data = responses[q_id]
#                     question_text = response_data.get('question_text', f'Question {q_id}')
#                     response = response_data.get('response', 'No response')
#                     intensity = intensity_data.get(q_id)
                    
#                     body += f"\n{q_id}. {question_text}\n"
#                     body += f"   Response: {response}\n"
#                     if intensity:
#                         body += f"   Intensity: {intensity}/7\n"
#                     body += f"   Timestamp: {response_data.get('timestamp', 'Unknown')}\n"
            
#             body += f"""

# ═══════════════════════════════════════════════════════════

# 🔧 TECHNICAL ASSESSMENT METADATA

# Assessment Algorithm: Comprehensive Behavioral Pattern Analysis v2.0
# Completion Quality: {completion_rate:.0f}% ({total_questions} questions answered)
# Clinical Confidence: {self._assess_clinical_confidence(completion_rate, len(pattern_scores))}
# Data Integrity: {self._assess_data_integrity(responses)}

# Therapist Assignment Recommendation: {self._recommend_therapist_type(risk_flags, urgency)}
# Next Clinical Review: {self._get_next_review_date(urgency, risk_flags)}

# ⚠️ CONFIDENTIAL CLINICAL DOCUMENT
# Contains sensitive psychological assessment data
# Licensed therapist review required before client contact

# ═══════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Clinical Assessment System
# Generated: {timestamp}
# Client Reference: {name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}
#             """
            
#             return body
            
#         except Exception as e:
#             print(f"[ERROR] Error formatting clinical email: {e}")
#             # Return basic email with error info
#             return f"""
# CLINICAL ASSESSMENT RESULTS - FORMATTING ERROR

# Client: {data.get('contact_info', {}).get('name', 'Unknown')}
# Email: {data.get('contact_info', {}).get('email', 'Unknown')}
# Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Error Details: {str(e)}

# Raw assessment data available - manual review required.
# Complete responses preserved for clinical analysis.

# Bangkok Hypnotherapy Clinic - Clinical Assessment System
#             """
    
#     # ================== STANDARD BOOKING EMAILS ==================
    
#     def send_booking_email(self, name, email, concern, message, booking_type):
#         """Send standard booking notification (maintains compatibility)"""
#         try:
#             print(f"[DEBUG] Sending {booking_type} booking email")
            
#             subject = f"📞 New {booking_type} Request - {name}"
#             body = self._format_booking_email_body(name, email, concern, message, booking_type)
            
#             return self._send_email(subject, body, booking_type)
            
#         except Exception as e:
#             print(f"[ERROR] Booking email error: {e}")
#             return False
    
#     def send_discovery_call_email(self, booking_data):
#         """Send discovery call booking notification"""
#         try:
#             name = booking_data.get('name', '')
#             email = booking_data.get('email', '')
#             concern = booking_data.get('concern', '')
#             message = booking_data.get('concern_description', '') or booking_data.get('message', '')
#             urgency = booking_data.get('urgency', '')
#             experience = booking_data.get('experience', '')
            
#             subject = f"📞 New Discovery Call Request - {name}"
#             body = self._format_discovery_call_body(name, email, concern, message, urgency, experience)
            
#             return self._send_email(subject, body, "Discovery Call")
            
#         except Exception as e:
#             print(f"[ERROR] Discovery call email error: {e}")
#             return False
    
#     def send_package_booking_email(self, booking_data):
#         """Send transformation package booking notification"""
#         try:
#             name = booking_data.get('name', '')
#             email = booking_data.get('email', '')
#             concern = booking_data.get('concern', '')
#             message = booking_data.get('message', '')
#             package_type = booking_data.get('package_type', '')
#             experience = booking_data.get('experience', '')
            
#             subject = f"💰 New Transformation Package Booking - {name}"
#             body = self._format_package_booking_body(name, email, concern, message, package_type, experience)
            
#             return self._send_email(subject, body, "Package Booking")
            
#         except Exception as e:
#             print(f"[ERROR] Package booking email error: {e}")
#             return False
    
#     def _format_booking_email_body(self, name, email, concern, message, booking_type):
#         """Format standard booking email (maintains compatibility)"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         return f"""
# 📞 NEW {booking_type.upper()} REQUEST
# Received: {timestamp}

# ═══════════════════════════════════════════

# 👤 CONTACT INFORMATION:
# Name: {name}
# Email: {email}

# 🎯 CONCERN DETAILS:
# Primary Concern: {concern}
# Message: {message}

# 📞 NEXT STEPS:
# Please contact this person within 24-48 hours to schedule their {booking_type.lower()}.

# ═══════════════════════════════════════════
# Bangkok Hypnotherapy Clinic
# Automated Booking System
#         """
    
#     def _format_discovery_call_body(self, name, email, concern, message, urgency, experience):
#         """Format discovery call email with enhanced details"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Determine priority based on urgency
#         if 'extremely urgent' in urgency.lower():
#             priority = "🔴 HIGH PRIORITY"
#         elif 'very urgent' in urgency.lower():
#             priority = "🟡 PRIORITY"
#         else:
#             priority = "📋 STANDARD"
        
#         return f"""
# {priority} DISCOVERY CALL REQUEST
# Received: {timestamp}

# ═══════════════════════════════════════════

# 👤 CLIENT INFORMATION:
# Name: {name}
# Email: {email}

# 🎯 CONCERN DETAILS:
# Primary Concern: {concern}
# Urgency Level: {urgency}
# Previous Experience: {experience}

# 💬 CLIENT MESSAGE:
# {message}

# 📞 ACTION REQUIRED:
# Contact Timeline: {self._get_simple_contact_timeline(urgency)}

# RECOMMENDED APPROACH:
# 1. {self._get_discovery_call_approach(concern, urgency)}
# 2. Assess suitability for rapid transformation method
# 3. Explain 2-session approach if appropriate
# 4. Schedule Session 1 if client is ready to proceed

# ═══════════════════════════════════════════
# Bangkok Hypnotherapy Clinic
# Discovery Call System
#         """
    
#     def _format_package_booking_body(self, name, email, concern, message, package_type, experience):
#         """Format package booking email with enhanced details"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         return f"""
# 💰 TRANSFORMATION PACKAGE BOOKING
# Received: {timestamp}

# ═══════════════════════════════════════════

# 👤 CLIENT INFORMATION:
# Name: {name}
# Email: {email}

# 📦 PACKAGE DETAILS:
# Selected Package: {package_type}
# Primary Concern: {concern}
# Previous Experience: {experience}

# 💬 CLIENT MESSAGE:
# {message}

# 📞 HIGH PRIORITY ACTION REQUIRED:
# This client is ready to proceed with transformation package.

# IMMEDIATE STEPS:
# 1. Send welcome email with package confirmation
# 2. Schedule Session 1 within 48-72 hours
# 3. Send pre-session preparation materials
# 4. Confirm payment method and schedule

# 💰 EXPECTED REVENUE: 3,000-4,000 THB

# ═══════════════════════════════════════════
# Bangkok Hypnotherapy Clinic
# Package Booking System
#         """
    
#     # ================== EMAIL SENDING INFRASTRUCTURE ==================
    
#     def _send_email(self, subject, body, email_type):
#         """Send email via Gmail SMTP"""
#         try:
#             if not self.password:
#                 print(f"[DEBUG] {email_type} email simulation (no password configured)")
#                 print(f"[DEBUG] To: {self.recipient_email}")
#                 print(f"[DEBUG] Subject: {subject}")
#                 return True
            
#             # Create message
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = subject
#             msg.attach(MIMEText(body, 'plain'))
            
#             # Send email
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
#             server.starttls()
#             server.login(self.sender_email, self.password)
#             server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
#             server.quit()
            
#             print(f"[SUCCESS] {email_type} email sent successfully")
#             return True
            
#         except Exception as e:
#             print(f"[ERROR] SMTP error for {email_type}: {e}")
#             return False
    
#     # ================== CLINICAL ANALYSIS HELPER METHODS ==================
    
#     def _get_priority_flag(self, urgency, risk_flags):
#         """Determine clinical priority flag"""
#         if len(risk_flags) >= 3:
#             return "🔴 HIGH RISK"
#         elif 'extremely urgent' in urgency.lower():
#             return "🟠 URGENT"
#         elif 'very urgent' in urgency.lower():
#             return "🟡 PRIORITY"
#         else:
#             return "📋 ASSESSMENT"
    
#     def _get_clinical_priority(self, urgency, risk_flags):
#         if len(risk_flags) >= 3:
#             return "HIGH RISK - Specialized approach required"
#         elif 'extremely urgent' in urgency.lower():
#             return "URGENT - Priority scheduling within 24 hours"
#         elif 'very urgent' in urgency.lower():
#             return "ELEVATED - Contact within 48 hours"
#         else:
#             return "STANDARD - Contact within 72 hours"
    
#     def _get_intensity_level(self, score):
#         if score >= 8:
#             return "Very High"
#         elif score >= 6:
#             return "High"
#         elif score >= 4:
#             return "Moderate"
#         elif score >= 2:
#             return "Low"
#         else:
#             return "Minimal"
    
#     def _get_clinical_significance(self, pattern_id, score):
#         base_significance = {
#             1: "Blocks positive therapeutic outcomes, requires permission-based approach",
#             2: "May resist directive techniques, needs collaborative framework",
#             3: "Trust-building essential before intervention, transparency required",
#             4: "Expand thinking flexibility, address either/or cognitive patterns",
#             5: "Separate self-worth from performance, emphasize being over doing",
#             6: "Identity integration work needed across contexts",
#             7: "Self-care resistance expected, reframe as strength for helping others",
#             8: "Family loyalty conflicts may emerge, honor while expanding choice",
#             9: "Context-dependent response patterns, strengthen consistent boundaries"
#         }.get(pattern_id, "Pattern-specific intervention required")
        
#         if score >= 8:
#             return f"DOMINANT PATTERN: {base_significance}"
#         elif score >= 6:
#             return f"SIGNIFICANT PATTERN: {base_significance}"
#         else:
#             return f"SUPPORTING PATTERN: {base_significance}"
    
#     def _get_therapeutic_approach(self, pattern_id):
#         approaches = {
#             1: "Permission installation, positive expectation building, success tolerance",
#             2: "Collaborative empowerment, shared control, non-directive language",
#             3: "Trust-first approach, transparent explanations, evidence-based interventions",
#             4: "Integration therapy, both/and thinking, possibility expansion",
#             5: "Being-centered work, inherent worth installation, performance separation",
#             6: "Authentic self integration across contexts, consistency building",
#             7: "Self-care strength reframing, boundary establishment, balanced care",
#             8: "Personal desire differentiation, respectful family honor, authentic vision",
#             9: "Context-independent strength, consistent boundary maintenance"
#         }
#         return approaches.get(pattern_id, "Pattern-specific individualized approach")
    
#     def _get_session_priority(self, pattern_id, is_dominant):
#         if is_dominant:
#             priorities = {
#                 1: "Session 1 Priority - Address happiness resistance, install permission",
#                 2: "Session 1 Priority - Establish collaboration, avoid power dynamics",
#                 3: "Session 1 Priority - Build trust foundation, transparent process",
#                 4: "Session 1 Priority - Expand thinking flexibility, explore options",
#                 5: "Session 1 Priority - Separate worth from doing, establish being value",
#                 6: "Session 1 Priority - Support authentic consistency across contexts",
#                 7: "Session 1 Priority - Reframe self-care as strength for service",
#                 8: "Session 1 Priority - Honor family while supporting personal truth",
#                 9: "Session 1 Priority - Strengthen consistent boundaries across contexts"
#             }
#             return priorities.get(pattern_id, "Session 1 Priority - Address dominant pattern")
#         else:
#             return "Session 2 Integration - Address as supporting pattern"
    
#     def _assess_overall_risk_level(self, risk_flags):
#         if len(risk_flags) >= 4:
#             return "HIGH - Specialized clinical approach required"
#         elif len(risk_flags) >= 2:
#             return "ELEVATED - Modified approach with safety protocols"
#         elif len(risk_flags) >= 1:
#             return "MODERATE - Standard approach with precautions"
#         else:
#             return "LOW - Standard hypnotherapy approach suitable"
    
#     def _get_risk_description(self, flag):
#         descriptions = {
#             'risk_q_10': "Current medical/mental health care - coordination required",
#             'risk_q_11': "Intense emotional states - emotional regulation concerns",
#             'risk_q_12': "Dissociation/panic/self-harm history - safety protocols needed",
#             'risk_q_13': "Substance use patterns - sobriety considerations"
#         }
#         return descriptions.get(flag, f"Risk factor identified - {flag}")
    
#     def _get_risk_management(self, flag):
#         management = {
#             'risk_q_10': "Coordinate with existing care providers before sessions",
#             'risk_q_11': "Use grounding techniques, shorter sessions, emotion regulation",
#             'risk_q_12': "Safety assessment, crisis resources, modified approach",
#             'risk_q_13': "Address substance use, consider timing of intervention"
#         }
#         return management.get(flag, "Standard clinical precautions")
    
#     def _get_recommended_approach(self, dominant_pattern, risk_flags):
#         if len(risk_flags) >= 2:
#             return "Modified hypnotherapy with specialized safety protocols"
#         elif dominant_pattern in [1, 2, 3]:
#             return "Collaborative, permission-based hypnotherapy approach"
#         elif dominant_pattern in [7, 8, 9]:
#             return "Gentle, supportive hypnotherapy with boundary work"
#         else:
#             return "Standard clinical hypnotherapy with pattern-specific modifications"
    
#     def _estimate_session_count(self, pattern_scores, risk_flags):
#         if len(risk_flags) >= 2:
#             return "3-4 sessions (additional support needed)"
#         elif len(pattern_scores) >= 3:
#             return "2-3 sessions (complex pattern integration)"
#         else:
#             return "2 sessions (standard rapid transformation)"
    
#     def _estimate_success_probability(self, completion_rate, risk_count):
#         if completion_rate >= 90 and risk_count == 0:
#             return "HIGH (85%+) - Excellent assessment quality, no risk factors"
#         elif completion_rate >= 75 and risk_count <= 1:
#             return "GOOD (70-85%) - Good assessment quality, minimal risk"
#         elif completion_rate >= 60:
#             return "MODERATE (55-70%) - Fair assessment, some complexity"
#         else:
#             return "VARIABLE - May need additional assessment for optimization"
    
#     def _get_session_1_focus(self, dominant_pattern, concern):
#         if dominant_pattern:
#             pattern_name = self.pattern_descriptions.get(dominant_pattern, f"Pattern {dominant_pattern}")
#             return f"Address {pattern_name} - rapport building and initial pattern interruption"
#         else:
#             return f"Exploratory session focused on client's primary concern: {concern[:100]}"
    
#     def _get_session_2_focus(self, dominant_pattern, pattern_scores):
#         if dominant_pattern and len(pattern_scores) >= 2:
#             return "Core transformation of dominant pattern with supporting pattern integration"
#         elif dominant_pattern:
#             return f"Deep transformation of {self.pattern_descriptions.get(dominant_pattern)}"
#         else:
#             return "Individualized transformation based on session 1 insights"
    
#     def _identify_resistance_points(self, pattern_scores, responses):
#         resistance_patterns = []
        
#         # Check for specific resistance indicators
#         if 1 in pattern_scores:  # Unhappiness culture
#             resistance_patterns.append("• May resist positive suggestions or success imagery")
#         if 2 in pattern_scores:  # Power struggles
#             resistance_patterns.append("• May challenge therapist authority or directive language")
#         if 3 in pattern_scores:  # Mistrust
#             resistance_patterns.append("• May question techniques or need extensive explanations")
        
#         # Check secondary gain responses
#         secondary_gain_responses = [r for r in responses.values() 
#                                   if 'secondary_gain' in r.get('question_text', '').lower()]
#         if secondary_gain_responses:
#             resistance_patterns.append("• Secondary gains identified - address benefits of current pattern")
        
#         return '\n'.join(resistance_patterns) if resistance_patterns else "• Minimal resistance predicted based on assessment"
    
#     def _generate_hypnotherapy_protocol(self, dominant_pattern, intensity_data):
#         if not dominant_pattern:
#             return "Standard protocol with individualization based on session 1 findings"
        
#         protocols = {
#             1: "Gentle permission-based induction, positive expectation installation, happiness tolerance",
#             2: "Collaborative induction, shared control language, empowerment suggestions",
#             3: "Transparent explanation of process, trust-building suggestions, evidence-based approach",
#             4: "Integration-focused suggestions, both/and language, possibility expansion",
#             5: "Being-centered induction, worth installation separate from doing, presence anchoring",
#             6: "Consistent identity suggestions across contexts, authenticity integration",
#             7: "Self-care strength installation, balanced care suggestions, boundary visualization",
#             8: "Family honor with personal truth, loyalty reframe, authentic path suggestions",
#             9: "Consistent strength installation, boundary integrity across all contexts"
#         }
        
#         base_protocol = protocols.get(dominant_pattern, "Standard individualized approach")
        
#         # Modify based on intensity data
#         if intensity_data and max(intensity_data.values()) >= 6:
#             base_protocol += " - High intensity responses require gentle pacing and grounding"
        
#         return base_protocol
    
#     def _extract_key_responses(self, responses):
#         """Extract the most clinically relevant responses"""
#         key_responses = {}
        
#         for q_id, response_data in responses.items():
#             question = response_data.get('question_text', '')
#             response = response_data.get('response', '')
            
#             # Include key assessment questions
#             if any(keyword in question.lower() for keyword in 
#                    ['specific behavior', 'trigger', 'physical sensation', 'inner voice', 'behavioral response']):
#                 key_responses[question[:80] + "..."] = str(response)[:150]
        
#         return dict(list(key_responses.items())[:5])  # Top 5 most relevant
    
#     def _get_contact_timeline(self, urgency, risk_flags):
#         if len(risk_flags) >= 3:
#             return "IMMEDIATE - Within 12 hours for safety assessment"
#         elif 'extremely urgent' in urgency.lower():
#             return "PRIORITY - Within 24 hours for urgent scheduling"
#         elif 'very urgent' in urgency.lower():
#             return "ELEVATED - Within 48 hours for prompt response"
#         else:
#             return "STANDARD - Within 72 hours for routine follow-up"
    
#     def _get_recommended_response(self, next_step):
#         if 'consultation' in next_step.lower():
#             return "Schedule free consultation call via provided contact information"
#         elif 'package' in next_step.lower():
#             return "Send transformation package information and pricing"
#         elif 'analysis' in next_step.lower():
#             return "Email detailed analysis with specific recommendations first"
#         else:
#             return "Contact client to discuss personalized next steps"
    
#     def _get_specific_preparation(self, dominant_pattern, risk_flags):
#         if len(risk_flags) >= 2:
#             return "Prepare safety protocols and crisis resources"
#         elif dominant_pattern == 1:
#             return "Prepare permission-based language, avoid overwhelming positivity"
#         elif dominant_pattern == 2:
#             return "Prepare collaborative approach, avoid directive commands"
#         elif dominant_pattern == 3:
#             return "Prepare transparent explanations, evidence-based rationales"
#         else:
#             return f"Prepare pattern-specific approach for {self.pattern_descriptions.get(dominant_pattern, 'identified pattern')}"
    
#     def _assess_clinical_confidence(self, completion_rate, pattern_count):
#         if completion_rate >= 90 and pattern_count >= 2:
#             return "HIGH - Comprehensive data for targeted intervention"
#         elif completion_rate >= 75:
#             return "GOOD - Adequate data for effective treatment planning"
#         else:
#             return "MODERATE - May benefit from supplemental assessment"
    
#     def _assess_data_integrity(self, responses):
#         if len(responses) >= 20:
#             return "EXCELLENT - Comprehensive response set"
#         elif len(responses) >= 15:
#             return "GOOD - Adequate response coverage"
#         else:
#             return "FAIR - Limited responses, focus on quality of available data"
    
#     def _recommend_therapist_type(self, risk_flags, urgency):
#         if len(risk_flags) >= 3:
#             return "Licensed clinical psychologist with hypnotherapy specialization"
#         elif len(risk_flags) >= 1:
#             return "Licensed clinical hypnotherapist with safety training"
#         elif 'extremely urgent' in urgency.lower():
#             return "Experienced rapid-change hypnotherapist"
#         else:
#             return "Certified clinical hypnotherapist"
    
#     def _get_next_review_date(self, urgency, risk_flags):
#         if len(risk_flags) >= 2:
#             return "24-48 hours post-contact for safety monitoring"
#         elif 'extremely urgent' in urgency.lower():
#             return "1 week post-session for progress assessment"
#         else:
#             return "2 weeks post-completion for outcome tracking"
    
#     # ================== BOOKING HELPER METHODS ==================
    
#     def _get_simple_contact_timeline(self, urgency):
#         """Get simple contact timeline for booking emails"""
#         if 'extremely urgent' in urgency.lower():
#             return "Within 24 hours (high priority)"
#         elif 'very urgent' in urgency.lower():
#             return "Within 48 hours (priority)"
#         else:
#             return "Within 72 hours (standard)"
    
#     def _get_discovery_call_approach(self, concern, urgency):
#         """Get recommended approach for discovery call"""
#         if 'anxiety' in concern.lower():
#             return "Use calm, reassuring approach - explain safety of hypnotherapy"
#         elif 'smoking' in concern.lower():
#             return "Focus on rapid cessation method - emphasize 2-session success rate"
#         elif 'habit' in concern.lower():
#             return "Explain pattern interruption approach - assess habit specifics"
#         elif 'extremely urgent' in urgency.lower():
#             return "Acknowledge urgency, assess suitability for immediate scheduling"
#         else:
#             return "Standard discovery call approach - assess suitability and explain method"


# # ================== GLOBAL INSTANCE AND HELPER FUNCTIONS ==================

# # Global instance
# comprehensive_email_handler = ComprehensiveEmailHandler()

# # ====== MAIN ASSESSMENT FUNCTION ======
# def send_clinical_assessment_results(assessment_data):
#     """Send clinical assessment results - Main function for assess.py integration"""
#     try:
#         print("[DEBUG] Sending clinical assessment results via comprehensive handler")
#         return comprehensive_email_handler.send_clinical_assessment_results(assessment_data)
#     except Exception as e:
#         print(f"[ERROR] Exception in clinical assessment email: {e}")
#         return False

# # ====== STANDARD BOOKING FUNCTIONS ======
# def send_booking_email(name, email, concern, message, booking_type):
#     """Send standard booking email - Maintains existing compatibility"""
#     try:
#         print(f"[DEBUG] Sending {booking_type} booking email")
#         return comprehensive_email_handler.send_booking_email(name, email, concern, message, booking_type)
#     except Exception as e:
#         print(f"[ERROR] Exception in booking email: {e}")
#         return False

# def send_discovery_call_email(booking_data):
#     """Send discovery call booking notification"""
#     try:
#         print("[DEBUG] Sending discovery call email")
#         return comprehensive_email_handler.send_discovery_call_email(booking_data)
#     except Exception as e:
#         print(f"[ERROR] Exception in discovery call email: {e}")
#         return False

# def send_package_booking_email(booking_data):
#     """Send package booking notification"""
#     try:
#         print("[DEBUG] Sending package booking email")
#         return comprehensive_email_handler.send_package_booking_email(booking_data)
#     except Exception as e:
#         print(f"[ERROR] Exception in package booking email: {e}")
#         return False

# # ====== BACKWARD COMPATIBILITY FUNCTIONS ======
# def send_assessment_results_email(data):
#     """Backward compatibility for assessment results"""
#     return send_clinical_assessment_results(data)

# def send_contact_form_email(data):
#     """Backward compatibility for contact forms"""
#     # Convert contact form data to booking format
#     booking_data = {
#         'name': data.get('name', ''),
#         'email': data.get('email', ''),
#         'concern': data.get('concern', ''),
#         'message': data.get('message', ''),
#         'urgency': data.get('urgency', ''),
#         'experience': data.get('experience', '')
#     }
#     return send_discovery_call_email(booking_data)

# def send_booking_confirmation_email(data):
#     """Backward compatibility for booking confirmations"""
#     return send_discovery_call_email(data)






"""
Enhanced Email Handler for Hypnotherapy Website
Comprehensive clinical assessment integration with complete intervention mapping
Maintains all existing booking functionality while adding advanced clinical analysis
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
import re

class EmailHandler:
    """Complete email handler with advanced clinical assessment capabilities"""
    
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
        
        # Clinical pattern analysis tables
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
        
        # Intervention mapping tables
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
            }
        }
        
        # Session protocol templates
        self.session_protocols = {
            "session_1_template": {
                "opening": "Validate assessment findings and build therapeutic alliance",
                "exploration": "Map behavioral chain and pattern origins",
                "intervention": "Install initial positive programming",
                "closing": "Assess readiness and plan session 2"
            },
            "session_2_template": {
                "opening": "Review changes and reinforce session 1 work",
                "transformation": "Core pattern interruption and rewiring",
                "integration": "Install new identity and behavior patterns",
                "closing": "Future pace and reinforce transformation"
            }
        }

    # ================== EXISTING BOOKING FUNCTIONS (UNCHANGED) ==================
    
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification - MAINTAINS ORIGINAL FUNCTIONALITY"""
        try:
            print(f"[DEBUG] send_discovery_call_email called with data keys: {list(booking_data.keys())}")
            
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "🔔 New Discovery Call Booking Request"
            
            # Format the email body using original method
            body = self._format_discovery_email_body(booking_data)
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email if password is available
            if self.password:
                return self._send_email(msg)
            else:
                print(f"Discovery Call Booking: {booking_data}")
                return True
                    
        except Exception as e:
            print(f"[ERROR] Exception in send_discovery_call_email: {e}")
            return False
    
    def send_package_booking_email(self, booking_data):
        """Send package booking notification - MAINTAINS ORIGINAL FUNCTIONALITY"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "💰 New Transformation Package Booking"
            
            body = self._format_package_email_body(booking_data)
            msg.attach(MIMEText(body, 'plain'))
            
            if self.password:
                return self._send_email(msg)
            else:
                print(f"Package Booking: {booking_data}")
                return True
                
        except Exception as e:
            print(f"Email sending error: {e}")
            return False

    # ================== NEW CLINICAL ASSESSMENT FUNCTION ==================
    
    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment with complete intervention mapping"""
        try:
            print("[DEBUG] Sending enhanced clinical assessment results email")
            
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
                print(f"[DEBUG] Enhanced clinical assessment email sent: {result}")
                return result
            else:
                print(f"Enhanced Clinical Assessment Results: {assessment_data}")
                return True
                
        except Exception as e:
            print(f"[ERROR] Exception in send_clinical_assessment_results: {e}")
            import traceback
            traceback.print_exc()
            return False

    # ================== COMPREHENSIVE CLINICAL ANALYSIS ==================
    
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

    # ================== CLINICAL ANALYSIS COMPONENTS ==================
    
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

🔗 Pattern Interaction Analysis:"""
                
                # Add pattern interaction analysis
                if i == 1 and len(sorted_patterns) > 1:
                    analysis += f"\n   Primary pattern {pattern_id} creates foundation for secondary patterns"
                elif i > 1:
                    analysis += f"\n   Pattern {pattern_id} reinforces and maintains Pattern {sorted_patterns[0][0]} dynamics"
                
                analysis += "\n"
        
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
        chain_analysis += """
🎯 CHAIN DISRUPTION STRATEGY:
• PRIMARY INTERRUPTION POINT: """ + self._identify_primary_interruption_point(trigger_chain) + """
• SECONDARY ANCHOR POINTS: """ + self._identify_secondary_anchor_points(trigger_chain) + """
• INTERVENTION SEQUENCE: """ + self._generate_intervention_sequence(trigger_chain) + """

📊 CHAIN PATTERN ANALYSIS:
• Chain complexity: """ + self._assess_chain_complexity(trigger_chain) + """
• Intervention readiness: """ + self._assess_intervention_readiness(trigger_chain) + """
• Success probability: """ + self._estimate_chain_success_probability(trigger_chain) + """
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
        
        # Analyze environmental triggers
        environmental_factors = self._extract_environmental_factors(responses)
        if environmental_factors:
            systemic_analysis += f"""
🏠 ENVIRONMENTAL FACTORS:
{environmental_factors}

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
        
        # Analyze family loyalty patterns
        family_loyalty_analysis = self._analyze_family_loyalty_patterns(responses)
        if family_loyalty_analysis:
            identity_analysis += f"""
👪 FAMILY LOYALTY ANALYSIS:
{family_loyalty_analysis}

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
    
    # ================== HELPER METHODS FOR CLINICAL ANALYSIS ==================
    
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
    
    def _extract_environmental_factors(self, responses):
        """Extract environmental factors from responses"""
        environmental_factors = []
        
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            question_text = str(response_data.get('question_text', '')).lower()
            
            if 'situation' in question_text or 'environment' in question_text or 'context' in question_text:
                if any(env_word in response_text for env_word in ['work', 'home', 'social', 'public', 'family']):
                    environmental_factors.append(f"• {response_data.get('response', '')[:100]}...")
        
        return "\n".join(environmental_factors[:3]) if environmental_factors else "• Environmental trigger analysis pending Session 1"
    
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
    
    def _analyze_family_loyalty_patterns(self, responses):
        """Analyze family loyalty patterns from responses"""
        loyalty_patterns = []
        
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            question_text = str(response_data.get('question_text', '')).lower()
            
            if any(keyword in question_text for keyword in ['family', 'disappoint', 'expectations', 'loyalty']):
                if any(loyalty_word in response_text for loyalty_word in ['family', 'loyal', 'betray', 'disappoint', 'honor']):
                    loyalty_patterns.append(f"• {response_data.get('response', '')[:80]}...")
        
        return "\n".join(loyalty_patterns[:3]) if loyalty_patterns else "Family loyalty analysis requires Session 1 exploration"
    
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
• Test chain accuracy with recent examples
"""
        else:
            return """
COMPLETE CHAIN MAPPING NEEDED:
• Map complete trigger → response → consequence sequence
• Identify environmental and internal triggers
• Document physiological response patterns
• Capture automatic thought sequences
• Map emotional progression and intensity
• Document behavioral choices and patterns
• Analyze short and long-term consequences
"""
    
    def _generate_pattern_specific_considerations(self, pattern_id):
        """Generate pattern-specific considerations for Session 1"""
        considerations = {
            1: "• Use gentle, permission-based language\n• Avoid overwhelming positivity\n• Normalize protective function of pattern\n• Address happiness = danger beliefs",
            2: "• Use collaborative rather than directive approach\n• Avoid authority-based language\n• Honor client's need for control\n• Frame therapy as partnership",
            3: "• Build trust gradually with transparency\n• Explain all techniques before using\n• Respect client's pace and boundaries\n• Avoid pressure to 'let go' or 'trust'"
        }
        return considerations.get(int(pattern_id), "• Use individualized approach based on pattern characteristics\n• Respect client's protective mechanisms\n• Build alliance before intervention")
    
    def _generate_core_transformation_protocol(self, pattern_id, trigger_chain):
        """Generate core transformation protocol for Session 2"""
        transformation_protocols = {
            1: """
UNHAPPINESS PATTERN TRANSFORMATION:
• Install permission for positive states with safety anchoring
• Reframe happiness as honoring family love and support
• Create positive state tolerance through graduated exposure
• Install "I can be happy AND stay connected" identity integration
• Anchor joy as natural birthright rather than earned privilege
""",
            2: """
POWER STRUGGLE TRANSFORMATION:
• Install collaborative strength identity
• Reframe cooperation as ultimate power expression
• Create win-win scenario templates
• Install "I can be strong AND cooperative" integration
• Anchor personal power that includes rather than dominates
""",
            3: """
MISTRUST PATTERN TRANSFORMATION:
• Install selective trust wisdom rather than blanket mistrust
• Create trust gradation skills (not all-or-nothing)
• Reframe trust as honoring own discernment ability
• Install "I can be wise AND open when appropriate" integration
• Anchor trust as strength rather than vulnerability
"""
        }
        
        return transformation_protocols.get(int(pattern_id), """
PATTERN-SPECIFIC TRANSFORMATION:
• Interrupt pattern at neurological level
• Install alternative response patterns
• Integrate new identity across contexts
• Anchor sustainable transformation
• Test new patterns in imagined scenarios
""")
    
    def _generate_hypnotic_techniques_for_pattern(self, pattern_id):
        """Generate specific hypnotic techniques for pattern"""
        techniques = {
            1: "• Permission-based induction with safety anchoring\n• Positive state installation with family love connection\n• Happiness tolerance building through gentle exposure\n• Joy anchoring as natural birthright",
            2: "• Collaborative induction with shared control\n• Strength reframing from domination to inclusion\n• Win-win scenario installation\n• Power anchoring through cooperation",
            3: "• Transparent induction with full explanation\n• Gradual trust building with safety maintenance\n• Selective trust wisdom installation\n• Trust anchoring as discernment strength"
        }
        return techniques.get(int(pattern_id), "• Pattern-specific techniques based on assessment findings\n• Individualized approach honoring client's protective mechanisms\n• Integration of new patterns with existing strengths")
    
    def _generate_intervention_tools(self, pattern_id, trigger_chain):
        """Generate specific intervention tools"""
        tools = []
        
        if 'physical_response' in trigger_chain:
            tools.append("• Somatic intervention techniques for body-based pattern interruption")
        
        if 'automatic_thought' in trigger_chain:
            tools.append("• Cognitive reframing tools for thought pattern modification")
        
        if 'emotional_response' in trigger_chain:
            tools.append("• Emotional regulation anchoring for feeling state management")
        
        # Pattern-specific tools
        pattern_tools = {
            1: "• Joy permission installation tools\n• Positive state anchoring techniques\n• Family connection + happiness integration",
            2: "• Collaborative strength tools\n• Win-win scenario creation\n• Power-sharing techniques",
            3: "• Trust gradation tools\n• Safety-first trust building\n• Discernment enhancement techniques"
        }
        
        if int(pattern_id) in pattern_tools:
            tools.append(pattern_tools[int(pattern_id)])
        
        return "\n".join(tools) if tools else "• Standard hypnotherapy intervention tools\n• Pattern-specific modifications based on assessment"
    
    def _generate_transformation_considerations(self, pattern_id, contact_info):
        """Generate transformation considerations"""
        urgency = contact_info.get('urgency', '').lower()
        
        considerations = []
        
        if 'urgent' in urgency:
            considerations.append("• Urgency consideration: May need longer sessions or accelerated approach")
        
        # Pattern-specific considerations
        pattern_considerations = {
            1: "• Resistance to positive suggestions likely - use permission-based approach",
            2: "• Resistance to directive language - maintain collaborative stance throughout",
            3: "• Trust building essential - transparency and client control paramount"
        }
        
        if int(pattern_id) in pattern_considerations:
            considerations.append(pattern_considerations[int(pattern_id)])
        
        considerations.append("• Monitor client response and adjust approach as needed")
        considerations.append("• Respect protective function of patterns while installing alternatives")
        
        return "\n".join(considerations)
    
    def _extract_client_language_patterns(self, responses):
        """Extract client's exact language patterns for mirroring"""
        language_patterns = []
        
        # Look for key descriptive responses
        for response_data in responses.values():
            response_text = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            if isinstance(response_text, str) and len(response_text) > 20:
                # Extract responses to key questions
                if any(keyword in question_text.lower() for keyword in ['behavior', 'feeling', 'thought', 'situation']):
                    language_patterns.append(f"• \"{response_text[:80]}...\"")
        
        return "\n".join(language_patterns[:5]) if language_patterns else "Client language patterns require Session 1 exploration"
    
    def _generate_therapeutic_reframes(self, responses, pattern_id):
        """Generate therapeutic reframes for client's language"""
        reframes = []
        
        # Pattern-specific reframe templates
        reframe_templates = {
            1: "Reframe negative language to permission language: '{negative}' → 'You have permission to {positive}'",
            2: "Reframe struggle language to choice language: '{struggle}' → 'You can choose {cooperation}'", 
            3: "Reframe danger language to wisdom language: '{danger}' → 'Your wisdom guides you to {safety}'"
        }
        
        if int(pattern_id) in reframe_templates:
            reframes.append(reframe_templates[int(pattern_id)])
        
        # Look for specific language to reframe
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            
            if any(negative in response_text for negative in ['can\'t', 'never', 'always', 'impossible']):
                reframes.append(f"• Reframe absolute language to possibility language")
                break
        
        return "\n".join(reframes) if reframes else "Therapeutic reframes will be developed based on Session 1 language exploration"
    
    def _recommend_induction_style(self, pattern_scores, responses):
        """Recommend induction style based on patterns"""
        if not pattern_scores:
            return "Induction style recommendation requires pattern identification"
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        
        induction_recommendations = {
            1: "GENTLE PERMISSION-BASED: Use 'when you're ready' and 'if it feels right' language throughout",
            2: "COLLABORATIVE SHARED CONTROL: Client maintains awareness and choice throughout process",
            3: "TRANSPARENT EXPLANATORY: Explain each step before proceeding, maintain client control",
            4: "INTEGRATION-FOCUSED: Both/and language, multiple pathway options",
            5: "BEING-CENTERED: Focus on present moment awareness rather than achievement",
            6: "AUTHENTIC CONSISTENCY: Same approach regardless of context or setting",
            7: "BALANCED CARE: Include self-care as part of service to others",
            8: "PERSONAL TRUTH HONORING: Honor family while supporting individual path",
            9: "CONSISTENT STRENGTH: Same strength available regardless of context"
        }
        
        return induction_recommendations.get(int(dominant_pattern), "INDIVIDUALIZED: Adapt based on client response and pattern characteristics")
    
    def _format_complete_response_transcript(self, assessment_responses, intensity_responses):
        """Format complete response transcript for clinical reference"""
        if not assessment_responses:
            return "No response transcript available"
        
        transcript = """
COMPLETE CLIENT RESPONSE TRANSCRIPT:
(For clinical reference and therapeutic planning)

"""
        
        # Sort responses by question ID
        for q_id in sorted(assessment_responses.keys()):
            response_data = assessment_responses[q_id]
            question_text = response_data.get('question_text', f'Question {q_id}')
            response = response_data.get('response', 'No response')
            intensity = intensity_responses.get(q_id)
            timestamp = response_data.get('timestamp', 'Unknown time')
            phase = response_data.get('phase', 'Unknown phase')
            
            transcript += f"""
Q{q_id} [{phase.upper()}]: {question_text}
Response: {response}"""
            
            if intensity:
                transcript += f"""
Intensity: {intensity}/7 ({self._get_intensity_label(intensity)})"""
            
            transcript += f"""
Timestamp: {timestamp}
{'─' * 80}
"""
        
        return transcript
    
    def _get_intensity_label(self, intensity):
        """Get intensity label for numerical rating"""
        labels = {
            1: "Very Mild", 2: "Mild", 3: "Moderate-Low", 4: "Moderate", 
            5: "Moderate-High", 6: "High", 7: "Very High"
        }
        return labels.get(intensity, "Unknown")
    
    def _generate_success_tracking_protocol(self, pattern_scores, contact_info):
        """Generate success tracking and follow-up protocol"""
        if not pattern_scores:
            return """
SUCCESS TRACKING PROTOCOL:

📊 SESSION 1 SUCCESS INDICATORS:
• Client reports feeling understood and validated
• Complete behavioral chain mapping achieved
• Pattern origins and functions identified
• Strong therapeutic alliance established
• Client expresses readiness for transformation

📊 SESSION 2 SUCCESS INDICATORS:
• Reduced intensity of pattern activation
• Natural alternative responses in trigger situations
• Increased sense of authentic identity
• Sustained motivation without conscious effort
• Client reports feeling fundamentally different

📅 FOLLOW-UP PROTOCOL:
• 1 week post-Session 2: Brief check-in call or email
• 1 month post-completion: Transformation maintenance assessment
• 3 months post-completion: Long-term success evaluation
• Optional Session 3 if reinforcement needed
"""
        
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_structures.get(int(dominant_pattern), {})
        
        success_protocol = f"""
SUCCESS TRACKING PROTOCOL:

🎯 PATTERN-SPECIFIC SUCCESS INDICATORS:

PRIMARY PATTERN ({pattern_info.get('name', f'Pattern {dominant_pattern}')}):
• BEFORE: {pattern_info.get('core_belief', 'Pattern-driven behavior')}
• AFTER: {pattern_info.get('intervention_strategy', 'Transformed response')}

📊 SESSION 1 SUCCESS MARKERS:
• Client validates assessment accuracy: "Yes, this is exactly how I experience it"
• Pattern function clarity: "I understand why this pattern developed"
• Behavioral chain completion: All trigger → response → consequence mapped
• Alliance strength: Client feels heard, understood, and hopeful
• Change readiness: "I'm ready to let this pattern transform"

📊 SESSION 2 SUCCESS MARKERS:
• Immediate shift: "Something feels fundamentally different"
• Natural responses: New behaviors emerge without conscious effort
• Identity integration: "This feels like who I really am"
• Reduced activation: Old triggers no longer create same intensity
• Future confidence: "I can handle situations that used to overwhelm me"

📊 PATTERN-SPECIFIC SUCCESS INDICATORS:
{self._generate_pattern_specific_success_indicators(dominant_pattern)}

📅 FOLLOW-UP TIMELINE:
• 48-72 hours post-Session 2: "How are you experiencing the changes?"
• 1 week: "What differences are you noticing in trigger situations?"
• 2 weeks: "How integrated do the new responses feel?"
• 1 month: "What lasting changes have stabilized?"
• 3 months: "How has your overall life experience shifted?"

⚠️ REINFORCEMENT INDICATORS:
If client reports:
• Some old patterns still activating at 50%+ intensity
• New responses feel forced rather than natural
• Confidence wavers in challenging situations
• Identity integration feels incomplete
→ RECOMMEND: Optional Session 3 for reinforcement and integration

🎯 LONG-TERM SUCCESS CRITERIA:
• Pattern activation reduced by 80%+ in intensity
• New responses feel natural and automatic
• Identity feels consistent across all contexts
• Client reports sustained wellbeing and confidence
• Life goals and relationships show positive changes

📧 FOLLOW-UP COMMUNICATION TEMPLATES:
• Week 1: "How are you experiencing the shifts from our sessions?"
• Month 1: "What changes have become your new normal?"
• Month 3: "Looking back, how has your overall experience of life changed?"

🏆 CLIENT SUCCESS STORY DEVELOPMENT:
With client permission, document transformation for:
• Future client testimonials
• Therapeutic method validation
• Clinical training examples
• Success rate tracking
"""
        
        return success_protocol
    
    def _generate_pattern_specific_success_indicators(self, pattern_id):
        """Generate specific success indicators for each pattern"""
        indicators = {
            1: """
• Spontaneous moments of joy without guilt or anxiety
• Positive events accepted without searching for problems
• Natural celebration of achievements and good news
• Comfort with others' happiness and success
• Future optimism feels safe and natural
""",
            2: """
• Conflicts resolved through collaboration rather than domination
• Comfortable with others having different opinions
• Natural win-win thinking in challenging situations
• Strength expressed through inclusion rather than exclusion
• Relaxed jaw and shoulders in disagreement situations
""",
            3: """
• Selective trust based on evidence rather than blanket mistrust
• Comfortable vulnerability in appropriate relationships
• Kindness from others accepted without suspicion
• Trust decisions feel wise rather than naive
• Heart feels open while maintaining appropriate boundaries
"""
        }
        return indicators.get(int(pattern_id), "• Pattern-specific indicators to be developed based on identified patterns")

    # ================== ORIGINAL EMAIL FORMATTING METHODS (UNCHANGED) ==================
    
    def _send_email(self, msg):
        """Send email via Gmail SMTP - ORIGINAL METHOD"""
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
    
    def _format_discovery_email_body(self, data):
        """Format discovery call email body - ORIGINAL METHOD"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
🔔 NEW DISCOVERY CALL BOOKING REQUEST
Received: {timestamp}

═══════════════════════════════════════

👤 CONTACT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}

🎯 CONCERN DETAILS:
Primary Concern: {data.get('concern', 'Not specified')}
Description: {data.get('concern_description', 'Not provided')}

📋 ADDITIONAL INFORMATION:
Urgency Level: {data.get('urgency', 'Not specified')}
Previous Experience: {data.get('experience', 'Not specified')}
Preferred Contact: {data.get('contact_method', 'Not specified')}

💬 ADDITIONAL MESSAGE:
{data.get('message', 'None provided')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
Please contact this person within 24 hours to schedule their discovery call.

📞 Next Steps:
1. Send confirmation email to client
2. Schedule discovery call via Calendly
3. Prepare personalized approach based on their concerns

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic
Automated Booking System
        """
    
    def _format_package_email_body(self, data):
        """Format package booking email body - ORIGINAL METHOD"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
💰 NEW TRANSFORMATION PACKAGE BOOKING
Received: {timestamp}

═══════════════════════════════════════

👤 CONTACT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}

🎯 PACKAGE DETAILS:
Selected Package: {data.get('package_type', 'Not specified')}
Primary Concern: {data.get('concern', 'Not specified')}
Previous Experience: {data.get('experience', 'Not specified')}

💬 CLIENT MESSAGE:
{data.get('message', 'None provided')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
High-priority booking - client ready to proceed with transformation package.

📞 Next Steps:
1. Send welcome email with package details
2. Schedule Session 1 via Calendly
3. Send pre-session preparation materials
4. Confirm payment method and schedule

💰 Package Value: 3,000-4,000 THB

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic
Automated Booking System
        """
    
    def _format_fallback_clinical_email(self, data, error):
        """Fallback clinical email format preserving all data"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        contact_info = data.get('contact_info', {})
        name = contact_info.get('name', 'Not provided')
        email = contact_info.get('email', 'Not provided')
        urgency = contact_info.get('urgency', 'Not specified')
        
        return f"""
🧠 CLINICAL ASSESSMENT - DATA PRESERVATION MODE
Generated: {timestamp}

ERROR HANDLING: Complete data preservation due to: {str(error)}

═══════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}
Urgency Level: {urgency}
Assessment Date: {timestamp}

⚡ PRIORITY CONTACT REQUIRED:
Contact {email} within 24 hours for assessment follow-up

═══════════════════════════════════════
🔍 COMPLETE ASSESSMENT DATA
═══════════════════════════════════════

{json.dumps(data, indent=2, default=str)}

═══════════════════════════════════════

📞 MANUAL REVIEW PROTOCOL:
1. Contact client immediately for assessment validation
2. Schedule discovery call to review findings
3. Prepare pattern-specific therapeutic approach
4. Consider urgency level in session scheduling

All assessment data preserved above for complete clinical analysis.

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Complete Data Preservation Mode
        """


# ================== GLOBAL INSTANCES AND FUNCTIONS (MAINTAINS COMPATIBILITY) ==================

# Global instance for easy import - MAINTAINS ORIGINAL STRUCTURE
email_handler = EmailHandler()

def send_discovery_call_email(booking_data):
    """Send discovery call booking email - ORIGINAL FUNCTION SIGNATURE"""
    return email_handler.send_discovery_call_email(booking_data)

def send_package_booking_email(booking_data):
    """Send package booking email - ORIGINAL FUNCTION SIGNATURE"""
    return email_handler.send_package_booking_email(booking_data)

def send_clinical_assessment_results(assessment_data):
    """Send clinical assessment results email - NEW FUNCTION FOR assess.py"""
    return email_handler.send_clinical_assessment_results(assessment_data)

# ================== BACKWARD COMPATIBILITY FUNCTIONS ==================

def send_booking_email(name, email, concern, message, booking_type):
    """Backward compatibility for standard booking - ORIGINAL FUNCTION"""
    booking_data = {
        'name': name,
        'email': email,
        'concern': concern,
        'message': message
    }
    
    if 'discovery' in booking_type.lower():
        return send_discovery_call_email(booking_data)
    else:
        return send_package_booking_email(booking_data)

def send_assessment_results_email(data):
    """Backward compatibility for assessment results"""
    return send_clinical_assessment_results(data)

def send_contact_form_email(data):
    """Backward compatibility for contact forms"""
    return send_discovery_call_email(data)

def send_booking_confirmation_email(data):
    """Backward compatibility for booking confirmations"""
    return send_discovery_call_email(data)
