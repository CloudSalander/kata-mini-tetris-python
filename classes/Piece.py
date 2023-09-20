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
    
    def isLastRow(self,max_row):
        for position in self.__positions:
            if position.y >= max_row-1: return True  
        return False

    def moveDown(self):
        for position in self.__positions:
            position.y += 1 

    def moveLeft(self):
        if self.__canMoveLeft(): 
            for position in self.__positions:
                position.x -= 1  
        
    def moveRight(self,max_column):
        if self.__canMoveRight(max_column): 
            for position in self.__positions:
                position.x += 1  
    
    def __canMoveLeft(self):
        for position in self.__positions:
            if position.x <= 0: return False  
        return True
    
    def __canMoveRight(self,max_column):
        for position in self.__positions:
            if position.x >= max_column-1: return False  
        return True