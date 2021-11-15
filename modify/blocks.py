from pico2d import *
import framework
import mario

time_per_action=6
action_per_time=1.0/time_per_action
frames_per_action=8

class ground:
    def __init__(self):
        self.image = load_image('Ground.png')
        self.x,self.y=0,0

    def draw(self):
        self.image.draw(self.x-mario.marioXEX, self.y)

    def update(self):
        pass


class itembox:
    def __init__(self):
        self.image = load_image('itembox.png')
        self.frame = 0
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        if self.state==1:
            self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x - mario.marioXEX, self.y)
        else : self.image.clip_draw(3 * 32, 0, 32, 32, self.x - mario.marioXEX, self.y)


    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 3.0


class brick:
    def __init__(self):
        self.image = load_image('brick.png')
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        self.image.draw(self.x-mario.marioXEX, self.y)

    def update(self):
        pass


class pipe:
    def __init__(self):
        self.image = load_image('pipe.png')
        self.x,self.y=0,0

    def draw(self):
        self.image.draw(self.x-mario.marioXEX, self.y)

    def update(self):
        pass

#함수
def updateStage(index,b,itm):
    for i in range(b1n): b[i].update()
    for i in range(i1n): itm[i].update()


def drawStage(index,g,b,itm,p):
    if index==1:
        for i in range(len(g)): g[i].draw()
        for i in range(len(b)): b[i].draw()
        for i in range(len(itm)): itm[i].draw()
        for i in range(len(p)): p[i].draw()


#------------------set Stage1----------------------------
g1n,b1n,i1n=240,3,4
p1n=4
def stage1():
    global g1n,b1n,i1n,p1n
    #바닥
    ground1 = [ground() for i in range(g1n)]
    for i in range(120):
        ground1[i].x, ground1[i].y = i * 32, 48
    for i in range(120, 240):
        ground1[i].x, ground1[i].y = ground1[i-120].x, 16

    #일반벽돌
    bricks1 = [brick() for i in range(b1n)]
    bricks1[0].x, bricks1[0].y = 32 * 17, 32 * 5
    bricks1[1].x, bricks1[1].y = 32 * 19, 32 * 5
    bricks1[2].x, bricks1[2].y = 32 * 21, 32 * 5
    
    #아이템블록
    itemboxs1 = [itembox() for i in range(i1n)]
    itemboxs1[0].x, itemboxs1[0].y = 32 * 14, 32 * 5
    itemboxs1[1].x, itemboxs1[1].y = 32 * 18, 32 * 5
    itemboxs1[2].x, itemboxs1[2].y = 32 * 20, 32 * 5
    itemboxs1[2].state = 0
    itemboxs1[3].x, itemboxs1[3].y = 32 * 19, 32 * 9
    
    #파이프
    pipe1 = [pipe() for i in range(p1n)]
    pipe1[0].x,pipe1[0].y= 32 * 30, 32 * 3
    pipe1[1].x, pipe1[1].y = 32 * 40, 32 * 3
    pipe1[2].x, pipe1[2].y = 32 * 60, 32 * 3
    pipe1[3].x, pipe1[3].y = 32 * 70, 32 * 3
    return ground1,bricks1,itemboxs1,pipe1
#=======================================================
