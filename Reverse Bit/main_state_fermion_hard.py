import random
import json
import os

from pico2d import *

import threading
import game_framework
import title_state_hard
import result_state

from note_S import Note_S
from note_D import Note_D
from note_F import Note_F
from note_SPACE import Note_SPACE
from note_J import Note_J
from note_K import Note_K
from note_L import Note_L

from machine_key import Machine_key
from machine import Machine
from score_gauge import Score_gauge
from life_gauge import Life_gauge
from fermion import Fermion



name = "MainState_fermion_hard"

note_1s = None
note_2 = None
note_3 = None
machine_key = None
effect_1 = None
score_gauge = None
fermion = None
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
    global note_Ss,note_Ds,note_Fs,note_SPACEs,note_Js,note_Ks,note_Ls
    global machine_key,effect_1,effect_2,score_gauge,fermion, life_gauge, machine,score
    global plz
    machine = Machine()
    note_Ss = [Note_S() for i in range(10)]
    note_Ds = [Note_D() for i in range(10)]
    note_Fs = [Note_F() for i in range(10)]
    note_SPACEs = [Note_SPACE() for i in range(10)]
    note_Js = [Note_J() for i in range(10)]
    note_Ks = [Note_K() for i in range(10)]
    note_Ls = [Note_L() for i in range(10)]

    machine_key = Machine_key()
    effect_1 = Effect_1()
    effect_2 = Effect_2()
    score_gauge = Score_gauge()
    fermion = Fermion()
    life_gauge = Life_gauge()
    plz = Plz()



def destroy_world():
    global note_Ss, note_Ds, note_Fs,note_SPACEs,note_Js,note_Ks,note_Ls
    global machine_key, effect_1, score_gauge, fermion, life_gauge, machine

    del(note_Ss)
    del(note_Ds)
    del(note_Fs)
    del(note_SPACEs)
    del(note_Js)
    del(note_Ks)
    del(note_Ls)
    del(machine_key)
    del(effect_1)
    del(score_gauge)
    del(fermion)
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
    global note_Ss, note_D, note_F, note_SPACE, note_J, note_K, note_L
    global machine_key, effect_1, score_gauge, machine, life_gauge, fermion,font
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
    global x,note_Ss,note_Ds,note_Fs,note_SPACEs,note_Js,note_Ks,note_Ls,machine
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
            for note_SPACE in note_SPACEs:
             if collide(machine, note_SPACE):
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
            for note_L in note_Ls:
             if collide(machine, note_L):
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
            for note_K in note_Ks:
             if collide(machine, note_K):
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
            for note_J in note_Js:
             if collide(machine, note_J):
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
            for note_F in note_Fs:
             if collide(machine, note_F):
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
            for note_D in note_Ds:
             if collide(machine, note_D):
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
            for note_S in note_Ss:
             if collide(machine, note_S):
                effect_2.draw()
                #note_1.remove()
                score_1 += 100
                print(score_1)
                update_canvas()
                delay(0.01)

def update():
    global note_S,note_Ss, note_D,note_Ds, note_F,note_Fs,note_SPACE,note_SPACEs,note_J,note_Js, note_K,note_Ks,note_L,note_Ls
    global machine_key, effect_1,effect_2, score_gauge, fermion, life_gauge, machine_1
    global playtime

    for note_S in note_Ss:
        note_S.update()
    for note_D in note_Ds:
        note_D.update()
    for note_F in note_Fs:
        note_F.update()
    for note_SPACE in note_SPACEs:
        note_SPACE.update()
    for note_J in note_Js:
        note_J.update()
    for note_K in note_Ks:
        note_K.update()
    for note_L in note_Ls:
        note_L.update()


    if (playtime > 400.0):
        playtime = 0
        game_framework.push_state(result_state)
    delay(0.01)
    playtime += 0.05









def draw():
    global plz
    clear_canvas()

    fermion.draw()
    machine.draw()
    #machine.draw_bb()


    for note_S in note_Ss:
        note_S.draw()
    #for note_1 in note_1s:
        #note_1.draw_bb()

    for note_D in note_Ds:
        note_D.draw()
    #for note_2 in note_2s:
        #note_2.draw_bb()

    for note_F in note_Fs:
        note_F.draw()
    #for note_3 in note_3s:
        #note_3.draw_bb()

    for note_SPACE in note_SPACEs:
        note_SPACE.draw()
    #for note_4 in note_4s:
        #note_4.draw_bb()

    for note_J in note_Js:
        note_J.draw()
    #for note_5 in note_5s:
        #note_5.draw_bb()

    for note_K in note_Ks:
        note_K.draw()
    #for note_6 in note_6s:
        #note_6.draw_bb()

    for note_L in note_Ls:
        note_L.draw()
    #for note_7 in note_7s:
       # note_7.draw_bb()



    machine_key.draw()

    score_gauge.draw()
    life_gauge.draw()
    #font.draw(50, 550, 'Ranking', (255, 0, 0))
    #plz.draw()


    update_canvas()