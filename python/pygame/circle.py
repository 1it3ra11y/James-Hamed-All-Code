import pygame
pygame.init()

r = int(input("Red value: "))
g = int(input("Green value: "))
b = int(input("Blue value: "))
s = int(input("size: "))
x = int(input("x value(out of 500): "))
y = int(input("y value(out of 500): "))

screen = pygame.display.set_mode([500, 500])

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (r, g, b), (x, y), s)
    
    pygame.display.flip()
pygame.quit()