import requests

class Connection:
    def __init__(self, username, api_key):
        self.base_url = "https://api.rockgympro.com"

        # starting a session for easy connection management
        self._session = requests.Session()  

        # setting up http basic auth
        self._session.auth = (username, api_key)

    def get(self, path, params=None):
        response = self._session.get(url=f"{self.base_url}/{path}", params=params)
        return self.handler(response=response)
        
    def handler(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            raise AttributeError(f"{response}: Bad Request")
        elif response.status_code == 401:
            raise AttributeError(f"{response}: Unauthorized")
        elif response.status_code == 404:
            raise AttributeError(f"{response}: Not Found")
        elif response.status_code == 422:
            raise AttributeError(f"{response}: Input validation failed")
