from pico2d import *
import collision
import framework
import server
import image
import stage_select
import player
import stage_change
import sound

cup_y=144

def enter():
   server.mario.y=144
   server.mario.x=80
   sound.stage4.play(1)

def exit():
    sound.stage4.stop()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE: framework.quit()
        else: server.mario.handle_event(event)

def update():
    server.mario.update()
    collision.player_stage4()
    server.enemy_s4_update()

    global cup_y
    if server.mario.x >= 2700:
        server.mario.running = False
        server.mario.jummping = False
        if server.mario.y > 80:
            server.mario.y -= 32 * 4 * framework.frame_time
            for pl in server.platform_s4:
                pl.y-= 32 * 4 * framework.frame_time
            cup_y -= 32 * 4 * framework.frame_time
            if cup_y<0:
                server.game_win=True
                framework.change_state(stage_change)




    server.time_left -= framework.frame_time
    if server.number_of_life < 0:
        framework.change_state(stage_change)
    elif server.mario.state == 0 and server.mario.y < 0:
        framework.change_state(stage_select)
    elif server.time_left <= 0:
        server.time_left = 120
        server.mario.die()
    elif server.mario.y < 0:
        server.mario.die()



def draw():

    clear_canvas()
    image.image_background_black.draw(400,300)

    #state
    image.write_letter('score', 20, 580)
    image.show_score(40,540)
    image.image_font.clip_draw(64, 0, 32, 32, 260, 570)
    image.image_numbers.clip_draw(int(server.coin_earned % 100 / 10) * 32, 0, 32, 32, 260 + 32, 570)
    image.image_numbers.clip_draw(int(server.coin_earned % 10) * 32, 0, 32, 32, 260 + 64, 570)
    image.show_timeleft(700,570)
    image.show_life(500,570)

    #map
    server.draw_s4()
    image.image_tiles2.clip_draw(0, 32*4, 32, 32, 2700 - player.x_over, 144)
    image.image_enemy.clip_draw(0, 64, 64, 64, 2850 - player.x_over, cup_y+16)

    #mario
    server.mario.draw()
    server.enemy_s4_draw()

    update_canvas()