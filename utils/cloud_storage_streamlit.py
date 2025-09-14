"""
Create utils/cloud_storage_streamlit.py:
"""

import streamlit as st
import json
from datetime import datetime
import base64
import tempfile
import os

# COMMENTED OUT: Google Cloud Storage alternative
"""
# Alternative: Google Cloud Storage implementation
# Uncomment and configure for production use

from google.cloud import storage
from google.oauth2 import service_account
import os

class GoogleCloudStorage:
    def __init__(self):
        # Initialize Google Cloud Storage
        self.bucket_name = os.getenv('GCS_BUCKET_NAME', 'behavioral-assessment-data')
        
        # Initialize client with service account
        try:
            # Option 1: Using service account key file
            credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
            if credentials_path and os.path.exists(credentials_path):
                credentials = service_account.Credentials.from_service_account_file(credentials_path)
                self.client = storage.Client(credentials=credentials)
            else:
                # Option 2: Using service account key from environment variable
                credentials_json = os.getenv('GCS_SERVICE_ACCOUNT_JSON')
                if credentials_json:
                    import json
                    credentials_info = json.loads(credentials_json)
                    credentials = service_account.Credentials.from_service_account_info(credentials_info)
                    self.client = storage.Client(credentials=credentials)
                else:
                    # Option 3: Default credentials (for deployed environments)
                    self.client = storage.Client()
            
            self.bucket = self.client.bucket(self.bucket_name)
            
        except Exception as e:
            st.error(f"Google Cloud Storage initialization failed: {str(e)}")
            self.client = None
            self.bucket = None
    
    def save_assessment_data(self, assessment_data, filename):
        if not self.client:
            return None
        
        try:
            # Prepare data for storage
            storage_data = {
                'assessment_data': assessment_data,
                'saved_at': datetime.now().isoformat(),
                'version': '2.0'
            }
            
            # Convert to JSON
            json_data = json.dumps(storage_data, indent=2, default=str)
            
            # Upload to GCS
            blob_name = f"assessments/{datetime.now().year}/{datetime.now().month}/{filename}"
            blob = self.bucket.blob(blob_name)
            
            blob.upload_from_string(
                json_data,
                content_type='application/json'
            )
            
            # Set metadata
            blob.metadata = {
                'session_id': assessment_data.get('session_id', ''),
                'user_email': assessment_data.get('contact_info', {}).get('email', ''),
                'pattern_count': str(len(assessment_data.get('pattern_scores', {}))),
                'is_digital_native': str(assessment_data.get('is_digital_native', False))
            }
            blob.patch()
            
            # Generate signed URL (valid for 30 days)
            url = blob.generate_signed_url(
                version="v4",
                expiration=datetime.now() + timedelta(days=30),
                method="GET"
            )
            
            return url
            
        except Exception as e:
            st.error(f"Failed to save to Google Cloud Storage: {str(e)}")
            return None
    
    def save_pdf(self, pdf_bytes, filename):
        if not self.client:
            return None
        
        try:
            # Upload PDF to GCS
            blob_name = f"reports/{datetime.now().year}/{datetime.now().month}/{filename}"
            blob = self.bucket.blob(blob_name)
            
            blob.upload_from_string(
                pdf_bytes,
                content_type='application/pdf'
            )
            
            # Set metadata
            blob.metadata = {
                'generated_at': datetime.now().isoformat(),
                'file_type': 'behavioral_blueprint_pdf'
            }
            blob.patch()
            
            # Generate signed URL (valid for 30 days)
            url = blob.generate_signed_url(
                version="v4",
                expiration=datetime.now() + timedelta(days=30),
                method="GET"
            )
            
            return url
            
        except Exception as e:
            st.error(f"Failed to save PDF to Google Cloud Storage: {str(e)}")
            return None
    
    def retrieve_assessment_data(self, session_id):
        if not self.client:
            return None
        
        try:
            # List blobs and find matching session_id
            blobs = self.client.list_blobs(self.bucket, prefix='assessments/')
            
            for blob in blobs:
                if blob.metadata and blob.metadata.get('session_id') == session_id:
                    # Download and parse JSON
                    json_data = blob.download_as_text()
                    data = json.loads(json_data)
                    return data.get('assessment_data')
            
            return None
            
        except Exception as e:
            st.error(f"Failed to retrieve data from Google Cloud Storage: {str(e)}")
            return None

# Environment variables for Google Cloud Storage:
# GCS_BUCKET_NAME=your-bucket-name
# GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
# OR
# GCS_SERVICE_ACCOUNT_JSON={"type": "service_account", "project_id": "...", ...}
"""

class StreamlitCloudStorage:
    """Streamlit Community Cloud compatible storage using session state and downloads"""
    
    def __init__(self):
        # Initialize session state storage
        if 'cloud_storage' not in st.session_state:
            st.session_state.cloud_storage = {}
    
    def save_assessment_data(self, assessment_data, filename):
        """Save assessment data to session state and offer download"""
        try:
            # Prepare data for storage
            storage_data = {
                'assessment_data': assessment_data,
                'saved_at': datetime.now().isoformat(),
                'version': '2.0',
                'filename': filename
            }
            
            # Convert to JSON
            json_data = json.dumps(storage_data, indent=2, default=str)
            
            # Store in session state
            session_id = assessment_data.get('session_id', 'unknown')
            st.session_state.cloud_storage[session_id] = {
                'data': json_data,
                'filename': filename,
                'type': 'assessment',
                'saved_at': datetime.now().isoformat()
            }
            
            # Offer download in sidebar or expander
            self._offer_data_download(json_data, filename)
            
            return f"session_storage://{session_id}"
            
        except Exception as e:
            st.error(f"Failed to save assessment data: {str(e)}")
            return None
    
    def save_pdf(self, pdf_bytes, filename):
        """Save PDF to session state and offer download"""
        try:
            # Store PDF in session state
            pdf_b64 = base64.b64encode(pdf_bytes).decode()
            
            session_key = f"pdf_{datetime.now().timestamp()}"
            st.session_state.cloud_storage[session_key] = {
                'data': pdf_b64,
                'filename': filename,
                'type': 'pdf',
                'saved_at': datetime.now().isoformat()
            }
            
            return f"session_storage://{session_key}"
            
        except Exception as e:
            st.error(f"Failed to save PDF: {str(e)}")
            return None
    
    def _offer_data_download(self, json_data, filename):
        """Offer JSON data download"""
        try:
            with st.expander("💾 Download your assessment data", expanded=False):
                st.markdown("**Backup your assessment data:**")
                st.download_button(
                    label="📁 Download JSON Data",
                    data=json_data,
                    file_name=filename,
                    mime="application/json",
                    help="Download your complete assessment data for your records"
                )
                st.caption("Keep this file safe - it contains your complete assessment results")
        except:
            pass  # Fail silently if download widget can't be created
    
    def retrieve_assessment_data(self, session_id):
        """Retrieve assessment data from session state"""
        try:
            storage_data = st.session_state.cloud_storage.get(session_id)
            if storage_data and storage_data['type'] == 'assessment':
                json_data = storage_data['data']
                data = json.loads(json_data)
                return data.get('assessment_data')
            return None
        except Exception as e:
            st.error(f"Failed to retrieve assessment data: {str(e)}")
            return None
    
    def list_stored_assessments(self):
        """List all stored assessments in session"""
        assessments = []
        for key, data in st.session_state.cloud_storage.items():
            if data['type'] == 'assessment':
                assessments.append({
                    'session_id': key,
                    'filename': data['filename'],
                    'saved_at': data['saved_at']
                })
        return assessments
    
    def cleanup_old_data(self, days=7):
        """Clean up data older than specified days"""
        try:
            cutoff_date = datetime.now() - timedelta(days=days)
            
            keys_to_remove = []
            for key, data in st.session_state.cloud_storage.items():
                saved_at = datetime.fromisoformat(data['saved_at'])
                if saved_at < cutoff_date:
                    keys_to_remove.append(key)
            
            for key in keys_to_remove:
                del st.session_state.cloud_storage[key]
                
            return len(keys_to_remove)
            
        except Exception as e:
            st.error(f"Cleanup failed: {str(e)}")
            return 0
