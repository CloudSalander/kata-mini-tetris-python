from classes.Move import Move
move = Move.DOWN
while move != 0:
    print("1-DOWN")
    print("2-RIGHT")
    print("3-LEFT")
    print("4-DOWN")
    move = int(input("Enter movement"))