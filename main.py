#import b
#from b import board,u1
#from b import *

from fun.board import showBoard,userInput,gameStatus,score

run = True
showBoard()
count = 0
while run:
    if(count%2==0):
        pl = "X"
    else:
        pl = "O"
    userInput(pl)
    run = gameStatus()
    showBoard()
    count += 1
    run = score()
    if not run:
        print("Game over")
