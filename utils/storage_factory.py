# utils/storage_factory.py
import streamlit as st

def create_storage_client():
    """Factory function to create appropriate storage client"""
    
    storage_type = st.secrets.get("storage", {}).get("type", "session")
    
    if storage_type == "gcs" and _gcs_available():
        from utils.cloud_storage_streamlit import GoogleCloudStorage
        return GoogleCloudStorage()
    elif storage_type == "s3" and _s3_available():
        from utils.cloud_storage_streamlit import S3CloudStorage  # Create this
        return S3CloudStorage()
    else:
        # Default to session storage for Streamlit Community Cloud
        from utils.cloud_storage_streamlit import StreamlitCloudStorage
        return StreamlitCloudStorage()

def _gcs_available():
    """Check if GCS credentials are available"""
    return bool(st.secrets.get("gcs", {}).get("credentials"))

def _s3_available():
    """Check if S3 credentials are available"""
    return bool(st.secrets.get("aws", {}).get("access_key"))
