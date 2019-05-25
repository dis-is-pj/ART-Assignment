def fun(s):
    a = ''
    f = 0
    for i in range(len(s)):
        if f==0 and (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
            f = 1
            a = s[i]
        elif f==1 and (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
            a = a + s[i]
    return int(a)

s = input('Please enter a string\n')
print(fun(s))
