import turtle as t

t.shape('turtle')
t.color('blue')
t.width(2)
t.penup()
t.goto(-300, 0)
t.pendown()


def draw_zero():
    for a in (80, 160, 80, 160):
        t.forward(a)
        t.right(90)


def draw_one():
    t.left(45)
    for a in (80 * 2 ** 0.5, 160):
        t.forward(a)
        t.right(135)
    t.left(135)


def draw_four():
    for i in range(3):
        t.forward(80)
        t.left(90)
    t.left(90)
    t.forward(160)


def draw_seven():
    t.forward(80)
    t.right(135)
    t.forward(80 * 2 ** 0.5)
    t.left(45)
    t.forward(80)


def move_do_not_draw_to_draw_index2():
    t.penup()
    t.goto(-180, 80)
    t.pendown()


def move_do_not_draw_to_draw_index3():
    t.penup()
    t.goto(-60, 0)
    t.left(90)
    t.pendown()


def move_do_not_draw_to_draw_index4():
    t.penup()
    t.goto(60, 80)
    t.left(90)
    t.pendown()


def move_do_not_draw_to_draw_index5():
    t.penup()
    t.goto(180, 80)
    t.left(90)
    t.pendown()


def move_do_not_draw_to_draw_index6():
    t.penup()
    t.goto(300, 80)
    t.pendown()


def draw_index_with_141700():
    draw_one()
    move_do_not_draw_to_draw_index2()
    draw_four()
    move_do_not_draw_to_draw_index3()
    draw_one()
    move_do_not_draw_to_draw_index4()
    draw_seven()
    move_do_not_draw_to_draw_index5()
    draw_zero()
    move_do_not_draw_to_draw_index6()
    draw_zero()


draw_index_with_141700()
t.hideturtle()
