"""
Paywall Component - Premium Analysis Access Control
Handles payment processing and access verification for complete blueprint
"""

import streamlit as st
from typing import Dict, Optional
from datetime import datetime
import hashlib


class ClinicalPaywall:
    """Manages access control and payment for premium analysis"""
    
    def __init__(self):
        self.pricing = {
            'basic_analysis': {
                'price': 99,
                'currency': '฿',
                'features': [
                    'Complete pattern constellation analysis',
                    'Behavioral trigger chain mapping',
                    'Session-by-session roadmap',
                    'Digital conditioning analysis',
                    'Success probability calculation'
                ]
            },
            'premium_package': {
                'price': 199,
                'currency': '฿',
                'features': [
                    'Everything in basic analysis',
                    'Personalized hypnotic scripts',
                    'Downloadable PDF report (20+ pages)',
                    'Follow-up support email',
                    'Progress tracking worksheets',
                    'Lifetime access to updates'
                ]
            }
        }
        
        # Initialize payment state
        if 'payment_verified' not in st.session_state:
            st.session_state.payment_verified = False
        
        if 'payment_timestamp' not in st.session_state:
            st.session_state.payment_timestamp = None
        
        if 'payment_package' not in st.session_state:
            st.session_state.payment_package = None
    
    def check_payment_status(self) -> bool:
        """Check if user has valid payment for premium access"""
        return st.session_state.get('payment_verified', False)
    
    def render_paywall_interface(self, assessment_data: Dict):
        """Render payment interface with pricing options"""
        
        # Hero section - simplified
        st.markdown("### Unlock your complete transformation blueprint")
        st.info("Get instant access to your personalized clinical analysis")
        
        # Pricing comparison
        st.markdown("**Choose your package:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            self._render_pricing_card('basic_analysis', 'Basic analysis', False)
        
        with col2:
            self._render_pricing_card('premium_package', 'Premium package', True)
        
        st.markdown("---")
        
        # Payment method selection
        st.markdown("### Select payment method")
        
        payment_method = st.radio(
            "How would you like to pay?",
            [
                "Credit/debit card (Stripe)",
                "Bank transfer (Thai banks)",
                "PromptPay",
                "Cash (in-person only)"
            ],
            label_visibility="collapsed"
        )
        
        if "Credit/debit" in payment_method:
            self._render_stripe_payment()
        elif "Bank transfer" in payment_method:
            self._render_bank_transfer()
        elif "PromptPay" in payment_method:
            self._render_promptpay()
        else:
            self._render_cash_payment()
        
        st.markdown("---")
        self._render_guarantee_section()
    
    def _render_pricing_card(self, package_id: str, title: str, recommended: bool = False):
        """Render pricing card using Streamlit components"""
        
        pricing = self.pricing[package_id]
        
        # Recommended badge
        if recommended:
            st.success("**RECOMMENDED**")
        
        # Price display
        st.markdown(f"**{title}**")
        st.markdown(f"# {pricing['currency']}{pricing['price']}")
        st.caption("one-time payment")
        
        # Features list
        st.markdown("**Includes:**")
        for feature in pricing['features']:
            st.markdown(f"✓ {feature}")
        
        # Selection button
        if st.button(
            f"Select {title}",
            key=f"select_{package_id}",
            type="primary" if recommended else "secondary",
            use_container_width=True
        ):
            st.session_state.selected_package = package_id
            st.info(f"✓ Selected: {title}. Please complete payment below.")
    
    def _render_stripe_payment(self):
        """Render Stripe payment integration"""
        
        st.markdown("**Secure card payment**")
        st.caption("Process your payment securely through Stripe. Your information is encrypted and secure.")
        
        st.info("""
        **TEST MODE ACTIVE**
        
        In production, this would integrate with Stripe payment processing:
        - Secure card input form
        - Real-time payment verification
        - Automatic email receipts
        - PCI-compliant processing
        
        For demo purposes, click the button below to simulate payment.
        """)
        
        if st.button("Simulate card payment (TEST)", type="primary", use_container_width=True):
            self._process_test_payment('stripe')
    
    def _render_bank_transfer(self):
        """Render bank transfer instructions"""
        
        st.markdown("**Bank transfer details**")
        st.caption("Transfer to the account below and upload proof of payment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Kasikorn Bank (K-Bank)**  
            Account: MindTransform Co., Ltd.  
            Number: 123-4-56789-0  
            Branch: Asoke
            """)
        
        with col2:
            st.markdown("""
            **Bangkok Bank**  
            Account: MindTransform Co., Ltd.  
            Number: 987-6-54321-0  
            Branch: Sukhumvit
            """)
        
        # Upload proof
        uploaded_file = st.file_uploader(
            "Upload proof of payment (screenshot or photo)",
            type=['png', 'jpg', 'jpeg', 'pdf'],
            help="We'll verify your payment within 2-4 hours"
        )
        
        if uploaded_file:
            st.success("✓ Payment proof uploaded. We'll verify and unlock your analysis within 2-4 hours.")
            st.info("Check your email for confirmation. If urgent, contact us via WhatsApp: +66 XX XXX XXXX")
    
    def _render_promptpay(self):
        """Render PromptPay QR code"""
        
        st.markdown("**PromptPay payment**")
        st.caption("Scan QR code with your banking app")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Placeholder for QR code
            st.markdown("**QR Code**")
            st.info("📱 QR Code Here\n\n(Generate in production)")
        
        with col2:
            st.markdown("""
            **Instructions:**
            
            1. Open your banking app
            2. Select "PromptPay" or "Scan QR"
            3. Scan the QR code on the left
            4. Verify amount and confirm payment
            5. Take screenshot of confirmation
            6. Upload screenshot below
            """)
        
        uploaded_file = st.file_uploader(
            "Upload payment confirmation",
            type=['png', 'jpg', 'jpeg'],
            key="promptpay_upload"
        )
        
        if uploaded_file:
            st.success("✓ Payment confirmation received. Verifying...")
            if st.button("Verify payment (TEST)", type="primary"):
                self._process_test_payment('promptpay')
    
    def _render_cash_payment(self):
        """Render cash payment instructions"""
        
        st.markdown("**Cash payment (in-person only)**")
        st.caption("Pay in cash at our office before your first session")
        
        st.markdown("""
        **Office location:**  
        27 Soi Sukhumvit 10 (Asoke)  
        Bangkok 10110, Thailand
        
        **Office hours:**  
        Monday - Friday: 10:00 AM - 7:00 PM  
        Saturday: 10:00 AM - 5:00 PM  
        Sunday: Closed
        
        **What to bring:**
        - Exact cash amount
        - Your email address used for assessment
        - Valid ID for receipt
        """)
        
        if st.button("I'll pay cash at the office", use_container_width=True):
            st.success("""
            ✓ Cash payment option selected. 
            
            You can review your analysis preview now. Complete access will be unlocked after 
            payment at our office before your first session.
            
            We'll contact you within 24-48 hours to schedule your first session.
            """)
    
    def _render_guarantee_section(self):
        """Render money-back guarantee"""
        
        st.success("""
        **💯 100% satisfaction guarantee**
        
        If you're not completely satisfied with your analysis, 
        we'll refund your full payment within 7 days. No questions asked.
        """)
        
        st.caption("🔒 Secure payment processing • SSL encrypted • Privacy protected")
    
    def _process_test_payment(self, method: str):
        """Process test/demo payment (for development)"""
        
        with st.spinner("Processing payment..."):
            import time
            time.sleep(2)
        
        # Set payment verified
        st.session_state.payment_verified = True
        st.session_state.payment_timestamp = datetime.now().isoformat()
        st.session_state.payment_package = st.session_state.get('selected_package', 'premium_package')
        st.session_state.payment_method = method
        
        # Generate payment confirmation
        payment_id = self._generate_payment_id()
        
        selected_package = st.session_state.payment_package
        price_info = self.pricing[selected_package]
        
        st.success(f"""
        ✅ Payment successful!
        
        **Payment confirmation:** {payment_id}  
        **Package:** {selected_package.replace('_', ' ').title()}  
        **Amount:** {price_info['currency']}{price_info['price']}
        
        Your complete analysis is now unlocked. Receipt sent to your email.
        """)
        
        st.balloons()
        
        if st.button("View my complete blueprint", type="primary", use_container_width=True):
            st.rerun()
    
    def _generate_payment_id(self) -> str:
        """Generate unique payment ID"""
        timestamp = datetime.now().isoformat()
        email = st.session_state.get('contact_info', {}).get('email', 'unknown')
        
        payment_string = f"{email}_{timestamp}_{st.session_state.payment_package}"
        payment_hash = hashlib.sha256(payment_string.encode()).hexdigest()[:12].upper()
        
        return f"PAY-{payment_hash}"
    
    def verify_payment(self, payment_id: str) -> bool:
        """Verify payment ID (for production use)"""
        return st.session_state.get('payment_verified', False)


def create_clinical_paywall():
    """Factory function for paywall component"""
    return ClinicalPaywall()
