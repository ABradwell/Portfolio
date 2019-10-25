#Assignment Two
#October 9th, 2018
'''Exercise 2 – Statistics calculations
• Develop a software that gets a list of students’ marks and find: the
marks average, the maximum value, and the minimum value.
– The main program bloc gets students’ marks from the user
9stored in a list) and calls a function to calculate the
average, the maximum and minimum values. It displays also
the results to the user.
– the function receive a lisy and calculate the average,
minimum and maximum. The result returned is a list with
three values.'''


def maxmin (grades):
    results = [None]
    addition = 0
    i = 0
    while i < len(grades):
        addition = addition + grades[i]
        i = i+1
    average = addition / len(grades)
    results.append(average)
    grades.sort()
    minimum = grades[0]
    results.append(minimum)
    maximum = grades[(len(grades) - 1)]
    results.append(maximum)
    return results

grade = input('Please enter the student"s grades, seperated by commas:    ')
grades = list(eval(grade))
results = maxmin(grades)
print('The average is :   ', results[1])
print('The maximum is :   ', results[3])
print('The minimum is :   ',  results[2])
