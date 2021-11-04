import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 30
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
    global Number_all_balls
    Number_all_balls += 1
    color = random.choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
    x, y = [random.randint(70, 920), random.randint(70, 620)]
    radius_ball = random.randint(30, 50)
    speed_ball_axis_x = random.choice([-4, -3, -2, -1.5, 1.5, 2, 3, 4])
    speed_ball_axis_y = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    circle(sc, color, [x, y], radius_ball)
    return [color, [x, y], radius_ball, speed_ball_axis_x, speed_ball_axis_y]


def move_ball(list_parametr_of_new_ball):
    circle(sc, list_parametr_of_new_ball[0], list_parametr_of_new_ball[1], list_parametr_of_new_ball[2])
    if list_parametr_of_new_ball[1][0] >= 1000 - list_parametr_of_new_ball[2] or list_parametr_of_new_ball[1][0] <= \
            list_parametr_of_new_ball[2]:
        list_parametr_of_new_ball[3] = -list_parametr_of_new_ball[3]
    if list_parametr_of_new_ball[1][1] >= 700 - list_parametr_of_new_ball[2] or list_parametr_of_new_ball[1][1] <= \
            list_parametr_of_new_ball[2]:
        list_parametr_of_new_ball[4] = -list_parametr_of_new_ball[4]
    list_parametr_of_new_ball[1][0] += list_parametr_of_new_ball[3]
    list_parametr_of_new_ball[1][1] += list_parametr_of_new_ball[4]


def click(event, list_parametr_of_new_ball):
    global Your_score, wrong_clicks, hit_the_target
    ax = (list_parametr_of_new_ball[1][0] - event.pos[0]) ** 2
    by = (list_parametr_of_new_ball[1][1] - event.pos[1]) ** 2
    distance = (ax + by) ** 0.5  # distance between mouse and ball center
    if distance <= list_parametr_of_new_ball[2]:
        Your_score += 1
    else:
        wrong_clicks += 1
    print('Your_score : ', Your_score,
          'Number wrong clicks : ', wrong_clicks)


# end body programm

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
# main loop
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, list_parametr_of_new_ball)
    clock.tick(FPS)
    if n % 50 == 0:
        list_parametr_of_new_ball = new_ball()
    else:
        move_ball(list_parametr_of_new_ball)
    n += 1
    pygame.display.update()
    sc.fill('lightgrey')

print('Number_all_balls : ', Number_all_balls, 'Total score : ', Your_score)
pygame.quit()
