import random

from IPython.display import clear_output

def display_board(board):
    clear_output()  
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_side():
    p1 = ''
    p2 = ''
    acceptable_values = ['X', 'O']
    in_values = False

    while not p1 or not p2 or not in_values:
        side = input('Pick an icon (X or O): ')
        if side == 'X':
            p1 = 'X'
            p2 = 'O'
        elif side == 'O':
            p1 = 'O'
            p2 = 'X'
        else:
            print('Please choose either "X" or "O".')
            continue
        
        if side in acceptable_values:
            in_values = True
        else:
            print('Please choose either "X" or "O".')
            in_values = False
            
    return p1, p2

def player_placement(board, player_pos):
    pos = range(1, 10)
    
    while True:
        position = input('Pick a position between(1-9): ')
        if position.isdigit() and int(position) in pos:
            position = int(position)
            if board[position] == ' ':
               board[position] = player_pos
               break
            else:
               print('Position already taken, choose another position:')
        else:
            print('Enter a valid position(1-9):')
    
    return board

def decide_first_player(player1, player2):
    random_number = random.randint(0, 1)
    first_player = player1 if random_number == 0 else player2
    return first_player

def win_con(board, player_side):
    winner = None
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]

    for combo in winning_combinations:
        if all(board[pos] == player_side for pos in combo):
            winner = player_side
            print(f'{player_side} has won!')
            break
    
    return winner

def full_board_check(board):
    return ' ' not in board[1:]

def gameon_choice():
    choice = 'W'

    while choice not in ['Y', 'N']:
       choice = input('Do you wanna keep playing?[Y - YES or N - NO]')
       
       if choice not in ['Y', 'N']:
          print('Please Enter Y for Yes N for No:')
    
    if choice == 'Y':
        return True
    else:
        print('GGWP!')
        return False

# Function to initialize a new board
def initialize_board():
    return [' '] * 10

# Existing code

game_on = True

player1, player2 = player_side()
current_player = decide_first_player(player1, player2)
print(f"{current_player} goes first.")

while game_on:
    board = initialize_board()  # Initialize a new board for each game
    
    while True:
        print(f"{current_player}'s turn")
        display_board(board)
        board = player_placement(board, current_player)
        
        if win_con(board, current_player):
            print('Game over')
            break
        elif full_board_check(board):
            print('Game over: Board is full')
            break
        else:
            # Switch to the other player's turn
            current_player = player2 if current_player == player1 else player1
    
    game_on = gameon_choice()