a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = []

limit = max(max(a),max(b))

for x in range(0,limit):
    if(x in a and x in b):
        overlap.append(x)


'''
for x in a:
    if x in b:
        overlap.append(x)
        
#then you remove duplicates
'''

# in one line
# print (set(a) & set(b))
print(overlap)