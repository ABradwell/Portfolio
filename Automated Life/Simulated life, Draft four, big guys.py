#######IMPORTING PACKAGES##############
from graphics import *
from random import *
from itertools import product
import os
import time
import time
from multiprocessing import Pool
from multiprocessing import Process
import os

def common (landconnect):

    ### Three possible situations
    currentcolor = randint(1, 1000)
    color = 'blue'
    #Situation 1, there is no color asssigned yet
    if landconnect == 0:
        #Set odds of initial land
        a=250
        b =500
        c = 750
        #set floor type // color
        if  currentcolor > 1 and currentcolor <= a:
            color = 'green'
            landconnect = 1
        elif currentcolor > a and currentcolor <= b:
            color = 'darkgreen'
            landconnect = 1
        elif currentcolor > b and currentcolor <= c:
            color = 'blue'
            landconnect = 2
        elif currentcolor > c and currentcolor <= 1000:
            color = 'darkblue'
            landconnect = 2
        return color, landconnect

        #Situation 2, there is already land assigned
    elif landconnect == 1:
        #set odds of grounded continuation
        a =600
        b =980
        c = 1000
        #set floor type // color
        if  currentcolor> 1 and currentcolor <= a:
            color = 'green'
            landconnect = 1
        elif currentcolor> a and currentcolor <= b:
            color = 'darkgreen'
            landconnect = 1
        elif currentcolor> b and currentcolor <= c:
            color = 'blue'
            landconnect = 2
        return color, landconnect

        #Situation 3, there is already water assigned
    elif landconnect == 2:
        #set odds of wet continuation
        a =400
        b =750
        c = 1000
        #set floor type // color
        if  currentcolor> 1 and currentcolor <= a:
            color = 'blue'
            landconnect = 2
        elif currentcolor> a and currentcolor <= b:
            color = 'darkblue'
            landconnect = 2
        elif currentcolor> b and currentcolor <= c:
            color = 'green'
            landconnect = 1
        return color, landconnect


def mapprint(visuals, size):
    #Begin grid system
    #two grids, one consisting of ones and zeros
    #Ones | Water
    #Zeros | Ground
    #The secone consists of the w value (what rect it is starting top left working way down)
    #find postionvector[x]/ #of cubes horizontally
    #the remainder is the x value
    #the rounded number is the collumn.
    positiongrid = []
    colorgrid = []
    w = 0
    cubewidth = visuals.getWidth()/size
    cubeheight = visuals.getHeight()/size
    arraylength = size
    arrayheight = size
    landconnect = 0
    #Start first row, ect
    cubey = -cubeheight
    for i in range(arrayheight):
        cubey = cubey + cubeheight
        cubex = 0
        #Square by square tile placement
        for u in range(arraylength):
            w +=1
            rect = Rectangle(Point(cubex, cubey),Point(cubex + cubewidth,cubey + cubeheight))
            cubex = cubex + cubewidth
            color, landconnect = common(landconnect)
            #Apply  type of square (water, land)5
            rect.setFill(color)
            #Draw Map
            rect.draw(visuals)
            #  grid
            positiongrid.append(w)
            colorgrid.append(landconnect)
    return (positiongrid, colorgrid)


def moveleft(visuals,creature, groundtype, cubewidth):
    #check not water
    if groundtype == 'water' :
            void()
    # If ground, and not past left of screen
    elif groundtype == 'ground' and (creature.getAnchor().getX()-cubewidth//2) > 0:
            direction = 'left'
            #movement
            creature.move(-cubewidth//2, 0)
            
def moveright(visuals,creature, groundtype, cubewidth):
    #check not water
    if groundtype =='water' :
        void()
    # If ground, and not past right of screen
    elif groundtype == 'ground' and (creature.getAnchor().getX()+cubewidth//2) < 1000:
            direction = 'right'
            #movement
            creature.move(cubewidth//2, 0)
            
def moveup(visuals,creature, groundtype, cubeheight):
    #check not water
    if groundtype == 'water' :
            void()
    # If ground, and not past top of screen
    elif groundtype == 'ground' and (creature.getAnchor().getY()-cubeheight//2) > 0:
        direction = 'up'
        #movement
        creature.move(0, -cubeheight//2)
        
def movedown(visuals,creature, groundtype, cubeheight):
    #check not water
    if groundtype == 'water' :
            void()
    # If ground, and not past bottom of screen
    elif groundtype == 'ground' and (creature.getAnchor().getY()+cubeheight//2) < 1000:
        direction = 'down'
        #movement
        creature.move(0, cubeheight//2)




def desiredcalculations (positiongrid, colorgrid, visuals, size, currentx, currenty,direc):
    run = True
    #DATA
    arraylength = size
    arrayheight = size
    cubewidth = int(visuals.getWidth()//size)
    cubeheight = int(visuals.getHeight()//size)
    #Current x1 - left side of squares location
    #currentx - right side of squares location
    #currenty - top of square location
    #currenty - bottom of sqaure location
    #calculate which cube they are entering
    print (direc)
    if direc == 'up' :
        #Desired begins
        dw1 = int(currenty)
        desiredpoint1 = int(dw1 * size + currentx)
    elif direc == 'right' :
        #Desired begins
        dw1 = int(currentx + 1)
        desiredpoint1 = int(currenty*size+ dw1)
    elif direc == 'left' :
        #Desired begins
        dw1 = int(currentx - 1)
        desiredpoint1 = int(currenty*size+ dw1)
    elif direc == 'down' :
        #Desired begins
        dw1 = int(currenty + 2)
        desiredpoint1 = int(dw1*size+ currentx)
    else :
        desiredpoint1 == int(0)


    #Second point
    if direc == 'up' :
        #Desired begins
        dw2 = int(currenty - 1)
        desiredpoint2= int(dw2 * (visuals.getWidth()//cubewidth) + currentx)
    elif direc == 'right' :
        #Desired begins
        dw2 = int(currentx + 1)
        desiredpoint2 = int(currenty*(visuals.getWidth()//cubewidth) + dw2)
    elif direc == 'left' :
        #Desired begins
        dw2 = int(currentx - 1)
        desiredpoint2 = int(currenty*(visuals.getWidth()//cubewidth) + dw2)
    elif direc == 'down' :
        #Desired begins
        dw2 = int(currenty +1)
        desiredpoint2 = int(dw2* (visuals.getWidth()//cubewidth) + currentx)
    else :
        desiredpoint2 == int (0)
 #desiredpoint1 is the left side
#desiredpoint2 is the right side
        #find cube sizes for calculations
    cubewidth = int(visuals.getWidth()//size)
    cubeheight = int(visuals.getHeight()//size)
    #how many cubes are on the map?
    colorgridsize = (visuals.getWidth() // cubewidth) * (visuals.getHeight() // cubeheight)
    if desiredpoint1 <  colorgridsize and desiredpoint2 < colorgridsize:
        if colorgrid[ desiredpoint1 ] == 1 and colorgrid[ desiredpoint2 ] == 1:
            groundtype = 'ground'
            run = True
        else :
            groundtype = 'water'
            run = False
    else :
        groundtype = 'water'
        run = False
    return run, groundtype

def animalspawn2 (positiongrid, colorgrid, visuals, size):
    print (size)
    animalcolor = 'darkred'
    animalsize = visuals.getWidth()/size
    arraylength = size//2
    arrayheight = size//2
    
    spawnattempt = False
    while spawnattempt == False :
        #choose coords
        randx = randint(1, visuals.getWidth())
        randy = randint(1, visuals.getHeight())
        locationy = 0
        locationx = 0
        #actual creature creation
        imagepoint = Point((randx +(randx + animalsize)//2), (randy + (randy + animalsize)//2))
        if  size == 25:
            creature = Image( imagepoint,"doggo40.png")
        elif size == 50:
            creature = Image( imagepoint,"doggo20.png")
        elif size == 75:
            creature = Image( imagepoint,"doggo13.png")
        else:
            creature = Image( imagepoint,"doggo10.png")
        
        #Make sure not in water
        spawnattempt = waterspawntest(size, visuals,creature,colorgrid)
    #Draw
    creature.draw(visuals)
    #movement calculations
    cubewidth = int(visuals.getWidth()/size)
    cubeheight = int(visuals.getHeight()/size)
    cubex = int(randx //cubewidth)
    cubey = int(randy //cubeheight)
    compplace = int(( cubey * size ) + cubex)
    #speed of creature
    fps =45
    #begin life
    moveinstruction = randint(1, 100)
    #intial direction
    moverun = True
    run = True
    while moverun == True:
        if moveinstruction >0 and moveinstruction <= 25 :
            direction = 'up'
        elif moveinstruction >25 and moveinstruction <= 50:
            direction = 'left'
        elif moveinstruction >50 and moveinstruction <= 75:
            direction = 'down'
        elif moveinstruction >75 and moveinstruction <= 100:
            direction = 'right'
        a = 50
        b =  75
        run = True
        while run == True:
            time.sleep(.1)
            #If already moving up
            if direction == 'up':
                moveinstruction = randint(1, 100)
                #continue
                if moveinstruction >1 and moveinstruction <= a :
                    #calculate current position
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)

                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)

                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)

           # If already moving right
            elif direction =='right':
                moveinstruction = randint(1, 100)
                #continue
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)

            #If already moving downwards
            elif direction =='down':
                moveinstruction = randint(1, 100)
               #continue
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)

            #If already moving left
            elif direction =='left':
                moveinstruction = randint(1, 100)
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)


def currentposition(positiongrid, colorgrid, visuals, size, creature):
    # DATA
    cubewidth = visuals.getWidth()/size
    cubeheight = visuals.getHeight()/size
    #Find current x, y coords in relation to the cubes of the map
    currentx = creature.getAnchor().getX()//cubewidth
    currenty = creature.getAnchor() .getY()//cubeheight
    return currentx, currenty

def animalspawn (positiongrid, colorgrid, visuals, size):
    print (size)
    animalcolor = 'darkred'
    animalsize = visuals.getWidth()/size
    arraylength = size//2
    arrayheight = size//2
    
    spawnattempt = False
    while spawnattempt == False :
        #choose coords
        randx = randint(1, visuals.getWidth())
        randy = randint(1, visuals.getHeight())
        locationy = 0
        locationx = 0
        #actual creature creation
        imagepoint = Point((randx +(randx + animalsize)//2), (randy + (randy + animalsize)//2))
        if  size == 25:
            creature = Image( imagepoint,"doggo40.png")
        elif size == 50:
            creature = Image( imagepoint,"doggo20.png")
        elif size == 75:
            creature = Image( imagepoint,"doggo13.png")
        else:
            creature = Image( imagepoint,"doggo10.png")
        
        #Make sure not in water
        spawnattempt = waterspawntest(size, visuals,creature,colorgrid)
    #Draw
    creature.draw(visuals)
    #movement calculations
    cubewidth = int(visuals.getWidth()/size)
    cubeheight = int(visuals.getHeight()/size)
    cubex = int(randx //cubewidth)
    cubey = int(randy //cubeheight)
    compplace = int(( cubey * size ) + cubex)
    #speed of creature
    fps =45
    #begin life
    moveinstruction = randint(1, 100)
    #intial direction
    moverun = True
    run = True
    while moverun == True:
        if moveinstruction >0 and moveinstruction <= 25 :
            direction = 'up'
        elif moveinstruction >25 and moveinstruction <= 50:
            direction = 'left'
        elif moveinstruction >50 and moveinstruction <= 75:
            direction = 'down'
        elif moveinstruction >75 and moveinstruction <= 100:
            direction = 'right'
        a = 50
        b =  75
        run = True
        while run == True:
            time.sleep(.1)
            #If already moving up
            if direction == 'up':
                moveinstruction = randint(1, 100)
                #continue
                if moveinstruction >1 and moveinstruction <= a :
                    #calculate current position
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)

                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)

                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)

           # If already moving right
            elif direction =='right':
                moveinstruction = randint(1, 100)
                #continue
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)

            #If already moving downwards
            elif direction =='down':
                moveinstruction = randint(1, 100)
               #continue
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'right'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveright(visuals,creature, groundtype, cubewidth)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)

            #If already moving left
            elif direction =='left':
                moveinstruction = randint(1, 100)
                if moveinstruction >1 and moveinstruction <= a :
                    proposeddirection = 'left'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveleft(visuals,creature, groundtype, cubewidth)
                #Left
                elif moveinstruction >a and moveinstruction <= b:
                    proposeddirection = 'down'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    movedown(visuals,creature, groundtype, cubeheight)
                #Right
                elif moveinstruction > b and moveinstruction <= 100:
                    proposeddirection = 'up'
                    currentx, currenty = currentposition(positiongrid, colorgrid, visuals, size, creature)
                    run, groundtype = desiredcalculations(positiongrid, colorgrid, visuals, size, currentx, currenty,proposeddirection)
                    moveup(visuals,creature, groundtype, cubeheight)

def mainmenu():
    #Main Menu System

    menu = True
    run= True
    while run == True:
        time.sleep(1)
        #Set start gap
        visuals = GraphWin('Main Menu',1000,1000)
        visuals.setBackground('black')
        title = 'Main Menu'
        rect = titleprint(visuals, title)
        
        #set what buttons do
        def functionone()  :
            size = 25
            positiongrid, colorgrid = mapprint(visuals, size)
            p = Process(target=animalspawn2, args=(positiongrid, colorgrid, visuals, size))
            p.start()
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functiontwo()  :
            size = 50
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functionthree()  :
            size = 75
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functionfour()  :
            size = 100
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functionfive()  :
            size = 200
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functionsix() :
            size = 250
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
    #Print Menu
        printclickablemenu(visuals, 'Create New Map (25 X 25)','Create New Map (50 X 50)','Create New Map (75 X 75)','Create New Map (100 X 100)','Create New Map (200 X  200)','Create New Map (250 X 250)',title ,rect, functionone,functiontwo,functionthree,functionfour,functionfive,functionsix, menu )

def printclickablemenu(win, menone,mentwo,menthree,menfour,menfive,mensix, currentprogram,rect,  functionone,functiontwo,functionthree,functionfour,functionfive,functionsix, menu):
    run = True
    while run== True:
        currentplacement = 200
        rangespace =190
        #Line 1
        topone = Point( win.getWidth()/2, rangespace)
        currentplacement= printline(win,menone,currentplacement,25)
        bottomone = Point( win.getWidth()/2, rangespace+20)
        #Line 2
        toptwo = Point( win.getWidth()/2, rangespace+25)
        currentplacement= printline(win,mentwo,currentplacement,25)
        bottomtwo = Point( win.getWidth()/2, rangespace+45)
        #Line 3
        topthree = Point( win.getWidth()/2, rangespace +50)
        currentplacement= printline(win,menthree,currentplacement,25)
        bottomthree = Point( win.getWidth()/2, rangespace+70)
        #Line 4
        topfour = Point( win.getWidth()/2, rangespace+75)
        currentplacement=  printline(win,menfour,currentplacement,25)
        bottomfour = Point( win.getWidth()/2, rangespace+95)
        #Line 5
        topfive = Point( win.getWidth()/2, rangespace+100)
        currentplacement=  printline(win,menfive,currentplacement,25)
        bottomfive = Point( win.getWidth()/2, rangespace+120)
        #Line 6
        topsix = Point( win.getWidth()/2, rangespace+125)
        currentplacement= printline(win,mensix,currentplacement,25)
        bottomsix = Point( win.getWidth()/2, rangespace+145)
        run = True
        #Allow Clickable part
        while run == True:
            mouseclick = win.getMouse()
            mousey, mousex = mouseclick.getY(), mouseclick.getX()
            currenty = Text(Point(mousex, mousey), '+')
            currenty.setTextColor('green')
            currenty.draw(win)
            print (mouseclick.getY())
            #Exit Button Standardized code
            if menu == False:
                rect =Rectangle(Point((win.getWidth()/2-60), 60),Point((win.getWidth()/2+60),90))
                upperleft= rect.getP1()
                lowerright= rect.getP2()
                if mouseclick.getX() > rect.getP1().getX() and mouseclick.getX() < rect.getP2().getX() and mouseclick.getY() > rect.getP1().getY() and mouseclick.getY() < rect.getP2().getY() :
                    win.close()
                    return void
            elif menu == True:
                    ect =Rectangle(Point((win.getWidth()/2-60), 60),Point((win.getWidth()/2+60),90))
                    upperleft= rect.getP1()
                    lowerright= rect.getP2()
                    if mouseclick.getX() > rect.getP1().getX() and mouseclick.getX() < rect.getP2().getX() and mouseclick.getY() > rect.getP1().getY() and mouseclick.getY() < rect.getP2().getY() :
                        return void
            #Find Button
            if mouseclick.getY() > topone.getY() and mouseclick.getY() < bottomone.getY() :
                functionone()
                print (menone)
            elif mouseclick.getY()  > toptwo.getY()  and mouseclick.getY() <bottomtwo.getY() :
                functiontwo()
                print (mentwo)
            elif mouseclick.getY()  > topthree.getY()   and mouseclick.getY()  < bottomthree.getY() :
                functionthree()
                print (menthree)
            elif mouseclick.getY()  > topfour.getY()  and mouseclick.getY() < bottomfour.getY() :
                functionfour()
                print (menfour)
            elif mouseclick.getY() > topfive.getY()  and mouseclick.getY() < bottomfive.getY() :
                functionfive()
                print (menfive)
            elif mouseclick.getY()  >topsix.getY()  and mouseclick.getY() < bottomsix.getY() :
                functionsix()
                print (mensix)

def titleprint(visuals, title):
    #Printing Title of Program
    titleprint= Text(Point(visuals.getWidth()/2, 50), title)
    titleprint.setTextColor ('red')
    titleprint.setSize(15)
    titleprint.setStyle('bold')
    titleprint.draw(visuals)
    #Printing square to click
    rect = Rectangle(Point((visuals.getWidth()/2-60), 60),Point((visuals.getWidth()/2+60),90))
    rect.setFill('darkred')
    rect.draw(visuals)
    #Printing Exit Text
    exitprint = Text(Point((visuals.getWidth()/2-15), 75), 'Click To Exit')
    exitprint.setSize(10)
    exitprint.setTextColor ('white')
    exitprint.draw(visuals)
    return rect


def printline(visuals, line, currentplacement,gap):
    #Fucntion to print lines in menue, or any menu for that matter
    printed =  Text(Point(visuals.getWidth()/2, currentplacement),line)
    printed.setTextColor ('white')
    printed.setSize(17)
    printed.draw(visuals)
    currentplacement += gap
    return (currentplacement)


def void():
    math = 1 + 1
############TESTS##################3
def postiontest(currentx,currenty):
    print ('current x coord: ' , currentx, '-' , currentx)
    print ('current y coord: ' , currenty, '-' , currenty)

def waterspawntest(size, visuals, creature, colorgrid):
    groundtype = False
    arraylength = size
    arrayheight = size
    cubewidth = int(visuals.getWidth()//size)
    cubeheight = int(visuals.getHeight()//size)
    #Check starting lcoation
    currentx = creature.getAnchor().getX()//cubewidth
    currenty = creature.getAnchor().getY()//cubeheight
    placement = int(currenty * (visuals.getWidth()//cubewidth) +currentx)
 #desiredpoint1 is the left side
#desiredpoint2 is the right side
    colorgridsize = (visuals.getWidth() // cubewidth) * (visuals.getHeight() // cubeheight)
    if placement <  colorgridsize :
        if colorgrid[ placement ] == 0 :
            groundtype = False
        else :
            groundtype = True
    return groundtype



###############################
    #MAIN CODE#
###############################

mainmenu()


