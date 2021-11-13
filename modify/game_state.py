from pico2d import *
import framework
import world

from mario import Mario
import blocks

mario=None

def enter():
    global mario
    mario = Mario()
    world.add_object(mario, 1)

    g1n,ground1,b1n,bricks,i1n,itembox1=blocks.stage1()
    for i in range(g1n): world.add_object(ground1[i],1)
    for i in range(b1n): world.add_object(bricks[i],1)
    for i in range(i1n): world.add_object(itembox1[i],1)




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
    for object in world.all_objects():
        object.update()


def draw():
    clear_canvas()
    sky = pico2d.load_image('background.png')
    sky.draw(400, 300)
    for game_object in world.all_objects():
        game_object.draw()
    update_canvas()
