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

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16



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

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class brick:
    def __init__(self):
        self.image = load_image('brick.png')
        self.x, self.y = 0, 0
        self.state = 1

    def draw(self):
        if self.state==1:
            self.image.draw(self.x - mario.marioXEX, self.y)


    def update(self):
        pass

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class pipe:
    def __init__(self):
        self.image = load_image('pipe.png')
        self.x,self.y=0,0

    def draw(self):
        self.image.draw(self.x-mario.marioXEX, self.y)

    def get_bb(self):
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32


#함수

def updateStage(index,b,itm):
    for i in range(b1n): b[i].update()
    for i in range(i1n): itm[i].update()


def drawStage(index,g,b,itm,p):
    if index==1:
        for i in range(len(g)):g[i].draw()
        for i in range(len(b)): b[i].draw()
        for i in range(len(itm)): itm[i].draw()
        for i in range(len(p)): p[i].draw()


#------------------set Stage1----------------------------
g1n,b1n,i1n=240,11,39
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
    bricks1[3].x, bricks1[3].y = 32 * 46, 32 * 5
    bricks1[4].x, bricks1[4].y = 32 * 48, 32 * 5
    bricks1[5].x, bricks1[5].y = 32 * 50, 32 * 9
    bricks1[6].x, bricks1[6].y = 32 * 51, 32 * 9
    bricks1[7].x, bricks1[7].y = 32 * 52, 32 * 9
    bricks1[8].x, bricks1[8].y = 32 * 53, 32 * 9
    bricks1[9].x, bricks1[9].y = 32 * 54, 32 * 9
    bricks1[10].x, bricks1[10].y = 32 * 55, 32 * 9


    
    #아이템블록
    itemboxs1 = [itembox() for i in range(i1n)]
    itemboxs1[0].x, itemboxs1[0].y = 32 * 14, 32 * 5
    itemboxs1[1].x, itemboxs1[1].y = 32 * 18, 32 * 5
    itemboxs1[2].x, itemboxs1[2].y = 32 * 20, 32 * 5
    itemboxs1[3].x, itemboxs1[3].y = 32 * 19, 32 * 9
    itemboxs1[4].x, itemboxs1[4].y = 32 * 47, 32 * 5

    for i in range(5,13):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (80+i-5), 32 * 2 + 16
    for i in range(13,20):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (81+i-13), 32 * 3 + 16
    for i in range(20,26):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (82+i-20), 32 * 4 + 16
    for i in range(26,31):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (83+i-26), 32 * 5 + 16
    for i in range(31,35):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (84+i-31), 32 * 6 + 16
    for i in range(35,38):
        itemboxs1[i].state=0
        itemboxs1[i].x, itemboxs1[i].y = 32 * (85+i-35), 32 * 7 + 16



    
    #파이프
    pipe1 = [pipe() for i in range(p1n)]
    pipe1[0].x,pipe1[0].y= 32 * 30, 32 * 3
    pipe1[1].x, pipe1[1].y = 32 * 40, 32 * 3
    pipe1[2].x, pipe1[2].y = 32 * 60, 32 * 3
    pipe1[3].x, pipe1[3].y = 32 * 70, 32 * 3
    return ground1,bricks1,itemboxs1,pipe1
#=======================================================
