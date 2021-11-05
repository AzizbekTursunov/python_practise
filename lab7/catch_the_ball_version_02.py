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
# Counters
Your_score = 0
Number_all_balls = 0
Number_all_Squares = 0


def new_ball():
    """
    This function must created (only parametrs) one new ball
    :return: the function must return list with elements:
    color ball
    coordinate ball(axis x and axis y) '[x, y]'
    radius ball
    speed ball on axis x
    speed ball on axis y
    """
    global Number_all_balls
    Number_all_balls += 1
    color = random.choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
    x, y = [random.randint(70, 920), random.randint(70, 620)]
    radius_ball = random.randint(30, 50)
    speed_ball_axis_x = random.choice([-4, -3, -2, -1.5, 1.5, 2, 3, 4])
    speed_ball_axis_y = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    # circle(sc, color, [x, y], radius_ball) This function does not have to show us the ball on the screen.
    # We only need the parameters of the new_ball
    return [color, [x, y], radius_ball, speed_ball_axis_x, speed_ball_axis_y]


def new_square():
    """
    This function must created (only parametrs) one new square
    :return: the function must return list with elements:
    color square
    coordinates of the top-left corner of the square(axis x and axis y) '[x, y]'
    width and height square h
    speed square on axis x
    speed square on axis y
    """
    global Number_all_Squares
    Number_all_Squares += 1
    color_sqr = random.choice([RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN])
    x, y = [random.randint(70, 920), random.randint(70, 620)]
    h = random.randint(30, 50)
    speed_square_axis_x = random.choice([-4, -3, -2, -1.5, 1.5, 2, 3, 4])
    speed_square_axis_y = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    rect(sc, color_sqr, [x, y, h, h])
    return [color_sqr, [x, y, h, h], speed_square_axis_x, speed_square_axis_y]


def move_ball(list_parametr_of_new_ball):
    """
    In this function is written move law of the ball. This function changes list 'list_parametr_of_new_ball'.
    :param list_parametr_of_new_ball: function 'new_ball()' returned this list, then function move_ball taked this list
    :return: None
    """
    circle(sc, list_parametr_of_new_ball[0], list_parametr_of_new_ball[1], list_parametr_of_new_ball[2])
    if list_parametr_of_new_ball[1][0] >= 1000 - list_parametr_of_new_ball[2] or list_parametr_of_new_ball[1][0] <= \
            list_parametr_of_new_ball[2]:
        list_parametr_of_new_ball[3] = -list_parametr_of_new_ball[3]
    if list_parametr_of_new_ball[1][1] >= 700 - list_parametr_of_new_ball[2] or list_parametr_of_new_ball[1][1] <= \
            list_parametr_of_new_ball[2]:
        list_parametr_of_new_ball[4] = -list_parametr_of_new_ball[4]
    list_parametr_of_new_ball[1][0] += list_parametr_of_new_ball[3]
    list_parametr_of_new_ball[1][1] += list_parametr_of_new_ball[4]


def move_square(list_parametr_of_new_square):
    """
    In this function is written move law of the square. This function changes list 'list_parametr_of_new_square'.
    :param list_parametr_of_new_square: function 'new_square()' returned this list, then function move_square taked
    this list list_parametr_of_new_square = [color_sqr, [x, y, h, h], speed_square_axis_x, speed_square_axis_y]
    :return: None
    """
    rect(sc, list_parametr_of_new_square[0], list_parametr_of_new_square[1])
    if list_parametr_of_new_square[1][0] >= 1000 - list_parametr_of_new_square[1][2] or list_parametr_of_new_square[1][
        0] <= 0:
        list_parametr_of_new_square[2] = -list_parametr_of_new_square[2]
    if list_parametr_of_new_square[1][1] >= 700 - list_parametr_of_new_square[1][2] or list_parametr_of_new_square[1][
        1] <= 0:
        list_parametr_of_new_square[3] = -list_parametr_of_new_square[3]
    list_parametr_of_new_square[1][0] += list_parametr_of_new_square[2]
    list_parametr_of_new_square[1][1] += list_parametr_of_new_square[3]


def click(event, list_parametr_of_new_ball):
    """
    This function checked, you are hit the ball or not
    :param event: All events in 'pygame.event.get()'
    :param list_parametr_of_new_ball:  function 'new_ball()' returned this list, then function click taked this list
    :return: the varrable 'hit_the_target'. If we hit any ball, then ball to be hidden.
    This varriable must to do that.
    """
    global Your_score
    ax = (list_parametr_of_new_ball[1][0] - event.pos[0]) ** 2
    by = (list_parametr_of_new_ball[1][1] - event.pos[1]) ** 2
    distance = (ax + by) ** 0.5  # distance between mouse and ball center
    hit_the_target = False
    if distance <= list_parametr_of_new_ball[2]:
        Your_score += 1
        hit_the_target = True
    return hit_the_target


def click_target_2(event):
    global Your_score
    if (list_parametr_of_new_square[1][0] <= event.pos[0]) and (
            (list_parametr_of_new_square[1][0] + list_parametr_of_new_square[1][2]) >= event.pos[0]) and (
            list_parametr_of_new_square[1][1] <= event.pos[1]) and (
            (list_parametr_of_new_square[1][1] + list_parametr_of_new_square[1][2]) >= event.pos[1]):
        print('You hit the square')
        Your_score += 1
    else:
        print('try again')


# end body programm

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
# main loop. All functions are called here.
hit_the_target_list = [False, False, False, False]  # If we hit any ball, then ball to be hidden.
# This varriable must to do that.
hit_the_target2 = [False]  # If we hit any square, then ball to be hidden.
# This varriable must to do that.
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hit_the_target_list[0] = click(event, list_parametr_of_new_ball_1)
            hit_the_target_list[1] = click(event, list_parametr_of_new_ball_2)
            hit_the_target_list[2] = click(event, list_parametr_of_new_ball_3)
            hit_the_target_list[3] = click(event, list_parametr_of_new_ball_4)
            click_target_2(event)
    if n % 50 == 0:
        list_parametr_of_new_ball_1 = new_ball()
        list_parametr_of_new_ball_2 = new_ball()
        list_parametr_of_new_ball_3 = new_ball()
        list_parametr_of_new_ball_4 = new_ball()
        list_parametr_of_new_square = new_square()
    if not hit_the_target_list[0]:
        move_ball(list_parametr_of_new_ball_1)
    if not hit_the_target_list[1]:
        move_ball(list_parametr_of_new_ball_2)
    if not hit_the_target_list[2]:
        move_ball(list_parametr_of_new_ball_3)
    if not hit_the_target_list[3]:
        move_ball(list_parametr_of_new_ball_4)
    if not hit_the_target2[0]:
        move_square(list_parametr_of_new_square)
    n += 1
    pygame.display.update()
    sc.fill('lightgray')
print('Number_all_balls :', Number_all_balls, 'Number_all_Squares :', Number_all_Squares, 'Total score :', Your_score)
pygame.quit()
