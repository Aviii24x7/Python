# PROJECT 1:- Making An Interactive TIC-TAC-TOE game

# IMPORTING RANDOM TO A FAIR AND RANDOM CHANCE FOR BOTH PLAYER
import random

# IMPORTING OS FOR CLEARING THE SCREEN OF TERMINAL EVERTIME THE BOARD GETS UPDATE
import os

# DISPLAYING FUNCTION FOR THE GAME BOARD

def display_board(board):

    # CLEARING SCREEN
    os.system('cls')

    print('')
    print("\t"*6 + "    |   |")
    print("\t"*6 + "  " + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("\t"*6 + "    |   |")
    print("\t"*6 + "-------------")
    print("\t"*6 + "    |   |")
    print("\t"*6 + "  " + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("\t"*6 + "    |   |")
    print("\t"*6 + "-------------")
    print("\t"*6 + "    |   |")
    print("\t"*6 + "  " + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("\t"*6 + "    |   |")
    print('\n')


display_board([' ']*10)

# ASKING THE PLAYERS CHOICE IS X OR O

def user_input():

    mark = ''

    # IF THE INPUT IS NOT X OR O KEEP ASKING TO CHOSE
    while mark not in ['X', 'O']:
        mark = input('PLAYER 1: What do you want to chose(X OR O) :').upper()

    # ASSIGNING THE MARKS TO BOTH PLAYERS
    if mark == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

# PLACING THE MARKER TO THE POSTION CHOSE BY PLAYERS

def place_mark(board, position, mark):

    board[position] = mark


# CHECCKING IF ANY PLAYER HAS WON THE GAME

def win_check(board, mark):

    return((board[1] == mark and board[2] == mark and board[3] == mark) or      # row1
           (board[4] == mark and board[5] == mark and board[6] == mark) or      # row2
           (board[7] == mark and board[8] == mark and board[9] == mark) or      # row3
           (board[1] == mark and board[4] == mark and board[7] == mark) or      # column1
           (board[2] == mark and board[5] == mark and board[8] == mark) or      # column2
           (board[3] == mark and board[6] == mark and board[9] == mark) or      # column3
           (board[1] == mark and board[5] == mark and board[9] == mark) or      # diagonal1
           (board[3] == mark and board[5] == mark and board[7] == mark))        # diagonal2


# CHOSING WHICH PLAYER WILL CHOSE FIRST FOR THE MARK

def first_turn():

    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

# CHECKING IF THE BOARD HAVE THE CHOSED POSITION AS A BLANK

def space_chk(board, position):

    return board[position] == ' '

# CHECKING IF THE BOARD HAS FILLED ALL SPACE AND THE GAME IS DRAW

def full_board(board):
    for i in range(1, 10):
        if space_chk(board, i):
            return False
    return True

#ASKING FOR PLAYERS CHOICE FOR NEXT MARK

def player_choice(board):

    position = 0
    # index position should be from 1-9 and also the space should be vacant or unused
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_chk(board, position):
        position = int(input('\nEnter The next Position(1-9): '))
    return position

# RETURNS TRUE IF THE ANSWER IS 'Y' TO THE PLAY AGAIN

def play_again():

    return input('\nTo Play again type YES______OR press any other key to EXIT:  ').lower().startswith('y')


# MAIN FUNCTION

while True:
    # '@' BEACASUE INDEX ZERO CANT BE EMPTY
    updated_board = ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print('\t\t\t\tWelcome to the TIC-TAC-TOE game!!!\n')

    # TUPLE UNPACKING THE FUNCTION RETURNS AND ASSIGNING MARKERS
    player1_marker, player2_marker = user_input()

    turn = first_turn()
    print('\n' + turn + ' will play the first')

    # MAKING A BOOL TO KNOW IF THE GAME SHOULD BE CONTINUED OR NOT

    play_game = input('\nAre you ready to play? Enter Yes or No.:')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        # PLAYER 1's TURN
        if turn == 'player1':

            new_index = player_choice(updated_board)                    #ASKING FOR THE PLAYER1 MARKER INDEX
            place_mark(updated_board, new_index, player1_marker)        #PLACING THE MARKER AT THE INDEX
            display_board(updated_board)                                #DISPLAYING THE UPDATED BOARD WITH NEW MARK

            #IF THE PLAYER 1 WIN, CONGRATULATE AND BREAK THE LOOP
            if win_check(updated_board, player1_marker):
                display_board(updated_board)
                print('\nWOHOOO!! PLAYER 1 has won the Game!')
                game_on = False

            else:
                #IF THE BOARD IS FULL AND NO ONE WIN, DRAW THE GAME AND BREAK THE LOOP
                if full_board(updated_board):
                    display_board(updated_board)
                    print('\nThe game is DRAW!!')
                    break
                #GOING TO THE OTHER PLAYER'S TURN
                else:
                    turn = 'player2'

        # PLAYER 2's TURN
        if turn == 'player2':

            new_index = player_choice(updated_board)                    #ASKING FOR THE PLAYER1 MARKER INDEX
            place_mark(updated_board, new_index, player2_marker)        #PLACING THE MARKER AT THE INDEX
            display_board(updated_board)                                #DISPLAYING THE UPDATED BOARD WITH NEW MARK

            #IF THE PLAYER 2 WIN, CONGRATULATE AND BREAK THE LOOP
            if win_check(updated_board, player2_marker):
                display_board(updated_board)
                print('\nWOHOOO!! PLAYER 2 has won the Game!')
                game_on = False

            else:
                #IF THE BOARD IS FULL AND NO ONE WIN, DRAW THE GAME AND BREAK THE LOOP
                if full_board(updated_board):
                    display_board(updated_board)
                    print('\nThe game is DRAW!!')
                    break
                else:
                    #GOING BACK TO THE OTHER PLAYER'S TURN
                    turn = 'player1'

    #AFTER THE LOOP BREAKS DUE TO DRAW OR WIN THE GAME, ASKING USER TO PLAY AGAIN, IF NOT THEN EXIT OF THE PROGRAM
    if not play_again():
        break
    
