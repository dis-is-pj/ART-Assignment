# program to delete all .xlsx files from current working dir.
# impoting libraries
import os

# this function will remove all files with extension .xlsx
def rmv_all(suf = '.xlsx'):
    lst = os.listdir()
    a = [x for x in lst if x.endswith(suf)]
    for i in range(len(a)):
        os.remove(a[i])

rmv_all()

