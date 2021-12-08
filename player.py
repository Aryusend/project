from pico2d import *
import framework
import server
import image
import sound

pixel_per_meter=(8/1.0)
run_speed_kmph=2
run_speed_mph=(run_speed_kmph*1000/60.0)
run_speed_mps=(run_speed_mph/60.0)
run_speed_pps=(run_speed_mph*pixel_per_meter)

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

x_over=0
class Mario:
    def __init__(self):
        #rendering
        self.frame = 0

        #move
        self.x,self.y=80,80
        self.dir=1
        self.velocity=1
        self.jumph=0

        #state
        self.running=False
        self.jummping=False
        self.state = 1  # 0 dead /1 small /2 big /3 fire /4 invincible
        self.powerup=False

    def get_bb(self):
        if self.state==1:
            return self.x-16, self.y-16, self.x+16, self.y+16
        else :
            return self.x-16, self.y-16, self.x+16, self.y+48


    def update(self):
        global x_over
        for fb in server.fireballs: fb.update()
        #움직임
        if self.powerup==True:
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.frame>=3:
                self.powerup=False
                if self.state==1: self.state=2
                elif self.state==2: self.state=3

        if self.running == True:
            self.velocity=run_speed_pps*framework.frame_time
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            if self.x<400 or x_over<0:
                self.x += self.dir * self.velocity
                x_over=0
            elif self.x>=3200:
                self.x += self.dir * self.velocity
            else:
                x_over = self.x - 400
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
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.dir = 1
            self.running = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            self.running = False
            self.frame = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
            if self.state==3:
                server.fireballs[server.fireball_counter].activate = True
                server.fireballs[server.fireball_counter].x, server.fireballs[server.fireball_counter].y = self.x, self.y
                server.fireballs[server.fireball_counter].dir_x = self.dir
                server.fireball_counter += 1
                if server.fireball_counter >= 20: server.fireball_counter = 0
        if event.type==SDL_KEYDOWN and event.key==SDLK_UP and self.jummping==False:
            self.jummping=True
            self.jumph = 48
            sound.jump.set_volume(20)
            sound.jump.play(1)


    def draw(self):
        global x_over
        for fb in server.fireballs:fb.draw()
        if self.powerup==True:
            if self.state==1:
                if self.dir < 0:image.image_mario_small.clip_draw(int(self.frame) * 32, 64 * 0, 32, 64, self.x - x_over,self.y + 16)
                else:image.image_mario_small.clip_draw(int(self.frame) * 32, 64 * 1, 32, 64, self.x - x_over,self.y + 16)
            if self.state==2:
                if self.dir < 0:image.image_mario_small.clip_draw(int(self.frame) * 32, 64 * 1, 32, 64, self.x - x_over,self.y + 16)
                else:image.image_mario_small.clip_draw(int(self.frame) * 32, 64 * 0, 32, 64, self.x - x_over,self.y + 16)



        elif self.state==0:
            image.image_mario_small.clip_draw(0, 32*4, 32, 32, self.x-x_over, self.y)
        elif self.state == 1:
            if self.dir < 0:
                if self.jummping==True: image.image_mario_small.clip_draw(0, 32*5, 32, 32, self.x-x_over, self.y)
                else :image.image_mario_small.clip_draw(int(self.frame) * 32, 32*7, 32, 32, self.x-x_over, self.y)
            else:
                if self.jummping == True: image.image_mario_small.clip_draw(32, 32*5, 32, 32, self.x-x_over, self.y)
                else :image.image_mario_small.clip_draw(int(self.frame) * 32, 32*6, 32, 32, self.x-x_over, self.y)
        elif self.state == 2:
            if self.dir < 0:
                if self.jummping == True: image.image_mario_big.clip_draw(0, 64*2, 32, 64, self.x-x_over, self.y + 16)
                else: image.image_mario_big.clip_draw(int(self.frame) * 32, 64*4, 32, 64, self.x-x_over, self.y + 16)
            else:
                if self.jummping == True: image.image_mario_big.clip_draw(32, 64*2, 32, 64, self.x-x_over, self.y + 16)
                else :image.image_mario_big.clip_draw(int(self.frame) * 32, 64*3, 32, 64, self.x-x_over, self.y + 16)
        elif self.state == 3:
            if self.dir < 0:
                if self.jummping == True: image.image_mario_fire.clip_draw(0, 64*2, 32, 64, self.x-x_over, self.y + 16)
                else :image.image_mario_fire.clip_draw(int(self.frame) * 32, 64*4, 32, 64, self.x-x_over, self.y + 16)
            else:
                if self.jummping == True: image.image_mario_fire.clip_draw(32, 64*2, 32, 64, self.x-x_over, self.y + 16)
                else :image.image_mario_fire.clip_draw(int(self.frame) * 32, 64*3, 32, 64, self.x-x_over, self.y + 16)

    def die(self):
        self.running=False
        self.state=0
        self.jummping=True
        self.jumph=48
        server.number_of_life-=1
        sound.sound_die.set_volume(30)
        sound.sound_die.play(1)

