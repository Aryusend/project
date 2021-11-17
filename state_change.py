import framework
import title_state
import game_state_lobby
import game_state_stage1
import game_state_stage2
import game_state_stage3
import game_state_stage4
from pico2d import *

stageSelect=0
background=None
stage_font=None
numimg=None
presss=None
lifeX=None
gameover_font=None

def enter():
    global stage_font,background,numimg
    background=load_image('state.png')
    stage_font=load_image('stage_font.png')
    numimg=load_image('number.png')
    global stageSelect,presss
    stageSelect=game_state_lobby.stageSelect
    presss=load_image('pressspace.png')
    global lifeX
    lifeX=load_image('lifeX.png')
    global gameover_font
    gameover_font=load_image('gameover_font.png')


def exit():
    pass


def draw():
    clear_canvas()
    background.draw(400,300)
    if framework.marioHeart>=0:
        stage_font.draw(360, 400)
        numimg.clip_draw(stageSelect * 32, 0, 32, 64, 480, 400)
        presss.draw(400, 50)
        lifeX.draw(370, 250)
        numimg.clip_draw(framework.marioHeart * 32, 0, 32, 64, 430, 250)
    else:
        gameover_font.draw(400,300)
    update_canvas()

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
                if framework.marioHeart<0:
                    framework.change_state(title_state)
                else:
                    if stageSelect == 1:
                        framework.change_state(game_state_stage1)
                    if stageSelect == 2:
                        framework.change_state(game_state_stage2)
                    if stageSelect == 3:
                        framework.change_state(game_state_stage3)
                    if stageSelect == 4:
                        framework.change_state(game_state_stage4)

