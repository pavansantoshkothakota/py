# Tic Tac Toe

# Display the game board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Check if any player has won
def check_win(board, player):
    # Check rows
    if (board[7] == board[8] == board[9] == player or
        board[4] == board[5] == board[6] == player or
        board[1] == board[2] == board[3] == player):
        return True
    # Check columns
    if (board[7] == board[4] == board[1] == player or
        board[8] == board[5] == board[2] == player or
        board[9] == board[6] == board[3] == player):
        return True
    # Check diagonals
    if (board[7] == board[5] == board[3] == player or
        board[9] == board[5] == board[1] == player):
        return True
    return False

# Check if the board is full
def check_draw(board):
    return all(cell != ' ' for cell in board)

# Main game function
def play_game():
    # Initialize the board
    board = [' '] * 10

    # Initialize players
    players = ['X', 'O']
    current_player = players[0]

    # Game loop
    while True:
        # Display the board
        display_board(board)

        # Get the player's move
        while True:
            move = input("Player " + current_player + ", enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)] == ' ':
                break
            print("Invalid move. Please try again.")

        # Update the board
        board[int(move)] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            display_board(board)
            print("Player " + current_player + " wins!")
            break

        # Check if it's a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = players[(players.index(current_player) + 1) % 2]

# Start the game
play_game()