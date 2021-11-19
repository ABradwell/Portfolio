#Aiden Bradwell
#June 2018

#######IMPORTING PACKAGES##############
from graphics import *
from random import *
from itertools import product
import os
import time

def common (landconnect):
    
    ### Three possible situations
    currentcolor = randint(1, 1000)
    print(landconnect)
    color = 'blue'
    #Situation 1, there is no color asssigned yet
    if landconnect == 0:
        a=250
        b =250
        c = 250
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
        a =600
        b =960
        c = 1000
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
        a =600
        b =750
        c = 1000
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
    cubey = 0
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
            #Update grid
            if color == 'green' or 'darkgreen' :
                colornum = 0
            elif color == 'blue' or 'darkblue' :
                colornum = 1
            positiongrid.append(w)
            colorgrid.append(colornum)
    return (positiongrid, colorgrid)

def animalspawn (positiongrid, colorgrid, visuals, size):
    animalcolor = 'darkred'
    animalsize = 25
    arraylength = size
    arrayheight = size
    randx = randint(1, visuals.getWidth())
    randy = randint(1, visuals.getHeight())
    locationy = 0
    locationx = 0
    #actual creature creation
    creature = Rectangle(Point(randx, randy),Point(randx + animalsize,randy + animalsize))
    creature.setFill(animalcolor)
    creature.draw(visuals)
    #movement calculations
    cubewidth = visuals.getWidth()/size
    cubeheight = visuals.getHeight()/size
    cubex = randx /cubewidth
    cubey = randy /cubeheight
    compplace = ( cubey * size ) + cubex
    #begin life
    moveinstruction = randint(1, 100)
    #intial direction
    if moveinstruction >1 and moveinstruction <= 25 :
        direction = 'up'
    elif moveinstruction >25 and moveinstruction <= 50:
        direction = 'right'
    elif moveinstruction >50 and moveinstruction <= 75:
        direction = 'down'
    elif moveinstruction >75 and moveinstruction <= 100:
        direction = 'left'
    run = True

    while run == True:
        #If already moving up
        if direction == 'up':
            moveinstruction = randint(1, 100)
            #continue
            if moveinstruction >1 and moveinstruction <= 51 :
                direction = direction
                creature.move(0, -cubeheight)
                update(30)
            #Left
            elif moveinstruction >51 and moveinstruction <= 75:
                direction = 'left'
                creature.move(-cubewidth, 0)
                update(30)
            #Right
            elif moveinstruction > 75 and moveinstruction <= 100:
                direction = 'right'
                creature.move(cubewidth, 0)
                update(30)
                
       # If already moving right      
        elif direction =='right':
            moveinstruction = randint(1, 100)
            #continue
            if moveinstruction >1 and moveinstruction <= 51 :
                direction = direction
                creature.move(cubewidth, 0)
                update(30)
            #Left
            elif moveinstruction >51 and moveinstruction <= 75:
                direction = 'up'
                creature.move(0, -cubeheight)
                update(30)
            #Right
            elif moveinstruction > 75 and moveinstruction <= 100:
                direction = 'down'
                creature.move(0, cubeheight)
                update(30)
                
        #If already moving downwards
        elif direction =='down':
            moveinstruction = randint(1, 100)
           #continue
            if moveinstruction >1 and moveinstruction <= 51 :
                direction = direction
                creature.move(0, cubeheight)
                update(30)
            #Left
            elif moveinstruction >51 and moveinstruction <= 75:
                direction = 'right'
                creature.move(cubewidth, 0)
                update(30)
            #Right
            elif moveinstruction > 75 and moveinstruction <= 100:
                direction = 'left'
                creature.move(-cubewidth, 0)
                update(30)

        #If already moving left
        elif direction =='left':
            moveinstruction = randint(1, 100)
            #continue
            if moveinstruction >1 and moveinstruction <= 51 :
                direction = direction
                creature.move(-cubewidth, 0)
                update(30)
            #Left
            elif moveinstruction >51 and moveinstruction <= 75:
                direction = 'down'
                creature.move(0, cubeheight)
                update(30)
            #Right
            elif moveinstruction > 75 and moveinstruction <= 100:
                direction = 'up'
                creature.move(0, -cubeheight)
                update(30)
            
            
    
    
    















    
def mainmenu():
    #Main Menu System
    
    menu = True
    run= True
    while run == True:
        #Set start gap
        visuals = GraphWin('Main Menu',1000,1000)
        visuals.setBackground('black')
        title = 'Main Menu'
        rect = titleprint(visuals, title)
        def functionone()  :
            size = 25
            positiongrid, colorgrid = mapprint(visuals, size)
            animal = animalspawn(positiongrid, colorgrid, visuals, size)
        def functiontwo()  :
            size = 50
            positiongrid, colorgrid = mapprint(visuals, size)
        def functionthree()  :
            size = 75
            positiongrid, colorgrid = mapprint(visuals, size)
        def functionfour()  :
            size = 100
            positiongrid, colorgrid = mapprint(visuals, size)
        def functionfive()  :
            size = 200
            positiongrid, colorgrid = mapprint(visuals, size)
        def functionsix() :
            size = 250
            positiongrid, colorgrid = mapprint(visuals, size)
            
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
###############################
    #MAIN CODE#
###############################

mainmenu()


