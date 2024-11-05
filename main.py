import pygame
from constants import * 
from player import *

def main():
    pygame.init()
    time_clock=  pygame.time.Clock()
    updatable=pygame.sprite.Group()    
    drawable=pygame.sprite.Group()

   
    dt=0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black=(0,0,0)
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)
    
    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        screen.fill(black)
        for things in drawable:
            things.draw(screen)
           
        for things in updatable:
            things.update(dt)
        
        pygame.display.flip()
        dt = time_clock.tick(60)/1000
        
        
        
    
    
    
    

    
if __name__ == "__main__":
    main()