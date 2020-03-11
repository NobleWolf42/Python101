import sys, pygame
from pygame import*

atbg=pygame.image.load("at.png")
im=pygame.image.load("im.png")
bgrect=atbg.get_rect()
screen=pygame.display.set_mode((1250,703))

x=800
y=50
vx=0
vy=0

done=False
while(not done):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                vx=5
            elif event.key==pygame.K_LEFT:
                vx=-5
            elif event.key==pygame.K_UP:
                vy=-5
            elif event.key==pygame.K_DOWN:
                vy=5
        if event.type==pygame.KEYUP:
            vx=0
            vy=0
    x=x+vx
    y=y+vy
    screen.blit(atbg, bgrect)
    screen.blit(im,(x,y))
    pygame.display.update()
pygame.quit()
