import random
import json
import os

from pico2d import *

import threading
import game_framework
import title_state_extreme
import result_state
import frametime
import Fermion_Note

from note_1_extreme import Note_1_extreme
from note_2_extreme import Note_2_extreme
from note_3_extreme import Note_3_extreme
from note_4_extreme import Note_4_extreme
from note_5_extreme import Note_5_extreme
from note_6_extreme import Note_6_extreme
from note_7_extreme import Note_7_extreme

from machine_key_extreme import Machine_key_extreme
from machine_extreme import Machine_extreme
from score_gauge import Score_gauge
from life_gauge import Life_gauge
from fermion import Fermion



name = "MainState_fermion_extreme"

note_1s_extreme = None
note_2s_extreme = None
note_3s_extreme = None
note_4s_extreme = None
note_5s_extreme = None
note_6s_extreme = None
note_7s_extreme = None
machine_key_extreme = None
effect_1 = None
score_gauge = None
fermion = None
life_gauge = None
machine_extreme = None
playtime = 0.0
score_1 = 0
font = None
plz = None



class Effect_1():
    global x
    def __init__(self):
        self.image = load_image('effect_3.png')
    def draw(self):
        self.image.clip_draw(0,0,60,60,x,920)
    def update(self):
        pass
class Effect_2():
    global x
    def __init__(self):
        self.image = load_image('effect_2.png')

    def draw(self):
        self.image.clip_draw(0,0,60,60,x,800)
    def update(self):
        pass

class Score:
    global score_1
    sc = 100
    def draw(self):
        font.draw(500, 50, 'SCORE : %8d' % score_1, (255, 255, 255))

def create_world():
    global note_1s_extreme,note_2s_extreme,note_3s_extreme,note_4s_extreme,note_5s_extreme,note_6s_extreme,note_7s_extreme
    global machine_key_extreme,effect_1,effect_2,score_gauge,fermion, life_gauge, machine_extreme,score
    global plz, score
    score = Score()
    machine_extreme = Machine_extreme()

    Fermion_Note.note_reset()



    note_1s_extreme = [Note_1_extreme() for i in range(Fermion_Note.note_s_size)]
    note_2s_extreme = [Note_2_extreme() for i in range(Fermion_Note.note_d_size)]
    note_3s_extreme = [Note_3_extreme() for i in range(Fermion_Note.note_f_size)]
    note_4s_extreme = [Note_4_extreme() for i in range(Fermion_Note.note_sp_size)]
    note_5s_extreme = [Note_5_extreme() for i in range(Fermion_Note.note_j_size)]
    note_6s_extreme = [Note_6_extreme() for i in range(Fermion_Note.note_k_size)]
    note_7s_extreme = [Note_7_extreme() for i in range(Fermion_Note.note_l_size)]

    frametime.frame_time = frametime.get_frame_time()
    frametime.current_time += frametime.frame_time

    machine_key_extreme = Machine_key_extreme()
    effect_1 = Effect_1()
    effect_2 = Effect_2()
    score_gauge = Score_gauge()
    fermion = Fermion()
    life_gauge = Life_gauge()




def destroy_world():
    global note_1s_extreme, note_2s_extreme, note_3s_extreme,note_4s_extreme,note_5s_extreme,note_6s_extreme,note_7s_extreme
    global machine_key_extreme, effect_1, score_gauge, fermion, life_gauge, machine_extreme

    del(note_1s_extreme)
    del(note_2s_extreme)
    del(note_3s_extreme)
    del(note_4s_extreme)
    del(note_5s_extreme)
    del(note_6s_extreme)
    del(note_7s_extreme)
    del(machine_key_extreme)
    del(effect_1)
    del(score_gauge)
    del(fermion)
    del(life_gauge)
    del(machine_extreme)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a > bottom_b: return False
    if bottom_a < top_b: return False

    return True


def enter():
    global note_1s_extreme, note_2s_extreme, note_3s_extreme, note_4s_extreme, note_5s_extreme, note_6s_extreme, note_7s_extreme
    global machine_key_extreme, effect_1, score_gauge, machine_extreme, life_gauge, fermion,font
    create_world()

    font = load_font('ENCR10B.TTF',50)





def exit():
    global font
    del(font)
    destroy_world()
    #del(font)

def pause():
    pass


def resume():
    pass

y = 1000
class Effect(threading.Thread):
    def run(self):
        global y
        for _ in range(100000):
            y -= 0.4
            delay(0.001)
SendEffect = Effect()


def handle_events():
    global x,note_1s_extreme,note_2s_extreme,note_3s_extreme,note_4s_extreme,note_5s_extreme,note_6s_extreme,note_7s_extreme,machine_extreme
    global score_1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state_extreme)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            x = 203
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_4_extreme in note_4s_extreme:
             if collide(machine_extreme,note_4_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            x = 370
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_7_extreme in note_7s_extreme:
             if collide(note_7_extreme,machine_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            x = 320
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_6_extreme in note_6s_extreme:
             if collide(note_6_extreme,machine_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            x = 266
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_5_extreme in note_5s_extreme:
             if collide(note_5_extreme,machine_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            x = 140
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_3_extreme in note_3s_extreme:
             if collide(note_3_extreme,machine_extreme,):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k:
            x = 87
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_2_extreme in note_2s_extreme:
             if collide(note_2_extreme,machine_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            x = 37
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_1_extreme in note_1s_extreme:
             if collide(note_1_extreme,machine_extreme):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)

def update():
    global note_1_extreme,note_1s_extreme, note_2_extreme,note_2s_extreme, note_3_extreme,note_3s_extreme
    global note_4_extreme,note_4s_extreme,note_5_extreme,note_5s_extreme, note_6_extreme,note_6s_extreme,note_7_extreme,note_7s_extreme
    global machine_key_extreme, effect_1,effect_2, score_gauge, fermion, life_gauge, machine_1_extreme
    global playtime

    frametime.frame_time = frametime.get_frame_time()
    frametime.current_time += frametime.frame_time

    for note_1_extreme in note_1s_extreme:
        note_1_extreme.update()
    for note_2_extreme in note_2s_extreme:
        note_2_extreme.update()
    for note_3_extreme in note_3s_extreme:
        note_3_extreme.update()
    for note_4_extreme in note_4s_extreme:
        note_4_extreme.update()
    for note_5_extreme in note_5s_extreme:
        note_5_extreme.update()
    for note_6_extreme in note_6s_extreme:
        note_6_extreme.update()
    for note_7_extreme in note_7s_extreme:
        note_7_extreme.update()


    if (playtime > 300.0):
        playtime = 0
        game_framework.push_state(result_state)
    delay(0.01)
    playtime += 0.05









def draw():
    global plz
    clear_canvas()

    life_gauge.draw()
    fermion.draw()

    machine_extreme.draw()
    #machine_extreme.draw_bb()


    for note_1_extreme in note_1s_extreme:
        note_1_extreme.draw()
    #for note_1_extreme in note_1s_extreme:
        #note_1_extreme.draw_bb()

    for note_2_extreme in note_2s_extreme:
        note_2_extreme.draw()
    #for note_2_extreme in note_2s_extreme:
        #note_2_extreme.draw_bb()

    for note_3_extreme in note_3s_extreme:
        note_3_extreme.draw()
    #for note_3_extreme in note_3s_extreme:
       # note_3_extreme.draw_bb()

    for note_4_extreme in note_4s_extreme:
        note_4_extreme.draw()
    #for note_4_extreme in note_4s_extreme:
        #note_4_extreme.draw_bb()

    for note_5_extreme in note_5s_extreme:
        note_5_extreme.draw()
    #for note_5_extreme in note_5s_extreme:
        #note_5_extreme.draw_bb()

    for note_6_extreme in note_6s_extreme:
        note_6_extreme.draw()
    #for note_6_extreme in note_6s_extreme:
        #note_6_extreme.draw_bb()

    for note_7_extreme in note_7s_extreme:
        note_7_extreme.draw()
    #for note_7_extreme in note_7s_extreme:
       #note_7_extreme.draw_bb()

    machine_key_extreme.draw()
    score_gauge.draw()

    #font.draw(50, 550, 'Ranking', (255, 0, 0))
    #plz.draw()
    #score,draw()


    update_canvas()