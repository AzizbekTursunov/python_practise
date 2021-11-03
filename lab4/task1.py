import pygame
from pygame.draw import *

pygame.init()
sc = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Angry smile")
pygame.display.set_icon(pygame.image.load("angry_smile.jpg"))

# block color

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
gray = (200, 200, 200)
sc.fill(gray)
flruning = True

# draw_smile_block_---------------------------------------------

# koordinate_smile's_head_and_eyes

circle_center_koordinate_head_smile = (300, 300)
circle_center_koordinate_right_eye_smile = (400, 230)
circle_center_koordinate_left_eye_smile = (200, 230)

# draw_head

circle(sc, yellow, circle_center_koordinate_head_smile, 200)
circle(sc, black, circle_center_koordinate_head_smile, 200, 1)

# drae_right_eye

circle(sc, red, circle_center_koordinate_right_eye_smile, 30)
circle(sc, black, circle_center_koordinate_right_eye_smile, 30, 1)
circle(sc, black, circle_center_koordinate_right_eye_smile, 15)

# draw_left_eye

circle(sc, red, circle_center_koordinate_left_eye_smile, 40)
circle(sc, black, circle_center_koordinate_left_eye_smile, 40, 1)
circle(sc, black, circle_center_koordinate_left_eye_smile, 20)

# draw_mounth

rect(sc, black, (200, 380, 200, 40))

# draw_right_brow

polygon(sc, black, [(340, 230), (340-10, 230-12), (480-10, 150-12), (480, 150)])

# draw_left_brow

polygon(sc, black, [(250, 220), (264, 208), (115+14-10, 115-12-10), (115-10, 115-10)])

# end draw_smile_block_---------------------------------------------

pygame.display.update()
while flruning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flruning = False
