#Aiden Stevenson Bradwell
#October 16th, 2018
#Assignment one

s1 = 'good'
s2 = 'bad'
s3 = 'crazy'

def a():
    global s1, s2, s3
    if 'azy' in s3:
        return True
    else:
        return False

def b():
    global s1, s2, s3
    if ' ' in s1:
        return True
    else:
        return False

def c():
    global s1, s2, s3
    return (s1 + s2 +s3)

def d():
    global s1, s2, s3
    cancat = (s1 + s2 + ' ' + s3)
    return (' ' in cancat)
    
def e():
    global s1, s2, s3
    return ( s3 * 10)

def f():
    global s1, s2, s3
    concat = (s1 + s2 + s3)
    return (len(concat))

a = a()
print (a)
b = b()
print (b)
c = c()
print (c)
d = d()
print (d)
e = e()
print (e)
f = f()
print (f)
