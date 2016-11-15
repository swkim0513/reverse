import random
import json
import os

from pico2d import *

import threading
import game_framework
import title_state_hard
import result_state

from note_1 import Note_1
from note_2 import Note_2
from note_3 import Note_3
from note_4 import Note_4
from note_5 import Note_5
from note_6 import Note_6
from note_7 import Note_7

from machine_key import Machine_key
from machine import Machine
from score_gauge import Score_gauge
from life_gauge import Life_gauge
from pdm import Pdm



name = "MainState_pdm_hard"

note_1s = None
note_2 = None
note_3 = None
machine_key = None
effect_1 = None
score_gauge = None
pdm = None
life_gauge = None
machine = None
playtime = 0.0
score_1 = 0
font = None
plz = None



class Effect_1():
    global x
    def __init__(self):
        self.image = load_image('effect_3.png')
    def draw(self):
        self.image.clip_draw(0,0,60,60,x,40)
    def update(self):
        pass
class Effect_2():
    global x
    def __init__(self):
        self.image = load_image('effect_2.png')

    def draw(self):
        self.image.clip_draw(0,0,60,60,x,100)
    def update(self):
        pass
class Plz():
    image = None

    def __init__(self):
        self.x,self.y = 400,300
        self.time = 0

    def update(self):
        pass
    def draw(self):
        font.draw('ENCR10B.TTF','Ranking', (255, 0, 0))


def create_world():
    global note_1s,note_2s,note_3s,note_4s,note_5s,note_6s,note_7s
    global machine_key,effect_1,effect_2,score_gauge,pdm, life_gauge, machine,score
    global plz
    machine = Machine()
    note_1s = [Note_1() for i in range(10)]
    note_2s = [Note_2() for i in range(10)]
    note_3s = [Note_3() for i in range(10)]
    note_4s = [Note_4() for i in range(10)]
    note_5s = [Note_5() for i in range(10)]
    note_6s = [Note_6() for i in range(10)]
    note_7s = [Note_7() for i in range(10)]

    machine_key = Machine_key()
    effect_1 = Effect_1()
    effect_2 = Effect_2()
    score_gauge = Score_gauge()
    pdm = Pdm()
    life_gauge = Life_gauge()
    plz = Plz()



def destroy_world():
    global note_1s, note_2s, note_3s,note_4s,note_5s,note_6s,note_7s
    global machine_key, effect_1, score_gauge, pdm, life_gauge, machine

    del(note_1s)
    del(note_2s)
    del(note_3s)
    del(note_4s)
    del(note_5s)
    del(note_6s)
    del(note_7s)
    del(machine_key)
    del(effect_1)
    del(score_gauge)
    del(pdm)
    del(life_gauge)
    del(machine)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global note_1s, note_2, note_3, note_4, note_5, note_6, note_7
    global machine_key, effect_1, score_gauge, machine, life_gauge, pdm,font
    global plz
    create_world()
    plz = Plz()
    font = load_font('ENCR10B.TTF',30)





def exit():
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
    global x,note_1s,note_2s,note_3s,note_4s,note_5s,note_6s,note_7s,machine
    global score_1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state_hard)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            x = 203
            effect_1.draw()
            update_canvas()
            delay(0.01)
            for note_4 in note_4s:
             if collide(machine, note_4):
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
            for note_7 in note_7s:
             if collide(machine, note_7):
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
            for note_6 in note_6s:
             if collide(machine, note_6):
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
            for note_5 in note_5s:
             if collide(machine, note_5):
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
            for note_3 in note_3s:
             if collide(machine, note_3):
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
            for note_2 in note_2s:
             if collide(machine, note_2):
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
            for note_1 in note_1s:
             if collide(machine, note_1):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)

def update():
    global note_1,note_1s, note_2,note_2s, note_3,note_3s,note_4,note_4s,note_5,note_5s, note_6,note_6s,note_7,note_7s
    global machine_key, effect_1,effect_2, score_gauge, pdm, life_gauge, machine_1
    global playtime

    for note_1 in note_1s:
        note_1.update()
    for note_2 in note_2s:
        note_2.update()
    for note_3 in note_3s:
        note_3.update()
    for note_4 in note_4s:
        note_4.update()
    for note_5 in note_5s:
        note_5.update()
    for note_6 in note_6s:
        note_6.update()
    for note_7 in note_7s:
        note_7.update()


    if (playtime > 400.0):
        playtime = 0
        game_framework.push_state(result_state)
    delay(0.01)
    playtime += 0.05









def draw():
    global plz
    clear_canvas()

    pdm.draw()
    machine.draw()
    #machine.draw_bb()


    for note_1 in note_1s:
        note_1.draw()
    #for note_1 in note_1s:
        #note_1.draw_bb()

    for note_2 in note_2s:
        note_2.draw()
    #for note_2 in note_2s:
        #note_2.draw_bb()

    for note_3 in note_3s:
        note_3.draw()
    #for note_3 in note_3s:
        #note_3.draw_bb()

    for note_4 in note_4s:
        note_4.draw()
    #for note_4 in note_4s:
        #note_4.draw_bb()

    for note_5 in note_5s:
        note_5.draw()
    #for note_5 in note_5s:
        #note_5.draw_bb()

    for note_6 in note_6s:
        note_6.draw()
    #for note_6 in note_6s:
        #note_6.draw_bb()

    for note_7 in note_7s:
        note_7.draw()
    #for note_7 in note_7s:
       # note_7.draw_bb()



    machine_key.draw()

    score_gauge.draw()
    life_gauge.draw()
    #font.draw(50, 550, 'Ranking', (255, 0, 0))
    #plz.draw()


    update_canvas()