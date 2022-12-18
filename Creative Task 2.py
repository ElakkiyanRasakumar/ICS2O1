from cmu_graphics import *

# Fill me in!
# Drag shape on a piece of stone, and rotate one of the pieces to acertain angle (maygbe make it so they have to find how many click as a easter egg on the xcreen)
#and when all of them are there release the princess and win game incorprate random rotateagnle

#How to win, find the number of times you need to press the pentagon to revela the key. Then being the key to the princess, and drag the princess to the wizard withouht touching the cage


app.background=gradient(rgb(49, 41, 118), rgb(48, 101, 151), rgb(46, 176, 190), start='left-top')
import random
app.stepsPerSecond = 1

invisble_counter = Label(1, 200, 200, visible=False)
intro1 = Label("Welcome to my game", 280, 50, visible=False, size=14)
intro2 = Label('Rotate the pentagon, to find the key,', 280, 75, visible=False, size=14)
intro3 = Label('to reunite the Princess with its parents', 280, 100, visible=False, size=14)
hint = Label(randrange(2, 10), 95, 183, visible=False, size=20)
toStopLoseTrigger = Rect(0, 0, 400, 400, fill=None)
toStopClickEarly = Rect(0, 0, 400, 400, fill=None) # to stop you fools from speedrunning this game


def loseScreen():
    r = Rect(0, 0, 400, 400, fill='red')
    r.toFront()
    Label('YOU LOSE!', 200, 200, size=60)
def winScreen():
    win = Rect(0, 0, 400, 400, fill='green')
    win.toFront()
    Label('YOU WIN!', 200, 200, size=60)

###WIZARD
def wizard(visiblity):
    leg_for_wizard=Group(
        #Legs
        Oval(85, 295, 8, 80, fill=rgb(231, 190, 162), rotateAngle=8, visible=visiblity),
        Oval(100, 295, 8, 80, fill=rgb(231, 190, 162), rotateAngle=-8, visible=visiblity),
        )
    leg_for_wizard.centerX +=230
    leg_for_wizard.centerY+=50
    
    wizzy=Group(
        Circle(95, 240, 30, fill=rgb(231, 190, 162), visible=visiblity),
        Polygon(65, 230, 65, 253, 71, 269, 95, 285, 113, 270, 120, 256, 124, 249, 125, 242, 129, 228, 116, 228, 112, 253, 95, 250, 77, 253, 73, 225, fill='grey', visible=visiblity),
        Polygon(90, 170, 151, 193, 159, 221, 146, 203, 118, 197, 125, 215, 127, 221, 138, 226, 158, 230, 48, 230, fill=rgb(84, 100, 156), visible=visiblity),
        Oval(80, 240, 5, 10, visible=visiblity),
        Oval(105, 240, 5, 10, visible=visiblity),
        
        #Right Arm w/ Body cs y not
        Oval(110, 310, 16, 20, rotateAngle=-30, fill=rgb(231, 190, 162), visible=visiblity),
        Polygon(81, 276, 77, 315, 75, 334, 108, 334, 106, 276, fill=rgb(84, 100, 156), visible=visiblity),
        Polygon(106, 276, 121, 307, 98, 310, fill=rgb(84, 100, 156), visible=visiblity),
        
        #Left Arm
        Oval(55, 298, 14, 20, rotateAngle=95, fill=rgb(231, 190, 162), visible=visiblity),
        Polygon(81, 276, 70, 295, 55, 290, 52, 305, 75, 304, 87, 297, fill=rgb(84, 100, 156), visible=visiblity),
            )
    wizzy.centerX+=230
    wizzy.centerY+=30
    #Wand
    wand=Group(
        Line(51, 300, 46, 247),
        Star(46, 247, 10, 5, fill='yellow', rotateAngle=-5),
        )
    wand.centerX +=230
    wand.centerY +=50
wizard_w = wizard(True)

###Cage
cage1 = Rect(25, 15, 140, 35, fill='grey')
cage2 = Rect(25, 166, 140, 35, fill='grey')
princessDogTag = Label("Save Her", 95, 32, size=20, font='monospace', bold=True)

bar = Group(
    Rect(40, 48, 10, 120, fill='grey'),
    Rect(60, 48, 10, 120, fill='grey'),
    Rect(80, 48, 10, 120, fill='grey'),
    Rect(100, 48, 10, 120, fill='grey'),
    Rect(120, 48, 10, 120, fill='grey'),
    Rect(140, 48, 10, 120, fill='grey'),
    )

###Princess
def princess(visiblity):
    trappedprincess = Group(
    # Hair
    Polygon(80, 147, 80, 153, 77, 163, 73, 167, 67, 167, 62, 164, 58, 159, 56, 157, 58, 157, 64, 155, 67, 149, 68, 142, 68, 129, 71, 114, 76, 108, 82, 107, 87, 104, 94, 103, 98, 105, 101, 111, 106, 111, 112, 114, 117, 120, 119, 132, 117, 133, 112, 129, 110, 127, 106, 124, 101, 133, 92, 137, fill=rgb(86, 54, 5), visible=visiblity),
    #Face
    Polygon(80, 143, 86, 138, 93, 136, 99, 132, 103, 128, 105, 125, 107, 123, 110, 125, 112, 128, 116, 130, 118, 133, 117, 141, 113, 148, 109, 151.5, 104, 154, 99, 155, 92, 155, 87, 153, 83, 150, 81, 143, fill=rgb(195, 153, 107), visible=visiblity),
    #Neck
    Polygon(101, 152, 101, 166, 97, 166, 96, 152, fill=rgb(195, 153, 107), visible=visiblity),
    #Right Arm
    Polygon(109, 166, 111, 173, 124, 168, 121, 170, 110, 176, 104, 166, fill=rgb(195, 153, 107), visible=visiblity),
    #Left Arm
    Polygon(94, 166, 88, 177, 91, 181, 90, 183, 88, 180, 85, 177, 90, 166, fill=rgb(195, 153, 107), visible=visiblity),
    #Left Leg
    Oval(90, 200, 5, 30, rotateAngle=10, fill=rgb(195, 153, 107), visible=visiblity),
    #Right Leg
    Oval(110, 200, 5, 30, rotateAngle=-10, fill=rgb(195, 153, 107), visible=visiblity),
    #Body w/o arms
    Polygon(102, 161, 105, 160, 108, 161, 109, 163, 109, 164, 109, 166, 108, 168, 106, 168, 105, 168, 104, 171, 106, 175, 111, 181, 115, 184, 116, 185, 117, 187, 118, 188, 119, 191, 120, 192, 122, 198, 122, 203, 79, 203, 79, 199, 80, 193, 82, 187, 85, 183, 89, 179, 94, 176, 95, 175, 95, 167, 92, 167, 93, 169, 89, 168, 89, 164, 90, 161, 92, 159, 98, 162, fill=rgb(132, 87, 166), visible=visiblity),
    )
    return trappedprincess

princess_r = princess(True)
for x in princess_r:
    x.centerY-=50

###Key
key = Group(
    Circle(230, 194, 20, fill='gold'),
    Circle(240, 194, 5, fill='white'),
    Rect(165, 185, 60, 16, fill='gold'),
    Rect(169, 185, 8, 26, fill='gold'),
    Rect(185, 185, 9, 29, fill='gold'),
    Rect(202, 185, 6, 27, fill='gold'),
    )
key.visible=False
key.centerX = 300
key.centerY = 100
###Rock
Polygon(18, 400, 25, 381, 26, 375, 31, 372, 38, 344, 40, 326, 53, 318, 63, 293, 56, 267, 71, 248, 97, 247, 114, 242, 117, 242, 126, 251, 131, 269, 133, 281, 134, 295, 134, 302, 142, 311, 145, 315, 147, 329, 148, 335, 148, 346, 156, 355, 160, 359, 163, 369, 165, 385, 166, 389, 166, 392, 166, 400, fill='grey', border='black', borderWidth=2)
Rect(21, 398, 143, 10, fill='grey') #To cover the bottom black line
###Formatting and Drawing Wizard
bar.toFront()
bar.opacity = 60
wizard(True)
###Timer
def onStep():
    invisble_counter.value+=1

    if invisble_counter.value <5:
        intro1.visible=True
        intro2.visible=True
        intro3.visible=True
    elif invisble_counter.value <6:
        intro1.visible = False
        intro2.visible = False
        intro3.visible = False
        hint.visible=True
        hint.toFront()

    elif invisble_counter.value < 6.000000000001: #tbh got no clue tf I am doing here with the extra zero's. Docs + Colors don't give me enough info. Idek if the zero's doing anything. 
        hint.visible = False
        toStopClickEarly.visible = False
    elif invisble_counter.value == 20 and toStopLoseTrigger.visible == True:#and some other variable that triggers when you win is visible = false #why true? Because it starts off true
        loseScreen()
        princess_r.visible=False
###Locking System
key_storage = RegularPolygon(95, 345, 30, 5, fill='yellow')
cage1.clicks = 0 #Custom Property to track the numbers of click 
safety_box = Rect(60, 48, 70, 120, fill=None)
def onMousePress(mouseX, mouseY):
    if toStopClickEarly.visible == False:
        cage1.clicks +=1
        if key_storage.contains(mouseX, mouseY):
            key_storage.rotateAngle +=10
            if cage1.clicks == hint.value:  
                key.visible=True
            if cage1.clicks > hint.value:
                loseScreen()
        
def onMouseDrag (mouseX, mouseY):
    if key.hits(mouseX, mouseY):
        key.centerX = mouseX
        key.centerY = mouseY
    if safety_box.hitsShape(key) == True:
        key.visible=False
        cage1.visible = False
        bar.visible = False
        princessDogTag.visible = False
def onMouseMove(mouseX, mouseY):
    if princess_r.hits(mouseX, mouseY) and cage1.visible == False: 
        princess_r.centerX = mouseX
        princess_r.centerY = mouseY
        princess_r.toFront()
        if princess_r.hitsShape(cage2) == True:
            loseScreen()
    if princess_r.centerX > 300 and princess_r.centerY > 280 :
        toStopLoseTrigger.visible = False #why false? Because it starts off true
        winScreen()
        princess_r.visible = False
    
    
    
    
if __name__ == "__main__":
    cmu_graphics.run()
    




    
