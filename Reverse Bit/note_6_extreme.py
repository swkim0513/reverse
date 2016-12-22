from pico2d import *
import random
import frametime
import Fermion_Note
import Pdm_Note
import title_num

y_change = 0

class Note_6_extreme:

    image = None;


    def __init__(self):
        global y_change
        self.x = 320
        if (title_num.num == 0):
            if (Fermion_Note.note_knum < Fermion_Note.note_k_size):
                self.y = Fermion_Note.note_ky[Fermion_Note.note_knum] * -1
                Fermion_Note.note_knum += 1
            else:
                self.y = 0
        elif (title_num.num == 1):
            if (Pdm_Note.note_knum < Pdm_Note.note_k_size):
                self.y = Pdm_Note.note_ky[Pdm_Note.note_knum] * -1
                Pdm_Note.note_knum += 1
            else:
                self.y = 0
        if Note_6_extreme.image == None:
            Note_6_extreme.image = load_image('note_3.png')
    def update(self):
        distance = frametime.RUN_SPEED_PPS * frametime.frame_time
        self.y += (distance * 4)

        delay(0.0001)

    #def remove(self):
        #self.y = -1000

    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 30, self.x +10,self.y+30


    def draw_bb(self):
        draw_rectangle(*self.get_bb())