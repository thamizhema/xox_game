board = ["-"]*9



def showBoard():
    for i in range(len(board)):
        print(board[i],end=" ")
        if (i+1) % 3 == 0:
            print()

def userInput(player):
    flag = True
    while flag:
        inp = int(input(f"it's {player} turn : "))
        if (inp>=1 and inp <= 9 and board[inp-1]=="-"  ):
            board[inp-1] = player
            flag = False
        else:
            print("invalid input please try again!")

def gameStatus():
    return "-" in board

def score():
    
    xwin = [
    (board[0] == "X" and board[1] == "X"and board[2]=="X"),
    (board[3] == "X" and board[4] == "X"and board[5]=="X"),
    (board[6] == "X" and board[7] == "X"and board[8]=="X"),
    (board[0] == "X" and board[4] == "X"and board[8]=="X"),
    (board[2] == "X" and board[4] == "X"and board[6]=="X"),
    (board[0] == "X" and board[3] == "X"and board[6]=="X"),
    (board[1] == "X" and board[4] == "X"and board[7]=="X"),
    (board[2] == "X" and board[5] == "X"and board[8]=="X"),
    
    ]
    owin = [
    (board[0] == "O" and board[1] == "O"and board[2]=="O"),
    (board[3] == "O" and board[4] == "O"and board[5]=="O"),
    (board[6] == "O" and board[7] == "O"and board[8]=="O"),
    (board[0] == "O" and board[4] == "O"and board[8]=="O"),
    (board[2] == "O" and board[4] == "O"and board[6]=="O"),
    (board[0] == "O" and board[3] == "O"and board[6]=="O"),
    (board[1] == "O" and board[4] == "O"and board[7]=="O"),
    (board[2] == "O" and board[5] == "O"and board[8]=="O"),
    ]

    if(any(xwin)):
        print("X is win")
        return False
    if(any(owin)):
        
        print("O is win")
        return False

    return True







    
        
