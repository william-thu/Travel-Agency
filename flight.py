"""
---------------------------------------------------
Responsible Team Member: Zhen Yang
---------------------------------------------------
"""
class Flight():
  def __init__(self,flight_number,airline,destination,d_y,d_m,d_d,d_h,d_min,a_y,a_m,a_d,a_h,a_min,cost):
      self.flight_number = flight_number
      self.airline = airline
      self.destination = destination
      self.d_y = d_y
      self.d_m = d_m
      self.d_d = d_d
      self.d_h = d_h
      self.d_min = d_min
      self.a_y = a_y
      self.a_m = a_m
      self.a_d = a_d
      self.a_h = a_h
      self.a_min = a_min
      self.cost = cost

  def show(self):
      print('Flight number：' + self.flight_number)
      print('Airline: ' + self.airline)
      print('Destination: ' + self.destination)
      print('Departure: ' + self.d_y+'-' + self.d_m+'-'+self.d_d+' '+self.d_h+':'+self.d_min)
      print('Arrival: ' + self.a_y + '-'+ self.a_m+'-'+self.a_d+' '+self.a_h+':'+self.a_min)
      print('Cost: £' + str(self.cost))
      print()

def getTotalCost(x):
  total_cost = 0
  for a in x:
      total_cost = total_cost + float(a)
  return total_cost

def flight_main():
  print('Please input the flight information \n(Format(use numbers to represent dates and times): \nFlight number-Airline-Destination-Departure year-D month-D day-D hour-D minute-Arrival year-A month-A day-A hour-A minute-Cost\neg. BA123-British Airways-Beijing-2023-10-01-09-01-2023-10-01-19-01-347.48):\n')
  global lst,lst2
  lst = []
  lst2 = []
  year = list(range(2022,3001))
  month = list(range(1,13))
  day = list(range(0, 32))
  hour = list(range(0, 25))
  minute = list(range(0, 61))
  while True:
      try:
          s = input('Please input information of this flight:')
          s_lst = s.split('-')
          a = s_lst[13]#cost
          b = int(s_lst[4])#month
          c = int(s_lst[5])#day
          d = int(s_lst[6])#hour
          e = int(s_lst[7])#minute
          f = int(s_lst[9])#month
          g = int(s_lst[10])#day
          h = int(s_lst[11])#hour
          i = int(s_lst[12])#minute
          j = int(s_lst[3])#year
          k = int(s_lst[8])#year
          if (j or k) not in year or (b or f) not in month or (c or g) not in day or (d or h) not in hour or (e or i) not in minute:
              print('Please input the valid time!')
              continue
          elif len(s_lst)>14:
              print('Please input 14 valid information!')
              continue
          lst2.append(a)
          flight = Flight(s_lst[0],s_lst[1],s_lst[2],s_lst[3],s_lst[4],s_lst[5],s_lst[6],s_lst[7],s_lst[8],s_lst[9],s_lst[10],s_lst[11],s_lst[12],float(s_lst[13]))
          lst.append(flight)
          more_flights = input("Do you want to add another flight? yes or no: ")
          if more_flights.upper() != 'YES':
              break
      except BaseException:
          print('Please input the information according to the format!')
