import pico2d
import framework
import game_state

import mario
import blocks

pico2d.open_canvas(800, 600)
framework.run(game_state)
pico2d.close_canvas()