import pico2d
import framework
import image
import sound
import title

pico2d.open_canvas(800, 600)
image.load_all_image()
sound.load_sound()
framework.run(title)
pico2d.close_canvas()