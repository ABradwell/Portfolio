##– Exercise 3: Multiplication with arrays
#Exercise Three
#November 6th, 2018
'''
>>> m = product_matrixes([[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]])
>>> m
[[22, 28], [49, 64]]
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

def  product_matrixes(A,B):
      C = []
      k = 0
      while k < len(A):
            newrow = []
            for i in range(0,len(A)):
                  temp = 0
                  for j in range(0, len(B)):
                        temp = temp + A[i][j]*B[j][k]
                  newrow.append(temp)
            C.append(newrow)
            k = k + 1


      C = transform(C)
      return(C)

def printmatricies(m):
      print('\n\n\n NEW MATRIX BEGINS')
      row = len(m)
      for i in range(0, row):
            print(m[i])

rows = int(input('Please enter the number of rows you would like the matrix to have:   '))
A = matrixcreate('A', rows)
B = matrixcreate('B', rows)
printmatricies(A)
printmatricies(B)
C =  product_matrixes(A,B)
print(C)








      
