import math

# -----------------------------
# GAME BOARD
# -----------------------------

board = [" " for _ in range(9)]

human = "X"
ai = "O"


# -----------------------------
# DISPLAY BOARD
# -----------------------------

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# -----------------------------
# CHECK WINNER
# -----------------------------

def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# -----------------------------
# MINIMAX ALGORITHM
# -----------------------------

def minimax(is_maximizing):
    result = check_winner()

    # Terminal states
    if result == ai:
        return 1

    if result == human:
        return -1

    if result == "Draw":
        return 0

    # AI's turn
    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = ai

                score = minimax(False)

                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    # Human's turn
    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = human

                score = minimax(True)

                board[i] = " "
                best_score = min(best_score, score)

        return best_score


# -----------------------------
# AI MOVE
# -----------------------------

def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = ai

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = ai


# -----------------------------
# HUMAN MOVE
# -----------------------------

def human_move():
    while True:
        try:
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("❌ Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("❌ That position is already occupied.")
                continue

            board[move] = human
            break

        except ValueError:
            print("❌ Please enter a valid number.")


# -----------------------------
# MAIN GAME
# -----------------------------

def play_game():

    print("\n================================")
    print("       TIC-TAC-TOE AI")
    print("================================")
    print("You are X")
    print("AI is O")
    print("AI uses Minimax Algorithm")
    print("================================")

    print("\nPositions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        # Human turn
        human_move()
        print_board()

        result = check_winner()

        if result:
            break

        # AI turn
        print("🤖 AI is thinking...")
        ai_move()
        print_board()

        result = check_winner()

        if result:
            break

    # Result
    if result == human:
        print("🎉 Congratulations! You Win!")

    elif result == ai:
        print("🤖 AI Wins! Better luck next time!")

    else:
        print("🤝 It's a Draw!")


# -----------------------------
# PROGRAM START
# -----------------------------

if __name__ == "__main__":
    play_game()