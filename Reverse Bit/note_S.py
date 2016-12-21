#s-key
from pico2d import *
import random
import frametime
import Fermion_Note
import Pdm_Note
import title_num

y_change = 0


class Note_S:

    image = None;


    def __init__(self):
        global y_change
        self.x = 37
        if(title_num.num == 0):
            if (Fermion_Note.note_snum < Fermion_Note.note_s_size):
                self.y = Fermion_Note.note_sy[Fermion_Note.note_snum]
                Fermion_Note.note_snum += 1
            else:
                self.y = 0
        elif(title_num.num == 1):
            if (Pdm_Note.note_snum < Pdm_Note.note_s_size):
                self.y = Pdm_Note.note_sy[Pdm_Note.note_snum]
                Pdm_Note.note_snum += 1
            else:
                self.y = 0

        if Note_S.image == None:
            Note_S.image = load_image('note_1.png')
    def update(self):
        distance = frametime.RUN_SPEED_PPS * frametime.frame_time
        self.y -= (distance * 4)




        delay(0.0001)


    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

