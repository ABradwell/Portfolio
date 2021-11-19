#Lab 7
#Exercise 4
#October 30th, 2018
#Aiden Stevenson Bradwell




def move_zeros_v1(list1):
      tmp = []
      counter= 0
      for c in list1:
            if c == 0:
                  counter = counter + 1
            else:
                  tmp.append(c)
      for c in range(counter):
            tmp.append(0)
      return tmp

def move_zeros_v2(list1):
      tmp = []
      counter= 0
      for c in list1:
            if c == 0:
                  counter = counter + 1
            else:
                  tmp.append(c)
      for c in range(counter):
            tmp.append(0)
      for i in range(len(list1)):
            list1[i] = tmp[i]

def move_zeros_v3(list1):
      for v in range(len(list1)):
            for c in range(len(list1)):
                  i = 0
                  while (i + 1) < len(list1):
                        if list1[i] ==0:
                              list1[i] = list1[i + 1]
                              list1[i + 1] = 0
                        i = i + 1




user = input('Please enter a list, seperated by spaces: ').strip().split()
index = 0
for c in user:
      user[index] = int(c)
      index = index + 1
list1 = user.copy()
#Version One
list2 = move_zeros_v1(list1)
print ('Version One:',list2)
#Version Two
move_zeros_v2(user)
print('Version Two:', user)
#Version Three
move_zeros_v3(list1)
print('Version Three:', list1)


























##def sum_of_three(t):
##      '''(tuple)->bool
##      Returns True if the sum of 3 consecutive
##      elements is zero
##      Precondition: the tuple has at least 3
##      elements
##      >>> t = (1,2,-3,4,-1,3)
##      >>> sum_of_three(t)
##      True
##      '''
##      allgood = False
##      if len(t)-3 >0: 
##            for i in range(len(t) - 2):
##                  int1 = float(t[i])
##                  int2 = float(t[i + 1])
##                  int3 = float(t[i + 2])
##                  if (int1 +int2 + int3) == 0:           
##                        allgood = True
##      return allgood
##
##
##
##t = input("Please enter a tuple, seperating each value with a commas:    ")
##t = t.replace(',', ' ')
##t = t.strip().split()
##t = tuple(t)
##allgood = sum_of_three(t)
##print(allgood)
