from classes.Position import Position 

class Piece:

    ROTATION_INCREMENTALS =  [[[1,-1],[0,0],[1,1],[2,2]],[[1,1],[0,0],[-1,1],[-2,2]],[[-1,1],[0,0],[-1,-1],[-2,-2]],[[-1,-1],[0,0],[1,-1],[2,-2]]]

    def __init__(self):
        self.__positions = []
        self.__positions.append(Position(4,0))
        self.__positions.append(Position(4,1))
        self.__positions.append(Position(5,1))
        self.__positions.append(Position(6,1))
        self.__status = 1

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

    def rotate(self,max_row, max_column):
        new_status = self.__changeStatus()
        if self.__canRotate(max_row,max_column,new_status-1):
            self.__status = new_status
            i = 0
            while i < len(self.__positions):
                self.__positions[i].x += self.ROTATION_INCREMENTALS[self.__status-1][i][0]
                self.__positions[i].y += self.ROTATION_INCREMENTALS[self.__status-1][i][1]
                i+=1  
    
    def __canMoveLeft(self):
        for position in self.__positions:
            if position.x <= 0: return False  
        return True
    
    def __canMoveRight(self,max_column):
        for position in self.__positions:
            if position.x >= max_column-1: return False  
        return True
    
    def __changeStatus(self):
        if self.__status == 4: return 1
        return self.__status + 1
    
    def __canRotate(self,max_row,max_column,status):
        i = 0
        print(status)
        while i < len(self.__positions):
            column_variation = self.__positions[i].x + self.ROTATION_INCREMENTALS[status][i][0]
            row_variation = self.__positions[i].y + self.ROTATION_INCREMENTALS[status][i][1]
            #print(column_variation)
            #print(row_variation)
            if (column_variation  < 0 or column_variation >= max_column) or (row_variation < 0 or row_variation >= max_row): return False
            i += 1
        return True