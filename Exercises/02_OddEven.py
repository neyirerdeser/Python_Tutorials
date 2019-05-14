number = int(input('Please enter a number...: '))
if(number%4==0):
    print('your number is divisible by 4')
elif(number%2==0):
    print('your number is even')
else:
    print('your number is odd')


num = int(input('number1: '))
check = int(input('number2: '))

if(check%num==0):
    print('you first number divides the second one evenly')
