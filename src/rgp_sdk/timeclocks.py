from typing import TypedDict, Unpack

class ValidTimeclockFilters(TypedDict, total=False):
    startId : int
    customerGuid : str
    startDateTime : str
    endDateTime : str
    limit : int
    page : int

class Timeclock:

    def __init__(self, conn):
        self._conn = conn

    def get_all_facility_timeclock_entries(self, facilityCode, **filters : Unpack[ValidTimeclockFilters]):
        return self._conn.get(path=f"timeclocks/facility/{facilityCode}", params=filters)

    def get_timeclock_details(self, facilityCode, timeclockId):
        return self._conn.get(path=f"timeclocks/facility/{facilityCode}/{timeclockId}")