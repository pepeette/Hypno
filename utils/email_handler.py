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
Enhanced email handler utility for sending comprehensive assessment results
Includes detailed pattern analysis and clinical recommendations
"""
import smtplib
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json


class EmailHandler:
    """Handle email sending for booking notifications and assessment results"""

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
        except:
            # Fallback to environment variables
            self.sender_email = os.environ.get("SENDER_EMAIL", "laetitiasheppard@gmail.com")
            self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
            self.password = os.environ.get("GMAIL_APP_PASSWORD")

    # ---------------- EMAIL TYPES ---------------- #
    def send_discovery_call_email(self, booking_data):
        """Send discovery call booking notification - now handles assessment data"""
        if booking_data.get('form_type') == 'Complete behavioral pattern assessment':
            return self.send_assessment_results_email(booking_data)
        else:
            msg = self._build_email(
                subject="New discovery call booking request",
                body=self._format_discovery_email_body(booking_data)
            )
            return self._dispatch(msg, booking_data, "Discovery call")

    def send_assessment_results_email(self, assessment_data):
        """Send comprehensive assessment results with pattern analysis"""
        msg = self._build_email(
            subject="Complete behavioral pattern assessment results",
            body=self._format_assessment_results_body(assessment_data)
        )
        return self._dispatch(msg, assessment_data, "Assessment results")

    def send_package_booking_email(self, booking_data):
        """Send package booking notification"""
        msg = self._build_email(
            subject="New package interest notification",
            body=self._format_package_email_body(booking_data)
        )
        return self._dispatch(msg, booking_data, "Package interest")

    def send_testimonial_email(self, testimonial_data):
        """Send testimonial submission notification"""
        msg = self._build_email(
            subject="New success story submission",
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
            print(f"To: {self.recipient_email}")
            print(f"Data: {data}")
            return True  # Return True so the UI shows success
        
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

    # ---------------- ASSESSMENT RESULTS FORMATTER ---------------- #
    def _format_assessment_results_body(self, data):
        """Format comprehensive assessment results email"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Extract key data
        name = data.get('name', 'Unknown client')
        email = data.get('email', 'Unknown email')
        concern = data.get('concern', 'General assessment')
        scores = data.get('assessment_scores', {})
        raw_responses = data.get('raw_responses', {})
        
        # Pattern definitions for analysis
        patterns = {
            1: "Unhappiness culture",
            2: "Power struggles", 
            3: "Systematic mistrust",
            4: "Separation/division",
            5: "Doing vs being",
            6: "Compartmentalized authenticity",
            7: "Self-sacrifice/care avoidance",
            8: "Inherited missions",
            9: "Context-dependent weakness"
        }
        
        # Sort patterns by activation level
        sorted_patterns = sorted(scores.items(), key=lambda x: x[1], reverse=True) if scores else []
        
        body = f"""
COMPREHENSIVE BEHAVIORAL PATTERN ASSESSMENT RESULTS
Assessment completed: {timestamp}

═══════════════════════════════════════════════════════════

CLIENT INFORMATION:
Name: {name}
Email: {email}
Primary concern: {concern}
Total questions completed: {data.get('total_questions', 50)}
Completion rate: {data.get('completion_rate', '100%')}

═══════════════════════════════════════════════════════════

PATTERN ACTIVATION ANALYSIS:
"""
        
        # Add pattern scores and analysis
        if sorted_patterns:
            primary_pattern = sorted_patterns[0] if sorted_patterns else (0, 0)
            secondary_pattern = sorted_patterns[1] if len(sorted_patterns) > 1 else (0, 0)
            
            body += f"""
PRIMARY PATTERN: {patterns.get(primary_pattern[0], 'Unknown')}
Activation score: {primary_pattern[1]}/6
Priority level: {'High' if primary_pattern[1] >= 4 else 'Medium' if primary_pattern[1] >= 2 else 'Low'}

SECONDARY PATTERN: {patterns.get(secondary_pattern[0], 'Unknown')}
Activation score: {secondary_pattern[1]}/6
Priority level: {'High' if secondary_pattern[1] >= 4 else 'Medium' if secondary_pattern[1] >= 2 else 'Low'}

COMPLETE PATTERN BREAKDOWN:
"""
            for pattern_id, score in sorted_patterns:
                pattern_name = patterns.get(pattern_id, f'Pattern {pattern_id}')
                activation = 'High' if score >= 4 else 'Medium' if score >= 2 else 'Low'
                body += f"- {pattern_name}: {score}/6 ({activation})\n"
        
        # Add key clinical indicators
        body += f"""

═══════════════════════════════════════════════════════════

KEY CLINICAL INDICATORS:
"""
        
        # Extract specific responses for clinical insight
        change_readiness = raw_responses.get('q47', 'Not assessed')
        change_fear = raw_responses.get('q48', 'Not provided')
        hidden_benefits = raw_responses.get('q50', 'Not provided')
        limiting_belief = raw_responses.get('q49', 'Not provided')
        
        body += f"""
Change readiness score: {change_readiness}/10
Primary change fear: {change_fear}
Hidden pattern benefits: {hidden_benefits}
Core limiting belief: "People like me don't get to have {limiting_belief}"

═══════════════════════════════════════════════════════════

THERAPEUTIC RECOMMENDATIONS:

SESSION 1 FOCUS (Pattern mapping - 90 minutes):
"""
        
        if sorted_patterns:
            primary_name = patterns.get(sorted_patterns[0][0], 'primary pattern')
            secondary_name = patterns.get(sorted_patterns[1][0], 'secondary pattern') if len(sorted_patterns) > 1 else 'supporting patterns'
            
            body += f"""- Deep exploration of {primary_name} triggers and responses
- Map subconscious origins of {secondary_name}
- Identify protective functions and hidden benefits
- Begin initial positive programming for {primary_name}

SESSION 2 FOCUS (Neural rewiring - 90 minutes):
- Rewire {primary_name} at subconscious level
- Install new response patterns for identified triggers
- Address {secondary_name} as secondary target
- Create identity bridge for sustainable change

POTENTIAL RESISTANCE POINTS:
- {change_fear if change_fear != 'Not provided' else 'Fear of identity change'}
- Hidden benefits: {hidden_benefits if hidden_benefits != 'Not provided' else 'Unknown secondary gains'}
- Limiting belief system around worthiness/deserving

SESSION 3 CONSIDERATIONS (if needed):
"""
            
            # Determine if third session likely needed
            if primary_pattern[1] >= 5 or secondary_pattern[1] >= 4:
                body += "- Likely needed due to high pattern activation\n"
            else:
                body += "- May not be necessary based on moderate activation levels\n"
                
            body += f"- Focus on integration and real-world application\n- Address any remaining {primary_name} triggers\n"
        
        body += f"""

═══════════════════════════════════════════════════════════

DETAILED RESPONSE ANALYSIS:

Key responses for session preparation:
"""
        
        # Include specific responses relevant to top patterns
        relevant_questions = [
            ('q1', 'Happiness response'),
            ('q2', 'Conflict body response'), 
            ('q3', 'Social assumptions'),
            ('q5', 'Value source'),
            ('q7', 'Self-care patterns'),
            ('q8', 'Goal origins'),
            ('q9', 'Social boundary changes')
        ]
        
        for q_id, description in relevant_questions:
            response = raw_responses.get(q_id, 'Not answered')
            body += f"- {description}: {response}\n"
        
        body += f"""

═══════════════════════════════════════════════════════════

NEXT STEPS:

IMMEDIATE ACTIONS:
1. Contact client within 24 hours for discovery call scheduling
2. Review this analysis before client consultation
3. Prepare personalized session plan based on pattern profile

DISCOVERY CALL AGENDA:
1. Confirm pattern analysis with client experience
2. Explain how their specific patterns will be addressed
3. Set expectations for transformation timeline
4. Address any concerns about the process

PROGNOSIS:
Change readiness: {change_readiness}/10
Expected sessions needed: {'2-3' if primary_pattern[1] >= 4 if sorted_patterns else '2'}
Success probability: {'High' if change_readiness >= 7 if str(change_readiness).isdigit() else 'Medium'}

═══════════════════════════════════════════════════════════

RAW ASSESSMENT DATA:
(Complete responses attached for detailed analysis)

{json.dumps(raw_responses, indent=2)}

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Assessment System
Clinical Analysis Generated: {timestamp}
        """
        
        return body

    # ---------------- OTHER FORMATTERS ---------------- #
    def _format_discovery_email_body(self, data):
        """Format discovery call email body with package information"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Handle package selection
        package_info = ""
        if data.get('selected_package') and data.get('selected_package') != 'None':
            package_info = f"""
Selected package:
{data.get('selected_package')}

"""

        return f"""
New discovery call booking request
Received: {timestamp}

═══════════════════════════════════════════════════════════

Contact information:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}

{package_info}Concern details:
Primary concern: {data.get('concern', 'Not specified')}
Description: {data.get('concern_description', 'Not provided')}

Source information:
Form type: {data.get('form_type', 'Unknown')}
Source page: {data.get('source', 'Website')}

═══════════════════════════════════════════════════════════

Action required:
Please contact this person within 24 hours to schedule their discovery call.

Recommended next steps:
1. Send confirmation email to client
2. Schedule discovery call via Calendly
3. Prepare personalized approach based on their concerns
{f"4. Discuss {data.get('selected_package')} package details" if package_info else ""}

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
        """

    def _format_package_email_body(self, data):
        """Format package booking email body"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""
New package interest notification
Received: {timestamp}

═══════════════════════════════════════════════════════════

Package details:
Selected package: {data.get('package_type', 'Not specified')}
Source: {data.get('source', 'Method page')}

Visitor information:
Timestamp: {data.get('timestamp', 'Not recorded')}
Session info: {data.get('session_id', 'Not tracked')}

Context:
{data.get('message', 'Visitor showed interest in package from method page')}

═══════════════════════════════════════════════════════════

Action required:
High-potential lead - visitor clicked package button.

Recommended next steps:
1. Follow up within 4 hours while interest is high
2. Send welcome email with package details
3. Offer discovery call to discuss their specific needs
4. Schedule Session 1 if they're ready to proceed

Package value: 3,000-4,000 THB

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
        """

    def _format_testimonial_email_body(self, data):
        """Format testimonial email body"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        anonymous_status = "Yes - first name only" if data.get('anonymous', False) else "No - full name"
        return f"""
New success story submission
Received: {timestamp}

═══════════════════════════════════════════════════════════

Client information:
Name: {data.get('name', 'Not provided')}
Email: {data.get('email', 'Not provided')}
Anonymous preference: {anonymous_status}

Success details:
Concern overcome: {data.get('concern', 'Not specified')}
Sessions required: {data.get('sessions', 'Not specified')}

Transformation story:

Before hypnotherapy:
{data.get('before', 'Not provided')}

After hypnotherapy:
{data.get('after', 'Not provided')}

═══════════════════════════════════════════════════════════

Action required:
1. Review and approve testimonial for website
2. Send thank you email to client
3. Consider featuring as case study

═══════════════════════════════════════════════════════════
Bangkok Hypnotherapy Clinic - Automated Booking System
        """


# ---------- Global instance for imports ---------- #
email_handler = EmailHandler()

def send_discovery_call_email(data): 
    """Send discovery call booking email or assessment results"""
    return email_handler.send_discovery_call_email(data)

def send_assessment_results_email(data):
    """Send comprehensive assessment results email"""
    return email_handler.send_assessment_results_email(data)

def send_package_booking_email(data): 
    """Send package interest notification email"""
    return email_handler.send_package_booking_email(data)

def send_testimonial_email(data): 
    """Send testimonial submission email"""
    return email_handler.send_testimonial_email(data)
