##– Exercise 1: Matrix transposed
##– Exercise 2: Sum of an array
##– Exercise 3: Multiplication with arrays

#Exercise One
#November 6th, 2018

'''
for example use... 1 2 3,
                           4 5 6
'''

def transform(A):
      AT = []
      collums = len(A)
      rows = len(A[0])
      i = 0
      for i in range(0, rows):
            newrow = []
            for j in range(0, collums):
                  newrow.append(A[j][i])
            AT.append(newrow)
      return(AT)

rows = int(input('Please enter the number of rows you would like the matrix to have:   '))
A = []
index = 0
while index < rows:
      newrow = input('Please enter the row integer values, seperated by spaces:     ').strip().split()
      for i in range(0, len(newrow)):
            newrow[i] = int(newrow[i])
      A.append(newrow)
      index = index + 1
AT = transform(A)
print(AT)
