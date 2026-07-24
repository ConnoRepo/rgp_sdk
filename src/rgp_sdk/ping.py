import requests

class Ping: 

    def __init__(self, conn=None):
        self._conn = conn

    def test_ping():
        return requests.get(url="https://api.rockgympro.com/ping")

    def test_ping_auth(self):
        return self._conn.get(path="v1/ping", params=None)

    def auth_token_info(self):
        return self._conn.get(path="v1/me", params=None)