from pico2d import *
import random
import frametime
import Fermion_Note
import Pdm_Note
import title_num

y_change = 0

class Note_4_extreme:

    image = None;


    def __init__(self):
        global y_change
        self.x = 203
        if (title_num.num == 0):
            if (Fermion_Note.note_spnum < Fermion_Note.note_sp_size):
                self.y = Fermion_Note.note_spy[Fermion_Note.note_spnum] * -1
                Fermion_Note.note_spnum += 1
            else:
                self.y = 0
        elif (title_num.num == 1):
            if (Pdm_Note.note_spnum < Pdm_Note.note_sp_size):
                self.y = Pdm_Note.note_spy[Pdm_Note.note_spnum] * -1
                Pdm_Note.note_spnum += 1
            else:
                self.y = 0
        if Note_4_extreme.image == None:
            Note_4_extreme.image = load_image('note_2.png')
    def update(self):
        distance = frametime.RUN_SPEED_PPS * frametime.frame_time
        self.y += (distance * 4)
        print(self.y)
        delay(0.0001)

    #def remove(self):
        #self.y = -1000

    def draw(self):
        self.image.clip_draw(0,0,60,30,self.x,self.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x +10,self.y+20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())