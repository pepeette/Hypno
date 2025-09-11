"""
Paywall component for Clinical Analysis feature
Integrates with Stripe for payment processing and email delivery
"""
import streamlit as st
import hashlib
import time
from datetime import datetime, timedelta
import json

class ClinicalAnalysisPaywall:
    """Paywall for premium clinical analysis feature"""
    
    def __init__(self):
        # Pricing configuration
        self.analysis_price = 1000  # THB
        self.currency = "thb"
        
        # Session state keys
        self.payment_status_key = "clinical_analysis_paid"
        self.payment_session_key = "payment_session_id"
        self.analysis_access_key = "analysis_access_token"
        
        # Mock Stripe configuration (replace with real keys in production)
        self.stripe_public_key = "pk_test_..."  # Replace with real Stripe public key
        self.stripe_secret_key = st.secrets.get("STRIPE_SECRET_KEY", "sk_test_...")
        
        # Initialize session state
        self._init_session_state()
    
    def _init_session_state(self):
        """Initialize payment-related session state"""
        if self.payment_status_key not in st.session_state:
            st.session_state[self.payment_status_key] = False
        if self.payment_session_key not in st.session_state:
            st.session_state[self.payment_session_key] = None
        if self.analysis_access_key not in st.session_state:
            st.session_state[self.analysis_access_key] = None
    
    def check_payment_status(self, assessment_id=None):
        """Check if user has paid for clinical analysis"""
        # Check session state first
        if st.session_state.get(self.payment_status_key, False):
            return True
        
        # Check if there's a valid access token
        access_token = st.session_state.get(self.analysis_access_key)
        if access_token and self._validate_access_token(access_token, assessment_id):
            st.session_state[self.payment_status_key] = True
            return True
        
        return False
    
    def render_paywall_interface(self, assessment_data):
        """Render the paywall interface for clinical analysis"""
        st.markdown("### 🔒 Premium behavioral analysis")
        
        # Show what's included
        self._render_premium_features()
        
        # Payment options
        self._render_payment_options(assessment_data)
        
        # Alternative access
        self._render_access_token_input()
    
    def _render_premium_features(self):
        """Show what the premium analysis includes"""
        st.markdown("""
        **Unlock your complete behavioral pattern analysis:**
        
        ✨ **Detailed pattern breakdown** - See exactly which of the 9 core patterns are most active in your life
        
        🎯 **Therapeutic priorities** - Ranked list of which patterns to address first for maximum impact
        
        🧠 **Clinical insights** - Professional interpretation of your responses with psychological context
        
        📋 **Session planning** - Specific recommendations for how to structure your hypnotherapy sessions
        
        💬 **Personalized approach** - Communication and learning style adaptations for your sessions
        """)
        
        # Pricing
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4CA1A3 0%, #E1F0F0 100%); 
                    border-radius: 12px; padding: 2rem; text-align: center; margin: 1rem 0;">
            <h3 style="color: white; margin-bottom: 1rem;">Complete Analysis Report</h3>
            <div style="color: white; font-size: 2rem; font-weight: bold; margin: 1rem 0;">
                ฿{self.analysis_price}
            </div>
            <p style="color: white; opacity: 0.9; margin: 0;">
                One-time payment • Instant access • Delivered via email
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_payment_options(self, assessment_data):
        """Render payment options"""
        st.markdown("### Payment Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💳 Pay with Card (Stripe)", type="primary", use_container_width=True):
                self._initiate_stripe_payment(assessment_data)
        
        with col2:
            if st.button("🏦 Bank Transfer", use_container_width=True):
                self._show_bank_transfer_info(assessment_data)
    
    def _render_access_token_input(self):
        """Render access token input for users who already paid"""
        with st.expander("Already paid? Enter your access code"):
            access_code = st.text_input(
                "Access Code", 
                placeholder="Enter the code from your payment confirmation email",
                key="access_code_input"
            )
            
            if st.button("Unlock Analysis"):
                if self._validate_access_code(access_code):
                    st.session_state[self.payment_status_key] = True
                    st.session_state[self.analysis_access_key] = access_code
                    st.success("✅ Access granted! Reloading analysis...")
                    st.rerun()
                else:
                    st.error("❌ Invalid access code. Please check your email or contact support.")
    
    def _initiate_stripe_payment(self, assessment_data):
        """Initiate Stripe payment process"""
        try:
            # In a real implementation, you would:
            # 1. Create a Stripe checkout session
            # 2. Redirect user to Stripe's hosted checkout
            # 3. Handle webhook for payment completion
            
            # For demo purposes, we'll show the payment flow
            st.info("""
            **Stripe Payment Integration**
            
            In production, this would:
            1. Create a Stripe checkout session
            2. Redirect to secure payment page
            3. Process payment and send analysis via email
            4. Provide access code for immediate viewing
            
            For testing, use the demo button below.
            """)
            
            # Demo payment simulation
            if st.button("🔧 Simulate Payment (Demo)", key="demo_payment"):
                self._simulate_payment_success(assessment_data)
        
        except Exception as e:
            st.error(f"Payment initialization failed: {str(e)}")
    
    def _show_bank_transfer_info(self, assessment_data):
        """Show bank transfer information"""
        # Generate unique reference
        reference = self._generate_payment_reference(assessment_data)
        
        st.info(f"""
        **Bank Transfer Details**
        
        **Account Name:** Bangkok Hypnotherapy Clinic  
        **Bank:** KrungSri Bank  
        **Account Number:** 119674532 
        **Amount:** ฿{self.analysis_price}  
        **Reference:** {reference}
        
        **Important:** Include the reference number in your transfer description.
        
        After transfer, send proof of payment to: laetitiasheppard@gmail.com
        You'll receive your analysis within 2 hours of payment confirmation.
        """)
        
        # Store reference for tracking
        st.session_state[f"transfer_ref_{reference}"] = {
            'assessment_data': assessment_data,
            'timestamp': datetime.now().isoformat(),
            'amount': self.analysis_price
        }
    
    def _simulate_payment_success(self, assessment_data):
        """Simulate successful payment for demo purposes"""
        # Generate access token
        access_token = self._generate_access_token(assessment_data)
        
        # Update session state
        st.session_state[self.payment_status_key] = True
        st.session_state[self.analysis_access_key] = access_token
        
        # Send analysis email
        self._send_premium_analysis_email(assessment_data, access_token)
        
        st.success(f"""
        ✅ Payment successful! 
        
        Your clinical analysis has been sent to your email.
        Access code: `{access_token}`
        
        The page will reload to show your premium analysis.
        """)
        
        # Auto-reload after 3 seconds
        time.sleep(3)
        st.rerun()
    
    def _generate_payment_reference(self, assessment_data):
        """Generate unique payment reference"""
        email = assessment_data.get('email', 'unknown')
        timestamp = str(int(time.time()))
        combined = f"{email}_{timestamp}"
        return hashlib.md5(combined.encode()).hexdigest()[:8].upper()
    
    def _generate_access_token(self, assessment_data):
        """Generate access token for paid analysis"""
        email = assessment_data.get('email', 'unknown')
        timestamp = str(int(time.time()))
        combined = f"CLINICAL_{email}_{timestamp}"
        return hashlib.sha256(combined.encode()).hexdigest()[:16].upper()
    
    def _validate_access_token(self, token, assessment_id=None):
        """Validate access token"""
        # In production, you'd check against a database
        # For demo, accept any 16-character uppercase token
        return len(token) == 16 and token.isupper() and token.isalnum()
    
    def _validate_access_code(self, code):
        """Validate access code entered by user"""
        return self._validate_access_token(code)
    
    def _send_premium_analysis_email(self, assessment_data, access_token):
        """Send premium analysis via email"""
        try:
            from utils.email_handler import send_assessment_results_email
            
            # Add premium analysis data
            premium_data = assessment_data.copy()
            premium_data['is_premium'] = True
            premium_data['access_token'] = access_token
            premium_data['analysis_type'] = 'Premium Clinical Analysis'
            premium_data['payment_amount'] = self.analysis_price
            premium_data['payment_timestamp'] = datetime.now().isoformat()
            
            # Send enhanced email
            success = send_assessment_results_email(premium_data)
            
            if success:
                st.success("📧 Premium analysis sent to your email!")
            else:
                st.warning("⚠️ Payment processed, but email delivery failed. Contact support with your access code.")
                
        except Exception as e:
            st.error(f"Error sending premium analysis: {str(e)}")
    
    def render_premium_analysis(self, assessment_data):
        """Render the premium clinical analysis content"""
        if not self.check_payment_status():
            st.error("Access denied. Please complete payment first.")
            return
        
        st.success("Premium Clinical Analysis Unlocked")
        
        # Extract analysis results safely
        assessment_results = assessment_data.get('assessment_results', {})
        if not assessment_results:
            st.error("No assessment results found. Please complete the assessment first.")
            return
            
        pattern_scores = assessment_results.get('pattern_scores', {})
        clinical_insights = assessment_results.get('clinical_insights', {})
        
        # Pattern definitions
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
        
        # Detailed pattern analysis
        st.markdown("### 🎯 Your Primary Behavioral Patterns")
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            for i, (pattern_id, score) in enumerate(sorted_patterns[:5]):
                pattern_name = pattern_names.get(pattern_id, f"Pattern {pattern_id}")
                activation_level = "High" if score >= 8 else "Medium" if score >= 4 else "Low"
                
                # Color coding for activation levels
                color = "#dc2626" if activation_level == "High" else "#ea580c" if activation_level == "Medium" else "#65a30d"
                
                st.markdown(f"""
                <div style="background: white; border-left: 4px solid {color}; 
                            padding: 1rem; margin: 1rem 0; border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h4 style="color: {color}; margin-bottom: 0.5rem;">
                        #{i+1}: {pattern_name}
                    </h4>
                    <p><strong>Activation Level:</strong> {activation_level} (Score: {score})</p>
                    <p><strong>Therapeutic Priority:</strong> {'Immediate attention needed' if activation_level == 'High' else 'Address in session 2-3' if activation_level == 'Medium' else 'Monitor and maintain'}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Clinical insights
        if clinical_insights:
            st.markdown("### 🔍 Clinical insights")
            
            priority_insights = [
                ('limiting_belief', 'Core limiting belief'),
                ('change_fear', 'Primary change fear'),
                ('secondary_gain', 'Hidden benefits'),
                ('family_origin', 'Family origin pattern')
            ]
            
            for insight_key, insight_label in priority_insights:
                if insight_key in clinical_insights:
                    value = clinical_insights[insight_key]
                    if isinstance(value, str) and value.strip():
                        st.markdown(f"""
                        <div style="background: #f8fafc; padding: 1rem; margin: 0.5rem 0; 
                                    border-radius: 8px; border: 1px solid #e2e8f0;">
                            <strong style="color: #4CA1A3;">{insight_label}:</strong><br>
                            {value}
                        </div>
                        """, unsafe_allow_html=True)
        
        # Session recommendations
        st.markdown("### 📋 Personalized session plan")
        
        if pattern_scores:
            sorted_patterns = sorted(pattern_scores.items(), key=lambda x: x[1], reverse=True)
            
            if len(sorted_patterns) >= 2:
                primary_pattern = pattern_names.get(sorted_patterns[0][0], "Primary Pattern")
                secondary_pattern = pattern_names.get(sorted_patterns[1][0], "Secondary Pattern")
                
                st.markdown(f"""
                **Session 1: Pattern mapping & initial programming**
                - Primary focus: {primary_pattern}
                - Secondary assessment: {secondary_pattern}
                - Initial positive programming to provide immediate relief
                
                **Session 2: Deep neural rewiring**
                - Target {primary_pattern} for complete transformation
                - Install new automatic responses
                - Create positive anchors for lasting change
                
                **Session 3: Reinforcement (if needed)**
                - Strengthen any remaining weak spots
                - Address unexpected triggers
                - Ensure complete integration
                """)
        
        # Download option
        if st.button("📄 Download full analysis report", use_container_width=True):
            self._generate_downloadable_report(assessment_data)
    
    def _generate_downloadable_report(self, assessment_data):
        """Generate downloadable PDF report"""
        st.info("📄 Report generation feature coming soon. Your complete analysis is available in the email sent to you.")


# Factory function
def create_clinical_paywall():
    """Factory function to create paywall instance"""
    return ClinicalAnalysisPaywall()
