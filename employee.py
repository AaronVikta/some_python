# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:22:28 2020

@author: Awam Victor
"""
import string 
import random

class Employee():
    
    
    def __init__(self, first_name, last_name, email, password):
        """Initialize an Employee"""
        self.first_name = first_name
        self.last_name= last_name
        self.password = password
        self.email = email
        
    def register():
        """Register an employee"""
        first_name= input("what is your first name ")
        last_name = input("what is your last name ")
        email=input("What is your email ")
        length= 7
        full_name = first_name+last_name
        
        full_name= full_name.strip()
        generated_pass = ''.join(random.choice(full_name) for i in range(length))
        
        print(generated_pass)
        
        response = input("Are you Okay with the password: Y/N")
        if response=="Y":
            password =generated_pass
            print("Thank you for registering")
            Employee.store(first_name,last_name,password,email)
            Employee.register()
        elif response=="N":
            user_password= input("Choose your Password")
            if len(user_password)<7 :
                print("Error: Password must be greater than 7 characters")
                Employee.register()
            else:
                password= user_password
                print("Thank you for registering")
                Employee.store(first_name,last_name,password,email)
                Employee.register()
    
    def login():
        """Initialize login"""
        email=input("what is your email")
        password=input("what is your password")
        
        
    def store( first_name, last_name, password, email):
        """store the employee details"""
        filename= "employees.txt"
        
        with open(filename, 'a') as data:
            data.write( "First Name: "+first_name)
            data.write("Last Name: "+last_name)
            data.write( "Password: "+password)
            data.write( "Email: "+email)
            
    def fetch_employees():
        """Fetch employees"""
        filename ="employees.txt"
        try:
            with open(filename) as data:
                contents =data.read()
                print(contents)
        except FileNotFoundError:
            error ="Sorry" +filename+ "does not exist"
            print(error)
            
         
            
        
        
        
        
        
        
register = Employee.register()