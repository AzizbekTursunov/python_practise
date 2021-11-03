import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(10)


def move_back_do_not_draw():
    t.penup()
    t.left(180)
    t.forward(100)
    t.right(180)
    t.pendown()


for i in range(12):
    t.right(30)
    t.forward(100)
    t.stamp()
    move_back_do_not_draw()
