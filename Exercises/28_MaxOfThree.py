def get_input():
    a = int(input('1st number: '))
    b = int(input('2nd number: '))
    c = int(input('3rd number: '))

    return [a,b,c]


def find_max(list):
    max = float('-inf')
    for x in list:
        if x > max:
            max = x
    return max

if __name__ == '__main__':
    nums = get_input()
    print('greatest number you entered is: ',find_max(nums))