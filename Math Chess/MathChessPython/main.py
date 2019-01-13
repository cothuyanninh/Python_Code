import pygame
from pygame.locals import *
from boardPos import *
from eventProcess import *
from showBoard import *
import logicProcess
from ai import *

pygame.init()
ttt = pygame.display.set_mode ((540, 700))
pygame.display.set_caption ('Co Toan Viet Nam')

board = initBoard (ttt)

running = 1
LEFT = 1
RIGHT = 3
left_point = None
range_list = None
right_point = None
flag =1

while (running == 1):
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        left_click =1
        while left_click == 1:
            left_point = click_board_on_left_mouse(board)
            if left_point[0] != None:
                left_click = 0

        if left_point[0] == None:
            continue

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
        right_click = 1
        while right_click == 1 and right_point != left_point:
            right_point = click_board_on_right_mouse(board)
            if right_point != None :
                right_click = 0
    if (flag == 0):
        if (left_point != None):
            range_list = logicProcess.checkPos(left_point[0], left_point[1][0], left_point[1][1], grid).run()
        if (right_point != None and range_list != None):
            if (right_point[0] in range_list):
                logicProcess.remove(left_point[0], right_point[0], grid)
                flag = 1
        show_Number(board)
        showBoard (ttt, board)

    if (flag == 1):
        list_random = check_all_node(grid)
        logicProcess.remove(list_random[0], list_random[1], grid)
        # print("-----------------------------------------")
        show_Number(board)
        showBoard (ttt, board)
        flag = 0
