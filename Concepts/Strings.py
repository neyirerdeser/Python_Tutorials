import random
import sys
import os

long_string = "i'll catch you if you fall. - the floor"

print(long_string[0:4])
print(long_string[-5:]) # only in this case you can't fill the gap with 0
print(long_string[:-5])

print(long_string[:4]+' be there')

print('%c is my %s letter and my munber %d number is %.5f' %('x','fav',1,.14))
# %.5f means ill need 5 decimal points


print(long_string.capitalize())
print(long_string.find("floor")) # case sensetive, gives -1 if not there
print(long_string.isalpha()) # check if all capital
print(len(long_string))
print(long_string.replace('floor','ground'))
print(long_string.strip())

quote_list = long_string.split(" ")
print(quote_list)