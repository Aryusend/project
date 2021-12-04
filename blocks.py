from pico2d import *
import framework
import server
from mario import mario_x_over

time_per_action=6
action_per_time=1.0/time_per_action
frames_per_action=8

class ground:
    def __init__(self):
        self.x,self.y=0,0

    def draw(self):
        server.image_tiles.clip_draw(0, 32 * 4, 32, 32, self.x - mario_x_over, self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16



class itembox:
    def __init__(self):
        self.frame = 0
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        if self.state==1:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x - mario_x_over, self.y)
        else : self.image.clip_draw(3 * 32, 0, 32, 32, self.x - mario_x_over, self.y)


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
            self.image.draw(self.x - mario_x_over, self.y)


    def update(self):
        pass

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class pipe:
    def __init__(self):
        self.x,self.y=0,0

    def draw(self):
        self.image.draw(self.x-mario_x_over, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32


#------------------set Stage1----------------------------
#ground
ground_stage1=[ground() for i in range(240)]
for i in range(120): ground_stage1[i].x, ground_stage1[i].y = i * 32, 48
for i in range(120, 240):ground_stage1[i].x, ground_stage1[i].y = ground_stage1[i - 120].x, 16
#brick
bricks_stage1 = [brick() for i in range(11)]
bricks_stage1[0].x, bricks_stage1[0].y = 32 * 17, 32 * 5
bricks_stage1[1].x, bricks_stage1[1].y = 32 * 19, 32 * 5
bricks_stage1[2].x, bricks_stage1[2].y = 32 * 21, 32 * 5
bricks_stage1[3].x, bricks_stage1[3].y = 32 * 46, 32 * 5
bricks_stage1[4].x, bricks_stage1[4].y = 32 * 48, 32 * 5
bricks_stage1[5].x, bricks_stage1[5].y = 32 * 50, 32 * 9
bricks_stage1[6].x, bricks_stage1[6].y = 32 * 51, 32 * 9
bricks_stage1[7].x, bricks_stage1[7].y = 32 * 52, 32 * 9
bricks_stage1[8].x, bricks_stage1[8].y = 32 * 53, 32 * 9
bricks_stage1[9].x, bricks_stage1[9].y = 32 * 54, 32 * 9
bricks_stage1[10].x, bricks_stage1[10].y = 32 * 55, 32 * 9
#itembox
itemboxs_stage1 = [itembox() for i in range(5)]
itemboxs_stage1[0].x, itemboxs_stage1[0].y = 32 * 14, 32 * 5
itemboxs_stage1[1].x, itemboxs_stage1[1].y = 32 * 18, 32 * 5
itemboxs_stage1[2].x, itemboxs_stage1[2].y = 32 * 20, 32 * 5
itemboxs_stage1[3].x, itemboxs_stage1[3].y = 32 * 19, 32 * 9
itemboxs_stage1[4].x, itemboxs_stage1[4].y = 32 * 47, 32 * 5
pipe_stage1 = [pipe() for i in range(4)]
pipe_stage1[0].x,pipe_stage1[0].y= 32 * 30, 32 * 3
pipe_stage1[1].x, pipe_stage1[1].y = 32 * 40, 32 * 3
pipe_stage1[2].x, pipe_stage1[2].y = 32 * 60, 32 * 3
pipe_stage1[3].x, pipe_stage1[3].y = 32 * 70, 32 * 3
#=======================================================
