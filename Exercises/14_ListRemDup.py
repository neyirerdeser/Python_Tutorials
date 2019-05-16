import random


def random_list():
    return list(random.sample(range(50), random.randint(0,25)))


def rem_dup(l):
    a = list()  # better than using [], tells the variable
    for x in l:
        if x not in a:
            a.append(x)
    return a


# a_list = random_list()
a_list = [3, 6, 8, 4, 24, 5, 7, 54, 5, 3, 5, 7, 9]
clean_list = rem_dup(a_list)

print(a_list)
print(clean_list)

'''
sets have the same logic as sets in maths
if you convert a list to a set, it will lose duplicates, indices (and any ties -- there's no next element, just elements)

in this case:

a = random_list()
a = set(a)

will  cast the list into set hence remove duplicates

'''

