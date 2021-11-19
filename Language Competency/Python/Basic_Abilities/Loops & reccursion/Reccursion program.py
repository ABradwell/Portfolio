#Assignment 2
#December 3rd, 2018
#Aiden Stevenson Bradwell

def stars(n):
     '''
     int---> null
     prints a series of stars in descending and ascending quanitity
     '''
     if n  > 1:
          print('*' * n)
          n = n-1
          stars(n)
          if n == 1:
               print('*')
          n = n + 1
     print('*' *n)
     
     
def sumListPos_rec (lis,items):
     '''
     list, int ---> int
     outputs the total of all positive integers in the list
     '''
     overall = 0
     if items > 0:
          items = items -1
          overall = sumListPos_rec(lis,items)
          items = items + 1
     if items < len(lis):
          if lis[items] > 0:
               value = lis[items]
          else:
               value = 0
     else:
          value = 0
     return overall + value



          
               
