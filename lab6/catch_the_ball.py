import pygame
from pygame.draw import *
import random
import time

pygame.init()

FPS = 1
sc = pygame.display.set_mode((1000, 700))
sc.fill('lightgrey')

# start body programm
# colors, witch to use to paint balls
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

Your_score = 0
Number_all_balls = 0
wrong_clicks = 0


def new_ball():
    global x, y, radius_ball, Number_all_balls, cordinate_ball
    Number_all_balls += 1
    color = random.choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
    x, y = [random.randint(50, 950), random.randint(50, 650)]
    cordinate_ball = [x, y]
    radius_ball = random.randint(20, 100)
    for i in range(100):
        ball = circle(sc, color,  cordinate_ball, radius_ball)
        cordinate_ball[0] += 5
        cordinate_ball[1] += 0
        pygame.display.update()
        time.sleep(0.05)
        sc.fill('lightgray')

def move_ball():
    pass


def click(event):
    global Your_score, wrong_clicks, cordinate_ball
    distance = ((cordinate_ball[0] - event.pos[0]) ** 2 + (cordinate_ball[1] - event.pos[1]) ** 2) ** 0.5  # distance between mouse and ball center
    print(cordinate_ball)
    if distance <= radius_ball:
        Your_score += 1
    else:
        wrong_clicks += 1
    print('Your_score : ',  Your_score,
          'Number wrong clicks : ', wrong_clicks)


# end body programm

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    pygame.display.update()
    sc.fill('lightgrey')

print('Number_all_balls : ', Number_all_balls)
pygame.quit()
