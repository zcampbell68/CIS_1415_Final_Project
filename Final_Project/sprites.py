# sprite classes
import random
import pygame as p
from settings import *

class Player(p.sprite.Sprite):
    #creating he movable character
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((30,40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.vy = 0
        self.vx = 0
        self.score=0
        
        

    def gravity(self):
        #this will cause the player to fall
       self.vy += .5
       if self.rect.y> height-40 and self.vy >= 0:
           self.vy =0
           self.rect.y = height-40
       
            
        

    def update(self):
        self.gravity()
        self.vx = 0
        keys = p.key.get_pressed()
        if keys[p.K_LEFT] and self.rect.left > 0:
            self.vx=-5
            
        if keys[p.K_RIGHT] and self.rect.right <480:
            self.vx=5
            
        if keys[p.K_UP] and self.rect.top > 0:
            self.vy =-5

    

      
        
        
        self.rect.x += self.vx
        self.rect.y += self.vy



class Mob(p.sprite.Sprite):
    # the enemy 
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((30,5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0,height - self.rect.height)
        self.rect.x = random.randrange(490, 520)
        self.speedx = random.randrange(2,5)
        self.speedy = random.randrange(-2,2)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right < -10 or self.rect.bottom > 610 or self.rect.top < -10:
            self.rect.y = random.randrange(0,height - self.rect.height)
            self.rect.x = random.randrange(490, 520)
            self.speed = random.randrange(1,3)
            self.speedy = random.randrange(-2,2)
            
class Mob2(p.sprite.Sprite):
    # the points that you want to collect
    def __init__(self):
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface((10,20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0,height - self.rect.height)
        self.rect.x = random.randrange(490, 520)
        self.speedx = random.randrange(2,5)
        self.speedy = random.randrange(-2,2)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right < -10 or self.rect.bottom > 610 or self.rect.top < -10:
            self.rect.y = random.randrange(0,height - self.rect.height)
            self.rect.x = random.randrange(490, 520)
            self.speed = random.randrange(1,3)
            self.speedy = random.randrange(-2,2)
