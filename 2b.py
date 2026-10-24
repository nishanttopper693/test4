board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def winner():
    lines = [(0,1,2), (3,4,5), (6,7,8),
             (0,3,6), (1,4,7), (2,5,8),
             (0,4,8), (2,4,6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def minimax(maximize, alpha, beta):
    w = winner()
    if w == "O":
        return 1
    if w == "X":
        return -1
    if " " not in board:
        return 0

    if maximize:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False, alpha, beta))
                board[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True, alpha, beta))
                board[i] = " "
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def computer_move():
    best, move = -float("inf"), -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -float("inf"), float("inf"))
            board[i] = " "
            if score > best:
                best, move = score, i
    board[move] = "O"

print("Tic-Tac-Toe: You are X, Computer is O")
show()

while not winner() and " " in board:
    try:
        pos = int(input("Enter position (1-9): ")) - 1
        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid position!")
            continue
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    board[pos] = "X"
    if winner() or " " not in board:
        break

    computer_move()
    print("\nComputer's move:")
    show()

show()
if winner():
    print(winner(), "wins!")
else:
    print("It's a draw!")