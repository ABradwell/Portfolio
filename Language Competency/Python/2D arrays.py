#AIden Stevenson Bradwell
#November 8th, 2018
#Assignment 4, question one



def add(arr):
      for i in range (0, len(arr)):
            for u in range(0, len(arr[i])):
                  arr[i][u] = arr[i][u] + 1
                  
def add_v2(arr):
      newarr = []
      for i in range(0,len(arr)):
            newrow = []
            for u in range(0,len(arr[i])):
                  newrow.append(arr[i][u] + 1)
            newarr.append(newrow)
      return newarr




run = True
arr = []
print('Input the array elements with spaces between columns. ')
print('One row per line, and an empty line at the end. ')
while run:
      newrow = input().strip().split()
      if newrow != []:
            for i in range(0, len(newrow)):
                  newrow[i] = int(newrow[i])
            arr.append(newrow)
      else:
            run = False
print('The array is:')
print(arr)
add(arr)
print('After executing the function add, the array is:')
print (arr)
newarr = add_v2(arr)
print('A new array created with add_V2:')
print (arr)
print('After executing the function add_V2, the initial array is:')
print(newarr)
