file = open('names.txt', 'r')
text = file.read()

'''
with open('file_to_read.txt', 'r') as open_file:
    all_text = open_file.read()
'''


namelist = text.split()

names = {x: 0 for x in set(namelist)}

for i in range(0, len(namelist)):
    for name in names:
        if namelist[i] == name:
            names[name] += 1

print(names)
