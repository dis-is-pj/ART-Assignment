
# function to check if the word starts with a vowel of not
def isvowel(a):
    l = [ord('a'),ord('A'),ord('e'),ord('E'),ord('i'),ord('I'),ord('o'),ord('O'),ord('u'),ord('U')]
    if l.count(ord(a[0])):
        return 1
    else:
        return 0

# this function will print number of occurences of words started with a vowel
def f(a): # parameter a : a list of many strings
    i = 0
    while(i<len(a)):
        if isvowel(a[i]):
            a[i] = a[i].lower()
            i += 1
        else:
            a.remove(a[i])
    b = list(set(a))
    for i in range(len(b)):
        print(b[i],' : ', a.count(b[i]))


a = ['apple', 'word', 'prince', 'Apple', 'Eye', 'eye', 'Uncle', 'uncle']
f(a)
