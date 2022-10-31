from pico2d import *

RD, LD, RU, LU, TIMER, A = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : A
}

table = {
    "SLEEP": {"HIT": "WAKE"},
    "WAKE": {"TIMER10":"SLEEP"}
}

#class를 이용한 스테이트 구현
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter_IDLE')
        self.dir = 0 # 정지한 상태
        self.timer = 1000
        pass
    @staticmethod
    def exit(self):
        print('exit_IDLE')
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    @staticmethod
    def enter(self, event):
        print('enter_RUN')

        #어떤 이벤트 떄문에 들어 왔는지 파악하고 그 이벤트에 대해서 dir 피드백
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        pass

    @staticmethod
    def exit(self):
        print('exit_RUN')
        #런 상태에서 나갈때 현재 방향을 저장
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        # 달리게 만들기
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0,self.x,800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
            -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
            3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        self.face_dir = self.dir

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass


next_state = {
    IDLE :{RD : RUN, LD : RUN, RU : RUN, LU: RUN, A:AUTO_RUN },
    RUN : {RD : IDLE, LD : IDLE, RU : IDLE, LU : IDLE, A:AUTO_RUN},
    SLEEP : {RD : RUN, LD : RUN, RU : RUN, LU : RUN},
    AUTO_RUN : {RD : RUN, LD : RUN, RU : RUN, LU : RUN}
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if (self.q):
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.q.insert(0,event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # if event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
        pass

