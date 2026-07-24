from typing import TypedDict, Unpack

class ValidStaffFilters(TypedDict, total=False):
    startId : int
    limit : int
    page : int

class Staff:

    def __init__(self, conn):
        self._conn = conn

    def get_staff_records(self, **filters : Unpack[ValidStaffFilters]):
        return self._conn.get(path="v1/staff", params=filters)