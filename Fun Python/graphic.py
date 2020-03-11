#This is the basic code to open a window and fill it with a background color.
#graphics_template.py   Heather Booth  7/12/13

#**import*** Always start with this.
import sys, pygame, random
from pygame import *

#initialize the graphics
pygame.init()
screen = pygame.display.set_mode((600,400))
#Needed to set the speed of the game
Clock=pygame.time.Clock()
background_color = (16, 161, 69)

done = False
while done==False:
    #***Setting the speed of the loop. This makes it 60 frames (loops) per second
    Clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    #erase
    screen.fill(background_color)

    #DRAW NEW STUFF YOUR CODE HERE
    rectangle1 = pygame.draw.rect(screen, (0, 208, 255), (0,0, 600, 225)) 
    #send it to the screen
    pygame.display.update()

pygame.quit()
