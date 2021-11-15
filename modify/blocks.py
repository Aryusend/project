from pico2d import *
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
        self.x+=mario.Mario().xEX


class itembox:
    def __init__(self):
        self.image = load_image('itembox.png')
        self.frame = 0
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        self.image.clip_draw(self.frame*32, 0, 32, 32, self.x, self.y)

    def update(self):
        self.x += mario.Mario().xEX
        self.frame = (self.frame + 1) % 3


class brick:
    def __init__(self):
        self.image = load_image('brick.png')
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += mario.Mario().xEX


def drawStage(index,g,b,itm):
    if index==1:
        global  g1n, b1n, i1n
        for i in range(g1n): g[i].draw()
        for i in range(b1n): b[i].draw()
        for i in range(i1n): itm[i].draw()


#------------------set Stage1----------------------------
g1n,b1n,i1n=60,3,4
def stage1():
    global g1n,b1n,i1n
    ground1 = [ground() for i in range(g1n)]
    for i in range(30):
        ground1[i].x, ground1[i].y = i * 32, 48
    for i in range(30, 60):
        ground1[i].x, ground1[i].y = (i - 30) * 32, 16

    bricks1 = [brick() for i in range(b1n)]
    bricks1[0].x, bricks1[0].y = 32 * 13, 32 * 5
    bricks1[1].x, bricks1[1].y = 32 * 15, 32 * 5
    bricks1[2].x, bricks1[2].y = 32 * 17, 32 * 5

    itemboxs1 = [itembox() for i in range(i1n)]
    itemboxs1[0].x, itemboxs1[0].y = 32 * 10, 32 * 5
    itemboxs1[1].x, itemboxs1[1].y = 32 * 14, 32 * 5
    itemboxs1[2].x, itemboxs1[2].y = 32 * 16, 32 * 5
    itemboxs1[2].state = 0
    itemboxs1[3].x, itemboxs1[3].y = 32 * 15, 32 * 9
    return ground1,bricks1,itemboxs1
#=======================================================
