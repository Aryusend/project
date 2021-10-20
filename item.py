from pico2d import *

class Item:
    def __init__(self):
        self.mushroom = load_image('mushroom.png')
        self.flower = load_image('flower.png')
        self.x,self.y=0,0
        self.activate=False
        self.acount=0
        self.state=0

    def update(self):
        if self.activate==True:
            if self.acount<32:
                self.y+=8
                self.acount+=8

    def draw(self):
        if self.state==1:self.mushroom.draw(self.x,self.y)
        elif self.state == 2: self.flower.draw(self.x, self.y)

