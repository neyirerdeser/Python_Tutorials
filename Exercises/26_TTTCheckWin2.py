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


def row(board, i):  # i-th row
    row = []
    for x in range(0, len(board)):
        row.append(board[i][x])
    return row


def col(board, i):  # i-th column
    col = []
    for x in range(0, len(board)):
        col.append(board[x][i])
    return col


def dia(board, i):  # 1 for negative sloped diagonal, 2 for positive
    dia = []
    for x in range(0, len(board)):
        if i == 1:
            dia.append(board[x][x])
        elif i == 2:
            dia.append(board[x][len(board)-1-x])
    return dia


def match(line):
    for i in range(0, len(line)-1):
        if line[i] != line[i+1]:
            return False
    return True


def check_winner(board):
    winner = 0
    line = []
    for i in range(0, len(board)):
        if match(row(board, i)):
            line = row(board, i)
            break
        elif match(col(board, i)):
            line = col(board, i)
            break
        elif match(dia(board, 1)):
            line = dia(board, 1)
            break
        elif match(dia(board, 2)):
            line = dia(board, 2)
            break

    if line:
        if line[0] == 1:
            winner = 1
        elif line[0] == 2:
            winner = 2

    return winner


if __name__ == '__main__':
    boards = [winner_1, winner_is_2, winner_is_1, winner_is_also_1, no_winner, also_no_winner]
    print(check_winner(boards[5]))