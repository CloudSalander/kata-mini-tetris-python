from classes.Position import Position 

class Piece:
    def __init__(self):
        self.__positions = []
        self.__positions.append(Position(4,0))
        self.__positions.append(Position(4,1))
        self.__positions.append(Position(5,1))
        self.__positions.append(Position(6,1))

    def hasPieceInPosition(self,x,y):
        for position in self.__positions:
            if position.x == x and position.y == y: return True  
        return False