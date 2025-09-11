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
Complete working email handler utility for sending booking notifications via Gmail SMTP
Full script with all original functionality + assessment capabilities
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

class EmailHandler:
    """Handle email sending for booking notifications with clinical assessment capabilities"""
    
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
    
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification - maintains original functionality"""
        try:
            print(f"[DEBUG] send_discovery_call_email called with data keys: {list(booking_data.keys())}")
            print(f"[DEBUG] Form type: {booking_data.get('form_type', 'Not specified')}")
            
            # Check if this is assessment data - improved detection
            form_type = str(booking_data.get('form_type', '')).lower()
            is_assessment = any([
                'behavioral pattern assessment' in form_type,
                'complete behavioral' in form_type,
                'assessment' in form_type and 'behavioral' in form_type,
                'assessment_scores' in booking_data,
                'raw_responses' in booking_data and isinstance(booking_data.get('raw_responses'), dict) and len(booking_data.get('raw_responses', {})) > 10
            ])
            
            if is_assessment:
                print("[DEBUG] Detected assessment data, routing to assessment handler")
                return self.send_assessment_results_email(booking_data)
            else:
                print("[DEBUG] Regular discovery call booking")
                # Create message for regular discovery call
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
                    # Log the booking data for debugging
                    print(f"Discovery Call Booking: {booking_data}")
                    return True  # Simulate success when no password is configured
                    
        except Exception as e:
            print(f"[ERROR] Exception in send_discovery_call_email: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def send_package_booking_email(self, booking_data):
        """Send package booking notification - original functionality"""
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
    
    def send_assessment_results_email(self, assessment_data):
        """Send comprehensive clinical assessment results email"""
        try:
            print("[DEBUG] Sending clinical assessment results email")
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "🧠 CLINICAL ASSESSMENT RESULTS - Comprehensive Analysis"
            
            # Format the comprehensive clinical email body
            body = self._format_assessment_results_body(assessment_data)
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email if password is available
            if self.password:
                result = self._send_email(msg)
                print(f"[DEBUG] Clinical assessment email sent: {result}")
                return result
            else:
                # Log the assessment data for debugging
                print(f"Clinical Assessment Results: {assessment_data}")
                return True  # Simulate success when no password is configured
                
        except Exception as e:
            print(f"[ERROR] Exception in send_assessment_results_email: {e}")
            import traceback
            traceback.print_exc()
            return False
    
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
    
    def _format_discovery_email_body(self, data):
        """Format discovery call email body - original method"""
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
        """Format package booking email body - original method"""
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
    
    def _format_assessment_results_body(self, data):
        """Format comprehensive clinical assessment with error handling"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Safely extract core data
            name = data.get('name', 'Not provided')
            email = data.get('email', 'Not provided')
            concern = data.get('concern', 'Not specified')
            
            # Handle assessment data safely
            assessment_scores = data.get('assessment_scores', {})
            raw_responses = data.get('raw_responses', {})
            clinical_insights = data.get('clinical_insights', {})
            
            # Safe type checking
            if not isinstance(assessment_scores, dict):
                assessment_scores = {}
            if not isinstance(raw_responses, dict):
                raw_responses = {}
            if not isinstance(clinical_insights, dict):
                clinical_insights = {}
            
            # Extract key scores safely
            readiness_score = assessment_scores.get('readiness_score', 'Not calculated')
            pattern_scores = assessment_scores.get('pattern_scores', {})
            
            # Start building comprehensive email
            email_body = f"""
🧠 COMPREHENSIVE CLINICAL ASSESSMENT ANALYSIS
Generated: {timestamp}

═══════════════════════════════════════════════════════════════
CLIENT PROFILE & ASSESSMENT SUMMARY
═══════════════════════════════════════════════════════════════

👤 CLIENT DETAILS:
Name: {name}
Email: {email}
Primary Concern: {concern}
Assessment Date: {timestamp}
Completion Status: {data.get('completion_rate', '100%')}
Total Questions: {data.get('total_questions', 'Complete')}

🎯 TRANSFORMATION READINESS SCORE: {readiness_score}

═══════════════════════════════════════════════════════════════
📊 BEHAVIORAL PATTERN ANALYSIS
═══════════════════════════════════════════════════════════════
"""
            
            # Add pattern analysis
            if isinstance(pattern_scores, dict) and pattern_scores:
                email_body += "\n🔍 IDENTIFIED BEHAVIORAL PATTERNS:\n"
                high_patterns = []
                medium_patterns = []
                for pattern, score in pattern_scores.items():
                    if isinstance(score, (int, float)):
                        if score > 70:
                            high_patterns.append(f"{pattern}: {score}%")
                        elif score > 40:
                            medium_patterns.append(f"{pattern}: {score}%")
                
                if high_patterns:
                    email_body += "🔴 HIGH INTENSITY PATTERNS (Priority for Session 1):\n"
                    for pattern in high_patterns:
                        email_body += f"   • {pattern}\n"
                
                if medium_patterns:
                    email_body += "\n🟡 MODERATE PATTERNS (Session 2 targets):\n"
                    for pattern in medium_patterns:
                        email_body += f"   • {pattern}\n"
            
            # Add behavioral chain analysis
            email_body += self._analyze_behavioral_chains(raw_responses)
            
            # Add clinical insights
            if clinical_insights:
                email_body += "\n\n💡 CLINICAL INSIGHTS:\n"
                for insight_type, insight_data in clinical_insights.items():
                    email_body += f"• {insight_type}: {str(insight_data)[:200]}\n"
            
            # Add session recommendations
            email_body += self._generate_session_recommendations(readiness_score, pattern_scores, concern)
            
            # Add intervention strategies
            email_body += self._generate_intervention_strategies(pattern_scores, readiness_score)
            
            # Add contact protocol
            email_body += self._generate_contact_protocol(readiness_score, email, concern)
            
            # Add raw data for clinical reference
            if raw_responses:
                email_body += f"""

═══════════════════════════════════════════════════════════════
📋 RAW ASSESSMENT DATA (Clinical Reference)
═══════════════════════════════════════════════════════════════

Assessment Scores Summary:
{json.dumps(assessment_scores, indent=2)[:1000]}

Key Response Patterns:
{self._extract_key_responses(raw_responses)}

═══════════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Clinical Assessment System
Comprehensive Analysis Complete - Ready for Client Contact
"""
            
            return email_body
            
        except Exception as e:
            # Fallback to simple format
            return self._format_assessment_fallback(data, e)
    
    def _analyze_behavioral_chains(self, responses):
        """Analyze behavioral chains from responses"""
        if not responses:
            return "\n\n🔗 BEHAVIORAL CHAIN ANALYSIS:\nRequires Session 1 exploration for complete mapping."
        
        chain_analysis = "\n\n🔗 BEHAVIORAL CHAIN ANALYSIS:\n"
        
        # Extract triggers
        triggers = [v for k, v in responses.items() if isinstance(v, str) and any(word in k.lower() for word in ['trigger', 'situation', 'when'])]
        if triggers:
            chain_analysis += f"┌─ TRIGGERS: {triggers[0][:100]}...\n"
        else:
            chain_analysis += "┌─ TRIGGERS: Needs Session 1 exploration\n"
        
        # Extract emotions
        emotions = [v for k, v in responses.items() if isinstance(v, str) and any(word in k.lower() for word in ['feel', 'emotion', 'mood'])]
        if emotions:
            chain_analysis += f"├─ EMOTIONS: {emotions[0][:100]}...\n"
        else:
            chain_analysis += "├─ EMOTIONS: Requires emotional mapping\n"
        
        # Extract behaviors
        behaviors = [v for k, v in responses.items() if isinstance(v, str) and any(word in k.lower() for word in ['do', 'behavior', 'action'])]
        if behaviors:
            chain_analysis += f"└─ BEHAVIORS: {behaviors[0][:100]}...\n"
        else:
            chain_analysis += "└─ BEHAVIORS: Needs behavioral tracking\n"
        
        chain_analysis += "\n🎯 INTERVENTION POINTS:\n"
        chain_analysis += "   • Trigger interruption strategies ready\n"
        chain_analysis += "   • Emotional regulation techniques prepared\n"
        chain_analysis += "   • Behavioral pattern modification planned\n"
        
        return chain_analysis
    
    def _generate_session_recommendations(self, readiness_score, pattern_scores, concern):
        """Generate specific session recommendations"""
        recommendations = f"""

═══════════════════════════════════════════════════════════════
🎭 SESSION PROTOCOL RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

📋 SESSION 1 PROTOCOL - Pattern Analysis & Initial Programming:
1. Establish rapport using client's natural language patterns
2. Deep exploration of '{concern}' behavioral sequences
3. Map complete trigger → response → consequence chains
4. Identify resistance patterns and protective functions
5. Install initial positive programming for immediate relief

📋 SESSION 2 PROTOCOL - Transformation & Integration:"""
        
        if isinstance(readiness_score, (int, float)) and readiness_score > 70:
            recommendations += """
1. Direct hypnotic intervention (high readiness detected)
2. Pattern interruption at identified trigger points
3. Install new behavioral patterns using client's values
4. Identity integration work with future progression
5. Anchor success states and positive associations"""
        else:
            recommendations += """
1. Gentle hypnotic approach (building readiness first)
2. Permission-based pattern modification
3. Gradual behavioral change with client control
4. Resistance honoring and gradual transformation
5. Success state development with safety protocols"""
        
        # Add timing recommendations
        recommendations += f"""

⏰ TIMING RECOMMENDATIONS:
• Session 1: 90 minutes (60% analysis, 40% initial programming)
• Gap between sessions: 1-2 weeks for integration
• Session 2: 90 minutes (20% review, 80% transformation)
• Follow-up: 30-day email check-in recommended"""
        
        return recommendations
    
    def _generate_intervention_strategies(self, pattern_scores, readiness_score):
        """Generate specific intervention strategies"""
        strategies = f"""

═══════════════════════════════════════════════════════════════
🎯 SPECIFIC INTERVENTION STRATEGIES
═══════════════════════════════════════════════════════════════

🔧 HYPNOTHERAPY TECHNIQUES TO DEPLOY:"""
        
        if isinstance(pattern_scores, dict) and pattern_scores:
            high_patterns = [p for p, s in pattern_scores.items() if isinstance(s, (int, float)) and s > 70]
            if high_patterns:
                strategies += f"""
• DIRECT INTERVENTION for high-intensity patterns: {', '.join(high_patterns)}
• Pattern interruption and immediate replacement protocols
• Intensive hypnotic programming with safety protocols
• Somatic anchoring for rapid neural pathway changes"""
            else:
                strategies += """
• SUPPORTIVE APPROACH for moderate-intensity patterns
• Gradual pattern modification with client permission
• Resource building and confidence enhancement
• Gentle hypnotic suggestion with positive reinforcement"""
        
        strategies += f"""

🎨 SPECIFIC HYPNOTIC APPROACHES:
• Analytical hypnotherapy for deep pattern exploration
• Direct suggestion using client's exact language patterns
• Metaphorical reframing aligned with client's values
• Somatic experiencing for body-based pattern shifts
• Timeline therapy for pattern origin resolution

✅ SUCCESS INDICATORS TO MONITOR:
• Immediate: Reduced anxiety about the change process
• Week 1: Decreased intensity of old trigger responses
• Week 2: Natural adoption of new behavioral patterns
• Month 1: Sustained change without conscious effort
• Month 3: Complete integration and identity shift"""
        
        return strategies
    
    def _generate_contact_protocol(self, readiness_score, email, concern):
        """Generate contact protocol for therapist"""
        # Determine priority level
        if isinstance(readiness_score, (int, float)):
            if readiness_score > 80:
                priority = "🚨 HIGH PRIORITY - Ready for immediate intervention"
                urgency = "Contact within 12 hours"
            elif readiness_score > 60:
                priority = "🟡 MEDIUM PRIORITY - Good candidate with preparation"
                urgency = "Contact within 24 hours"
            else:
                priority = "🟢 STANDARD PRIORITY - Requires readiness building"
                urgency = "Contact within 48 hours"
        else:
            priority = "📋 ASSESSMENT PRIORITY - Further evaluation needed"
            urgency = "Contact within 24 hours for clarification"
        
        protocol = f"""

═══════════════════════════════════════════════════════════════
⚡ IMMEDIATE CONTACT PROTOCOL
═══════════════════════════════════════════════════════════════

{priority}

📞 CONTACT INSTRUCTIONS:
• {urgency}
• Email: {email}
• Reference: Comprehensive behavioral assessment completed
• Focus: '{concern}' transformation using 2-session method

🎯 DISCOVERY CALL AGENDA:
1. Acknowledge assessment completion and insights discovered
2. Confirm key patterns identified match client's experience
3. Explain personalized 2-session transformation approach
4. Address any questions about hypnotherapy process
5. Schedule Session 1 if client is ready to proceed

💼 SESSION 1 PREPARATION REQUIRED:
• Review complete pattern analysis above
• Prepare client-specific analytical questions
• Ready intervention strategies for identified patterns
• Have resistance management protocols prepared

📧 EMAIL TEMPLATE FOR CLIENT CONTACT:
"Hi [Name], Thank you for completing our comprehensive behavioral assessment. 
The results show clear pathways for rapid transformation of your [concern] using 
our proven 2-session method. I'd love to discuss your personalized approach in 
a brief discovery call. When would be a good time to connect?"

═══════════════════════════════════════════════════════════════"""
        
        return protocol
    
    def _extract_key_responses(self, responses):
        """Extract key responses for clinical reference"""
        if not responses:
            return "No detailed responses recorded."
        
        key_responses = []
        response_count = 0
        
        for key, value in responses.items():
            if isinstance(value, str) and len(value) > 20 and response_count < 5:
                key_responses.append(f"• {key}: {value[:150]}...")
                response_count += 1
        
        return '\n'.join(key_responses) if key_responses else "Responses require manual review."
    
    def _format_assessment_fallback(self, data, error):
        """Fallback format if main processing fails"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
🧠 CLINICAL ASSESSMENT RESULTS - SAFE MODE
Generated: {timestamp}

PROCESSING NOTE: Using simplified format due to: {str(error)}

═══════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}
Primary Concern: {data.get('concern', 'Not specified')}
Assessment Date: {timestamp}

📊 ASSESSMENT DATA SUMMARY:
Readiness Score: {data.get('assessment_scores', {}).get('readiness_score', 'Not calculated')}
Total Questions: {data.get('total_questions', 'Unknown')}
Completion Rate: {data.get('completion_rate', 'Unknown')}

🔍 RAW DATA (First 1000 characters):
{str(data)[:1000]}...

═══════════════════════════════════════

⚡ IMMEDIATE ACTION REQUIRED:
1. Contact client within 24 hours: {data.get('email', 'Email not provided')}
2. Conduct discovery call to gather additional insights
3. Manual review of assessment data recommended
4. Prepare standard 2-session approach for '{data.get('concern', 'stated concern')}'

📞 CONTACT PRIORITY: Standard - Discovery call recommended

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Safe Mode Processing
        """

# Global instance for easy import - MAINTAINS ORIGINAL STRUCTURE
email_handler = EmailHandler()

def send_discovery_call_email(booking_data):
    """Send discovery call booking email - ORIGINAL FUNCTION SIGNATURE"""
    return email_handler.send_discovery_call_email(booking_data)

def send_package_booking_email(booking_data):
    """Send package booking email - ORIGINAL FUNCTION SIGNATURE"""
    return email_handler.send_package_booking_email(booking_data)

def send_assessment_results_email(assessment_data):
    """Send assessment results email - NEW FUNCTION FOR ASSESSMENTS"""
    return email_handler.send_assessment_results_email(assessment_data)
