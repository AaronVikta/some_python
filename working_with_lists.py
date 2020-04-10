# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:50:42 2019

@author: Awam Victor
"""

#working with lists
#looping through an entire list

magicians =['alice','carolina','david',
            'kaniz']
for magician in magicians:
    print(magician.title()+ ","
          "what a trick")

#making numerical lists
    for value in range(1,5):
        print(value)
#using range to make a list of numbers
numbers = list(range(1,6))
print(numbers)

#using range to create even_numbers
even_numbers = list(range(0,20,2))
print(even_numbers)

#creating squares with range
squares =[]
for value in range(1,11):
    square =value**2
    squares.append(square)
print(squares)
anotherSquare= []
for item in range(1,11):
    anotherSquare.append(item**2)
print(anotherSquare)

#imple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
LSquares = [values**2 for values in
            range(1,11)]
print(LSquares)

#assignment for cubes
cubes = [cube**3 for cube in range(1,10)]
print(cubes)

#working with part of a list 
#slicing a list 
players =['charles', 'martina','michael',
          'florence','eli']
print(players[0:3])
print(players[-1:])
print(players[-2:])
print(players[-3:])

#looping through a slice
print("here are the first three players")
for player in players[:3]:
    print(player.title())
    
#copying a list
my_foods= ['pizza','cake','nuts','rice']
friend_foods= my_foods[:]
print(friend_foods)

#Tuples: a permanent form of list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#looping through a tuple
for dimension in dimensions :
    print("Dimension is "+str(dimension))
    
