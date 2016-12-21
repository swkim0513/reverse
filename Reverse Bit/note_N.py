from pico2d import *
import random
import frametime


class Note_N:

    image = None;


    def __init__(self):
        self.x = 70
        self.y = random.randint(1000,50000)
        if Note_N.image == None:
            Note_N.image = load_image('note_1.png')
    def update(self):
        distance = frametime.RUN_SPEED_PPS * frametime.frame_time
        self.y -= (distance * 3)


        print(distance)

        delay(0.0001)


    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

