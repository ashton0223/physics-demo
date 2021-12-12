import time
from math import sqrt
import pygame
from pygame.locals import *

WIDTH    =   640
HEIGHT   =   400
CENTER   =   (WIDTH / 2, HEIGHT / 2)
ACC      =   -9.8
BLUE     =   (0, 0, 255)
ADD_BALL =   pygame.USEREVENT + 1

class Demo:
    def __init__(self):
        self._display_surf = None
        self.size = self.weight, self.height = WIDTH, HEIGHT

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            pygame.quit()
        if event.type == ADD_BALL:
            pygame.draw.circle(self._display_surf, BLUE, CENTER, 20)
            pygame.display.update()

    def start(self):
        if self.on_init() == False:
            self._running = False

    def begin_loop(self):
        while(True):
            for event in pygame.event.get():
                self.on_event(event)


    def add_ball(self, x, y):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.circle(self._display_surf, BLUE, (x, y), 20)
        pygame.display.update()
        for event in pygame.event.get():
            self.on_event(event)

def get_elapsed_time(start):
    return (time.process_time() - start) * 5

def get_final_v(v0, a, deltay):
    return sqrt((v0 ** 2) + 2 * a * deltay)

if __name__ == "__main__":
    demo = Demo()
    demo.start()

    radius = 20
    start_time = time.process_time()
    v0 = 0
    finaly = -CENTER[1] + radius
    rebound_v = get_final_v(v0, ACC, finaly)
    begin = CENTER[1]

    while True:
        # Wonderful kinematic equation
        deltay = (v0 * get_elapsed_time(start_time)) + ((1/2) * (ACC) * (get_elapsed_time(start_time) ** 2))
        if (deltay <= finaly):
            v0 = rebound_v
            deltay = finaly

            # So the ball doesn't fall through the floor
            begin = HEIGHT - radius
            finaly = 0

            # Don't just keep falling
            start_time = time.process_time()

        demo.add_ball(CENTER[0], begin - deltay)