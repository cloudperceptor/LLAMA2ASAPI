########################################################
# Cloudperceptor                                        #
# #######################################################
import requests
import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account

def invoke_llama2(prompt):
    # Define the required SCOPES
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

    # Replace 'NAME_OF_FILE' with your service account JSON file name that you downloaded
    SERVICE_ACCOUNT_FILE = 'cap-neural-netizens-421ef50e5b56.json'

    # Load credentials from the service account file with the specified SCOPES
    cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Create an authentication request
    auth_req = google.auth.transport.requests.Request()

    # Refresh the credentials
    cred.refresh(auth_req)

    # Obtain the bearer token
    bearer_token = cred.token

    # Define the base URL for your specific region (us-central1 in this example)
    base_url = "https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/endpoints/{endpoint_id}:predict"

    # GCP project ID
    project_id = "cap-neural-netizens"

    # Endpoint ID from the model dashboard
    endpoint_id = "997962932857864192"

    # Define the request body for your specific prompt and parameters
    request_body = {
        "instances": [
            {
                "prompt": prompt,
                "max_tokens": 200,
                "top_k": 10,
                "top_p" : 1.0
            }
        ]
    }

    # Create the full URL using the project and endpoint IDs
    full_url = base_url.format(project_id=project_id, endpoint_id=endpoint_id)

    headers = {
        "Authorization": "Bearer {bearer_token}".format(bearer_token=bearer_token),
        "Content-Type": "application/json"
    }

    # Send a POST request to the model endpoint
    resp = requests.post(full_url, json=request_body, headers=headers)
    
    # return the response from the model
    return resp.json()
