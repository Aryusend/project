from pico2d import *
import server

#images
#font & background
image_font=None
image_numbers=None
image_lobby=None
image_title=None
image_background_blue=None
image_background_black=None
#maps
image_stage1_map=None
image_stage2_map=None
image_stage3_map=None
image_stage4_map=None

#blocks
image_tiles=None
image_tiles2=None
image_pipes=None
image_flagstick=None
image_flag=None
image_castle=None
#mario
image_mario_small=None
image_mario_big=None
image_mario_fire=None
image_fire=None
#item
image_coin=None
image_mushroom=None
image_flower=None
#enemy
image_enemy=None

def load_all_image():
    global image_font,image_numbers,image_lobby,image_title,image_background_blue,image_background_black
    image_font = load_image('font.png')
    image_numbers = load_image('numbers.png')
    image_lobby = load_image('lobby.png')
    image_title = load_image('title.png')
    image_background_blue = load_image('background_blue.png')
    image_background_black = load_image('background_black.png')

    global image_stage1_map,image_stage2_map,image_stage3_map,image_stage4_map
    image_stage1_map = load_image('stage1_map.png')
    image_stage2_map = load_image('stage2_map.png')
    image_stage3_map = load_image('stage3_map.png')
    image_stage4_map = load_image('stage4_map.png')

    global image_tiles, image_tiles2,image_pipes,image_flagstick,image_flag,image_castle
    image_tiles = load_image('tiles.png')
    image_tiles2 = load_image('tiles2.png')
    image_pipes = load_image('pipes.png')
    image_flagstick = load_image('flagstick.png')
    image_flag = load_image('flag.png')
    image_castle = load_image('castle.png')

    global image_mario_small,image_mario_big,image_mario_fire
    image_mario_small = load_image('mario_small.png')
    image_mario_big = load_image('mario_big.png')
    image_mario_fire = load_image('mario_fire.png')

    global image_coin,image_mushroom,image_flower
    image_coin= load_image('coin.png')
    image_mushroom= load_image('mushroom.png')
    image_flower= load_image('flower.png')

    global image_fire
    image_fire= load_image('fireballs.png')

    global image_enemy
    image_enemy=load_image('enemy.png')


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
        if char[i] == 'k': image_font.clip_draw(32 * 0, 32 * 2, 32, 32, x + 32 * i, y)
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

def show_score(x,y):
    global image_numbers
    image_numbers.clip_draw(int(server.total_score / 1000) * 32, 0, 32, 32, x + 32 * 0, y)
    image_numbers.clip_draw(int(server.total_score % 1000 / 100) * 32, 0, 32, 32, x + 32 * 1, y)
    image_numbers.clip_draw(int(server.total_score % 100 / 10) * 32, 0, 32, 32, x + 32 * 2, y)
    image_numbers.clip_draw(int(server.total_score % 10) * 32, 0, 32, 32, x + 32 * 3, y)

def show_timeleft(x,y):
    global image_font,image_numbers
    image_font.clip_draw(32, 0, 32, 32, x-30, y)
    image_numbers.clip_draw(int(server.time_left / 100) * 32, 0, 32, 32, x, y)
    image_numbers.clip_draw(int(server.time_left % 100 / 10) * 32, 0, 32, 32, x + 32, y)
    image_numbers.clip_draw(int(server.time_left % 10) * 32, 0, 32, 32, x + 64, y)

def show_life(x,y):
    global image_font
    image_font.clip_draw(32 * 5, 0, 48, 32, x, y)
    image_font.clip_draw(32 * 4, 0, 32, 32, x+48, y)
    image_numbers.clip_draw(server.number_of_life * 32, 0, 32, 32, x+80, y)