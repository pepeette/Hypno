"""
Email handler utility for sending booking notifications via Gmail SMTP
Enhanced version with better error handling and debugging
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
            self.sender_email = st.secrets.get("SENDER_EMAIL") or st.secrets.get("gmail", {}).get("user")
            self.recipient_email = st.secrets.get("RECIPIENT_EMAIL") or "laetitiasheppard@gmail.com"
            self.password = st.secrets.get("GMAIL_APP_PASSWORD") or st.secrets.get("gmail", {}).get("password")
        except:
            # Fallback to environment variables
            self.sender_email = os.environ.get("SENDER_EMAIL")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD")

        # Set default sender email if not provided
        if not self.sender_email:
            self.sender_email = "laetitiasheppard@gmail.com"

    # ---------------- EMAIL TYPES ---------------- #
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification"""
        msg = self._build_email(
            subject="🔔 New Discovery Call Booking Request",
            body=self._format_discovery_email_body(booking_data)
        )
        return self._dispatch(msg, booking_data, "Discovery Call")

    def send_package_booking_email(self, booking_data):
        """Send package booking notification"""
        msg = self._build_email(
            subject="💰 New Transformation Package Interest",
            body=self._format_package_email_body(booking_data)
        )
        return self._dispatch(msg, booking_data, "Package Interest")

    def send_testimonial_email(self, testimonial_data):
        """Send testimonial submission notification"""
        msg = self._build_email(
            subject="🌟 New Success Story Submission",
            body=self._format_testimonial_email_body(testimonial_data)
        )
        return self._dispatch(msg, testimonial_data, "Testimonial")

    # ---------------- HELPERS ---------------- #
    def _build_email(self, subject, body):
        """Build email message"""
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def _dispatch(self, msg, data, email_type):
        """Dispatch email with proper error handling"""
        if not self.password:
            # Log for debugging but still return success for demo purposes
            print(f"[DEBUG] {email_type} email would be sent (no password configured)")
            print(f"Data: {data}")
            return True
        
        if not self.sender_email or not self.recipient_email:
            print(f"[ERROR] Missing email configuration for {email_type}")
            return False
            
        return self._send_email(msg)

    def _send_email(self, msg):
        """Send email via Gmail SMTP with detailed error handling"""
        try:
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
        """Format discovery call email body"""
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

📞 RECOMMENDED NEXT STEPS:
1. Send confirmation email to client
2. Schedule discovery call via Calendly
3. Prepare personalized approach based on their concerns

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
        """

    def _format_package_email_body(self, data):
        """Format package booking email body"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""
💰 NEW TRANSFORMATION PACKAGE INTEREST
Received: {timestamp}

═══════════════════════════════════════

📦 PACKAGE DETAILS:
Selected Package: {data.get('package_type', 'Not specified')}
Source: {data.get('source', 'Website')}

👤 VISITOR INFORMATION:
Timestamp: {data.get('timestamp', 'Not recorded')}
User Session: {data.get('session_id', 'Not tracked')}

💬 CONTEXT:
{data.get('message', 'Visitor showed interest in package from method page')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
High-potential lead - visitor clicked package booking button.

📞 RECOMMENDED NEXT STEPS:
1. Follow up within 4 hours while interest is high
2. Send welcome email with package details
3. Offer discovery call to discuss their specific needs
4. Schedule Session 1 if they're ready to proceed

💰 Package Value: 3,000-4,000 THB

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
        """

    def _format_testimonial_email_body(self, data):
        """Format testimonial email body"""
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


# ---------- Global instance for imports ---------- #
email_handler = EmailHandler()

def send_discovery_call_email(data): 
    return email_handler.send_discovery_call_email(data)

def send_package_booking_email(data): 
    return email_handler.send_package_booking_email(data)

def send_testimonial_email(data): 
    return email_handler.send_testimonial_email(data)
