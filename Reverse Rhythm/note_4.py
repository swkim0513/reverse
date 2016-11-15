#space-key

from pico2d import *
import random


class Note_4:

    image = None;


    def __init__(self):
        self.x = 203
        self.y = random.randint(3000,10000)
        if Note_4.image == None:
            Note_4.image = load_image('note_2.png')
    def update(self):
        self.y -= 10
        delay(0.0001)

    #def remove(self):
        #self.y = -1000

    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 50, self.x +10,self.y+50


    def draw_bb(self):
        draw_rectangle(*self.get_bb())