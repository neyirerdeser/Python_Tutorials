print('WELCOME TO ROCK PAPER SCISSORS')
quit = ''
while(quit != 'QUIT'):
    p1 = int(input('PLAYER 1, choose your weapon\n'
          'Type 1 for Rock\n'
          'Type 2 for Paper\n'
          'Type 3 for Scissors\n'
          'Choice: '))
    p2 = int(input('PLAYER 2, choose your weapon\n'
          'Type 1 for Rock\n'
          'Type 2 for Paper\n'
          'Type 3 for Scissors\n'
          'Choice: '))

    if p1==1:
        if p2==1:
            print('Its a tie!')
        elif p2==2:
            print('Paper beats rock\nPLAYER 2 wins')
        elif p2==3:
            print('Rock beats scissors\nPLAYER 1 wins')
    elif p1==2:
        if p2==1:
            print('Paper beats rock\nPLAYER 2 wins')
        elif p2==2:
            print('Its a tie!')
        elif p2==3:
            print('Scissors beats paper\nPLAYER 1 wins')
    else:
        if p2==1:
            print('Rock beats scissors\nPLAYER 2 wins')
        elif p2==2:
            print('Scissors beat paper\nPLAYER 1 wins')
        elif p2==3:
            print('Its a tie!')

    quit = input('to quit type QUIT, to play press \'enter\'')