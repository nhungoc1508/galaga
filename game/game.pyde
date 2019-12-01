import os, random
import playership_pyde as ps

path = os.getcwd() + "/"
width = 480
height = 700
bg = loadImage(path + "../images/background.png")
score = 0

def scoredisplay():
    fill(0)
    textAlign(LEFT)
    textSize(20)
    text('Score:'+str(score), 10, 30)

def setup():
    size(width, height)
    frameRate(20)
    noStroke()
    imageMode(CENTER)


def draw():
# if frameCount % 12 == 0:
    x = frameCount % bg.height * 2
    copy(bg, 0, 0, width, bg.height, 0, x, width, bg.height)
    if bg.height - x<height:
        copy(bg, 0, bg.height - x, width, bg.height, 0, 0, width, bg.height)
    ps.playerShip.display()
    ps.playerShip.move()
    ps.bullets.shoot()

    scoredisplay()


def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            ps.playerShip.keyHandler[RIGHT] = True
            ps.playerShip.keyHandler[LEFT] = False
        elif keyCode == LEFT:
            ps.playerShip.keyHandler[RIGHT] = False
            ps.playerShip.keyHandler[LEFT] = True
