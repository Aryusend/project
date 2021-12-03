from pico2d import *
#title
image_title_background=None
image_title_cusor=None
#stage
image_show_life=None
image_show_score=None
image_numbers=None
image_castle=None
image_flag=None
image_flagstick=None
#stage1
image_stage1_sky=None
image_stage1_ground=None
image_stage1_itembox=None
image_stage1_brick=None
image_stage1_pipe=None
#stage2
image_stage2_ground=None
image_stage2_itembox=None
image_stage2_brick=None
image_stage2_pipe=None
#stage3
image_stage3_ground=None
image_stage3_itembox=None
image_stage3_brick=None
image_stage3_pipe=None
#stage4
image_stage4_ground=None
image_stage4_itembox=None
image_stage4_brick=None
image_stage4_pipe=None
#enemy
image_gumba=None
image_turtle=None
image_flower_enemy=None
image_boss=None
#image
image_mushroom=None
image_flower=None
image_star=None
#mario
image_small_mario=None
image_big_mario=None
image_fire_mario=None
image_fireball_mario=None


def load_all_image():
    title_image = load_image('title.png')
    title_cusor = load_image('cusor.png')
