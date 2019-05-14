num = int(input('check if prime: '))
counter = 0
for x in range(1, num):
    # print(num/x, num%x)
    if num % x == 0:
        counter += 1

if counter <= 2:
    print('prime')
else:
    print('has ', counter, ' divisors')
