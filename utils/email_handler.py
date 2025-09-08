"""
Email handler utility for sending booking notifications via Gmail SMTP
To be placed in utils/email_handler.py
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

        # Fetch from Streamlit secrets (preferred) or fallback to env
        self.sender_email = st.secrets.get("SENDER_EMAIL", os.environ.get("SENDER_EMAIL"))
        self.recipient_email = st.secrets.get("RECIPIENT_EMAIL", os.environ.get("RECIPIENT_EMAIL"))
        self.password = st.secrets.get("GMAIL_APP_PASSWORD", os.environ.get("GMAIL_APP_PASSWORD"))

    # ---------------- EMAIL TYPES ---------------- #
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification"""
        msg = self._build_email(
            subject="🔔 New Discovery Call Booking Request",
            body=self._format_discovery_email_body(booking_data)
        )
        return self._dispatch(msg, booking_data)

    def send_package_booking_email(self, booking_data):
        """Send package booking notification"""
        msg = self._build_email(
            subject="💰 New Transformation Package Booking",
            body=self._format_package_email_body(booking_data)
        )
        return self._dispatch(msg, booking_data)

    def send_testimonial_email(self, testimonial_data):
        """Send testimonial submission notification"""
        msg = self._build_email(
            subject="🌟 New Success Story Submission",
            body=self._format_testimonial_email_body(testimonial_data)
        )
        return self._dispatch(msg, testimonial_data)

    # ---------------- HELPERS ---------------- #
    def _build_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def _dispatch(self, msg, data):
        if not self.password:
            print(f"[DEBUG] Email not sent (no password). Data:\n{data}")
            return True
        return self._send_email(msg)

    def _send_email(self, msg):
        """Send email via Gmail SMTP"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"SMTP error: {e}")
            return False

    # ---------------- FORMATTERS ---------------- #
    def _format_discovery_email_body(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""
🔔 NEW DISCOVERY CALL BOOKING REQUEST
Received: {timestamp}

👤 Name: {data.get('name', 'Not provided')}
📧 Email: {data.get('email', 'Not provided')}

🎯 Concern: {data.get('concern', 'Not specified')}
Details: {data.get('concern_description', 'Not provided')}

Urgency: {data.get('urgency', 'Not specified')}
Experience: {data.get('experience', 'Not specified')}
Contact Method: {data.get('contact_method', 'Not specified')}

💬 Message:
{data.get('message', 'None provided')}
        """

    def _format_package_email_body(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""
💰 NEW TRANSFORMATION PACKAGE BOOKING
Received: {timestamp}

👤 Name: {data.get('name', 'Not provided')}
📧 Email: {data.get('email', 'Not provided')}

🎯 Selected Package: {data.get('package_type', 'Not specified')}
Concern: {data.get('concern', 'Not specified')}
Experience: {data.get('experience', 'Not specified')}

💬 Message:
{data.get('message', 'None provided')}
        """

    def _format_testimonial_email_body(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        anonymous_status = "YES - First name only" if data.get('anonymous', False) else "NO - Full name"
        return f"""
🌟 NEW SUCCESS STORY SUBMISSION
Received: {timestamp}

👤 Name: {data.get('name', 'Not provided')}
📧 Email: {data.get('email', 'Not provided')}
Anonymous: {anonymous_status}

🎯 Concern Overcome: {data.get('concern', 'Not specified')}
Sessions Required: {data.get('sessions', 'Not specified')}

BEFORE:
{data.get('before', 'Not provided')}

AFTER:
{data.get('after', 'Not provided')}
        """


# ---------- Global instance for imports ---------- #
email_handler = EmailHandler()

def send_discovery_call_email(data): return email_handler.send_discovery_call_email(data)
def send_package_booking_email(data): return email_handler.send_package_booking_email(data)
def send_testimonial_email(data): return email_handler.send_testimonial_email(data)
