import os, random
path = os.getcwd() + "/"
width = 480
height = 700
switch = [1, -1]
gif = 0
bg = loadImage(path + "images/background.png")

class playerShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.keyHandler = {LEFT: False, RIGHT: False}
    
    def display(self):
        global gif
        self.img = []
        self.img.append(loadImage(path + "images/me1.png"))
        self.img.append(loadImage(path + "images/me2.png"))
        image(self.img[gif], self.x, self.y)
        gif += switch[gif]
    
    def move(self):
        if self.keyHandler[RIGHT]:
            if self.x < 0:
                self.x = width
            elif self.x > width:
                self.x = 0
            else:
                self.x += 5
        if self.keyHandler[LEFT]:
            if self.x < 0:
                self.x = width
            elif self.x > width:
                self.x = 0
            else:
                self.x -= 5

class single_bullet:
    def __init__(self):
        self.x = playerShip.x
        self.y = playerShip.y
   
    def display(self):
        self.img = loadImage(path + "images/bullet1.png")
        image(self.img, self.x, self.y)
        
    def move(self):
        self.y -= 5
    
class bullets:
    def __init__(self):
        self.tray = []
        self.tray.append(single_bullet())
    
    def shoot(self):
        self.bullet = self.tray[0]
        self.bullet.display()
        self.bullet.y -=5
        #self.tray.append(single_bullet())

playerShip = playerShip(width/2, height/2)
bullets = bullets()

def setup():
    size(width, height)
    background(bg)
    frameRate(20)
    noStroke()
    imageMode(CENTER)

def draw():
    background(bg)
    if frameCount % 12 == 0:
        background(bg)
    playerShip.display()
    playerShip.move()
    bullets.shoot()
    
def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            playerShip.keyHandler[RIGHT] = True
            playerShip.keyHandler[LEFT] = False
        elif keyCode == LEFT:
            playerShip.keyHandler[RIGHT] = False
            playerShip.keyHandler[LEFT] = True
