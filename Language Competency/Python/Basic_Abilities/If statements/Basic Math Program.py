#Aiden Stevenson Bradwell
#September 25th, 2018
#Question Number 3
import random

#Main menu Function
def menu ():
    #Print formatting
    print("\n\n\n /////////////// WELCOME ////////////////")
    print(" Please choose one of the following to learn...")
    print("0] Addition...")
    print("1] Multiplication...")
    #User chooses action
    choice = int(input(""))
    #Determines function called
    if choice == 0:
        test(choice)
    elif choice ==  1:
        test(choice)
    #validitiy check
    else:
        print("Choice is invalid...")
        print("EXITING PROGRAM")

    

def test(choice):
    if choice == 1:
        #Print instructions
        print("Lets see if you can do multiplication!")
        print("enter the solution to the following...")
        #initialize variables
        i = 0
        right = 0
        questions = 0
        #Start questioning loops
        while i < 10:
            #sets up how many times its circle
            i = i+1
            #initiates random variable
            a = random.randint( 0 , 10)
            b = random.randint(0,10)
            #sets answer of random ints
            answer = a * b
            #prints questions
            print ( a, " x ",  b)
            #Gets user input
            studentanswer = int(input("Your answer : "))
        #Checks if the student was right
            if studentanswer == answer :
                print("Correct!")
                right = right +1
                questions = questions + 1
            else :
                print("Incorrect!")
                questions = questions + 1
        # Print right/wrong ratio
        print ("Right/Wrong ratio :", right, "/", questions)
        if  right > 5 :
            print("Congratulations!")
        else:
            print("Please ask your teacher for help")
    else :
        #Print instructions
        print("Lets see if you can do addition!")
        print("enter the solution to the following...")
        #initialize variables
        i = 0
        right = 0
        questions = 0
        #Start questioning loops
        while i < 10:
            #sets up how many times its circle
            i = i+1
            #initiates random variable
            a = random.randint( 0 , 100)
            b = random.randint(0,100)
            #sets answer of random ints
            answer = a + b
            #prints questions
            print ( a, " + ",  b)
            #Gets user input
            studentanswer = int(input("Your answer : "))
        #Checks if the student was right
            if studentanswer == answer :
                print("Correct!")
                right = right +1
                questions = questions + 1
            else :
                print("Incorrect!")
                questions = questions + 1
        # Print right/wrong ratio
        print ("Right/Wrong ratio :", right, "/", questions)
        if  right > 5 :
            print("Congratulations!")
        else:
            print("Please ask your teacher for help")

#Assures that the program keeps going
run = True
while run :
    menu()
