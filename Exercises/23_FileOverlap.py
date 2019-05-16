def file_to_intlist(filename):
    list = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list.append(int(line))
            line = f.readline()
    return list


prime = file_to_intlist('primenumbers.txt')
happy = file_to_intlist('happynumbers.txt')

overlap = set()

for x in prime:
    if x in happy:
        overlap.add(x)

print(prime)
print(happy)
print(overlap)
