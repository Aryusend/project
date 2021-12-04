from pico2d import *
import server
import framework
import stage_select

cusor_position=1

def enter():
    server.stage_opened = 1
    server.stage_selected = 0
    server.number_of_life = 3
    server.total_score = 0

def exit():
    pass

def draw():
    global cusor_position

    clear_canvas()

    server.image_title.draw(400,300)
    server.write_letter('start',344,260)
    server.write_letter('exit',360,200)
    server.write_letter('press space to select',80,32)

    if cusor_position==1: server.image_font.clip_draw(0, 0, 32, 32, 280,260)
    else : server.image_font.clip_draw(0, 0, 32, 32, 280, 200)


    update_canvas()

def update():
    pass

def handle_events():
    global cusor_position
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE): framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if cusor_position == 1: cusor_position = 2
                else: cusor_position=1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if cusor_position == 1: cusor_position = 2
                else:  cusor_position = 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if cusor_position==1: framework.change_state(stage_select)
                else : framework.quit()



