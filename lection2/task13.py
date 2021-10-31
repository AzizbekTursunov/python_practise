import turtle

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')


def right_eye():
    t.begin_fill()
    t.color('black', 'blue')
    for i in range(180):
        t.left(2)
        t.forward(0.7)
    t.end_fill()


def left_eye():
    t.begin_fill()
    t.color('black', 'blue')
    for i in range(180):
        t.left(2)
        t.forward(0.7)
    t.end_fill()


def draw_nose():
    t.penup()
    t.goto(0.0, 120)
    t.right(90)
    t.pendown()
    t.width(10)
    t.forward(30)


def draw_mouth():
    t.color('red')
    t.width(10)
    for i in range(90):
        t.right(2)
        t.forward(2.1)


def draw_head_smile():
    t.begin_fill()
    t.color('black', 'yellow')
    for i in range(180):
        t.left(2)
        t.forward(4)
    t.end_fill()


def draw_eyes():
    right_eye()
    t.penup()
    t.goto(-49, 150)
    t.pendown()
    left_eye()


def move_do_not_draw_for_to_draw_eyes():
    t.pendown()
    draw_eyes()
    draw_nose()
    t.penup()


def draw_smile():
    draw_head_smile()
    t.penup()
    t.goto(49, 150)
    move_do_not_draw_for_to_draw_eyes()
    t.goto(60, 92)
    t.pendown()
    draw_mouth()


draw_smile()
t.hideturtle()
