import os, random
path = os.getcwd() + "/../"
width = 480
height = 700

class enemyShip:
    def __init__(self,score):
        self.diff = score
        self.dead = 0
        if self.diff < 1000:
            # type is the type of ship
            # type 0 small
            # type 1 medium
            # type 2 big
            self.type = 1
            self.life = 1
        elif self.diff <5000:
            if random.random(0,1)<0.9:
                self.type = 1
                self.life = 1
            else:
                self.type = 2
                self.life = 5
        else:
            if random.random(0,1) < 0.7:
                self.type = 1
                self.life = 1
            elif random.random(0,1) < 0.9:
                self.type = 2
                self.life = 5
            else:
                self.type = 3
                self.life = 20

        self.img = []
        

        self.img.append(loadImage(path+'images/enemy'+str(self.type)+'.png'))
        self.img.append(loadImage(path+'images/enemy'+str(self.type)+'_down1.png'))
        self.img.append(loadImage(path+'images/enemy'+str(self.type)+'_down2.png'))
        self.img.append(loadImage(path+'images/enemy'+str(self.type)+'_down3.png'))
        self.img.append(loadImage(path+'images/enemy'+str(self.type)+'_down4.png'))
    
        self.x = random.randint(0,450)
        self.y = 0

    def display(self):
        self.y += 3
        image(self.img[0],self.x,self.y)

    def die(self):
        image(self.img[1],self.x,self.y)
        # image(self.img[2],self.x,self.y)
        # image(self.img[3],self.x,self.y)
        # image(self.img[4],self.x,self.y)
