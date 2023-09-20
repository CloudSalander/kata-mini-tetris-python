from classes.Piece import Piece

class Board:

    EMPTY_SQUARE= chr(int('000' + '2B1C', 16))
    BUSY_SQUARE = chr(int('000' + '2B1B', 16))

    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__piece = Piece()

    def draw(self, move = None):
        if type(move) != None: print(move)  
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
