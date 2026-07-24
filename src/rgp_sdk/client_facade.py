from _http import Connection
from customers import Customer
from daily_numbers import DailyNumbers

class rgp:

    def __init__(self, username, api_key):
        self._conn = Connection(username, api_key)
        self.customer = Customer(self._conn)
        self.daily_numbers = DailyNumbers(self._conn)
