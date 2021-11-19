#AIden Stevesnon Bradwell
#September 25th, 2018
#Exercise Four

a = float(input("Please enter an a value: "))
b = float(input("Please enter a b value: "))
c = float(input("Please enter a c value: "))

determine = (b*b) - (4*a*c)
if determine < 0:
    print ("No real roots. ")
if determine == 0:
    print("One real root. ")
if determine > 0:
    print("Two real roots")
