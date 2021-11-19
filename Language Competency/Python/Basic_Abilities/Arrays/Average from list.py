#Assignment One
#October 9th, 2018
''' Develop an algorithm to calculate the
average of a list elements. Implement your
algorithm in Python as a function.
• Develop a program that gets a list of values
from the user, call the l’algorithm/function
to calculate the average and print the
results.'''

def averagecalc(listo):
    addition = 0
    for i in listo:
        addition = addition + i
    average = addition / len(listo)
    return average


listone = input('Please enter a list of values, whihc will be averaged, seperated by commas:  ')
calclist = list(eval(listone))
average = averagecalc(calclist)
print('The average is :   ', average)
