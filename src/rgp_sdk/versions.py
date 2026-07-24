class Versions:

    def __init__(self, conn):
        self._conn = conn

    def versions(self, facility=None):
        if facility:

            # this will need to be adjusted depending on what the api is looking for
            facility = {
                "facilities" : facility
            }

        return self._conn.get(path="/v1/versions", params=facility)

    def facility_version(self, facilityCode):
        return self._conn.get(path=f"v1/versions/facility/{facilityCode}")
