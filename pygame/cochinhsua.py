import pygame
from pygame.locals import *

# declare our global variables for the game
XO   = "X"   # track whose turn it is; X goes first
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

# declare our support functions

def initBoard(ttt):
    # initialize the board and return it as a variable
    # ---------------------------------------------------------------
    # ttt : a properly initialized pyGame display variable

    # set up the background surface
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

    # return the board
    return background

def drawStatus (board):
    # draw the status (i.e., player turn, etc) at the bottom of the board
    # ---------------------------------------------------------------
    # board : the initialized game board surface where the status will
    #         be drawn

    # gain access to global variables
    global XO, winner

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
    board.blit(text, (10, 660))

def showBoard (ttt, board):
    # redraw the game board on the display
    # ---------------------------------------------------------------
    # ttt   : the initialized pyGame display
    # board : the game board surface

    drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()
    
def boardPos (mouseX, mouseY):
    # given a set of coordinates from the mouse, determine which board space
    # (row, column) the user clicked in.
    # ---------------------------------------------------------------
    # mouseX : the X coordinate the user clicked
    # mouseY : the Y coordinate the user clicked

    # determine the row the user clicked
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


    # return the tuple containg the row & column
    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):

    centerX = ((boardCol) * 60) + 30
    centerY = ((boardRow) * 60) + 30

    # draw the appropriate piece
    if (Piece == 'O'):
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 22, 2)
    else:
        pygame.draw.line (board, (0,0,0), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 2)

    # mark the space as used
    grid [boardRow][boardCol] = Piece
    
def clickBoard(board):
    # determine where the user clicked and if the space is not already
    # occupied, draw the appropriate piece there (X or O)
    # ---------------------------------------------------------------
    # board : the game board surface
    
    global grid, XO
    
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    # make sure no one's used this space
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
        # this space is in use
        return

    # draw an X or O
    drawMove (board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"
    
def gameWon(board):
    # determine if anyone has won the game
    # ---------------------------------------------------------------
    # board : the game board surface
    
    global grid, winner

    # check for winning rows
    for row in range (0, 3):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            # this row won
            winner = grid[row][0]
            pygame.draw.line (board, (250,0,0), (0, (row + 1)*100 - 50), \
                              (300, (row + 1)*100 - 50), 2)
            break

    # check for winning columns
    for col in range (0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            # this column won
            winner = grid[0][col]
            pygame.draw.line (board, (250,0,0), ((col + 1)* 100 - 50, 0), \
                              ((col + 1)* 100 - 50, 300), 2)
            break

    # check for diagonal winners
    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
       (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]
        pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
       (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
        pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)

# --------------------------------------------------------------------
# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((540, 700))
pygame.display.set_caption ('Tic-Tac-Toe')

# create the game board
board = initBoard (ttt)

# main event loop
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            clickBoard(board)

        # check for a winner
        gameWon (board)

        # update the display
        showBoard (ttt, board)
