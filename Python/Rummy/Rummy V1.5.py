#Aiden Stevenson Bradwell
#October 19th 2018
#Assignment Three
#Rummy Game


import random


def make_deck(rank):
    ''' int --> list
        This function takes in the rank, and then creates a deck for each suit with that number of cards in it.
        These 4 decks are then mixed into the strange Deck
        This Strange deck is returned
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
        '''
    stackone = []   #Initialize a series of decks
    stacktwo = []    
    stackthree = []    
    stackfour = []
    deck = []
    run = True    ##Initialize the variables for the deck creation
    base = 100

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

    for rankadd in range(99) :
        if (rankadd+100) in stackone:
            deck.append(rankadd+100)
        if (rankadd+200) in stacktwo:
            deck.append(rankadd+200)
        if (rankadd+300) in stackthree:
            deck.append(rankadd+300)
        if (rankadd+400) in stackfour:
            deck.append(rankadd+400)
    
    
    return deck    ##Returns strange deck

def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    random.shuffle(deck)


def meldremove(playerhand, meld):
    ''' List, List, List ---- > List, List
        This deletes a meld from the players hand, and then returns the hand
    '''
    for b in meld:
        if b in playerhand:
            index = playerhand.index(b)
            del playerhand[index]
    return playerhand             


def deal_cards_start(deck) :
    '''(list of int)-> list of int
    Returns a list representing the player's starting hand.
    It is  obtained by dealing the first 7 cards from the top of the deck.
    Precondition: len(dec)>=7'''
    if len(deck) > 6:
     ##This assures that the rank is large than 1 (Otherwise the decksize is not 7 large)
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



def deal_new_cards(deck, playerhand, roll):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If  the number  of cards in the deck is less than num then then all the remaining cards are from the deck.
    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    if roll < len(deck): #If there are more cards in the deck than the number on the dice
        i = 0        #Setup the loop
        while i < roll:        #Wile still wihtin the list
            playerhand.append(deck[(len(deck) -1)])            #Adds card from the top of the deck
            deck.remove(deck[(len(deck) -1)])            #Removes that card
            i = i+1            #Sets up index
    else:        #If deck is too small
        i = 0
        top = len(deck)
        while i < top:      #Adds from deck until deck is empty
            playerhand.append(deck[(len(deck) -1)])            #Deletes added card from deck
            deck.remove(deck[(len(deck) -1)])
            i = i+1


    
def print_deck_twice(playerhand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''

    

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
    for rankadd in range(99) :
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
    

def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    
    inhand = True    #Initialize
    inhandcount = 0    
    for v in cards:      #begin for each card in cards
        if v in player:        #Compare that card to each of the players hand
            math = 1 + 1            #void section
        else:
            inhand = False            #Otherwise, they are informed
            print( v, 'not in your hand. Invalid input')
    return inhand



def is_discardable_kind(rawmeld):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    meld = rawmeld.copy()
    meld.sort()
    meldy1 = False    ##Initialize the loops and arrays
    progressionlist = []
    meldlist = []
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
    if len(progressionlist) < 2:    #Check to make sure that the progression is the proper length
        meldy1 = False
        print('Invalid sequence. Discardable set needs to have at least 2 cards.')
    return meldy1



def is_discardable_seq(rawmeld):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    meld = rawmeld.copy()
    meld.sort()
    meldy2 = False
    progressionlist = []
    for v in meld:        #Create array in 
        progressionlist.append(v)
    index = 0
    while index+1 < len(progressionlist):        #Loop thorugh the meld ot make sure that the meld progresses based on rank
        if progressionlist[index + 1] == progressionlist[index] + 1:
            meldy2 = True
            index = index + 1
        else:            #If there is an object outside of the progression, Flase is returned
            if (progressionlist[index + 1] - progressionlist[index]) > 99:
                print('Invalid sequence. Cards are not of same suit.')
            if (progressionlist[index + 1] - progressionlist[index]) < 99:
                print('Invalid sequence. Cards are not of same suit.')
            meldy2 = False
            index = 1000
    if len(progressionlist) < 3:            #Check the length of the set. Assures it is not too short
        meldy2 = False
        print('Invalid input. Discardable progression needs to have at  least  3 cards.')
    return meldy2

def rolled_one_round(playerhand):
   
    ''' (list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player = [201,212,311,102]
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in the deck. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 
    
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
            while innerrun:    ##Begins the inner input
                deletechoice = input('Please enter the card number you would like to discard: ')    ##Asks for a card 
                deletelist = []
                deletechoice = float(deletechoice)
                deletelist.append(deletechoice)
                inhand = is_valid(deletelist, playerhand)    ##Makes sure card is in their hand
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
    print_deck_twice(playerhand)


def rolled_nonone_round(playerhand):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
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
                inhand = is_valid(meld, playerhand)      ##Checks that the player actually has the cards
                if inhand == True:                    ##Checks if its a meld or progression
                    meldly1 = is_discardable_kind(meld)
                    meldy2 = is_discardable_seq(meld)
                    if meldly1 == False and meldy2 == False:
                        print('This is neither a valid sequence, or a valid kind. Please enter another choice.')
                if inhand == True:                ##If they have the cards
                    if meldly1 == True or meldy2 == True :               ##And the cards are either a meld or a progression
                        if inhand == True:
                            run = False
                            playerhand = meldremove(playerhand,meld)      ##removes the meld or progression from the hand
                            print_deck_twice(playerhand)
                    else:
                        math = 1 + 1
                    innerrun = False
                else:
                    innerrun = False
        elif choice.upper() == 'NO':        ##If they dont want to make a meld or progression, the game just continues to the next round
            outterrun = False            ##Breaks free
            innerrun = False
    else:
        math = 1 + 1        ##Void math fucntion to keep loop going
    return playerhand 
    
def emptydeckcheck(deck):
    ''' List ---> Boolean
        Finds if the deck is now empty'''
    deckempty = False
    if deck == []:
        deckempty = True
    else:
        deckempty = False
    return deckempty


### Main  ###
game = True         ##Begins actual game loop

print('WELCOME TO THE RUMMY BOT')
print('The standard deck has 52 cards: 13 ranks times 4 suits')
check = True
while check:
    choice = input('Would you like to change the number of cards by changing the number of ranks?   ')
    if choice.upper() == 'YES':
        run = True
        while run:
            rank = float(input('Enter a number between 3 and 99, for the number of ranks:   '))
            if rank < 100 and rank > 0:
                run = False
            check = False
    else:
        rank = 13
        check = False

deck = make_deck(rank)         ##creates the strange deck
shuffle_deck(deck)
print('You are playing with a deck of ',len(deck), 'cards')         ##Prints the information of the deck
playerhand = deal_cards_start(deck)       ##Creates the players intial deck
print_deck_twice(playerhand)         ##Prints the information of the players hand
rounds = 0         ##Sets the round to begin
while game:
    rounds = rounds + 1
    print('Welcome to Round',rounds)         ##Prints the menu which they see
    deckempty = emptydeckcheck(deck)         
    if deckempty == False:         
        roll = rolldice(deck)         ##Has the player roll
        if roll == 1 :         ##Checks what they roll, and reacts accordingly
            rolled_one_round(playerhand)         ##Goes into the card discard function 
        else:         #
            print('Since your rolled, ', roll, ' the following', roll, 'or', len(deck), ' (if the deck has less than', roll, 'cards) will be added to your hand from the top of the deck')         ##Lets them know what has been added to their deck
            deal_new_cards(deck, playerhand, roll)         ##Actually adds those cards to the hand
            print_deck_twice(playerhand)      #Gives back the updated deck and players hand
            playerhand = rolled_nonone_round(playerhand)         ##Has the player make melds or progressions
    else:
        if playerhand == []:
            print('CONGRAGULATIONS! YOU HAVE COMPLETED THE GAME IN', rounds,'ROUNDS!')
            game = False
        else:
            print('The game is in empty deck phase.')
            print('Discard any card of your choosing.')
            delete = input('Which card would you like to discard?')
            deletelist = []
            delete = float(delete)
            deletelist.append(delete)
            inhand = is_valid(deletelist, playerhand)
            if delete in playerhand:
                index = playerhand.index(delete)
                del playerhand[index]
            if playerhand == []:
                print('\n\n\n CONGRAGULATIONS! YOU HAVE COMPLETED THE GAME IN', rounds,'ROUNDS!')
                game = False
            rounds = rounds + 1

# YOUR CODE GOES HERE and in all of the above functions instead of keyword pass


  
