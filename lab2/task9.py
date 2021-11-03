import turtle
import numpy as np

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.penup()
t.forward(50)
t.pendown()
R = 20


def alfa(i):
    angle = 90 + (90 - (180 * (i - 2)) / (2 * i))
    return angle


def line_polygon(i):
    return R * (2 * np.sin((2 * np.pi) / (2 * i)))


def draw_i_regular_polygons(i, x):
    for line in range(i):
        t.forward(x)
        t.left(360 / i)


def move_do_not_draw(i):
    t.right(alfa(i))
    t.penup()
    t.forward(10)
    t.pendown()


def draw_10_regular_polygons():
    global R
    for i in range(3, 13):
        t.left(alfa(i))
        x = line_polygon(i)
        draw_i_regular_polygons(i, x)
        R += 10.5
        move_do_not_draw(i)


draw_10_regular_polygons()
