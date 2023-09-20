class Board:
    def __init__(self,rows,columns):
        self.__rows = rows
        self.__columns = columns

    def draw(self):  
        rows_count = 0
        while rows_count < self.__rows:
            self.__drawDashesLine()
            rows_count += 1
		
    def __drawDashesLine(self):
        columns_count = 0 
        while columns_count < self.__columns:
            print("_|",end="")
            columns_count += 1
        print("")
