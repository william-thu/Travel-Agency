"""
---------------------------------------------------
Team Member(s) contribution:

- William:
-
---------------------------------------------------
"""

# ---------------------------- main.py - ---------------------------
from traveller import Traveller

class Holidays:
    def __init__(self):
        self.traveller_instance = Traveller(name="", dob="", passport_no="", phone_no="")
        self.traveller_list = []

    def obtain_details(self):
        self.traveller_instance.obtainDetails(self.traveller_list)

    def print_details(self):
        self.traveller_instance.printDetails(self.traveller_list)

    def calc_total_cost(self):
        pass


holidays_instance = Holidays()
holidays_instance.obtain_details()
holidays_instance.print_details()

# print("--------------- Holiday Booked! ---------------")
# print("Total cost of holiday: £" + str(total_cost))



