from pico2d import *
import framework
import mario

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

class gumba:
    def __init__(self):
        self.image=load_image('gumba.png')
        self.x,self.y=0,0
        self.state=1
        self.dir=1
        self.jummping = False
        self.frame=0
    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.state==1:self.x+=32*framework.frame_time*self.dir


    def draw(self):
        if self.state==0:
            self.image.clip_draw(0, 0, 32, 32, self.x-mario.marioXEX, self.y)
        else:
            self.image.clip_draw(int(self.frame+1) * 32, 0, 32, 32, self.x - mario.marioXEX, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class turtle:
    def __init__(self):
        self.image = load_image('turtle.png')
        self.x, self.y = 0, 0
        self.state = 1
        self.dir = 1
        self.jummping = False
        self.moving=True
        self.frame = 0

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.moving==True and self.state==1:self.x+=32*framework.frame_time*self.dir
        elif self.moving==True and self.state==0:self.x+=128*framework.frame_time*self.dir


    def draw(self):
        if self.state==0:
            self.image.clip_draw(int(self.frame+2) * 32, 0, 32, 32, self.x - mario.marioXEX, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x - mario.marioXEX, self.y+16)

    def get_bb(self):
        if self.state==1:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 48
        else:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 16




