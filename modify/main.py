from pico2d import *
import player
import level

open_canvas()

sky=load_image('background.png')

mario=player.Player()

def handle_events():
    global gameplaying
    events = get_events()
    for event in events:
        #menu
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gameplaying=False
        #player
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            mario.dir=-1
            mario.running=True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            mario.running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            mario.dir=1
            mario.running=True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            mario.running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP and mario.jumping == False:
            mario.jumping = True




gameplaying=True
mario.x, mario.y = 32 * 3, 32 * 3
g1n,ground1,b1n,bricks1,i1n,itemboxs1 = level.stage1()

while gameplaying:
    clear_canvas()
    sky.draw(400, 300)

    mario.draw()
    mario.update()

    level.drawStage(1,ground1,bricks1,itemboxs1)

    player.player_block_collision(mario,ground1,g1n)
    player.player_block_collision(mario, itemboxs1, i1n)
    player.player_block_collision(mario, bricks1, b1n)

    update_canvas()
    delay(0.05)
    handle_events()


close_canvas()