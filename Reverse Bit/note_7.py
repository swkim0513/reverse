#l-key

from pico2d import *
import random


class Note_7:

    image = None;


    def __init__(self):
        self.x = 370
        self.y = random.randint(3000,50000)
        if Note_7.image == None:
            Note_7.image = load_image('note_1.png')
    def update(self):
        self.y -= 10
        delay(0.0001)

    #def remove(self):
        #self.y = -1000

    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())