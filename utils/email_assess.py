# """
# Fixed Email Assessment Handler - utils/email_assess.py
# Addresses authentication and sending issues
# """
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime
# import traceback

# class ClinicalAssessmentEmailHandler:
#     """Fixed clinical assessment email handler"""
    
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
        
#         # Get password
#         self.password = self._get_email_password()

#     def _get_email_password(self):
#         """Get email password with multiple fallback methods"""
#         password = ""
        
#         # Method 1: Streamlit secrets
#         try:
#             import streamlit as st
#             password = st.secrets.get("gmail", {}).get("app_password", "")
#             if password:
#                 print("✅ Password loaded from st.secrets.gmail.app_password")
#                 return password
#         except Exception as e:
#             print(f"Streamlit secrets method failed: {e}")
        
#         # Method 2: Direct Streamlit secrets
#         try:
#             import streamlit as st
#             password = st.secrets.get("GMAIL_APP_PASSWORD", "")
#             if password:
#                 print("✅ Password loaded from st.secrets.GMAIL_APP_PASSWORD")
#                 return password
#         except Exception as e:
#             print(f"Direct Streamlit secrets failed: {e}")
        
#         # Method 3: Environment variable
#         try:
#             password = os.environ.get("GMAIL_APP_PASSWORD", "")
#             if password:
#                 print("✅ Password loaded from environment GMAIL_APP_PASSWORD")
#                 return password
#         except Exception as e:
#             print(f"Environment variable method failed: {e}")
        
#         # Method 4: .env file (if available)
#         try:
#             from dotenv import load_dotenv
#             load_dotenv()
#             password = os.environ.get("GMAIL_APP_PASSWORD", "")
#             if password:
#                 print("✅ Password loaded from .env file")
#                 return password
#         except Exception as e:
#             print(f"dotenv method failed: {e}")
        
#         print("⚠️ No email password found in any location")
#         print("Please set GMAIL_APP_PASSWORD in:")
#         print("- Streamlit secrets.toml: [gmail] app_password = 'your_password'")
#         print("- Environment variable: GMAIL_APP_PASSWORD=your_password")
#         return ""

#     def send_clinical_assessment_results(self, assessment_data):
#         """Send comprehensive clinical assessment results - MAIN FUNCTION"""
#         try:
#             print("🚀 Starting enhanced email send process...")
            
#             # Validate assessment_data
#             if not assessment_data:
#                 print("❌ No assessment data provided")
#                 return False
            
#             # Extract key information safely
#             contact_info = assessment_data.get('contact_info', {})
#             if not contact_info:
#                 print("❌ No contact info found")
#                 return False
            
#             assessment_results = assessment_data.get('assessment_results', {})
#             is_digital_native = assessment_data.get('is_digital_native', False)
#             digital_analysis = assessment_data.get('digital_despair_analysis')
            
#             email = contact_info.get('email', 'unknown@email.com')
#             name = contact_info.get('name', 'Assessment Participant')
#             urgency = contact_info.get('urgency', 'Not specified')
            
#             print(f"📧 Preparing email for: {name} ({email})")
#             print(f"🔴 Urgency level: {urgency}")
#             print(f"💻 Digital native: {is_digital_native}")
            
#             # Check password availability
#             if not self.password:
#                 print("⚠️ No email password available")
#                 self._log_assessment_locally(assessment_data)
#                 return True  # Return True for development - change to False for production
            
#             # Create email message
#             msg = MIMEMultipart('mixed')
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
#             success = self._send_email_smtp(msg)
            
#             if success:
#                 print("✅ EMAIL SENT SUCCESSFULLY!")
#                 return True
#             else:
#                 print("❌ EMAIL SEND FAILED!")
#                 self._log_assessment_locally(assessment_data)
#                 return False
                
#         except Exception as e:
#             print(f"💥 ERROR in send_clinical_assessment_results: {str(e)}")
#             print(f"🔍 Full traceback: {traceback.format_exc()}")
#             self._log_assessment_locally(assessment_data)
#             return False

#     def _send_email_smtp(self, msg):
#         """Send email via SMTP with enhanced error handling"""
#         try:
#             print("🔌 Connecting to Gmail SMTP server...")
            
#             # Create SMTP session with timeout
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30)
            
#             print("🔒 Starting TLS encryption...")
#             server.starttls()
            
#             print("🔑 Authenticating with Gmail...")
#             server.login(self.sender_email, self.password)
            
#             print("📤 Sending email...")
#             # Convert message to string
#             text = msg.as_string()
            
#             # Send the email
#             result = server.sendmail(self.sender_email, [self.recipient_email], text)
            
#             print("📚 Closing SMTP connection...")
#             server.quit()
            
#             if result:
#                 print(f"⚠️ Some recipients failed: {result}")
#                 return False
#             else:
#                 print("✅ EMAIL SENT SUCCESSFULLY TO ALL RECIPIENTS!")
#                 return True
            
#         except smtplib.SMTPAuthenticationError as e:
#             print(f"🚫 SMTP Authentication Error: {e}")
#             print("💡 Your Gmail App Password might be incorrect")
#             print("💡 Make sure 2-factor authentication is enabled")
#             print("💡 Generate a new App Password at: https://myaccount.google.com/apppasswords")
#             return False
#         except smtplib.SMTPRecipientsRefused as e:
#             print(f"📧 Recipients Refused: {e}")
#             return False
#         except smtplib.SMTPServerDisconnected as e:
#             print(f"🔌 Server Disconnected: {e}")
#             return False
#         except smtplib.SMTPException as e:
#             print(f"📧 SMTP Error: {e}")
#             return False
#         except Exception as e:
#             print(f"💥 General Email Error: {e}")
#             print(f"🔍 Error type: {type(e).__name__}")
#             return False

#     def _generate_email_subject(self, name, urgency, assessment_results, is_digital_native, digital_analysis):
#         """Generate contextual email subject"""
#         # Priority indicator
#         if 'extremely urgent' in urgency.lower():
#             priority = "🚨 EMERGENCY"
#         elif 'very urgent' in urgency.lower():
#             priority = "⚡ HIGH PRIORITY"
#         elif 'urgent' in urgency.lower():
#             priority = "🔋 URGENT"
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
        
#         # Pattern complexity
#         pattern_count = len(assessment_results.get('pattern_scores', {}))
#         complexity = "COMPLEX" if pattern_count >= 5 else "MULTI" if pattern_count >= 3 else "FOCUSED"
        
#         return f"{priority} ASSESSMENT: {name} - {assessment_type} {complexity} ({pattern_count} patterns)"

#     def _build_complete_email_body(self, assessment_data):
#         """Build comprehensive email body"""
#         body = ""
        
#         try:
#             # Header section
#             body += self._build_header_section(assessment_data)
            
#             # Digital analysis (if applicable)
#             if assessment_data.get('is_digital_native'):
#                 body += self._build_digital_analysis_section(assessment_data)
            
#             # Pattern analysis
#             body += self._build_pattern_analysis_section(assessment_data)
            
#             # Clinical template (if available)
#             clinical_template = assessment_data.get('clinical_template', '')
#             if clinical_template:
#                 body += f"\n{clinical_template}\n"
            
#             # Assessment responses summary
#             body += self._build_response_summary(assessment_data)
            
#             # Action items
#             body += self._build_action_items_section(assessment_data)
            
#             # Footer
#             body += self._build_footer_section()
            
#         except Exception as e:
#             print(f"Error building email body: {e}")
#             body += f"\nError generating full email body: {e}\n"
#             body += f"Assessment data available: {bool(assessment_data)}\n"
        
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
# ══════════════════════════════════════════════════════════════

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
        
#         header += "\n══════════════════════════════════════════════════════════════\n"
        
#         return header

#     def _build_digital_analysis_section(self, assessment_data):
#         """Build digital analysis section"""
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         if not digital_analysis:
#             return f"""
# 💻 DIGITAL NATIVE ASSESSMENT:
# ══════════════════════════════════════════════════════════════
# Status: Digital native identified but syndrome analysis incomplete
# Recommendation: Brief digital assessment completion recommended

# """
        
#         section = f"""
# 💻 DIGITAL DESPAIR SYNDROME ANALYSIS:
# ══════════════════════════════════════════════════════════════

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
#         """Build pattern analysis section"""
#         pattern_scores = assessment_data.get('pattern_scores', {})
        
#         if not pattern_scores:
#             return """
# 🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
# ══════════════════════════════════════════════════════════════
# Status: Insufficient pattern data - discovery session recommended

# """
        
#         section = f"""
# 🎯 TRADITIONAL BEHAVIORAL PATTERN ANALYSIS:
# ══════════════════════════════════════════════════════════════

# 📊 PATTERN HIERARCHY (Ranked by Activation Strength):
# """
        
#         sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
        
#         for i, (pattern_id, score) in enumerate(sorted_patterns, 1):
#             pattern_name = self.pattern_names.get(pattern_id, f"Pattern {pattern_id}")
#             activation_level = self._get_pattern_activation_level(score)
#             therapeutic_priority = self._get_therapeutic_priority(score)
            
#             section += f"""
# {i}. {pattern_name}:
#    Activation Score: {score:.1f}/10 ({activation_level})
#    Therapeutic Priority: {therapeutic_priority}
# """
        
#         return section + "\n"

#     def _build_response_summary(self, assessment_data):
#         """Build assessment response summary"""
#         responses = assessment_data.get('assessment_responses', {})
        
#         if not responses:
#             return """
# 📝 ASSESSMENT RESPONSE SUMMARY:
# ══════════════════════════════════════════════════════════════
# Status: No detailed responses available

# """
        
#         section = f"""
# 📝 ASSESSMENT RESPONSE SUMMARY:
# ══════════════════════════════════════════════════════════════

# RESPONSE STATISTICS:
# Total Questions Answered: {len(responses)}
# """
        
#         # Count response types
#         text_responses = 0
#         choice_responses = 0
#         intensity_responses = 0
        
#         for response_data in responses.values():
#             response = response_data.get('response', '')
#             if isinstance(response, str) and len(response.strip()) > 50:
#                 text_responses += 1
#             else:
#                 choice_responses += 1
            
#             if response_data.get('intensity'):
#                 intensity_responses += 1
        
#         section += f"""
# Text Responses: {text_responses}
# Choice Responses: {choice_responses}
# Intensity Ratings: {intensity_responses}

# KEY CLIENT RESPONSES:
# """
        
#         # Show most significant responses
#         significant_responses = []
#         for q_id, response_data in responses.items():
#             response = response_data.get('response', '')
#             question_text = response_data.get('question_text', '')
            
#             # Include responses with high intensity or long text
#             intensity = response_data.get('intensity', 0)
#             if intensity >= 6 or (isinstance(response, str) and len(response.strip()) > 100):
#                 significant_responses.append((q_id, response_data))
        
#         # Show top 5 significant responses
#         for i, (q_id, response_data) in enumerate(significant_responses[:5], 1):
#             question_text = response_data.get('question_text', 'Unknown question')
#             response = response_data.get('response', 'No response')
#             intensity = response_data.get('intensity')
            
#             section += f"\n{i}. Q{q_id}: {question_text[:100]}{'...' if len(question_text) > 100 else ''}\n"
            
#             if isinstance(response, str):
#                 response_preview = response[:150] + "..." if len(response) > 150 else response
#                 section += f"   Response: {response_preview}\n"
#             else:
#                 section += f"   Response: {str(response)}\n"
            
#             if intensity:
#                 section += f"   Intensity: {intensity}/7\n"
        
#         return section + "\n"

#     def _build_action_items_section(self, assessment_data):
#         """Build action items section"""
#         contact_info = assessment_data.get('contact_info', {})
#         urgency = contact_info.get('urgency', 'not specified').lower()
#         is_digital_native = assessment_data.get('is_digital_native', False)
#         digital_analysis = assessment_data.get('digital_despair_analysis')
        
#         section = """
# ⚡ IMMEDIATE ACTION ITEMS:
# ══════════════════════════════════════════════════════════════

# """
        
#         # Contact priority
#         if 'extremely urgent' in urgency:
#             contact_priority = "🚨 IMMEDIATE CONTACT (within 4-6 hours)"
#         elif 'very urgent' in urgency:
#             contact_priority = "⚡ PRIORITY CONTACT (within 12-24 hours)"
#         elif 'urgent' in urgency:
#             contact_priority = "🔋 URGENT CONTACT (within 24-48 hours)"
#         else:
#             contact_priority = "📞 STANDARD CONTACT (within 2-3 days)"
        
#         section += f"1. CONTACT PRIORITY: {contact_priority}\n"
#         section += f"   Client Email: {contact_info.get('email', 'Not provided')}\n"
#         section += f"   Phone: {contact_info.get('phone', 'Not provided')}\n"
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
# ══════════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Enhanced Clinical Assessment System
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# System Status: Operational | Priority: Review and Contact Client
# ══════════════════════════════════════════════════════════════
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

#     def _log_assessment_locally(self, assessment_data):
#         """Log assessment data when email cannot be sent"""
#         contact_info = assessment_data.get('contact_info', {})
#         assessment_results = assessment_data.get('assessment_results', {})
        
#         print("📊 ASSESSMENT LOGGED LOCALLY:")
#         print(f"   Name: {contact_info.get('name', 'Unknown')}")
#         print(f"   Email: {contact_info.get('email', 'Unknown')}")
#         print(f"   Urgency: {contact_info.get('urgency', 'Not specified')}")
#         print(f"   Questions: {assessment_results.get('total_questions_answered', 0)}")
#         print(f"   Patterns: {len(assessment_results.get('pattern_scores', {}))}")
#         print(f"   Digital Native: {assessment_data.get('is_digital_native', False)}")
        
#         # Save to file if possible
#         try:
#             timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#             filename = f"assessment_backup_{timestamp}.txt"
            
#             with open(filename, 'w', encoding='utf-8') as f:
#                 f.write(f"Assessment Backup - {datetime.now()}\n")
#                 f.write("=" * 50 + "\n")
#                 f.write(f"Name: {contact_info.get('name', 'Unknown')}\n")
#                 f.write(f"Email: {contact_info.get('email', 'Unknown')}\n")
#                 f.write(f"Urgency: {contact_info.get('urgency', 'Not specified')}\n")
#                 f.write(f"Assessment completed: {datetime.now()}\n")
#                 f.write("\nFull assessment data:\n")
#                 f.write(str(assessment_data))
            
#             print(f"📁 Assessment saved to: {filename}")
            
#         except Exception as e:
#             print(f"📁 Could not save to file: {e}")


# # Main function for assess.py to call
# def send_clinical_assessment_results(assessment_data):
#     """Main function called from assess.py - ENHANCED VERSION"""
#     print("🎯 send_clinical_assessment_results called with enhanced handler")
    
#     try:
#         handler = ClinicalAssessmentEmailHandler()
#         result = handler.send_clinical_assessment_results(assessment_data)
        
#         print(f"📧 Email sending result: {result}")
#         return result
        
#     except Exception as e:
#         print(f"💥 Error in main send function: {e}")
#         print(f"🔍 Traceback: {traceback.format_exc()}")
#         return False


# # Test function
# def test_email_functionality():
#     """Test email functionality with sample data"""
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
#         'assessment_responses': {
#             '1': {
#                 'question_text': 'Test question about patterns',
#                 'response': 'Test response showing engagement',
#                 'timestamp': datetime.now().isoformat(),
#                 'intensity': 6
#             }
#         },
#         'clinical_template': 'Basic clinical template for testing'
#     }
    
#     print("🧪 Testing enhanced email functionality...")
#     result = send_clinical_assessment_results(test_data)
    
#     if result:
#         print("✅ Enhanced email test successful!")
#     else:
#         print("❌ Enhanced email test failed!")
    
#     return result


# if __name__ == "__main__":
#     test_email_functionality()





"""
Enhanced Clinical Assessment Email Handler
Sends comprehensive assessment with rapid clinical summary template
Includes all trigger chain data and intervention protocols
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Dict, Any

try:
    from utils.config_assess import PatternDefinitions
    PATTERNS = PatternDefinitions.PATTERNS
    PATTERN_DESCRIPTIONS = PatternDefinitions.PATTERN_DESCRIPTIONS
except ImportError:
    PATTERNS = {i: f"Pattern {i}" for i in range(1, 10)}
    PATTERN_DESCRIPTIONS = {}


class ClinicalAssessmentEmailHandler:
    """Enhanced email handler with rapid clinical summary"""
    
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = self._get_config("SENDER_EMAIL", "laetitiasheppard@gmail.com")
        self.recipient_email = self._get_config("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
        self.password = self._get_email_password()
    
    def _get_config(self, key: str, default: str) -> str:
        try:
            import streamlit as st
            return st.secrets.get("email", {}).get(key, default)
        except:
            return os.getenv(key, default)
    
    def _get_email_password(self) -> str:
        try:
            import streamlit as st
            password = st.secrets.get("email", {}).get("GMAIL_APP_PASSWORD", "")
            if password and password.strip():
                return password
        except Exception as e:
            print(f"Could not access Streamlit secrets: {e}")
        
        password = os.getenv("GMAIL_APP_PASSWORD", "")
        if password and password.strip():
            return password
        
        print("ERROR: No email password configured")
        return ""
    
    def send_assessment_email(self, email_data: Dict[str, Any]) -> bool:
        """Send comprehensive assessment email with rapid clinical summary"""
        if not self.password:
            print("ERROR: Cannot send email - no password configured")
            return False
        
        try:
            contact = email_data.get('contact', {})
            analysis = email_data.get('analysis', {})
            responses = email_data.get('responses', {})
            
            msg = MIMEMultipart('alternative')
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = f"🎯 New Clinical Assessment: {contact.get('full_name', 'Unknown Client')}"
            
            html_body = self._create_comprehensive_email_body(contact, analysis, responses)
            msg.attach(MIMEText(html_body, 'html'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)
            
            print("✅ SUCCESS: Assessment email sent")
            return True
            
        except Exception as e:
            print(f"❌ ERROR: Failed to send email: {str(e)}")
            return False
    
    def _create_comprehensive_email_body(
        self,
        contact: Dict,
        analysis: Dict,
        responses: Dict
    ) -> str:
        """Create comprehensive HTML email with rapid clinical summary"""
        
        # Extract all analysis components
        pattern_hierarchy = analysis.get('pattern_hierarchy', {})
        clinical_summary = analysis.get('clinical_summary', {})
        trigger_chain_analysis = analysis.get('trigger_chain_analysis', {})
        success_prediction = analysis.get('success_prediction', {})
        digital_analysis = analysis.get('digital_analysis', {})
        
        # Extract key data
        dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})
        primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        pattern_count = pattern_hierarchy.get('pattern_count', 0)
        no_patterns = pattern_count == 0 or not dominant_pattern
        
        client_name = contact.get('full_name', 'Unknown Client')
        client_email = contact.get('email', '')
        urgency = contact.get('urgency', 'Not specified')
        
        # Build HTML email
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #273548;
            background: #f8fafc;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 0;
        }}
        .header {{
            background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2rem;
            font-weight: 700;
        }}
        .header p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.95;
        }}
        
        /* RAPID CLINICAL SUMMARY - TOP PRIORITY */
        .clinical-summary {{
            background: #fff3cd;
            border: 3px solid #eab308;
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem;
        }}
        .clinical-summary h2 {{
            color: #b45309;
            margin: 0 0 1.5rem 0;
            font-size: 1.5rem;
            border-bottom: 2px solid #eab308;
            padding-bottom: 0.5rem;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }}
        .summary-item {{
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4CA1A3;
        }}
        .summary-item strong {{
            display: block;
            color: #4CA1A3;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .summary-item span {{
            color: #273548;
            font-size: 1rem;
        }}
        .summary-full {{
            grid-column: 1 / -1;
        }}
        .resistance-list {{
            background: white;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }}
        .resistance-list ol {{
            margin: 0.5rem 0;
            padding-left: 1.5rem;
        }}
        .resistance-list li {{
            margin: 0.5rem 0;
            color: #273548;
        }}
        
        .section {{
            padding: 2rem;
            border-bottom: 1px solid #e2e8f0;
        }}
        .section h2 {{
            color: #273548;
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
        }}
        .section h3 {{
            color: #4CA1A3;
            margin: 1.5rem 0 0.75rem 0;
            font-size: 1.2rem;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin: 1rem 0;
        }}
        .info-item {{
            background: #f8fafc;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #cbd5e1;
        }}
        .info-item strong {{
            display: block;
            color: #556D7A;
            margin-bottom: 0.25rem;
            font-size: 0.85rem;
        }}
        .pattern-box {{
            background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .pattern-box h3 {{
            margin: 0;
            color: white;
            font-size: 1.3rem;
        }}
        .pattern-box p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.95;
        }}
        .trigger-chain {{
            background: #e1f0f0;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .trigger-step {{
            background: white;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 4px solid #4CA1A3;
            border-radius: 6px;
        }}
        .trigger-step strong {{
            color: #4CA1A3;
            display: block;
            margin-bottom: 0.25rem;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        th {{
            background: #f8fafc;
            font-weight: 600;
            color: #273548;
        }}
        .urgency-alert {{
            background: #fef2f2;
            border: 2px solid #ef4444;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .urgency-alert h3 {{
            color: #b91c1c;
            margin: 0 0 0.5rem 0;
        }}
        .healthy-baseline {{
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            margin: 1rem 0;
        }}
        .healthy-baseline h3 {{
            margin: 0;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <h1>Clinical behavioral pattern assessment</h1>
            <p>Comprehensive 71-question analysis with rapid clinical summary</p>
            <p>{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        {self._generate_rapid_clinical_summary(
            client_name, dominant_pattern, primary_patterns, 
            clinical_summary, no_patterns
        )}
        
        {self._generate_urgency_alert(urgency)}
        
        {self._generate_client_information(contact)}
        
        {self._generate_pattern_analysis(
            dominant_pattern, pattern_hierarchy, no_patterns
        )}
        
        {self._generate_trigger_chain_section(trigger_chain_analysis)}
        
        {self._generate_clinical_insights(clinical_summary, dominant_pattern)}
        
        {self._generate_success_prediction(success_prediction)}
        
        {self._generate_digital_analysis(digital_analysis)}
        
        {self._generate_response_transcript(responses)}
    </div>
</body>
</html>
        """
        
        return html
    
    def _generate_rapid_clinical_summary(
        self,
        client_name: str,
        dominant_pattern: Dict,
        primary_patterns: Dict,
        clinical_summary: Dict,
        no_patterns: bool
    ) -> str:
        """Generate rapid clinical summary template section"""
        
        if no_patterns:
            return """
                <div class="healthy-baseline" style="margin: 2rem;">
                    <h3>✓ Healthy baseline - no clinical intervention needed</h3>
                    <p style="margin: 0.5rem 0; opacity: 0.95;">
                        No significant behavioral patterns detected. Consider performance optimization services.
                    </p>
                </div>
            """
        
        # Extract data
        dominant_name = dominant_pattern.get('name', 'Unknown').title()
        dominant_score = dominant_pattern.get('score', 0)
        
        primary_1_name = "None"
        primary_1_score = 0
        primary_2_name = "None"
        primary_2_score = 0
        
        if len(primary_patterns) > 0:
            primary_1_name = primary_patterns[0].get('name', 'Unknown').title()
            primary_1_score = primary_patterns[0].get('score', 0)
        
        if len(primary_patterns) > 1:
            primary_2_name = primary_patterns[1].get('name', 'Unknown').title()
            primary_2_score = primary_patterns[1].get('score', 0)
        
        # Clinical summary data
        core_belief = clinical_summary.get('core_limiting_belief', 'Not identified')
        hidden_benefits = clinical_summary.get('hidden_benefits', 'Not identified')
        systemic_resistance = clinical_summary.get('systemic_resistance', 'Not identified')
        identity_threat = clinical_summary.get('identity_threat', 'Not identified')
        session_1_focus = clinical_summary.get('session_1_focus', 'Pattern exploration')
        session_2_target = clinical_summary.get('session_2_target', 'Core transformation')
        session_3_need = clinical_summary.get('potential_session_3_need', 'Unknown')
        readiness = clinical_summary.get('change_readiness_score', '0/10')
        intervention_keywords = clinical_summary.get('intervention_keywords', 'Not specified')
        avoid_language = clinical_summary.get('avoid_language', 'Not specified')
        
        resistance_points = clinical_summary.get('predicted_resistance_points', [])
        resistance_html = "".join([f"<li>{point}</li>" for point in resistance_points])
        
        return f"""
            <div class="clinical-summary">
                <h2>⚡ RAPID CLINICAL SUMMARY TEMPLATE</h2>
                
                <div class="summary-grid">
                    <div class="summary-item">
                        <strong>Client</strong>
                        <span>{client_name}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Date</strong>
                        <span>{datetime.now().strftime('%Y-%m-%d')}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Dominant Pattern</strong>
                        <span>{dominant_name} (Score: {dominant_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Primary Pattern</strong>
                        <span>{primary_1_name} (Score: {primary_1_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Secondary Pattern</strong>
                        <span>{primary_2_name} (Score: {primary_2_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Change Readiness</strong>
                        <span>{readiness}</span>
                    </div>
                    
                    <div class="summary-item summary-full">
                        <strong>Core Limiting Belief</strong>
                        <span>{core_belief}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Hidden Benefits</strong>
                        <span>{hidden_benefits}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Identity Threat</strong>
                        <span>{identity_threat}</span>
                    </div>
                    
                    <div class="summary-item summary-full">
                        <strong>Systemic Resistance</strong>
                        <span>{systemic_resistance}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Session 1 Focus</strong>
                        <span>{session_1_focus}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Session 2 Target</strong>
                        <span>{session_2_target}</span>
                    </div>
                    
                    <div class="summary-item summary-full">
                        <strong>Potential Session 3 Need</strong>
                        <span>{session_3_need}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Intervention Keywords</strong>
                        <span>{intervention_keywords}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Avoid Language</strong>
                        <span>{avoid_language}</span>
                    </div>
                </div>
                
                <div class="resistance-list">
                    <strong style="color: #b45309; display: block; margin-bottom: 0.5rem;">
                        Predicted Resistance Points:
                    </strong>
                    <ol>{resistance_html if resistance_html else '<li>Standard resistance patterns</li>'}</ol>
                </div>
            </div>
        """
    
    def _generate_urgency_alert(self, urgency: str) -> str:
        """Generate urgency alert if needed"""
        urgency_lower = urgency.lower()
        
        if 'extremely urgent' in urgency_lower or 'same day' in urgency_lower:
            return """
                <div class="urgency-alert" style="margin: 2rem;">
                    <h3>🚨 PRIORITY: EXTREMELY URGENT</h3>
                    <p><strong>Action Required:</strong> Contact client within 24 hours</p>
                    <p>Client has indicated extreme urgency - prioritize scheduling immediately</p>
                </div>
            """
        elif 'very urgent' in urgency_lower or '24 hours' in urgency_lower:
            return """
                <div class="urgency-alert" style="margin: 2rem; border-color: #eab308; background: #fef3c7;">
                    <h3 style="color: #b45309;">⚠️ HIGH PRIORITY: VERY URGENT</h3>
                    <p><strong>Action Required:</strong> Contact client within 24-48 hours</p>
                </div>
            """
        
        return ""
    
    def _generate_client_information(self, contact: Dict) -> str:
        """Generate client information section"""
        return f"""
            <div class="section">
                <h2>Client information</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Name:</strong>
                        <span>{contact.get('full_name', 'Unknown')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Email:</strong>
                        <span>{contact.get('email', '')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Phone:</strong>
                        <span>{contact.get('phone', 'Not provided')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Urgency:</strong>
                        <span>{contact.get('urgency', 'Not specified')}</span>
                    </div>
                </div>
                <div class="info-item" style="margin-top: 1rem; grid-column: 1 / -1;">
                    <strong>Primary Concern:</strong>
                    <span>{contact.get('primary_concern', 'Not provided')}</span>
                </div>
                {self._format_additional_info(contact.get('additional_info', ''))}
            </div>
        """
    
    def _format_additional_info(self, additional_info: str) -> str:
        """Format additional info if provided"""
        if additional_info and additional_info != "None provided":
            return f"""
                <div class="info-item" style="margin-top: 1rem;">
                    <strong>Additional Information:</strong>
                    <span>{additional_info}</span>
                </div>
            """
        return ""
    
    def _generate_pattern_analysis(
        self,
        dominant_pattern: Dict,
        pattern_hierarchy: Dict,
        no_patterns: bool
    ) -> str:
        """Generate pattern analysis section"""
        
        if no_patterns:
            return ""
        
        pattern_name = dominant_pattern.get('name', 'Unknown').title()
        pattern_score = dominant_pattern.get('score', 0)
        pattern_severity = dominant_pattern.get('severity', 'Unknown')
        pattern_desc = dominant_pattern.get('description', {})
        
        root_structure = pattern_desc.get('root_structure', 'Not available')
        systemic_factors = pattern_desc.get('systemic_factors', [])
        identity_conflict = pattern_desc.get('identity_conflict', 'Not available')
        hidden_loyalties = pattern_desc.get('hidden_loyalties', [])
        
        systemic_html = "".join([f"<li>{factor}</li>" for factor in systemic_factors])
        loyalties_html = "".join([f"<li>{loyalty}</li>" for loyalty in hidden_loyalties])
        
        all_scores = pattern_hierarchy.get('all_scores', {})
        pattern_table = self._generate_pattern_table(all_scores)
        
        return f"""
            <div class="section">
                <h2>Behavioral pattern analysis</h2>
                
                <div class="pattern-box">
                    <h3>Dominant pattern: {pattern_name}</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0;">
                        {pattern_score:.1f}/10 ({pattern_severity})
                    </p>
                </div>
                
                <h3>Root pattern structure</h3>
                <div class="info-item">
                    <strong>Core structural belief:</strong>
                    <span>{root_structure}</span>
                </div>
                
                <h3>Systemic factors maintaining pattern</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {systemic_html}
                </ul>
                
                <h3>Identity conflict</h3>
                <div class="info-item">
                    <span>{identity_conflict}</span>
                </div>
                
                <h3>Hidden loyalties creating resistance</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {loyalties_html}
                </ul>
                
                <h3>Pattern constellation (all scores)</h3>
                {pattern_table}
            </div>
        """
    
    def _generate_pattern_table(self, all_scores: Dict[int, float]) -> str:
        """Generate pattern scores table"""
        significant = {pid: score for pid, score in all_scores.items() if score >= 4.0}
        
        if not significant:
            return '<p style="color: #22c55e; font-weight: 600;">No clinically significant patterns detected</p>'
        
        rows = []
        for pid, score in sorted(significant.items(), key=lambda x: x[1], reverse=True):
            pattern_name = PATTERNS.get(pid, f"Pattern {pid}").title()
            severity = self._get_severity(score)
            rows.append(f"""
                <tr>
                    <td>{pattern_name}</td>
                    <td><strong>{score:.1f}/10</strong></td>
                    <td>{severity}</td>
                </tr>
            """)
        
        return f"""
            <table>
                <tr>
                    <th>Pattern</th>
                    <th>Score</th>
                    <th>Severity</th>
                </tr>
                {"".join(rows)}
            </table>
        """
    
    def _get_severity(self, score: float) -> str:
        if score >= 8.0: return "Severe"
        elif score >= 6.0: return "Moderate-High"
        elif score >= 4.0: return "Moderate"
        else: return "Mild"
    
    def _generate_trigger_chain_section(self, trigger_chain_analysis: Dict) -> str:
        """Generate trigger chain sequence section"""
        chain = trigger_chain_analysis.get('trigger_chain', {})
        intervention_windows = trigger_chain_analysis.get('intervention_windows', [])
        completeness = trigger_chain_analysis.get('sequence_completeness', 0)
        
        intervention_html = "".join([f"<li>{window}</li>" for window in intervention_windows])
        
        return f"""
            <div class="section">
                <h2>Complete trigger sequence mapping</h2>
                <p><strong>Sequence completeness:</strong> {completeness:.0f}%</p>
                
                <div class="trigger-chain">
                    <div class="trigger-step">
                        <strong>1. Environmental trigger:</strong>
                        <span>{chain.get('environmental_trigger', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>2. First awareness point:</strong>
                        <span>{chain.get('awareness_point', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>3. Physical response:</strong>
                        <span>{chain.get('physical_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>4. Automatic thought:</strong>
                        <span>{chain.get('automatic_thought', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>5. Emotional response:</strong>
                        <span>{chain.get('emotional_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>6. Behavioral response:</strong>
                        <span>{chain.get('behavioral_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>7. Immediate consequence:</strong>
                        <span>{chain.get('immediate_consequence', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>8. Longer-term impact:</strong>
                        <span>{chain.get('longer_term_impact', 'Not captured')}</span>
                    </div>
                </div>
                
                <h3>Intervention windows identified</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {intervention_html if intervention_html else '<li>Complete sequence in session 1</li>'}
                </ul>
            </div>
        """
    
    def _generate_clinical_insights(self, clinical_summary: Dict, dominant_pattern: Dict) -> str:
        """Generate clinical insights section"""
        pattern_desc = dominant_pattern.get('description', {})
        
        return f"""
            <div class="section">
                <h2>Clinical intervention protocols</h2>
                
                <h3>Protective function</h3>
                <div class="info-item">
                    <span>{pattern_desc.get('protective_function', 'Not identified')}</span>
                </div>
                
                <h3>Intervention focus</h3>
                <div class="info-item">
                    <span>{pattern_desc.get('intervention_focus', 'Not identified')}</span>
                </div>
                
                <h3>Language protocols</h3>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Intervention Keywords:</strong>
                        <span>{clinical_summary.get('intervention_keywords', 'Not specified')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Avoid Language:</strong>
                        <span>{clinical_summary.get('avoid_language', 'Not specified')}</span>
                    </div>
                </div>
            </div>
        """
    
    def _generate_success_prediction(self, success_prediction: Dict) -> str:
        """Generate success prediction section"""
        success_rate = success_prediction.get('overall_success_rate', 85)
        recommended_sessions = success_prediction.get('recommended_sessions', 2)
        timeline = success_prediction.get('timeline_estimate', '2 weeks')
        
        return f"""
            <div class="section">
                <h2>Success prediction</h2>
                
                <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%); 
                            color: white; border-radius: 12px; margin: 1rem 0;">
                    <div style="font-size: 3rem; font-weight: bold;">{success_rate}%</div>
                    <p style="margin: 0.5rem 0; opacity: 0.95;">Predicted success rate</p>
                </div>
                
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Recommended Sessions:</strong>
                        <span>{recommended_sessions} sessions</span>
                    </div>
                    <div class="info-item">
                        <strong>Timeline Estimate:</strong>
                        <span>{timeline}</span>
                    </div>
                </div>
            </div>
        """
    
    def _generate_digital_analysis(self, digital_analysis: Dict) -> str:
        """Generate digital analysis section if applicable"""
        if not digital_analysis or not digital_analysis.get('is_digital_native'):
            return ""
        
        severity = digital_analysis.get('severity_level', 'MINIMAL')
        score = digital_analysis.get('digital_despair_score', 0)
        interventions = digital_analysis.get('recommended_interventions', [])
        
        if severity in ['MINIMAL', 'MILD']:
            return ""
        
        interventions_html = "".join([f"<li>{intervention}</li>" for intervention in interventions])
        
        return f"""
            <div class="section">
                <h2>Digital conditioning analysis</h2>
                
                <div class="info-item" style="background: #fef3c7; border-left-color: #eab308;">
                    <strong>Digital Despair Score:</strong>
                    <span>{score:.1f}% ({severity})</span>
                </div>
                
                <h3>Specialized adaptations required</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {interventions_html}
                </ul>
            </div>
        """
    
    def _generate_response_transcript(self, responses: Dict[int, Any]) -> str:
        """Generate complete response transcript"""
        from utils.config_assess import COMPREHENSIVE_QUESTIONS
        
        items = []
        for q_id in sorted(responses.keys()):
            q_text = "Question not found"
            for q in COMPREHENSIVE_QUESTIONS:
                if q['id'] == q_id:
                    q_text = q['text']
                    break
            
            response = responses[q_id]
            if isinstance(response, (list, tuple)):
                response_text = ", ".join(str(r) for r in response)
            else:
                response_text = str(response)
            
            items.append(f"""
                <div style="background: #f8fafc; padding: 1rem; margin: 0.5rem 0; border-left: 4px solid #cbd5e1; border-radius: 6px;">
                    <strong style="color: #4CA1A3;">Q{q_id}:</strong> {q_text}<br>
                    <strong>Response:</strong> {response_text}
                </div>
            """)
        
        return f"""
            <div class="section">
                <h2>Complete response transcript</h2>
                <p><strong>Total questions answered:</strong> {len(responses)}</p>
                {"".join(items)}
            </div>
        """


# Global instance
_email_handler = ClinicalAssessmentEmailHandler()

def send_assessment_email(email_data: Dict[str, Any]) -> bool:
    """Send assessment email"""
    return _email_handler.send_assessment_email(email_data)
