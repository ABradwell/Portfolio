#Aiden Stevenson Bradwell
#September 25th, 2018


def integerprint(a,b) :
    if a < b :
        num = a
        print (a)
        while num < b:
            num = num + 1
            print(num)
    else:
        num = b
        print (b)
        while num < a:
            num = num + 1
            print(num)


            
a = int(input("Please enter the first integer:  "))
b = int(input("Please enter the second integer:  "))
integerprint(a,b)
