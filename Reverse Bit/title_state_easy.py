import game_framework
import main_state_fermion_easy
import main_state_pdm_easy
import difficulty_state
import title_num

from pico2d import *


name = "TitleStateEasy"
fermion_title = None
pdm_title = None


def enter():
    global fermion_title,pdm_title,select
    fermion_title = load_image('fermion.png')
    pdm_title = load_image('pdm.png')
    select = load_image('select.png')
def exit():
    global fermion_title,pdm_title,select
    del(fermion_title)
    del(pdm_title)
    del(select)

def handle_events():
    events = get_events()
    global x,y
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.change_state(difficulty_state)
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state_fermion_easy)
            elif (event.type) == (SDL_MOUSEMOTION):
                x, y = event.x, 950 - event.y
                if (y <= 475):
                    select.clip_draw(0, 0, 1200, 500, 600, 200)
                    update_canvas()

                if(y>475):
                    select.clip_draw(0,0,1200,500,600,700)
                    update_canvas()




            elif(event.type) == (SDL_MOUSEBUTTONDOWN):
                x,y = event.x,950 - event.y
                if(y>475):
                    title_num.num = 0
                    game_framework.change_state(main_state_fermion_easy)
                elif(y<475):
                    title_num.num = 1
                    game_framework.change_state(main_state_pdm_easy)



def draw():
    clear_canvas()
    fermion_title.clip_draw(0,0,1200,500,600,700)
    pdm_title.clip_draw(0,0,1200,500,600,200)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






