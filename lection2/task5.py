import turtle
t = turtle.Turtle()
t.shape('turtle')
def draw_square(x):
    for line in range(4):
        t.forward(x)
        t.left(90)
def transition_do_not_draw():
    t.penup()
    t.right(135)
    t.forward(10 * (2 ** 0.5))
    t.left(135)
    t.pendown()
def draw_10_squares():
    x = 20
    for i in range(10):
        square(x)
        transition_do_not_draw()
        x += 20
draw_10_squares()