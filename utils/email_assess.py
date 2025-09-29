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
Complete email functionality for assessment results
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class ClinicalAssessmentEmailHandler:
    """Clinical assessment email handler that sends emails"""

    def __init__(self):
        # Get email configuration from secrets or use defaults
        try:
            import streamlit as st
            email_config = st.secrets.get("email", {})
            self.smtp_server = email_config.get("SMTP_SERVER", "smtp.gmail.com")
            self.smtp_port = email_config.get("SMTP_PORT", 587)
            self.sender_email = email_config.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = email_config.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
        except:
            # Fallback to defaults
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
        """Get email password from environment or secrets"""
        try:
            import streamlit as st
            # Try Streamlit secrets with nested structure first
            password = st.secrets.get("email", {}).get("GMAIL_APP_PASSWORD", "")
            if password and password.strip():
                print("✅ Password loaded from Streamlit secrets [email] section")
                return password

            # Try direct access as fallback
            password = st.secrets.get("GMAIL_APP_PASSWORD", "")
            if password and password.strip():
                print("✅ Password loaded from Streamlit secrets (direct)")
                return password
        except Exception as e:
            print(f"[DEBUG] Could not access Streamlit secrets: {e}")

        # Try environment variable
        password = os.getenv("GMAIL_APP_PASSWORD", "")
        if password and password.strip():
            print("✅ Password loaded from environment")
            return password

        print("❌ No password found in secrets or environment")
        return ""

    def send_assessment_results(self, contact_info, responses, profile):
        """Send comprehensive assessment results to therapist"""

        if not self.password:
            print("❌ Cannot send email: No password configured")
            return False

        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = f"New Assessment: {contact_info.get('first_name', '')} {contact_info.get('last_name', '')}"

            # Create email body
            body = self._create_assessment_email_body(contact_info, responses, profile)
            msg.attach(MIMEText(body, 'html'))

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)

            print("✅ Assessment email sent successfully")
            return True

        except Exception as e:
            print(f"❌ Failed to send email: {str(e)}")
            return False

    def _create_assessment_email_body(self, contact_info, responses, profile):
        """Create HTML email body with assessment results"""

        # Get key information
        name = f"{contact_info.get('first_name', '')} {contact_info.get('last_name', '')}"
        email = contact_info.get('email', '')
        phone = contact_info.get('phone', 'Not provided')
        urgency = contact_info.get('urgency', 'Standard')
        additional_info = contact_info.get('additional_info', 'None provided')

        # Get pattern information
        pattern_hierarchy = profile.get('pattern_hierarchy', {})
        dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})

        # Get success prediction
        success_prediction = profile.get('success_prediction', {}).get('probability', 'Not calculated')

        # Count responses
        total_responses = len(responses)

        # Create HTML email
        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .header {{ background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%); color: white; padding: 20px; border-radius: 10px; }}
                .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #4CA1A3; background: #f8f9fa; }}
                .urgent {{ border-left-color: #dc3545; background: #fff5f5; }}
                .high-priority {{ border-left-color: #ffc107; background: #fffbf0; }}
                .contact-info {{ background: #e3f2fd; padding: 15px; border-radius: 8px; }}
                .pattern-info {{ background: #f3e5f5; padding: 15px; border-radius: 8px; }}
                .response-summary {{ background: #e8f5e8; padding: 15px; border-radius: 8px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h2>🎯 New Clinical Assessment Completed</h2>
                <p>Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>

            <div class="contact-info">
                <h3>📋 Client Information</h3>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Urgency Level:</strong> {urgency}</p>
                {f'<p><strong>Additional Information:</strong> {additional_info}</p>' if additional_info != 'None provided' else ''}
            </div>

            <div class="pattern-info">
                <h3>🧠 Assessment Results Summary</h3>
                <p><strong>Total Questions Answered:</strong> {total_responses}</p>
                <p><strong>Dominant Pattern:</strong> {dominant_pattern.get('name', 'Not identified').replace('_', ' ').title()}</p>
                <p><strong>Pattern Score:</strong> {dominant_pattern.get('score', 'N/A')}/5.0</p>
                <p><strong>Success Prediction:</strong> {success_prediction}%</p>
            </div>

            <div class="response-summary">
                <h3>📝 Response Summary</h3>
                <p><strong>Assessment Completion:</strong> {total_responses} questions answered</p>
                <p><strong>Submission Time:</strong> {contact_info.get('submission_time', 'Not recorded')}</p>
            </div>

            <div class="section">
                <h3>🎯 Recommended Next Steps</h3>
                <p>Based on the urgency level (<strong>{urgency}</strong>) and assessment results:</p>
                <ul>
                    <li>Contact client within the specified timeframe</li>
                    <li>Review detailed assessment data in the system</li>
                    <li>Prepare personalized treatment recommendations</li>
                    <li>Schedule initial consultation session</li>
                </ul>
            </div>

            <div class="section">
                <h3>📊 Quick Assessment Overview</h3>
                <p>This client has completed a comprehensive behavioral assessment. The system has identified specific patterns and provided treatment recommendations. Please access the full assessment dashboard for detailed analysis.</p>
            </div>

            <p style="margin-top: 30px; padding: 15px; background: #f0f0f0; border-radius: 8px; font-size: 0.9em; color: #666;">
                <strong>Note:</strong> This email contains summary information only. Full assessment data and detailed recommendations are available in the clinical dashboard.
            </p>
        </body>
        </html>
        """

        return html_body

# Create global instance
email_handler = ClinicalAssessmentEmailHandler()

def send_assessment_email(contact_info, responses, profile):
    """Convenience function to send assessment email"""
    return email_handler.send_assessment_results(contact_info, responses, profile)
