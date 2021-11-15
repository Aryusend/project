from pico2d import *
import framework
import world
import game_state_lobby

from mario import Mario
import blocks

mario=None

def enter():
    global mario
    mario = Mario()
    world.add_object(mario, 1)

def exit():
    world.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.quit()
        else:
            Mario.handle_event(mario,event)


def update():
    #if mario.x>400:
        #framework.stageindex=2
        #framework.change_state(game_state_lobby)
    for object in world.all_objects():
        object.update()





def draw():
    clear_canvas()
    sky = pico2d.load_image('background.png')
    sky.draw(400, 300)
    for game_object in world.all_objects():
        game_object.draw()
    update_canvas()
