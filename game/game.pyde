import os, random
import playership_pyde as ps
import enemyship as es

path = os.getcwd() + "/"
width = 480
height = 700
bg = loadImage(path + "../images/background.png")

class Game:
    def __init__(self):
        self.dead = False
        self.enemy=[]
        self.time = 0
        if self.time % 10 == 0:
            self.enemy.append(es.enemyShip(ps.playerShip.score))

    def scoreDisplay(self):
        fill(0)
        textAlign(LEFT)
        textSize(20)
        text('Score:'+str(ps.playerShip.score), 10, 30)
        
    def playerDie(self):
        for enemy in self.enemy:
            if ps.playerShip.distance(enemy) <= ps.playerShip.max_distance:
                ps.playerShip.dead = True
                if ps.playerShip.explode:
                    self.dead = True

    def gameOver(self):
        fill(0)
        textAlign(CENTER)
        textSize(50)
        text('GAME OVER!\n', width/2, height/3)
        text('Score:' + str(ps.playerShip.score), width/2, height/2)

    def display(self):
        for i in range(len(self.enemy)):
            self.enemy[i].display()

game = Game()

def setup():
    size(width, height)
    frameRate(60)
    noStroke()
    imageMode(CENTER)


def draw():
    if frameCount % 2 == 0 and not game.dead:
        x = frameCount % height 
        copy(bg, 0, 0, width, bg.height, 0, x, width, bg.height)
        copy(bg, 0, bg.height - x, width, bg.height, 0, 0, width, bg.height)
        ps.playerShip.display()
        ps.playerShip.move()
        ps.bullets.shoot()

        game.display()
        game.playerDie()
        game.scoreDisplay()
    game.time+=1
    if game.dead:
        game.gameOver()

def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            ps.playerShip.keyHandler[RIGHT] = True
            ps.playerShip.keyHandler[LEFT] = False
        elif keyCode == LEFT:
            ps.playerShip.keyHandler[RIGHT] = False
            ps.playerShip.keyHandler[LEFT] = True
