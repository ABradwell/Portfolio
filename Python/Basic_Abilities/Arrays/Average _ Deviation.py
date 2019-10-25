#Assignment Four
#October 9th, 2018
#AIden Stevenson Bradwell
import math
def averagecalc(lista):
    #This function begins the proccess of finding the average
    i = 0
    average = 0
    while i < len(lista):
        average = lista[i] + average
        i = i+1
    average = average / len(lista)
    return average

def deviation(a,lista):
    #This function begins the proccess of finding the deviation
    i = 0
    total = 0
    while i < len(lista) :
        squared =  (lista[i] - a)
        squared = squared*squared
        total = total + squared
        i = i + 1
    s = math.sqrt(total / (len(lista )- 1))
    return s


#### MAIN PROGRAM ####
lista = list(eval(input('Please enter a list of numbers:   ')))
a = averagecalc(lista)
s = deviation(a,lista)
print('The Standard Deviation is ', s) 
