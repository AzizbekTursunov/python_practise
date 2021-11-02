import pygame
from pygame.draw import *

pygame.init()
clock = pygame.time.Clock()
FPS = 60
sc = pygame.display.set_mode((540, 740), pygame.RESIZABLE)

# using colors in this programm

white = (255, 255, 255)
green = (0, 255, 0)
color_tree_life = (0, 150, 00)
cyan = (0, 255, 255)
color_sun = (255, 230, 124)
color_tree_body = (220, 220, 220)
black = (0, 0, 0)
red = (255, 0, 0)
color_fruit = (250, 218, 221)
color_eye_animal = (237, 172, 250)
color_horn_of_animal = (178, 69, 160)

# colors_for_hear_animal_and_stone

a = (178, 69, 160)
b = (232, 211, 143)
c = (172, 245, 76)
d = (250, 218, 221)
e = (234, 239, 82)
g = (200, 76, 245)
list_color_hear_animal = [a, b, g, d, a, g,
                          e, b, c, d, e, c]
list_color_stone = [a, b, g, d, a, g,
                    e, b, c, d, e, c,
                    e, b, c, d, e, c,
                    g, d, a, g, e, b,
                    b, g, d, a, c, d]

# draw picture with pygame.draw


def draw_grass_sky_and_sun():
    sc.fill(green)
    rect(sc, cyan, (0, 0, 540, 350))
    circle(sc, color_sun, (510, 70), 100)


def draw_tree():
    def draw_tree_body():
        polygon(sc, color_tree_body, ((70, 470 + 50), (100, 470 + 50),
                                      (100, 350 + 50), (70, 350 + 50)))

    def draw_tree_lifes():
        for i in [(15, 330, 140, 115), (-40, 240, 240, 115), (10, 125 + 10, 140, 150 + 10)]:
            ellipse(sc, color_tree_life, i)

    def draw_tree_fruits():
        for i in [(80 + 30, 370 + 20 + 10, 35, 35), (80 + 30 + 40, 370 + 20 + 10 - 110, 40, 35),
                  (80 + 30 - 125, 370 + 20 + 10 - 110, 40, 35), (80 + 30 - 20, 370 + 20 + 10 - 240, 40, 35)]:
            ellipse(sc, color_fruit, i)

    draw_tree_body()
    draw_tree_lifes()
    draw_tree_fruits()


def draw_animal():
    def draw_legs_animals():
        for i in [(430, 545, 13, 80), (385, 555, 18, 100),
                  (315, 550, 18, 80), (275, 545, 13, 100)]:
            rect(sc, white, i)

    def draw_body_animals():
        ellipse(sc, white, (255, 480, 210, 100))

    def draw_neck_animal():
        ellipse(sc, white, (388, 396, 80, 150))
        ellipse(sc, white, (405, 395, 65, 35))
        ellipse(sc, black, (350, 450, 80, 50), 1)
        ellipse(sc, white, (350, 450, 80, 50))

    def draw_face_animal():
        ellipse(sc, white, (432, 411, 65, 35))

    def draw_eye_animals():
        circle(sc, color_eye_animal, (449, 426), 9)
        circle(sc, black, (452, 426), 4)
        ellipse(sc, white, (442, 421, 10, 5))

    def draw_horn_of_animal():
        polygon(sc, color_horn_of_animal, [[430, 398], [450, 320], [430 + 20, 400]])

    draw_legs_animals()
    draw_body_animals()
    draw_neck_animal()
    draw_face_animal()
    draw_eye_animals()
    draw_horn_of_animal()


def hear_cordinate_list():
    x_list = [400, 390, 380, 360, 350, 350, 315, 320, 330, 310, 325, 325]
    y_list = [390, 400, 405, 430, 460, 450, 460, 460, 450, 460, 450, 440]
    width_list = [30, 35, 35, 45, 40, 45, 30, 35, 45, 30, 40, 65]
    height_list = [20, 25, 35, 30, 25, 20, 20, 25, 35, 20, 25, 20]
    list_all_coord = []
    for i in range(12):
        list_all_coord.append([x_list[i], y_list[i], width_list[i], height_list[i]])
    return list_all_coord


def draw_hear_animals():
    def hear_cord_list():
        x_list = [400, 390, 380, 360, 360, 350, 315, 320, 330, 310, 325, 325]
        y_list = [390, 400, 405, 430, 415, 450, 465, 460, 450, 460, 450, 440]
        width_list = [30, 35, 35, 45, 40, 45, 30, 35, 45, 30, 40, 65]
        height_list = [20, 25, 15, 20, 25, 20, 20, 25, 15, 20, 25, 20]
        list_all_coord = []
        for i in range(12):
            list_all_coord.append([x_list[i], y_list[i], width_list[i], height_list[i]])
        return list_all_coord

    # then draw_hears_animals

    for color_hear, hear_coordinate in zip(list_color_hear_animal, hear_cord_list()):
        ellipse(sc, color_hear, hear_coordinate)


def draw_stone_near_animal():
    def stone_cordinate_list():
        x_list = [180, 206, 215, 220, 175, 210, 215, 190, 220, 210,  # 10 value each st
                  225, 225, 170, 210, 190, 195, 200, 180, 200, 215,
                  225, 205, 220, 185, 210, 170, 230, 190, 180, 200, ]
        y_list = [620, 605, 515, 590, 510, 545, 560, 580, 530, 560,  # 10 value each st
                  625, 520, 615, 570, 515, 620, 550, 560, 530, 600,
                  500, 510, 550, 505, 500, 555, 580, 520, 550, 565]
        width_list = [30, 35, 35, 45, 40, 45, 30, 35, 45, 30,  # 10 value each st
                      40, 55, 30, 35, 35, 45, 50, 60, 45, 50,
                      45, 50, 45, 45, 50, 40, 45, 30, 35, 45, ]
        height_list = [20, 25, 15, 20, 25, 20, 20, 25, 18, 20,  # 10 value each st
                       25, 20, 20, 25, 15, 22, 13, 20, 25, 18,
                       20, 25, 15, 20, 25, 22, 13, 20, 20, 23, ]
        list_all_coord = []
        for i in range(30):
            list_all_coord.append([x_list[i], y_list[i], width_list[i], height_list[i]])
        return list_all_coord

    # then draw_stones

    for color_stone, stone_coordinate in zip(list_color_stone, stone_cordinate_list()):
        ellipse(sc, color_stone, stone_coordinate)


def function_for_draw_all_picture():
    draw_grass_sky_and_sun()
    draw_tree()
    draw_stone_near_animal()
    draw_animal()
    draw_hear_animals()


function_for_draw_all_picture()
# end_draw_picture
pygame.display.update()
for_quit_mainloop = True
while for_quit_mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            for_quit_mainloop = False
            clock.tick(FPS)
