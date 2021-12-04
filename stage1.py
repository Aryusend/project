from pico2d import *
import framework
import server
import state_change
import stage_select
from mario import player
import blocks

def enter():
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  framework.quit()
        else: player.handle_event(event)


def update():
    player.update()








def draw():

    clear_canvas()
    server.image_background_blue.draw(400,300)

    player.draw()

    for ground in blocks.ground_stage1:
        ground.draw()


    update_canvas()