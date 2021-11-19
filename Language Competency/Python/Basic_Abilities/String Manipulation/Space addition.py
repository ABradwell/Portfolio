#Assignment Five
#October 16th, 2018
#Aiden Stevenson Bradwell

def spaces(s):
    for var in s:
        s = s.replace (var, var + ' ')
    return s

s = input('Please enter a string: ')
s = spaces(s)
print (s)
