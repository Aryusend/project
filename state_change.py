from pico2d import *
import framework
import server
import title
import stage_select

import stage1

def enter():
    pass

def exit():
    pass

def draw():
    clear_canvas()

    server.image_background_black.draw(400,300)

    if server.number_of_life <=0: server.write_letter('game over',280,300)
    else:
        server.write_letter('stage',300,350)
        server.image_numbers.clip_draw(server.stage_selected * 32, 0, 32, 32, 480, 350)
        server.image_font.clip_draw(32*5, 0, 48, 32, 340, 250)
        server.image_font.clip_draw(32*4, 0, 32, 32, 400, 250)
        server.image_numbers.clip_draw(server.number_of_life * 32, 0, 32, 32, 450, 250)

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
                if server.number_of_life <= 0: framework.change_state(title)
                else:
                    if server.stage_selected == 1: framework.change_state(stage1)
                    elif server.stage_selected == 2: framework.change_state(stage1)
                    elif server.stage_selected == 3: framework.change_state(stage1)
                    elif server.stage_selected == 4: framework.change_state(stage1)


