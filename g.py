def fun(a):
    for i in range(len(a)):
        if (ord(a[i])>=ord('a') and ord(a[i])<=ord('z')) or (ord(a[i])>=ord('A') and ord(a[i])<=ord('Z')):
            print(a[i],' is a character')

        elif (ord(a[i])>=ord('0') and ord(a[i])<=ord('9')):
            print(a[i],' is a number')

        elif ord(a[i])>20:
            print(a[i],' is a special character.')

s = input("Enter a string with all kind of characters : ")
a = list(s)
fun(a)
        
            
        
