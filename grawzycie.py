import sys

import random
import pygame

boardSize = input().split('x') 
height = int(boardSize[0])
width = int(boardSize[1])


cellSize = 40
size = cellSize * height, cellSize * width

screen = pygame.display.set_mode(size)

earth = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
state = earth

def wypiszBakt():
    print('-----------------------------')
    for y in range(height):
        for x in range(width):
            print(earth[y][x], end=' ')
        print('')
    print('-----------------------------')

def policzIleSasiadow(x, y):
    dx = [1, 1, -1, -1, 0, 0]
    dy = [-1, 0, 1, 0, 1 , -1]

    liczbaSasiadow = 0

    for k in range(len(dx)):
        sx = (x + dx[k]) % width
        sy = (y + dy[k]) % height
        liczbaSasiadow += earth[sy][sx]
    
    return liczbaSasiadow

wypiszBakt()
loop = True
while loop:
    
    screen.fill((255, 255, 255))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    for y in range(height):
        for x in range(width):

            if earth[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), ((x * cellSize, y * cellSize), (cellSize, cellSize)))

            sasiedzi = policzIleSasiadow(x, y)

            if earth[y][x] == 1:
                if sasiedzi > 3 or sasiedzi < 2:
                    state[y][x] = 0
            else:
                if sasiedzi == 3:
                    state[y][x] = 1
    
    earth = state
    wypiszBakt()
    pygame.display.flip()
    pygame.time.delay(2500)