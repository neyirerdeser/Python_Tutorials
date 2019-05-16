# a = int(input('up to how many-th fibonacci number do you want to see: '))


def fibonacci(n):
    if n <= 0:
        return

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib(n, loc=1, res1=1, res2=1):

    if n in (1, 2):
        return 1

    if loc == n:
        return res1

    return fib(n, loc+1, res2, res1+res2)


print(fib(40))
