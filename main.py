from pico2d import *
import player
import level
import item

open_canvas()
sky=load_image('background.png')
mario=player.Player()

mush=item.Item()
flower=item.Item()
star=item.Item()

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
            mario.frame=0
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            mario.dir=1
            mario.running=True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            mario.running = False
            mario.frame=0
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP and mario.jumping==False:
            mario.jumping=True


gameplaying=True
mario.x, mario.y = 32 * 3, 32 * 3
g1n,ground1,b1n,bricks1,i1n,itemboxs1 = level.stage1()


mush.x, mush.y,mush.state = itemboxs1[0].x, itemboxs1[0].y,1
flower.x, flower.y,flower.state= itemboxs1[1].x, itemboxs1[1].y,2
star.x, star.y,star.state= itemboxs1[3].x, itemboxs1[3].y,3

while gameplaying:
    clear_canvas()

    sky.draw(400,300)

    mush.draw()
    flower.draw()
    star.draw()

    level.drawStage(1, ground1, bricks1, itemboxs1)
    for i in range(4): itemboxs1[i].update()



    mario.draw()
    mario.update()

    player.player_block_collider(mario,ground1,g1n)
    player.player_block_collider(mario,itemboxs1,i1n)
    player.player_block_collider(mario,bricks1,b1n)





    if mario.x>400and mario.running==True:
        for i in range(60):
            ground1[i].x-=mario.dir*8
        for i in range(3):
            bricks1[i].x -= mario.dir*8
        for i in range(4):
            itemboxs1[i].x -= mario.dir*8



    if itemboxs1[0].state==0: mush.activate=True
    if itemboxs1[1].state == 0: flower.activate = True
    if itemboxs1[3].state == 0: star.activate = True

    mush.update()
    flower.update()
    star.update()
    mush.x,flower.x=itemboxs1[0].x,itemboxs1[1].x
    star.x=itemboxs1[3].x

    for mx in range(mario.x - 16, mario.x + 16):
        if mx > mush.x - 16 and mx < mush.x + 16:
            for my in range(mario.y - 16, mario.y + 16):
                if my > mush.y - 16 and my < mush.y + 16:
                    if mush.state>0:
                        mario.state=2
                        mush.state=0

    for mx in range(mario.x - 16, mario.x + 16):
        if mx > flower.x - 16 and mx < flower.x + 16:
            for my in range(mario.y - 16, mario.y + 16):
                if my > flower.y - 16 and my < flower.y + 16:
                    if flower.state>0:
                        mario.state=3
                        flower.state=0




    update_canvas()
    delay(0.05)
    handle_events()


close_canvas()



