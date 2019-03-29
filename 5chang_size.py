import pygame
from pygame.locals import *
from sys import exit
import time

SCREEN_SIZE = (640,480)
background_image = 'image/xia.jpg'
screen = pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
background = pygame.image.load(background_image).convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        pygame.display.set_caption("Window resize to" + str(event.size))

        print("adsdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    screen_width,screen_height = SCREEN_SIZE
    for y in range(0,screen_height,background.get_height()):
        for x in range(0,screen_width,background.get_width()):

           # print("sssssssds")
            screen.blit(background,(x,y))
            #time.sleep(1)
    pygame.display.update()