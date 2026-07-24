from typing import TypedDict, Unpack

class ValidSalesFilters:
    starId : int
    productId : int
    startDateTime : str
    endDateTime : str
    limit : int
    page : int

class Sales:

    def __init__(self, conn):
        self._conn = conn

    def get_facility_sales(self, facilityCode, **filters : Unpack[ValidSalesFilters]):
        return self._conn.get(path=f'sales/facility/{facilityCode}', params=filters)