import pygame
from pygame.locals import *
from boardPos import boardPos
  
grid = [ [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], \
         [ None, None, None, None, None, None, None, None, None], ]

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

def setInit( board):
   message = 9
   pos_A = 20
   pos_B = 20

   for i in range(9):
    
      font = pygame.font.Font(None, 50)
      text1 = font.render(str(message), 1, (10, 10, 10))
      text2 = font.render(str(10-message), 1, (255, 0, 0))
      board.blit(text1, (pos_A, 20))
      board.blit(text2, (pos_B, 620))
      pos_A += 60
      pos_B += 60
      grid[0][i] = message
      grid[10][i] = 10-message
      message -= 1 

   text3 = font.render(str(0), 1, (10, 10, 10))
   text4 = font.render(str(0), 1, (255, 0, 0))
   board.blit(text3, (260, 80))
   board.blit(text4, (260, 560))
   grid[1][4] = 0
   grid[9][4] = 0
   pygame.display.flip()

def drawStatus (board):
    # draw the status (i.e., player turn, etc) at the bottom of the board
    # ---------------------------------------------------------------
    # board : the initialized game board surface where the status will
    #         be drawn

    # gain access to global variables
    global XO , winner
    XO = '1'
    # determine the status message
    if (winner is None):
        message = XO + "'s turn"
    else:
        message = winner + " won!"
        
    # render the status message
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    # copy the rendered message onto the board
    # board.fill ((250, 250, 250), (0, 300, 300, 25))
    board.blit(text, (20, 680))


def showBoard (ttt, board):

    ttt.blit (board, (0, 0))
    pygame.display.flip()

def drawMove (board, left, right):

   centerX = right[1]*60 +20
   centerY = right[0]*60 +20
   centerX1 = left[1]*60 +30
   centerY1 = left[0]*60 +30
   font = pygame.font.Font(None, 50)
   text5 = font.render(str(grid[left[0]][left[1]]), 1, (10, 10, 10))
   board.blit(text5, (centerX, centerY))
   grid[right[0]][right[1]] = str(grid[left[0]][left[1]])
   grid[left[0]][left[1]] = None
   pygame.draw.circle (board, (250,250,250), (centerX1, centerY1), 25, 25)


def cicrleDraw(board, pos_x, pos_y):
   pygame.draw.circle (board, (250,250,250), (pos_x, pos_y), 25, 25)

def circleDrawForWord(board, pos_x, pos_y):
  pygame.draw.circle(board, (250, 250, 250) , (pos_x, pos_y), 25, 25)

def clickBoard1(board):

    global grid
    (mouseX1, mouseY1) = pygame.mouse.get_pos()
    (row1, col1) = boardPos (mouseX1, mouseY1)
    # if ((grid[row][col] == '0') or (grid[row][col] == None)):
    #     # this space is in use
    #     return
    diem1 =  (row1, col1)
    print("Toa do diem chon: ")
    print(diem1)
    print("Voi gia tri: %s"%grid[row1][col1])
    return diem1


def clickBoard2(board):

    global grid
    
    (mouseX2, mouseY2) = pygame.mouse.get_pos()
    (row2, col2) = boardPos (mouseX2, mouseY2)
    # if (grid[row2][col2] != None):
    #   return
    #     # this space is in usereturn
    diem2 = (row2, col2)
    print("Toa do diem den: ")
    print(diem2)
    # print("Voi gia tri den: %d"%grid[row2][col2])
    return diem2

def checkRoad(diem1, diem2):
   #check hang Doc
  if (diem1[1] == diem2[1]) and abs(int(diem1[0]) - int(diem2[0])) <= int(str(grid[diem1[0]][diem1[1]])):
    # 
    print("Di theo chieu doc")
    return True
   #check hang Ngang
  if (diem1[0] == diem2[0]) and abs(int(diem1[1]) - int(diem2[1])) <= int(str(grid[diem1[0]][diem1[1]])):
    return True
   # check an Doc
  if (diem1[1] == diem2[1]):
    if int(str(grid[diem1[0]+1][diem1[1]])) != 0 and diem1[0] <= 9:
      if (int(str(grid[diem1[0]][diem1[1]])) + int(str(grid[diem1[0]+1][diem1[1]])))%10 == diem2[1]+1 :
        cicrleDraw(board, diem2[1]*60+30, diem2[0]*60+30)
        return True

   # #check neu co con ben canh se khong cho di theo chieu doc
   # if (diem1[1] == diem2[1]):
   #    if int(grid[diem1[0]+1][diem1[1]]) != 0: #or int(grid[diem1[0]-1][diem1[1]]) != 0:
   #       return False


  print("Khong di duoc")
  return False

def checkWin(board):
   if grid[1][4] != 0 or grid[9][4] != 0:
      return 0

pygame.init()
ttt = pygame.display.set_mode ((540, 700))
pygame.display.set_caption ('Co Toan Viet Nam')

# create the game board
board = initBoard (ttt)
setInit(board)
# main event loop
running = 1
LEFT = 1
RIGHT = 3
ahihi = 0
while (running == 1):
   event = pygame.event.poll()
   if event.type == pygame.QUIT:
      running = 0
   elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
      left_point = clickBoard1(board)
   elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
      right_point = clickBoard2(board)
      checkRoad(left_point, right_point)
      if checkRoad(left_point, right_point) == True and right_point != left_point:
         drawMove(board, left_point, right_point)
         if ahihi %2 == 0:
          XO = '1'
         else:
          circleDrawForWord(board, 20, 680)
          XO = '2'
          circleDrawForWord(board, 20, 680)

         
      else :
         print("Khong di duoc")
      ahihi += 1

   drawStatus(board)
   showBoard (ttt, board)
   if checkWin(board) == 0:
      running =0
   
