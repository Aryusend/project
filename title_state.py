import framework
import game_state_lobby
from pico2d import *


image = None
cusor = None
menuindex=1
def enter():
    global image
    global cusor
    image = load_image('title.png')
    cusor = load_image('cusor.png')
    framework.marioHeart=3

def exit():
    global image,cusor
    del(image)
    del(cusor)

def draw():
    clear_canvas()
    image.draw(400,300)
    if menuindex==1:
        cusor.draw(280,260)
    else :
        cusor.draw(280, 200)
    update_canvas()

def update():
    pass

def handle_events():
    global menuindex
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if menuindex == 1: menuindex = 2
                else: menuindex=1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if menuindex == 1: menuindex = 2
                else:  menuindex = 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if menuindex==1: framework.change_state(game_state_lobby)
                else : framework.quit()



