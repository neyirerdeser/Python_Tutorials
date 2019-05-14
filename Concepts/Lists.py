import random
import sys
import os

grocery_list = ['juice','tomato','potatoes','bananas']
print("first item", grocery_list[0])

print(grocery_list[1:3]) #3 is not included
other_events = ['Wash car','cash check']

to_do = [other_events, grocery_list] # two lists in one list

print(to_do)
print(to_do[1][1])

grocery_list.append('onions') # adds at the end of the list
grocery_list.insert(1,"pickle")
print(to_do)
grocery_list.sort() # alphabetically
print(to_do)
grocery_list.reverse()
print(to_do)

to_do2 = other_events + grocery_list # add lists together
print(len(to_do2))
print(max(to_do2))
print(len(to_do))
print(max(to_do))
