from typing import TypedDict, Unpack

class ValidWidgetFilters(TypedDict, total=False): 
    includeInactiveWidgets : int
    limit : int
    page : int
    startDateTime : str
    endDateTime : str

class Widgets:

    def __init__(self, conn):
        self._conn = conn

    def get_facilityJ_widget_guids(self, facilityCode, **filters : Unpack[ValidWidgetFilters]):
        return self._conn.get(path=f"widgets/events/facility/{facilityCode}", params=filters)

    def get_events_from_facility_guid(self, facilityCode, eventWidgetGuid, startDateTime, endDateTime):

        # need to validate that these are the names of the params that the api is looking for
        params = {
            "startDateTime" : startDateTime,
            "endDateTime" : endDateTime
        }

        return self._conn.get(path=f"widgets/events/facility/{facilityCode}/{eventWidgetGuid}", params=params)

    def get_events_widget_guid(self, eventWidgetGuid, **filters : Unpack[ValidWidgetFilters]):

        if filters not in ["startDateTime", "endDateTime"]:
            raise ValueError(f"Invalid Parameter Provided: {filters}")

        return self._conn.get(path=f"widgets/events/{eventWidgetGuid}", params=filters)