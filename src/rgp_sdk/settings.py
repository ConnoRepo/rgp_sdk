class Settings: 

    def __init__(self, conn):
        self._conn = conn

    def single_setting(self, name, facility=None):

        if name is None:
            raise ValueError("Name is a required parameter")

        if name and facility is not None: 

            # keys will need to be changed to values that api will accept 
            # TBD during testing
            params = {
                "setting_name" : name,
                "facility_codes" : facility
            }
        else:
            params = None 

        return self._conn.get(path="v1/settings", params=params)

    def facility_settings(self, facilityCode): 
        return self._conn(path=f"v1/settings/facility/{facilityCode}")