from cmu_graphics import *

##### THE FALLEN CASTLE :'(
#####Click WASD to move the Wizard 
#####Left-click to show Wizard's Palace after a long war 
#####Lef-Click to reset Wizards Position

    ###Drawing The Background###
Rect(0, 0, 400, 75, fill='dodgerBlue')
Rect(0, 75, 400, 250, fill=gradient('dodgerBlue', 'deepSkyBlue', start='top'))
Circle(80, 475, 200, fill=gradient('green', 'forestGreen', start='bottom-left'))
Circle(300, 455, 200, fill=gradient('green', 'forestGreen', start='bottom-left'))


###Sun
Star(0, 0, 200, 20, fill='yellow', opacity=90)
Circle(25, 25, 80, fill=gradient('khaki', 'yellow'), opacity=90)


###Adding Cloud###
a=Group(
    Circle(48, 85, 30, fill='lavender'),
    Circle(75, 95, 30, fill='lavender'),
    Circle(74, 69, 30, fill='lavender'),
    Circle(110, 60, 30, fill='lavender'),
    Circle(110, 60, 30, fill='lavender'),
    Circle(135, 80, 30, fill='lavender'),
    Circle(110, 95, 30, fill='lavender'),
    )

a.centerX-=15
a.centerY+=18

b=Group(
    Circle(48, 85, 30, fill='lavender'),
    Circle(75, 95, 30, fill='lavender'),
    Circle(74, 69, 30, fill='lavender'),
    Circle(110, 60, 30, fill='lavender'),
    Circle(110, 60, 30, fill='lavender'),
    Circle(135, 80, 30, fill='lavender'),
    Circle(110, 95, 30, fill='lavender'),
    )
    
b.centerX+=147
b.centerY-=15


c=Group(
Circle(220, 70, 30, fill='lavender'),
Circle(247, 80, 30, fill='lavender'),
Circle(246, 54, 30, fill='lavender'),
Circle(282, 60, 30, fill='lavender'),
Circle(282, 45, 30, fill='lavender'),
Circle(307, 65, 30, fill='lavender'),
Circle(282, 80, 30, fill='lavender'),
    )

c.centerX+=150
c.centerY+=10


###Tower###
d=Group(
    Polygon(370, 325, 380, 300, 345, 265, 345, 190, 270, 285, 260, 325),
    Rect(300, 150, 50, 175),
    )
# d.fill=gradient('darkSlateBlue', 'mediumPurple', start='bottom')
d.fill=rgb(84, 100, 156)


Oval(325, 150, 130, 80, fill=rgb(84, 100, 156))
Rect(240, 135, 160, 25, fill=rgb(22, 158, 255))

e=Group(

Rect(280, 130, 10, 30),
Rect(300, 130, 10, 30),
Rect(320, 130, 10, 30),
Rect(340, 130, 10, 30),
Rect(360, 130, 10, 30),
    )

e.fill=rgb(84, 100, 156)
# e.fill=gradient(rgb(123, 95, 191), rgb(133, 102, 202), start='bottom')

###WIZARD

leg_for_wizard=Group(
    #Legs
    Oval(85, 295, 8, 80, fill=rgb(231, 190, 162), rotateAngle=8),
    Oval(100, 295, 8, 80, fill=rgb(231, 190, 162), rotateAngle=-8),
    )

wizzy=Group(
    Circle(95, 240, 30, fill=rgb(231, 190, 162)),
    Polygon(65, 230, 65, 253, 71, 269, 95, 285, 113, 270, 120, 256, 124, 249, 125, 242, 129, 228, 116, 228, 112, 253, 95, 250, 77, 253, 73, 225, fill='grey'),
    Polygon(90, 170, 151, 193, 159, 221, 146, 203, 118, 197, 125, 215, 127, 221, 138, 226, 158, 230, 48, 230, fill=rgb(84, 100, 156)),
    Oval(80, 240, 5, 10),
    Oval(105, 240, 5, 10),
    
    #Right Arm w/ Body cs y not
    Oval(110, 310, 16, 20, rotateAngle=-30, fill=rgb(231, 190, 162)),
    Polygon(81, 276, 77, 315, 75, 334, 108, 334, 106, 276, fill=rgb(84, 100, 156)),
    Polygon(106, 276, 121, 307, 98, 310, fill=rgb(84, 100, 156)),
    
    #Left Arm
    Oval(55, 298, 14, 20, rotateAngle=95, fill=rgb(231, 190, 162)),
    Polygon(81, 276, 70, 295, 55, 290, 52, 305, 75, 304, 87, 297, fill=rgb(84, 100, 156)),
        )

wizzy.centerY-=20

#Wand
wand=Group(
    Line(51, 300, 46, 247),
    Star(46, 247, 10, 5, fill='yellow', rotateAngle=-5),
    )

#####Wizard's Movement 

def onKeyPress(key):
    if (key == 'a'):
        wizzy.centerX-=10
        wand.centerX-=10
        leg_for_wizard.centerX-=10
    elif(key == 'd'):
        wizzy.centerX+=10
        wand.centerX+=10
        leg_for_wizard.centerX+=10
    elif(key == 'w'):
        wizzy.centerY-=10
        wand.centerY-=10
        leg_for_wizard.centerY-=10
    elif(key == 's'):
        wizzy.centerY+=10
        wand.centerY+=10
        leg_for_wizard.centerY+=10
        
        
    
# Label(leg_for_wizard.centerY, 200, 200)
#####NIGHT SIDE

    ###Drawing The Background###

i=Group(
    Rect(0, 0, 400, 75, fill='fireBrick'),
    Rect(0, 75, 400, 250, fill=gradient('fireBrick', 'darkRed', start='top')),
    Circle(80, 475, 200, fill='darkSlateBlue'),
    Circle(300, 455, 200, fill='darkSlateBlue'),
    Circle(250, 120, 30, fill='gray', opacity=30),
    Circle(262, 42, 40, fill='gray', opacity=10),
    )

###Adding Cloud###
f=Group(
    Circle(48, 85, 30, fill='black'),
    Circle(75, 95, 30, fill='black'),
    Circle(74, 69, 30, fill='black'),
    Circle(110, 60, 30, fill='black'),
    Circle(110, 60, 30, fill='black'),
    Circle(135, 80, 30, fill='black'),
    Circle(110, 95, 30, fill='black'),
    )

f.centerX-=15
f.centerY+=18


g=Group(
    Circle(48, 85, 30, fill='black'),
    Circle(75, 95, 30, fill='black'),
    Circle(74, 69, 30, fill='black'),
    Circle(110, 60, 30, fill='black'),
    Circle(110, 60, 30, fill='black'),
    Circle(135, 80, 30, fill='black'),
    Circle(110, 95, 30, fill='black'),
    )
    
g.centerX+=147
g.centerY-=15

h=Group(
Circle(220, 70, 30, fill='black'),
Circle(247, 80, 30, fill='black'),
Circle(246, 54, 30, fill='black'),
Circle(282, 60, 30, fill='black'),
Circle(282, 45, 30, fill='black'),
Circle(307, 65, 30, fill='black'),
Circle(282, 80, 30, fill='black'),
    )

h.centerX+=150
h.centerY+=10


###Tower###
j=Group(
    Polygon(260, 325, 370, 325, 380, 300, 345, 265, 345, 190, 325, 200, 300, 165, 299, 246, 270, 285),
     )

l=Group(
    Polygon(200, 200, 225, 185, 245, 225, 240, 280, 200, 280, rotateAngle=57),
    )

l.centerX-=60
l.centerY+=50

k=Group(
    
    Oval(325, 150, 130, 80, fill='black'),
    Rect(240, 135, 160, 25, fill='darkSlateBlue'),
    Rect(280, 130, 10, 30, fill='black'),
    Rect(300, 130, 10, 30, fill='black'),
    Rect(320, 130, 10, 30, fill='black'),
    Rect(340, 130, 10, 30, fill='black'),
    Rect(360, 130, 10, 30, fill='black'),
    )

k.centerX-=225
k.centerY+=180
k.rotateAngle=240

m=Group(
    Oval(58, 256.5, 48.5, 37, rotateAngle=330, fill=rgb(151, 10, 10)),
    Oval(93, 251, 50, 37, rotateAngle=10, fill=rgb(151, 10, 10)),
    Oval(70, 254, 50, 37, fill=rgb(151, 10, 10)),
    Circle(215, 250, 5, fill='gray', opacity=90),
    Circle(230, 225, 10, fill='gray', opacity=70),
    Circle(240, 180, 20, fill='gray', opacity=50),
    )

###TombStone
n=Group(
    Circle(260, 295, 30, fill='grey', visible=True),
    Polygon(230, 365, 290, 365, 290, 320, 283, 312, 290, 305, 290, 290, 230, 290, 230, 305, 230, 330, 238, 340, 230, 350, fill='grey'),
    Label('R. I. P.', 260, 305),
    Label('1931-2000', 260, 353, size=11),
    Line(240, 272, 250, 279, opacity=70),
    Line(250, 279, 263, 278, opacity=70),
    Line(250, 279, 246, 283, opacity=70),
    Line(246, 283, 239, 284, opacity=70),
    Line(258, 278, 258, 271, opacity=70),
    Line(258, 271, 262, 270, opacity=70),
    Line(263, 278, 270, 285, opacity=70),
    )

n.centerX+=5
n.centerY-=20

###Left-Click Visible
f.visible=False
g.visible=False
h.visible=False
i.visible=False
j.visible=False
k.visible=False
l.visible=False
m.visible=False
n.visible=False

def onMousePress(mouseX, mouseY):
    f.visible=True
    g.visible=True
    h.visible=True
    i.visible=True
    j.visible=True
    k.visible=True
    l.visible=True
    m.visible=True
    n.visible=True
    
def onMouseRelease(mouseX, mouseY):
    f.visible=False
    g.visible=False
    h.visible=False
    i.visible=False
    j.visible=False
    k.visible=False
    l.visible=False
    m.visible=False
    n.visible=False
    
    wizzy.centerX=102
    wand.centerX=45.73
    leg_for_wizard.centerX=92.5
    wizzy.centerY=232
    wand.centerY=269
    leg_for_wizard.centerY=295
    

#Then on mouse release reset everything back to normal


 
if __name__ == "__main__":
    cmu_graphics.run()



    
