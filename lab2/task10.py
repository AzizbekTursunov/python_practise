import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)


def draw_one_round1():
    for i in range(180):
        t.left(2)
        t.forward(3)


def draw_one_round2():
    for i in range(180):
        t.right(2)
        t.forward(3)


def flower():
    for i in range(3):
        draw_one_round1()
        draw_one_round2()
        t.left(60)


flower()
