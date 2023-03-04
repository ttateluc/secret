from types import NoneType
from graphics import *
import random


win = GraphWin('Tic Tac Toe', 500, 500)
win.yUp()


gameOver = 0
                             #corner valid future move (cVFM) list      #valid future move (VFM) list

cpuPicked = []
didCPUWin = []                                                #ist of computer-picked boxes
playerPicked = []   
didPlayerWin = []                                             #list of player-picked boxes                       #list of corner diagonal pairs

winning_combinations = [
    [1, 2, 3], [1, 4, 7], [1, 5, 9],
    [2, 5, 8], [3, 6, 9], [3, 5, 7],
    [4, 5, 6], [7, 8, 9]
    ]

potential_winning_combinations = [
    [1, 2], [2, 3], [1, 3],
    [1, 4], [1, 7], [4, 7],
    [1, 5], [1, 9], [5, 9],
    [2, 5], [2, 8], [5, 8],
    [3, 6], [3, 9], [6, 9],
    [3, 7], [5, 7], [3, 5],
    [4, 6], [5, 6], [4, 5],
    [7, 8], [7, 9], [8, 9]
    ]

combination_counters = [
    [350,350,3], [150,350,1], [250,350,2],
    [150,150,7], [150,250,4], [150,350,1],
    [350,150,9], [250,250,5], [150,350,1],
    [250,150,8], [250,250,5], [250,350,2],
    [350,150,9], [350,250,6], [350,350,3],
    [250,250,5], [350,350,3], [150,150,7],
    [250,250,5], [150,250,4], [350,250,6],
    [350,150,9], [250,150,8], [150,150,7]
    ]


selectList = []
boxesPicked = [0]
cpuChoiceList = [[150,350,1],[250,350,2],[350,350,3],[150,250,4],[250,250,5],[350,250,6],[150,150,7],[250,150,8],[350,150,9]]

def startScreen():                                                  #displays start menu options
    global startMessage
    startMessage = Text(Point(win.getWidth()/2,450),
                        "Welcome to Tic Tac Toe!")
    startMessage.setSize(25)
    startMessage.setOutline("purple")
    startMessage.setStyle("bold")
    startMessage.draw(win)
    global instruct1
    instruct1 = Text(Point(win.getWidth()/2,410),
                     "Click an option below to begin your game")
    instruct1.draw(win)
    global playerBox
    playerBox = Rectangle(Point(100,350),Point(400,250))
    playerBox.setFill("pink")
    playerBox.draw(win)
    global playerStart
    playerStart = Text(Point(win.getWidth()/2,300),
                       "vs Player")
    playerStart.draw(win)
    global cpuBox
    cpuBox = Rectangle(Point(100,200),Point(400,100))
    cpuBox.setFill("light blue")
    cpuBox.draw(win)
    global cpuStart
    cpuStart = Text(Point(win.getWidth()/2,150),
                    "vs CPU")
    cpuStart.draw(win)


def grid():                                                         #displays 3x3 TicTacToe grid
    leftLine = Line(Point(200,100),Point(200,400))
    leftLine.setWidth(5)
    leftLine.draw(win)
    rightLine = Line(Point(300,100),Point(300,400))
    rightLine.setWidth(5)
    rightLine.draw(win)
    downLine = Line(Point(100,200),Point(400,200))
    downLine.setWidth(5)
    downLine.draw(win)
    upLine = Line(Point(100,300),Point(400,300))
    upLine.setWidth(5)
    upLine.draw(win)

def isBetween(x,end1,end2):                                         #checks if a point is found between given endpoints
    return end1 <= x <= end2 or end2 <= x <= end1

def pwcChecker():
        playerPicked.sort()
        didPlayerWin.sort()

def relocate(pt):                
        global b                                        #take user click location and recenter in respective box
        if isBetween(pt.getX(),100,200) and isBetween(pt.getY(),300,400):
            pt = Point(150,350)
            b = 1
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),200,300) and isBetween(pt.getY(),300,400):
            pt = Point(250,350)
            b = 2
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),300,400) and isBetween(pt.getY(),300,400):
            pt = Point(350,350)
            b = 3
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),100,200) and isBetween(pt.getY(),200,300):
            pt = Point(150,250)
            b = 4
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),200,300) and isBetween(pt.getY(),200,300):
            pt = Point(250,250)
            b = 5
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),300,400) and isBetween(pt.getY(),200,300):
            pt = Point(350,250)
            b = 6
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),100,200) and isBetween(pt.getY(),100,200):
            pt = Point(150,150)
            b = 7
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),200,300) and isBetween(pt.getY(),100,200):
            pt = Point(250,150)
            b = 8
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        elif isBetween(pt.getX(),300,400) and isBetween(pt.getY(),100,200):
            pt = Point(350,150)
            b = 9
            if b in boxesPicked:
                return alreadyPickedError()
            else:
                boxesPicked.append(b)
                playerPicked.append(b)
                didPlayerWin.append(b)
                pwcChecker()
                return pt
        else:
            return relocateError() 

    
def pvpMode():                                                      #code for Player vs Player mode
    startMessage.undraw()                                           #clear menu boxes
    instruct1.undraw()
    playerStart.undraw()
    cpuStart.undraw()
    playerBox.undraw()
    cpuBox.undraw()
    
    pvpMessage = Text(Point(win.getWidth()/2,450),                  #Prompt user which shape they want to use
                      "Player vs Player Mode Selected!")
    pvpMessage.setSize(20)
    pvpMessage.setOutline("red")
    pvpMessage.draw(win)
    pvpInstruct = Text(Point(win.getWidth()/2,410),
                       "Player 1: choose your shape")
    pvpInstruct.draw(win)
    
    xoSelect()   
    global pvpHeader
    global gameInstruct                                                   #Display shape selection menu boxes

    count = 0
    while count < 1:                                                #Determine user shape selection
        pt = win.getMouse()                                         
        if isBetween(pt.getX(),100,400) and isBetween(pt.getY(),250,350):
            pvpHeader = Text(Point(win.getWidth()/2,450),
                             "Player 1 is X, Player 2 is O")
            p1x = 1                                                 #Save user's choice
            count = count + 1
        elif isBetween(pt.getX(),100,400) and isBetween(pt.getY(),100,200):
            pvpHeader = Text(Point(win.getWidth()/2,450),
                             "Player 1 is O, Player 2 is X")
            p1x = 0
            count = count + 1
        else:
            selectScreenError()                                     #if misclick, show error
    if 'selectError' in globals():                                  #erase error message before game starts
        selectError.undraw()
        
    pvpMessage.undraw()                                             #clear menu boxes and draw grid
    pvpInstruct.undraw()
    xBox.undraw()
    xText.undraw()
    oBox.undraw()
    oText.undraw()
    grid()
    
    pvpHeader.setSize(20)                                           #show game instruction
    pvpHeader.setOutline("red")
    pvpHeader.draw(win)
    gameInstruct = Text(Point(win.getWidth()/2,50),
                        "Click inside a square to place your shape")
    gameInstruct.setStyle("italic")
    gameInstruct.draw(win)

    

    

    turn = 0
    global relocate
    global b
    if p1x == 1:                                                    #if player 1 chose X:
        while gameOver == 0 and turn < 9:                           #if neither player has won and boxes are open
            place = win.getMouse()
            place = relocate(place)                                 #place shape in middle of box where user clicked
            X = Image(place,"ttt-x.png")
            X.draw(win)
            playerOne.append(b)
            gameOverCheckerPVP()
            turn = turn + 1
            if turn >= 9:                                           #check for full grid after each turn
                break
            place = win.getMouse()
            place = relocate(place)
            O = Image(place,"ttt-o.png")
            O.draw(win)
            playerTwo.append(b)
            gameOverCheckerPVP()
            turn = turn + 1

    else:                                                           #if player 1 chose O:
        while gameOver == 0 and turn < 9:
            place = win.getMouse()
            place = relocate(place)
            O = Image(place,"ttt-o.png")
            O.draw(win)
            playerOne.append(b)
            gameOverCheckerPVP()
            turn = turn + 1
            if turn >= 9:
                break
            place = win.getMouse()
            place = relocate(place)
            X = Image(place,"ttt-x.png")
            X.draw(win)
            playerTwo.append(b)
            gameOverCheckerPVP()
            turn = turn + 1

    if turn >= 9:                                                   #if game ends in a tie, display tie result
        pvpHeader.undraw()
        tieMessage = Text(Point(win.getWidth()/2,450),
                          "Tie Game!")
        tieMessage.setSize(20)
        tieMessage.setOutline("red")
        tieMessage.draw(win)
        gameInstruct.undraw()
        tieInstruct = Text(Point(win.getWidth()/2,50),
                        "Click anywhere to exit the window")
        tieInstruct.setStyle("italic")
        tieInstruct.draw(win)
        win.getMouse()
        win.close()

playerOne = []
playerTwo = []

def gameOverCheckerPVP():
    global playerOne
    global playerTwo
    global pvpHeader
    global gameInstruct
    for i in range(len(winning_combinations)):
        if set(winning_combinations[i]).intersection(set(playerOne)) == set(winning_combinations[i]):
            pvpHeader.undraw()
            winMessage = Text(Point(win.getWidth()/2,450),
            "Player 1 Wins!")
            winMessage.setSize(20)
            winMessage.setOutline("red")
            winMessage.draw(win)
            gameInstruct.undraw()
            winInstruct = Text(Point(win.getWidth()/2,50),
                            "Click anywhere to exit the window")
            winInstruct.setStyle("italic")
            winInstruct.draw(win)
            win.getMouse()
            win.close()
        elif set(winning_combinations[i]).intersection(set(playerTwo)) == set(winning_combinations[i]):
            pvpHeader.undraw()
            winMessage = Text(Point(win.getWidth()/2,450),
            "Player 2 Wins!")
            winMessage.setSize(20)
            winMessage.setOutline("red")
            winMessage.draw(win)
            gameInstruct.undraw()
            winInstruct = Text(Point(win.getWidth()/2,50),
                            "Click anywhere to exit the window")
            winInstruct.setStyle("italic")
            winInstruct.draw(win)
            win.getMouse()
            win.close()

turn = 0

def pvcMode():           
                                               #code for Player vs CPU mode
    startMessage.undraw()                                           #clear menu boxes
    instruct1.undraw()
    playerStart.undraw()
    cpuStart.undraw()
    playerBox.undraw()
    cpuBox.undraw()
    
    pvcMessage = Text(Point(win.getWidth()/2,450),                  #prompt user which shape they want to use
                      "Player vs Computer Mode Selected!")
    pvcMessage.setSize(20)
    pvcMessage.setOutline("blue")
    pvcMessage.draw(win)
    pvcInstruct = Text(Point(win.getWidth()/2,410),
                       "Choose your shape")
    pvcInstruct.draw(win)

    xoSelect()                                                      #Display shape selection menu boxes

    pt = win.getMouse()                                             #Determine user shape selection
    if isBetween(pt.getX(),100,400) and isBetween(pt.getY(),250,350):
        pvcHeader = Text(Point(win.getWidth()/2,450),
                         "You are playing as X vs the CPU")
        p1xc = 0
    elif isBetween(pt.getX(),100,400) and isBetween(pt.getY(),100,200):
                pvcHeader = Text(Point(win.getWidth()/2,450),
                         "You are playing as O vs the CPU")
                p1xc = 1
    else:
        selectScreenError()                                         #if misclick, display error

    pvcMessage.undraw()                                             #clear menu boxes and show grid
    pvcInstruct.undraw()
    xBox.undraw()
    xText.undraw()
    oBox.undraw()
    oText.undraw()
    grid()
    
    pvcHeader.setSize(20)                                           #show game instruction
    pvcHeader.setOutline("blue")
    pvcHeader.draw(win)
    gameInstruct = Text(Point(win.getWidth()/2,50),
                        "Click inside a square to place your shape")
    gameInstruct.setStyle("italic")
    gameInstruct.draw(win)

    def tieGame():     
                                                
        pvcHeader.undraw()
        tieMessage = Text(Point(win.getWidth()/2,450),
                            "Tie Game!")
        tieMessage.setSize(20)
        tieMessage.setOutline("red")
        tieMessage.draw(win)
        gameInstruct.undraw()
        tieInstruct = Text(Point(win.getWidth()/2,50),
                        "Click anywhere to exit the window")
        tieInstruct.setStyle("italic")
        tieInstruct.draw(win)
        win.getMouse()
        win.close()

    
        

    def cpucChecker():
        cpuPicked.sort()
        didCPUWin.sort()
        

                                     #if click outside of grid, show error
    
    def gameOverChecker():
        
        for i in range(len(winning_combinations)):

                #checks if all numbers of xNumbers array belong to (intersect) one of the winning combinations subarrays
            if set(winning_combinations[i]).intersection(set(didPlayerWin)) == set(winning_combinations[i]):
                pvcHeader.undraw()
                winMessage = Text(Point(win.getWidth()/2,450),
                "Player Wins!")
                winMessage.setSize(20)
                winMessage.setOutline("red")
                winMessage.draw(win)
                gameInstruct.undraw()
                winInstruct = Text(Point(win.getWidth()/2,50),
                                "Click anywhere to exit the window")
                winInstruct.setStyle("italic")
                winInstruct.draw(win)
                win.getMouse()
                win.close()
            elif set(winning_combinations[i]).intersection(set(didCPUWin)) == set(winning_combinations[i]):
                pvcHeader.undraw()
                winMessage = Text(Point(win.getWidth()/2,450),
                "CPU Wins!")
                winMessage.setSize(20)
                winMessage.setOutline("red")
                winMessage.draw(win)
                gameInstruct.undraw()
                winInstruct = Text(Point(win.getWidth()/2,50),
                                "Click anywhere to exit the window")
                winInstruct.setStyle("italic")
                winInstruct.draw(win)
                win.getMouse()
                win.close()
    
    def turnChecker():
        global turn
        turn += 1
        if turn >= 9:
            tieGame()

    def pickRandomCorner():                   
        global cpuChoice                  #for when any corner will do
        cpuCornerList = [[150,350,1],[350,350,3],[150,150,7],[350,150,9]]  
        cpuChoice = random.choice(cpuCornerList)
        if cpuChoice[2] in boxesPicked:
            while cpuChoice[2] in boxesPicked:
                cpuChoice = random.choice(cpuCornerList)
        
    

    def counterMove():
        global cpuChoice

        cpuChoice = random.choice(cpuChoiceList)
        if cpuChoice[2] in boxesPicked:
            while cpuChoice[2] in boxesPicked:
                cpuChoice = random.choice(cpuChoiceList)

        for i in range(len(potential_winning_combinations)):

            counter = combination_counters[i]
            if set(potential_winning_combinations[i]).intersection(set(cpuPicked)) == set(potential_winning_combinations[i]) and counter[2] not in boxesPicked:
    
                    cpuChoice = counter

                    if cpuChoice[2] in boxesPicked:
                        while cpuChoice[2] in boxesPicked:
                            cpuChoice = random.choice(cpuChoiceList)
                    return cpuChoice
                    

            elif set(potential_winning_combinations[i]).intersection(set(playerPicked)) == set(potential_winning_combinations[i]) and counter[2] not in boxesPicked:
                
                    cpuChoice = counter

                    if cpuChoice[2] in boxesPicked:
                        while cpuChoice[2] in boxesPicked:
                            cpuChoice = random.choice(cpuChoiceList)
                    return cpuChoice

             
            

                
                
           
        



    def playerTurn1():
        place = win.getMouse()
        place = relocate(place)                                   
        X = Image(place,"ttt-x.png")
        X.draw(win)

    def cpuTurn1():
        cpuChoice = random.choice(cpuChoiceList)
        if cpuChoice[2] in boxesPicked:
            while cpuChoice[2] in boxesPicked:
                cpuChoice = random.choice(cpuChoiceList)  
        else:    
            if cpuChoice[2] < 3:
                cpuChoice = cpuChoiceList[4]
                if cpuChoice[2] in boxesPicked:
                    while cpuChoice[2] in boxesPicked:
                        cpuChoice = random.choice(cpuChoiceList)                                          #60% chance of center pick
            elif cpuChoice[2] in boxesPicked:
                pickRandomCorner()
        
        pt = Point(cpuChoice[0], cpuChoice[1])
        O = Image(pt,"ttt-o.png")
        O.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def playerTurn2():
        place = win.getMouse()
        place = relocate(place)                                   
        X = Image(place,"ttt-x.png")
        X.draw(win)

    def cpuTurn2():
        counterMove()
        
        pt = Point(cpuChoice[0], cpuChoice[1])
        O = Image(pt,"ttt-o.png")
        O.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def playerTurn3():
        place = win.getMouse()
        place = relocate(place)                                   
        X = Image(place,"ttt-x.png")
        X.draw(win)

    def cpuTurn3():
        counterMove()

        pt = Point(cpuChoice[0], cpuChoice[1])
        O = Image(pt,"ttt-o.png")
        O.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def playerTurn4():
        place = win.getMouse()
        place = relocate(place)                                   
        X = Image(place,"ttt-x.png")
        X.draw(win)

    def cpuTurn4():
        counterMove()

        pt = Point(cpuChoice[0], cpuChoice[1])
        O = Image(pt,"ttt-o.png")
        O.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def playerTurn5():
        place = win.getMouse()
        place = relocate(place)                                   
        X = Image(place,"ttt-x.png")
        X.draw(win)


    def bcpuTurn1():
        cpuChoice = random.choice(cpuChoiceList)
        if cpuChoice[2] in boxesPicked:
            while cpuChoice[2] in boxesPicked:
                cpuChoice = random.choice(cpuChoiceList)  
        else:    
            if cpuChoice[2] < 3:
                cpuChoice = cpuChoiceList[4]
                if cpuChoice[2] in boxesPicked:
                    while cpuChoice[2] in boxesPicked:
                        cpuChoice = random.choice(cpuChoiceList)                                          #60% chance of center pick
            elif cpuChoice[2] in boxesPicked:
                pickRandomCorner()
        
        pt = Point(cpuChoice[0], cpuChoice[1])
        X = Image(pt,"ttt-x.png")
        X.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def bplayerTurn1():
        place = win.getMouse()
        place = relocate(place)                                   
        O = Image(place,"ttt-o.png")
        O.draw(win) 

    def bcpuTurn2():
        counterMove()      
        
        pt = Point(cpuChoice[0], cpuChoice[1])
        X = Image(pt,"ttt-x.png")
        X.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def bplayerTurn2():
        place = win.getMouse()
        place = relocate(place)                                   
        O = Image(place,"ttt-o.png")
        O.draw(win) 

    def bcpuTurn3():
        counterMove()

        pt = Point(cpuChoice[0], cpuChoice[1])
        X = Image(pt,"ttt-x.png")
        X.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def bplayerTurn3():
        place = win.getMouse()
        place = relocate(place)                                   
        O = Image(place,"ttt-o.png")
        O.draw(win) 

    def bcpuTurn4():
        counterMove()

        pt = Point(cpuChoice[0], cpuChoice[1])
        X = Image(pt,"ttt-x.png")
        X.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()

    def bplayerTurn4():
        place = win.getMouse()
        place = relocate(place)  
        O = Image(place,"ttt-o.png")
        O.draw(win)                                 
        
    
    def bcpuTurn5():
        counterMove()

        pt = Point(cpuChoice[0], cpuChoice[1])
        X = Image(pt,"ttt-x.png")
        X.draw(win)
         
        boxesPicked.append(cpuChoice[2])
        cpuPicked.append(cpuChoice[2])
        didCPUWin.append(cpuChoice[2])
        cpucChecker()
    

## beginning of kolby's code

    if p1xc == 0:
        playerTurn1()
        gameOverChecker()
        turnChecker()
        cpuTurn1()
        gameOverChecker()
        turnChecker()
        playerTurn2()
        gameOverChecker()
        turnChecker()
        cpuTurn2()
        gameOverChecker()
        turnChecker()
        playerTurn3()
        gameOverChecker()
        turnChecker()
        cpuTurn3()
        gameOverChecker()
        turnChecker()
        playerTurn4()
        gameOverChecker()
        turnChecker()
        cpuTurn4()
        gameOverChecker()
        turnChecker()
        playerTurn5()
        gameOverChecker()
        turnChecker()
    elif p1xc == 1:
        bcpuTurn1()
        gameOverChecker()
        turnChecker()
        bplayerTurn1()
        gameOverChecker()
        turnChecker()
        bcpuTurn2()
        gameOverChecker()
        turnChecker()
        bplayerTurn2()
        gameOverChecker()
        turnChecker()
        bcpuTurn3()
        gameOverChecker()
        turnChecker()
        bplayerTurn3()
        gameOverChecker()
        turnChecker()
        bcpuTurn4()
        gameOverChecker()
        turnChecker()
        bplayerTurn4()
        gameOverChecker()
        turnChecker()
        bcpuTurn5()
        gameOverChecker()
        turnChecker()


    

def relocateError(): 
    global relocate                                           #display error message
    errorMessage = Text(Point(win.getWidth()/2,80),
                        "Please click within a square")
    errorMessage.setOutline("red")
    errorMessage.draw(win)
    place = win.getMouse()
    errorMessage.undraw()
    place = relocate(place)
    return place

    
def alreadyPickedError():
    global relocate
    errorMessage = Text(Point(win.getWidth()/2,80),
                        "This square is already used... try again.")
    errorMessage.setOutline("red")
    errorMessage.draw(win)
    place = win.getMouse()
    errorMessage.undraw()
    place = relocate(place)
    return place

    
def xoSelect():                                                 #display shape selection menu boxes
    global xBox
    xBox = Rectangle(Point(100,350),Point(400,250))
    xBox.setFill("gray")
    xBox.draw(win)
    global oBox
    oBox = Rectangle(Point(100,200),Point(400,100))
    oBox.setFill("light green")
    oBox.draw(win)
    global xText
    xText = Text(Point(win.getWidth()/2,300),
                 "Click here to play as X")
    xText.draw(win)
    global oText
    oText = Text(Point(win.getWidth()/2,150),
                 "Click here to play as O")
    oText.draw(win)

def selectScreenError():                                        #display misclick error on shape select screen
    if 'selectError' in globals():                              #no need to draw multiple errors for multiple misclicks
        return
    global selectError
    selectError = Text(Point(win.getWidth()/2,50),
                       "Please make a selection")
    selectError.setOutline("red")
    selectError.draw(win)
    
def startScreenError():                                         #display mislick error on start screen
    if 'startError' in globals():                               #no need to draw multiple errors for multiple misclicks
        return
    global startError
    startError = Text(Point(win.getWidth()/2,50),
                        "Please make a selection")
    startError.setOutline("red")
    startError.draw(win)

def main():                                                     #main function
    startScreen()                                               #display start screen
    count = 0
    while count < 1:
        pt = win.getMouse()                                     #read user selection on start screen
        if isBetween(pt.getX(),100,400) and isBetween(pt.getY(),250,350):
            if 'startError' in globals():
                startError.undraw()
            pvpMode()
            count = count+1
        elif isBetween(pt.getX(),100,400) and isBetween(pt.getY(),100,200):
            if 'startError' in globals():
                startError.undraw()
            pvcMode()
            count = count+1
        else:
            startScreenError()


    
main()
