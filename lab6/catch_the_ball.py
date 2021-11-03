import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 2
sc = pygame.display.set_mode((1000, 700))
sc.fill('lightgrey')

# start body programm

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    color = random.choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
    x, y = [random.randint(50, 950), random.randint(50, 650)]
    cordinate_ball = (x, y)
    radius_ball = random.randint(20, 100)
    circle(sc, color, cordinate_ball, radius_ball)


# end body programm

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            finished = True

    new_ball()
    pygame.display.update()
    sc.fill('lightgrey')

pygame.quit()
