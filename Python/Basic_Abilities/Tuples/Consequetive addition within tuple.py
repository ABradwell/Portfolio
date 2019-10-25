#Lab 7
#Exercise 3
#October 30th, 2018
#Aiden Stevenson Bradwell

def sum_of_three(t):
      '''(tuple)->bool
      Returns True if the sum of 3 consecutive
      elements is zero
      Precondition: the tuple has at least 3
      elements
      >>> t = (1,2,-3,4,-1,3)
      >>> sum_of_three(t)
      True
      '''
      allgood = False
      if len(t)-3 >0: 
            for i in range(len(t) - 2):
                  int1 = float(t[i])
                  int2 = float(t[i + 1])
                  int3 = float(t[i + 2])
                  if (int1 +int2 + int3) == 0:           
                        allgood = True
      return allgood



t = input("Please enter a tuple, seperating each value with a commas:    ")
t = t.replace(',', ' ')
t = t.strip().split()
t = tuple(t)
allgood = sum_of_three(t)
print(allgood)
