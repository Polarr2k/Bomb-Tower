#!/usr/bin/python3

# Bomb Tower

import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

#display
pygame.display.set_caption('Bomb Tower')
displaySize = (1280,720)
display = pygame.display.set_mode(displaySize)
pygame.display.update()

player = pygame.image.load('Untitled-1.png')
playerLocation =(0,0)

screenColor = (0,0,0)

#Game loop
running = True
while running:
    
    display.fill(screenColor)

    display.blit(player,playerLocation)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                print("hi")
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()