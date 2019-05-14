import random
import sys
import os

# if else elif == != > >= < <=

age = 21


if age >= 21 :
    print('you old')
elif age >= 16 :
    print("You are old-ish")
else:
    print('youre baby')


if ((age >= 1) and (age <= 18)) :
    print('birthday')
elif (age==21) or (age >=65) :
    print('also birthday')
elif not(age==30) :
    print('you dont get a birthday')
else :
    print('sure get it')