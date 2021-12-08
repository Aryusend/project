import image
import framework
import player

time_per_action=0.5
action_per_time=1.0/time_per_action
frames_per_action=8

class fireball:
    def __init__(self):
        self.x,self.y=0,0
        self.dir_x=1
        self.frame=0
        self.activate=False

    def get_bb(self):
        return self.x - 4, self.y - 4, self.x + 4, self.y + 4

    def update(self):
        if self.activate==True:
            self.frame = (self.frame + frames_per_action * action_per_time * framework.frame_time) % 4.0
            self.x += 512 * framework.frame_time * self.dir_x


    def draw(self):
        if self.activate==True:
            image.image_fire.clip_draw(int(self.frame) * 8, 16, 8, 8, self.x-player.x_over, self.y)


