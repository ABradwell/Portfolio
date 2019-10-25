'''
• Searching an element in an array
Create a function that takes an array and an integer v,and
returns True if v is in the array / list 2D (False otherwise).

• The function should be efficient and stop searching the 2
loops as soon as possible. the function should add a variable
N steps to count the number of steps used by the algorithm
when loops execute then display that information.
 
• The main program takes an array / list 2D, call the function,
and display the result.
'''

def find_m(M, v):
      step = 0
      breakout = False
      for w in M:
            if breakout:
                  break
            for i in w:
                  step = step + 1
                  if i== v:
                        N = step
                        inarr = True
                        breakout = True
                        break
                  else:
                        N = 'Not Found'
                        inarr = False
      return(N, inarr)

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
N, inarr = find_m(M, v)
print('Number of steps:', N)
print(inarr)







            
