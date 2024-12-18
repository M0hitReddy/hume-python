# authenticator.py

import base64
import requests


class Authenticator:


    def __init__(self, api_key: str, secret_key: str, host: str = "test-api.hume.ai"):

        self.api_key = api_key
        self.secret_key = secret_key
        self.host = host

    def fetch_access_token(self) -> str:

        # Prepare the authorization string
        auth_string = f"{self.api_key}:{self.secret_key}"
        encoded = base64.b64encode(auth_string.encode()).decode()

        # Set up the headers
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded}",
        }

        # Prepare the body
        data = {
            "grant_type": "client_credentials",
        }

        # Make the POST request to the OAuth2 token endpoint
        response = requests.post(
            f"https://{self.host}/oauth2-cc/token", headers=headers, data=data
        )

        # Parse the JSON response
        data = response.json()

        # Extract the access token, raise an error if not found
        if "access_token" not in data:
            raise ValueError("Access token not found in response")

        return data["access_token"]
