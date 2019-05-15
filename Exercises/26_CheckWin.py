# some example boards
game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


def check_row(board):
    n = len(board)
    win = True
    for i in range(0,n):
        for j in range(0,n):
            if board[i][0] != board[i][j]
                win = False
    return win


def check_col(board):
    n = len(board)
    win = True
    for i in range(0,n):
        for j in range(0,n):
            if board[0][i] != board[j][i]
                win = False
    return win


def check_dia_neg(board):
    n = len(board)
    win = True
    for i in range(0,n):
        if board[0][0] != board[i][i]
            win = False
    return win


def check_dia_pos(board):
    n = len(board)
    win = True
    for i in range(0,n):
        for j in range(n,0):
            if board[0,n-1] != board[i][j]
                win = False
    return win


def check_win(board):
    return check_row(board) or check_col(board) or check_dia_neg(board) or check_dia_pos(board)


# later check WHO wins
