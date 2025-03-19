import base64
from locust import HttpUser, task, between
import requests


def to_b64(file_path):
    try:
        with open(file_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        raise Exception(f'File: {file_path} - Info: {e}')


class FileUploadUser(HttpUser):
    # Wait time between tasks
    # wait_time = between(1, 3)
    
    @task
    def upload_file(self):
        # Define the endpoint for the POST request
        # url = "/pdf_parse"  # Replace with the actual endpoint
        url = "/predict"
        # File to upload
        # files = {
        #     # "pdf_file": ("ASMEC_537.pdf", open("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf","rb"), "application/pdf"),
        #     # "file": ("ASMEC_537.pdf", open("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf","rb"), "application/pdf"),
        #     'file': to_b64("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf")
        # }
        files=[]
        
        # Additional data (if needed)
        data = {
            "key": "value",  # Replace with actual key-value pairs
            'file': to_b64("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf")
        }
        
        # Sending the POST request
        response = self.client.post(url, files=files, json=data)
        
        
        # response = requests.post("http://127.0.0.1:8000/predict", json={
        #     'file': to_b64("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf"),
        #     # 'kwargs': kwargs
        # })
        
        
        # Log the response
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        assert int(response.status_code)==200
