#Exercise Three
#AIden Bradwell
#October 2nd,  2018
import random
'''Develop a software to play a guessing game. The programm
generate a number betweeen 1 and 10, and then ask the user to
guess it. If the user does not get it, the program indicate if it is
high or low and ask again the user to guess. One the user find the
response, a successful message comes up with the number of tries.
– Develop your algorithm. Convert in Python.
– The program must generate a random number snd cll the
l’algorithm/function guess(). It displays the successful
message and the number of tries as the result.'''

number = random.randint(1,10)
run = True
tries = 1
while run :
    guess = float(input('Please enter your guess:   '))
    if guess == number:
        print('Good job!')
        print ('Number of Tries: ' , tries)
        run = False
    else:
        print('This is wrong...')
        tries = tries +1
        
    
