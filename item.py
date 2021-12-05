from pico2d import *
import framework
import server
import mario


time_per_action=8
action_per_time=1.0/time_per_action
frames_per_action=16

class mushroom:
    def __init__(self):
        self.x, self.y = 0, 0
        self.activate = False
        self.acount = 0
        self.dir=1
        self.state=1

    def update(self):
        if self.activate == True:
            if self.acount < 32:
                self.y += 16*framework.frame_time
                self.acount += 16*framework.frame_time
            else :
                pass
                #self.x+=self.dir*32*framework.frame_time

    def draw(self):
        if self.state==1:
            server.image_mushroom.draw(self.x-mario.mario_x_over,self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class flower:
    def __init__(self):
        self.x, self.y = 0, 0
        self.activate = False
        self.acount = 0
        self.state = 1

    def update(self):
        if self.activate == True:
            if self.acount < 32:
                self.y += 16*framework.frame_time
                self.acount += 16*framework.frame_time

    def draw(self):
        if self.state==1:
            server.image_flower.draw(self.x-mario.mario_x_over,self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class star:
    def __init__(self):
        self.x, self.y = 0, 0
        self.activate = False
        self.acount = 0
        self.state = 1

    def update(self):
        if self.activate == True:
            if self.acount < 32:
                self.y += 16*framework.frame_time
                self.acount += 16*framework.frame_time

    def draw(self):
        if self.state==1:
            server.image_star.draw(self.x-mario.mario_x_over,self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class coin:
    def __init__(self):
        self.x, self.y = 0, 0
        self.activate = False
        self.acount = 0
        self.state = 1
        self.frame=0

    def update(self):
        if self.activate == True:
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.acount < 32:
                self.y += 16 * framework.frame_time
                self.acount += 16 * framework.frame_time

    def draw(self):
        if self.state == 1:
            server.image_coin.clip_draw(int(self.frame) * 16, 0, 16, 32, self.x - mario.mario_x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

