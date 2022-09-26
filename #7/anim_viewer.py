from pico2d import *
import math

open_canvas()
fire = load_image('fire4_64.png')
ghostfire = load_image('fire2_64.png')

def anim_fire():
    frame_x = 0
    frame_y = 5
    for dgr in range(-90, 540+1, 3):
        cx, cy, r = 400, 300, 200
        x = cx + r *math.cos(dgr / 360 * 2 * math.pi)
        y = cy + r *math.sin(dgr / 360 * 2 * math.pi)
        clear_canvas()

        if frame_x == 0:
            frame_y = (frame_y - 1) % 6

        fire.clip_draw(frame_x * 64, frame_y * 64, 50, 55, 400, 300)
        ghostfire.clip_draw(frame_x * 64, frame_y * 64, 50, 55, x, y/2 + 150)
        ghostfire.clip_draw(frame_x * 64, frame_y * 64, 50, 55, x/2+200, y)

        update_canvas()

        frame_x = (frame_x + 1) % 10

        delay(0.05)
        get_events()

anim_fire()


close_canvas()

