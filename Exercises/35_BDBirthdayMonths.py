import json
from collections import Counter

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)


num_to_str = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'jun',
    7: 'jul',
    8: 'aug',
    9: 'sep',
    10: 'oct',
    11: 'nov',
    12: 'dec'
}
months = []

for x in birthdays:
    month = int(birthdays[x][0:2])
    months.append(num_to_str[month])

print(Counter(months))