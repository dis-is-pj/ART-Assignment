def fun(s):
    a = list(s)
    i = 0
    while(i<len(a)):
        if not((ord(a[i])<=ord('z') and ord(a[i])>=ord('a'))
        or (ord(a[i])<=ord('z') and ord(a[i])>=ord('a'))):
            a.pop(i)
        else:
            i += 1

    return ''.join(a)

s = input('Please enter a string\n')
print(fun(s))
