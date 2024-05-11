import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.newBlock = False
        
        self.head_up = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/head_up.png').convert_alpha() 
        self.head_down = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/body_bl.png').convert_alpha()
        
    def drawSnake(self):
        for block in self.body:
            snakeRect = pygame.Rect(int(block.x * cellSize), int(block.y * cellSize), cellSize, cellSize)
            pygame.draw.rect(screen, (66, 161, 79), snakeRect)
    
    def moveSnake(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]
            self.newBlock = False
        else:   
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]
        
    def addBlock(self):
        self.newBlock = True
        

class FRUIT:
    def __init__(self):
       self.randomize()
        
    def drawFruit(self):
        fruitRect = pygame.Rect(int(self.pos.x * cellSize), int(self.pos.y * cellSize), cellSize, cellSize)
        screen.blit(fruit,fruitRect)
        
    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = Vector2(self.x, self.y)
        
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()
        
    def drawElements(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()
        
    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addBlock() 
            
    def checkFail(self):
        if not 0 <= self.snake.body[0].x < cellNumber or not 0 <= self.snake.body[0].y < cellNumber:
            self.gameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()
            
    def gameOver(self):
        pygame.quit()
        sys.exit()
        
         
pygame.init()

cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellSize * cellNumber, cellNumber * cellSize))
clock = pygame.time.Clock()
fruit = pygame.image.load("C:/Users/jamie/OneDrive/Desktop/Code/python/pygame/pygameImages/ppl4.png").convert_alpha()
mainGame = MAIN()
screenupdate = pygame.USEREVENT
pygame.time.set_timer(screenupdate, 150)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenupdate:
            mainGame.update()
          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if mainGame.snake.direction != Vector2(0, 1):
                    mainGame.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:
                if mainGame.snake.direction != Vector2(0, -1):
                    mainGame.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_a:
                if mainGame.snake.direction != Vector2(1, 0):
                    mainGame.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_d:
                if mainGame.snake.direction != Vector2(-1, 0):
                    mainGame.snake.direction = Vector2(1, 0)
                
            
    screen.fill((175, 215, 70))
    mainGame.drawElements()
        
    clock.tick(60)   
    pygame.display.update()
     