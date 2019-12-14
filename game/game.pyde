add_library('minim')
player = Minim(this)
import os, random
import playership_pyde as ps
import enemyship as es

path = os.getcwd() + "/"
width = 480
height = 700
pS_width = 102
pS_height = 126
bg = loadImage(path + "../images/background.png")
convert = [5,25,100]

class Game:
    def __init__(self):
        self.dead = False
        self.enemy=[]
        self.time = 0
        self.score = 0
        self.bgSound = player.loadFile(path + "../sound/game_music.wav")
        self.bgSound.play()
        self.bgSound.loop()
        self.enemy_down_sounds = []
        self.enemy_down_sounds.append(player.loadFile(path + "../sound/enemy1_down.wav"))
        self.enemy_down_sounds.append(player.loadFile(path + "../sound/enemy2_down.wav"))
        self.enemy_down_sounds.append(player.loadFile(path + "../sound/enemy3_down.wav"))
        self.player_down_sound = player.loadFile(path + "../sound/me_down.wav")
        self.bullet_sound = player.loadFile(path + "../sound/bullet.wav")
        

    def scoreDisplay(self):
        fill(0)
        textAlign(LEFT)
        textSize(20)
        text('Score: '+str(self.score), 10, 30)
        
    def playerDie(self):
        for enemy in self.enemy:
            if ps.playerShip.distance(enemy) <= ps.playerShip.max_distance:
                ps.playerShip.dead = True
                if ps.playerShip.explode:
                    self.dead = True
                    self.player_down_sound.rewind()
                    self.player_down_sound.play()

    def gameOver(self):
        fill(0)
        textAlign(CENTER)
        textSize(50)
        text('GAME OVER!\n', width/2, height/3)
        text('Score:\n' + str(self.score), width/2, height/2)
        text('Click to restart', width/2, height*3/4)

    def display(self):
        for i in range(len(self.enemy)):
            if self.enemy[i].type == 1:
                if self.enemy[i].diecounter==0:
                    self.enemy[i].display()
            if self.enemy[i].type == 2:
                if self.enemy[i].diecounter<=7:
                    self.enemy[i].display()           
            if self.enemy[i].type == 3:
                if self.enemy[i].diecounter<=15:
                    self.enemy[i].display()

    def isdead_enemy(self):
        for i in range(len(self.enemy)):
            for j in range(len(ps.bullets.tray)):
                try:
                    if (self.enemy[i].y > 0) and (ps.bullets.tray[j].x+30 >= self.enemy[i].x >= ps.bullets.tray[j].x-30) and (ps.bullets.tray[j].y+30 >= self.enemy[i].y >= ps.bullets.tray[j].y-30):
                        if self.enemy[i].type == 1:                
                            if self.enemy[i].diecounter == 0:
                                ps.bullets.tray[j].x = -1000
                                self.enemy_down_sounds[0].rewind()
                                self.enemy_down_sounds[0].play()
                            if self.enemy[i].diecounter < 4:
                                image(self.enemy[i].img[self.enemy[i].diecounter],self.enemy[i].x,self.enemy[i].y)
                                self.enemy[i].diecounter+=1
                            else:
                                game.score+=convert[self.enemy[i].type-1]
                                self.enemy.pop(i)
                        elif self.enemy[i].type == 2:
                            if self.enemy[i].diecounter == 0:
                                self.enemy_down_sounds[1].rewind()
                                self.enemy_down_sounds[1].play()
                            if self.enemy[i].diecounter < 7:
                                ps.bullets.tray[j].x = -1000
                                self.enemy[i].diecounter+=1
                            elif self.enemy[i].diecounter < 11:
                                image(self.enemy[i].img[self.enemy[i].diecounter-7],self.enemy[i].x,self.enemy[i].y)
                                self.enemy[i].diecounter+=1
                            else:
                                game.score+=convert[self.enemy[i].type-1]
                                self.enemy.pop(i)
                        elif self.enemy[i].type == 3:
                            if self.enemy[i].diecounter == 0:
                                self.enemy_down_sounds[2].rewind()
                                self.enemy_down_sounds[2].play()
                            if self.enemy[i].diecounter < 15:
                                ps.bullets.tray[j].x = -1000
                                self.enemy[i].diecounter+=1
                            elif self.enemy[i].diecounter < 19:
                                image(self.enemy[i].img[self.enemy[i].diecounter-7],self.enemy[i].x,self.enemy[i].y)
                                self.enemy[i].diecounter+=1
                            else:
                                game.score+=convert[self.enemy[i].type-1]
                                self.enemy.pop(i)
                            
                except:
                    continue

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
        game.bullet_sound.play()
        game.bullet_sound.rewind()

        game.isdead_enemy()
        game.display()
        game.playerDie()
        game.scoreDisplay()
    game.time+=1
    if game.time % 50 == 0:
        game.enemy.append(es.enemyShip(game.score))
    if game.dead:
        game.bgSound.pause()
        game.gameOver()

def mouseClicked():
    if game.dead:
        game.__init__()
        ps.playerShip.__init__(width/2, height-pS_height/2)
        game.bgSound.rewind()

def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            ps.playerShip.keyHandler[RIGHT] = True
            ps.playerShip.keyHandler[LEFT] = False
        elif keyCode == LEFT:
            ps.playerShip.keyHandler[RIGHT] = False
            ps.playerShip.keyHandler[LEFT] = True
