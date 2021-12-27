import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

#Display setup
pygame.display.set_caption('Platformer (IDK the name yet)')
displaySize = (1280, 720)
display = pygame.display.set_mode(displaySize)
pygame.display.update()
pygame.display.Info()
#game functions

player = pygame.image.load('images/pepshesh.png')
playerLocation = [50,600]

movingRight = False
movingLeft = False
movingDown = False
movingUp = False
playerMoving = False

playerSpeed = [0,0]
#game loop
open = True
while open:

    display.fill((0,0,0))

    display.blit(player,playerLocation)

    #gravity

    playerSpeed[1] += 0.04

   #movement
    if movingRight == True:
        playerSpeed[0] += 0.05
    if movingLeft == True:
        playerSpeed[0] -= 0.05
    if movingDown == True:
        playerSpeed[1] += 0.05
    if movingUp == True:
        playerSpeed[1] -= 0.05
    
    playerLocation[0] += playerSpeed[0]
    playerLocation[1] += playerSpeed[1]
    playerSpeed[0] *= 0.95
    playerSpeed[1] *= 0.95

    #clip

    if playerLocation[1] >= 600:
        playerLocation[1] = 600

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                movingRight = True
                playerMoving = True
            if event.key == K_LEFT:
                movingLeft = True
                playerMoving = True
            if event.key == K_DOWN:
                movingDown = True
                playerMoving = True
            if event.key == K_UP:
                movingUp = True
                playerMoving = True
            if event.key == K_q:
                playerSpeed += 1
            if event.key == K_SPACE:
                playerSpeed[1] -= 10
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                movingRight = False
                playerMoving = False
            if event.key == K_LEFT:
                movingLeft = False
                playerMoving = False
            if event.key == K_DOWN:
                movingDown = False
                playerMoving = False
            if event.key == K_UP:
                movingUp = False
                playerMoving = False
    
    pygame.display.update()
    clock.tick(60)

pygame.draw.rect()
pygame.quit()
quit()