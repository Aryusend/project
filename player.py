from pico2d import *

class Player:
    def __init__(self):
       #rendering
       self.seeL = load_image('MgoingL.png')
       self.seeR = load_image('MgoingR.png')
       self.BseeL = load_image('BMgoingL.png')
       self.BseeR = load_image('BMgoingR.png')
       self.FseeL = load_image('FMgoingL.png')
       self.FseeR = load_image('FMgoingR.png')
       self.frame=0

       #move
       self.dir = 1
       self.x, self.y = 0, 0
       self.running = False
       self.jumping = False
       self.jumpcounter=0

       #collision
       self.collision=True
       self.ly=16

       #state
       self.state = 1 #0 dead 1 small 2 big 3 fire

    def update(self):
        if self.running==True:
            self.frame=(self.frame+1)%4
            self.x += self.dir * 8
        if self.collision==False:
            self.y-=8
            #self.jumping=False
        if self.jumping==True and self.jumpcounter<6:
            self.y+=32
            self.jumpcounter+=1


    def draw(self):
        if self.state==1:
            if self.dir < 0:
                self.seeL.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
            else:
                self.seeR.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
        elif self.state==2:
            if self.dir < 0:
                self.BseeL.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y+16)
            else:
                self.BseeR.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y+16)
        elif self.state==3:
            if self.dir < 0:
                self.FseeL.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y+16)
            else:
                self.FseeR.clip_draw(self.frame * 32, 0, 32, 64, self.x, self.y+16)




def player_block_collider(player,block,num):
    player.collision=False
    for i in range(num):
        for mx in range(player.x-16,player.x+16):
            if block[i].id==2 and block[i].state<1 : continue
            if mx >block[i].x-16 and mx <block[i].x+16:
                for my in range(player.y-16,player.y+16):
                    if my > block[i].y - 16 and my < block[i].y + 16:
                        player.collision=True
                        if my>block[i].y:yy=block[i].y+32
                        else :
                            if block[i].id==3:
                                block[i].state = 0
                                yy = block[i].y - 32
                            elif block[i].id==2:
                                yy = block[i].y - 32
                                block[i].state = 0
                            else: yy=block[i].y - 32
                        break
            if player.collision==True : break
        if player.collision == True: break

    if player.collision==True:
        player.y = yy
        player.jumping=False
        player.jumpcounter=0

