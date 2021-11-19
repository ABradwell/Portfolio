#Assigment Three
#October 9th, 2018
#Aiden Stevenson Bradwell

'''• Derive an algorithm/function in Python that will
calculate the distance (horizontal, in meters)
traveled by a ball tossed at
v meters per second,
saccording to the angle
θ (in degres) of the toss.
• Return a list of values where:
distance[0]: ball tossed at 0 degres above the horizontal.
distance[1]: ball tossed at 10 degres abovr the horizontal.
…
distance[9]: ball tossed at 90 degres above the horizontal.
(directly upward).
• Complete the main bloc of your program: call the
function to create a list described above and
display the contents.'''

import math
def anglecalc(v, angles):
    distances = []
    i = 0
    while i< len(angles) :
        radians = (math.pi / 180) * angles[i]
        distance = (2*(v*v) * math.cos(radians) * math.sin(radians) ) / 9.8
        distances.append(distance)
        i = i+1
    return distances




v = float(input('Please input the power of the throw, in meters per seconds:   '))
angles = [0,10,20,30,40,50,60,70,80,90]
distances = anglecalc(v, angles)
i = 0
while i < len(distances):
    print('If thrown ', angles[(i)], ' degrees, it will go ', distances[(i)] , ' Meters')
    i = i+1
