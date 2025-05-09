def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while not check_winner(board) and moves < 9:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if 0 <= row <=2 and 0 <= col <=2:
                if board[row][col] == " ":
                    board[row][col] = player
                    moves += 1
                    if check_winner(board):
                        break
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid coordinates! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers.")

    print_board(board)
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
