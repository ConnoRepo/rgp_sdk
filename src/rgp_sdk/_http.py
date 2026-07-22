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
            raise response.json()
        elif response == 400:
            raise AttributeError(f"{response}: Bad Request")
        elif response == 401:
            raise AttributeError(f"{response}: Unauthorized")
        elif response == 404:
            raise AttributeError(f"{response}: Not Found")
        elif response == 422:
            raise AttributeError(f"{response}: Input validation failed")

        