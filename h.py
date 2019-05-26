from xlwt import Workbook as wb
wb = wb()
sheet1 = wb.add_sheet('test')
wb.save('example.xlsx')
