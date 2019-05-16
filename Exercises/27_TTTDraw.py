def create_board(n):
    '''
    game = []
    row = []
    for i in range(0,n):
        for j in range(0,n):
            row.append(0)
        game.append(row)
    return game
    '''
    return [[0 for i in range(n)] for j in range(n)]


def get_move(board, player):
    print('Player %d please enter your move in format (row,column): ' % player)
    valid = False
    while not valid:
        coord = input()
        move = coord.split(',')
        move[0] = int(move[0])-1
        move[1] = int(move[1])-1
        if board[move[0]][move[1]] != 0:
            print('the spot it occupied, please enter a valid move (row,column): ')
        else:
            valid = True
            if player == 1: board[move[0]][move[1]] = 'X'
            if player == 2: board[move[0]][move[1]] = 'O'


def full(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        print(board[i])

if __name__ == '__main__':
    size = int(input('size pls (3 is suggested) : '))
    game = create_board(size)
    count = 1
    while not full(game):
        print_board(game)
        count += 1
        get_move(game,count%2+1)
    print('no more valid mores. its a tie')