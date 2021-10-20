from pico2d import *

class block:
    def __init__(self):
        #rendering
        self.ground = load_image('Ground.png')
        self.itembox = load_image('itembox.png')
        self.brick = load_image('brick.png')
        self.frame=0

        #set
        self.x, self.y = 0, 0
        self.id=1 #1ground 2brick 3itembox
        self.state=1

    def update(self):
        if self.id==3:
            self.frame = (self.frame + 1) % 40

    def draw(self):
        if self.id==1:
            self.ground.draw(self.x, self.y)
        elif self.id==2:
            if self.state == 1:
                self.brick.draw(self.x, self.y)
        elif self.id==3:
            if self.state == 1:
                if self.frame < 30: self.itembox.clip_draw(0 * 32, 0, 32, 32, self.x, self.y)
                if (self.frame >= 30) and (self.frame < 34): self.itembox.clip_draw(1 * 32, 0, 32, 32, self.x, self.y)
                if (self.frame >= 34) and (self.frame < 40): self.itembox.clip_draw(2 * 32, 0, 32, 32, self.x, self.y)
            else:
                self.itembox.clip_draw(3 * 32, 0, 32, 32, self.x, self.y)


def stage1():
    ground1 = [block() for i in range(60)]
    for i in range(30):
        ground1[i].id = 1
        ground1[i].x, ground1[i].y = i * 32, 32
    for i in range(30, 60):
        ground1[i].id = 1
        ground1[i].x, ground1[i].y = (i - 30) * 32, 0

    bricks1 = [block() for i in range(3)]
    for i in range(3): bricks1[i].id = 2
    bricks1[0].x, bricks1[0].y = 32 * 13, 32 * 5
    bricks1[1].x, bricks1[1].y = 32 * 15, 32 * 5
    bricks1[2].x, bricks1[2].y = 32 * 17, 32 * 5

    itemboxs1 = [block() for i in range(4)]
    for i in range(4): itemboxs1[i].id = 3
    itemboxs1[0].x, itemboxs1[0].y = 32 * 10, 32 * 5
    itemboxs1[1].x, itemboxs1[1].y = 32 * 14, 32 * 5
    itemboxs1[2].x, itemboxs1[2].y = 32 * 16, 32 * 5
    itemboxs1[2].state = 0
    itemboxs1[3].x, itemboxs1[3].y = 32 * 15, 32 * 9
    return ground1,bricks1,itemboxs1