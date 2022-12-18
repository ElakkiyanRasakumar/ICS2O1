from cmu_graphics import *

# Fill me in!
import time
import datetime
app.stepsPerSecond = 30 # When sumbiting set to 30
app.setMaxShapeCount(10000000000000)
#init Music
bg_music = Sound("https://cdn.discordapp.com/attachments/954600117049098240/978859941433577582/Pokemon_Black_and_White_Music__Nimbasa_City_Music.mp3")
bg_music.play()
battle = Sound("https://cdn.discordapp.com/attachments/954600117049098240/978857136090124288/Pokemon_Black__White_-_Trainer_Battle_Music_HQ.mp3")
app.unleashPikachu = False
app.battle_phase = False
app.csacademyhastheworstcodeinthewholeentireworld = Rect(290, 305, 110, 95, fill=None)
#init Group and Variables 
Menu = Group()
pikachu = Group()
charmander = Group()
blocks = Group()
b_grass_patch = Group()
t_grass_patch = Group()
b_level = Group()
t_level = Group()
b_hp = Group()
t_hp = Group()
Red = Group()
Blue = Group()
Green = Group()
Yellow = Group()
pointer = Group()
Catcher = Group()
charmander.hp = 100
pointer.dx = 15
app.px = 0
app.dx2 = 0
app.catch = False
app.turnOff= True
app.catch_phase = True
app.start_time = time.time()
app.secondcurve = False
app.frickoff = False
app.frickoff2 = False
app.rotation1 = True
app.rotation2 = False
app.rotation3 = False
app.final_rotation = False
app.gamefreak_logo = Label("G A M E F R E A K", 200, 200, fill="white", size=60, bold = True, font = "monospace", visible = False)
app.star = Star(45, 45, 30, 5, fill="white", visible = False)
app.rect = Rect(0, 0, 400, 400, fill='black')
app.vicstar1 = Star(312, 135, 10, 5, visible = False, opacity = 50, fill="yellow")
app.vicstar2 = Star(312, 135, 10, 5, visible = False, opacity = 50, fill="yellow")
app.vicstar3 = Star(312, 135, 10, 5, visible = False, opacity = 50, fill="yellow")

def main():
    create_ground()
    draw_sprite()
    draw_charmander()
    
def create_ground():
    i=0
    color = "green"
    for x in range(0, 401, 15):
        for y in range(0, 401, 15):
            blocks.add(Rect(x, y, 15, 15, fill=color))
            i +=1
            if i % 2 == 0:
                color = "green"
            else:
                color = "lightGreen"
def draw_sprite():
        pikachu.add(
        #Y Level 0
        Rect(20, 0, 10, 10),
        Rect(120, 0, 10, 10),
        Rect(130, 0, 10, 10),
        #Y Level 10
        Rect(10, 10, 10, 10),
        Rect(20, 10, 10, 10, fill="yellow"),
        Rect(30, 10, 10, 10),
        Rect(120, 10, 10, 10),
        Rect(130, 10, 10, 10),
        Rect(140, 10, 10, 10),
        #Y Level 20
        Rect(0, 20, 10, 10),
        Rect(10, 20, 10, 10, fill="yellow"),
        Rect(20, 20, 10, 10, fill="yellow"),
        Rect(30, 20, 10, 10, fill="yellow"),
        Rect(40, 20, 10, 10),
        Rect(120, 20, 10, 10),
        Rect(130, 20, 10, 10, fill="yellow"),
        Rect(140, 20, 10, 10, fill="black"),
        #Y Level 30
        Rect(0, 30, 10, 10),
        Rect(10, 30, 10, 10, fill="yellow"),
        Rect(20, 30, 10, 10, fill="yellow"),
        Rect(30, 30, 10, 10, fill="yellow"),
        Rect(40, 30, 10, 10, fill="yellow"),
        Rect(50, 30, 10, 10),
        Rect(60, 30, 10, 10),
        Rect(70, 30, 10, 10),
        Rect(120, 30, 10, 10),
        Rect(130, 30, 10, 10, fill="yellow"),
        Rect(140, 30, 10, 10, fill="yellow"),
        Rect(150, 30, 10, 10),
        #Y Level 40
        Rect(10, 40, 10, 10),
        Rect(20, 40, 10, 10, fill="yellow"),
        Rect(30, 40, 10, 10, fill="yellow"),
        Rect(40, 40, 10, 10, fill="yellow"),
        Rect(50, 40, 10, 10),
        Rect(60, 40, 10, 10),
        Rect(70, 40, 10, 10),
        Rect(80, 40, 10, 10),
        Rect(90, 40, 10, 10),
        Rect(120, 40, 10, 10),
        Rect(130, 40, 10, 10, fill="yellow"),
        Rect(140, 40, 10, 10, fill="yellow"),
        Rect(150, 40, 10, 10),
        #Y Level 50
        Rect(20, 50, 10, 10, fill="black"),
        Rect(30, 50, 10, 10, fill="yellow"),
        Rect(40, 50, 10, 10, fill="yellow"),
        Rect(50, 50, 10, 10, fill="yellow"),
        Rect(60, 50, 10, 10),
        Rect(70, 50, 10, 10),
        Rect(80, 50, 10, 10, fill="yellow"),
        Rect(90, 50, 10, 10, fill="yellow"),
        Rect(100, 50, 10, 10),
        Rect(110, 50, 10, 10),
        Rect(120, 50, 10, 10, fill="yellow"),
        Rect(130, 50, 10, 10, fill="yellow"),
        Rect(140, 50, 10, 10, fill="yellow"),
        Rect(150, 50, 10, 10, fill="yellow"),
        Rect(160, 50, 10, 10),
        # Y Level 60
        Rect(30, 60, 10, 10),
        Rect(40, 60, 10, 10, fill="yellow"),
        Rect(50, 60, 10, 10, fill="yellow"),
        Rect(60, 60, 10, 10),
        Rect(70, 60, 10, 10),
        Rect(80, 60, 10, 10, fill="yellow"),
        Rect(90, 60, 10, 10, fill="yellow"),
        Rect(100, 60, 10, 10, fill="yellow"),
        Rect(110, 60, 10, 10, fill="yellow"),
        Rect(120, 60, 10, 10, fill="yellow"),
        Rect(130, 60, 10, 10, fill="yellow"),
        Rect(140, 60, 10, 10, fill="yellow"),
        Rect(150, 60, 10, 10, fill="yellow"),
        Rect(160, 60, 10, 10, fill="yellow"),
        Rect(170, 60, 10, 10),
        # Y Level 70
        Rect(20, 70, 10, 10),
        Rect(30, 70, 10, 10, fill="yellow"),
        Rect(40, 70, 10, 10, fill="yellow"),
        Rect(50, 70, 10, 10),
        Rect(70, 70, 10, 10),
        Rect(80, 70, 10, 10, fill="yellow"),
        Rect(90, 70, 10, 10, fill="yellow"),
        Rect(100, 70, 10, 10, fill="yellow"),
        Rect(110, 70, 10, 10, fill="yellow"),
        Rect(120, 70, 10, 10, fill="yellow"),
        Rect(130, 70, 10, 10, fill="yellow"),
        Rect(140, 70, 10, 10, fill="yellow"),
        Rect(150, 70, 10, 10, fill="yellow"),
        Rect(160, 70, 10, 10, fill="yellow"),
        Rect(170, 70, 10, 10, fill='white'),
        Rect(180, 70, 10, 10),
        # Y Level 80
        Rect(20, 80, 10, 10),
        Rect(30, 80, 10, 10, fill="yellow"),
        Rect(40, 80, 10, 10),
        Rect(70, 80, 10, 10),
        Rect(80, 80, 10, 10, fill="yellow"),
        Rect(90, 80, 10, 10, fill="yellow"),
        Rect(100, 80, 10, 10, fill="yellow"),
        Rect(110, 80, 10, 10, fill="yellow"),
        Rect(120, 80, 10, 10, fill="yellow"),
        Rect(130, 80, 10, 10, fill="yellow"),
        Rect(140, 80, 10, 10, fill="yellow"),
        Rect(150, 80, 10, 10, fill="yellow"),
        Rect(160, 80, 10, 10, fill="yellow"),
        Rect(170, 80, 10, 10, fill='black'),
        Rect(180, 80, 10, 10),
        # Y Level 90
        Rect(30, 90, 10, 10),
        Rect(40, 90, 10, 10, fill="yellow"),
        Rect(50, 90, 10, 10),
        Rect(60, 90, 10, 10),
        Rect(70, 90, 10, 10, fill="yellow"),
        Rect(80, 90, 10, 10, fill="yellow"),
        Rect(90, 90, 10, 10, fill="yellow"),
        Rect(100, 90, 10, 10, fill="yellow"),
        Rect(110, 90, 10, 10, fill="yellow"),
        Rect(120, 90, 10, 10, fill="black"),
        Rect(130, 90, 10, 10, fill="white"),
        Rect(140, 90, 10, 10, fill="yellow"),
        Rect(150, 90, 10, 10, fill="yellow"),
        Rect(160, 90, 10, 10, fill="yellow"),
        Rect(170, 90, 10, 10, fill="yellow"),
        Rect(180, 90, 10, 10),
        # Y Level 100
        Rect(40, 100, 10, 10),
        Rect(50, 100, 10, 10),
        Rect(60, 100, 10, 10),
        Rect(70, 100, 10, 10, fill="yellow"),
        Rect(80, 100, 10, 10, fill="yellow"),
        Rect(90, 100, 10, 10, fill="yellow"),
        Rect(100, 100, 10, 10, fill="red"),
        Rect(110, 100, 10, 10, fill="red"),
        Rect(120, 100, 10, 10),
        Rect(130, 100, 10, 10),
        Rect(140, 100, 10, 10, fill="yellow"),
        Rect(150, 100, 10, 10, fill="yellow"),
        Rect(160, 100, 10, 10, fill="yellow"),
        Rect(170, 100, 10, 10),
        # Y Level 110
        Rect(50, 110, 10, 10),
        Rect(60, 110, 10, 10),
        Rect(70, 110, 10, 10),
        Rect(80, 110, 10, 10, fill="yellow"),
        Rect(90, 110, 10, 10, fill="yellow"),
        Rect(100, 110, 10, 10, fill="yellow"),
        Rect(110, 110, 10, 10, fill="red"),
        Rect(120, 110, 10, 10, fill="yellow"),
        Rect(130, 110, 10, 10, fill="yellow"),
        Rect(140, 110, 10, 10, fill="yellow"),
        Rect(150, 110, 10, 10, fill="yellow"),
        Rect(160, 110, 10, 10),
        # Y Level 120
        Rect(50, 120, 10, 10),
        Rect(60, 120, 10, 10, fill="yellow"),
        Rect(70, 120, 10, 10, fill="yellow"),
        Rect(80, 120, 10, 10, fill="yellow"),
        Rect(90, 120, 10, 10, fill="yellow"),
        Rect(100, 120, 10, 10, fill="yellow"),
        Rect(110, 120, 10, 10, fill="yellow"),
        Rect(120, 120, 10, 10, fill="yellow"),
        Rect(130, 120, 10, 10, fill="yellow"),
        Rect(140, 120, 10, 10, fill="yellow"),
        Rect(150, 120, 10, 10, fill="yellow"),
        Rect(160, 120, 10, 10, fill="yellow"),
        Rect(170, 120, 10, 10),
        # Y Level 130
        Rect(50, 130, 10, 10),
        Rect(60, 130, 10, 10),
        Rect(70, 130, 10, 10, fill="yellow"),
        Rect(80, 130, 10, 10, fill="yellow"),
        Rect(90, 130, 10, 10),
        Rect(100, 130, 10, 10, fill="yellow"),
        Rect(110, 130, 10, 10, fill="yellow"),
        Rect(120, 130, 10, 10, fill="yellow"),
        Rect(130, 130, 10, 10, fill="yellow"),
        Rect(140, 130, 10, 10, fill="yellow"),
        Rect(150, 130, 10, 10),
        Rect(160, 130, 10, 10),
        # Y Level 140
        Rect(50, 140, 10, 10),
        Rect(60, 140, 10, 10, fill="yellow"),
        Rect(70, 140, 10, 10, fill="yellow"),
        Rect(80, 140, 10, 10, fill="yellow"),
        Rect(90, 140, 10, 10, fill="yellow"),
        Rect(100, 140, 10, 10),
        Rect(110, 140, 10, 10, fill="yellow"),
        Rect(120, 140, 10, 10, fill="yellow"),
        Rect(130, 140, 10, 10, fill="yellow"),
        Rect(140, 140, 10, 10, fill="yellow"),
        Rect(150, 140, 10, 10),
        # Y Level 150
        Rect(50, 150, 10, 10),
        Rect(60, 150, 10, 10, fill="yellow"),
        Rect(70, 150, 10, 10, fill="yellow"),
        Rect(80, 150, 10, 10, fill="yellow"),
        Rect(90, 150, 10, 10),
        Rect(100, 150, 10, 10, fill="yellow"),
        Rect(110, 150, 10, 10, fill="yellow"),
        Rect(120, 150, 10, 10, fill="yellow"),
        Rect(130, 150, 10, 10, fill="yellow"),
        Rect(140, 150, 10, 10),
        Rect(150, 150, 10, 10, fill="yellow"),
        Rect(160, 150, 10, 10),
        # Y Level 160
        Rect(60, 160, 10, 10),
        Rect(70, 160, 10, 10, fill="yellow"),
        Rect(80, 160, 10, 10, fill="yellow"),
        Rect(90, 160, 10, 10, fill="yellow"),
        Rect(100, 160, 10, 10, fill="yellow"),
        Rect(110, 160, 10, 10, fill="yellow"),
        Rect(120, 160, 10, 10),
        Rect(130, 160, 10, 10),
        Rect(140, 160, 10, 10),
        Rect(150, 160, 10, 10),
        Rect(160, 160, 10, 10),
        # Y Level 170
        Rect(60, 170, 10, 10),
        Rect(70, 170, 10, 10),
        Rect(80, 170, 10, 10, fill="yellow"),
        Rect(90, 170, 10, 10),
        Rect(100, 170, 10, 10),
        Rect(110, 170, 10, 10),
        # Y Level 180
        Rect(60, 180, 10, 10),
        Rect(70, 180, 10, 10, fill="yellow"),
        Rect(80, 180, 10, 10, fill="yellow"),
        Rect(90, 180, 10, 10, fill="yellow"),
        Rect(100, 180, 10, 10),
        # Y Level 190

        Rect(70, 190, 10, 10),
        Rect(80, 190, 10, 10),
        Rect(90, 190, 10, 10),
        )
        
        pikachu.toFront()
        pikachu.width = pikachu.width/2
        pikachu.height = pikachu.height/2
        
        for i in pikachu:
            i.border=i.fill
            i.borderWidth 
        pikachu.centerX = 62.5
        pikachu.centerY = 59
def draw_charmander():
    
    charmander.add(
        # Y Level 280
        Rect(270, 280, 10, 10),
        Rect(280, 280, 10, 10),
        Rect(290, 280, 10, 10),
        Rect(370, 280, 10, 10),
        # Y Level 290
        Rect(260, 290, 10, 10),
        Rect(270, 290, 10, 10, fill="orange"),
        Rect(280, 290, 10, 10, fill="orange"),
        Rect(290, 290, 10, 10, fill="orange"),
        Rect(300, 290, 10, 10),
        Rect(360, 290, 10, 10),
        Rect(370, 290, 10, 10,fill="red"),
        Rect(380, 290, 10, 10),
        # Y Level 300
        Rect(250, 300, 10, 10),
        Rect(260, 300, 10, 10, fill="orange"),
        Rect(270, 300, 10, 10, fill="orange"),
        Rect(280, 300, 10, 10, fill="orange"),
        Rect(290, 300, 10, 10, fill="orange"),
        Rect(300, 300, 10, 10, fill="orange"),
        Rect(310, 300, 10, 10),
        Rect(360, 300, 10, 10),
        Rect(370, 300, 10, 10,fill="red"),
        Rect(380, 300, 10, 10),
        # Y Level 310
        Rect(250, 310, 10, 10),
        Rect(260, 310, 10, 10, fill="orange"),
        Rect(270, 310, 10, 10, fill="orange"),
        Rect(280, 310, 10, 10, fill="orange"),
        Rect(290, 310, 10, 10, fill="orange"),
        Rect(300, 310, 10, 10, fill="orange"),
        Rect(310, 310, 10, 10),
        Rect(350, 310, 10, 10),
        Rect(360, 310, 10, 10, fill="red"),
        Rect(370, 310, 10, 10,fill="yellow"),
        Rect(380, 310, 10, 10, fill="red"),
        Rect(390, 310, 10, 10),
        # Y Level 320
        Rect(240, 320, 10, 10),
        Rect(250, 320, 10, 10, fill="orange"),
        Rect(260, 320, 10, 10, fill="orange"),
        Rect(270, 320, 10, 10, fill="orange"),
        Rect(280, 320, 10, 10, fill="orange"),
        Rect(290, 320, 10, 10, fill="orange"),
        Rect(300, 320, 10, 10, fill="orange"),
        Rect(310, 320, 10, 10, fill="orange"),
        Rect(320, 320, 10, 10),
        Rect(350, 320, 10, 10),
        Rect(360, 320, 10, 10, fill="red"),
        Rect(370, 320, 10, 10,fill="yellow"),
        Rect(380, 320, 10, 10, fill="red"),
        Rect(390, 320, 10, 10),
        # Y Level 320(eyes)
        Rect(280, 320, 10, 10, fill="white"),
        Rect(290, 320, 10, 10),
        # Y Level 330
        Rect(240, 330, 10, 10),
        Rect(250, 330, 10, 10, fill="orange"),
        Rect(260, 330, 10, 10, fill="orange"),
        Rect(270, 330, 10, 10, fill="orange"),
        Rect(280, 330, 10, 10, fill="orange"),
        Rect(290, 330, 10, 10, fill="orange"),
        Rect(300, 330, 10, 10, fill="orange"),
        Rect(310, 330, 10, 10, fill="orange"),
        Rect(320, 330, 10, 10),
        Rect(360, 330, 10, 10),
        Rect(370, 330, 10, 10,fill="yellow"),
        Rect(380, 330, 10, 10),
        # Y Level 330 (eyes)
        Rect(280, 330, 10, 10),
        Rect(290, 330, 10, 10),
        # Y Level 340
        Rect(250, 340, 10, 10),
        Rect(260, 340, 10, 10, fill="orange"),
        Rect(270, 340, 10, 10, fill="orange"),
        Rect(280, 340, 10, 10, fill="orange"),
        Rect(290, 340, 10, 10, fill="orange"),
        Rect(300, 340, 10, 10, fill="orange"),
        Rect(310, 340, 10, 10, fill="orange"),
        Rect(320, 340, 10, 10, fill="orange"),
        Rect(330, 340, 10, 10),
        Rect(360, 340, 10, 10),
        Rect(370, 340, 10, 10,fill="orange"),
        Rect(380, 340, 10, 10),
        # Y Level 350
        Rect(260, 350, 10, 10),
        Rect(270, 350, 10, 10),
        Rect(280, 350, 10, 10),
        Rect(290, 350, 10, 10, fill="orange"),
        Rect(300, 350, 10, 10, fill="orange"),
        Rect(310, 350, 10, 10),
        Rect(320, 350, 10, 10, fill="orange"),
        Rect(330, 350, 10, 10, fill="orange"),
        Rect(340, 350, 10, 10),
        Rect(350, 350, 10, 10),
        Rect(360, 350, 10, 10, fill="orange"),
        Rect(370, 350, 10, 10),
        # Y Level 360
        Rect(280, 360, 10, 10),
        Rect(290, 360, 10, 10, fill="coral"),
        Rect(300, 360, 10, 10),
        Rect(310, 360, 10, 10, fill="orange"),
        Rect(320, 360, 10, 10, fill="orange"),
        Rect(330, 360, 10, 10, fill="orange"),
        Rect(340, 360, 10, 10),
        Rect(350, 360, 10, 10, fill="orange"),
        Rect(360, 360, 10, 10, fill="orange"),
        Rect(370, 360, 10, 10),
        # Y Level 370
        Rect(280, 370, 10, 10),
        Rect(290, 370, 10, 10, fill="coral"),
        Rect(300, 370, 10, 10, fill="coral"),
        Rect(310, 370, 10, 10),
        Rect(320, 370, 10, 10),
        Rect(330, 370, 10, 10, fill="orange"),
        Rect(340, 370, 10, 10, fill="orange"),
        Rect(350, 370, 10, 10),
        Rect(360, 370, 10, 10),
        # Y Level 380
        Rect(270, 380, 10, 10),
        Rect(280, 380, 10, 10, fill="white"),
        Rect(290, 380, 10, 10),
        Rect(300, 380, 10, 10, fill="coral"),
        Rect(310, 380, 10, 10, fill="coral"),
        Rect(320, 380, 10, 10, fill="orange"),
        Rect(330, 380, 10, 10, fill="orange"),
        Rect(340, 380, 10, 10, fill="orange"),
        Rect(350, 380, 10, 10),
        # Y Level 390
        Rect(280, 390, 10, 10),
        Rect(290, 390, 10, 10),
        Rect(300, 390, 10, 10),
        Rect(310, 390, 10, 10),
        Rect(320, 390, 10, 10, fill="orange"),
        Rect(330, 390, 10, 10),
        Rect(340, 390, 10, 10),
        # Y Level 400
        Rect(300, 400, 10, 10),
        Rect(310, 400, 10, 10,fill="white"),
        Rect(320, 400, 10, 10, fill="orange"),
        Rect(330, 400, 10, 10,fill='white'),
        Rect(340, 400, 10, 10),
        # Y Level 410
        Rect(310, 410, 10, 10),
        Rect(320, 410, 10, 10),
        Rect(330, 410, 10, 10),
        )
    charmander.toFront()
    charmander.width = charmander.width/1.5
    charmander.height = charmander.height/1.5
    for i in charmander:
        i.border=i.fill
    charmander.centerX = 337.04

pikachu.visible = False
charmander.visible = False

pokeball = Group(
    Arc(50, 350, 40, 40, 270, 180, fill='red'),
    Arc(50, 350, 40, 40, 90, 180, fill="white"),
    Circle(50, 350, 20, fill=None, border="black"),
    Line(30, 350, 45, 350),
    Line(70, 350, 55, 350),
    Circle(50, 350, 5),
    Circle(50, 350, 2.5, fill="white"),
   )
pokeball.visible = False
charmander_pokeball = Group(
    Arc(50, 350, 40, 40, 270, 180, fill='red'),
    Arc(50, 350, 40, 40, 90, 180, fill="white"),
    Circle(50, 350, 20, fill=None, border="black"),
    Line(30, 350, 45, 350),
    Line(70, 350, 55, 350),
    Circle(50, 350, 5),
    Circle(50, 350, 2.5, fill="white"),
  )
charmander_pokeball.visible = False
charmander_pokeball.centerX = 0
charmander_pokeball.centerY = 175
def top_battle_screen():
    #top level 
    #Hp bar

    t_level.add(
        Polygon(-10, 40, 160, 40, 190, 100, -10, 100, fill=rgb(224, 224, 224), borderWidth=2, border=rgb(72, 72, 72)),
        Label("Charmander   Lv.17", 73, 52, size=14, font="montserrat", bold=True),
        Rect(15, 68, 33, 20),
        Rect(15, 68, 139, 20, border="black", fill=None, borderWidth=6),
        Label("HP", 34, 77, size=14, font="montserrat", bold=True, fill="yellow"),
        )
    t_level.right=0 

    #Grass Patch
    t_grass_patch.add(
        Oval(315, 150, 260, 80, fill=rgb(96, 208, 128), rotateAngle=1, border=rgb(224, 192, 96), borderWidth=5),
        Oval(312, 150, 260/1.5, 80/1.5, fill=rgb(72, 184, 104), rotateAngle=1),
        )
t_hp.add(
    Rect(48, 74, 100, 8, fill='green'),
    )
t_hp.right = 0
t_hp.visible = False
def bottom_battle_screen():
    #bottom level
    b_level.add(
        Polygon(410, 213, 240, 213, 210, 273, 410, 273, fill=rgb(224, 224, 224), borderWidth=2, border=rgb(72, 72, 72)),
        Label("Pikachu   Lv.15", 325, 223, size=14, font="montserrat", bold=True),
        Rect(245, 240, 33, 20),
        Rect(245, 240, 139, 20, border="black", fill=None, borderWidth=6),
        Label("HP", 264, 249, size=14, font="montserrat", bold=True, fill="yellow"),
        )
    b_level.left = 400
    b_hp.add(
        Rect(0, 246, 100, 8, fill="green")
        )
    b_hp.left = 400
    #Grass Patch
    b_grass_patch.add(
        Oval(90, 320, 260, 100, rotateAngle = 3, fill=rgb(96, 208, 128),border=rgb(224, 192, 96), borderWidth=5),
        Oval(90, 320, 260/1.5, 100/1.5, fill=rgb(72, 184, 104), rotateAngle=3), 
        )


def atk_menu():
        Rect(0, 325, 400, 75,border="grey", borderWidth=4, fill=gradient(rgb(128, 216, 128), rgb(232, 248, 208), rgb(128, 216, 128), start="top")),
        Rect(8, 333, 190, 59, border=rgb(72, 72, 72), fill=rgb(248, 216, 104), borderWidth=2),
        Rect(12, 337, 182, 51, fill=rgb(248, 248, 248), border=rgb(96, 96, 104), borderWidth=3),
        Label("Pick a Move", 103, 362.5, fill="black", font="orbitron", size=20, bold=True)
        Red.add(Rect(202, 333, 93, 29.5, fill=gradient(rgb(197, 67, 67), rgb(197, 67, 67), rgb(120, 25, 25), start="top"))),
        Red.toFront(),
        Label("Tackle", 248, 348, fill="white", font="orbitron", size=16, bold=True),
        Yellow.add(Rect(299, 333, 93, 29.5, fill=gradient(rgb(224, 152, 40), rgb(224, 152, 40), rgb(136, 104, 56), start="top"))),
        Yellow.toFront(),
        Label("Thunderbolt", 345.5, 348, fill="white", font="orbitron", size=12, bold=True)
        Green.add(Rect(202, 365.5, 93, 26.5, fill=gradient(rgb(88, 176, 40), rgb(88, 176, 40), rgb(80, 112, 64), start="top"))),
        Green.toFront(),
        Label("Thunder", 248.5, 379, fill="white", font="orbitron", size=16, bold=True),
        Blue.add(Rect(299, 365.5, 93, 26.5, fill=gradient(rgb(40, 144, 200), rgb(40, 144, 200), rgb(64, 88, 112), start="top"))),
        Blue.toFront(),
        Label("Catch", 346, 379, fill="white", font="orbitron", size=16, bold=True)
        
Clock = Label(0, 200, 200, visible = False)
copyright_info = Group(
    Label("© 2010 Pokémon", 200, 155, fill="white", size = 14),
    Label("© 1995-2010 Nintendo", 200, 180, fill="white", size=14),
    Label("© 1995-2010 Creatures inc.", 200, 205, fill="white", size=14),
    Label("© 1995-2010 GAME FREAK inc.", 200, 230, fill="white", size=14),
    )
def catching_system():
    catcher_range_X = randrange(25, 341)
    catcher_range_width = randrange(5, 36)
    Rect(0, 325, 400, 75,border="grey", borderWidth=4, fill=gradient(rgb(128, 216, 128), rgb(232, 248, 208), rgb(128, 216, 128), start="top")),
    Rect(25, 340, 350, 45, fill="silver", border="black", borderWidth=4)
    Catcher.add(Rect(catcher_range_X, 344, catcher_range_width, 37, fill="red"))
    pointer.add(RegularPolygon(40, 341, 15, 3, rotateAngle=180, border="black", fill="green", borderWidth=1))
    pointer.toFront()

bg = Group(
    Rect(0, 0, 400, 35, fill=rgb(80, 232, 210)),
    Polygon(180, 4, 200, 29, 400, 29, 400, 4, fill=rgb(64, 224, 200)),
    Rect(0, 35, 400, 25, fill=rgb(90, 235, 212)),
    Rect(0, 60, 400, 10, fill=rgb(64, 224, 200)),
    Rect(0, 70, 400, 50, fill=rgb(165, 235, 230)),
    Rect(0, 85, 400, 20, fill=rgb(160, 240, 224)),
    Rect(0, 120, 400, 40, fill=rgb(128, 232, 208)),
    Rect(0, 160, 400, 50, fill=rgb(56, 208, 112)),
    Polygon(175, 170, 205, 200, 400, 200, 400, 170, fill=rgb(48, 195, 112)),
    Rect(0, 210, 400, 190, fill=rgb(200, 248, 129)),
    Rect(0, 0, 400, 400, fill="white", opacity = 50),
    )
bg.visible=False
main()
def onKeyHold(keys):
    if not app.battle_phase and app.frickoff:
        if "up" in keys:
            pikachu.centerY -= 5
        if "down" in keys:
            pikachu.centerY += 5
        if "left" in keys:
            pikachu.centerX -= 5
        if "right" in keys:
            pikachu.centerX += 5
        if pikachu.left <= 0:
            pikachu.left = 0
        if pikachu.right >= 400:
            pikachu.right = 400
        if pikachu.top <= 0:
            pikachu.top = 0
        if pikachu.bottom >= 400:
            pikachu.bottom = 400
    if app.turnOff and pikachu.hitsShape(app.csacademyhastheworstcodeinthewholeentireworld):
        bg.visible=True
        bg.toBack()
        app.turnOff = False
        app.battle_phase = True
        blocks.visible = False
        pikachu.visible = False
        charmander.visible = False
        bottom_battle_screen()
        top_battle_screen()
        t_hp.visible = True
        atk_menu()
        charmander.centerX = 308
        charmander.centerY = 119
        charmander.visible = True
        charmander.toFront()
        
def onKeyPress(key):
    if key == "space":
        if pointer.hitsShape(Catcher):
            pointer.dx = 0
            pokeball.centerX = 0
            pokeball.centerY = 175
            pointer.visible = False
            Catcher.visible = False
            app.catch = True
            #draw pokeball follwing parabolic path on the onStep. (check onStep)

def onMousePress(x,y):
    r_power = 2
    random_thunder = randrange(0, 101)   
    random_thunderbolt = randrange(0, 101)
    if t_hp.visible and b_hp.visible and pikachu.visible and app.catch==False:
        if Red.hits(x,y):
            if (b_hp.width-r_power/4) < 0:
                b_hp.visible = False
                pikachu.visible = False
            else:
                b_hp.width -= (r_power/4)
            if b_hp.width <= 45:
                b_hp.fill="yellow"
            if b_hp.width <= 22:
                b_hp.fill="red"
            if (charmander.hp-r_power) < 0:
                t_hp.visible = False
                charmander.visible = False
                b_hp.left = 273
            else:
                charmander.hp -= 2
                t_hp.width -= r_power
                t_hp.left = 48
                b_hp.left = 273
                b_hp.width -= (r_power/4)
                if t_hp.width <= 45:
                    t_hp.fill="yellow"
                if t_hp.width <= 22:
                    t_hp.fill="red"
                if b_hp.width <= 45:
                    b_hp.fill="yellow"
                if b_hp.width <= 22:
                    b_hp.fill="red"
        if Green.hits(x,y) and t_hp.visible and pikachu.visible:
            g_power = 50
            if (b_hp.width-g_power/10) < 0:
                b_hp.visible = False
                pikachu.visible = False
            else: 
                b_hp.width -= (g_power/10)
                b_hp.left = 273
            if b_hp.width <= 45:
                b_hp.fill="yellow"
            if b_hp.width <= 22:
                b_hp.fill="red"
            if random_thunder % 10 ==0:
                if (charmander.hp-g_power) <= 0:
                    t_hp.visible = False
                    charmander.visible = False
                else:
                    charmander.hp -= 50
                    t_hp.width -= g_power
                    t_hp.left = 48
                    if t_hp.width <= 50:
                        t_hp.fill="yellow"
                    if t_hp.width <= 25:
                        t_hp.fill="red"
                    if b_hp.width <= 45:
                        b_hp.fill="yellow"
                    if b_hp.width <= 22:
                        b_hp.fill="red"
            else:
                print("You Missed")
    
        if Yellow.hits(x,y) and t_hp.visible and pikachu.visible:
            y_power = 10
            if (b_hp.width-y_power) <= 0:
                b_hp.visible = False
                pikachu.visible = False
            else:
                b_hp.width -= (y_power/4)
                b_hp.left = 273
            if b_hp.width <= 45:
                b_hp.fill="yellow"
            if b_hp.width <= 22:
                b_hp.fill="red"
            if random_thunder % 2 ==0:
                charmander.hp -= 10
                if (charmander.hp-y_power) < 0:
                    t_hp.visible = False
                    charmander.visible = False
                else:
                    t_hp.width -= y_power
                    t_hp.left = 48
                    b_hp.width -= (y_power/4)
                    b_hp.left = 273
                    if b_hp.width <= 45:
                        b_hp.fill="yellow"
                    if b_hp.width <= 22:
                        b_hp.fill="red"
                    if t_hp.width <= 45:
                        t_hp.fill="yellow"
                    if t_hp.width <= 22:
                        t_hp.fill="red"
            else:
                print("You Missed")
        if Blue.hits(x,y) and t_hp.visible and pikachu.visible and t_hp.fill == "red" and app.catch_phase:
            catching_system()
            app.catch_phase = False
def onStep():
    #Time (Thanks theodore, for helping me with the timedelta part(that shit was annoying asf))
    final_time = time.time() - app.start_time
    final_time = str(datetime.timedelta(seconds=final_time)).split(".")[0].split(":")[2]
    Clock.value = int(final_time)
    #####Animation for intro
    if Clock.value == 4 and not app.secondcurve: # orginal value is 3
        copyright_info.visible= False
        app.gamefreak_logo.visible = True
    if Clock.value >= 4 and app.gamefreak_logo.size >= 30: # orgonal value is 3
        app.gamefreak_logo.size -= 0.5
    if app.star.right <= 400 and not app.secondcurve:
        if app.gamefreak_logo.size <= 29.5:
            app.star.visible = True
            if app.star.radius >= 1:
                app.star.radius -= 0.05
                app.star.rotateAngle += 5
                if app.star.right <= 400:
                    app.star.centerX += 2 # Orginal Value 1
                    app.star.centerY = 7/25205*(app.star.centerX-45)**2+45 # Vertex Form
                    if app.star.right >= 400:
                        app.secondcurve = True
    if app.secondcurve and not app.frickoff:
        if not app.star.centerX<=269 and not app.star.centerY >=182:
            app.star.rotateAngle -= 1
            app.star.centerX -= 1
            app.star.centerY = 415/59536*(app.star.centerX-391)**2+78.25 # Vertex Form
            app.star.radius += 0.05
            app.star.rotateAngle -= 5
        else:
            app.star.radius += 5
            app.star.rotateAngle += 5
            if app.star.radius >= 899:
                #remove everything and make pickchu and charmander visible
                app.star.visible = False
                app.gamefreak_logo.visible = False
                pikachu.visible = True
                app.rect.visible = False
                charmander.visible = True
                pikachu.toFront()
                charmander.toFront()
                app.frickoff = True
    if app.battle_phase and not pokeball.centerX >= 84:
        #Yayyy more math. 
        bg_music.pause()
        battle.play()
        pokeball.visible = True
        app.px += 1
        py = 0.03*(app.px-25)**2+186 # Vertex Form
        pokeball.centerX = app.px
        pokeball.centerY = py
        pokeball.toFront()
        pokeball.rotateAngle += 4.25
        
        #moving hp info
        if t_level.right <= 188:
            t_level.right += 2.5
        if t_hp.right <= 148:
            t_hp.centerX = t_level.centerX +8
        if b_hp.centerX >= 267:
            b_hp.centerX = b_level.centerX +18
        if b_level.centerX >= 307.5:
            b_level.centerX -= 2.5

        #Unleash Pikachu
        if pokeball.centerX >= 84:
            app.unleashPikachu = True
        if app.unleashPikachu:
            t_hp.left = 48
            pikachu.centerX = 80
            pikachu.centerY = 280
            pikachu.visible = True
            pokeball.visible = False
            pikachu.toFront()
            Menu.toFront()
            atk_menu()
    pointer.centerX += pointer.dx
    Catcher.toFront()
    pointer.toFront()
    if pointer.centerX<= 40:
        pointer.dx*= -1
        pointer.dx += 1
    if pointer.centerX>= 370:
        pointer.dx*= -1
        Catcher.toFront()
        pointer.toFront()
    if app.catch:
        b_hp.left = 273
        app.stepsPerSecond = 80
        charmander_pokeball.toFront()
        charmander_pokeball.visible = True
        if app.dx2 <= 200:
            app.dx2 += 1
            app.dy = 13/4000*(app.dx2-200)**2+45
            charmander_pokeball.centerX = app.dx2
            charmander_pokeball.centerY = app.dy
            charmander_pokeball.rotateAngle += 5
        elif app.dy <= 175 and not app.frickoff2:
            app.dx2 += 1
            app.dy = 45/6272*(app.dx2-200)**2+45
            charmander_pokeball.centerX = app.dx2
            charmander_pokeball.centerY = app.dy
            charmander_pokeball.rotateAngle += 5
        if charmander_pokeball.centerX >= 309 and not app.frickoff2:
            charmander_pokeball.centerX = 312
            charmander_pokeball.centerY = 135
            charmander.centerX = 500
            charmander_pokeball.rotateAngle = 0
            app.frickoff2 = True
        if charmander_pokeball.centerX >= 309:
            charmander_pokeball.centerX = 312
            charmander_pokeball.centerY = 135
            ##### Change 2 to rotateAngle 2 and see if its slow. 
            if not app.final_rotation:
                if app.rotation1:
                    charmander_pokeball.rotateAngle +=2
                if charmander_pokeball.rotateAngle >= 45:
                    app.rotation1 = False
                    app.rotation2 = True
                if app.rotation2:
                    charmander_pokeball.rotateAngle -= 2
                if charmander_pokeball.rotateAngle <= -45 and app.rotation2:
                    app.rotation3 = True
                    app.rotation2 = False
                if app.rotation3:
                    charmander_pokeball.rotateAngle += 2 
                if charmander_pokeball.rotateAngle >= 45:
                    app.final_rotation = True
            if app.final_rotation: 
                if charmander_pokeball.rotateAngle > 0:
                    charmander_pokeball.rotateAngle -= 2
                if charmander_pokeball.rotateAngle == 0:
                    app.vicstar1.visible = True
                    app.vicstar2.visible = True
                    app.vicstar3.visible = True
                    if app.vicstar1.centerX >= 272 and app.vicstar1.centerY >= 85:
                        # Parabolic Path for Star 1
                        app.vicstar1.centerX -= 1
                        app.vicstar1.centerY = 40/1369*(app.vicstar1.centerX-272)**2+85
                        if app.vicstar1.opacity < 100: app.vicstar1.opacity += 1
                    if app.vicstar2.centerY >=95:
                        app.vicstar2.centerY -= 1
                        if app.vicstar2.opacity < 100: app.vicstar2.opacity += 1
                    if app.vicstar3.centerX <= 352 and app.vicstar3.centerY >= 85:
                        # Parabolic Path for Star 1
                        app.vicstar3.centerX += 1
                        app.vicstar3.centerY = 40/1369*(app.vicstar3.centerX-352)**2+85
                        if app.vicstar3.opacity < 100: app.vicstar3.opacity += 1

if __name__ == "__main__":
    cmu_graphics.run()
