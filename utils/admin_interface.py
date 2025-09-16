"""
Create admin_interface.py for manual email processing:
"""

# utils/admin_production.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.storage_factory import create_storage_client

class ProductionAdminInterface:
    """Production admin dashboard"""
    
    def __init__(self):
        self.storage = create_storage_client()
    
    def render_dashboard(self):
        """Render complete admin dashboard"""
        if not self._authenticate():
            return
        
        st.title("🔧 Clinical Admin Dashboard")
        
        # Tabs for different admin functions
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Analytics", 
            "📧 Email Queue", 
            "💳 Payments", 
            "⚙️ System"
        ])
        
        with tab1:
            self._render_analytics()
        
        with tab2:
            self._render_email_management()
        
        with tab3:
            self._render_payment_management()
        
        with tab4:
            self._render_system_management()
    
    def _authenticate(self):
        """Admin authentication"""
        if st.session_state.get('admin_authenticated'):
            return True
        
        with st.sidebar:
            st.markdown("### 🔐 Admin Login")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                if password == st.secrets["admin"]["password"]:
                    st.session_state.admin_authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid password")
        
        return False
    
    def _render_analytics(self):
        """Render analytics dashboard"""
        st.markdown("### Assessment Analytics")
        
        # Get assessment data
        assessments = self._get_recent_assessments()
        
        if assessments:
            # Convert to DataFrame for analysis
            df = pd.DataFrame(assessments)
            
            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Assessments", len(df))
            
            with col2:
                completed = len(df[df['completion_rate'] >= 0.8])
                st.metric("Completed", completed)
            
            with col3:
                digital_natives = len(df[df['is_digital_native'] == True])
                st.metric("Digital Natives", digital_natives)
            
            with col4:
                avg_patterns = df['pattern_count'].mean()
                st.metric("Avg Patterns", f"{avg_patterns:.1f}")
            
            # Recent assessments table
            st.markdown("### Recent Assessments")
            display_df = df[['timestamp', 'email', 'urgency', 'pattern_count', 'completion_rate']].copy()
            st.dataframe(display_df, use_container_width=True)
            
        else:
            st.info("No assessment data available")
    
    def _render_payment_management(self):
        """Render payment management"""
        st.markdown("### Payment Management")
        
        # Payment records
        payments = self._get_payment_records()
        
        if payments:
            for payment in payments[-10:]:  # Show last 10
                with st.expander(f"Payment: {payment['customer_email']} - ฿{payment['amount']/100}"):
                    st.json(payment)
        else:
            st.info("No payment records found")

def render_admin_interface():
    """Admin interface for processing email requests and viewing analytics"""
    
    if st.sidebar.button("🔐 Admin Login"):
        admin_password = st.text_input("Admin Password", type="password")
        
        if admin_password == st.secrets.get("admin", {}).get("password", "admin123"):
            st.session_state.admin_authenticated = True
            st.rerun()
    
    if st.session_state.get('admin_authenticated', False):
        st.sidebar.success("✅ Admin Access")
        
        tab1, tab2, tab3 = st.tabs(["📧 Email Queue", "📊 Analytics", "💾 Storage"])
        
        with tab1:
            st.markdown("### Pending Email Requests")
            
            from utils.email_blueprint_streamlit import get_pending_email_requests, clear_email_requests
            
            email_requests = get_pending_email_requests()
            
            if email_requests:
                for i, request in enumerate(email_requests):
                    with st.expander(f"Email {i+1}: {request['recipient']} - {request['assessment_summary']['urgency']}"):
                        st.json(request)
                        
                        if st.button(f"Mark as processed {i+1}", key=f"process_{i}"):
                            # Remove this request
                            email_requests.pop(i)
                            st.success("Request marked as processed")
                            st.rerun()
                
                if st.button("Clear All Processed"):
                    clear_email_requests()
                    st.success("All email requests cleared")
                    st.rerun()
            else:
                st.info("No pending email requests")
        
        with tab2:
            st.markdown("### Assessment Analytics")
            
            # Display session storage analytics
            storage = StreamlitCloudStorage()
            assessments = storage.list_stored_assessments()
            
            if assessments:
                st.metric("Total Assessments", len(assessments))
                
                # Show recent assessments
                st.markdown("**Recent Assessments:**")
                for assessment in assessments[-5:]:
                    st.markdown(f"• {assessment['filename']} - {assessment['saved_at']}")
            else:
                st.info("No assessments in current session")
        
        with tab3:
            st.markdown("### Storage Management")
            
            storage = StreamlitCloudStorage()
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🧹 Cleanup Old Data"):
                    cleaned = storage.cleanup_old_data(days=7)
                    st.success(f"Cleaned up {cleaned} old entries")
            
            with col2:
                storage_size = len(st.session_state.get('cloud_storage', {}))
                st.metric("Items in Storage", storage_size)
