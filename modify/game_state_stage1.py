from pico2d import *
import framework
import game_state_lobby

import mario
import blocks

M=None
ground=None
itembox=None
brick=None
pipe=None

def enter():
    global M,ground,itembox,brick,pipe
    M = mario.Mario()
    ground,brick,itembox,pipe=blocks.stage1()


def exit():
    global M, ground, itembox, brick,pipe
    del(M)
    del(ground)
    del(itembox)
    del(brick)
    del(pipe)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.quit()
        else:
            mario.Mario.handle_event(M,event)


def update():
    global itembox,ground,brick,pipe
    mario.Mario.update(M)
    blocks.updateStage(1,brick,itembox)

    #블럭충돌




    if M.y < 80:
        M.y = 80
        M.jummping = False
        M.jumph = 0

    #골인
    #if mario.x>400:
        #framework.stageindex=2
        #framework.change_state(game_state_lobby)


def draw():
    global mario
    clear_canvas()
    sky = pico2d.load_image('background.png')
    sky.draw(400, 300)
    mario.Mario.draw(M)
    blocks.drawStage(1,ground,brick,itembox,pipe)
    update_canvas()
