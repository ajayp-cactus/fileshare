from locust import HttpUser, task, between

class FileUploadUser(HttpUser):
    # Wait time between tasks
    # wait_time = between(1, 3)
    
    @task
    def upload_file(self):
        # Define the endpoint for the POST request
        url = "/pdf_parse"  # Replace with the actual endpoint
#        url="/predict"        
        # File to upload
        files = {
#            "file": ("ASMEC_537.pdf", open("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf","rb").read(), "application/pdf"),
           "pdf_file": ("ASMEC_537.pdf", open("/home/ajay_prakash/fileshare/PDF Testing Files/ASMEC_537.pdf","rb"), "application/pdf"), 
       }
        
        # Additional data (if needed)
        data = {
            "key": "value",  # Replace with actual key-value pairs
        }
        
        # Sending the POST request
        response = self.client.post(url, files=files, data=data)
        
        # Log the response
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
