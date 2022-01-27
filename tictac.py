board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
marker1 = ''
marker2 = ''
win = ''


def print_board():
    print('\n'+board[0]+'|'+board[1]+'|'+board[2])
    print("-|-|-")
    print(board[3]+'|'+board[4]+'|'+board[5])
    print("-|-|-")
    print(board[6]+'|'+board[7]+'|'+board[8]+'\n')


def input_board():
    marker1 = input("Player 1 choose your marker : X or O ").upper()

    if marker1 == 'X':
        marker2 = 'O'

    else:
        marker2 = 'X'

    print('Player 1 goes first.')

    turn = 1

    while check_empty() == True:

        print_board()
        inp2 = 0

        pos = int(
            input("Enter the box number in which you want to place your marker : \n"))

        if board[pos-1] != ' ':
            inp2 = 1
            print("Box occupied.")

        else:
            if turn % 2 != 0:
                board[pos-1] = marker1

            else:
                board[pos-1] = marker2

        if inp2 == 1:
            continue
        else:
            turn += 1
            inp2 = 0

        def check_win(marker):
            return ((board[0] == board[1] == board[2] == marker) or
                    (board[3] == board[4] == board[5] == marker) or
                    (board[6] == board[7] == board[8] == marker) or
                    (board[0] == board[3] == board[6] == marker) or
                    (board[1] == board[4] == board[7] == marker) or
                    (board[2] == board[5] == board[8] == marker) or
                    (board[0] == board[4] == board[8] == marker) or
                    (board[2] == board[4] == board[6] == marker))

        if check_win(marker1) == True:
            winner('Player 1')
            break
        elif check_win(marker2) == True:
            winner('Player 2')
            break
        elif turn == 10 and check_win != True:
            print("Tie game!")


def check_empty():
    count = 0
    for i in range(len(board)):
        if board[i] == ' ':
            count += 1

    if count == 0:
        return False
    else:
        return True


def winner(win):
    print_board()
    print("{} won the game!".format(win))


input_board()