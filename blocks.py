from pico2d import *
import framework
import server
import mario

time_per_action=6
action_per_time=1.0/time_per_action
frames_per_action=8

class ground:
    def __init__(self):
        self.x,self.y=0,0
        self.id=1

    def draw(self):
        if self.id==1:server.image_tiles.clip_draw(0, 32 * 4, 32, 32, self.x-mario.mario_x_over, self.y)
        else :server.image_tiles.clip_draw(0, 32 * 3, 32, 32, self.x-mario.mario_x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16



class itembox:
    def __init__(self):
        self.frame = 0
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        if self.state==1:
            server.image_tiles.clip_draw(int(self.frame) * 32, 32*2, 32, 32, self.x - mario.mario_x_over, self.y)
        else :
            server.image_tiles.clip_draw(3 * 32, 32*2, 32, 32, self.x - mario.mario_x_over, self.y)


    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 3.0

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class brick:
    def __init__(self):
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        if self.state==1:
            server.image_tiles.clip_draw(0, 32*5, 32, 32, self.x - mario.mario_x_over, self.y)


    def update(self):
        pass

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class pipe:
    def __init__(self):
        self.x,self.y=0,0

    def draw(self):
        server.image_pipes.clip_draw(0, 64*3, 64, 64, self.x - mario.mario_x_over, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32
