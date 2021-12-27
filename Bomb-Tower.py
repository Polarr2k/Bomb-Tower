<<<<<<< HEAD
#!/usr/bin/python3

# Bomb Tower

import pygame
from pygame.locals import *

pygame.init()

#display
pygame.display.set_caption('Bomb Tower')
displaySize = (1280,720)
display = pygame.display.set_mode(displaySize)
pygame.display.update()


#Game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                print("hi")


pygame.quit()
quit()