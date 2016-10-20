import game_framework
import main_state

from pico2d import *


name = "TitleState"
image = None


def enter():
    global image,anotitle
    image = load_image('fermion_title.png')
    anotitle = load_image('anotitle.png')
def exit():
    global image,anotitle
    del(image)
    del(anotitle)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.clip_draw(0,0,1200,400,600,800)
    anotitle.clip_draw(0,0,1200,800,600,200)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






