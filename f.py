class date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2001

    def input(self, a):
        print(a)
        self.day = int(input('Enter the Day : '))
        self.month = int(input('Enter the Month : '))
        self.year = int(input('Enter the Year : '))

    def print(self):
        print(str(self.day)+ '/' + str(self.month) + '/' + str(self.year))

day1 = date()
day2 = date()
day1.input('Enter date for day1')
print('\n')
day2.input('Enter date for day2')

s = 0
s = s + (day1.year - day2.year)*(365*24*60*60)
s = s + (day1.month - day2.month)*(30*24*60*60)
s = s + (day1.day - day2.day)*(24*60*60)

print(abs(s))











        
    
