import pygame
from pygame.locals import *
from sys import exit
background_image = 'image/xia.jpg'
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image).convert()

x,y = 0,0
move_x,move_y = 0,0
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            if event.key == K_RIGHT:
                move_x = +1
            if event.key == K_UP:
                move_y = -1
            if event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

    y += move_y
    x += move_x
    screen.fill((0,0,0))
    screen.blit(background,(x,y))

    pygame.display.update()
