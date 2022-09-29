from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
pose = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if dir_x == 1:
        character.clip_draw(frame * 100, pose, 100, 100, x, y)
        pose = 100
    elif dir_y == 1:
        character.clip_draw(frame * 100, pose, 100, 100, x, y)
    elif dir_x == -1:
        character.clip_draw(frame * 100, pose, 100, 100, x, y)
        pose = 0
    elif dir_y == -1:
        character.clip_draw(frame * 100, pose, 100, 100, x, y)
    elif dir_x == 0 and dir_y == 0:
        pose += 200
        character.clip_draw(frame * 100, pose, 100, 100, x, y)
        pose -= 200
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x + 10 <= KPU_WIDTH  and x - 10 >= 0 + 20:
        x += dir_x * 10
    elif x + 10 > KPU_WIDTH:
        x -= 10
    elif x - 10 < 0 + 20:
        x += 10
    if y + 20 <= KPU_HEIGHT - 20 and y - 20 >= 0 + 20:
        y += dir_y * 10
    elif y + 20 > KPU_HEIGHT - 20 :
        y -= 10
    elif y - 20 < 0 + 20:
        y += 10

    delay(0.01)

close_canvas()

