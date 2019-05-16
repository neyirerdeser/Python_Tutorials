def draw_board(n):
    for line in range(1,2*n):
        if line%2 == 1:
            draw_ver(n)
        elif line%2 == 0:
            draw_hor(n)


def draw_ver(n):
    for i in range(0,n-1):
        print(' |',end='')
    print(' ')


def draw_hor(n):
    for line in range(1,2*n):
        if line%2 == 1:
            print('-',end='')
        elif line%2 == 0:
            print('+',end='')
    print()

draw_board(3)