from pico2d import *
import framework
import server
import image

import title
import stage1
import stage2
import stage3
import stage4

def enter():
    if server.mario.state==0:
        server.mario.state=1
    server.time_left=120

def exit():
    pass

def draw():
    clear_canvas()

    image.image_background_black.draw(400,300)
    if server.game_win==True:
        image.write_letter('you win',280,300)
        image.write_letter('thank you for playing',80,32)
    elif server.number_of_life <0: image.write_letter('game over',280,300)
    else:
        image.write_letter('stage',300,350)
        image.image_numbers.clip_draw(server.stage_selected * 32, 0, 32, 32, 480, 350)
        image.image_font.clip_draw(32*5, 0, 48, 32, 340, 250)
        image.image_font.clip_draw(32*4, 0, 32, 32, 400, 250)
        image.image_numbers.clip_draw(server.number_of_life * 32, 0, 32, 32, 450, 250)

    update_canvas()

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE): framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if server.game_win==True: framework.change_state(title)
                elif server.number_of_life < 0: framework.change_state(title)
                elif server.number_of_life >= 0:
                    if server.stage_selected == 1: framework.change_state(stage1)
                    elif server.stage_selected == 2: framework.change_state(stage2)
                    elif server.stage_selected == 3: framework.change_state(stage3)
                    elif server.stage_selected == 4: framework.change_state(stage4)


