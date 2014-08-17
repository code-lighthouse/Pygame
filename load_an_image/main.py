import sys
import pygame

# load a image 

pygame.init()

size = width, height = 500, 410

screen = pygame.display.set_mode(size)

trusty = pygame.image.load("image.png").convert_alpha()

screen.blit(trusty, (55, 5))
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
