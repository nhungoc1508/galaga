import os, random
import playership_pyde as ps
import enemyship as es

path = os.getcwd() + "/"
width = 480
height = 700
bg = loadImage(path + "../images/background.png")

class Game:
    def __init__(self):
        self.enemy=[]
        self.time = 0
        if self.time % 10 == 0:
            self.enemy.append(es.enemyShip(ps.playerShip.score))

    def scoreDisplay(self):
        fill(0)
        textAlign(LEFT)
        textSize(20)
        text('Score:'+str(ps.playerShip.score), 10, 30)

    def gameOver(self):
        fill(0)
        textAlign(CENTER)
        textSize(50)
        text('GAME OVER!\n')
        text('Score:' + str(ps.playerShip.score))

    def display(self):
        for i in range(len(self.enemy)):
            if self.enemy[i].diecounter==0:
                self.enemy[i].display()

    def isdead_enemy(self):
        for i in range(len(self.enemy)):
            for j in range(len(ps.bullets.tray)):
                try:
                    if (ps.bullets.tray[j].x+30 >= self.enemy[i].x >= ps.bullets.tray[j].x-30) and (ps.bullets.tray[j].y+30 >= self.enemy[i].y >= ps.bullets.tray[j].y-30):
                        if self.enemy[i].diecounter == 0:
                            ps.bullets.tray.pop(j)
                        if self.enemy[i].diecounter < 4:
                            image(self.enemy[i].img[self.enemy[i].diecounter],self.enemy[i].x,self.enemy[i].y)
                            self.enemy[i].diecounter+=1
                        else:
                            enemy.pop(i)
                except:
                    continue
game = Game()

def setup():
    size(width, height)
    frameRate(60)
    noStroke()
    imageMode(CENTER)


def draw():
    if frameCount % 2 == 0:
        x = frameCount % height 
        copy(bg, 0, 0, width, bg.height, 0, x, width, bg.height)
        copy(bg, 0, bg.height - x, width, bg.height, 0, 0, width, bg.height)
        ps.playerShip.display()
        ps.playerShip.move()
        ps.bullets.shoot()

        game.isdead_enemy()
        game.display()
        game.scoreDisplay()
    game.time+=1

def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            ps.playerShip.keyHandler[RIGHT] = True
            ps.playerShip.keyHandler[LEFT] = False
        elif keyCode == LEFT:
            ps.playerShip.keyHandler[RIGHT] = False
            ps.playerShip.keyHandler[LEFT] = True
