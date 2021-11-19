##– Exercise 3: Multiplication with arrays
#Exercise Two
#November 6th, 2018
'''
>>> m = sum_matrixes([[1,2],[3,4]], [[1,1],[1,1]])
>>> m
[[2, 3], [4, 5]]'''

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

def matrixcreate(letter, rows):
      print('\n\n\n NEW MATRIX BEGINS')
      newmatrix = []
      index = 0
      while index < rows:
            print('Please enter the integer values for matrix', letter + 'row', (index + 1) ,'seperated by spaces:     ')
            newrow = input().strip().split()
            for i in range(0, len(newrow)):
                  newrow[i] = int(newrow[i])
            newmatrix.append(newrow)
            index = index + 1
      return (newmatrix)
def sum_matrixes(A,B):
      C = []
      collums = len(A[0])
      rows = len(A)

      for i in range(0, rows):
            newrow = []
            for j in range(0, collums):
                  newrow.append(A[i][j] + B[i][j])
            C.append(newrow)
      return(C)
            

rows = int(input('Please enter the number of rows you would like the matrix to have:   '))
A = matrixcreate('A', rows)
B = matrixcreate('B', rows)
C = matrixaddition(A,B)
print(C)








      
