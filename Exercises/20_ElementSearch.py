import random


def random_list():
    return list(random.sample(range(50), random.randint(0,25)))


def search(a, start, end, k):
    if start >= end:
        return -1
    mid = int((end+start)/2)
    if k == a[mid]:
        return mid

    if k < a[mid]:
        print(start, mid, k)
        return search(a, start, mid, k)
    if k > a[mid]:
        print(mid, end, k)
        return search(a, mid, end, k)


a = [1,2,3,4,5,6]
a.sort()
key = 7

print(0, len(a)-1, key)
val = search(a, 0, len(a), key)
print(val)
