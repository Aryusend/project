from pico2d import *
import framework
import server

pixel_per_meter=(8/1.0)
run_speed_kmph=2
run_speed_mph=(run_speed_kmph*1000/60.0)
run_speed_mps=(run_speed_mph/60.0)
run_speed_pps=(run_speed_mph*pixel_per_meter)

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

mario_x_over=0


class Mario:
    def __init__(self):
        #rendering
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

    def get_bb(self):
        if self.state==1:
            return self.x-16, self.y-16, self.x+16, self.y+16
        else :
            return self.x-16, self.y-16, self.x+16, self.y+48


    def update(self):
        global mario_x_over
        #움직임
        if self.running == True:
            self.velocity=run_speed_pps*framework.frame_time
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.x<400 or mario_x_over<0:
                self.x += self.dir * self.velocity
                mario_x_over=0
            elif self.x>=3200:
                self.x += self.dir * self.velocity
            else:
                mario_x_over = self.x - 400
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
        global mario_x_over
        if self.state==0:
            server.image_mario_small.draw(self.x-mario_x_over,self.y)
        elif self.state == 1:
            if self.dir < 0:
                if self.jummping==True: server.image_mario_small.clip_draw(0, 32*5, 32, 32, self.x-mario_x_over, self.y)
                else :server.image_mario_small.clip_draw(int(self.frame) * 32, 32*7, 32, 32, self.x-mario_x_over, self.y)
            else:
                if self.jummping == True: server.image_mario_small.clip_draw(32, 32*5, 32, 32, self.x-mario_x_over, self.y)
                else :server.image_mario_small.clip_draw(int(self.frame) * 32, 32*6, 32, 32, self.x-mario_x_over, self.y)
        elif self.state == 2:
            if self.dir < 0:
                if self.jummping == True: server.image_mario_big.clip_draw(0, 64*2, 32, 64, self.x-mario_x_over, self.y + 16)
                else: server.image_mario_big.clip_draw(int(self.frame) * 32, 64*4, 32, 64, self.x-mario_x_over, self.y + 16)
            else:
                if self.jummping == True: server.image_mario_big.clip_draw(32, 64*2, 32, 64, self.x-mario_x_over, self.y + 16)
                else :server.image_mario_big.clip_draw(int(self.frame) * 32, 64*3, 32, 64, self.x-mario_x_over, self.y + 16)
        elif self.state == 3:
            if self.dir < 0:
                if self.jummping == True: server.image_mario_fire.clip_draw(0, 64*2, 32, 64, self.x-mario_x_over, self.y + 16)
                else :server.image_mario_fire.clip_draw(int(self.frame) * 32, 64*4, 32, 64, self.x-mario_x_over, self.y + 16)
            else:
                if self.jummping == True: server.image_mario_fire.clip_draw(32, 64*2, 32, 64, self.x-mario_x_over, self.y + 16)
                else :server.image_mario_fire.clip_draw(int(self.frame) * 32, 64*3, 32, 64, self.x-mario_x_over, self.y + 16)
