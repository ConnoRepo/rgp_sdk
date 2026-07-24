class Facilities:

    def __init__(self, conn):
        self._conn = conn

    def get_facilities(self):
        return self._conn.get(path="facilities", params=None)