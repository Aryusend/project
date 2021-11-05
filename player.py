from pico2d import *

class Player:
    def __init__(self):
       #rendering
       self.seeL = load_image('MgoingL.png')
       self.seeR = load_image('MgoingR.png')
       self.BseeL = load_image('BMgoingL.png')
       self.BseeR = load_image('BMgoingR.png')
       self.FseeL = load_image('FMgoingL.png')
       self.FseeR = load_image('FMgoingR.png')
       self.frame=0

       #move
       self.dir = 1
       self.x, self.y = 0, 0
       self.running = False
       self.jumping = False
       self.jumpcounter=0

       #collision
       self.collision=True
       self.ly=16

       #state
       self.state = 1 #0 dead 1 small 2 big 3 fire

    def update(self):
        if self.running==True:
            self.frame=(self.frame+1)%4
            self.x += self.dir * 8
        if self.collision==False:
            self.y-=8
            self.jumping=False
        if self.jumping==True and self.jumpcounter<6:
            self.y+=32
            self.jumpcounter+=1




    def draw(self):
        if self.state==1:
            if self.dir < 0:
                self.seeL.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
            else:
                self.seeR.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
        elif self.state==2:
            if self.dir < 0:
                self.BseeL.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y)
            else:
                self.BseeR.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y)
        elif self.state==3:
            if self.dir < 0:
                self.FseeL.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y)
            else:
                self.FseeR.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y)


