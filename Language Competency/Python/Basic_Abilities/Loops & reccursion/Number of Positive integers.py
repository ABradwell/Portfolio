#Aiden Stevenson Bradwell
#Assignment Three
#Part One
#October 19th, 2018

def count_pos(list1):
    ''' (list) --> int
    Takes a list as an input, scans through the list and then returns
    the quantity of positive numbers in that list

    Preconditions: the list entered is already divided and must be all integers
    '''
    count = 0
    for v in list1:
        if v > 0 :
            count = count + 1
    return count





intlist = []
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
int_list = raw_input
index = 0
for v in raw_input:
    if v == ' ' :
        int_list[index] = 'X'
    else:
        int_list[index] = float(v)
    index = index + 1


    
count = count_pos(int_list)
print('There are', count, 'positive numbers in your list.')
