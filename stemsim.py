import pygame
from pygame.locals import *
pygame.init()
vec=pygame.math.Vector2
clock=pygame.time.Clock()

black=(0,0,0)
brown=(139,69,19)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
screen=pygame.display.set_mode((600,600))
WIDTH=screen.get_width()
HEIGHT=screen.get_height()
class FrictionSurf(pygame.sprite.Sprite):
    def __init__(self, color, friction, bounce):
        super().__init__()
        self.friction=friction
        self.surf=pygame.Surface((WIDTH,10))
        self.surf.fill(color)
        self.rect=self.surf.get_rect()
        self.bounce=bounce


class Body(pygame.sprite.Sprite):
    def __init__(self, velocity, acceleration, position, color, size):
        super.__init__()
        self.surf=pygame.Surface(size)
        self.surf.fill(color)
        self.rect=self.surf.get_rect(center=(position))
        self.vel=vec(velocity)
        self.acc=vec(acceleration)
        
    def changevel(self,surface):
        if pygame.sprites.spritecollideany(self,surface):
            self.vel.y = -self.vel.y+surface.bounce

        

while True: 
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            quit()
    
    screen.fill(white)

    



