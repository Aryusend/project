from pico2d import *
import world
import framework
import mario

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

class ground:
    def __init__(self):
        self.image = load_image('Ground.png')
        self.x,self.y=0,0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class itembox:
    def __init__(self):
        self.image = load_image('itembox.png')
        self.frame = 0
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        self.image.clip_draw(self.frame*32, 0, 32, 32, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 3




class block:
    def __init__(self):
        self.image = load_image('brick.png')
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass