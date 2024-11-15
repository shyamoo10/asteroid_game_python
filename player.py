import pygame
from circleshape import *
from constants import *
from main import *

 


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation= 0
        self.timer=0
    
    
    
    # in the player class
    def triangle(self):
     forward = pygame.Vector2(0, 1).rotate(self.rotation)
     right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
     a = self.position + forward * self.radius
     b = self.position - forward * self.radius - right
     c = self.position - forward * self.radius + right
     return [a, b, c]    

    def draw(self, screen):
       pygame.draw.polygon(screen,"white",self.triangle(),2)
       
       
    def rotate(self,dt):
        self.rotation= self.rotation+ PLAYER_TURN_SPEED*dt
         
    
    def update(self, dt):
        self.timer-= dt
        keys = pygame.key.get_pressed()
        neg_dt= 0-dt
        if keys[pygame.K_LEFT]:
           
            self.rotate(neg_dt)
            
            
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
             
        if keys[pygame.K_UP]:
            self.move(dt)    
        if keys[pygame.K_DOWN]:
            self.move(neg_dt)   
        if keys[pygame.K_SPACE] :
            if self.timer  < 0: 
             self.shoot(dt)    
    
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    
        
    def collision(self,circle_obj):
        dist= pygame.Vector2.distance_to(self.position, circle_obj.position)
        if (dist <= self.radius+circle_obj.radius):
            print("collision")
            exit()
    
    def shoot(self,dt):
          self.timer=  PLAYER_SHOOT_COOLDOWN
          shot= Shot(self.position.x,self.position.y,SHOT_RADIUS) 
        
         
          shot.velocity= pygame.Vector2(0,1).rotate(self.rotation)
          shot.velocity*=PLAYER_SHOOT_SPEED
          
         
          
          
          
          
         
          
          
      
       
      
      
        
               