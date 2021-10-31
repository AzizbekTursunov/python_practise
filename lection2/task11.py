import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.left(90)


def draw_one_round1(step):
    for i in range(180):
        t.left(2)
        t.forward(step)


def draw_one_round2(step):
    for i in range(180):
        t.right(2)
        t.forward(step)


def draw_babochka():
    step = 1
    for i in range(8):
        draw_one_round1(step)
        draw_one_round2(step)
        step = step + 0.2


draw_babochka()
