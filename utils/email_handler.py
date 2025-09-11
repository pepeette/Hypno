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






import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class ComprehensiveEmailHandler:
    """Complete email handler for all website needs, with enhanced assessment email."""

    def __init__(self):
        # SMTP setup: Gmail as default
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        try:
            import streamlit as st
            self.sender_email = st.secrets.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        except:
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD", "")

        self.pattern_descriptions = {
            1: "Unhappiness Culture - Difficulty maintaining positive states",
            2: "Power Struggles - Recurring conflicts and control issues",
            3: "Systematic Mistrust - Skepticism and trust difficulties",
            4: "Separation/Division - Black-and-white thinking",
            5: "Doing vs Being - Self-worth tied to achievement",
            6: "Compartmentalized Authenticity - Inconsistent identity",
            7: "Self-Sacrifice - Prioritizing others over self-care",
            8: "Inherited Missions - Life goals shaped by family expectations",
            9: "Contextual Weakness - Loss of boundaries situationally"
        }

    # -- Assessment Email Handling --

    def send_clinical_assessment_results(self, assessment_data):
        """Compose and send the clinical assessment email, returns True on success."""
        try:
            if not assessment_data.get('contact_info'):
                print("[ERROR] Missing contact_info in assessment data")
                return False
            
            results = assessment_data.get('assessment_results', {})
            pattern_scores = results.get('pattern_scores', {}) or assessment_data.get('pattern_scores', {})
            if not results and not pattern_scores:
                print("[ERROR] Missing assessment results or pattern scores")
                return False
            
            urgency = assessment_data['contact_info'].get('urgency', '')
            risk_flags = results.get('risk_flags', []) or assessment_data.get('risk_flags', [])
            priority_flag = self._get_priority_flag(urgency, risk_flags)
            subject = f"{priority_flag} Clinical Assessment - {assessment_data['contact_info'].get('name', 'Client')}"

            body = self._format_clinical_email_body(assessment_data)
            if not body or len(body) < 100:
                print("[ERROR] Email body is empty or too short")
                return False
            
            return self._send_email(subject, body, "Clinical Assessment")

        except Exception as e:
            import traceback
            print(f"[ERROR] Exception sending clinical assessment email: {e}")
            print(traceback.format_exc())
            return False

    def _format_clinical_email_body(self, data):
        """Generates detailed assessment email text from data dict."""
        try:
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            contact = data.get('contact_info', {})
            results = data.get('assessment_results', {})
            responses = data.get('assessment_responses', {})
            intensity = data.get('intensity_responses', {})
            chain = data.get('trigger_chain', {})
            phase_completion = results.get('phase_completion', {})
            triggered = results.get('triggered_patterns', [])
            risk_flags = results.get('risk_flags', []) or data.get('risk_flags', [])
            adaptive_paths = results.get('adaptive_paths', []) or data.get('adaptive_triggered', [])

            name = contact.get('name', 'Unknown')
            email = contact.get('email', 'Unknown')
            phone = contact.get('phone', 'Not provided')
            urgency = contact.get('urgency', 'Not specified')
            primary_concern = contact.get('primary_concern', 'Not provided')
            next_step = contact.get('next_step', 'Not specified')
            pattern_scores = results.get('pattern_scores', {}) or data.get('pattern_scores', {})
            completion = results.get('completion_rate', 0) * 100
            total_questions = results.get('total_questions_answered', 0)
            dominant_pattern = results.get('dominant_pattern', None)

            body = f"""
🧠 COMPREHENSIVE BEHAVIORAL ASSESSMENT REPORT
Date: {ts}
Priority: {self._get_clinical_priority(urgency, risk_flags)}

--- PATIENT INFO ---
Name: {name}
Email: {email}
Phone: {phone}
Urgency Level: {urgency}
Primary Concern: {primary_concern}
Preferred Next Step: {next_step}

Completion: {completion:.1f}% ({total_questions} questions answered)
Adaptive Paths Triggered: {len(adaptive_paths)}

--- PHASE COMPLETION ---
Engagement: {phase_completion.get('engagement', 'N/A')} questions
Trigger Mapping: {phase_completion.get('trigger_mapping', 'N/A')}
Pattern Specific: {phase_completion.get('pattern_specific', 'N/A')}
Integration: {phase_completion.get('integration', 'N/A')}

--- BEHAVIORAL PATTERNS IDENTIFIED ---
"""
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            for i, (pid, score) in enumerate(sorted_patterns[:5]):
                desc = self.pattern_descriptions.get(pid, f"Pattern {pid}")
                intensity_lbl = self._score_to_intensity(score)
                rank = "DOMINANT" if i == 0 else f"Secondary #{i}"
                triggered_lbl = "TRIGGERED" if pid in triggered else "DETECTED"
                body += f"{rank}: {desc} ({triggered_lbl})\n"
                body += f"  Score: {score:.2f} ({intensity_lbl} intensity)\n"
                body += f"  Clinical Note: {self._pattern_clinical_note(pid, score)}\n"
                body += f"  Therapy Approach: {self._pattern_therapy_approach(pid)}\n"
                body += f"  Session Priority: {self._session_priority(pid, i == 0)}\n\n"
            if len(sorted_patterns) > 5:
                body += f"... plus {len(sorted_patterns) - 5} additional patterns detected\n"

            if chain:
                body += "--- BEHAVIORAL CHAIN ---\n"
                steps = ['awareness_point','physical_response','automatic_thought','emotional_response',
                         'behavioral_response','immediate_consequence','longer_term_impact']
                for step in steps:
                    if step in chain:
                        body += f"{step.replace('_',' ').title()}: {chain[step]}\n"
                body += f"Primary Intervention: {self._primary_intervention_point(chain)}\n"
                body += f"Secondary Intervention: {self._secondary_intervention_point(chain)}\n"

            body += "\n--- RISK ASSESSMENT ---\n"
            risk_level = self._overall_risk_level(risk_flags)
            body += f"Risk Level: {risk_level}\n"
            if risk_flags:
                body += "Risk Factors & Recommended Management:\n"
                for idx, risk in enumerate(risk_flags, 1):
                    body += f"{idx}. {self._risk_description(risk)}\n"
                    body += f"   Management: {self._risk_management(risk)}\n"
            else:
                body += "No significant risk factors detected.\n"

            body += "\n--- THERAPY RECOMMENDATIONS ---\n"
            body += f"Recommended Approach: {self._therapy_recommendation(dominant_pattern, risk_flags)}\n"
            body += f"Expected Sessions: {self._expected_sessions(pattern_scores, risk_flags)}\n"
            body += f"Success Probability: {self._success_probability(completion, len(risk_flags))}\n"
            body += f"Session 1 Focus:\n{self._session_one_focus(dominant_pattern, primary_concern, chain)}\n"
            body += f"Session 2 Focus:\n{self._session_two_focus(dominant_pattern, pattern_scores)}\n"
            body += f"Potential Resistance:\n{self._resistance_factors(pattern_scores, responses)}\n"
            body += f"Hypnotherapy Protocol:\n{self._hypnotherapy_protocol(dominant_pattern, intensity, chain)}\n"

            body += "\n--- CLIENT RESPONSES (Top 8) ---\n"
            key_resps = self._extract_key_responses(responses)
            for k, v in key_resps.items():
                body += f"{k}: {v}\n"

            if intensity:
                high_intensities = {k:v for k,v in intensity.items() if v>=6}
                if high_intensities:
                    avg_inten = sum(high_intensities.values())/len(high_intensities)
                    body += f"\nHigh intensity responses: {len(high_intensities)} (avg {avg_inten:.1f}/7)\n"

            body += f"\nAdaptive Paths Triggered: {', '.join(adaptive_paths) or 'None'}\n"
            body += f"Patterns with Deep Dives: {', '.join(self.pattern_descriptions.get(p, f'Pattern {p}') for p in triggered) or 'None'}\n"

            body += "\n--- IMMEDIATE ACTION ---\n"
            body += f"Contact Timeline: {self._contact_timeline(urgency, risk_flags)}\n"
            body += f"Recommended Response: {self._response_recommendation(next_step)}\n"
            body += "Preparation Checklist:\n"
            body += f" 1. Review client data\n"
            body += f" 2. Plan session focusing on {self.pattern_descriptions.get(dominant_pattern, 'patterns')}\n"
            body += f" 3. {self._session_preparation(dominant_pattern, risk_flags)}\n"
            body += " 4. Ready environment and materials\n"
            if chain:
                body += f" 5. Target interventions at chain points: {', '.join(chain.keys())}\n"

            body += "\n--- FULL CLIENT INTERVIEW TRANSCRIPT ---\n"
            last_phase = None
            for qid in sorted(responses.keys()):
                resp = responses[qid]
                phase = resp.get('phase','')
                if phase != last_phase:
                    last_phase = phase
                    body += f"\n== {phase.upper()} Phase ==\n"
                body += f"{qid}. {resp.get('question_text', f'Question {qid}')}\n"
                body += f"   Response: {resp.get('response','')}\n"
                if qid in intensity:
                    body += f"   Intensity: {intensity[qid]}/7\n"
                body += f"   Timestamp: {resp.get('timestamp','')}\n"

            body += f"""
--- TECHNICAL AND CONFIDENTIALITY ---

Confidence Level: {self._confidence_level(completion, len(pattern_scores))}
Data Quality: {self._data_quality(responses)}
Chain Completeness: {self._chain_completeness(chain)}

Assigned Therapist: {self._assigned_therapist(urgency, risk_flags)}
Review Timing: {self._review_schedule(urgency, risk_flags)}

CONFIDENTIAL: For licensed clinical use only.
Generated by Bangkok Hypnotherapy Clinic System at {ts}
"""
            return body

        except Exception as e:
            import traceback
            print(f"[ERROR] Formatting clinical email failed: {e}")
            print(traceback.format_exc())
            return f"Error formatting clinical assessment email. Please review data manually."

    # --- Helper Methods for assessment email ---

    def _get_priority_flag(self, urgency, risks):
        if len(risks) >= 3:
            return "🔴 HIGH RISK"
        if 'extremely' in urgency.lower():
            return "🟠 URGENT"
        if 'very' in urgency.lower():
            return "🟡 PRIORITY"
        return "📋 ASSESSMENT"

    def _get_clinical_priority(self, urgency, risks):
        if len(risks) >= 3:
            return "High risk - specialized approach needed"
        if 'extremely' in urgency.lower():
            return "Urgent - contact within 24 hours"
        if 'very' in urgency.lower():
            return "Priority - contact within 48 hours"
        return "Standard priority - contact within 72 hours"

    def _score_to_intensity(self, score):
        if score >= 8:
            return "Very High"
        if score >= 6:
            return "High"
        if score >= 4:
            return "Moderate"
        if score >= 2:
            return "Low"
        return "Minimal"

    def _pattern_clinical_note(self, pid, score):
        notes = {
            1: "Blocks positive therapeutic progress, needs permission-based approach",
            2: "Tendency for resistance, collaborative therapy best",
            3: "Trust should be built prior to deep work",
            4: "Work on cognitive flexibility recommended",
            5: "Focus on decoupling worth from doing",
            6: "Integration of identities across contexts required",
            7: "Carefully reframe self-care as strength",
            8: "Address family loyalty conflicts gently",
            9: "Strengthen consistent boundary maintenance"
        }
        base = notes.get(pid, "Clinical notes not available.")
        if score >= 8:
            return "Dominant pattern: " + base
        if score >= 6:
            return "Significant pattern: " + base
        return "Supporting pattern: " + base

    def _pattern_therapy_approach(self, pid):
        therapy = {
            1: "Permission and tolerance installation",
            2: "Empowerment and collaboration",
            3: "Transparent evidence-based approach",
            4: "Facilitate ‘both/and’ cognition",
            5: "Install inherent worth separate from doing",
            6: "Strengthen authentic identity",
            7: "Balance self-care with service",
            8: "Support personal autonomy with respect",
            9: "Anchor boundary integrity"
        }
        return therapy.get(pid, "Individualized protocol")

    def _session_priority(self, pid, dominant):
        if dominant:
            priority = {
                1: "Session 1 focus on permission and acceptance",
                2: "Session 1 focus on power rebalancing",
                3: "Session 1 focus on trust-building",
                4: "Session 1 focus on cognitive expansion",
                5: "Session 1 focus on worth installation",
                6: "Session 1 focus on identity integration",
                7: "Session 1 focus on self-care installation",
                8: "Session 1 focus on autonomy support",
                9: "Session 1 focus on boundary work"
            }
            return priority.get(pid, "Session 1 priority")
        else:
            return "Secondary pattern: integration in later sessions"

    def _pattern_therapy_approach(self, pid):
        therapy = {
            1: "Permission and tolerance installation",
            2: "Empowerment and collaboration",
            3: "Transparent evidence-based approach",
            4: "Facilitate ‘both/and’ cognition",
            5: "Install inherent worth separate from doing",
            6: "Strengthen authentic identity",
            7: "Balance self-care with service",
            8: "Support personal autonomy with respect",
            9: "Anchor boundary integrity"
        }
        return therapy.get(pid, "Standard clinical approach")

    def _overall_risk_level(self, risk_flags):
        if len(risk_flags) >= 4:
            return "High risk - intensive supervision required"
        if len(risk_flags) >= 2:
            return "Elevated risk - modified protocol needed"
        if len(risk_flags) >= 1:
            return "Moderate risk - proceed with caution"
        return "Low risk - standard protocol suitable"

    def _risk_description(self, flag):
        descriptions = {
            'risk_q_10': "Ongoing medical or mental health care coordination required",
            'risk_q_11': "High emotional lability detected; clinical caution",
            'risk_q_12': "Dissociation or self-harm history; emergency plan needed",
            'risk_q_13': "Substance use concerns detected"
        }
        return descriptions.get(flag, f"Unknown risk factor: {flag}")

    def _risk_management(self, flag):
        management = {
            'risk_q_10': "Coordinate therapy with existing care providers",
            'risk_q_11': "Use grounding and emotion regulation methods",
            'risk_q_12': "Implement safety and crisis resources",
            'risk_q_13': "Address substance use prior to therapy"
        }
        return management.get(flag, "Follow clinical precautions")

    def _therapy_recommendation(self, dominant, risks):
        if len(risks) >= 2:
            return "Modified approach emphasizing safety and pacing"
        if dominant in [1,2,3]:
            return "Collaborative permission-based hypnotherapy"
        if dominant in [7,8,9]:
            return "Gentle approach facilitating boundary and self-care"
        return "Standard structured hypnotherapy"

    def _expected_sessions(self, scores, risks):
        if len(risks) >= 2:
            return "3-4 sessions recommended for complexity"
        if len(scores) >= 3:
            return "2-3 sessions for multiple patterns"
        return "2 sessions - rapid intervention"

    def _success_probability(self, completion, risk_count):
        if completion >= 90 and risk_count == 0:
            return "High (85%+ chance of success)"
        if completion >=75 and risk_count <=1:
            return "Good (70-85%)"
        if completion >=60:
            return "Moderate (55-70%)"
        return "Variable - monitor progress carefully"

    def _session_one_focus(self, dominant, concern, chain):
        base = ""
        if dominant:
            desc = self.pattern_descriptions.get(dominant, f"Pattern {dominant}")
            base = f"Focus on {desc} and initial rapport building."
        else:
            base = f"Exploratory session focusing on: {concern[:100]}"
        if chain:
            if 'automatic_thought' in chain:
                base += f"\nTarget cognitive restructuring of: {chain['automatic_thought'][:50]}..."
            elif 'physical_response' in chain:
                base += f"\nIncorporate somatic focus on: {chain['physical_response'][:50]}..."
        return base

    def _session_two_focus(self, dominant, scores):
        if dominant:
            if len(scores) > 1:
                return f"Integrate treatment of {self.pattern_descriptions.get(dominant)} with secondary patterns."
            else:
                return f"Deepen transformation of {self.pattern_descriptions.get(dominant)}."
        return "Personalized continuation based on session 1."

    def _resistance_factors(self, scores, responses):
        factors = []
        if 1 in scores:
            factors.append("Possible resistance to positive imagery.")
        if 2 in scores:
            factors.append("Potential power struggle with therapist authority.")
        if 3 in scores:
            factors.append("Need for clear information due to mistrust.")
        # Look for secondary gain text hints in responses (simplified)
        for resp in responses.values():
            text = resp.get('question_text','').lower()
            if 'secondary gain' in text or 'would lose' in text:
                factors.append("Secondary gain identified; may impede change.")
                break
        return "\n".join(factors) if factors else "No significant resistance anticipated."

    def _hypnotherapy_protocol(self, dominant, intensity, chain):
        protos = {
            1: "Gentle permission, install success tolerance.",
            2: "Empowerment and shared control induction.",
            3: "Trust-building, explain process thoroughly.",
            4: "Encourage integrative flexibility and creativity.",
            5: "Separate worth from behavior; reinforce being.",
            6: "Build authenticity and consistency.",
            7: "Install balanced self-care and boundaries.",
            8: "Honor family ties while empowering autonomy.",
            9: "Strengthen boundaries across contexts."
        }
        proto = protos.get(dominant, "Standard individualized protocol.")
        if intensity and max(intensity.values()) >= 6:
            proto += " Adjust pace for high emotional intensity."
        if chain:
            if 'physical_response' in chain:
                proto += f" Include somatic work on: {chain['physical_response'][:30]}."
            if 'automatic_thought' in chain:
                proto += f" Address cognitive frames: {chain['automatic_thought'][:40]}."
        return proto

    def _extract_key_responses(self, responses):
        keys = []
        for qid, resp in sorted(responses.items()):
            question = resp.get('question_text','').lower()
            if any(x in question for x in ['behavior', 'trigger', 'thought', 'feeling']):
                keys.append((qid, resp.get('question_text',''), resp.get('response','')))
            if len(keys) >=8:
                break
        return {f"Q{qid} {qtxt[:60]}...": rtxt[:150] for qid,qtxt,rtxt in keys}

    def _primary_intervention_point(self, chain):
        if 'automatic_thought' in chain:
            return "Focus cognitive restructuring on automatic thought."
        if 'physical_response' in chain:
            return "Intervene somatically at physical sensation."
        if 'emotional_response' in chain:
            return "Modulate emotional response emerging."
        return "Interrupt behavioral pattern where possible."

    def _secondary_intervention_point(self, chain):
        if 'behavioral_response' in chain:
            return "Modify choices at behavioral response."
        if 'immediate_consequence' in chain:
            return "Reframe immediate consequences."
        return "Alter environment or triggers."

    def _chain_completeness(self, chain):
        elements = ['awareness_point', 'physical_response', 'automatic_thought', 'emotional_response', 'behavioral_response', 'immediate_consequence']
        found = sum(1 for e in elements if e in chain)
        percent = (found / len(elements)) * 100
        if percent >= 80:
            return f"Excellent ({percent:.0f}%) comprehensive chain documented."
        if percent >= 60:
            return f"Good ({percent:.0f}%) chain coverage."
        return f"Partial ({percent:.0f}%) chain documented."

    def _confidence_level(self, completion, num_patterns):
        if completion >= 90 and num_patterns >= 2:
            return "High confidence in data quality."
        if completion >= 75:
            return "Moderate confidence."
        return "Limited confidence; supplement assessment recommended."

    def _data_quality(self, responses):
        n = len(responses)
        if n >= 20:
            return "Excellent data coverage."
        if n >=15:
            return "Adequate data coverage."
        return "Limited responses."

    def _assigned_therapist(self, urgency, risk_flags):
        if len(risk_flags) >=3:
            return "Assign licensed clinical psychologist with hypnotherapy specialization."
        if len(risk_flags) >=1:
            return "Assign experienced clinical hypnotherapist with safety training."
        if 'extremely' in urgency.lower():
            return "Experienced rapid change hypnotherapist."
        return "Certified clinical hypnotherapist."

    def _review_schedule(self, urgency, risk_flags):
        if len(risk_flags) >=2:
            return "Review within 24-48 hours after initial contact."
        if 'extremely' in urgency.lower():
            return "Review within 1 week of contact."
        return "Review 2 weeks post completion."

    def _contact_timeline(self, urgency, risk_flags):
        if len(risk_flags) >= 3:
            return "Immediate - contact within 12 hours."
        if 'extremely' in urgency.lower():
            return "Within 24 hours."
        if 'very' in urgency.lower():
            return "Within 48 hours."
        return "Within 72 hours."

    def _response_recommendation(self, next_step):
        nl = next_step.lower() if next_step else ""
        if 'consult' in nl:
            return "Schedule free consultation call."
        if 'package' in nl:
            return "Send package info and pricing."
        if 'analysis' in nl:
            return "Send detailed assessment analysis."
        return "Initiate contact per client preference."

    def _session_preparation(self, pattern, risk_flags):
        if len(risk_flags) >= 2:
            return "Prepare safety strategies and crisis management."
        if pattern == 1:
            return "Prepare permission based modalities."
        if pattern == 2:
            return "Prepare collaborative empowerment techniques."
        if pattern == 3:
            return "Ensure transparency and clarity in protocol."
        return "Standard session preparation."

    # ---- Email sending infrastructure ----

    def _send_email(self, subject, body, email_type):
        try:
            if not self.password:
                print(f"[SIMULATE] Email sending disabled. Subject: {subject}")
                print(body[:500])  # Print snippet
                return True
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, "plain"))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            print(f"[SUCCESS] Sent {email_type} email: {subject}")
            return True
        except Exception as e:
            print(f"[ERROR] SMTP error sending {email_type} email: {e}")
            return False

# Global instance to use for callback
comprehensive_email_handler = ComprehensiveEmailHandler()

# API functions called by other modules

def send_clinical_assessment_results(data):
    return comprehensive_email_handler.send_clinical_assessment_results(data)

def send_booking_email(name, email, concern, message, booking_type):
    # Unchanged: pass through to handler's method
    try:
        return comprehensive_email_handler.send_booking_email(name, email, concern, message, booking_type)
    except Exception as e:
        print(f"[ERROR] Booking email sending error: {e}")
        return False

def send_discovery_email(data):
    try:
        return comprehensive_email_handler.send_discovery_email(data)
    except Exception as e:
        print(f"[ERROR] Discovery email sending error: {e}")
        return False

def send_package_email(data):
    try:
        return comprehensive_email_handler.send_package_email(data)
    except Exception as e:
        print(f"[ERROR] Package email sending error: {e}")
        return False
