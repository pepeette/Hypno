# """
# Enhanced Clinical Assessment Email Handler v2.0
# - Comprehensive crisis screening alerts
# - Enhanced password management with clear error handling
# - Improved clinical summary template with intervention protocols
# - Outcome tracking preparation
# - Better HTML formatting and structure
# - Referral protocol integration
# """
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime
# from typing import Dict, Any, List, Optional

# try:
#     from utils.config_assess import PatternDefinitions
#     PATTERNS = PatternDefinitions.PATTERNS
#     PATTERN_DESCRIPTIONS = PatternDefinitions.PATTERN_DESCRIPTIONS
# except ImportError:
#     PATTERNS = {i: f"Pattern {i}" for i in range(1, 11)}
#     PATTERN_DESCRIPTIONS = {}


# class ClinicalAssessmentEmailHandler:
#     """Enhanced email handler with comprehensive clinical protocols"""
    
#     def __init__(self):
#         self.smtp_server = "smtp.gmail.com"
#         self.smtp_port = 587
#         self.sender_email = self._get_config("SENDER_EMAIL", "laetitiasheppard@gmail.com")
#         self.recipient_email = self._get_config("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
#         self.password = self._get_email_password()
        
#         # Email configuration validation
#         if not self.password:
#             print("⚠️  WARNING: Email system not configured - notifications disabled")
    
#     def _get_config(self, key: str, default: str) -> str:
#         """Get configuration with proper fallback chain"""
#         # Try Streamlit secrets first
#         try:
#             import streamlit as st
#             if hasattr(st, 'secrets') and 'email' in st.secrets:
#                 value = st.secrets.get("email", {}).get(key, None)
#                 if value and str(value).strip():
#                     return str(value).strip()
#         except Exception as e:
#             print(f"Note: Streamlit secrets unavailable for {key}: {e}")
        
#         # Fallback to environment variable
#         value = os.getenv(key, default)
#         return str(value).strip() if value else default
    
#     def _get_email_password(self) -> str:
#         """Get email password with comprehensive error handling"""
#         # Try Streamlit secrets
#         try:
#             import streamlit as st
#             if hasattr(st, 'secrets') and 'email' in st.secrets:
#                 password = st.secrets.get("email", {}).get("GMAIL_APP_PASSWORD", "")
#                 if password and str(password).strip():
#                     print("✅ Email configured via Streamlit secrets")
#                     return str(password).strip()
#         except Exception as e:
#             print(f"Streamlit secrets check failed: {e}")
        
#         # Try environment variable
#         password = os.getenv("GMAIL_APP_PASSWORD", "")
#         if password and password.strip():
#             print("✅ Email configured via environment variable")
#             return password.strip()
        
#         # No password found
#         print("=" * 70)
#         print("⚠️  EMAIL CONFIGURATION REQUIRED")
#         print("=" * 70)
#         print("No Gmail App Password found. Email notifications are disabled.")
#         print("\nTo enable email notifications:")
#         print("1. Go to: https://myaccount.google.com/apppasswords")
#         print("2. Generate an App Password for 'Mail'")
#         print("3. Add to Streamlit secrets (secrets.toml):")
#         print("   [email]")
#         print("   GMAIL_APP_PASSWORD = \"your-16-char-app-password\"")
#         print("   SENDER_EMAIL = \"your-email@gmail.com\"")
#         print("   RECIPIENT_EMAIL = \"therapist-email@gmail.com\"")
#         print("\nOr set environment variable: GMAIL_APP_PASSWORD")
#         print("=" * 70)
        
#         return ""
    
#     def send_assessment_email(self, email_data: Dict[str, Any]) -> bool:
#         """Send comprehensive assessment email with enhanced protocols"""
        
#         # Validate email configuration
#         if not self.password:
#             print("❌ ERROR: Cannot send email - no password configured")
#             print("Assessment data saved but notification not sent")
#             return False
        
#         if not self.sender_email or not self.recipient_email:
#             print("❌ ERROR: Invalid email configuration")
#             print(f"Sender: {self.sender_email}, Recipient: {self.recipient_email}")
#             return False
        
#         try:
#             # Extract data
#             contact = email_data.get('contact', {})
#             analysis = email_data.get('analysis', {})
#             responses = email_data.get('responses', {})
            
#             # Validate required data
#             if not contact or not analysis:
#                 print("❌ ERROR: Missing required email data (contact or analysis)")
#                 return False
            
#             # Check for crisis indicators
#             crisis_level = self._assess_crisis_level(analysis, responses)
            
#             # Create email
#             msg = MIMEMultipart('alternative')
#             msg['From'] = self.sender_email
#             msg['To'] = self.recipient_email
            
#             # Crisis-aware subject line
#             if crisis_level == 'CRITICAL':
#                 msg['Subject'] = f"🚨 URGENT CRISIS: {contact.get('full_name', 'Unknown Client')} - IMMEDIATE ACTION REQUIRED"
#             elif crisis_level == 'HIGH':
#                 msg['Subject'] = f"⚠️ High Priority Assessment: {contact.get('full_name', 'Unknown Client')}"
#             else:
#                 msg['Subject'] = f"🎯 New Clinical Assessment: {contact.get('full_name', 'Unknown Client')}"
            
#             # Generate comprehensive HTML body
#             html_body = self._create_comprehensive_email_body(
#                 contact, analysis, responses, crisis_level
#             )
#             msg.attach(MIMEText(html_body, 'html'))
            
#             # Send email
#             with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
#                 server.starttls()
#                 server.login(self.sender_email, self.password)
#                 server.send_message(msg)
            
#             print("✅ SUCCESS: Assessment email sent")
#             print(f"   Sent to: {self.recipient_email}")
#             print(f"   Client: {contact.get('full_name', 'Unknown')}")
#             print(f"   Crisis Level: {crisis_level}")
#             return True
            
#         except smtplib.SMTPAuthenticationError:
#             print("❌ ERROR: Email authentication failed")
#             print("Please check your Gmail App Password is correct")
#             return False
#         except smtplib.SMTPException as e:
#             print(f"❌ ERROR: SMTP error: {str(e)}")
#             return False
#         except Exception as e:
#             print(f"❌ ERROR: Failed to send email: {str(e)}")
#             import traceback
#             traceback.print_exc()
#             return False
    
#     def _assess_crisis_level(
#         self, 
#         analysis: Dict[str, Any], 
#         responses: Dict[int, Any]
#     ) -> str:
#         """Assess crisis level from assessment data"""
        
#         # Check for crisis indicators in responses
#         crisis_indicators = []
        
#         # Q6: Dissociation/panic/suicidal thoughts
#         q6_response = responses.get(6, "")
#         if isinstance(q6_response, str):
#             if "currently experiencing" in q6_response.lower():
#                 crisis_indicators.append("Current crisis symptoms reported")
#             elif "frequently" in q6_response.lower():
#                 crisis_indicators.append("Frequent dissociation/panic episodes")
        
#         # Q7: Substance use
#         q7_response = responses.get(7, "")
#         if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
#             crisis_indicators.append("Active substance use")
        
#         # Check pattern severity
#         pattern_hierarchy = analysis.get('pattern_hierarchy', {})
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
#         if dominant.get('score', 0) >= 9.0:
#             crisis_indicators.append(f"Severe {dominant.get('name', 'pattern')} (9+/10)")
        
#         # Check urgency
#         pattern_scores = analysis.get('pattern_scores', {})
#         severe_count = sum(1 for score in pattern_scores.values() if score >= 8.0)
#         if severe_count >= 4:
#             crisis_indicators.append("Multiple severe patterns (4+)")
        
#         # Determine crisis level
#         if len(crisis_indicators) >= 3:
#             return 'CRITICAL'
#         elif len(crisis_indicators) >= 1:
#             return 'HIGH'
#         else:
#             return 'STANDARD'
    
#     def _create_comprehensive_email_body(
#         self,
#         contact: Dict,
#         analysis: Dict,
#         responses: Dict,
#         crisis_level: str
#     ) -> str:
#         """Create comprehensive HTML email with enhanced clinical protocols"""
        
#         # Extract all analysis components
#         pattern_hierarchy = analysis.get('pattern_hierarchy', {})
#         clinical_summary = analysis.get('clinical_summary', {})
#         trigger_chain_analysis = analysis.get('trigger_chain_analysis', {})
#         success_prediction = analysis.get('success_prediction', {})
#         digital_analysis = analysis.get('digital_analysis', {})
#         hidden_barriers = analysis.get('hidden_barriers', {})
#         constellation_analysis = analysis.get('constellation_analysis', {})
        
#         # Extract key data
#         dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})
#         primary_patterns = pattern_hierarchy.get('primary_patterns', [])
#         pattern_count = pattern_hierarchy.get('pattern_count', 0)
#         no_patterns = pattern_count == 0 or not dominant_pattern
        
#         client_name = contact.get('full_name', 'Unknown Client')
#         client_email = contact.get('email', '')
#         urgency = contact.get('urgency', 'Not specified')
        
#         # Build HTML email
#         html = f"""
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <style>
#         body {{
#             font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
#             line-height: 1.6;
#             color: #273548;
#             background: #f8fafc;
#             margin: 0;
#             padding: 0;
#         }}
#         .container {{
#             max-width: 900px;
#             margin: 0 auto;
#             background: white;
#         }}
#         .header {{
#             background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
#             color: white;
#             padding: 2rem;
#             text-align: center;
#         }}
#         .header h1 {{
#             margin: 0;
#             font-size: 2rem;
#             font-weight: 700;
#         }}
#         .header p {{
#             margin: 0.5rem 0 0 0;
#             opacity: 0.95;
#         }}
        
#         /* CRISIS ALERT - HIGHEST PRIORITY */
#         .crisis-alert {{
#             background: #fef2f2;
#             border: 4px solid #ef4444;
#             border-radius: 12px;
#             padding: 2rem;
#             margin: 2rem;
#             animation: pulse 2s infinite;
#         }}
#         @keyframes pulse {{
#             0%, 100% {{ border-color: #ef4444; }}
#             50% {{ border-color: #dc2626; }}
#         }}
#         .crisis-alert h2 {{
#             color: #b91c1c;
#             margin: 0 0 1rem 0;
#             font-size: 1.8rem;
#         }}
#         .crisis-indicators {{
#             background: white;
#             padding: 1rem;
#             border-radius: 8px;
#             margin-top: 1rem;
#         }}
#         .crisis-indicators li {{
#             margin: 0.5rem 0;
#             color: #b91c1c;
#             font-weight: 600;
#         }}
        
#         /* RAPID CLINICAL SUMMARY */
#         .clinical-summary {{
#             background: #fff3cd;
#             border: 3px solid #eab308;
#             border-radius: 12px;
#             padding: 2rem;
#             margin: 2rem;
#         }}
#         .clinical-summary h2 {{
#             color: #b45309;
#             margin: 0 0 1.5rem 0;
#             font-size: 1.5rem;
#             border-bottom: 2px solid #eab308;
#             padding-bottom: 0.5rem;
#         }}
#         .summary-grid {{
#             display: grid;
#             grid-template-columns: 1fr 1fr;
#             gap: 1rem;
#             margin-top: 1.5rem;
#         }}
#         .summary-item {{
#             background: white;
#             padding: 1rem;
#             border-radius: 8px;
#             border-left: 4px solid #4CA1A3;
#         }}
#         .summary-item strong {{
#             display: block;
#             color: #4CA1A3;
#             margin-bottom: 0.5rem;
#             font-size: 0.85rem;
#             text-transform: uppercase;
#             letter-spacing: 0.5px;
#         }}
#         .summary-item span {{
#             color: #273548;
#             font-size: 1rem;
#             display: block;
#             line-height: 1.4;
#         }}
#         .summary-full {{
#             grid-column: 1 / -1;
#         }}
        
#         /* INTERVENTION PROTOCOLS */
#         .intervention-box {{
#             background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#             border-left: 4px solid #00897b;
#         }}
#         .intervention-box h4 {{
#             margin: 0 0 0.5rem 0;
#             color: #00695c;
#         }}
#         .intervention-box ul {{
#             margin: 0.5rem 0;
#             padding-left: 1.5rem;
#         }}
        
#         /* RESISTANCE PREDICTION */
#         .resistance-box {{
#             background: #fef3c7;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#             border-left: 4px solid #f59e0b;
#         }}
#         .resistance-box h4 {{
#             margin: 0 0 0.5rem 0;
#             color: #d97706;
#         }}
        
#         /* OUTCOME TRACKING */
#         .outcome-tracking {{
#             background: #e1f0f0;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#             border-left: 4px solid #4CA1A3;
#         }}
        
#         .section {{
#             padding: 2rem;
#             border-bottom: 1px solid #e2e8f0;
#         }}
#         .section h2 {{
#             color: #273548;
#             margin: 0 0 1rem 0;
#             font-size: 1.5rem;
#         }}
#         .section h3 {{
#             color: #4CA1A3;
#             margin: 1.5rem 0 0.75rem 0;
#             font-size: 1.2rem;
#         }}
#         .info-grid {{
#             display: grid;
#             grid-template-columns: 1fr 1fr;
#             gap: 1rem;
#             margin: 1rem 0;
#         }}
#         .info-item {{
#             background: #f8fafc;
#             padding: 1rem;
#             border-radius: 8px;
#             border-left: 4px solid #cbd5e1;
#         }}
#         .info-item strong {{
#             display: block;
#             color: #556D7A;
#             margin-bottom: 0.25rem;
#             font-size: 0.85rem;
#         }}
#         .pattern-box {{
#             background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
#             color: white;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#         }}
#         .pattern-box h3 {{
#             margin: 0;
#             color: white;
#             font-size: 1.3rem;
#         }}
#         .pattern-box p {{
#             margin: 0.5rem 0 0 0;
#             opacity: 0.95;
#         }}
#         .trigger-chain {{
#             background: #e1f0f0;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#         }}
#         .trigger-step {{
#             background: white;
#             padding: 1rem;
#             margin: 0.5rem 0;
#             border-left: 4px solid #4CA1A3;
#             border-radius: 6px;
#         }}
#         .trigger-step strong {{
#             color: #4CA1A3;
#             display: block;
#             margin-bottom: 0.25rem;
#         }}
#         table {{
#             width: 100%;
#             border-collapse: collapse;
#             margin: 1rem 0;
#         }}
#         th, td {{
#             padding: 0.75rem;
#             text-align: left;
#             border-bottom: 1px solid #e2e8f0;
#         }}
#         th {{
#             background: #f8fafc;
#             font-weight: 600;
#             color: #273548;
#         }}
#         .urgency-alert {{
#             background: #fef2f2;
#             border: 2px solid #ef4444;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#         }}
#         .urgency-alert h3 {{
#             color: #b91c1c;
#             margin: 0 0 0.5rem 0;
#         }}
#         .healthy-baseline {{
#             background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
#             color: white;
#             padding: 2rem;
#             border-radius: 12px;
#             text-align: center;
#             margin: 1rem 0;
#         }}
#         .healthy-baseline h3 {{
#             margin: 0;
#             color: white;
#         }}
#         .referral-box {{
#             background: #fef3c7;
#             border: 2px solid #f59e0b;
#             padding: 1.5rem;
#             border-radius: 12px;
#             margin: 1rem 0;
#         }}
#         .referral-box h3 {{
#             color: #d97706;
#             margin: 0 0 1rem 0;
#         }}
#         @media (max-width: 600px) {{
#             .summary-grid, .info-grid {{
#                 grid-template-columns: 1fr;
#             }}
#             .section {{
#                 padding: 1rem;
#             }}
#         }}
#     </style>
# </head>
# <body>
#     <div class="container">
#         <!-- HEADER -->
#         <div class="header">
#             <h1>Clinical behavioral pattern assessment</h1>
#             <p>Comprehensive 97-question analysis with clinical protocols</p>
#             <p>{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
#         </div>
        
#         {self._generate_crisis_alert(crisis_level, analysis, responses)}
        
#         {self._generate_rapid_clinical_summary(
#             client_name, dominant_pattern, primary_patterns, 
#             clinical_summary, no_patterns, constellation_analysis
#         )}
        
#         {self._generate_intervention_protocols(
#             dominant_pattern, clinical_summary, digital_analysis, hidden_barriers
#         )}
        
#         {self._generate_urgency_alert(urgency)}
        
#         {self._generate_client_information(contact)}
        
#         {self._generate_pattern_analysis(
#             dominant_pattern, pattern_hierarchy, no_patterns
#         )}
        
#         {self._generate_trigger_chain_section(trigger_chain_analysis)}
        
#         {self._generate_resistance_prediction(hidden_barriers, clinical_summary)}
        
#         {self._generate_success_prediction(success_prediction, analysis)}
        
#         {self._generate_digital_analysis(digital_analysis)}
        
#         {self._generate_referral_recommendations(analysis, responses)}
        
#         {self._generate_outcome_tracking_template(client_name, dominant_pattern)}
        
#         {self._generate_response_transcript(responses)}
#     </div>
# </body>
# </html>
#         """
        
#         return html
    
#     def _generate_crisis_alert(
#         self, 
#         crisis_level: str, 
#         analysis: Dict, 
#         responses: Dict
#     ) -> str:
#         """Generate crisis alert if needed"""
        
#         if crisis_level == 'STANDARD':
#             return ""
        
#         # Collect crisis indicators
#         crisis_indicators = []
        
#         # Check Q6: Dissociation/panic/suicidal
#         q6_response = responses.get(6, "")
#         if isinstance(q6_response, str) and ("currently experiencing" in q6_response.lower() or "frequently" in q6_response.lower()):
#             crisis_indicators.append("Active crisis symptoms (dissociation/panic/suicidal ideation)")
        
#         # Check Q7: Substance use
#         q7_response = responses.get(7, "")
#         if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
#             crisis_indicators.append("Active substance use reported")
        
#         # Check pattern severity
#         pattern_hierarchy = analysis.get('pattern_hierarchy', {})
#         dominant = pattern_hierarchy.get('dominant_pattern', {})
#         if dominant.get('score', 0) >= 9.0:
#             crisis_indicators.append(f"Severe {dominant.get('name', 'pattern')} pattern (9+/10)")
        
#         # Check for multiple severe patterns
#         pattern_scores = analysis.get('pattern_scores', {})
#         severe_count = sum(1 for score in pattern_scores.values() if score >= 8.0)
#         if severe_count >= 4:
#             crisis_indicators.append(f"Multiple severe patterns ({severe_count} patterns at 8+/10)")
        
#         indicators_html = "".join([f"<li>{indicator}</li>" for indicator in crisis_indicators])
        
#         if crisis_level == 'CRITICAL':
#             return f"""
#                 <div class="crisis-alert">
#                     <h2>🚨 CRITICAL: IMMEDIATE ACTION REQUIRED</h2>
#                     <p style="font-size: 1.2rem; font-weight: 600; margin: 1rem 0;">
#                         This assessment indicates acute crisis risk requiring immediate clinical response.
#                     </p>
#                     <div class="crisis-indicators">
#                         <strong style="color: #b91c1c; display: block; margin-bottom: 0.5rem;">
#                             Crisis Indicators Detected:
#                         </strong>
#                         <ul>{indicators_html}</ul>
#                     </div>
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="color: #b91c1c; display: block; margin-bottom: 0.5rem;">
#                             IMMEDIATE ACTIONS REQUIRED:
#                         </strong>
#                         <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                             <li><strong>Contact client within 2-4 hours</strong></li>
#                             <li>Assess immediate safety and suicidality</li>
#                             <li>Provide crisis resources if needed</li>
#                             <li>Consider referral for psychiatric evaluation</li>
#                             <li>Document all crisis interventions</li>
#                         </ol>
#                     </div>
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong>Crisis Resources to Provide:</strong>
#                         <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                             <li>National Suicide Prevention Lifeline: 988</li>
#                             <li>Crisis Text Line: Text HOME to 741741</li>
#                             <li>Emergency Services: Local emergency number</li>
#                         </ul>
#                     </div>
#                 </div>
#             """
#         else:  # HIGH
#             return f"""
#                 <div class="crisis-alert" style="border-color: #f59e0b; background: #fef3c7;">
#                     <h3 style="color: #d97706;">⚠️ HIGH PRIORITY: ELEVATED RISK</h3>
#                     <div class="crisis-indicators" style="background: white;">
#                         <strong style="color: #d97706; display: block; margin-bottom: 0.5rem;">
#                             Risk Indicators:
#                         </strong>
#                         <ul style="color: #d97706;">{indicators_html}</ul>
#                     </div>
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="color: #d97706;">Recommended Actions:</strong>
#                         <ol style="margin: 0.5rem 0; padding-left: 1.5rem; color: #92400e;">
#                             <li>Contact client within 24 hours</li>
#                             <li>Assess safety and readiness for intervention</li>
#                             <li>Prepare crisis resources for session 1</li>
#                             <li>Consider consultation before proceeding</li>
#                         </ol>
#                     </div>
#                 </div>
#             """
    
#     def _generate_rapid_clinical_summary(
#         self,
#         client_name: str,
#         dominant_pattern: Dict,
#         primary_patterns: List[Dict],
#         clinical_summary: Dict,
#         no_patterns: bool,
#         constellation_analysis: Dict
#     ) -> str:
#         """Generate rapid clinical summary template section"""
        
#         if no_patterns:
#             return """
#                 <div class="healthy-baseline" style="margin: 2rem;">
#                     <h3>✓ Healthy baseline - no clinical intervention needed</h3>
#                     <p style="margin: 0.5rem 0; opacity: 0.95;">
#                         No significant behavioral patterns detected. Consider performance optimization services.
#                     </p>
#                 </div>
#             """
        
#         # Extract data with proper fallbacks
#         dominant_name = dominant_pattern.get('name', 'Unknown').title()
#         dominant_score = dominant_pattern.get('score', 0)
        
#         primary_1_name = "None"
#         primary_1_score = 0
#         primary_2_name = "None"
#         primary_2_score = 0
        
#         if len(primary_patterns) > 0:
#             primary_1_name = primary_patterns[0].get('name', 'Unknown').title()
#             primary_1_score = primary_patterns[0].get('score', 0)
        
#         if len(primary_patterns) > 1:
#             primary_2_name = primary_patterns[1].get('name', 'Unknown').title()
#             primary_2_score = primary_patterns[1].get('score', 0)
        
#         # Clinical summary data
#         core_belief = clinical_summary.get('core_limiting_belief', 'Not identified')
#         hidden_benefits = clinical_summary.get('hidden_benefits', 'Not identified')
#         systemic_resistance = clinical_summary.get('systemic_resistance', 'Not identified')
#         identity_threat = clinical_summary.get('identity_threat', 'Not identified')
#         session_1_focus = clinical_summary.get('session_1_focus', 'Pattern exploration')
#         session_2_target = clinical_summary.get('session_2_target', 'Core transformation')
#         session_3_need = clinical_summary.get('potential_session_3_need', 'Unknown')
#         readiness = clinical_summary.get('change_readiness_score', '0/10')
#         intervention_keywords = clinical_summary.get('intervention_keywords', 'Not specified')
#         avoid_language = clinical_summary.get('avoid_language', 'Not specified')
        
#         # Constellation data
#         constellation_multiplier = constellation_analysis.get('constellation_multiplier', 1.0)
#         constellation_complexity = constellation_analysis.get('constellation_complexity', 'Unknown')
        
#         resistance_points = clinical_summary.get('predicted_resistance_points', [])
#         if not resistance_points:
#             resistance_points = ["Standard resistance patterns expected"]
#         resistance_html = "".join([f"<li>{point}</li>" for point in resistance_points])
        
#         return f"""
#             <div class="clinical-summary">
#                 <h2>⚡ RAPID CLINICAL SUMMARY TEMPLATE</h2>
                
#                 <div class="summary-grid">
#                     <div class="summary-item">
#                         <strong>Client</strong>
#                         <span>{client_name}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Date</strong>
#                         <span>{datetime.now().strftime('%Y-%m-%d')}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Dominant Pattern</strong>
#                         <span>{dominant_name}<br>(Score: {dominant_score:.1f}/10)</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Primary Pattern</strong>
#                         <span>{primary_1_name}<br>(Score: {primary_1_score:.1f}/10)</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Secondary Pattern</strong>
#                         <span>{primary_2_name}<br>(Score: {primary_2_score:.1f}/10)</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Change Readiness</strong>
#                         <span>{readiness}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Pattern Constellation</strong>
#                         <span>{constellation_complexity}<br>Amplification: {constellation_multiplier}x</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Session 3 Probability</strong>
#                         <span>{session_3_need}</span>
#                     </div>
                    
#                     <div class="summary-item summary-full">
#                         <strong>Core Limiting Belief</strong>
#                         <span>{core_belief}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Hidden Benefits (Secondary Gain)</strong>
#                         <span>{hidden_benefits}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Identity Threat</strong>
#                         <span>{identity_threat}</span>
#                     </div>
                    
#                     <div class="summary-item summary-full">
#                         <strong>Systemic Resistance Sources</strong>
#                         <span>{systemic_resistance}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Session 1 Focus</strong>
#                         <span>{session_1_focus}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>Session 2 Target</strong>
#                         <span>{session_2_target}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>✓ Intervention Keywords</strong>
#                         <span style="color: #22c55e;">{intervention_keywords}</span>
#                     </div>
                    
#                     <div class="summary-item">
#                         <strong>✗ Avoid Language</strong>
#                         <span style="color: #ef4444;">{avoid_language}</span>
#                     </div>
#                 </div>
                
#                 <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                     <strong style="color: #b45309; display: block; margin-bottom: 0.5rem;">
#                         🎯 Predicted Resistance Points:
#                     </strong>
#                     <ol style="margin: 0.5rem 0; padding-left: 1.5rem; color: #92400e;">{resistance_html}</ol>
#                 </div>
#             </div>
#         """
    
#     def _generate_intervention_protocols(
#         self,
#         dominant_pattern: Dict,
#         clinical_summary: Dict,
#         digital_analysis: Dict,
#         hidden_barriers: Dict
#     ) -> str:
#         """Generate specific intervention protocols section"""
        
#         if not dominant_pattern:
#             return ""
        
#         pattern_name = dominant_pattern.get('name', 'Unknown').title()
#         pattern_desc = dominant_pattern.get('description', {})
        
#         # Session 1 protocols
#         session_1_protocols = [
#             clinical_summary.get('session_1_focus', 'Pattern mapping'),
#             "Establish therapeutic alliance with collaborative language",
#             "Complete behavioral chain analysis",
#             "Initial positive programming via light hypnosis"
#         ]
        
#         # Session 2 protocols
#         session_2_protocols = [
#             clinical_summary.get('session_2_target', 'Core transformation'),
#             f"Deep hypnotic pattern interruption of {pattern_name}",
#             "Neural pathway installation for new responses",
#             "Future pacing and integration work"
#         ]
        
#         # Digital adaptations if needed
#         digital_adaptations = []
#         if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
#             digital_adaptations = [
#                 "Shorten session segments to 15-30 minutes",
#                 "Use collaborative non-authoritative language",
#                 "Address ironic detachment before emotional work",
#                 "Honor digital competencies as strengths"
#             ]
        
#         # Resistance management
#         resistance_type = hidden_barriers.get('resistance_type', 'Standard resistance')
#         resistance_management = self._get_resistance_management_protocol(resistance_type)
        
#         session_1_html = "".join([f"<li>{protocol}</li>" for protocol in session_1_protocols])
#         session_2_html = "".join([f"<li>{protocol}</li>" for protocol in session_2_protocols])
#         digital_html = "".join([f"<li>{adaptation}</li>" for adaptation in digital_adaptations]) if digital_adaptations else "<li>Standard protocols appropriate</li>"
#         resistance_html = "".join([f"<li>{strategy}</li>" for strategy in resistance_management])
        
#         return f"""
#             <div class="section">
#                 <h2>🎯 Intervention protocols & clinical strategies</h2>
                
#                 <div class="intervention-box">
#                     <h4>Session 1 Protocol (90 minutes)</h4>
#                     <ul>{session_1_html}</ul>
#                 </div>
                
#                 <div class="intervention-box">
#                     <h4>Session 2 Protocol (90 minutes)</h4>
#                     <ul>{session_2_html}</ul>
#                 </div>
                
#                 <div class="intervention-box" style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-left-color: #f59e0b;">
#                     <h4 style="color: #d97706;">Digital-Native Adaptations</h4>
#                     <ul>{digital_html}</ul>
#                 </div>
                
#                 <div class="resistance-box">
#                     <h4>Resistance Management Strategy</h4>
#                     <p><strong>Predicted resistance type:</strong> {resistance_type}</p>
#                     <ul>{resistance_html}</ul>
#                 </div>
#             </div>
#         """
    
#     def _get_resistance_management_protocol(self, resistance_type: str) -> List[str]:
#         """Get specific resistance management strategies"""
        
#         protocols = {
#             'Identity-based': [
#                 "Frame change as evolution, not abandonment of self",
#                 "Honor protective function before updating it",
#                 "Use 'both/and' language for identity integration"
#             ],
#             'Systemic': [
#                 "Prepare for relationship pushback",
#                 "Install boundary maintenance protocols",
#                 "Create scripts for communicating changes"
#             ],
#             'Emotional': [
#                 "Titrate emotional exposure gradually",
#                 "Use resource anchoring before affect work",
#                 "Install emotional regulation tools first"
#             ],
#             'Existential': [
#                 "Build evidence incrementally, avoid hope talk",
#                 "Focus on curiosity rather than optimism",
#                 "Use 'what if it were possible' reframing"
#             ],
#             'Minimal': [
#                 "Standard therapeutic alliance building",
#                 "Direct subconscious access via theta state",
#                 "Collaborative goal-setting"
#             ]
#         }
        
#         # Find matching protocol
#         for key, protocol in protocols.items():
#             if key in resistance_type:
#                 return protocol
        
#         return protocols['Minimal']
    
#     def _generate_urgency_alert(self, urgency: str) -> str:
#         """Generate urgency alert if needed"""
        
#         if not urgency or urgency == 'Not specified':
#             return ""
        
#         urgency_lower = urgency.lower()
        
#         if 'extremely urgent' in urgency_lower or 'same day' in urgency_lower:
#             return """
#                 <div class="urgency-alert" style="margin: 2rem;">
#                     <h3>🚨 CLIENT URGENCY: EXTREMELY URGENT</h3>
#                     <p><strong>Action Required:</strong> Contact client within 24 hours</p>
#                     <p>Client has indicated extreme urgency - prioritize scheduling immediately</p>
#                 </div>
#             """
#         elif 'very urgent' in urgency_lower or '24 hours' in urgency_lower or 'within the next week' in urgency_lower:
#             return """
#                 <div class="urgency-alert" style="border-color: #eab308; background: #fef3c7;">
#                     <h3 style="color: #b45309;">⚠️ HIGH PRIORITY: VERY URGENT</h3>
#                     <p><strong>Action Required:</strong> Contact client within 24-48 hours</p>
#                 </div>
#             """
#         elif 'moderately urgent' in urgency_lower or 'within the next month' in urgency_lower:
#             return """
#                 <div style="background: #e1f0f0; border: 2px solid #4CA1A3; padding: 1rem; border-radius: 8px; margin: 2rem;">
#                     <h3 style="color: #00695c; margin: 0 0 0.5rem 0;">⏰ Moderate Priority</h3>
#                     <p style="margin: 0;">Contact client within 3-5 days</p>
#                 </div>
#             """
        
#         return ""
    
#     def _generate_client_information(self, contact: Dict) -> str:
#         """Generate client information section"""
        
#         additional_info = contact.get('additional_info', '')
#         additional_html = ""
#         if additional_info and additional_info not in ['None provided', '']:
#             additional_html = f"""
#                 <div class="info-item" style="grid-column: 1 / -1; margin-top: 0.5rem;">
#                     <strong>Additional Information:</strong>
#                     <span>{additional_info}</span>
#                 </div>
#             """
        
#         return f"""
#             <div class="section">
#                 <h2>Client information</h2>
#                 <div class="info-grid">
#                     <div class="info-item">
#                         <strong>Name:</strong>
#                         <span>{contact.get('full_name', 'Unknown')}</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Email:</strong>
#                         <span>{contact.get('email', 'Not provided')}</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Phone:</strong>
#                         <span>{contact.get('phone', 'Not provided')}</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Urgency:</strong>
#                         <span>{contact.get('urgency', 'Not specified')}</span>
#                     </div>
#                 </div>
#                 <div class="info-item" style="margin-top: 1rem;">
#                     <strong>Primary Concern:</strong>
#                     <span>{contact.get('primary_concern', 'Not provided')}</span>
#                 </div>
#                 {additional_html}
#             </div>
#         """
    
#     def _generate_pattern_analysis(
#         self,
#         dominant_pattern: Dict,
#         pattern_hierarchy: Dict,
#         no_patterns: bool
#     ) -> str:
#         """Generate pattern analysis section"""
        
#         if no_patterns:
#             return ""
        
#         pattern_name = dominant_pattern.get('name', 'Unknown').title()
#         pattern_score = dominant_pattern.get('score', 0)
#         pattern_severity = dominant_pattern.get('severity', 'Unknown')
#         pattern_desc = dominant_pattern.get('description', {})
        
#         root_structure = pattern_desc.get('root_structure', 'Not available')
#         systemic_factors = pattern_desc.get('systemic_factors', [])
#         identity_conflict = pattern_desc.get('identity_conflict', 'Not available')
#         hidden_loyalties = pattern_desc.get('hidden_loyalties', [])
#         protective_function = pattern_desc.get('protective_function', 'Not identified')
#         intervention_focus = pattern_desc.get('intervention_focus', 'Not identified')
        
#         systemic_html = "".join([f"<li>{factor}</li>" for factor in systemic_factors]) if systemic_factors else "<li>None identified</li>"
#         loyalties_html = "".join([f"<li>{loyalty}</li>" for loyalty in hidden_loyalties]) if hidden_loyalties else "<li>None identified</li>"
        
#         all_scores = pattern_hierarchy.get('all_scores', {})
#         pattern_table = self._generate_pattern_table(all_scores)
        
#         return f"""
#             <div class="section">
#                 <h2>Behavioral pattern analysis</h2>
                
#                 <div class="pattern-box">
#                     <h3>Dominant pattern: {pattern_name}</h3>
#                     <p style="font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0;">
#                         {pattern_score:.1f}/10 ({pattern_severity})
#                     </p>
#                 </div>
                
#                 <h3>Pattern structure & function</h3>
#                 <div class="info-item">
#                     <strong>Root structural belief:</strong>
#                     <span>{root_structure}</span>
#                 </div>
                
#                 <div class="info-item" style="margin-top: 0.5rem;">
#                     <strong>Protective function:</strong>
#                     <span>{protective_function}</span>
#                 </div>
                
#                 <div class="info-item" style="margin-top: 0.5rem;">
#                     <strong>Intervention focus:</strong>
#                     <span>{intervention_focus}</span>
#                 </div>
                
#                 <h3>Systemic factors maintaining pattern</h3>
#                 <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                     {systemic_html}
#                 </ul>
                
#                 <h3>Identity conflict</h3>
#                 <div class="info-item">
#                     <span>{identity_conflict}</span>
#                 </div>
                
#                 <h3>Hidden loyalties creating resistance</h3>
#                 <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                     {loyalties_html}
#                 </ul>
                
#                 <h3>Complete pattern constellation</h3>
#                 {pattern_table}
#             </div>
#         """
    
#     def _generate_pattern_table(self, all_scores: Dict[int, float]) -> str:
#         """Generate pattern scores table"""
        
#         significant = {pid: score for pid, score in all_scores.items() if score >= 4.0}
        
#         if not significant:
#             return '<p style="color: #22c55e; font-weight: 600;">✓ No clinically significant patterns detected</p>'
        
#         rows = []
#         for pid, score in sorted(significant.items(), key=lambda x: x[1], reverse=True):
#             pattern_name = PATTERNS.get(pid, f"Pattern {pid}").title()
#             severity = self._get_severity(score)
            
#             # Color code severity
#             severity_color = "#ef4444" if "Severe" in severity else "#eab308" if "Moderate" in severity else "#4CA1A3"
            
#             rows.append(f"""
#                 <tr>
#                     <td>{pattern_name}</td>
#                     <td><strong>{score:.1f}/10</strong></td>
#                     <td style="color: {severity_color}; font-weight: 600;">{severity}</td>
#                 </tr>
#             """)
        
#         return f"""
#             <table>
#                 <tr>
#                     <th>Pattern</th>
#                     <th>Score</th>
#                     <th>Severity</th>
#                 </tr>
#                 {"".join(rows)}
#             </table>
#         """
    
#     def _get_severity(self, score: float) -> str:
#         """Get severity classification"""
#         if score >= 8.0: return "Severe"
#         elif score >= 6.0: return "Moderate-High"
#         elif score >= 4.0: return "Moderate"
#         else: return "Mild"
    
#     def _generate_trigger_chain_section(self, trigger_chain_analysis: Dict) -> str:
#         """Generate trigger chain sequence section"""
        
#         chain = trigger_chain_analysis.get('trigger_sequence', {})
#         intervention_windows = trigger_chain_analysis.get('intervention_windows', [])
#         completeness = trigger_chain_analysis.get('sequence_completeness', 0)
        
#         intervention_html = ""
#         if intervention_windows:
#             for window in intervention_windows:
#                 point = window.get('point', 'Unknown')
#                 description = window.get('description', '')
#                 technique = window.get('technique', '')
#                 intervention_html += f"""
#                     <li><strong>{point}:</strong> {description}<br>
#                     <em style="color: #556D7A;">Technique: {technique}</em></li>
#                 """
#         else:
#             intervention_html = "<li>Complete sequence mapping in session 1</li>"
        
#         return f"""
#             <div class="section">
#                 <h2>Complete trigger sequence mapping</h2>
#                 <p><strong>Sequence completeness:</strong> {completeness:.0f}%</p>
                
#                 <div class="trigger-chain">
#                     <div class="trigger-step">
#                         <strong>1. Environmental trigger:</strong>
#                         <span>{chain.get('environmental_trigger', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>2. First awareness point:</strong>
#                         <span>{chain.get('awareness_entry_point', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>3. Physical response:</strong>
#                         <span>{chain.get('physical_response', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>4. Automatic thought:</strong>
#                         <span>{chain.get('automatic_thought', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>5. Emotional response:</strong>
#                         <span>{chain.get('emotional_response', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>6. Behavioral response:</strong>
#                         <span>{chain.get('behavioral_response', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>7. Immediate consequence:</strong>
#                         <span>{chain.get('immediate_consequence', 'Not captured')}</span>
#                     </div>
                    
#                     <div class="trigger-step">
#                         <strong>8. Extended impact:</strong>
#                         <span>{chain.get('extended_impact', 'Not captured')}</span>
#                     </div>
#                 </div>
                
#                 <h3>Intervention windows identified</h3>
#                 <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                     {intervention_html}
#                 </ul>
#             </div>
#         """
    
#     def _generate_resistance_prediction(
#         self,
#         hidden_barriers: Dict,
#         clinical_summary: Dict
#     ) -> str:
#         """Generate resistance prediction section"""
        
#         resistance_type = hidden_barriers.get('resistance_type', 'Standard resistance')
#         resistance_intensity = hidden_barriers.get('resistance_intensity', 'Unknown')
#         secondary_gain = hidden_barriers.get('secondary_gain', 'Not identified')
#         systemic_stakeholders = hidden_barriers.get('systemic_stakeholders', ['Not identified'])
#         protective_functions = hidden_barriers.get('protective_functions', ['Not identified'])
        
#         resistance_points = clinical_summary.get('predicted_resistance_points', [])
#         if not resistance_points:
#             resistance_points = ["Standard therapeutic resistance expected"]
        
#         stakeholders_html = "".join([f"<li>{stakeholder}</li>" for stakeholder in systemic_stakeholders])
#         functions_html = "".join([f"<li>{function}</li>" for function in protective_functions])
#         points_html = "".join([f"<li>{point}</li>" for point in resistance_points])
        
#         # Color code intensity
#         intensity_color = "#ef4444" if "High" in resistance_intensity else "#eab308" if "Moderate" in resistance_intensity else "#22c55e"
        
#         return f"""
#             <div class="section">
#                 <h2>Resistance prediction & management</h2>
                
#                 <div class="resistance-box">
#                     <h4>Resistance Profile</h4>
#                     <div class="info-grid" style="margin-top: 1rem;">
#                         <div class="info-item" style="border-left-color: {intensity_color};">
#                             <strong>Resistance Intensity:</strong>
#                             <span style="color: {intensity_color}; font-weight: 600;">{resistance_intensity}</span>
#                         </div>
#                         <div class="info-item">
#                             <strong>Resistance Type:</strong>
#                             <span>{resistance_type}</span>
#                         </div>
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="display: block; margin-bottom: 0.5rem;">Secondary Gain (What pattern protects):</strong>
#                         <span>{secondary_gain}</span>
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="display: block; margin-bottom: 0.5rem;">Protective Functions:</strong>
#                         <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">{functions_html}</ul>
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="display: block; margin-bottom: 0.5rem;">Systemic Stakeholders (Who benefits from pattern staying):</strong>
#                         <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">{stakeholders_html}</ul>
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong style="display: block; margin-bottom: 0.5rem;">Specific Resistance Points to Anticipate:</strong>
#                         <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">{points_html}</ol>
#                     </div>
#                 </div>
#             </div>
#         """
    
#     def _generate_success_prediction(self, success_prediction: Dict, analysis: Dict) -> str:
#         """Generate success prediction section"""
        
#         success_rate = success_prediction.get('overall_success_rate', 85)
#         success_tier = success_prediction.get('success_tier', 'High')
#         recommended_sessions = success_prediction.get('recommended_sessions', 2)
#         timeline = success_prediction.get('timeline_estimate', '2 weeks')
        
#         # Get session prediction details
#         session_prediction = analysis.get('session_prediction', {})
#         complexity_score = session_prediction.get('complexity_score', 0)
#         session_3_probability = session_prediction.get('session_3_probability', 'Low')
        
#         # Color code success rate
#         success_color = "#22c55e" if success_rate >= 85 else "#4CA1A3" if success_rate >= 80 else "#eab308"
        
#         return f"""
#             <div class="section">
#                 <h2>Success prediction & timeline</h2>
                
#                 <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, {success_color} 0%, #4CA1A3 100%); 
#                             color: white; border-radius: 12px; margin: 1rem 0;">
#                     <div style="font-size: 3rem; font-weight: bold;">{success_rate}%</div>
#                     <p style="margin: 0.5rem 0; opacity: 0.95; font-size: 1.2rem;">
#                         Predicted success rate ({success_tier})
#                     </p>
#                 </div>
                
#                 <div class="info-grid">
#                     <div class="info-item">
#                         <strong>Recommended Sessions:</strong>
#                         <span>{recommended_sessions} sessions</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Timeline Estimate:</strong>
#                         <span>{timeline}</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Complexity Score:</strong>
#                         <span>{complexity_score:.1f}/15</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Session 3 Probability:</strong>
#                         <span>{session_3_probability}</span>
#                     </div>
#                 </div>
                
#                 <div style="background: #e1f0f0; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                     <strong style="display: block; margin-bottom: 0.5rem;">Expected Timeline:</strong>
#                     <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                         <li><strong>Week 1:</strong> Session 1 - Pattern mapping & initial programming</li>
#                         <li><strong>Week 2:</strong> Session 2 - Core transformation & neural rewiring</li>
#                         <li><strong>Week 3-4:</strong> Integration period (subconscious consolidation)</li>
#                         {f'<li><strong>Session 3 (if needed):</strong> Reinforcement & stabilization</li>' if session_3_probability != 'Low' else ''}
#                     </ul>
#                 </div>
#             </div>
#         """
    
#     def _generate_digital_analysis(self, digital_analysis: Dict) -> str:
#         """Generate digital analysis section if applicable"""
        
#         if not digital_analysis or not digital_analysis.get('is_digital_native'):
#             return ""
        
#         severity = digital_analysis.get('severity_level', 'MINIMAL')
#         score = digital_analysis.get('digital_despair_score', 0)
        
#         if severity == 'MINIMAL':
#             return ""
        
#         primary_driver = digital_analysis.get('primary_digital_driver', 'Unknown').replace('_', ' ').title()
#         screen_time = digital_analysis.get('screen_time_hours', 0)
#         social_media_pct = digital_analysis.get('social_media_percentage', 0)
        
#         # Get digital interplay if available
#         digital_interplay = digital_analysis.get('digital_interplay', {})
#         amplification_effects = digital_interplay.get('amplification_effects', {})
#         intervention_priorities = digital_interplay.get('intervention_priority', [])
        
#         amplification_html = ""
#         if amplification_effects:
#             for effect_name, effect_data in amplification_effects.items():
#                 amplification_html += f"""
#                     <li><strong>{effect_name.replace('_', ' ').title()}:</strong> 
#                     {effect_data.get('description', 'No description')}<br>
#                     <em style="color: #556D7A;">Intervention: {effect_data.get('intervention', 'Standard protocol')}</em></li>
#                 """
        
#         priorities_html = "".join([f"<li>{priority}</li>" for priority in intervention_priorities[:5]])
#         if not priorities_html:
#             priorities_html = "<li>Standard digital-aware protocols</li>"
        
#         # Severity-specific recommendations
#         severity_recommendations = {
#             'SEVERE': [
#                 "Use 15-30 minute session segments (not 50 minutes)",
#                 "Employ anti-authority collaborative language throughout",
#                 "Address ironic detachment before authentic emotional work",
#                 "Build digital bridge: honor online competencies as real skills",
#                 "Install gradual digital detox (not cold turkey elimination)",
#                 "Dopamine regulation protocols before joy permission work"
#             ],
#             'MODERATE': [
#                 "Use 45-60 minute sessions with movement breaks",
#                 "Reduce directive language, increase collaboration",
#                 "Validate digital achievements alongside offline goals",
#                 "Address comparison anxiety and FOMO explicitly",
#                 "Implement mindful digital use (not elimination)"
#             ],
#             'MILD': [
#                 "Standard protocol with digital awareness",
#                 "Address digital factors as contextual influences",
#                 "Integrate digital competencies as strengths"
#             ]
#         }
        
#         recommendations = severity_recommendations.get(severity, severity_recommendations['MILD'])
#         recommendations_html = "".join([f"<li>{rec}</li>" for rec in recommendations])
        
#         return f"""
#             <div class="section">
#                 <h2>📱 Digital conditioning analysis & specialized protocols</h2>
                
#                 <div class="info-item" style="background: #fef3c7; border-left-color: #eab308;">
#                     <strong>Digital Despair Score:</strong>
#                     <span style="font-size: 1.2rem; font-weight: 600;">{score:.1f}% ({severity})</span>
#                 </div>
                
#                 <div class="info-grid" style="margin-top: 1rem;">
#                     <div class="info-item">
#                         <strong>Primary Digital Driver:</strong>
#                         <span>{primary_driver}</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Screen Time:</strong>
#                         <span>{screen_time:.1f} hours/day</span>
#                     </div>
#                     <div class="info-item">
#                         <strong>Social Media Usage:</strong>
#                         <span>{social_media_pct:.0f}% of digital time</span>
#                     </div>
#                 </div>
                
#                 <h3>Specialized adaptations required ({severity})</h3>
#                 <ul style="margin: 0.5rem 0; padding-left: 1.5rem; background: #fef3c7; padding: 1rem; border-radius: 8px;">
#                     {recommendations_html}
#                 </ul>
                
#                 {f'''
#                 <h3>Digital-Pattern amplification effects</h3>
#                 <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                     {amplification_html}
#                 </ul>
#                 ''' if amplification_html else ''}
                
#                 <h3>Digital intervention priorities</h3>
#                 <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                     {priorities_html}
#                 </ol>
                
#                 <div style="background: #e1f0f0; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                     <strong style="display: block; margin-bottom: 0.5rem;">⚡ Why specialized protocol works:</strong>
#                     <p style="margin: 0.5rem 0;">Digital-native brains have different neuroplasticity patterns due to algorithmic conditioning. 
#                     Standard 50-minute sessions don't match their attention architecture. Our adapted protocols respect their neurology 
#                     while facilitating transformation.</p>
#                 </div>
#             </div>
#         """
    
#     def _generate_referral_recommendations(self, analysis: Dict, responses: Dict) -> str:
#         """Generate referral recommendations when appropriate"""
        
#         referrals_needed = []
        
#         # Check crisis indicators
#         q6_response = responses.get(6, "")
#         if isinstance(q6_response, str) and ("currently experiencing" in q6_response.lower() or "frequently" in q6_response.lower()):
#             referrals_needed.append({
#                 'type': 'Psychiatric Evaluation',
#                 'reason': 'Active crisis symptoms (dissociation/panic/suicidal ideation)',
#                 'urgency': 'URGENT',
#                 'action': 'Refer before beginning hypnotherapy sessions'
#             })
        
#         # Check substance use
#         q7_response = responses.get(7, "")
#         if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
#             referrals_needed.append({
#                 'type': 'Substance Abuse Assessment',
#                 'reason': 'Active substance use reported',
#                 'urgency': 'HIGH',
#                 'action': 'Concurrent treatment recommended'
#             })
        
#         # Check medical care
#         q5_response = responses.get(5, "")
#         if isinstance(q5_response, str):
#             if "mental health" in q5_response.lower() or "psychiatric" in q5_response.lower():
#                 referrals_needed.append({
#                     'type': 'Psychiatrist Coordination',
#                     'reason': 'Currently under psychiatric care',
#                     'urgency': 'STANDARD',
#                     'action': 'Coordinate with existing provider before proceeding'
#                 })
        
#         # Check pattern severity
#         pattern_scores = analysis.get('pattern_scores', {})
#         severe_count = sum(1 for score in pattern_scores.values() if score >= 9.0)
#         if severe_count >= 2:
#             referrals_needed.append({
#                 'type': 'Psychiatric Consultation',
#                 'reason': 'Multiple severe patterns (9+/10) may indicate underlying condition',
#                 'urgency': 'MODERATE',
#                 'action': 'Consider consultation to rule out comorbid conditions'
#             })
        
#         if not referrals_needed:
#             return ""
        
#         referrals_html = ""
#         for referral in referrals_needed:
#             urgency_color = "#ef4444" if referral['urgency'] == 'URGENT' else "#eab308" if referral['urgency'] == 'HIGH' else "#4CA1A3"
#             referrals_html += f"""
#                 <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 4px solid {urgency_color};">
#                     <strong style="color: {urgency_color};">{referral['type']} ({referral['urgency']})</strong><br>
#                     <strong>Reason:</strong> {referral['reason']}<br>
#                     <strong>Action:</strong> {referral['action']}
#                 </div>
#             """
        
#         return f"""
#             <div class="section">
#                 <div class="referral-box">
#                     <h3>🏥 Referral recommendations</h3>
#                     <p><strong>The following referrals are recommended before or concurrent with hypnotherapy:</strong></p>
#                     {referrals_html}
#                 </div>
#             </div>
#         """
    
#     def _generate_outcome_tracking_template(
#         self,
#         client_name: str,
#         dominant_pattern: Dict
#     ) -> str:
#         """Generate outcome tracking template for evidence-based practice"""
        
#         if not dominant_pattern:
#             return ""
        
#         pattern_name = dominant_pattern.get('name', 'Unknown').title()
#         pattern_score = dominant_pattern.get('score', 0)
        
#         return f"""
#             <div class="section">
#                 <div class="outcome-tracking">
#                     <h3>📊 Outcome tracking template</h3>
#                     <p>For evidence-based practice and quality improvement, track the following:</p>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong>Client:</strong> {client_name}<br>
#                         <strong>Primary Pattern:</strong> {pattern_name} (Baseline: {pattern_score:.1f}/10)<br>
#                         <strong>Assessment Date:</strong> {datetime.now().strftime('%Y-%m-%d')}
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong>Recommended Tracking Schedule:</strong>
#                         <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                             <li><strong>Post-Session 1:</strong> Initial pattern shift assessment</li>
#                             <li><strong>Post-Session 2:</strong> Core transformation measurement</li>
#                             <li><strong>1-month follow-up:</strong> Pattern stability check</li>
#                             <li><strong>6-month follow-up:</strong> Long-term maintenance assessment</li>
#                         </ul>
#                     </div>
                    
#                     <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#                         <strong>Key Metrics to Track:</strong>
#                         <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
#                             <li>{pattern_name} pattern intensity (0-10 scale)</li>
#                             <li>Trigger charge reduction (percentage)</li>
#                             <li>Functional impact (life areas improved)</li>
#                             <li>Client satisfaction (0-10 scale)</li>
#                             <li>Session count used (2 vs 3)</li>
#                         </ol>
#                     </div>
#                 </div>
#             </div>
#         """
    
#     def _generate_response_transcript(self, responses: Dict[int, Any]) -> str:
#         """Generate complete response transcript"""
        
#         try:
#             from utils.config_assess import COMPLETE_QUESTION_SET
#         except ImportError:
#             return "<div class='section'><p>Response transcript unavailable</p></div>"
        
#         items = []
#         for q_id in sorted(responses.keys()):
#             # Find question text
#             q_text = "Question not found"
#             for q in COMPLETE_QUESTION_SET:
#                 if q['id'] == q_id:
#                     q_text = q['text']
#                     break
            
#             # Format response
#             response = responses[q_id]
#             if isinstance(response, (list, tuple)):
#                 response_text = ", ".join(str(r) for r in response)
#             else:
#                 response_text = str(response)
            
#             # Truncate very long responses for email
#             if len(response_text) > 500:
#                 response_text = response_text[:500] + "... [truncated]"
            
#             items.append(f"""
#                 <div style="background: #f8fafc; padding: 1rem; margin: 0.5rem 0; border-left: 4px solid #cbd5e1; border-radius: 6px;">
#                     <strong style="color: #4CA1A3;">Q{q_id}:</strong> {q_text}<br>
#                     <strong>Response:</strong> {response_text}
#                 </div>
#             """)
        
#         return f"""
#             <div class="section">
#                 <h2>Complete response transcript</h2>
#                 <p><strong>Total questions answered:</strong> {len(responses)}/97</p>
#                 {"".join(items)}
#             </div>
#         """


# # ============================================================================
# # GLOBAL INSTANCE & PUBLIC FUNCTION
# # ============================================================================

# _email_handler = ClinicalAssessmentEmailHandler()

# def send_assessment_email(email_data: Dict[str, Any]) -> bool:
#     """
#     Send clinical assessment email with comprehensive protocols
    
#     Args:
#         email_data: Dictionary containing:
#             - contact: Client contact information
#             - analysis: Complete analytics results
#             - responses: Raw assessment responses
    
#     Returns:
#         bool: True if email sent successfully, False otherwise
#     """
#     return _email_handler.send_assessment_email(email_data)


# # ============================================================================
# # CONFIGURATION VALIDATION
# # ============================================================================

# def validate_email_configuration() -> Dict[str, Any]:
#     """
#     Validate email configuration and return status
    
#     Returns:
#         Dictionary with configuration status
#     """
#     handler = ClinicalAssessmentEmailHandler()
    
#     return {
#         'configured': bool(handler.password),
#         'sender_email': handler.sender_email,
#         'recipient_email': handler.recipient_email,
#         'smtp_server': handler.smtp_server,
#         'smtp_port': handler.smtp_port
#     }









"""
Enhanced Clinical Assessment Email Handler v2.0
- Comprehensive crisis screening alerts
- Enhanced password management with clear error handling
- Improved clinical summary template with intervention protocols
- Outcome tracking preparation
- Better HTML formatting and structure
- Referral protocol integration
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Dict, Any, List, Optional

try:
    from utils.config_assess import PatternDefinitions
    PATTERNS = PatternDefinitions.PATTERNS
    PATTERN_DESCRIPTIONS = PatternDefinitions.PATTERN_DESCRIPTIONS
except ImportError:
    PATTERNS = {i: f"Pattern {i}" for i in range(1, 11)}
    PATTERN_DESCRIPTIONS = {}


class ClinicalAssessmentEmailHandler:
    """Enhanced email handler with comprehensive clinical protocols"""
    
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = self._get_config("SENDER_EMAIL", "laetitiasheppard@gmail.com")
        self.recipient_email = self._get_config("RECIPIENT_EMAIL", "laetitiasheppard@gmail.com")
        self.password = self._get_email_password()
        
        # Email configuration validation
        if not self.password:
            print("⚠️  WARNING: Email system not configured - notifications disabled")
    
    def _get_config(self, key: str, default: str) -> str:
        """Get configuration with proper fallback chain"""
        # Try Streamlit secrets first
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'email' in st.secrets:
                value = st.secrets.get("email", {}).get(key, None)
                if value and str(value).strip():
                    return str(value).strip()
        except Exception as e:
            print(f"Note: Streamlit secrets unavailable for {key}: {e}")
        
        # Fallback to environment variable
        value = os.getenv(key, default)
        return str(value).strip() if value else default
    
    def _get_email_password(self) -> str:
        """Get email password with comprehensive error handling"""
        # Try Streamlit secrets
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'email' in st.secrets:
                password = st.secrets.get("email", {}).get("GMAIL_APP_PASSWORD", "")
                if password and str(password).strip():
                    # Production-safe: No details about configuration source
                    return str(password).strip()
        except Exception as e:
            print(f"Streamlit secrets check failed: {e}")
        
        # Try environment variable
        password = os.getenv("GMAIL_APP_PASSWORD", "")
        if password and password.strip():
            # Production-safe: No details about configuration source
            return password.strip()
        
        # No password found
        print("=" * 70)
        print("⚠️  EMAIL CONFIGURATION REQUIRED")
        print("=" * 70)
        print("No Gmail App Password found. Email notifications are disabled.")
        print("\nTo enable email notifications:")
        print("1. Go to: https://myaccount.google.com/apppasswords")
        print("2. Generate an App Password for 'Mail'")
        print("3. Add to Streamlit secrets (secrets.toml):")
        print("   [email]")
        print("   GMAIL_APP_PASSWORD = \"your-16-char-app-password\"")
        print("   SENDER_EMAIL = \"your-email@gmail.com\"")
        print("   RECIPIENT_EMAIL = \"therapist-email@gmail.com\"")
        print("\nOr set environment variable: GMAIL_APP_PASSWORD")
        print("=" * 70)
        
        return ""
    
    def send_assessment_email(self, email_data: Dict[str, Any]) -> bool:
        """Send comprehensive assessment email with enhanced protocols"""
        
        # Validate email configuration
        if not self.password:
            print("❌ ERROR: Cannot send email - no password configured")
            print("Assessment data saved but notification not sent")
            return False
        
        if not self.sender_email or not self.recipient_email:
            print("❌ ERROR: Invalid email configuration")
            # Email addresses removed from logs for production security
            return False
        
        try:
            # Extract data
            contact = email_data.get('contact', {})
            analysis = email_data.get('analysis', {})
            responses = email_data.get('responses', {})

            # ✅ NEW: Detect profile category
            profile_category = email_data.get('profile_category', 'CLINICAL')
            wellness_profile = email_data.get('wellness_profile', {})
            
            # Validate required data
            if not contact or not analysis:
                print("❌ ERROR: Missing required email data (contact or analysis)")
                return False
            
            # Check for crisis indicators
            crisis_level = self._assess_crisis_level(analysis, responses)
                        
            # ✅ NEW: Handle both wellness and clinical
            msg = MIMEMultipart('alternative')
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email

            if profile_category == 'WELLNESS':
                # Wellness profile - celebratory subject
                msg['Subject'] = f"🌟 Wellness Profile: {contact.get('full_name', 'Unknown Client')} - No Intervention Needed"
                crisis_level = 'WELLNESS'  # Skip crisis assessment
            else:
                # Clinical case - check for crisis
                crisis_level = self._assess_crisis_level(analysis, responses)
                
                if crisis_level == 'CRITICAL':
                    msg['Subject'] = f"🚨 URGENT CRISIS: {contact.get('full_name', 'Unknown Client')} - IMMEDIATE ACTION REQUIRED"
                elif crisis_level == 'HIGH':
                    msg['Subject'] = f"⚠️ High Priority Assessment: {contact.get('full_name', 'Unknown Client')}"
                else:
                    msg['Subject'] = f"🎯 New Clinical Assessment: {contact.get('full_name', 'Unknown Client')}"


            # Generate comprehensive HTML body
            if profile_category == 'WELLNESS':
                html_body = self._create_wellness_email_body(
                    contact, wellness_profile, analysis
                )
            else:
                html_body = self._create_comprehensive_email_body(
                    contact, analysis, responses, crisis_level
                )

            msg.attach(MIMEText(html_body, 'html'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)
            
            # Production-safe logging (no PII in terminal)
            print("✅ SUCCESS: Assessment email sent")
            # PII removed from terminal output for production security
            # Full details logged in email system only
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("❌ ERROR: Email authentication failed")
            print("Please check your Gmail App Password is correct")
            return False
        except smtplib.SMTPException as e:
            print(f"❌ ERROR: SMTP error: {str(e)}")
            return False
        except Exception as e:
            print(f"❌ ERROR: Failed to send email: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
       
    
    def _assess_crisis_level(
        self, 
        analysis: Dict[str, Any], 
        responses: Dict[int, Any]
    ) -> str:
        """Assess crisis level from assessment data"""
        
        # Check for crisis indicators in responses
        crisis_indicators = []
        
        # Q6: Dissociation/panic/suicidal thoughts
        q6_response = responses.get(6, "")
        if isinstance(q6_response, str):
            if "currently experiencing" in q6_response.lower():
                crisis_indicators.append("Current crisis symptoms reported")
            elif "frequently" in q6_response.lower():
                crisis_indicators.append("Frequent dissociation/panic episodes")
        
        # Q7: Substance use
        q7_response = responses.get(7, "")
        if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
            crisis_indicators.append("Active substance use")
        
        # Check pattern severity
        pattern_hierarchy = analysis.get('pattern_hierarchy', {})
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        if dominant.get('score', 0) >= 9.0:
            crisis_indicators.append(f"Severe {dominant.get('name', 'pattern')} (9+/10)")
        
        # Check urgency
        pattern_scores = analysis.get('pattern_scores', {})
        severe_count = sum(1 for score in pattern_scores.values() if score >= 8.0)
        if severe_count >= 4:
            crisis_indicators.append("Multiple severe patterns (4+)")
        
        # Determine crisis level
        if len(crisis_indicators) >= 3:
            return 'CRITICAL'
        elif len(crisis_indicators) >= 1:
            return 'HIGH'
        else:
            return 'STANDARD'
    
    def _create_comprehensive_email_body(
        self,
        contact: Dict,
        analysis: Dict,
        responses: Dict,
        crisis_level: str
    ) -> str:
        """Create comprehensive HTML email with enhanced clinical protocols"""
        
        # Extract all analysis components
        pattern_hierarchy = analysis.get('pattern_hierarchy', {})
        clinical_summary = analysis.get('clinical_summary', {})
        trigger_chain_analysis = analysis.get('trigger_chain_analysis', {})
        success_prediction = analysis.get('success_prediction', {})
        digital_analysis = analysis.get('digital_analysis', {})
        hidden_barriers = analysis.get('hidden_barriers', {})
        constellation_analysis = analysis.get('constellation_analysis', {})
        
        # Extract key data
        dominant_pattern = pattern_hierarchy.get('dominant_pattern', {})
        primary_patterns = pattern_hierarchy.get('primary_patterns', [])
        pattern_count = pattern_hierarchy.get('pattern_count', 0)
        no_patterns = pattern_count == 0 or not dominant_pattern
        
        client_name = contact.get('full_name', 'Unknown Client')
        client_email = contact.get('email', '')
        urgency = contact.get('urgency', 'Not specified')
        
        # Build HTML email
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #273548;
            background: #f8fafc;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
        }}
        .header {{
            background: linear-gradient(135deg, #4CA1A3 0%, #22c55e 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2rem;
            font-weight: 700;
        }}
        .header p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.95;
        }}
        
        /* CRISIS ALERT - HIGHEST PRIORITY */
        .crisis-alert {{
            background: #fef2f2;
            border: 4px solid #ef4444;
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ border-color: #ef4444; }}
            50% {{ border-color: #dc2626; }}
        }}
        .crisis-alert h2 {{
            color: #b91c1c;
            margin: 0 0 1rem 0;
            font-size: 1.8rem;
        }}
        .crisis-indicators {{
            background: white;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }}
        .crisis-indicators li {{
            margin: 0.5rem 0;
            color: #b91c1c;
            font-weight: 600;
        }}
        
        /* RAPID CLINICAL SUMMARY */
        .clinical-summary {{
            background: #fff3cd;
            border: 3px solid #eab308;
            border-radius: 12px;
            padding: 2rem;
            margin: 2rem;
        }}
        .clinical-summary h2 {{
            color: #b45309;
            margin: 0 0 1.5rem 0;
            font-size: 1.5rem;
            border-bottom: 2px solid #eab308;
            padding-bottom: 0.5rem;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-top: 1.5rem;
        }}
        .summary-item {{
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4CA1A3;
        }}
        .summary-item strong {{
            display: block;
            color: #4CA1A3;
            margin-bottom: 0.5rem;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .summary-item span {{
            color: #273548;
            font-size: 1rem;
            display: block;
            line-height: 1.4;
        }}
        .summary-full {{
            grid-column: 1 / -1;
        }}
        
        /* INTERVENTION PROTOCOLS */
        .intervention-box {{
            background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            border-left: 4px solid #00897b;
        }}
        .intervention-box h4 {{
            margin: 0 0 0.5rem 0;
            color: #00695c;
        }}
        .intervention-box ul {{
            margin: 0.5rem 0;
            padding-left: 1.5rem;
        }}
        
        /* RESISTANCE PREDICTION */
        .resistance-box {{
            background: #fef3c7;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            border-left: 4px solid #f59e0b;
        }}
        .resistance-box h4 {{
            margin: 0 0 0.5rem 0;
            color: #d97706;
        }}
        
        /* OUTCOME TRACKING */
        .outcome-tracking {{
            background: #e1f0f0;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            border-left: 4px solid #4CA1A3;
        }}
        
        .section {{
            padding: 2rem;
            border-bottom: 1px solid #e2e8f0;
        }}
        .section h2 {{
            color: #273548;
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
        }}
        .section h3 {{
            color: #4CA1A3;
            margin: 1.5rem 0 0.75rem 0;
            font-size: 1.2rem;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin: 1rem 0;
        }}
        .info-item {{
            background: #f8fafc;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #cbd5e1;
        }}
        .info-item strong {{
            display: block;
            color: #556D7A;
            margin-bottom: 0.25rem;
            font-size: 0.85rem;
        }}
        .pattern-box {{
            background: linear-gradient(135deg, #4CA1A3 0%, #3B7A7A 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .pattern-box h3 {{
            margin: 0;
            color: white;
            font-size: 1.3rem;
        }}
        .pattern-box p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.95;
        }}
        .trigger-chain {{
            background: #e1f0f0;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .trigger-step {{
            background: white;
            padding: 1rem;
            margin: 0.5rem 0;
            border-left: 4px solid #4CA1A3;
            border-radius: 6px;
        }}
        .trigger-step strong {{
            color: #4CA1A3;
            display: block;
            margin-bottom: 0.25rem;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        th {{
            background: #f8fafc;
            font-weight: 600;
            color: #273548;
        }}
        .urgency-alert {{
            background: #fef2f2;
            border: 2px solid #ef4444;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .urgency-alert h3 {{
            color: #b91c1c;
            margin: 0 0 0.5rem 0;
        }}
        .healthy-baseline {{
            background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            margin: 1rem 0;
        }}
        .healthy-baseline h3 {{
            margin: 0;
            color: white;
        }}
        .referral-box {{
            background: #fef3c7;
            border: 2px solid #f59e0b;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }}
        .referral-box h3 {{
            color: #d97706;
            margin: 0 0 1rem 0;
        }}
        @media (max-width: 600px) {{
            .summary-grid, .info-grid {{
                grid-template-columns: 1fr;
            }}
            .section {{
                padding: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- HEADER -->
        <div class="header">
            <h1>Clinical behavioral pattern assessment</h1>
            <p>Comprehensive 97-question analysis with clinical protocols</p>
            <p>{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        {self._generate_crisis_alert(crisis_level, analysis, responses)}
        
        {self._generate_rapid_clinical_summary(
            client_name, dominant_pattern, primary_patterns, 
            clinical_summary, no_patterns, constellation_analysis
        )}
        
        {self._generate_intervention_protocols(
            dominant_pattern, clinical_summary, digital_analysis, hidden_barriers
        )}
        
        {self._generate_urgency_alert(urgency)}
        
        {self._generate_client_information(contact)}
        
        {self._generate_pattern_analysis(
            dominant_pattern, pattern_hierarchy, no_patterns
        )}
        
        {self._generate_trigger_chain_section(trigger_chain_analysis)}
        
        {self._generate_resistance_prediction(hidden_barriers, clinical_summary)}
        
        {self._generate_success_prediction(success_prediction, analysis)}
        
        {self._generate_digital_analysis(digital_analysis)}
        
        {self._generate_referral_recommendations(analysis, responses)}
        
        {self._generate_outcome_tracking_template(client_name, dominant_pattern)}
        
        {self._generate_response_transcript(responses)}
    </div>
</body>
</html>
        """
        
        return html
    
    def _create_wellness_email_body(
        self,
        contact: Dict,
        wellness_profile: Dict,
        analysis: Dict
    ) -> str:
        """Create celebratory email for wellness profiles - NO therapy needed"""

        client_name = contact.get('full_name', 'Unknown Client')
        client_email = contact.get('email', '')

        # Handle empty wellness_profile (fallback to creating one from analysis)
        if not wellness_profile or not wellness_profile.get('your_superpowers'):
            # Generate basic wellness profile from pattern scores
            pattern_scores = analysis.get('pattern_scores', {})
            if pattern_scores:
                # Calculate health score (inverse of pattern scores)
                health_score = 10 - (sum(pattern_scores.values()) / len(pattern_scores))
                percentile = int((health_score / 10) * 100)
            else:
                health_score = 8.0
                percentile = 80

            celebration_message = 'Congratulations! This client demonstrates exceptional psychological resilience'
            profile_classification = 'HEALTHY'
            superpowers = [
                {'superpower': 'Strong psychological resilience', 'pattern_score': health_score,
                 'what_this_means': 'No clinically significant behavioral patterns detected'},
                {'superpower': 'Adaptive coping mechanisms', 'pattern_score': health_score,
                 'what_this_means': 'Healthy responses to stress and challenges'},
                {'superpower': 'Emotional regulation', 'pattern_score': health_score,
                 'what_this_means': 'Effective management of emotions across situations'}
            ]
            growth_opportunities = []
            recommendations = {
                'recommendation_text': 'This client has a strong psychological foundation and does not require clinical intervention.',
                'primary_recommendation': 'Continue maintaining current wellness practices'
            }
        else:
            # Extract wellness data from provided profile
            celebration_message = wellness_profile.get('celebration_message',
                'Congratulations! This client demonstrates exceptional psychological resilience')
            profile_classification = wellness_profile.get('profile_classification', 'HEALTHY')
            health_score = wellness_profile.get('health_score', 8.0)
            percentile = wellness_profile.get('percentile_ranking', 80)
            superpowers = wellness_profile.get('your_superpowers', [])[:3]
            growth_opportunities = wellness_profile.get('growth_opportunities', [])
            recommendations = wellness_profile.get('recommendations', {})
        
        # Build superpowers HTML
        superpowers_html = ""
        for i, strength in enumerate(superpowers, 1):
            superpower_name = strength.get('superpower', 'Strength')
            pattern_score = strength.get('pattern_score', 0)
            what_this_means = strength.get('what_this_means', '')
            superpowers_html += f"""
                <div style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
                            padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981; 
                            margin-bottom: 1rem;">
                    <h4 style="color: #065f46; margin: 0 0 0.5rem 0;">
                        #{i}: {superpower_name} ({pattern_score:.1f}/10)
                    </h4>
                    <p style="color: #047857; margin: 0;">{what_this_means}</p>
                </div>
            """
        
        # Build growth opportunities HTML
        growth_html = ""
        if growth_opportunities:
            for growth in growth_opportunities[:3]:
                pattern_name = growth.get('pattern_name', 'Area')
                growth_opportunity = growth.get('growth_opportunity', '')
                growth_html += f"""
                    <li><strong>{pattern_name}:</strong> {growth_opportunity}</li>
                """
        else:
            growth_html = "<li>No specific growth areas identified - excellent overall wellness</li>"
        
        # Recommendation
        recommendation_text = recommendations.get('recommendation_text', 
            'This client has a strong psychological foundation and does not require clinical intervention.')
        
        html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #273548;
                background: #f8fafc;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: white;
            }}
            .header {{
                background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
                color: white;
                padding: 2rem;
                text-align: center;
            }}
            .wellness-hero {{
                background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
                padding: 2.5rem;
                border-radius: 16px;
                text-align: center;
                margin: 2rem;
            }}
            .section {{
                padding: 2rem;
                border-bottom: 1px solid #e2e8f0;
            }}
            .info-item {{
                background: #f8fafc;
                padding: 1rem;
                margin: 0.5rem 0;
                border-radius: 8px;
                border-left: 4px solid #22c55e;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- HEADER -->
            <div class="header">
                <h1>🌟 WELLNESS PROFILE ASSESSMENT</h1>
                <p>NO CLINICAL INTERVENTION NEEDED</p>
                <p>{datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
            </div>
            
            <!-- WELLNESS HERO -->
            <div class="wellness-hero">
                <h2 style="color: #065f46; margin: 0 0 1rem 0; font-size: 2rem;">
                    {celebration_message}
                </h2>
                <div style="display: flex; justify-content: center; gap: 2rem; margin: 1.5rem 0;">
                    <div>
                        <div style="font-size: 2.5rem; font-weight: bold; color: #059669;">
                            {health_score:.1f}/10
                        </div>
                        <div style="color: #047857;">Wellness Score</div>
                    </div>
                    <div>
                        <div style="font-size: 2.5rem; font-weight: bold; color: #059669;">
                            Top {percentile}%
                        </div>
                        <div style="color: #047857;">Population</div>
                    </div>
                </div>
                <p style="color: #047857; font-size: 1.2rem; margin: 0;">
                    Profile: {profile_classification.replace('_', ' ').title()}
                </p>
            </div>
            
            <!-- CLINICAL NOTE -->
            <div style="background: #fef3c7; border: 3px solid #eab308; padding: 2rem; margin: 2rem; border-radius: 12px;">
                <h3 style="color: #b45309; margin: 0 0 1rem 0;">📋 CLINICAL NOTE</h3>
                <p style="margin: 0.5rem 0; font-size: 1.1rem; font-weight: 600; color: #92400e;">
                    NO HYPNOTHERAPY NEEDED - Healthy Baseline
                </p>
                <p style="margin: 0.5rem 0; color: #92400e;">
                    This client demonstrates exceptional psychological resilience with no clinically 
                    significant behavioral patterns requiring therapeutic intervention.
                </p>
                <p style="margin: 1rem 0 0 0; color: #92400e;">
                    <strong>Recommendation:</strong> {recommendation_text}
                </p>
            </div>
            
            <!-- CLIENT INFO -->
            <div class="section">
                <h2>Client information</h2>
                <div class="info-item">
                    <strong>Name:</strong> {client_name}
                </div>
                <div class="info-item">
                    <strong>Email:</strong> {client_email}
                </div>
                <div class="info-item">
                    <strong>Phone:</strong> {contact.get('phone', 'Not provided')}
                </div>
                <div class="info-item">
                    <strong>Primary Concern:</strong> {contact.get('primary_concern', 'Not provided')}
                </div>
            </div>
            
            <!-- PSYCHOLOGICAL STRENGTHS -->
            <div class="section">
                <h2>🎯 Psychological strengths (Top 3)</h2>
                {superpowers_html}
            </div>
            
            <!-- GROWTH OPPORTUNITIES -->
            <div class="section">
                <h2>📈 Optional growth opportunities</h2>
                <p style="color: #556D7A; font-style: italic;">
                    These aren't problems—they're areas where already-strong skills could be further enhanced.
                </p>
                <ul style="margin: 1rem 0; padding-left: 1.5rem;">
                    {growth_html}
                </ul>
            </div>
            
            <!-- SUGGESTED RESPONSE -->
            <div class="section">
                <h2>💬 Suggested client communication</h2>
                <div style="background: #e1f0f0; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #22c55e;">
                    <p style="margin: 0 0 1rem 0;"><strong>Suggested message to client:</strong></p>
                    <p style="margin: 0; font-style: italic; color: #273548;">
                        "Thank you for completing the assessment. Your results indicate exceptional psychological 
                        resilience with no patterns requiring clinical intervention. This is excellent news! 
                        Your strong baseline means you're well-equipped to handle life's challenges independently.
                        
                        If you're interested in peak performance optimization or advanced personal development, 
                        we do offer optional coaching services. However, this is entirely optional given your 
                        already-strong foundation.
                        
                        Congratulations on your psychological wellness!"
                    </p>
                </div>
            </div>
            
            <!-- OPTIONAL SERVICES -->
            <div class="section">
                <h2>🚀 Optional services (if client interested)</h2>
                <div style="background: #f8fafc; padding: 1rem; border-radius: 8px;">
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li><strong>Peak Performance Coaching:</strong> 1-2 sessions, ฿1,500-3,000</li>
                        <li><strong>Advanced Personal Development:</strong> Customized program</li>
                        <li><strong>Leadership Development:</strong> Executive coaching</li>
                    </ul>
                    <p style="margin: 1rem 0 0 0; color: #556D7A; font-size: 0.9rem;">
                        <em>Note: Given their strong baseline, these services are entirely optional. 
                        Client can continue their wellness journey independently.</em>
                    </p>
                </div>
            </div>
        </div>
    </body>
    </html>
        """
        
        return html

    def _generate_crisis_alert(
        self, 
        crisis_level: str, 
        analysis: Dict, 
        responses: Dict
    ) -> str:
        """Generate crisis alert if needed"""
        
        if crisis_level == 'STANDARD':
            return ""
        
        # Collect crisis indicators
        crisis_indicators = []
        
        # Check Q6: Dissociation/panic/suicidal
        q6_response = responses.get(6, "")
        if isinstance(q6_response, str) and ("currently experiencing" in q6_response.lower() or "frequently" in q6_response.lower()):
            crisis_indicators.append("Active crisis symptoms (dissociation/panic/suicidal ideation)")
        
        # Check Q7: Substance use
        q7_response = responses.get(7, "")
        if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
            crisis_indicators.append("Active substance use reported")
        
        # Check pattern severity
        pattern_hierarchy = analysis.get('pattern_hierarchy', {})
        dominant = pattern_hierarchy.get('dominant_pattern', {})
        if dominant.get('score', 0) >= 9.0:
            crisis_indicators.append(f"Severe {dominant.get('name', 'pattern')} pattern (9+/10)")
        
        # Check for multiple severe patterns
        pattern_scores = analysis.get('pattern_scores', {})
        severe_count = sum(1 for score in pattern_scores.values() if score >= 8.0)
        if severe_count >= 4:
            crisis_indicators.append(f"Multiple severe patterns ({severe_count} patterns at 8+/10)")
        
        indicators_html = "".join([f"<li>{indicator}</li>" for indicator in crisis_indicators])
        
        if crisis_level == 'CRITICAL':
            return f"""
                <div class="crisis-alert">
                    <h2>🚨 CRITICAL: IMMEDIATE ACTION REQUIRED</h2>
                    <p style="font-size: 1.2rem; font-weight: 600; margin: 1rem 0;">
                        This assessment indicates acute crisis risk requiring immediate clinical response.
                    </p>
                    <div class="crisis-indicators">
                        <strong style="color: #b91c1c; display: block; margin-bottom: 0.5rem;">
                            Crisis Indicators Detected:
                        </strong>
                        <ul>{indicators_html}</ul>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="color: #b91c1c; display: block; margin-bottom: 0.5rem;">
                            IMMEDIATE ACTIONS REQUIRED:
                        </strong>
                        <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li><strong>Contact client within 2-4 hours</strong></li>
                            <li>Assess immediate safety and suicidality</li>
                            <li>Provide crisis resources if needed</li>
                            <li>Consider referral for psychiatric evaluation</li>
                            <li>Document all crisis interventions</li>
                        </ol>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong>Crisis Resources to Provide:</strong>
                        <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li>National Suicide Prevention Lifeline: 988</li>
                            <li>Crisis Text Line: Text HOME to 741741</li>
                            <li>Emergency Services: Local emergency number</li>
                        </ul>
                    </div>
                </div>
            """
        else:  # HIGH
            return f"""
                <div class="crisis-alert" style="border-color: #f59e0b; background: #fef3c7;">
                    <h3 style="color: #d97706;">⚠️ HIGH PRIORITY: ELEVATED RISK</h3>
                    <div class="crisis-indicators" style="background: white;">
                        <strong style="color: #d97706; display: block; margin-bottom: 0.5rem;">
                            Risk Indicators:
                        </strong>
                        <ul style="color: #d97706;">{indicators_html}</ul>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="color: #d97706;">Recommended Actions:</strong>
                        <ol style="margin: 0.5rem 0; padding-left: 1.5rem; color: #92400e;">
                            <li>Contact client within 24 hours</li>
                            <li>Assess safety and readiness for intervention</li>
                            <li>Prepare crisis resources for session 1</li>
                            <li>Consider consultation before proceeding</li>
                        </ol>
                    </div>
                </div>
            """
    
    def _generate_rapid_clinical_summary(
        self,
        client_name: str,
        dominant_pattern: Dict,
        primary_patterns: List[Dict],
        clinical_summary: Dict,
        no_patterns: bool,
        constellation_analysis: Dict
    ) -> str:
        """Generate rapid clinical summary template section"""
        
        if no_patterns:
            return """
                <div class="healthy-baseline" style="margin: 2rem;">
                    <h3>✓ Healthy baseline - no clinical intervention needed</h3>
                    <p style="margin: 0.5rem 0; opacity: 0.95;">
                        No significant behavioral patterns detected. Consider performance optimization services.
                    </p>
                </div>
            """
        
        # Extract data with proper fallbacks
        dominant_name = dominant_pattern.get('name', 'Unknown').title()
        dominant_score = dominant_pattern.get('score', 0)
        
        primary_1_name = "None"
        primary_1_score = 0
        primary_2_name = "None"
        primary_2_score = 0
        
        if len(primary_patterns) > 0:
            primary_1_name = primary_patterns[0].get('name', 'Unknown').title()
            primary_1_score = primary_patterns[0].get('score', 0)
        
        if len(primary_patterns) > 1:
            primary_2_name = primary_patterns[1].get('name', 'Unknown').title()
            primary_2_score = primary_patterns[1].get('score', 0)
        
        # Clinical summary data
        core_belief = clinical_summary.get('core_limiting_belief', 'Not identified')
        hidden_benefits = clinical_summary.get('hidden_benefits', 'Not identified')
        systemic_resistance = clinical_summary.get('systemic_resistance', 'Not identified')
        identity_threat = clinical_summary.get('identity_threat', 'Not identified')
        session_1_focus = clinical_summary.get('session_1_focus', 'Pattern exploration')
        session_2_target = clinical_summary.get('session_2_target', 'Core transformation')
        session_3_need = clinical_summary.get('potential_session_3_need', 'Unknown')
        readiness = clinical_summary.get('change_readiness_score', '0/10')
        intervention_keywords = clinical_summary.get('intervention_keywords', 'Not specified')
        avoid_language = clinical_summary.get('avoid_language', 'Not specified')
        
        # Constellation data
        constellation_multiplier = constellation_analysis.get('constellation_multiplier', 1.0)
        constellation_complexity = constellation_analysis.get('constellation_complexity', 'Unknown')
        
        resistance_points = clinical_summary.get('predicted_resistance_points', [])
        if not resistance_points:
            resistance_points = ["Standard resistance patterns expected"]
        resistance_html = "".join([f"<li>{point}</li>" for point in resistance_points])
        
        return f"""
            <div class="clinical-summary">
                <h2>⚡ RAPID CLINICAL SUMMARY TEMPLATE</h2>
                
                <div class="summary-grid">
                    <div class="summary-item">
                        <strong>Client</strong>
                        <span>{client_name}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Date</strong>
                        <span>{datetime.now().strftime('%Y-%m-%d')}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Dominant Pattern</strong>
                        <span>{dominant_name}<br>(Score: {dominant_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Primary Pattern</strong>
                        <span>{primary_1_name}<br>(Score: {primary_1_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Secondary Pattern</strong>
                        <span>{primary_2_name}<br>(Score: {primary_2_score:.1f}/10)</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Change Readiness</strong>
                        <span>{readiness}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Pattern Constellation</strong>
                        <span>{constellation_complexity}<br>Amplification: {constellation_multiplier}x</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Session 3 Probability</strong>
                        <span>{session_3_need}</span>
                    </div>
                    
                    <div class="summary-item summary-full">
                        <strong>Core Limiting Belief</strong>
                        <span>{core_belief}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Hidden Benefits (Secondary Gain)</strong>
                        <span>{hidden_benefits}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Identity Threat</strong>
                        <span>{identity_threat}</span>
                    </div>
                    
                    <div class="summary-item summary-full">
                        <strong>Systemic Resistance Sources</strong>
                        <span>{systemic_resistance}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Session 1 Focus</strong>
                        <span>{session_1_focus}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>Session 2 Target</strong>
                        <span>{session_2_target}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>✓ Intervention Keywords</strong>
                        <span style="color: #22c55e;">{intervention_keywords}</span>
                    </div>
                    
                    <div class="summary-item">
                        <strong>✗ Avoid Language</strong>
                        <span style="color: #ef4444;">{avoid_language}</span>
                    </div>
                </div>
                
                <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                    <strong style="color: #b45309; display: block; margin-bottom: 0.5rem;">
                        🎯 Predicted Resistance Points:
                    </strong>
                    <ol style="margin: 0.5rem 0; padding-left: 1.5rem; color: #92400e;">{resistance_html}</ol>
                </div>
            </div>
        """
    
    def _generate_intervention_protocols(
        self,
        dominant_pattern: Dict,
        clinical_summary: Dict,
        digital_analysis: Dict,
        hidden_barriers: Dict
    ) -> str:
        """Generate specific intervention protocols section"""
        
        if not dominant_pattern:
            return ""
        
        pattern_name = dominant_pattern.get('name', 'Unknown').title()
        pattern_desc = dominant_pattern.get('description', {})
        
        # Session 1 protocols
        session_1_protocols = [
            clinical_summary.get('session_1_focus', 'Pattern mapping'),
            "Establish therapeutic alliance with collaborative language",
            "Complete behavioral chain analysis",
            "Initial positive programming via light hypnosis"
        ]
        
        # Session 2 protocols
        session_2_protocols = [
            clinical_summary.get('session_2_target', 'Core transformation'),
            f"Deep hypnotic pattern interruption of {pattern_name}",
            "Neural pathway installation for new responses",
            "Future pacing and integration work"
        ]
        
        # Digital adaptations if needed
        digital_adaptations = []
        if digital_analysis and digital_analysis.get('severity_level') in ['SEVERE', 'MODERATE']:
            digital_adaptations = [
                "Shorten session segments to 15-30 minutes",
                "Use collaborative non-authoritative language",
                "Address ironic detachment before emotional work",
                "Honor digital competencies as strengths"
            ]
        
        # Resistance management
        resistance_type = hidden_barriers.get('resistance_type', 'Standard resistance')
        resistance_management = self._get_resistance_management_protocol(resistance_type)
        
        session_1_html = "".join([f"<li>{protocol}</li>" for protocol in session_1_protocols])
        session_2_html = "".join([f"<li>{protocol}</li>" for protocol in session_2_protocols])
        digital_html = "".join([f"<li>{adaptation}</li>" for adaptation in digital_adaptations]) if digital_adaptations else "<li>Standard protocols appropriate</li>"
        resistance_html = "".join([f"<li>{strategy}</li>" for strategy in resistance_management])
        
        return f"""
            <div class="section">
                <h2>🎯 Intervention protocols & clinical strategies</h2>
                
                <div class="intervention-box">
                    <h4>Session 1 Protocol (90 minutes)</h4>
                    <ul>{session_1_html}</ul>
                </div>
                
                <div class="intervention-box">
                    <h4>Session 2 Protocol (90 minutes)</h4>
                    <ul>{session_2_html}</ul>
                </div>
                
                <div class="intervention-box" style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-left-color: #f59e0b;">
                    <h4 style="color: #d97706;">Digital-Native Adaptations</h4>
                    <ul>{digital_html}</ul>
                </div>
                
                <div class="resistance-box">
                    <h4>Resistance Management Strategy</h4>
                    <p><strong>Predicted resistance type:</strong> {resistance_type}</p>
                    <ul>{resistance_html}</ul>
                </div>
            </div>
        """
    
    def _get_resistance_management_protocol(self, resistance_type: str) -> List[str]:
        """Get specific resistance management strategies"""
        
        protocols = {
            'Identity-based': [
                "Frame change as evolution, not abandonment of self",
                "Honor protective function before updating it",
                "Use 'both/and' language for identity integration"
            ],
            'Systemic': [
                "Prepare for relationship pushback",
                "Install boundary maintenance protocols",
                "Create scripts for communicating changes"
            ],
            'Emotional': [
                "Titrate emotional exposure gradually",
                "Use resource anchoring before affect work",
                "Install emotional regulation tools first"
            ],
            'Existential': [
                "Build evidence incrementally, avoid hope talk",
                "Focus on curiosity rather than optimism",
                "Use 'what if it were possible' reframing"
            ],
            'Minimal': [
                "Standard therapeutic alliance building",
                "Direct subconscious access via theta state",
                "Collaborative goal-setting"
            ]
        }
        
        # Find matching protocol
        for key, protocol in protocols.items():
            if key in resistance_type:
                return protocol
        
        return protocols['Minimal']
    
    def _generate_urgency_alert(self, urgency: str) -> str:
        """Generate urgency alert if needed"""
        
        if not urgency or urgency == 'Not specified':
            return ""
        
        urgency_lower = urgency.lower()
        
        if 'extremely urgent' in urgency_lower or 'same day' in urgency_lower:
            return """
                <div class="urgency-alert" style="margin: 2rem;">
                    <h3>🚨 CLIENT URGENCY: EXTREMELY URGENT</h3>
                    <p><strong>Action Required:</strong> Contact client within 24 hours</p>
                    <p>Client has indicated extreme urgency - prioritize scheduling immediately</p>
                </div>
            """
        elif 'very urgent' in urgency_lower or '24 hours' in urgency_lower or 'within the next week' in urgency_lower:
            return """
                <div class="urgency-alert" style="border-color: #eab308; background: #fef3c7;">
                    <h3 style="color: #b45309;">⚠️ HIGH PRIORITY: VERY URGENT</h3>
                    <p><strong>Action Required:</strong> Contact client within 24-48 hours</p>
                </div>
            """
        elif 'moderately urgent' in urgency_lower or 'within the next month' in urgency_lower:
            return """
                <div style="background: #e1f0f0; border: 2px solid #4CA1A3; padding: 1rem; border-radius: 8px; margin: 2rem;">
                    <h3 style="color: #00695c; margin: 0 0 0.5rem 0;">⏰ Moderate Priority</h3>
                    <p style="margin: 0;">Contact client within 3-5 days</p>
                </div>
            """
        
        return ""
    
    def _generate_client_information(self, contact: Dict) -> str:
        """Generate client information section"""
        
        additional_info = contact.get('additional_info', '')
        additional_html = ""
        if additional_info and additional_info not in ['None provided', '']:
            additional_html = f"""
                <div class="info-item" style="grid-column: 1 / -1; margin-top: 0.5rem;">
                    <strong>Additional Information:</strong>
                    <span>{additional_info}</span>
                </div>
            """
        
        return f"""
            <div class="section">
                <h2>Client information</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Name:</strong>
                        <span>{contact.get('full_name', 'Unknown')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Email:</strong>
                        <span>{contact.get('email', 'Not provided')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Phone:</strong>
                        <span>{contact.get('phone', 'Not provided')}</span>
                    </div>
                    <div class="info-item">
                        <strong>Urgency:</strong>
                        <span>{contact.get('urgency', 'Not specified')}</span>
                    </div>
                </div>
                <div class="info-item" style="margin-top: 1rem;">
                    <strong>Primary Concern:</strong>
                    <span>{contact.get('primary_concern', 'Not provided')}</span>
                </div>
                {additional_html}
            </div>
        """
    
    def _generate_pattern_analysis(
        self,
        dominant_pattern: Dict,
        pattern_hierarchy: Dict,
        no_patterns: bool
    ) -> str:
        """Generate pattern analysis section"""
        
        if no_patterns:
            return ""
        
        pattern_name = dominant_pattern.get('name', 'Unknown').title()
        pattern_score = dominant_pattern.get('score', 0)
        pattern_severity = dominant_pattern.get('severity', 'Unknown')
        pattern_desc = dominant_pattern.get('description', {})
        
        root_structure = pattern_desc.get('root_structure', 'Not available')
        systemic_factors = pattern_desc.get('systemic_factors', [])
        identity_conflict = pattern_desc.get('identity_conflict', 'Not available')
        hidden_loyalties = pattern_desc.get('hidden_loyalties', [])
        protective_function = pattern_desc.get('protective_function', 'Not identified')
        intervention_focus = pattern_desc.get('intervention_focus', 'Not identified')
        
        systemic_html = "".join([f"<li>{factor}</li>" for factor in systemic_factors]) if systemic_factors else "<li>None identified</li>"
        loyalties_html = "".join([f"<li>{loyalty}</li>" for loyalty in hidden_loyalties]) if hidden_loyalties else "<li>None identified</li>"
        
        all_scores = pattern_hierarchy.get('all_scores', {})
        pattern_table = self._generate_pattern_table(all_scores)
        
        return f"""
            <div class="section">
                <h2>Behavioral pattern analysis</h2>
                
                <div class="pattern-box">
                    <h3>Dominant pattern: {pattern_name}</h3>
                    <p style="font-size: 1.5rem; font-weight: bold; margin: 0.5rem 0;">
                        {pattern_score:.1f}/10 ({pattern_severity})
                    </p>
                </div>
                
                <h3>Pattern structure & function</h3>
                <div class="info-item">
                    <strong>Root structural belief:</strong>
                    <span>{root_structure}</span>
                </div>
                
                <div class="info-item" style="margin-top: 0.5rem;">
                    <strong>Protective function:</strong>
                    <span>{protective_function}</span>
                </div>
                
                <div class="info-item" style="margin-top: 0.5rem;">
                    <strong>Intervention focus:</strong>
                    <span>{intervention_focus}</span>
                </div>
                
                <h3>Systemic factors maintaining pattern</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {systemic_html}
                </ul>
                
                <h3>Identity conflict</h3>
                <div class="info-item">
                    <span>{identity_conflict}</span>
                </div>
                
                <h3>Hidden loyalties creating resistance</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {loyalties_html}
                </ul>
                
                <h3>Complete pattern constellation</h3>
                {pattern_table}
            </div>
        """
    
    def _generate_pattern_table(self, all_scores: Dict[int, float]) -> str:
        """Generate pattern scores table"""
        
        significant = {pid: score for pid, score in all_scores.items() if score >= 4.0}
        
        if not significant:
            return '<p style="color: #22c55e; font-weight: 600;">✓ No clinically significant patterns detected</p>'
        
        rows = []
        for pid, score in sorted(significant.items(), key=lambda x: x[1], reverse=True):
            pattern_name = PATTERNS.get(pid, f"Pattern {pid}").title()
            severity = self._get_severity(score)
            
            # Color code severity
            severity_color = "#ef4444" if "Severe" in severity else "#eab308" if "Moderate" in severity else "#4CA1A3"
            
            rows.append(f"""
                <tr>
                    <td>{pattern_name}</td>
                    <td><strong>{score:.1f}/10</strong></td>
                    <td style="color: {severity_color}; font-weight: 600;">{severity}</td>
                </tr>
            """)
        
        return f"""
            <table>
                <tr>
                    <th>Pattern</th>
                    <th>Score</th>
                    <th>Severity</th>
                </tr>
                {"".join(rows)}
            </table>
        """
    
    def _get_severity(self, score: float) -> str:
        """Get severity classification"""
        if score >= 8.0: return "Severe"
        elif score >= 6.0: return "Moderate-High"
        elif score >= 4.0: return "Moderate"
        else: return "Mild"
    
    def _generate_trigger_chain_section(self, trigger_chain_analysis: Dict) -> str:
        """Generate trigger chain sequence section"""
        
        chain = trigger_chain_analysis.get('trigger_sequence', {})
        intervention_windows = trigger_chain_analysis.get('intervention_windows', [])
        completeness = trigger_chain_analysis.get('sequence_completeness', 0)
        
        intervention_html = ""
        if intervention_windows:
            for window in intervention_windows:
                point = window.get('point', 'Unknown')
                description = window.get('description', '')
                technique = window.get('technique', '')
                intervention_html += f"""
                    <li><strong>{point}:</strong> {description}<br>
                    <em style="color: #556D7A;">Technique: {technique}</em></li>
                """
        else:
            intervention_html = "<li>Complete sequence mapping in session 1</li>"
        
        return f"""
            <div class="section">
                <h2>Complete trigger sequence mapping</h2>
                <p><strong>Sequence completeness:</strong> {completeness:.0f}%</p>
                
                <div class="trigger-chain">
                    <div class="trigger-step">
                        <strong>1. Environmental trigger:</strong>
                        <span>{chain.get('environmental_trigger', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>2. First awareness point:</strong>
                        <span>{chain.get('awareness_entry_point', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>3. Physical response:</strong>
                        <span>{chain.get('physical_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>4. Automatic thought:</strong>
                        <span>{chain.get('automatic_thought', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>5. Emotional response:</strong>
                        <span>{chain.get('emotional_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>6. Behavioral response:</strong>
                        <span>{chain.get('behavioral_response', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>7. Immediate consequence:</strong>
                        <span>{chain.get('immediate_consequence', 'Not captured')}</span>
                    </div>
                    
                    <div class="trigger-step">
                        <strong>8. Extended impact:</strong>
                        <span>{chain.get('extended_impact', 'Not captured')}</span>
                    </div>
                </div>
                
                <h3>Intervention windows identified</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {intervention_html}
                </ul>
            </div>
        """
    
    def _generate_resistance_prediction(
        self,
        hidden_barriers: Dict,
        clinical_summary: Dict
    ) -> str:
        """Generate resistance prediction section"""
        
        resistance_type = hidden_barriers.get('resistance_type', 'Standard resistance')
        resistance_intensity = hidden_barriers.get('resistance_intensity', 'Unknown')
        secondary_gain = hidden_barriers.get('secondary_gain', 'Not identified')
        systemic_stakeholders = hidden_barriers.get('systemic_stakeholders', ['Not identified'])
        protective_functions = hidden_barriers.get('protective_functions', ['Not identified'])
        
        resistance_points = clinical_summary.get('predicted_resistance_points', [])
        if not resistance_points:
            resistance_points = ["Standard therapeutic resistance expected"]
        
        stakeholders_html = "".join([f"<li>{stakeholder}</li>" for stakeholder in systemic_stakeholders])
        functions_html = "".join([f"<li>{function}</li>" for function in protective_functions])
        points_html = "".join([f"<li>{point}</li>" for point in resistance_points])
        
        # Color code intensity
        intensity_color = "#ef4444" if "High" in resistance_intensity else "#eab308" if "Moderate" in resistance_intensity else "#22c55e"
        
        return f"""
            <div class="section">
                <h2>Resistance prediction & management</h2>
                
                <div class="resistance-box">
                    <h4>Resistance Profile</h4>
                    <div class="info-grid" style="margin-top: 1rem;">
                        <div class="info-item" style="border-left-color: {intensity_color};">
                            <strong>Resistance Intensity:</strong>
                            <span style="color: {intensity_color}; font-weight: 600;">{resistance_intensity}</span>
                        </div>
                        <div class="info-item">
                            <strong>Resistance Type:</strong>
                            <span>{resistance_type}</span>
                        </div>
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="display: block; margin-bottom: 0.5rem;">Secondary Gain (What pattern protects):</strong>
                        <span>{secondary_gain}</span>
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="display: block; margin-bottom: 0.5rem;">Protective Functions:</strong>
                        <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">{functions_html}</ul>
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="display: block; margin-bottom: 0.5rem;">Systemic Stakeholders (Who benefits from pattern staying):</strong>
                        <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">{stakeholders_html}</ul>
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong style="display: block; margin-bottom: 0.5rem;">Specific Resistance Points to Anticipate:</strong>
                        <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">{points_html}</ol>
                    </div>
                </div>
            </div>
        """
    
    def _generate_success_prediction(self, success_prediction: Dict, analysis: Dict) -> str:
        """Generate success prediction section"""
        
        success_rate = success_prediction.get('overall_success_rate', 85)
        success_tier = success_prediction.get('success_tier', 'High')
        recommended_sessions = success_prediction.get('recommended_sessions', 2)
        timeline = success_prediction.get('timeline_estimate', '2 weeks')
        
        # Get session prediction details
        session_prediction = analysis.get('session_prediction', {})
        complexity_score = session_prediction.get('complexity_score', 0)
        session_3_probability = session_prediction.get('session_3_probability', 'Low')
        
        # Color code success rate
        success_color = "#22c55e" if success_rate >= 85 else "#4CA1A3" if success_rate >= 80 else "#eab308"
        
        return f"""
            <div class="section">
                <h2>Success prediction & timeline</h2>
                
                <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, {success_color} 0%, #4CA1A3 100%); 
                            color: white; border-radius: 12px; margin: 1rem 0;">
                    <div style="font-size: 3rem; font-weight: bold;">{success_rate}%</div>
                    <p style="margin: 0.5rem 0; opacity: 0.95; font-size: 1.2rem;">
                        Predicted success rate ({success_tier})
                    </p>
                </div>
                
                <div class="info-grid">
                    <div class="info-item">
                        <strong>Recommended Sessions:</strong>
                        <span>{recommended_sessions} sessions</span>
                    </div>
                    <div class="info-item">
                        <strong>Timeline Estimate:</strong>
                        <span>{timeline}</span>
                    </div>
                    <div class="info-item">
                        <strong>Complexity Score:</strong>
                        <span>{complexity_score:.1f}/15</span>
                    </div>
                    <div class="info-item">
                        <strong>Session 3 Probability:</strong>
                        <span>{session_3_probability}</span>
                    </div>
                </div>
                
                <div style="background: #e1f0f0; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                    <strong style="display: block; margin-bottom: 0.5rem;">Expected Timeline:</strong>
                    <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li><strong>Week 1:</strong> Session 1 - Pattern mapping & initial programming</li>
                        <li><strong>Week 2:</strong> Session 2 - Core transformation & neural rewiring</li>
                        <li><strong>Week 3-4:</strong> Integration period (subconscious consolidation)</li>
                        {f'<li><strong>Session 3 (if needed):</strong> Reinforcement & stabilization</li>' if session_3_probability != 'Low' else ''}
                    </ul>
                </div>
            </div>
        """
    
    def _generate_digital_analysis(self, digital_analysis: Dict) -> str:
        """Generate digital analysis section if applicable"""
        
        if not digital_analysis or not digital_analysis.get('is_digital_native'):
            return ""
        
        severity = digital_analysis.get('severity_level', 'MINIMAL')
        score = digital_analysis.get('digital_despair_score', 0)
        
        if severity == 'MINIMAL':
            return ""
        
        primary_driver = digital_analysis.get('primary_digital_driver', 'Unknown').replace('_', ' ').title()
        screen_time = digital_analysis.get('screen_time_hours', 0)
        social_media_pct = digital_analysis.get('social_media_percentage', 0)
        
        # Get digital interplay if available
        digital_interplay = digital_analysis.get('digital_interplay', {})
        amplification_effects = digital_interplay.get('amplification_effects', {})
        intervention_priorities = digital_interplay.get('intervention_priority', [])
        
        amplification_html = ""
        if amplification_effects:
            for effect_name, effect_data in amplification_effects.items():
                amplification_html += f"""
                    <li><strong>{effect_name.replace('_', ' ').title()}:</strong> 
                    {effect_data.get('description', 'No description')}<br>
                    <em style="color: #556D7A;">Intervention: {effect_data.get('intervention', 'Standard protocol')}</em></li>
                """
        
        priorities_html = "".join([f"<li>{priority}</li>" for priority in intervention_priorities[:5]])
        if not priorities_html:
            priorities_html = "<li>Standard digital-aware protocols</li>"
        
        # Severity-specific recommendations
        severity_recommendations = {
            'SEVERE': [
                "Use 15-30 minute session segments (not 50 minutes)",
                "Employ anti-authority collaborative language throughout",
                "Address ironic detachment before authentic emotional work",
                "Build digital bridge: honor online competencies as real skills",
                "Install gradual digital detox (not cold turkey elimination)",
                "Dopamine regulation protocols before joy permission work"
            ],
            'MODERATE': [
                "Use 45-60 minute sessions with movement breaks",
                "Reduce directive language, increase collaboration",
                "Validate digital achievements alongside offline goals",
                "Address comparison anxiety and FOMO explicitly",
                "Implement mindful digital use (not elimination)"
            ],
            'MILD': [
                "Standard protocol with digital awareness",
                "Address digital factors as contextual influences",
                "Integrate digital competencies as strengths"
            ]
        }
        
        recommendations = severity_recommendations.get(severity, severity_recommendations['MILD'])
        recommendations_html = "".join([f"<li>{rec}</li>" for rec in recommendations])
        
        return f"""
            <div class="section">
                <h2>📱 Digital conditioning analysis & specialized protocols</h2>
                
                <div class="info-item" style="background: #fef3c7; border-left-color: #eab308;">
                    <strong>Digital Despair Score:</strong>
                    <span style="font-size: 1.2rem; font-weight: 600;">{score:.1f}% ({severity})</span>
                </div>
                
                <div class="info-grid" style="margin-top: 1rem;">
                    <div class="info-item">
                        <strong>Primary Digital Driver:</strong>
                        <span>{primary_driver}</span>
                    </div>
                    <div class="info-item">
                        <strong>Screen Time:</strong>
                        <span>{screen_time:.1f} hours/day</span>
                    </div>
                    <div class="info-item">
                        <strong>Social Media Usage:</strong>
                        <span>{social_media_pct:.0f}% of digital time</span>
                    </div>
                </div>
                
                <h3>Specialized adaptations required ({severity})</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem; background: #fef3c7; padding: 1rem; border-radius: 8px;">
                    {recommendations_html}
                </ul>
                
                {f'''
                <h3>Digital-Pattern amplification effects</h3>
                <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {amplification_html}
                </ul>
                ''' if amplification_html else ''}
                
                <h3>Digital intervention priorities</h3>
                <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
                    {priorities_html}
                </ol>
                
                <div style="background: #e1f0f0; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                    <strong style="display: block; margin-bottom: 0.5rem;">⚡ Why specialized protocol works:</strong>
                    <p style="margin: 0.5rem 0;">Digital-native brains have different neuroplasticity patterns due to algorithmic conditioning. 
                    Standard 50-minute sessions don't match their attention architecture. Our adapted protocols respect their neurology 
                    while facilitating transformation.</p>
                </div>
            </div>
        """
    
    def _generate_referral_recommendations(self, analysis: Dict, responses: Dict) -> str:
        """Generate referral recommendations when appropriate"""
        
        referrals_needed = []
        
        # Check crisis indicators
        q6_response = responses.get(6, "")
        if isinstance(q6_response, str) and ("currently experiencing" in q6_response.lower() or "frequently" in q6_response.lower()):
            referrals_needed.append({
                'type': 'Psychiatric Evaluation',
                'reason': 'Active crisis symptoms (dissociation/panic/suicidal ideation)',
                'urgency': 'URGENT',
                'action': 'Refer before beginning hypnotherapy sessions'
            })
        
        # Check substance use
        q7_response = responses.get(7, "")
        if isinstance(q7_response, str) and "recreational drugs" in q7_response.lower():
            referrals_needed.append({
                'type': 'Substance Abuse Assessment',
                'reason': 'Active substance use reported',
                'urgency': 'HIGH',
                'action': 'Concurrent treatment recommended'
            })
        
        # Check medical care
        q5_response = responses.get(5, "")
        if isinstance(q5_response, str):
            if "mental health" in q5_response.lower() or "psychiatric" in q5_response.lower():
                referrals_needed.append({
                    'type': 'Psychiatrist Coordination',
                    'reason': 'Currently under psychiatric care',
                    'urgency': 'STANDARD',
                    'action': 'Coordinate with existing provider before proceeding'
                })
        
        # Check pattern severity
        pattern_scores = analysis.get('pattern_scores', {})
        severe_count = sum(1 for score in pattern_scores.values() if score >= 9.0)
        if severe_count >= 2:
            referrals_needed.append({
                'type': 'Psychiatric Consultation',
                'reason': 'Multiple severe patterns (9+/10) may indicate underlying condition',
                'urgency': 'MODERATE',
                'action': 'Consider consultation to rule out comorbid conditions'
            })
        
        if not referrals_needed:
            return ""
        
        referrals_html = ""
        for referral in referrals_needed:
            urgency_color = "#ef4444" if referral['urgency'] == 'URGENT' else "#eab308" if referral['urgency'] == 'HIGH' else "#4CA1A3"
            referrals_html += f"""
                <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 4px solid {urgency_color};">
                    <strong style="color: {urgency_color};">{referral['type']} ({referral['urgency']})</strong><br>
                    <strong>Reason:</strong> {referral['reason']}<br>
                    <strong>Action:</strong> {referral['action']}
                </div>
            """
        
        return f"""
            <div class="section">
                <div class="referral-box">
                    <h3>🏥 Referral recommendations</h3>
                    <p><strong>The following referrals are recommended before or concurrent with hypnotherapy:</strong></p>
                    {referrals_html}
                </div>
            </div>
        """
    
    def _generate_outcome_tracking_template(
        self,
        client_name: str,
        dominant_pattern: Dict
    ) -> str:
        """Generate outcome tracking template for evidence-based practice"""
        
        if not dominant_pattern:
            return ""
        
        pattern_name = dominant_pattern.get('name', 'Unknown').title()
        pattern_score = dominant_pattern.get('score', 0)
        
        return f"""
            <div class="section">
                <div class="outcome-tracking">
                    <h3>📊 Outcome tracking template</h3>
                    <p>For evidence-based practice and quality improvement, track the following:</p>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong>Client:</strong> {client_name}<br>
                        <strong>Primary Pattern:</strong> {pattern_name} (Baseline: {pattern_score:.1f}/10)<br>
                        <strong>Assessment Date:</strong> {datetime.now().strftime('%Y-%m-%d')}
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong>Recommended Tracking Schedule:</strong>
                        <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li><strong>Post-Session 1:</strong> Initial pattern shift assessment</li>
                            <li><strong>Post-Session 2:</strong> Core transformation measurement</li>
                            <li><strong>1-month follow-up:</strong> Pattern stability check</li>
                            <li><strong>6-month follow-up:</strong> Long-term maintenance assessment</li>
                        </ul>
                    </div>
                    
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <strong>Key Metrics to Track:</strong>
                        <ol style="margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li>{pattern_name} pattern intensity (0-10 scale)</li>
                            <li>Trigger charge reduction (percentage)</li>
                            <li>Functional impact (life areas improved)</li>
                            <li>Client satisfaction (0-10 scale)</li>
                            <li>Session count used (2 vs 3)</li>
                        </ol>
                    </div>
                </div>
            </div>
        """
    
    def _generate_response_transcript(self, responses: Dict[int, Any]) -> str:
        """Generate complete response transcript"""
        
        try:
            from utils.config_assess import COMPLETE_QUESTION_SET
        except ImportError:
            return "<div class='section'><p>Response transcript unavailable</p></div>"
        
        items = []
        for q_id in sorted(responses.keys()):
            # Find question text
            q_text = "Question not found"
            for q in COMPLETE_QUESTION_SET:
                if q['id'] == q_id:
                    q_text = q['text']
                    break
            
            # Format response
            response = responses[q_id]
            if isinstance(response, (list, tuple)):
                response_text = ", ".join(str(r) for r in response)
            else:
                response_text = str(response)
            
            # Truncate very long responses for email
            if len(response_text) > 500:
                response_text = response_text[:500] + "... [truncated]"
            
            items.append(f"""
                <div style="background: #f8fafc; padding: 1rem; margin: 0.5rem 0; border-left: 4px solid #cbd5e1; border-radius: 6px;">
                    <strong style="color: #4CA1A3;">Q{q_id}:</strong> {q_text}<br>
                    <strong>Response:</strong> {response_text}
                </div>
            """)
        
        return f"""
            <div class="section">
                <h2>Complete response transcript</h2>
                <p><strong>Total questions answered:</strong> {len(responses)}/97</p>
                {"".join(items)}
            </div>
        """


# ============================================================================
# GLOBAL INSTANCE & PUBLIC FUNCTION
# ============================================================================

_email_handler = ClinicalAssessmentEmailHandler()

def send_assessment_email(email_data: Dict[str, Any]) -> bool:
    """
    Send clinical assessment email with comprehensive protocols
    
    Args:
        email_data: Dictionary containing:
            - contact: Client contact information
            - analysis: Complete analytics results
            - responses: Raw assessment responses
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    return _email_handler.send_assessment_email(email_data)


# ============================================================================
# CONFIGURATION VALIDATION
# ============================================================================

def validate_email_configuration() -> Dict[str, Any]:
    """
    Validate email configuration and return status
    
    Returns:
        Dictionary with configuration status
    """
    handler = ClinicalAssessmentEmailHandler()
    
    return {
        'configured': bool(handler.password),
        'sender_email': handler.sender_email,
        'recipient_email': handler.recipient_email,
        'smtp_server': handler.smtp_server,
        'smtp_port': handler.smtp_port
    }
