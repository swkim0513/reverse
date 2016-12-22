import game_framework
import difficulty_state

from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1200,950)
    image = load_image('title_2.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if(logo_time > 2.5):
        logo_time = 0
        # game_framework.quit()
        game_framework.push_state(difficulty_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.clip_draw(0,0,1200,950,600,475)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




