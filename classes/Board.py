from classes.Piece import Piece
from classes.Move import Move

class Board:

    EMPTY_SQUARE= chr(int('000' + '2B1C', 16))
    BUSY_SQUARE = chr(int('000' + '2B1B', 16))

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__piece = Piece()

    def play(self, move = None):
        if type(move) != None: self.__movePiece(move)
        self.__draw()
        
    def __draw(self):
        rows_count = 0
        while rows_count < self.__rows:
            self.__drawRow(rows_count)
            rows_count += 1
		
    def __drawRow(self, current_row):
        current_column = 0 
        while current_column < self.__columns:
            char_to_print = self.EMPTY_SQUARE
            if self.__piece.hasPieceInPosition(current_column,current_row):
                char_to_print = self.BUSY_SQUARE
            print(char_to_print,end="")
            current_column += 1
        print("")

    def __movePiece(self,move):
        if self.__piece.isLastRow(self.__rows) == False:
            if move == Move.DOWN:
                print("HOLA!")
                self.__piece.moveDown()
            
