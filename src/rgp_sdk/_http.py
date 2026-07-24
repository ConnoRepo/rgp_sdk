import requests

class Connection:
    def __init__(self, username, api_key):
        self.base_url = "https://api.rockgympro.com/v1"

        # starting a session for easy connection management
        self._session = requests.Session()  

        # setting up http basic auth
        self._session.auth = (username, api_key)

        # implement Accept header and User Agent
        # implement __enter__ __exit__ and close()

    def get(self, path, params=None):
        # need to add a parameter normalization function that converts bools, dates, and lists into api expected formats before passing to the get request
        # make sure to drop None values so that way the parameter doesn't get passed as None, it just doesn't get sent

        # add client side validation of documented constraints on different params

        # figure out a default timeout value that I want to have set here
        response = self._session.get(url=f"{self.base_url}/{path}", params=params)
        return self.handler(response=response)
        
    def handler(self, response):
        if response.status_code == 200:
            # wrap this in a try except block and raise custom errors
            return response.json()
        else:
            # need to add robust error handling, but for now simplifying erroring to consider anything that isn't 200 an error
            # this way we catch every error code without explicitly listing out every error code
            raise ValueError
