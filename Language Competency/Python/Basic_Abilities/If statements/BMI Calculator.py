#Aiden Stevenson Bradwell
#September 25th, 2018
#Question Number One

### Calculations: BOdy weight / height / height
def bodymaxindex(height, weight):
    #BMI Calculations
    BMI = weight / (height*height)
    return (BMI)


### MAIN PROGRAM ###
#Gather input for calculations
height = float(input("Please enter your height in meters: "))
weight= float(input("Please enter your weight in kilograms: "))
#SEnd for calculations
BMI = bodymaxindex(height, weight)
#begin determination of weight adn print results
if  BMI < 18.5 :
    print("You are underweight.")
elif  BMI < 25 :
    print("You are of Normal Weight.")
elif  BMI < 30 :
    print("You are Overweight.")
else :
    print ("You are Obese")
