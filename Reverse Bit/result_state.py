import random
import json
import os

from pico2d import *

import game_framework
import title_state_easy
import result_state
import result_score



name = "ResultState"

result = None
font = None

class Score:
    global score_1
    sc = 100
    def draw(self):
        font.draw(600, 475, 'SCORE : %8d' % result_score.result, (255, 255, 255))

class Result():
    def __init__(self):
        self.image = load_image('finish.png')
    def draw(self):
        self.image.clip_draw(0,0,1200,950,600,475)
    def update(self):
        pass

def enter():
    global result,font,score
    #font = load_font('ENCR10B.TTF', 100)
    #score = Score()
    result = Result()



def exit():
    global result
    del(result)
    del(font)




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
    #score.draw()

    update_canvas()





