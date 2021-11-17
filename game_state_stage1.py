from pico2d import *
import framework
import game_state_lobby
import state_change

import mario
import blocks

#마리오
M=None
#스테이지 구성
sky=None
ground=None
itembox=None
brick=None
pipe=None
flag_stick=None
flag=None
flagY=335
#UI
numimg=None
score_font=None
time_font=None
timeleft=0


def enter():
    global M
    M = mario.Mario()
    M.x,M.y=80,80
    mario.marioXEX=0
    global ground,itembox,brick,pipe,sky
    sky=load_image('background.png')
    ground,brick,itembox,pipe=blocks.stage1()
    global flag_stick,flag,flagY
    flag=load_image('flag.png')
    flag_stick=load_image('flag_1.png')
    flagY=335
    global score_font,numimg
    numimg = load_image('number.png')
    score_font = load_image('score_font.png')
    global timeleft,time_font
    timeleft=120
    time_font=load_image('time_font.png')



def exit():
    framework.totalscore += 500
    framework.totalscore += timeleft
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            framework.marioHeart-=1
            framework.change_state(state_change)
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
    global flagY
    if M.x>3200:
        M.holdflag=True
        framework.stageindex=2
        if flagY>80: flagY-=32*4*framework.frame_time

    if M.x>3800:
        framework.change_state(game_state_lobby)

    #시간
    global timeleft
    timeleft -= framework.frame_time



def draw():
    clear_canvas()

    #스테이지
    sky.draw(400, 300)
    blocks.drawStage(1,ground,brick,itembox,pipe)
    flag_stick.draw(3200-mario.marioXEX,223)
    flag.draw(3200-mario.marioXEX-16,flagY)

    #마리오
    mario.Mario.draw(M)
    
    #점수
    score_font.draw(100, 580)
    numimg.clip_draw(int(framework.totalscore / 1000) * 32, 0, 32, 64, 40, 540)
    numimg.clip_draw(int(framework.totalscore % 1000 / 100) * 32, 0, 32, 64, 80, 540)
    numimg.clip_draw(int(framework.totalscore % 100 / 10) * 32, 0, 32, 64, 120, 540)
    numimg.clip_draw(int(framework.totalscore % 10) * 32, 0, 32, 64, 160, 540)

    #시간
    time_font.draw(700, 580)
    numimg.clip_draw(int(timeleft / 100) * 32, 0, 32, 64, 660, 540)
    numimg.clip_draw(int(timeleft % 100 / 10) * 32, 0, 32, 64, 700, 540)
    numimg.clip_draw(int(timeleft % 10) * 32, 0, 32, 64, 740, 540)


    update_canvas()
