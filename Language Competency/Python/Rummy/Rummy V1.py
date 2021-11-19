#Aiden Stevenson Bradwell
#October 19th 2018
#Assignment Three
#Rummy Game

import random


def startup():
    print('WELCOME TO THE RUMMY BOT')
    print('The standard deck has 52 cards: 13 ranks times 4 suits')
    check = True
    while check:
        choice = input('Would you like to change the number of cards by changing the number of ranks?   ')
        if choice.upper() == 'YES':
            run = True
            while run:
                rank = float(input('Enter a number between 3 and 99, for the number of ranks:'))
                if rank < 100 and rank > 0:
                    run = False
                check = False
        else:
            rank = 13
            check = False

    return rank


def deckcreation(rank):
    ''' int --> list
        This function takes in the rank, and then creates a deck for each suit with that number of cards in it.
        These 4 decks are then mixed into the strange Deck
        This Strange deck is returned
    '''
    
    stackone = []#Initialize a series of decks
    stacktwo = []    
    stackthree = []    
    stackfour = []
    deck = []
    run = True    ##Initialize the variables for the deck creation
    base = 100
    size = 0
    i = 1
    while i < (rank +1):    ##Create the first suit
        stackone.append(base + i)
        i = i + 1
    base = base + 100
    i = 1
    while i < (rank +1):    ##Create the second suit
        stacktwo.append(base + i)
        i = i + 1
    base = base + 100
    i = 1
    while i < (rank +1):    ##Create the third suit
        stackthree.append(base + i)
        i = i + 1
    base = base + 100
    i = 1
    while i < (rank +1):    ##Create the fourth suit
        stackfour.append(base + i)
        i = i + 1
        
    ##Create the strange deck
    while size < (rank*4):    ##Randomly create a number that chooses the suit 1-4
        suit = random.randint (1,4) 
        card = random.randint(1,rank)    ##Chooses a random rank from that deck
        if suit == 1:    ##If in rank one
            addedcard = 100 + card    ##Creates card to be added to strange deck
            inset = addedcard in stackone
            if inset == True:    ##checks if this card is still to be adde to the strange deck
                deck.append(addedcard)
                stackone.remove(addedcard)
                size = size + 1
        elif suit == 2:   
            addedcard = 200 + card    ##Creates card to be added to strange deck
            inset = addedcard in stacktwo
            if inset == True:    ##checks if this card is still to be adde to the strange deck
                deck.append(addedcard)    ##Add card to strange deck
                stacktwo.remove(addedcard)    ##Remove card from original suit deck
                size = size + 1
        elif suit == 3:
            addedcard = 300 + card    ##Creates card to be added to strange deck
            inset = addedcard in stackthree
            if inset == True:    ##checks if this card is still to be adde to the strange deck
                deck.append(addedcard)    ##Add card to strange deck
                stackthree.remove(addedcard)    ##Remove card from original suit deck
                size = size + 1
        else:
            addedcard = 400 + card    ##Creates card to be added to strange deck
            inset = addedcard in stackfour
            if inset == True:    ##checks if this card is still to be adde to the strange deck
                deck.append(addedcard)    ##Add card to strange deck
                stackfour.remove(addedcard)   ##Remove card from original suit deck
                size = size + 1
    return deck    ##Returns strange deck

def handupdate(deck, rank):
    ''' List, Int ---> List
        This function takes the list, adn the rank, and creates the intiial player's hand from the deck. It then removes those cards from the deck
    '''
    
    if rank > 1:    ##This assures that the rank is large than 1 (Otherwise the decksize is not 7 large)
        playerhand = [deck[0], deck[1],deck[2],deck[3],deck[4],deck[5],deck[6]]    ##Initialize the hand
        deck.remove(playerhand[0])    ##Remove the cards from the deck
        deck.remove(playerhand[1])
        deck.remove(playerhand[2])
        deck.remove(playerhand[3])
        deck.remove(playerhand[4])
        deck.remove(playerhand[5])
        deck.remove(playerhand[6])
    else:
        playerhand = [deck[0], deck[1],deck[2],deck[3],deck[4]]    ##Initialize the hand
        deck.remove(playerhand[0])    ##Remove the cards from the deck
        deck.remove(playerhand[1])
        deck.remove(playerhand[2])
        deck.remove(playerhand[3])
    return playerhand


def rolldice(deck):
    ''' Null --> Int:
        Randomly rolls the dice, and produces a number 1 thorugh 6
    '''
    roll = random.randint(1,6)    ##Rolls the dice randomly
    redundant = input('Please roll the Dice')    ##Allows the player to feel in control of the roll
    if deck == []:
        roll = 1
    print('You rolled the dice and it shows:', roll)    ##Then tells them what it already is
    return roll





def discard(playerhand, deck, rounds):
    '''  List, List, Int ---> List, List, Int
        Gives the player the ability to remove a card in their hand
        Player is given the choice and then can choose to remove or pass
    
    '''
    outerrun = True    ##Initialize the input loops
    innerrun = True
    while outerrun:    ##Player makes a choice
        choice = input('Would you like to discard a card? [Yes/No]:     ')
        if choice == '':
            choice = 0 
        if choice.upper() == 'NO' :    ##If they choose not  to, the round just increases
            outerrun = False
        elif choice.upper() == 'YES':    ##Otherise if they said yes, they can delete a card
            outerrun = False    ##gets out of the outter loop
            handorganize(playerhand, rank)    ##Prints player's hand
            while innerrun:    ##Begins the inner input
                deletechoice = int(input('Please enter the card number you would like to discard: '))    ##Asks for a card 
                inhand = deleteinhandcheck(deletechoice, playerhand)    ##Makes sure card is in their hand
                if inhand == True:    ##If they have the card to be deleted
                    if deletechoice in playerhand:
                        index = playerhand.index(deletechoice)
                        del playerhand[index]
                        innerrun = False
                    else:
                        print('GAME OVER NEEDED HERE')    ##If the deck has no more cards the game is over  
                        innerrun = False   ##Exit out of loops
                        outerrun = False
                else:    ##If they dont have the card it keeps asking
                    innerrun = True
        else:    ##If they dont type yes or no it loops
            outerrun = True
    rounds = rounds + 1    ##Returns the updated hand and deck, wiht what round the player is on
    return deck, playerhand, rounds





def meldremove(deck, playerhand, meld):
    ''' List, List, List ---- > List, List
        This deletes a meld from the players hand, and then returns the hand
    '''
    for b in meld:
        if b in playerhand:
            index = playerhand.index(b)
            del playerhand[index]
    return deck, playerhand

def elseroll(roll, playerhand, deck):
    ''' Int, List, List ---> List, List
    This function  adds either cards in the quanitity of the roll, or all remaining cards in the deck (should the deck be smaller than the roll)
'''
    if roll < len(deck): #If there are more cards in the deck than the number on the dice
        i = 0        #Setup the loop
        while i < roll:        #Wile still wihtin the list
            playerhand.append(deck[0])            #Adds card from the top of the deck
            deck.remove(deck[0])            #Removes that card
            i = i+1            #Sets up index
    else:        #If deck is too small
        i = 0
        top = len(deck)
        while i < top:      #Adds from deck until deck is empty
            playerhand.append(deck[0])            #Deletes added card from deck
            deck.remove(deck[0])
            i = i+1    #Calls upon the playershand print fucntion

    handorganize(playerhand, rank)      #Gives back the updated deck and players hand
    return deck, playerhand

def deleteinhandcheck(delete, playerhand):
    ''' Int, List --> Boolean
    Takes the card trying to be deleted, and check to amke sure it is in the players hand
    '''

    inhand = False    #Initialize if in hand
    if delete in playerhand:    #If the card is in their hand
        inhand = True             #Return that it is
    else:
        inhand = False        #Otherwise let them know, return that it isnt
        print('Card ', delete, 'is not in your hand')
    return inhand
    

def inhandcheck(meld, playerhand):
    ''' List, List ---> List
    This function checks to amke sure that the meld is in the players hand '''

    inhand = True    #Initialize
    inhandcount = 0    
    for v in meld:      #begin for each card in meld
        if v in playerhand:        #Compare that card to each of the players hand
            math = 1 + 1            #void section
        else:
            inhand = False            #Otherwise, they are informed
            print('Card ', v, 'is not in your hand')
    return inhand


def handorganize(playerhand, rank):
    ''' List --->Null
        This function organizes and  prints the players hand in two different ways'''

    

    suitedhand = []    #Initialize the lists needed
    rankedhand = []
    mathhand = playerhand.copy()
    index = 0
    s1arr = []
    s2arr = []
    s3arr = []
    s4arr = []


    
    #TO ORGANIZE BY SUIT

    for v in playerhand:     #For every card in the hand
        a = v // 100        #Gets on the first number
          #Takes the first number, and then appends that variable to the list of the corrosposning number
        if a == 1:
            s1arr.append(v)
            s1arr.sort()
        elif a == 2:
            s2arr.append(v)
            s2arr.sort()
        elif a == 3:
            s3arr.append(v)
            s3arr.sort()
        else:
            s4arr.append(v)
            s4arr.sort()
    #Combines all sorted suits into one list to print
    suitedhand = s1arr + s2arr + s3arr + s4arr
    rank = rank + 1
    rank = int(rank)
    for rankadd in range(rank) :
        if (rankadd+100) in s1arr:
            rankedhand.append(rankadd+100)
        if (rankadd+200) in s2arr:
            rankedhand.append(rankadd+200)
        if (rankadd+300) in s3arr:
            rankedhand.append(rankadd+300)
        if (rankadd+400) in s4arr:
            rankedhand.append(rankadd+400) 
    if suitedhand == []:  ##If the llist is empty, print an empty space
        print ('\n Here is your new hand printed in two ways:\n')
        print ('\n \n ')
    else:    ##While there is something in the list, print it
        print ('\n Here is your new hand printed in two ways:\n')
        print( suitedhand, '\n')
        print (rankedhand)
        print (len(suitedhand))
def meldcheck(meld,inhand):
    ''' List --> Boolean, Boolean
        This fucntion checks to see whether the list is a meld or a progression
    '''
    
    meldy1 = False    ##Initialize the loops and arrays hello thre
    alreadyprinted = False
    meldy2 = False
    progressionlist = []
    meldlist = []
                                                               ##############   Check for a Set  Begins      ##############
    #Create a list of the set in form of it's ranks, regardless fo the suit
    for v in meld:
        a = v %100
        progressionlist.append(a)
    index = 0     #prepare actual check 
    while index + 1 < len(progressionlist):     #Loop thorugh the meld, and checks to make sure that the ranks are the same thorughout
        if progressionlist[index + 1] == progressionlist[index]:
            meldy1 = True
            index = index + 1
        else:         #If the entered set doesn't  exist, a False will be returned
            meldy1 = False
            index = 1000
            alreadyprinted = True
    if len(progressionlist) < 2 and meldy1 == True:    #Check to make sure that the progression is the proper length
        meldy1 = False
        alreadyprinted = True
        print('Invalid sequence. Discardable set needs to have at least 2 cards.')

                                                    ############## Check for a progression  Begins  ##############
    if meldy1 == False:
        for v in meld:        #Create array in 
            meldlist.append(v)
        index = 0
        while index+1 < len(meldlist):        #Loop thorugh the meld ot make sure that the meld progresses based on rank
            if meldlist[index + 1] == meldlist[index] + 1:
                meldy2 = True
                index = index + 1
                alreadyprinted = True
            else:            #If there is an object outside of the progression, Flase is returned
                meldy2 = False
                index = 1000
            if len(progressionlist) < 3 and meldy2 == True:            #Check the length of the set. Assures it is not too short
                meldy2 = False
                alreadyprinted = True
                print('Invalid input. Discardable progression needs to have at  least  3 cards.')
    else:
        meldy2 = False
    return meldy1, meldy2




def move(deck, playerhand,rounds):
    ''' List, List, Int -----> Int, List, List
    This function is where the actual players turn occurs. This is where they choose if they would like to make melds, progressions, or even delete a card. 
    '''
    run = True     ##Setup the hand checks
    innerrun = True
    outterrun = True
    cancleinner = False
    while outterrun:    #Begin outter check
        choice = input('Yes or no, do you have a sequences of three or more cards of the same suit or two or more of a kind? ')        ##Sees if player wants to make melds
        innerrun = True        
        if  cancleinner:            ##Decides whether or not it should continue to ask the question, based on if they have already answered the following question
            innerrun = False
        if choice.upper() == 'YES':        ##If the want to make a meld
            while innerrun:
                raw_input = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ").strip().split()                ##Creates a list of the meld
                meld = raw_input
                index = 0
                for v in raw_input:
                    if v == ' ' :
                        meld[index] = 'X'
                    else:
                       meld[index] = float(v)
                    index = index + 1
                if len (meld) == 0:
                    meld = [0]
                inhand = inhandcheck(meld, playerhand)      ##Checks that the player actually has the cards
                if inhand == True:                    ##Checks if its a meld or progression
                    meldly1, meldy2 = meldcheck(meld,inhand)
                if inhand == True:                ##If they have the cards
                    if meldly1 == True or meldy2 == True :               ##And the cards are either a meld or a progression
                        if inhand == True:
                            run = False
                            deck, playerhand = meldremove(deck, playerhand, meld)      ##removes the meld or progression from the hand
                            handorganize(playerhand, rank)
                    else:
                        math = 1 + 1
                    innerrun = False
                else:
                    innerrun = False
        elif choice.upper() == 'NO':        ##If they dont want to make a meld or progression, the game just continues to the next round
            outterrun = False            ##Breaks free
            innerrun = False
            rounds = rounds + 1            ##round is added
    else:
        math = 1 + 1        ##Void math fucntion to keep loop going
    return rounds, deck, playerhand 


def emptydeckcheck(deck):
    ''' List ---> Boolean
        Finds if the deck is now empty'''
    deckempty = False
    if deck == []:
        deckempty = True
    else:
        deckempty = False
    return deckempty


########################################

game = True         ##Begins actual game loop
rank = startup()         ##Finds if the player wants to change the rank
deck = deckcreation(rank)         ##creates the strange deck
print('You are playing with a deck of ',len(deck), 'cards')         ##Prints the information of the deck
playerhand = handupdate(deck,rank)         ##Creates the players intial deck
handorganize(playerhand, rank)         ##Prints the information of the players hand
rounds = 1         ##Sets the round to begin
while game:
    print('Welcome to Round',rounds)         ##Prints the menu which they see
    deckempty = emptydeckcheck(deck)         
    if deckempty == False:         
        roll = rolldice(deck)         ##Has the player roll
        if roll == 1 :         ##Checks what they roll, and reacts accordingly
            deck, playerhand,rounds = discard(playerhand, deck,rounds)         ##Goes into the card discard function 
        else:         #
            print('Since your rolled, ', roll, ' the following', roll, 'or', len(deck), ' (if the deck has less than', roll, 'cards) will be added to your hand from the top of the deck')         ##Lets them know what has been added to their deck
            deck, playerhand = elseroll(roll, playerhand, deck)         ##Actually adds those cards to the hand
            rounds, deck, playerhand = move(deck, playerhand,rounds)         ##Has the player make melds or progressions
    else:
        if playerhand == []:
            print('CONGRAGULATIONS! YOU HAVE COMPLETED THE GAME IN', rounds,'ROUNDS!')
            game = False
        else:
            print('The game is in empty deck phase.')
            print('Discard any card of your choosing.')
            delete = float(input('Which card would you like to discard?'))
            inhand = deleteinhandcheck(delete, playerhand)
            if delete in playerhand:
                index = playerhand.index(delete)
                del playerhand[index]
            if playerhand == []:
                print('\n\n\n CONGRAGULATIONS! YOU HAVE COMPLETED THE GAME IN', rounds,'ROUNDS!')
                game = False
    





            
