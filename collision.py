import server

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_True(M,C):
    if M.dir>0:
        if M.y < C.y + 16 and M.y > C.y - 16:
            if M.x < C.x:
                M.x = C.x - 34
                return
    else:
        if M.y < C.y + 16 and M.y > C.y - 16:
            if M.x > C.x:
                M.x = C.x + 34
                return


    if M.state == 1:
        if M.y < C.y:
            M.y = C.y - 33
            M.jumph = 0
            return
    else:
        if M.y < C.y:
            M.y = C.y - 65
            M.jumph = 0
            return
    #y
    if M.y > C.y:
        M.y = C.y + 32
        M.jummping = False
        M.jumph = 0
        return



def collision_stage1():

    #mario-block
    M=server.player
    ground=server.ground_stage1
    brick=server.bricks_stage1
    itembox=server.itemboxs_stage1
    pipe=server.pipe_stage1
    M_collider = False
    if M.state > 0:
        if M_collider == False:
            for i in range(len(ground)):
                M_collider = collide(M, ground[i])
                if M_collider == True:
                    collide_True(M, ground[i])
                    break
        if M_collider == False:
            for i in range(len(brick)):
                if brick[i].state == 1:
                    M_collider = collide(M, brick[i])
                if M_collider == True:
                    collide_True(M, brick[i])
                    if brick[i].y > M.y: brick[i].state = 0
                    break
        if M_collider == False:
            for i in range(len(itembox)):
                M_collider = collide(M, itembox[i])
                if M_collider == True:
                    collide_True(M, itembox[i])
                    if itembox[i].y > M.y: itembox[i].state = 0
                    break
        if M_collider == False:
            for i in range(len(pipe)):
                M_collider = collide(M, pipe[i])
                if M_collider == True:
                    M.y = pipe[i].y + 48
                    M.jummping = False
                    M.jumph = 0
                    if M.y<pipe[i].y+31:
                        if M.dir==1: M.x=pipe[i].x-49
                        elif M.dir == -1: M.x = pipe[i].x + 49

                    break
        if M_collider==False:
            M.jummping=True



    #mario-item
    for coin in server.coins_stage1:
        if coin.activate==True:
            if collide(M, coin) == True:
                coin.activate = False
                server.coin_earned += 1
                server.total_score += 10

    if server.mushroom_stage1.state==1:
        if collide(M,server.mushroom_stage1)==True:
            M.state=2
            server.mushroom_stage1.state=0
            server.total_score+=10


    #mario-enemy

    #enemy-block



