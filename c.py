# function to remove all the digits and special characters
def fun(s):  # parameter s : string
    a = list(s)
    i = 0
    while(i<len(a)):
        # using ascii value to check type of character
        if not((ord(a[i])<=ord('z') and ord(a[i])>=ord('a'))
        or (ord(a[i])<=ord('z') and ord(a[i])>=ord('a'))):
            a.pop(i)
        else:
            i += 1

    return ''.join(a)

# Taking user input
s = input('Please enter a string\n') 
print(fun(s))
