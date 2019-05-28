# program to create a .xlsx file in current working dir.

# importing the libraries
from xlwt import Workbook as wb

# creating the empty .xlsx file
wb = wb()  

# adding the sheet named 'test' in .xlsx file.
sheet1 = wb.add_sheet('test')

# saving the xlsx file in current working directory with name example.
wb.save('example.xlsx')
