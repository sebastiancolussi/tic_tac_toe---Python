# Create a Board
# Display the Board
# Play Game, Player 1 and Player 2
# Handle Turn
# Check Win
# Check Rows
# Check Columns
# Check Diagonals
# Check Tie
# Flip from X to O


print("Welcome to Tic Tac Hoe")

#player1 = input("Player 1: Do you want to be X or O?")

board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board(board):
    print(board[7] + '|'+board[8] + '|' + board[9])
    print(board[4] + '|'+board[5] + '|' + board[6])
    print(board[1] + '|'+board[2] + '|' + board[3])


display_board(board)


def player_input():
    marker = ""
    while marker != "X" or marker != "O":
        marker = input('Player 1: Please select X or O: ').upper()

        if marker == 'X':
            return('X', 'O')
        elif marker == 'O':
            return('O', 'X')
        else:
            print('Please select X or O')

# While marker is different to X or O continue to ask the user
