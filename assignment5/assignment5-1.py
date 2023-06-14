from pyfiglet import Figlet

game_board = [["_","_","_"],
              ["_","_","_"],
              ["_","_","_"]]

player = 1

def show():
    for i in range(3):
        for j in range(3):
            print(game_board[i][j] , end=" ")
        print("\n")

def placement(p , i , j):
    global player
    if 0 <= i < 3 and 0 <= j < 3:
        if game_board[i][j] == "_":
            if p == 1:
                game_board[i][j] = "X"
                player = 2
            else:
                game_board[i][j] = "O"
                player = 1
        else:
            print("\nthe cell is full , select another cell!")
    else:
        print("\nthe cell not found! , please select again")

def check_win():
    for i1 in range(3):
        if game_board[i1][0] == game_board[i1][1] == game_board[i1][2] != "_" or game_board[0][i1] == game_board[1][i1] == game_board[2][i1] != "_":
            return False
    
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "_" or game_board[0][2] == game_board[1][1] == game_board[2][0] != "_" :
        return False

    return True

font = Figlet(font='slant')
print(font.renderText('tic tac toe'))

show()

while check_win():
    user_input = input("player number {} , enter row and col : ".format(player))
    row , col = map(int , user_input.split(","))
    placement(player , row , col)
    show()

if player == 1:
    print("the player number 2 win!")
else:
    print("the player number 1 win!")
   