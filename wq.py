import pygame
import pygame.font
from pygame.locals import *
ZiTi=pygame.font.get_fonts()
SCREEN_SIZE = (700,520)
#screen = pygame.display.set_mode([640,480])
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
screen.fill([255,255,255])

for i in ZiTi:

   print(i)