import turtle
import random

window = turtle.Screen()


def draw_container():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.up()
    t.goto(300, 300)
    t.down()
    t.width(10)
    for i in range(4):
        t.right(90)
        t.forward(600)


draw_container()
number_molekule = 2
gas_molekule_list = []

def create_gas_molekule():
    for i in range(number_molekule):
        unit = turtle.Turtle('circle')
        unit.hideturtle()
        unit.color('cyan')
        unit.width(1)
        Vx = random.randint(-10, 10)
        Vy = random.randint(-10, 10)
        if Vx == 0 or Vy == 0:
            Vx = 3
            Vy = -3
        unit.penup()
        unit.goto(random.randint(-250, 250), random.randint(-250, 250))
        unit.pendown()
        unit.showturtle()
        gas_molekule_list.append([unit, Vx, Vy])
    return gas_molekule_list


create_gas_molekule()


def move_all_molekules():
    loop = 0

    while loop <= 500:

        for one_molekule in gas_molekule_list:
            unit_molekule = one_molekule[0]
            Vx = one_molekule[1]
            Vy = one_molekule[2]
            x, y = unit_molekule.position()
            if x + Vx >= 282 or x + Vx <= -282:
                one_molekule[2] = -one_molekule[2]  # Vx = -Vx
            if y + Vy >= 282 or y + Vy <= -282:
                one_molekule[2] = -one_molekule[2]  # Vy = -Vy
            unit_molekule.penup()
            unit_molekule.speed(0)
            unit_molekule.goto(x + Vx, y + Vy)
            unit_molekule.pendown()
        loop += 1


move_all_molekules()

window.mainloop()
