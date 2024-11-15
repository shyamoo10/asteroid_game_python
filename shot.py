import pygame
from  circleshape import *
from main import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
        
    def draw(self, screen):
       pygame.draw.circle(screen, "white",(self.position),self.radius, 2)
    
    def update(self, dt):
        print(self.position.x)
        self.position.x+= self.velocity.x*dt
        self.position.y+= self.velocity.y*dt
    
    def collision(self, circle_obj):
        dist= pygame.Vector2.distance_to(self.position, circle_obj.position)
        if (dist <= self.radius+circle_obj.radius):
            print("collision")
            self.kill()
            circle_obj.kill()
           
        
        
    