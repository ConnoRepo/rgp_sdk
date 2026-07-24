from typing import Unpack, TypedDict, Literal

class ValidDailyFilters(TypedDict, total=False):
    startDate : str
    endDate : str
    tag : str
    limit : int
    page : int

class DailyNumbers:

    def __init__(self, conn):
        self._conn = conn

    def get_daily_numbers(self, facilityCode, **filters : Unpack[ValidDailyFilters]): 
        return self._conn.get(path=f"/dailynumbers/facility/{facilityCode}", params=filters)