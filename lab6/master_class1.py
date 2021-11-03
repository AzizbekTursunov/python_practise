import pygame
from pygame.draw import *

pygame.init()
FPS = 30

sc = pygame.display.set_mode((1000, 700))

sc.fill('white')
pygame.display.update()
clock = pygame.time.Clock()
fineshed = False

while not fineshed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            fineshed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(sc, 'red', event.pos, 50)
                pygame.display.update()
            elif event.button == 2:
                circle(sc, 'gray', event.pos, 50)
                pygame.display.update()
            elif event.button == 3:
                circle(sc, 'blue', event.pos, 50)
                pygame.display.update()
