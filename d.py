# function to extract the numeric value from a string
# considering there is only one numeric value in given string
def fun(s):
    a = ''
    f = 0
    for i in range(len(s)):
        if f==0 and (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
            f = 1
            a = s[i]
        elif f==1 and (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
            a = a + s[i]
    # if there are more than one numeric value in the string
    # the function will only return the value appeared first from left
    return int(a)

s = input('Please enter a string\n')
print(fun(s))
