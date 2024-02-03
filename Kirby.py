# INSTRUCTIONS!!!
#Drag your mouse around the canvas to draw a chain of Kirby's stars
#press the color blocks to change kirby's color
#have fun!
Label("Instructions", 200,100, size = 40, font = 'montserrat', bold = True)
Label('1. Drag your mouse around the canvas to draw stars', 55, 140, align = 'left', font = 'montserrat')
Label('2. Press color blocks to change the color of Kirby',55 ,160, align = 'left', font = 'montserrat')
Label('3. Enjoy!', 55, 180,align = 'left', font = 'montserrat')
#Note: it takes 5 seconds for project to load from instruction screen
sleep(5)
Rect(0,0,400,200, fill = 'white')
RegularPolygon(200,200,300,4, rotateAngle= 45, fill = 'grey', opacity = 5)
Line(0,350,400,350,lineWidth = 1, dashes = True)
    
def drawKirby(bodyColor, borderColor, footColorOne, footColorTwo):
    #background
    

    #rightfooot
    Oval(165,130,55,85, fill =gradient(footColorOne,footColorTwo), rotateAngle = 50)
    
    #body 
    Circle(100,100,75,fill = bodyColor,border =borderColor,borderWidth = 3)
    Oval(84,129,15,9,fill = rgb(237,74,124), opacity = 60)
    Oval(153,127,15,9,fill = rgb(237,74,124), opacity = 60)
    #hammer
    Oval(155,270,40,60,rotateAngle = -74, fill = rgb(200,200,200),border = rgb(160,164,166),borderWidth = 4)
    Rect(110,150,18,100, rotateAngle = -40, fill = rgb(122, 79,35), border = rgb(91,56,18))
    Oval(142,231,20,80,rotateAngle = 20,fill = rgb(122,79,35), border = rgb(91,56,18))
    Oval(189,249,20,80,rotateAngle = 20,fill = rgb(122,79,35), border = rgb(91,56,18))
    Rect(140,200,50,80, rotateAngle = 20,fill = rgb(122,79,35))
    Oval(176,210,40,60, rotateAngle = -74, fill = rgb(255,87,94), border = rgb(242,246,247), borderWidth =4)
    Star(176,210,16,5,roundness = 40,rotateAngle = 80, fill = rgb(253,254,108))
    #left arm
    Oval(80,170,40,60,fill = bodyColor, rotateAngle = -20,border =borderColor,borderWidth = 1)
    #rightarm
    Oval(130,170,40,60,fill = bodyColor, rotateAngle = 20,border =borderColor,borderWidth = 1)
    #leftFoot
    Oval(45,140,65,87, fill =gradient(footColorOne, footColorTwo), rotateAngle = -30)
    
    #footedge covers
    Rect(98,132,50,30,fill = bodyColor, rotateAngle = -23)
    Rect(81,140,25,31,fill = bodyColor)
    
    #Eyes
    Oval(105,110,20,35,rotateAngle = 2,fill = gradient('black', 'blue'))
    Oval(135,110,20,35,rotateAngle = -2,fill = gradient('black', 'blue'))
    Oval(135,102,14,16,fill = 'white')
    Oval(105,102,14,16,fill = 'white')
    Line(143,92,121,102,lineWidth = 3)
    Line(95,91,117,101,lineWidth = 3)
    Polygon(93,89,115,98,50,50,fill = bodyColor)
    Polygon(143,90,121,100,100,50,fill = bodyColor)
    
    #mouth
    Circle(120,135,4,fill = 'black')  
    
    #Kirby 
    Label('K', 320,60,size = 50, font = 'montserrat', bold = True, fill = bodyColor, border = borderColor)  
    Label('I', 320,120, size = 50, font = 'montserrat', bold = True,  fill = bodyColor, border = borderColor)
    Label('R', 320,180,size = 50,font = 'montserrat', bold = True,  fill = bodyColor, border = borderColor)  
    Label('B', 320,240, size = 50, font = 'montserrat', bold = True,  fill = bodyColor, border = borderColor)
    Label('Y', 320,300,size = 50, font = 'montserrat', bold = True, fill = bodyColor, border = borderColor)
#color boxes   
Rect(280,360,30,30,fill = rgb(231,145,191))
Rect(320,360,30,30, fill = rgb(137,223,125))
Rect(360,360,30,30,fill = rgb(62,215,241))
Rect(240,360,30,30, fill = rgb(255,228,30))
Rect(200,360,30,30,fill = rgb(193,193,193))
Rect(160,360,30,30,fill = rgb(245,72,101))
Label('Chose a color:',80,375,size = 20, font = 'montserrat')

    
  
#draws kirby of colors(bodyColor, borderColor, footColorOne, footColorTwo)
#if statements are used to make sure mouse is pressing corresponding box

def onMousePress(mouseX, mouseY):
    if(mouseX >280 and mouseX<310 and mouseY>360 and mouseY<390):
        drawKirby(rgb(231,145,191), rgb(210,60,99), rgb(191,10,49), rgb(210,31,60))
    if(mouseX>320 and mouseX <350 and mouseY >360 and mouseY <390):
        drawKirby(rgb(137,223,125), rgb(79,157,69), rgb(240,190,66), rgb(184,136,15))
    if(mouseX>360 and mouseX <390 and mouseY>360 and mouseY<390):
        drawKirby(rgb(62,215,241), rgb(47,167,211), rgb(51,57,248), rgb(3,7,140))
    if(mouseX>240 and mouseX <270 and mouseY>360 and mouseY<390):
        drawKirby(rgb(255,228,30), rgb(255,215,1), rgb(253,95,0), rgb(203,73,1))
    if(mouseX>200 and mouseX <230 and mouseY>360 and mouseY<390):
        drawKirby(rgb(193,193,193), rgb(158,158,158), rgb(52,52,52), rgb(76,76,76))
    if(mouseX>160 and mouseX <190 and mouseY > 360 and mouseY<390):
        drawKirby(rgb(245,72,101), rgb(211,29,54), rgb(167,29,88), rgb(70,12,37))


#code for drawing stars

def onMouseDrag(mouseX, mouseY):
    Star(mouseX, mouseY,10,5, fill = 'yellow', border = 'gold', roundness = 60)
    

#Color References 
#Pink Body(231,145,191)
#Pink Body Border (210,60,99)
#foot Color 1 = 191,10,49, 
#foot color 2 = 210,31,60
 
#Greenbody(137,223,125)
#Greenbody border (79,157,69)
#Greenfootcolor1 (240,190,66)
#Greenfootcolor2 (184,136,15)

#Blue body (62,215,241)
#bluebody border(47,167,211)
#bluefootcolor 1 (51,57,248)
#bluefootcolor2(3,7,140)

#Yellow Body (255,228,30)
#Yellow body border(255,215,1)
#yellow foot color 1(253,95,0)
#yellow foot color 2 (203,73,1)

#greybody (193,193,193)
#greybody border(158,158,158)
#Grey foot color 1(52,52,52)
#Grey foot color 2(76,76,76)

#red body (245,72,101)
#red body border  (211,29,54)
#red foot color 1 (167,29,88)
#red foot color 2 (70,12,37)

