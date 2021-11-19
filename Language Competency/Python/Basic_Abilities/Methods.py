#AIden Stevenson Bradwell
#September 14th, 2018
#Homework Assignment 3
#Light Years
## Appraoch needed:


#Calcuations which turns light years into lightseconds
def secondcalcuations( days, hours, minutes, seconds, lightyears) :
    lightseconds = days * hours * minutes * seconds
    lightseconds = lightseconds * lightyears
    #Return nuber of seconds
    return lightseconds
#Calculations used to convert seconds into kilometers traveled
def  kilometerconversion( lightseconds):
    travel = lightseconds * 300000
    #Return # of kilometers
    return travel

#Initlaize the values of time
days = 365.26
hours = 24
minutes = 60
seconds = 60


#### || MAIN PROGRAM BEGINS || ####
#Begin User input
lightyears = float(input(" Please enter a number of light years: "))
#find seconds taken, print results
secondo = secondcalcuations( days, hours, minutes, seconds, lightyears)
print ("The number of seconds is: ", secondo)
#Find kilometers traveled, print results
travel = kilometerconversion( secondo)
print ("The distance is: ", travel)
#User inputs second set of information
firststar = float(input("Please enter distance to the first star, in light years: "))
secondstar = float(input("Please enter distance to the second star, in light years: "))
#calculates distance of stars
lightyears = firststar + secondstar
#FInd seconds between earth and stars
seconda = secondcalcuations (days,hours,minutes, seconds, lightyears)
#Finds distance ebtween earth adn stars, prints results
travel = kilometerconversion(seconda)
print ("The distance between two stars is: ", travel)
#### || MAIN PROGRAM TERMINATED || ####
