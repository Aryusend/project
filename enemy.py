import image
import framework
import player

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

class gumba:
    def __init__(self):
        self.x,self.y=0,0
        self.state=1
        self.dir=-1
        self.jummping = False
        self.frame=0
        self.stage_index=1

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.state==1:self.x+=32*framework.frame_time*self.dir

    def draw(self):
        if self.stage_index==1:
            if self.state == 0:
                image.image_enemy.clip_draw(0, 32 * 11, 32, 32, self.x - player.x_over, self.y)
            else:
                image.image_enemy.clip_draw(int(self.frame + 1) * 32, 32 * 11, 32, 32, self.x - player.x_over, self.y)
        else:
            if self.state == 0:
                image.image_enemy.clip_draw(0, 32 * 10, 32, 32, self.x - player.x_over, self.y)
            else:
                image.image_enemy.clip_draw(int(self.frame + 1) * 32, 32 * 10, 32, 32, self.x - player.x_over, self.y)


    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class turtle:
    def __init__(self):
        self.x, self.y = 0, 0
        self.state = 1
        self.dir = 1
        self.jummping = False
        self.moving=True
        self.frame = 0

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.moving==True and self.state==1:self.x+=32*framework.frame_time*self.dir
        elif self.moving==True and self.state==0:self.x+=128*framework.frame_time*self.dir


    def draw(self):
        if self.state==0:
            image.image_enemy.clip_draw(int(self.frame+4) * 32, 32*7, 32, 32, self.x - player.x_over, self.y)
        else:
            if self.dir==1:
                image.image_enemy.clip_draw(int(self.frame+2) * 32, 32 * 7, 32, 64, self.x - player.x_over, self.y + 16)
            else :
                image.image_enemy.clip_draw(int(self.frame) * 32, 32 * 7, 32, 64, self.x - player.x_over,self.y + 16)

    def get_bb(self):
        if self.state==1:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 48
        else:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class cave_turtle:
    def __init__(self):
        self.x, self.y = 0, 0
        self.state = 1
        self.dir = -1
        self.jummping = False
        self.moving=True
        self.frame = 0
        self.jumpcount=0

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.moving==True and self.state==1:self.x+=32*framework.frame_time*self.dir
        elif self.moving==True and self.state==0:self.x+=128*framework.frame_time*self.dir
        self.jumpcount+=framework.frame_time
        if self.jumpcount>=2:
            self.jumpcount=0
            self.y+=64
        elif self.y>=80: self.y-=64*framework.frame_time



    def draw(self):
        if self.state==0:
            image.image_enemy.clip_draw(32*4, 32*4, 32, 32, self.x - player.x_over, self.y)
        else:
            if self.dir==1:
                image.image_enemy.clip_draw(int(self.frame+2) * 32, 32 * 4, 32, 32, self.x - player.x_over, self.y)
            else :
                image.image_enemy.clip_draw(int(self.frame) * 32, 32 * 4, 32, 32, self.x - player.x_over,self.y)

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16


class winged_turtle:
    def __init__(self):
        self.x, self.y = 0, 0
        self.state = 1
        self.dir = -1
        self.jummping = False
        self.moving=True
        self.frame = 0

    def update(self):
        self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 2.0
        if self.moving==True and self.state==1:self.y+=32*framework.frame_time*self.dir
        elif self.state==0:self.y+=128*framework.frame_time*-1
        if self.y>=32*13: self.dir=-1
        elif self.y<=32*8: self.dir=1


    def draw(self):
        if self.state==0:
            image.image_enemy.clip_draw(int(self.frame+4) * 32, 32*5, 32, 32, self.x - player.x_over, self.y)
        else:
            if self.dir==1:
                image.image_enemy.clip_draw(int(self.frame+2) * 32, 32 * 5, 32, 64, self.x - player.x_over, self.y + 16)
            else :
                image.image_enemy.clip_draw(int(self.frame) * 32, 32 * 5, 32, 64, self.x - player.x_over,self.y + 16)

    def get_bb(self):
        if self.state==1:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 48
        else:
            return self.x - 16, self.y - 16, self.x + 16, self.y + 16

class larva:
    def __init__(self):
        self.x, self.y = 0, 0
        self.dir = 1

    def draw(self):
        if self.dir==1: image.image_enemy.clip_draw(1* 32, 32 * 9, 32, 32, self.x - player.x_over, self.y)
        else : image.image_enemy.clip_draw(0 * 32, 32 * 9, 32, 32, self.x - player.x_over, self.y)

    def update(self):
        self.y+=512*self.dir*framework.frame_time
        if self.y >= 32 * 13:
            self.dir = -1
        elif self.y <= -32:
            self.dir = 1

    def get_bb(self):
        return self.x - 16, self.y - 16, self.x + 16, self.y + 16
