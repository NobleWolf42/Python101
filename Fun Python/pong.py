import pygame, random

pygame.init()

PINK=(255,0,195)
PURPLE=(100,0,128)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,245)
YELLOW=(242,255,0)
rad=5
sw=1000
sh=800
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Breakout")

score=0
life=3

def drawetc(x,y):
    pygame.draw.circle(screen,PINK,(x+7,y+7),7,0)

##class Player(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image=pygame.Surface([14,14])
##        self.image.fill(PURPLE)
##        self.rect=self.image.get_rect()
##    def update(self):
##        self.rect.x+=vx
##        self.rect.y+=vy

class Block(pygame.sprite.Sprite):
    lives = 3
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([100,15])
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
    def update(self):
        if Block.lives == 2:
            self.image=pygame.Surface([100,15])
            self.image.fill(YELLOW)
            self.rect=self.image.get_rect()
        if Block.lives == 1:
            self.image=pygame.Surface([100,15])
            self.image.fill(RED)
            self.rect=self.image.get_rect()
        

block_list=pygame.sprite.Group()
target_hit_list = pygame.sprite.Group()

for i in range(9):
    for j in range(5):
        block=Block()
        block.rect.x=(i*110)+10
        block.rect.y=(j*30)+50
        block_list.add(block)
x=500
y=400
vx=2
vy=3
px=500
py=740
pv=0

clock=pygame.time.Clock()
done=False


ect_width=14
ect_height=14


while(not done):
    myfont=pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                pv=10
            elif event.key==pygame.K_LEFT:
                pv=-10
        if event.type==pygame.KEYUP:
            pv=0
    if (x<=0) or (x+ect_width>=sw):
        vx*=-1
    if (y<=0) or (y+ect_height>=sh):
        vy*=-1
    x+=vx
    y+=vy
    px=px+pv

    brect=pygame.draw.rect(screen,PURPLE,(x,y,ect_width,ect_height),1)
    screen.fill(PURPLE)
    paddle=pygame.draw.rect(screen,BLUE,(px,py,75,10))
    if brect.colliderect(paddle):
        vy=vy*-1
        y+=-10
    if (y+ect_height>=sh):
        x=500
        y=400
        vx=random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        vy=random.choice([-5,-4,-3,-2,-1,1,2,3,4,5])
        life=life-1
    if px<0:
        pv=0
        px=0
    if px>925:
        pv=0
        px=925
        

   # target_hit_list=pygame.Rect.colliderect(brect,block_list,True)
    for block in block_list:
        if(brect.colliderect(block.rect)):
            block.lives -= 1
            block_list.update()
            #if(block.lives == 0):
                #block_list.update()
            target_hit_list.add(block)
            vy=random.choice([5,4,3,2,1])
            score=score+1
    for block in target_hit_list:
        block_list.remove(block)

    if life==0:
        done=True
    if score == 45:
        done = True
    
    text=myfont.render("Score:"+str(score),1,(255,255,255))
    text2=myfont.render("Lives:"+str(life),1,(255,255,255))
    screen.blit(text,(20,20))
    screen.blit(text2,(900,20))
    drawetc(x,y)
    block_list.update()
    block_list.draw(screen)
    pygame.display.flip()
    clock.tick(70)
pygame.quit()
