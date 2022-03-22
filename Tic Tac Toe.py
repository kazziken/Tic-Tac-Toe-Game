# Tic Tac Toe

from IPython.display import clear_output

test_board = [' ',' ',' ','',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

display_board(test_board)


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player1_marker, player2_marker = player_input()
player2_marker

def place_marker(board, marker, position):
    
    board[position] = marker

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def win_check(board, mark):
     
    #win Tic tac toe ? check all rows and see if they all share the same marker
    return((board[1] == mark and board[2] == mark and board [3] == mark) or
    (board[4] == mark and board[5] == mark and board [6] == mark) or
    (board[7] == mark and board[8] == mark and board [9] == mark) or
    #another way is
    #(board[4]==board[5]==board[6] == mark)
    
    # all columns, check to see if all markers matches
    (board[1] == mark and board[4] == mark and board [7] == mark) or
    (board[2] == mark and board[5] == mark and board [8] == mark) or
    (board[3] == mark and board[6] == mark and board [9] == mark) or
    # 2 diagonals
    (board[1] == mark and board[5] == mark and board [9] == mark) or
    (board[3] == mark and board[5] == mark and board [7] == mark))


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range (0,10):
        if space_check(board,i):
            return False
    #board is full if we return True
    return True

def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position 1-9: '))
    
    return position

def replay():
    
    choice = input("Play Again? Enter Y/N: ").upper
    
    return choice == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    
    ##Set everything up (board, who is first, choose marker x ,o))
    the_board = [' '] * 10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? Y/N')
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    
    while game_on:    
        #Player 1 Turn
        if turn == 'Player 1':
            #show board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won 
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            
            
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'
            
            #no tie and no win? Then next player's turn

        
        # Player2's turn.
        else:
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if they won 
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            
            
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        print('Okay see you next time!')
        break