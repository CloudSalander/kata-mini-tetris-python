from classes.Move import Move
from classes.Board import Board
BOARD_ROWS = 10
BOARD_COLUMNS = 10
MOVE_MSG = "Next move!"
AVAILABLE_MOVES = ["1-DOWN","2-LEFT","3-RIGHT","4-ROTATE"]

def writeAvailableMoves():
    for available_move in AVAILABLE_MOVES:
        print(available_move)

def isRightMove(move):
    if move > 0 and move < 5: return True 
    return False

move = -1
board = Board(BOARD_ROWS,BOARD_COLUMNS)
board.play()

while move != 0:
    writeAvailableMoves()
    move = int(input("Enter movement"))
    if(isRightMove(move)): 
        board.play(Move(move))
