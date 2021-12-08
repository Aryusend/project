import tiles

stage_opened=1
stage_selected=0
#
number_of_life=3
total_score=0
coin_earned=0
time_left=120
#
game_win=False
game_pause=False



#/////////////////
import player
mario=player.Mario()
import mario_fire
fireballs=[mario_fire.fireball() for i in range(20)]
fireball_counter=0

#/////////////////
import tiles
#stage1
ground_s1=[tiles.ground() for i in range(216)]
for g in ground_s1: g.stage_index=1
for i in range(71):ground_s1[i].x,ground_s1[i].y=i*32+16,32+16
for i in range(71,108):ground_s1[i].x,ground_s1[i].y=(i+5)*32+16,32+16
for i in range(108,179):ground_s1[i].x,ground_s1[i].y=(i-108)*32+16,16
for i in range(179,216):ground_s1[i].x,ground_s1[i].y=(i-108+5)*32+16,16

block_s1=[tiles.block() for i in range(15)]
for bl in block_s1: bl.stage_index=1
for i in range(5):block_s1[i].x,block_s1[i].y=(85+i)*32+16,32*2+16
for i in range(5,9):block_s1[i].x,block_s1[i].y=(86+i-5)*32+16,32*3+16
for i in range(9,12):block_s1[i].x,block_s1[i].y=(87+i-9)*32+16,32*4+16
for i in range(12,14):block_s1[i].x,block_s1[i].y=(88+i-12)*32+16,32*5+16
block_s1[14].x,block_s1[14].y=89*32+16,32*6+16

pipe_s1=[tiles.pipe() for i in range(4)]
pipe_s1[0].x,pipe_s1[0].y=32 * 33, 32 * 3
pipe_s1[1].x,pipe_s1[1].y=32 * 46, 32 * 3
pipe_s1[2].x,pipe_s1[2].y=32 * 67, 32 * 3
pipe_s1[3].x,pipe_s1[3].y=32 * 80, 32 * 3

brick_s1=[tiles.brick() for i in range(11)]
for br in brick_s1: br.stage_index=1
brick_s1[0].x,brick_s1[0].y=32*22+16,32*5+16
brick_s1[1].x,brick_s1[1].y=32*24+16,32*5+16
brick_s1[2].x,brick_s1[2].y=32*26+16,32*5+16
brick_s1[3].x,brick_s1[3].y=32*51+16,32*5+16
brick_s1[4].x,brick_s1[4].y=32*53+16,32*5+16
for i in range(5,11): brick_s1[i].x,brick_s1[i].y=32*(56+i-5)+16,32*9+16

itembox_s1=[tiles.itembox() for i in range(5)]
itembox_s1[0].x,itembox_s1[0].y=32*19+16,32*5+16
itembox_s1[1].x,itembox_s1[1].y=32*23+16,32*5+16
itembox_s1[2].x,itembox_s1[2].y=32*25+16,32*5+16
itembox_s1[3].x,itembox_s1[3].y=32*24+16,32*9+16
itembox_s1[4].x,itembox_s1[4].y=32*52+16,32*5+16

def draw_s1():
    global ground_s1
    for g in ground_s1: g.draw()
    global block_s1
    for bl in block_s1: bl.draw()
    global pipe_s1
    for p in pipe_s1:p.draw()
    global brick_s1
    for br in brick_s1: br.draw()
    global itembox_s1
    for itm in itembox_s1: itm.draw()

#stage2
ground_s2 = [tiles.ground() for i in range(194)]
for g in ground_s2: g.stage_index = 2
for i in range(78): ground_s2[i].x, ground_s2[i].y = i * 32 + 16, 32 + 16
for i in range(78,81): ground_s2[i].x, ground_s2[i].y = (i+8) * 32 + 16, 32 + 16
for i in range(81, 97): ground_s2[i].x, ground_s2[i].y = (i + 16) * 32 + 16, 32 + 16
for i in range(97,175): ground_s2[i].x, ground_s2[i].y = (i-97) * 32 + 16,16
for i in range(175,178): ground_s2[i].x, ground_s2[i].y = (i+8-97) * 32 + 16,16
for i in range(178,194): ground_s2[i].x, ground_s2[i].y = (i + 16-97) * 32 + 16,16


brick_s2 = [tiles.brick() for i in range(50)]
for br in brick_s2: br.stage_index = 2
for i in range(5): brick_s2[i].x, brick_s2[i].y = (68+i) * 32 + 16, 32*5+16
for i in range(5,10): brick_s2[i].x, brick_s2[i].y = (68+i-5) * 32 + 16, 32*6+16
for i in range(10,15): brick_s2[i].x, brick_s2[i].y = (52+i-10) * 32 + 16, 32*5+16
for i in range(15,20): brick_s2[i].x, brick_s2[i].y = (52+i-15) * 32 + 16, 32*9+16
for i in range(20,25): brick_s2[i].x, brick_s2[i].y = 57 * 32 + 16, 32*(5+i-20)+16
for i in range(25,30): brick_s2[i].x, brick_s2[i].y = 52 * 32 + 16, 32*(10+i-25)+16
for i in range(30,35): brick_s2[i].x, brick_s2[i].y = 47 * 32 + 16, 32*(10+i-30)+16
for i in range(35,40): brick_s2[i].x, brick_s2[i].y = (43+i-35) * 32 + 16, 32*5+16
for i in range(40,45): brick_s2[i].x, brick_s2[i].y = (43+i-40) * 32 + 16, 32*9+16
for i in range(45,50): brick_s2[i].x, brick_s2[i].y = 42 * 32 + 16, 32*(5+i-45)+16

block_s2=[tiles.block() for i in range(10)]
for bl in block_s2: bl.stage_index=2
block_s2[0].x,block_s2[0].y=28*32+16,32*2+16
for i in range(1,3): block_s2[i].x, block_s2[i].y = 30*32+16,32*(1+i)+16
for i in range(3,6): block_s2[i].x, block_s2[i].y = 32*32+16,32*(1+i-2)+16
for i in range(6,10): block_s2[i].x, block_s2[i].y = 34*32+16,32*(1+i-5)+16

itembox_s2 = [tiles.itembox() for i in range(5)]
for i in range(5): itembox_s2[i].x, itembox_s2[i].y = (20+i) * 32 + 16, 32*5+16

platform_s2=[tiles.platfrom() for i in range(4)]
platform_s2[0].x,platform_s2[0].y=81*32,32*5+16
platform_s2[1].x,platform_s2[1].y=83*32,32*5+16
platform_s2[2].x,platform_s2[2].y=92*32,32*5+16
platform_s2[3].x,platform_s2[3].y=94*32,32*5+16


def draw_s2():
    global ground_s2
    for g in ground_s2: g.draw()
    global brick_s2
    for br in brick_s2: br.draw()
    global block_s2
    for bl in block_s2: bl.draw()
    global platform_s2
    for pl in platform_s2: pl.draw()
    global itembox_s2
    for itm in itembox_s2: itm.draw()

#stage3
ground_s3 = [tiles.ground() for i in range(88)]
for g in ground_s3: g.stage_index = 3
for i in range(28): ground_s3[i].x, ground_s3[i].y = (i+85) * 32 + 16, 32 + 16
for i in range(28,44): ground_s3[i].x, ground_s3[i].y = (i-28) * 32 + 16, 32 + 16
for i in range(44,72): ground_s3[i].x, ground_s3[i].y = (i+85-44) * 32 + 16, 16
for i in range(72,88): ground_s3[i].x, ground_s3[i].y = (i-28-44) * 32 + 16,  16

platform_s3=[tiles.platfrom() for i in range(4)]
platform_s3[0].x,platform_s3[0].y=50*32,32*5+16
platform_s3[1].x,platform_s3[1].y=52*32,32*5+16
platform_s3[2].x,platform_s3[2].y=81*32,32*5+16
platform_s3[3].x,platform_s3[3].y=83*32,32*5+16

block_s3=[tiles.block() for i in range(11)]
for bl in block_s3: bl.stage_index=3
for i in range(5): block_s3[i].x, block_s3[i].y = 32*87+16,32*(2+i)+16
for i in range(5,11): block_s3[i].x, block_s3[i].y = 32*88+16,32*(1+i-4)+16

mushroom_s3=[tiles.mushroom() for i in range(51)]
for i in range(5): mushroom_s3[i].x, mushroom_s3[i].y = (74+i)*32,32*9+16; mushroom_s3[0].index,mushroom_s3[4].index=0,2
for i in range(5,8): mushroom_s3[i].x, mushroom_s3[i].y = (67+i-5)*32,32*6+16; mushroom_s3[5].index,mushroom_s3[7].index=0,2
for i in range(8,13): mushroom_s3[i].x, mushroom_s3[i].y = (62+i-8)*32,32*2+16; mushroom_s3[8].index,mushroom_s3[12].index=0,2
for i in range(13,18): mushroom_s3[i].x, mushroom_s3[i].y = (56+i-13)*32,32*2+16; mushroom_s3[13].index,mushroom_s3[17].index=0,2
for i in range(18,21): mushroom_s3[i].x, mushroom_s3[i].y = (58+i-18)*32,32*10+16; mushroom_s3[18].index,mushroom_s3[20].index=0,2
for i in range(21,25): mushroom_s3[i].x, mushroom_s3[i].y = (43+i-21)*32,32*2+16; mushroom_s3[21].index,mushroom_s3[24].index=0,2
for i in range(25,31): mushroom_s3[i].x, mushroom_s3[i].y = (35+i-25)*32,32*11+16; mushroom_s3[25].index,mushroom_s3[30].index=0,2
for i in range(31,36): mushroom_s3[i].x, mushroom_s3[i].y = (30+i-31)*32,32*7+16; mushroom_s3[31].index,mushroom_s3[35].index=0,2
for i in range(36,44): mushroom_s3[i].x, mushroom_s3[i].y = (19+i-36)*32,32*5+16; mushroom_s3[36].index,mushroom_s3[43].index=0,2
for i in range(44,47): mushroom_s3[i].x, mushroom_s3[i].y = (27+i-44)*32,32*2+16; mushroom_s3[44].index,mushroom_s3[46].index=0,2
for i in range(47,51): mushroom_s3[i].x, mushroom_s3[i].y = (21+i-47)*32,32*9+16; mushroom_s3[47].index,mushroom_s3[50].index=0,2

tile_s3=[tiles.tile() for i in range(163)]
for tl in tile_s3: tl.stage_index=1
for i in range(6): tile_s3[i].x, tile_s3[i].y = (20+i)*32,32*4+16
for i in range(6,12): tile_s3[i].x, tile_s3[i].y = (20+i-6)*32,32*3+16
for i in range(12,18): tile_s3[i].x, tile_s3[i].y = (20+i-12)*32,32*2+16
for i in range(18,24): tile_s3[i].x, tile_s3[i].y = (20+i-18)*32,32*1+16
for i in range(24,30): tile_s3[i].x, tile_s3[i].y = (20+i-24)*32,32*0+16
for i in range(30,32): tile_s3[i].x, tile_s3[i].y = (22+i-30)*32,32*8+16
for i in range(32,34): tile_s3[i].x, tile_s3[i].y = (22+i-32)*32,32*7+16
for i in range(34,36): tile_s3[i].x, tile_s3[i].y = (22+i-34)*32,32*6+16
for i in range(36,38): tile_s3[i].x, tile_s3[i].y = 28*32,32*(i-36)+16
for i in range(38,41): tile_s3[i].x, tile_s3[i].y = (31+i-38)*32,32*6+16
for i in range(41,44): tile_s3[i].x, tile_s3[i].y = (31+i-41)*32,32*5+16
for i in range(44,47): tile_s3[i].x, tile_s3[i].y = (31+i-44)*32,32*4+16
for i in range(47,50): tile_s3[i].x, tile_s3[i].y = (31+i-47)*32,32*3+16
for i in range(50,53): tile_s3[i].x, tile_s3[i].y = (31+i-50)*32,32*2+16
for i in range(53,56): tile_s3[i].x, tile_s3[i].y = (31+i-53)*32,32*1+16
for i in range(56,59): tile_s3[i].x, tile_s3[i].y = (31+i-56)*32,32*0+16
for i in range(63,67): tile_s3[i].x, tile_s3[i].y = (36+i-63)*32,32*10+16
for i in range(67,71): tile_s3[i].x, tile_s3[i].y = (36+i-67)*32,32*9+16
for i in range(71,75): tile_s3[i].x, tile_s3[i].y = (36+i-71)*32,32*8+16
for i in range(75,79): tile_s3[i].x, tile_s3[i].y = (36+i-75)*32,32*7+16
for i in range(79,83): tile_s3[i].x, tile_s3[i].y = (36+i-79)*32,32*6+16
for i in range(83,87): tile_s3[i].x, tile_s3[i].y = (36+i-83)*32,32*5+16
for i in range(87,91): tile_s3[i].x, tile_s3[i].y = (36+i-87)*32,32*4+16
for i in range(91,95): tile_s3[i].x, tile_s3[i].y = (36+i-91)*32,32*3+16
for i in range(95,99): tile_s3[i].x, tile_s3[i].y = (36+i-95)*32,32*2+16
for i in range(99,103): tile_s3[i].x, tile_s3[i].y = (36+i-99)*32,32*1+16
for i in range(103,107): tile_s3[i].x, tile_s3[i].y = (36+i-103)*32,32*0+16
for i in range(107,109): tile_s3[i].x, tile_s3[i].y = (44+i-107)*32,32*1+16
for i in range(109,111): tile_s3[i].x, tile_s3[i].y = (44+i-109)*32,32*0+16
for i in range(111,114): tile_s3[i].x, tile_s3[i].y = (57+i-111)*32,32*1+16
for i in range(114,117): tile_s3[i].x, tile_s3[i].y = (57+i-114)*32,32*0+16
for i in range(117,120): tile_s3[i].x, tile_s3[i].y = (63+i-117)*32,32*1+16
for i in range(120,123): tile_s3[i].x, tile_s3[i].y = (63+i-120)*32,32*0+16
for i in range(123,130): tile_s3[i].x, tile_s3[i].y = 59*32,32*(3+i-123)+16
for i in range(130,136): tile_s3[i].x, tile_s3[i].y = 68*32,32*(i-130)+16
for i in range(136,139): tile_s3[i].x, tile_s3[i].y = (75+i-136)*32,32*7+16
for i in range(139,142): tile_s3[i].x, tile_s3[i].y = (75+i-139)*32,32*6+16
for i in range(142,145): tile_s3[i].x, tile_s3[i].y = (75+i-142)*32,32*5+16
for i in range(145,148): tile_s3[i].x, tile_s3[i].y = (75+i-145)*32,32*4+16
for i in range(148,151): tile_s3[i].x, tile_s3[i].y = (75+i-148)*32,32*3+16
for i in range(151,154): tile_s3[i].x, tile_s3[i].y = (75+i-151)*32,32*2+16
for i in range(154,157): tile_s3[i].x, tile_s3[i].y = (75+i-154)*32,32*1+16
for i in range(157,160): tile_s3[i].x, tile_s3[i].y = (75+i-157)*32,32*0+16
for i in range(160,163): tile_s3[i].x, tile_s3[i].y = (75+i-160)*32,32*8+16

def draw_s3():
    global ground_s3
    for g in ground_s3: g.draw()
    global platform_s3
    for pl in platform_s3: pl.draw()
    global block_s3
    for bl in block_s3: bl.draw()
    global mushroom_s3
    for mus in mushroom_s3: mus.draw()
    global tile_s3
    for tl in tile_s3: tl.draw()



#stage4
brick_s4 = [tiles.brick() for i in range(174)]
for br in brick_s4: br.stage_index = 4
for i in range(10): brick_s4[i].x, brick_s4[i].y = i * 32 + 16, 32*3+16
for i in range(10,20): brick_s4[i].x, brick_s4[i].y = (i-10) * 32 + 16, 32*2+16
for i in range(20,30): brick_s4[i].x, brick_s4[i].y = (i-20) * 32 + 16, 32*1+16
for i in range(30,40): brick_s4[i].x, brick_s4[i].y = (i-30) * 32 + 16, 32*0+16
for i in range(40,45): brick_s4[i].x, brick_s4[i].y = (14+i-40) * 32 + 16, 32*3+16
for i in range(45,50): brick_s4[i].x, brick_s4[i].y = (14+i-45) * 32 + 16, 32*2+16
for i in range(50,55): brick_s4[i].x, brick_s4[i].y = (14+i-50) * 32 + 16, 32*1+16
for i in range(55,60): brick_s4[i].x, brick_s4[i].y = (14+i-55) * 32 + 16, 32*0+16
for i in range(60,65): brick_s4[i].x, brick_s4[i].y = (23+i-60) * 32 + 16, 32*3+16
for i in range(65,70): brick_s4[i].x, brick_s4[i].y = (23+i-65) * 32 + 16, 32*2+16
for i in range(70,75): brick_s4[i].x, brick_s4[i].y = (23+i-70) * 32 + 16, 32*1+16
for i in range(75,80): brick_s4[i].x, brick_s4[i].y = (23+i-75) * 32 + 16, 32*0+16
for i in range(80,100): brick_s4[i].x, brick_s4[i].y = (32+i-80) * 32 + 16, 32*3+16
for i in range(100,120): brick_s4[i].x, brick_s4[i].y = (56+i-100) * 32 + 16, 32*3+16
for i in range(120,125): brick_s4[i].x, brick_s4[i].y = (80+i-120) * 32 + 16, 32*3+16
for i in range(125,130): brick_s4[i].x, brick_s4[i].y = (80+i-125) * 32 + 16, 32*2+16
for i in range(130,135): brick_s4[i].x, brick_s4[i].y = (80+i-130) * 32 + 16, 32*1+16
for i in range(135,140): brick_s4[i].x, brick_s4[i].y = (80+i-135) * 32 + 16, 32*0+16
for i in range(140,145): brick_s4[i].x, brick_s4[i].y = (105+i-140) * 32 + 16, 32*3+16
for i in range(145,150): brick_s4[i].x, brick_s4[i].y = (105+i-145) * 32 + 16, 32*2+16
for i in range(150,155): brick_s4[i].x, brick_s4[i].y = (105+i-150) * 32 + 16, 32*1+16
for i in range(155,160): brick_s4[i].x, brick_s4[i].y = (105+i-155) * 32 + 16, 32*0+16
for i in range(160,163): brick_s4[i].x, brick_s4[i].y = (110+i-160) * 32 + 16, 32*3+16
for i in range(163,166): brick_s4[i].x, brick_s4[i].y = (110+i-163) * 32 + 16, 32*2+16
for i in range(166,169): brick_s4[i].x, brick_s4[i].y = (110+i-166) * 32 + 16, 32*1+16
for i in range(169,172): brick_s4[i].x, brick_s4[i].y = (110+i-169) * 32 + 16, 32*0+16
brick_s4[172].x, brick_s4[172].y =  60* 32 + 16, 32*7+16
brick_s4[173].x, brick_s4[173].y =  71* 32 + 16, 32*7+16

tile_s4=[tiles.tile() for i in range(105)]
for tl in tile_s4: tl.index=2
for i in range(105): tile_s4[i].x, tile_s4[i].y = i * 32 + 16,16

platform_s4=[tiles.platfrom() for i in range(10)]
platform_s4[0].x,platform_s4[0].y=86*32,32*3+16+8
platform_s4[1].x,platform_s4[1].y=88*32,32*3+16+8
platform_s4[2].x,platform_s4[2].y=90*32,32*3+16+8
platform_s4[3].x,platform_s4[3].y=92*32,32*3+16+8
platform_s4[4].x,platform_s4[4].y=94*32,32*3+16+8
platform_s4[5].x,platform_s4[5].y=96*32,32*3+16+8
platform_s4[6].x,platform_s4[6].y=98*32,32*3+16+8
platform_s4[7].x,platform_s4[7].y=100*32,32*3+16+8
platform_s4[8].x,platform_s4[8].y=102*32,32*3+16+8
platform_s4[9].x,platform_s4[9].y=104*32,32*3+16+8

def draw_s4():
    global tile_s4
    for tl in tile_s4: tl.draw()
    global platform_s4
    for pl in platform_s4: pl.draw()
    global brick_s4
    for br in brick_s4: br.draw()

import item
coin_s1=[item.coin() for i in range(15)]
coin_s1[0].x,coin_s1[0].y=itembox_s1[0].x,itembox_s1[0].y
coin_s1[1].x,coin_s1[1].y=itembox_s1[2].x,itembox_s1[2].y
coin_s1[2].x,coin_s1[2].y=itembox_s1[3].x,itembox_s1[3].y
for i in range(3,9):
    coin_s1[i].x, coin_s1[i].y=32*(56+i-3)+16,32*9+16
    coin_s1[i].activate=True
for i in range(9,15):
    coin_s1[i].x, coin_s1[i].y=32*(56+i-9)+16,32*1+16
    coin_s1[i].activate=True

item_s1=[item.items() for i in range(2)]
item_s1[0].x,item_s1[0].y=itembox_s1[1].x,itembox_s1[1].y
item_s1[1].x,item_s1[1].y=itembox_s1[4].x,itembox_s1[4].y

def update_s1_item():
    for co in coin_s1:
        co.update()
    if itembox_s1[0].state == 0: coin_s1[0].activate = True
    if itembox_s1[2].state == 0: coin_s1[1].activate = True
    if itembox_s1[3].state == 0: coin_s1[2].activate = True

    for itm in item_s1:
        itm.update()

    if itembox_s1[1].state == 0: item_s1[0].activate = True
    if itembox_s1[4].state == 0: item_s1[1].activate = True


def draw_s1_item():
    for co in coin_s1:
        if co.state==1:co.draw()
    for itm in item_s1:
        if itm.state>0:itm.draw()

coin_s2=[item.coin() for i in range(46)]
for i in range(4):
    coin_s2[i].x,coin_s2[i].y=itembox_s2[i].x,itembox_s2[i].y
for i in range(4,18):
    coin_s2[i].x, coin_s2[i].y = (43+i-4)*32+16,32*5+16
    coin_s2[i].activate = True
for i in range(18,32):
    coin_s2[i].x, coin_s2[i].y = (43+i-18)*32+16,32*6+16
    coin_s2[i].activate = True
for i in range(32,46):
    coin_s2[i].x, coin_s2[i].y = (43+i-32)*32+16,32*7+16
    coin_s2[i].activate = True

item_s2=item.items()
item_s2.x,item_s2.y=itembox_s2[4].x,itembox_s2[4].y

def update_s2_item():
    for co in coin_s2:
        co.update()
    for i in range(4):
        if itembox_s2[i].state == 0: coin_s2[i].activate = True

    item_s2.update()
    if itembox_s2[4].state == 0: item_s2.activate = True

def draw_s2_item():
    for co in coin_s2:
        if co.state==1:co.draw()
    if item_s2.state>0:item_s2.draw()


coin_s3=[item.coin() for i in range(11)]
for co in coin_s3:co.activate=True
coin_s3[0].x,coin_s3[0].y=32*22+16,32*5+16
coin_s3[1].x,coin_s3[1].y=32*22+16,32*9+16
coin_s3[2].x,coin_s3[2].y=32*27+32,32*2+16
coin_s3[3].x,coin_s3[3].y=32*31+32,32*7+16
coin_s3[4].x,coin_s3[4].y=32*37+16,32*11+16
coin_s3[5].x,coin_s3[5].y=32*44+16,32*2+16
coin_s3[6].x,coin_s3[6].y=32*58,32*2+16
coin_s3[7].x,coin_s3[7].y=32*64,32*2+16
coin_s3[8].x,coin_s3[8].y=32*68,32*6+16
coin_s3[9].x,coin_s3[9].y=32*59,32*10+16
coin_s3[10].x,coin_s3[10].y=32*76,32*9+16

def update_s3_item():
    for co in coin_s3:
        co.update()

def draw_s3_item():
    for co in coin_s3:
        if co.state==1:co.draw()


import enemy
gumba_s1=[enemy.gumba() for i in range(3)]
gumba_s1[0].x,gumba_s1[0].y=32*23,80
gumba_s1[1].x,gumba_s1[1].y=32*25,80
gumba_s1[2].x,gumba_s1[2].y=32*27,80
turtle_s1=enemy.turtle()
turtle_s1.x,turtle_s1.y=32*55,80

def enemy_s1_draw():
    for gum in gumba_s1:
        gum.draw()
    turtle_s1.draw()

def enemy_s1_update():
    for gum in gumba_s1:
        gum.update()

    turtle_s1.update()

gumba_s2=[enemy.gumba() for i in range(3)]
for gum in gumba_s2:
    gum.stage_index=2
gumba_s2[0].x,gumba_s2[0].y=32*50,80
gumba_s2[1].x,gumba_s2[1].y=32*52,80
gumba_s2[2].x,gumba_s2[2].y=32*54,80

turtle_s2=enemy.cave_turtle()
turtle_s2.x,turtle_s2.y=32*56,80

def enemy_s2_draw():
    for gum in gumba_s2:
        gum.draw()
    turtle_s2.draw()

def enemy_s2_update():
    for gum in gumba_s2:
        gum.update()

    turtle_s2.update()


turtle_s3=enemy.winged_turtle()
turtle_s3.x,turtle_s3.y=32*71,32*10
def enemy_s3_draw():
    turtle_s3.draw()

def enemy_s3_update():
    turtle_s3.update()


larva_s4=[enemy.larva() for i in range(3)]
larva_s4[0].x,larva_s4[0].y=32*40,0
larva_s4[1].x,larva_s4[1].y=32*44,0
larva_s4[2].x,larva_s4[2].y=32*48,0
def enemy_s4_draw():
    for la in larva_s4:
        la.draw()

def enemy_s4_update():
    for la in larva_s4:
        la.update()

