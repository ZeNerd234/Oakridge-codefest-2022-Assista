import pygame
from pygame.locals import *

vec=pygame.math.Vector2
class FrictionSurf(pygame.sprite.Sprite):
    def __init__(self, color, friction, bounce):
        super().__init__()
        WIDTH=600
        HEIGHT=600
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
        self.jumping=False
        self.grav=0.1

        
    def changevel(self,surface):
        self.surface=surface
        if pygame.sprite.spritecollideany(self,surface):
            if self.vel.y!=0:
                self.vel.y =0
                self.jumping=False

            

    def move(self):
        pk=pygame.key.get_pressed()
        if pk[K_LEFT]:
            self.acc.x = -self.ACC
        if pk[K_RIGHT]:
            self.acc.x = self.ACC
        if pk[K_UP]:
            if pygame.sprite.spritecollideany(self,self.surface):
                self.vel.y=-8
            self.jumping=True
        self.acc.x += self.vel.x * self.friction
        self.vel += self.acc
        if not self.vel==0:
            self.pos += self.vel + 0.5 * self.acc
            self.rect.bottomright=self.pos
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.right>600:
            self.rect.right=600
        if self.jumping:
            self.vel.y+=self.grav
        if self.vel.y==0:
            self.jumping=False

        
                
        
#wood=FrictionSurf(brown,-0.5,0.1)               
#glass=FrictionSurf(blue,-0.2,0.5)
#sand=FrictionSurf(yellow, -0.7,0.7)
def simulate():
    pygame.init()
    
    clock=pygame.time.Clock()

    black=(0,0,0)
    brown=(139,69,19)
    green=(0,255,0)
    red=(255,0,0)
    blue=(30,144,255)
    white=(255,255,255)
    yellow=(255,255,0)
    grey=(192,192,192)
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Friction simulation')
    WIDTH=screen.get_width()
    HEIGHT=screen.get_height()
    sprites=pygame.sprite.Group()
    font=pygame.font.SysFont('Courier',20)
    font2=pygame.font.SysFont('Courier',15)
    w=font.render('Wood',True,black)
    g=font.render('Glass',True,black)
    s=font.render('Sand',True,black)
    t=font.render('Stop',True,black)
    r=font.render('Gravity',True,black)
    plus=font.render('+',True,black)
    minus=font.render('-',True,black)
    b=Body(vec(0,0),vec(0,0),(50,HEIGHT-20),green,(30,30))
    wood=FrictionSurf(brown,-0.5,0.1)
    b.friction=wood.friction
    sprites=pygame.sprite.Group(b)
    obs=pygame.sprite.Group(wood)
    b.friction=wood.friction
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                return
            if event.type==MOUSEBUTTONDOWN:
                if 50<mouse[0]<100 and 50<mouse[1]<70:
                    wood=FrictionSurf(brown,-0.5,0.1)
                    b.friction=wood.friction
                if 150<mouse[0]<210 and 50<mouse[1]<70:
                    wood=FrictionSurf(blue,-0.2,0.5)
                    b.friction=wood.friction
                if 250<mouse[0]<300 and 50<mouse[1]<70:
                    wood=FrictionSurf(yellow, -0.7,0.7)
                    b.friction=wood.friction
                if 350<mouse[0]<400 and 50<mouse[1]<70:
                    pygame.quit()
                    return
                if 450<mouse[0]<465 and 75<mouse[1]<90:
                    if b.grav<0.9:
                        b.grav+=0.1
                    else:
                        b.grav=0.9
                if 525<mouse[0]<540 and 75<mouse[1]<90:
                    if b.grav>0.1:
                        b.grav-=0.1
                    else:
                        b.grav=0.1
        screen.fill(white)
        gv=int(round(b.grav*10))
        gr=font2.render(str(gv),True,black)
        pygame.draw.rect(screen,blue,[50,50,50,20])
        screen.blit(w,(50,50))
        pygame.draw.rect(screen,blue,[150,50,60,20])
        screen.blit(g,(150,50))
        pygame.draw.rect(screen,blue,[250,50,50,20])
        screen.blit(s,(250,50))
        pygame.draw.rect(screen,red,[350,50,50,20])
        screen.blit(t,(350,50))
        screen.blit(r,(450,50))
        pygame.draw.rect(screen,grey,[450,75,15,15])
        pygame.draw.rect(screen,grey,[525,75,15,15])
        screen.blit(plus,(450,70))
        screen.blit(minus,(525,70))
        screen.blit(gr,(475,75))
        mouse=pygame.mouse.get_pos()
        b.move()
        b.changevel(obs)
        screen.blit(wood.surf,wood.rect)
        for sprite in sprites:
            screen.blit(sprite.surf,sprite.rect)
        pygame.display.update()
        clock.tick(60)

if __name__=='__main__':
    simulate()  
