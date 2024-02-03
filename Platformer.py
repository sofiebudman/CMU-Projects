  ###INSTRUCTIONS:
##Use arrow keys to navigate  your player through the platforms, collect coins and avoid the spikes.
##reach the flag to get to th next level
## There will be other elements such a bounce pads and moving obstacles that will either assisst or harm your player
##turn on volume to hear sound effect
## try to reach the end with the highest score possible
## ***if needed there is a cheat button to skip level. Press n to skip a level. Try to play each level before though!
## Goodluck!
###*note: due to delays while running on a slow computer there may be some bugs when first loading, if issue continues try refreshing

###beginning print message, shortened version of the instructions
print("Welcome to platformer game")
print("Use arrow keys or WASD to navigate your player through   the platforms, collect coins, and avoid spikes")
print('Have fun!!')

###custom app properties
app.stepsPerSecond = 40
app.level = -2
app.isJumping = False

#This array contains the game colors which helps make the colors more easy to access and manipulate:
#0-player, 1-background, 2-platforms, 3-outsidecoin, 4-insidecoin, 5-spikefill, 6-spike border, 7-flag color
app.colors = ['lightSkyBlue', rgb(10,10,99), 'lightCyan', 'lightCyan', 'deepSkyBlue', rgb(121,190,219), rgb(41,108,181), rgb(54,235,255)]

#score 
scoreLabel = Label("score:", 30,20, fill = 'white', size = 17, font = 'montserrat', bold = True)
score = Label(0, 70,20,fill = 'white', size = 17, font = 'montserrat')

###more custom app properties
#these booleons keep track of if a coin has been collected already or not. So if a player dies, they don't have the oppourtunity to get points back.
app.coinOneCollected = False
app.coinTwoCollected = False
app.coinThreeCollected = False
app.gameStart = False
app.background = app.colors[1]

###sound effects
coinCollectedOneS = Sound("cmu://681287/28197671/coin.mp3")
coinCollectedTwoS= Sound("cmu://681287/28197671/coin.mp3")
coinCollectedThreeS = Sound("cmu://681287/28197671/coin.mp3")
jumpPad = Sound("cmu://681287/28197678/jumppad.mp3")
nextLevelSound = Sound("cmu://681287/28252208/nextlevel.wav")
dieSound = Sound("cmu://681287/28252259/hit.wav")
backgroundMusic = Sound("cmu://681287/28252945/videogameBG.wav")
backgroundMusic.play(loop = True)

###shape group: players and game elements
flag = Group(
    Line(600,600,600,560, fill = app.colors[7]), 
    Rect(570,560,30,20, fill = app.colors[7])
    )
    
#spikeballs for level 5
spikeBallOne = Star(200,300,20,16,roundness = 70, fill = app.colors[5], border = app.colors[6],visible = False)
spikeBallOne.dx = 5
spikeBallOne.dy = 5
spikeBallTwo = Star(100,300,20,16,roundness = 70, fill = app.colors[5], border = app.colors[6],visible = False)
spikeBallTwo.dx = 7
spikeBallTwo.dy = 5
spikeBallThree = Star(300,200,20,16,roundness = 70, fill = app.colors[5], border = app.colors[6],visible = False)
spikeBallThree.dx = 5
spikeBallThree.dy = 7
spikeBallFour = Star(300,100,20,16,roundness = 70, fill = app.colors[5], border = app.colors[6], visible = False)
spikeBallFour.dx = 5
spikeBallFour.dy = 5


##PLAYER
#to use the updateColors method later in the code, many elements of a group are stored as child properties   
playerFace = Rect(200,200,30,30, fill = app.colors[0], align = 'center')
player = Group(
    
    )
player.add(playerFace,Rect(193,195,9,9,fill = 'white', align = 'center'),Rect(207,195,9,9,fill = 'white', align = 'center'),Rect(193,195,3.5,3.5,align = 'center'),Rect(207,195,3.5,3.5,align = 'center'))
#custom player properties
player.vy = 0


##COINS
outsideCoinOne = Circle(300,100,15,fill = app.colors[3], opacity = 20)
insideCoinOne = Circle(300,100,7,fill = app.colors[4], opacity = 30)
coinOne = Group(
    )
coinOne.add(outsideCoinOne,insideCoinOne)
outsideCoinTwo = Circle(300,100,15,fill = app.colors[3], opacity = 20)
insideCoinTwo = Circle(300,100,7,fill = app.colors[4], opacity = 30)
coinTwo = Group(
    )
coinTwo.add(outsideCoinTwo,insideCoinTwo)
outsideCoinThree = Circle(300,100,15,fill = app.colors[3], opacity = 20)
insideCoinThree = Circle(300,100,7,fill = app.colors[4], opacity = 30)
coinThree = Group(
    )
coinThree.add(outsideCoinThree,insideCoinThree)

#BOUNCEPAD
bP1 =Rect(370,370,30,30, fill = app.colors[2], border = app.colors[6])
bP2 = Line(385,370,385,363, fill = app.colors[6])
bP3 = Line(370,363,400,363, fill = app.colors[6])
bouncePad = Group(
    
    )
bouncePad.add(bP1,bP2,bP3)
bouncePad.visible = False

#SPIKES
tsOne = RegularPolygon(200,200,17,3, fill = app.colors[5], border = app.colors[6])
tsTwo = RegularPolygon(230,200,17,3, fill = app.colors[5], border = app.colors[6])
tsThree = RegularPolygon(260,200,17,3, fill = app.colors[5], border = app.colors[6])
threeSpikes = Group(
    
)
threeSpikes.add(tsOne,tsTwo,tsThree)
threeSpikes.visible = False
oneSpike = RegularPolygon(200,200,17,3, fill = app.colors[5], border = app.colors[6])
oneSpike.visible = False
##PLATFORMS
#level 1
oneOne = Line(30,370,100,370,fill = app.colors[2], lineWidth = 3, visible = False)
oneTwo = Line(135,330,220,330,fill = app.colors[2], lineWidth = 3, visible = False)
oneThree = Line(265,300,350,300,fill = app.colors[2], lineWidth = 3, visible = False)
oneFour = Line(370,260,400,260,fill = app.colors[2], lineWidth = 3, visible = False)
#level two
twoOne = Line (0,370,400,370,fill = app.colors[2], lineWidth = 3, visible = False)

#level three
threeOne = Line(0,350,50,350, fill = app.colors[2], lineWidth = 3, visible = False)
threeTwo = Line(90,320,120,320, fill = app.colors[2], lineWidth = 3, visible = False)
threeThree = Line(140,260,210,260, fill = app.colors[2], lineWidth = 3, visible = False)
threeFour = Line(160,170,190,170, fill = app.colors[2], lineWidth = 3, visible = False)
threeFive = Line(270,225,330,225, fill = app.colors[2], lineWidth = 3, visible = False)
threeSix = Line(270,110,360,110, fill = app.colors[2], lineWidth = 3, visible = False)
threeSeven = Line(360,50,400,50, fill = app.colors[2], lineWidth = 3, visible = False)

#level 4
fourOne = Line(0,220, 50,220, fill = app.colors[2], lineWidth = 3, visible = False)
fourTwo = Line(45,300,170,300, fill = app.colors[2], lineWidth = 3, visible = False)
fourThree = Line(220,360,320,360, fill = app.colors[2], lineWidth = 3, visible = False)
fourFour = Line(300,70,350,70,fill = app.colors[2], lineWidth = 3, visible = False)

#level 5
fiveOne = Line(0,370,400,370,fill = app.colors[2], lineWidth = 3, visible = False)
#different levels are added to this group
platforms = Group(

    )
    
###INSTRUCTION SCREEN
instructions1 = Image("cmu://681287/28224950/insturctions+two+(1).png",0,0, visible = False)
instructions2 = Image("cmu://681287/28225020/insturctions+two+(2).png",0,0,visible = False)
instructions3 = Image("cmu://681287/28226136/instruction+3.png", 0,0,visible = False)
youWin = Image("cmu://681287/28335560/youwin.png", 0,0,visible = False)
##click these rectangles to change the color theme of the game
blueTheme = Rect(50,270,50,50, fill = 'skyBlue', visible = False)
greenTheme = Rect(110,270,50,50,fill = 'paleGreen', visible = False)
yellowTheme = Rect(170,270,50,50,fill = 'gold', visible = False)
pinkTheme = Rect(230,270,50,50,fill = rgb(255,158,236), visible = False)
greyTheme = Rect(290,270,50,50,fill = 'gainsboro', visible = False)
selectedColor = Rect(50,270,52,52,fill = None, border = 'dodgerBlue', borderWidth = 3, visible = False)

###UPDATE COLORS
#method to update colors using the app.colors array, makes changing the color theme more efficient and easier to debug and modify
def updateColors():
    playerFace.fill = app.colors[0]
    app.background = app.colors[1]
    outsideCoinOne.fill = app.colors[3]
    outsideCoinTwo.fill = app.colors[3]
    outsideCoinTwo.fill = app.colors[3]
    insideCoinOne.fill = app.colors[4]
    insideCoinTwo.fill = app.colors[4]
    insideCoinTwo.fill = app.colors[4]
    threeSpikes.fill = app.colors[5]
    oneSpike.fill = app.colors[5]
    tsOne.border = app.colors[6]
    tsTwo.border = app.colors[6]
    tsThree.border = app.colors[6]
    oneSpike.border = app.colors[6]
    flag.fill = app.colors[7]
    bP1.fill = app.colors[2]
    bP1.border = app.colors[6]
    bP2.fill = app.colors[6]
    bP3.fill = app.colors[6]
    spikeBallOne.fill = app.colors[5]
    spikeBallOne.border = app.colors[6]
    spikeBallTwo.fill = app.colors[5]
    spikeBallTwo.border = app.colors[6]
    spikeBallThree.fill = app.colors[5]
    spikeBallThree.border = app.colors[6]
    spikeBallFour.fill = app.colors[5]
    spikeBallFour.border = app.colors[6]
    
   
### set game element method
#this method has many parameters, but it makes setting up each level much more convient
#you set the visibility and location of commonly used game elements to make the setUpLevel() method shorter
def setGameElements(coinOneVisible, coinOneX, coinOneY, coinTwoVisible, coinTwoX, coinTwoY,coinThreeVisible, coinThreeX, coinThreeY, threeSpikesVisible, threeSpikesX, threeSpikesBottom, oneSpikeVisible, oneSpikeX, oneSpikeBottom, flagX, flagBottom, bouncePadVisible, bouncePadX,bouncePadBottom ):
    if(app.coinOneCollected == False):
        if(coinOneVisible == True):
            coinOne.centerX = coinOneX
            coinOne.centerY = coinOneY
            coinOne.visible = True
        elif(coinOneVisible == False):
            coinOne.visible = False
    else:
        coinOne.visible = False
    if(app.coinTwoCollected == False):
        if(coinTwoVisible == True):
            coinTwo.centerX = coinTwoX
            coinTwo.centerY = coinTwoY
            coinTwo.visible = True
        elif(coinTwoVisible == False):
            coinTwo.visible = False
    else:
        coinTwo.visible = False
    if(app.coinThreeCollected == False):
        if(coinThreeVisible == True):
            coinThree.centerX = coinThreeX
            coinThree.centerY = coinThreeY
            coinThree.visible = True
        elif(coinThreeVisible == False):
            coinThree.visible = False
    else:
        coinThree.visible = False
            
            
    if(threeSpikesVisible == True):
        threeSpikes.centerX = threeSpikesX
        threeSpikes.bottom = threeSpikesBottom
        threeSpikes.visible = True
    elif(threeSpikesVisible == False):
        threeSpikes.visible = False
    if(oneSpikeVisible == True):
        oneSpike.centerX = oneSpikeX
        oneSpike.bottom = oneSpikeBottom
        oneSpike.visible = True
    elif(oneSpikeVisible == False):
        oneSpike.visible = False
        
    if(bouncePadVisible == True):
        bouncePad.visible = True
        bouncePad.centerX = bouncePadX
        bouncePad.bottom = bouncePadBottom
    elif(bouncePadVisible == False):
        bouncePad.visible = False
    flag.centerX = flagX
    flag.bottom = flagBottom
    if(bouncePadVisible == True):
        bouncePad.centerX = bouncePadX
        bouncePad.bottom = bouncePadBottom
        bouncePad.visible = True
    else:
        bouncePad.visible == False
        
### method to set up level
#the parameter is the level
#negative levels represents the instructions screens
#uses the previous method to set up spikes, flags, coins, and other elements
def setUpLevel(level):
    ##this is used to reset what the character looks like
    player.visible = True
    player.opacity = 100
    #level -2 represents the intro screen
    if(level == -2):
        instructions1.visible = True
    #level -1 represents the instructions screen
    if(level == -1):
        instructions2.visible = True
        instructions1.visible = False
        player.centerX = 45
        player.bottom = 370
    #level 0 is the settings screen
    if(level == 0):
        blueTheme.visible = True
        greenTheme.visible = True
        yellowTheme.visible = True
        pinkTheme.visible = True
        greyTheme.visible = True
        selectedColor.visible = True
        instructions3.visible = True
        instructions2.visible = False
        instructions1.visible = False
    if(level == 1):
        player.centerX = 45
        player.centerY = 0
        instructions3.visible = False
        instructions1.visible = False
        selectedColor.visible = False
        platforms.add(oneOne,oneTwo,oneThree,oneFour)
        threeSpikes.rotateAngle = 0
        oneSpike.rotateAngle = 0
        #use the setGameElements to position the coins, spikes, etc.
        setGameElements(True,175,280,True,300,246,False, 600,600, False,600,600,False, 600,600, 380,260, False, 600,600)

    if(level == 2):
        platforms.remove(oneOne)
        platforms.remove(oneTwo)
        platforms.remove(oneThree)
        platforms.remove(oneFour)
        platforms.add(twoOne)
        player.centerX = 45
        player.centerY = 0
        
        setGameElements(True,190,300,False,600,600,False,600,600,True,280,370,True,130,370,380,370, False,600,600)
    if(level == 3):
        platforms.remove(twoOne)
        platforms.add(threeOne)
        platforms.add(threeTwo)
        platforms.add(threeThree)
        platforms.add(threeFour)
        platforms.add(threeFive)
        platforms.add(threeSix)
        platforms.add(threeSeven)
        player.centerX = 45
        player.centerY = 0
        threeSpikes.rotateAngle = 180
        oneSpike.rotateAngle = 180
        
        setGameElements(True,300,180,True,168,76,False,600,600,True,313.5,137,True,176,195,380,49, False,600,600)
        #(coinOneVisible, coinOneX, coinOneY, coinTwoVisible, coinTwoX, coinTwoY,coinThreeVisible, coinThreeX, coinThreeY, threeSpikesVisible, threeSpikesX, threeSpikesBottom, oneSpikeVisible, oneSpikeX, oneSpikeBottom, flagX, flagBottom, bouncePadVisible, bouncePadX,bouncePadBottom ):
    if(level == 4):
        player.centerX = 45
        player.centerY = 0
        platforms.remove(threeOne)
        platforms.remove(threeTwo)
        platforms.remove(threeThree)
        platforms.remove(threeFour)
        platforms.remove(threeFive)
        platforms.remove(threeSix)
        platforms.remove(threeSeven)
        platforms.add(fourOne,fourTwo,fourThree,fourFour)
        threeSpikes.rotateAngle = 0
        setGameElements(True,270,270,False, 600,600,False, 600,600,True,90,300,False,600,600,330,70,True,240,360)
        
    if(level == 5):
        player.centerX = 45
        player.centerY = 0
        platforms.remove(fourOne)
        platforms.remove(fourTwo)
        platforms.remove(fourThree)
        platforms.remove(fourFour)
        platforms.add(fiveOne)
        setGameElements(False,600,600,False,600,600,False,600,600,False,600,600,False,600,600,360,370,False,600,600)
        spikeBallOne.visible = True
        spikeBallTwo.visible = True
        spikeBallThree.visible = True
        spikeBallFour.visible = True
    #level 6 represents the you win screen
    if(level == 6):
        youWin.visible = True
        app.stop()
        platforms.remove(fiveOne)
        setGameElements(False,600,600,False,600,600,False,600,600,False,600,600,False,600,600,600,600,False,600,600)
        spikeBallOne.visible = False
        spikeBallTwo.visible = False
        spikeBallThree.visible = False
        spikeBallFour.visible = False 
        coinCollectedOneS.pause()
        coinCollectedTwoS.pause()
        coinCollectedThreeS.pause()
        jumpPad.pause()
        nextLevelSound.pause()
        scoreLabel.centerX =170
        scoreLabel.centerY = 144
        score.centerX = 220
        score.centerY = 144
        scoreLabel.fill = 'black'
        score.fill = 'black'
        scoreLabel.toFront()
        score.toFront() 
setUpLevel(app.level)
### Death Animation 
def die():
    #the player flashes and slowly loses opacity
    
    player.visible = False
    sleep(0.1)
    player.opacity -= 20
    player.visible = True
    sleep(0.1)
    player.visible = False
    sleep(0.1)
    player.opacity -= 20
    player.visible = True
    sleep(0.1)
    player.visible = False
    sleep(0.1)
    player.opacity -= 20
    player.visible = True
    sleep(0.1)
    player.visible = False
    sleep(0.1)
    score.value -=2
    setUpLevel(app.level)
    
        
#method to move onto the next level if the player hits the flag
def nextLevel():
    if(player.hitsShape(flag) == True and flag.visible == True):
        if(app.gameStart == True):
            nextLevelSound.play()
        
        app.coinOneCollected = False
        app.coinTwoCollected = False
        app.coinThreeCollected = False
        app.level +=1
        score.value +=10
        setUpLevel(app.level)
        

#this method is the logic for jumping and gravity        
def checkPlatformHits():
    if(app.gameStart == True):
        player.vy -=1
        if(player.hitsShape(platforms) == True):
            player.centerY -=1
            if(player.hitsShape(platforms) == True):
                player.centerY -=1
                if(player.hitsShape(platforms) == True):
                    player.centerY -=1
                    if(player.hitsShape(platforms) == True):
                        player.centerY -=1
                    if(player.hitsShape(platforms)== True):
                        player.centerY -=1
                    
                        player.centerY +=5
        player.centerY -=player.vy
        if(player.hitsShape(platforms)== True):
            player.centerY += player.vy
            player.vy = 0
        player.centerY +=1
        if(player.hitsShape(platforms) == True):
            if(app.isJumping == True):
                player.vy =16
    
#player movement   
def onKeyHold(keys):
    if(('a' in keys) or ('left' in keys)):
        player.centerX -=9
    if(('d' in keys) or ('right' in keys)):
        player.centerX +=9
    if(('up' in keys) or ('w' in keys)):
        app.isJumping = True
    
def onKeyRelease(key):
    #this is used for jumping logic
    app.isJumping = False
    
### Onstep loop, where the game is "run"
#This loop contains calls to previously declared methods
def onStep():
    #change the app.level in intro screen
    if(app.level == -1):
        setUpLevel(-1)
    if(app.level == 0):
        setUpLevel(0)
    checkPlatformHits()
    nextLevel()
    
    
    #sets up spikeball movement
    if(app.level == 5):
        spikeBallOne.centerX += spikeBallOne.dx
        spikeBallOne.centerY += spikeBallOne.dy
        spikeBallTwo.centerX += spikeBallTwo.dx
        spikeBallTwo.centerY += spikeBallTwo.dy
        spikeBallThree.centerX += spikeBallThree.dx
        spikeBallThree.centerY += spikeBallThree.dy
        spikeBallFour.centerX += spikeBallFour.dx
        spikeBallFour.centerY +=spikeBallFour.dy
        if(spikeBallOne.left <= 0):
            spikeBallOne.dx = 5
        if(spikeBallOne.right >= 400):
            spikeBallOne.dx = -5
        if(spikeBallOne.top <= 0):
            spikeBallOne.dy = 5
        if(spikeBallOne.bottom >= 370):
            spikeBallOne.dy = -5
            
        if(spikeBallTwo.left <= 0):
            spikeBallTwo.dx = 7
        if(spikeBallTwo.right >= 400):
            spikeBallTwo.dx = -7
        if(spikeBallTwo.top <= 0):
            spikeBallTwo.dy = 5
        if(spikeBallTwo.bottom >= 370):
            spikeBallTwo.dy = -5
            
        if(spikeBallThree.left <= 0):
            spikeBallThree.dx = 5
        if(spikeBallThree.right >= 400):
            spikeBallThree.dx = -5
        if(spikeBallThree.top <= 0):
            spikeBallThree.dy = 7
        if(spikeBallThree.bottom >= 370):
            spikeBallThree.dy = -7
            
        if(spikeBallFour.left <= 0):
            spikeBallFour.dx = 5
        if(spikeBallFour.right >= 400):
            spikeBallFour.dx = -5
        if(spikeBallFour.top <= 0):
            spikeBallFour.dy = 5
        if(spikeBallFour.bottom >= 370):
            spikeBallFour.dy = -5
        
    

    #bouncepad logic
    if(player.hitsShape(bouncePad)== True and bouncePad.visible == True):
        player.bottom = bouncePad.top
        if(app.isJumping == True):
            player.vy = 25
            jumpPad.play()
        else:
           player.vy = -1

            
    #checks falling
    if(player.centerY >= 390 and app.gameStart == True):
        die()
        
        
    #checks spike hits
    if(((player.hitsShape(threeSpikes) == True) and (threeSpikes.visible == True) )or ((player.hitsShape(oneSpike) == True) and (oneSpike.visible == True)) and app.gameStart == True):
        
        dieSound.play()
        die()
        

    #prevents offscreen motion
    if(player.left < 0):
        player.left = 0
    if(player.centerX > 400):
        player.right = 400
    
    #check spikeball hits
    if((player.hitsShape(spikeBallOne) == True and spikeBallOne.visible == True) or (player.hitsShape(spikeBallTwo) == True and spikeBallTwo.visible == True) or (player.hitsShape(spikeBallThree) == True and spikeBallThree.visible == True) ):
        dieSound.play()
        die()
        spikeBallOne.centerX = 200
        spikeBallOne.centerY = 300
        spikeBallTwo.centerX = 100
        spikeBallTwo.centerX = 300
        spikeBallThree.centerX = 300
        spikeBallThree.centerY = 200
        spikeBallFour.centerX = 300
        spikeBallFour.centerY = 100
        
    #check coin hits    
    if(player.hitsShape(coinOne) == True and coinOne.visible == True and app.gameStart == True):
        coinOne.visible = False
        score.value +=2
        app.coinOneCollected = True
        coinCollectedOneS.play()
    if(player.hitsShape(coinTwo) == True and coinTwo.visible == True and app.gameStart == True):
        coinTwo.visible = False
        score.value +=2
        app.coinTwoCollected = True
        coinCollectedTwoS.play()
        
    if(player.hitsShape(coinThree) == True and coinThree.visible == True and app.gameStart == True):
        coinThree.visible = False
        score.value +=2
        app.coinThreeCollected = True
        coinCollectedThreeS.play()
#the on mouse press function is used to help the player customize the game color
def onMousePress(mouseX,mouseY):
     
        if(blueTheme.contains(mouseX, mouseY) == True and blueTheme.visible == True):
            app.colors[0] = 'lightSkyBlue'
            app.colors[1] = rgb(10,10,99)
            app.colors[2] = 'lightCyan'
            app.colors[3] = 'lightCyan'
            app.colors[4] = 'deepSkyBlue'
            app.colors[5] = rgb(121,190,219)
            app.colors[6] = rgb(41,108,181)
            app.colors[7] = rgb(54,235,255)
            selectedColor.left = 50

        if(greenTheme.contains(mouseX,mouseY) == True and greenTheme.visible == True):
            app.colors[0] = 'darkSeaGreen'
            app.colors[1] = rgb(8,46,9)
            app.colors[2] = 'honeyDew'
            app.colors[3] = 'chartreuse'
            app.colors[4] = 'mediumSeaGreen' 
            app.colors[5] = 'oliveDrab'
            app.colors[6] = 'darkOliveGreen'
            app.colors[7] =  'yellowGreen'
            selectedColor.left  = 110 
        if(yellowTheme.contains(mouseX,mouseY )== True and yellowTheme.visible == True):
            app.colors[0] = 'gold'
            app.colors[1] = rgb(128,103,4)
            app.colors[2] = 'lightYellow'
            app.colors[3] = 'paleGoldenRod'
            app.colors[4] = 'khaki' 
            app.colors[5] = 'lightGoldenrodYellow'
            app.colors[6] = 'papayaWhip'
            app.colors[7] =  'yellow'
            selectedColor.left  = 170
        if(pinkTheme.contains(mouseX,mouseY) == True and pinkTheme.visible == True):
            app.colors[0] = 'pink'
            app.colors[1] = rgb(140,8,68)
            app.colors[2] = 'lavenderBlush'
            app.colors[3] = 'deepPink'
            app.colors[4] = 'hotPink' 
            app.colors[5] = 'paleVioletRed'
            app.colors[6] = 'mediumVioletRed'
            app.colors[7] =  'lightPink'
            selectedColor.left  = 230
        if(greyTheme.contains(mouseX,mouseY) == True and greyTheme.visible == True):
            app.colors[0] = 'gainsboro'
            app.colors[1] = rgb(70,70,70)
            app.colors[2] = rgb(155,155,155)
            app.colors[3] = 'lightGray'
            app.colors[4] = 'silver' 
            app.colors[5] = 'darkGray'
            app.colors[6] = 'gray'
            app.colors[7] =  'gray'
            selectedColor.left  = 290
            
        updateColors()
            
            
        
def onKeyPress(key):
    if(key == 'space' and app.gameStart == False):
        if(app.level == -2 or app.level ==  -1):
            app.level +=1
            
        elif(app.level == 0):
            app.level = 1
            instructions3.visible = False
            blueTheme.visible = False 
            greenTheme.visible = False
            yellowTheme.visible = False
            pinkTheme.visible = False
            greyTheme.visible = False
            app.gameStart = True
            setUpLevel(1)
            score.value = 0
    ##cheat button
    if(key == 'n'):
        app.level +=1
        setUpLevel(app.level)
            
            

            
    


        

    
