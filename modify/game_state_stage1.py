from pico2d import *
import framework
import game_state_lobby

from mario import Mario
import blocks

mario=None
ground=None
itembox=None
brick=None
gn,itn,bn=0,0,0

def enter():
    global mario,ground,itembox,brick,gn,itn,bn
    mario = Mario()
    ground,brick,itembox=blocks.stage1()


def exit():
    pass

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
    global itembox,ground,brick
    Mario.update(mario)
    for i in itembox:
        i.update()
    for g in ground:
        g.update()
    for b in brick:
        b.update()
    #if mario.x>400:
        #framework.stageindex=2
        #framework.change_state(game_state_lobby)


def draw():
    global mario
    clear_canvas()
    sky = pico2d.load_image('background.png')
    sky.draw(400, 300)
    Mario.draw(mario)
    blocks.drawStage(1,ground,brick,itembox)
    update_canvas()
