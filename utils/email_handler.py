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
Complete Clinical Assessment Analysis with Therapeutic Intelligence
Maintains backward compatibility while adding comprehensive session preparation data
"""
import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class ComprehensiveEmailHandler:
    """Enhanced email handler with deep clinical analysis and therapeutic mapping"""

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

        # Enhanced pattern mapping with therapeutic intelligence
        self.pattern_analysis = {
            1: {
                "name": "Unhappiness Culture",
                "root_structure": "Unconscious belief that happiness is dangerous/undeserved",
                "core_beliefs": ["Happiness leads to disappointment", "I don't deserve good things", "Others' happiness matters more"],
                "systemic_factors": ["Family depression/anxiety patterns", "Cultural happiness skepticism", "Early happiness punishment"],
                "identity_conflicts": ["Happy me vs responsible me", "Joy conflicts with loyalty to suffering family"],
                "hidden_loyalties": ["Loyalty to depressed parent", "Family tradition of struggle", "Religious guilt about pleasure"],
                "intervention_strategy": "Permission installation, happiness tolerance building, loyalty reframing",
                "hypnotic_language": "Allow yourself to be happy while honoring those you love",
                "session_1_focus": "Map happiness fears and family patterns",
                "session_2_focus": "Install permission for happiness while maintaining love connections"
            },
            2: {
                "name": "Power Struggles", 
                "root_structure": "Core belief that control equals safety and survival",
                "core_beliefs": ["If I don't control, bad things happen", "Others can't be trusted with power", "Vulnerability equals danger"],
                "systemic_factors": ["Family power dynamics", "Early powerlessness trauma", "Authority figure conflicts"],
                "identity_conflicts": ["Strong me vs collaborative me", "Leader vs team player"],
                "hidden_loyalties": ["Loyalty to rebel parent", "Family mistrust of authority", "Protection of family honor"],
                "intervention_strategy": "Collaborative empowerment, shared control, strength through cooperation",
                "hypnotic_language": "You can be strong while working with others",
                "session_1_focus": "Understand control fears and early power dynamics",
                "session_2_focus": "Install collaborative strength and trust in partnership"
            },
            3: {
                "name": "Systematic Mistrust",
                "root_structure": "Deep belief that trust leads to betrayal and hurt",
                "core_beliefs": ["People always disappoint", "Trust leads to betrayal", "I'm safer alone"],
                "systemic_factors": ["Early betrayal experiences", "Family trust violations", "Cultural mistrust patterns"],
                "identity_conflicts": ["Independent me vs connected me", "Protected vs vulnerable"],
                "hidden_loyalties": ["Loyalty to betrayed parent", "Family survival strategy", "Cultural protection patterns"],
                "intervention_strategy": "Gradual trust building, safety establishment, discernment development",
                "hypnotic_language": "You can trust wisely while staying safe",
                "session_1_focus": "Map trust wounds and protective patterns",
                "session_2_focus": "Install discerning trust and safety in connection"
            },
            4: {
                "name": "Separation/Division",
                "root_structure": "World divided into rigid either/or categories limiting options",
                "core_beliefs": ["It's either perfect or failure", "All or nothing", "No middle ground exists"],
                "systemic_factors": ["Perfectionist family systems", "Religious black/white thinking", "Academic either/or pressure"],
                "identity_conflicts": ["Perfect me vs human me", "Right vs wrong identity"],
                "hidden_loyalties": ["Family perfectionist standards", "Religious absolute thinking", "Cultural purity concepts"],
                "intervention_strategy": "Both/and thinking installation, middle ground exploration, integration work",
                "hypnotic_language": "You can embrace both perfection and humanity",
                "session_1_focus": "Identify binary patterns and their origins",
                "session_2_focus": "Install flexible thinking and integration capacity"
            },
            5: {
                "name": "Doing vs Being",
                "root_structure": "Self-worth completely dependent on productivity and achievement",
                "core_beliefs": ["I am what I do", "Rest equals laziness", "Worth must be earned"],
                "systemic_factors": ["Achievement-oriented family", "Cultural productivity worship", "Economic survival fears"],
                "identity_conflicts": ["Achiever me vs human being me", "Valuable vs worthless"],
                "hidden_loyalties": ["Family work ethic", "Cultural success definitions", "Provider role loyalty"],
                "intervention_strategy": "Inherent worth installation, being value recognition, balanced achievement",
                "hypnotic_language": "Your worth exists in your being, not just your doing",
                "session_1_focus": "Separate worth from productivity patterns",
                "session_2_focus": "Install inherent value and balanced achievement"
            },
            6: {
                "name": "Compartmentalized Authenticity",
                "root_structure": "Identity fragments across contexts for safety/acceptance",
                "core_beliefs": ["Different situations require different selves", "My real self isn't acceptable", "Authenticity is dangerous"],
                "systemic_factors": ["Family role requirements", "Social masking needs", "Cultural conformity pressure"],
                "identity_conflicts": ["Real me vs acceptable me", "Authentic vs safe identity"],
                "hidden_loyalties": ["Family role expectations", "Social belonging needs", "Cultural fitting in"],
                "intervention_strategy": "Authentic integration, consistent identity, safe self-expression",
                "hypnotic_language": "You can be authentically yourself in all contexts",
                "session_1_focus": "Map identity fragments and safety needs",
                "session_2_focus": "Integrate authentic self across all contexts"
            },
            7: {
                "name": "Self-Sacrifice/Care Avoidance",
                "root_structure": "Others' needs always supersede own needs for love/acceptance",
                "core_beliefs": ["Others matter more", "Self-care is selfish", "I exist to serve others"],
                "systemic_factors": ["Caretaker family role", "Cultural service orientation", "Religious self-sacrifice"],
                "identity_conflicts": ["Caretaker me vs self-caring me", "Good vs selfish"],
                "hidden_loyalties": ["Family caretaker role", "Religious service ideals", "Cultural sacrifice values"],
                "intervention_strategy": "Balanced care installation, self-care as service, boundary strengthening",
                "hypnotic_language": "Caring for yourself allows you to better serve others",
                "session_1_focus": "Understand sacrifice patterns and loyalties",
                "session_2_focus": "Install balanced care and healthy boundaries"
            },
            8: {
                "name": "Inherited Missions",
                "root_structure": "Life goals determined by family expectations rather than personal desires",
                "core_beliefs": ["I must fulfill family dreams", "My desires don't matter", "Disappointing family equals betrayal"],
                "systemic_factors": ["Generational sacrifice patterns", "Family dream projection", "Cultural duty concepts"],
                "identity_conflicts": ["Family loyalist vs individual", "Dutiful vs authentic"],
                "hidden_loyalties": ["Parents' unfulfilled dreams", "Family honor", "Generational sacrifice"],
                "intervention_strategy": "Personal desire recognition, family honor with authenticity, respectful individuation",
                "hypnotic_language": "You can honor your family while following your authentic path",
                "session_1_focus": "Separate personal desires from family missions",
                "session_2_focus": "Install authentic goals while maintaining family love"
            },
            9: {
                "name": "Context-Dependent Weakness",
                "root_structure": "Personal power collapses in specific triggering contexts",
                "core_beliefs": ["I'm powerless with certain people", "Some situations defeat me", "Context determines my strength"],
                "systemic_factors": ["Early power violations", "Specific trauma contexts", "Learned helplessness patterns"],
                "identity_conflicts": ["Strong me vs powerless me", "Capable vs victim identity"],
                "hidden_loyalties": ["Victim role protection", "Family powerlessness patterns", "Trauma bonding"],
                "intervention_strategy": "Context-independent strength, power anchoring, consistent boundaries",
                "hypnotic_language": "Your strength remains constant across all contexts",
                "session_1_focus": "Identify power collapse triggers and contexts",
                "session_2_focus": "Install consistent strength and boundary integrity"
            }
        }

        # Behavioral chain intervention mapping
        self.chain_interventions = {
            "trigger_mapping": {
                "environmental": "External anchor modification, context reframing",
                "interpersonal": "Relationship dynamic interruption, boundary installation",
                "internal": "Thought pattern interruption, belief updating",
                "temporal": "Timing awareness, pattern prediction training",
                "somatic": "Body awareness, physical state management"
            },
            "physical_response": {
                "chest_tightness": "Breathing regulation, heart coherence training",
                "stomach_distress": "Gut-brain connection, digestive calm installation",
                "muscle_tension": "Progressive relaxation, tension release protocols",
                "temperature_changes": "Thermal regulation, comfort anchoring",
                "dissociation": "Grounding techniques, presence anchoring",
                "energy_shifts": "Energy management, vitality regulation"
            },
            "automatic_thoughts": {
                "catastrophic": "Realistic thinking installation, perspective broadening",
                "self_critical": "Self-compassion training, inner voice updating",
                "control_focused": "Acceptance training, flow state access",
                "safety_seeking": "Security anchoring, trust building",
                "performance": "Inherent worth installation, pressure release"
            },
            "emotional_responses": {
                "anxiety": "Calm confidence installation, safety anchoring",
                "anger": "Emotional regulation, healthy expression",
                "shame": "Self-acceptance training, worth installation",
                "sadness": "Emotional processing, comfort anchoring",
                "overwhelm": "Capacity building, manageable sizing"
            },
            "behavioral_patterns": {
                "avoidance": "Approach confidence, courage building",
                "compulsive": "Choice awareness, freedom installation",
                "people_pleasing": "Authentic expression, boundary strength",
                "perfectionism": "Good enough acceptance, progress celebration",
                "control_seeking": "Flow state access, trust building"
            }
        }

        # Somatic intervention mapping
        self.somatic_markers = {
            "breathing_patterns": "Coherent breathing, calm regulation",
            "heart_rate": "Heart coherence, rhythm stability",
            "muscle_tension": "Progressive relaxation, ease installation",
            "digestive_responses": "Gut-brain harmony, digestive calm",
            "energy_levels": "Vitality optimization, energy management",
            "sleep_patterns": "Rest quality, rejuvenation access"
        }

    # ==========================================
    # ENHANCED CLINICAL ASSESSMENT METHODS
    # ==========================================

    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment with deep therapeutic analysis"""
        try:
            print("[DEBUG] Starting enhanced clinical assessment email process")
            
            # Extract and validate data
            contact_info = assessment_data.get('contact_info', {})
            results = assessment_data.get('assessment_results', {})
            
            if not contact_info or not contact_info.get('email'):
                print("[ERROR] No valid contact_info found")
                return False
            
            if not results and not assessment_data.get('pattern_scores'):
                print("[ERROR] No assessment results found")
                return False
            
            # Enhanced priority assessment
            urgency = contact_info.get('urgency', 'Standard priority')
            risk_flags = results.get('risk_flags', []) or assessment_data.get('risk_flags', [])
            pattern_scores = results.get('pattern_scores', {}) or assessment_data.get('pattern_scores', {})
            
            # Determine clinical priority
            priority_flag = self._get_enhanced_priority_flag(urgency, risk_flags, pattern_scores)
            subject = f"{priority_flag} Clinical Assessment - {contact_info.get('name', 'Client')}"
            
            # Generate comprehensive therapeutic analysis
            body = self._format_enhanced_clinical_email(assessment_data)
            
            if not body or len(body) < 200:
                print("[ERROR] Enhanced email body generation failed")
                return False
            
            print(f"[DEBUG] Enhanced clinical email generated: {len(body)} characters")
            return self._send_email(subject, body, "Enhanced Clinical Assessment")
            
        except Exception as e:
            print(f"[ERROR] Enhanced clinical assessment email error: {e}")
            import traceback
            print(f"[ERROR] Traceback: {traceback.format_exc()}")
            return False

    def _format_enhanced_clinical_email(self, data):
        """Generate comprehensive therapeutic intelligence email"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract all data components
            contact = data.get('contact_info', {})
            results = data.get('assessment_results', {})
            responses = data.get('assessment_responses', {})
            intensity = data.get('intensity_responses', {})
            trigger_chain = data.get('trigger_chain', {})
            pattern_scores = results.get('pattern_scores', {}) or data.get('pattern_scores', {})
            risk_flags = results.get('risk_flags', []) or data.get('risk_flags', [])
            
            # Basic client information
            name = contact.get('name', 'Unknown')
            email = contact.get('email', 'Unknown')
            urgency = contact.get('urgency', 'Not specified')
            primary_concern = contact.get('primary_concern', 'Not provided')
            next_step = contact.get('next_step', 'Not specified')
            completion = results.get('completion_rate', 0) * 100
            total_questions = results.get('total_questions_answered', 0)

            # Generate therapeutic intelligence
            root_patterns = self._analyze_root_pattern_structures(pattern_scores, responses)
            systemic_analysis = self._analyze_systemic_factors(responses, pattern_scores)
            identity_conflicts = self._analyze_identity_conflicts(pattern_scores, responses)
            hidden_loyalties = self._analyze_hidden_loyalties(responses, pattern_scores)
            behavioral_chain = self._analyze_complete_behavioral_chain(trigger_chain, responses, intensity)
            intervention_mapping = self._generate_intervention_mapping_table(pattern_scores, trigger_chain, responses)
            session_protocols = self._generate_session_protocols(pattern_scores, behavioral_chain, root_patterns)
            hypnotic_language = self._generate_hypnotic_language_preparation(responses, pattern_scores)

            # Build comprehensive email
            body = f"""
🧠 COMPREHENSIVE THERAPEUTIC INTELLIGENCE REPORT
Generated: {timestamp}
Clinical Priority: {self._get_enhanced_clinical_priority(urgency, risk_flags, pattern_scores)}

═══════════════════════════════════════════════════════════════════════════════

👤 CLIENT PROFILE & THERAPEUTIC CONTEXT

Name: {name}
Email: {email}
Primary Concern: {primary_concern}
Urgency Level: {urgency}
Preferred Next Step: {next_step}
Assessment Quality: {completion:.0f}% completion ({total_questions} questions)

═══════════════════════════════════════════════════════════════════════════════

🎯 ROOT PATTERN STRUCTURE ANALYSIS

{root_patterns}

═══════════════════════════════════════════════════════════════════════════════

🌐 SYSTEMIC FACTORS MAINTAINING PROBLEMS

{systemic_analysis}

═══════════════════════════════════════════════════════════════════════════════

🆔 IDENTITY CONFLICTS BLOCKING CHANGE

{identity_conflicts}

═══════════════════════════════════════════════════════════════════════════════

🛡️ HIDDEN LOYALTIES CREATING RESISTANCE

{hidden_loyalties}

═══════════════════════════════════════════════════════════════════════════════

🔄 COMPLETE BEHAVIORAL CHAIN MAPPING

{behavioral_chain}

═══════════════════════════════════════════════════════════════════════════════

🎯 INTERVENTION MAPPING TABLE

{intervention_mapping}

═══════════════════════════════════════════════════════════════════════════════

📋 SESSION PROTOCOLS & THERAPEUTIC DESIGN

{session_protocols}

═══════════════════════════════════════════════════════════════════════════════

🎭 HYPNOTIC LANGUAGE PREPARATION

{hypnotic_language}

═══════════════════════════════════════════════════════════════════════════════

⚠️ CLINICAL RISK ASSESSMENT

Risk Level: {self._assess_comprehensive_risk_level(risk_flags, pattern_scores)}
Risk Factors: {len(risk_flags)} identified
{self._format_enhanced_risk_analysis(risk_flags, pattern_scores)}

═══════════════════════════════════════════════════════════════════════════════

📞 IMMEDIATE THERAPEUTIC ACTION PROTOCOL

Contact Timeline: {self._get_enhanced_contact_timeline(urgency, risk_flags, pattern_scores)}
Recommended Response: {self._get_enhanced_response_protocol(next_step, pattern_scores)}

Session Preparation Checklist:
1. Review complete behavioral chain mapping for intervention points
2. Prepare pattern-specific hypnotic language from client's exact words
3. {self._get_specific_session_preparation(pattern_scores, risk_flags)}
4. Set up environment for identified somatic interventions
5. Prepare resistance management for hidden loyalty patterns

═══════════════════════════════════════════════════════════════════════════════

💬 COMPLETE CLIENT RESPONSE ANALYSIS

{self._format_detailed_response_analysis(responses, intensity, trigger_chain)}

═══════════════════════════════════════════════════════════════════════════════

🔧 THERAPEUTIC METADATA & CLINICAL NOTES

Assessment Algorithm: Enhanced Behavioral Pattern Analysis v3.0
Therapeutic Confidence: {self._assess_therapeutic_confidence(completion, len(pattern_scores), risk_flags)}
Data Integrity: {self._assess_enhanced_data_integrity(responses, trigger_chain)}
Intervention Complexity: {self._assess_intervention_complexity(pattern_scores, risk_flags)}

Recommended Therapist Profile: {self._recommend_enhanced_therapist_type(risk_flags, pattern_scores)}
Session Timing Optimization: {self._recommend_session_timing(pattern_scores, urgency)}
Follow-up Protocol: {self._recommend_follow_up_protocol(pattern_scores, risk_flags)}

⚠️ CONFIDENTIAL THERAPEUTIC DOCUMENT
Contains comprehensive psychological assessment and intervention strategies
Licensed clinical hypnotherapist review required before client contact

═══════════════════════════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Enhanced Clinical Intelligence System
Generated: {timestamp}
Client Reference: {name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Enhanced email formatting failed: {e}")
            import traceback
            print(f"[ERROR] Traceback: {traceback.format_exc()}")
            return self._generate_fallback_email(data, str(e))

    def _analyze_root_pattern_structures(self, pattern_scores, responses):
        """Analyze root psychological structures causing surface symptoms"""
        if not pattern_scores:
            return "No significant patterns detected - surface intervention may be sufficient"
        
        analysis = "ROOT PATTERN STRUCTURES:\n\n"
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
            if pattern_id not in self.pattern_analysis:
                continue
                
            pattern_info = self.pattern_analysis[pattern_id]
            intensity = self._score_to_intensity_level(score)
            rank = "🔴 DOMINANT" if i == 0 else f"🟡 SECONDARY #{i}"
            
            analysis += f"{rank} PATTERN: {pattern_info['name']} ({intensity} intensity)\n"
            analysis += f"├─ Root Structure: {pattern_info['root_structure']}\n"
            analysis += f"├─ Core Beliefs:\n"
            for belief in pattern_info['core_beliefs']:
                analysis += f"│  • {belief}\n"
            analysis += f"└─ Therapeutic Target: {pattern_info['intervention_strategy']}\n\n"
        
        # Pattern interaction analysis
        if len(sorted_patterns) >= 2:
            analysis += "PATTERN INTERACTIONS:\n"
            dominant = sorted_patterns[0][0]
            secondary = sorted_patterns[1][0] if len(sorted_patterns) > 1 else None
            
            if dominant and secondary:
                interaction = self._analyze_pattern_interaction(dominant, secondary)
                analysis += f"• {self.pattern_analysis[dominant]['name']} + {self.pattern_analysis[secondary]['name']}: {interaction}\n"
        
        return analysis

    def _analyze_systemic_factors(self, responses, pattern_scores):
        """Analyze family, cultural, and environmental factors maintaining problems"""
        analysis = "SYSTEMIC MAINTENANCE FACTORS:\n\n"
        
        # Extract family system information from responses
        family_patterns = []
        cultural_factors = []
        environmental_triggers = []
        
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            question_text = response_data.get('question_text', '').lower()
            
            # Family system patterns
            if any(word in response_text for word in ['family', 'parent', 'mother', 'father', 'sibling']):
                family_patterns.append(response_data.get('response', ''))
            
            # Cultural factors
            if any(word in response_text for word in ['culture', 'tradition', 'religion', 'society', 'community']):
                cultural_factors.append(response_data.get('response', ''))
            
            # Environmental triggers
            if 'trigger' in question_text or 'situation' in question_text:
                environmental_triggers.append(response_data.get('response', ''))
        
        # Analyze dominant patterns for systemic factors
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            if dominant_pattern in self.pattern_analysis:
                pattern_info = self.pattern_analysis[dominant_pattern]
                analysis += f"PRIMARY PATTERN SYSTEMIC FACTORS ({pattern_info['name']}):\n"
                for factor in pattern_info['systemic_factors']:
                    analysis += f"• {factor}\n"
                analysis += "\n"
        
        # Family system analysis
        if family_patterns:
            analysis += "FAMILY SYSTEM PATTERNS:\n"
            for i, pattern in enumerate(family_patterns[:3], 1):
                analysis += f"{i}. {pattern[:100]}...\n"
            analysis += "\n"
        
        # Environmental factors
        if environmental_triggers:
            analysis += "ENVIRONMENTAL TRIGGERS:\n"
            for i, trigger in enumerate(environmental_triggers[:3], 1):
                analysis += f"{i}. {trigger[:100]}...\n"
            analysis += "\n"
        
        analysis += "SYSTEMIC INTERVENTION STRATEGY:\n"
        analysis += "• Address family loyalty conflicts during Session 1\n"
        analysis += "• Reframe cultural values to support change\n"
        analysis += "• Modify environmental triggers through anchoring\n"
        analysis += "• Install systemic change while honoring relationships\n"
        
        return analysis

    def _analyze_identity_conflicts(self, pattern_scores, responses):
        """Analyze core identity conflicts blocking change"""
        analysis = "IDENTITY CONFLICTS BLOCKING CHANGE:\n\n"
        
        if not pattern_scores:
            return analysis + "No significant identity conflicts detected"
        
        # Analyze each significant pattern for identity conflicts
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
            if pattern_id not in self.pattern_analysis:
                continue
                
            pattern_info = self.pattern_analysis[pattern_id]
            rank = "PRIMARY" if i == 0 else "SECONDARY"
            
            analysis += f"{rank} IDENTITY CONFLICT ({pattern_info['name']}):\n"
            for conflict in pattern_info['identity_conflicts']:
                analysis += f"• {conflict}\n"
            analysis += "\n"
        
        # Extract identity language from responses
        identity_responses = []
        for response_data in responses.values():
            response_text = str(response_data.get('response', ''))
            question_text = response_data.get('question_text', '').lower()
            
            if any(word in question_text for word in ['identity', 'self', 'personality', 'who you are']):
                identity_responses.append(response_text)
        
        if identity_responses:
            analysis += "CLIENT IDENTITY LANGUAGE:\n"
            for i, response in enumerate(identity_responses[:2], 1):
                analysis += f"{i}. \"{response[:150]}...\"\n"
            analysis += "\n"
        
        analysis += "IDENTITY INTEGRATION STRATEGY:\n"
        analysis += "• Session 1: Map conflicting identity parts\n"
        analysis += "• Session 2: Install integrated identity across contexts\n"
        analysis += "• Use client's own language for identity acceptance\n"
        analysis += "• Create bridges between conflicting parts\n"
        
        return analysis

    def _analyze_hidden_loyalties(self, responses, pattern_scores):
        """Analyze hidden family/cultural loyalties creating resistance"""
        analysis = "HIDDEN LOYALTIES CREATING RESISTANCE:\n\n"
        
        if not pattern_scores:
            return analysis + "No significant loyalty conflicts detected"
        
        # Analyze loyalty patterns from dominant behavioral patterns
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns[:2]):
            if pattern_id not in self.pattern_analysis:
                continue
                
            pattern_info = self.pattern_analysis[pattern_id]
            rank = "PRIMARY" if i == 0 else "SECONDARY"
            
            analysis += f"{rank} LOYALTY PATTERN ({pattern_info['name']}):\n"
            for loyalty in pattern_info['hidden_loyalties']:
                analysis += f"• {loyalty}\n"
            analysis += "\n"
        
        # Extract loyalty language from responses
        loyalty_indicators = []
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            
            # Look for loyalty language
            if any(word in response_text for word in ['family', 'parent', 'should', 'duty', 'responsible', 'loyal', 'tradition']):
                loyalty_indicators.append(response_data.get('response', ''))
        
        if loyalty_indicators:
            analysis += "CLIENT LOYALTY LANGUAGE:\n"
            for i, indicator in enumerate(loyalty_indicators[:3], 1):
                analysis += f"{i}. \"{indicator[:120]}...\"\n"
            analysis += "\n"
        
        analysis += "LOYALTY HONORING STRATEGY:\n"
        analysis += "• Session 1: Identify and honor all loyalty patterns\n"
        analysis += "• Reframe change as honoring deeper loyalty values\n"
        analysis += "• Install 'both/and' thinking: loyal AND authentic\n"
        analysis += "• Use loyalty language to support change\n"
        analysis += "• Create new loyalty: to authentic self and family happiness\n"
        
        return analysis

    def _analyze_complete_behavioral_chain(self, trigger_chain, responses, intensity_data):
        """Analyze complete behavioral chain for precise intervention points"""
        analysis = "COMPLETE BEHAVIORAL CHAIN ANALYSIS:\n\n"
        
        # Use trigger_chain if available, otherwise extract from responses
        if trigger_chain:
            analysis += "MAPPED BEHAVIORAL SEQUENCE:\n"
            
            chain_steps = [
                ('awareness_point', 'TRIGGER AWARENESS'),
                ('physical_response', 'PHYSICAL RESPONSE'),
                ('automatic_thought', 'AUTOMATIC THOUGHT'),
                ('emotional_response', 'EMOTIONAL RESPONSE'),
                ('behavioral_response', 'BEHAVIORAL RESPONSE'),
                ('immediate_consequence', 'IMMEDIATE CONSEQUENCE'),
                ('longer_term_impact', 'LONGER-TERM IMPACT')
            ]
            
            for step_key, step_name in chain_steps:
                if step_key in trigger_chain:
                    response = trigger_chain[step_key]
                    intervention = self._get_chain_intervention(step_key, response)
                    analysis += f"{step_name}:\n"
                    analysis += f"├─ Client Response: \"{response}\"\n"
                    analysis += f"├─ Intervention Point: {intervention}\n"
                    analysis += f"└─ Session Target: {self._get_session_target(step_key)}\n\n"
        else:
            # Extract behavioral chain from general responses
            analysis += "BEHAVIORAL PATTERNS EXTRACTED FROM RESPONSES:\n"
            
            # Look for trigger descriptions
            trigger_responses = []
            thought_responses = []
            emotional_responses = []
            behavioral_responses = []
            
            for response_data in responses.values():
                question_text = response_data.get('question_text', '').lower()
                response = response_data.get('response', '')
                
                if 'trigger' in question_text or 'situation' in question_text:
                    trigger_responses.append(response)
                elif 'thought' in question_text or 'inner voice' in question_text:
                    thought_responses.append(response)
                elif 'emotion' in question_text or 'feel' in question_text:
                    emotional_responses.append(response)
                elif 'behavior' in question_text or 'response' in question_text:
                    behavioral_responses.append(response)
            
            if trigger_responses:
                analysis += f"TRIGGERS: {trigger_responses[0][:100]}...\n"
            if thought_responses:
                analysis += f"THOUGHTS: {thought_responses[0][:100]}...\n"
            if emotional_responses:
                analysis += f"EMOTIONS: {emotional_responses[0][:100]}...\n"
            if behavioral_responses:
                analysis += f"BEHAVIORS: {behavioral_responses[0][:100]}...\n"
        
        # Add intensity analysis if available
        if intensity_data:
            high_intensity = {k: v for k, v in intensity_data.items() if v >= 6}
            if high_intensity:
                analysis += f"\nHIGH INTENSITY RESPONSES ({len(high_intensity)} items rated 6-7/7):\n"
                analysis += "• Requires gentle pacing and grounding techniques\n"
                analysis += "• Use somatic regulation before cognitive work\n"
                analysis += "• Install safety anchors before pattern interruption\n"
        
        analysis += "\nCHAIN INTERVENTION STRATEGY:\n"
        analysis += "• Session 1: Map complete chain and install awareness\n"
        analysis += "• Session 2: Install new responses at each intervention point\n"
        analysis += "• Use client's exact language for maximum resonance\n"
        analysis += "• Create new automatic chain: Trigger → Calm → Choice → Response\n"
        
        return analysis

    def _generate_intervention_mapping_table(self, pattern_scores, trigger_chain, responses):
        """Generate direct response-to-intervention mapping table"""
        mapping = "INTERVENTION MAPPING TABLE:\n\n"
        
        if not pattern_scores and not responses:
            return mapping + "Insufficient data for intervention mapping"
        
        mapping += "PATTERN-SPECIFIC INTERVENTIONS:\n"
        
        # Map each identified pattern to specific interventions
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            for i, (pattern_id, score) in enumerate(sorted_patterns[:3]):
                if pattern_id not in self.pattern_analysis:
                    continue
                    
                pattern_info = self.pattern_analysis[pattern_id]
                priority = "HIGH" if i == 0 else "MEDIUM" if i == 1 else "LOW"
                
                mapping += f"\n{priority} PRIORITY: {pattern_info['name']} (Score: {score:.1f})\n"
                mapping += f"├─ Session 1 Protocol: {pattern_info['session_1_focus']}\n"
                mapping += f"├─ Session 2 Protocol: {pattern_info['session_2_focus']}\n"
                mapping += f"├─ Hypnotic Language: \"{pattern_info['hypnotic_language']}\"\n"
                mapping += f"├─ Intervention Strategy: {pattern_info['intervention_strategy']}\n"
                mapping += f"└─ Success Marker: Client can {self._get_success_marker(pattern_id)}\n"
        
        # Map behavioral chain interventions
        if trigger_chain:
            mapping += "\nBEHAVIORAL CHAIN INTERVENTIONS:\n"
            
            for step_key, response in trigger_chain.items():
                if step_key in self.chain_interventions:
                    intervention_type = self._classify_response_type(response)
                    specific_intervention = self._get_specific_intervention(step_key, intervention_type, response)
                    
                    mapping += f"\n{step_key.upper().replace('_', ' ')}:\n"
                    mapping += f"├─ Client Pattern: \"{response[:80]}...\"\n"
                    mapping += f"├─ Intervention Type: {intervention_type}\n"
                    mapping += f"├─ Specific Technique: {specific_intervention}\n"
                    mapping += f"└─ Installation Method: {self._get_installation_method(step_key)}\n"
        
        # Extract key response interventions from general responses
        mapping += "\nKEY RESPONSE INTERVENTIONS:\n"
        
        intervention_responses = []
        for response_data in responses.values():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            # Identify responses that need specific interventions
            if len(response) > 50 and any(keyword in question_text.lower() for keyword in 
                ['behavior', 'pattern', 'response', 'trigger', 'thought', 'emotion']):
                intervention_responses.append((question_text, response))
        
        for i, (question, response) in enumerate(intervention_responses[:5], 1):
            intervention = self._generate_response_intervention(question, response)
            mapping += f"\n{i}. RESPONSE: \"{response[:60]}...\"\n"
            mapping += f"   └─ INTERVENTION: {intervention}\n"
        
        return mapping

    def _generate_session_protocols(self, pattern_scores, behavioral_chain, root_patterns):
        """Generate specific Session 1 and Session 2 protocols"""
        protocols = "SESSION PROTOCOLS & THERAPEUTIC DESIGN:\n\n"
        
        if not pattern_scores:
            return protocols + "Standard exploratory protocol recommended"
        
        # Determine dominant pattern for session structure
        dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
        pattern_info = self.pattern_analysis.get(dominant_pattern, {})
        
        protocols += f"DOMINANT PATTERN: {pattern_info.get('name', 'Unknown')}\n\n"
        
        # Session 1 Protocol
        protocols += "SESSION 1 PROTOCOL (90 minutes):\n"
        protocols += "┌─ RAPPORT & SAFETY (15 min)\n"
        protocols += f"├─ PATTERN MAPPING: {pattern_info.get('session_1_focus', 'Standard mapping')}\n"
        protocols += "├─ TRIGGER CHAIN ANALYSIS: Map complete behavioral sequence\n"
        protocols += "├─ LOYALTY ASSESSMENT: Identify hidden resistance patterns\n"
        protocols += "├─ IDENTITY MAPPING: Understand conflicting self-concepts\n"
        protocols += "├─ SOMATIC AWARENESS: Establish body-mind connection\n"
        protocols += "├─ PRELIMINARY INSTALLATION: Initial safety and choice anchors\n"
        protocols += "└─ SESSION CLOSE: Future pace Session 2 transformation\n\n"
        
        # Session 2 Protocol
        protocols += "SESSION 2 PROTOCOL (90 minutes):\n"
        protocols += "┌─ STATE INDUCTION (20 min): Pattern-specific approach\n"
        protocols += f"├─ CORE TRANSFORMATION: {pattern_info.get('session_2_focus', 'Standard transformation')}\n"
        protocols += "├─ CHAIN REWIRING: Install new automatic responses\n"
        protocols += "├─ LOYALTY HONORING: Maintain relationships while changing\n"
        protocols += "├─ IDENTITY INTEGRATION: Unified self across contexts\n"
        protocols += "├─ SOMATIC ANCHORING: Body-based change reinforcement\n"
        protocols += "├─ FUTURE REHEARSAL: Practice new patterns in imagination\n"
        protocols += "└─ INTEGRATION CLOSE: Seal changes and provide resources\n\n"
        
        # Induction Style Recommendations
        protocols += "INDUCTION STYLE RECOMMENDATIONS:\n"
        
        if dominant_pattern in [1, 7]:  # Unhappiness, Self-sacrifice
            protocols += "• Gentle, permission-based induction\n"
            protocols += "• Avoid overwhelming positive suggestions\n"
            protocols += "• Use client's own pace and comfort level\n"
        elif dominant_pattern in [2, 3]:  # Power struggles, Mistrust
            protocols += "• Collaborative, transparent induction\n"
            protocols += "• Explain each step and maintain client control\n"
            protocols += "• Use partnership language throughout\n"
        elif dominant_pattern in [4, 5]:  # Separation, Doing vs Being
            protocols += "• Integration-focused induction\n"
            protocols += "• Both/and language instead of either/or\n"
            protocols += "• Emphasize wholeness and balance\n"
        else:
            protocols += "• Standard clinical induction\n"
            protocols += "• Adapt based on client response\n"
        
        # Resistance Management
        protocols += "\nRESISTANCE MANAGEMENT PROTOCOL:\n"
        protocols += f"• Expected Resistance: {self._predict_resistance(dominant_pattern)}\n"
        protocols += f"• Management Strategy: {pattern_info.get('intervention_strategy', 'Standard approach')}\n"
        protocols += "• Reframe resistance as protective wisdom\n"
        protocols += "• Honor the positive intention of old patterns\n"
        protocols += "• Install change while maintaining safety\n"
        
        return protocols

    def _generate_hypnotic_language_preparation(self, responses, pattern_scores):
        """Generate client-specific hypnotic language using their exact words"""
        language_prep = "HYPNOTIC LANGUAGE PREPARATION:\n\n"
        
        # Extract client's exact language for mirroring
        client_language = {}
        emotional_words = []
        value_words = []
        concern_words = []
        
        for response_data in responses.values():
            response = str(response_data.get('response', ''))
            question_text = response_data.get('question_text', '').lower()
            
            # Extract emotional language
            if 'emotion' in question_text or 'feel' in question_text:
                emotional_words.extend(self._extract_key_words(response))
            
            # Extract value language
            if 'important' in question_text or 'value' in question_text or 'matter' in question_text:
                value_words.extend(self._extract_key_words(response))
            
            # Extract concern language
            if 'concern' in question_text or 'problem' in question_text or 'change' in question_text:
                concern_words.extend(self._extract_key_words(response))
        
        # Client's language for mirroring
        language_prep += "CLIENT'S LANGUAGE FOR MIRRORING:\n"
        if emotional_words:
            language_prep += f"• Emotional Words: {', '.join(emotional_words[:8])}\n"
        if value_words:
            language_prep += f"• Value Words: {', '.join(value_words[:8])}\n"
        if concern_words:
            language_prep += f"• Concern Words: {', '.join(concern_words[:8])}\n"
        
        # Pattern-specific therapeutic language
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            pattern_info = self.pattern_analysis.get(dominant_pattern, {})
            
            language_prep += f"\nPATTERN-SPECIFIC THERAPEUTIC LANGUAGE:\n"
            language_prep += f"• Core Installation: \"{pattern_info.get('hypnotic_language', 'Standard positive installation')}\"\n"
            
            # Generate specific suggestions based on pattern
            suggestions = self._generate_pattern_suggestions(dominant_pattern, client_language)
            language_prep += f"• Specific Suggestions:\n"
            for suggestion in suggestions:
                language_prep += f"  - \"{suggestion}\"\n"
        
        # Somatic anchoring language
        language_prep += "\nSOMATIC ANCHORING LANGUAGE:\n"
        physical_responses = []
        for response_data in responses.values():
            if 'physical' in response_data.get('question_text', '').lower():
                physical_responses.append(response_data.get('response', ''))
        
        if physical_responses:
            language_prep += f"• Client's Physical Language: \"{physical_responses[0][:80]}...\"\n"
            language_prep += f"• Anchoring Approach: {self._get_somatic_approach(physical_responses[0])}\n"
        
        # Metaphor and imagery suggestions
        language_prep += "\nMETAPHOR & IMAGERY SUGGESTIONS:\n"
        metaphors = self._generate_client_metaphors(responses, pattern_scores)
        for metaphor in metaphors:
            language_prep += f"• {metaphor}\n"
        
        return language_prep

    # ==========================================
    # ENHANCED ANALYSIS HELPER METHODS
    # ==========================================

    def _get_enhanced_priority_flag(self, urgency, risk_flags, pattern_scores):
        """Enhanced priority assessment including pattern severity"""
        risk_count = len(risk_flags)
        pattern_severity = max(pattern_scores.values()) if pattern_scores else 0
        
        if risk_count >= 3 or pattern_severity >= 10:
            return "🔴 CRITICAL"
        elif risk_count >= 2 or pattern_severity >= 8 or 'extremely urgent' in urgency.lower():
            return "🟠 HIGH PRIORITY"
        elif risk_count >= 1 or pattern_severity >= 6 or 'very urgent' in urgency.lower():
            return "🟡 PRIORITY"
        else:
            return "📋 ASSESSMENT"

    def _get_enhanced_clinical_priority(self, urgency, risk_flags, pattern_scores):
        """Enhanced clinical priority with pattern consideration"""
        risk_count = len(risk_flags)
        pattern_severity = max(pattern_scores.values()) if pattern_scores else 0
        
        if risk_count >= 3:
            return "CRITICAL - Immediate specialized intervention required"
        elif pattern_severity >= 10:
            return "HIGH COMPLEXITY - Advanced clinical approach needed"
        elif 'extremely urgent' in urgency.lower():
            return "URGENT - Priority scheduling within 24 hours"
        elif pattern_severity >= 8 or 'very urgent' in urgency.lower():
            return "ELEVATED - Contact within 48 hours"
        else:
            return "STANDARD - Contact within 72 hours"

    def _score_to_intensity_level(self, score):
        """Convert numeric score to intensity description"""
        if score >= 10:
            return "Critical"
        elif score >= 8:
            return "Very High"
        elif score >= 6:
            return "High"
        elif score >= 4:
            return "Moderate"
        elif score >= 2:
            return "Low"
        else:
            return "Minimal"

    def _analyze_pattern_interaction(self, dominant, secondary):
        """Analyze how two patterns interact to create complexity"""
        interactions = {
            (1, 2): "Unhappiness culture reinforces power struggles - client fights for right to be miserable",
            (1, 7): "Unhappiness culture + self-sacrifice creates martyr complex - suffering validates worth",
            (2, 3): "Power struggles + mistrust creates defensive isolation - control through withdrawal",
            (3, 7): "Mistrust + self-sacrifice creates exhausting hypervigilance for others' needs",
            (4, 5): "Binary thinking + doing addiction creates perfectionist burnout cycles",
            (5, 7): "Doing addiction + self-sacrifice creates compulsive caretaking and productivity",
            (6, 9): "Compartmentalized authenticity + context weakness creates complete identity collapse"
        }
        
        return interactions.get((dominant, secondary), "Complex pattern interaction requiring individualized approach")

    def _get_chain_intervention(self, step_key, response):
        """Get specific intervention for behavioral chain step"""
        interventions = {
            'awareness_point': f"Environmental modification and trigger reframing",
            'physical_response': f"Somatic regulation: {self._get_somatic_intervention(response)}",
            'automatic_thought': f"Cognitive reframing: {self._get_cognitive_intervention(response)}",
            'emotional_response': f"Emotional regulation: {self._get_emotional_intervention(response)}",
            'behavioral_response': f"Behavioral interruption: {self._get_behavioral_intervention(response)}",
            'immediate_consequence': f"Consequence reframing and pattern interruption",
            'longer_term_impact': f"Future vision installation and motivation anchoring"
        }
        
        return interventions.get(step_key, "Standard intervention protocol")

    def _get_session_target(self, step_key):
        """Get session targeting for each chain step"""
        targets = {
            'awareness_point': "Session 1 - Trigger mapping and awareness installation",
            'physical_response': "Session 2 - Somatic retraining and body anchoring",
            'automatic_thought': "Session 2 - Thought pattern rewiring and belief updating",
            'emotional_response': "Session 2 - Emotional regulation and new response installation",
            'behavioral_response': "Session 2 - New behavioral pattern programming",
            'immediate_consequence': "Session 2 - Positive consequence anchoring",
            'longer_term_impact': "Session 2 - Future vision and motivation installation"
        }
        
        return targets.get(step_key, "Standard session approach")

    def _get_somatic_intervention(self, response):
        """Get specific somatic intervention based on physical response"""
        response_lower = response.lower()
        
        if 'chest' in response_lower or 'heart' in response_lower or 'breath' in response_lower:
            return "Breathing regulation, heart coherence training"
        elif 'stomach' in response_lower or 'nausea' in response_lower or 'gut' in response_lower:
            return "Digestive calm installation, gut-brain harmony"
        elif 'tension' in response_lower or 'tight' in response_lower or 'muscle' in response_lower:
            return "Progressive relaxation, tension release protocols"
        elif 'hot' in response_lower or 'cold' in response_lower or 'temperature' in response_lower:
            return "Thermal regulation, comfort anchoring"
        elif 'numb' in response_lower or 'disconnect' in response_lower or 'dissociat' in response_lower:
            return "Grounding techniques, presence anchoring"
        else:
            return "General somatic regulation and body awareness"

    def _get_cognitive_intervention(self, response):
        """Get specific cognitive intervention based on automatic thoughts"""
        response_lower = response.lower()
        
        if 'not good enough' in response_lower or 'inadequate' in response_lower:
            return "Self-worth installation, adequacy anchoring"
        elif 'danger' in response_lower or 'bad will happen' in response_lower:
            return "Safety installation, realistic thinking training"
        elif 'can\'t handle' in response_lower or 'powerless' in response_lower:
            return "Capability installation, empowerment anchoring"
        elif 'reject' in response_lower or 'abandon' in response_lower:
            return "Acceptance anchoring, relationship security"
        elif 'should' in response_lower or 'must' in response_lower:
            return "Choice installation, pressure release"
        else:
            return "General cognitive reframing and belief updating"

    def _get_emotional_intervention(self, response):
        """Get specific emotional intervention based on emotional responses"""
        if isinstance(response, dict):
            # Handle multi-select emotional responses
            emotions = list(response.keys())
            primary_emotion = emotions[0] if emotions else "mixed"
        else:
            primary_emotion = str(response).lower()
        
        if 'anxiety' in primary_emotion or 'fear' in primary_emotion:
            return "Calm confidence installation, safety anchoring"
        elif 'anger' in primary_emotion or 'rage' in primary_emotion:
            return "Emotional regulation, healthy expression training"
        elif 'shame' in primary_emotion or 'embarrass' in primary_emotion:
            return "Self-acceptance training, dignity restoration"
        elif 'sad' in primary_emotion or 'grief' in primary_emotion:
            return "Emotional processing, comfort anchoring"
        elif 'overwhelm' in primary_emotion or 'panic' in primary_emotion:
            return "Capacity building, manageable sizing"
        else:
            return "General emotional regulation and balance"

    def _get_behavioral_intervention(self, response):
        """Get specific behavioral intervention based on behavioral patterns"""
        response_lower = str(response).lower()
        
        if 'avoid' in response_lower or 'withdraw' in response_lower:
            return "Approach confidence, courage building"
        elif 'compulsive' in response_lower or 'repetition' in response_lower:
            return "Choice awareness, freedom installation"
        elif 'reassurance' in response_lower or 'approval' in response_lower:
            return "Self-validation, independence strengthening"
        elif 'self-critical' in response_lower or 'self-punishment' in response_lower:
            return "Self-compassion training, inner kindness"
        elif 'perfectionism' in response_lower or 'over-preparation' in response_lower:
            return "Good enough acceptance, progress celebration"
        else:
            return "General behavioral flexibility and choice expansion"

    def _classify_response_type(self, response):
        """Classify response type for intervention mapping"""
        response_lower = str(response).lower()
        
        if any(word in response_lower for word in ['family', 'parent', 'childhood']):
            return "Family System"
        elif any(word in response_lower for word in ['work', 'job', 'professional']):
            return "Professional Context"
        elif any(word in response_lower for word in ['relationship', 'partner', 'friend']):
            return "Interpersonal"
        elif any(word in response_lower for word in ['physical', 'body', 'sensation']):
            return "Somatic"
        elif any(word in response_lower for word in ['thought', 'think', 'mind']):
            return "Cognitive"
        elif any(word in response_lower for word in ['feel', 'emotion', 'mood']):
            return "Emotional"
        else:
            return "General Pattern"

    def _get_specific_intervention(self, step_key, intervention_type, response):
        """Get specific intervention based on step, type, and response content"""
        base_interventions = {
            'trigger_mapping': {
                'Family System': "Family pattern interruption, loyalty reframing",
                'Professional Context': "Work context anchoring, performance confidence",
                'Interpersonal': "Relationship dynamic modification, boundary installation",
                'General Pattern': "Environmental trigger modification"
            },
            'physical_response': {
                'Somatic': self._get_somatic_intervention(response),
                'General Pattern': "General somatic regulation"
            },
            'automatic_thought': {
                'Cognitive': self._get_cognitive_intervention(response),
                'General Pattern': "Thought pattern interruption"
            }
        }
        
        step_interventions = base_interventions.get(step_key, {})
        return step_interventions.get(intervention_type, f"Specialized {intervention_type.lower()} intervention")

    def _get_installation_method(self, step_key):
        """Get installation method for each chain step"""
        methods = {
            'awareness_point': "Awareness anchoring and environmental cueing",
            'physical_response': "Somatic anchoring and body-based installation",
            'automatic_thought': "Cognitive anchoring and belief integration",
            'emotional_response': "Emotional anchoring and feeling state installation",
            'behavioral_response': "Behavioral anchoring and action pattern programming",
            'immediate_consequence': "Consequence anchoring and feedback loop installation",
            'longer_term_impact': "Future vision anchoring and motivation programming"
        }
        
        return methods.get(step_key, "Standard hypnotic installation")

    def _generate_response_intervention(self, question, response):
        """Generate specific intervention based on question-response pair"""
        question_lower = question.lower()
        response_lower = str(response).lower()
        
        # Pattern-specific interventions based on question type
        if 'trigger' in question_lower:
            return f"Trigger reframing: Transform '{response[:30]}...' into empowerment cue"
        elif 'physical' in question_lower:
            return f"Somatic retraining: {self._get_somatic_intervention(response)}"
        elif 'thought' in question_lower or 'inner voice' in question_lower:
            return f"Cognitive rewiring: Replace with supportive inner dialogue"
        elif 'emotion' in question_lower:
            return f"Emotional regulation: {self._get_emotional_intervention(response)}"
        elif 'behavior' in question_lower:
            return f"Behavioral modification: {self._get_behavioral_intervention(response)}"
        else:
            return "Comprehensive pattern interruption and positive installation"

    def _get_success_marker(self, pattern_id):
        """Get success markers for each pattern"""
        markers = {
            1: "experience and maintain happiness naturally",
            2: "collaborate powerfully while maintaining strength",
            3: "trust wisely and connect safely",
            4: "embrace both/and thinking and flexible choices",
            5: "feel valuable for being, not just doing",
            6: "express authentically across all contexts",
            7: "care for self while serving others",
            8: "follow authentic path while honoring family",
            9: "maintain strength and boundaries in all contexts"
        }
        
        return markers.get(pattern_id, "achieve desired behavioral change")

    def _predict_resistance(self, pattern_id):
        """Predict likely resistance patterns"""
        resistance_patterns = {
            1: "May resist positive suggestions or happiness installation",
            2: "May challenge therapist authority or directive approaches",
            3: "May question techniques or need extensive explanations",
            4: "May struggle with 'both/and' concepts initially",
            5: "May feel guilty about not being productive during sessions",
            6: "May present different personas in different sessions",
            7: "May resist focusing on self during therapeutic work",
            8: "May worry about betraying family through personal change",
            9: "May lose therapeutic gains in triggering contexts"
        }
        
        return resistance_patterns.get(pattern_id, "Standard therapeutic resistance patterns")

    def _extract_key_words(self, text):
        """Extract key emotional and value words from text"""
        text = str(text).lower()
        
        # Remove common words and extract meaningful terms
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
        
        words = re.findall(r'\b\w+\b', text)
        key_words = [word for word in words if len(word) > 3 and word not in stop_words]
        
        # Return unique words, limited to most relevant
        return list(dict.fromkeys(key_words))[:10]

    def _generate_pattern_suggestions(self, pattern_id, client_language):
        """Generate specific hypnotic suggestions for pattern"""
        base_suggestions = {
            1: [
                "You deserve happiness as much as anyone else",
                "It's safe to feel good about your life",
                "You can be happy while caring about others"
            ],
            2: [
                "You can be strong while working with others",
                "True power comes from collaboration",
                "You lead best when you listen"
            ],
            3: [
                "You can trust wisely and stay safe",
                "Some people are trustworthy and deserving of your openness",
                "Discernment protects you while connection enriches you"
            ],
            4: [
                "You can choose both excellence and humanity",
                "Life offers many possibilities beyond either/or",
                "You find wisdom in the middle ground"
            ],
            5: [
                "Your worth exists in your being, not just your doing",
                "You matter because you exist",
                "Rest and productivity can both serve your life"
            ],
            6: [
                "Your authentic self is welcome everywhere",
                "You can be consistently yourself across all contexts",
                "Authenticity creates deeper connections"
            ],
            7: [
                "Caring for yourself allows you to better serve others",
                "Self-care is an act of love for those who depend on you",
                "You can give generously from a full cup"
            ],
            8: [
                "You can honor your family while following your authentic path",
                "Your happiness brings joy to those who truly love you",
                "Living authentically is the highest honor to your family"
            ],
            9: [
                "Your strength remains constant across all situations",
                "You maintain your power regardless of context",
                "Your boundaries protect both you and others"
            ]
        }
        
        return base_suggestions.get(pattern_id, ["You have the power to change and grow"])

    def _get_somatic_approach(self, physical_response):
        """Get somatic approach based on client's physical response description"""
        response_lower = str(physical_response).lower()
        
        if 'chest' in response_lower or 'heart' in response_lower:
            return "Heart-centered breathing and cardiac coherence"
        elif 'stomach' in response_lower or 'gut' in response_lower:
            return "Digestive calm and gut-brain harmony"
        elif 'tension' in response_lower or 'tight' in response_lower:
            return "Progressive relaxation and muscle release"
        elif 'energy' in response_lower:
            return "Energy regulation and vitality balancing"
        else:
            return "General somatic regulation and body awareness"

    def _generate_client_metaphors(self, responses, pattern_scores):
        """Generate client-appropriate metaphors and imagery"""
        metaphors = []
        
        # Extract imagery preferences from responses
        nature_words = []
        action_words = []
        
        for response_data in responses.values():
            response_text = str(response_data.get('response', '')).lower()
            
            if any(word in response_text for word in ['nature', 'tree', 'water', 'ocean', 'mountain', 'garden', 'forest']):
                nature_words.append('nature')
            
            if any(word in response_text for word in ['build', 'create', 'make', 'construct', 'develop']):
                action_words.append('building')
        
        # Pattern-specific metaphors
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            
            if 'nature' in nature_words:
                metaphors.append(f"Like a garden that needs both sun and rain to grow")
                metaphors.append(f"Strong like a tree that bends but doesn't break")
            
            if 'building' in action_words:
                metaphors.append(f"Building new pathways like constructing a bridge")
                metaphors.append(f"Creating change like an architect designing a new foundation")
            
            # Default metaphors for each pattern
            pattern_metaphors = {
                1: "Allowing happiness like opening curtains to let in natural light",
                2: "Finding strength in collaboration like musicians in harmony",
                3: "Building trust like creating a secure foundation",
                4: "Embracing both/and like a river flowing around obstacles",
                5: "Recognizing inherent worth like appreciating a beautiful sunset",
                6: "Authentic expression like a flower blooming naturally",
                7: "Balanced care like breathing in and breathing out",
                8: "Honoring family while being authentic like branches growing from strong roots",
                9: "Consistent strength like a lighthouse steady in all weather"
            }
            
            metaphors.append(pattern_metaphors.get(dominant_pattern, "Growing and changing like nature's seasons"))
        
        return metaphors[:4]  # Return top 4 metaphors

    # Continue with enhanced helper methods...

    def _assess_comprehensive_risk_level(self, risk_flags, pattern_scores):
        """Comprehensive risk assessment including pattern severity"""
        risk_count = len(risk_flags)
        pattern_severity = max(pattern_scores.values()) if pattern_scores else 0
        high_risk_patterns = [pid for pid, score in pattern_scores.items() if score >= 8] if pattern_scores else []
        
        if risk_count >= 4 or pattern_severity >= 12:
            return "CRITICAL - Immediate specialized intervention required"
        elif risk_count >= 3 or pattern_severity >= 10 or len(high_risk_patterns) >= 2:
            return "HIGH - Intensive clinical approach needed"
        elif risk_count >= 2 or pattern_severity >= 8:
            return "ELEVATED - Modified protocols with safety measures"
        elif risk_count >= 1 or pattern_severity >= 6:
            return "MODERATE - Standard approach with precautions"
        else:
            return "LOW - Standard hypnotherapy approach suitable"

    def _format_enhanced_risk_analysis(self, risk_flags, pattern_scores):
        """Format comprehensive risk analysis"""
        analysis = ""
        
        if risk_flags:
            analysis += "IDENTIFIED RISK FACTORS:\n"
            for i, flag in enumerate(risk_flags, 1):
                risk_desc = self._get_enhanced_risk_description(flag)
                management = self._get_enhanced_risk_management(flag)
                analysis += f"{i}. {risk_desc}\n"
                analysis += f"   └─ Management Protocol: {management}\n"
            analysis += "\n"
        
        # Pattern-based risk assessment
        if pattern_scores:
            high_risk_patterns = [(pid, score) for pid, score in pattern_scores.items() if score >= 8]
            if high_risk_patterns:
                analysis += "HIGH INTENSITY PATTERNS (Clinical Caution Required):\n"
                for pattern_id, score in high_risk_patterns:
                    pattern_name = self.pattern_analysis.get(pattern_id, {}).get('name', f'Pattern {pattern_id}')
                    analysis += f"• {pattern_name} (Score: {score:.1f}) - Requires specialized approach\n"
                analysis += "\n"
        
        if not risk_flags and not any(score >= 6 for score in pattern_scores.values() if pattern_scores):
            analysis += "✅ No significant risk factors identified - standard approach suitable\n"
        
        return analysis

    def _get_enhanced_risk_description(self, flag):
        """Enhanced risk factor descriptions"""
        descriptions = {
            'risk_q_10': "Current medical/mental health care - Coordination with existing providers required",
            'risk_q_11': "High emotional intensity - Emotional regulation capacity assessment needed",
            'risk_q_12': "Dissociation/panic/self-harm history - Comprehensive safety protocols required",
            'risk_q_13': "Substance use patterns - Sobriety considerations and timing assessment",
            'high_pattern_intensity': "Severe pattern entrenchment - Extended session protocols may be needed"
        }
        return descriptions.get(flag, f"Unspecified risk factor: {flag}")

    def _get_enhanced_risk_management(self, flag):
        """Enhanced risk management protocols"""
        management = {
            'risk_q_10': "Contact existing providers before sessions, coordinate treatment approach",
            'risk_q_11': "Implement grounding techniques, shorter initial sessions, emotion regulation focus",
            'risk_q_12': "Establish safety plan, provide crisis resources, use stabilization-first approach",
            'risk_q_13': "Assess current substance use, consider timing of intervention, safety monitoring",
            'high_pattern_intensity': "Extended assessment phase, gradual approach, additional support sessions"
        }
        return management.get(flag, "Standard clinical safety precautions")

    def _get_enhanced_contact_timeline(self, urgency, risk_flags, pattern_scores):
        """Enhanced contact timeline considering all factors"""
        risk_count = len(risk_flags)
        pattern_severity = max(pattern_scores.values()) if pattern_scores else 0
        
        if risk_count >= 3 or pattern_severity >= 10:
            return "IMMEDIATE - Contact within 12 hours for comprehensive assessment"
        elif 'extremely urgent' in urgency.lower() or risk_count >= 2:
            return "PRIORITY - Contact within 24 hours for urgent scheduling"
        elif 'very urgent' in urgency.lower() or pattern_severity >= 8:
            return "ELEVATED - Contact within 48 hours for prompt response"
        else:
            return "STANDARD - Contact within 72 hours for routine follow-up"

    def _get_enhanced_response_protocol(self, next_step, pattern_scores):
        """Enhanced response protocol based on patterns and preferences"""
        base_response = self._get_standard_response_protocol(next_step)
        
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            
            # Pattern-specific response modifications
            if dominant_pattern in [2, 3]:  # Power struggles, Mistrust
                return base_response + " - Use collaborative, transparent communication approach"
            elif dominant_pattern in [1, 7]:  # Unhappiness, Self-sacrifice
                return base_response + " - Use gentle, permission-based communication"
            elif dominant_pattern in [4, 5]:  # Binary thinking, Doing vs Being
                return base_response + " - Provide multiple options and flexible scheduling"
            else:
                return base_response + " - Standard professional communication approach"
        
        return base_response

    def _get_standard_response_protocol(self, next_step):
        """Standard response protocol"""
        if 'consult' in next_step.lower():
            return "Schedule free consultation call via provided contact information"
        elif 'package' in next_step.lower():
            return "Send transformation package information and detailed pricing"
        elif 'analysis' in next_step.lower():
            return "Email comprehensive analysis with specific therapeutic recommendations"
        else:
            return "Initiate personalized contact based on assessment findings"

    def _get_specific_session_preparation(self, pattern_scores, risk_flags):
        """Get specific session preparation based on patterns and risks"""
        if len(risk_flags) >= 2:
            return "Prepare comprehensive safety protocols and crisis intervention resources"
        
        if pattern_scores:
            dominant_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
            pattern_info = self.pattern_analysis.get(dominant_pattern, {})
            
            preparation_notes = {
                1: "Prepare permission-based language, avoid overwhelming positivity",
                2: "Prepare collaborative approach, avoid directive commands or authority positioning",
                3: "Prepare transparent explanations, provide evidence-based rationales for all techniques",
                4: "Prepare integration work, use both/and language instead of either/or framing",
                5: "Prepare being-centered work, separate worth from productivity in all interactions",
                6: "Prepare authenticity integration, support consistent identity across contexts",
                7: "Prepare balanced care approach, reframe self-care as service to others",
                8: "Prepare family honor work, support authentic path while maintaining love connections",
                9: "Prepare context-independent strength building, consistent boundary maintenance"
            }
            
            return preparation_notes.get(dominant_pattern, f"Prepare specialized approach for {pattern_info.get('name', 'identified pattern')}")
        
        return "Prepare individualized approach based on assessment findings"

    def _assess_therapeutic_confidence(self, completion, pattern_count, risk_flags):
        """Assess therapeutic confidence based on data quality"""
        if completion >= 90 and pattern_count >= 2 and len(risk_flags) <= 1:
            return "HIGH - Comprehensive data enables targeted, confident intervention"
        elif completion >= 75 and pattern_count >= 1:
            return "GOOD - Adequate data for effective treatment planning and execution"
        elif completion >= 60:
            return "MODERATE - Sufficient data for standard approach with ongoing assessment"
        else:
            return "LIMITED - Recommend additional assessment for optimization"

    def _assess_enhanced_data_integrity(self, responses, trigger_chain):
        """Assess data integrity including behavioral chain completeness"""
        response_quality = len(responses)
        chain_completeness = len(trigger_chain) if trigger_chain else 0
        
        if response_quality >= 20 and chain_completeness >= 5:
            return "EXCELLENT - Comprehensive responses with complete behavioral mapping"
        elif response_quality >= 15 and chain_completeness >= 3:
            return "GOOD - Strong response set with adequate behavioral chain data"
        elif response_quality >= 10:
            return "FAIR - Basic response coverage, focus on available high-quality data"
        else:
            return "LIMITED - Recommend supplemental assessment for complete picture"

    def _assess_intervention_complexity(self, pattern_scores, risk_flags):
        """Assess intervention complexity level"""
        pattern_count = len(pattern_scores) if pattern_scores else 0
        max_score = max(pattern_scores.values()) if pattern_scores else 0
        risk_count = len(risk_flags)
        
        if pattern_count >= 3 and max_score >= 8 and risk_count >= 2:
            return "COMPLEX - Multi-pattern, high-intensity case requiring extended protocols"
        elif pattern_count >= 2 and max_score >= 6:
            return "MODERATE - Standard complexity with pattern-specific modifications"
        elif pattern_count >= 1:
            return "STANDARD - Single pattern focus with straightforward intervention"
        else:
            return "SIMPLE - Surface-level intervention may be sufficient"

    def _recommend_enhanced_therapist_type(self, risk_flags, pattern_scores):
        """Recommend therapist type based on complexity"""
        risk_count = len(risk_flags)
        pattern_complexity = len(pattern_scores) if pattern_scores else 0
        max_intensity = max(pattern_scores.values()) if pattern_scores else 0
        
        if risk_count >= 3 or max_intensity >= 10:
            return "Licensed clinical psychologist with advanced hypnotherapy specialization"
        elif risk_count >= 2 or pattern_complexity >= 3:
            return "Licensed clinical hypnotherapist with trauma-informed training"
        elif max_intensity >= 8:
            return "Experienced rapid-change hypnotherapist with pattern specialization"
        else:
            return "Certified clinical hypnotherapist with standard training"

    def _recommend_session_timing(self, pattern_scores, urgency):
        """Recommend optimal session timing"""
        if 'extremely urgent' in urgency.lower():
            return "Sessions within 48-72 hours, same week completion preferred"
        elif pattern_scores and max(pattern_scores.values()) >= 8:
            return "Sessions within 1 week, allow time for integration between sessions"
        else:
            return "Standard timing: Sessions within 1-2 weeks, normal integration time"

    def _recommend_follow_up_protocol(self, pattern_scores, risk_flags):
        """Recommend follow-up protocol"""
        risk_count = len(risk_flags)
        complexity = len(pattern_scores) if pattern_scores else 0
        
        if risk_count >= 2:
            return "Weekly check-ins for 1 month, then monthly for 3 months"
        elif complexity >= 3:
            return "2-week check-in, then monthly for 6 months"
        else:
            return "1-month check-in, then 3-month follow-up"

    def _format_detailed_response_analysis(self, responses, intensity, trigger_chain):
        """Format detailed analysis of all client responses"""
        analysis = "DETAILED CLIENT RESPONSE TRANSCRIPT:\n\n"
        
        # Organize responses by category
        trigger_responses = []
        pattern_responses = []
        chain_responses = []
        intensity_responses = []
        
        for q_id in sorted(responses.keys()):
            response_data = responses[q_id]
            question_text = response_data.get('question_text', f'Question {q_id}')
            response = response_data.get('response', 'No response provided')
            timestamp = response_data.get('timestamp', 'Unknown time')
            
            # Categorize responses
            if 'trigger' in question_text.lower():
                trigger_responses.append((q_id, question_text, response))
            elif any(word in question_text.lower() for word in ['pattern', 'behavior', 'response']):
                pattern_responses.append((q_id, question_text, response))
            elif 'chain' in question_text.lower() or q_id in trigger_chain:
                chain_responses.append((q_id, question_text, response))
            
            # Add intensity if available
            if q_id in intensity:
                intensity_responses.append((q_id, intensity[q_id]))
        
        # Format categorized responses
        if trigger_responses:
            analysis += "TRIGGER & SITUATIONAL RESPONSES:\n"
            for q_id, question, response in trigger_responses:
                analysis += f"{q_id}. {question}\n"
                analysis += f"   Client Response: \"{response}\"\n"
                if q_id in intensity:
                    analysis += f"   Intensity Rating: {intensity[q_id]}/7\n"
                analysis += "\n"
        
        if pattern_responses:
            analysis += "BEHAVIORAL PATTERN RESPONSES:\n"
            for q_id, question, response in pattern_responses:
                analysis += f"{q_id}. {question}\n"
                analysis += f"   Client Response: \"{response}\"\n"
                if q_id in intensity:
                    analysis += f"   Intensity Rating: {intensity[q_id]}/7\n"
                analysis += "\n"
        
        # Complete response transcript
        analysis += "COMPLETE RESPONSE TRANSCRIPT:\n"
        for q_id in sorted(responses.keys()):
            response_data = responses[q_id]
            question_text = response_data.get('question_text', f'Question {q_id}')
            response = response_data.get('response', 'No response')
            
            analysis += f"\n{q_id}. {question_text}\n"
            analysis += f"   Response: {response}\n"
            
            if q_id in intensity:
                analysis += f"   Intensity: {intensity[q_id]}/7\n"
            
            analysis += f"   Timestamp: {response_data.get('timestamp', 'Unknown')}\n"
        
        return analysis

    def _generate_fallback_email(self, data, error_info):
        """Generate fallback email when main formatting fails"""
        contact = data.get('contact_info', {})
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
CLINICAL ASSESSMENT RESULTS - FALLBACK FORMAT
Generated: {timestamp}

ERROR NOTICE: Enhanced formatting encountered an issue: {error_info}
Raw assessment data preserved below for manual clinical review.

═══════════════════════════════════════════

CLIENT INFORMATION:
Name: {contact.get('name', 'Unknown')}
Email: {contact.get('email', 'Unknown')}
Phone: {contact.get('phone', 'Not provided')}
Primary Concern: {contact.get('primary_concern', 'Not provided')}
Urgency: {contact.get('urgency', 'Not specified')}

═══════════════════════════════════════════

ASSESSMENT DATA AVAILABLE:
- Contact Information: {len(contact)} fields
- Assessment Results: {len(data.get('assessment_results', {}))} data points
- Response Count: {len(data.get('assessment_responses', {}))} responses
- Pattern Scores: {len(data.get('pattern_scores', {}))} patterns identified
- Risk Flags: {len(data.get('risk_flags', []))} risk factors
- Intensity Data: {len(data.get('intensity_responses', {}))} intensity ratings

RECOMMENDED ACTION:
Manual review of complete assessment data required.
Contact client within 48 hours for standard follow-up.
All raw data preserved for clinical analysis.

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Clinical Assessment System
Error Recovery Mode - Manual Review Required
        """

    # ==========================================
    # STANDARD BOOKING EMAIL METHODS (UNCHANGED)
    # ==========================================

    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification - MAINTAINS COMPATIBILITY"""
        try:
            print("[DEBUG] Sending discovery call email")
            
            name = booking_data.get('name', '')
            email = booking_data.get('email', '')
            concern = booking_data.get('concern', '')
            message = booking_data.get('concern_description', '') or booking_data.get('message', '')
            urgency = booking_data.get('urgency', '')
            selected_package = booking_data.get('selected_package', '')
            
            subject = f"📞 New Discovery Call Request - {name}"
            body = self._format_discovery_call_body(name, email, concern, message, urgency, selected_package)
            
            return self._send_email(subject, body, "Discovery Call")
            
        except Exception as e:
            print(f"[ERROR] Discovery call email error: {e}")
            return False

    def _format_discovery_call_body(self, name, email, concern, message, urgency, selected_package):
        """Format discovery call email - UNCHANGED"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if urgency and 'extremely urgent' in urgency.lower():
            priority = "🔴 HIGH PRIORITY"
        elif urgency and 'very urgent' in urgency.lower():
            priority = "🟡 PRIORITY"
        else:
            priority = "📋 STANDARD"
        
        return f"""
{priority} DISCOVERY CALL REQUEST
Received: {timestamp}

═══════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}

🎯 CONCERN DETAILS:
Primary Concern: {concern}
Urgency Level: {urgency or 'Not specified'}
Selected Package: {selected_package or 'None'}

💬 CLIENT MESSAGE:
{message or 'No additional message provided'}

📞 ACTION REQUIRED:
Contact Timeline: {self._get_simple_contact_timeline(urgency)}

RECOMMENDED APPROACH:
1. {self._get_discovery_approach(concern, urgency)}
2. Assess suitability for rapid transformation method
3. Explain 2-session approach if appropriate
4. Schedule Session 1 if client is ready to proceed

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Discovery Call System
        """

    def send_booking_email(self, name, email, concern, message, booking_type):
        """Send standard booking notification - MAINTAINS COMPATIBILITY"""
        try:
            print(f"[DEBUG] Sending {booking_type} booking email")
            
            subject = f"📞 New {booking_type} Request - {name}"
            body = self._format_standard_booking_body(name, email, concern, message, booking_type)
            
            return self._send_email(subject, body, booking_type)
            
        except Exception as e:
            print(f"[ERROR] Booking email error: {e}")
            return False

    def _format_standard_booking_body(self, name, email, concern, message, booking_type):
        """Format standard booking email - UNCHANGED"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
📞 NEW {booking_type.upper()} REQUEST
Received: {timestamp}

═══════════════════════════════════════════

👤 CONTACT INFORMATION:
Name: {name}
Email: {email}

🎯 CONCERN DETAILS:
Primary Concern: {concern}
Message: {message}

📞 NEXT STEPS:
Please contact this person within 24-48 hours to schedule their {booking_type.lower()}.

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Automated Booking System
        """

    def send_package_booking_email(self, booking_data):
        """Send transformation package booking notification - UNCHANGED"""
        try:
            name = booking_data.get('name', '')
            email = booking_data.get('email', '')
            concern = booking_data.get('concern', '')
            message = booking_data.get('message', '')
            package_type = booking_data.get('package_type', '')
            
            subject = f"💰 New Transformation Package Booking - {name}"
            body = self._format_package_booking_body(name, email, concern, message, package_type)
            
            return self._send_email(subject, body, "Package Booking")
            
        except Exception as e:
            print(f"[ERROR] Package booking email error: {e}")
            return False

    def _format_package_booking_body(self, name, email, concern, message, package_type):
        """Format package booking email - UNCHANGED"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""
💰 TRANSFORMATION PACKAGE BOOKING
Received: {timestamp}

═══════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}

📦 PACKAGE DETAILS:
Selected Package: {package_type}
Primary Concern: {concern}

💬 CLIENT MESSAGE:
{message}

📞 HIGH PRIORITY ACTION REQUIRED:
This client is ready to proceed with transformation package.

IMMEDIATE STEPS:
1. Send welcome email with package confirmation
2. Schedule Session 1 within 48-72 hours
3. Send pre-session preparation materials
4. Confirm payment method and schedule

💰 EXPECTED REVENUE: 3,000-4,000 THB

═══════════════════════════════════════════
Bangkok Hypnotherapy Clinic
Package Booking System
        """

    # ==========================================
    # EMAIL SENDING INFRASTRUCTURE (UNCHANGED)
    # ==========================================

    def _send_email(self, subject, body, email_type):
        """Send email via Gmail SMTP - UNCHANGED"""
        try:
            if not self.password:
                print(f"[SIMULATE] {email_type} email (no password configured)")
                print(f"[SIMULATE] To: {self.recipient_email}")
                print(f"[SIMULATE] Subject: {subject}")
                print(f"[SIMULATE] Body preview: {body[:200]}...")
                return True
            
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            
            print(f"[SUCCESS] {email_type} email sent successfully")
            return True
            
        except Exception as e:
            print(f"[ERROR] SMTP error for {email_type}: {e}")
            return False

    # ==========================================
    # SIMPLE HELPER METHODS (UNCHANGED)
    # ==========================================

    def _get_simple_contact_timeline(self, urgency):
        """Get simple contact timeline for booking emails - UNCHANGED"""
        if urgency and 'extremely urgent' in urgency.lower():
            return "Within 24 hours (high priority)"
        elif urgency and 'very urgent' in urgency.lower():
            return "Within 48 hours (priority)"
        else:
            return "Within 72 hours (standard)"

    def _get_discovery_approach(self, concern, urgency):
        """Get recommended approach for discovery call - UNCHANGED"""
        if concern and 'anxiety' in concern.lower():
            return "Use calm, reassuring approach - explain safety of hypnotherapy"
        elif concern and 'smoking' in concern.lower():
            return "Focus on rapid cessation method - emphasize 2-session success rate"
        elif concern and 'habit' in concern.lower():
            return "Explain pattern interruption approach - assess habit specifics"
        elif urgency and 'extremely urgent' in urgency.lower():
            return "Acknowledge urgency, assess suitability for immediate scheduling"
        else:
            return "Standard discovery call approach - assess suitability and explain method"


# ==========================================
# GLOBAL INSTANCE AND API FUNCTIONS
# ==========================================

# Global instance
comprehensive_email_handler = ComprehensiveEmailHandler()

# ====== MAIN FUNCTIONS CALLED BY OTHER MODULES ======

def send_clinical_assessment_results(assessment_data):
    """Send enhanced clinical assessment results - MAIN FUNCTION for assess.py"""
    try:
        print("[DEBUG] Sending enhanced clinical assessment results")
        return comprehensive_email_handler.send_clinical_assessment_results(assessment_data)
    except Exception as e:
        print(f"[ERROR] Exception in enhanced clinical assessment email: {e}")
        return False

def send_discovery_call_email(booking_data):
    """Send discovery call booking notification - CALLED BY booking_form.py"""
    try:
        print("[DEBUG] Sending discovery call email")
        return comprehensive_email_handler.send_discovery_call_email(booking_data)
    except Exception as e:
        print(f"[ERROR] Exception in discovery call email: {e}")
        return False

def send_booking_email(name, email, concern, message, booking_type):
    """Send standard booking email - MAINTAINS COMPATIBILITY"""
    try:
        print(f"[DEBUG] Sending {booking_type} booking email")
        return comprehensive_email_handler.send_booking_email(name, email, concern, message, booking_type)
    except Exception as e:
        print(f"[ERROR] Exception in booking email: {e}")
        return False

def send_package_booking_email(booking_data):
    """Send package booking notification - UNCHANGED"""
    try:
        print("[DEBUG] Sending package booking email")
        return comprehensive_email_handler.send_package_booking_email(booking_data)
    except Exception as e:
        print(f"[ERROR] Exception in package booking email: {e}")
        return False

# ====== BACKWARD COMPATIBILITY FUNCTIONS ======

def send_assessment_results_email(data):
    """Backward compatibility for assessment results"""
    return send_clinical_assessment_results(data)

def send_contact_form_email(data):
    """Backward compatibility for contact forms"""
    booking_data = {
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'concern': data.get('concern', ''),
        'message': data.get('message', ''),
        'urgency': data.get('urgency', ''),
        'experience': data.get('experience', '')
    }
    return send_discovery_call_email(booking_data)

def send_booking_confirmation_email(data):
    """Backward compatibility for booking confirmations"""
    return send_discovery_call_email(data)
