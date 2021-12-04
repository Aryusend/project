import pico2d
import framework
import server
import title

pico2d.open_canvas(800, 600)
server.load_all_image()
framework.run(title)
pico2d.close_canvas()