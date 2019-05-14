import random
import sys
import os

# for loop

for x in range(0,10) :
    print(x,' ',end="") # so it doesnt print new lines

print()

grocery_list = ['juice','tomat','potat','banana']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x,' ',end="")
print()

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y],'  ',end="")
    print()

# while loop

random_number = random.randrange(0,100)

while(random_number != 15) :
    print(random_number)
    random_number = random.randrange(0, 100)

i = 0;
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i==9):
        break
    i+=1