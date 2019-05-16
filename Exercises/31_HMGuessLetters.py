clue = 'EVAPORATE'
guessed_letters = []

def guessed(c):
    return c in guessed_letters



def get_letter(mistake):
    letter = input('letter : ')
    if letter not in clue and letter not in guessed_letters:
        mistake += 1
    guessed_letters.append(letter)

    return mistake


def display_word():
    for x in clue:
        if guessed(x):
            print(x, end=' ')
        else:
            print('_', end=' ')
    print()


def win():
    for x in clue:
        if x not in guessed_letters:
            return False
    return True

mistake = 0
print('Welcome to Hangman. You can have at most 6 mistakes. Good luck!')
while not win():
    mistake = get_letter(mistake)
    if mistake >= 6:
        print('you made too many wrong guesses. better luck next time')
        exit()
    display_word()
print('congratulations!')