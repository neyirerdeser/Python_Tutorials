import random

goal = random.randint(1,9)
print(goal)
game = 'yes'
counter = 0
while(game=='yes'):
    counter+=1
    guess = input('guess what im thinking from 1 to 9\n'
                      'type exit anytime to quit\n'
                      'Guess: ')
    if guess=='exit': break
    else:
        guess = int(guess)
    if guess<goal:
        print('you need to go higer')
        continue
    elif guess>goal:
        print('you need to go lower')
        continue
    else:
        print('YOU GOT IT\nand it took you %d tries',counter)
        game = input('Do you wanna keep playing?\n'
                     'type yes if you do, anything else if not')