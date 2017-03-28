from __future__ import print_function

import random
import sys
import os

print("Hello World")
name = "Annette"
print(name)

# Numbers, Strings, Lists, Tuples, Dictionaries
# + - * / % ** //
# PEMDAS, ORDER OF OPERATIONS

multi_line_quote  = ''' just like everyone else\"'''
quote = "\"Always remember you are unique"
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print ('\n' * 5)
# Need to import future, print_function module 2.x
print ("I don't like ", end="")
print("newlines")

# LISTS

grocery_list = ['Juice', 'Tomato', 'Potatos', 'Bananas']
print("First Item:", grocery_list[0])
print('Items:', grocery_list[1:3])

other_events = ['Wash car', 'PickUp kids']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))
grocery_list.append("Onions")
print("Appended",to_do_list)

grocery_list.insert(1, "Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

# TUPLES ARE IMMUTABLE, AND LISTS USE [] AND TUPLES USE ()
pi_tuple =(3,1,4,1,5,9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print("NEW print")
print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))

print(new_tuple)
print(new_list)

# DICTIONARIES / CANT JOIN DICTIONARIES

super_villains = {'Fiddler':'Isaac Bowin', 'Captain Cold': 'Leonard Snart', 'Weather Wizard':'Mark Mardon', 'Mirror Master': 'Sam Scudder', 'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captain Cold'])
del super_villains['Fiddler']
print(super_villains)
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))

print(super_villains.get("Pied Piper"))
print(super_villains.keys())
print(super_villains.values())

#CONDITIONS IF ELSE ELIF == != > >= <=

age = 31
if age > 16:
    print('You are old enough to drive, IF')
else:
    print('You are not old enough to drive, FIRST ELSE')
if age >= 21:
    print('You are old enough, SECOND IF')
#ELIF if(not a) and b
elif age >= 16:
    print('You are old enough to drive a car, ELIF')
#ELSE if not a and if not b
else:
    print("You are not old enough to drive, LOGICALS NEXT")

## LOGICAL OPERATORS AND OR NOT, ONCE CONDITION IS MET, WILL NOT GO THROUGH REST OF FUNCTION

if ((age >= 1) and (age <= 18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get tequila with worm")
#ELIF NOT (THE OPPOSITE OF THE RIGHT STATEMENT, NOT == TO AGE)
elif not(age == 30):
    print("You don't get a birthday, elifNOT")
else:
    print("You are getting a big party!")

# FOR LOOP

for x in range(0,10):
    print(x, ' ', end="")
print('\n')

errands_list = ['Hello to bella', 'Talk to boo', 'Study for Amazon']

for x in errands_list:
    print(x)
