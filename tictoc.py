def print_board(board):
    
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Player " + player + ", enter row number (1-3): "))
        col = int(input("Player " + player + ", enter column number (1-3): "))
        if board[row-1][col-1] != " ":
            print("That position is already taken. Try again.")
            continue
        board[row-1][col-1] = player
        if check_win(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

play_game()
