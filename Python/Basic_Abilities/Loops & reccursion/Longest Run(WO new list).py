#Aiden Stevenson Bradwell
#Assignment Three
#Part 1.3
#October 19th, 2018


def  longest_run (listone):
    ''' (list) --> int
    Accepts a list, and finds the longest consquetive seires of the same number

    Preconditions: the list entered is already divided and must be all float- variables
    '''
    #Initialize the variables
    index = 0
    streak = 0
    counter  = 0
    #Chooses the placment
    while index  < len(listone):
        tempstreak = 1
        while (counter + 1) < len(listone):
            if listone[counter] == listone [ counter + 1]:
                tempstreak = tempstreak + 1
                counter = counter + 1
                if tempstreak > streak:
                    streak = tempstreak
            else:
                counter = counter +1
                if tempstreak > streak:
                    streak = tempstreak
                break
        index = counter + 1
    return streak
        
                
    


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

longest = longest_run(int_list)
print (longest)
