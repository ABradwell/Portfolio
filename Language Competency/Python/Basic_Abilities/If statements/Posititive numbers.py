#Aiden Stevenson Bradwell
#Assignment Three
#Part One
#October 19th, 2018

def count_pos(stringlist):
    ''' (int list) ---> Int
        Takes in a list of integers, and returns the number of posotive integers within it
    '''
    count = 0
    for v in stringlist:
        if v > 0:
            count = count + 1
    return count






raw_input = input("Please input a list of numbers separated by space: ").strip().split()
int_list = raw_input
index = 0
for v in raw_input:
    if v == ' ' :
        int_list[index] = 'X'
    else:
        int_list[index] = float(v)
    index = index + 1
if len (int_list) == 0:
    int_list = [0]


            
print (count_pos(int_list))
    
