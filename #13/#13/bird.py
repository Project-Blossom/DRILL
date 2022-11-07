from pico2d import *

import game_framework
import game_world
from ball import Ball
import random
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#2 : 상태의 정의

class FLY:
    def enter(self, event):
        print('ENTER RUN')
        # if event == RD:
        #     self.dir += 1
        # elif event == LD:
        #     self.dir -= 1
        # elif event == RU:
        #     self.dir -= 1
        # elif event == LU:
        #     self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if(int(self.frame) == 0):
            self.frame_pg = (self.frame_pg + 1) % 3
        if(int(self.frame) == 4 and self.frame_pg == 2):
            self.frame = 0
            self.frame_pg = 0

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if(self.x > 1600):
            self.x = 1600
            self.dir = -1
        elif(self.x < 0):
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame)*185, 170*self.frame_pg, 185, 170,0, 'h', self.x, self.y, 185, 170)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*185, 170*self.frame_pg, 185, 170, self.x, self.y)



class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(300, 500)
        self.frame = random.randint(0,5)
        self.frame_pg = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')
        self.timer = 100

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

