# program to make .csv file from .xlsx in curren working directory.
# importing pandas library
import pandas as pd

# this function will read .xlsx from current working directory and write .csv.
def xl2csv(a):
    xl = pd.read_excel('mart.xlsx')
    xl.to_csv('mart_csv.csv', index = False, encoding = 'utf-8')

xl2csv(input('Enter the name of Excel file to convert into .csv'))
