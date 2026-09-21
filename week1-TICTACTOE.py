board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
player = "X"
while True:
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    position = int(input("Player " + player + ", enter position (1-9): ")) - 1
    if board[position] == "X" or board[position] == "O":
        print("Position already occupied!")
        continue
    board[position] = player
    winning = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    win = False
    for combination in winning:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            win = True
            break
    if win:
        print("\n")
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print("Player", player, "wins!")
        break
    if all(position == "X" or position == "O" for position in board):
        print("It's a draw!")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"
