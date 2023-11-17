"""
---------------------------------------------------
Team Member(s) contribution:

- William:
-
---------------------------------------------------
"""

# ---------------------------- main.py - ---------------------------
from traveller import Traveller
import hotel
import flight
import car_hire

class HolidayBooking:
    def __init__(self):
        self.travellers = []
        self.flights = []
        self.car_hires = []

    def obtain_details(self):
        pass

    def print_details(self):
        pass

    def calc_total_cost(self):
        pass

    def book_holiday(self):
        self.obtain_details()
        self.print_details()
        total_cost = self.calc_total_cost()
        print("--------------- Holiday Booked! ---------------")
        print("Total cost of holiday: £" + str(total_cost))



