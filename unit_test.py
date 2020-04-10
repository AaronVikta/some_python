# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:24:07 2020

@author: Awam Victor
"""

import unittest
from testing_in_python import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'testing_in_python.py'"""
    
    def test_first_last_name(self):
        """Does names like 'aaron victor' work?"""
        formatted_name= get_formatted_name('aaron','victor')
        self.assertEqual(formatted_name,'Aaron Victor')
        
    def test_first_last_middle_name(self):
        """Does names like 'Awam vikto aryan' work"""
        formatted_name = get_formatted_name(
                'awam','vikto','aryan')
        self.assertEqual(formatted_name,"Awam Aryan Vikto")

unittest.main()