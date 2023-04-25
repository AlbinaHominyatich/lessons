import random

def print_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def get_player_move(board):
    while True:
        move = input("Введіть число від 1 до 9: ")
        try:
            move = int(move) - 1
            if move in range(9) and board[move] == " ":
                return move
            else:
                print("Недійсний хід, спробуйте ще раз.")
        except ValueError:
            print("Недійсний хід, спробуйте ще раз.")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    if " " not in board:
        return "tie"
    return None

def get_computer_move(board, current_player):
    # Перевірка на перемогу гравця X
    if current_player == "O":
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_winner(board) == "X":
                    board[i] = "O"
                    return

                board[i] = " "

    # Перевірка на перемогу гравця O
    if current_player == "O":
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_winner(board) == "O":
                    return

                board[i] = " "

    # Випадковий хід
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            return

def tic_tac_toe():
    board = [" " for i in range(9)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            move = get_player_move(board)
            board[move] = "X"
        else:
            get_computer_move(board, current_player)

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            if winner == "tie":
                print("Нічия!")
            else:
                print(winner, "виграв!")
            return

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
