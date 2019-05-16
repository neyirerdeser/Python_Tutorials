import json

def make_file():
    birthdays = {
            'Albert Einstein': '03/14/1879',
            'Benjamin Franklin': '01/17/1706',
            'Ada Lovelace': '12/10/1815',
            'Donald Trump': '06/14/1946',
            'Rowan Atkinson': '01/6/1955'
    }

    with open('birthdays.json','w') as f:
        json.dump(birthdays,f)



def get_date(filename):
    with open(filename, 'r') as f:
        birthdays = json.load(f)
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays.keys():
        print(name)
    name = input('Who\'s birthday do you want to look up?\n')
    print(name, '\'s birthday is', birthdays[name])

if __name__ == '__main__':
    make_file()
    get_date('birthdays.json')