import random


def generate_number():
    return random.randint(1000,9999)


def get_digits(num):
    return [(num - num % 1000)/1000, (num % 1000 - num % 100)/100, (num % 100 - num % 10)/10, num % 10]


def check_cows(codedigit, guessdigit):
    cow = 0
    for i in range(0,4):
        if codedigit[i] == guessdigit[i]:
            cow += 1
    return cow


def check_bulls(codedigit, guessdigit):
    bull = 0
    for i in range(0,4):
        if codedigit[i] != guessdigit[i] and codedigit[i] in guessdigit:
            bull += 1
    return bull


if __name__ == "__main__":
    code = generate_number()
    cows = 0
    count = 1
    while cows < 4:
        print(count,'th guess:',end=' ')
        guess = int(input())
        cows = check_cows(get_digits(code), get_digits(guess))
        bulls = check_bulls(get_digits(code), get_digits(guess))
        if cows == 4:
            print('you got it in ', count, ' tries!')
        else:
            print(cows, ' cows, ', bulls, ' bulls')
            count += 1
