import pygame 
import sys

pygame.init() 
 
canvas = pygame.display.set_mode((500, 500))
canvas.fill((200, 0,0 ))

pygame.display.set_caption("This Pygame is a Pyshame") 
exit = False

pygame.draw.rect(canvas, (0, 0, 255), [50, 175, 400, 100], 0)
pygame.draw.rect(canvas, (255, 255, 255), [50, 175, 100, 50], 0)
pygame.display.update() 
while not exit: 
    
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
             print("space")
         elif event.key == pygame.K_w:
             print("w")
         elif event.key == pygame.K_a:
             print("a")
         elif event.key == pygame.K_s:
             print("s")
         elif event.key == pygame.K_d:
             print("d")
 
 pygame.display.update() 

