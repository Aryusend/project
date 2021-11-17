from pico2d import *
import framework
import game_state_lobby
import state_change

import mario
import blocks
import item
import enemy

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
castle=None
movingpipe=False
#UI
numimg=None
score_font=None
time_font=None
timeleft=0
money=0
lifeX=None
coinX=None

#item
mushroom=None
flower=None
star=None
coins=None

#enemy
gumba=None
turtle=None


def enter():
    global M
    M = mario.Mario()
    M.x,M.y=80,80
    mario.marioXEX=0
    global ground,itembox,brick,pipe,sky
    sky=load_image('background.png')
    ground,brick,itembox,pipe=blocks.stage1()
    global flag_stick,flag,flagY,castle
    flag=load_image('flag.png')
    flag_stick=load_image('flag_1.png')
    flagY=335
    castle=load_image('castle.png')
    global score_font,numimg
    numimg = load_image('number.png')
    score_font = load_image('score_font.png')
    global timeleft,time_font
    timeleft=120
    time_font=load_image('time_font.png')
    global mushroom,flower,star
    mushroom=item.mushroom()
    flower=item.flower()
    star=item.star()
    mushroom.x,mushroom.y=itembox[1].x,itembox[1].y
    flower.x, flower.y = itembox[3].x, itembox[3].y
    star.x, star.y = itembox[4].x, itembox[4].y
    global gumba
    gumba=enemy.gumba()
    gumba.x,gumba.y=32*35,80
    global turtle
    turtle=enemy.turtle()
    turtle.x,turtle.y=32*45,80
    global coins
    coins=[item.coin() for i in range(5)]
    coins[0].x,coins[0].y=itembox[0].x,itembox[0].y
    coins[1].x, coins[1].y = itembox[2].x, itembox[2].y
    coins[2].x, coins[2].y = 32*51,32*9; coins[2].activate=True
    coins[3].x, coins[3].y = 32*52,32*9; coins[3].activate=True
    coins[4].x, coins[4].y = 32*53,32*9; coins[4].activate=True
    global lifeX,coinX
    lifeX = load_image('lifeX.png')
    coinX=load_image('coinX.png')



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
    global M,pipe,movingpipe
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if M.x>pipe[1].x-32 and M.x<pipe[1].x+32:
                movingpipe=True
            if M.x>pipe[2].x-32 and M.x<pipe[2].x+32:
                movingpipe=True
        else:
            mario.Mario.handle_event(M,event)

def update():
    global itembox,ground,brick,pipe
    mario.Mario.update(M)
    blocks.updateStage(1,brick,itembox)

    #블럭충돌
    M_collider=False
    if M.state>0:
        if M_collider == False:
            for i in range(len(ground)):
                M_collider = collide(M, ground[i])
                if M_collider == True:
                    collide_True(M, ground[i])
                    break
        if M_collider == False:
            for i in range(len(brick)):
                if brick[i].state == 1:
                    M_collider = collide(M, brick[i])
                if M_collider == True:
                    collide_True(M, brick[i])
                    if brick[i].y > M.y: brick[i].state = 0
                    break
        if M_collider == False:
            for i in range(len(itembox)):
                M_collider = collide(M, itembox[i])
                if M_collider == True:
                    collide_True(M, itembox[i])
                    if itembox[i].y > M.y: itembox[i].state = 0
                    break

        # 파이프 이동
        global movingpipe
        if movingpipe == True:
            M.y -= framework.frame_time
            if M.x > pipe[1].x - 32 and M.x < pipe[1].x + 32:
                if M.y < pipe[1].y:
                    M.x = pipe[2].x
                    movingpipe = False
            elif M.x > pipe[2].x - 32 and M.x < pipe[2].x + 32:
                if M.y < pipe[2].y:
                    M.x = pipe[1].x
                    movingpipe = False
        else:
            if M_collider == False:
                for i in range(len(pipe)):
                    M_collider = collide(M, pipe[i])
                    if M_collider == True:
                        M.y = pipe[i].y + 48
                        M.jummping = False
                        M.jumph = 0
                        break
    if M_collider == False:
        M.jummping = True


    #아이템
    global mushroom,flower,star,coins
    if itembox[0].state==0:
        coins[0].activate=True
    if itembox[1].state==0:
        mushroom.activate=True
    if itembox[2].state==0:
        coins[1].activate=True
    if itembox[3].state==0:
        flower.activate=True
    if itembox[4].state==0:
        star.activate=True

    if mushroom.state==1:
        if collide(M, mushroom) == True:
            mushroom.state = 0
            M.state = 2
            mushroom.activate = False
    if flower.state==1:
        if collide(M, flower) == True:
            flower.state = 0
            M.state = 3
            flower.activate = False
    global money
    for i in range(5):
        if coins[i].state == 1:
            if collide(M, coins[i]) == True:
                money+=1
                framework.totalscore+=100
                coins[i].state = 0
                coins[i].activate = False


    for i in range(5): coins[i].update()
    mushroom.update()
    flower.update()
    star.update()

    if M.state > 0:
        # 굼바
        enemy_c = False
        for i in range(len(pipe)):
            enemy_c = collide(gumba, pipe[i])
            if enemy_c == True: break
        if enemy_c == True: gumba.dir *= -1

        if gumba.state == 1:
            if collide(M, gumba) == True:
                if M.y > gumba.y + 15:
                    framework.totalscore += 20
                    gumba.state = 0
                    M.jumping = True
                    M.jumph = 32
                else:
                    if M.state == 2:
                        M.state = 1
                    elif M.state == 3:
                        M.state = 2
                    elif M.state == 1:
                        playerdie()

        # 엉금엉금
        enemy_c = False
        for i in range(len(pipe)):
            enemy_c = collide(turtle, pipe[i])
            if enemy_c == True: break
        if enemy_c == True: turtle.dir *= -1

        if turtle.state == 1:
            if collide(M, turtle) == True:
                if M.y > turtle.y + 31:
                    framework.totalscore += 20
                    turtle.moving = False
                    turtle.state = 0
                    M.jumping = True
                    M.jumph = 32
                else:
                    if M.state == 2:
                        M.state = 1
                    elif M.state == 3:
                        M.state = 2
                    elif M.state == 1:
                        playerdie()
        else:
            if collide(M, turtle) == True:
                if M.y > turtle.y + 15:
                    turtle.moving = False
                    M.jumping = True
                    M.jumph = 32
                else:
                    framework.totalscore += 5
                    turtle.dir = M.dir
                    turtle.moving = True

    gumba.update()
    turtle.update()

    if M.state==0 and M.y<0:
        framework.change_state(state_change)

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
    if timeleft<=0:
        timeleft=120
        playerdie()









def draw():
    clear_canvas()

    #스테이지
    sky.draw(400, 300)
    mario.Mario.draw(M)

    for i in range(5): coins[i].draw()
    star.draw()
    flower.draw()
    mushroom.draw()

    blocks.drawStage(1,ground,brick,itembox,pipe)
    flag_stick.draw(3200-mario.marioXEX,223)
    flag.draw(3200-mario.marioXEX-16,flagY)
    castle.draw(3400-mario.marioXEX,155)

    gumba.draw()
    turtle.draw()

    
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

    #life
    lifeX.draw(270, 560)
    numimg.clip_draw(framework.marioHeart * 32, 0, 32, 64, 330, 560)

    #coin
    coinX.draw(440, 560)
    numimg.clip_draw(int(money/10) * 32, 0, 32, 64, 500, 560)
    numimg.clip_draw(int(money % 10) * 32, 0, 32, 64, 530, 560)




    update_canvas()

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_True(M,C):
    if M.state == 1:
        if M.y < C.y:
            M.y = C.y - 33
        else:
            M.y = C.y + 32
    else:
        if M.y < C.y:
            M.y = C.y - 65
        else:
            M.y = C.y + 32
    M.jummping = False
    M.jumph = 0

def playerdie():
    M.running=False
    M.state=0
    M.jumping=True
    M.jumph=48
    framework.marioHeart-=1
