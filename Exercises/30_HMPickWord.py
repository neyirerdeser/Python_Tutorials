import random

text = ''
with open('sowpods.txt','r') as f:
    line = f.readline()
    while line:
        text += line
        line = f.readline()

words = text.split()
n = len(words)
randword = words[random.randint(0,n-1)]
print(randword)
