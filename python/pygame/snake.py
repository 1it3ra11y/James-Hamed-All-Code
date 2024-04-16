import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        
    def drawSnake(self):
        for block in self.body:
            snakeRect = pygame.Rect(int(block.x * cellSize), int(block.y * cellSize), cellSize, cellSize)
            pygame.draw.rect(screen, (66, 161, 79), snakeRect)
    
    def moveSnake(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = Vector2(self.x, self.y)
        
    def drawFruit(self):
        fruitRect = pygame.Rect(int(self.pos.x * cellSize), int(self.pos.y * cellSize), cellSize, cellSize)
        pygame.draw.rect(screen, (126, 166, 114), fruitRect)
        
pygame.init()

cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize * cellNumber, cellNumber * cellSize))
clock = pygame.time.Clock()
fruit1 = FRUIT()
snake = SNAKE()
screenupdate = pygame.USEREVENT
pygame.time.set_timer(screenupdate, 150)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenupdate:
            snake.moveSnake()
            
    screen.fill((175, 215, 70))
    fruit1.drawFruit()
    snake.drawSnake()
        
    clock.tick(60)   
    pygame.display.update()
     