from pico2d import *
import framework
import image
import player
import server

time_per_action=8
action_per_time=1.0/time_per_action
frames_per_action=16

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
            image.image_coin.clip_draw(int(self.frame) * 16, 0, 16, 32, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16



class items:
    def __init__(self):
        self.x, self.y = 0, 0
        self.activate = False
        self.acount = 0
        self.state = 1
        self.frame = 0

    def update(self):
        if self.state!=0:
            if server.mario.state == 1:
                self.state = 1
            else:
                self.state = 2
        if self.activate == True:
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.acount < 32:
                self.y += 16 * framework.frame_time
                self.acount += 16 * framework.frame_time

    def draw(self):
        if self.state == 1:
            image.image_mushroom.clip_draw(0, 0, 32, 32, self.x - player.x_over, self.y)
        elif self.state==2:
            image.image_flower.clip_draw(0, 0, 32, 32, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16