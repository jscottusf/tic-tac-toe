import os
import time
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " ", ""]

#Print the header
def print_header():
    print("""

    TIC-TAC-TOE 1 | 2 | 3
                4 | 5 | 6
                7 | 8 | 9
To play Tic-Tac-Toe, you need to get three in a row...
Your choices are defined, they must be from 1 to 9...

""")

#Define the print_board function
def print_board():
    print ("   |   |   ")
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print ("   |   |   ")
    print ("---|---|---")
    print ("   |   |   ")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print ("   |   |   ")
    print ("---|---|---")
    print ("   |   |   ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print ("   |   |   ")

#Define winning
def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

#Define is board full?
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

#Define clear/print_header/print_board
def clear_print():
    os.system("clear")
    print_header()
    print_board()

#Define get_computer_move(board, player)
def get_computer_move(board, player):
    #Check for win
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = player
            if is_winner(board, player):
                return i
            else:
                board[i] = " "

    #Check for X win:=
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "X"
            if is_winner(board, "X"):
                board[i] = player
                return i
            else:
                board[i] = " "

    #if the center square is empty choose that
    if board[5] == (" "):
        return 5

    #respond appropriately to the X's second move
    #check corners strategy
    for i in range(1, 10):
        if board[1] and board[9] == "X" or \
            board[3] and board[9] =="X":

            move = (random.randint(1,4) * 2)
            if board[move] == " ":
                return move

    #check even number strategy
    if ((board[2] == "X" and board[4] == "X") and board[1] == " ") or \
        ((board[2] == "X" and board[7] == "X") and board[1] == " ") or \
        ((board[3] == "X" and board[4] == "X") and board[1] == " "):
        return 1

    if ((board[2] == "X" and board[6] == "X") and board[3] == " ") or \
        ((board[2] == "X" and board[4] == "X") and board[3] == " ") or \
        ((board[1] == "X" and board[9] == "X") and board[3] == " "):
        return 3

    if ((board[6] == "X" and board[8] == "X") and board[9] == " ") or \
        ((board[2] == "X" and board[4] == "X") and board[9] == " ") or \
        ((board[3] == "X" and board[8] == "X") and board[9] == " "):
        return 9

    if ((board[4] == "X" and board[8] == "X") and board[7] == " ") or \
        ((board[2] == "X" and board[4] == "X") and board[7] == " ") or \
        ((board[1] == "X" and board[8] == "X") and board[7] == " "):
        return 7

    #while True:
    #pick any random odd number except for five
    #not sure if there is a more intuitive way to do this in Python, but it works
    #problem was if it picked 5, it would then pick an even number, which made the computer vulnerable to losing
    move = random.randrange(1,10,2)
    if move == 5:
        move = random.randrange(1,5,2)
    if move == 5:
        move = random.randrange(7,9,2)
    #if move is blank go ahead and return otherise try again
    if board[move] == " ":
        return move
    else:
        move = random.randint(1,10)
        if board[move] == " ":
            return move


#Main loop
while True:
    clear_print()

    #Get player X Input
    while True:
        choice = input("Please choose an empty space for X. ")
        choice = int(choice)

        #Check to see if the space if empty first
        if board[choice] == " ":
            board[choice] = "X"
            break

        else:
            print ("Sorry, that space is not empty")
            time.sleep(1.5)
            clear_print()

    #Check for X win
    if is_winner(board, "X"):
        clear_print()
        print ("X wins! Congratulations!")
        break

    clear_print()

    if is_board_full(board):
        print ("Tie!")
        break

    #Get player O input
    choice = get_computer_move(board, "O")

    #Check to see if the space if empty first
    if board[choice] == " ":
        board[choice] = "O"

    #Check for O win
    if is_winner(board, "O"):
        clear_print()
        print ("\n Computer WINS! \n FIRST, TIC-TAC-TOE. \n NEXT, WORLD DOMINATION!!!!!!!!!!")
        break

    #Check for a tie (is the board full)
    #If the board if full, do something
    if is_board_full(board):
        clear_print()
        print ("Tie!")
        break
