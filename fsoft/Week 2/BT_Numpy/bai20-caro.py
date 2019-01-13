import pygame
from pygame.locals import *
import numpy as np
import sys

XO   = 2

grid = np.ones(99).reshape(11,9)
winner = None


def initBoard(ttt):
   
    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    for i in range(9):
        pygame.draw.line (background, (0,0,0), (60*(i+1), 0), (60*(i+1), 660), 2)

    for i in range(11):
        pygame.draw.line (background, (0,0,0), (0, 60*(i+1)), (660, 60*(i+1)), 2)

    return background


def showBoard (ttt, board):

    ttt.blit (board, (0, 0))
    pygame.display.flip()
    
def boardPos (mouseX, mouseY):

    if (mouseY < 60):
        row = 0
    elif (mouseY < 120):
        row = 1
    elif (mouseY < 180):
        row = 2
    elif (mouseY < 240):
        row = 3
    elif (mouseY < 300):
        row = 4
    elif (mouseY < 360):
        row = 5
    elif (mouseY < 420):
        row = 6
    elif (mouseY < 480):
        row = 7
    elif (mouseY < 540):
        row = 8
    elif (mouseY < 600):
        row = 9
    else:
        row = 10


    if (mouseX < 60):
        col = 0
    elif (mouseX < 120):
        col = 1
    elif (mouseX < 180):
        col = 2
    elif (mouseX < 240):
        col = 3
    elif (mouseX < 300):
        col = 4
    elif (mouseX < 360):
        col = 5
    elif (mouseX < 420):
        col = 6
    elif (mouseX < 480):
        col = 7
    else:
        col = 8

    return (row, col)

def drawMove(board, boardRow, boardCol, Piece):

    centerX = ((boardCol) * 60) + 30
    centerY = ((boardRow) * 60) + 30

    if (Piece == 0):
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 22, 2)
    else:
        pygame.draw.line (board, (0,0,0), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 2)

    grid [boardRow][boardCol] = Piece
    
def clickBoard(board):

    global grid, XO
    
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    if ((grid[row][col] == 2) or (grid[row][col] == 0)):
        return

    drawMove (board, row, col, XO)

    
def gameAI(board):
    
    global grid, winner
    list_temp = [(x,y) for x in range(11) for y in range(9) if grid[x][y] ==1]
    random_choice = list_temp[np.random.choice(len(list_temp))]

    drawMove(board,random_choice[0], random_choice[1],  0)

def checkWinner(board):

    global grid, winner
    # check ngang
    for i in range(len(grid)):
        for j in range(len(grid[i])-4):
            if grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] != 1:
                return True

    #check doc
    for i in range(len(grid)-4):
        for j in range(len(grid[i])):
            if grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j] != 1:
                return True

    #check cheo trai sang phai
    for i in range(len(grid)-4):
        for j in range(len(grid[i]) - 4):
            if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] != 1:
                return True


    #check cheo phai sang trai
    for i in range(3, len(grid)):
        for j in range(len(grid[i]) - 4):
            if grid[i][j] == grid[i-1][j+1] == grid[i-2][j+2] == grid[i-3][j+3] != 1:
                return True

pygame.init()
ttt = pygame.display.set_mode ((540, 700))
pygame.display.set_caption ('Tic-Tac-Toe')

board = initBoard (ttt)

running = 1
var_run = 0
while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN and var_run == 1:
            clickBoard(board)
            var_run = 0
            
        if var_run == 0:
            gameAI(board)
            if checkWinner(board) == True:
                running = 0

        showBoard (ttt, board)
        var_run = 1
import time
time.sleep(20)