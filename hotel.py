"""
---------------------------------------------------
Responsible Team Member: Aigerim
---------------------------------------------------
"""
#hotel name, full address, star rating, board, amount of days, arriving day, hotel cost
# functions: obtain_details, print, check_errors, get_cost

class Hotel:
    def __init__(self, hotels):
        self._hotels = hotels
        self._star_rating = ["1", "2", "3", "4", "5"]
        self._board_options = ["full", "half", "bed and breakfast"]
        self._month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self._hotels_details = {}
        self._address = ""
        self._arriving_date = ""
        # self.obtain_details()



    def check_errors(self, input_value):
        if len(input_value) == 0 or input_value.isdigit() or len(input_value) < 4:
            print("Error! Enter the correct details")
            print("Your input was either empty, a number was provided or it was less than 4 letters")
            return False
        else:
            return True


    def obtain_details(self):
        isHotel = True

        while isHotel:
            self._name = input("Enter the name of the hotel: ")

            while not self.check_errors(self._name):
                self._name = input("Enter the name of the hotel: ")

            print("Enter the full address of hotel")
            self._city = input("City: ")

            while not self.check_errors(self._city):
                self._city = input("City: ")

            self._street = input("Street: ")
            while not self.check_errors(self._street):
                self._street = input("Street: ")


            while True:
                self._build_number = input("Building number: ")
                if len(self._build_number) != 0 and self._build_number.isdigit() and len(self._build_number) <= 5:
                    break
                else:
                    print("Error! Enter correct building number")
                    print("Must be a number")

            self._address = self._build_number + " " +self._street + " " + self._city



            while True:
                self._star_input = input("Please select a star rating (1 to 5): ")
                if self._star_input in self._star_rating:
                    break
                else:
                    print("Error! Select from 1 to 5")


            while True:
                self._board_input = input("Please type one of the board options -> full, half, bed and breakfast: ")
                if self._board_input in self._board_options:
                    break
                else:
                    print("Error! Enter correct option")


            while True:
                self._days = input("How many days do you want to spend in the hotel? ")
                if self._days.isdigit() and int(self._days) < 365 and len(self._days) > 0:
                    break
                else:
                    print("Error! Must be a number and not more than a 1 year!")

            while True:
                self._day = input("Enter the arriving day (only the day): ")
                if self._day.isdigit() and int(self._day) < 31 and len(self._day) > 0:
                    break
                else:
                    print("Error! Must be a number and no more than 31")

            while True:
                self._month = input("Enter the month by numbers (1, 2, 3 etc): ")
                if self._month in self._month:
                    break
                else:
                    print("Error! Must be a number")

            while True:
                self._year = input("Enter the year: ")
                if self._year.isdigit() and len(self._year) == 4 and 2023 <= int(self._year) <= 2025:
                    break
                else:
                    print("Error! Please enter a valid four-digit number between 2023 and 2025.")

            if int(self._month) <10:
                self._arriving_date = self._day + "-0" + self._month + "-" + self._year
            else:
                self._arriving_date = self._day + "-" + self._month + "-" + self._year

            while True:
                self._cost_input = input("Enter the cost (in pounds): ")
                if self._cost_input.isdigit():
                    break
                else:
                    print("Error! Must be a number")


            isHotel = False
            self._hotel_details = {"Name": self._name, "Address": self._address, "Rating": self._star_input,
                                   "Board": self._board_input, "Days": self._days, "Date": self._arriving_date,
                                   "Cost": self._cost_input}
            self._hotels.append(self._hotel_details)

    def get_cost(self):
      return float(self._cost_input)


    def print(self):
        print("Name: " + self._hotels[0]["Name"])
        print("Address: " + self._hotels[0]["Address"])
        print("Rating: " + self._hotels[0]["Rating"])
        print("Board: " + self._hotels[0]["Board"])
        print("Number of days: " + self._hotels[0]["Days"])
        print("Arriving date: " + self._hotels[0]["Date"])
        print("Cost: " + self._hotels[0]["Cost"])





# hotels = []
# hotel1 = Hotel(hotels)
# hotel1.print()