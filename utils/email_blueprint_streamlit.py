"""
Create utils/email_blueprint_streamlit.py:
"""

import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import tempfile
import os

# COMMENTED OUT: Full email implementation for production
"""
# Full email implementation - uncomment for production use
# Requires email server configuration

def send_blueprint_email_production(user_email, user_name, assessment_data, pdf_attachment=None):
    try:
        # Email configuration from Streamlit secrets
        smtp_server = st.secrets.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(st.secrets.get("SMTP_PORT", "587"))
        sender_email = st.secrets.get("SENDER_EMAIL")
        sender_password = st.secrets.get("SENDER_PASSWORD")
        
        if not all([sender_email, sender_password]):
            st.error("Email configuration missing in secrets")
            return False
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = f"Your Personalized Behavioral Transformation Blueprint - {user_name}"
        
        # Email body
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        body = f'''
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
        '''
        
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
        st.error(f"Email sending failed: {str(e)}")
        return False


# Streamlit secrets configuration for email:
# Add to .streamlit/secrets.toml:
# [email]
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# SENDER_EMAIL = "your_clinical_email@gmail.com"  
# SENDER_PASSWORD = "your_app_password"
"""

def send_blueprint_email_streamlit(user_email, user_name, assessment_data, pdf_attachment=None):
    """Streamlit Community Cloud compatible email handling"""
    
    try:
        # For Streamlit Community Cloud, we'll prepare the email data
        # and store it for manual processing by the clinical team
        
        pattern_count = len(assessment_data.get('pattern_scores', {}))
        is_digital_native = assessment_data.get('is_digital_native', False)
        
        # Prepare email data for manual processing
        email_data = {
            'recipient': user_email,
            'recipient_name': user_name,
            'subject': f"Behavioral Transformation Blueprint - {user_name}",
            'assessment_summary': {
                'pattern_count': pattern_count,
                'completion_rate': f"{assessment_data.get('completion_rate', 1.0)*100:.0f}%",
                'is_digital_native': is_digital_native,
                'session_id': assessment_data.get('session_id', '')[:8],
                'urgency': assessment_data.get('contact_info', {}).get('urgency', 'Standard')
            },
            'timestamp': datetime.now().isoformat(),
            'has_pdf_attachment': pdf_attachment is not None
        }
        
        # Store email request in session state for admin processing
        if 'email_requests' not in st.session_state:
            st.session_state.email_requests = []
        
        st.session_state.email_requests.append(email_data)
        
        # Also save to a temporary file for admin access
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        import json
        json.dump(email_data, temp_file, indent=2, default=str)
        temp_file.close()
        
        # Show admin download option in sidebar
        with st.sidebar:
            if st.button("📧 Admin: Download Email Queue"):
                with open(temp_file.name, 'r') as f:
                    st.download_button(
                        "Download Email Request",
                        f.read(),
                        file_name=f"email_request_{email_data['assessment_summary']['session_id']}.json",
                        mime="application/json"
                    )
        
        # Clean up temp file
        os.unlink(temp_file.name)
        
        return True
        
    except Exception as e:
        st.error(f"Email preparation failed: {str(e)}")
        return False

def get_pending_email_requests():
    """Get all pending email requests for admin processing"""
    return st.session_state.get('email_requests', [])

def clear_email_requests():
    """Clear processed email requests"""
    st.session_state.email_requests = []
