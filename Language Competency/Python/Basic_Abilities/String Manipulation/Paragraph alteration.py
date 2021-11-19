#Assignment Three
#October 16th, 2018
#Aiden Stevenson Bradwell

'''Copy this expression in the Python interpretor:
s = """ En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … """
(The begining of the novel Les misérables by Victor Hugo.)
Do the following exercises in the interpretor:
(a) Create a copy of s, named nS, with characters . , ; and \n replaced by
spaces.
(b) Erase the spaces that are at the start and end of nS (and affect the new chaine
in the same variable nS).
(c) Change all the caracters of nS in lower case (and name the new chain nS).
(d) Calculate the number of times nS contains 'de'.
(e) Change all the sub-chains était to est (and name the new chain nS).'''

s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''

#A
nS = s
nS = nS.replace(',',' ')
nS = nS.replace('.',' ')
nS = nS.replace(';',' ')
nS = nS.replace('\n',' ')
print (nS)

#B
nS = nS[1: (len(nS)-1)]
print (nS)
#C
nS = nS.lower()
print (nS)
#D
count = nS.count('de')
print(count)
#E
nS = nS.replace('était', 'est')
print(nS)
