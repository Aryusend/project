from pico2d import *
import framework
import server
import image
import stage_select
import player
import collision
import stage_change
import enemy
import sound

flag_y=0

def enter():
    global flag_y
    flag_y = 32 * 11 - 16
    server.mario.x,server.mario.y=80,80
    server.mario.jummping, server.mario.jumph = False, 0
    server.mario.running,player.x_over = False,0
    sound.stage1.play(1)


def exit():
    sound.stage1.stop()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:  framework.quit()
        else: server.mario.handle_event(event)

def update():
    server.mario.update()
    for itm in server.itembox_s1: itm.update()
    collision.player_stage1()
    server.update_s1_item()
    collision.item_player_s1()
    server.enemy_s1_update()
    collision.enemy_player_s1()


    global flag_y
    if server.mario.x>=3200:
        server.mario.running=False
        server.mario.jummping=False
        if server.mario.y>80:
            server.mario.y-=32*4*framework.frame_time
            sound.clear.play(1)
        if flag_y<=112:
            server.mario.dir=1
            server.mario.running=True
        else: flag_y-=32*4*framework.frame_time
    if server.mario.x>=3400:
        server.stage_opened=2
        framework.change_state(stage_select)



    server.time_left -= framework.frame_time
    if server.number_of_life < 0: framework.change_state(stage_change)
    elif server.mario.state==0 and server.mario.y<0:
        framework.change_state(stage_select)
    elif server.time_left<=0:
        server.time_left = 120
        server.mario.die()
    elif server.mario.y<0:
        server.mario.die()

    if server.coin_earned>=30:
        server.coin_earned-=30
        server.number_of_life+=1







def draw():

    clear_canvas()
    image.image_background_blue.draw(400,300)

    #state
    image.write_letter('score', 20, 580)
    image.show_score(40,540)
    image.image_font.clip_draw(64, 0, 32, 32, 260, 570)
    image.image_numbers.clip_draw(int(server.coin_earned % 100 / 10) * 32, 0, 32, 32, 260 + 32, 570)
    image.image_numbers.clip_draw(int(server.coin_earned % 10) * 32, 0, 32, 32, 260 + 64, 570)
    image.show_timeleft(700,570)
    image.show_life(500,570)

    #map
    global flag_y
    image.image_castle.draw(32*106-player.x_over,32*5)
    image.image_flagstick.draw(32*100-player.x_over,32*7)
    image.image_flag.draw(32*100-16-player.x_over,flag_y)
    server.draw_s1_item()
    server.draw_s1()

    #mario
    server.mario.draw()
    server.enemy_s1_draw()


    update_canvas()