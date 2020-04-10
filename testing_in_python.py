# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 01:38:27 2020

@author: Awam Victor
"""

def get_formatted_name(first, last,middle=''):
    """generate a neatly formatted full name"""
    if middle:
        full_name = first+' '+middle+' '+last
    else:
        full_name = first+' '+last
    
    return full_name.title()

my_fullname = get_formatted_name('Awam','Victor')
print(my_fullname)

