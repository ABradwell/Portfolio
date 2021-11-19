#AIden Stevenson Bradwell
#September 25th, 2018

def isDivisible(number):
    divide2 = number
    divide3 = number

    divisible2 = ((divide2 % 2) == 0)
    divisible3 = ((divide3 % 3) == 0)

    if divisible2 and divisible3:
        return 1
    elif divisible2 or divisible3:
        return 2
    else:
        return 0


number = float(input("Please enter a number: "))
determination = isDivisible(number)
if determination == 0:
    print("Not divisble by either 2 or 3")
elif determination == 2:
    print("Divisble by either 2 or 3")
else:
    print("Divisible by both 2 and 3")

    
