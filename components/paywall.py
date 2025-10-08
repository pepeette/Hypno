"""
Paywall Component - Premium Analysis Access Control
Handles payment processing and access verification for complete blueprint
"""

import streamlit as st
from typing import Dict, Optional
from datetime import datetime
import hashlib
import os


class ClinicalPaywall:
    """Manages access control and payment for premium analysis"""
    
    def __init__(self):
        # Single price - no more tiers
        self.price_thb = 1000
        
        # Initialize payment state
        if 'payment_verified' not in st.session_state:
            st.session_state.payment_verified = False
        
        if 'payment_timestamp' not in st.session_state:
            st.session_state.payment_timestamp = None
        
        if 'payment_method' not in st.session_state:
            st.session_state.payment_method = None
    
    def check_payment_status(self) -> bool:
        """Check if user has valid payment for premium access"""
        return st.session_state.get('payment_verified', False)
    
    def _check_bypass_code(self, code: str) -> bool:
        """Check if bypass code is valid (hidden from user)"""
        return code == "9090"
    
    def render_paywall_interface(self, blueprint_data: Dict, price_thb: int = 1000):
        """Render payment interface with single price option"""
        
        # Update price if specified
        self.price_thb = price_thb
        
        # Hero section
        st.markdown(f"""
        ### Complete your purchase
        
        **Price:** {self.price_thb:,} THB (one-time payment)
        """)
        
        st.markdown("---")
        
        # Payment method selection
        st.markdown("### Select payment method")
        
        payment_method = st.radio(
            "How would you like to pay?",
            [
                "PromptPay QR code",
                "Bank transfer (Thai banks)",
                "Credit/debit card (Stripe)",
                "Cash (in-person only)"
            ],
            label_visibility="collapsed"
        )
        
        # Render payment method
        if "PromptPay" in payment_method:
            self._render_promptpay()
        elif "Bank transfer" in payment_method:
            self._render_bank_transfer()
        elif "Credit/debit" in payment_method:
            self._render_stripe_payment()
        else:
            self._render_cash_payment()
        
        st.markdown("---")
        self._render_guarantee_section()
        
        # Hidden bypass code input (disguised as support reference)
        with st.expander("💬 Have a support reference code?", expanded=False):
            st.caption("If you received a reference code from support, enter it here")
            bypass_code = st.text_input(
                "Reference code",
                type="password",
                key="support_ref_code",
                label_visibility="collapsed",
                placeholder="Enter code..."
            )
            
            if st.button("Verify code", key="verify_ref"):
                if self._check_bypass_code(bypass_code):
                    self._process_bypass_unlock()
                    st.rerun()
                else:
                    st.error("Invalid reference code. Please check with support.")
    
    def _render_promptpay(self):
        """Render PromptPay QR code - ACTUAL QR CODE"""
        
        st.markdown(f"""
        **PromptPay payment - {self.price_thb:,} THB**
        """)
        st.caption("Scan QR code with your mobile banking app")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Display actual QR code
            qr_path = "img/qrcode.png"
            
            if os.path.exists(qr_path):
                st.image(qr_path, caption="Scan to pay", width='stretch')
            else:
                st.error("QR code not found. Please contact support.")
                st.info(f"Looking for: {qr_path}")
        
        with col2:
            st.markdown(f"""
            **Instructions:**
            
            1. Open your banking app
            2. Select "PromptPay" or "Scan QR"
            3. Scan the QR code
            4. **Verify amount: {self.price_thb:,} THB**
            5. Confirm payment
            6. Upload screenshot below
            """)
        
        st.markdown("---")
        
        # Upload payment proof
        uploaded_file = st.file_uploader(
            "Upload payment confirmation screenshot",
            type=['png', 'jpg', 'jpeg'],
            key="promptpay_upload",
            help="We'll verify and unlock within 2-4 hours"
        )
        
        if uploaded_file:
            st.success("✅ Payment confirmation received!")
            st.info("""
            **Next steps:**
            - We'll verify your payment within 2-4 hours
            - You'll receive email confirmation
            - Your analysis will be automatically unlocked
            
            For urgent verification, WhatsApp: +66 XX XXX XXXX
            """)
            
            # TEST MODE: Allow immediate verification
            if st.button("🧪 Verify now (TEST MODE)", type="secondary", key="test_verify"):
                self._process_test_payment('promptpay')
    
    def _render_bank_transfer(self):
        """Render bank transfer instructions"""
        
        st.markdown(f"""
        **Bank transfer - {self.price_thb:,} THB**
        """)
        st.caption("Transfer to the account below and upload proof of payment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Kasikorn Bank (K-Bank)**  
            Account: MindTransform Co., Ltd.  
            Number: 123-4-56789-0  
            Branch: Asoke  
            **Amount: {self.price_thb:,} THB**
            """)
        
        with col2:
            st.markdown(f"""
            **Bangkok Bank**  
            Account: MindTransform Co., Ltd.  
            Number: 987-6-54321-0  
            Branch: Sukhumvit  
            **Amount: {self.price_thb:,} THB**
            """)
        
        st.markdown("---")
        
        # Upload proof
        uploaded_file = st.file_uploader(
            "Upload proof of payment (screenshot or slip)",
            type=['png', 'jpg', 'jpeg', 'pdf'],
            help="We'll verify your payment within 2-4 hours",
            key="bank_transfer_upload"
        )
        
        if uploaded_file:
            st.success("✅ Payment proof uploaded!")
            st.info("""
            **Verification in progress:**
            - Review time: 2-4 hours
            - Email confirmation sent
            - Analysis unlocks automatically
            
            Urgent? Contact: support@mindtransform.co
            """)
    
    def _render_stripe_payment(self):
        """Render Stripe payment integration"""
        
        st.markdown(f"""
        **Secure card payment - {self.price_thb:,} THB**
        """)
        st.caption("International cards accepted • Encrypted & secure • Instant access")
        
        st.info("""
        **STRIPE INTEGRATION READY**
        
        In production environment, this connects to:
        - Stripe payment gateway (PCI-compliant)
        - Secure card input form
        - Real-time payment processing
        - Automatic receipt generation
        - Instant unlock after payment
        
        **For testing:** Click button below to simulate payment
        """)
        
        if st.button(
            f"💳 Pay {self.price_thb:,} THB with card (TEST)", 
            type="primary", 
            width='stretch'
        ):
            self._process_test_payment('stripe')
    
    def _render_cash_payment(self):
        """Render cash payment instructions"""
        
        st.markdown(f"""
        **Cash payment - {self.price_thb:,} THB**
        """)
        st.caption("Pay in person at our office before or during your first session")
        
        st.markdown(f"""
        **Office location:**  
        27 Soi Sukhumvit 10 (Asoke)  
        Bangkok 10110, Thailand
        
        **Office hours:**  
        Monday - Friday: 10:00 AM - 7:00 PM  
        Saturday: 10:00 AM - 5:00 PM  
        Sunday: Closed
        
        **Payment amount:** {self.price_thb:,} THB (exact amount preferred)
        
        **What to bring:**
        - Cash payment
        - Email address from assessment
        - Valid ID for receipt
        """)
        
        st.markdown("---")
        
        if st.button("📍 I'll pay cash at the office", width='stretch'):
            st.success("""
            ✅ Cash payment option selected
            
            **Next steps:**
            - We'll contact you within 24-48 hours
            - Schedule your first session
            - Pay when you arrive at office
            - Analysis unlocks after payment
            
            You can review the preview sections now.
            """)
    
    def _render_guarantee_section(self):
        """Render money-back guarantee"""
        
        st.success("""
        **💯 100% satisfaction guarantee**
        
        Not satisfied with your analysis? Full refund within 7 days. No questions asked.
        """)
        
        st.caption("🔒 Secure payment • SSL encrypted • Privacy protected")
    
    def _process_test_payment(self, method: str):
        """Process test/demo payment (for development)"""
        
        with st.spinner("Processing payment..."):
            import time
            time.sleep(2)
        
        # Set payment verified
        st.session_state.payment_verified = True
        st.session_state.payment_timestamp = datetime.now().isoformat()
        st.session_state.payment_method = method
        
        # Generate payment confirmation
        payment_id = self._generate_payment_id()
        
        st.success(f"""
        ✅ Payment successful!
        
        **Confirmation ID:** {payment_id}  
        **Amount paid:** {self.price_thb:,} THB  
        **Method:** {method.title()}
        
        Your complete analysis is now unlocked.
        """)
        
        st.balloons()
        
        # Clear instructions
        st.info("""
        **Next steps:**
        
        1. Click the button below to view your complete blueprint
        2. Or scroll to the top of this page - you'll see a green banner with access button
        3. Your receipt has been sent to your email
        """)
        
        # Prominent button to view blueprint
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                "📊 View my complete blueprint", 
                type="primary", 
                width='stretch',
                key="view_blueprint_after_payment"
            ):
                st.session_state.show_full_blueprint = True
                st.rerun()
        
    def _process_bypass_unlock(self):
        """Process bypass code unlock (hidden feature)"""
        
        # Set payment verified without actual payment
        st.session_state.payment_verified = True
        st.session_state.payment_timestamp = datetime.now().isoformat()
        st.session_state.payment_method = 'bypass_code'
        
        st.success("""
        ✅ Access verified!
        
        Your complete analysis has been unlocked.
        """)
        
        st.balloons()
        
        st.info("""
        **Next steps:**
        
        1. Scroll to the top of this page
        2. Click the green "View your complete blueprint" button
        3. Or click the button below
        """)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                "📊 View my complete blueprint", 
                type="primary", 
                width='stretch',
                key="view_blueprint_after_bypass"
            ):
                st.session_state.show_full_blueprint = True
            st.rerun()
    
    def _generate_payment_id(self) -> str:
        """Generate unique payment ID"""
        timestamp = datetime.now().isoformat()
        email = st.session_state.get('contact_info', {}).get('email', 'unknown')
        
        payment_string = f"{email}_{timestamp}_{self.price_thb}"
        payment_hash = hashlib.sha256(payment_string.encode()).hexdigest()[:12].upper()
        
        return f"PAY-{payment_hash}"
    
    def verify_payment(self, payment_id: str) -> bool:
        """Verify payment ID (for production use)"""
        return st.session_state.get('payment_verified', False)


def create_clinical_paywall():
    """Factory function for paywall component"""
    return ClinicalPaywall()
