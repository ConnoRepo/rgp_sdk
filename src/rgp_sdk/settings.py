class Settings: 

    def __init__(self, conn):
        self._conn = conn

    def single_setting(self, setting_name, facility_codes=None):

        if setting_name is None:
            raise ValueError("Name is a required parameter")

        params = {"setting_name" : setting_name}

        # need to write and then use a helper function that will unpack list and make the comma seperated values here and other places
        if facility_codes is not None:
            params["facility_codes"] = facility_codes

        return self._conn.get(path="settings", params=params)

    def facility_settings(self, facilityCode): 
        return self._conn.get(path=f"settings/facility/{facilityCode}")