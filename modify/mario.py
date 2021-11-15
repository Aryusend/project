from pico2d import *
import framework

pixel_per_meter=(32/1.0)
run_speed_kmph=20
run_speed_mph=(run_speed_kmph*1000/60.0)
run_speed_mps=(run_speed_mph/60.0)
run_speed_pps=(run_speed_mph*pixel_per_meter)

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8


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
        self.h = 32

        #move
        self.x,self.y=80,80
        self.dir=1
        self.velocity=1
        self.accel=0
        self.jumph=0
        self.xEX=0

        #state
        self.running=False
        self.jummping=False
        self.state = 1  # 0 dead /1 small /2 big /3 fire /4 invincible

    def update(self):
        if self.running == True:
            self.accel += run_speed_pps * framework.frame_time
            self.velocity = self.accel
            self.velocity = clamp(0, self.velocity, 0.5)
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.x<400 or self.xEX<0:
                self.x += self.dir * self.velocity * 4
                self.xEX=0
            else:
                self.xEX+= self.dir * self.velocity * 4

        if self.jummping==True:
            self.jumph-=8*framework.frame_time*10
            self.y+=self.jumph*framework.frame_time*10
        if self.y<80:
            self.y=80
            self.jummping=False
            self.jumph=0


    def handle_event(self,event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.dir = -1
            self.running = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            self.running = False
            self.frame = 0
            self.accel = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
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
                self.seeL.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y)
            else:
                self.seeR.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y)
        elif self.state == 2:
            if self.dir < 0:
                self.BseeL.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x, self.y + 16)
            else:
                self.BseeR.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x, self.y + 16)
        elif self.state == 3:
            if self.dir < 0:
                self.FseeL.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x, self.y + 16)
            else:
                self.FseeR.clip_draw(int(self.frame) * 32, 0, 32, 64, self.x, self.y + 16)

