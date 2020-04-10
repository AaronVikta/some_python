# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:40:05 2019

@author: Awam Victor
"""

#String manipulation

string = "awam victor"
#capitalize first words
print(string.title())

#capitalize everything
print(string.upper())
#make lower case
print(string.lower())

#string concatenation
first_name ="aryan"
last_name = "vikta"
full_name = first_name +" "+last_name

print("Hello, "+full_name.title()+"!")

#adding whitespaces and newlines
message = "Languages I program in:\nJS\nPHP"
print(message)

#trimming whitespaces
message =" awam Victor "
print(message.lstrip())
print(message.rstrip())
print(message.strip())