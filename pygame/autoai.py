import pygame
from pygame.locals import *
from boardPos import boardPos

grid = [[ [9,'X'], [8, 'X'], [7, 'X'], [6, 'X'], [5, 'X'], [4, 'X'], [3, 'X'], [2, 'X'], [1, 'X']], \
        [ [None,None], [None,None], [None,None], [None,None], [0, 'X'], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None], [None,None]], \
        [ [None,None], [None,None], [None,None], [None,None], [0, 'Y'], [None,None], [None,None], [None,None], [None,None]], \
        [ [1, 'Y'], [2, 'Y'], [3, 'Y'], [4, 'Y'], [5, 'Y'], [6, 'Y'], [7, 'Y'], [8, 'Y'], [9, 'Y']], ]

winner = None

def initBoard(ttt):

    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    # draw the grid lines
    # vertical lines...
    pygame.draw.line (background, (0,0,0), (60, 0), (60, 660), 2)
    pygame.draw.line (background, (0,0,0), (120, 0), (120, 660), 2)
    pygame.draw.line (background, (0,0,0), (180, 0), (180, 660), 2)
    pygame.draw.line (background, (0,0,0), (240, 0), (240, 660), 2)
    pygame.draw.line (background, (0,0,0), (300, 0), (300, 660), 2)
    pygame.draw.line (background, (0,0,0), (360, 0), (360, 660), 2)
    pygame.draw.line (background, (0,0,0), (420, 0), (420, 660), 2)
    pygame.draw.line (background, (0,0,0), (480, 0), (480, 660), 2)
    pygame.draw.line (background, (0,0,0), (540, 0), (540, 660), 2)

    # horizontal lines...
    pygame.draw.line (background, (0,0,0), (0, 60), (660, 60), 2)
    pygame.draw.line (background, (0,0,0), (0, 120), (660, 120), 2)
    pygame.draw.line (background, (0,0,0), (0, 180), (660, 180), 2)
    pygame.draw.line (background, (0,0,0), (0, 240), (660, 240), 2)
    pygame.draw.line (background, (0,0,0), (0, 300), (660, 300), 2)
    pygame.draw.line (background, (0,0,0), (0, 360), (660, 360), 2)
    pygame.draw.line (background, (0,0,0), (0, 420), (660, 420), 2)
    pygame.draw.line (background, (0,0,0), (0, 480), (660, 480), 2)
    pygame.draw.line (background, (0,0,0), (0, 540), (660, 540), 2)
    pygame.draw.line (background, (0,0,0), (0, 600), (660, 600), 2)
    pygame.draw.line (background, (0,0,0), (0, 660), (660, 660), 2)


    return background

# def setDefaultTable(board):
def cicrleDraw(board, pos_x, pos_y):
    pygame.draw.circle (board, (250,250,250), (pos_x, pos_y), 25, 25)   

def showBoard (ttt, board):

    # drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()

def show_Number(board):
    global grid
    font = pygame.font.Font(None, 50)
    
    for x_doc in range(11):
        for y_ngang in range(9):
            if grid[x_doc][y_ngang][0] == None:
                cicrleDraw(board, (y_ngang)*60+30, (x_doc)*60+30)   
                continue 
            if str(grid[x_doc][y_ngang][1]) == 'X':
                text1 = font.render(str(grid[x_doc][y_ngang][0]), 1, (10, 10, 10))
                board.blit(text1, ((y_ngang)*60+15, (x_doc)*60+15))
            if str(grid[x_doc][y_ngang][1]) == 'Y':
                text2 = font.render(str(grid[x_doc][y_ngang][0]), 1, (255, 0, 0))   
                board.blit(text2, ((y_ngang)*60+15, (x_doc)*60+15))

def show_Init_Board(board):
    pos_x, pos_y, pos_space = 20, 20, 60
    
def click_board_on_left_mouse(board):
    global grid
    (mouseX1, mouseY1) = pygame.mouse.get_pos()
    (row1, col1) = boardPos (mouseX1, mouseY1)
    diem1 =  (row1, col1)
    print("Toa do diem chon: ")
    print(diem1)
    print("Voi gia tri: %s"%grid[row1][col1])
    return diem1

def click_board_on_right_mouse(board):
    global grid
    
    (mouseX2, mouseY2) = pygame.mouse.get_pos()
    (row2, col2) = boardPos (mouseX2, mouseY2)
    diem2 = (row2, col2)
    print("Toa do diem den: ")
    print(diem2)
    print("Voi gia tri den: %s"%grid[row2][col2])
    return diem2

def checkRoad(diem1, diem2):
    #check hang doc
    if (diem1 == diem2):
        return False
    if (diem1[1] == diem2[1]) and abs(int(diem1[0]) - int(diem2[0])) <= int(str(grid[diem1[0]][diem1[1]][0])):
        # for i in range(min(int(diem1[0]), int(diem2[0])), max(int(diem1[0]), int(diem2[0])) ):
        #     if grid[i+1][diem1[1]] != None :
        #         return False
        return True

   #check hang Ngang
    if (diem1[0] == diem2[0]) and abs(int(diem1[1]) - int(diem2[1])) <= int(str(grid[diem1[0]][diem1[1]][0])):
        return True

    #check an theo hang doc
    # if diem1[0]!= 9:
    #     if grid[diem1[0]+1][diem1[1]] != None and diem1[1] == diem2[1] :
    #         if int(grid[diem1[0]][diem1[1]][0]) + int (grid[diem1[0]+1][diem1[1]][0]) == int(grid[diem2[0]][diem2[1]][0]):
    #             cicrleDraw(board, diem2[1]*60+30, diem2[0]*60+30)
    #             return True


    return False

#main
pygame.init()
ttt = pygame.display.set_mode ((540, 700))
pygame.display.set_caption ('Co Toan Viet Nam')

# create the game board
board = initBoard (ttt)

# main event loop
player = 1
running = 1
LEFT = 1
RIGHT = 3
left_point = None
while (running == 1):
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        left_click =1
        while left_click == 1:
            left_point = click_board_on_left_mouse(board)
            if left_point != None:
                left_click = 0

        if left_point == None:
            continue

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
        right_click = 1
        while right_click == 1:
            right_point = click_board_on_right_mouse(board)
            # if right_point = left_point :
            #     continue
            if right_point != None :
                right_click = 0

        if checkRoad(left_point, right_point) == True:
               grid[right_point[0]][right_point[1]][0] = grid[left_point[0]][left_point[1]][0]
               grid[right_point[0]][right_point[1]][1] = grid[left_point[0]][left_point[1]][1]
               grid[left_point[0]][left_point[1]][0] = None
        else:
            print("Khong dung")
    show_Number(board)
    showBoard (ttt, board)
