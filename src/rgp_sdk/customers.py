from typing import Unpack, TypedDict, Literal

class ValidCustomerFilters(TypedDict, total=False):
    type: Literal["GUEST", "PUNCH CARD", "MEMBER", "CORPORATE"]
    status: Literal["TERMINATED", "FROZEN", "EXPIRED", "OK"]
    waiverSigned: bool
    birthdayMonth: int                  # 1-12
    birthdayUpcoming: int               # 1-365
    firstContactDateEnding: str         # yyyy-mm-dd
    firstContactDateStarting: str       # yyyy-mm-dd
    lastVisitDateEnding: str            # yyyy-mm-dd
    lastVisitDateStarting: str          # yyyy-mm-dd
    lastEditDateEnding: str             # yyyy-mm-dd
    lastEditDateStarting: str           # yyyy-mm-dd
    firstName: str                      # % wildcard allowed
    middleName: str                     # % wildcard allowed
    lastName: str                       # % wildcard allowed
    city: str                           # % wildcard allowed
    state: str                          # % wildcard allowed
    postalCode: str                     # % wildcard allowed
    country: str                        # % wildcard allowed
    ageGreaterThan: int                 # >= 1
    ageLessThan: int                    # >= 1
    onlineAccountLinked: bool
    emailAddressPopulated: bool
    emailAllowMarketing: bool
    emailTouchDateEnding: str           # yyyy-mm-dd
    emailTouchDateStarting: str         # yyyy-mm-dd
    emailAddress: str                   # % wildcard allowed
    limit: int                          # 10-200, default 100
    page: int                           # >= 1, default 1

class Customer:

    def __init__(self, conn):
        self._conn = conn

    def single_customer(self, customer_guid):
        return self._conn.get(path="customers/", params=customer_guid)

    def  any_customers(self, customer_guid_list):
        return self._conn.get(path="customers/", params=customer_guid_list) 
    
    def filtered_customers(self, facility_code, **filters: Unpack[ValidCustomerFilters]):
        return self._conn.get(path=f"customers/facility/{facility_code}", params=filters)