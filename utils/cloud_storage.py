
import boto3
import json
from datetime import datetime, timedelta
import streamlit as st
from botocore.exceptions import ClientError
import os

class CloudStorage:
    """Handle cloud storage operations for assessment data and PDFs"""
    
    def __init__(self):
        # Initialize with your cloud provider (AWS S3 example)
        self.bucket_name = os.getenv('ASSESSMENT_BUCKET', 'behavioral-assessment-data')
        self.region = os.getenv('AWS_REGION', 'us-east-1')
        
        # Initialize S3 client
        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=self.region
            )
        except Exception as e:
            st.error(f"Cloud storage initialization failed: {str(e)}")
            self.s3_client = None
    
    def save_assessment_data(self, assessment_data, filename):
        """Save assessment data as JSON to cloud storage"""
        if not self.s3_client:
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
            
            # Upload to S3
            key = f"assessments/{datetime.now().year}/{datetime.now().month}/{filename}"
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=json_data,
                ContentType='application/json',
                Metadata={
                    'session_id': assessment_data.get('session_id', ''),
                    'user_email': assessment_data.get('contact_info', {}).get('email', ''),
                    'pattern_count': str(len(assessment_data.get('pattern_scores', {}))),
                    'is_digital_native': str(assessment_data.get('is_digital_native', False))
                }
            )
            
            # Generate presigned URL for access (valid for 30 days)
            url = self.generate_presigned_url(key, expiration=2592000)  # 30 days
            
            return url
            
        except ClientError as e:
            st.error(f"Failed to save to cloud storage: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error saving data: {str(e)}")
            return None
    
    def save_pdf(self, pdf_bytes, filename):
        """Save PDF to cloud storage"""
        if not self.s3_client:
            return None
        
        try:
            # Upload PDF to S3
            key = f"reports/{datetime.now().year}/{datetime.now().month}/{filename}"
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=pdf_bytes,
                ContentType='application/pdf',
                Metadata={
                    'generated_at': datetime.now().isoformat(),
                    'file_type': 'behavioral_blueprint_pdf'
                }
            )
            
            # Generate presigned URL (valid for 30 days)
            url = self.generate_presigned_url(key, expiration=2592000)
            
            return url
            
        except ClientError as e:
            st.error(f"Failed to save PDF to cloud: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error saving PDF: {str(e)}")
            return None
    
    def generate_presigned_url(self, object_key, expiration=3600):
        """Generate a presigned URL for the object"""
        try:
            response = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': object_key},
                ExpiresIn=expiration
            )
            return response
        except ClientError as e:
            st.error(f"Failed to generate access URL: {str(e)}")
            return None
    
    def retrieve_assessment_data(self, session_id):
        """Retrieve assessment data by session ID"""
        if not self.s3_client:
            return None
        
        try:
            # List objects with session_id in metadata
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=f"assessments/"
            )
            
            # Find matching object (in a production app, you'd use a database index)
            for obj in response.get('Contents', []):
                # Get object metadata
                head_response = self.s3_client.head_object(
                    Bucket=self.bucket_name,
                    Key=obj['Key']
                )
                
                if head_response.get('Metadata', {}).get('session_id') == session_id:
                    # Retrieve the object
                    get_response = self.s3_client.get_object(
                        Bucket=self.bucket_name,
                        Key=obj['Key']
                    )
                    
                    data = json.loads(get_response['Body'].read())
                    return data.get('assessment_data')
            
            return None
            
        except ClientError as e:
            st.error(f"Failed to retrieve data: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error retrieving data: {str(e)}")
            return None
