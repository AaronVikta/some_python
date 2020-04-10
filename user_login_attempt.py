# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:24:07 2020

@author: Awam Victor
"""

class User():
    def __init__(self,first_name,last_name):
        """Initialize a user"""
        self.first_name=first_name
        self.last_name=last_name
        self.attempts =0
        
    
    def describe_user(self):
        """describe the user"""
        full_name=self.first_name+' '+self.last_name
        print("\n Your fullname is "+full_name.title())
    
    def greet_user(self):
        """greet the user"""
        print("Hello "+self.first_name)
        
    def increment_login_attempts(self,attempt):
        """increment the login attempt"""
        self.attempts +=attempt
        print("you have made "+str(self.attempts)+' attempts')
    
    def reset_login_attempts(self):
        """reset the login attempts"""
        self.attempts=0
        print("you have made "+str(self.attempts)+' attempts')

my_user =User('awam','victor')
my_user.greet_user()
my_user.increment_login_attempts(2)
my_user.reset_login_attempts()

#inheritance
class DormantUser(User):
    """modeling a dormant user"""
    def __init__(self,first_name,last_name):
        """initialize the attributes of parent class"""
        super().__init__(first_name,last_name)

dormant_user=DormantUser('akor','jordan')
dormant_user.describe_user()