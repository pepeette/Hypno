"""
Create utils/email_blueprint.py:
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from datetime import datetime

def send_blueprint_email(user_email, user_name, assessment_data, pdf_attachment=None):
    """Send blueprint email with optional PDF attachment"""
    
    try:
        # Email configuration
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_PASSWORD')
        
        if not all([sender_email, sender_password]):
            return False
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = f"Your Personalized Behavioral Transformation Blueprint - {user_name}"
        
        # Email body
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        body = f"""
Dear {user_name},

Thank you for completing your comprehensive behavioral pattern assessment. Your personalized transformation blueprint is attached to this email.

KEY FINDINGS:
• {pattern_count} behavioral patterns identified
• Assessment completion: {assessment_data.get('completion_rate', 1.0)*100:.0f}%
{'• Digital conditioning detected - specialized approach recommended' if is_digital_native else ''}

Your blueprint includes:
✓ Detailed analysis of each behavioral pattern
✓ Hidden cost calculations and future projections
✓ Personalized transformation roadmap
✓ Investment analysis and ROI calculations
✓ Success probability factors
✓ Next steps for rapid transformation

WHAT HAPPENS NEXT:
1. Clinical Review (24-48 hours): Licensed therapist analyzes your assessment
2. Personal Contact (48-72 hours): We'll reach out to schedule your sessions
3. Transformation Begins (Within 1 week): Your personalized protocol starts

IMMEDIATE ACCESS:
• Learn about our method: https://hypnotherapy.streamlit.app
• Schedule consultation: https://calendly.com/laetitiasheppard/discovery

Your transformation journey begins now. We're excited to support you in creating the authentic, empowered life you deserve.

Best regards,
The Clinical Transformation Team

P.S. Keep this blueprint confidential as it contains sensitive psychological insights. Refer back to it throughout your transformation journey.

---
This email was generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
Assessment ID: {assessment_data.get('session_id', 'N/A')[:8]}
        """
        
        # Attach body
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach PDF if provided
        if pdf_attachment:
            pdf_part = MIMEApplication(pdf_attachment, _subtype='pdf')
            pdf_part.add_header('Content-Disposition', 'attachment', 
                              filename=f'behavioral_blueprint_{assessment_data.get("session_id", "")[:8]}.pdf')
            msg.attach(pdf_part)
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, user_email, text)
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False
