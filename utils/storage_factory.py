"""
Create utils/storage_factory.py:
"""

def create_storage_client():
    """Factory function to create appropriate storage client"""
    
    storage_type = st.secrets.get("storage", {}).get("storage_type", "session")
    
    if storage_type == "gcs":
        # Use Google Cloud Storage if configured
        try:
            from utils.cloud_storage_streamlit import GoogleCloudStorage
            return GoogleCloudStorage()
        except ImportError:
            st.warning("Google Cloud Storage not available, falling back to session storage")
            from utils.cloud_storage_streamlit import StreamlitCloudStorage
            return StreamlitCloudStorage()
    else:
        # Default to Streamlit session storage
        from utils.cloud_storage_streamlit import StreamlitCloudStorage
        return StreamlitCloudStorage()
