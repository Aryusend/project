import framework
import game_state_stage1
import game_state_stage2
import game_state_stage3
import game_state_stage4
from pico2d import *

image = None
image_stage1=None
image_stage2=None
image_stage3=None
image_stage4=None
marioL=None
marioR=None

marioX=100
marioFrame=0
marioMoving=False
marioDir=1
stageSelect=0

def enter():
    global image,marioL,marioR
    global image_stage1,image_stage2,image_stage3,image_stage4
    image = load_image('lobby.png')
    image_stage1 = load_image('pipe.png')
    image_stage2 = load_image('pipe2.png')
    image_stage3 = load_image('pipe3.png')
    image_stage4 = load_image('pipe4.png')
    marioL= load_image('MgoingL.png')
    marioR = load_image('MgoingR.png')


def exit():
    global image,image_stage1,image_stage2,image_stage3,image_stage4,marioL,marioR
    del(image)
    del (image_stage1)
    del (image_stage2)
    del (image_stage3)
    del (image_stage4)
    del (marioL)
    del (marioR)


def draw():
    clear_canvas()
    image.draw(400,300)
    image_stage1.draw(180,95)
    if framework.stageindex>=2: image_stage2.draw(330, 95)
    if framework.stageindex >= 3: image_stage3.draw(480, 95)
    if framework.stageindex >= 4: image_stage4.draw(630, 95)

    if marioDir > 0: marioR.clip_draw(marioFrame * 32, 0, 32, 32, marioX, 80)
    if marioDir < 0: marioL.clip_draw(marioFrame * 32, 0, 32, 32, marioX, 80)
    update_canvas()

def update():
    global marioFrame,marioMoving,marioDir,marioX,stageSelect
    marioFrame=(marioFrame+1)%4
    if marioMoving==True:
        if marioDir >0:
            if stageSelect==1:
                if marioX<=180: marioX+=1
                else : marioMoving=False
            elif stageSelect==2:
                if marioX<=330: marioX+=1
                else : marioMoving=False
            elif stageSelect==3:
                if marioX<=480: marioX+=1
                else : marioMoving=False
            elif stageSelect==4:
                if marioX<=630: marioX+=1
                else : marioMoving=False
            else : marioMoving=False
        if marioDir <0:
            if stageSelect==1:
                if marioX>180: marioX-=1
                else : marioMoving=False
            elif stageSelect==2:
                if marioX>330: marioX-=1
                else : marioMoving=False
            elif stageSelect==3:
                if marioX>480: marioX-=1
                else : marioMoving=False
            elif stageSelect==4:
                if marioX>630: marioX-=1
                else : marioMoving=False
            else :
                if marioX>100: marioX-=1
                else : marioMoving=False



def handle_events():
    global marioDir,marioMoving,stageSelect
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT) and marioMoving==False:
                if stageSelect < 4 : stageSelect+=1
                stageSelect=clamp(0,stageSelect,framework.stageindex)
                marioMoving=True
                marioDir=1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT) and marioMoving==False:
                if stageSelect > 0: stageSelect -= 1
                stageSelect = clamp(0, stageSelect, framework.stageselect)
                marioMoving=True
                marioDir=-1

            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if stageSelect==1:
                    framework.change_state(game_state_stage1)
                if stageSelect==2:
                    framework.change_state(game_state_stage2)
                if stageSelect==3:
                    framework.change_state(game_state_stage3)
                if stageSelect==4:
                    framework.change_state(game_state_stage4)
