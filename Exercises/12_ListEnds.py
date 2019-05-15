import random as rand # you can put anything to write it as

a = [5, 10, 15, 20, 25]

def random_list():
    return list(rand.sample(range(50), rand.randint(0,25)))  #randint is already that way

def list_ends(a):  # take the array just with a not a[],
    list = [a[0], a[-1]]
    return list

a = random_list()
l = list_ends(a)
print(a)
print(l)