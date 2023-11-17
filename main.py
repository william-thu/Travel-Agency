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
        # Create an instance of the Traveller class
        traveller_instance = Traveller(name="", dob="", passport_no="", phone_no="")
        traveller_instance.obtainDetails(self.travellers)

    def print_details(self):
        print("--------------- Traveller Details ---------------")
        for traveller in self.travellers:
            print("Name: ", traveller.get_name())
            print("Date of Birth: ", traveller.get_dob())
            print("Passport Number: ", traveller.get_passport_no())
            print("Phone Number: ", traveller.get_phone_no())
            print("------------------------------------------")

    def calc_total_cost(self):
        pass

    def book_holiday(self):
        self.obtain_details()
        self.print_details()
        total_cost = self.calc_total_cost()
        print("--------------- Holiday Booked! ---------------")
        print("Total cost of holiday: £" + str(total_cost))



