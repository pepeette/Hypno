"""
Create admin_interface.py for manual email processing:
"""

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
