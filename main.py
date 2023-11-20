"""
---------------------------------------------------
Team Member(s) contribution:

- William: set up main.py (Holidays class, methods and new holiday instance), holiday iteration, calc holiday cost
-Zhen Yang: participated in writing main.py
- Aigerim: added needed hotel class codes
---------------------------------------------------
"""

# ---------------------------- main.py - ---------------------------
from traveller import Traveller
from hotel import Hotel
import flight

class Holidays:
    def __init__(self):
        self.traveller_instance = Traveller(name="", dob="", passport_no="", phone_no="")
        self.traveller_list = []
        self._hotels = []
        self.hotel_instance = Hotel(self._hotels)

    # method to obtain details
    def obtain_details(self):
        self.traveller_instance.obtainDetails(self.traveller_list)
        self.hotel_instance.obtain_details()
        flight.flight_main()
        for item in flight.lst:
            item.show()
        flight_cost = flight.getTotalCost(flight.lst2)

    # method to print details
    def print_details(self):
        self.traveller_instance.printDetails(self.traveller_list)
        self.hotel_instance.print()

    # method to calculate total cost of holiday
    def calc_total_cost(self):
        total_cost = 0
        total_cost = total_cost + flight.getTotalCost(flight.lst2) + self.hotel_instance.get_cost()
        return total_cost

#Obtain the flight module and calculate flight.cost

# print("Total cost of holiday: £" + str(total_cost))


'''
total_cost = 0
total_cost = total_cost + flight_cost
'''

# please do not touch
while True:
    holidays_instance = Holidays()
    holidays_instance.obtain_details()
    holidays_instance.print_details()
    total_cost = holidays_instance.calc_total_cost()

    print("--------------- Holiday Booked! ---------------")
    print("Total cost of holiday: £" + str(total_cost))

    response = input("Do you want to book another holiday? (yes / no): ").lower()
    if response == "no":
        print("Thank you for booking! Have a great holiday.")
        break
    elif response == "yes":
      pass
    else:
      print("Invalid input.")


