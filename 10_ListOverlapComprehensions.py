import random
a = random.sample(range(1,30), random.randint(5,15))
b = random.sample(range(1,30), random.randint(5,15))

c = [x for x in set(a) if x in b] # set here keep the duplicates out
print(a)
print(b)
print(c)
# print (set(a) & set(b))
# c = [x for x in a if x%2==0]