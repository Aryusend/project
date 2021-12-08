import server
import sound

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def player_collision32x32(block):
    if server.mario.state == 1:
        if server.mario.y < block.y:
            server.mario.y = block.y - 33
        else:
            server.mario.y = block.y + 32
    else:
        if server.mario.y < block.y:
            server.mario.y = block.y - 65
        else:
            server.mario.y = block.y + 32
    server.mario.jummping = False
    server.mario.jumph = 0

def player_stage1():
    player_stage_collision=False
    if server.mario.state>0:
        if player_stage_collision==False:
            for gr in server.ground_s1:
                player_stage_collision = collide(server.mario, gr)
                if player_stage_collision==True:
                    player_collision32x32(gr)
                    break
        if player_stage_collision==False:
            for bl in server.block_s1:
                player_stage_collision = collide(server.mario, bl)
                if player_stage_collision==True:
                    player_collision32x32(bl)
                    break
        if player_stage_collision==False:
            for br in server.brick_s1:
                if br.state==0:continue
                player_stage_collision = collide(server.mario, br)
                if player_stage_collision==True:
                    player_collision32x32(br)
                    if br.y > server.mario.y:
                        br.state = 0
                        server.total_score+=10
                    break
        if player_stage_collision==False:
            for itm in server.itembox_s1:
                player_stage_collision = collide(server.mario, itm)
                if player_stage_collision==True:
                    player_collision32x32(itm)
                    if itm.y > server.mario.y:
                        itm.state = 0
                        server.total_score += 15
                    break
        if player_stage_collision==False:
            for pipe in server.pipe_s1:
                player_stage_collision = collide(server.mario, pipe)
                if player_stage_collision==True:
                    server.mario.y = pipe.y + 48
                    server.mario.jummping = False
                    server.mario.jumph = 0
                    break
        if player_stage_collision == False:
            server.mario.jummping = True



def player_stage2():
    player_stage_collision=False
    if server.mario.state>0:
        if player_stage_collision==False:
            for gr in server.ground_s2:
                player_stage_collision = collide(server.mario, gr)
                if player_stage_collision==True:
                    player_collision32x32(gr)
                    break
        if player_stage_collision==False:
            for bl in server.block_s2:
                player_stage_collision = collide(server.mario, bl)
                if player_stage_collision==True:
                    player_collision32x32(bl)
                    break
        if player_stage_collision==False:
            for br in server.brick_s2:
                if br.state==0:continue
                player_stage_collision = collide(server.mario, br)
                if player_stage_collision==True:
                    player_collision32x32(br)
                    if br.y > server.mario.y:
                        br.state = 0
                        server.total_score+=10
                    break
        if player_stage_collision==False:
            for itm in server.itembox_s2:
                player_stage_collision = collide(server.mario, itm)
                if player_stage_collision==True:
                    player_collision32x32(itm)
                    if itm.y > server.mario.y:
                        itm.state = 0
                        server.total_score += 15
                    break
        if player_stage_collision == False:
            server.mario.jummping = True
        if player_stage_collision==False:
            for plat in server.platform_s2:
                player_stage_collision = collide(server.mario, plat)
                if player_stage_collision==True:
                    server.mario.y = plat.y + 24
                    server.mario.jummping = False
                    server.mario.jumph = 0
                    break


def player_stage3():
    player_stage_collision=False
    if server.mario.state>0:
        if player_stage_collision==False:
            for gr in server.ground_s3:
                player_stage_collision = collide(server.mario, gr)
                if player_stage_collision==True:
                    player_collision32x32(gr)
                    break
        if player_stage_collision==False:
            for bl in server.block_s3:
                player_stage_collision = collide(server.mario, bl)
                if player_stage_collision==True:
                    player_collision32x32(bl)
                    break
        if player_stage_collision==False:
            for mus in server.mushroom_s3:
                player_stage_collision = collide(server.mario, mus)
                if player_stage_collision==True:
                    player_collision32x32(mus)
                    break
        if player_stage_collision == False:
            for plat in server.platform_s3:
                player_stage_collision = collide(server.mario, plat)
                if player_stage_collision == True:
                    server.mario.y = plat.y + 24
                    server.mario.jummping = False
                    server.mario.jumph = 0
                    break

        if player_stage_collision == False:
            server.mario.jummping = True

def player_stage4():
    player_stage_collision=False
    if server.mario.state>0:
        if player_stage_collision==False:
            for br in server.brick_s4:
                if br.state==0:continue
                player_stage_collision = collide(server.mario, br)
                if player_stage_collision==True:
                    player_collision32x32(br)
                    if br.y > server.mario.y:
                        br.state = 0
                        server.total_score+=10
                    break
        if player_stage_collision == False:
            for plat in server.platform_s4:
                player_stage_collision = collide(server.mario, plat)
                if player_stage_collision == True:
                    server.mario.y = plat.y + 24
                    server.mario.jummping = False
                    server.mario.jumph = 0
                    break
        if player_stage_collision == False:
            server.mario.jummping = True


def item_player_s1():
    for co in server.coin_s1:
        if co.state==0:continue
        if collide(server.mario,co)==True and co.activate==True:
            co.state=0
            server.coin_earned+=1
            server.total_score+=5
            sound.sound_coin.play(1)

    for itm in server.item_s1:
        if itm.state==0:continue
        elif collide(server.mario,itm)==True and itm.activate==True:
            itm.state=0
            server.total_score+=5
            server.mario.powerup=True
            sound.item.play(1)


def item_player_s2():
    for co in server.coin_s2:
        if co.state==0:continue
        if collide(server.mario,co)==True and co.activate==True:
            co.state=0
            server.coin_earned+=1
            server.total_score+=5
            sound.sound_coin.play(1)

    if server.item_s2.state != 0:
        if collide(server.mario, server.item_s2) == True and server.item_s2.activate == True:
            server.item_s2.state = 0
            server.total_score += 5
            server.mario.powerup = True
            sound.item.play(1)


def item_player_s3():
    for co in server.coin_s3:
        if co.state==0:continue
        if collide(server.mario,co)==True and co.activate==True:
            co.state=0
            server.coin_earned+=1
            server.total_score+=5
            sound.sound_coin.play(1)



def enemy_player_s1():
    for gum in server.gumba_s1:
        if gum.state==1 and server.mario.state!=0:
            if collide(server.mario, gum) == True:
                if server.mario.y>gum.y+15:
                    server.total_score+=50
                    gum.state=0
                    server.mario.jummping=True
                    server.mario.jumph=32
                else:
                    if server.mario.state==3:
                        server.mario.state=2
                        server.mario.x=gum.x-50*server.mario.dir
                        server.mario.y=gum.y-50*server.mario.dir
                        break
                    elif server.mario.state==2:
                        server.mario.state =1
                        server.mario.x = gum.x - 50 * server.mario.dir
                        server.mario.y = gum.y - 50 * server.mario.dir
                        break
                    elif server.mario.state==1:
                        server.mario.die()
                        break

    for pipe in server.pipe_s1:
        if collide(server.turtle_s1, pipe):
            server.turtle_s1.dir*=-1

    if server.turtle_s1.state == 1:
        if collide(server.mario, server.turtle_s1) == True:
            if server.mario.y > server.turtle_s1.y + 31:
                server.total_score += 20
                server.turtle_s1.moving = False
                server.turtle_s1.state = 0
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                if server.mario.state == 3:
                    server.mario.state = 2
                    server.mario.x = server.turtle_s1.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s1.y - 50 * server.mario.dir

                elif server.mario.state == 2:
                    server.mario.state = 1
                    server.mario.x = server.turtle_s1.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s1.y - 50 * server.mario.dir

                elif server.mario.state == 1:
                    server.mario.die()

    else:
        if collide(server.mario, server.turtle_s1) == True:
            if server.mario.y > server.turtle_s1.y + 15:
                server.turtle_s1.moving = False
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                server.total_score += 5
                server.turtle_s1.dir = server.mario.dir
                server.turtle_s1.moving = True

def enemy_player_s2():
    for block in server.block_s2:
        for gum in server.gumba_s2:
            if collide(gum, block):
                gum.dir *= -1


    for gum in server.gumba_s2:
        if gum.state==1 and server.mario.state!=0:
            if collide(server.mario, gum) == True:
                if server.mario.y>gum.y+15:
                    server.total_score+=50
                    gum.state=0
                    server.mario.jummping=True
                    server.mario.jumph=32
                else:
                    if server.mario.state==3:
                        server.mario.state=2
                        server.mario.x=gum.x-50*server.mario.dir
                        server.mario.y=gum.y-50*server.mario.dir
                        break
                    elif server.mario.state==2:
                        server.mario.state =1
                        server.mario.x = gum.x - 50 * server.mario.dir
                        server.mario.y = gum.y - 50 * server.mario.dir
                        break
                    elif server.mario.state==1:
                        server.mario.die()
                        break

    for bl in server.block_s2:
        if collide(server.turtle_s2, bl):
            server.turtle_s2.dir*=-1

    if server.turtle_s2.state == 1:
        if collide(server.mario, server.turtle_s2) == True:
            if server.mario.y > server.turtle_s2.y + 15:
                server.total_score += 20
                server.turtle_s2.moving = False
                server.turtle_s2.state = 0
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                if server.mario.state == 3:
                    server.mario.state = 2
                    server.mario.x = server.turtle_s2.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s2.y - 50 * server.mario.dir

                elif server.mario.state == 2:
                    server.mario.state = 1
                    server.mario.x = server.turtle_s2.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s2.y - 50 * server.mario.dir

                elif server.mario.state == 1:
                    server.mario.die()

    else:
        if collide(server.mario, server.turtle_s2) == True:
            if server.mario.y > server.turtle_s2.y + 15:
                server.turtle_s2.moving = False
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                server.total_score += 5
                server.turtle_s2.dir = server.mario.dir
                server.turtle_s2.moving = True



def enemy_player_s3():
    if server.turtle_s3.state == 1:
        if collide(server.mario, server.turtle_s3) == True:
            if server.mario.y > server.turtle_s3.y + 31:
                server.total_score += 20
                server.turtle_s3.moving = False
                server.turtle_s3.state = 0
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                if server.mario.state == 3:
                    server.mario.state = 2
                    server.mario.x = server.turtle_s3.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s3.y - 50 * server.mario.dir

                elif server.mario.state == 2:
                    server.mario.state = 1
                    server.mario.x = server.turtle_s3.x - 50 * server.mario.dir
                    server.mario.y = server.turtle_s3.y - 50 * server.mario.dir

                elif server.mario.state == 1:
                    server.mario.die()

    else:
        if collide(server.mario, server.turtle_s3) == True:
            if server.mario.y > server.turtle_s3.y + 15:
                server.turtle_s3.moving = False
                server.mario.jumping = True
                server.mario.jumph = 32
            else:
                server.total_score += 5
                server.turtle_s3.dir = server.mario.dir
                server.turtle_s3.moving = True