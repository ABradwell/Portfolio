'''
Count the number of an element
occurrences in a list
• Create a function that takes a list and an integer v, and
returns the number of occurrences of v is in the list. Add
the variable NP as to count number of times the loop
runs (and display a message).
• The main program should generate a list, call the
function, and display the result.
>>> l = 52 14 14 8 85 69 1 77 94 96 51 65 35 32 87 92 74 47 27 88 11 11 26 14 100 37 62 3 63 5 20 53 28 10 43 16 94 6 82 49 74 55 89 97 12 38 72 94 3 77 42 26 25 16 89 10 8 63 93 77 68 56 74 45 54 50 80 33 69 95 2 79 73 6 3 41 38 81 88 12 39 77 49 30 18 22 40 40 12 51 69 32 76 77 90 60 41 12 30 65
>>> account (l3,6)
Number of steps 100
2
'''

def account(M, v):
      NP = 0
      count = 0
      breakout = False
      for w in M:
            NP = NP + 1
            if w== v:
                  count = count + 1
      return(count, NP)

M = []
run = True
entered = input('Please enter a series of integers, split by spaces to add to the list:   ').strip().split()
for v in entered:
      inty = int(v)
      M.append(inty)
v = int(input('Please enter a number to be searched for: '))
count, NP = account(M, v)
print('Number of steps:', NP)
print(count)







            
