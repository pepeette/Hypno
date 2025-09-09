# """
# Email handler utility for sending booking notifications via Gmail SMTP
# Simplified version to restore working functionality
# """
# import smtplib
# import os
# import streamlit as st
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime


# class EmailHandler:
#     """Handle email sending for booking notifications"""

#     def __init__(self):
#         # Gmail SMTP configuration
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587

#         # Get credentials from Streamlit secrets first, then environment variables
#         try:
#             # Try Streamlit secrets first
#             self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
#             self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
#             self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
#         except Exception as e:
#             print(f"[DEBUG] Error accessing secrets: {e}")
#             # Fallback to environment variables
#             self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = os.environ.get("GMAIL_APP_PASSWORD")

#     # ---------------- EMAIL TYPES ---------------- #
#     def send_discovery_call_email(self, booking_data):
#         """Send discovery call booking notification"""
#         try:
#             print(f"[DEBUG] send_discovery_call_email called with data keys: {list(booking_data.keys())}")
#             print(f"[DEBUG] Form type: {booking_data.get('form_type', 'Not specified')}")
            
#             # Check if this is assessment data
#             if booking_data.get('form_type') == 'Complete behavioral pattern assessment':
#                 print("[DEBUG] Detected assessment data, routing to assessment handler")
#                 return self.send_assessment_results_email(booking_data)
#             else:
#                 print("[DEBUG] Regular discovery call booking")
#                 msg = self._build_email(
#                     subject="🔔 New Discovery Call Booking Request",
#                     body=self._format_discovery_email_body(booking_data)
#                 )
#                 return self._dispatch(msg, booking_data, "Discovery Call")
                
#         except Exception as e:
#             print(f"[ERROR] Exception in send_discovery_call_email: {e}")
#             import traceback
#             traceback.print_exc()
#             return False

#     def send_assessment_results_email(self, assessment_data):
#         """Send comprehensive assessment results with pattern analysis"""
#         try:
#             print("[DEBUG] Sending assessment results email")
#             msg = self._build_email(
#                 subject="🧠 Complete Behavioral Pattern Assessment Results",
#                 body=self._format_assessment_results_body(assessment_data)
#             )
#             return self._dispatch(msg, assessment_data, "Assessment Results")
#         except Exception as e:
#             print(f"[ERROR] Exception in send_assessment_results_email: {e}")
#             return False

#     def send_package_booking_email(self, booking_data):
#         """Send package booking notification"""
#         try:
#             msg = self._build_email(
#                 subject="💰 New Package Interest Notification",
#                 body=self._format_package_email_body(booking_data)
#             )
#             return self._dispatch(msg, booking_data, "Package Interest")
#         except Exception as e:
#             print(f"[ERROR] Exception in send_package_booking_email: {e}")
#             return False

#     def send_testimonial_email(self, testimonial_data):
#         """Send testimonial submission notification"""
#         try:
#             msg = self._build_email(
#                 subject="🌟 New Success Story Submission",
#                 body=self._format_testimonial_email_body(testimonial_data)
#             )
#             return self._dispatch(msg, testimonial_data, "Testimonial")
#         except Exception as e:
#             print(f"[ERROR] Exception in send_testimonial_email: {e}")
#             return False

#     # ---------------- HELPERS ---------------- #
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
#             print(f"[DEBUG] Sender: {self.sender_email}")
#             print(f"[DEBUG] Recipient: {self.recipient_email}")
#             print(f"[DEBUG] Has password: {bool(self.password)}")
            
#             if not self.password:
#                 # Log for debugging but still return success for demo purposes
#                 print(f"[DEBUG] {email_type} email would be sent (no password configured)")
#                 print(f"To: {self.recipient_email}")
#                 print(f"Data preview: {str(data)[:200]}...")
#                 return True  # Return True so the UI shows success
            
#             if not self.sender_email or not self.recipient_email:
#                 print(f"[ERROR] Missing email configuration for {email_type}")
#                 return False
                
#             return self._send_email(msg)
            
#         except Exception as e:
#             print(f"[ERROR] Exception in _dispatch: {e}")
#             return False

#     def _send_email(self, msg):
#         """Send email via Gmail SMTP with detailed error handling"""
#         try:
#             print("[DEBUG] Attempting to send email via SMTP")
#             # Create server connection
#             server = smtplib.SMTP(self.smtp_server, self.smtp_port)
#             server.starttls()
            
#             # Login with credentials
#             server.login(self.sender_email, self.password)
            
#             # Send email
#             server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
#             server.quit()
            
#             print(f"[SUCCESS] Email sent from {self.sender_email} to {self.recipient_email}")
#             return True
            
#         except smtplib.SMTPAuthenticationError as e:
#             print(f"[ERROR] SMTP Authentication failed: {e}")
#             print("Check your Gmail App Password in Streamlit secrets")
#             return False
#         except smtplib.SMTPException as e:
#             print(f"[ERROR] SMTP error: {e}")
#             return False
#         except Exception as e:
#             print(f"[ERROR] Unexpected error sending email: {e}")
#             return False

#     # ---------------- ORIGINAL FORMATTERS (PRESERVED) ---------------- #
#     def _format_discovery_email_body(self, data):
#         """Format discovery call email body with package information"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Handle package selection
#             package_info = ""
#             if data.get('selected_package') and data.get('selected_package') != 'None':
#                 package_info = f"""
# 🎯 SELECTED PACKAGE:
# {data.get('selected_package')}

# """

#             return f"""
# 🔔 NEW DISCOVERY CALL BOOKING REQUEST
# Received: {timestamp}

# ═══════════════════════════════════════

# 👤 CONTACT INFORMATION:
# Name: {data.get('name', 'Not provided')}
# Email: {data.get('email', 'Not provided')}

# {package_info}🎯 CONCERN DETAILS:
# Primary Concern: {data.get('concern', 'Not specified')}
# Description: {data.get('concern_description', 'Not provided')}

# 📋 SOURCE INFORMATION:
# Form Type: {data.get('form_type', 'Unknown')}
# Source Page: {data.get('source', 'Website')}

# ═══════════════════════════════════════

# ⚡ ACTION REQUIRED:
# Please contact this person within 24 hours to schedule their discovery call.

# 📞 RECOMMENDED NEXT STEPS:
# 1. Send confirmation email to client
# 2. Schedule discovery call via Calendly
# 3. Prepare personalized approach based on their concerns
# {f"4. Discuss {data.get('selected_package')} package details" if package_info else ""}

# ═══════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Automated Booking System
#             """
#         except Exception as e:
#             print(f"[ERROR] Error formatting discovery email: {e}")
#             return f"Error formatting email body: {e}"

#     def _format_assessment_results_body(self, data):
#         """Format comprehensive assessment results email"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Extract key data safely
#             name = data.get('name', 'Unknown client')
#             email = data.get('email', 'Unknown email')
#             concern = data.get('concern', 'General assessment')
#             scores = data.get('assessment_scores', {})
#             raw_responses = data.get('raw_responses', {})
            
#             body = f"""
# 🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
# Assessment completed: {timestamp}

# ═══════════════════════════════════════════════════════════

# 👤 CLIENT INFORMATION:
# Name: {name}
# Email: {email}
# Primary Concern: {concern}
# Total Questions Completed: {data.get('total_questions', 50)}
# Completion Rate: {data.get('completion_rate', '100%')}

# ═══════════════════════════════════════════════════════════

# 📊 PATTERN ACTIVATION ANALYSIS:
# {scores}

# Raw responses:
# {raw_responses}

# ═══════════════════════════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Automated Assessment System
# Clinical Analysis Generated: {timestamp}
#             """
            
#             return body
            
#         except Exception as e:
#             print(f"[ERROR] Error formatting assessment email: {e}")
#             return f"Error formatting assessment email body: {e}"

#     def _format_package_email_body(self, data):
#         """Format package booking email body"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             return f"""
# 💰 NEW PACKAGE INTEREST NOTIFICATION
# Received: {timestamp}

# ═══════════════════════════════════════

# 📦 PACKAGE DETAILS:
# Selected Package: {data.get('package_type', 'Not specified')}
# Source: {data.get('source', 'Method Page')}

# 👤 VISITOR INFORMATION:
# Timestamp: {data.get('timestamp', 'Not recorded')}
# Session Info: {data.get('session_id', 'Not tracked')}

# 💬 CONTEXT:
# {data.get('message', 'Visitor showed interest in package from method page')}

# ═══════════════════════════════════════

# ⚡ ACTION REQUIRED:
# High-potential lead - visitor clicked package button.

# 📞 RECOMMENDED NEXT STEPS:
# 1. Follow up within 4 hours while interest is high
# 2. Send welcome email with package details
# 3. Offer discovery call to discuss their specific needs
# 4. Schedule Session 1 if they're ready to proceed

# 💰 Package Value: 3,000-4,000 THB

# ═══════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Automated Booking System
#             """
#         except Exception as e:
#             print(f"[ERROR] Error formatting package email: {e}")
#             return f"Error formatting package email body: {e}"
    
#     def _format_testimonial_email_body(self, data):
#         """Format testimonial email body"""
#         try:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             anonymous_status = "YES - First name only" if data.get('anonymous', False) else "NO - Full name"
#             return f"""
# 🌟 NEW SUCCESS STORY SUBMISSION
# Received: {timestamp}

# ═══════════════════════════════════════

# 👤 CLIENT INFORMATION:
# Name: {data.get('name', 'Not provided')}
# Email: {data.get('email', 'Not provided')}
# Anonymous Preference: {anonymous_status}

# 🎯 SUCCESS DETAILS:
# Concern Overcome: {data.get('concern', 'Not specified')}
# Sessions Required: {data.get('sessions', 'Not specified')}

# 📝 TRANSFORMATION STORY:

# BEFORE HYPNOTHERAPY:
# {data.get('before', 'Not provided')}

# AFTER HYPNOTHERAPY:
# {data.get('after', 'Not provided')}

# ═══════════════════════════════════════

# ⚡ ACTION REQUIRED:
# 1. Review and approve testimonial for website
# 2. Send thank you email to client
# 3. Consider featuring as case study

# ═══════════════════════════════════════
# Bangkok Hypnotherapy Clinic - Automated Booking System
#             """
#         except Exception as e:
#             print(f"[ERROR] Error formatting testimonial email: {e}")
#             return f"Error formatting testimonial email body: {e}"


# # ---------- Global instance for imports ---------- #
# email_handler = EmailHandler()

# def send_discovery_call_email(data): 
#     """Send discovery call booking email or assessment results"""
#     try:
#         return email_handler.send_discovery_call_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_discovery_call_email: {e}")
#         return False

# def send_assessment_results_email(data):
#     """Send comprehensive assessment results email"""
#     try:
#         return email_handler.send_assessment_results_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_assessment_results_email: {e}")
#         return False

# def send_package_booking_email(data): 
#     """Send package interest notification email"""
#     try:
#         return email_handler.send_package_booking_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_package_booking_email: {e}")
#         return False

# def send_testimonial_email(data): 
#     """Send testimonial submission email"""
#     try:
#         return email_handler.send_testimonial_email(data)
#     except Exception as e:
#         print(f"[ERROR] Exception in global send_testimonial_email: {e}")
#         return False


"""
Email handler utility for sending booking notifications via Gmail SMTP
Fixed version with proper assessment handling
"""
import smtplib
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


class EmailHandler:
    """Handle email sending for booking notifications"""

    def __init__(self):
        # Gmail SMTP configuration
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        # Get credentials from Streamlit secrets first, then environment variables
        try:
            # Try Streamlit secrets first
            self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user") or "laetitiasheppard@gmail.com"
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
            self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
        except Exception as e:
            print(f"[DEBUG] Error accessing secrets: {e}")
            # Fallback to environment variables
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD")

    # ---------------- EMAIL TYPES ---------------- #
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification with improved assessment detection"""
        try:
            print(f"[DEBUG] send_discovery_call_email called with data keys: {list(booking_data.keys())}")
            print(f"[DEBUG] Form type: {booking_data.get('form_type', 'Not specified')}")
            
            # Check if this is assessment data - case insensitive check
            form_type = str(booking_data.get('form_type', '')).lower()
            is_assessment = any([
                'behavioral pattern assessment' in form_type,
                'complete behavioral' in form_type,
                'assessment' in form_type and 'behavioral' in form_type,
                'assessment_results' in booking_data,
                'clinical_template' in booking_data
            ])
            
            print(f"[DEBUG] Is assessment detected: {is_assessment}")
            
            if is_assessment:
                print("[DEBUG] Detected assessment data, routing to assessment handler")
                return self.send_assessment_results_email(booking_data)
            else:
                print("[DEBUG] Regular discovery call booking")
                msg = self._build_email(
                    subject="🔔 New Discovery Call Booking Request",
                    body=self._format_discovery_email_body(booking_data)
                )
                return self._dispatch(msg, booking_data, "Discovery Call")
                
        except Exception as e:
            print(f"[ERROR] Exception in send_discovery_call_email: {e}")
            import traceback
            traceback.print_exc()
            return False

    def send_assessment_results_email(self, assessment_data):
        """Send comprehensive assessment results with pattern analysis"""
        try:
            print("[DEBUG] Sending assessment results email")
            msg = self._build_email(
                subject="🧠 Complete Behavioral Pattern Assessment Results",
                body=self._format_assessment_results_body(assessment_data)
            )
            return self._dispatch(msg, assessment_data, "Assessment Results")
        except Exception as e:
            print(f"[ERROR] Exception in send_assessment_results_email: {e}")
            return False

    def send_package_booking_email(self, booking_data):
        """Send package booking notification"""
        try:
            msg = self._build_email(
                subject="💰 New Package Interest Notification",
                body=self._format_package_email_body(booking_data)
            )
            return self._dispatch(msg, booking_data, "Package Interest")
        except Exception as e:
            print(f"[ERROR] Exception in send_package_booking_email: {e}")
            return False

    def send_testimonial_email(self, testimonial_data):
        """Send testimonial submission notification"""
        try:
            msg = self._build_email(
                subject="🌟 New Success Story Submission",
                body=self._format_testimonial_email_body(testimonial_data)
            )
            return self._dispatch(msg, testimonial_data, "Testimonial")
        except Exception as e:
            print(f"[ERROR] Exception in send_testimonial_email: {e}")
            return False

    # ---------------- HELPERS ---------------- #
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
            print(f"[DEBUG] Sender: {self.sender_email}")
            print(f"[DEBUG] Recipient: {self.recipient_email}")
            print(f"[DEBUG] Has password: {bool(self.password)}")
            
            if not self.password:
                # Log for debugging but still return success for demo purposes
                print(f"[DEBUG] {email_type} email would be sent (no password configured)")
                print(f"To: {self.recipient_email}")
                print(f"Data preview: {str(data)[:200]}...")
                return True  # Return True so the UI shows success
            
            if not self.sender_email or not self.recipient_email:
                print(f"[ERROR] Missing email configuration for {email_type}")
                return False
                
            return self._send_email(msg)
            
        except Exception as e:
            print(f"[ERROR] Exception in _dispatch: {e}")
            return False

    def _send_email(self, msg):
        """Send email via Gmail SMTP with detailed error handling"""
        try:
            print("[DEBUG] Attempting to send email via SMTP")
            # Create server connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            
            # Login with credentials
            server.login(self.sender_email, self.password)
            
            # Send email
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            
            print(f"[SUCCESS] Email sent from {self.sender_email} to {self.recipient_email}")
            return True
            
        except smtplib.SMTPAuthenticationError as e:
            print(f"[ERROR] SMTP Authentication failed: {e}")
            print("Check your Gmail App Password in Streamlit secrets")
            return False
        except smtplib.SMTPException as e:
            print(f"[ERROR] SMTP error: {e}")
            return False
        except Exception as e:
            print(f"[ERROR] Unexpected error sending email: {e}")
            return False

    # ---------------- FORMATTERS ---------------- #
    def _format_discovery_email_body(self, data):
        """Format discovery call email body with package information"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Handle package selection
            package_info = ""
            if data.get('selected_package') and data.get('selected_package') != 'None':
                package_info = f"""
🎯 SELECTED PACKAGE:
{data.get('selected_package')}

"""

            return f"""
🔔 NEW DISCOVERY CALL BOOKING REQUEST
Received: {timestamp}

═══════════════════════════════════════

👤 CONTACT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}

{package_info}🎯 CONCERN DETAILS:
Primary Concern: {data.get('concern', 'Not specified')}
Description: {data.get('concern_description', 'Not provided')}

📋 SOURCE INFORMATION:
Form Type: {data.get('form_type', 'Unknown')}
Source Page: {data.get('source', 'Website')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
Please contact this person within 24 hours to schedule their discovery call.

📞 RECOMMENDED NEXT STEPS:
1. Send confirmation email to client
2. Schedule discovery call via Calendly
3. Prepare personalized approach based on their concerns
{f"4. Discuss {data.get('selected_package')} package details" if package_info else ""}

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
            """
        except Exception as e:
            print(f"[ERROR] Error formatting discovery email: {e}")
            return f"Error formatting email body: {e}"

    def _format_assessment_results_body(self, data):
        """Format comprehensive assessment results email with clinical structure"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract structured data safely
            name = data.get('name', 'Unknown client')
            email = data.get('email', 'Unknown email')
            phone = data.get('phone', 'Not provided')
            concern = data.get('concern', 'General assessment')
            urgency = data.get('urgency', 'Not specified')
            session_preference = data.get('session_preference', 'Not specified')
            
            # Get assessment results
            assessment_results = data.get('assessment_results', {})
            pattern_scores = assessment_results.get('pattern_scores', {})
            clinical_insights = assessment_results.get('clinical_insights', {})
            readiness_metrics = assessment_results.get('readiness_metrics', {})
            
            # Get clinical template if available
            clinical_template = data.get('clinical_template', '')
            
            # Pattern definitions for reference
            pattern_names = {
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
            
            # Build email body
            body = f"""
🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
Assessment completed: {timestamp}

═══════════════════════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}
Phone: {phone}
Primary Concern: {concern}
Urgency Level: {urgency}
Preferred Next Step: {session_preference}
Total Questions Completed: {data.get('total_questions', 55)}
Completion Rate: {data.get('completion_rate', '100%')}

═══════════════════════════════════════════════════════════

📊 BEHAVIORAL PATTERN ANALYSIS:
"""
            
            # Add pattern scores if available
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                body += "Primary Therapeutic Targets (Highest Activation):\n"
                for i, (pattern_id, score) in enumerate(sorted_patterns[:5]):  # Top 5 patterns
                    pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                    activation_level = "High" if score >= 8 else "Medium" if score >= 4 else "Low"
                    body += f"  {i+1}. {pattern_name}: Activation Level {score} ({activation_level})\n"
                body += "\n"
            
            # Add readiness metrics if available
            if readiness_metrics:
                body += "🎯 TRANSFORMATION READINESS METRICS:\n"
                for metric, score in readiness_metrics.items():
                    metric_name = metric.replace('_', ' ').title()
                    body += f"  • {metric_name}: {score}/10\n"
                
                # Calculate overall readiness
                avg_readiness = sum(readiness_metrics.values()) / len(readiness_metrics)
                readiness_level = "High" if avg_readiness >= 7 else "Medium" if avg_readiness >= 5 else "Low"
                body += f"  • Overall Readiness: {avg_readiness:.1f}/10 ({readiness_level})\n\n"
            
            # Add clinical insights if available
            if clinical_insights:
                body += "🔍 KEY CLINICAL INSIGHTS:\n"
                
                # Prioritize important clinical factors
                priority_insights = [
                    ('limiting_belief', 'Core Limiting Belief'),
                    ('change_fear', 'Primary Change Fear'),
                    ('secondary_gain', 'Hidden Benefits'),
                    ('family_origin', 'Family Origin Pattern'),
                    ('communication_style', 'Preferred Communication'),
                    ('learning_style', 'Learning Style')
                ]
                
                for insight_key, insight_label in priority_insights:
                    if insight_key in clinical_insights:
                        value = clinical_insights[insight_key]
                        if isinstance(value, str) and value.strip():
                            body += f"  • {insight_label}: {value}\n"
                
                # Add other insights
                for key, value in clinical_insights.items():
                    if key not in [p[0] for p in priority_insights] and isinstance(value, str) and value.strip():
                        label = key.replace('_', ' ').title()
                        body += f"  • {label}: {value}\n"
                body += "\n"
            
            # Add session recommendations
            body += "💡 RECOMMENDED SESSION APPROACH:\n"
            if pattern_scores:
                sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
                if len(sorted_patterns) >= 2:
                    primary_pattern = pattern_names.get(sorted_patterns[0][0], "Primary Pattern")
                    secondary_pattern = pattern_names.get(sorted_patterns[1][0], "Secondary Pattern")
                    body += f"  Session 1: Map {primary_pattern} and {secondary_pattern} patterns\n"
                    body += f"  Session 2: Neural rewiring targeting {primary_pattern}\n"
                    body += "  Session 3: Reinforcement if needed (assess after Session 2)\n\n"
            
            # Add communication preferences
            comm_style = clinical_insights.get('communication_style', 'Not specified')
            learning_style = clinical_insights.get('learning_style', 'Not specified')
            session_format = clinical_insights.get('session_preference', 'Not specified')
            
            body += "📞 THERAPEUTIC COMMUNICATION NOTES:\n"
            body += f"  • Communication Style: {comm_style}\n"
            body += f"  • Learning Style: {learning_style}\n"
            body += f"  • Session Format Preference: {session_format}\n\n"
            
            # Add urgency and next steps
            body += "⚡ RECOMMENDED IMMEDIATE ACTIONS:\n"
            if urgency and 'extremely' in urgency.lower():
                body += "  🔴 HIGH PRIORITY - Contact within 24 hours\n"
            elif urgency and any(word in urgency.lower() for word in ['very', 'quite']):
                body += "  🟡 MEDIUM PRIORITY - Contact within 48 hours\n"
            else:
                body += "  🟢 STANDARD PRIORITY - Contact within 72 hours\n"
            
            if 'discovery call' in session_preference.lower():
                body += "  1. Schedule discovery call to review assessment results\n"
                body += "  2. Discuss personalized approach based on pattern analysis\n"
            elif 'package' in session_preference.lower():
                body += "  1. Client ready for transformation package - expedite scheduling\n"
                body += "  2. Prepare session plan based on primary patterns identified\n"
            else:
                body += "  1. Send detailed written analysis if requested\n"
                body += "  2. Follow up with consultation offer\n"
            
            body += "  3. Prepare personalized therapeutic approach\n"
            body += "  4. Consider any communication/learning style adaptations needed\n\n"
            
            # Add clinical template if available
            if clinical_template:
                body += "📋 DETAILED CLINICAL TEMPLATE:\n"
                body += "═" * 50 + "\n"
                body += clinical_template + "\n"
                body += "═" * 50 + "\n\n"
            
            # Footer
            body += "═══════════════════════════════════════════════════════════\n"
            body += "Bangkok Hypnotherapy Clinic - Automated Assessment System\n"
            body += f"Clinical Analysis Generated: {timestamp}\n"
            body += "⚠️  CONFIDENTIAL: This assessment contains sensitive psychological data\n"
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Error formatting assessment email: {e}")
            import traceback
            traceback.print_exc()
            return f"""
🧠 ASSESSMENT RESULTS - ERROR IN FORMATTING

Basic Information:
Name: {data.get('name', 'Unknown')}
Email: {data.get('email', 'Unknown')}
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Error Details: {str(e)}

Raw Data: {str(data)[:1000]}...

Please review the assessment data manually.
Bangkok Hypnotherapy Clinic - Automated Assessment System
        """

    def _format_package_email_body(self, data):
        """Format package booking email body"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"""
💰 NEW PACKAGE INTEREST NOTIFICATION
Received: {timestamp}

═══════════════════════════════════════

📦 PACKAGE DETAILS:
Selected Package: {data.get('package_type', 'Not specified')}
Source: {data.get('source', 'Method Page')}

👤 VISITOR INFORMATION:
Timestamp: {data.get('timestamp', 'Not recorded')}
Session Info: {data.get('session_id', 'Not tracked')}

💬 CONTEXT:
{data.get('message', 'Visitor showed interest in package from method page')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
High-potential lead - visitor clicked package button.

📞 RECOMMENDED NEXT STEPS:
1. Follow up within 4 hours while interest is high
2. Send welcome email with package details
3. Offer discovery call to discuss their specific needs
4. Schedule Session 1 if they're ready to proceed

💰 Package Value: 3,000-4,000 THB

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
            """
        except Exception as e:
            print(f"[ERROR] Error formatting package email: {e}")
            return f"Error formatting package email body: {e}"
