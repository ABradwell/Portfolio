#Assignment Five
#October 16th, 2018
#Aiden Stevenson Bradwell

def  code(s):
    swapnum1 = 0
    swapnum2 = 1
    swapchar1 = ''
    swapchar2= ''
    slist = []
    while swapnum2 < len(s):
        swapchar1 = s[swapnum1]
        swapchar2 = s[swapnum2]
        slist.append(swapchar2)
        slist.append(swapchar1)
        swapnum1 = swapnum1 + 2
        swapnum2 = swapnum2 + 2
    slist = "".join(slist)
    return slist


s = 'Please consider this good enough'
slist = code(s)
print (slist)
