import random
import sys
import os

#####
test_file = open("test.txt", 'wb') # writing

print(test_file.mode)
print(test_file.name)

test_file.write(bytes('write me\n','UTF-8'))

test_file.close()
######

######
test_file = open('test.txt', 'r+') # reading and writing
text = test_file.read()
print(text)

os.remove('test.txt')