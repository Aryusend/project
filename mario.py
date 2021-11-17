from pico2d import *
import framework
import game_state_stage1
import state_change

pixel_per_meter=(8/1.0)
run_speed_kmph=2
run_speed_mph=(run_speed_kmph*1000/60.0)
run_speed_mps=(run_speed_mph/60.0)
run_speed_pps=(run_speed_mph*pixel_per_meter)

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

marioXEX=0

class Mario:
    def __init__(self):
        #rendering
        self.seeL = load_image('MgoingL.png')
        self.seeR = load_image('MgoingR.png')
        self.BseeL = load_image('BMgoingL.png')
        self.BseeR = load_image('BMgoingR.png')
        self.FseeL = load_image('FMgoingL.png')
        self.FseeR = load_image('FMgoingR.png')
        self.frame = 0

        #move
        self.x,self.y=80,80
        self.dir=1
        self.velocity=1
        self.accel=0
        self.jumph=0

        #state
        self.running=False
        self.jummping=False
        self.holdflag=False
        self.state = 1  # 0 dead /1 small /2 big /3 fire /4 invincible

    def update(self):
        global marioXEX
        #골인
        if self.holdflag==True:
            self.running=False
            self.jummping=False
            if self.y>80: self.y-=32*4*framework.frame_time
            if game_state_stage1.flagY<=80:
                self.x+=32*10* framework.frame_time

        #움직임
        if self.running == True:
            #self.accel += run_speed_pps * framework.frame_time
            #self.velocity = self.accel
            #self.velocity = clamp(0, self.velocity, 0.5)
            self.velocity=run_speed_pps*framework.frame_time
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.x<400 or marioXEX<0:
                self.x += self.dir * self.velocity
                marioXEX=0
            elif self.x>=3200:
                self.x += self.dir * self.velocity
            else:
                marioXEX = self.x - 400
                self.x += self.dir * self.velocity

        #점프
        if self.jummping==True:
            self.jumph-=8*framework.frame_time*10
            self.y+=self.jumph*framework.frame_time*10


    def handle_event(self,event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.dir = -1
            self.running = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            self.running = False
            self.frame = 0
            self.accel = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            print(self.x)
            self.dir = 1
            self.running = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            self.running = False
            self.frame = 0
            self.accel = 0
        if event.type==SDL_KEYDOWN and event.key==SDLK_UP and self.jummping==False:
            self.jummping=True
            self.jumph = 48


    def draw(self):
        if self.state == 1:
            if self.dir < 0:
                self.seeL.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x-marioXEX, self.y)
            else:
                self.seeR.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x-marioXEX, self.y)
        elif self.state == 2:
            if self.dir < 0:
                self.BseeL.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x-marioXEX, self.y + 16)
            else:
                self.BseeR.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x-marioXEX, self.y + 16)
        elif self.state == 3:
            if self.dir < 0:
                self.FseeL.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x-marioXEX, self.y + 16)
            else:
                self.FseeR.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x-marioXEX, self.y + 16)

