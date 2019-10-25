#Aiden Stevenson Bradwell
#September 25th, 2018

activities = ['swimming','soccer','volleyball','skiing']
temp = float(input("Please enter the temperature: "))

if temp > 79 :
    choice = 0
elif 59< temp < 80 :
    choice = 1
elif 39< temp < 60:
    choice = 2
else :
    choice = 3
print("Suggested activity : ", activities[choice])
