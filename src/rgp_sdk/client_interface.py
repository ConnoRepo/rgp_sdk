from ._http import Connection
from .customers import Customers
from .daily_numbers import DailyNumbers
from .sales import Sales
from .bookings import Bookings
from .check_ins import CheckIns
from .facilities import Facilities
from .invoices import Invoices
from .ping import Ping
from .settings import Settings
from .versions import Versions
from .staff import Staff
from .timeclocks import Timeclocks
from .widgets import Widgets

class RGP:

    def __init__(self, username, api_key):
        self._conn = Connection(username, api_key)
        self.customer = Customers(self._conn)
        self.daily_numbers = DailyNumbers(self._conn)
        self.sales = Sales(self._conn)
        self.bookings = Bookings(self._conn)
        self.check_ins = CheckIns(self._conn)
        self.facilities = Facilities(self._conn)
        self.invoices = Invoices(self._conn)
        self.ping = Ping(self._conn)
        self.settings = Settings(self._conn)
        self.versions = Versions(self._conn)
        self.staff = Staff(self._conn)
        self.timeclock = Timeclocks(self._conn)
        self.widgets = Widgets(self._conn)
