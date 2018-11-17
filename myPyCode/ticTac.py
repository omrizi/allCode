from IPython.display import clear_output
#clear_output --> clear the screen

def display_board(board):
    print(" {} |".format(board[0]),end='')
    print(" {} |".format(board[1]),end='')
    print(" {}  ".format(board[2]))
    print("-----------")
    print(" {} |".format(board[3]),end='')
    print(" {} |".format(board[4]),end='')
    print(" {}  ".format(board[5]))
    print("-----------")
    print(" {} |".format(board[6]),end='')
    print(" {} |".format(board[7]),end='')	
    print(" {}  ".format(board[8]))

def isWinner(board):
    if(board[0] ==  board[1] == board[2] and board[0] != " "):
        print("{} won the game".format(board[0]))
        return board[0]
    elif(board[3] ==  board[4] == board[5] and board[3] != " "):
        print("{} won the game".format(board[3]))
        return board[3]
    elif(board[6] ==  board[7] == board[8] and board[6] != " "):
        print("{} won the game".format(board[6]))
        return board[6]
    elif(board[0] ==  board[3] == board[6] and board[0] != " " ):
        print("{} won the game".format(board[0]))
        return board[0]
    elif(board[1] ==  board[4] == board[7] and board[1] != " "):
        print("{} won the game".format(board[1]))
        return board[1]
    elif(board[2] ==  board[5] == board[8] and board[2] != " "):
        print("{} won the game".format(board[2]))
        return board[2]
    elif(board[0] ==  board[4] == board[8] and board[0] != " " ):
        print("{} won the game".format(board[0]))
        return board[0]
    elif(board[2] ==  board[4] == board[6] and board[2] != " "):
        print("{} won the game".format(board[2]))
        return board[2]
    else:return False

player1 = input("Hello player1, chose wether to play as X or as O\n\n")
if(player1 =="X"): player2 ="O"
else: player2 = "X"

print("Player1 is {}".format(player1))
print("Player2 is {}".format(player2))

boardExample = ["0","1","2","3","4","5","6","7","8"]
#board        = [" "," "," "," "," "," "," "," "," "]
board        = [" "]*9

gameOver = False
turn = 1 # 1 = player 1, 2 = player2
move = 0
boardStatus = 0
while(gameOver == False):
    display_board(boardExample)    
    print("\n")
    display_board(board)
    move = int(input(("hey player,write youre move\n\n")))
    if(move > 8 or move < 0 or board[move] != " "):
        print("Wrong Move, try again!")
        continue
    elif(turn == 1):
        board[move] = player1
        turn = 2
        boardStatus += 1
    else:
        board[move] = player2
        turn = 1 
        boardStatus += 1
    gameOver = isWinner(board)
    if(gameOver == True):break
    #print('\n'*100)
    if(boardStatus == 9):
        print('This is a tie!')

print("The winner is {}".format(gameOver))
display_board(board)
