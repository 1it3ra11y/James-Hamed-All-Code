import pygame, sys
pygame.init() 

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
Testsurface = pygame.Surface((100, 100))
Testsurface.fill((0, 0, 255))
player = Testsurface.get_rect(center = (250, 250))

while True:
    screen.fill((0, 0, 0))
    screen.blit(Testsurface, player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-2, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(2, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 2)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -2)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
              
    pygame.display.update()
    clock.tick(60)
    