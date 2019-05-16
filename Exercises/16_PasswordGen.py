import random


lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbr = '1234567890'
symbl = '!@#$%^&*()'

strength = int(input('0. weak\n'
                     '1. okay\n'
                     '2. medium\n'
                     '3. strong\n'
                     'chose strength level: '))
length = int(input('enter length: '))

def get_password():
    if strength not in (0, 3) or length < 1:
        raise Exception('invalid argument')

    if strength == 0:
        pool = lower

    if strength == 1:
        pool = lower+upper

    if strength == 2:
        pool = lower+upper+numbr

    if strength == 3:
        pool = lower+upper+numbr+symbl


    password = random.sample(pool, length)
    password = "".join(password)
    return password


print(get_password())
