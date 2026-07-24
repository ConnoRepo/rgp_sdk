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
        return self._conn.get(path=f"bookings/facility/{facilityCode}", params=filters)

    def get_specific_booking_info(self, facilityCode, bookingId):
        return self._conn.get(path=f"bookings/facility/{facilityCode}/{bookingId}")