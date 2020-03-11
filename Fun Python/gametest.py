import pygame, random

pygame.init()
rad=5
screen = pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
done=False
while(not done):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    #(100,0,128)
    screen.fill((255,0,195))
    #rad=random.randint(25,100)
    pygame.draw.circle(screen,(0,255,0),(320,240),rad,0)
    if (rad>240):
        rad=1
    rad=rad+1
    x=random.randint(0,640)
    y=random.randint(0,480)
    r=random.randint(0,250)
    g=random.randint(0,250)
    b=random.randint(0,250)
    rect1=pygame.draw.rect(screen,(r,g,b),(x,y,100,75),0)
    tri=pygame.draw.lines(screen,(r,g,b),True,[(40,400),(600,400),(320,80)],5)
    pygame.display.update()
    clock.tick(300000000000000000)
pygame.quit()
