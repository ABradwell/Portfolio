#Assignment Four
#October 16th, 2018
#Aiden Stevenson Bradwell

def withcount(c, chain):
    count = chain.count(c)
    return count




def withloop(c,chain):
    count = 0
    for var in chain:
        if var == c:
            count = count + 1
    return count


s = input('Please enter a string: ')
two =withloop('a', s)
print ( two)
two =withloop('dela', s)
print ( two)
one = withcount('a', s)
print (one)
