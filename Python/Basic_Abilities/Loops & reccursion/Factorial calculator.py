#Exercise Four
#AIden Bradwell
#October 2nd, 2018
'''The n factorial (n!) is the product of integers between 1 and n.
Thus 4! = 1*2*3*4 = 24. By definition 0! = 1. The factorial is not
defined for negative numbers.
• Develop a program that asks for a non negative integer (≥0),
calculate and display the factorial. Note that the computing of
the factorial is similar to the of integers between 1 and N, but
with the multiplication instead of the addition (and very similar to
the product 1 to N). But do not forget to produce a value for 0.
– Developp an algorithm for yourself.
– Convert it in Python.
– the program must ask the user a positive number, call computeFact()
to obtain the factorial, and display the result.
– The algorithm/function computeFact() calculatee the factorial.'''

def computeFact(n):
    overall = 1
    cycle = 1
    while (cycle < n+1):
            overall =  overall * cycle
            cycle = cycle + 1
    return (overall)

run = True
while run:
    n = float(input('Please Enter a Non-Negative integer:   '))
    if n <0:
        print('Please Enter a Proper Number')
    else:
        overall = computeFact(n)
        print(overall)
        break
    
