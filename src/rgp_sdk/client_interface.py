from _http import Connection
from customers import Customer
from daily_numbers import DailyNumbers
from sales import Sales
from bookings import Bookings
from check_ins import CheckIn


class rgp:

    def __init__(self, username, api_key):
        self._conn = Connection(username, api_key)
        self.customer = Customer(self._conn)
        self.daily_numbers = DailyNumbers(self._conn)
        self.sales = Sales(self._conn)
        self.bookings = Bookings(self._conn)
        self.check_ins = CheckIn(self._conn)
