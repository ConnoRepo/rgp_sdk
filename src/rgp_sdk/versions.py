class Versions:

    def __init__(self, conn):
        self._conn = conn

    def versions(self, facility=None):
        if facility:

            # this will need to be adjusted depending on what the api is looking for
            params = {
                "facility" : facility
            }

        return self._conn.get(path="versions", params=params)

    def facility_version(self, facilityCode):
        return self._conn.get(path=f"versions/facility/{facilityCode}")
