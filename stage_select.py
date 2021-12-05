from pico2d import *
import framework
import server
import state_change
from math import floor

def enter():
    pass

def exit():
    pass

mx,my,dir=80,80,1
counter=0
def draw():
    clear_canvas()

    server.image_lobby.draw(400,300)
    server.image_pipes.clip_draw(0, 64*3, 64, 64, 180, 95)
    if server.stage_opened >= 2: server.image_pipes.clip_draw(0, 64*2, 64, 64, 330, 95)
    if server.stage_opened >= 3: server.image_pipes.clip_draw(0, 64*1, 64, 64, 480, 95)
    if server.stage_opened >= 4: server.image_pipes.clip_draw(0, 64*0, 64, 64, 630, 95)

    if server.stage_selected > 0:
        server.write_letter('stage',300,200)
        server.image_numbers.clip_draw(server.stage_selected * 32, 0, 32, 32, 480, 200)


    server.write_letter('score',20,580)
    server.image_numbers.clip_draw(int(server.total_score / 1000) * 32, 0, 32, 32, 40+32*0, 540)
    server.image_numbers.clip_draw(int(server.total_score % 1000 / 100) * 32, 0, 32, 32, 40+32*1, 540)
    server.image_numbers.clip_draw(int(server.total_score % 100 / 10) * 32, 0, 32, 32, 40+32*2, 540)
    server.image_numbers.clip_draw(int(server.total_score % 10) * 32, 0, 32, 32, 40+32*3, 540)

    server.image_font.clip_draw(64, 0, 32, 32, 260, 570)
    server.image_numbers.clip_draw(int(server.coin_earned % 100 / 10) * 32, 0, 32, 32, 260 + 32, 570)
    server.image_numbers.clip_draw(int(server.coin_earned % 10) * 32, 0, 32, 32, 260 + 64, 570)

    if server.stage_selected == 1: server.image_stage2_map.draw(400, 350)
    elif server.stage_selected == 2: server.image_stage2_map.draw(400, 350)
    elif server.stage_selected == 3: server.image_stage2_map.draw(400, 350)
    elif server.stage_selected == 4: server.image_stage2_map.draw(400, 350)

    global mx,my,dir
    if dir==1: server.image_mario_small.clip_draw(0, 32*6, 32, 32, mx, my)
    else : server.image_mario_small.clip_draw(0, 32*7, 32, 32, mx, my)

    update_canvas()

def update():
    global my,counter
    counter+=framework.frame_time*2
    if floor(counter)%2==1: my=143
    else : my=80

def handle_events():
    global mx,my,dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if server.stage_selected < 4 : server.stage_selected+=1
                server.stage_selected=clamp(0,server.stage_selected,server.stage_opened)
                if server.stage_selected == 0: mx, dir = 80, 1
                if server.stage_selected == 1: mx, dir = 180, 1
                if server.stage_selected == 2: mx, dir = 330, 1
                if server.stage_selected == 3: mx, dir = 480, 1
                if server.stage_selected == 4: mx, dir = 630, 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if server.stage_selected  > 0: server.stage_selected  -= 1
                server.stage_selected  = clamp(0, server.stage_selected,server.stage_opened)
                if server.stage_selected == 0: mx, dir = 80, -1
                if server.stage_selected == 1: mx, dir = 180, -1
                if server.stage_selected == 2: mx, dir = 330, -1
                if server.stage_selected == 3: mx, dir = 480, -1
                if server.stage_selected == 4: mx, dir = 630, -1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and server.stage_selected>0:
                framework.change_state(state_change)
