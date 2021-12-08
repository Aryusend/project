from pico2d import *

sound_die=None
sound_coin=None
clear=None
jump=None
item=None
stage1=None
stage2=None
stage3=None
stage4=None
def load_sound():
    global sound_die
    sound_die = load_music('mariodie.mp3')
    global sound_coin
    sound_coin=load_music('mariocoin.mp3')
    global clear
    clear=load_music('marioclear.mp3')
    global jump
    jump=load_music('jump.mp3')
    global item
    item=load_music('item.mp3')
    global stage1,stage2,stage3,stage4
    stage1=load_music('stage1.mp3')
    stage2 = load_music('stage2.mp3')
    stage3 = load_music('stage3.mp3')
    stage4 = load_music('stage4.mp3')
