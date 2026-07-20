import requests

class Connection:
    def __init__(self, username, api_key, base_url="https://api.rockgympro.com"):
        self.base_url = base_url

        # starting a session for easy connection management
        self._session = requests.Session()  

        # setting up http basic auth
        self._session.auth = (username, api_key)

    def get(self, base_url, path, params):
        response = self._session.get(url=f"{base_url}/{path}", params=params)
        return self.handler(response=response)
        
    def handler(self, response):
        if response == 200:
            return response.json()
        elif response == 400:
            return "400: Bad Request"
        elif response == 401:
            return "401: Unauthorized"
        elif response == 404:
            return "404: Not Found"
        elif response == 422:
            return "422: Input validation failed"

        