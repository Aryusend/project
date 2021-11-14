import framework
import game_state_stage1
from pico2d import *

def enter():
    pass

def exit():
    pass

def draw():
    pass

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                framework.change_state(game_state_stage1)