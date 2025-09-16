# utils/email_unified.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import streamlit as st

class UnifiedEmailHandler:
    """Single email handler for all assessment communications"""
    
    def __init__(self):
        self.smtp_server = st.secrets.get("email", {}).get("smtp_server", "smtp.gmail.com")
        self.smtp_port = int(st.secrets.get("email", {}).get("smtp_port", 587))
        self.sender_email = st.secrets.get("email", {}).get("sender_email")
        self.password = st.secrets.get("email", {}).get("password")
        
    def send_assessment_results(self, assessment_data, template_type="standard"):
        """Send assessment results with specified template"""
        templates = {
            "standard": self._create_standard_template,
            "premium": self._create_premium_template,
            "blueprint": self._create_blueprint_template
        }
        
        template_func = templates.get(template_type, self._create_standard_template)
        email_content = template_func(assessment_data)
        
        return self._send_email(email_content)
    
    def send_with_attachment(self, assessment_data, attachment_data, filename):
        """Send email with PDF attachment"""
        email_content = self._create_blueprint_template(assessment_data)
        email_content['attachments'] = [(attachment_data, filename, 'application/pdf')]
        
        return self._send_email(email_content)

# Replace both email_assess.py and email_blueprint_streamlit.py with this
