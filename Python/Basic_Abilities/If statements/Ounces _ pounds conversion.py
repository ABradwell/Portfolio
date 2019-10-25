#Homework Assignment One:
#Aiden Stevenson Bradwell
#SEptember 14th, 2018
#Prompt the user to enter the weight in pounds and ounces, and have your program print the weight in kilograms


#Receives input
pounds = float(input('Please enter the amount of pounds: '))
ounces = float(input('Please enter the amount of ounces'))
#COnverts input to float format, for formatting results
poundconversion = 0.453592
ounceconversion = 0.453592/16
#Calculates the weight in kilgrams
kilogram_temp = pounds*poundconversion
#1 ounce = 1/16 pounds| therefore ounce/35.2
kilogram = kilogram_temp + ounces*ounceconversion
#Print answer
print( pounds ,' pounds and ',ounces,' ounces is aproximatley:  ',kilogram,' KG')
