from pico2d import *
import mario
import blocks
import item

#images
#font & background
image_font=None
image_numbers=None
image_lobby=None
image_title=None
image_background_blue=None
image_background_black=None
#maps
image_stage2_map=None
#blocks
image_tiles=None
image_pipes=None
image_flagstick=None
image_flag=None
image_castle=None
#mario
image_mario_small=None
image_mario_big=None
image_mario_fire=None
#item
image_mushroom=None
image_star=None
image_flower=None
image_coin=None
#enemy
image_gumba=None

def load_all_image():
    global image_font,image_numbers,image_lobby,image_title,image_background_blue,image_background_black,\
        image_stage2_map,image_tiles,image_pipes,image_flagstick,image_flag,image_castle,\
        image_mario_small,image_mario_big,image_mario_fire,\
        image_mushroom,image_star,image_flower,image_coin,image_gumba

    # font & background
    image_font = load_image('font.png')
    image_numbers = load_image('numbers.png')
    image_lobby = load_image('lobby.png')
    image_title = load_image('title.png')
    image_background_blue = load_image('background_blue.png')
    image_background_black = load_image('background_black.png')
    # maps
    image_stage2_map = load_image('stage2_map.png')
    # blocks
    image_tiles = load_image('tiles.png')
    image_pipes = load_image('pipes.png')
    image_flagstick = load_image('flagstick.png')
    image_flag = load_image('flag.png')
    image_castle = load_image('castle.png')
    # mario
    image_mario_small = load_image('mario_small.png')
    image_mario_big = load_image('mario_big.png')
    image_mario_fire = load_image('mario_fire.png')
    # item
    image_mushroom = load_image('mushroom.png')
    image_star = load_image('flower.png')
    image_flower = load_image('flower.png')
    image_coin = load_image('coin.png')
    # enemy
    image_gumba = load_image('gumba.png')


def write_letter(char,x,y):
    global image_font
    n=len(char)
    for i in range(n):
        if char[i] == 'a': image_font.clip_draw(32 * 0, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'b': image_font.clip_draw(32 * 1, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'c': image_font.clip_draw(32 * 2, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'd': image_font.clip_draw(32 * 3, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'e': image_font.clip_draw(32 * 4, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'f': image_font.clip_draw(32 * 5, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'g': image_font.clip_draw(32 * 6, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'h': image_font.clip_draw(32 * 7, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'i': image_font.clip_draw(32 * 8, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'j': image_font.clip_draw(32 * 9, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'k': image_font.clip_draw(32 * 0, 32 * 3, 32, 32, x + 32 * i, y)
        if char[i] == 'l': image_font.clip_draw(32 * 1, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'm': image_font.clip_draw(32 * 2, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'n': image_font.clip_draw(32 * 3, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'o': image_font.clip_draw(32 * 4, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'p': image_font.clip_draw(32 * 5, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'q': image_font.clip_draw(32 * 6, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'r': image_font.clip_draw(32 * 7, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 's': image_font.clip_draw(32 * 8, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 't': image_font.clip_draw(32 * 9, 32 * 2, 32, 32, x + 32 * i, y)
        if char[i] == 'u': image_font.clip_draw(32 * 0, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == 'v': image_font.clip_draw(32 * 1, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == 'w': image_font.clip_draw(32 * 2, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == 'x': image_font.clip_draw(32 * 3, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == 'y': image_font.clip_draw(32 * 4, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == 'z': image_font.clip_draw(32 * 5, 32 * 1, 32, 32, x + 32 * i, y)
        if char[i] == ' ': image_font.clip_draw(32 * 6, 32 * 1, 32, 32, x + 32 * i, y)

#object
player=mario.Mario()

#variables
stage_opened=1
stage_selected=1
number_of_life=3
total_score=0
coin_earned=0

#------------------set Stage1----------------------------
#ground
ground_stage1=[blocks.ground() for i in range(255)]
for i in range(120): ground_stage1[i].x, ground_stage1[i].y = i * 32, 48
for i in range(120, 240):ground_stage1[i].x, ground_stage1[i].y = ground_stage1[i - 120].x, 16
for i in range(240, 255):ground_stage1[i].id=2
for i in range(240, 245):ground_stage1[i].x, ground_stage1[i].y = 32*(80+i-241),32*2+16
for i in range(245, 249):ground_stage1[i].x, ground_stage1[i].y = 32*(81+i-246),32*3+16
for i in range(249, 252):ground_stage1[i].x, ground_stage1[i].y = 32*(82+i-250),32*4+16
for i in range(252, 254):ground_stage1[i].x, ground_stage1[i].y = 32*(83+i-253),32*5+16
ground_stage1[254].x, ground_stage1[254].y = 32*83,32*6+16
#brick
bricks_stage1 = [blocks.brick() for i in range(11)]
bricks_stage1[0].x, bricks_stage1[0].y = 32 * 17, 32 * 5
bricks_stage1[1].x, bricks_stage1[1].y = 32 * 19, 32 * 5
bricks_stage1[2].x, bricks_stage1[2].y = 32 * 21, 32 * 5
bricks_stage1[3].x, bricks_stage1[3].y = 32 * 46, 32 * 5
bricks_stage1[4].x, bricks_stage1[4].y = 32 * 48, 32 * 5
bricks_stage1[5].x, bricks_stage1[5].y = 32 * 50, 32 * 9
bricks_stage1[6].x, bricks_stage1[6].y = 32 * 51, 32 * 9
bricks_stage1[7].x, bricks_stage1[7].y = 32 * 52, 32 * 9
bricks_stage1[8].x, bricks_stage1[8].y = 32 * 53, 32 * 9
bricks_stage1[9].x, bricks_stage1[9].y = 32 * 54, 32 * 9
bricks_stage1[10].x, bricks_stage1[10].y = 32 * 55, 32 * 9
#itembox
itemboxs_stage1 = [blocks.itembox() for i in range(5)]
itemboxs_stage1[0].x, itemboxs_stage1[0].y = 32 * 14, 32 * 5
itemboxs_stage1[1].x, itemboxs_stage1[1].y = 32 * 18, 32 * 5
itemboxs_stage1[2].x, itemboxs_stage1[2].y = 32 * 20, 32 * 5
itemboxs_stage1[3].x, itemboxs_stage1[3].y = 32 * 19, 32 * 9
itemboxs_stage1[4].x, itemboxs_stage1[4].y = 32 * 47, 32 * 5
pipe_stage1 = [blocks.pipe() for i in range(4)]
pipe_stage1[0].x,pipe_stage1[0].y= 32 * 30, 32 * 3
pipe_stage1[1].x, pipe_stage1[1].y = 32 * 40, 32 * 3
pipe_stage1[2].x, pipe_stage1[2].y = 32 * 60, 32 * 3
pipe_stage1[3].x, pipe_stage1[3].y = 32 * 70, 32 * 3
def draw_stage1():
    for g in ground_stage1:g.draw()
    for i in itemboxs_stage1: i.draw()
    for b in bricks_stage1: b.draw()
    for p in pipe_stage1: p.draw()
def update_stage1():
    for i in itemboxs_stage1: i.update()

coins_stage1=[item.coin() for i in range(12)]
for i in range(6): coins_stage1[i].x,coins_stage1[i].y,coins_stage1[i].activate=32 * (50+i), 32 * 9,True
for i in range(6,12):coins_stage1[i].x,coins_stage1[i].y,coins_stage1[i].activate=32 * (50+i-6), 32 * 1+16,True
mushroom_stage1=item.mushroom()
mushroom_stage1.x,mushroom_stage1.y=itemboxs_stage1[1].x,itemboxs_stage1[1].y


def draw_item1():
    for c in coins_stage1:
        if c.activate==True: c.draw()
    if mushroom_stage1.state==1:mushroom_stage1.draw()
def update_item1():
    for c in coins_stage1: c.update()
    mushroom_stage1.update()

    if itemboxs_stage1[1].state==0:
        mushroom_stage1.activate=True
#=======================================================
