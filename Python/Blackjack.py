#AIden Stevenson Bradwell
#Rummy Game

from random import shuffle

class Blackjack:
     values={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
     def play(self):
          '''play a game'''   
          d = GameOfCards()
          d.mix()
          bank = Hand('Bank')
          player = Hand('Player')

          # gives two cards to the player and two to the bank
          for i in range(2):  
               player.addCard(d.getCard())
               bank.addCard(d.getCard())

          # show the hands
          print("Bank's Hand")
          bank.showHand()
          print("Player's Hand")
          player.showHand()

          # as long as the player ask for a Card!, The bank gets cards
          response = input('Would you like another Card? Yes or No? (By default Yes) ')
          while response in ['','y','Y','yes','YES']:
               c = d.getCard()
               print("You Draw the Card:")
               print(c)
               player.addCard(c)
               playervalue = self.total(player)
               if  playervalue > 21:
                    print("You have passed 21. You have lost.")
                    break
               print("Player's Hand")
               player.showHand()
               response = input('Would you like another Card? Yes or No? (by default Yes) ')

# the bank play with those rules  
          while self.total(bank) < 17:
               c = d.getCard()
               print("The bank has:")
               print(c)
               bank.addCard(c)
               if self.total(bank) > 21:
                    print("The bank has passed 21. You have won.")
                    break
               print("Bank's Hand")
               bank.showHand()

  # if 21 is has not been passed, compare the hands to find the winner  
               self.compare(bank, player)

          if self.total(bank) >= 17 and response  not in ['','y','Y','yes','YES']:
               self.compare(bank, player)
               

      
     def total(self, hand):
          ''' (Hand) -> int
          calculate the sum of all the cards' values in the hand
          '''
          inhand = False
          total = 0
          for card in hand.playerhand:
               if card.value in ['1','2','3','4','5','6','7','8','9','10']:
                    total = total + int(card.value)
               else:
                    if card.value == 'A':
                         inhand = True
                    val = 10
                    total = total + 10
                
          if inhand and total > 21:
               total = total - 10
          return total 

     def compare(self, bank, player):
          '''(Hand, Hand) -> None Compare the Hand of the player with the hand of the bank and display the messages'''
          # call the method self.total for the bank and for the player
          playertotal = self.total(player)
          banktotal = self.total(bank)
          if banktotal > playertotal:   
               print('You have lost.')
          elif playertotal > banktotal:
               print('You have won.')
          else:
               for card in player.playerhand:
                    if card.value == 'A':
                         aceinphand = True
                    elif card.value == 'K':
                         loginphand = True
                    elif card.value == 'Q':
                         loginphand = True
                    elif card.value == 'J':
                         loginphand = True
                    elif card.value == '10':
                         loginphand = True
               for card in bank.playerhand:
                    if card.value == 'A':
                         aceinbhand = True
                    elif card.value == 'K':
                         loginbhand = True
                    elif card.value == 'Q':
                         loginbhand = True
                    elif card.value == 'J':
                         loginbhand = True
                    elif card.value == '10':
                         loginbhand = True
               if aceinphand == aceinbhand == loginphand == loginbhand:
                    print('This is a draw.')
               elif aceinbhand and loginbhand:
                    if aceinphand == False or loginphand == False:
                         print('You have lost.')
               elif aceinphand and loginphand:
                    if aceinbhand == False or loginbhand == False:
                         print('You have won.')


class Hand(object):
     '''represents a Hand of cards to play'''

     def __init__(self, player):
          '''(Hand, str)-> none
          initializes the player's name and the card list with list being empty'''
          self.playerhand = []
          self.name = player
        
     def addCard(self, card):
          '''(Hand, Card) -> None
          add a card to the hand'''
          self.playerhand.append(card)

     def showHand(self):
          '''(Hand)-> None
          display the player's name and the hand'''
          for card in self.playerhand:
               print("{0} {1}".format(card.value,card.color))

     def __eq__(self, other):
          '''returns True if the hands have the same cards in the same order'''

          index = 0
          while index < len(self.playerhand):
               if self.playerhand[index] == other.playerhand[index]:
                            answer = True
               else:
                            answer = False
                            break
          return answer
                            
     def __repr__(self):
          '''returns a representation of the object'''

          print(self.name , "'s Hand...")
          for i in range(0, len(self.playerhand)):
               print(self.playerhand[i])

class Card:
     '''represente a card to play'''

     def __init__(self, value, color):
          '''(Card,str,str)->None        
          initializes the value and the color of the card'''
          self.value = value
          self.color = color  # spade, heart, club or diamond

     def __repr__(self):
          '''(Card)->str
          returns the representation of the object'''
          return 'Card('+self.value+', '+self.color+')'

     def __eq__(self, other):
          '''(Card,Card)->bool
          self == other if the value and color are the same'''
          return self.value == other.value and self.color == other.color

class GameOfCards:
     '''Represent the game of 52 cards'''
     # values and colors are variables of class
     values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
     colors = ['\u2660', '\u2661', '\u2662', '\u2663']
     # colors is a set of 4 symbols Unicode that represents the 4 colors
     # spade, heart, club or diamond

     def __init__(self):
          'initializes the packet of 52 cards'
          self.packet = []          # packet is empty at the start
          for color in GameOfCards.colors: 
               for value in GameOfCards.values: # variables of the class
               # add a card of value and color
                    self.packet.append(Card(value,color))

     def getCard(self):
          '''(GameOfCards)->Card
          distribute a card, the first from the packet'''
          return self.packet.pop()

     def mix(self):
          '''(GameOfCards)->None
          to mix the card game'''
          shuffle(self.packet)

     def __repr__(self):
          '''returns a representation of the object'''
          return 'Packet('+str(self.packet)+')'

     def __eq__(self, other):
          '''return True if the packets are the same cards in the same order'''
          return self.packet == other.packet


b = Blackjack()
b.play()

