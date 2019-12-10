import os, random

path = os.getcwd() + "/../"
width = 480
height = 700
bg_width = 480
bg_height = 700
pS_width = 102
pS_height = 126
e_width = 57
e_height = 43
switch = [1, -1]
gif = 0
ex = 0
bg = loadImage(path + "images/background.png")

class playerShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead = False
        self.explode = False
        self.max_distance = (((pS_width+e_width)/2)**2 + ((pS_height+e_height)/2))**0.5
        self.keyHandler = {LEFT: False, RIGHT: False}
        self.score = 0

    def display(self):
        global gif
        global ex
        if not self.dead:
            self.img = []
            self.img.append(loadImage(path + "images/me1.png"))
            self.img.append(loadImage(path + "images/me2.png"))
            image(self.img[gif], self.x, self.y)
            gif += switch[gif]
        else:
            self.destroy = []
            self.destroy.append(loadImage(path + "images/me_destroy_1.png"))
            self.destroy.append(loadImage(path + "images/me_destroy_2.png"))
            self.destroy.append(loadImage(path + "images/me_destroy_3.png"))
            self.destroy.append(loadImage(path + "images/me_destroy_4.png"))
            image(self.destroy[ex], self.x, self.y)
            ex += 1
        if ex == 4:
            self.explode = True
    
    def move(self):
        if self.keyHandler[RIGHT]:
            if self.x+5 < bg_width:
                self.x += 5
        if self.keyHandler[LEFT]:
            if self.x-5 > 0:
                self.x -= 5

    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5

class single_bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        self.img = loadImage(path + "images/bullet1.png")
        image(self.img, self.x, self.y)
    
    def update(self):
        #if self.y <= playerShip.y:
        self.display()
        #self.x = playerShip.x
        self.y = self.y - 20

class bullets:
    def __init__(self):
        self.tray = []
        self.tray.append(single_bullet(playerShip.x, playerShip.y))
        
    def shoot(self):
        for bullet in self.tray:
            bullet.update()
        if self.tray[-1].y == playerShip.y - 80:
            self.tray.append(single_bullet(playerShip.x, playerShip.y))
        if len(self.tray)>30:
            self.tray.pop(0)
    # Problems with bullets: movement is ok but right now bullets are skipping 20px
    # at once. How to make it go 1px (to not miss targets) and speed up?

playerShip = playerShip(width/2, bg_height-pS_height/2)
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
