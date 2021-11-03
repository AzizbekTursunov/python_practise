import pygame
from pygame.draw import *

pygame.init()
FPS = 30
sc = pygame.display.set_mode((1000, 600))


# start draw picture with pygame.draw
def draw_hare(x, y, width, height):
    """
    This function must draw picture hares, where this environment.
    :param x: central coordinate picture hare in axis x
    :param y: central coordinate picture hare in axis y
    :param width: width picture hare
    :param height: height picture hare
    :return: none
    """

    def draw_body(hare_cord_x, hare_cord_y, width_hare, height_hare):
        """
        Рисует тело зайца.
        surface - объект pygame.Surface
        x, y - координаты центра изображения
        width, height - ширина и высота изобажения
        color - цвет, заданный в формате, подходящем для pygame.Color
        """
        ellipse(sc, (159, 146, 137),
                (hare_cord_x - width_hare // 2, hare_cord_y - height_hare // 2, width_hare, height_hare))

    def draw_head(cord_axis_x, cord_axis_y, size):
        """
        Рисует голову зайца.
        surface - объект pygame.Surface
        x, y - координаты центра изображения
        size - диаметр головы
        color - цвет, заданный в формате, подходящем для pygame.Color
        """
        circle(sc, (159, 146, 137), (cord_axis_x, cord_axis_y), size // 2)

    def draw_ear(cord_axis_x, cord_axis_y, width_hare, height_hare):
        """
        Рисует ухо зайца.
        surface - объект pygame.Surface
        x, y - координаты центра изображения
        width, height - ширина и высота изобажения
        color - цвет, заданный в формате, подходящем для pygame.Color
        """
        ellipse(sc, (159, 146, 137), (cord_axis_x - width_hare // 2,
                                      cord_axis_y - height_hare // 2, width_hare, height_hare))

    def draw_leg(cord_axis_x, cord_axis_y, width_hare, height_hare):
        """
        Рисует ногу зайца.
        surface - объект pygame.Surface
        x, y - координаты центра изображения
        width, height - ширина и высота изобажения
        color - цвет, заданный в формате, подходящем для pygame.Color
        """
        ellipse(sc, (159, 146, 137), (cord_axis_x - width_hare // 2,
                                      cord_axis_y - height_hare // 2, width_hare, height_hare))

    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(x, body_y, body_width, body_height)

    head_size = height // 4
    draw_head(x, y - head_size // 2, head_size)

    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 4, x + head_size // 4):
        draw_ear(ear_x, ear_y, width // 8, ear_height)

    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    for leg_x in (x - width // 4, x + width // 4):
        draw_leg(leg_x, leg_y, width // 4, leg_height)


def draw_environment():
    """
    This function must draw environment(grass, sky, sun, mountain, tree) in this picture.
    :return: none
    """

    def draw_grass():
        color_grass = (0, 154, 23)
        rect(sc, color_grass, (0, 300, 1000, 300))

    def draw_sky():
        color_sky = (135, 206, 235)
        rect(sc, color_sky, (0, 0, 1000, 300))

    def draw_sun():
        color_sun = (255, 223, 34)
        circle(sc, color_sun, (940, 60), 100)

    def draw_tree():
        color_tree_leg = (205, 133, 63)
        color_tree_leaves = (34, 139, 34)

        def draw_down_leaf():
            top_left_coordinate_down_leaf_axis_x = 2.5
            top_left_coordinate_down_leaf_axis_y = 260
            width_down_leaf = 200
            height_down_leaf = 80
            parametr_list_down_leaf = [top_left_coordinate_down_leaf_axis_x, top_left_coordinate_down_leaf_axis_y,
                                       width_down_leaf, height_down_leaf]
            ellipse(sc, color_tree_leaves, parametr_list_down_leaf)

        def draw_median_down_leaf():
            top_left_coordinate_median_down_leaf_axis_x = -47.5
            top_left_coordinate_median_down_leaf_axis_y = 190
            width_median_down_leaf = 300
            height_median_down_leaf = 100
            parametr_list_median_down_leaf = [top_left_coordinate_median_down_leaf_axis_x,
                                              top_left_coordinate_median_down_leaf_axis_y,
                                              width_median_down_leaf,
                                              height_median_down_leaf]
            ellipse(sc, color_tree_leaves, parametr_list_median_down_leaf)

        def draw_median_up_leaf():
            top_left_coordinate_median_up_leaf_axis_x = -97.5
            top_left_coordinate_median_up_leaf_axis_y = 90
            width_median_up_leaf = 400
            height_median_up_leaf = 140
            parametr_list_median_up_leaf = [top_left_coordinate_median_up_leaf_axis_x,
                                            top_left_coordinate_median_up_leaf_axis_y,
                                            width_median_up_leaf,
                                            height_median_up_leaf]

            ellipse(sc, color_tree_leaves, parametr_list_median_up_leaf)

        def draw_up_leaf():
            top_left_coordinate_up_leaf_axis_x = -22.5
            top_left_coordinate_up_leaf_axis_y = 20
            width_up_leaf = 250
            height_up_leaf = 100
            parametr_list_up_leaf = [top_left_coordinate_up_leaf_axis_x,
                                     top_left_coordinate_up_leaf_axis_y,
                                     width_up_leaf,
                                     height_up_leaf]
            ellipse(sc, color_tree_leaves, parametr_list_up_leaf)

        rect(sc, color_tree_leg, (90, 340, 25, 100))
        draw_down_leaf()
        draw_median_down_leaf()
        draw_median_up_leaf()
        draw_up_leaf()

    def draw_mountain():
        color_mountain = (196, 215, 212)
        color_snow_mountain = (240, 240, 240)

        def draw_left_mountain():
            polygon(sc, color_mountain, [(0, 300), (400, 300), (200, 150)])

        def draw_median_mountain():
            polygon(sc, color_mountain, [(250, 300), (850, 300), (450, 50)])

        def draw_snow_median_mountain():
            polygon(sc, color_snow_mountain, [(395, 120), (565, 120), (450, 50)])

        def draw_right_mountain():
            polygon(sc, color_mountain, [(600, 300), (1000, 300), (800, 150)])

        def draw_snow_right_mountain():
            polygon(sc, color_snow_mountain, [(773, 170), (827, 170), (800, 150)])

        draw_left_mountain()
        draw_median_mountain()
        draw_snow_median_mountain()
        draw_right_mountain()
        draw_snow_right_mountain()

    draw_grass()
    draw_sky()
    draw_sun()
    draw_mountain()
    draw_tree()


draw_environment()
draw_hare(700, 350, 200, 400)
# end draw picture
pygame.display.update()
clock = pygame.time.Clock()
finish_program = False

while not finish_program:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            finish_program = True
