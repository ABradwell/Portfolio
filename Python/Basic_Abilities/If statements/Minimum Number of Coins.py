#Homework Assignment One:
#Aiden Stevenson Bradwell
#SEptember 14th, 2018
#Calculate the least amount of coins needed for a cashier to give back
#Approach, largest coin = 25, so find if 25 can be removed, then  5, and so on...


#Set up for loop
run = True
#Initialize both moneyowed, and the coins owed thus far
coinsowed = 0
moneyowed = float(input("Please enter amount of money owed:  (W/O $)    "))
#Makes money owed a logical number, easier to calculate with
moneyowed = moneyowed*100
#Begin loop of calcuating
while run == True:
    #Is it greater than a quarter?
     #Subtract a quarter if it is
    if (moneyowed >= 25) :
        moneyowed = moneyowed - 25
        coinsowed = coinsowed + 1
    #Is it greater than a dime?
         #Subtract a dime if it is
    elif (moneyowed <25 and moneyowed >= 10) :
        moneyowed = moneyowed - 10
        coinsowed = coinsowed + 1
    #Is it greater than a nickel?
         #Subtract a nickel if it is
    elif(moneyowed <10 and moneyowed >= 5) :
        moneyowed = moneyowed - 5
        coinsowed = coinsowed + 1
    #Is it greater than a penny?
        #Subtract a penny if it is
    elif (moneyowed <5 and moneyowed >= 1) :
        moneyowed = moneyowed - 1
        coinsowed = coinsowed + 1
    #There is no more money owed, print results
    else :
        print("The Minimum number of coins the cashier can return is: ", coinsowed)
        run = False
