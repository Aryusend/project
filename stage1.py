from pico2d import *
import framework
import server
import state_change
import stage_select
import blocks
import collision

time_left=0;

def enter():
    global time_left
    time_left=120

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  framework.quit()
        else: server.player.handle_event(event)

def update():
    server.player.update()
    server.update_stage1()
    server.update_item1()
    collision.collision_stage1()





def draw():

    clear_canvas()
    server.image_background_blue.draw(400,300)

    server.write_letter('score', 20, 580)
    server.image_numbers.clip_draw(int(server.total_score / 1000) * 32, 0, 32, 32, 40 + 32 * 0, 540)
    server.image_numbers.clip_draw(int(server.total_score % 1000 / 100) * 32, 0, 32, 32, 40 + 32 * 1, 540)
    server.image_numbers.clip_draw(int(server.total_score % 100 / 10) * 32, 0, 32, 32, 40 + 32 * 2, 540)
    server.image_numbers.clip_draw(int(server.total_score % 10) * 32, 0, 32, 32, 40 + 32 * 3, 540)

    server.image_font.clip_draw(64, 0, 32, 32, 260, 570)
    server.image_numbers.clip_draw(int(server.coin_earned % 100 / 10) * 32, 0, 32, 32, 260 + 32, 570)
    server.image_numbers.clip_draw(int(server.coin_earned % 10) * 32, 0, 32, 32, 260 + 64, 570)

    global time_left
    server.image_font.clip_draw(32, 0, 32, 32, 670, 570)
    server.image_numbers.clip_draw(int(time_left / 100) * 32, 0, 32, 32, 700, 570)
    server.image_numbers.clip_draw(int(time_left % 100 / 10) * 32, 0, 32, 32, 700+32, 570)
    server.image_numbers.clip_draw(int(time_left % 10) * 32, 0, 32, 32, 700+64, 570)



    server.player.draw()
    server.draw_item1()
    server.draw_stage1()

    update_canvas()