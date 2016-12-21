#d-key
from pico2d import *
import random
import frametime
import Fermion_Note
import title_num
import Pdm_Note

y_change = 0


class Note_D:

    image = None;


    def __init__(self):
        global y_change
        self.x = 87
        if(title_num.num == 0):
            if (Fermion_Note.note_dnum < Fermion_Note.note_d_size):
                self.y = Fermion_Note.note_dy[Fermion_Note.note_dnum]
                Fermion_Note.note_dnum += 1
            else:
                self.y = 0
        elif(title_num.num == 1):
            if (Pdm_Note.note_dnum < Pdm_Note.note_d_size):
                self.y = Pdm_Note.note_dy[Pdm_Note.note_dnum]
                Pdm_Note.note_dnum += 1
            else:
                self.y = 0

        if Note_D.image == None:
            Note_D.image = load_image('note_1.png')
    def update(self):
        distance = frametime.RUN_SPEED_PPS * frametime.frame_time
        self.y -= (distance * 3)



        delay(0.0001)


    def draw(self):
        self.image.clip_draw(0,0,50,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

