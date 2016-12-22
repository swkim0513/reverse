import game_framework
import title_state_easy
import title_state_hard
import title_state_extreme


from pico2d import *

from music import Music

name = "DifficultyState"
easy = None
hard = None
extreme = None
music = None


def enter():
    global easy,hard,extreme,lite,music
    lite = load_image('lite_2.png')
    easy = load_image('easy.png')
    hard = load_image('hard.png')
    extreme = load_image('extreme.png')
    music = Music()

def exit():
    global easy,hard,extreme,lite
    del(easy)
    del(hard)
    del(extreme)
    del(lite)



def handle_events():
    events = get_events()
    global x,y
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title_state_easy)
            elif(event.type) == (SDL_MOUSEMOTION):
                x,y = event.x,950 - event.y
                if(y>634):
                    easy.clip_draw(0, 0, 1200, 400, 600, 850)
                    update_canvas()
                    delay(0.01)
                if(y<=634):
                    if(y>317):
                        hard.clip_draw(0, 0, 1200, 400, 600, 525)
                        update_canvas()
                        delay(0.01)
                if(y<=317):
                    extreme.clip_draw(0, 0, 1200, 400, 600, 200)
                    update_canvas()
                    delay(0.01)

            elif(event.type) == (SDL_MOUSEBUTTONDOWN):
                x,y = event.x,950 - event.y
                if(y>634):
                    game_framework.change_state(title_state_easy)
                if(y<=634):
                    if(y>317):
                       game_framework.change_state(title_state_hard)
                if(y<=317):
                    game_framework.change_state(title_state_extreme)




def draw():
    clear_canvas()
    lite.clip_draw(0,0,1200,950,600,475)

    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






