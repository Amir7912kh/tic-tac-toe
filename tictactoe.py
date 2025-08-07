"""
This module contains the logic for a Tic-Tac-Toe game with an AI opponent.
"""

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_move(player):
    """Gets the player's move and updates the board."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter col (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(player):
    """Checks if the specified player has won."""
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    """Checks if the game is a draw."""
    return all(cell != ' ' for row in board for cell in row)

def minimax(is_maximizing):
    """Minimax algorithm to find the best move."""
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    """Finds the best move for the AI and updates the board."""
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

def main():
    """
    The main function to run the Tic-Tac-Toe game.
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O.")

    while True:
        print_board()
        if check_win('X'):
            print("You win!")
            break
        if check_win('O'):
            print("AI wins!")
            break
        if check_draw():
            print("It's a draw!")
            break

        player_move('X')
        if check_win('X') or check_draw():
            continue

        print("\nAI is thinking...")
        ai_move()


if __name__ == "__main__":
    main()
