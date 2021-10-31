import turtle

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')
t.left(90)


def big_arc():
    for i in range(90):
        t.right(2)
        t.forward(2)


def small_arc():
    for i in range(90):
        t.right(2)
        t.forward(0.25)


def spring():
    for i in range(3):
        big_arc()
        small_arc()


spring()
