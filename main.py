import random

import time
import random
import copy
import sys
import pygame
from pygame.locals import KEYDOWN, K_q

SCREENSIZE = WIDTH, HEIGHT = 1000, 1000 # tamnho  da tela em pixeis
BLACK = (255,255, 255) # cores
RED = (255,255, 0) # cores
GREY = (0, 0,0 ) # cores
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 60, 60 #margem
# VARS:
_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (20, 20), 'gridCells': 5, 'lineWidth': 2}

def drawGrid(divisions):
    CONTAINER_WIDTH_HEIGHT = 3000  # Not to be confused with SCREENSIZE
    cont_x, cont_y = 10, 10  # TOP LEFT OF CONTAINER

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), 2)
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), 2)
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, CONTAINER_WIDTH_HEIGHT + cont_y), 2)

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT / divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x + (cellSize * x), cont_y),
            (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
        # # HORIZONTAl DIVISIONS
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x, cont_y + (cellSize * x)),
            (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize * x)), 2)


def setUniverse(sizeOfUniverse = 300):

    universe = [[0 for j in range(sizeOfUniverse)] for i in range(sizeOfUniverse)]

    return universe

def buildGilderat(universe,r,c):
    sizeUniverse = len(universe)

    universe[r][c] = 1
    universe[(r + 1) % sizeUniverse][(c + 1) % sizeUniverse] = 1
    universe[(r + 1) % sizeUniverse][(c + 2) % sizeUniverse] = 1
    universe[r][(c + 2) % sizeUniverse] = 1
    universe[r - 1][(c + 2) % sizeUniverse] = 1
    #universe[r + 1][c + 1] = 1
    #universe[r + 1][c + 2] = 1
   #universe[r][c + 2] = 1
   #universe[r - 1][c + 2] = 1

def randomState(universe,r,c):

    #buildGilderat(universe,14,14)
   # buildGilderat(universe, 8, 8)
    for i in range(r):
        for j in range(c):
            universe[i][j] = random.randint(1,100) % 2



def initalState(universe):

    randomState(universe,300,300)
    #buildGilderat(universe,14,14)
    #buildGilderat(universe,5,8)

def checkNeighbours(universe,x,y):
    sizeOfUniverse = len(universe)
    aliveNeighbours = 0

    if universe[(x + 1) % sizeOfUniverse][y] == 1: # baixo

        aliveNeighbours += 1

    if universe[(x + 1) % sizeOfUniverse][y - 1] == 1: # diag esq inf

        aliveNeighbours += 1

    if universe[(x + 1) % sizeOfUniverse][(y + 1) % sizeOfUniverse] == 1: #diag dir inf
        aliveNeighbours += 1

    if universe[x][(y + 1) % sizeOfUniverse] == 1: # dir

        aliveNeighbours += 1

    if universe[x][y - 1] == 1: # esq

        aliveNeighbours += 1

    if universe[x - 1][y] == 1: # em cima

        aliveNeighbours += 1

    if universe[x - 1][y - 1] == 1: # diag esq sup

        aliveNeighbours += 1

    if universe[(x - 1)][(y + 1) % sizeOfUniverse] == 1: # diag dir sup

        aliveNeighbours += 1

    return aliveNeighbours

def applyRules(alive,neighbours,universe, x, y):
    flag = False

    if alive == 1 and neighbours > 3:    #superpopulação
        universe[x][y] = 0      #solidão
        flag = True

    if alive == 1 and neighbours < 2:
        universe[x][y] = 0
        flag = True

    if alive == 0 and neighbours == 3: #ressucita
        universe[x][y] = 1
        flag = True

    return flag

'''def applyRules(alive,neighbours,universe, x, y):
    flag = False
    if neighbours > 4:
        universe[x][y] = 0
        flag = True
    if neighbours < 4:
        universe[x][y] = 1
        flag = True
    return flag '''




def setState(universe,copy):
    #changed = 0
    for i in range(len(universe)):
        for j in range(len(universe)):
            neighbours = checkNeighbours(copy,i,j)
            applyRules(universe[i][j],neighbours, universe, i, j)
                #print(changed)
                #changed += 1
    #print(changed)
    #return changed > 0

def printUniverse(universe):
    for i in range(len(universe)):
        for j in range(len(universe)):
            print(universe[i][j],end=" ")
        print("\n")

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

def drawRectTrans(x,y,universe):
    SquareSize =  3000 / len(universe)
    pygame.draw.rect(

        _VARS['surf'], RED,
        (10 + x * SquareSize, 10 + y * SquareSize, SquareSize, SquareSize))

def drawRect(x,y,universe):
    SquareSize =  3000 / len(universe)
    pygame.draw.rect(

        _VARS['surf'], BLACK,
        (10 + x * SquareSize, 10 + y * SquareSize, SquareSize, SquareSize))

def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    universe = setUniverse()
    prev = setUniverse()
    initalState(universe)
    initalState(prev)
    sizeUniverse = len(universe)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        for i in range(sizeUniverse):
            for j in range(sizeUniverse):
                if universe[i][j] == 1:
                    drawRectTrans(j,i,universe)
        setState(universe,prev)
        time.sleep(0.1)
        for i in range(sizeUniverse):
            for j in range(sizeUniverse):
                if universe[i][j] == 1:
                    drawRect(j,i,universe)
        setState(universe,prev)
        prev = copy.deepcopy(universe)
        drawGrid(sizeUniverse)
        pygame.display.update()


    #print("ESTADO INICIAL: \n")
    #printUniverse(universe)
    setState(universe,prev)
if __name__ == '__main__':
    main()