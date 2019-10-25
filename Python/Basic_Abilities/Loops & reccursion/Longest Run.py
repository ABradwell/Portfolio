#Aiden Stevenson Bradwell
#Assignment Three
#Part 1.2
#October 19th, 2018


def two_length_run (listone):
    ''' (list) --> Boolean
    Accepts a list,w hich it then checks to see any back-to-back number placements within
    If there is a back to back placement, a boolean responds accordingly

    Preconditions: the list entered is already divided and must be all float
    '''
    index = 0
    confirmed = False
    while (index + 1) < len(listone):
        if listone[index] == listone[index + 1]:
            confirmed = True
            break
        else :
            index = index  + 1
    return confirmed



#### Main program  ####
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

confirmed = two_length_run(int_list)
print (confirmed)
