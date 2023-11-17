"""
---------------------------------------------------
Responsible Team Member: William
---------------------------------------------------
"""

class Traveller:
    def __init__(self, name, dob, passport_no, phone_no):
        self._name = name
        self._dob = dob
        self._passport_no = passport_no
        self._phone_no = phone_no

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def get_passport_no(self):
        return self._passport_no

    def get_phone_no(self):
        return self._phone_no
    
    # Check if input has any special characters
    def has_special_characters(self, input_string):
        special_characters = "!`¬£$%^&*()-_=+[]{}#~'@;:/?><.,|"
        for char in input_string:
            if char in special_characters:
                return True
            else:
                return False

    # Check if input has any numbers
    def has_numerical_characters(self, input_string):
        numerical_characters = "1234567890"
        for char in input_string:
            if char in numerical_characters:
                return True
            else:
                return False

    # Function to validate Date of Birth format
    def validate_dob(self, dob):
        valid_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

        # Split the provided dob by '/'
        date_parts = dob.split('/')

        # Check the three parts of the format, and assign them to dd/mm/yyyy respectively
        if len(date_parts) != 3:
            print("Invalid DoB provided.")
            return False
        else:
            day = date_parts[0]
            month = date_parts[1]
            year = date_parts[2]
            if not (day.isdigit() and year.isdigit()):
                print("Day and year must be numeric values.")
                return False
            elif len(day) >= 3 or int(day) >= 32:
                print("Invalid date. (1-31 only)")
                return False
            elif len(year) >= 5:
                print("Invalid year.")
                return False
            if month.lower() not in valid_months:
                print("Use three-letter abbreviations (jan, feb, etc...)")
                return False
        return True

    # Get Traveller details
    def set_name(self, initial_name):
        valid_name = False
        name = initial_name
        while not valid_name:
            if self.has_numerical_characters(name):
                print("Name cannot contain numeric characters.")
            elif self.has_special_characters(name):
                print("Name cannot contain special characters.")
            else:
                valid_name = True
                # Break out of the loop only when a valid name is entered
                break
            name = input("Enter traveller's name: ")  # Ask for input again if the name is invalid
        self._name = name  # Set the valid name to the instance variable

    def set_dob(self, initial_dob):
        valid_dob = False
        dob = initial_dob
        while not valid_dob:
            if not self.validate_dob(dob):
                print("Use the provided format.")
            else:
                valid_dob = True
                break
            dob = input("Enter Date of Birth (dd/mm/yyyy) - Month must be 3-letters abbreviated (e.g.: 07/Mar/2002): ")
        self._dob = dob

    def set_phone_no(self, initial_phone_no):
        valid_phone_no = False
        phone_no = initial_phone_no
        while not valid_phone_no:
            if self.has_special_characters(phone_no):
                print("Phone no. cannot contain special characters.")
            elif not self.has_numerical_characters(phone_no):
                print("Phone no. cannot contain non-numeric characters.")
            else:
                valid_phone = True
                break
            phone_no = input("Enter Phone No.: ")
        self._phone_no = phone_no

    def set_passport(self, initial_passport):
        valid_passport = False
        passport_no = initial_passport
        while not valid_passport:
            if self.has_special_characters(passport_no):
                print("Passport cannot contain special characters.")
            else:
                valid_passport = True
                break
            passport_no = input("Enter Passport: ")
        self._passport_no = passport_no

    def obtainDetails(self, travellers):
        print("-------------- You are now booking for a Holiday! --------------")
        more_travellers = True
        while more_travellers == True:
            self.set_name(input("Enter traveller's name: "))
            self.set_dob(input("Enter Date of Birth (dd/mm/yyyy) - Month must be 3-letters abbreviated (e.g.: 07/Mar/2002): "))
            self.set_phone_no(input("Enter Phone No.: "))
            self.set_passport(input("Enter Passport: "))

            traveller = {
                "Name": self._name,
                "Date of Birth": self._dob,
                "Passport Number": self._passport_no,
                "Phone Number": self._phone_no
            }

            travellers.append(traveller)
            while True:
                response = input("Do you want to enter another traveller information? (yes / no): ").lower()
                if response == "yes":
                    break
                elif response == "no":
                    more_travellers = False
                    break
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")

    def printDetails(self, travellers):
        print("--------------- Traveller Details ---------------")
        for traveller in travellers:
            print("Name: ", traveller["Name"])
            print("Date of Birth: ", traveller["Date of Birth"])
            print("Passport Number: ", traveller["Passport Number"])
            print("Phone Number: ", traveller["Phone Number"])
            print("------------------------------------------")


travellers_list = []

# Create an instance of the Traveller class
traveller_instance = Traveller(name="", dob="", passport_no="", phone_no="")

# Obtain details and add to the list
traveller_instance.obtainDetails(travellers_list)

# Print details from the list
traveller_instance.printDetails(travellers_list)