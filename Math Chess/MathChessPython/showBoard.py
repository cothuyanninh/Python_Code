import pygame
from pygame.locals import *
from boardPos import *

def initBoard(ttt):

    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    for i in range(1,10):
    	pygame.draw.line (background, (0,0,0), (i*60, 0), (i*60, 660), 2)

    for i in range(1,12):
    	pygame.draw.line (background, (0,0,0), (0, i*60), (660, i*60), 2)

    return background


def showBoard (ttt, board):

    ttt.blit (board, (0, 0))
    pygame.display.flip()


def show_Number(board):

    global grid
    font = pygame.font.Font(None, 50)
    
    for x_doc in range(11):
        for y_ngang in range(9):
            if grid[x_doc][y_ngang][0] == None:
                cicrleDraw(board, (y_ngang)*60+30, (x_doc)*60+30, 25, 250)   
                continue 
            if str(grid[x_doc][y_ngang][1]) == 'X':
                text1 = font.render(str(grid[x_doc][y_ngang][0]), 1, (10, 10, 10))
                board.blit(text1, ((y_ngang)*60+15, (x_doc)*60+15))
            if str(grid[x_doc][y_ngang][1]) == 'Y':
                text2 = font.render(str(grid[x_doc][y_ngang][0]), 1, (255, 0, 0))   
                board.blit(text2, ((y_ngang)*60+15, (x_doc)*60+15))


def cicrleDraw(board, pos_x, pos_y, radian, color):
    pygame.draw.circle (board, (color,color,color), (pos_x, pos_y), radian, radian)   