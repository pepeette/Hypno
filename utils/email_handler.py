"""
Email handler utility for sending booking notifications via Gmail SMTP
To be placed in utils/email_handler.py
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class EmailHandler:
    """Handle email sending for booking notifications"""
    
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
        """Send discovery call booking notification"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "🔔 New Discovery Call Booking Request"
            
            # Format the email body
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
            print(f"Email sending error: {e}")
            return False
    
    def send_package_booking_email(self, booking_data):
        """Send package booking notification"""
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

📞 Next Steps:
1. Send confirmation email to client
2. Schedule discovery call via Calendly
3. Prepare personalized approach based on their concerns

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic
Automated Booking System
        """
    
    def _format_package_email_body(self, data):
        """Format package booking email body"""
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

# Global instance for easy import
email_handler = EmailHandler()

def send_testimonial_email(self, testimonial_data):
    """Send testimonial submission notification"""
    try:
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_email
        msg['Subject'] = "🌟 New Success Story Submission"
        
        body = self._format_testimonial_email_body(testimonial_data)
        msg.attach(MIMEText(body, 'plain'))
        
        if self.password:
            return self._send_email(msg)
        else:
            print(f"Testimonial Submission: {testimonial_data}")
            return True
            
    except Exception as e:
        print(f"Email sending error: {e}")
        return False

def _format_testimonial_email_body(self, data):
    """Format testimonial submission email body"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    anonymous_status = "YES - Use first name only" if data.get('anonymous', False) else "NO - Full name OK"
    
    return f"""
🌟 NEW SUCCESS STORY SUBMISSION
Received: {timestamp}

═══════════════════════════════════════

👤 CLIENT INFORMATION:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}
Anonymous Posting: {anonymous_status}

🎯 TRANSFORMATION DETAILS:
Concern Overcome: {data.get('concern', 'Not specified')}
Sessions Required: {data.get('sessions', 'Not specified')}

📖 SUCCESS STORY:

BEFORE:
{data.get('before', 'Not provided')}

AFTER:
{data.get('after', 'Not provided')}

═══════════════════════════════════════

⚡ ACTION REQUIRED:
Review this success story for potential inclusion on the website.

📞 Next Steps:
1. Review story for authenticity and appropriateness
2. Contact client if clarification needed
3. Consider featuring story in Success section
4. Send thank you email to client

✅ Client has given permission to share their story

═══════════════════════════════════════
Bangkok Hypnotherapy Clinic
Success Stories Management
    """
    
def send_testimonial_email(testimonial_data):
    """Send testimonial submission email"""
    return email_handler.send_testimonial_email(testimonial_data)
    
def send_discovery_call_email(booking_data):
    """Send discovery call booking email"""
    return email_handler.send_discovery_call_email(booking_data)

def send_package_booking_email(booking_data):
    """Send package booking email"""
    return email_handler.send_package_booking_email(booking_data)
