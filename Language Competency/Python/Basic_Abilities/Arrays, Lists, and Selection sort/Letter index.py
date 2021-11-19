'''Searching for an element in a list (linear
search)
• Create a function that takes a list and an integer v, and
returns True if v is in the list (False otherwise). The
function should be efficient and stop searching as soon as
possible.

• The main program must generate a very large list with
random elements, call the function to search a value and
display the result.

• Add in the function a variable N steps to count the number of
steps used by the algorithm (number of times the loop is
executed) and display a message with this information.

'''
import random
def find(l, v):
      step = 0
      inarr = False
      for w in l:
            step = step+1
            if w == v:
                  inarr = True
                  N = step
                  break
            else:
                  N = 'Not found'
      return(N, inarr)


n = 1000
l = []
for i in range(n):
      v = random.randrange(1,n+1)
      l.append(v)
v = int(input('Please enter an integer value to search the array for:   '))
N, inarr = find(l,v)
print ('Number of steps: ', N)
print(inarr)
