from typing import TypedDict, Unpack

class ValidBookingFilters(TypedDict, total=False): 
    startId : int
    customerGuid : str
    startDateTime : str
    endDateTime : str
    limit : int
    page : int

class Bookings: 

    def __init__(self, conn):
        self._conn = conn

    def get_facility_bookings(self, facilityCode, **filters : Unpack[ValidBookingFilters]):
        