# Program to tell diffrence between two dates in seconds

# creating a data type of date.
class date:
    def __init__(self):
        self.day = 1     # setting the default date 01/01/2001
        self.month = 1
        self.year = 2001

    def input(self, a):  # input function for date
        print(a)
        self.day = int(input('Enter the Day : '))
        self.month = int(input('Enter the Month : '))
        self.year = int(input('Enter the Year : '))

    def print(self):    # printing function for date
        print(str(self.day)+ '/' + str(self.month) + '/' + str(self.year))

# taking two dates as input from user
day1 = date()
day2 = date()
day1.input('Enter date for day1')
print('\n')
day2.input('Enter date for day2')

s = 0                                             # it is condidered that a year has 365 days and a month has 30 days.
s = s + (day1.year - day2.year)*(365*24*60*60)    # adding difference of years
s = s + (day1.month - day2.month)*(30*24*60*60)   # adding difference of months
s = s + (day1.day - day2.day)*(24*60*60)          # adding difference of days

print(abs(s))











        
    
