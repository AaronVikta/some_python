# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:32:52 2019

@author: Awam Victor
"""
#if statements
girls =['vicky','divine', 'jenny',
        'crystal']
for girl in girls:
    if girl =='vicky':
        print("Vicky was my best XX "
              "friend")
    else:
        print(girl.title())

#conditional Tests
#== returns true if the the condition is 
#true

#ignoring case when chacking for equality
#convert the two strings you want to
#compare to lowercase using .lower() method

#chacking for inequality use !=
#checking multiple con 
age=19
age <21
if (age>19 and age <21 ):
    print(age)
if (age>19 or age <21 ):
    print(age)

#checking if a value is in a list use *in*
requested_toppings =['mushrooms','onions', 
                     'pineapple']
if ('mushrooms' in requested_toppings):
    print(True)
else:
    print(False)
    
#checking if a value is not in a list
banned_users = ['iruoma','ihuoma','ifeoma']
user='marie'
if user not in banned_users:
    print(user+" is not banned")

#the if-elif-else chain
age =12
if age<4:
    print("Your admission cost is $0")
elif age<18:
    print("Your admission cost is $5")
else: 
    print("Your admission cost is $10")

#using if statements with lists
#checking for special items
toppings = ['onions','pepper','cheese']
for topping in toppings:
    print("Adding "+topping )
print("Finished making your pizza")

#case where there is no more pepper
for topping in toppings:
    if topping =='pepper':
        print("No more Pepper")
    else:
        print("Adding "+topping )
print("Finished making your pizza")

#checking that a list is not empty 
seas = []
if seas:
    for sea in seas:
        print(sea)
else:
    print('Have you ever seen a dry sea')

#using multiple lists
ingredients = ['mushrooms', 'olives', 
               'peppers','pineapple',
               'cheese']
requested_ingredients =['mushrooms',
                        'fries','cheese']
for spice in requested_ingredients:
    if spice in ingredients:
        print("Adding "+spice)
    else:
        print(spice+" is not in stock")
print("Your pizza is ready")
    
