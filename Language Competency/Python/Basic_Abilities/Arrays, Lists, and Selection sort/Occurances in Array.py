
'''
Compter le nombre d’occurrences d'un élément dans une matrice
• Create a function that takes an array and an integer v,
and returns the number of v occurrences in the array.
Add a variable Nsteps to count how many times the
loops have executed and display that information in a
message.
• The main program must take an array / list 2D, call the
function, and display the result.

'''

def account(M, v):
      NP = 0
      count = 0
      breakout = False
      for w in M:
            for i in w:
                  NP = NP + 1
                  if i== v:
                        count = count + 1
      return(count, NP)

M = []
run = True
while run:
      print('To continue without adding a new row, leave this part empty...')
      entered = input('Please enter a series of integers, split by spaces to add to the array in row format:   ').strip().split()
      newrow = []
      if entered == []:
            run = False
      else:
            for v in entered:
                  inty = int(v)
                  newrow.append(inty)
            M.append(newrow)
v = int(input('Please enter a number to be searched for: '))
count, NP = account(M, v)
print('Number of steps:', NP)
print('Number of times appeared', count)







            






            
