import pygame,sys

pygame.init()
sceen = pygame.display.set_mode([640,480])
sceen.fill([255,255,255])
pygame.draw.rect(sceen,[255,0,0],[250, 150, 300, 200],0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()