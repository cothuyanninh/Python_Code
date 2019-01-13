from boardPos import *
from showBoard import *

def click_board_on_left_mouse(board):
    global grid
    (mouseX1, mouseY1) = pygame.mouse.get_pos()
    (row1, col1) = boardPos (mouseX1, mouseY1)
    diem1 =  [(row1, col1)]
    # print("Toa do diem chon: ")
    # print(diem1)
    # print("Voi gia tri: %s"%grid[row1][col1])
    diem1.append(grid[row1][col1])
    # print(grid[row1][col1][1])
    return diem1

def click_board_on_right_mouse(board):
    global grid
    
    (mouseX2, mouseY2) = pygame.mouse.get_pos()
    (row2, col2) = boardPos (mouseX2, mouseY2)
    diem2 = [(row2, col2)]
    # print("Toa do diem den: ")
    # print(diem2)
    # print("Voi gia tri den: %s"%grid[row2][col2])
    diem2.append(grid[row2][col2])
    # print(diem2)
    return diem2

def check_winer ():
    global grid
    if grid[1][4][0] != 0: 
        return False
    if grid[9][4][0] != 0:
        return False