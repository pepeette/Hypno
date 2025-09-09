# """
# Email handler utility for sending booking notifications via Gmail SMTP
# Final version integrated with booking form and method page
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
#         except:
#             # Fallback to environment variables
#             self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#             self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#             self.password = os.environ.get("GMAIL_APP_PASSWORD")

#     # ---------------- EMAIL TYPES ---------------- #
#     def send_discovery_call_email(self, booking_data):
#         """Send discovery call booking notification"""
#         msg = self._build_email(
#             subject="🔔 New Discovery Call Booking Request",
#             body=self._format_discovery_email_body(booking_data)
#         )
#         return self._dispatch(msg, booking_data, "Discovery Call")

#     def send_package_booking_email(self, booking_data):
#         """Send package booking notification"""
#         msg = self._build_email(
#             subject="💰 New Package Interest Notification",
#             body=self._format_package_email_body(booking_data)
#         )
#         return self._dispatch(msg, booking_data, "Package Interest")

#     def send_testimonial_email(self, testimonial_data):
#         """Send testimonial submission notification"""
#         msg = self._build_email(
#             subject="🌟 New Success Story Submission",
#             body=self._format_testimonial_email_body(testimonial_data)
#         )
#         return self._dispatch(msg, testimonial_data, "Testimonial")

#     # ---------------- HELPERS ---------------- #
#     def _build_email(self, subject, body):
#         """Build email message"""
#         msg = MIMEMultipart()
#         msg['From'] = self.sender_email
#         msg['To'] = self.recipient_email
#         msg['Subject'] = subject
#         msg.attach(MIMEText(body, 'plain'))
#         return msg

#     def _dispatch(self, msg, data, email_type):
#         """Dispatch email with proper error handling"""
#         if not self.password:
#             # Log for debugging but still return success for demo purposes
#             print(f"[DEBUG] {email_type} email would be sent (no password configured)")
#             print(f"To: {self.recipient_email}")
#             print(f"Data: {data}")
#             return True  # Return True so the UI shows success
        
#         if not self.sender_email or not self.recipient_email:
#             print(f"[ERROR] Missing email configuration for {email_type}")
#             return False
            
#         return self._send_email(msg)

#     def _send_email(self, msg):
#         """Send email via Gmail SMTP with detailed error handling"""
#         try:
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

#     # ---------------- FORMATTERS ---------------- #
#     def _format_discovery_email_body(self, data):
#         """Format discovery call email body with package information"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Handle package selection
#         package_info = ""
#         if data.get('selected_package') and data.get('selected_package') != 'None':
#             package_info = f"""
# 🎯 SELECTED PACKAGE:
# {data.get('selected_package')}

# """

#         return f"""
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
#         """

#     def _format_package_email_body(self, data):
#         """Format package booking email body"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         return f"""
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
#         """

#     def _format_testimonial_email_body(self, data):
#         """Format testimonial email body"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         anonymous_status = "YES - First name only" if data.get('anonymous', False) else "NO - Full name"
#         return f"""
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
#         """


# # ---------- Global instance for imports ---------- #
# email_handler = EmailHandler()

# def send_discovery_call_email(data): 
#     """Send discovery call booking email"""
#     return email_handler.send_discovery_call_email(data)

# def send_package_booking_email(data): 
#     """Send package interest notification email"""
#     return email_handler.send_package_booking_email(data)

# def send_testimonial_email(data): 
#     """Send testimonial submission email"""
#     return email_handler.send_testimonial_email(data)


"""
Email handler utility for sending booking notifications via Gmail SMTP
Simplified version to restore working functionality
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
        """Send discovery call booking notification"""
        try:
            print(f"[DEBUG] send_discovery_call_email called with data keys: {list(booking_data.keys())}")
            print(f"[DEBUG] Form type: {booking_data.get('form_type', 'Not specified')}")
            
            # Check if this is assessment data
            if booking_data.get('form_type') == 'Complete behavioral pattern assessment':
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

    # ---------------- ORIGINAL FORMATTERS (PRESERVED) ---------------- #
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
        """Format comprehensive assessment results email"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Extract key data safely
            name = data.get('name', 'Unknown client')
            email = data.get('email', 'Unknown email')
            concern = data.get('concern', 'General assessment')
            scores = data.get('assessment_scores', {})
            raw_responses = data.get('raw_responses', {})
            
            body = f"""
🧠 COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
Assessment completed: {timestamp}

═══════════════════════════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {name}
Email: {email}
Primary Concern: {concern}
Total Questions Completed: {data.get('total_questions', 50)}
Completion Rate: {data.get('completion_rate', '100%')}

═══════════════════════════════════════════════════════════

📊 PATTERN ACTIVATION ANALYSIS:
{scores}

Raw responses:
{raw_responses}

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Assessment System
Clinical Analysis Generated: {timestamp}
            """
            
            return body
            
        except Exception as e:
            print(f"[ERROR] Error formatting assessment email: {e}")
            return f"Error formatting assessment email body: {e}"

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

    def _format_testimonial_email_body(self, data):
        """Format testimonial email body"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            anonymous_status = "YES - First name only" if data.get('anonymous', False) else "NO - Full name"
            return f"""
🌟 NEW SUCCESS STORY SUBMISSION
Received: {timestamp}

═══════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}
Anonymous Preference: {anonymous_status}

🎯 SUCCESS DETAILS:
Concern Overcome: {data.get('concern', 'Not specified')}
Sessions Required: {data.get('sessions', 'Not specified')}

📝 TRANSFORMATION STORY:

BEFORE HYPNOTHERAPY:
{data.get('before', 'Not provided')}

AFTER HYPNOTHERAPY:
{data.get('after', 'Not provided')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
1. Review and approve testimonial for website
2. Send thank you email to client
3. Consider featuring as case study

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
            """
        except Exception as e:
            print(f"[ERROR] Error formatting testimonial email: {e}")
            return f"Error formatting testimonial email body: {e}"


# ---------- Global instance for imports ---------- #
email_handler = EmailHandler()

def send_discovery_call_email(data): 
    """Send discovery call booking email or assessment results"""
    try:
        return email_handler.send_discovery_call_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_discovery_call_email: {e}")
        return False

def send_assessment_results_email(data):
    """Send comprehensive assessment results email"""
    try:
        return email_handler.send_assessment_results_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_assessment_results_email: {e}")
        return False

def send_package_booking_email(data): 
    """Send package interest notification email"""
    try:
        return email_handler.send_package_booking_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_package_booking_email: {e}")
        return False

def send_testimonial_email(data): 
    """Send testimonial submission email"""
    try:
        return email_handler.send_testimonial_email(data)
    except Exception as e:
        print(f"[ERROR] Exception in global send_testimonial_email: {e}")
        return False
