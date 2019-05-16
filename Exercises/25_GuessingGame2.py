# need to use capital letters


def guess_number(low, high):
    number = int((low+high)/2)
    print('my guess is : ', number)
    return number


def get_feedback():
    ans = input('did i get it? (Y/N) : ')
    if ans == 'N':
        ans = input('Is your number higher or lower than my guess?\n(H/L) : ')
    return ans


if __name__ == "__main__":
    low = 0
    high = 100
    print('think of a number between 0 and 100 and ill try to guess, press enter when ready')
    input()
    guessed = False
    count = 0
    while not guessed:
        count += 1
        number = guess_number(low, high)

        fb = get_feedback()
        if fb == 'Y':
            print('YAY guessed in ',count,'th try')
            break
        if fb == 'H':
            low = number
        else:
            high = number
