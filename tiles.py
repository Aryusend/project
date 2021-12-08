from pico2d import *
import framework
import image
import player

time_per_action=6
action_per_time=1.0/time_per_action
frames_per_action=8

class ground:
    def __init__(self):
        self.x,self.y=0,0
        self.stage_index=1

    def draw(self):
        if self.stage_index == 1:image.image_tiles.clip_draw(0, 32 * 4, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 2:image.image_tiles.clip_draw(32, 32 * 4, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 3:image.image_tiles.clip_draw(0, 32 * 4, 32, 32, self.x - player.x_over, self.y)
        elif self.stage_index == 4:image.image_tiles.clip_draw(64, 32 * 4, 32, 32, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class block:
    def __init__(self):
        self.x,self.y=0,0
        self.stage_index=1

    def draw(self):
        if self.stage_index == 1:image.image_tiles.clip_draw(0, 32 * 3, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 2:image.image_tiles.clip_draw(32, 32 * 3, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 3:image.image_tiles.clip_draw(0, 32 * 3, 32, 32, self.x - player.x_over, self.y)
        elif self.stage_index == 4:image.image_tiles.clip_draw(64, 32 * 3, 32, 32, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class brick():
    def __init__(self):
        self.x,self.y=0,0
        self.stage_index=1
        self.state=1

    def draw(self):
        if self.state==0:return
        elif self.stage_index == 1:image.image_tiles.clip_draw(0, 32 * 5, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 2:image.image_tiles.clip_draw(32, 32 * 5, 32, 32, self.x-player.x_over, self.y)
        elif self.stage_index == 3:image.image_tiles.clip_draw(0, 32 * 5, 32, 32, self.x - player.x_over, self.y)
        elif self.stage_index == 4:image.image_tiles.clip_draw(64, 32 * 5, 32, 32, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class itembox():
    def __init__(self):
        self.x,self.y=0,0
        self.stage_index=1
        self.state=1
        self.frame=0

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 3.0

    def draw(self):
        if self.state==1:
            if self.stage_index == 1:
                image.image_tiles.clip_draw(int(self.frame)*32, 32 * 2, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 2:
                image.image_tiles.clip_draw(int(self.frame)*32, 32 * 1, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 3:
                image.image_tiles.clip_draw(int(self.frame)*32, 32 * 2, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 4:
                image.image_tiles.clip_draw(int(self.frame)*32, 32 * 0, 32, 32, self.x - player.x_over, self.y)
        else:
            if self.stage_index == 1:
                image.image_tiles.clip_draw(3*32, 32 * 2, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 2:
                image.image_tiles.clip_draw(3*32, 32 * 1, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 3:
                image.image_tiles.clip_draw(3*32, 32 * 2, 32, 32, self.x - player.x_over, self.y)
            elif self.stage_index == 4:
                image.image_tiles.clip_draw(3*32, 32 * 0, 32, 32, self.x - player.x_over, self.y)


    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class platfrom:
    def __init__(self):
        self.x,self.y=0,0

    def draw(self):
        image.image_tiles2.clip_draw(32, 32 * 6, 64, 16, self.x-player.x_over, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 8, self.x + 32, self.y + 8


class mushroom:
    def __init__(self):
        self.x,self.y=0,0
        self.index=1

    def draw(self):
        image.image_tiles2.clip_draw(32*self.index, 32 * 5, 32, 32, self.x-player.x_over, self.y)


    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class tile:
    def __init__(self):
        self.x,self.y=0,0
        self.index=1

    def draw(self):
        if self.index==1:image.image_tiles2.clip_draw(0, 32 * 6, 32, 32, self.x-player.x_over, self.y)
        if self.index == 2: image.image_tiles2.clip_draw(64, 32 * 3, 32, 32, self.x - player.x_over, self.y)


class pipe:
    def __init__(self):
        self.x,self.y=0,0
        self.stage_index = 1

    def draw(self):
        if self.stage_index == 1:
            image.image_pipes.clip_draw(0, 64*3, 64, 64, self.x - player.x_over, self.y)
        elif self.stage_index == 2:
            image.image_pipes.clip_draw(0, 64*2, 64, 64, self.x - player.x_over, self.y)
        elif self.stage_index == 3:
            image.image_pipes.clip_draw(0, 64*1, 64, 64, self.x - player.x_over, self.y)
        elif self.stage_index == 4:
            image.image_pipes.clip_draw(0, 64*0, 64, 64, self.x - player.x_over, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32
