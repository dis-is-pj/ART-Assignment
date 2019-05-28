# Python program to detect Number of
# Characters and Words in a string

def char(a):
    # This function returns the number of
    # Characters in string a
    return(len(a))

def words(a):
    # This function returns the number
    # Words in string a

    # Number of Characters = Number of Spaces + 1
    s = a.count(' ')
    if a.count('  '):   # Taking care of the typing mistake.
        return(s+1-a.count('  '))    # When typer types 2 spaces acciedentally.
    else:
        return(s+1)

# Taking user input String
a = input('Please input a string\n')
print('Number of Characters:', char(a))
print('Number of Words:', words(a))
