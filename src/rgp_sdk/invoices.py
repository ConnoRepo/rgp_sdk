from typing import TypedDict, Unpack

class ValidInvoiceFilters(TypedDict, total=False):
    startId : int
    customerGuid : str
    startDateTime : str
    endDateTime : str
    includeVoidInvoices : int
    limit : int
    page : int

class Invoices:

    def __init__(self, conn):
        self._conn = conn

    def get_facility_invoices(self, facilityCode, **filters : Unpack[ValidInvoiceFilters]):
        return self._conn.get(path=f"invoices/facility/{facilityCode}", params=filters)

    def get_invoice_details(self, facilityCode, invoiceId):
        return self._conn.get(path=f"invoices/facility/{facilityCode}/{invoiceId}")
