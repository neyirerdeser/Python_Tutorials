number = int(input('your number: '))

print('your number is divisible by:',end=" ")
for x in range(1,number):
    if(number%x==0):
        print(x, end=" ")
print(number)