import turtle

t = turtle.Turtle()
t.penup()
t.forward(150)
t.pendown()


def draw_star():
    for i in range(5):
        t.forward(400)
        t.left(144)


draw_star()
t.penup()
t.back(500)
t.pendown()


def draw_11star():
    for i in range(11):
        t.forward(400)
        t.left(163.6)


draw_11star()
