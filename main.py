"""
---------------------------------------------------
Team Member(s) contribution:

- William:
-
---------------------------------------------------
"""

# ---------------------------- main.py - ---------------------------
from traveller import Traveller

travellers_list = []

# Create an instance of the Traveller class
traveller_instance = Traveller(name="", dob="", passport_no="", phone_no="")

# Obtain details and add to the list
traveller_instance.obtainDetails(travellers_list)

# Print details from the list
traveller_instance.printDetails(travellers_list)

