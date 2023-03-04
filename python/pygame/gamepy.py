import pygame 
import sys
import time
pygame.init()

screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255)) 

while True:
    for event in pygame.event.get():
        #screen.fill((255, 255, 255)) 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print("hi")    
            pygame.draw.circle(screen, (100, 0, 200), (250, 250), 100)
            time.sleep(10)
            screen.fill((255, 255, 255))
    
    
    pygame.display.flip()
                   
