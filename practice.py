# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# marker1 = ''
# marker2 = ''
# win = ''


# def print_board():
#     print('\n'+board[0]+'|'+board[1]+'|'+board[2])
#     print("-|-|-")
#     print(board[3]+'|'+board[4]+'|'+board[5])
#     print("-|-|-")
#     print(board[6]+'|'+board[7]+'|'+board[8]+'\n')


# def input_board():
#     marker1 = input("Player 1 choose your marker : X or O").upper()

#     if marker1 == 'X':
#         marker2 = 'O'
#     else:
#         marker2 = 'X'

#     print("Player 1 goes first")

#     turn = 1

#     while check_empty() == True:
#         print_board()
#         inp2 = 0

#         pos = int(
#             input("Enter the box number in which you want to place your marker: \n"))
#         if board[pos-1] != ' ':
#             inp2 = 1
#             print("Box occupied.")

#         else:
#             if turn % 2 != 0:
#                 board[pos-1] = marker1
#             else:
#                 board[pos-1] = marker2

#         if inp2 == 1:
#             continue
#         else:
#             turn += 1
#             inp2 = 0

#         def check_win(marker):
#             return ((board[0] == board[1] == board[2] == marker) or
#                      (board[3] == board[4] == board[5] == marker) or
#                      (board[6] == board[7] == board[8] == marker) or
#                      (board[0] == board[3] == board[6] == marker) or
#                      (board[1] == board[4] == board[7] == marker) or
#                      (board[2] == board[5] == board[8] == marker) or
#                      (board[0] == board[4] == board[8] == marker) or
#                      (board[2] == board[4] == board[6] == marker)  )
        

#         if check_win(marker1) == True:
#             winner('player 1')
#             break
#         elif check_win(marker2) == True:
#             winner('player 2')
#             break
#         elif turn == 10 and check_win != True:
#             print("Tie game!")


# def check_empty():
#     count = 0
#     for i in range(len(board)):
#         if board[i] == '':
#             count+=1
    
#     if count == 0:
#         return False
#     else:
#         return True


# def winner(win):
#     print_board()
#     print("{} won the game!".format(win))


# input_board()
























# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# marker1 = ''
# marker2 = ''
# win =''

# def print_board():
#     print(f"\n {board[0]} | {board[1]} | {board[2]}")
#     print("-|-|-")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("-|-|-")
#     print(f"{board[6]} | {board[7]} | {board[8]}")


# def input_board():
#     marker1 = input("Player 1 choose the marker X or O\n").uper()

#     if marker1 == 'X':
#         marker2 =='O'

#     else:
#         marker2=='X'
    
#     print("PLayer 1 goes first\n")



# def game():
#     pos = int(input("Enter the position where you want to place the marker\n"))

#     if board[pos-1]!=' ':
#         print("Box occupied\n")

#     else :
#         if 



# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# player = 1
# print("Player 1 [X] --- Player 2 [O]\n")    
# print()    
# print()    
# print("Please Wait...")    
    
# while(True):    
#     #os.system('cls')    
#     DrawBoard()    
#     if(player % 2 != 0):    
#         print("Player 1's chance")    
#         Mark = 'X'    
#     else:    
#         print("Player 2's chance")    
#         Mark = 'O'    
#     choice = int(input("Enter the position between [1-9] where you want to mark : "))    
#     if(CheckPosition(choice)):    
#         board[choice] = Mark    
#         player+=1    
#         CheckWin()    
    
# #os.system('cls')    
# DrawBoard()    
# if(Game==Draw):    
#     print("Game Draw")    
# elif(Game==Win):    
#     player-=1    
#     if(player%2!=0):    
#         print("Player 1 Won")    
#     else:    
#         print("Player 2 Won")






board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("_|_|_")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("_|_|_")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")

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




# board = [1,2,3,4]
# print(f"1.{board[1]} 2. {board[2]}\n")