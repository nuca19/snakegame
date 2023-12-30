import pygame
import sys
import random

pygame.init()

SW, SH = 600, 600

BLOCK_SIZE = 50
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Consolas", 50)

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            block = pygame.Rect(x,y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#36013f", block, 1)

class Fruit:
    def __init__(self):
        self.x, self.y = random.randrange(0,SW,BLOCK_SIZE), random.randrange(0,SH,BLOCK_SIZE)
        self.pos = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    
    def remove(self):
        self.pos = None
     
    
class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if snake.head.x < 0 or snake.head.x >= SW or snake.head.y < 0 or snake.head.y >= SH:
                snake.dead = True

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

    def remove(self):
        self.head = None
        self.body = None



score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))

drawGrid()
snake = Snake()
fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.ydir!=-1:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir!=1:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir!=-1:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir!=1:
                snake.ydir = 0
                snake.xdir = -1

    if snake.dead:
        snake = Snake()
        fruit.remove
        fruit = Fruit()
        
    snake.update()
    screen.fill("black")
    drawGrid()

    score = FONT.render(str(len(snake.body)), True, "white")
    pygame.draw.rect(screen, "red", fruit.pos)
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    if snake.head.x == fruit.x and snake.head.y == fruit.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        fruit.remove
        fruit = Fruit()

    screen.blit(score, score_rect)
    
    pygame.display.update()
    clock.tick(10)