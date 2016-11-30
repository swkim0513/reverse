#k-key

from pico2d import *
import random


class Note_K:

    image = None;


    def __init__(self):
        self.x = 320
        self.y = random.randint(3000,50000)
        if Note_K.image == None:
            Note_K.image = load_image('note_3.png')
    def update(self):
        self.y -= 10
        delay(0.0001)

    #def remove(self):
        #self.y = -1000

    def draw(self):
        self.image.clip_draw(0,0,50,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())