# some example boards
winner_1 = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[1, 1, 1],
                    [2, 2, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


def check_row(board, player):
    n = len(board)
    win = True
    check = False
    for i in range(0,n):
        if board[i][0] != player:
            continue
        else:
            check = True
        for j in range(0,n):
            if board[i][0] != board[i][j]:
                win = False
    return win and check


def check_col(board, player):
    n = len(board)
    win = True
    check = False
    for i in range(0,n):
        if board[0][i] != player:
            continue
        else:
            check = True
        for j in range(0,n):
            if board[0][i] != board[j][i]:
                win = False
            print('j loop end: n= %d, win=%s, check=%s' %(n, win, check))
    return win and check


def check_dia_neg(board, player):
    if board[0][0] != player:
        return False
    n = len(board)
    win = True
    for i in range(0,n):
        if board[0][0] != board[i][i]:
            win = False
    return win


def check_dia_pos(board, player):
    n = len(board)
    if board[0][n-1] != player:
        return False
    win = True
    for i in range(0,n):
        for j in range(n,0):
            if board[0][n-1] != board[i][j]:
                win = False
    return win


def check_win(board, player):
    return check_row(board, player) or check_col(board, player) or check_dia_neg(board, player) or check_dia_pos(board, player)


if __name__ == "__main__":
    board = [winner_1, winner_is_2, winner_is_1, winner_is_also_1, no_winner, also_no_winner]
    print(check_win(board[1], 2))

    ### ERRORS
    # board[1], 2 --> false
