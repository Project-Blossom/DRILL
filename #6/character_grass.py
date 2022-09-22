from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 0
r = -5
while (True):
    
    
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90+y)
        x = x+5
        delay(0.01)
    
    while(y<510):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90+y)
        y=y+5
        delay(0.01)
    
    while (x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90+y)
        x = x-5
        delay(0.01)
        
    while(y>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90+y)
        y=y-5
        delay(0.01)

    while (x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90+y)
        x = x+5
        delay(0.01)
        
     
    while(r<8):

            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+math.cos(r)*270,300+math.sin(r)*270)
            r = r+0.05
            delay(0.01)
        

close_canvas()
