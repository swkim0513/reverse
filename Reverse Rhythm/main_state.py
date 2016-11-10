import random
import json
import os

from pico2d import *

import threading
import game_framework
import title_state
import result_state



name = "MainState"

fermion = None
life_gauge = None
machine = None
note = None

class Fermion():
    def __init__(self):
        self.image = load_image('fermion.png')
    def draw(self):
        self.image.clip_draw(0,0,1200,950,600,550)
    def update(self):
        pass

class Life_gauge():
    def __init__(self):
        self.image = load_image('life_gauge.png')
    def draw(self):
        self.image.clip_draw(0,0,400,50,900,50)
    def update(self):
        pass
class Machine_1():
    def __init__(self):
        self.image = load_image('machine_2.png')
    def draw(self):
        self.image.clip_draw(0,0,400,950,200,550)
    def update(self):
        pass
class Machine_key():
    def __init__(self):
        self.image = load_image('machine_key.png')
    def draw(self):
        self.image.clip_draw(0,0,400,80,200,40)
class Effect_1():
    global x
    def __init__(self):
        self.image = load_image('Effect_2.png')
    def draw(self):
        self.image.clip_draw(0,0,40,50,x,40)
    def update(self):
        pass

class Score_gauge():
    def __init__(self):
        self.image = load_image('score_gauge.png')
    def draw(self):
        self.image.clip_draw(0,0,800,100,800,50)
    def update(self):
        pass

class Note():

    def __init__(self):
        self.note_1 = load_image('Note_1.png')
        self.note_2 = load_image('Note_2.png')
        self.note_3 = load_image('Note_3.png')
        self.y = 3000
        self.frame = 0

    def draw(self):
        #노트제작구간
        self.note_1.clip_draw(0,0,60,30,37,self.y)
        self.note_1.clip_draw(0,0,50,30,87,self.y + 500)
        self.note_1.clip_draw(0,0,60,30,140,self.y + 1000)
        self.note_2.clip_draw(0,0,60,30,203,self.y + 1500)
        self.note_3.clip_draw(0,0,60,30,266,self.y + 2000)
        self.note_3.clip_draw(0,0,50,30,320,self.y + 2500)
        self.note_3.clip_draw(0,0,60,30,370,self.y + 3000)
    def update(self):
        self.y -= 40
        delay(0.07)




def enter():
    global fermion, life_gauge, machine_1,machine_key, effect_1, note , score_gauge

    fermion = Fermion()
    life_gauge = Life_gauge()
    machine_1 = Machine_1()
    machine_key = Machine_key()
    effect_1 = Effect_1()
    note = Note()
    score_gauge = Score_gauge()




def exit():
    global fermion, life_gauge, machine_1,machine_key,note,score_gauge
    del(fermion)
    del(life_gauge)
    del(machine_1)
    del(machine_key)
    del(note)
    del(score_gauge)


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
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(result_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            x = 37
            effect_1.draw()
            update_canvas()
            delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            x = 90
            effect_1.draw()
            update_canvas()
            delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            x = 140
            effect_1.draw()
            update_canvas()
            delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_j:
            x = 267
            effect_1.draw()
            update_canvas()
            delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_k:
            x = 310
            effect_1.draw()
            update_canvas()
            delay(0.01)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            x = 365
            effect_1.draw()
            update_canvas()
            delay(0.01)

def update():
    note.update()




def draw():

    clear_canvas()

    fermion.draw()
    machine_1.draw()

    note.draw()

    machine_key.draw()
    score_gauge.draw()
    life_gauge.draw()



    update_canvas()





