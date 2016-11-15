import random
import json
import os

from pico2d import *

import game_framework
import title_state_easy
import result_state



name = "ResultState"

result = None

class Result():
    def __init__(self):
        self.image = load_image('result.png')
    def draw(self):
        self.image.clip_draw(0,0,1200,950,600,475)
    def update(self):
        pass

def enter():
    global result
    result = Result()



def exit():
    global result
    del(result)



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(result)



def update():
    result.update()


def draw():
    clear_canvas()
    result.draw()

    update_canvas()





