from classes.Move import Move
from classes.Board import Board
BOARD_ROWS = 10
BOARD_COLUMNS = 10


move = Move.DOWN
board = Board(BOARD_ROWS,BOARD_COLUMNS)
board.draw()

while move != 0:
    print("1-DOWN")
    print("2-RIGHT")
    print("3-LEFT")
    print("4-DOWN")
    move = int(input("Enter movement"))