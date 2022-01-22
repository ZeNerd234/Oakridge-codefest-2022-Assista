import pygame
from pygame.locals import *
pygame.init()
vec=pygame.math.Vector2
clock=pygame.time.Clock()

black=(0,0,0)
brown=(139,69,19)
green=(0,255,0)
red=(255,0,0)
blue=(30,144,255)
white=(255,255,255)
yellow=(255,255,0)
screen=pygame.display.set_mode((600,600))
WIDTH=screen.get_width()
HEIGHT=screen.get_height()
class FrictionSurf(pygame.sprite.Sprite):
    def __init__(self, color, friction, bounce):
        super().__init__()
        self.friction=friction
        self.surf=pygame.Surface((WIDTH,20))
        self.surf.fill(color)
        self.rect=self.surf.get_rect(bottomleft=(0,HEIGHT))
        self.bounce=bounce


class Body(pygame.sprite.Sprite):
    def __init__(self, velocity, acceleration, position, color, size, fixed_acc=0.5):
        super().__init__()
        self.surf=pygame.Surface(size)
        self.surf.fill(color)
        self.pos=vec(position)
        self.rect=self.surf.get_rect(bottomright=(self.pos))
        self.vel=vec(velocity)
        self.acc=vec(acceleration)
        self.ACC=fixed_acc

        
    def changevel(self,surface, surf):
        if pygame.sprite.spritecollideany(self,surface):
            if self.vel.y!=0:
                self.vel.y = -self.vel.y-surf.bounce

            

    def move(self):
        pk=pygame.key.get_pressed()
        if pk[K_LEFT]:
            self.acc.x = -self.ACC
        if pk[K_RIGHT]:
            self.acc.x = self.ACC
        self.acc.x += self.vel.x * self.friction
        self.vel += self.acc
        if not self.vel==0:
            self.pos += self.vel + 0.5 * self.acc
            self.rect.bottomright=self.pos
        if self.rect.x<0:
            self.rect.x=WIDTH
        if self.rect.x>WIDTH:
            self.rect.x=0
        
                
        
#wood=FrictionSurf(brown,-0.5,0.1)               
#glass=FrictionSurf(blue,-0.2,0.5)
#sand=FrictionSurf(yellow, -0.7,0.7)
sprites=pygame.sprite.Group()
font=pygame.font.SysFont('Courier',20)
w=font.render('Wood',True,black)
g=font.render('Glass',True,black)
s=font.render('Sand',True,black)
b=Body(vec(0,0),vec(0,0),(50,HEIGHT-20),green,(30,30))
wood=FrictionSurf(brown,-0.1,0.1)
b.friction=wood.friction
sprites=pygame.sprite.Group(b)
obs=pygame.sprite.Group(wood)
b.friction=wood.friction
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            quit()
        '''if event.type==KEYDOWN:
            if event.key==K_UP:'''
        if event.type==MOUSEBUTTONDOWN:
            if 50<mouse[0]<100 and 50<mouse[1]<70:
                wood=FrictionSurf(brown,-0.1,0.1)
                b.friction=wood.friction
            
    
    screen.fill(white)
    pygame.draw.rect(screen,blue,[50,50,50,20])
    screen.blit(w,(50,50))
    pygame.draw.rect(screen,blue,[150,50,60,20])
    screen.blit(g,(150,50))
    pygame.draw.rect(screen,blue,[250,50,50,20])
    screen.blit(s,(250,50))
    mouse=pygame.mouse.get_pos()
    b.move()
    b.changevel(obs,wood)
    screen.blit(wood.surf,wood.rect)
    for sprite in sprites:
        screen.blit(sprite.surf,sprite.rect)
    pygame.display.update()
    clock.tick(60)

    
