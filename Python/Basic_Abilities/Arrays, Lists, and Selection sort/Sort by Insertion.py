'''
Sorted a list
• Think of a simple algorithm to sort a list in ascending
order.
• Implement it in a Python function and add a to count the
number of stepstaken.
• The function must modify the initial list.
• Is your function efficient? How many steps have been
executed?
• Note: There is a predefined function sort(). What
algorithm does it use?
• If the list's name is l1, we can sort it wit:
>>> l1.sort()
'''

'''
Binary search in a sorted list
• If the list is already sorted in an ascending order, can you
find an effacient algorithm to look for the value v, without
havibg to go through the whole list?
• Add a variable to count the number of steps executed by
your function.
>>> binary_search([1, 2, 3, 4, 4, 5, 7, 9, 10, 13],
10)
Number of steps 3
True
>>> binary_search([1, 2, 3, 4, 4, 5, 7, 9, 10, 13],
6)
Number of steps 4
False
'''


'''
Sort by insertion
• An efficient algorithm can be done by insertion (Insertion
Sort):
Insert a value in the good position in the list already
sorted on the left. The first element is in the good position.
Check the second element, and insehe left part of the the list
before him (thus the left part of the list is sorted). Repete
with the other elements, until the list is fully sortede.
• Modify thr initial list. Calculate the number of steps.
Example
>>> L = [3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]
>>> sort_by_insertion(L)
Number of steps 38
>>> L
[-2, -1, -1, 2, 3, 4, 5, 7, 7, 16, 17, 82]
'''




def sort_by_insertion(arr):
      newarr = [arr[0]]
      del arr[0]
      steps = 0
      i = 0
      run = True
      while run:
            if arr == []:
                  break
            initiallength = len(arr)
            if i < initiallength:
                  steps = steps +1
                  newindex = 0
                  i = i + 1
                  for v in newarr:
                        if arr[0] < v:
                              newarr.insert(newindex, arr[0])
                              del arr[0]
                              break
                        else:
                              newindex = newindex + 1
                        if newindex == len(newarr):
                              newarr.append(arr[0])
                              del arr[0]
                              break
            else:
                  i = 0
      print("Organized array: ", newarr)
      print("Number of steps: ", steps)
L = [3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]
sort_by_insertion(L)





      
