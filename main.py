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
    if (move.isnumeric()) and  int(move) >= 0 and int(move) < 5: return True 
    return False

move = -1
board = Board(BOARD_ROWS,BOARD_COLUMNS)
board.play()

while move != "0":
    writeAvailableMoves()
    move = input("Enter movement")
    if(isRightMove(move) and move!= "0"): 
            board.play(Move(int(move)))
