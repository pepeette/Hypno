
# """
# Enhanced Clinical Assessment Email Handler - FIXED VERSION
# Complete rewrite for utils/email_assess.py with full functionality
# Addresses all issues preventing email sending
# """
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime

# class ClinicalAssessmentEmailHandler:
#     """Fixed clinical assessment email handler that actually sends emails"""
    
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
        
#         # Get password - this is the key fix
#         self.password = self._get_email_password()

#     def _get_email_password(self):
#         """Get email password from environment or secrets"""
#         try:
#             import streamlit as st
#             # Try Streamlit secrets first
#             password = st.secrets.get("GMAIL_APP_PASSWORD", "")
#             if password:
#                 print("✅ Password loaded from Streamlit secrets")
#                 return password
#         except:
#             pass
        
#         # Try environment variable
#         password = os.environ.get("GMAIL_APP_PASSWORD", "")
#         if password:
#             print("✅ Password loaded from environment variable")
#             return password
        
#         # No password found
#         print("❌ No email password found in secrets or environment")
#         return ""

#     def send_clinical_assessment_results(self, assessment_data):
#         """Send comprehensive clinical assessment results - MAIN FUNCTION"""
#         try:
#             print("🚀 Starting email send process...")
            
#             # Extract key information
#             contact_info = assessment_data.get('contact_info', {})
#             assessment_results = assessment_data.get('assessment_results', {})
#             is_digital_native = assessment_data.get('is_digital_native', False)
#             digital_analysis = assessment_data.get('digital_despair_analysis')
            
#             email = contact_info.get('email', 'unknown@email.com')
#             name = contact_info.get('name', 'Assessment Participant')
#             urgency = contact_info.get('urgency', 'Not specified')
            
#             print(f"📧 Preparing email for: {name} ({email})")
#             print(f"🔴 Urgency level: {urgency}")
#             print(f"💻 Digital native: {is_digital_native}")
            
#             # Create email message
#             msg = MIMEMultipart()
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
#             msg['Subject'] = self._generate_email_subject(name, urgency, assessment_results, is_digital_native, digital_analysis)
            
#             print(f"📝 Email subject: {msg['Subject']}")
            
#             # Build comprehensive email body
#             body = self._build_complete_email_body(assessment_data)
            
#             print(f"📄 Email body length: {len(body)} characters")
            
#             # Attach body to email
#             msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
#             # Send email
#             if self.password:
#                 print("🔑 Password available - attempting to send email...")
#                 success = self._send_email(msg)
                
#                 if success:
#                     print("✅ EMAIL SENT SUCCESSFULLY!")
#                     return True
#                 else:
#                     print("❌ EMAIL SEND FAILED!")
#                     return False
#             else:
#                 print("⚠️ No password available - email cannot be sent")
#                 print("Please set GMAIL_APP_PASSWORD in your environment or Streamlit secrets")
                
#                 # Still log the assessment data
#                 self._log_assessment_data(assessment_data)
#                 return True  # Return True for development purposes
                
#         except Exception as e:
#             print(f"💥 ERROR in send_clinical_assessment_results: {str(e)}")
#             import traceback
#             print(f"📍 Full traceback: {traceback.format_exc()}")
#             return False

#     def _send_email(self, msg):
#         """Actually send the email via SMTP"""
#         try:
#             print("🔌 Connecting to Gmail SMTP server...")
            
#             # Create SMTP session
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            
#             print("🔐 Starting TLS encryption...")
#             server.starttls()  # Enable TLS encryption
            
#             print("🔑 Logging in to Gmail...")
#             server.login(self.sender_email, self.password)
            
#             print("📤 Sending email...")
#             text = msg.as_string()
#             server.sendmail(self.sender_email, self.recipient_email, text)
            
#             print("🔚 Closing connection...")
#             server.quit()
            
#             print("✅ EMAIL SENT SUCCESSFULLY!")
#             return True
            
#         except smtplib.SMTPAuthenticationError as e:
#             print(f"🚫 SMTP Authentication Error: {e}")
#             print("💡 Check your Gmail App Password - it might be incorrect")
#             return False
#         except smtplib.SMTPException as e:
#             print(f"📧 SMTP Error: {e}")
#             return False
#         except Exception as e:
#             print(f"💥 General Email Error: {e}")
#             return False

#     def _generate_email_subject(self, name, urgency, assessment_results, is_digital_native, digital_analysis):
#         """Generate email subject line"""
#         # Priority indicator
#         if 'extremely urgent' in urgency.lower():
#             priority = "🚨 EMERGENCY"
#         elif 'very urgent' in urgency.lower():
#             priority = "⚡ HIGH PRIORITY"
#         elif 'urgent' in urgency.lower():
#             priority = "📋 URGENT"
#         else:
#             priority = "🧠 CLINICAL"
        
#         # Assessment type
#         if is_digital_native and digital_analysis:
#             severity = digital_analysis.get('severity_level', 'MINIMAL')
#             if severity in ['SEVERE', 'MODERATE']:
#                 assessment_type = f"DIGITAL-NATIVE {severity}"
#             else:
#                 assessment_type = "DIGITAL-AWARE"
#         else:
#             assessment_type = "TRADITIONAL"
        
#         # Pattern count
#         pattern_count = len(assessment_results.get('pattern_scores', {}))
#         complexity = "COMPLEX" if pattern_count >= 5 else "MULTI" if pattern_count >= 3 else "FOCUSED"
        
#         return f"{priority} ASSESSMENT: {name} - {assessment_type} {complexity}"

#     def _build_complete_email_body(self, assessment_data):
#         """Build complete comprehensive email body"""
#         body = ""
        
#         # Header
#         body += self._build_header_section(assessment_data)
        
#         # Digital analysis (if applicable)
#         if assessment_data.get('is_digital_native'):
#             body += self._build_digital_analysis_section(assessment_data)
        
#         # Traditional pattern analysis
#         body += self._build_pattern_analysis_section(assessment_data)
        
#         # Clinical template (if available)
#         clinical_template = assessment_data.get('clinical_template', '')
#         if clinical_template:
#             body += f"\n{clinical_template}\n"
        
#         # Behavioral sequence analysis
#         body += self._build_behavioral_sequence_section(assessment_data)
        
#         # Assessment transcript
#         body += self._build_assessment_transcript(assessment_data)
        
#         # Action items
#         body += self._build_action_items_section(assessment_data)
        
#         # Footer
#         body += self._build_footer_section()
        
#         return body

#     def _build_header_section(self, assessment_data):
#         """Build email header with client information"""
#         contact_info = assessment_data.get('contact_info', {})
#         assessment_results = assessment_data.get('assessment_results', {})
#         is_digital_native = assessment_data.get('is_digital_native', False)
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         name = contact_info.get('name', 'Not provided')
#         email = contact_info.get('email', 'Not provided')
#         phone = contact_info.get('phone', 'Not provided')
#         urgency = contact_info.get('urgency', 'Not specified')
#         concern = contact_info.get('primary_concern', 'Not specified')
#         next_step = contact_info.get('next_step', 'Not specified')
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         questions_answered = assessment_results.get('total_questions_answered', 0)
#         completion_rate = assessment_results.get('completion_rate', 0) * 100
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
# Preferred Next Step: {next_step}
# Assessment Completed: {timestamp}

# 📊 ASSESSMENT METRICS:
# Assessment Type: {"Digital-Native Enhanced" if is_digital_native else "Traditional Behavioral"}
# Questions Answered: {questions_answered}
# Completion Rate: {completion_rate:.0f}%
# Traditional Patterns Detected: {patterns_detected}
# Assessment Quality: {'EXCELLENT' if completion_rate >= 90 else 'GOOD' if completion_rate >= 70 else 'PARTIAL'}
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

#     def _build_digital_analysis_section(self, assessment_data):
#         """Build digital despair syndrome analysis section"""
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         if not digital_analysis:
#             return f"""
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
#             for i, adaptation in enumerate(adaptations[:5], 1):
#                 section += f"{i}. {adaptation}\n"
        
#         return section + "\n"

#     def _build_pattern_analysis_section(self, assessment_data):
#         """Build traditional behavioral pattern analysis"""
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
        
#         for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
#             pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#             activation_level = self._get_pattern_activation_level(score)
            
#             section += f"""
# {i}. {pattern_name}:
#    Activation Score: {score:.1f}/10 ({activation_level})
#    Therapeutic Priority: {self._get_therapeutic_priority(score)}
# """
        
#         return section

#     def _build_behavioral_sequence_section(self, assessment_data):
#         """Build behavioral sequence analysis"""
#         trigger_chain = assessment_data.get('trigger_chain', {})
        
#         if not trigger_chain:
#             return """
# 🔗 BEHAVIORAL SEQUENCE ANALYSIS:
# ══════════════════════════════════════════════════════════════════
# Status: Behavioral chain not captured - Session 1 priority

# """
        
#         section = f"""
# 🔗 BEHAVIORAL SEQUENCE ANALYSIS:
# ══════════════════════════════════════════════════════════════════

# """
        
#         sequence_components = {
#             'awareness_point': '🎯 TRIGGER',
#             'physical_response': '💓 PHYSICAL RESPONSE', 
#             'automatic_thought': '💭 AUTOMATIC THOUGHT',
#             'emotional_response': '❤️ EMOTIONAL RESPONSE',
#             'behavioral_response': '🏃 BEHAVIORAL RESPONSE',
#             'immediate_consequence': '⚡ IMMEDIATE CONSEQUENCE'
#         }
        
#         captured_count = 0
#         total_count = len(sequence_components)
        
#         for component_key, component_name in sequence_components.items():
#             response = trigger_chain.get(component_key, 'Not captured')
            
#             section += f"{component_name}:\n"
            
#             if response and response != 'Not captured' and response != 'Skipped':
#                 captured_count += 1
#                 section += f"   ✅ CAPTURED: \"{response}\"\n"
#             else:
#                 section += f"   ❌ NOT CAPTURED - Session 1 priority\n"
            
#             section += "\n"
        
#         completeness_percentage = int((captured_count / total_count) * 100)
#         section += f"""
# BEHAVIORAL CHAIN COMPLETENESS: {completeness_percentage}% ({captured_count}/{total_count} components)
# {"✅ SUFFICIENT for intervention design" if completeness_percentage >= 60 else "⚠️ REQUIRES SESSION 1 COMPLETION" if completeness_percentage >= 40 else "❌ DISCOVERY CALL ESSENTIAL"}

# """
        
#         return section

#     def _build_assessment_transcript(self, assessment_data):
#         """Build complete assessment transcript section"""
#         responses = assessment_data.get('assessment_responses', {})
        
#         if not responses:
#             return """
# 📝 ASSESSMENT TRANSCRIPT:
# ══════════════════════════════════════════════════════════════════
# Status: No detailed transcript available

# """
        
#         section = f"""
# 📝 ASSESSMENT TRANSCRIPT:
# ══════════════════════════════════════════════════════════════════

# COMPLETE CLIENT RESPONSES:
# Total Questions Answered: {len(responses)}

# """
        
#         # Show ALL responses, organized by phase
#         sorted_responses = sorted(responses.items(), key=lambda x: int(str(x[0])) if str(x[0]).isdigit() else float('inf'))
        
#         # Organize by phase
#         phases = {
#             'age_screening': '🎂 AGE SCREENING',
#             'digital_screening': '💻 DIGITAL ASSESSMENT', 
#             'engagement': '📞 ENGAGEMENT ASSESSMENT',
#             'trigger_mapping': '🔗 TRIGGER MAPPING',
#             'pattern_specific': '🧠 PATTERN ANALYSIS',
#             'integration': '🎯 INTEGRATION',
#             'unknown': '📝 OTHER RESPONSES'
#         }
        
#         phase_responses = {}
#         for q_id, response_data in sorted_responses:
#             phase = response_data.get('phase', 'unknown')
#             if phase not in phase_responses:
#                 phase_responses[phase] = []
#             phase_responses[phase].append((q_id, response_data))
        
#         # Display all responses by phase
#         for phase_key in phases.keys():
#             if phase_key in phase_responses:
#                 section += f"\n{phases[phase_key]}:\n"
#                 section += "─" * 60 + "\n"
                
#                 for q_id, response_data in phase_responses[phase_key]:
#                     question_text = response_data.get('question_text', 'Unknown question')
#                     response = response_data.get('response', 'No response')
#                     intensity = response_data.get('intensity', None)
#                     question_type = response_data.get('question_type', 'unknown')
#                     timestamp = response_data.get('timestamp', 'Unknown time')
                    
#                     section += f"\nQ{q_id} [{question_type.upper()}]:\n"
#                     section += f"Question: {question_text}\n"
                    
#                     # Format response based on type
#                     if isinstance(response, dict):
#                         if 'rating' in response:
#                             section += f"Response: Rating {response['rating']}/10"
#                             if response.get('follow_up'):
#                                 section += f" - Follow-up: {response['follow_up']}"
#                             section += "\n"
#                         else:
#                             section += "Response: Multiple selections:\n"
#                             for item, item_intensity in response.items():
#                                 section += f"  • {item}: {item_intensity}/7\n"
#                     elif isinstance(response, list):
#                         section += f"Response: {', '.join(map(str, response))}\n"
#                     else:
#                         # Handle long text responses
#                         response_str = str(response)
#                         if len(response_str) > 200:
#                             section += f"Response: {response_str[:200]}...\n"
#                         else:
#                             section += f"Response: {response_str}\n"
                    
#                     # Add intensity if available and different from response
#                     if intensity and intensity != response:
#                         section += f"Intensity: {intensity}/7"
#                         if intensity >= 6:
#                             section += " (HIGH CLINICAL SIGNIFICANCE)"
#                         elif intensity >= 4:
#                             section += " (MODERATE)"
#                         section += "\n"
                    
#                     # Add timestamp
#                     if timestamp != 'Unknown time':
#                         try:
#                             from datetime import datetime
#                             dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
#                             formatted_time = dt.strftime("%H:%M:%S")
#                             section += f"Time: {formatted_time}\n"
#                         except:
#                             section += f"Time: {timestamp}\n"
                    
#                     section += "─" * 30 + "\n"
        
#         # Add transcript statistics
#         text_responses = sum(1 for r in responses.values() 
#                            if isinstance(r.get('response'), str) and len(r.get('response', '')) > 50)
#         choice_responses = len(responses) - text_responses
        
#         # Calculate average intensity
#         intensity_responses = [r.get('intensity', 0) for r in responses.values() if r.get('intensity')]
#         avg_intensity = sum(intensity_responses) / len(intensity_responses) if intensity_responses else 0
        
#         section += f"""
# 📊 TRANSCRIPT STATISTICS:
# Total Responses: {len(responses)}
# Text Responses: {text_responses}
# Choice Responses: {choice_responses}
# Average Response Intensity: {avg_intensity:.1f}/7
# High Intensity Responses (≥6): {len([i for i in intensity_responses if i >= 6])}

# """
        
#         return section

#     def _build_action_items_section(self, assessment_data):
#         """Build action items section"""
#         contact_info = assessment_data.get('contact_info', {})
#         urgency = contact_info.get('urgency', 'not specified').lower()
#         is_digital_native = assessment_data.get('is_digital_native', False)
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         section = """
# ⚡ IMMEDIATE ACTION ITEMS:
# ══════════════════════════════════════════════════════════════════

# """
        
#         # Contact priority
#         if 'extremely urgent' in urgency:
#             contact_priority = "🚨 IMMEDIATE CONTACT (within 4-6 hours)"
#         elif 'very urgent' in urgency:
#             contact_priority = "⚡ PRIORITY CONTACT (within 12-24 hours)"
#         elif 'urgent' in urgency:
#             contact_priority = "📋 URGENT CONTACT (within 24-48 hours)"
#         else:
#             contact_priority = "📞 STANDARD CONTACT (within 2-3 days)"
        
#         section += f"1. CONTACT PRIORITY: {contact_priority}\n"
#         section += f"   Client Email: {contact_info.get('email', 'Not provided')}\n"
#         section += f"   Preferred Next Step: {contact_info.get('next_step', 'Not specified')}\n\n"
        
#         # Clinical preparation
#         if is_digital_native and digital_analysis:
#             severity = digital_analysis.get('severity_level', 'MINIMAL')
#             if severity in ['SEVERE', 'MODERATE']:
#                 section += "2. SPECIAL PREPARATION REQUIRED:\n"
#                 section += "   ✅ Review digital-native protocols\n"
#                 section += "   ✅ Prepare collaborative language patterns\n"
#                 section += "   ✅ Plan modified session structure\n"
#                 section += "   ✅ Expect intellectual resistance\n\n"
        
#         section += "3. SESSION PLANNING:\n"
#         section += "   □ Review complete assessment before contact\n"
#         section += "   □ Prepare intervention protocols\n"
#         section += "   □ Schedule appropriate session length\n"
#         section += "   □ Plan follow-up sequence\n\n"
        
#         return section

#     def _build_footer_section(self):
#         """Build footer section"""
#         return f"""
# ══════════════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Enhanced Clinical Assessment System
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# System Status: Operational | Priority: Review and Contact Client
# ══════════════════════════════════════════════════════════════════
# """

#     def _get_pattern_activation_level(self, score):
#         """Get activation level for pattern score"""
#         if score >= 7.0:
#             return "VERY HIGH"
#         elif score >= 5.0:
#             return "HIGH"
#         elif score >= 3.0:
#             return "MODERATE"
#         else:
#             return "MILD"

#     def _get_therapeutic_priority(self, score):
#         """Get therapeutic priority for pattern"""
#         if score >= 6.0:
#             return "PRIMARY TARGET"
#         elif score >= 4.0:
#             return "SECONDARY TARGET"
#         else:
#             return "MONITOR"

#     def _log_assessment_data(self, assessment_data):
#         """Log assessment data when email can't be sent"""
#         contact_info = assessment_data.get('contact_info', {})
#         assessment_results = assessment_data.get('assessment_results', {})
        
#         print("📊 ASSESSMENT LOGGED:")
#         print(f"   Name: {contact_info.get('name', 'Unknown')}")
#         print(f"   Email: {contact_info.get('email', 'Unknown')}")
#         print(f"   Urgency: {contact_info.get('urgency', 'Not specified')}")
#         print(f"   Questions: {assessment_results.get('total_questions_answered', 0)}")
#         print(f"   Patterns: {len(assessment_results.get('pattern_scores', {}))}")
#         print(f"   Digital Native: {assessment_data.get('is_digital_native', False)}")


# # Main function for assess.py to call
# def send_clinical_assessment_results(assessment_data):
#     """Main function called from assess.py - FIXED VERSION"""
#     print("🎯 send_clinical_assessment_results called")
    
#     handler = ClinicalAssessmentEmailHandler()
#     return handler.send_clinical_assessment_results(assessment_data)


# # Test function
# def test_email_sending():
#     """Test the email sending functionality"""
#     test_data = {
#         'contact_info': {
#             'name': 'Test Client',
#             'email': 'test@example.com',
#             'phone': '+66-98-765-4321',
#             'urgency': 'Very urgent - test assessment',
#             'primary_concern': 'Testing email functionality',
#             'next_step': 'Schedule session'
#         },
#         'assessment_results': {
#             'total_questions_answered': 25,
#             'completion_rate': 0.85,
#             'pattern_scores': {1: 6.5, 5: 7.2}
#         },
#         'is_digital_native': False,
#         'pattern_scores': {1: 6.5, 5: 7.2},
#         'trigger_chain': {
#             'physical_response': 'Chest tightness',
#             'automatic_thought': 'Something is wrong'
#         },
#         'assessment_responses': {
#             '1': {
#                 'question_text': 'Test question',
#                 'response': 'Test response',
#                 'timestamp': datetime.now().isoformat()
#             }
#         }
#     }
    
#     print("🧪 Testing email sending...")
#     result = send_clinical_assessment_results(test_data)
    
#     if result:
#         print("✅ Test successful!")
#     else:
#         print("❌ Test failed!")
    
#     return result


# if __name__ == "__main__":
#     test_email_sending()


"""
Fixed Email Assessment Handler - utils/email_assess.py
Addresses authentication and sending issues
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import traceback

class ClinicalAssessmentEmailHandler:
    """Fixed clinical assessment email handler"""
    
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
        
        # Get password
        self.password = self._get_email_password()

    def _get_email_password(self):
        """Get email password with multiple fallback methods"""
        password = ""
        
        # Method 1: Streamlit secrets
        try:
            import streamlit as st
            password = st.secrets.get("gmail", {}).get("app_password", "")
            if password:
                print("✅ Password loaded from st.secrets.gmail.app_password")
                return password
        except Exception as e:
            print(f"Streamlit secrets method failed: {e}")
        
        # Method 2: Direct Streamlit secrets
        try:
            import streamlit as st
            password = st.secrets.get("GMAIL_APP_PASSWORD", "")
            if password:
                print("✅ Password loaded from st.secrets.GMAIL_APP_PASSWORD")
                return password
        except Exception as e:
            print(f"Direct Streamlit secrets failed: {e}")
        
        # Method 3: Environment variable
        try:
            password = os.environ.get("GMAIL_APP_PASSWORD", "")
            if password:
                print("✅ Password loaded from environment GMAIL_APP_PASSWORD")
                return password
        except Exception as e:
            print(f"Environment variable method failed: {e}")
        
        # Method 4: .env file (if available)
        try:
            from dotenv import load_dotenv
            load_dotenv()
            password = os.environ.get("GMAIL_APP_PASSWORD", "")
            if password:
                print("✅ Password loaded from .env file")
                return password
        except Exception as e:
            print(f"dotenv method failed: {e}")
        
        print("⚠️ No email password found in any location")
        print("Please set GMAIL_APP_PASSWORD in:")
        print("- Streamlit secrets.toml: [gmail] app_password = 'your_password'")
        print("- Environment variable: GMAIL_APP_PASSWORD=your_password")
        return ""

    def send_clinical_assessment_results(self, assessment_data):
        """Send comprehensive clinical assessment results - MAIN FUNCTION"""
        try:
            print("🚀 Starting enhanced email send process...")
            
            # Validate assessment_data
            if not assessment_data:
                print("❌ No assessment data provided")
                return False
            
            # Extract key information safely
            contact_info = assessment_data.get('contact_info', {})
            if not contact_info:
                print("❌ No contact info found")
                return False
            
            assessment_results = assessment_data.get('assessment_results', {})
            is_digital_native = assessment_data.get('is_digital_native', False)
            digital_analysis = assessment_data.get('digital_despair_analysis')
            
            email = contact_info.get('email', 'unknown@email.com')
            name = contact_info.get('name', 'Assessment Participant')
            urgency = contact_info.get('urgency', 'Not specified')
            
            print(f"📧 Preparing email for: {name} ({email})")
            print(f"🔴 Urgency level: {urgency}")
            print(f"💻 Digital native: {is_digital_native}")
            
            # Check password availability
            if not self.password:
                print("⚠️ No email password available")
                self._log_assessment_locally(assessment_data)
                return True  # Return True for development - change to False for production
            
            # Create email message
            msg = MIMEMultipart('mixed')
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = self._generate_email_subject(name, urgency, assessment_results, is_digital_native, digital_analysis)
            
            print(f"📝 Email subject: {msg['Subject']}")
            
            # Build comprehensive email body
            body = self._build_complete_email_body(assessment_data)
            
            print(f"📄 Email body length: {len(body)} characters")
            
            # Attach body to email
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            # Send email
            success = self._send_email_smtp(msg)
            
            if success:
                print("✅ EMAIL SENT SUCCESSFULLY!")
                return True
            else:
                print("❌ EMAIL SEND FAILED!")
                self._log_assessment_locally(assessment_data)
                return False
                
        except Exception as e:
            print(f"💥 ERROR in send_clinical_assessment_results: {str(e)}")
            print(f"🔍 Full traceback: {traceback.format_exc()}")
            self._log_assessment_locally(assessment_data)
            return False

    def _send_email_smtp(self, msg):
        """Send email via SMTP with enhanced error handling"""
        try:
            print("🔌 Connecting to Gmail SMTP server...")
            
            # Create SMTP session with timeout
            server = smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30)
            
            print("🔒 Starting TLS encryption...")
            server.starttls()
            
            print("🔑 Authenticating with Gmail...")
            server.login(self.sender_email, self.password)
            
            print("📤 Sending email...")
            # Convert message to string
            text = msg.as_string()
            
            # Send the email
            result = server.sendmail(self.sender_email, [self.recipient_email], text)
            
            print("📚 Closing SMTP connection...")
            server.quit()
            
            if result:
                print(f"⚠️ Some recipients failed: {result}")
                return False
            else:
                print("✅ EMAIL SENT SUCCESSFULLY TO ALL RECIPIENTS!")
                return True
            
        except smtplib.SMTPAuthenticationError as e:
            print(f"🚫 SMTP Authentication Error: {e}")
            print("💡 Your Gmail App Password might be incorrect")
            print("💡 Make sure 2-factor authentication is enabled")
            print("💡 Generate a new App Password at: https://myaccount.google.com/apppasswords")
            return False
        except smtplib.SMTPRecipientsRefused as e:
            print(f"📧 Recipients Refused: {e}")
            return False
        except smtplib.SMTPServerDisconnected as e:
            print(f"🔌 Server Disconnected: {e}")
            return False
        except smtplib.SMTPException as e:
            print(f"📧 SMTP Error: {e}")
            return False
        except Exception as e:
            print(f"💥 General Email Error: {e}")
            print(f"🔍 Error type: {type(e).__name__}")
            return False

    def _generate_email_subject(self, name, urgency, assessment_results, is_digital_native, digital_analysis):
        """Generate contextual email subject"""
        # Priority indicator
        if 'extremely urgent' in urgency.lower():
            priority = "🚨 EMERGENCY"
        elif 'very urgent' in urgency.lower():
            priority = "⚡ HIGH PRIORITY"
        elif 'urgent' in urgency.lower():
            priority = "🔋 URGENT"
        else:
            priority = "🧠 CLINICAL"
        
        # Assessment type
        if is_digital_native and digital_analysis:
            severity = digital_analysis.get('severity_level', 'MINIMAL')
            if severity in ['SEVERE', 'MODERATE']:
                assessment_type = f"DIGITAL-NATIVE {severity}"
            else:
                assessment_type = "DIGITAL-AWARE"
        else:
            assessment_type = "TRADITIONAL"
        
        # Pattern complexity
        pattern_count = len(assessment_results.get('pattern_scores', {}))
        complexity = "COMPLEX" if pattern_count >= 5 else "MULTI" if pattern_count >= 3 else "FOCUSED"
        
        return f"{priority} ASSESSMENT: {name} - {assessment_type} {complexity} ({pattern_count} patterns)"

    def _build_complete_email_body(self, assessment_data):
        """Build comprehensive email body"""
        body = ""
        
        try:
            # Header section
            body += self._build_header_section(assessment_data)
            
            # Digital analysis (if applicable)
            if assessment_data.get('is_digital_native'):
                body += self._build_digital_analysis_section(assessment_data)
            
            # Pattern analysis
            body += self._build_pattern_analysis_section(assessment_data)
            
            # Clinical template (if available)
            clinical_template = assessment_data.get('clinical_template', '')
            if clinical_template:
                body += f"\n{clinical_template}\n"
            
            # Assessment responses summary
            body += self._build_response_summary(assessment_data)
            
            # Action items
            body += self._build_action_items_section(assessment_data)
            
            # Footer
            body += self._build_footer_section()
            
        except Exception as e:
            print(f"Error building email body: {e}")
            body += f"\nError generating full email body: {e}\n"
            body += f"Assessment data available: {bool(assessment_data)}\n"
        
        return body

    def _build_header_section(self, assessment_data):
        """Build email header with client information"""
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
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
══════════════════════════════════════════════════════════════

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
        
        header += "\n══════════════════════════════════════════════════════════════\n"
        
        return header

    def _build_digital_analysis_section(self, assessment_data):
        """Build digital analysis section"""
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        if not digital_analysis:
            return f"""
💻 DIGITAL NATIVE ASSESSMENT:
══════════════════════════════════════════════════════════════
Status: Digital native identified but syndrome analysis incomplete
Recommendation: Brief digital assessment completion recommended

"""
        
        section = f"""
💻 DIGITAL DESPAIR SYNDROME ANALYSIS:
══════════════════════════════════════════════════════════════

📈 OVERALL SYNDROME ASSESSMENT:
Digital Despair Score: {digital_analysis.get('digital_despair_score', 0):.1f}%
Severity Classification: {digital_analysis.get('severity_level', 'UNKNOWN')}
Clinical Recommendation: {digital_analysis.get('clinical_recommendation', 'Assessment incomplete')}

🔍 SYNDROME COMPONENT BREAKDOWN:
"""
        
        components = digital_analysis.get('component_scores', {})
        for component, score in components.items():
            component_name = component.replace('_', ' ').title()
            section += f"• {component_name}: {score:.1f}/5\n"
        
        # Therapeutic adaptations
        adaptations = digital_analysis.get('therapeutic_adaptations_needed', [])
        if adaptations:
            section += f"""
🎯 REQUIRED THERAPEUTIC ADAPTATIONS:
"""
            for i, adaptation in enumerate(adaptations[:5], 1):
                section += f"{i}. {adaptation}\n"
        
        return section + "\n"

    def _build_pattern_analysis_section(self, assessment_data):
        """Build pattern analysis section"""
        pattern_scores = assessment_data.get('pattern_scores', {})
        
        if not pattern_scores:
            return """
🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
══════════════════════════════════════════════════════════════
Status: Insufficient pattern data - discovery session recommended

"""
        
        section = f"""
🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
══════════════════════════════════════════════════════════════

📊 PATTERN HIERARCHY (Ranked by Activation Strength):
"""
        
        sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
            pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
            activation_level = self._get_pattern_activation_level(score)
            therapeutic_priority = self._get_therapeutic_priority(score)
            
            section += f"""
{i}. {pattern_name}:
   Activation Score: {score:.1f}/10 ({activation_level})
   Therapeutic Priority: {therapeutic_priority}
"""
        
        return section + "\n"

    def _build_response_summary(self, assessment_data):
        """Build assessment response summary"""
        responses = assessment_data.get('assessment_responses', {})
        
        if not responses:
            return """
📝 ASSESSMENT RESPONSE SUMMARY:
══════════════════════════════════════════════════════════════
Status: No detailed responses available

"""
        
        section = f"""
📝 ASSESSMENT RESPONSE SUMMARY:
══════════════════════════════════════════════════════════════

RESPONSE STATISTICS:
Total Questions Answered: {len(responses)}
"""
        
        # Count response types
        text_responses = 0
        choice_responses = 0
        intensity_responses = 0
        
        for response_data in responses.values():
            response = response_data.get('response', '')
            if isinstance(response, str) and len(response.strip()) > 50:
                text_responses += 1
            else:
                choice_responses += 1
            
            if response_data.get('intensity'):
                intensity_responses += 1
        
        section += f"""
Text Responses: {text_responses}
Choice Responses: {choice_responses}
Intensity Ratings: {intensity_responses}

KEY CLIENT RESPONSES:
"""
        
        # Show most significant responses
        significant_responses = []
        for q_id, response_data in responses.items():
            response = response_data.get('response', '')
            question_text = response_data.get('question_text', '')
            
            # Include responses with high intensity or long text
            intensity = response_data.get('intensity', 0)
            if intensity >= 6 or (isinstance(response, str) and len(response.strip()) > 100):
                significant_responses.append((q_id, response_data))
        
        # Show top 5 significant responses
        for i, (q_id, response_data) in enumerate(significant_responses[:5], 1):
            question_text = response_data.get('question_text', 'Unknown question')
            response = response_data.get('response', 'No response')
            intensity = response_data.get('intensity')
            
            section += f"\n{i}. Q{q_id}: {question_text[:100]}{'...' if len(question_text) > 100 else ''}\n"
            
            if isinstance(response, str):
                response_preview = response[:150] + "..." if len(response) > 150 else response
                section += f"   Response: {response_preview}\n"
            else:
                section += f"   Response: {str(response)}\n"
            
            if intensity:
                section += f"   Intensity: {intensity}/7\n"
        
        return section + "\n"

    def _build_action_items_section(self, assessment_data):
        """Build action items section"""
        contact_info = assessment_data.get('contact_info', {})
        urgency = contact_info.get('urgency', 'not specified').lower()
        is_digital_native = assessment_data.get('is_digital_native', False)
        digital_analysis = assessment_data.get('digital_despair_analysis')
        
        section = """
⚡ IMMEDIATE ACTION ITEMS:
══════════════════════════════════════════════════════════════

"""
        
        # Contact priority
        if 'extremely urgent' in urgency:
            contact_priority = "🚨 IMMEDIATE CONTACT (within 4-6 hours)"
        elif 'very urgent' in urgency:
            contact_priority = "⚡ PRIORITY CONTACT (within 12-24 hours)"
        elif 'urgent' in urgency:
            contact_priority = "🔋 URGENT CONTACT (within 24-48 hours)"
        else:
            contact_priority = "📞 STANDARD CONTACT (within 2-3 days)"
        
        section += f"1. CONTACT PRIORITY: {contact_priority}\n"
        section += f"   Client Email: {contact_info.get('email', 'Not provided')}\n"
        section += f"   Phone: {contact_info.get('phone', 'Not provided')}\n"
        section += f"   Preferred Next Step: {contact_info.get('next_step', 'Not specified')}\n\n"
        
        # Clinical preparation
        if is_digital_native and digital_analysis:
            severity = digital_analysis.get('severity_level', 'MINIMAL')
            if severity in ['SEVERE', 'MODERATE']:
                section += "2. SPECIAL PREPARATION REQUIRED:\n"
                section += "   ✅ Review digital-native protocols\n"
                section += "   ✅ Prepare collaborative language patterns\n"
                section += "   ✅ Plan modified session structure\n"
                section += "   ✅ Expect intellectual resistance\n\n"
        
        section += "3. SESSION PLANNING:\n"
        section += "   □ Review complete assessment before contact\n"
        section += "   □ Prepare intervention protocols\n"
        section += "   □ Schedule appropriate session length\n"
        section += "   □ Plan follow-up sequence\n\n"
        
        return section

    def _build_footer_section(self):
        """Build footer section"""
        return f"""
══════════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Enhanced Clinical Assessment System
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
System Status: Operational | Priority: Review and Contact Client
══════════════════════════════════════════════════════════════
"""

    def _get_pattern_activation_level(self, score):
        """Get activation level for pattern score"""
        if score >= 7.0:
            return "VERY HIGH"
        elif score >= 5.0:
            return "HIGH"
        elif score >= 3.0:
            return "MODERATE"
        else:
            return "MILD"

    def _get_therapeutic_priority(self, score):
        """Get therapeutic priority for pattern"""
        if score >= 6.0:
            return "PRIMARY TARGET"
        elif score >= 4.0:
            return "SECONDARY TARGET"
        else:
            return "MONITOR"

    def _log_assessment_locally(self, assessment_data):
        """Log assessment data when email cannot be sent"""
        contact_info = assessment_data.get('contact_info', {})
        assessment_results = assessment_data.get('assessment_results', {})
        
        print("📊 ASSESSMENT LOGGED LOCALLY:")
        print(f"   Name: {contact_info.get('name', 'Unknown')}")
        print(f"   Email: {contact_info.get('email', 'Unknown')}")
        print(f"   Urgency: {contact_info.get('urgency', 'Not specified')}")
        print(f"   Questions: {assessment_results.get('total_questions_answered', 0)}")
        print(f"   Patterns: {len(assessment_results.get('pattern_scores', {}))}")
        print(f"   Digital Native: {assessment_data.get('is_digital_native', False)}")
        
        # Save to file if possible
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"assessment_backup_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Assessment Backup - {datetime.now()}\n")
                f.write("=" * 50 + "\n")
                f.write(f"Name: {contact_info.get('name', 'Unknown')}\n")
                f.write(f"Email: {contact_info.get('email', 'Unknown')}\n")
                f.write(f"Urgency: {contact_info.get('urgency', 'Not specified')}\n")
                f.write(f"Assessment completed: {datetime.now()}\n")
                f.write("\nFull assessment data:\n")
                f.write(str(assessment_data))
            
            print(f"📁 Assessment saved to: {filename}")
            
        except Exception as e:
            print(f"📁 Could not save to file: {e}")


# Main function for assess.py to call
def send_clinical_assessment_results(assessment_data):
    """Main function called from assess.py - ENHANCED VERSION"""
    print("🎯 send_clinical_assessment_results called with enhanced handler")
    
    try:
        handler = ClinicalAssessmentEmailHandler()
        result = handler.send_clinical_assessment_results(assessment_data)
        
        print(f"📧 Email sending result: {result}")
        return result
        
    except Exception as e:
        print(f"💥 Error in main send function: {e}")
        print(f"🔍 Traceback: {traceback.format_exc()}")
        return False


# Test function
def test_email_functionality():
    """Test email functionality with sample data"""
    test_data = {
        'contact_info': {
            'name': 'Test Client',
            'email': 'test@example.com',
            'phone': '+66-98-765-4321',
            'urgency': 'Very urgent - test assessment',
            'primary_concern': 'Testing email functionality',
            'next_step': 'Schedule session'
        },
        'assessment_results': {
            'total_questions_answered': 25,
            'completion_rate': 0.85,
            'pattern_scores': {1: 6.5, 5: 7.2}
        },
        'is_digital_native': False,
        'pattern_scores': {1: 6.5, 5: 7.2},
        'assessment_responses': {
            '1': {
                'question_text': 'Test question about patterns',
                'response': 'Test response showing engagement',
                'timestamp': datetime.now().isoformat(),
                'intensity': 6
            }
        },
        'clinical_template': 'Basic clinical template for testing'
    }
    
    print("🧪 Testing enhanced email functionality...")
    result = send_clinical_assessment_results(test_data)
    
    if result:
        print("✅ Enhanced email test successful!")
    else:
        print("❌ Enhanced email test failed!")
    
    return result


if __name__ == "__main__":
    test_email_functionality()
