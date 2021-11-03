import turtle as t
import random as r

t.speed(0)
t.color('red')


def move_broun():
    for i in range(100):
        distance = r.randint(1, 50)
        angle = r.randint(-180, 180)
        t.forward(distance)
        t.right(angle)


move_broun()
