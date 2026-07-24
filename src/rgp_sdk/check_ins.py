from typing import TypedDict, Unpack

class ValidCheckinTypes(TypedDict, total=False):
    startId : int
    customerGuid : str
    customerDetails : bool
    remoteOnly : bool
    startDateTime : str
    endDateTime : str
    limit : int
    page : int

class CheckIns: 

    def __init__(self, conn):
        self._conn = conn

    def get_facility_checkins(self, facilityCode, **filters : Unpack[ValidCheckinTypes]):
        return self._conn.get(path=f"checkins/facility/{facilityCode}", params=filters)

    def get_singular_checkin_details(self, facilityCode, checkinId):
        return self._conn.get(path=f"checkins/facility/{facilityCode}/{checkinId}")

    def get_active_checkins(self, facilityCode):
        return self._conn.get(path=f"checkins/active/facility/{facilityCode}")
        