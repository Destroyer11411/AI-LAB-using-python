board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# def DrawBoard():    
#     print(" %c | %c | %c " % (board[1],board[2],board[3]))    
#     print("_|_|_")    
#     print(" %c | %c | %c " % (board[4],board[5],board[6]))    
#     print("_|_|_")    
#     print(" %c | %c | %c " % (board[7],board[8],board[9]))    
#     print("   |   |   ")

def DrawBoard():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def checkposition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False 


def check_win(marker):
    if (board[1] == board[2] == board[3] == marker):
        return True
    elif(board[4] == board[5] == board[6] == marker):
        return True
    elif(board[7] == board[8] == board[9] == marker):
        return True
    elif (board[1] == board[4] == board[7] == marker):
        return True
    elif (board[2] == board[5] == board[8] == marker):
        return True
    elif (board[3] == board[6] == board[9] == marker):
        return True
    elif (board[1] == board[5] == board[9] == marker):
        return True
    elif (board[3] == board[5] == board[7] == marker):
        return True
    else:
        return False


print("Welcome to TIC-TAC-TOE game\n")
print("Player 1 has X marker\n")
print("Player 2 has O marker")

chance = 0
player = 1
turn  = 9
mark = 'X'

while (chance<turn):
    DrawBoard()
    if(player%2!=0):
        print("player 1 turn\n")
        mark = 'X'
    else:
        print("Player 2 turn\n")
        mark = 'O'
    
    choice = int(input("Enter the position where you want to place the marker\n"))
    if (checkposition(choice)):
        board[choice]=mark
        player+=1
        turn-=1
    if check_win('X') == True:
            #winner('Player 1')
            print("Player 1 wins the game\n")
            break
    elif check_win('O') == True:
            #winner('Player 2')
            print("Player 2 wins the game\n")
            break
    # elif turn == 10 and check_win != True:
    #         print("Tie game!")

    if turn == 0:
        print("End of the game\n")
        break