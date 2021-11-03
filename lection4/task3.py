import pygame
from pygame.draw import *

pygame.init()
FPS = 30
pygame.display.set_mode((1000, 600))


# start draw picture with pygame.draw
def draw_hare(x, y, width, height):
    """
    This function must draw picture hares, where this environment.
    :param x: central coordinate picture hare in axis x
    :param y: central coordinate picture hare in axis y
    :param width: width picture hare
    :param height: height picture hare
    :return:
    """
    pass


def draw_environment():
    """
    This function must draw environment(grass, sky, sun, mountain) in this picture.
    :return: none
    """
    pass


draw_hare(500, 300, 300, 500)
draw_environment()
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
